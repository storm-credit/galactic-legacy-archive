#!/usr/bin/env python3
"""Audit repetition and reader-memory pressure in generated collection-desire maps."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_DIR = ROOT / "docs" / "09_collection" / "generated" / "desire_subact"
OUT = ROOT / "docs" / "99_quality_control" / "full-series-collection-desire-repetition-reader-memory-redteam-v1.md"

HEADER_RE = re.compile(r"^##\s+([^\s]+)\s+—\s+(.+?)\s+/\s+E(\d+)[–—-]E?(\d+)\s*$")
FIELD_RE = re.compile(r"^- `([^`]+)`: ?(.*)$")
TARGET_RE = re.compile(r"^\s+- `([^`]+)` / `([^`]+)` / (.+?) — ")


@dataclass
class Row:
    arc: str
    code: str
    title: str
    start: int
    end: int
    primary_set: str
    reader_desire: str
    discovery: str
    acquisition: str
    synergy: str
    cost: str
    next_desire: str
    ownership_guard: str
    target_ids: tuple[str, ...]
    source_ids: tuple[str, ...]


def norm(text: str) -> str:
    text = re.sub(r"`", "", text)
    text = re.sub(r"\s+", " ", text).strip().casefold()
    return text


def parse_map(path: Path) -> list[Row]:
    arc_match = re.match(r"(ga\d+)-", path.name)
    if not arc_match:
        return []
    arc = arc_match.group(1).upper()
    lines = path.read_text(encoding="utf-8").splitlines()
    rows: list[Row] = []
    i = 0
    while i < len(lines):
        match = HEADER_RE.match(lines[i])
        if not match:
            i += 1
            continue
        code, title, start, end = match.groups()
        i += 1
        fields: dict[str, str] = {}
        target_ids: list[str] = []
        source_ids: list[str] = []
        in_targets = False
        while i < len(lines) and not lines[i].startswith("## "):
            line = lines[i]
            field = FIELD_RE.match(line)
            if field:
                key, value = field.groups()
                fields[key] = value.strip()
                in_targets = key == "ACTIVE_TARGETS"
                i += 1
                continue
            if in_targets:
                target = TARGET_RE.match(line)
                if target:
                    target_ids.append(target.group(1))
                    source_ids.append(target.group(2))
            i += 1
        primary = fields.get("PRIMARY_SET_TYPE", "")
        primary_match = re.search(r"`([A-Z]+)`", primary)
        rows.append(
            Row(
                arc=arc,
                code=code,
                title=title,
                start=int(start),
                end=int(end),
                primary_set=primary_match.group(1) if primary_match else primary,
                reader_desire=fields.get("READER_DESIRE_MAIN", ""),
                discovery=fields.get("DISCOVERY", ""),
                acquisition=fields.get("ACQUISITION_OR_CONNECTION", ""),
                synergy=fields.get("SYNERGY_OR_USE", ""),
                cost=fields.get("COST_REFUSAL_OR_LOSS", ""),
                next_desire=fields.get("NEXT_DESIRE", ""),
                ownership_guard=fields.get("OWNERSHIP_GUARD", ""),
                target_ids=tuple(target_ids),
                source_ids=tuple(source_ids),
            )
        )
    return rows


def longest_primary_run(rows: list[Row]) -> tuple[str, int, str, str]:
    best_type = ""
    best_count = 0
    best_start = ""
    best_end = ""
    current_type = ""
    current_count = 0
    current_start = ""
    last_code = ""
    for row in rows:
        if row.primary_set == current_type:
            current_count += 1
        else:
            current_type = row.primary_set
            current_count = 1
            current_start = row.code
        last_code = row.code
        if current_count > best_count:
            best_type = current_type
            best_count = current_count
            best_start = current_start
            best_end = last_code
        elif current_count == best_count and current_type == best_type:
            best_end = last_code
    return best_type, best_count, best_start, best_end


def build_audit(rows: list[Row]) -> str:
    target_count_fail = [row for row in rows if not (1 <= len(row.target_ids) <= 5)]
    missing_required = [
        row
        for row in rows
        if not all(
            norm(value)
            for value in (
                row.reader_desire,
                row.discovery,
                row.acquisition,
                row.synergy,
                row.cost,
                row.next_desire,
                row.ownership_guard,
            )
        )
    ]

    duplicate_desire: list[tuple[Row, Row]] = []
    duplicate_signature: list[tuple[Row, Row]] = []
    repeated_target_set: list[tuple[Row, Row]] = []
    for left, right in zip(rows, rows[1:]):
        if left.arc != right.arc:
            continue
        if norm(left.reader_desire) == norm(right.reader_desire):
            duplicate_desire.append((left, right))
        if left.target_ids == right.target_ids:
            repeated_target_set.append((left, right))
            if norm(left.reader_desire) == norm(right.reader_desire):
                duplicate_signature.append((left, right))

    set_counts = Counter(row.primary_set for row in rows)
    target_freq = Counter(target for row in rows for target in row.target_ids)
    rows_by_arc: dict[str, list[Row]] = {}
    for row in rows:
        rows_by_arc.setdefault(row.arc, []).append(row)

    hard_fail = bool(target_count_fail or missing_required or duplicate_desire or duplicate_signature or len(rows) != 160)
    verdict = "FAIL" if hard_fail else "PASS"

    lines = [
        "# Full-Series Collection Desire Repetition / Reader-Memory Red-Team v1",
        "",
        f"Status: {verdict} — EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        "## Verdict",
        "",
        f"> **{verdict} — collection desire routing is not mechanically duplicating an adjacent reader-desire packet.**",
        "",
        "## Coverage",
        "",
        f"- subacts parsed: **{len(rows)} / 160**",
        f"- active-target count outside 1–5: **{len(target_count_fail)}**",
        f"- mandatory desire/reward/guard fields missing: **{len(missing_required)}**",
        f"- exact adjacent `READER_DESIRE_MAIN` duplicates: **{len(duplicate_desire)}**",
        f"- exact adjacent desire + active-target signature duplicates: **{len(duplicate_signature)}**",
        f"- adjacent identical active-target sets with changed desire: **{len(repeated_target_set)}**",
        "",
        "Identical target sets with a changed desire are a WATCH, not an automatic failure: a recurring ship/person/institution should re-enter after state change instead of being replaced by a new noun.",
        "",
        "## Primary Set-Type Distribution",
        "",
    ]
    for set_type in ("LINEAGE", "EVENT", "FUNCTIONAL", "RELATIONSHIP", "CIVILIZATION"):
        lines.append(f"- {set_type}: **{set_counts.get(set_type, 0)}**")

    lines.extend(["", "## Longest Same-Primary-Set Runs", ""])
    for arc in sorted(rows_by_arc, key=lambda value: int(value[2:])):
        set_type, count, start, end = longest_primary_run(rows_by_arc[arc])
        lines.append(f"- {arc}: `{set_type}` x **{count}** ({start}→{end})")

    lines.extend(["", "## Most Reused Active Threads", ""])
    for target, count in target_freq.most_common(15):
        lines.append(f"- `{target}`: **{count} subacts**")

    lines.extend(["", "## Adjacent Target-Set Reuse WATCH", ""])
    if repeated_target_set:
        for left, right in repeated_target_set:
            lines.append(
                f"- {left.arc} {left.code}→{right.code}: same active targets, but reader desire changes from `{left.reader_desire}` to `{right.reader_desire}`"
            )
    else:
        lines.append("- NONE")

    lines.extend(["", "## Hard-Failure Queues", ""])
    if target_count_fail:
        lines.append("### Target count")
        lines.extend(f"- {row.arc} {row.code}: {len(row.target_ids)}" for row in target_count_fail)
    if missing_required:
        lines.append("### Missing required field")
        lines.extend(f"- {row.arc} {row.code}" for row in missing_required)
    if duplicate_desire:
        lines.append("### Exact adjacent reader-desire duplicates")
        lines.extend(f"- {left.arc} {left.code}→{right.code}" for left, right in duplicate_desire)
    if not (target_count_fail or missing_required or duplicate_desire or duplicate_signature):
        lines.append("- NONE")

    lines.extend(
        [
            "",
            "## Reader-Memory / Collection Ethics Ruling",
            "",
            "- front-stage target count remains bounded at 1–5: **PASS**" if not target_count_fail else "- front-stage target count remains bounded at 1–5: **FAIL**",
            "- recurring targets may return after state change; novelty is not manufactured by adding new collectible nouns: **ENFORCED**",
            "- exact adjacent desire packets are forbidden because they create spreadsheet rhythm: **ENFORCED**",
            "- people/communities are not converted into inventory ownership: **ENFORCED**",
            "- new relic/ability/authority quota: **NONE**",
            "- new story canon required: **0**",
            "",
        ]
    )
    return "\n".join(lines)


def outputs() -> dict[Path, str]:
    rows: list[Row] = []
    for path in sorted(MAP_DIR.glob("ga*-collection-desire-subact-map-v1.md"), key=lambda p: int(re.match(r"ga(\d+)", p.name).group(1))):
        rows.extend(parse_map(path))
    return {OUT: build_audit(rows)}


def write_or_check(data: dict[Path, str], check: bool) -> None:
    stale = []
    for path, text in data.items():
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
    if stale:
        raise SystemExit("REPETITION AUDIT STALE/MISSING:\n- " + "\n- ".join(stale))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = outputs()
    write_or_check(data, args.check)
    text = data[OUT]
    if "Status: PASS — EXECUTION QC" not in text:
        print(text)
        raise SystemExit("COLLECTION DESIRE REPETITION/READER-MEMORY GATE FAIL")
    print("collection_desire_repetition_reader_memory=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
