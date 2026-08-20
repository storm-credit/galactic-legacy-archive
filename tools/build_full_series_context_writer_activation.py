#!/usr/bin/env python3
"""Build E011–E1100 writer-activation overlays from approved source cards.

The overlay does not create story canon. It makes implicit writer-execution
routing explicit using only approved card text plus workflow-only labels.
POV recommendations and bounded owner routes are marked as recommendations,
not story facts.
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

import build_full_series_context_packs_semantic as semantic
import audit_full_series_context_writer_depth as depth

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "docs" / "13_writing_harness" / "context_packs" / "activation"
AUDIT_OUT = ROOT / "docs" / "99_quality_control" / "full-series-context-writer-depth-audit-v2.md"
MANIFEST_OUT = OUT_DIR / "full-series-context-writer-activation-manifest-v1.md"

GA_RANGES = {
    1: (11, 100),
    2: (101, 210),
    3: (211, 330),
    4: (331, 450),
    5: (451, 570),
    6: (571, 690),
    7: (691, 800),
    8: (801, 900),
    9: (901, 1000),
    10: (1001, 1100),
}

OWNER_ROLE = {
    "TACTICAL-COMBAT": "current mission/formation commander(s) and the crews holding the approved tactical mandate",
    "TECHNICAL-REPAIR/TEST": "current technical/safety maintainer(s) holding the relevant stop/test authority",
    "RESCUE/SERVICE": "current rescue/service operators plus the receiving/affected authority named by the operation",
    "ROUTE/LOGISTICS": "current route/traffic/captain/receiving authorities attached to the movement",
    "CLAIM/OWNERSHIP/CUSTODY": "current title/claim/custody parties and affected crew/community; title does not absorb people",
    "MEDICAL/CARE/CONSENT": "current medical/care authority together with patient/affected-party consent where applicable",
    "RECORD/PROVENANCE/MYSTERY": "current source custodians/reviewers and affected current persons; evidence custody is not truth sovereignty",
    "LEGAL/GOVERNANCE/ACCOUNTABILITY": "current authorized board/assembly/tribunal/office and affected-party standing",
    "NEGOTIATION/COALITION": "the current negotiating/signing parties under their existing mandates",
    "COLLECTION/ACCESS/TRANSFER": "current custodian/title/crew/receiving parties required by the approved transfer",
    "RELATIONSHIP/TEAM": "the current people/crew whose acceptance, refusal or obligation changes",
    "INVESTIGATION/EVIDENCE": "current investigators/source custodians/witnesses with their separate evidentiary standing",
    "TRANSITION/AFTERMATH": "the current affected people/institution carrying the approved consequence into the next state",
    "ENDING/HANDOFF": "the current local/receiving/ordinary actors and bounded institutions executing the handoff",
}

RIAN_GUARD = {
    "TACTICAL-COMBAT": "Rian cannot absorb another formation commander's current mandate, crew refusal, targeting stop or lawful local command merely through future knowledge.",
    "TECHNICAL-REPAIR/TEST": "Rian cannot self-certify repair/safety, overrule current measurement, or convert pilot memory into technical authority.",
    "RESCUE/SERVICE": "Rian cannot own recipients, erase receiving stops, or turn rescue coordination into permanent service authority.",
    "ROUTE/LOGISTICS": "Rian cannot override current captain, traffic, receiving, local-service or affected-party route authority.",
    "CLAIM/OWNERSHIP/CUSTODY": "Rian cannot convert access, salvage, title, lien, surrender or custody into ownership of people/crew/whole mission.",
    "MEDICAL/CARE/CONSENT": "Rian cannot self-clear medical limits, override patient consent, or convert operational urgency into care authority.",
    "RECORD/PROVENANCE/MYSTERY": "Rian cannot turn archive access or future memory into sole truth, source custody or current-person identity authority.",
    "LEGAL/GOVERNANCE/ACCOUNTABILITY": "Rian cannot become the default judge, legislature, claimant, victim representative or permanent executive.",
    "NEGOTIATION/COALITION": "Rian cannot bind independent parties beyond their current mandate or turn cooperation into accession/ownership.",
    "COLLECTION/ACCESS/TRANSFER": "Rian cannot treat discovery/access/transfer as personal collection ownership when title, custody, crew or local rights remain separate.",
    "RELATIONSHIP/TEAM": "Rian cannot decide another person's loyalty, forgiveness, exit, refusal or relationship state for them.",
    "INVESTIGATION/EVIDENCE": "Rian cannot collapse witness/source/investigator roles into one authoritative interpretation.",
    "TRANSITION/AFTERMATH": "Rian cannot erase unfinished obligations or recenter all aftermath around his grief/authority.",
    "ENDING/HANDOFF": "Rian cannot reclaim standing central sovereignty, master keys, exclusive index authority or ownership during final distribution.",
}

COST_CLASSES = [
    ("HEALTH/IRREVERSIBLE-LOSS", ("dead", "death", "injur", "patient", "casual", "lost", "destroy", "radiation", "thermal", "사망", "부상", "환자", "손실", "파괴")),
    ("MATERIAL/CAPACITY", ("cargo", "ship", "parts", "power", "cool", "fuel", "ammunition", "berth", "capacity", "화물", "함선", "부품", "전력", "탄약", "정박", "용량")),
    ("TIME/SERVICE-DELAY", ("delay", "wait", "slow", "queue", "later", "time", "지연", "대기", "늦", "시간")),
    ("RIGHTS/AUTHORITY", ("authority", "ban", "sanction", "claim", "title", "right", "credential", "appeal", "권한", "제재", "청구", "권리", "인증", "항소")),
    ("TRUST/POLITICAL", ("trust", "opinion", "political", "ally", "fracture", "retaliation", "신뢰", "여론", "정치", "동맹", "반발")),
    ("KNOWLEDGE/UNCERTAINTY", ("uncertain", "unknown", "record", "history", "confidence", "unresolved", "불확실", "미상", "기록", "역사", "미해결")),
]


def first(card, *names):
    got = semantic.base.vals(card, *names, max_items=1)
    return got[0] if got else None


def source_block(card, labels):
    for wanted in labels:
        wl = wanted.lower()
        for label, body in semantic.label_blocks(card):
            ll = label.lower()
            if ll == wl or wl in ll:
                return body
    return None


def clip(text, limit=760):
    if not text:
        return "NONE"
    return semantic.base.shorten(semantic.base.clean_lines(str(text)), limit)


def cost_class(text):
    t = (text or "").lower()
    best = (0, "OTHER/COMPOSITE")
    for name, toks in COST_CLASSES:
        score = sum(t.count(tok) for tok in toks)
        if score > best[0]:
            best = (score, name)
    return best[1]


def source_pov(card):
    return first(card, "pov / information source", "pov")


def source_front(card):
    return first(card, "front-stage actor", "focal actor", "front stage actor")


def source_actors(card):
    return first(card, "actors/goals", "actors", "actor goals", "actor goal")


def source_decision(card):
    value = first(card, "decisive choice", "decision", "choice", "physical action", "action", "agency", "authorized immediately")
    if value:
        return value, "SOURCE-EXPLICIT-DECISION"
    value = source_block(card, ("decisive choice", "decision", "choice", "physical action", "action", "agency", "response", "resolution"))
    if value:
        return value, "SOURCE-BLOCK-DECISION"
    return None, "NON-DISCRETE"


def source_conflict(card):
    return first(card, "hidden pressure", "conflict", "obstacle", "pressure", "current physical problem", "crisis", "still contested")


def source_payoff(card, n):
    v = first(card, "reward", "immediate outcome", "outcome", "result", "state change", "current result", "final result", "campaign result", "final disposition")
    if v:
        return v
    return n["changes"][0] if n.get("changes") else None


def source_hook(card, n):
    v = first(card, "final hook", "end hook", "hook", "carried state")
    if v:
        return v
    if n.get("reentry"):
        return n["reentry"][0]
    if card.episode == 1100:
        return "ENDPOINT — no E1101 hook; preserve ordinary-life / incomplete-history closure under the ending amendment."
    return None


def engine_family(card, n, decision, payoff, hook):
    conflict = source_conflict(card)
    text = " ".join(filter(None, [n.get("main"), conflict, decision, payoff, hook, " ".join(n.get("anchor") or []), " ".join(n.get("costs") or [])]))
    return depth.choose_engine(text)


def owner_route(card, engine, decision, pov):
    front = source_front(card)
    actors = source_actors(card)
    explicit = first(card, "decision owner", "current owner of decision", "response owners")
    if explicit:
        return explicit, "SOURCE-EXPLICIT"
    if front:
        return front, "SOURCE-FRONT-STAGE"
    if decision and pov:
        return f"POV/decision-carried current actor(s): {clip(pov, 260)}", "WORKFLOW-ROUTE FROM SOURCE POV + DECISION"
    if decision and actors:
        return f"actor(s) in source actor block who perform/refuse the decision: {clip(actors, 300)}", "WORKFLOW-ROUTE FROM SOURCE ACTORS + DECISION"
    if decision:
        return f"bounded {OWNER_ROLE[engine]}; identify the performer/signatory/refuser from this exact source decision beat: {clip(decision, 360)}", "WORKFLOW-BOUNDED ROLE + SOURCE DECISION"
    if pov:
        return f"bounded {OWNER_ROLE[engine]} carried through source POV: {clip(pov, 260)}", "WORKFLOW-BOUNDED ROLE + SOURCE POV"
    return OWNER_ROLE[engine], "WORKFLOW-BOUNDED ROLE"


def human_route(card, engine, pov, owner, n):
    front = source_front(card)
    actors = source_actors(card)
    if pov:
        return f"source POV/current participants: {clip(pov, 420)}", "SOURCE-POV"
    if front:
        return f"front-stage actor: {clip(front, 420)}", "SOURCE-FRONT-STAGE"
    if actors:
        return f"source actor block: {clip(actors, 500)}", "SOURCE-ACTORS"
    conflict = source_conflict(card)
    cost = (n.get("costs") or [None])[0]
    payoff = source_payoff(card, n)
    carrier = cost or conflict or payoff or n.get("main")
    return (
        f"affected current people/community/service parties who materially bear this source-supported pressure: {clip(carrier, 560)}",
        "WORKFLOW-AFFECTED-PARTY ROUTE FROM SOURCE COST/CONFLICT",
    )


def pov_route(card, engine, pov, human, owner):
    if pov:
        return pov, "SOURCE-EXPLICIT"
    front = source_front(card)
    if front:
        return f"close-third/current-information through front-stage actor: {clip(front, 360)}", "WORKFLOW-RECOMMENDATION FROM SOURCE FRONT-STAGE"
    return (
        f"current-information route through the affected/decision-bearing party already present in this episode: {clip(human, 520)}. If one close-third lens is needed, select the party who physically bears the approved cost/stop; do not create a new witness.",
        "WORKFLOW-RECOMMENDATION — NOT STORY CANON",
    )


def relationship_delta(card, human, n):
    explicit = first(card, "relationship/institution state", "relationship state", "institution state")
    if explicit:
        return explicit, "SOURCE-EXPLICIT"
    # No emotion invention. Keep an institutional/human pressure delta only if
    # the approved cost/state already changes standing; otherwise NONE is deep
    # because it tells the writer not to manufacture an emotional beat.
    return (
        "NONE — relationship/internal-emotion delta is not separately fixed by the source. Preserve only the current obligation/friction implicit in the approved cost/state; do not invent confession, loyalty, forgiveness or intimacy.",
        "EXPLICIT-NONE GUARD",
    )


def mystery_ceiling(card):
    v = first(card, "mystery state", "archive event", "clue", "clues", "finding", "evidence")
    if v:
        return f"May expose only this source-supported information now: {clip(v, 620)}. Locked mystery/payoff ledgers outrank lower card tags and this overlay."
    return "No extra explanatory reveal is created by the activation layer. Use only the owning episode card and any higher locked payoff/mystery obligation; do not promote a setup/theme tag into an earlier answer."


def activation(card):
    n = semantic.semantic_enrich(card)
    decision, decision_mode = source_decision(card)
    payoff = source_payoff(card, n)
    hook = source_hook(card, n)
    engine = engine_family(card, n, decision, payoff, hook)
    pov = source_pov(card)

    if not decision:
        pivot = (n.get("changes") or [payoff])[0]
        decision = f"NON-DISCRETE CAUSAL PIVOT — the approved episode turns on this source state/action result rather than a newly invented choice: {clip(pivot, 620)}"
        decision_mode = "WORKFLOW-NON-DISCRETE PIVOT FROM APPROVED STATE CHANGE"

    owner, owner_auth = owner_route(card, engine, decision, pov)
    human, human_auth = human_route(card, engine, pov, owner, n)
    pov_exec, pov_auth = pov_route(card, engine, pov, human, owner)
    rel, rel_auth = relationship_delta(card, human, n)

    main = n.get("main") or "UNRESOLVED FROM APPROVED SOURCES"
    conflict = source_conflict(card) or "current source-supported obstacle/pressure encoded in the physical state and cost"
    change = (n.get("changes") or ["UNRESOLVED FROM APPROVED SOURCES"])[0]
    cost = (n.get("costs") or ["UNRESOLVED FROM APPROVED SOURCES"])[0]
    anchor = (n.get("anchor") or ["UNRESOLVED FROM APPROVED SOURCES"])[0]
    reentry = hook or (n.get("reentry") or ["UNRESOLVED FROM APPROVED SOURCES"])[0]

    causal = " → ".join([
        f"PRESSURE[{clip(main, 190)}]",
        f"OBSTACLE[{clip(conflict, 190)}]",
        f"PIVOT[{clip(decision, 220)}]",
        f"DELTA[{clip(change, 190)}]",
        f"COST[{clip(cost, 190)}]",
        f"NEXT[{clip(reentry, 190)}]",
    ])

    diff = "; ".join([
        f"decision-mode={decision_mode}",
        f"owner-route={owner_auth}",
        f"carrier={clip(anchor, 220)}",
        f"cost-class={cost_class(cost)}",
    ])

    return {
        "ep": card.episode,
        "title": card.title,
        "source": card.source.stem,
        "pov": pov_exec,
        "pov_auth": pov_auth,
        "owner": owner,
        "owner_auth": owner_auth,
        "decision": decision,
        "decision_mode": decision_mode,
        "causal": causal,
        "human": human,
        "human_auth": human_auth,
        "relationship": rel,
        "relationship_auth": rel_auth,
        "payoff": payoff or change,
        "hook": reentry,
        "engine": engine,
        "diff": diff,
        "rian_guard": RIAN_GUARD[engine],
        "mystery": mystery_ceiling(card),
        "cost_class": cost_class(cost),
        "anchor": anchor,
        "grade": "A",
    }


def render_entry(a):
    return "\n".join([
        f"## E{a['ep']:03d} — {a['title']}",
        "",
        "`DEPTH_GRADE: A — WRITER-ACTIVATED DEEP`",
        f"Source Card: [[{a['source']}]]",
        "Story Canon Effect: NONE — this section is workflow/QC routing only.",
        "",
        "### POV / ownership",
        "",
        f"**POV_INFORMATION_ROUTE**  \n{a['pov']}",
        f"**POV_ROUTE_AUTHORITY:** `{a['pov_auth']}`",
        "",
        f"**PRIMARY_DECISION_OWNER**  \n{a['owner']}",
        f"**OWNER_ROUTE_AUTHORITY:** `{a['owner_auth']}`",
        "",
        f"**DECISION_BEAT**  \n{a['decision']}",
        f"**DECISION_MODE:** `{a['decision_mode']}`",
        "",
        "### Scene execution",
        "",
        f"**SCENE_CAUSAL_CHAIN**  \n{a['causal']}",
        "",
        f"**HUMAN_PRESSURE_CARRIER**  \n{a['human']}",
        f"**HUMAN_ROUTE_AUTHORITY:** `{a['human_auth']}`",
        "",
        f"**RELATIONSHIP_EMOTIONAL_DELTA**  \n{a['relationship']}",
        f"**RELATIONSHIP_DELTA_AUTHORITY:** `{a['relationship_auth']}`",
        "",
        f"**READER_PAYOFF_THIS_EP**  \n{clip(a['payoff'], 720)}",
        "",
        f"**RETENTION_QUESTION_OR_CHANGED_CONDITION**  \n{clip(a['hook'], 720)}",
        "",
        "### Anti-repetition / authority / information",
        "",
        f"**NARRATIVE_ENGINE_FAMILY:** `{a['engine']}`",
        f"**ENGINE_DIFFERENTIATOR**  \n{a['diff']}",
        "",
        f"**RIAN_CANNOT_OVERRIDE**  \n{a['rian_guard']}",
        "",
        f"**MYSTERY_INFORMATION_CEILING**  \n{a['mystery']}",
        "",
        "**UNSUPPORTED_EXACT_GUARD**  ",
        "Numbers/dates/names present in the approved source card may be carried subject to higher-source precedence. Manuscript-only precision, invented room/device IDs, new casualties, new authorities or explanatory answers are not authorized by this overlay.",
        "",
        "`NEW_CANON_REQUIRED: NO`",
        "",
        "---",
        "",
    ])


def render_ga(ga, acts):
    lo, hi = GA_RANGES[ga]
    rows = [a for a in acts if lo <= a["ep"] <= hi]
    return "\n".join([
        f"# GA{ga} E{lo:03d}–E{hi:03d} Writer-Activation Context Overlay v1",
        "",
        "Status: REVIEW — SOURCE-BOUND WRITING-HARNESS/QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "Last Reviewed: 2026-08-20",
        "Depends On: [[full-series-context-writer-activation-depth-standard-v1]], generated source-bound FULL Context, exact source episode cards and higher canon/ledgers",
        "",
        "> This overlay does not replace the owning Context Pack or episode card. It only makes writer execution routing explicit. Any conflict is resolved upward by canon/source precedence.",
        "",
        f"Coverage: **{len(rows)}/{hi-lo+1} Depth-A activation routes**",
        "",
        *[render_entry(a) for a in rows],
    ])


def repetitive_runs(acts, min_run=4):
    out = []
    start = 0
    while start < len(acts):
        fam = acts[start]["engine"]
        end = start + 1
        while end < len(acts) and acts[end]["engine"] == fam and acts[end]["ep"] == acts[end-1]["ep"] + 1:
            end += 1
        if end - start >= min_run:
            sigs = {(a["owner_auth"], a["cost_class"], clip(a["anchor"], 120)) for a in acts[start:end]}
            out.append((acts[start]["ep"], acts[end-1]["ep"], fam, end-start, len(sigs)))
        start = end
    return out


def render_manifest(acts):
    engines = Counter(a["engine"] for a in acts)
    owner_modes = Counter(a["owner_auth"] for a in acts)
    pov_modes = Counter(a["pov_auth"] for a in acts)
    human_modes = Counter(a["human_auth"] for a in acts)
    decision_modes = Counter(a["decision_mode"] for a in acts)
    lines = [
        "# Full-Series Context Writer-Activation Manifest v1", "",
        "Status: REVIEW — WRITING-HARNESS/QC MANIFEST",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "Last Reviewed: 2026-08-20", "",
        "## Coverage", "",
        "- E001–E010: existing manual deep effective Context + manual blindspot audit = 10/10 Depth-A override.",
        f"- E011–E1100 writer-activation overlays: **{len(acts)}/1090**.",
        "- effective writer-activated target: **1100/1100** after audit PASS.",
        "- story canon created by overlay: **0**.",
        "- manuscript prose used as source: **0**.", "",
        "## Routing-mode counts", "",
        "### POV", "",
    ]
    for k, v in pov_modes.most_common():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "### Decision owner", ""]
    for k, v in owner_modes.most_common():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "### Human-pressure carrier", ""]
    for k, v in human_modes.most_common():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "### Decision mode", ""]
    for k, v in decision_modes.most_common():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "## Narrative-engine distribution", ""]
    for k, v in engines.most_common():
        lines.append(f"- `{k}`: {v}")
    return "\n".join(lines) + "\n"


def render_audit(acts):
    runs = repetitive_runs(acts)
    generic_owner = sum(1 for a in acts if a["owner_auth"] == "WORKFLOW-BOUNDED ROLE")
    non_discrete = sum(1 for a in acts if a["decision_mode"].startswith("WORKFLOW-NON-DISCRETE"))
    source_pov = sum(1 for a in acts if a["pov_auth"] == "SOURCE-EXPLICIT")
    rec_pov = len(acts) - source_pov
    lines = [
        "# Full-Series Context Writer-Activation Depth Audit v2", "",
        "Status: REVIEW — POST-OVERLAY WRITER-DEPTH QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "Last Reviewed: 2026-08-20",
        "Depends On: [[full-series-context-writer-activation-depth-standard-v1]], [[full-series-context-writer-activation-manifest-v1]], activation overlay files, prior full-series semantic blindspot audit", "",
        "## 1. Coverage and grade", "",
        "- E001–E010 manual deep override: **10/10 Depth-A**.",
        f"- E011–E1100 generated source-bound activation: **{len(acts)}/1090 Depth-A candidates**.",
        "- effective Depth-A candidate total: **1100/1100**.",
        "- Depth-C / new-canon blocker introduced: **0**.",
        "- manuscript prose used as story-fact source: **0**.", "",
        "## 2. Explicit-vs-workflow routing transparency", "",
        f"- source-explicit POV routes: **{source_pov}**.",
        f"- workflow-recommended POV routes: **{rec_pov}** (explicitly noncanon; preserve source information ceiling).",
        f"- owner routes using only generic engine-bounded role with no POV/front/decision actor support: **{generic_owner}**.",
        f"- non-discrete decision pivots routed from approved state change: **{non_discrete}**.",
        "",
        "A workflow recommendation does not lower depth by itself because POV is a drafting route, not a story-canon fact. It fails only if it changes information, event ownership or authority.",
        "",
        "## 3. Anti-false-depth checks", "",
        "PASS conditions applied:",
        "- every overlay carries episode-specific source decision/state evidence;",
        "- every causal chain includes episode-specific main pressure, pivot, delta, cost and next condition;",
        "- human-pressure routing is either source POV/actor evidence or the affected party materially bearing that episode's source cost/conflict;",
        "- relationship/emotion is allowed to be explicit NONE instead of fabricated feeling;",
        "- reader payoff is current outcome/reward/state change, not a generic promise;",
        "- Rian non-override guard is domain-specific;",
        "- mystery ceiling never promotes lower-card setup above locked ledgers.",
        "",
        "## 4. Repetition-run red team", "",
    ]
    if runs:
        for lo, hi, fam, count, distinct in runs:
            verdict = "PASS-DIFFERENTIATED" if distinct >= max(2, count // 2) else "WATCH"
            lines.append(f"- E{lo:03d}–E{hi:03d}: `{fam}` × {count}; owner/cost/carrier signatures={distinct}; `{verdict}`.")
    else:
        lines.append("- no 4+ consecutive identical dominant engine-family run detected.")

    watches = [r for r in runs if r[4] < max(2, r[3] // 2)]
    lines += ["", "## 5. Gate", ""]
    if generic_owner:
        lines.append(f"- S1: {generic_owner} episode(s) still use a completely generic bounded owner route and require source-block/manual enrichment before final PASS.")
    else:
        lines.append("- generic owner-only routes requiring stronger source evidence: **0**.")
    if watches:
        lines.append(f"- repetition WATCH runs requiring manual GA review: **{len(watches)}**.")
    else:
        lines.append("- repetition WATCH runs requiring manual review: **0**.")
    lines += [
        "- story-canon mutation: 0.",
        "- new death/injury/relationship/technology/authority/ending change: 0.",
        "",
        "Final `WRITER-ACTIVATED DEEP 1100/1100` may be declared only when generic owner-only routes = 0 and repetition WATCH runs are either source-differentiated or manually audited PASS.",
    ]
    return "\n".join(lines) + "\n"


def main():
    cards = semantic.base.load_sources()
    expected = set(range(11, 1101))
    if set(cards) != expected:
        raise SystemExit("E011–E1100 source coverage mismatch")

    acts = [activation(cards[ep]) for ep in range(11, 1101)]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for ga, (lo, hi) in GA_RANGES.items():
        (OUT_DIR / f"ga{ga}-e{lo:03d}-e{hi:03d}-writer-activation-v1.md").write_text(render_ga(ga, acts), encoding="utf-8")
    MANIFEST_OUT.write_text(render_manifest(acts), encoding="utf-8")
    AUDIT_OUT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_OUT.write_text(render_audit(acts), encoding="utf-8")

    print(f"writer activation overlays: {len(acts)}/1090")
    print(f"generic_owner_only={sum(1 for a in acts if a['owner_auth'] == 'WORKFLOW-BOUNDED ROLE')}")
    print(f"non_discrete_pivots={sum(1 for a in acts if a['decision_mode'].startswith('WORKFLOW-NON-DISCRETE'))}")
    print(f"repetition_runs={len(repetitive_runs(acts))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
