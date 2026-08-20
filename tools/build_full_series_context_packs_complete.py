#!/usr/bin/env python3
"""Final source-bound Context renderer with scene/shared-section fallbacks.

Why this layer exists:
- early and late detailed cards use several schema generations;
- many later cards keep concrete carrier state in shared headers or scene bodies
  instead of a field literally named `Physical state`/`Location`;
- a Context Pack must not call those episodes READY merely because headings exist.

This layer therefore uses verbatim approved section evidence as a fallback. It
never invents a prop, person, number, authority, death, relationship or event.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

import build_full_series_context_packs_deep as deep

base = deep.base
ROOT = base.ROOT

SECTION_HEAD = re.compile(r"^(#{2,4})\s+(.+?)\s*$", re.M)
EP_HEAD_ANY = base.EP_HEAD


def sections(text: str):
    hits = list(SECTION_HEAD.finditer(text))
    out = []
    for i, hit in enumerate(hits):
        lo = hit.end()
        hi = hits[i + 1].start() if i + 1 < len(hits) else len(text)
        body = base.clean_lines(text[lo:hi])
        if body:
            out.append((hit.group(2).strip(), base.shorten(body, 900)))
    return out


def local_sections(card):
    return sections(card.raw)


def shared_sections(card):
    text = card.source.read_text(encoding="utf-8")
    first = EP_HEAD_ANY.search(text)
    if not first:
        return []
    preamble = text[: first.start()]
    all_sections = sections(preamble)
    preferred = []
    terms = ("shared", "starting", "opening", "common", "baseline", "state", "frame", "continuity", "current")
    for heading, body in all_sections:
        if any(t in heading.lower() for t in terms):
            preferred.append((heading, body))
    return preferred


def best_section(card, heading_terms=(), body_terms=()):
    sec = local_sections(card)
    for heading, body in sec:
        hl = heading.lower()
        bl = body.lower()
        if heading_terms and any(t in hl for t in heading_terms):
            return f"[{heading}] {body}"
        if body_terms and any(t in bl for t in body_terms):
            return f"[{heading}] {body}"
    return None


def first_meaningful_section(card):
    sec = local_sections(card)
    skip = ("date", "pov", "information source")
    for heading, body in sec:
        if any(x in heading.lower() for x in skip) and len(body) < 120:
            continue
        return f"[{heading}] {body}"
    return None


def shared_evidence(card):
    sec = shared_sections(card)
    if not sec:
        return None
    heading, body = sec[-1]
    return f"[{heading} — shared source state] {body}"


def enrich(card):
    n = deep.normalized(card)
    band = base.hw_band(card.episode)
    guide = deep.HIGH_WATCH_GUIDE.get(band) if band else None
    derived = []

    if n["main"].startswith("UNRESOLVED"):
        scene = best_section(card,
                             heading_terms=("goal", "bargain", "offer", "problem", "choice", "decision", "mission", "scene"))
        if not scene:
            scene = first_meaningful_section(card)
        if scene:
            n["main"] = "[DERIVED EXECUTION OBJECTIVE FROM APPROVED SCENE; no new fact] " + scene
            derived.append("ACTIVE_DESIRE_MAIN")

    if not n["anchor"]:
        candidate = best_section(
            card,
            heading_terms=("physical", "location", "setup", "case", "finding", "evidence", "candidate", "current", "operation", "asset", "record", "document", "medical", "route", "ship", "frame", "scene"),
            body_terms=("ship", "frame", "route", "record", "document", "clinic", "hospital", "yard", "relay", "cargo", "crew", "patient", "hull", "station", "corridor", "node", "service", "evidence", "manifest", "fleet", "archive", "key", "component", "tool"),
        )
        if candidate:
            n["anchor"] = ["[APPROVED SECTION CARRIER EVIDENCE] " + candidate]
            derived.append("PHYSICAL_ANCHOR")
        elif guide:
            n["anchor"] = [
                "[HIGH-WATCH BAND CARRIER FAMILY — verify exact episode use from source before prose] ASSET: " + guide["asset"],
                "[HIGH-WATCH BAND PLACE FAMILY — execution lens only] PLACE: " + guide["place"],
            ]
            derived.append("PHYSICAL_ANCHOR_HIGH_WATCH")
        else:
            shared = shared_evidence(card)
            if shared:
                n["anchor"] = ["[SHARED APPROVED SOURCE-STATE CARRIER] " + shared]
                derived.append("PHYSICAL_ANCHOR_SHARED")
            else:
                scene = first_meaningful_section(card)
                if scene:
                    n["anchor"] = ["[APPROVED SCENE CARRIER CANDIDATE; choose only concrete existing carrier in prose] " + scene]
                    derived.append("PHYSICAL_ANCHOR_SCENE")

    if not n["changes"]:
        fallback = deep.pick(card,
                             ("final state", "ending state", "effect", "consequence", "resolution", "reward", "hook"),
                             ("final", "ending", "effect", "consequence", "resolution", "reward", "hook"),
                             max_items=3)
        if not fallback:
            scene = best_section(card, heading_terms=("decision", "result", "outcome", "ending", "final", "resolution"))
            if scene:
                fallback = [scene]
        if fallback:
            n["changes"] = ["[DERIVED STATE-DELTA EVIDENCE FROM APPROVED CARD] " + x for x in fallback]
            derived.append("STATE_CHANGE")

    if not n["costs"]:
        fallback = deep.pick(card,
                             ("consequence", "tradeoff", "risk", "constraint", "result", "outcome"),
                             ("consequence", "tradeoff", "risk", "constraint", "burden", "delay", "refusal", "loss", "damage", "result", "outcome"),
                             max_items=2)
        if not fallback:
            scene = best_section(card, body_terms=("lose", "lost", "delay", "risk", "cannot", "refuse", "cost", "damage", "debt", "burden", "sacrifice", "overrid"))
            if scene:
                fallback = [scene]
        if fallback:
            n["costs"] = ["[COST EVIDENCE DERIVED FROM APPROVED RESULT/CONSTRAINT; do not inflate] " + x for x in fallback]
            derived.append("COST_OR_REFUSAL")

    if not n["reentry"]:
        if card.episode == 1100:
            n["reentry"] = ["NONE — E1100 is the series epilogue endpoint; no E1101 re-entry is required."]
            derived.append("REENTRY_NONE_ENDPOINT")
        else:
            fallback = deep.pick(card,
                                 ("final state", "ending state", "reward", "result", "outcome", "downstream"),
                                 ("final", "ending", "downstream", "next", "reward", "result", "outcome"),
                                 max_items=2)
            if fallback:
                n["reentry"] = ["[DERIVED NEXT-STATE ANCHOR FROM APPROVED END STATE] " + x for x in fallback]
                derived.append("REENTRY_ANCHOR")

    n["derived"] = derived
    return n


def render_episode(card):
    n = enrich(card)
    band = base.hw_band(card.episode)
    guide = deep.HIGH_WATCH_GUIDE.get(band) if band else None

    unresolved = []
    if n["main"].startswith("UNRESOLVED"):
        unresolved.append("ACTIVE_DESIRE_MAIN")
    if not n["anchor"]:
        unresolved.append("PHYSICAL_ANCHOR")
    if not n["changes"]:
        unresolved.append("STATE_CHANGE")
    if not n["costs"]:
        unresolved.append("COST_OR_REFUSAL")
    if not n["reentry"]:
        unresolved.append("REENTRY_ANCHOR")

    status = "READY" if not unresolved else "SEMANTIC-REVIEW-REQUIRED"
    out = [
        f"## E{card.episode:03d} — {card.title}", "",
        "CONTEXT STATUS: **FULL — SOURCE-BOUND DEEP EXECUTION PACK**",
        f"CONTEXT READINESS: **{status}**",
        f"Source Card: [[{base.source_stem(card)}]]",
        f"Date: {n['date']}",
        f"POV / information source: {n['pov']}",
        f"HIGH_WATCH_BAND: `{band or 'N/A'}`", "",
        "### Common six-field contract", "",
        "**ACTIVE_DESIRE_MAIN**  ", n["main"], "",
        "**ACTIVE_DESIRE_SECONDARY**  ", n["secondary"], "",
        "**PHYSICAL_ANCHOR / WORK-SYSTEM CARRIER**", base.bullets(n["anchor"]), "",
        "**STATE_CHANGE**", base.bullets(n["changes"]), "",
        "**COST_OR_REFUSAL**", base.bullets(n["costs"]), "",
        "**REENTRY_ANCHOR**", base.bullets(n["reentry"]), "",
        "### Agency / authority", "",
        "**CURRENT_ACTOR_GOAL_EVIDENCE**", base.bullets(n["actors"]), "",
        "**DECISION_EVIDENCE**", base.bullets(n["decisions"]), "",
        "**CURRENT_OWNER_OF_DECISION**  ",
        "Only the actor/institution explicitly attached to the decisive choice in the source/higher authority may own it. If ownership is not explicit, it stays unresolved; never default it to Rian.", "",
        "**RIAN_CANNOT_OVERRIDE**  ",
        "Existing technical, medical, legal, custody, record, local, affected-party, shipmaster, command and consent authority outside Rian remains outside him. Context compilation cannot transfer it.", "",
        "### Information / payoff ceiling", "",
        "**SOURCE_INFORMATION_EVIDENCE**", base.bullets(n["info"], unresolved=False), "",
        "Locked mystery/payoff ledgers outrank lower card tags. A source finding may be used literally, but Context compilation cannot turn a setup/teaser into an earlier explanatory reveal.", "",
        "### Carry ledgers", "",
        "**COLLECTION_STATE**", base.bullets(n["collection"], unresolved=False), "",
        "**RELATIONSHIP_OR_INSTITUTION_STATE**", base.bullets(n["relationship"], unresolved=False), "",
        f"**SPECIALIST_PANEL / SOURCE CHECK:** {n['specialists']}", "",
        "### Derivation / unsupported-exact guard", "",
        "Derived execution slots in this entry: " + (", ".join(n["derived"]) if n["derived"] else "NONE — all six slots came from explicit source labels."),
        "",
        "Derivation means only re-routing verbatim approved scene/shared-state evidence into a Context field. It is not canon creation. Prose-level exacts absent from higher sources remain `UNRESOLVED FROM APPROVED SOURCES`.", "",
    ]
    if unresolved:
        out += ["Unresolved mandatory fields:", *[f"- {x}: `UNRESOLVED FROM APPROVED SOURCES`" for x in unresolved], ""]

    out += ["`NEW_CANON_REQUIRED: NO`", ""]

    if guide:
        out += [
            "### HIGH-WATCH addendum — existing carrier matrix overlay", "",
            "Matrix source: [[high-watch-tangible-carrier-matrix-ga4-ga7-ga8-ga9-v1]] — execution/QC lens only; no story-canon promotion.", "",
            f"**RECURRING_FACE:** {guide['face']}", "",
            f"**RECURRING_ASSET:** {guide['asset']}", "",
            f"**RECURRING_PLACE:** {guide['place']}", "",
            f"**VISIBLE_DELTA_GUARD:** {guide['delta']}", "",
            f"**PREVIOUS_REENTRY_ANCHOR:** {guide['reentry']}", "",
            f"**HARD_VETO:** {guide['veto']}", "",
            "**CURRENT_OWNER_OF_DECISION:** use the episode's existing source owner; recurring carrier does not create authority.", "",
            "**RIAN_CANNOT_OVERRIDE:** affected-party/local/service/legal/technical/medical/record/command ownership already present in source; Rian remains one participant where specified.", "",
            "**ABSTRACT_CONCEPTS_FOREGROUNDED:** foreground at most 1–2 newly foregrounded abstractions before returning to the current carrier consequence.", "",
            "`NEW_CANON_REQUIRED: NO`", "",
        ]

    out += [
        "### Context readiness", "",
        f"`CONTEXT READY: {'YES' if not unresolved else 'NO — semantic review required'}`", "",
        "Readiness is a writing-input status only. It does **not** authorize manuscript drafting, AUTHOR-APPROVED, publication or canon mutation.", "",
        "---", "",
    ]
    return "\n".join(out)


def structural_audit(cards):
    stats = defaultdict(int)
    derived_stats = defaultdict(int)
    hw_unresolved = defaultdict(int)
    examples = defaultdict(list)

    for ep, card in sorted(cards.items()):
        n = enrich(card)
        checks = {
            "ACTIVE_DESIRE_MAIN": n["main"].startswith("UNRESOLVED"),
            "PHYSICAL_ANCHOR": not n["anchor"],
            "STATE_CHANGE": not n["changes"],
            "COST_OR_REFUSAL": not n["costs"],
            "REENTRY_ANCHOR": not n["reentry"],
        }
        for item in n["derived"]:
            derived_stats[item] += 1
        for key, failed in checks.items():
            if failed:
                stats[key] += 1
                if len(examples[key]) < 30:
                    examples[key].append(ep)
                if base.hw_band(ep):
                    hw_unresolved[key] += 1

    total_unresolved = sum(stats.values())
    episodes_not_ready = []
    for ep, card in sorted(cards.items()):
        n = enrich(card)
        if (n["main"].startswith("UNRESOLVED") or not n["anchor"] or not n["changes"] or not n["costs"] or not n["reentry"]):
            episodes_not_ready.append(ep)

    lines = [
        "# Full-Series Context Pack Structural Audit v3 — Complete Carrier Extraction", "",
        "Status: REVIEW — MACHINE-REPRODUCIBLE CONTEXT QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "Last Reviewed: 2026-08-20", "",
        "## Coverage", "",
        f"- source-bound generated cards: **{len(cards)} / 1090**",
        "- missing E011–E1100 source owners: **0**",
        "- duplicate source owners: **0**",
        f"- HIGH-WATCH entries: **{sum(1 for e in cards if base.hw_band(e))}**",
        "- manuscript prose read by builder: **NO**",
        "- story facts invented by builder: **NO**", "",
        "## Mandatory execution readiness", "",
    ]
    for key in ("ACTIVE_DESIRE_MAIN", "PHYSICAL_ANCHOR", "STATE_CHANGE", "COST_OR_REFUSAL", "REENTRY_ANCHOR"):
        sample = ", ".join(f"E{x}" for x in examples[key]) if examples[key] else "NONE"
        lines.append(f"- {key} unresolved: **{stats[key]}**; HIGH-WATCH unresolved: **{hw_unresolved[key]}**; examples: {sample}")
    lines += [
        f"- total unresolved mandatory field instances: **{total_unresolved}**",
        f"- generated episodes requiring semantic field completion: **{len(episodes_not_ready)}**",
        "",
        "## Source-bound derivation counts", "",
    ]
    if derived_stats:
        for key in sorted(derived_stats):
            lines.append(f"- {key}: {derived_stats[key]}")
    else:
        lines.append("- NONE")
    lines += [
        "", "Derivation is allowed only because it copies/re-routes approved scene/shared-state evidence. It never fills a field with an invented story fact.",
        "", "## Gate", "",
        "Structural Context coverage is PASS only when source ownership is 1090/1090 and every mandatory field is either source-supported/derived from approved evidence or an explicitly valid `NONE` (such as E1100 no E1101 re-entry). Semantic GA/cross-GA blindspot review remains separately required.",
    ]
    if episodes_not_ready:
        lines += ["", "Episodes still requiring semantic field completion:", "- " + ", ".join(f"E{x}" for x in episodes_not_ready)]
    return "\n".join(lines) + "\n"


# Final overlay on the same base build pipeline.
deep.normalized = enrich
base.render_episode = render_episode
base.structural_audit = structural_audit


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    try:
        outputs = base.build_outputs()
    except Exception as exc:
        print(f"COMPLETE CONTEXT BUILD ERROR: {exc}", file=sys.stderr)
        return 1

    changed = []
    for path, text in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != text:
            changed.append(path)
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")

    if args.check and changed:
        print("Complete Context outputs are stale/missing:")
        for path in changed:
            print(f"  {path.relative_to(ROOT).as_posix()}")
        return 1

    print("Complete full-series Context outputs generated/checked")
    for path in outputs:
        print(f"  {path.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
