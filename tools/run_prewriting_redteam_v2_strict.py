#!/usr/bin/env python3
"""Run the v2 hostile audit with false-positive controls.

The first discovery pass intentionally over-recalled candidates. This wrapper:
- normalizes generated set-family labels before comparison;
- narrows orphan attention to source threads with explicit episode/subact placement;
- records two source-reviewed set-family exceptions where active-target domain
  counts do not describe the actual reader reward/combination engine.

It changes audit interpretation only, not story canon or generated story facts.
"""

from __future__ import annotations

import re

import audit_prewriting_redteam_v2 as audit

_FAMILY = re.compile(r"\b(LINEAGE|EVENT|FUNCTIONAL|RELATIONSHIP|CIVILIZATION)\b")
_ORIGINAL_PARSE_MAPS = audit.parse_maps
_ORIGINAL_SET_MISMATCH = audit.set_family_mismatches

# Manual source review on 2026-08-21:
# - GA1 A3 is FUNCTIONAL because the reader reward is the combined operation of
#   medical + route + technical + service authority; C1-heavy registry domains
#   are carriers/constraints, not the primary set effect.
# - GA8 8C-3 is CIVILIZATION because the reward is a plural rights/compression/
#   audit/access protocol for civilizational operation; C1 registry coding marks
#   rights holders, not a personal-relationship set.
_REVIEWED_SET_EXCEPTIONS = {("GA1", "A3"), ("GA8", "8C-3")}


def parse_maps_normalized():
    rows = _ORIGINAL_PARSE_MAPS()
    for row in rows:
        raw = row["fields"].get("PRIMARY_SET_TYPE", "")
        match = _FAMILY.search(raw)
        if match:
            row["fields"]["PRIMARY_SET_TYPE"] = match.group(1)
    return rows


def set_family_mismatches_reviewed(rows, threads):
    findings = _ORIGINAL_SET_MISMATCH(rows, threads)
    return [
        finding for finding in findings
        if (finding[0]["arc"], finding[0]["code"]) not in _REVIEWED_SET_EXCEPTIONS
    ]


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
audit.set_family_mismatches = set_family_mismatches_reviewed
audit.orphan_watch = orphan_watch_strict


if __name__ == "__main__":
    raise SystemExit(audit.main())
