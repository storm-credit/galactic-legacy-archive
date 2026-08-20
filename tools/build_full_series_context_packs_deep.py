#!/usr/bin/env python3
"""Deep Context renderer layered on build_full_series_context_packs.py.

The base builder owns source discovery, duplicate/gap hard-fails and GA ranges.
This renderer broadens extraction across the several detailed-card schemas used
from GA1 through GA10 and overlays the existing HIGH-WATCH carrier matrix as an
execution/QC lens. It still reads no manuscript prose and invents no story fact.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

import build_full_series_context_packs as base

ROOT = base.ROOT
OUT = base.OUT

# Existing noncanon execution aid explicitly adopted as a source lens by the
# Context Pack execution spec. These are band-level carrier families, not new
# episode facts.
HIGH_WATCH_GUIDE = {
    "GA4 E431–438": {
        "face": "existing successor/office candidates; K-5 service-field/current operators",
        "asset": "K-5 relay/service state; existing outside armed ships/frames; bounded appointment/authority instruments",
        "place": "existing ratification/office setting + K-5 live-service context",
        "delta": "which field a holder can actually exercise or cannot exercise changes",
        "reentry": "E421–430 K-5 operational pressure",
        "veto": "no new claimant, crown relic or battle merely to make the band tangible",
    },
    "GA7 E716–723": {
        "face": "existing operators/signers/witnesses; Haren is a subject/current actor, not the sole answer",
        "asset": "existing D4/signature/command records and custody chain",
        "place": "preceding route/service failure locations + existing evidence-custody spaces",
        "delta": "212 records narrow from one-person legend toward layered responsibility",
        "reentry": "E698–715 lost cargo/ships/people",
        "veto": "do not turn document counts into lore-only exposition and do not add a secret mastermind",
    },
    "GA7 E776–783": {
        "face": "Haren; affected-region/victim actors; saved-core beneficiaries; Lin-related current claimants/records",
        "asset": "Lin's existing ledgers/evidence; compensation/service/route records",
        "place": "current service/recovery/hearing environments already supported",
        "delta": "sanction, access, role, restitution and model-governance alter current function",
        "reentry": "E746–765 Haren/Lin/D4 consequences",
        "veto": "no Lin resurrection, new victim solely for proof, or sentence change",
    },
    "GA7 E784–790": {
        "face": "existing federation/local/affected delegates and operators",
        "asset": "existing residual-duty reserve; route/mission resources; ships/cargo/crew time already in state design",
        "place": "current federation/route operating environment",
        "delta": "reserved capacity or field separation makes other missions unavailable before E790 live risk",
        "reentry": "D4 postmortem + First Bridge preparation",
        "veto": "do not render the eight fields as a UI skill tree",
    },
    "GA8 E836–843": {
        "face": "Serrat living parties, AI communities, custodians, descendants and translators",
        "asset": "existing 20,960 disputed governance/founding corpus and current access/custody states",
        "place": "Serrat habitats and already-defined disputed physical spaces",
        "delta": "translation/legal effect changes current access, service or custody",
        "reentry": "E823 physical return + E833/E834 service/space conflict",
        "veto": "no sacred archive object or one true founding document",
    },
    "GA8 E851–860": {
        "face": "existing Palimpsest maintainers, translators, archive/service operators and AI/community actors",
        "asset": "existing Seed object corpus + old service/authority systems supported by atlas/bibles",
        "place": "Palimpsest inhabited service sites / Continuity Assembly environments",
        "delta": "Seed layer separation changes what can observe, rank, credential or enforce",
        "reentry": "Palimpsest 'Archive Is A Profession' identity",
        "veto": "no ancient supercomputer room, hidden master AI or new ancient race",
    },
    "GA8 E861–868": {
        "face": "caregivers; current unregistered/mobile people; AI forks/communities; language practitioners; nonstandard-tech workers; Rian is one of 43",
        "asset": "existing care/service/identity/repair records and systems",
        "place": "same Serrat/Palimpsest current workplaces and services",
        "delta": "omission fields, current corrections and succession redundancy become actionable",
        "reentry": "E851–860 Seed findings",
        "veto": "no five new case-of-week protagonists and no Rian chosen-one staging",
    },
    "GA9 E926–935": {
        "face": "recurring mobile settlement cluster; plural AI/mixed households; nonstandard care/engineering actors; outsider-linked crews",
        "asset": "route slots; current-standing/identity proofs; insurance/repair access; clinic/technology service assets",
        "place": "same settlement/route/yard/clinic chain",
        "delta": "one low-continuity profile cumulatively closes multiple service doors",
        "reentry": "E901–925 Perfect Route benefits",
        "veto": "do not introduce a different victim-protagonist for every domain",
    },
    "GA9 E936–943": {
        "face": "same affected actors + Current Standing/Diversity representatives",
        "asset": "current-standing warrants; existing clinic component/safety evidence; parallel-lane ships/guarantees",
        "place": "clinic + repair/insurance environment + parallel route",
        "delta": "minimum service reopens while some limits remain; outside lane stays slower/costlier",
        "reentry": "E926–935 same six-door chain",
        "veto": "do not turn the warrant into a magical identity item",
    },
}


def exact(card, *names, max_items=4, limit_each=700):
    return base.vals(card, *names, max_items=max_items, limit_each=limit_each)


def fuzzy(card, terms, *, exclude=(), max_items=4, limit_each=700):
    out = []
    for key, values in card.fields.items():
        kl = key.lower()
        if not any(term in kl for term in terms):
            continue
        if any(term in kl for term in exclude):
            continue
        for value in values:
            value = base.shorten(value, limit_each)
            if value and value not in out:
                out.append(value)
            if len(out) >= max_items:
                return out
    return out


def pick(card, exact_names, fuzzy_terms=(), *, max_items=4, limit_each=700, exclude=()):
    out = exact(card, *exact_names, max_items=max_items, limit_each=limit_each)
    if len(out) < max_items and fuzzy_terms:
        for value in fuzzy(card, fuzzy_terms, exclude=exclude, max_items=max_items, limit_each=limit_each):
            if value not in out:
                out.append(value)
            if len(out) >= max_items:
                break
    return out


def one(card, exact_names, fuzzy_terms=(), *, default="UNRESOLVED FROM APPROVED SOURCES"):
    vals = pick(card, exact_names, fuzzy_terms, max_items=1)
    return vals[0] if vals else default


def normalized(card):
    main = one(card,
               ("visible goal", "goal", "objective", "purpose", "mission goal"),
               ("goal", "objective", "purpose"))

    secondary_items = pick(card,
                           ("hidden pressure", "secondary pressure", "obstacle", "pressure", "conflict", "opposition"),
                           ("hidden pressure", "secondary pressure", "obstacle", "conflict", "opposition"),
                           max_items=2)
    secondary = secondary_items[0] if secondary_items else "NONE — no separate competing desire/pressure is explicitly stored in the source card"

    opening = pick(card,
                   ("opening state", "physical state", "physical setup", "physical reality", "current state", "starting state"),
                   ("opening state", "physical state", "physical setup", "physical reality", "current state", "starting state"),
                   max_items=2)
    places = pick(card,
                  ("location/time", "location / time", "location", "place"),
                  ("location", "place"), max_items=3, limit_each=450)
    evidence = pick(card,
                    ("finding", "findings", "case", "evidence", "document corpus", "usable corpus", "results", "physical finding", "current population/service claim", "current outer front force"),
                    ("finding", "evidence", "case", "corpus", "result", "record", "document", "physical"),
                    exclude=("resulting",), max_items=3, limit_each=600)
    anchor = []
    for value in opening + places + evidence:
        if value not in anchor:
            anchor.append(value)
        if len(anchor) >= 5:
            break

    changes = pick(card,
                   ("state change", "immediate result", "immediate outcome", "result", "outcome", "end state", "carried state", "decision", "reward"),
                   ("state change", "immediate result", "immediate outcome", "outcome", "end state", "carried state", "decision", "reward"),
                   max_items=5)

    costs = pick(card,
                 ("cost", "cost/loss/debt", "loss", "debt", "damage", "refusal", "opposition"),
                 ("cost", "loss", "debt", "damage", "refusal", "opposition"),
                 max_items=4)

    reentry = pick(card,
                   ("carried state", "final hook", "end hook", "hook", "next state", "downstream"),
                   ("carried", "hook", "downstream", "next"),
                   max_items=3)

    actors = pick(card,
                  ("actors/goals", "actors", "actor goal", "actor goals", "front-stage actor", "active actors", "current actor"),
                  ("actor", "signer", "operator", "witness", "claimant"),
                  exclude=("reactor",), max_items=5)
    if not actors and main != "UNRESOLVED FROM APPROVED SOURCES":
        actors = [f"Goal evidence only; exact acting owner must remain source-bound: {main}"]

    decisions = pick(card,
                     ("decisive choice", "decision", "choice", "ruling", "resolution"),
                     ("decisive choice", "decision", "choice", "ruling", "resolution"),
                     max_items=4)

    info = pick(card,
                ("mystery state", "archive event", "clue", "clues", "finding", "findings", "evidence", "reveal", "results"),
                ("mystery", "clue", "finding", "evidence", "reveal", "result"),
                max_items=4)

    collection = pick(card, ("collection state",), ("collection state",), max_items=3)
    relationship = pick(card,
                        ("relationship/institution state", "relationship state", "institution state", "authority state", "political state"),
                        ("relationship", "institution state", "authority state", "political state"),
                        max_items=3)

    date = one(card, ("date",), ("date",))
    pov = one(card, ("pov / information source", "pov", "viewpoint", "information source"), ("pov", "viewpoint", "information source"))
    specialists = one(card, ("specialist panel",), ("specialist panel",), default="N/A — source card does not store a panel")

    return {
        "main": main, "secondary": secondary, "anchor": anchor, "changes": changes,
        "costs": costs, "reentry": reentry, "actors": actors, "decisions": decisions,
        "info": info, "collection": collection, "relationship": relationship,
        "date": date, "pov": pov, "specialists": specialists,
    }


def render_episode(card):
    n = normalized(card)
    band = base.hw_band(card.episode)
    guide = HIGH_WATCH_GUIDE.get(band) if band else None

    missing = []
    if n["main"].startswith("UNRESOLVED"):
        missing.append("ACTIVE_DESIRE_MAIN exact source label")
    if not n["anchor"]:
        missing.append("PHYSICAL_ANCHOR concrete carrier")
    if not n["changes"]:
        missing.append("STATE_CHANGE approved result/decision evidence")
    if not n["costs"]:
        missing.append("COST_OR_REFUSAL approved cost")
    if not n["reentry"]:
        missing.append("REENTRY_ANCHOR approved carry/hook")

    out = [
        f"## E{card.episode:03d} — {card.title}", "",
        "CONTEXT STATUS: **FULL — SOURCE-BOUND DEEP EXECUTION PACK**",
        f"Source Card: [[{base.source_stem(card)}]]",
        f"Date: {n['date']}",
        f"POV / information source: {n['pov']}",
        f"HIGH_WATCH_BAND: `{band or 'N/A'}`", "",
        "### Common six-field contract", "",
        "**ACTIVE_DESIRE_MAIN**  ", n["main"], "",
        "**ACTIVE_DESIRE_SECONDARY**  ", n["secondary"], "",
        "**PHYSICAL_ANCHOR — approved carrier/evidence**", base.bullets(n["anchor"]), "",
        "**STATE_CHANGE — derived only from approved result/decision/reward fields**", base.bullets(n["changes"]), "",
        "**COST_OR_REFUSAL**", base.bullets(n["costs"]), "",
        "**REENTRY_ANCHOR**", base.bullets(n["reentry"]), "",
        "### Agency / authority", "",
        "**CURRENT_ACTOR_GOAL_EVIDENCE**", base.bullets(n["actors"]), "",
        "**DECISION_EVIDENCE**", base.bullets(n["decisions"]), "",
        "**CURRENT_OWNER_OF_DECISION**  ",
        "Use only the actor/institution explicitly attached to the decisive choice in the source card or higher authority documents. If the card states a decision without naming its legal/physical owner, owner remains `UNRESOLVED FROM APPROVED SOURCES`; the compiler never defaults ownership to Rian.", "",
        "**RIAN_CANNOT_OVERRIDE**  ",
        "Any technical, medical, legal, custody, record, local, affected-party, shipmaster, command or consent authority explicitly owned by another actor/institution in the source card/higher state. Context compilation never migrates that authority to Rian.", "",
        "### Information / payoff ceiling", "",
        "**SOURCE_INFORMATION_EVIDENCE**", base.bullets(n["info"], unresolved=False), "",
        "Formal mystery/clue/payoff accounting follows the highest locked ledger. Source-card findings remain literally available, but a lower tag/open plant window cannot be promoted into an earlier explanatory reveal by this Context Pack.", "",
        "### Carry ledgers", "",
        "**COLLECTION_STATE**", base.bullets(n["collection"], unresolved=False), "",
        "**RELATIONSHIP_OR_INSTITUTION_STATE**", base.bullets(n["relationship"], unresolved=False), "",
        f"**SPECIALIST_PANEL / SOURCE CHECK:** {n['specialists']}", "",
        "### Unsupported exacts / source-precedence guard", "",
    ]

    if missing:
        out += [
            "These execution details are not explicit enough in the parsed source. They remain unresolved rather than being invented:",
            *[f"- {m}: `UNRESOLVED FROM APPROVED SOURCES`" for m in missing],
        ]
    else:
        out.append("All mandatory execution slots have approved source evidence. Prose-level exact numbers/names/layouts absent from higher sources still remain `UNRESOLVED FROM APPROVED SOURCES`.")

    out += ["", "`NEW_CANON_REQUIRED: NO`", ""]

    if guide:
        out += [
            "### HIGH-WATCH addendum — existing carrier matrix overlay", "",
            f"Matrix source: [[high-watch-tangible-carrier-matrix-ga4-ga7-ga8-ga9-v1]] — execution lens only; no canon promotion.", "",
            f"**RECURRING_FACE:** {guide['face']}", "",
            f"**RECURRING_ASSET:** {guide['asset']}", "",
            f"**RECURRING_PLACE:** {guide['place']}", "",
            f"**VISIBLE_DELTA_GUARD:** {guide['delta']}", "",
            f"**PREVIOUS_REENTRY_ANCHOR:** {guide['reentry']}", "",
            f"**HARD_VETO:** {guide['veto']}", "",
            "**CURRENT_OWNER_OF_DECISION:** use this episode's source decision owner; the band carrier list never grants new authority.", "",
            "**RIAN_CANNOT_OVERRIDE:** affected-party/local/service/legal/technical/medical/record/command ownership already present in the source and matrix; Rian remains one participant where specified.", "",
            "**ABSTRACT_CONCEPTS_FOREGROUNDED:** foreground no more than the 1–2 concepts needed to understand the current carrier consequence before widening.", "",
            "`NEW_CANON_REQUIRED: NO`", "",
        ]

    out += [
        "### Context readiness", "",
        "`CONTEXT READY: YES — source-bound execution layer only`", "",
        "This readiness does **not** authorize manuscript drafting, AUTHOR-APPROVED status, publication or canon mutation.", "",
        "---", "",
    ]
    return "\n".join(out)


def structural_audit(cards):
    stats = defaultdict(int)
    hw_stats = defaultdict(int)
    examples = defaultdict(list)
    for ep, card in sorted(cards.items()):
        n = normalized(card)
        checks = {
            "main_desire_unresolved": n["main"].startswith("UNRESOLVED"),
            "anchor_unresolved": not n["anchor"],
            "state_change_unresolved": not n["changes"],
            "cost_unresolved": not n["costs"],
            "reentry_unresolved": not n["reentry"],
        }
        for key, failed in checks.items():
            if failed:
                stats[key] += 1
                if len(examples[key]) < 20:
                    examples[key].append(ep)
                if base.hw_band(ep):
                    hw_stats[key] += 1

    lines = [
        "# Full-Series Context Pack Structural Audit v2 — Deep Schema Normalization", "",
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
        "- story facts generated by builder: **NO**", "",
        "## Mandatory execution-field diagnostics", "",
    ]
    labels = [
        ("main_desire_unresolved", "ACTIVE_DESIRE_MAIN"),
        ("anchor_unresolved", "PHYSICAL_ANCHOR"),
        ("state_change_unresolved", "STATE_CHANGE"),
        ("cost_unresolved", "COST_OR_REFUSAL"),
        ("reentry_unresolved", "REENTRY_ANCHOR"),
    ]
    for key, label in labels:
        sample = ", ".join(f"E{x}" for x in examples[key]) if examples[key] else "NONE"
        lines.append(f"- {label} unresolved: **{stats[key]}**; HIGH-WATCH unresolved: **{hw_stats[key]}**; first examples: {sample}")

    lines += [
        "", "Interpretation:",
        "- a zero is preferred but not achieved by invention;",
        "- `NONE` is valid for ACTIVE_DESIRE_SECONDARY;",
        "- any remaining unresolved mandatory field is a semantic review target, not permission for generated lore;",
        "- HIGH-WATCH carrier families come from the existing carrier matrix and remain execution/QC guidance only.",
        "", "## Hard fail / anti-fake-completeness rules", "",
        "1. any missing or duplicate E011–E1100 source owner hard-fails generation;",
        "2. E001–E010 manually audited Context remains the effective override;",
        "3. no manuscript is read as a story-fact source;",
        "4. no unresolved field is silently filled by an LLM-style guess;",
        "5. full-series completion still requires semantic GA/cross-GA blindspot review after machine coverage.",
    ]
    return "\n".join(lines) + "\n"


# Patch only rendering/audit. Source discovery and gap/duplicate hard-fails remain
# owned by the base builder.
base.render_episode = render_episode
base.structural_audit = structural_audit


def build_outputs():
    return base.build_outputs()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    try:
        outputs = build_outputs()
    except Exception as exc:
        print(f"DEEP CONTEXT BUILD ERROR: {exc}", file=sys.stderr)
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
        print("Deep Context outputs are stale/missing:")
        for path in changed:
            print(f"  {path.relative_to(ROOT).as_posix()}")
        return 1

    print("Deep full-series Context outputs generated/checked")
    for path in outputs:
        print(f"  {path.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
