#!/usr/bin/env python3
"""Run writer activation with no-POV-owner + source-performer precision fixes.

This wrapper changes workflow/QC routing only. A POV can carry information
without owning the decisive action. When the source does not expose an owner
field but the exact decision sentence itself begins with a named/code actor or
institution performing/refusing that decision, retain that source performer in
the writer route. Otherwise keep the owner bounded to an existing role; never
invent a person or promote the protagonist merely because they are POV.
"""

from __future__ import annotations

import re

import build_full_series_context_writer_activation as base

VERBS = (
    "keeps", "keep", "maps", "map", "orders", "order", "chooses", "choose",
    "votes", "vote", "refuses", "refuse", "rejects", "reject", "signs", "sign",
    "accepts", "accept", "authorizes", "authorize", "approves", "approve",
    "commits", "commit", "holds", "hold", "uses", "use", "opens", "open",
    "releases", "release", "separates", "separate", "isolates", "isolate",
    "decides", "decide", "selects", "select", "retains", "retain", "stays", "stay",
    "transmits", "transmit", "grants", "grant", "withholds", "withhold",
    "deploys", "deploy", "restores", "restore", "adopts", "adopt", "requests", "request",
    "leaves", "leave", "hands", "hand", "records", "record", "publishes", "publish",
    "agrees", "agree", "moves", "move", "routes", "route", "cancels", "cancel",
    "stops", "stop", "permits", "permit", "allows", "allow", "maintains", "maintain",
    "suspends", "suspend", "limits", "limit", "continues", "continue", "withdraws", "withdraw",
    "enters", "enter", "issues", "issue", "removes", "remove", "distributes", "distribute",
)
PERFORMER_RE = re.compile(
    r"^(.{1,120}?)\s+(" + "|".join(sorted(VERBS, key=len, reverse=True)) + r")\b",
    re.I,
)
GENERIC_BAD = {
    "it", "this", "that", "there", "one", "someone", "something", "the episode",
    "the approved episode", "the source", "a result", "an outcome", "the result",
}


def source_named_decision_performer(decision: str) -> str | None:
    """Return only a high-confidence source-written performer phrase.

    This is deliberately narrower than a general NLP subject extractor. It
    accepts a sentence-initial actor only when the phrase contains either a
    project actor code (`KT-441`, `H-001`, etc.) or a capitalized proper/institution
    token sequence. Generic role phrases stay bounded for later manual review.
    """
    text = re.sub(r"\s+", " ", decision or "").strip()
    if not text or text.startswith("NON-DISCRETE"):
        return None
    text = re.sub(r"^\[[^\]]+\]\s*", "", text)
    first = re.split(r"(?<=[.!?])\s+|\s*;\s*", text, maxsplit=1)[0].strip()
    match = PERFORMER_RE.match(first)
    if not match:
        return None
    actor = match.group(1).strip(" -,:`[]()")
    low = actor.casefold()
    if low in GENERIC_BAD or len(actor.split()) > 12:
        return None
    if any(x in low for x in ("because ", "while ", " if ", " when ", " after ", " before ", " so that ")):
        return None

    has_code = bool(re.search(r"\b[A-Z]{1,5}-\d{1,4}\b", actor))
    proper = bool(
        re.fullmatch(
            r"[A-Z][A-Za-z'’-]+(?:\s+[A-Z][A-Za-z'’-]+){0,3}"
            r"(?:\s+and\s+[A-Z][A-Za-z'’-]+(?:\s+[A-Z][A-Za-z'’-]+){0,3})?",
            actor,
        )
    )
    if not (has_code or proper):
        return None
    return actor


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
        performer = source_named_decision_performer(decision)
        if performer:
            return (
                "source decision performer/authority actor(s): " + performer,
                "SOURCE-DECISION-PERFORMER + SOURCE DECISION",
            )
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
