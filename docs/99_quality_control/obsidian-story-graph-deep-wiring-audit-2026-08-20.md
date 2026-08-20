# Obsidian Story Graph Deep-Wiring Audit — 2026-08-20

Status: PASS — NAVIGATION / STATE-WIRING QC
Effective Authority: QC over navigation structure only
Story Canon Effect: NONE
Publication: NOT AUTHORIZED
Owner Agents: A00 PM / N02 Act Architecture / N03 Episode / O01 Canon / X04 Continuity / X06 Coverage / X02 Reader Memory
Last Reviewed: 2026-08-20
Depends On: [[architecture-rules]], [[1000-episode-grand-act-map-v1]], [[first-100-act-map-v2-consolidated]], GA2–GA10 act maps, [[ga1-10-state-checkpoint-matrix-v1]], [[ga1-10-operational-checkpoint-snapshots-v1]], [[context-pack-tangible-reader-memory-execution-spec-proposal-v1]], [[docs/_entities/README]]
Used By: Obsidian Graph View, Context Pack preparation, scene-card navigation, continuity audit
Open Risks: final exact character/ship/place visual canon remains separately author-held; Context Packs are produced just-in-time rather than pre-generated for 1,100 episodes

---

## 0. Audit Question

> Can a writer/reviewer enter the project from the series or a Grand Act, descend through Act and Subact, reach episode design / Context Pack execution, and from there resolve the **current** character, collection/legacy, frame, ship, weapon, relic, technology, faction, place, visual-memory and loss/payoff/authority state without creating a second canon source?

Verdict:

> **PASS — STRUCTURAL STORY GRAPH WIRED AT GRAND-ACT → ACT → SUBACT → EXECUTION → CURRENT-STATE LEVEL.**

The graph is deliberately a navigation layer. It is not a summary encyclopedia and cannot create facts.

---

## 1. Project-Specific Hierarchy Ruling

The user supplied another project's example:

`Grand Act → Act Hub → Volume → 60 Subact Hub → episode Act-map/Context Pack → current state`.

That shape is **not imported literally**.

[[architecture-rules]] defines this project's hierarchy as:

`SERIES → SAGA → GRAND ACT → ACT → SUBACT → EPISODE BLOCK → EPISODE → SCENE`.

Current GA1–GA10 architecture uses:

- 10 Grand Acts;
- 4 Acts per Grand Act;
- 4 Subacts per Act;
- therefore **160 Subact navigation nodes**.

A new canonical `Volume` layer would be an invented hierarchy and is not added. If a later publication platform needs volumes, they may be generated as a noncanonical presentation view without becoming story authority.

---

## 2. Implemented Navigation Graph

Physical Markdown files under `docs/_graph/`:

| Layer | Count | Function |
|---|---:|---|
| Graph rules README | 1 | authority and anti-duplication rules |
| Series root | 1 | entry point |
| Grand Act hubs | 10 | GA1–GA10 navigation |
| Act hubs | 40 | four Acts per GA |
| Subact hubs | 160 | four Subacts per Act |
| GA Current-State Spines | 10 | execution → current-state fan-out |
| Domain-State hubs | 11 | authoritative domain routing |
| **Total Markdown files** | **233** | navigation graph |

The 160 Subact nodes are also linked as one chronological previous/next chain from GA01 A1 through GA10 D4.

---

## 3. Effective Graph Path

Primary descent:

```text
[[story-graph-root]]
  ↓
Grand Act Hub
  ↓
Act Hub
  ↓
Subact Hub
  ├─→ authoritative Act-map
  ├─→ GA Collection Registry
  ├─→ episode design/index bridge
  ├─→ [[context-pack-tangible-reader-memory-execution-spec-proposal-v1]]
  └─→ GA Current-State Spine
          ↓
      11 Domain-State Hubs
          ↓
      canon/AS/WC registries, bibles, state/loss/payoff ledgers, entity notes
```

The same edge is visible in reverse through Obsidian backlinks. Detail episode cards already cite their GA Act-map as a dependency, so the graph can traverse `Subact Hub → Act-map ← Detailed Episode Card` without duplicating every detail-card filename into 160 hubs.

This is intentional: copying packet filenames into all Subact hubs would create 160 stale lists whenever detailed-card batch files are split or regrouped.

---

## 4. Episode / Context Pack Bridge

### GA1

[[episode-briefs]] already assigns registry items to Subacts and provides exact per-episode design-card links for the first 100 episodes.

### GA2–GA10

Every GA Current-State Spine now additionally links:

- [[episodes-101-1100-detail-production-standard-and-batch-map-v1]];
- the corresponding GA Act-map;
- the corresponding collection registry;
- state checkpoint/snapshot sources;
- Context Pack execution spec.

The detail-production standard requires every detailed episode card to carry character, institution, hardware, route, economy/service, collection/mystery, relationship, irreversible-state and downstream-dependency fields. It therefore functions as the stable episode-design junction rather than copying those facts into graph hubs.

### Context Pack

Context Packs remain **just-in-time execution objects**, not 1,100 pre-generated notes.

The graph always exposes the adopted Context Pack schema. During actual drafting the pack is populated from approved sources using:

- `ACTIVE_DESIRE_MAIN`;
- `ACTIVE_DESIRE_SECONDARY`;
- `PHYSICAL_ANCHOR`;
- `STATE_CHANGE`;
- `COST_OR_REFUSAL`;
- `REENTRY_ANCHOR`;
- HIGH-WATCH additions where applicable.

Unsupported exact detail remains `UNRESOLVED FROM APPROVED SOURCES`; the graph is never used to invent the missing value.

---

## 5. Current-State Resolution Algorithm

For an episode or Subact, resolve current state in this order:

1. **Current author instruction / Canon Amendment / Errata**.
2. **Authoritative GA Act-map / exact detailed episode card** for local causal placement.
3. **GA Current-State Spine** for the state sources that must be checked.
4. **State checkpoint matrix / operational snapshots** for inherited and carried state.
5. **GA collection registry** for desire/acquisition/refusal/loss/re-entry status.
6. **Domain registry/bible** for exact object/person/institution rules.
7. **Entity note**, only if that subject has been promoted to a front-stage navigation note.
8. **Loss/payoff/authority hub and ledgers** for irreversible losses, authority owner, refused authority and locked payoff.
9. **Visual-memory hub** for reader-recognition direction and anti-similarity constraints.
10. **Context Pack** turns the resolved state into episode execution fields; it never overrides steps 1–9.

This prevents a lower graph note from becoming newer merely because it is convenient.

---

## 6. Eleven State Domains

### 6.1 Characters

[[graph-state-characters]] routes to:
- character index;
- entity-note rules;
- canonical names/voice lock;
- state checkpoints / operational snapshots;
- reader-memory and anti-similarity QC.

Purpose:
- location;
- health/fatigue;
- authority;
- affiliation;
- relationship;
- knowledge/confidence;
- debt/obligation;
- exit/death status;
- reader-recognition direction.

### 6.2 Collection / Reader Desire

[[graph-state-collection]] routes to the collection master/index/bible and completion scorecard.

Purpose:
- discovery;
- relationship/acquisition;
- access/custody/operation;
- refusal/counter-collection;
- cost/loss;
- state change;
- re-entry;
- legacy/payoff.

### 6.3 Maneuver Frames

[[graph-state-frames]] routes to frame index, lineup architecture, combat/collectibility audit and front-stage frame notes.

Purpose:
- chassis/lineage;
- operational state;
- damage/maintenance;
- pilot/authority limits;
- reader-recognition silhouette;
- retirement/legacy state.

### 6.4 Ships / Hulls

[[graph-state-ships]] routes to hull registry, first-ship bible and operational snapshots.

Purpose:
- title/custody;
- crew authority;
- propulsion;
- damage;
- maintenance;
- interior/service role;
- irreversible loss;
- home/re-entry memory.

### 6.5 Weapons / Parts

[[graph-state-weapons-parts]] routes to the named weapon/part registry.

Purpose:
- function;
- carrier;
- compatibility;
- certification;
- custody;
- damage;
- support cost.

### 6.6 Relics / Provenance / Records

[[graph-state-relics-provenance]] routes to provenance registry and payoff ledgers.

Purpose:
- physical object versus legal/information claim separation;
- origin/provenance;
- rightful custodian;
- interpretation change;
- return/payoff.

### 6.7 Technology / Lineage

[[graph-state-technology]] routes to technology-lineage and interoperability sources.

Purpose:
- theory;
- prototype/process;
- validation;
- certification;
- teaching/diffusion;
- governance and compatibility cost.

### 6.8 Factions / Institutions

[[graph-state-factions-institutions]] routes to faction registry, succession/culture/visual matrix and state checkpoints.

Purpose:
- constituency;
- current authority;
- internal blocs;
- succession;
- services;
- coercive shadow;
- institutional independence from protagonist.

### 6.9 Places / Routes / Nodes

[[graph-state-places-routes]] routes to world index, named-place/corridor registry, chronology and operational snapshots.

Purpose:
- jurisdiction;
- service state;
- route access;
- damage;
- ordinary-life carrier;
- sensory re-entry anchor.

### 6.10 Visual / Reader Memory

[[graph-state-visual-memory]] routes to visual language, faction visual grammar, reader-memory completion scorecard and anti-similarity reference audits.

Purpose:
- silhouette;
- material/surface;
- motion/habit;
- sensory anchor;
- scar/evolution;
- re-entry recognition;
- same-face / costume / famous-composition collision avoidance.

**Boundary:** exact final face, hair, eye, body, costume or illustration composition is not created by the graph and remains under its existing author lock.

### 6.11 Loss / Payoff / Authority

[[graph-state-loss-payoff-authority]] routes to payoff ledgers, state ledgers and continuity issues.

Purpose:
- irreversible loss;
- current authority owner;
- prohibited/expired authority;
- payoff timing;
- unresolved claim;
- continuity conflict.

A graph edit can never restore a death, injury, lost capability, destroyed route or revoked authority.

---

## 7. Visual Deep-Wiring Verdict

The earlier visual work is now **connected into the story graph**, but this must not be confused with final art canonization.

Connected:
- faction visual grammar;
- character reader-recognition direction;
- machine/ship/place visual-memory direction;
- anti-similarity reference deconstruction;
- hair-off face-geometry collision check;
- same-light neutral-head comparison;
- uniform-normalized check;
- props-off check;
- 64px silhouette check;
- scars/evolution/re-entry memory.

Still author-held:
- exact core-cast final faces;
- exact hair/eye/body variables;
- final costume sheets;
- final Parus exterior art direction;
- final major-place art direction;
- mass visual sheets for every minor character/hull/system.

This is intentional. Bulk art canonization would create false specificity and same-face/reference-clone risk.

---

## 8. Entity-Note Expansion Rule

Existing [[docs/_entities/README]] already correctly rejects creating every possible entity note up front.

Therefore this graph does **not** generate:
- 197 empty person notes;
- all candidate frame notes;
- all hull notes;
- all 612 system notes.

An entity note is created when the subject is front-stage enough that backlinks materially improve writing/review. Until then, the domain index/registry is the graph endpoint.

This gives graph depth without graph noise.

---

## 9. Blind-Spot Sweep

| Risk | Failure | Guard |
|---|---|---|
| Duplicate canon | Hub summaries quietly become source of truth | navigation-only status; source-owned facts |
| Other-project hierarchy import | Volume/60-subact model rewrites this project's architecture | explicit project-specific hierarchy guard |
| Empty-node explosion | 197/612 low-value nodes obscure useful graph | front-stage entity-note rule |
| Stale episode packet lists | 160 hubs copy exact packet filenames and drift after file splits | Act-map / episode-production junction + backlinks |
| Same-face visual convergence | visual layer is linked but not collision-tested | visual-memory hub + anti-similarity QC |
| Permanent-loss restoration | current-state convenience forgets a loss | loss/payoff/authority hub |
| Protagonist authority absorption | current state defaults to Rian | authority state must resolve from source/ledger |
| Late abstract acts become paperwork | collection/legal/record state lacks physical carrier | Context Pack tangible fields + visual/place/asset hubs |
| Graph silently breaks after rename | wiki target no longer exists | `tools/validate_story_graph.py` CI |
| Subact disappears from chronological flow | local hub exists but is isolated | 160-node previous/next chain validation |
| Historical GA10 ending reopens | old OPEN text wins through navigation | GA10 hub/state/D subacts directly link current Canon Amendment |

No S0/S1 story rewrite requirement was created by this audit.

---

## 10. Mechanical Validation Contract

`tools/validate_story_graph.py` must pass before graph changes merge.

It checks:
- 233 Markdown files under `docs/_graph`;
- 10 GA hubs;
- 40 Act hubs;
- 160 Subact hubs;
- 10 GA state spines;
- 11 domain-state hubs;
- root → GA/domain links;
- GA → Act/state/source/collection links;
- Act → four Subact links;
- Subact → parent/source/collection/state/episode/Context Pack links;
- GA2–GA10 → detail-production-index bridge;
- full 160-node chronological previous/next chain;
- GA10 D-subact ending-amendment link;
- all graph wiki targets resolve to real Markdown sources;
- project-specific no-Volume/no-60-subact guard.

The dedicated GitHub Action `.github/workflows/validate-story-graph.yml` runs this validator when graph/index/entity navigation files change.

---

## 11. What This Work Does Not Claim

It does not claim:
- every visual variable is finally approved;
- every minor character deserves an entity node;
- every 1,100 Context Pack already exists;
- every episode card has been duplicated into the graph layer;
- navigation authority equals story canon;
- publication is authorized.

It does establish a stable path to retrieve the sources needed to answer those questions at the correct production moment.

---

## 12. Final Ruling

> **OBSIDIAN STORY GRAPH: DEEP-WIRING STRUCTURE COMPLETE**
>
> **PROJECT-SPECIFIC HIERARCHY: 10 GRAND ACTS / 40 ACTS / 160 SUBACTS**
>
> **EXECUTION BRIDGE: ACT-MAP + EPISODE DESIGN INDEX + CONTEXT PACK**
>
> **CURRENT-STATE BRIDGE: 10 GA SPINES → 11 DOMAIN HUBS**
>
> **COLLECTION / CHARACTER / MECHA / SHIP / PLACE / FACTION / VISUAL / LOSS-PAYOFF-AUTHORITY: GRAPH-REACHABLE**
>
> **FINAL EXACT VISUAL CANON: STILL AUTHOR-CONTROLLED**
>
> **STORY CANON CHANGES CREATED BY GRAPH WORK: 0**
>
> **PUBLICATION: NOT AUTHORIZED**
