# Deferred-Detail Completion Red Team v1

Status: REVIEW COMPLETE — CONDITIONAL PASS PENDING CI
Owner Agents: A16 Red Team / X01 Logic / X02 Reader Memory / X03 Ethics / X04 Continuity / X06 Coverage / O01 Canon / O02 Gates
Last Reviewed: 2026-08-03
Depends On: all detail-completion files on `agent/deferred-detail-completion-pass`
Used By: PR gate, deferred-register v2, next scene-card production phase
Open Risks: structured census/route validation must pass in GitHub Actions before merge

## 1. Audit Scope

This red team attacks whether the new detail packet:

- creates false encyclopedic completeness;
- introduces pseudo-precise numbers unsupported by existing canon;
- contradicts Academy, galaxy, economy, military or ending scale;
- overwhelms reader memory;
- creates unlimited fleets/routes/production;
- turns medical or social technology into plot magic;
- opens new core mysteries after their lock;
- falsely claims E101–1100 episode cards are complete.

## 2. Executive Verdict

> **CONDITIONAL PASS — FOUNDATIONAL DETAIL EXPANSION IS COHERENT**

Conditions before promotion:

1. census CI must confirm exactly 612 unique systems, region populations, node quotas and protected systems;
2. route generator must confirm one connected graph, minimum degree ≥2 and valid cluster references;
3. PR review must verify no generated data file is omitted;
4. final status must state E101–1100 cards remain 0/1,000 under the new standard;
5. manuscript and human-reader gates remain blocked.

## 3. Attack A — Fake Precision in the 612-System Census

Risk:
- exact three-decimal population values can look like omniscient truth;
- generated names and industries can be mistaken for fully developed local bibles;
- one malformed row can invalidate totals.

Controls added:
- author-side census interpretation;
- ±10% local correction range through change control;
- legal/mobile populations separated;
- exact macro totals treated as planning constraints, not in-world perfect knowledge;
- automated row, uniqueness, population, node and cluster validation;
- generated minor names remain author-side until front-stage collision review.

Verdict:
- `PASS WITH CI CONDITION`.

## 4. Attack B — K-13 Population Contradiction

Risk:
- census gives 620,000 while Academy bible gives approximately 3,000 permanent residents.

Resolution:
- 620,000 is the full inhabited K-13 system;
- approximately 3,000 is the Academy station population;
- Academy is roughly 0.5% of registered system population;
- separate system civilians, employment and governance are now explicit.

Verdict:
- `PASS`.

## 5. Attack C — L0 Anchors All Belonging to the Core

Risk:
- one Inner L0 (`Joraas`) could appear to violate Core/anchor assumptions.

Resolution:
- nine L0 anchors explicitly listed;
- Joraas is an early auxiliary anchor later neutralized under multilateral charter;
- physical node class and political sovereignty are distinct;
- Joraas lacks the complete central Archive/Imperial root.

Verdict:
- `PASS`.

## 6. Attack D — Route Graph as Arbitrary Connectivity

Risk:
- a census without edges is not a usable travel map;
- a dense generated graph could permit convenient shortcuts;
- disconnected systems or single-edge traps could appear accidentally.

Controls:
- 81 explicit cluster-backbone routes;
- deterministic local rings and gateway spokes;
- route status and travel-band rules;
- graph connectivity and minimum-degree validation;
- scene travel still requires queue, authorization, approach and current route state;
- generated edge does not mean continuously open passage.

Residual risk:
- exact orbital approach and temporary wartime closures remain scene/operation detail.

Verdict:
- `PASS WITH CI CONDITION`.

## 7. Attack E — Pseudo-Hard-SF Weapon Numbers

Risk:
- wide numerical bands can be read as real-world scientific prediction;
- exact range may override sensor state, geometry or objective;
- frame/ship power could inflate through selective use of maxima.

Controls:
- numbers explicitly defined as author-side performance envelopes;
- sensor state S0–S6 required before fire-control;
- thermal state T0–T6 and ammunition/crew/acceleration limits;
- hull-specific fit remains operation-derived;
- peak values cannot be combined without mass/heat/support accounting;
- direct prohibitions against invisible damage reset and frame strategic travel.

Verdict:
- `PASS FOR FICTION CALIBRATION`, not external engineering certification.

## 8. Attack F — Formation Double Counting

Risk:
- source fleets and joint mission formations may be summed as independent ships;
- the protagonist could appear to create hundreds of hulls by reflagging.

Controls:
- source vs derived formation classes;
- explicit non-additive rule;
- source-to-derived detachment records required;
- global ceiling and local duty left uncovered;
- separate hull, crew, support, command and legal status.

Verdict:
- `PASS`.

## 9. Attack G — Institution and Proper-Noun Inflation

Risk:
- 48 minor organizations plus 612 system names become unreadable;
- organizations exist only to simulate depth.

Controls:
- front-stage active limit of 3–5 organizations per arc;
- each institution has service, constituency, internal split and coercive shadow;
- at least 18 must act independently of Rian;
- generated census names remain author-side by default;
- terminology budgets per episode and 10-episode window;
- retire/reintroduce rules and phonetic collision checks.

Verdict:
- `PASS WITH EXECUTION RISK S1`.

## 10. Attack H — Reproductive Technology as Twist Machine

Risk:
- artificial gestation, genetics or cloning can erase bodily, family and identity stakes;
- child/copy may be treated as property;
- secret lineage becomes convenient plot answer.

Controls:
- normal developmental time retained;
- facility, staff, power, cost and route dependence;
- parenthood, genetic contribution, gestation and custody separated;
- copies/whole-body clones are new persons unless continuity separately established;
- no genetic determination of morality/genius/loyalty;
- surprise reproductive twist prohibited without prior bible expansion and clues.

Verdict:
- `PASS`.

## 11. Attack I — Visual Bible as Franchise Reskin

Risk:
- humanoid frame, old escort and imperial/corporate aesthetics can resemble known franchises;
- faction identity could collapse to color coding.

Controls:
- function, maintenance, authority and ordinary-life evidence required;
- silhouette and material variation derived from service constraints;
- explicit prohibited similarities;
- three structural-premise transformations required before visual canon;
- no actual image becomes canon without separate review.

Verdict:
- `PASS FOR TEXTUAL BRIEF`; actual art remains open.

## 12. Attack J — Secondary Mysteries Delaying Core Payoffs

Risk:
- forty-one local questions create endless mystery debt;
- a late decoy could become a new core secret.

Controls:
- every question has an answer/retirement window;
- no new foundational mystery after GA6;
- only 2–4 active secondary mysteries per 25 episodes;
- false relics retire as evidence, public objects or discarded names;
- core M-001–M-020 timing remains authoritative.

Verdict:
- `PASS`.

## 13. Attack K — Epilogue Statistics as Moral Scoreboard

Risk:
- percentages may imply one political model is objectively good;
- aggregate population growth could erase hundreds of millions of deaths;
- exact figures could imply perfect in-world census knowledge.

Controls:
- confidence bands H/M/L;
- deaths, missing and excess mortality shown separately;
- T0/T6 centralization has real service advantages;
- T3 has stronger appeal/local power but weaker reliability;
- T5 may fail both materially and politically;
- no model is universal endpoint;
- final scene remains local and present-tense.

Verdict:
- `PASS WITH IDEOLOGICAL-BALANCE MONITORING`.

## 14. Attack L — Economy Becomes Spreadsheet Fiction

Risk:
- taxes, input units and cost tables overwhelm scenes;
- BSC and production units become reader-facing game currency.

Controls:
- BSC/ST/PM/etc. explicitly author-side;
- scenes use wages, shortages, signatures, work, queues and concrete goods;
- every plan must identify cash, physical input, labor, route, liability and displaced allocation;
- only front-stage numbers appear in dialogue/narration.

Verdict:
- `PASS WITH READER-LOAD RISK S1`.

## 15. Attack M — Claiming All Detail Is Complete

Risk:
- resolving encyclopedic packets may be conflated with completing every episode.

Control:
- production standard explicitly reports actual E101–1100 cards as `0 / 1,000` at creation;
- 42-batch queue does not count as episode cards;
- exact battle detachments/losses remain coupled to those cards;
- deferred register v2 preserves this boundary.

Verdict:
- `PASS IF FINAL REPORT USES QUALIFICATION`.

## 16. Attack N — Accidental Manuscript Re-entry

Risk:
- “episode detail” could become dialogue or chapter prose.

Controls:
- episode-card schema is state/scene design only;
- dialogue draft, chapter prose and publication lengths explicitly excluded;
- authorial scope remains blocked;
- A00 has V4 stop authority for prose outside instruction.

Verdict:
- `PASS`.

## 17. S0 / S1 / S2

### S0 blockers before merge

- failed structured-data CI;
- disconnected route graph;
- missing census file/row;
- contradiction with protected system or total scale;
- final status falsely claiming E101–1100 cards complete.

### S1 execution risks

- generated-name density;
- institutional names used without human service/action;
- weapon maxima cherry-picked;
- joint formation double counting in future operation sheets;
- epilogue statistics used as political verdict;
- author-side tables leaking into prose;
- exact scene cards becoming repetitive procedural templates.

### S2 local risks

- minor visual palette collisions;
- local tax/statutory wording;
- local orbital data;
- private relationship choices;
- human recall evidence.

## 18. Required PR Evidence

Before merge:

1. GitHub Actions `Validate design data` passes;
2. changed files include all census parts, cluster backbone, validators and world/detail bibles;
3. PR is mergeable;
4. after merge, `merged=true` is verified;
5. `main` contains the detail status and at least one census/validation file.

## 19. Final Conditional Ruling

> **DETAIL-EXPANSION DESIGN: CONDITIONAL PASS**

> **PROMOTION BLOCKED UNTIL STRUCTURED-DATA CI PASSES**

> **E101–1100 ACTUAL EPISODE CARDS: NOT YET COMPLETE**

After CI success, this audit may be promoted to final PASS without changing the substantive findings.