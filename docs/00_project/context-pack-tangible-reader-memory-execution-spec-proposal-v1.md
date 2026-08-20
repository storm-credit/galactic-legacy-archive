# Context Pack Tangible Reader-Memory Execution Spec Proposal v1

Status: PROPOSED — NONCANON WORKFLOW/QC
Effective Authority: NC
Canon Promotion: NOT AUTHORIZED
Publication: NOT AUTHORIZED
Owner Agents: A00 PM / A11 Prose & Serialization / N03 Episode / X02 Reader Memory / X04 Continuity / O01 Canon
Last Reviewed: 2026-08-20
Depends On: [[manuscript-production-workflow-v1]], [[effective-canon-status-manifest-v1]], [[continuity-issues]], [[ga4-ga7-ga8-ga9-tangible-execution-and-reader-memory-overlay-v1]], [[high-watch-tangible-carrier-matrix-ga4-ga7-ga8-ga9-v1]], approved episode cards and current state/loss/payoff ledgers
Used By: future episode Context Pack production and prose execution audit after separate adoption decision
Open Risks: current `main` does not expose a dedicated canonical Context Pack schema file or the exact literal field names listed below; this proposal therefore normalizes execution semantics without modifying project-control workflow or scene cards.

---

## 0. Purpose

PR #191 found no missing late-series foundation plot/lore blocker. The remaining risk is execution: an approved political, legal, archival or institutional event can become abstract prose even when the detailed cards already contain people, assets, places and consequences.

This proposal connects that QC result to Context Pack production **without changing canon events, cards or the project-control workflow**.

The target reader sequence is:

> current person / ship / place problem → choice or refusal → visible physical/service change → only then abstract rule, institution, Seed or record explanation

This is an execution ordering rule, not a license to create new content.

---

## 1. Preflight Findings and Assumption

### 1.1 Repository finding

Current `main` was checked before this proposal.

- `manuscript-production-workflow-v1.md` defines the manuscript pipeline and required inputs but does not contain a dedicated Context Pack field schema.
- repository search for the exact literals `ACTIVE_DESIRE_MAIN`, `ACTIVE_DESIRE_SECONDARY`, `PHYSICAL_ANCHOR`, `STATE_CHANGE`, `COST_OR_REFUSAL`, `REENTRY_ANCHOR` did not locate a current main schema file.
- current control/production documents nevertheless establish the required semantics: approved card goal/choice/cost/state change, current canon/state/loss constraints, prose/retention audit, and no-silent-rewrite.
- PR #191 already contains two overlapping HIGH-WATCH Context Pack vocabularies: the overlay uses `TANGIBLE_*`, while the carrier matrix uses `RECURRING_*` / `VISIBLE_DELTA_THIS_EP`.

### 1.2 [ASSUMPTION]

The six GA-wide fields supplied in the current handoff are treated as the intended common Context Pack execution slots:

```text
ACTIVE_DESIRE_MAIN
ACTIVE_DESIRE_SECONDARY
PHYSICAL_ANCHOR
STATE_CHANGE
COST_OR_REFUSAL
REENTRY_ANCHOR
```

This proposal does **not** declare those literals Project-Control Canon. It defines a single noncanon mapping so future adoption cannot create three competing schemas.

If a pre-existing canonical Context Pack schema is later located, that higher-authority schema wins and this proposal must be remapped rather than duplicated.

---

## 2. Non-Negotiable Boundary

A Context Pack may select, foreground and order already-approved material. It may not create or silently alter it.

Forbidden through this spec:

- new plot event;
- new death, injury or permanent loss;
- resurrection or recovery of an irreversible loss;
- new ability, technology, authority or institutional power;
- new relationship state;
- new species/faction/mecha/ship/relic merely to provide tangibility;
- changed number, date, sentence, responsibility allocation or ending;
- new named character solely to fill a FACE field;
- transfer of a local/medical/archive/service decision to Rian;
- rewrite of approved scene cards;
- `AUTHOR-APPROVED`, canon promotion or publication authorization.

If a required execution carrier cannot be obtained from approved cards/bibles/state ledgers, record `NEW_CANON_REQUIRED: YES` and stop that change path.

---

## 3. Source Precedence for Context Pack Population

Populate fields from the highest available authority, in this order:

1. current explicit author instruction and Project-Control Canon / errata;
2. master chronology, state, loss and payoff ledgers;
3. relevant Working Canon bible;
4. approved act/subact/episode structure and exact detailed card at that episode;
5. approved QC constraint that does not create facts;
6. noncanon proposal only as an execution lens, never as a fact source;
7. manuscript prose last.

A field may be `NONE`, `N/A` or `UNRESOLVED FROM APPROVED SOURCES`. It must never be filled by invention just because the template has a blank.

---

## 4. GA-Wide Common Field Contract

These six fields are the common execution layer for ordinary and HIGH-WATCH episodes.

| Field | Meaning | Allowed source | Hard guard |
|---|---|---|---|
| `ACTIVE_DESIRE_MAIN` | the current focal actor/community's immediate want, refusal or action pressure | episode card goal/choice + current character/faction state | do not convert a future title/role into present desire |
| `ACTIVE_DESIRE_SECONDARY` | one competing current desire that materially pressures the same episode | existing secondary actor/community/card pressure | optional; `NONE` is preferable to inventing a conflict |
| `PHYSICAL_ANCHOR` | already-existing person-held object, ship/frame/cargo/service hardware, record medium or concrete place through which the episode is experienced | card + relevant bible/state | no new relic, special device, facility or dedicated machine |
| `STATE_CHANGE` | the approved end-state delta of person/asset/place/service/authority after the episode | decisive choice/result/cost/state ledger | must not add a result absent from approved structure |
| `COST_OR_REFUSAL` | existing time/material/trust/access/health/autonomy/role cost or explicit refusal | episode card/canon loss/state | no casualty inflation or punishment inflation |
| `REENTRY_ANCHOR` | familiar existing person/ship/place/scar/service/record returning in a changed state | prior cards + current continuity | optional; do not move a carrier impossibly to force reuse |

### 4.1 General episode rule

For a normal episode, these six fields are enough. Do **not** add HIGH-WATCH-only carrier rows automatically.

### 4.2 No mechanical formula

The fields are preparation checks, not a mandatory prose order for every paragraph. An episode can legitimately have:

- no secondary desire;
- no re-entry anchor;
- a place as the physical anchor rather than a portable asset;
- a cost that becomes visible in the next approved episode rather than the same one.

The purpose is to prevent abstraction drift, not to make every episode look identical.

---

## 5. HIGH-WATCH Minimal Addendum

Only the nine HIGH-WATCH bands identified by PR #191 require extra stored checks:

1. GA4 E431–438
2. GA7 E716–723
3. GA7 E776–783
4. GA7 E784–790
5. GA8 E836–843
6. GA8 E851–860
7. GA8 E861–868
8. GA9 E926–935
9. GA9 E936–943

### 5.1 Store only the non-duplicative additions

```text
HIGH_WATCH_BAND:
RECURRING_FACE:
RECURRING_ASSET:
RECURRING_PLACE:
CURRENT_OWNER_OF_DECISION:
RIAN_CANNOT_OVERRIDE:
ABSTRACT_CONCEPTS_FOREGROUNDED:
NEW_CANON_REQUIRED: NO / YES-STOP
```

`HIGH_WATCH_BAND` is an identifier. The remaining seven rows are the extra HIGH-WATCH execution checks.

### 5.2 Do not store duplicate aliases

The following PR #191 labels are **validation aliases**, not additional Context Pack fields:

| HIGH-WATCH check | Canonical pack value to inspect | Do not duplicate as |
|---|---|---|
| FACE | `RECURRING_FACE` + actor named by `ACTIVE_DESIRE_MAIN` | `TANGIBLE_FACE` |
| ASSET | `RECURRING_ASSET` and/or `PHYSICAL_ANCHOR` | `TANGIBLE_ASSET` |
| PLACE | `RECURRING_PLACE` and/or `PHYSICAL_ANCHOR` | `TANGIBLE_PLACE` |
| DELTA | `STATE_CHANGE` | `VISIBLE_DELTA`, `VISIBLE_DELTA_THIS_EP` |
| COST | `COST_OR_REFUSAL` | another cost field |
| REENTRY | `REENTRY_ANCHOR` | `PREVIOUS_REENTRY_ANCHOR` as a second copy |

This resolves the vocabulary overlap between the existing PR #191 overlay and carrier matrix without editing those historical proposal files.

### 5.3 Optional planning note, not a stored field

`NEXT_PHYSICAL_PAYOFF` from the carrier matrix can be used as a drafting note when the detailed card explicitly supports a same/next-episode payoff. It must not become a promise generator and therefore is not part of the minimum stored schema.

---

## 6. HIGH-WATCH Field Semantics

### `RECURRING_FACE`

Who already exists in approved material and carries a current want/refusal/consequence across this band?

Allowed:
- existing named character;
- existing role/community already present in cards;
- existing unnamed role if no exact name is required by prose.

Not allowed:
- inventing a named exemplar because a legal or archival concept feels abstract.

### `RECURRING_ASSET`

Which already-existing ship, cargo, record, relay, clinic/service asset, repair equipment or other hard asset can preserve reader memory across the band?

It may equal `PHYSICAL_ANCHOR`.

### `RECURRING_PLACE`

Which already-defined route, workspace, node, habitat, clinic, yard, archive/service environment or other place carries multiple consequences?

It may equal `PHYSICAL_ANCHOR` when the place itself is the episode's physical anchor.

### `CURRENT_OWNER_OF_DECISION`

Who is already authorized by canon/cards to make the decisive choice?

This is a custody/agency guard. It must reproduce current decision ownership, not redesign it.

### `RIAN_CANNOT_OVERRIDE`

What decision, service, medical, local, archival or affected-party authority remains outside Rian's unilateral control in this episode?

Use `N/A` only when the episode has no meaningful Rian-involvement/authority risk.

### `ABSTRACT_CONCEPTS_FOREGROUNDED`

Recommended maximum: 1–2 newly foregrounded abstract concepts per episode.

This is a readability guard, **not a lore-deletion rule**. More concepts may remain present if already required by the card, but the prose should foreground at most the concepts necessary to understand the current carrier problem before widening.

### `NEW_CANON_REQUIRED`

Default `NO`.

If `YES`, do not improvise. Record the blocked need and route it through normal change control.

---

## 7. Population Algorithm

For each episode Context Pack:

1. load the exact episode card and current chronology/state/loss/payoff constraints;
2. identify the current focal actor and approved decisive choice;
3. fill `ACTIVE_DESIRE_MAIN` from that current want/refusal, not from the character's future destiny;
4. fill `ACTIVE_DESIRE_SECONDARY` only if an existing competing current desire actually changes the scene;
5. choose one strongest existing `PHYSICAL_ANCHOR` already supported by card/bible;
6. copy the approved result into `STATE_CHANGE`;
7. copy the approved cost/refusal into `COST_OR_REFUSAL`;
8. look backward for an existing carrier whose changed state can legitimately re-enter; otherwise use `NONE`;
9. if not HIGH-WATCH, stop the tangible mapping here;
10. if HIGH-WATCH, load the existing carrier matrix row and fill the `HIGH_WATCH_BAND` identifier plus the seven execution checks in §5.1;
11. verify current physical location/time of every recurring carrier;
12. verify decision owner and Rian authority boundary;
13. if any field requires new canon, set `NEW_CANON_REQUIRED: YES-STOP` and do not draft that invention.

---

## 8. Prose Execution Order

This proposal does not force every scene to begin identically. When abstraction risk is present, prefer:

1. current FACE/PLACE/ASSET condition;
2. immediate desire, refusal or operational problem;
3. approved choice;
4. visible `STATE_CHANGE` / `COST_OR_REFUSAL`;
5. only then the institutional/legal/Seed/archive explanation needed to understand what happened;
6. re-entry or next approved concrete problem.

Reader-memory objective:

> not “I learned another rule,” but “the person/ship/place I already know is different because of this rule.”

---

## 9. Five-Episode Window Guard

The HAPΔ principle remains a **window-level guard**, not a per-episode formula.

Across most five-episode windows inside a HIGH-WATCH band, the draft should make it possible to answer:

- FACE — who currently wants/refuses/loses something?
- ASSET — what tangible thing/service is being carried, moved, repaired, blocked or used?
- PLACE — where does the rule matter in lived space?
- DELTA — what approved state changed?
- COST — what current cost/refusal became visible?
- REENTRY — what familiar carrier returned in a changed state?

Do not create a new object or character merely because one individual episode has no independent answer to all six.

---

## 10. Draft Audit Integration

The Context Pack is an input/guard layer. It does not replace the existing manuscript workflow.

### Before workflow §3.1 drafting

- load cards + current state + voice/prose constraints;
- populate the common six fields;
- populate HIGH-WATCH addendum only when applicable.

### During §3.2 structure/causality/motivation audit

Check:
- `ACTIVE_DESIRE_MAIN` actually drives a choice;
- `STATE_CHANGE` matches the approved card;
- no invented transition was inserted to make the episode more tangible.

### During §3.3 canon/continuity audit

Check:
- all carriers existed and could physically be present;
- loss/authority/relationship states match current canon;
- `CURRENT_OWNER_OF_DECISION` was not reassigned;
- `NEW_CANON_REQUIRED` remains `NO`.

### During §3.4 prose audit

For HIGH-WATCH:
- current problem is visible before extended abstraction where practical;
- the same information is not repeated in table/UI/dialogue/narration;
- physicality is functional, not decorative sensory padding;
- no new object was inserted solely for texture.

### During §3.5 retention/hook audit

Prefer the next question to remain attached to a person/ship/place/current consequence when the approved hook allows it. Do not replace the approved hook with a new tangible hook.

---

## 11. HIGH-WATCH Draft Fail Conditions

For HIGH-WATCH drafts, review these seven questions:

1. Is there a visible current person/place/object or service condition early enough that the abstract issue has a carrier?
2. Does the reader see the present problem before or alongside the explanation of the rule?
3. Does the episode end with the approved state actually changed or its approved consequence clearly pending?
4. Is the same information being repeated through UI/table/dialogue/narration?
5. Was a new exemplar created even though an existing person/ship/place could carry the consequence?
6. Did Rian absorb another actor's decision, authority or credit?
7. Is reader curiosity attached to what happens to a known carrier as well as to the abstract answer?

If two or more of 3/4/5/7 fail, return to prose revision **without rewriting the scene card**.

Any failure on 6 or `NEW_CANON_REQUIRED=YES` is a stop/escalation condition, not a prose-polish task.

---

## 12. Overcorrection Guards

Reject:

- adding combat/raid/chase to every meeting;
- teleporting recurring characters between physically incompatible locations;
- turning every record into a relic;
- adding decorative smell/light/texture that moves no action, information, relation, risk or cost;
- using new higher-tier mecha as a late-series tangibility patch;
- giving every key character a dedicated machine/weapon;
- adding injury/death to prove cost;
- reducing GA8/GA9 intellectual complexity into one villain or one simple rule;
- making every five-episode window mechanically identical;
- treating a warrant, record or interface as a magical ownership item.

---

## 13. Impact Audit

### `manuscript-production-workflow-v1.md`

**NO CHANGE IN PR #191.**

Reason:
- current workflow already has the correct authority boundaries and audit stages;
- this proposal can operate as an additive preparation/QC layer;
- modifying Project-Control/production workflow before the proposal is approved would raise authority unnecessarily.

Future adoption, if explicitly approved, should add at most a short reference from the workflow to one Context Pack source of truth rather than copying this field list into multiple files.

### Scene cards / act maps / chronology

**NO CHANGE.**

This spec reads them; it does not rewrite them.

### Canon / decision log

**NO CANON CHANGE. NO ACCEPTED DECISION ENTRY.**

This file is proposal-level only.

### Manuscript

**NO CHANGE.**

The proposal prepares future drafting/audit inputs and does not itself revise prose.

### PR #191 existing overlay/matrix

**NO RETROACTIVE EDIT REQUIRED NOW.**

Their two schemas remain historical proposal evidence. This file is the normalization layer future Context Packs should consult if/when adopted.

---

## 14. Worked Mapping Examples — Structure Only

These examples show field mapping, not new plot.

### GA7 E776–783 band

- `ACTIVE_DESIRE_MAIN`: use the current affected actor/Haren/claimant desire already specified by the exact episode card.
- `PHYSICAL_ANCHOR`: existing Lin/D4/service/restitution records or current service environment already present in approved sources.
- `STATE_CHANGE`: existing sanction/access/role/restitution/model-governance delta from the exact card.
- `COST_OR_REFUSAL`: existing loss of role/access/service/time/trust; never a new victim.
- `RECURRING_FACE`: Haren + existing affected/saved constituencies as physically possible in that episode.
- `CURRENT_OWNER_OF_DECISION`: existing hearing/service/affected-party authority, not Rian by default.

### GA8 E851–860 band

- `PHYSICAL_ANCHOR`: existing maintenance/translation/archive/service infrastructure.
- `STATE_CHANGE`: only the approved observation/ranking/credential/enforcement interpretation or current service effect of that episode.
- `RECURRING_FACE`: existing Palimpsest maintainers/translators/operators/community actors.
- `ABSTRACT_CONCEPTS_FOREGROUNDED`: select the 1–2 concepts needed for that current carrier problem; do not erase the rest of the approved architecture.

### GA9 E926–943 bands

- `REENTRY_ANCHOR`: same approved settlement/household/crew/clinic/service chain where physically continuous.
- `STATE_CHANGE`: each existing door closing/reopening or route/service remedy specified by cards.
- `COST_OR_REFUSAL`: current slower/costlier route, delayed repair, access limit or other approved consequence.
- `RIAN_CANNOT_OVERRIDE`: affected/community/local/medical/technical decision rights remain distinct.

---

## 15. Completion Criteria

This mapping is usable when:

1. ordinary episodes need only the common six slots;
2. HIGH-WATCH episodes add no duplicate DELTA/COST/REENTRY storage;
3. HIGH-WATCH recurring carriers come only from existing approved sources;
4. current time/location continuity is checked before reuse;
5. decision ownership is explicitly preserved;
6. no new proper noun is required just to complete a template;
7. no plot/lore/death/ability/relationship/authority change is introduced;
8. `manuscript-production-workflow-v1.md` and scene cards remain untouched;
9. this proposal remains NONCANON until a later explicit adoption/promotion decision.

---

## 16. Final Ruling

> **CONTEXT PACK TANGIBLE EXECUTION BRIDGE: READY AT PROPOSAL LEVEL**
>
> **GENERAL STORED FIELDS: 6**
>
> **HIGH-WATCH BAND IDENTIFIER: 1 + EXTRA EXECUTION CHECKS: 7**
>
> **DUPLICATE DELTA/COST/REENTRY FIELDS: REMOVED BY MAPPING, NOT BY EDITING HISTORY**
>
> **SCENE-CARD REWRITE: 0**
>
> **NEW PLOT / LORE / DEATH / ABILITY / RELATIONSHIP / AUTHORITY: 0**
>
> **CANON CHANGE: 0**
>
> **WORKFLOW CONTROL FILE CHANGE: 0**
>
> **MANUSCRIPT CHANGE: 0**
>
> **PR #191 FINAL MERGE: NOT AUTHORIZED**
