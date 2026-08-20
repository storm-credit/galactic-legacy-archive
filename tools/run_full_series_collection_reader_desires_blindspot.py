#!/usr/bin/env python3
"""Run the Collection Desire finalizer with source-bound semantic blindspot fixes.

No new collectible, event or authority is created. This wrapper prevents
backticked registry status shorthand from becoming writer-facing reader desire
when the approved act/subact map already supplies an ending hook/trigger.
Named operational labels such as Window A/B/C are source language, not status
shorthand, and are preserved.
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
# Registry state shorthand is written as backticked status codes (`C/G`,
# `G/R/L — ...`). Do not confuse it with real source names such as Window A/B/C.
_STATUS_CODE = re.compile(r"`[A-Z](?:/[A-Z]){1,5}(?:\s+—[^`]*)?`")


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


if __name__ == "__main__":
    raise SystemExit(runner.main())
