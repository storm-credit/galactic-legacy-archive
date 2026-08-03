#!/usr/bin/env python3
"""Validate structured design datasets for the Galactic Legacy archive.

This script intentionally uses only the Python standard library so it can run in
GitHub Actions and local authoring environments without dependency setup.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

CENSUS_FILES = [
    DATA_DIR / "galaxy-612-system-census-core-v1.csv",
    DATA_DIR / "galaxy-612-system-census-inner-v1.csv",
    DATA_DIR / "galaxy-612-system-census-middle-a-v1.csv",
    DATA_DIR / "galaxy-612-system-census-middle-b-v1.csv",
    DATA_DIR / "galaxy-612-system-census-middle-c-v1.csv",
    DATA_DIR / "galaxy-612-system-census-frontier-a-v1.csv",
    DATA_DIR / "galaxy-612-system-census-frontier-b-v1.csv",
    DATA_DIR / "galaxy-612-system-census-frontier-c-v1.csv",
]

EXPECTED_COLUMNS = [
    "system_id",
    "system_name",
    "macro_region",
    "cluster",
    "primary_node",
    "registered_population_m",
    "main_specialization",
    "secondary_specialization",
    "governance_at_R0",
    "route_profile",
    "GA10_transition_seed",
    "notes",
]

EXPECTED_REGION_COUNTS = {
    "CORE": 24,
    "INNER": 96,
    "MIDDLE": 180,
    "FRONTIER": 312,
}

EXPECTED_REGION_POPULATION_M = {
    "CORE": Decimal("24000.000"),
    "INNER": Decimal("25000.000"),
    "MIDDLE": Decimal("18000.000"),
    "FRONTIER": Decimal("9000.000"),
}

EXPECTED_NODE_COUNTS = {
    "L0": 9,
    "L1": 46,
    "L2": 192,
    "L3": 365,
}

EXPECTED_CLUSTER_COUNTS = {
    "CORE": 4,
    "INNER": 8,
    "MIDDLE": 15,
    "FRONTIER": 21,
}

ALLOWED_TRANSITIONS = {
    "T0 synchronized",
    "T1 delegated",
    "T2 joint transition",
    "T3 local plural",
    "T4 asynchronous",
    "T5 contested",
    "T6 re-centralized",
}

PROTECTED_SYSTEMS = {
    "Aurel Prime": ("CORE", "L0", Decimal("4200.0")),
    "Lumen": ("INNER", "L1", Decimal("1100.0")),
    "Kael": ("INNER", "L2", Decimal("620.0")),
    "Brann": ("INNER", "L2", Decimal("850.0")),
    "Neris": ("INNER", "L2", Decimal("430.0")),
    "Marn": ("MIDDLE", "L3", Decimal("18.0")),
    "Silex": ("MIDDLE", "L3", Decimal("6.5")),
    "Ardis": ("MIDDLE", "L3", Decimal("1.42")),
    "K-13": ("MIDDLE", "L3", Decimal("0.62")),
}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def read_rows(errors: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in CENSUS_FILES:
        if not path.exists():
            fail(f"missing census file: {path.relative_to(ROOT)}", errors)
            continue
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != EXPECTED_COLUMNS:
                fail(
                    f"column mismatch in {path.name}: {reader.fieldnames!r}",
                    errors,
                )
            for line_no, row in enumerate(reader, start=2):
                row["__file"] = path.name
                row["__line"] = str(line_no)
                rows.append(row)
    return rows


def validate_census(rows: list[dict[str, str]], errors: list[str]) -> None:
    if len(rows) != 612:
        fail(f"expected 612 census rows, found {len(rows)}", errors)

    id_counts = Counter(row.get("system_id", "").strip() for row in rows)
    name_counts = Counter(row.get("system_name", "").strip() for row in rows)

    for system_id, count in sorted(id_counts.items()):
        if not system_id:
            fail("blank system_id", errors)
        elif count != 1:
            fail(f"duplicate system_id {system_id!r}: {count}", errors)

    for name, count in sorted(name_counts.items()):
        if not name:
            fail("blank system_name", errors)
        elif count != 1:
            fail(f"duplicate system_name {name!r}: {count}", errors)

    region_counts: Counter[str] = Counter()
    node_counts: Counter[str] = Counter()
    region_population: defaultdict[str, Decimal] = defaultdict(Decimal)
    clusters: defaultdict[str, set[str]] = defaultdict(set)
    by_name: dict[str, dict[str, str]] = {}

    for row in rows:
        location = f"{row.get('__file')}:{row.get('__line')}"
        region = row.get("macro_region", "").strip()
        node = row.get("primary_node", "").strip()
        transition = row.get("GA10_transition_seed", "").strip()
        name = row.get("system_name", "").strip()
        cluster = row.get("cluster", "").strip()
        population_text = row.get("registered_population_m", "").strip()

        region_counts[region] += 1
        node_counts[node] += 1
        clusters[region].add(cluster)
        by_name[name] = row

        if region not in EXPECTED_REGION_COUNTS:
            fail(f"{location}: invalid macro_region {region!r}", errors)
        if node not in EXPECTED_NODE_COUNTS:
            fail(f"{location}: invalid primary_node {node!r}", errors)
        if transition not in ALLOWED_TRANSITIONS:
            fail(f"{location}: invalid transition seed {transition!r}", errors)
        if not cluster:
            fail(f"{location}: blank cluster", errors)
        if row.get("main_specialization", "").strip() == row.get(
            "secondary_specialization", ""
        ).strip():
            fail(f"{location}: duplicated specialization", errors)

        try:
            population = Decimal(population_text)
        except InvalidOperation:
            fail(f"{location}: invalid population {population_text!r}", errors)
            continue

        if population <= 0:
            fail(f"{location}: population must be positive", errors)
        region_population[region] += population

    if dict(region_counts) != EXPECTED_REGION_COUNTS:
        fail(
            f"region counts mismatch: expected {EXPECTED_REGION_COUNTS}, "
            f"found {dict(region_counts)}",
            errors,
        )

    if dict(node_counts) != EXPECTED_NODE_COUNTS:
        fail(
            f"node counts mismatch: expected {EXPECTED_NODE_COUNTS}, "
            f"found {dict(node_counts)}",
            errors,
        )

    for region, expected in EXPECTED_REGION_POPULATION_M.items():
        actual = region_population[region]
        if abs(actual - expected) > Decimal("0.001"):
            fail(
                f"{region} population mismatch: expected {expected}, found {actual}",
                errors,
            )

    total_population = sum(region_population.values(), Decimal("0"))
    if abs(total_population - Decimal("76000.000")) > Decimal("0.001"):
        fail(
            f"total population mismatch: expected 76000.000m, found {total_population}",
            errors,
        )

    for region, expected in EXPECTED_CLUSTER_COUNTS.items():
        actual = len(clusters[region])
        if actual != expected:
            fail(
                f"{region} cluster count mismatch: expected {expected}, found {actual}",
                errors,
            )

    for name, (region, node, population) in PROTECTED_SYSTEMS.items():
        row = by_name.get(name)
        if row is None:
            fail(f"protected system missing: {name}", errors)
            continue
        if row["macro_region"] != region:
            fail(
                f"protected system {name}: expected region {region}, "
                f"found {row['macro_region']}",
                errors,
            )
        if row["primary_node"] != node:
            fail(
                f"protected system {name}: expected node {node}, "
                f"found {row['primary_node']}",
                errors,
            )
        actual_population = Decimal(row["registered_population_m"])
        if actual_population != population:
            fail(
                f"protected system {name}: expected population {population}m, "
                f"found {actual_population}m",
                errors,
            )


def main() -> int:
    errors: list[str] = []
    rows = read_rows(errors)
    validate_census(rows, errors)

    if errors:
        print("DESIGN DATA VALIDATION FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("DESIGN DATA VALIDATION PASSED")
    print(f"- census rows: {len(rows)}")
    print("- registered population: 76.000 billion")
    print("- primary nodes: L0=9, L1=46, L2=192, L3=365")
    print("- clusters: Core=4, Inner=8, Middle=15, Frontier=21")
    print(f"- protected systems: {len(PROTECTED_SYSTEMS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
