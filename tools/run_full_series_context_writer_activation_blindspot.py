#!/usr/bin/env python3
"""Run writer activation with the no-POV-owner blindspot closure.

This wrapper changes workflow/QC routing only. A POV can carry information
without owning the decisive action. When the source does not explicitly name a
decision owner, keep the owner bounded to an existing role plus the exact
source decision instead of promoting the protagonist/POV by default.
"""

from __future__ import annotations

import build_full_series_context_writer_activation as base


def owner_route_no_pov_fallback(card, engine, decision, pov):
    explicit = base.first(
        card,
        "decision owner",
        "current owner of decision",
        "response owners",
        "pov / decision owner",
        "pov/decision owner",
        "pov / decision owners",
        "pov/decision owners",
    )
    front = base.source_front(card)
    actors = base.source_actors(card)

    if explicit:
        return explicit, "SOURCE-EXPLICIT"
    if front:
        return front, "SOURCE-FRONT-STAGE"
    if decision and actors:
        return (
            "actor(s) in source actor block who perform/refuse the exact decision: "
            + base.clip(actors, 300),
            "WORKFLOW-ROUTE FROM SOURCE ACTORS + DECISION",
        )
    if decision:
        return (
            f"bounded {base.OWNER_ROLE[engine]}; identify the performer/signatory/refuser from this exact source decision beat: "
            + base.clip(decision, 420),
            "WORKFLOW-BOUNDED ROLE + SOURCE DECISION",
        )
    if actors:
        return (
            "bounded decision-bearing actor(s) already present in the source actor block: "
            + base.clip(actors, 320),
            "WORKFLOW-BOUNDED ROLE + SOURCE ACTORS",
        )
    return base.OWNER_ROLE[engine], "WORKFLOW-BOUNDED ROLE"


base.owner_route = owner_route_no_pov_fallback

# Import after the patch so the existing enhanced label normalization,
# load-bearing loss/payoff overrides and final epilogue routes are preserved.
import finalize_context_load_bearing_overrides as finalizer  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(finalizer.runner.main())
