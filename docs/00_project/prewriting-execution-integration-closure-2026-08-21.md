# Pre-Writing Execution Integration Closure — 2026-08-21

Status: PASS — READY FOR MAIN INTEGRATION
Effective Authority: PC — PROJECT-CONTROL WORKFLOW/QC ADDENDUM
Story Canon Effect: NONE
Publication: NOT AUTHORIZED
Owner Agents: A00 PM / A11 Prose / O01 Canon / O02 Gates / X02 Reader Memory / X04 Continuity
Last Reviewed: 2026-08-21
Depends On: [[pre-writing-gate-open-record-2026-08-06]], [[manuscript-production-workflow-v1]], [[first-writing-batch-readiness-v1]], [[full-series-context-writer-activation-depth-standard-v1]], [[full-series-collection-desire-subact-completion-checkpoint-2026-08-21]], [[continuity-issues]]
Used By: every manuscript/context activation after this record
Open Risks: publication remains blocked by issue #26; this record does not grant AUTHOR-APPROVED status. The repository-wide generic validator still has pre-existing generated-index currentness debt; canon/link/manuscript-contract validation is green.

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

- `NEXT_DESIRE`, `DISCOVERY`, `ACQUISITION_OR_CONNECTION`, `SYNERGY_OR_USE`, `COST_REFUSAL_OR_LOSS` and `SET_ADVANCE_CONDITION` may not be bare internal registry status codes such as backticked `C/G/L`.
- Source-native operational labels such as `Window A/B/C` remain valid.
- If an owning subact has no usable explicit ending hook and the old registry fallback is only status metadata, `NEXT_DESIRE` may bridge to the **next approved subact's already source-bound `READER_DESIRE_MAIN`**. This is execution routing, not new story canon.

## 6. CI correctness rule

A pull-request validation workflow must validate the PR head, not a historical production branch.

A green Context/Writer-Activation check produced from a hard-coded old branch is not acceptable evidence for the current PR.

The Context Pack and Writer-Activation workflows now validate the actual pull-request head. The integration workflow also rebuilds both execution layers on the same head before accepting their cross-layer result.

## 7. Validation checkpoint — PR #213

Validated human/connector head before generated-output persistence: `64e8d6d071dc0bde6a4785758bc9a45fe2717f44`.

Validated generated execution outputs were then persisted by bot commit:

- generated-output persistence commit: `6784b9d7737bbc9363561d130c6d7535c6d067a6`;
- story/act/scene-card/manuscript source files changed by that persistence: **0**;
- outputs affected: Writer-Activation overlays, Collection Desire maps and their QC audits only.

### 7.1 Decision ownership

- E011–E1100 activation entries scanned: **1090 / 1090**;
- banned `POV + decision => owner` routes: **0**;
- banned rendered `POV/decision-carried current actor(s)` owners: **0**;
- missing owner/authority fields: **0**;
- new story authority granted: **0**.

### 7.2 Collection semantic readability

- subacts scanned: **160 / 160**;
- writer-unusable semantic fields: **0**;
- registry-status NEXT_DESIRE packets bridged to approved source/next-subact desire: **12**;
- concise readable fields remaining as WATCH: **3**;
- target-title fallback: **0**;
- malformed/missing desire packets: **0**.

### 7.3 Collection ↔ episode execution bridge

- Collection subacts: **160 / 160**;
- generated Writer-Activation episodes: **1090 / 1090**;
- E011–E1100 episodes without exactly one CLSET range: **0**;
- E011–E1100 episodes inside overlapping CLSET ranges: **0**;
- hard bridge failures: **0**;
- lexical exit-hook WATCH: **93** — review aid only; this lexical heuristic is not treated as a story/canon failure because conceptually equivalent handoffs may use different wording.

### 7.4 Existing gates retained

On the same validated head:

- full-series Context Pack build: **PASS**;
- Writer-Activation depth/load-bearing gates: **PASS**;
- Collection source/provenance gate: **PASS**;
- Collection repetition/reader-memory gate: **PASS**;
- canon/link/manuscript-contract validation: **PASS**;
- generic repository workflow: still red only at pre-existing generated-index currentness step.

## 8. Gate impact

- Story canon mutation: **0**
- New event/person/death/technology/authority/relationship: **0**
- Ending change: **0**
- E001–E1100 architecture redesign: **0**
- Manuscript files changed: **0**
- Manuscript authorization expansion: **0**
- `AUTHOR-APPROVED`: **NOT GRANTED**
- Publication authorization: **0 / NOT AUTHORIZED**

## 9. Integration disposition

> **PASS — READY FOR MAIN INTEGRATION.**

PR #213 may be squash-merged as a workflow/QC correction after the persisted-output head is revalidated. After merge, `CI-20260821-01` is treated as FIXED once actual `main` contains the merge result.
