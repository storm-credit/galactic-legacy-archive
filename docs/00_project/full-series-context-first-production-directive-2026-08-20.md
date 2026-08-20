# Full-Series Context-First Production Directive — 2026-08-20

Status: CANON — PROJECT-CONTROL WORKFLOW/QC
Effective Authority: USER-DIRECTED PRODUCTION ORDER
Story Canon Effect: NONE
Publication: NOT AUTHORIZED
Owner Agents: A00 PM / A11 Prose & Serialization / N03 Episode / X02 Reader Memory / X04 Continuity / O01 Canon
Last Reviewed: 2026-08-20
Depends On: [[context-pack-tangible-reader-memory-execution-spec-proposal-v1]], [[manuscript-production-workflow-v1]], [[effective-canon-status-manifest-v1]], [[continuity-issues]], completed act/subact maps and detailed episode cards
Used By: all future Context Pack production and manuscript scheduling
Open Risks: context completion does not itself authorize any manuscript batch, AUTHOR-APPROVED promotion or publication.

---

## 1. Current author instruction

The production order is now:

> **Complete the FULL deep Context Pack layer for E001–E1100 before any further manuscript drafting/revision is started.**

This is a workflow/order decision only. It does not change any story event, death, survival, relationship, technology, authority, loss, ending or publication state.

Existing manuscript Draft PRs remain preserved as historical/current draft work but are not advanced while the full-series Context layer is incomplete.

---

## 2. Why this is the correct layer

The project already has:

- Grand Act / Act / Subact architecture;
- E001–E100 opening architecture and scene cards;
- E101–E1100 detailed episode design, completed 1,000/1,000;
- chronology/state/loss/payoff/mystery/collection/authority ledgers;
- character/faction/world/hardware bibles;
- Context Pack execution schema.

Therefore Context Pack production must **not redesign the story**.

Its job is to turn approved design into a writer-ready execution layer that prevents:

- source-precedence drift;
- future knowledge becoming omniscience;
- Rian absorbing technical/medical/legal/local authority;
- clue/payoff timing leakage;
- loss or asset-state discontinuity;
- abstract institutional episodes losing tangible reader carriers;
- manuscript-origin exact numbers becoming canon by repetition;
- previous-episode state failing to enter the next episode.

---

## 3. Full-series completion target

Target coverage:

- E001–E1100: **1,100 / 1,100 FULL Context Packs**.

Completion requires all of the following:

1. every episode has a source-bound FULL Context entry;
2. every entry exposes the common six-field execution contract;
3. every entry records source card, date/POV where available, current carrier evidence, state/cost/reentry, authority/agency evidence, information/mystery ceiling, collection/relationship carry and unresolved exacts;
4. all designated HIGH-WATCH bands carry the adopted HIGH-WATCH addendum;
5. E001–E010 manually audited packs remain the effective overrides over any generated baseline;
6. source coverage has zero duplicate episode owners and zero episode gaps;
7. GA-level and full-series blindspot audits PASS;
8. all Context/QC material is merged to `main`;
9. manuscript production remains paused until the Context completion checkpoint is reached.

`NEW_CANON_REQUIRED` defaults to `NO`; if an episode genuinely requires a new story fact to become executable, that episode is marked `YES-STOP` rather than silently invented.

---

## 4. Deep Context minimum

Every episode must carry, directly or by source-bound evidence:

```text
ACTIVE_DESIRE_MAIN
ACTIVE_DESIRE_SECONDARY
PHYSICAL_ANCHOR
STATE_CHANGE
COST_OR_REFUSAL
REENTRY_ANCHOR
SOURCE_CARD
POV / DATE when source supplies them
DECISION / AUTHORITY EVIDENCE
RIAN_CANNOT_OVERRIDE guard
MYSTERY / INFORMATION CEILING
COLLECTION / RELATIONSHIP / INSTITUTION STATE
UNRESOLVED EXACTS
NEW_CANON_REQUIRED
```

For designated HIGH-WATCH bands also retain the normalized addendum from [[context-pack-tangible-reader-memory-execution-spec-proposal-v1]].

This is intentionally deeper than a synopsis and shall not be reduced to one-line plot summaries.

---

## 5. Source rule

Populate Context from the highest available approved source in this order:

1. current explicit author instruction / Canon controls;
2. chronology, state, loss and payoff/mystery ledgers;
3. current domain bibles;
4. approved act/subact architecture and detailed episode card;
5. approved QC constraints;
6. manuscript prose last, and never as a source of new story fact.

Generated Context may copy/reorganize approved source material but may not invent a carrier, person, number, rule, event or authority merely to fill a field.

---

## 6. Production batching

For repository manageability, Context Pack files are grouped by Grand Act / contiguous episode ranges, while every episode retains its own heading and fields.

Batching is a storage choice only. Completion is still counted per episode.

Production sequence:

1. E001–E100 / GA1;
2. E101–E210 / GA2;
3. E211–E330 / GA3;
4. E331–E450 / GA4;
5. E451–E560 / GA5;
6. E561–E690 / GA6;
7. E691–E810 / GA7;
8. E811–E900 / GA8;
9. E901–E1000 / GA9;
10. E1001–E1100 / GA10;
11. full-series cross-GA blindspot audit and final status manifest.

The exact GA boundaries follow current project architecture; if a higher source defines a narrower internal batch, that source controls.

---

## 7. Manuscript hold

Until the full-series completion checkpoint:

- do not create additional manuscript revision/draft PRs;
- do not merge existing manuscript Draft PRs without separate explicit author approval;
- do not grant `AUTHOR-APPROVED`;
- do not expand publication authority;
- issue #26 remains a pre-publication hard blocker.

This hold does not close or delete existing manuscript drafts. It only changes the next production priority.

---

## 8. Blindspot requirement

Context production is not complete merely because 1,100 headings exist.

Required audits include:

- episode-source gaps/duplicates;
- act/subact boundary carry;
- chronology/location continuity;
- named death/permanent-loss preservation;
- equipment/ship/frame state continuity;
- collection ownership/custody/claim continuity;
- clue/payoff timing against locked ledgers;
- relationship and exit/refusal rights;
- domain decision ownership / anti-Rian authority creep;
- repeated episode engine patterns;
- abstract-concept overload and tangible carrier coverage;
- HIGH-WATCH HAPΔ coverage;
- ending/amendment precedence in GA10.

Any semantic conflict discovered by the Context audit is reported; Context itself does not silently rewrite the underlying canon/card.

---

## 9. Completion declaration

Only after the full-series status manifest reports:

> `E001–E1100 FULL CONTEXT: 1100/1100`  
> `GA BLINDSPOT AUDITS: PASS`  
> `CROSS-GA CONTINUITY AUDIT: PASS`  
> `NEW_CANON_REQUIRED unresolved blockers: 0 or explicitly author-held`

may manuscript scheduling resume under the separate manuscript-production authorization rules.
