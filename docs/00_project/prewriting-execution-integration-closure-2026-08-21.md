# Pre-Writing Execution Integration Closure — 2026-08-21

Status: CANON PROJECT CONTROL — WORKFLOW/QC ADDENDUM
Effective Authority: PC
Story Canon Effect: NONE
Publication: NOT AUTHORIZED
Owner Agents: A00 PM / A11 Prose / O01 Canon / O02 Gates / X02 Reader Memory / X04 Continuity
Last Reviewed: 2026-08-21
Depends On: [[pre-writing-gate-open-record-2026-08-06]], [[manuscript-production-workflow-v1]], [[first-writing-batch-readiness-v1]], [[full-series-context-writer-activation-depth-standard-v1]], [[full-series-collection-desire-subact-completion-checkpoint-2026-08-21]], [[continuity-issues]]
Used By: every manuscript/context activation after this record
Open Risks: publication remains blocked by issue #26; this record does not grant AUTHOR-APPROVED status.

## 1. Purpose

This record closes execution-layer drift discovered after the full-series Context writer-activation and Collection Desire layers were integrated to `main`.

It does not redesign plot or settings. It reconciles existing project-control decisions and makes the already-completed execution layers mandatory manuscript inputs.

## 2. Existing decisions reaffirmed

1. E001–E020 v1 manuscript files are **revision starting points only** under the later author-approved Pre-Writing Gate decision. Their prose and `Locked Development Outcomes` do not create canon. Every fact must be rechecked against approved scene cards and higher canon.
2. `docs/99_quality_control/continuity-issues.md` already exists and is the living continuity registry. Any older workflow sentence saying it is absent is historical/stale.
3. Draft production authorization remains E001–E005 unless a later explicit author scope decision expands it.
4. `AUTHOR-APPROVED`, public release and publication remain separate decisions.

## 3. Mandatory manuscript activation inputs

Before drafting or revising any authorized episode, the writer must load all of the following in addition to the existing canon/card/bible inputs:

1. the episode's effective FULL Context Pack;
2. the episode's Writer-Activation Overlay (`POV_INFORMATION_ROUTE`, `PRIMARY_DECISION_OWNER`, decision beat, causal chain, human carrier, current payoff, retention condition, Rian non-override and mystery ceiling);
3. the single `CLSET-*` Collection Desire subact packet whose episode range contains the episode;
4. the Collection↔Context cross-layer audit/crosswalk when available.

The CLSET packet controls **reader-desire/set progression at subact scale**. The episode activation controls **current episode execution**. Neither is a story-fact authority; higher canon/cards/ledgers always win.

## 4. Decision-owner anti-centralization rule

POV is not authority.

- `Rian close-third` does not imply Rian owns the episode's decisive choice.
- An explicit technical, medical, legal, local, captain/crew, affected-party, claimant/custodian or institutional owner must retain that decision.
- If no exact person is fixed, use a bounded existing role plus the exact source decision; do not promote the protagonist merely because he is the POV.

The old workflow route `decision + POV => POV/decision-carried owner` is prohibited.

## 5. Collection semantic rule

Collection Desire packets must use writer-readable reader psychology, not internal shorthand.

- `NEXT_DESIRE`, `DISCOVERY`, `ACQUISITION_OR_CONNECTION`, `SYNERGY_OR_USE`, `COST_REFUSAL_OR_LOSS` and `SET_ADVANCE_CONDITION` may not be bare internal category codes such as `C/G/L`.
- Existing codes may remain as source metadata, but the execution packet must explain what the reader is meant to want/learn/complete next.

## 6. CI correctness rule

A pull-request validation workflow must validate the PR head, not a historical production branch.

A green Context/Writer-Activation check produced from a hard-coded old branch is not acceptable evidence for the current PR.

## 7. Gate impact

- Story canon mutation: **0**
- New event/person/death/technology/authority/relationship: **0**
- Ending change: **0**
- E001–E1100 architecture redesign: **0**
- Manuscript authorization expansion: **0**
- Publication authorization: **0**

This record is a workflow/QC integration correction only.
