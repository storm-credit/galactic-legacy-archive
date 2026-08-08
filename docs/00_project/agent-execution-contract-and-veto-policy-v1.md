# Agent Execution Contract & Veto Policy v1

Status: CANON PROJECT CONTROL
Owner Agents: A00 PM / O01 Canon / O02 Gates / X04 Continuity
Last Reviewed: 2026-08-03
Depends On: agent orchestra registry, [[CLAUDE]]
Used By: every new foundational design artifact and every future canon revision
Open Risks: excessive process overhead for local details; use the proportional-review rule

## 1. Purpose

This document converts specialist labels into enforceable work contracts.

A specialist assignment is valid only when the work record shows:

- the specialist’s question;
- the inputs reviewed;
- the conclusion or design contribution;
- objections and conditions;
- whether the pass was role-based or independently executed;
- the final gate decision.

An `Owner Agents` header alone is not a completed review record.

---

## 2. Execution Modes

### Mode R — Role-Based Orchestrator Pass

Definition:
- the PM orchestrator performs the specialist review as a distinct pass.

Required disclosure:
- `Execution Mode: R`.

Evidence:
- questions asked, findings, changes and unresolved risks.

Default:
- all existing work is presumed Mode R unless a record explicitly states otherwise.

### Mode I — Independent AI Specialist Session

Definition:
- a separately invoked AI session receives a bounded brief and produces an independent result.

Required disclosure:
- `Execution Mode: I`;
- session/model identifier if available;
- input packet;
- output summary;
- whether the specialist saw other reviews before answering.

Restriction:
- independence must not be claimed merely because a different agent code appears in a header.

### Mode H — Human Specialist Review

Definition:
- an identifiable human with relevant expertise reviews the artifact.

Required disclosure:
- reviewer role/qualification as voluntarily provided;
- scope reviewed;
- date;
- findings and limitations;
- no private personal information beyond what the reviewer permits.

### Mode E — External Evidence Check

Definition:
- primary sources, official documentation or research are used to test a factual/technical claim.

Required disclosure:
- source list and what each source supports;
- what remains speculative for fiction.

---

## 3. Specialist Work Contract

Every assigned specialist must answer five fields.

1. **Question** — What specific uncertainty does this role own?
2. **Finding** — What does the current design imply?
3. **Decision** — What is accepted, rejected or changed?
4. **Boundary** — What is outside this role’s authority?
5. **Risk** — What remains uncertain or needs another specialist?

Recommended record:

```markdown
### Specialist Review — M05 Logistics
Execution Mode: R
Question: Can the force sustain the designed operation under the current route, crew, ammunition and repair constraints?
Inputs: `<files/sections>`
Finding: `<analysis summary>`
Decision: PASS | PASS WITH CONDITIONS | FAIL
Conditions: `<specific limits>`
Boundary: does not determine political legitimacy or character morality
Risks/Escalation: `<P02, M08, X04 etc.>`
```

---

## 4. Veto Classes

### V0 — Advisory

- style, naming preference, optional enrichment;
- may be overruled by A00 with a short reason.

### V1 — Execution Condition

- artifact may proceed only if a named condition is tracked;
- example: exact weapon range deferred, but every battle must use a state sheet.

### V2 — Domain Block

- the specific artifact cannot become Working Canon until resolved;
- example: missing life-support capacity, contradictory jurisdiction, impossible travel time.

### V3 — Project Gate Block

- the entire downstream phase is blocked;
- limited to O02 or an escalated X01/X03/X04/X06 finding accepted by O02.

### V4 — Author Scope Block

- work violates explicit author instruction;
- A00 must stop immediately and restore scope.
- no other specialist can override this class.

---

## 5. Fixed Hard-Veto Ownership

| Domain | Primary hard-veto roles | Typical veto trigger |
|---|---|---|
| author scope | A00/O01 | manuscript written while design-only scope is active |
| canon conflict | O01/X04 | two incompatible facts both treated as current canon |
| gate integrity | O02 | PASS claimed without required evidence |
| logic/resources | X01 | outcome requires nonexistent time, capacity, force or resource |
| agency/personhood | X03 | person/community reduced to owned object or coerced choice erased |
| chronology/state | X04 | age, travel, damage, death, possession or authority conflict |
| coverage/completion | X06 | foundational gap hidden as optional detail |
| travel/comms | T02 | instant movement/information violates locked system |
| life support/thermal | T03 | unlimited habitability, heat disposal or evacuation |
| mecha/ship operation | T06/H02/H04/H06 | capability without structure, crew, maintenance or damage persistence |
| military reach | M02/M03/M05 | force appears or sustains combat without route/support/readiness |
| law/rights | P03 | right, seizure, custody or emergency order lacks process/jurisdiction |
| economic capacity | P02 | money substitutes for nonexistent goods, staff, route or permission |
| collection ethics | G01/X03 | hero/faction/person treated as inventory ownership |
| mystery/payoff | N05/N06/O01 | late rule invents answer without clue/authority trail |

---

## 6. Conflict Resolution

When specialists disagree:

1. identify whether the disagreement is factual, causal, ethical, experiential or preference-based;
2. keep each domain’s finding separate;
3. produce at least two viable alternatives when possible;
4. state the cost shifted by each alternative;
5. O01 resolves canon conflicts;
6. O02 resolves gate status;
7. A00 selects the integrated design only after blockers are cleared.

No majority vote automatically defeats a hard veto.

Example:
- M01 may prefer a rapid centralized operation;
- X03 may identify loss of local consent;
- P03 may identify lawful emergency authority;
- M05 may prove the distributed option causes more immediate deaths.

The integrated answer must preserve these facts rather than declaring one specialist morally correct.

---

## 7. Proportional Review Rule

Not every local detail requires the full orchestra.

### Level F — Foundational

Examples:
- physics, political system, collection ontology, major faction, grand-act ending.

Required:
- primary domain panel;
- X01/X03/X04 as applicable;
- A16 red team;
- O01/O02/A00 signoff.

### Level M — Major Operational

Examples:
- city bible, ship bible, campaign, major character institution.

Required:
- 2–5 relevant specialists;
- X04;
- one logic/ethics/retention review as applicable;
- A00 integration.

### Level L — Local Expansion

Examples:
- one minor settlement, local food, one weapon variant, one supporting official.

Required:
- one domain owner;
- dependency/continuity check;
- no full red team unless a new rule is introduced.

### Level C — Cosmetic

Examples:
- color, nickname, decorative detail with no plot/system effect.

Required:
- P05/C06 or relevant visual/naming check;
- no canon-system review unless meaning changes.

---

## 8. Signoff Language

Allowed:

- `Reviewed in Mode R by M03/M05; conditions recorded.`
- `Independent AI review not performed.`
- `Human technical review not performed.`
- `Working Canon under existing fictional envelope.`

Prohibited:

- `전문가들이 모두 검증했다` when only owner labels exist;
- `과학적으로 정확하다` without defined evidence and limits;
- `실제 군사전문가 감수 완료` without Mode H record;
- `독립 멀티에이전트 합의` without Mode I evidence.

---

## 9. Change Control

Changing a specialist’s mandate, veto or code requires:

- original rule;
- proposed change;
- reason;
- affected documents;
- migration plan;
- O01/O02 approval.

A one-time domain overlap does not redefine the registry.

## 10. Policy Status

> **CANON — REQUIRED FOR ALL FUTURE FOUNDATIONAL AND MAJOR DESIGN WORK**

Existing documents remain valid under their final completion audit, but their reviews are classified retrospectively as Mode R unless separately evidenced.