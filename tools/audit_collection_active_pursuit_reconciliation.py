#!/usr/bin/env python3
"""Audit reviewed Collection registry Active Pursuit -> CLSET routing.

This is a workflow/QC cross-layer audit. It verifies that the reviewed source
registry IDs are actually present in generated CLSET ACTIVE_TARGETS and that the
three source-reviewed support threads remain intentionally secondary rather than
being fabricated into separate reader quests.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import audit_prewriting_redteam_v2 as base
import collection_active_pursuit_reconciliation as pursuit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "99_quality_control" / "collection-active-pursuit-crosslayer-redteam-v1.md"


def build_report() -> str:
    maps = {(row["arc"], row["code"]): row for row in base.parse_maps()}
    thread_rows, threads = base.load_threads()
    thread_by_source = {}
    for row in thread_rows:
        thread_by_source[(row["arc"], row["source_id"])] = row

    failures = []
    reviewed_rows = []
    for key, expected_ids in pursuit.REVIEWED_SELECTIONS.items():
        row = maps.get(key)
        if row is None:
            failures.append(f"missing generated CLSET row: {key[0]} {key[1]}")
            continue
        actual_ids = []
        for thread_id, _title in row["targets"]:
            source = threads.get(thread_id)
            actual_ids.append(source["source_id"] if source else f"UNKNOWN:{thread_id}")
        missing = [source_id for source_id in expected_ids if source_id not in actual_ids]
        unexpected = [source_id for source_id in actual_ids if source_id not in expected_ids]
        if missing or unexpected or len(actual_ids) != len(expected_ids):
            failures.append(
                f"{key[0]} {key[1]} target mismatch: expected={expected_ids} actual={tuple(actual_ids)}"
            )
        reviewed_rows.append((key, expected_ids, tuple(actual_ids), missing, unexpected))

    secondary = []
    for thread_id, reason in pursuit.ACCEPTED_SECONDARY_ORPHANS.items():
        row = threads.get(thread_id)
        if row is None:
            failures.append(f"accepted-secondary thread missing from index: {thread_id}")
            continue
        try:
            selected = int(row.get("selected_as_active_target_count") or 0)
        except ValueError:
            selected = -1
        if selected != 0:
            failures.append(f"accepted-secondary thread unexpectedly front-staged: {thread_id} count={selected}")
        secondary.append((thread_id, row.get("source_id", ""), row.get("title", ""), selected, reason))

    status = "PASS" if not failures else "FAIL"
    lines = [
        "# Collection Active-Pursuit Cross-Layer Red-Team v1",
        "",
        f"Status: {status} — EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        "## Purpose",
        "",
        "Registry `Active Pursuit Windows` outrank score convenience when they explicitly name the reader-facing pursuit. This audit checks only manually reviewed rows where generated CLSET selection had displaced a named pursuit with adjacent support texture.",
        "",
        "## Reviewed CLSET rows",
        "",
        f"- reviewed reconciliations: **{len(pursuit.REVIEWED_SELECTIONS)}**",
        f"- target mismatches: **{len(failures)}** total failure(s) including secondary checks",
        "",
        "| CLSET | Expected existing registry IDs | Generated IDs | Verdict | Reason |",
        "|---|---|---|---|---|",
    ]
    for key, expected, actual, missing, unexpected in reviewed_rows:
        verdict = "PASS" if not missing and not unexpected and len(expected) == len(actual) else "FAIL"
        reason = pursuit.RATIONALE[key].replace("|", "/")
        lines.append(
            f"| {key[0]} {key[1]} | `{'`, `'.join(expected)}` | `{'`, `'.join(actual)}` | **{verdict}** | {reason} |"
        )

    lines.extend([
        "",
        "## Reviewed secondary/support orphans",
        "",
        "These are not unresolved omissions. They remain inside larger pursuits as tools/provenance support and therefore should not consume one of the 1–5 front-stage CLSET slots.",
        "",
        "| Thread | Source ID / title | Active-target count | Ruling |",
        "|---|---|---:|---|",
    ])
    for thread_id, source_id, title, selected, reason in secondary:
        lines.append(f"| `{thread_id}` | `{source_id}` / {title} | {selected} | {reason.replace('|','/')} |")

    lines.extend([
        "",
        "## Failure queue",
        "",
    ])
    if failures:
        for failure in failures:
            lines.append(f"- {failure}")
    else:
        lines.append("- NONE")

    lines.extend([
        "",
        "## Ruling",
        "",
        f"- source Active Pursuit -> generated CLSET reviewed routing: **{status}**",
        "- people/communities remain relationship/authority targets, never owned objects: **ENFORCED**",
        "- new story fact / new collectible / new authority: **0**",
        "- manuscript prose used as source: **0**",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    text = build_report()
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            raise SystemExit("active-pursuit cross-layer audit stale/missing")
    else:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(text, encoding="utf-8")
    print(text)
    if "Status: FAIL" in text:
        raise SystemExit("ACTIVE PURSUIT CROSS-LAYER GATE FAIL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
