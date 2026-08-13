#!/usr/bin/env python3
"""Materialise the 612-system census the atlas already locked.

Why this is generated
---------------------
`galaxy-612-system-census-and-cluster-atlas-v1.md` section 3 lists eleven
fields of `data/galaxy-612-system-census-v1.csv`, and that file did not exist.
Documents were doing arithmetic on a dataset nobody could read.

Writing 612 rows by hand would have invented 612 systems. Generating them does
not: the atlas already locks every aggregate this file has to satisfy --
612 inhabited systems, node classes L0 9 / L1 46 / L2 192 / L3 365, macroregion
allocation Core 24 / Inner 96 / Middle 180 / Frontier 312, and 48 clusters
split 4 / 8 / 15 / 21. This script lays those locks out as rows and stops.

So the census carries **structure, not fiction**. A row gets a stable ID, its
macroregion, its cluster, its node class and a population drawn from the locked
regional totals. It gets a reader-facing name only if a document already gave
it one -- canon place names from the phonetics bible, and the proposed places
from the named-place registry. Every other row's name field is empty on
purpose: atlas canon rule 7 says the census does not imply all 612 systems
appear in prose, and inventing 570 names would contradict that.

Population is deterministic, not random. Scripts here may not use randomness
(it would make the file change on every build), so each region's total is
distributed across its systems by a fixed rule and the remainder lands on the
largest node.

    python tools/build_census.py            write the census
    python tools/build_census.py --check    fail if it is out of date
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ATLAS = DOCS / "02_world/galaxy-612-system-census-and-cluster-atlas-v1.md"
PLACES = DOCS / "02_world/named-place-and-corridor-registry-v1.md"
OUT = DOCS / "02_world/data/galaxy-612-system-census-v1.csv"

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

# Locked by the atlas. Changing these means changing canon, not this script.
REGIONS = [
    # name, systems, clusters, registered population in millions
    ("Core", 24, 4, 24_000),
    ("Inner", 96, 8, 25_000),
    ("Middle", 180, 15, 18_000),
    ("Frontier", 312, 21, 9_000),
]
NODE_CLASSES = [("L0", 9), ("L1", 46), ("L2", 192), ("L3", 365)]

# Node class concentrates toward the Core. The atlas does not fix the joint
# distribution, so the rule is stated here rather than hidden: fill the highest
# class available to each region in region order, Core first.
FIELDS = [
    "system_id", "reader_name", "macroregion", "cluster", "primary_node",
    "registered_population_millions", "specialisation_1", "specialisation_2",
    "governance_r0", "route_profile", "ga10_transition_seed",
    "protected_continuity_note",
]

SPECIALISATIONS = {
    "Core": [("administration", "finance"), ("fleet_yard", "certification"),
             ("archive", "law"), ("relay_trunk", "transit")],
    "Inner": [("manufacturing", "certification"), ("education", "training"),
              ("medical", "care"), ("logistics", "supply")],
    "Middle": [("workshop", "repair"), ("agriculture", "supply"),
               ("mining", "materials"), ("port", "trade")],
    "Frontier": [("salvage", "recovery"), ("outpost", "patrol"),
                 ("settlement", "subsistence"), ("relay", "rescue")],
}
GOVERNANCE = {
    "Core": "imperial_direct",
    "Inner": "imperial_chartered",
    "Middle": "mixed_local_charter",
    "Frontier": "unaligned_or_local",
}
ROUTE_PROFILE = {
    "Core": "trunk_dense",
    "Inner": "trunk_connected",
    "Middle": "branch_connected",
    "Frontier": "sparse_or_seasonal",
}

PLACE_ROW = re.compile(r"^\| N-\d+ \| \*?\*?([^|*]+?)\*?\*? \| ([^|]+) \|")


def read_named_places() -> list[tuple[str, str]]:
    """(name, macroregion) for every place a document already named.

    The canon rows carry the macroregion in their second column; the proposed
    rows carry a node class there and put the region in the section heading.
    Reading the heading covers both without a second regex.
    """
    out: list[tuple[str, str]] = []
    section = ""
    regions = {r for r, _, _, _ in REGIONS}
    for line in PLACES.read_text(encoding="utf-8").split("\n"):
        if line.startswith("### 3."):
            for region in regions:
                if region in line:
                    section = region
                    break
        m = PLACE_ROW.match(line)
        if m:
            second = m.group(2).strip()
            out.append((m.group(1).strip(), second if second in regions else section))
    return out


def node_plan() -> dict[str, list[str]]:
    """Assign node classes to regions, highest class toward the Core."""
    pool = [(name, count) for name, count in NODE_CLASSES]
    plan: dict[str, list[str]] = {}
    pi = 0
    remaining = dict(pool)
    order = [n for n, _ in NODE_CLASSES]
    for region, systems, _, _ in REGIONS:
        assigned: list[str] = []
        while len(assigned) < systems:
            cls = order[pi]
            take = min(remaining[cls], systems - len(assigned))
            assigned += [cls] * take
            remaining[cls] -= take
            if remaining[cls] == 0:
                pi += 1
        plan[region] = assigned
    return plan


def verify_locks_against_atlas() -> None:
    """The constants above claim to mirror the atlas. Prove it every run.

    Without this the script would keep emitting the old shape after someone
    edits the atlas, and the census would quietly stop being the census the
    documents cite.
    """
    text = ATLAS.read_text(encoding="utf-8")
    expected = {f"{name}: {systems} systems" for name, systems, _, _ in REGIONS}
    for phrase in expected:
        region, rest = phrase.split(": ")
        if not re.search(rf"{region}: {rest.split()[0]} systems", text):
            raise SystemExit(f"atlas no longer says '{phrase}' — update REGIONS")
    for cls, count in NODE_CLASSES:
        if not re.search(rf"{cls}: {count} systems", text):
            raise SystemExit(f"atlas no longer says '{cls}: {count} systems' — update NODE_CLASSES")
    total_clusters = sum(c for _, _, c, _ in REGIONS)
    if f"**{total_clusters} operational clusters**" not in text:
        raise SystemExit(f"atlas no longer locks {total_clusters} clusters — update REGIONS")


def build_rows() -> list[dict[str, str]]:
    named = read_named_places()
    by_region: dict[str, list[str]] = {r: [] for r, _, _, _ in REGIONS}
    for name, where in named:
        for region in by_region:
            if where.startswith(region):
                by_region[region].append(name)
                break
    plan = node_plan()
    rows: list[dict[str, str]] = []
    seq = 0
    for region, systems, clusters, pop_millions in REGIONS:
        names = list(by_region[region])
        # split the locked regional population evenly, remainder to the first
        base, extra = divmod(pop_millions, systems)
        specs = SPECIALISATIONS[region]
        for i in range(systems):
            seq += 1
            cluster_index = i % clusters
            rows.append({
                "system_id": f"SYS-{seq:03d}",
                "reader_name": names.pop(0) if names else "",
                "macroregion": region,
                "cluster": f"{region[:2].upper()}-C{cluster_index + 1:02d}",
                "primary_node": plan[region][i],
                "registered_population_millions": str(base + (extra if i == 0 else 0)),
                "specialisation_1": specs[i % len(specs)][0],
                "specialisation_2": specs[i % len(specs)][1],
                "governance_r0": GOVERNANCE[region],
                "route_profile": ROUTE_PROFILE[region],
                "ga10_transition_seed": "PENDING",
                "protected_continuity_note": "PROTECTED_NAME" if rows and rows[-1]["reader_name"] else "",
            })
    for row in rows:
        row["protected_continuity_note"] = "PROTECTED_NAME" if row["reader_name"] else ""
    return rows


def render(rows: list[dict[str, str]]) -> str:
    from io import StringIO
    buf = StringIO()
    writer = csv.DictWriter(buf, fieldnames=FIELDS, quoting=csv.QUOTE_ALL,
                            lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    verify_locks_against_atlas()
    rows = build_rows()
    assert len(rows) == 612, len(rows)
    text = render(rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    current = OUT.read_text(encoding="utf-8") if OUT.exists() else None
    if current != text:
        if args.check:
            print(f"{OUT.relative_to(ROOT).as_posix()} is out of date. "
                  f"Run: python tools/build_census.py")
            return 1
        OUT.write_text(text, encoding="utf-8")
    print(f"  {OUT.relative_to(ROOT).as_posix()}: {len(rows)} systems, "
          f"{sum(1 for r in rows if r['reader_name'])} named")
    return 0


if __name__ == "__main__":
    sys.exit(main())
