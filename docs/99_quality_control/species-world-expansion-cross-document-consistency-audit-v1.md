# Species / World Expansion Cross-Document Consistency Audit v1

Status: QUALITY-CONTROL — NONCANON BRANCH AUDIT
Effective Authority: QC only
Owner Agents: O01 Canon / O02 Gate / X01 Logic / X02 Reader Memory / X04 Continuity / X06 Coverage / A16 Red Team
Last Reviewed: 2026-08-19
Depends On: all PR #188 proposal/QC documents through [[species-world-expansion-author-decision-gate-v2]]
Used By: PR #188 review, future promotion split, next-chat handoff
Canon Promotion: NOT AUTHORIZED
Publication: NOT AUTHORIZED

## 1. Audit question

Does PR #188 now form one internally coherent NONCANON expansion layer, or have the prototype/species/ecology/faction/naming documents begun contradicting each other or current main authority?

Result:

> **PASS WITH EXPLICIT HOLDS — no S0 internal contradiction found.**

The branch contains a large amount of new design, but the governing boundaries remain consistent:
- existing main canon/spec/manuscript is not edited;
- new species facts remain proposal-level;
- history/population/naming decisions are isolated rather than silently canonized;
- 07/AXIOM and GA1–GA10 boundaries remain intact.

## 2. Git-level safety finding

At the latest compare before this audit:
- branch was ahead of main and `behind_by=0`;
- every changed path was an **added proposal/QC file**;
- there were no modifications or deletions to existing main files in PR #188.

Interpretation:
- current canon text has not been silently rewritten;
- merging PR #188 would add proposal/QC material to main, not promote its content to canon by itself;
- final merge still requires author approval under project rules.

## 3. Population and geography invariants

### Locked values checked

- 612 inhabited systems;
- 48 clusters;
- 76.0b registered population;
- ~6b irregular/mobile/stateless population;
- Core: 24 / 24.0b;
- Inner: 96 / 25.0b;
- Middle: 180 / 18.0b;
- Frontier: 312 / 9.0b.

Finding:
- no PR #188 proposal changes these totals.

### Demographic scenario check

DEM-B uses ranges:
- human/human-derived 50–60%;
- core nonhuman combined 30–40%;
- regional/rare 8–15%.

Potential ambiguity found:
- independent range maxima can sum above 100%.

Correction already encoded in [[species-world-expansion-author-decision-gate-v2]]:
- ranges are scenario bands, not independent additive maxima;
- any instantiated demographic mix must sum to 100%;
- `55/35/10` may be used only as a calculation fixture.

Verdict:
- **PASS after clarification.**

## 4. Settlement-sphere terminology conflict

Existing main authority uses:
- `인류 정착격자권 / Human Lattice Sphere`.

PR #188 proposes a genuinely multi-species present.

This is a real semantic/historical conflict, not a numerical contradiction.

Resolution state:
- **HOLD isolated in Decision G**.

Recommended future resolution:
- retain `Human Lattice Sphere` as historical/Core legacy terminology under IMP-D;
- establish one modern neutral formal/common name if author approves;
- do not overwrite the old term as a mere typo.

Verdict:
- **PASS WITH AUTHOR HOLD.**

## 5. Species portfolio-count consistency

Master planning target:
- S1 core: roughly 6–8 reader-important species/peoples;
- S2: 10–15 regional;
- S3: 3–6 rare/isolated/extinct/disputed.

Current branch:
- humanity/human-derived anchor + seven nonhuman functional S1 slots = 8 top-level core entries if humanity is counted;
- S2 active 10 + reserve 4 + one cut/merge;
- S3 functional candidates 4.

Finding:
- all are within the original planning envelope.

Important:
- S1-08 may become human-derived instead of independently nonhuman.
- if so, total biological-origin diversity changes but the reader-memory envelope does not automatically require replacement.

Verdict:
- **PASS.**

## 6. Naming consistency

Problem:
- early proposal files use aliases Braxi / Seia / Numar / Ivra / Tesar / Kelik / Verin.
- external collision screening later rejected or reopened several aliases.

Control now in force:
- stable identities are S1-02 through S1-08;
- [[species-working-name-status-overlay-v1]] explicitly maps old aliases to slot IDs;
- [[species-replacement-name-second-pass-2026-08-19]] holds final naming rather than forcing churn;
- [[species-world-expansion-author-decision-gate-v2]] no longer asks the author to approve the old names.

Finding:
- old labels are stale aliases, not contradictory biology.

Risk:
- a future agent could read an older file without the overlay.

Mitigation:
- promotion/handoff should list overlay as mandatory read;
- one atomic alias migration before any canon-promotion split.

Verdict:
- **PASS WITH NAMING HOLD.**

## 7. Species ≠ faction consistency

Checked across:
- species master architecture;
- faction distribution crosswalk;
- faith/civic organizations;
- houses/orders/mercenaries/local defense;
- character role bundles;
- GA exposure audit.

Shared rule remains consistent:
- biological species does not determine state/faction/culture/religion/class/loyalty;
- same species must appear across different political contexts;
- a species-majority polity does not represent the whole species.

No file authorizes one species = one empire/faction.

Verdict:
- **PASS.**

## 8. Species ≠ dedicated mecha consistency

Checked across:
- species role matrix;
- prototype cards;
- organization→frame crosswalk;
- prototype↔species ergonomics audit.

Shared rule:
1. use standard equipment if possible;
2. use seat/software/adapter module next;
3. dedicated cockpit/environment module if necessary;
4. separate chassis only after repeated mission/production/service demand proves it.

No automatic one-species/one-frame roster is authorized.

Verdict:
- **PASS.**

## 9. 01–20 prototype consistency

Stable proposal rule:
- numbered objects are historical demonstrator slots/test articles, not a modern 20-machine lineup;
- success, partial success, failure and cancellation coexist;
- developmental result and present provenance are separate axes;
- not a collectible scavenger checklist.

Species cross-audit does not redefine the program.

It only marks:
- H03/H09/H15/H17 as species-sensitive secondary pressures;
- H07 as strongest direct service/interface connection.

07 remains:
- service/interoperability ancestry;
- not universal species machine;
- not the strongest frame;
- not proven multi-species pilot-certified.

AXIOM remains:
- separate HOLD;
- not universal master blueprint.

Verdict:
- **PASS.**

## 10. 07 designation/origin conflict remains pre-existing

Known existing tension:
- `CTF-13/07`;
- `AUX-07`;
- `AUXILIA-0` lineage/origin language.

PR #188 does not silently resolve this.

The prototype architecture deliberately avoids naming the whole 01–20 program AUXILIA.

Verdict:
- **PASS / PRE-EXISTING HOLD PRESERVED.**

## 11. Posthuman / cybernetic / species boundary consistency

Shared taxonomy:
- baseline humans;
- human-derived genetic/posthuman lineages;
- cybernetic/prosthetic/embodiment states;
- biological independent species;
- engineered biological lineages;
- AI/composite persons.

Important:
- cybernetic state is not itself a species;
- AI/composite persons are not counted as biological species;
- S1-08 ontology remains explicitly unresolved.

Verdict:
- **PASS WITH S1-08 HOLD.**

## 12. Genetics and reproduction consistency

Existing G0–G5 genetic medicine remains governing authority.

PR #188 does not authorize:
- deterministic genius/loyalty bloodlines;
- universal hidden genetic origin;
- universal cross-species reproduction.

Recommended E2 rule remains proposal-only:
- independent species mostly genetically incompatible;
- limited assisted reproduction only where actual biology permits;
- human-derived clades potentially broader compatibility;
- family/guardianship not defined by genetics.

Verdict:
- **PASS WITH AUTHOR HOLD.**

## 13. Multi-species infrastructure consistency

Shared architecture:
- equal personhood does not imply every site supports every physiology;
- MS0–MS3 describe service capability, not citizen worth;
- adaptation consumes mass, volume, power, staff, training and money;
- emergency scarcity remains real;
- operational separation by environment must not silently become political segregation.

Reference ship and Ardis district both implement the same rule.

Macroregion scaffold is compatible:
- Core/Inner generally higher service density;
- Middle variable;
- Frontier may be less mixed per settlement because support itself is costly.

Verdict:
- **PASS.**

## 14. Planetary ecology consistency

Architecture and five reference cases agree on:
- native/engineered/mixed/closed/damaged/extreme ecology;
- no “breathable = edible/safe” shortcut;
- terraforming is slow, maintained infrastructure;
- ecological damage can outlast wars;
- native life is usually ecologically ordinary, not monster-of-the-week content;
- no requirement to design 612 biospheres.

Front-stage derivation rule remains:
- only worlds that enter story receive full ecological packets.

Verdict:
- **PASS.**

## 15. Crime / gray economy / civic institutions consistency

Crime architecture and faith/civic architecture both obey:
- institutions require money, property, labor, jurisdiction/succession;
- morally positive service does not imply moral purity;
- illicit systems arise from real gaps in sanctions, certification, medicine, title, route and identity;
- organizations act independently of Rian.

No gray group or civic movement is automatically granted a dedicated frame/fleet.

Verdict:
- **PASS.**

## 16. Language / translation consistency

Shared rule:
- routine translation can be excellent;
- legal, medical, military and historical translation preserves liability/provenance;
- non-auditory species channels require interface/interpretation rather than magical universalization;
- public reader-facing name remains simple.

Naming hold is compatible with this because slot IDs are author-side only, not reader-facing canon.

Verdict:
- **PASS.**

## 17. GA1–GA10 continuity consistency

No existing approved scene card has been changed.

Exposure ceiling:
- GA1: X0 background only by default;
- GA2: first 2 S1 recurring ordinary people;
- GA3: normalization in city/public service;
- GA4: law/history only after ordinary coexistence is established;
- GA5: mixed-fleet logistics;
- GA6: no new species, evacuation payoff;
- GA7: same species across multiple sides;
- GA8: S3/deep-history layer;
- GA9: classification/standardization;
- GA10: no novelty push, ordinary plural ending.

This preserves existing act engines rather than adding a species subplot.

Verdict:
- **PASS.**

## 18. Reader-memory consistency

Potential load:
- seven S1 slots;
- up to ten active S2 concepts;
- four S3 functions;
- existing huge cast/faction/mecha vocabulary.

Controls agree across files:
- not all slots are named/foregrounded simultaneously;
- 5–6 species names max central in one subact;
- reuse before introduction;
- GA6+ shifts toward payoff;
- old aliases are not reader canon.

Verdict:
- **PASS IF EXPOSURE CEILINGS ARE ENFORCED.**

## 19. Main-authority modification audit

At audit time PR #188 compare showed only newly added paths.

Therefore it has not changed:
- current Canon Constitution/control docs;
- decision log;
- effective canon manifest;
- existing world bibles;
- scene cards;
- manuscript;
- code/tools/data.

This is intentional.

Future canon promotion must happen through a smaller follow-up change set after author decisions, not by pretending proposal presence equals authority.

Verdict:
- **PASS.**

## 20. Open issue register

### HOLD-01 — Imperial history
Decision A / IMP-D.

### HOLD-02 — Human Lattice Sphere terminology
Decision G; coupled to IMP-D.

### HOLD-03 — exact demographics
DEM-B range only; no fixed percentage.

### HOLD-04 — seven functional S1 portfolio
Safe for design, not approved canon.

### HOLD-05 — S1-08 ontology
Independent engineered nonhuman vs human-derived clade.

### HOLD-06 — reproduction
E2 recommended, not canon.

### HOLD-07 — species names
Slot IDs stable; final public names pending.

### HOLD-08 — exact first-appearance episodes
Exposure architecture exists; card insertion not authorized.

### HOLD-09 — 07/AUX designation reconciliation
Pre-existing issue preserved.

### HOLD-10 — AXIOM
Origin/capability/pilot/deployment still separate HOLD.

No HOLD is hidden as a completed canon fact.

## 21. Final critic verdict

### Internal logic
**PASS**

### Canon preservation
**PASS**

### Reader-load control
**PASS WITH DISCIPLINE REQUIREMENT**

### Naming
**HOLD**

### Historical integration
**HOLD**

### Publication
**NOT AUTHORIZED**

### Overall

> **PASS WITH EXPLICIT AUTHOR-DECISION HOLDS.**

No further generic foundation architecture should be created merely to increase document count.

Next useful work is one of:
1. author resolves A/G/C/D when ready;
2. derive a specific front-stage species/world only when a GA role demands it;
3. run independent promotion critique on this branch;
4. split approved architecture from speculative alternatives before any future canon promotion.