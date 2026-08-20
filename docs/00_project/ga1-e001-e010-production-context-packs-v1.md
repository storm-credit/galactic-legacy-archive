# GA1 E001–E010 Production Context Packs v1

Status: PRODUCTION INPUT — SOURCE-BOUND / NON-STORY-CANON
Effective Authority: PC WORKFLOW/QC APPLICATION ONLY
Story Canon Effect: NONE
Canon Promotion: NOT AUTHORIZED BY THIS FILE
Publication: NOT AUTHORIZED
Owner Agents: A00 PM / A11 Prose & Serialization / N03 Episode / N04 Causality / X02 Reader Memory / X04 Continuity / O01 Canon
Last Reviewed: 2026-08-20
Base Main: `590f5c66099cc822d995eba97efde914c74b233f`
Depends On: [[CLAUDE]], [[pre-writing-gate-open-record-2026-08-06]], [[manuscript-production-workflow-v1]], [[first-writing-batch-readiness-v1]], [[effective-canon-status-manifest-v1]], [[continuity-issues]], [[context-pack-tangible-reader-memory-execution-spec-proposal-v1]], [[first-100-act-map-v2-consolidated]], [[ga1-episodes-1-20-beat-map-v1]], [[ga1-episodes-1-5-noncanon-scene-cards-v1]], [[ga1-episodes-6-10-scene-cards-v1]], [[master-series-chronology-v1]], [[ga1-10-state-checkpoint-matrix-v1]], [[academy-and-07-opening-operational-state-v1]], [[protagonist-p001-bible-v1]], [[rian-index-removal-memory-and-medical-state-v1]], [[hero-h001-bible-v1]], [[hero-h002-mechanic-bible-v1]], [[student-s001-data-cadet-bible-v1]], [[student-m001-medical-rescue-bible-v1]], [[core-canonical-names-and-voice-lock-v1]], [[opening-institutional-representatives-v1]], [[first-frame-bible-v1]], [[first-100-collectible-registry-v1]], [[m001-m020-early-clue-episode-ledger-v1]], [[final-payoff-scene-ledger-locked-v1]], [[named-loss-and-irreversible-transformation-ledger-v1]]
Used By: E001 manuscript preparation; E002–E010 rolling Context refresh; state-delta handoff between episode drafts
Open Risks: E002–E010 are PRELOAD/FORECAST only. Their dynamic opening state must be refreshed from the immediately preceding episode's actual draft result before drafting. Unsupported exact people, objects, procedures or IDs remain unresolved rather than invented.

---

## 0. Authority and Provenance Ruling

- Pre-Writing Gate remains **OPEN — DRAFT PRODUCTION ONLY**. Publication/public release/paid serialization remain blocked.
- [[context-pack-tangible-reader-memory-execution-spec-proposal-v1]] is the adopted Project-Control workflow/QC source of truth despite the historical `proposal` filename.
- Per CI-20260817-01 in [[continuity-issues]], [[ga1-episodes-1-5-noncanon-scene-cards-v1]] retains its legacy filename/header but its approved scene-level structure is valid AS drafting authority for E001–E005. This file does **not** rename or promote that source file.
- E006–E010 use [[ga1-episodes-6-10-scene-cards-v1]] as the exact scene-card input.
- Manuscript prose is last-priority evidence and cannot create story canon.
- GA1 E001–E010 are **not** among the currently designated HIGH-WATCH bands. HIGH-WATCH-only fields are therefore `N/A` unless included below as a non-high-watch agency/reader-memory check explicitly requested for production safety.

### Source-precedence reminder

1. current explicit author instruction / Project-Control / errata;
2. chronology, state, loss and payoff ledgers;
3. relevant Working Canon bibles;
4. approved act/subact/exact episode structure;
5. workflow/QC constraints;
6. NONCANON material as execution lens only;
7. manuscript prose last.

---

## 1. Rolling Production Rule — FULL → STATE DELTA → REFRESH

Do **not** pre-freeze 1,100 episode packs.

Operational sequence:

`E(n) FULL Context` → `E(n) draft` → `E(n) STATE DELTA` → `E(n+1) Context refresh` → `E(n+1) FULL Context`.

E002–E010 in this file are only **PRELOAD / FORECAST**. Approved cards define the expected envelope, but the actual opening state is not considered refreshed until the previous episode draft has been audited.

### 1.1 Run-local State Delta record

This is a production handoff record, not a new story-canon class or a replacement for existing ledgers.

For each completed episode draft record at minimum:

```text
STATE_DELTA_AFTER_E###:
- CHARACTER_STATE_CHANGED:
- PHYSICAL_POSSESSION_CHANGED:
- LOCATION_CHANGED:
- RELATIONSHIP_PRESSURE_CHANGED:
- KNOWLEDGE_REVEALED:
- COST_OR_LOSS_INCURRED:
- PROMISE_OR_DEBT_CREATED:
- AUTHORITY_CHANGED:
- UNRESOLVED_HOOK:
- TANGIBLE_OBJECT_STATE:
- RECURRING_FACE_PLACE_ASSET_STATE:
```

Each asserted item must carry one production classification:

- `[CANON-CONFIRMED]` — already supported by an approved source independent of prose.
- `[DRAFT-ONLY]` — exists only in the current draft wording/staging. It cannot update canon or a canonical ledger by itself.
- `[CONTINUITY-CARRY-FORWARD]` — a source-bounded or draft-created production fact that the next draft must remember to avoid a reset. This label does **not** promote it to canon.

If a draft creates an unsupported fact that would be required for the next episode, do not silently carry it forward as canon. Either revise the draft back inside approved sources or route it through normal change control.

---

# 2. E001 FULL Context Pack — WRITING INPUT

CONTEXT STATUS: **FULL / PRE-DRAFT-READY**
Episode: E001
Date: `CY 742-03-17`
POV: Rian close third; present sensory/body information outranks future-memory certainty.
Gate: DRAFT PRODUCTION AUTHORIZED / PUBLICATION NOT AUTHORIZED

## 2.1 Episode Objective

Get through Academy intake without exposing impossible knowledge and establish the date; when the current 07 hangar failure becomes immediate, prevent injury while preserving the fact that Rian has no present authority, licence or control over the staff who actually secure the machine.

## 2.2 Opening State

### Rian

- 17-year-old correctional cadet; no independent flight licence.
- weak/current adolescent body; former-life habits can exceed present neural/physical tolerance.
- future memory is vivid by relevance/emotional shock but Academy-opening details are incomplete.
- no standing command, equipment ownership, service master key or right to use the cockpit.
- current sensory evidence must be treated as more reliable than future familiarity.

### 07

- Academy physical custody; stripping/claim process pending.
- red disposal/stripping presentation at intake.
- main movement/reactor use unavailable at E001; maintenance/inspection power only.
- left-shoulder maintenance-arm/load mismatch is the immediate physical failure carrier.
- right-ankle manual floor lock is available to the dock worker response.
- no assigned student crew; no cockpit use.

### Institution / surrounding actors

- Academy intake and maintenance staff control the hangar, equipment custody and incident review.
- Bram Ido is an ordinary dock worker whose manual action can complete the physical safety response.
- Nera may notice that Rian uses service-interface language a cadet should not normally know; this is suspicion, not loyalty or subordinate status.
- the future core cast remains independent; E001 does not pre-form the cell.

## 2.3 Required Common Context Fields

`ACTIVE_DESIRE_MAIN`
- Rian wants to pass intake without drawing attention and determine when he has returned; once the support failure begins, he wants to stop the immediate injury without exposing regression-level knowledge.

`ACTIVE_DESIRE_SECONDARY`
- After intervening, Rian wants to avoid medical isolation/security detention and keep his knowledge source explainable in present terms.

`PHYSICAL_ANCHOR`
- 07's current left-shoulder maintenance-arm/load mismatch and the dock-side manual lock chain, including Bram Ido's right-ankle floor-lock action.

`STATE_CHANGE`
- Approved envelope: the immediate accident is prevented; Rian becomes a monitored anomaly; 07 stripping is paused for incident inspection rather than permanently cancelled; the powered-down frame returns an old service-type response to Rian.

`COST_OR_REFUSAL`
- Minor impact/synchronization shock; scrutiny; risk that the incident becomes a collective/institutional liability. No permanent injury or irreversible loss is authorized here.

`REENTRY_ANCHOR`
- The E001 incident record/evidence chain + Bram's physical lock contribution + 07's temporary inspection hold. E002 must reopen through the consequence of this event rather than resetting to generic school life.

## 2.4 Current Relationships

- **Rian ↔ Bram:** Rian can identify the immediate action, but Bram owns the physical lock step that completes the save. Do not transfer Bram's credit to Rian.
- **Rian ↔ Nera:** present-machine/service knowledge creates technical suspicion. No trust, devotion or future-role recruitment is established.
- **Rian ↔ Academy staff:** useful intervention and restricted-equipment knowledge create simultaneous value and suspicion.
- **Rian ↔ future core cast:** any remembered future importance is Rian's biased internal frame, not a current ownership claim or present loyalty state.

## 2.5 Authority / Limitation

- Rian may choose whether to intervene and may give an immediate physical warning.
- Bram/work crew retain the physical maintenance action needed to secure the machine.
- Academy staff retain equipment custody, incident classification/review and any inspection hold.
- Rian cannot pilot 07, authorize repair, override maintenance safety, cancel stripping, suppress the record, or invoke former rank.
- No hidden key grants universal equipment/institution access.

## 2.6 Known Cost / Loss Envelope

- **Allowed current cost:** minor impact/sync shock, surveillance/monitoring, institutional review, possible collective-liability pressure.
- **Not allowed:** new death, lost limb, major permanent injury, permanent 07 damage, 07 ownership transfer, miraculous strengthening, restoration of any later locked loss.
- [[named-loss-and-irreversible-transformation-ledger-v1]] contains no E001 locked death/permanent-loss event; do not manufacture one for intensity.

## 2.7 Current Faction / Institutional Pressure

Foreground only what the approved E001 sources require:

- Academy intake/equipment custody.
- disposal/inspection pressure on 07.
- incident/security/medical review risk after Rian's intervention.

Do **not** pull later Helix, Imperial, Neutral, Black Ward or high-level Continuity politics into E001 merely because they exist in the setting.

## 2.8 Scene-by-Scene Causality

### Scene 1 — Intake line / hangar threshold

1. Rian attempts a quiet intake and date check.
2. 07's present body contradicts/activates his future memory.
3. Archive produces the opening `역사에 기록되지 않음` warning state.
4. Result: his assumed advantage is immediately destabilized; he has a mystery, not a master key.

### Scene 2 — Current physical failure

1. Present 07/support geometry begins to fail.
2. Rian must choose between remaining inconspicuous and preventing immediate harm.
3. He gives a precise current physical instruction and moves despite his weak body/no authority.
4. Bram/work crew execute the decisive manual lock sequence.
5. Result: injury is prevented; Rian pays a body/suspicion cost; his memory's missing human name becomes a flaw rather than an omniscient advantage.

### Scene 3 — Institutional consequence

1. The intervention creates evidence of restricted-equipment knowledge.
2. Rian offers a bounded present-world explanation rather than revealing regression.
3. Academy staff flag/review him and pause stripping only for incident inspection.
4. The powered-down service response becomes the episode hook.
5. Result: the immediate save creates the exact problem that drives E002 — attribution, liability and collective consequence.

## 2.9 Reader Information Budget

### Allowed / required

- Rian subjectively lived a defeated future and has returned to a younger Academy body.
- his future knowledge is not complete at the human-detail level.
- he recognizes 07 from the future, but present 07 differs materially from remembered later use.
- Archive/system state says he is not recorded in history.
- the current failure can be understood through visible machine/support geometry.
- an ordinary worker's action is causally necessary.
- the powered-down 07 gives an old service-type response rather than a clean pilot-recognition victory.

### Forbidden / withheld

- no full explanation of regression mechanism or Continuity Seed.
- no deity/chosen-one mission explanation.
- no proof of 07's true civil-interoperability lineage; the first locked M-003 clue is E008.
- no royal-superweapon answer, master-key answer or seven-secret-machines answer.
- no full Orpheus truth; the first locked M-007 clue is E004.
- no late-series Authority F/G, connector ontology, Palimpsest or final-index explanation.
- no exact future-core death/disappearance countdown used as objective truth.
- no `Blood Admiral` metadata reveal merely to advertise Haren before its approved clue timing.

## 2.10 Payoff / Mystery Duties

- **M-009 regression cause:** E001 is a locked early clue because no deity/system grants a mission and Rian appears amid a failed Archive query/connection state. Preserve ambiguity.
- **M-001 unrecorded status:** the opening warning is required; E002 is the locked follow-up clue where the exact statement can coexist with operational response. Do not resolve origin.
- **07 lineage:** E001 service response may carry the mystery, but it must not become the formal M-003 lineage clue or explanation before E008.
- **ordinary actor:** Bram's physical action must remain materially necessary; do not convert the episode into a solo-hero save.

## 2.11 Reader-Memory / Agency Checks

`HIGH_WATCH_BAND: N/A — E001 is outside the current HIGH-WATCH list`

`RECURRING_FACE`
- Bram Ido as the current ordinary worker attached to the accident/evidence chain. Do not invent a second named exemplar solely for memory.

`RECURRING_ASSET`
- 07 / its incident evidence and temporary inspection state.

`RECURRING_PLACE`
- Academy intake frame hangar. Do not invent a dedicated named chamber for the incident.

`CURRENT_OWNER_OF_DECISION`
- Split by domain: Rian owns whether he intervenes; Bram/work crew own the decisive maintenance lock action; Academy staff own custody/review/inspection disposition.

`RIAN_CANNOT_OVERRIDE`
- maintenance safety, equipment custody, medical/security review, record attribution, or 07 movement/pilot authorization.

`ABSTRACT_CONCEPTS_FOREGROUNDED`
- Keep foreground abstraction to the immediate `recorded / not recorded` contradiction. All larger Archive/Continuity explanations remain background mystery.

`NEW_CANON_REQUIRED: NO`

## 2.12 Ending Hook

The powered-down cockpit/service system answers Rian's presence with an old authority/service handshake rather than a pilot-recognition salute.

The hook asks **why the machine responds operationally to someone history does not record**, not “what secret superweapon did he unlock?”

## 2.13 E002 Reentry Anchor

Open E002 from the concrete aftermath of E001:

- incident log / attribution chain;
- Bram's final physical action and whether the official record preserves it;
- Rian's monitoring/review status;
- 07's incident-inspection hold;
- liability spreading beyond one individual.

Do not reopen on a disconnected classroom exposition block.

## 2.14 Source-Bound Unresolved Fields

- exact identity of the person directly under the collapsing assembly if prose requires one: `UNRESOLVED FROM APPROVED SOURCES` (approved cards allow worker/cadet; do not invent a named victim).
- exact incident-review staff member speaking every line: `UNRESOLVED FROM APPROVED SOURCES` unless an already-approved representative is explicitly assigned by a higher source.
- exact UI/service-light technical wording beyond the approved hook function: `UNRESOLVED FROM APPROVED SOURCES`.
- any dedicated serial number, room name, special device or new protocol label created only for texture: `UNRESOLVED FROM APPROVED SOURCES` / do not add.

## 2.15 Writing Readiness

`WRITING READINESS: READY`

Reasons:

- exact E001 scene-level AS drafting authority exists;
- chronology/opening operational state and protagonist limits are compatible;
- no open S0/S1 continuity blocker targets E001;
- required physical carrier, current desire, cost, agency split, information ceiling and E002 reentry are source-supported;
- draft production is authorized by the open gate;
- human/mobile issue #26 remains a **publication** hard blocker, not an E001 drafting blocker;
- `NEW_CANON_REQUIRED: NO`.

---

# 3. E002–E010 PRELOAD / FORECAST Context Packs

These are not final opening states. Every pack below must be refreshed from the previous episode's audited State Delta before it becomes `FULL`.

---

## E002 PRELOAD

`CONTEXT STATUS: PRELOAD / FORECAST`

`CURRENT_EXPECTED_OBJECTIVE`
- Prevent the E001 accident from being reduced to sabotage/individual misconduct and keep the consequence from immediately freezing the linked community/evaluation path.

`KNOWN_OPENING_DEPENDENCIES`
- E001 incident record/evidence; Bram's physical contribution; Rian's review/monitoring state; 07 inspection hold.

`ACTIVE_DESIRE_MAIN`
- Rian: explain the intervention without revealing regression and keep the event from becoming a simple violation category.

`ACTIVE_DESIRE_SECONDARY`
- Haren: protect current community medicine/ration/identity/transfer interests without becoming Rian's grateful dependent.
- Serin: preserve accurate attribution/provenance rather than clean heroic credit.

`PHYSICAL_ANCHOR`
- E001 incident log / attribution record and the concrete 07 re-test assignment created from the incident.

`STATE_CHANGE`
- FORECAST from approved structure: individual/simple violation is deferred into a joint safety re-test path; Rian loses clean individual credit; Rian/Haren liabilities become linked for the next evaluation.

`COST_OR_REFUSAL`
- Rian gives up individual heroic credit; Haren accepts only a time-buying arrangement, not loyalty; one failure can spread harm.

`KNOWN_RELATIONSHIP_PRESSURE`
- Rian sees future role/target value; Haren forces attention onto current people and obligations; Serin resists false attribution.

`KNOWN_PAYOFF_DUTIES`
- M-001: E002 is the locked follow-up where exact unrecorded status and operational response coexist.
- Do not expose the formal `Blood Admiral` metadata answer early; Haren may exist in Rian's future memory as a dangerous future figure without converting that into the later locked Archive label reveal.

`REENTRY_ANCHOR`
- E001 incident log + Bram contribution + 07 hold.

`CURRENT_OWNER_OF_DECISION`
- Rian controls whether he corrects his own credit/statement; Haren controls his acceptance/refusal; record provenance belongs to Serin's domain; authorized staff/institution control final classification/re-test status.

`RIAN_CANNOT_OVERRIDE`
- Haren consent/community standing, Serin provenance/privacy judgment, institutional discipline/evaluation authority.

`UNRESOLVED_SOURCE_DEPENDENT_ITEMS`
- exact community individuals named in dialogue; exact administrative form fields; exact reviewer identity: `UNRESOLVED FROM APPROVED SOURCES` unless supplied by an approved source at refresh.

`MUST_REFRESH_AFTER_E001_DRAFT`
- exact body/sync state; monitoring severity; exact incident-record wording/credit; which E001 details were actually disclosed to reader; physical 07 hold condition; Rian↔Bram/Nera pressure.

`NEW_CANON_REQUIRED: NO — PRELOAD; RECHECK AT REFRESH`

---

## E003 PRELOAD

`CONTEXT STATUS: PRELOAD / FORECAST`

`CURRENT_EXPECTED_OBJECTIVE`
- Make present 07 safe enough for the re-test without treating Rian's future configuration knowledge as current engineering truth.

`KNOWN_OPENING_DEPENDENCIES`
- E002 re-test path; linked liability; 07 still under inspection/restricted movement; provenance pressure.

`ACTIVE_DESIRE_MAIN`
- Rian: get 07 into a safe basic movement state for the current test.

`ACTIVE_DESIRE_SECONDARY`
- Nera: prevent a future-derived repair order from damaging the present machine and preserve actual contributor authorship/safety responsibility.

`PHYSICAL_ANCHOR`
- Current 07 mount/support geometry + change/contributor log + existing service coupler discovered during current-line repair.

`STATE_CHANGE`
- FORECAST: Nera disproves one future-derived fix; contributor/change logging becomes part of the work; 07 reaches restricted stand/movement capability; service coupler becomes visible without proving its full lineage.

`COST_OR_REFUSAL`
- Weapons/full output remain unavailable; Nera refuses whole-frame safety ownership; technical responsibility becomes plural rather than absorbed by Rian.

`KNOWN_RELATIONSHIP_PRESSURE`
- Rian must accept being corrected by present expertise; Nera requires rights and evidence before cooperation.

`KNOWN_PAYOFF_DUTIES`
- M-008: E003 is a locked clue that Archive/future compression can be operationally useful yet wrong about ownership/meaning.
- Do not turn the service coupler into the M-003 lineage reveal before E008.

`REENTRY_ANCHOR`
- E002 re-test assignment and incident-derived 07 inspection state.

`CURRENT_OWNER_OF_DECISION`
- Nera owns technical stop/repair judgment within her current competence; licensed staff retain movement/safety authorization; Rian owns only his proposal/pilot-side choice.

`RIAN_CANNOT_OVERRIDE`
- technical safety stop, contributor attribution, licensed movement authorization.

`UNRESOLVED_SOURCE_DEPENDENT_ITEMS`
- exact replacement-part model/serial; exact dedicated tool ID; new workshop room name: unresolved / do not invent.

`MUST_REFRESH_AFTER_E002_DRAFT`
- exact re-test classification; exact linked-liability wording; Rian/Haren/Serin relationship temperature; 07 hold deadline/status; reader knowledge carried from E002.

`NEW_CANON_REQUIRED: NO — PRELOAD; RECHECK AT REFRESH`

---

## E004 PRELOAD

`CONTEXT STATUS: PRELOAD / FORECAST`

`CURRENT_EXPECTED_OBJECTIVE`
- Use future warning only as a hypothesis for the re-test while keeping Rian medically safe enough to participate and proving that present conditions outrank exact remembered failure locations.

`KNOWN_OPENING_DEPENDENCIES`
- restricted 07 movement; service coupler known but unexplained; Rian has already been technically corrected; current sync/body cost must carry forward.

`ACTIVE_DESIRE_MAIN`
- Rian: predict the current test hazard and remain in the test without pretending his memory is exact.

`ACTIVE_DESIRE_SECONDARY`
- Mia: establish a real medical stop condition and prevent tactical urgency from erasing present body evidence.

`PHYSICAL_ANCHOR`
- current re-test route/07 load-transfer state + Mia's bounded medical monitoring/stop condition.

`STATE_CHANGE`
- FORECAST: exact future failure prediction is wrong; broader load-transfer principle remains useful after Nera/Haren/Mia adapt it; Rian becomes explicitly useful but medically/epistemically unreliable.

`COST_OR_REFUSAL`
- sync symptoms and loss of prophet-like certainty; Mia refuses `I'm fine` as sufficient medical authority.

`KNOWN_RELATIONSHIP_PRESSURE`
- Mia's medical authority is not subordinate to Rian's tactical knowledge; team expertise must transform his warning into a present plan.

`KNOWN_PAYOFF_DUTIES`
- M-007: E004 is the first locked Original Orpheus clue — clear State convoy memory with civilian/route details as blank ranked categories. Show fragment/body response, not full history.

`REENTRY_ANCHOR`
- E003's present-machine correction and service-coupler state, plus accumulated Rian sync symptoms.

`CURRENT_OWNER_OF_DECISION`
- Mia owns medical stop; Nera/current operators own present technical adaptation; Rian owns whether to disclose bounded symptoms and accept correction.

`RIAN_CANNOT_OVERRIDE`
- medical grounding/stop, present machine state, other actors' domain adaptation.

`UNRESOLVED_SOURCE_DEPENDENT_ITEMS`
- exact medical diagnosis/neurological terminology; exact current hazard coordinate if not on card: unresolved rather than invented.

`MUST_REFRESH_AFTER_E003_DRAFT`
- 07 exact movement/heat state; actual coupler information revealed; Rian symptoms; Nera trust/conflict state; any clue wording already exposed.

`NEW_CANON_REQUIRED: NO — PRELOAD; RECHECK AT REFRESH`

---

## E005 PRELOAD

`CONTEXT STATUS: PRELOAD / FORECAST`

`CURRENT_EXPECTED_OBJECTIVE`
- Complete the closed-choice safety test without abandoning the target, accepting sabotage classification, or assigning one person as sole sacrificial culprit.

`KNOWN_OPENING_DEPENDENCIES`
- Rian's prediction is now bounded/unreliable; Mia stop condition exists; 07 has limited movement only; Haren/Nera/Serin/Mia retain domain authority.

`ACTIVE_DESIRE_MAIN`
- Rian: keep the target/current people safe while preserving Haren's guarantee and 07's evaluation path, but share immediate risk instead of choosing alone.

`ACTIVE_DESIRE_SECONDARY`
- Core members: preserve their own domain limits/obligations rather than being absorbed into Rian's solution.

`PHYSICAL_ANCHOR`
- 07 at 25–35% supervised output + damaged training module/person + simulated route/corridor and rescue/manipulator action.

`STATE_CHANGE`
- FORECAST: slower partial rescue succeeds while official performance metric and one asset fail; provisional joint-evaluation cell forms; 07 stripping stays paused only under continuing value/liability proof.

`COST_OR_REFUSAL`
- one equipment asset is damaged/lost and another team or schedule bears a cost; failures become linked; no cost-free fifth answer.

`KNOWN_RELATIONSHIP_PRESSURE`
- every member must own a domain step; Haren/Nera/Serin/Mia may constrain Rian; ordinary actor owns one physical step.

`KNOWN_PAYOFF_DUTIES`
- The betrayal/fifth-answer structure may be demonstrated, but the locked M-006 formal clue cadence later resumes at E020. Do not turn E005 into proof that every closed choice has a perfect loophole.

`REENTRY_ANCHOR`
- E004 medical stop + present-machine correction + acknowledged uncertainty.

`CURRENT_OWNER_OF_DECISION`
- shared process: Haren manifest/obligation, Nera tool configuration, Serin record conflict/source, Mia body/time stop, ordinary actor physical step; Academy owns evaluation consequence.

`RIAN_CANNOT_OVERRIDE`
- the four domain constraints above or the other actor's physical step.

`UNRESOLVED_SOURCE_DEPENDENT_ITEMS`
- exact damaged/lost equipment asset; exact rival schedule/asset bearing cost; exact ordinary actor identity if not already approved: `UNRESOLVED FROM APPROVED SOURCES`.

`MUST_REFRESH_AFTER_E004_DRAFT`
- Rian medical condition; exact trust pressure; 07 heat/movement state; exact test parameter changes; exact reader exposure of Orpheus/hero-count material.

`NEW_CANON_REQUIRED: NO — PRELOAD; RECHECK AT REFRESH`

---

## E006 PRELOAD

`CONTEXT STATUS: PRELOAD / FORECAST`

`CURRENT_EXPECTED_OBJECTIVE`
- Understand what the seven-day provisional cell actually is, define current participation conditions, and interpret Archive's changing count without turning people into a fixed future roster.

`KNOWN_OPENING_DEPENDENCIES`
- E005 actual test result; provisional linked evaluation; 07 post-test cooling/inspection; weapons locked; stripping paused for seven-day evaluation.

`ACTIVE_DESIRE_MAIN`
- Rian: preserve a workable evaluation path for 07/Haren while trying to organize immediate roles.

`ACTIVE_DESIRE_SECONDARY`
- Haren/Nera/Serin/Mia: retain consent, domain authority and exit/refusal conditions rather than accept future-role assignment.

`PHYSICAL_ANCHOR`
- shared scorecard + classroom/equipment-status board displaying the 13/12/13 category mismatch.

`STATE_CHANGE`
- FORECAST: temporary roles and a domain-authority + time-limited emergency-lead + logged-review rule are adopted; the count mismatch is understood as a category problem, not proof of a person's disappearance.

`COST_OR_REFUSAL`
- decisions become slower; members can legally refuse/withdraw; Juno Hess's group bears a real workshop-slot cost from the allocation priority.

`KNOWN_RELATIONSHIP_PRESSURE`
- Rian's future-roster instinct is directly resisted; Juno remains an autonomous rival claimant rather than a bully or recruit.

`KNOWN_PAYOFF_DUTIES`
- M-002: E006 is the locked changing-count clue; one slot is office/function rather than named person.

`REENTRY_ANCHOR`
- E005 provisional-cell consequence and physical 07 post-test state.

`CURRENT_OWNER_OF_DECISION`
- each member owns their stated participation/domain condition; no one grants Rian permanent command by default.

`RIAN_CANNOT_OVERRIDE`
- withdrawal rights, medical stop, technical stop, provenance rules, community disclosure condition.

`UNRESOLVED_SOURCE_DEPENDENT_ITEMS`
- exact UI cosmetic layout beyond approved count/category function; no new slot identity.

`MUST_REFRESH_AFTER_E005_DRAFT`
- actual asset damage/loss; exact E005 liability/evaluation language; 07 post-test heat/damage; relationship pressure; any public fifth-answer framing created by the draft.

`NEW_CANON_REQUIRED: NO — PRELOAD; RECHECK AT REFRESH`

---

## E007 PRELOAD

`CONTEXT STATUS: PRELOAD / FORECAST`

`CURRENT_EXPECTED_OBJECTIVE`
- Keep 07 physically intact and usable through the ownership/stripping hearing without falsely converting several real claims into Rian's personal ownership.

`KNOWN_OPENING_DEPENDENCIES`
- E006 temporary roles/conditions; seven-day schedule; Juno workshop-cost pressure; 07 still incomplete and under inspection.

`ACTIVE_DESIRE_MAIN`
- Rian: preserve 07 for current mission/testing use.

`ACTIVE_DESIRE_SECONDARY`
- Nera/Haren/Serin/crew claimants: preserve labor, safety, data, custody and mission rights as separate claims.

`PHYSICAL_ANCHOR`
- physical tags/seals on different 07 parts/data + existing contributor/change records.

`STATE_CHANGE`
- FORECAST: 07 remains at Academy for seven days under supervised mission-use rights; title/custody/mission use/contribution/data/liability remain separated.

`COST_OR_REFUSAL`
- every use creates more sponsor/security/data/liability exposure; Nera refuses to surrender work logs without attribution/safety context.

`KNOWN_RELATIONSHIP_PRESSURE`
- Haren can rescue Rian's weak future-value argument by reframing current value; this is independent competence, not Rian delegated brilliance.

`KNOWN_PAYOFF_DUTIES`
- M-017: E007 is the locked ownership clue — several legal/technical claimants exist before Rian can use 07.

`REENTRY_ANCHOR`
- E006 conditions/schedule and Juno allocation debt; 07's physical post-test inspection state.

`CURRENT_OWNER_OF_DECISION`
- hearing/claim authorities own disposition; Nera owns her contributor-log refusal; cell can request mission use but not title.

`RIAN_CANNOT_OVERRIDE`
- claimant rights, contributor attribution, hearing disposition, unsafe-change termination.

`UNRESOLVED_SOURCE_DEPENDENT_ITEMS`
- exact hearing-chair identity and exact seal/device IDs: unresolved unless an approved source supplies them.

`MUST_REFRESH_AFTER_E006_DRAFT`
- exact temporary-role wording; any member withdrawal pressure; Juno debt; 07 condition; Archive count information already exposed.

`NEW_CANON_REQUIRED: NO — PRELOAD; RECHECK AT REFRESH`

---

## E008 PRELOAD

`CONTEXT STATUS: PRELOAD / FORECAST`

`CURRENT_EXPECTED_OBJECTIVE`
- Use the opened service documentation to prove a bounded current 07 maneuver while determining what the Imperial identification key actually grants.

`KNOWN_OPENING_DEPENDENCIES`
- seven-day mission-use bargain; service/maintenance layer opened; current 07 remains limited and physically mismatched from Rian's remembered future configuration.

`ACTIVE_DESIRE_MAIN`
- Rian: prove the service routine and preserve 07's trial value.

`ACTIVE_DESIRE_SECONDARY`
- Nera/Kara/Mia/Serin/Haren: keep the procedure within current technical, shutdown, medical, logging and movement-space limits.

`PHYSICAL_ANCHOR`
- existing Imperial identification key + service documentation + 07 moving from maintenance brace to a misaligned service cradle/port.

`STATE_CHANGE`
- FORECAST: key proves service/rescue/maintenance access rather than royal command/hidden weapon; Rian demonstrates elite timing but must accept current thruster mapping correction; 07 becomes more politically valuable/monitored.

`COST_OR_REFUSAL`
- surveillance/data restrictions rise; success accelerates Doran guarantee/medicine review pressure.

`KNOWN_RELATIONSHIP_PRESSURE`
- Nera's present mapping can stop a future-derived over-rotation; Kara retains shutdown; Mia medical check, Serin scope logging, Haren space/people clearance remain independent.

`KNOWN_PAYOFF_DUTIES`
- M-003: E008 is the first locked 07-lineage clue — incompatible civilian/rescue/military connectors, not an elegant weapons standard.
- Do not resolve the full AUXILIA/civil-interoperability origin.

`REENTRY_ANCHOR`
- E007 service-layer opening + seven-day claim/custody terms.

`CURRENT_OWNER_OF_DECISION`
- Rian owns piloting correction; Nera owns current technical map/call; Kara shutdown; Mia medical stop; Serin audit; Haren movement clearance.

`RIAN_CANNOT_OVERRIDE`
- technical mapping, shutdown, medical stop, logging/data scope, claim restrictions.

`UNRESOLVED_SOURCE_DEPENDENT_ITEMS`
- unnamed Imperial observer's personal identity; new hidden weapon; new crown access; unapproved key serial/name: unresolved / forbidden invention.

`MUST_REFRESH_AFTER_E007_DRAFT`
- exact claim/custody windows; logs preserved; current 07 repair/heat state; who observed what; liability language.

`NEW_CANON_REQUIRED: NO — PRELOAD; RECHECK AT REFRESH`

---

## E009 PRELOAD

`CONTEXT STATUS: PRELOAD / FORECAST`

`CURRENT_EXPECTED_OBJECTIVE`
- Restore current workshop/medical/07 access before the slot expires while correcting the narrow official-record error without exposing protected people through indiscriminate data release.

`KNOWN_OPENING_DEPENDENCIES`
- E008 heightened classification/surveillance; Doran deadline acceleration; 07 service maneuver completed within limits.

`ACTIVE_DESIRE_MAIN`
- Rian: restore access fast enough to keep the current repair/test path alive.

`ACTIVE_DESIRE_SECONDARY`
- Serin: correct legal effect through a source trail while protecting minors, medical data and Doran identities; Juno: ensure her group's schedule cost is recorded/compensated if she yields time.

`PHYSICAL_ANCHOR`
- access doors refusing the cell + raw sensor/manual-action records + narrow correction packet and workshop-slot clock.

`STATE_CHANGE`
- FORECAST: local correction restores access; Serin gains current audit standing; monitoring rises; query exposes physically active people with closed/duplicated/missing records, including Soma Ren.

`COST_OR_REFUSAL`
- Serin refuses raw-data dump; Juno grants only negotiated delay; Operations/Security scrutiny increases.

`KNOWN_RELATIONSHIP_PRESSURE`
- Rian's speed/transparency instinct conflicts with Serin privacy/provenance; Juno remains a claimant with a real opportunity cost.

`KNOWN_PAYOFF_DUTIES`
- Do not treat `official effect` as truth; show that a record can act before factual correction.
- Soma's body/record contradiction is the E010 reentry, not a solved identity doctrine.

`REENTRY_ANCHOR`
- E008 classification/data capture + accelerated community review.

`CURRENT_OWNER_OF_DECISION`
- Serin owns correction/provenance method; Juno owns whether to delay her slot under terms; authorized review process owns acceptance; Rian cannot publish others' protected data by fiat.

`RIAN_CANNOT_OVERRIDE`
- privacy/provenance limits, Juno's opportunity claim, official correction process.

`UNRESOLVED_SOURCE_DEPENDENT_ITEMS`
- exact wrong-identity pair/safety-violation fields beyond the approved card; exact office UI; no invented admin officer.

`MUST_REFRESH_AFTER_E008_DRAFT`
- actual surveillance level; exact data captured; Rian medical/07 state; Haren deadline; any service-lineage clue wording already exposed.

`NEW_CANON_REQUIRED: NO — PRELOAD; RECHECK AT REFRESH`

---

## E010 PRELOAD

`CONTEXT STATUS: PRELOAD / FORECAST`

`CURRENT_EXPECTED_OBJECTIVE`
- Preserve Soma Ren's immediate treatment/current-person standing without forcing restoration of an old legal identity that may reactivate custody/debt/guardian claims.

`KNOWN_OPENING_DEPENDENCIES`
- E009 closed-identity discovery; treatment renewal expires that night; cell access restored only under greater scrutiny.

`ACTIVE_DESIRE_MAIN`
- Rian initially wants to solve the contradiction quickly by restoring the old identity, then must surrender that solution when the current person refuses its consequences.

`ACTIVE_DESIRE_SECONDARY`
- Soma: keep treatment/presence without being forced back into an unwanted old legal-custody state.
- Mia: separate body/treatment need from identity solution.
- Serin: preserve present-person evidence without pretending it finally resolves identity.

`PHYSICAL_ANCHOR`
- Soma's present living body and scheduled neural/medical support in the medical bay + the closed administrative record that would deny treatment.

`STATE_CHANGE`
- FORECAST: a 72-hour treatment/presence hold preserves Soma without final identity restoration; Black Ward/medical/security bodies are notified; 07 receives movement authorization toward White Dock staging.

`COST_OR_REFUSAL`
- Soma refuses Rian's obvious-looking restoration; Rian admits the control error; institutional attention increases and Soma becomes a contested person/evidence target.

`KNOWN_RELATIONSHIP_PRESSURE`
- Soma owns limited consent; Mia owns medical necessity/stop; Serin owns provenance/current-status framing; Haren recognizes the community analogue; Rian's future-savior logic is explicitly bounded.

`KNOWN_PAYOFF_DUTIES`
- preserve the distinction among physical survival, treatment standing and old legal identity.
- M-014 Black Ward AI recognition is **not** due until E072; notification here does not authorize that protocol reveal.

`REENTRY_ANCHOR`
- E009 closed identity list + Soma treatment deadline + restored access under surveillance.

`CURRENT_OWNER_OF_DECISION`
- Soma owns current consent/refusal within capacity; Mia verifies treatment necessity; Serin records current-person evidence; Kara/medical authority signs the temporary hold. Rian explicitly does not own the identity decision.

`RIAN_CANNOT_OVERRIDE`
- Soma's consent, medical authority, record/evidence boundaries, custody-law consequence.

`UNRESOLVED_SOURCE_DEPENDENT_ITEMS`
- exact old institution/contract/guardian identity; exact medical treatment nomenclature; exact Black Ward contact official: unresolved unless supported by approved source.

`MUST_REFRESH_AFTER_E009_DRAFT`
- exact access restored; record error details; monitoring; Soma discovery wording; treatment deadline; Juno schedule debt; current 07 state.

`NEW_CANON_REQUIRED: NO — PRELOAD; RECHECK AT REFRESH`

---

# 4. Carry-Forward Refresh Gate for E002–E010

Before any PRELOAD above becomes `FULL`, execute:

1. read the previous episode's audited draft and its State Delta;
2. compare every delta against approved cards/chronology/state/loss/payoff sources;
3. preserve draft-only staging as `[DRAFT-ONLY]`, not story canon;
4. carry continuity-critical draft facts only as `[CONTINUITY-CARRY-FORWARD]`;
5. update physical state, possession/custody, location, knowledge and relationship pressure;
6. re-check clue exposure so the previous draft did not accidentally consume a later locked reveal;
7. re-check decision ownership and Rian's non-override boundary;
8. if the next episode now needs a new person/object/authority/event not supported by approved sources, set `NEW_CANON_REQUIRED: YES-STOP` for that change path;
9. otherwise promote the next pack from `PRELOAD / FORECAST` to `FULL / PRE-DRAFT-READY`.

No later pack in this file is evidence that its predicted dynamic state already occurred.

---

# 5. Red Team / Blindspot Audit — E001–E010 Context Layer

## RT-01 — Scene-card summary masquerading as Context

**Risk:** FAIL if the pack only retells beats.

**Result: PASS.** E001 adds current authority, information ceiling, physical anchor, reader-memory carrier, causality, unresolved-source fields and explicit E002 handoff. E002–E010 add refresh dependencies rather than only summaries.

## RT-02 — Abstract protagonist desire

**Risk:** `save the Empire / change history` is unusable at scene level.

**Result: PASS.** E001 desire is intake/date concealment → prevent current injury without exposing regression. Later packs likewise use immediate access, repair, test, record, treatment or rights problems.

## RT-03 — Everything moves only because Rian moves it

**Result: PASS WITH HARD GUARD.** Bram completes the E001 physical lock; Nera can reject current-machine misuse; Serin owns provenance/privacy; Mia owns medical stops; Haren owns community/manifest choices; Juno owns her opportunity claim; Soma owns consent; institutions own custody/review. Draft audit must fail if prose reassigns these choices to Rian.

## RT-04 — Decorative PHYSICAL_ANCHOR

**Result: PASS.** Anchors change what can physically happen: 07 support/lock geometry, incident log, current mount/coupler, medical stop, test module, scorecard, physical claim tags, service cradle, access doors/records, Soma's treatment state.

## RT-05 — No distinct reader-memory point

**Result: PASS.** Primary memory carriers rotate:

- E001 red-banded 07 + worker lock/service response;
- E002 incident record and 36-person consequence;
- E003 Nera's physical measurement/current-machine correction;
- E004 blank Orpheus fields + medical stop;
- E005 costly closed-choice rescue;
- E006 13/12/13 scorecard/category mismatch;
- E007 physical multi-claim tags on one frame;
- E008 service cradle maneuver / key grants service, not throne;
- E009 locked doors because the record acts first;
- E010 living body versus closed identity.

## RT-06 — Cost/refusal removed for convenience

**Result: PASS.** Every episode has a source-supported refusal, liability, body cost, opportunity cost, surveillance increase, rights limit or authority boundary. No new casualty is used to prove seriousness.

## RT-07 — Reentry vague / episodic reset

**Result: PASS.** Each pack names a concrete prior carrier and the refresh gate requires state delta before the next FULL pack.

## RT-08 — State transfer missing

**Result: PASS.** Run-local State Delta requires character, possession, location, relationship, knowledge, cost/loss, debt, authority, hook, tangible state and recurring-carrier state.

## RT-09 — PRELOAD silently becoming future canon

**Result: PASS WITH LABEL GUARD.** E002–E010 are explicitly `PRELOAD / FORECAST`; expected `STATE_CHANGE` is the approved AS envelope, not evidence that a draft already produced it. Dynamic fields must refresh episode by episode.

## RT-10 — Unsupported face/asset/place/technology/authority invented

**Result: PASS.** Exact unsupported details are intentionally left `UNRESOLVED FROM APPROVED SOURCES`. No new named exemplar, facility, device or authority is created.

## RT-11 — Locked losses conveniently restored or inflated

**Result: PASS.** The loss ledger contains no E001–E010 locked death/permanent-loss event. This pack neither restores later losses nor invents early permanent casualties.

## RT-12 — Foreshadow/payoff duplication or early exposure

**Result: PASS WITH WATCH ITEMS.** Hard timing guards retained:

- E001 regression-cause clue remains ambiguous;
- E002 unrecorded-status follow-up, not origin solution;
- E004 first locked Original Orpheus clue;
- E006 changing-count clue;
- E007 ownership clue;
- E008 first locked 07-lineage clue;
- formal later `Blood Admiral`, Black Ward/Authority/Seed reveals are not pulled forward.

## RT-13 — Same emotional/event pattern repeated E001–E010

**Result: PASS.** The dominant engines deliberately rotate: accident → liability → repair authority → memory/medical uncertainty → closed-choice process → contract/roles → ownership → service maneuver → record effect/privacy → personhood/treatment consent.

## RT-14 — Context Pack heavier than the manuscript

**Result: PASS FOR PRODUCTION, WATCH ON REFRESH.** One file stores one FULL pack and nine compact PRELOADs. Future refresh should update the affected episode section/state delta only; do not append redundant summaries of all previous episodes.

---

## 6. Integrated Verdict

- `E001 WRITING READINESS: READY`
- `E002–E010 CONTEXT STATUS: PRELOAD / FORECAST`
- `NEW CANON REQUIRED FOR CURRENT CONTEXT WORK: NO`
- `CANON MUTATION: 0`
- `PERMANENT LOSS MUTATION: 0`
- `RELATIONSHIP/AUTHORITY MUTATION: 0`
- `PUBLICATION: NOT AUTHORIZED`

Next authorized production action after this Context Pack is validated/merged: load E001 v1 + current E001 v2, perform v1 diagnosis against approved scene cards/canon, then prepare the next E001 v2 revision candidate through the manuscript workflow. Manuscript AUTHOR-APPROVED promotion and manuscript PR final merge remain author-only decisions.
