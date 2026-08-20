#!/usr/bin/env python3
"""Run the v2 hostile audit with false-positive controls.

The first discovery pass intentionally over-recalled candidates. This wrapper
normalizes generated set-family labels before comparison and narrows orphan
attention to source threads that have explicit episode/subact placement. It
changes audit interpretation only, not story canon or generated story facts.
"""

from __future__ import annotations

import re

import audit_prewriting_redteam_v2 as audit

_FAMILY = re.compile(r"\b(LINEAGE|EVENT|FUNCTIONAL|RELATIONSHIP|CIVILIZATION)\b")
_ORIGINAL_PARSE_MAPS = audit.parse_maps


def parse_maps_normalized():
    rows = _ORIGINAL_PARSE_MAPS()
    for row in rows:
        raw = row["fields"].get("PRIMARY_SET_TYPE", "")
        match = _FAMILY.search(raw)
        if match:
            row["fields"]["PRIMARY_SET_TYPE"] = match.group(1)
    return rows


def orphan_watch_strict(thread_rows):
    """Flag only explicit, episode-addressable threads that never front-stage.

    `ARC_WIDE_OR_UNSPECIFIED` rows are support/ledger architecture by design and
    cannot be called orphaned reader promises merely because they are not one of
    the 1–5 front-stage targets of a subact.
    """
    orphans = []
    high = []
    for row in thread_rows:
        try:
            selected = int(row.get("selected_as_active_target_count") or 0)
        except ValueError:
            selected = 0
        if selected:
            continue
        orphans.append(row)

        explicit_subacts = (row.get("explicit_subacts") or "").strip()
        if not explicit_subacts or explicit_subacts == "ARC_WIDE_OR_UNSPECIFIED":
            continue
        refs = [x.strip() for x in (row.get("explicit_episode_refs") or "").split("|") if x.strip()]
        if not refs:
            continue

        kinds = set(filter(None, (row.get("entry_kinds") or "").split("|")))
        phases = set(filter(None, (row.get("desire_phases") or "").split("|")))
        title_low = (row.get("title") or "").casefold()

        # Strong reader-facing evidence only: a narrative/set promise, or a
        # physical thread with acquisition+synergy and repeated episode refs,
        # or a clearly flagship/high-memory title with multiple refs.
        promise = bool(kinds & {"NARRATIVE_PROMISE", "SET"})
        physical_chain = (
            row.get("primary_domain") in audit.PHYSICAL_DOMAINS
            and {"ACQUISITION", "SYNERGY"} <= phases
            and len(refs) >= 3
        )
        title_flag = any(key in title_low for key in audit.HIGH_VALUE_TITLE) and len(refs) >= 2
        if promise or physical_chain or title_flag:
            high.append(row)
    return orphans, high


audit.parse_maps = parse_maps_normalized
audit.orphan_watch = orphan_watch_strict


if __name__ == "__main__":
    raise SystemExit(audit.main())
