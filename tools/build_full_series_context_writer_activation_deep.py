#!/usr/bin/env python3
"""Deepen the full-series writer-activation overlay.

This layer fixes false-A failure modes found by manual inspection of the first
activation pass:
- keyword-only engine misclassification in HIGH-WATCH bands;
- abstract cost language being reused as a fake human carrier;
- endpoint routing that obscures the actual ordinary-person carrier.

It still creates no story facts. HIGH-WATCH routing comes from the adopted
carrier guide; all other human routes come from source label blocks or bounded
existing-role routing tied to the exact source decision/cost.
"""

from __future__ import annotations

from collections import Counter

import build_full_series_context_packs_deep as deep
import build_full_series_context_writer_activation as base


HIGH_WATCH_ENGINE = {
    "GA4 E431–438": "LEGAL/GOVERNANCE/ACCOUNTABILITY",
    "GA7 E716–723": "INVESTIGATION/EVIDENCE",
    "GA7 E776–783": "LEGAL/GOVERNANCE/ACCOUNTABILITY",
    "GA7 E784–790": "LEGAL/GOVERNANCE/ACCOUNTABILITY",
    "GA8 E836–843": "RECORD/PROVENANCE/MYSTERY",
    "GA8 E851–860": "RECORD/PROVENANCE/MYSTERY",
    "GA8 E861–868": "RECORD/PROVENANCE/MYSTERY",
    "GA9 E926–935": "RESCUE/SERVICE",
    "GA9 E936–943": "COLLECTION/ACCESS/TRANSFER",
}

HIGH_WATCH_OWNER = {
    "GA4 E431–438": "current ratifying/appointing actors and the holder of each already-separated authority field; no candidate or Rian receives a master-heir bundle",
    "GA7 E716–723": "current signers/witnesses/source custodians/investigators own authentication and evidence handling in their separate roles; Haren is a subject/current actor, not the sole interpretive authority",
    "GA7 E776–783": "Haren owns his authenticated acts/acceptances; affected-party standing and the authorized judgment/sanction body own their distinct decisions; none collapses into Rian",
    "GA7 E784–790": "current federation/local/affected delegates and operators own their separated field decisions and reserve commitments; architecture is not a personal master key",
    "GA8 E836–843": "current Serrat living parties, AI/community actors, custodians, translators and lawful current institutions retain separate source/translation/access/service authority",
    "GA8 E851–860": "current investigation/custody/domain actors classify provenance and choose operational/legal consequences; Seed analysis itself has no decision sovereignty",
    "GA8 E861–868": "current caregivers, identity/service actors, AI/community custodians, language practitioners and nonstandard-technology workers retain their own correction/consent/operation domains",
    "GA9 E926–935": "the recurring affected settlement/household/crew/clinic actors and the current service/insurance/route/repair authorities own each live access decision",
    "GA9 E936–943": "current affected actors plus Current Standing/Diversity, clinic, repair/insurance and parallel-route authorities own the bounded reopening/limit decisions",
}

# Existing-card label families likely to contain a human/current-work carrier.
# These are source blocks, not invented cast.
HUMAN_BLOCK_LABELS = (
    "ordinary person",
    "current action",
    "current proof",
    "independent-current-state proof",
    "independent current state proof",
    "outsider action",
    "regional route assembly",
    "current legal state",
    "haren current legal state",
    "contributor families",
    "current participants",
    "participants",
    "affected parties",
    "affected actors",
    "response owners",
    "operators",
    "actors/goals",
    "actors",
    "front-stage actor",
    "focal actor",
    "current actor",
    "agency",
)

SPECIAL_ENGINE = {
    1096: "TECHNICAL-REPAIR/TEST",
    1097: "RESCUE/SERVICE",
    1098: "RELATIONSHIP/TEAM",
    1099: "NEGOTIATION/COALITION",
    1100: "ENDING/HANDOFF",
}


def source_human_block(card):
    return base.source_block(card, HUMAN_BLOCK_LABELS)


def high_watch_bundle(card, decision):
    band = base.semantic.base.hw_band(card.episode)
    if not band:
        return None
    guide = deep.HIGH_WATCH_GUIDE[band]
    engine = HIGH_WATCH_ENGINE[band]
    human = (
        "adopted HIGH-WATCH recurring face/work carrier — use these already-supported current roles, "
        f"not a newly invented exemplar: {guide['face']}"
    )
    owner = HIGH_WATCH_OWNER[band]
    pov = (
        "WORKFLOW POV recommendation — carry the episode through one of the existing HIGH-WATCH recurring "
        f"faces who physically handles/bears the exact source decision/cost: {guide['face']}. "
        "Do not invent a new named witness and do not treat this recommendation as story canon."
    )
    return {
        "band": band,
        "guide": guide,
        "engine": engine,
        "human": human,
        "human_auth": "ADOPTED-HIGH-WATCH-CARRIER-GUIDE",
        "owner": owner,
        "owner_auth": "ADOPTED-HIGH-WATCH-OWNER-GUARD + SOURCE DECISION",
        "pov": pov,
        "pov_auth": "WORKFLOW-RECOMMENDATION FROM ADOPTED HIGH-WATCH GUIDE — NOT STORY CANON",
    }


def activation_deep(card):
    a = base.activation(card)
    n = base.semantic.semantic_enrich(card)
    decision = a["decision"]

    # 1. HIGH-WATCH: adopted carrier/authority guide outranks keyword heuristics.
    hw = high_watch_bundle(card, decision)
    if hw:
        a["engine"] = hw["engine"]
        a["human"] = hw["human"]
        a["human_auth"] = hw["human_auth"]
        a["owner"] = hw["owner"] + "; exact episode pivot: " + base.clip(decision, 360)
        a["owner_auth"] = hw["owner_auth"]
        if base.source_pov(card):
            a["pov"] = base.source_pov(card)
            a["pov_auth"] = "SOURCE-EXPLICIT"
        else:
            a["pov"] = hw["pov"]
            a["pov_auth"] = hw["pov_auth"]
        a["rian_guard"] = base.RIAN_GUARD[a["engine"]] + " HIGH-WATCH veto: " + hw["guide"]["veto"] + "."

    # 2. Non-HIGH-WATCH without explicit POV/front/actor: prefer any exact human/work
    # block in the owning card before a generic affected-party cost summary.
    elif a["human_auth"] == "WORKFLOW-AFFECTED-PARTY ROUTE FROM SOURCE COST/CONFLICT":
        hblock = source_human_block(card)
        if hblock:
            a["human"] = "source human/current-work carrier block: " + base.clip(hblock, 720)
            a["human_auth"] = "SOURCE HUMAN/WORK BLOCK"
        else:
            # A bounded unnamed role is allowed by the Context standard when the
            # card does not name a focal. Tie it to the exact decision and cost so
            # it cannot become an invented generic witness.
            cost = (n.get("costs") or ["no separate cost line"])[0]
            a["human"] = (
                "writer face target — use an already-present performer/refuser/recipient from this episode's "
                f"bounded decision domain ({a['owner']}); ground that face in the exact source pivot "
                f"[{base.clip(decision, 300)}] and source cost [{base.clip(cost, 260)}]. "
                "Do not create a new named witness merely to supply emotion."
            )
            a["human_auth"] = "WORKFLOW BOUNDED EXISTING-ROLE TARGET + SOURCE DECISION/COST"

        if a["pov_auth"] == "WORKFLOW-RECOMMENDATION — NOT STORY CANON":
            a["pov"] = (
                "WORKFLOW POV recommendation — select the already-present human/work carrier identified below, "
                "prefer the actor who physically performs/refuses the source pivot or bears its immediate cost, "
                f"and reveal only information available through that current role: {base.clip(a['human'], 620)}"
            )
            a["pov_auth"] = "WORKFLOW-RECOMMENDATION FROM SOURCE/BOUNDED EXISTING ROLE — NOT STORY CANON"

    # 3. Endpoint/late epilogue routing: explicit higher-authority ending card shape.
    if card.episode in SPECIAL_ENGINE:
        a["engine"] = SPECIAL_ENGINE[card.episode]
        a["rian_guard"] = base.RIAN_GUARD[a["engine"]]

    if card.episode == 1100:
        ordinary = base.source_block(card, ("ordinary person",))
        rian = base.source_block(card, ("rian final behavior",))
        setting = base.source_block(card, ("setting rule",))
        if ordinary:
            a["human"] = "source-final human carrier: " + base.clip(ordinary, 900)
            a["human_auth"] = "SOURCE-EXPLICIT ORDINARY-PERSON BLOCK / ENDING AMENDMENT"
        a["owner"] = (
            "the ordinary present person owns their current name/refusal/need; the existing local service/care/work "
            "authority owns any domain service action; Rian owns only his own question/listening/help within ordinary rules"
        )
        a["owner_auth"] = "ENDING-CARD EXPLICIT AGENCY SPLIT"
        a["pov"] = (
            "WORKFLOW final-frame route — begin with the ordinary person's present need/action and keep Rian limited "
            "to ordinary records/local experts and asking the person's current name/need. No Archive label, future-rank "
            "query, chosen-one sign or master-history correction. Source evidence: "
            + base.clip((ordinary or "") + " " + (rian or "") + " " + (setting or ""), 1200)
        )
        a["pov_auth"] = "WORKFLOW-RECOMMENDATION FROM AUTHOR-APPROVED ENDING CARD — NOT STORY CANON"
        a["rian_guard"] = (
            "Rian cannot query future importance, label the ordinary person through Archive, own their future, restore "
            "a master history, or reclaim standing central authority. He may only act within ordinary current rules."
        )

    # Recompute differentiator after overrides.
    cost = (n.get("costs") or ["UNRESOLVED FROM APPROVED SOURCES"])[0]
    a["diff"] = "; ".join([
        f"decision-mode={a['decision_mode']}",
        f"owner-route={a['owner_auth']}",
        f"human-route={a['human_auth']}",
        f"carrier={base.clip(a['anchor'], 220)}",
        f"cost-class={base.cost_class(cost)}",
    ])
    return a


def render_strict_audit(acts):
    modes = Counter(a["human_auth"] for a in acts)
    hw = [a for a in acts if base.semantic.base.hw_band(a["ep"])]
    bad_hw = [a for a in hw if a["human_auth"] != "ADOPTED-HIGH-WATCH-CARRIER-GUIDE"]
    abstract_cost_faces = [a for a in acts if a["human_auth"] == "WORKFLOW-AFFECTED-PARTY ROUTE FROM SOURCE COST/CONFLICT"]
    endpoint = next(a for a in acts if a["ep"] == 1100)
    runs = base.repetitive_runs(acts)
    watches = [r for r in runs if r[4] < max(2, r[3] // 2)]
    lines = [
        "# Full-Series Context Writer-Activation False-A Red-Team Audit v1", "",
        "Status: REVIEW — STRICT POST-ACTIVATION RED TEAM",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "Last Reviewed: 2026-08-20", "",
        "## Mechanical anti-fraud gates", "",
        f"- activation entries E011–E1100: **{len(acts)}/1090**",
        f"- legacy abstract-cost-as-human-carrier routes remaining: **{len(abstract_cost_faces)}**",
        f"- HIGH-WATCH entries: **{len(hw)}**",
        f"- HIGH-WATCH entries not using adopted recurring-face guide: **{len(bad_hw)}**",
        f"- repetition runs still heuristically WATCH: **{len(watches)}**",
        "- new story fact required by these repairs: **0**", "",
        "## Human-route modes", "",
    ]
    for mode, count in modes.most_common():
        lines.append(f"- `{mode}`: {count}")
    lines += [
        "", "## Endpoint assertion", "",
        f"- E1100 engine: `{endpoint['engine']}`",
        f"- E1100 human authority: `{endpoint['human_auth']}`",
        f"- E1100 owner authority: `{endpoint['owner_auth']}`",
        "- E1100 rule: ordinary current person/need first; no Archive future label, chosen-one signal, master history or E1101 hook.",
        "", "## Gate", "",
    ]
    if abstract_cost_faces or bad_hw or watches:
        lines.append("**FAIL — false-A/manual-watch conditions remain.**")
    else:
        lines.append("**MACHINE GATE PASS — proceed to representative manual source-vs-overlay red-team before final completion declaration.**")
    return "\n".join(lines) + "\n"


# Patch the original generator so its normal GA files/manifest/audit use the
# stronger activation routing without duplicating the storage implementation.
base.activation = activation_deep


def main():
    rc = base.main()
    if rc:
        return rc
    cards = base.semantic.base.load_sources()
    acts = [activation_deep(cards[ep]) for ep in range(11, 1101)]
    strict = base.ROOT / "docs" / "99_quality_control" / "full-series-context-writer-activation-false-a-redteam-v1.md"
    strict.write_text(render_strict_audit(acts), encoding="utf-8")
    print(f"strict_false_a_audit={strict.relative_to(base.ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
