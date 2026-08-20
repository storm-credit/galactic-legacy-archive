# Context Pack Tangible Reader-Memory Execution Spec v1

Status: CANON — PROJECT-CONTROL WORKFLOW/QC
Effective Authority: PC — workflow/QC execution only
Story Canon Effect: NONE
Canon Promotion: WORKFLOW/QC ADOPTED — D-20260820-01
Publication: NOT AUTHORIZED
Owner Agents: A00 PM / A11 Prose & Serialization / N03 Episode / X02 Reader Memory / X04 Continuity / O01 Canon
Last Reviewed: 2026-08-20
Depends On: [[manuscript-production-workflow-v1]], [[effective-canon-status-manifest-v1]], [[continuity-issues]], [[ga4-ga7-ga8-ga9-tangible-execution-and-reader-memory-overlay-v1]], [[high-watch-tangible-carrier-matrix-ga4-ga7-ga8-ga9-v1]], [[ga7-e716-723-context-pack-dry-run-v1]], [[ga8-e851-860-context-pack-dry-run-v1]], [[context-pack-workflow-adoption-impact-review-2026-08-20]], approved episode cards and current state/loss/payoff ledgers
Used By: all episode Context Pack production, manuscript §3.1 drafting preparation and §3.3 canon/continuity audit
Open Risks: this file governs execution/QC fields only. It cannot create story facts, promote scene cards, alter deaths/relationships/authority/ending, or authorize publication. If approved sources do not support a field, use `NONE`, `N/A` or `UNRESOLVED FROM APPROVED SOURCES` rather than invention.

---

## 0. Adoption Record

This file began in PR #191 as a NONCANON normalization proposal because current `main` had no dedicated canonical Context Pack field schema and two HIGH-WATCH proposal vocabularies overlapped.

Validation then proceeded before adoption:

- PR #191: field normalization proposal and HIGH-WATCH carrier mapping;
- PR #192: GA7 E716–723 dry-run, **8/8 PASS**;
- PR #192: GA8 E851–860 dry-run, **10/10 PASS**;
- cross-mode result: legal/attribution and Seed/archive failure modes both worked with one schema;
- PR #193: narrow workflow-adoption impact review, **TECHNICALLY READY**;
- author instruction 2026-08-20: Option C adoption approved.

Ruling:

> This document is now the single Project-Control source of truth for Context Pack tangible reader-memory execution/QC fields.

The historical filename retains `proposal` for link stability. Its current status, not the filename, determines authority.

This adoption does **not** promote PR #191 visual/species/relic proposals, does not modify any scene-card fact, and does not make manuscript prose canon.

---

## 1. Purpose

Approved political, legal, archival or institutional events can become abstract prose even when detailed cards already contain people, assets, places and consequences.

The Context Pack therefore carries a small execution layer that helps the draft foreground approved concrete consequences without changing them.

Preferred reader sequence when abstraction risk is present:

> current person / ship / place problem → choice or refusal → visible physical/service change → only then abstract rule, institution, Seed or record explanation

This is an execution-ordering and QC rule, not permission to add content.

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
- new facility, room, device or object ID solely to fill a physical field;
- transfer of a local/medical/archive/service decision to Rian;
- rewrite of approved scene cards;
- `AUTHOR-APPROVED` promotion or publication authorization.

If approved sources do not identify an exact person, object, room or other carrier, the field may remain `UNRESOLVED FROM APPROVED SOURCES`.

For HIGH-WATCH packs, if execution genuinely requires a new story fact, set:

`NEW_CANON_REQUIRED: YES-STOP`

and stop that change path. Do not improvise the missing fact.

---

## 3. Source Precedence for Context Pack Population

Populate fields from the highest available authority, in this order:

1. current explicit author instruction and Project-Control Canon / errata;
2. master chronology, state, loss and payoff ledgers;
3. relevant Working Canon bible;
4. approved act/subact/episode structure and exact detailed card at that episode;
5. approved QC constraint that does not create facts;
6. NONCANON proposal only as an execution lens, never as a fact source;
7. manuscript prose last.

A field may be `NONE`, `N/A` or `UNRESOLVED FROM APPROVED SOURCES`. A template blank is never itself evidence that new canon must be created.

---

## 4. GA-Wide Common Field Contract

All episode Context Packs use these six execution slots.

```text
ACTIVE_DESIRE_MAIN:
ACTIVE_DESIRE_SECONDARY:
PHYSICAL_ANCHOR:
STATE_CHANGE:
COST_OR_REFUSAL:
REENTRY_ANCHOR:
```

| Field | Meaning | Allowed source | Hard guard |
|---|---|---|---|
| `ACTIVE_DESIRE_MAIN` | current focal actor/community's immediate want, refusal or action pressure | exact card goal/choice + current character/faction state | do not convert a future title/role into present desire |
| `ACTIVE_DESIRE_SECONDARY` | one competing current desire that materially pressures the episode | existing secondary actor/community/card pressure | optional; `NONE` is preferable to invented conflict |
| `PHYSICAL_ANCHOR` | existing object, ship/frame/cargo/service hardware, record medium, work system or concrete place through which the episode can be experienced | card + relevant bible/state | no new relic, special device, facility or dedicated machine |
| `STATE_CHANGE` | approved end-state delta of person/asset/place/service/authority | decisive choice/result/cost/state ledger | do not add a result absent from approved structure |
| `COST_OR_REFUSAL` | existing time/material/trust/access/health/autonomy/role cost or explicit refusal | episode card/canon loss/state | no casualty or punishment inflation |
| `REENTRY_ANCHOR` | familiar existing person/ship/place/scar/service/record returning in a changed state | prior cards + current continuity | optional; never break time/location continuity to force reuse |

### 4.1 `PHYSICAL_ANCHOR` is functional, not decorative

The GA8 dry-run confirmed that physicality is not limited to a portable prop. An existing maintenance system, record medium, custody environment, clinic/service system, route-control environment or other work system can be the anchor when that is what the approved card actually contains.

Do not invent a glowing device or dedicated artifact to make an abstract concept feel physical.

### 4.2 No mechanical formula

The six slots are preparation and audit checks, not a required six-beat scene formula.

An episode can legitimately have:

- no secondary desire;
- no re-entry anchor;
- a place/work system as the physical anchor;
- a cost whose approved visibility lands in the next episode.

The purpose is to prevent abstraction drift, not to make every episode identical.

---

## 5. HIGH-WATCH Minimal Addendum

Only the nine currently identified HIGH-WATCH bands require the additional stored checks below:

1. GA4 E431–438
2. GA7 E716–723
3. GA7 E776–783
4. GA7 E784–790
5. GA8 E836–843
6. GA8 E851–860
7. GA8 E861–868
8. GA9 E926–935
9. GA9 E936–943

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

`HIGH_WATCH_BAND` is one identifier. The remaining seven rows are the extra HIGH-WATCH execution checks.

### 5.1 Duplicate aliases are validation language only

| HIGH-WATCH check | Stored pack value to inspect | Do not duplicate as |
|---|---|---|
| FACE | `RECURRING_FACE` + actor in `ACTIVE_DESIRE_MAIN` | `TANGIBLE_FACE` |
| ASSET | `RECURRING_ASSET` and/or `PHYSICAL_ANCHOR` | `TANGIBLE_ASSET` |
| PLACE | `RECURRING_PLACE` and/or `PHYSICAL_ANCHOR` | `TANGIBLE_PLACE` |
| DELTA | `STATE_CHANGE` | `VISIBLE_DELTA`, `VISIBLE_DELTA_THIS_EP` |
| COST | `COST_OR_REFUSAL` | another cost field |
| REENTRY | `REENTRY_ANCHOR` | `PREVIOUS_REENTRY_ANCHOR` as a second copy |

Historical PR #191 overlay/matrix wording remains valid as QC history, but future Context Packs store the normalized fields defined here.

`NEXT_PHYSICAL_PAYOFF` may be used as a drafting note only when an exact approved card already supports it. It is not a required stored field and must never generate a promise or event.

---

## 6. HIGH-WATCH Field Semantics

### `RECURRING_FACE`

An existing named character, existing role/community, or existing unnamed role that carries a current want/refusal/consequence across the band.

Do not invent a named exemplar because a legal, institutional or archival concept feels abstract.

### `RECURRING_ASSET`

An existing ship, cargo, record, relay, clinic/service asset, repair equipment, custody package or other hard/work asset that can preserve reader memory across the band.

It may equal `PHYSICAL_ANCHOR`.

### `RECURRING_PLACE`

An already-defined route, workspace, node, habitat, clinic, yard, archive/service environment or other place that carries multiple consequences.

It may equal `PHYSICAL_ANCHOR` when the place itself is the episode anchor.

### `CURRENT_OWNER_OF_DECISION`

The actor or institution already authorized by canon/cards to make the decisive choice.

This is an agency/custody guard. It reproduces current decision ownership; it does not redesign it.

The GA7 dry-run confirmed this field is especially important in legal/attribution episodes where authentication, assembly, signing, review and physical execution can belong to different actors.

### `RIAN_CANNOT_OVERRIDE`

The meaningful decision, service, medical, local, archival, cultural, technical or affected-party authority that remains outside Rian's unilateral control.

Use `N/A` only when the episode presents no meaningful Rian-involvement/authority risk.

### `ABSTRACT_CONCEPTS_FOREGROUNDED`

Recommended maximum: 1–2 newly foregrounded abstract concepts per episode.

This is a readability guard, not a lore-deletion rule. Required background concepts may remain present, but prose should foreground only what is necessary to understand the current carrier problem before widening.

### `NEW_CANON_REQUIRED`

Default `NO`.

If `YES`, drafting may continue only around unaffected approved material. The missing change itself is blocked and routed through normal canon-change procedure.

---

## 7. Population Algorithm

For each episode Context Pack:

1. load the exact episode card and current chronology/state/loss/payoff constraints;
2. identify the current focal actor and approved decisive choice;
3. fill `ACTIVE_DESIRE_MAIN` from that current want/refusal, not future destiny;
4. fill `ACTIVE_DESIRE_SECONDARY` only if an existing competing desire changes the scene;
5. choose the strongest existing `PHYSICAL_ANCHOR` supported by approved sources;
6. copy the approved result into `STATE_CHANGE`;
7. copy the approved cost/refusal into `COST_OR_REFUSAL`;
8. look backward for a physically continuous existing carrier whose changed state can re-enter; otherwise `NONE`;
9. if not HIGH-WATCH, stop the tangible mapping here;
10. if HIGH-WATCH, load the current carrier-matrix row and fill `HIGH_WATCH_BAND` plus the seven checks;
11. verify current time/location of every recurring carrier;
12. verify decision owner and Rian authority boundary;
13. leave unsupported exact details `UNRESOLVED FROM APPROVED SOURCES`;
14. if execution requires new story canon, set `NEW_CANON_REQUIRED: YES-STOP` and do not invent it.

---

## 8. Prose Execution Order

When abstraction risk is present, prefer:

1. current FACE/PLACE/ASSET condition;
2. immediate desire, refusal or operational problem;
3. approved choice;
4. visible `STATE_CHANGE` / `COST_OR_REFUSAL`;
5. only then institutional/legal/Seed/archive explanation required to understand what happened;
6. re-entry or next approved concrete problem.

Reader-memory objective:

> not “I learned another rule,” but “the person/ship/place I already know is different because of this rule.”

This does not force every scene to start or end the same way.

---

## 9. Five-Episode Window Guard

HAPΔ remains a **window-level guard**, not a per-episode formula.

Across most five-episode windows inside a HIGH-WATCH band, the draft should make it possible to answer:

- FACE — who currently wants/refuses/loses something?
- ASSET — what tangible thing/service is being carried, moved, repaired, blocked or used?
- PLACE — where does the rule matter in lived space?
- DELTA — what approved state changed?
- COST — what current cost/refusal became visible?
- REENTRY — what familiar carrier returned in a changed state?

Do not create a new object or character merely because one individual episode lacks an independent answer to all six.

---

## 10. Manuscript Workflow Integration

This spec is an input/guard layer. It does not add a ninth manuscript-production stage and does not replace [[manuscript-production-workflow-v1]].

### Before workflow §3.1 drafting

- load cards + current state + voice/prose constraints;
- populate the common six fields;
- populate the HIGH-WATCH addendum only when applicable;
- preserve `UNRESOLVED FROM APPROVED SOURCES` instead of inventing a missing exact carrier.

### During §3.2 structure/causality/motivation audit

Check:

- `ACTIVE_DESIRE_MAIN` actually drives an approved choice;
- `STATE_CHANGE` matches the approved card;
- no invented transition was inserted merely to make the episode tangible.

### During §3.3 canon/continuity audit

Check:

- every asserted carrier existed and could physically be present;
- loss/authority/relationship states match current canon;
- `CURRENT_OWNER_OF_DECISION` was not reassigned;
- unsupported exact details remain unresolved rather than fabricated;
- `NEW_CANON_REQUIRED` remains `NO` for any drafted change.

### During §3.4 prose audit

For HIGH-WATCH:

- current problem is visible before extended abstraction where practical;
- information is not repeated in table/UI/dialogue/narration;
- physicality is functional, not decorative sensory padding;
- no new object was inserted solely for texture.

### During §3.5 retention/hook audit

Prefer the next question to remain attached to a person/ship/place/current consequence when the approved hook allows it. Never replace the approved hook with a newly invented tangible hook.

---

## 11. HIGH-WATCH Fail Conditions

Review these seven questions:

1. Is there a visible current person/place/object/service condition early enough that the abstract issue has a carrier?
2. Does the reader see the present problem before or alongside explanation of the rule?
3. Does the episode end with the approved state changed or its approved consequence clearly pending?
4. Is the same information repeated through UI/table/dialogue/narration?
5. Was a new exemplar created even though an existing person/ship/place could carry the consequence?
6. Did Rian absorb another actor's decision, authority or credit?
7. Is reader curiosity attached to what happens to a known carrier as well as to the abstract answer?

If two or more of 3/4/5/7 fail, return to prose revision **without rewriting the scene card**.

Any failure on 6, or any required drafted change with `NEW_CANON_REQUIRED=YES`, is a stop/escalation condition rather than prose polish.

---

## 12. Overcorrection Guards

Reject:

- adding combat/raid/chase to every meeting;
- teleporting recurring characters between incompatible locations;
- turning every record into a relic;
- decorative smell/light/texture that moves no action, information, relation, risk or cost;
- using new higher-tier mecha as a late-series tangibility patch;
- giving every key character a dedicated machine/weapon;
- adding injury/death to prove cost;
- reducing GA8/GA9 complexity into one villain or one simple rule;
- making every five-episode window mechanically identical;
- treating a warrant, record or interface as a magical ownership item.

---

## 13. Validated Dry-Run Findings

### GA7 E716–723

- 8/8 episode mapping PASS;
- one schema preserved 212 total records, 97 usable, 29/41/27 comparison groups and layered responsibility;
- `CURRENT_OWNER_OF_DECISION` and `RIAN_CANNOT_OVERRIDE` prevented one-person/one-key simplification;
- exact room/person details absent from approved sources were left unresolved rather than invented;
- new plot/lore/death/authority: 0.

### GA8 E851–860

- 10/10 episode mapping PASS;
- one schema preserved Seed-0/1/2/3 separation, 6,240 analytical subset, 48-case audit and 2,400-item sandbox arithmetic;
- `PHYSICAL_ANCHOR` successfully used existing work systems/records/custody/service environments rather than new artifacts;
- no single inventor/master machine was created;
- new plot/lore/death/authority: 0.

Cross-mode ruling:

> legal-attribution and archive/protocol episodes both fit the same schema. A third Context Pack schema is rejected.

---

## 14. Authority and Change-Control Ruling

This document now has Project-Control workflow/QC authority for Context Pack execution fields.

It does **not** have authority to override:

- author decisions;
- Canon Constitution / errata;
- chronology/state/loss/payoff ledgers;
- domain Working Canon;
- approved scene-card facts;
- current decision ownership;
- irreversible losses;
- manuscript publication gates.

If this spec conflicts with higher story-canon authority, higher authority wins and the Context Pack is corrected.

Future field-schema changes require:

1. identified execution failure;
2. dry-run evidence that current fields cannot represent it safely;
3. impact audit against workflow and existing packs;
4. decision-log entry before adoption.

Do not create parallel schemas by convenience.

---

## 15. Final Ruling

> **CONTEXT PACK TANGIBLE EXECUTION BRIDGE: ADOPTED**
>
> **AUTHORITY: PROJECT-CONTROL WORKFLOW/QC ONLY**
>
> **GENERAL STORED FIELDS: 6**
>
> **HIGH-WATCH BAND IDENTIFIER: 1 + EXTRA EXECUTION CHECKS: 7**
>
> **UNSUPPORTED EXACT DETAIL: `UNRESOLVED FROM APPROVED SOURCES`**
>
> **THIRD SCHEMA: REJECTED**
>
> **NEW WORKFLOW STAGE: 0**
>
> **STORY CANON CHANGE: 0**
>
> **SCENE-CARD REWRITE: 0**
>
> **MANUSCRIPT CONTENT CHANGE: 0**
>
> **PUBLICATION: NOT AUTHORIZED**