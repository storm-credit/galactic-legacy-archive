#!/usr/bin/env python3
"""Reviewed resolution of the v2 source-role decision-owner WATCH queue.

The role extractor intentionally over-recalls. This table resolves every row in
that 50-episode queue without inventing a person:
- `SAFE_ROLE_OWNERS` are exact source-written collective/institutional actors
  that visibly perform, refuse, authorize, or delimit the approved decision;
- `REVIEWED_NON_PERFORMERS` are imperative/passive/criteria phrases that only
  looked like subjects to the heuristic and must *not* be promoted.

Workflow/QC only; story canon effect = none.
"""

from __future__ import annotations

SAFE_ROLE_OWNERS: dict[int, str] = {
    30: "ordinary students/workers",
    71: "licensed clinicians",
    108: "the board",
    115: "board",
    130: "crew",
    131: "crew",
    150: "worker/caravan council",
    160: "crew",
    172: "Neutral captain",
    185: "technical board",
    208: "Orsa/Ardis operators",
    210: "crew",
    211: "Toma",
    214: "local authorities",
    217: "local operator/worker",
    221: "workers",
    242: "workers",
    267: "local representatives",
    280: "local Helix employees",
    283: "local Helix employees",
    293: "local actors",
    295: "the board",
    312: "survivors and families",
    329: "local current operators and affected bodies",
    549: "Lio/current operators, Asel, and local worker tugs",
    681: "Common Fact Board plus the field-specific current decision actors enumerated in the source decision",
    693: "local operators",
    815: "each community",
    1094: "Haren",
}

# Exact prior heuristic capture prefix -> reason not to promote it as owner.
REVIEWED_NON_PERFORMERS: dict[int, str] = {
    61: "passive object/state phrase ('patient-authorized local fragment deleted/locked'); the fragment is not a decision owner",
    205: "imperative/action result ('proceed once under local stop authority') with no source-written subject in the captured phrase",
    228: "imperative/action result ('complete a bounded temporary repair') rather than a source-written actor",
    288: "imperative classification instruction ('classify the path...') rather than a source-written actor",
    298: "imperative combination instruction ('combine central external coordination...') rather than a source-written actor",
    362: "imperative combination instruction ('combine Registry provenance...') rather than a source-written actor",
    386: "imperative result ('retain the care-first pilot sequence...') rather than a source-written actor",
    396: "imperative result ('continue the pilot...') rather than a source-written actor",
    453: "imperative result ('issue 14-day emergency...') rather than a source-written actor",
    488: "evaluation procedure ('score propulsion/thermal...') rather than a source-written actor",
    519: "allocation criteria list; the criteria rank seats/cargo but are not themselves an actor",
    587: "imperative stop result ('end the test...') rather than a source-written actor",
    598: "state/rule phrase ('patient consent... remain separate fields') rather than a single decision owner",
    624: "imperative resource mix ('use local tugs...') rather than a source-written actor",
    642: "imperative agreement form ('use named transport-service agreements...') rather than a source-written actor",
    654: "imperative allocation rule ('distribute holding...') rather than a source-written actor",
    678: "the captured prefix is a technical-stop mechanism; actual authority is distributed and already bounded by source decision/Ardo/rescue actors, so do not collapse it into one role-owner string",
    701: "noun/result bundle ('staged low-mass transfer, local worker stop...') rather than a grammatically source-written deciding subject",
    906: "imperative policy result ('retain local stops...') rather than a source-written actor",
    1087: "prohibition phrase naming people who explicitly do *not* receive the master key; naming them as owner would invert the source rule",
    1096: "passive ordinary-task completion; no single source-written deciding subject is fixed by the captured phrase",
}

EXPECTED_QUEUE = set(SAFE_ROLE_OWNERS) | set(REVIEWED_NON_PERFORMERS)
assert len(EXPECTED_QUEUE) == 50, len(EXPECTED_QUEUE)
assert not (set(SAFE_ROLE_OWNERS) & set(REVIEWED_NON_PERFORMERS))
