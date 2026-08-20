#!/usr/bin/env python3
"""Run the Collection Desire finalizer with source-bound semantic blindspot fixes.

No new collectible, event or authority is created. This wrapper prevents
backticked registry status shorthand from becoming writer-facing reader desire.
It first prefers an approved hook/ending trigger from the owning subact. If the
registry fallback is still only internal status metadata, NEXT_DESIRE is bridged
to the already-derived reader desire of the next approved subact.

Named operational labels such as Window A/B/C are source language, not status
shorthand, and are preserved. Bare backticked registry statuses such as `L`,
`G`, `C/G/L` are internal metadata and are not valid writer-facing desire text.
"""

from __future__ import annotations

import re

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

_ORIGINAL_SOURCE_FIELD_PACK = runner.reader.source_field_pack
_ORIGINAL_BUILD_OUTPUTS = runner.build_outputs
# Registry state shorthand is written as bare backticked one-letter or slash
# codes (`L`, `G`, `C/G`, `G/R/L — ...`). Source-native phrases such as
# "Window A/B/C" are ordinary text and therefore are not matched here.
_STATUS_CODE = re.compile(r"`[A-Z](?:/[A-Z]){0,5}(?:\s+—[^`]*)?`")
_MAP_NAME = re.compile(r"ga(\d+)-collection-desire-subact-map-v1\.md$")
_HEADING = re.compile(r"^##\s+([^\s]+)\s+—\s+(.+?)\s+/\s+E(\d+)[–—-]E?(\d+)\s*$")


def source_field_pack_no_registry_shorthand(subact, selected):
    fields = dict(_ORIGINAL_SOURCE_FIELD_PACK(subact, selected))
    hook = fields.get("hook", "")
    if _STATUS_CODE.search(hook):
        source_hook = runner.reader.layer.first_present(
            subact.block,
            (
                (
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
                ),
            ),
        )
        if source_hook and not _STATUS_CODE.search(source_hook):
            fields["hook"] = source_hook
    return fields


runner.reader.source_field_pack = source_field_pack_no_registry_shorthand


def _bridge_status_hooks(outputs):
    """Replace only unresolved status-metadata NEXT_DESIRE with next subact desire."""
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
        if not _STATUS_CODE.search(str(row["next"])):
            continue
        if idx + 1 >= len(rows):
            raise SystemExit(f"final subact still has registry-status NEXT_DESIRE: GA{row['ga']} {row['code']}")
        next_row = rows[idx + 1]
        next_desire = str(next_row["reader"]).strip()
        if not next_desire or _STATUS_CODE.search(next_desire):
            raise SystemExit(f"cannot source-bound bridge NEXT_DESIRE: GA{row['ga']} {row['code']}")
        line_idx = row["next_idx"]
        if line_idx is None:
            raise SystemExit(f"missing NEXT_DESIRE line: GA{row['ga']} {row['code']}")
        row["lines"][line_idx] = (
            "- `NEXT_DESIRE`: NEXT APPROVED SUBACT READER DESIRE — " + next_desire
        )
        changed += 1

    for _ga, path, _text in maps:
        # all row objects for the same path share the same mutable line list
        source_row = next(row for row in rows if row["path"] == path)
        outputs[path] = "\n".join(source_row["lines"]).rstrip() + "\n"

    return changed


def build_outputs_blindspot():
    outputs = _ORIGINAL_BUILD_OUTPUTS()
    changed = _bridge_status_hooks(outputs)
    # Set-family classification is unchanged by NEXT_DESIRE bridge; refresh the
    # audit text so one build path remains authoritative.
    outputs[runner.reader.semantic.SET_AUDIT] = runner.reader.semantic.set_audit_text(outputs)
    build_outputs_blindspot.bridged = changed
    return outputs


build_outputs_blindspot.bridged = 0
runner.build_outputs = build_outputs_blindspot


if __name__ == "__main__":
    code = runner.main()
    print(f"collection_status_hook_bridges={build_outputs_blindspot.bridged}")
    raise SystemExit(code)
