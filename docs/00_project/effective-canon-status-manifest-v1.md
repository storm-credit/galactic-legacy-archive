# Effective Canon Status Manifest v1 — 정본 상태 정규화 장부

Status: CANON PROJECT CONTROL
Owner Agents: O01 Canon / O02 Gates / X04 Continuity
Last Reviewed: 2026-08-03
Depends On: master index, final settings-bible audit, individual document headers
Used By: source resolution, status normalization and future revisions
Open Risks: individual legacy files may still display `Status: REVIEW`; this manifest defines their effective authority without mass-editing historical headers

## 1. Problem

Many major setting documents were created with headers such as:

- `DRAFT`;
- `REVIEW`;
- `REVIEW COMPLETE`;
- `CANON PROJECT CONTROL`.

The final completion audit later promoted selected integrated documents as Working Canon. Editing every historical header would erase useful process history and create a large accidental-change surface.

Therefore:

> **The effective status is determined by source precedence and this manifest, not by the legacy header alone.**

---

## 2. Status Classes

### PC — Project-Control Canon

Controls:
- scope;
- source precedence;
- names/errata;
- gates;
- handoff;
- completion/deferred boundaries.

Can be changed only through explicit change control.

### WC — Working Canon Design Authority

Foundational or major design accepted for downstream use.

Meaning:
- new work must conform to it;
- local detail may expand under existing rules;
- contradictions require O01/X04 resolution.

### AS — Approved Structure

Architecture approved at the declared level.

Meaning:
- causal sequence, goals, costs and outcomes are authoritative;
- scene-level staging may change without rewriting the act’s core result;
- exact episode cards are not implied unless stated.

### FR — Framework Authority

The system and constraints are authoritative, but local values/content remain to be filled.

Examples:
- exact weapon range;
- individual minor star catalogue;
- local dialect lexicon;
- scene-specific psychological rhythm.

### DD — Deferred Detail

Useful detail intentionally postponed to a later production phase.

It is not a completion blocker.

### NC — Non-Canon / Audit History

Cannot create setting facts or authorize downstream work.

### BL — Blocked

Work must not proceed without explicit author or gate authorization.

---

## 3. Project-Control Canon Files

Effective status `PC`:

- `CLAUDE.md`;
- `docs/00_project/settings-bible-master-index-v1.md`;
- `docs/00_project/settings-bible-final-status-2026-08-03.md`;
- `docs/99_quality_control/final-settings-bible-completion-audit-v3.md`;
- `docs/00_project/deferred-design-register-v1.md`;
- `docs/00_project/context-window-handoff-protocol.md`;
- `docs/00_project/design-only-scope-restoration-2026-08-03.md`;
- canonical name errata files;
- this manifest;
- agent orchestra registry and execution policy;
- document review signoff ledger.

---

## 4. Effective Working Canon by Domain

### Core premise, history and mystery — `WC`

Includes:
- regression/current-original timeline rules;
- Archive ontology and uncertainty;
- Continuity Seed/Aurel architecture;
- service authorities;
- final no-permanent-collector direction;
- locked payoff/loss ledgers.

### World physics and geography — `WC`

Includes:
- lattice physics;
- node hierarchy;
- travel/communication delays;
- opening route graph;
- Academy/White Dock geography;
- Ardis city/node engineering;
- GA8–10 regional atlases;
- galaxy scale envelopes.

### Technology, mecha, ships and AI — `WC`

Includes:
- technology eras and six interoperability layers;
- compatibility bands;
- 07 design/rights/end-state;
- first ship/crew/ownership/end-state;
- AI/process/person/office distinctions.

### Economy, trade and logistics — `WC`

Includes:
- BSC author-side unit;
- currencies, wages, household/student debt;
- prices and ship/frame/medical costs;
- trade flows, chokepoints, sanctions and war economy;
- fleet logistics/readiness burden.

### Military and security — `WC` with local `FR`

Working Canon:
- doctrines;
- force scales;
- command roles;
- readiness/replacement;
- support and logistics;
- grand-act holdings;
- strategic/operational battle constraints.

Framework Authority:
- exact weapon/sensor ranges;
- exact per-battle OOB after E100;
- exact ammunition and damage state for scenes not yet produced.

### Society, culture and ordinary life — `WC` with local `FR`

Working Canon:
- opening cultures;
- faith/philosophy;
- family, care, guardianship and personhood;
- education, media, art, sport, holidays and mourning;
- later-region/AI ordinary life;
- faction cultural/visual principles.

Framework Authority:
- exact costumes and concept art;
- full dialect lexicons;
- character-specific romance/family choices not yet selected.

### Law, rights, institutions and succession — `WC`

Includes:
- Academy jurisdiction/charter;
- custody and medical/data rights;
- ship mission trust;
- Ardis Joint Trust;
- Interim Authority Compact;
- Common Fleet Charter;
- Aurel and staged-transition authority;
- officeholder/succession state tables.

### Collection and progression — `WC SYSTEM AUTHORITY`

Includes:
- collection ontology;
- five control layers;
- acquisition/integration/refusal/loss/recovery;
- counter-collection;
- active-target and power-creep controls;
- first-100 and GA2 registries;
- category templates.

Late-act detailed item inventories are `DD`, not missing system authority.

### Characters and factions — `WC`

Includes:
- core names/voices and arcs;
- opening cast;
- protected community;
- first ship crew;
- Ardis factions;
- GA4–10 officeholders, deputies, ordinary focals and succession;
- named irreversible losses.

### Story architecture — mixed

- GA1–GA10 grand-act/act/subact maps: `AS`;
- final chronology and major states: `WC`;
- first 100 operational/scene-card design: `AS`;
- E101–1100 exact scene cards: `DD`;
- 650–750 alternate edition: `OPEN SEPARATE PROJECT`.

### Quality control — `PC/WC`

- final audit/gates/source precedence: `PC`;
- red-team findings and controls: `WC` conditions;
- old gap audits: historical evidence, superseded where stated.

---

## 5. Non-Canon and Blocked Material

Effective `NC`:

- accidental manuscript files from PR #35/#36;
- proxy prose samples;
- abandoned names superseded by errata;
- old issue descriptions contradicted by later project-control rulings;
- unmerged branch experiments unless explicitly promoted.

Effective `BL`:

- manuscript drafting, revision and publication preparation without new explicit author instruction;
- claims of human expert review without Mode H evidence;
- claims of independent multi-agent execution without Mode I evidence.

---

## 6. Conflict Resolution

When a legacy file says `REVIEW` but appears in the master index and final audit as accepted:

- use the effective status in this manifest;
- retain the old header as historical workflow metadata;
- do not mass-edit unless the content itself is being revised.

When two accepted files conflict:

1. current explicit author instruction;
2. project-control canon and errata;
3. later dated Working Canon with explicit change record;
4. final chronology/state/payoff ledgers;
5. act maps;
6. older review/draft documents.

O01/X04 must record the resolution.

---

## 7. Future File Header Standard

New foundational/major files should use one of:

```markdown
Status: CANON PROJECT CONTROL
Effective Authority: PC
```

```markdown
Status: WORKING CANON
Effective Authority: WC
```

```markdown
Status: APPROVED STRUCTURE
Effective Authority: AS
```

```markdown
Status: FRAMEWORK
Effective Authority: FR
```

```markdown
Status: NON-CANON TEST
Effective Authority: NC
```

Review state and effective authority should no longer be conflated.

## 8. Manifest Verdict

> **PASS — EFFECTIVE CANON STATUS IS NOW NORMALIZED WITHOUT REWRITING ALL HISTORICAL FILE HEADERS**

This resolves the discrepancy between legacy `REVIEW` headers and the final completion audit’s Working Canon promotion.