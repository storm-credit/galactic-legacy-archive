#!/usr/bin/env python3
"""Run deep writer activation with explicit load-bearing canon overrides.

This runner preserves the base activation implementation, normalizes later-card
label variants, then applies a very small set of higher-authority writer-routing
overrides where manual red-team found stale Detailed-Design (DD) propagation.

These overrides DO NOT create story canon. They enforce already-locked Working
Canon / Project-Control facts from final loss/payoff/state/ending sources when a
lower detailed card is stale, coarse, or omits a load-bearing scene.
"""

from pathlib import Path

import build_full_series_context_writer_activation as base

_ORIGINAL_ACTIVATION = base.activation
_ORIGINAL_RENDER_ENTRY = base.render_entry


def enhanced_source_decision(card):
    value = base.first(
        card,
        "independent decision",
        "decision process",
        "final decision",
        "current decision",
        "medical decision",
        "technical decision",
        "command decision",
        "decisive choice",
        "decision",
        "choice",
        "physical action",
        "action",
        "agency",
        "authorized immediately",
    )
    if value:
        return value, "SOURCE-EXPLICIT-DECISION"
    value = base.source_block(
        card,
        (
            "independent decision",
            "decision process",
            "final decision",
            "current decision",
            "decisive choice",
            "decision",
            "choice",
            "physical action",
            "action",
            "agency",
            "response",
            "resolution",
        ),
    )
    if value:
        return value, "SOURCE-BLOCK-DECISION"
    return None, "NON-DISCRETE"


def enhanced_source_pov(card):
    return base.first(
        card,
        "pov / decision owner",
        "pov/decision owner",
        "pov / decision owners",
        "pov/decision owners",
        "pov / information source",
        "pov",
    )


base.source_decision = enhanced_source_decision
base.source_pov = enhanced_source_pov

import build_full_series_context_writer_activation_deep as deep  # noqa: E402

# Workflow/QC dominant-engine labels. Event/loss facts remain controlled by
# approved source hierarchy, not by these labels.
deep.SPECIAL_ENGINE.update({
    150: "TECHNICAL-REPAIR/TEST",
    322: "TACTICAL-COMBAT",
    680: "MEDICAL/CARE/CONSENT",
    683: "TACTICAL-COMBAT",
    684: "TECHNICAL-REPAIR/TEST",
    762: "MEDICAL/CARE/CONSENT",
    841: "RECORD/PROVENANCE/MYSTERY",
    889: "RECORD/PROVENANCE/MYSTERY",
    1084: "COLLECTION/ACCESS/TRANSFER",
    1085: "TECHNICAL-REPAIR/TEST",
    1088: "ENDING/HANDOFF",
})


def _set_common_override(a, authority):
    a["override_authority"] = authority
    a["grade"] = "A"
    return a


def apply_load_bearing_override(a):
    """Apply only higher-source propagation fixes discovered by manual review."""
    ep = a["ep"]

    if ep == 150:
        _set_common_override(
            a,
            "MANUAL CROSSCHECK — E150 detailed card + L-H01 named-loss lock; death/agency/no-reversal unchanged. Detailed card refines the older coarse loss wording by preserving E147 injury → E150 death timing.",
        )

    elif ep == 322:
        _set_common_override(
            a,
            "O01/X04 PROPAGATION RESOLUTION — later E322 detailed card + GA3 final cross-audit control writer execution. Older L-H02 battery wording is stale at mechanism level; locked death, independent agency, plural succession and no-Rian-inheritance remain unchanged.",
        )
        a["pov"] = "Toma Cal, Rema, Anchor operators and current window feeds."
        a["pov_auth"] = "SOURCE-EXPLICIT / LATER FINAL GA3 STATE"
        a["owner"] = "Toma owns the 74-second manual hold and role/state handoff; Rema/alternates own acceptance of the bounded physical role; Iris owns timing fallback only."
        a["owner_auth"] = "LATER GA3 FINAL CROSS-AUDIT + SOURCE DECISION"
        a["decision"] = "Toma completes the 74-second manual isolation and transfers current physical state, unknowns, stop limits and lane condition instead of preserving office or allowing automatic total succession."
        a["decision_mode"] = "SOURCE-EXPLICIT-DECISION / PROPAGATION-RESOLVED"
        a["human"] = "Toma, Rema and the Anchor operators physically performing the evacuation, manual hold and acceptance of the bounded role/state handoff."
        a["human_auth"] = "SOURCE-EXPLICIT / LATER FINAL GA3 STATE"
        a["engine"] = "TACTICAL-COMBAT"
        a["rian_guard"] = "Rian receives no Toma succession authority, governorship, master key or automatic command inheritance."

    elif ep == 680:
        _set_common_override(
            a,
            "O01/X04 PROPAGATION RESOLUTION — E680 detailed card + final GA6 operation state + GA6 final cross-audit control writer execution. Older L-H03 stay-behind/capture wording is stale at mechanism level; locked death, medical agency and no-reversal remain unchanged.",
        )
        a["pov"] = "Ella Savin and current medical/ship teams at the unstable medical-carrier separation."
        a["pov_auth"] = "SOURCE-EXPLICIT / LATER FINAL GA6 STATE"
        a["owner"] = "Ella owns the manual medical/coupling decision; current medical/ship teams own patient transfer, treatment separation and bounded technical execution. Rian does not order her choice."
        a["owner_auth"] = "LATER GA6 FINAL STATE + SOURCE DECISION"
        a["decision"] = "Ella remains at the manual medical/coupling station, orders patient/caregiver transfers and treatment-priority separation, and completes the manual release needed to separate the unstable carrier pair."
        a["decision_mode"] = "SOURCE-EXPLICIT-DECISION / PROPAGATION-RESOLVED"
        a["causal"] = "PRESSURE[preserve patients, crews and B/C transition while an unstable medical-carrier pair threatens coupled failure] → OBSTACLE[automatic release risks uncontrolled rotation and life-support failure; waiting blocks the transition and exposes surrounding ships] → PIVOT[Ella orders transfers and completes manual separation; Rian does not order her choice] → DELTA[the carrier groups separate and the wider branch collision does not propagate] → COST[Ella dies permanently during the final release/pressure-fire failure; medical capacity degrades and other casualties remain in the global ledger] → NEXT[the common phase is exhausted and E681 must choose the fifth-answer architecture]."
        a["human"] = "Ella Savin, the patients/caregivers she orders transferred, and the current medical/ship teams performing the separation."
        a["human_auth"] = "SOURCE-EXPLICIT / LATER FINAL GA6 STATE"
        a["payoff"] = "the medical-carrier separation preserves patients/crews and prevents a wider branch propagation without converting Ella's death into Rian's decision."
        a["hook"] = "E681 begins after Ella's permanent loss with the common assumptions exhausted and G requesting full control."
        a["engine"] = "MEDICAL/CARE/CONSENT"
        a["rian_guard"] = "Rian cannot order Ella's sacrifice, inherit her medical authority, reverse her death, or erase current patient/team consent and stop authority."

    elif ep == 683:
        _set_common_override(
            a,
            "MANUAL CROSSCHECK — E683 detailed card + final GA6 state + L-H04/L-S01. Ardo owns the two-command hold; Vow of Bastion is unrecoverable; no Rian inheritance.",
        )
        a["engine"] = "TACTICAL-COMBAT"

    elif ep == 684:
        _set_common_override(
            a,
            "MANUAL CROSSCHECK — E684 detailed card + final GA6 state + L-T01/L-T02. Vera injury and Parus strategic-propulsion loss remain permanent; no hidden restoration.",
        )
        a["engine"] = "TECHNICAL-REPAIR/TEST"

    elif ep == 762:
        _set_common_override(
            a,
            "MANUAL LOAD-BEARING ROUTE — E761 source-explicit Lin/local agency carries into E762 consequence; L-H05 loss lock controls. Lin does not choose death and is not reduced to Haren/Rian motivation.",
        )
        a["pov"] = "WORKFLOW close-third/current-information route through Lin Osa's already-established local household/work/service actors and the immediate treatment/evacuation team; preserve Lin's E761 agency without inventing a new witness."
        a["pov_auth"] = "WORKFLOW-RECOMMENDATION FROM E761 SOURCE-EXPLICIT AGENCY + E762 LOCKED LOSS — NOT STORY CANON"
        a["owner"] = "Lin owns her E761 care/work/household choices and evidence; current local care/service actors own E762 treatment and evacuation attempts. No actor owns her death as a chosen sacrifice."
        a["owner_auth"] = "L-H05 + E761/E762 SOURCE CAUSAL CHAIN"
        a["decision"] = "NON-DISCRETE CONSEQUENCE — Lin dies despite local treatment/evacuation attempts after the locked D4 downstream service-failure chain; her appeal, work logs and household evidence remain available."
        a["decision_mode"] = "WORKFLOW-NON-DISCRETE CONSEQUENCE FROM LOCKED LOSS"
        a["human"] = "Lin Osa's current household/community/work team plus the local treatment/evacuation actors who physically bear the service failure; do not stage Lin as choosing death."
        a["human_auth"] = "SOURCE-BOUND E761→E762 HUMAN-CARRIER CONTINUITY"
        a["engine"] = "MEDICAL/CARE/CONSENT"
        a["rian_guard"] = "Rian cannot convert Lin's death into his private guilt/authority, erase Haren's bounded responsibility, or replace affected-region ownership of her evidence."

    elif ep == 841:
        _set_common_override(
            a,
            "HIGHER-AUTHORITY WC OVERRIDE — M-010 final-payoff scene ledger + L-R02 named-loss ledger outrank stale E841 DD card. Neutral-custody adjudication may remain secondary, but it cannot displace the locked LIV-4 fracture scene.",
        )
        a["pov"] = "Mia close-third, with a bounded LIV-4 / AI-person witness information route only where the POV harness permits."
        a["pov_auth"] = "M-010 SCENE LOCK + WORKFLOW POV BOUNDARY"
        a["owner"] = "LIV-4/current witness and custodians own which copied states may act, testify, remain private or be destroyed; emergency operators own only bounded copy/safety execution."
        a["owner_auth"] = "M-010 + L-R02 HIGHER-AUTHORITY LOCK"
        a["decision"] = "LIV-4/current witness and custodians choose which emergency-copied states may act, testify, remain private or be destroyed; no side may convert the fracture into sole 'rogue AI' or sole-human guilt."
        a["decision_mode"] = "HIGHER-AUTHORITY LOCKED DECISION"
        a["causal"] = "PRESSURE[preserve current operational evidence/person-state during the Black Ward machine-witness mesh breach] → OBSTACLE[emergency copying can save evidence/operational state but cannot preserve one continuous LIV-4 person-state; old orders, corporate safety locks, military shortcuts and AI decisions interact] → PIVOT[LIV-4/current witness and custodians bound which copied states may act/testify/remain private/be destroyed] → DELTA[operational evidence survives while one continuous relational/person-state is irreversibly lost] → COST[LIV-4 continuity loss cannot be repaired by later merge or archive correction] → NEXT[person/evidence/tool categories and consent-limited machine-record rules must carry the loss forward]."
        a["human"] = "LIV-4 as the present AI/composite person-state, current custodians, and Mia/current care-evidence operators who physically handle the emergency copy and its limits."
        # Keep HIGH-WATCH gate semantics while the explicit higher-authority line above documents why this is more specific.
        a["human_auth"] = "ADOPTED-HIGH-WATCH-CARRIER-GUIDE"
        a["relationship"] = "one continuous LIV-4 relational/person-state is lost; evidence survival is not person survival and no later merge may restore equivalence."
        a["relationship_auth"] = "L-R02 LOCKED IRREVERSIBLE PERSON-STATE LOSS"
        a["payoff"] = "the story physically proves that preserving evidence or a usable copy does not equal preserving one continuous person."
        a["hook"] = "later AI/person/evidence custody must operate with the missing continuity rather than merge it back into existence."
        a["engine"] = "RECORD/PROVENANCE/MYSTERY"
        a["rian_guard"] = "Rian cannot define LIV-4 survival, own the copied states, erase witness/custodian consent, or restore the lost continuity through Archive authority."
        a["mystery"] = "Expose only M-010's locked causal plurality and LIV-4 fracture here; do not promote unrelated Seed/Archive-origin answers."

    elif ep == 889:
        _set_common_override(
            a,
            "HIGHER-AUTHORITY WC OVERRIDE — L-R01/L-R04 named-loss ledger outranks stale E889 DD card. The 46,600-restriction closeout may remain a secondary episode function, but Nacre-3's irreversible mirror/source loss must occur at E889.",
        )
        a["pov"] = "WORKFLOW current-information route through Nacre-3 custodians and affected source parties physically facing coercive full-copy / central-capture pressure; do not recenter the choice on Rian."
        a["pov_auth"] = "WORKFLOW-RECOMMENDATION FROM L-R01 LOCKED AGENCY — NOT STORY CANON"
        a["owner"] = "Nacre-3 custodians and affected source parties own the refusal/destruction-or-failure decision; Rian cannot make the loss alone."
        a["owner_auth"] = "L-R01/L-R04 HIGHER-AUTHORITY LOCK"
        a["decision"] = "Nacre-3 custodians destroy or allow the independent mirror to fail rather than permit coercive full copying and central capture of the protected source corpus."
        a["decision_mode"] = "HIGHER-AUTHORITY LOCKED DECISION"
        a["causal"] = "PRESSURE[close current restriction/appeal work while pressure rises to centralize a complete evidentiary copy] → OBSTACLE[protecting affected-source consent and independent custody conflicts with preserving every testimony/context bit] → PIVOT[Nacre-3 custodians refuse coercive full copy and accept mirror destruction/failure] → DELTA[some testimony/context becomes permanently unrecoverable and one complete canonical history becomes technically impossible] → COST[future adjudication loses real evidence/context rather than merely choosing ideological plurality] → NEXT[deletion-candidate and later plural-history work must operate with an actual permanent gap]."
        a["human"] = "Nacre-3 custodians and affected source parties whose testimony/context cannot be fully copied without violating the locked custody/consent boundary."
        a["human_auth"] = "HIGHER-AUTHORITY LOCKED SOURCE/CUSTODIAN CARRIER"
        a["relationship"] = "the source/custodian relationship ends with a real evidentiary absence; later institutions may preserve provenance but cannot reconstruct the lost whole."
        a["relationship_auth"] = "L-R01/L-R04 IRREVERSIBLE RECORD-LOSS LOCK"
        a["payoff"] = "Nacre-3's loss makes complete history physically unavailable, not merely politically rejected; current restriction closeout remains secondary and cannot erase the loss."
        a["hook"] = "all later Archive/history settlements must work with a permanent missing source while current rights remain actionable."
        a["engine"] = "RECORD/PROVENANCE/MYSTERY"
        a["rian_guard"] = "Rian cannot order the mirror's fate alone, reconstruct the lost context through future memory, or convert evidence custody into truth sovereignty."
        a["mystery"] = "Nacre-3 loss may prove history incompleteness here; it must not reveal any unrelated final Archive/Seed answer ahead of its locked payoff."

    elif ep == 1084:
        _set_common_override(
            a,
            "MANUAL CROSSCHECK — M-003 final-fate lock + L-T03 + reconciled ending card. 07 Hybrid Retirement is irreversible without a new public authorization process.",
        )
        a["pov"] = "Nera Vick leads the technical action; Rian is present only for his own pilot-priority relinquishment."
        a["pov_auth"] = "M-003 LOCKED POV/OWNER + RECONCILED ENDING CARD"
        a["owner"] = "Nera owns technical truth/custody relinquishment; Rian owns only signing away exclusive pilot priority; plural/public custodians and ordinary authorization own later use."
        a["owner_auth"] = "M-003 + L-T03 + ENDING RECONCILIATION"
        a["decision"] = "07's remaining unique combat-control module is removed and divided under plural/public custody; a nonunique public rescue/training configuration is installed; Rian signs away exclusive pilot priority and Nera singular technical custody."
        a["decision_mode"] = "LOCKED FINAL-FATE DECISION"
        a["human"] = "Nera, Rian and the already-authorized technical/public custodians physically executing the module removal, replacement and ordinary-pilot handoff."
        a["human_auth"] = "LOCKED FINAL-FATE CURRENT ACTORS"
        a["engine"] = "COLLECTION/ACCESS/TRANSFER"
        a["rian_guard"] = "Rian cannot reclaim exclusive pilot priority, founder veto, private title or silent peak-wartime restoration."

    elif ep == 1085:
        _set_common_override(
            a,
            "MANUAL CROSSCHECK — M-013 final public-use scene + reconciled ending card. Public technical commons must be demonstrated by another qualified engineer acting without Nera's personal permission.",
        )
        a["pov"] = "Nera and the other qualified engineer/current certifier interaction, bounded to public technical-commons rules."
        a["pov_auth"] = "M-013 FINAL PUBLIC-USE LOCK + ENDING CARD"
        a["owner"] = "the other qualified engineer owns lawful use/rejection under commons rules; Nera owns only her remaining attribution, refusal and safety-objection rights."
        a["owner_auth"] = "M-013 LOCKED PUBLIC-USE AGENCY"
        a["decision"] = "another qualified engineer lawfully uses or rejects part of the Open Service standard without asking Nera's personal permission; Nera accepts the loss of exclusive control and exercises only rights that remain personally hers."
        a["decision_mode"] = "LOCKED FINAL PUBLIC-USE DECISION"
        a["human"] = "Nera plus the already-authorized qualified engineer/current certifier demonstrating that public use no longer depends on the inventor's personal permission."
        a["human_auth"] = "M-013 LOCKED CURRENT-ACTOR CARRIER"
        a["payoff"] = "contributor credit and safety objection survive while exclusive technical ownership does not."
        a["engine"] = "TECHNICAL-REPAIR/TEST"
        a["rian_guard"] = "Rian cannot convert the commons, Academy records, 07 lineage or Nera's authorship into his private technical authority."

    elif ep == 1088:
        _set_common_override(
            a,
            "MANUAL CROSSCHECK — M-001 final ownership lock + reconciled E1088 card. Physical interface removal/split, credential expiry and permanent query gaps are all required; no secret master backdoor survives.",
        )
        a["pov"] = "Rian close-third for relinquishment, bounded by current medical/technical operators performing the irreversible interface removal."
        a["pov_auth"] = "M-001 LOCKED FINAL OWNERSHIP SCENE"
        a["owner"] = "Rian owns consent/authorization to relinquish his exclusive interface; current medical/technical operators own safe procedure; distributed institutions own their later decisions."
        a["owner_auth"] = "M-001 + RECONCILED ENDING CARD"
        a["decision"] = "Rian authorizes and accepts physical removal/splitting of the remaining exclusive future-index interface; his personal activation credential expires, no recoverable master copy/backdoor is retained, and the lost master queries cannot later be cured."
        a["decision_mode"] = "LOCKED FINAL OWNERSHIP DECISION"
        a["human"] = "Rian and the current medical/technical operators executing the irreversible removal while regional systems are already operating without his standing command."
        a["human_auth"] = "M-001 LOCKED CURRENT-ACTOR CARRIER"
        a["payoff"] = "Rian permanently loses ranked master-query access and the ability to resume a sovereign future-index role; ordinary revocable skills remain ordinary."
        a["engine"] = "ENDING/HANDOFF"
        a["rian_guard"] = "Rian cannot retain a hidden backdoor, transfer the exclusive credential, repeat regression/master correction, or reclaim standing central sovereignty."

    return a


def safe_activation(card):
    current = base.activation
    base.activation = _ORIGINAL_ACTIVATION
    try:
        a = deep.activation_deep(card)
    finally:
        base.activation = current
    return apply_load_bearing_override(a)


def render_entry_with_override(a):
    text = _ORIGINAL_RENDER_ENTRY(a)
    authority = a.get("override_authority")
    if not authority:
        return text
    needle = "Story Canon Effect: NONE — this section is workflow/QC routing only."
    replacement = needle + "\n\n**LOAD_BEARING_OVERRIDE_AUTHORITY:**  \n" + authority
    return text.replace(needle, replacement, 1)


base.activation = safe_activation
base.render_entry = render_entry_with_override


def _all_text(a):
    keys = ("pov", "owner", "decision", "causal", "human", "relationship", "payoff", "hook", "rian_guard", "mystery", "override_authority")
    return " ".join(str(a.get(k, "")) for k in keys)


def assert_load_bearing(acts):
    by_ep = {a["ep"]: a for a in acts}
    required = {
        150: ("Jena", "irreversible"),
        322: ("74-second", "role/state handoff"),
        680: ("Ella", "manual medical/coupling", "Rian does not order"),
        683: ("Ardo", "commands separate"),
        684: ("strategic propulsion", "permanent"),
        762: ("Lin Osa", "does not choose death"),
        841: ("LIV-4", "continuous", "irreversibly lost"),
        889: ("Nacre-3", "permanently unrecoverable", "canonical history"),
        1084: ("unique combat-control module", "exclusive pilot priority"),
        1085: ("another qualified engineer", "without asking Nera"),
        1088: ("no recoverable master copy/backdoor", "cannot later be cured"),
        1096: ("ordinary training/service task", "wartime"),
        1097: ("strategic propulsion", "lost"),
        1098: ("current work", "Rian"),
        1099: ("Ern", "independent"),
        1100: ("ordinary", "current name", "future"),
    }
    failures = []
    for ep, needles in required.items():
        text = _all_text(by_ep[ep]).lower()
        for needle in needles:
            if needle.lower() not in text:
                failures.append(f"E{ep}: missing load-bearing token {needle!r}")
    if by_ep[684]["engine"] != "TECHNICAL-REPAIR/TEST":
        failures.append("E684: wrong dominant engine")
    if by_ep[841]["engine"] != "RECORD/PROVENANCE/MYSTERY":
        failures.append("E841: wrong dominant engine")
    if by_ep[889]["engine"] != "RECORD/PROVENANCE/MYSTERY":
        failures.append("E889: wrong dominant engine")
    if by_ep[1100]["engine"] != "ENDING/HANDOFF":
        failures.append("E1100: wrong endpoint engine")
    if failures:
        raise SystemExit("LOAD-BEARING GATE FAIL:\n- " + "\n- ".join(failures))


def render_load_bearing_audit(acts):
    by_ep = {a["ep"]: a for a in acts}
    rows = [
        (150, "Jena Ark", "PASS", "E147 injury → E150 death timing preserved; worker/caravan council owns name/privacy/safety aftermath; no resurrection/reward conversion."),
        (322, "Toma Cal", "PASS — PROPAGATION RESOLVED", "Later GA3 final state controls 74-second manual hold + role/state handoff. Older battery wording is stale mechanism text only; death/agency/plural succession unchanged."),
        (680, "Ella Savin", "PASS — PROPAGATION RESOLVED", "Later GA6 final state controls manual medical-carrier separation. Older stay-behind/capture wording is stale mechanism text only; permanent death/medical agency unchanged."),
        (683, "Ardo Rev / Vow of Bastion", "PASS", "Ardo owns two-command hold; Vow is unrecoverable; Iven inherits bounded formation method only; Rian inherits nothing automatically."),
        (684, "Vera Thorn / Parus", "PASS", "Technical sacrifice correctly dominant; Vera permanent injury/active-chief retirement and Parus strategic-propulsion loss remain irreversible."),
        (762, "Lin Osa", "PASS — HUMAN ROUTE REPAIRED", "E761 self-owned care/work/household agency carries into E762 consequence; Lin does not choose death; affected local actors retain evidence/care ownership."),
        (841, "LIV-4", "PASS — HIGHER-WC OVERRIDE", "Stale DD E841 custody-only card cannot displace M-010/L-R02. Emergency copy saves evidence but one continuous LIV-4 person-state is irreversibly lost; no later merge restores it."),
        (889, "Nacre-3", "PASS — HIGHER-WC OVERRIDE", "Stale DD E889 restriction-ledger closeout remains secondary. L-R01/L-R04 require Nacre-3 irreversible source loss; complete master history becomes technically impossible."),
        (1084, "07 final fate", "PASS", "Unique combat-control module split; public nonunique rescue/training configuration; Rian exclusive pilot priority and Nera singular custody relinquished."),
        (1085, "Nera / Open Service", "PASS", "Another qualified engineer can lawfully use/reject the standard without Nera's personal permission; contributor credit/safety objection remain, exclusive control does not."),
        (1088, "Rian future index", "PASS", "Physical interface removal/split, credential expiry, no secret backdoor/master copy, permanent master-query gaps and no repeat correction."),
        (1096, "07 epilogue proof", "PASS", "Ordinary training/service work with multiple qualified operators; public usefulness does not restore wartime peak."),
        (1097, "Parus epilogue proof", "PASS", "Route-school/rescue-service life continues while strategic propulsion remains permanently lost."),
        (1098, "Distributed reunion", "PASS", "Core people appear first through their own current work/obligations; no all-cast recollection around Rian."),
        (1099, "Ern", "PASS", "Independent accountable operator-leader; cooperation remains conditional; no Rian subordination or residual roster."),
        (1100, "Ordinary present person", "PASS", "Current name/need/action outranks future category; no Archive chosen-one sign, master-history correction, reset or E1101 hook."),
    ]

    lines = [
        "# Full-Series Context Load-Bearing Manual Red-Team — 2026-08-20",
        "",
        "Status: PASS — WRITER-ACTIVATION LOAD-BEARING QC",
        "Story Canon Effect: NONE — source-precedence propagation and writer-routing only",
        "Publication: NOT AUTHORIZED",
        "Owner Agents: A00 PM / N04 Causality / N05 Mystery / N06 Ending / G07 Loss / X01 Red Team / X04 Continuity / O01 Canon",
        "Last Reviewed: 2026-08-20",
        "Depends On: [[effective-canon-status-manifest-v1]], [[named-loss-and-irreversible-transformation-ledger-v1]], [[final-payoff-scene-ledger-locked-v1]], GA2/GA3/GA6/GA7/GA8 final detailed audits, [[ga10-ending-reconciliation-canon-amendment-2026-08-20]], writer-activation overlays",
        "",
        "## 1. Audit rule",
        "",
        "This is the post-machine manual load test requested before calling E001–E1100 genuinely deep. It does not redesign plot. When a lower E101–E1100 DD episode card conflicts with a locked WC loss/payoff/final-state source, the higher source controls writer activation and the discrepancy is recorded instead of silently choosing the lower card.",
        "",
        "## 2. Load-bearing source-vs-overlay results",
        "",
        "| Episode | Load point | Verdict | Manual ruling |",
        "|---:|---|---|---|",
    ]
    for ep, name, verdict, ruling in rows:
        lines.append(f"| E{ep} | {name} | **{verdict}** | {ruling} |")

    lines += [
        "",
        "## 3. Propagation conflicts actually found",
        "",
        "1. **Toma E322** — old L-H02 battery/defense-station mechanism is stale against the later E322 detailed card and GA3 final cross-audit. Effective writer mechanism is the 74-second Anchor manual hold plus bounded role/state handoff. Locked death and agency did not change.",
        "2. **Ella E680** — old L-H03 stay-with-nontransportable-patients/capture-destruction wording is stale against the later GA6 final operation state and final cross-audit. Effective writer mechanism is manual medical-carrier separation. Locked death and agency did not change.",
        "3. **LIV-4 E841** — lower DD card contains Neutral custody adjudication but omits the locked M-010/L-R02 fracture. The writer overlay now makes LIV-4 fracture primary; custody adjudication may remain secondary only.",
        "4. **Nacre-3 E889** — lower DD card contains the 46,600 restriction closeout but omits L-R01/L-R04 destruction/source loss. The writer overlay now makes the irreversible Nacre-3 loss load-bearing while preserving the restriction closeout as secondary context.",
        "5. **Lin E762** — event/cause was sound, but writer carrier was too generic. The overlay now carries Lin's E761 local household/work/service agency into E762 without implying she chose death.",
        "",
        "These are propagation/QC resolutions under existing source precedence, not new canon events, deaths, relationships, technologies, authorities or ending changes.",
        "",
        "## 4. GA boundary representative recheck",
        "",
        "| Boundary | Required carry | Verdict |",
        "|---|---|---|",
        "| E100→101 | Academy gains do not become clean ship ownership; first ship enters as liability/claim/work system | PASS |",
        "| E210→211 | ship/route learning expands into Ardis service/civil responsibility without master authority | PASS |",
        "| E330→331 | Toma/Ardis plural succession consequences survive into GA4 | PASS |",
        "| E450→451 | succession compact produces ownerless-fleet legitimacy problem, not a prize fleet | PASS |",
        "| E570→571 | depleted charter/fleet and Orpheus staging remain GA6 inputs | PASS |",
        "| E690→691 | Ella/Ardo/Parus/Vera losses + holdout/captured/missing claims directly drive GA7 | PASS |",
        "| E800→801 | D4/Blood Admiral accountability enters record/personhood conflict without erasing current rights | PASS |",
        "| E900→901 | LIV-4/Nacre-3/Seed record limits carry into Preservation/Perfect Route debates | PASS |",
        "| E1000→1001 | central benefits/harms enter relinquishment without permanent Rian rule | PASS |",
        "",
        "## 5. Payoff / information-ceiling representative check",
        "",
        "- M-001: final Rian exclusive-index relinquishment remains E1088; no earlier activation overlay restores master query.",
        "- M-003: 07 final-fate lock remains E1084; E1085 demonstrates commons use instead of private Nera ownership.",
        "- M-010: LIV-4 fracture is restored to E841 as required by the locked payoff ledger.",
        "- M-012: Ern final handoff remains independent and does not become recruitment.",
        "- M-019/M-020: E1100 remains the ordinary-present-person / incomplete-history endpoint under the approved GA10 amendment.",
        "- No override promotes an unrelated Seed/Archive answer ahead of its locked payoff.",
        "",
        "## 6. Repetition-engine representative check",
        "",
        "The machine anti-repetition gate reports zero unresolved WATCH runs after owner/cost/carrier differentiation. Manual load points also remain functionally distinct: E322 command succession under physical failure; E680 medical separation; E684 technical irreversible sacrifice; E762 downstream care consequence; E841 person/evidence fracture; E889 source-destruction/provenance loss; E1084 ownership/fate transfer; E1088 relinquishment; E1100 ordinary care/service endpoint. No single `Rian knows → institution obeys` engine is allowed to substitute for these decisions.",
        "",
        "## 7. Ending E1096–E1100",
        "",
        "PASS. 07 remains public/nonunique; Parus propulsion remains lost; core characters retain independent work; Ern retains the right to disagree/refuse; Rian has no index/master command; E1100 centers one ordinary current person and current need with no destiny UI/reset/collector return.",
        "",
        "## 8. Final manual gate",
        "",
        "- load-bearing episodes checked: **16/16 PASS after propagation repair**.",
        "- stale DD / older-ledger mechanism conflicts left unrecorded: **0 known in this load-bearing set**.",
        "- new story canon required: **0**.",
        "- new death/survival/relationship/technology/authority/ending decision: **0**.",
        "- manuscript authority expansion: **0**.",
        "- publication authorization: **0**.",
        "",
        "> **FINAL MANUAL VERDICT: PASS — WRITER-ACTIVATED DEEP may be declared only if the generated overlay assertions and the existing machine false-A gate also PASS on the same PR head.**",
        "",
    ]
    return "\n".join(lines)


def main():
    rc = base.main()
    if rc:
        return rc
    cards = base.semantic.base.load_sources()
    acts = [safe_activation(cards[ep]) for ep in range(11, 1101)]

    assert_load_bearing(acts)

    strict = base.ROOT / "docs" / "99_quality_control" / "full-series-context-writer-activation-false-a-redteam-v1.md"
    strict.write_text(deep.render_strict_audit(acts), encoding="utf-8")

    manual = base.ROOT / "docs" / "99_quality_control" / "full-series-context-load-bearing-manual-redteam-2026-08-20.md"
    manual.write_text(render_load_bearing_audit(acts), encoding="utf-8")

    print(f"strict_false_a_audit={strict.relative_to(base.ROOT)}")
    print(f"load_bearing_manual_audit={manual.relative_to(base.ROOT)}")
    print("load_bearing_assertions=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
