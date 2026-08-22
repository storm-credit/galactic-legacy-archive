#!/usr/bin/env python3
"""Run Collection Desire finalization with source-bound semantic blindspot fixes.

No new collectible, event or authority is created. This wrapper:
- prevents registry status shorthand from becoming writer-facing desire,
- closes reviewed NEXT_DESIRE skips to the immediate approved subact,
- reconciles a narrow reviewed set of CLSET front targets with explicit source
  `Active Pursuit Windows` when score ranking displaced the registered pursuit,
- and preserves source distinctions when a terse Reward line would otherwise be
  copied into several writer-execution fields.

Named operational labels such as Window A/B/C are source language and remain.
Bare backticked statuses such as `L`, `G`, `C/G/L` are internal metadata.
"""

from __future__ import annotations

import re

import collection_active_pursuit_reconciliation as pursuit
import run_full_series_collection_reader_desires as runner


runner.reader.OVERRIDES[("GA7", "7C-4")] = {
    "discovery": (
        "survivors, service-collapse evidence and affected-region claims must be preserved before federation, Continuity, State and Scorched narratives harden the incident into one convenient story."
    ),
    "acquisition": (
        "secure aid, records and claimant standing while H-001 accepts bounded emergency review, reparations and authority limits without using resignation or total guilt as an escape from specific responsibility."
    ),
    "synergy": (
        "survivor aid, preserved records, affected-region standing and emergency review keep material relief and accountability linked while victims retain the right to reject strategic abstraction."
    ),
    "cost": (
        "H-001's mandate is suspended or reduced or the coalition fractures, and personal relationships with PC/RF actors are damaged."
    ),
    "hook": (
        "evidence that several 'Blood Admiral' incidents occurred under different commanders, titles and timelines turns the next desire into a representative incident matrix and plural responsibility audit."
    ),
}

# GA10 10A-1 source already distinguishes cause, bounded emergency correction,
# irreversible cost and the region's demand to own the correction. The base
# extractor previously copied the terse Reward ('immediate collapse stopped')
# into acquisition/synergy/set-advance, which was mechanically valid but too
# shallow for writer execution. These phrases paraphrase only the approved
# 10A-1 Entry/Goal/Cause stack/P-001 response/Reward/Cost/Hook.
runner.reader.OVERRIDES[("GA10", "10A-1")] = {
    "discovery": (
        "the first handoff can fail through incomplete local staff/training, hidden central dependency or backdoor, local exploitation, hostile/hardliner attack and schedule pressure; the failure must be identified while authentication, payroll, hospital and route services are collapsing."
    ),
    "acquisition": (
        "stop the immediate mass-service collapse with a temporary bounded central correction whose expiration and trace are explicit, without cancelling the handoff or converting emergency use back into permanent central ownership."
    ),
    "synergy": (
        "the bounded correction preserves named people/services long enough for the failure cause to become usable evidence, while its trace/expiration makes the next local correction possible instead of hiding dependency behind another central takeover."
    ),
    "cost": (
        "one irreversible death/loss remains, and the successful emergency override publicly strengthens the argument that P-001's central control is safer."
    ),
    "hook": (
        "the transition region demands local ownership of the correction rather than another central takeover."
    ),
}

_ORIGINAL_SOURCE_FIELD_PACK = runner.reader.source_field_pack
_ORIGINAL_BUILD_OUTPUTS = runner.build_outputs
_STATUS_CODE = re.compile(r"`[A-Z](?:/[A-Z]){0,5}(?:\s+—[^`]*)?`")
_MAP_NAME = re.compile(r"ga(\d+)-collection-desire-subact-map-v1\.md$")
_HEADING = re.compile(r"^##\s+([^\s]+)\s+—\s+(.+?)\s+/\s+E(\d+)[–—-]E?(\d+)\s*$")

# Manual v2 cross-layer review: in these rows the prior NEXT_DESIRE represented
# a later macro pressure while an intervening approved subact still carried a
# distinct reader task. Bridge to the already-derived next-subact reader desire
# rather than inventing a transition sentence.
_REVIEWED_IMMEDIATE_SUBACT_BRIDGES = {
    (2, "2C-3"),
    (4, "4B-3"),
    (4, "4D-2"),
    (6, "6A-2"),
    (6, "6B-1"),
    (7, "7B-1"),
    (8, "8D-1"),
    (9, "9A-1"),
}


def source_field_pack_no_registry_shorthand(subact, selected):
    fields = dict(_ORIGINAL_SOURCE_FIELD_PACK(subact, selected))
    hook = fields.get("hook", "")
    if _STATUS_CODE.search(hook):
        source_hook = runner.reader.layer.first_present(
            subact.block,
            ((
                "hook",
                "final hook",
                "grand-act hook",
                "grand act hook",
                "act-ending trigger",
                "act ending trigger",
                "act-ending reveal",
                "act ending reveal",
                "ending trigger",
                "final trigger",
                "next pressure",
                "next question",
                "next",
            ),),
        )
        if source_hook and not _STATUS_CODE.search(source_hook):
            fields["hook"] = source_hook
    return fields


runner.reader.source_field_pack = source_field_pack_no_registry_shorthand

# `final.build_final_outputs()` assigns `layer.select_threads` from this module
# attribute at build time, so patch the attribute itself. Returning `A-DIRECT`
# keeps these rows out of the historical B-depth manual-closure count: they were
# already valid A rows; only the 1–5 foreground ordering was wrong.
_final = runner.reader.semantic.strict.final
_original_select_threads_manual = _final.select_threads_manual


def select_threads_with_active_pursuit(subact, threads):
    key = (subact.arc, subact.code)
    source_ids = pursuit.REVIEWED_SELECTIONS.get(key)
    if not source_ids:
        return _original_select_threads_manual(subact, threads)

    by_id = {thread.source_id: thread for thread in threads if thread.arc == subact.arc}
    missing = [source_id for source_id in source_ids if source_id not in by_id]
    if missing:
        raise SystemExit(f"{subact.arc} {subact.code}: missing active-pursuit registry IDs: {missing}")

    selected = [
        (by_id[source_id], 260 - index, "SOURCE-ACTIVE-PURSUIT-RECONCILIATION")
        for index, source_id in enumerate(source_ids)
    ]
    return selected, "A-DIRECT"


_final.select_threads_manual = select_threads_with_active_pursuit


def _bridge_status_hooks(outputs):
    maps = []
    for path, text in outputs.items():
        m = _MAP_NAME.match(path.name)
        if m:
            maps.append((int(m.group(1)), path, text))
    maps.sort()

    rows = []
    for ga, path, text in maps:
        lines = text.splitlines()
        current = None
        for idx, line in enumerate(lines):
            h = _HEADING.match(line)
            if h:
                current = {
                    "ga": ga,
                    "path": path,
                    "lines": lines,
                    "code": h.group(1),
                    "start": int(h.group(3)),
                    "reader": "",
                    "next_idx": None,
                    "next": "",
                }
                rows.append(current)
                continue
            if current is None:
                continue
            if line.startswith("- `READER_DESIRE_MAIN`: "):
                current["reader"] = line.split(": ", 1)[1].strip()
            elif line.startswith("- `NEXT_DESIRE`: "):
                current["next_idx"] = idx
                current["next"] = line.split(": ", 1)[1].strip()

    changed = 0
    for idx, row in enumerate(rows):
        needs_status_bridge = bool(_STATUS_CODE.search(str(row["next"])))
        needs_reviewed_bridge = (row["ga"], row["code"]) in _REVIEWED_IMMEDIATE_SUBACT_BRIDGES
        if not (needs_status_bridge or needs_reviewed_bridge):
            continue
        if idx + 1 >= len(rows):
            raise SystemExit(f"final subact still requires NEXT_DESIRE bridge: GA{row['ga']} {row['code']}")
        next_row = rows[idx + 1]
        next_desire = str(next_row["reader"]).strip()
        if not next_desire or _STATUS_CODE.search(next_desire):
            raise SystemExit(f"cannot source-bound bridge NEXT_DESIRE: GA{row['ga']} {row['code']}")
        line_idx = row["next_idx"]
        if line_idx is None:
            raise SystemExit(f"missing NEXT_DESIRE line: GA{row['ga']} {row['code']}")
        replacement = "NEXT APPROVED SUBACT READER DESIRE — " + next_desire
        if row["lines"][line_idx] != "- `NEXT_DESIRE`: " + replacement:
            row["lines"][line_idx] = "- `NEXT_DESIRE`: " + replacement
            changed += 1

    for _ga, path, _text in maps:
        source_row = next(row for row in rows if row["path"] == path)
        outputs[path] = "\n".join(source_row["lines"]).rstrip() + "\n"

    return changed


def build_outputs_blindspot():
    outputs = _ORIGINAL_BUILD_OUTPUTS()
    changed = _bridge_status_hooks(outputs)
    outputs[runner.reader.semantic.SET_AUDIT] = runner.reader.semantic.set_audit_text(outputs)
    build_outputs_blindspot.bridged = changed
    return outputs


build_outputs_blindspot.bridged = 0
runner.build_outputs = build_outputs_blindspot


if __name__ == "__main__":
    code = runner.main()
    print(f"collection_status_hook_bridges={build_outputs_blindspot.bridged}")
    print(f"collection_active_pursuit_reconciled_rows={len(pursuit.REVIEWED_SELECTIONS)}")
    raise SystemExit(code)
