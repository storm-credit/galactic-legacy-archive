#!/usr/bin/env python3
"""Validate the noncanon collection normalization outputs."""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "docs" / "09_collection" / "data"
SOURCE_FILE = DATA_DIR / "collection-normalization-full-source-rows-v1.csv"
EXPANDED_FILE = DATA_DIR / "collection-normalization-full-expanded-records-v1.csv"

EXPECTED_ARCS = {
    "GA1": 42,
    "GA2": 45,
    "GA3": 43,
    "GA4": 40,
    "GA5": 45,
    "GA6": 40,
    "GA7": 39,
    "GA8": 36,
    "GA9": 31,
    "GA10": 54,
}
ALLOWED_DOMAINS = {f"C{i}" for i in range(1, 9)}
ALLOWED_KINDS = {
    "ENTITY",
    "RELATIONSHIP",
    "CONTROL_CLAIM",
    "STATE_TRANSITION",
    "LOSS_OBLIGATION",
    "NARRATIVE_PROMISE",
    "SET",
}
ALLOWED_BASIS = {"DRY_RUN_REVIEWED", "SPECIALIST_CORRECTED", "HEURISTIC_PROVISIONAL"}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    errors: list[str] = []
    try:
        sources = read_csv(SOURCE_FILE)
        expanded = read_csv(EXPANDED_FILE)
    except FileNotFoundError as exc:
        print(f"missing output: {exc}", file=sys.stderr)
        return 1

    if len(sources) != 415:
        errors.append(f"expected 415 source rows, found {len(sources)}")
    if Counter(row["arc"] for row in sources) != Counter(EXPECTED_ARCS):
        errors.append(f"arc counts mismatch: {Counter(row['arc'] for row in sources)}")

    source_ids = [row["source_row_id"] for row in sources]
    source_keys = [row["source_key"] for row in sources]
    entry_ids = [row["entry_id"] for row in expanded]
    if len(source_ids) != len(set(source_ids)):
        errors.append("duplicate source_row_id")
    if len(source_keys) != len(set(source_keys)):
        errors.append("duplicate source_key")
    if len(entry_ids) != len(set(entry_ids)):
        errors.append("duplicate entry_id")

    expanded_by_id = {row["entry_id"]: row for row in expanded}
    source_by_id = {row["source_row_id"]: row for row in sources}
    referenced_entries: list[str] = []

    for row in sources:
        domains = set(row["domain_tags"].split("|"))
        kinds = set(row["entry_kinds"].split("|"))
        normalized_ids = row["normalized_record_ids"].split("|")
        referenced_entries.extend(normalized_ids)
        if not domains or not domains <= ALLOWED_DOMAINS:
            errors.append(f"{row['source_key']}: invalid domains {sorted(domains)}")
        if not kinds or not kinds <= ALLOWED_KINDS:
            errors.append(f"{row['source_key']}: invalid kinds {sorted(kinds)}")
        if row["primary_domain"] not in domains:
            errors.append(f"{row['source_key']}: primary domain absent from tags")
        if row["classification_basis"] not in ALLOWED_BASIS:
            errors.append(f"{row['source_key']}: invalid classification basis")
        if row["canon_promotion"] != "NONE":
            errors.append(f"{row['source_key']}: canon promotion must remain NONE")
        source_path = ROOT / row["source_file"]
        if not source_path.exists():
            errors.append(f"{row['source_key']}: missing source file")
        else:
            line_number = int(row["source_line"])
            lines = source_path.read_text(encoding="utf-8-sig").splitlines()
            expected_heading = f"## {row['source_id']} — {row['title']}"
            if line_number < 1 or line_number > len(lines) or lines[line_number - 1] != expected_heading:
                errors.append(f"{row['source_key']}: source line no longer matches heading")

    if set(referenced_entries) != set(entry_ids):
        errors.append("source-to-expanded entry coverage mismatch")
    if len(referenced_entries) != len(entry_ids):
        errors.append("expanded entry referenced more than once")

    for row in expanded:
        source = source_by_id.get(row["source_row_id"])
        if source is None:
            errors.append(f"{row['entry_id']}: missing source row")
            continue
        if row["entry_kind"] not in ALLOWED_KINDS:
            errors.append(f"{row['entry_id']}: invalid kind")
        if row["entry_kind"] not in source["entry_kinds"].split("|"):
            errors.append(f"{row['entry_id']}: kind absent from source row")
        domains = set(row["domain_tags"].split("|"))
        if not domains or not domains <= ALLOWED_DOMAINS:
            errors.append(f"{row['entry_id']}: invalid domains {sorted(domains)}")
        if row["primary_domain"] not in domains:
            errors.append(f"{row['entry_id']}: primary domain absent from tags")
        if row["source_key"] != source["source_key"]:
            errors.append(f"{row['entry_id']}: source key mismatch")
        if row["canon_promotion"] != "NONE":
            errors.append(f"{row['entry_id']}: canon promotion must remain NONE")

    expanded_kinds_by_source: dict[str, set[str]] = {}
    for row in expanded:
        expanded_kinds_by_source.setdefault(row["source_row_id"], set()).add(row["entry_kind"])
    for row in sources:
        if expanded_kinds_by_source.get(row["source_row_id"], set()) != set(row["entry_kinds"].split("|")):
            errors.append(f"{row['source_key']}: source/expanded kind coverage mismatch")

    if errors:
        print("COLLECTION NORMALIZATION VALIDATION FAILED", file=sys.stderr)
        for error in errors[:100]:
            print(f"- {error}", file=sys.stderr)
        if len(errors) > 100:
            print(f"- and {len(errors) - 100} more", file=sys.stderr)
        return 1

    print("COLLECTION NORMALIZATION VALIDATION PASSED")
    print(f"- source rows preserved: {len(sources)}")
    print(f"- expanded noncanon records linked: {len(expanded)}")
    print(f"- reviewed source rows: {sum(row['classification_basis'] == 'DRY_RUN_REVIEWED' for row in sources)}")
    print(f"- specialist-corrected source rows: {sum(row['classification_basis'] == 'SPECIALIST_CORRECTED' for row in sources)}")
    print(f"- provisional source rows: {sum(row['classification_basis'] == 'HEURISTIC_PROVISIONAL' for row in sources)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
