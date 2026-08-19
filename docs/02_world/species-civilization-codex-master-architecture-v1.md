# Species & Civilization Codex Master Architecture v1 — 종족·문명 도감 상위 설계

Status: PROPOSED — NONCANON
Effective Authority: NC — design proposal / audit only
Owner Agents: A00 PM / T01 Astroecology / T03 Life Support / P01 Politics / P04 Society / P05 Culture / P06 Factions / C02 Ensemble / M04 Military / H01 Frame Design / X01 Logic / X03 Ethics / X04 Continuity
Last Reviewed: 2026-08-19
Depends On: [[effective-canon-status-manifest-v1]], [[galaxy-612-system-census-and-cluster-atlas-v1]], [[faith-family-and-social-institutions-bible-v1]], [[later-region-cultures-and-ai-ordinary-life-v1]], [[reproductive-genetic-and-continuity-medicine-bible-v1]], [[faction-symmetry-harness]], [[technology-era-and-interoperability-bible-v1]], [[military-doctrine-and-force-structure-bible-v1]], [[galactic-legacy-collection-bible-v1]], [[foundational-prototype-program-and-lineage-architecture-v1]]
Used By: future species entries, civilization/faction design, character bios, multi-species infrastructure, military and frame ergonomics, Archive classification, GA reveal planning
Canon Promotion: NOT AUTHORIZED
Publication: NOT AUTHORIZED
Open Risks: exact species count, named species, homeworlds, first-contact chronology, Empire demographic composition, interspecies reproduction, AXIOM/precursor relation, alien-language implementation, exact faction allocation

---

## 0. Author direction captured

The author explicitly wants the galaxy to possess a reader-facing species catalogue comparable in *world-scale effect* to large space-operas: the setting should not feel like 612 inhabited systems populated only by visually similar humans and AI.

This does **not** authorize arbitrary alien insertion into existing canon scenes. This document creates the architecture required before named species are promoted.

Core design statement:

> 《은하유산록》의 종족은 외형 스킨이 아니라 생물학·환경·생활·문명·정치·산업·군사·기술·법·역사에 실제 차이를 만드는 세계 구성원이다.

---

## 1. Existing-canon compatibility

Current canon gives useful room:

- the 612-system census locks **76.0 billion registered population** plus ~6 billion irregular/mobile/stateless people, but does not lock all of them as one biological species;
- personhood already distinguishes biological humans, substantially modified humans, AI/composite persons and institutional/tool processes;
- faction/culture/species/personhood/geography are already declared separate axes;
- genetic medicine forbids treating morality, loyalty or genius as simple heredity;
- major factions are institutional rather than ethnic by default.

Therefore a multi-species layer can be added **without changing the total census**, provided demographic allocations and prior human-default assumptions are audited before canon promotion.

Hard continuity control:

> no existing character, population, faction or scene is silently reclassified as nonhuman. Any retroactive species assignment requires explicit impact review.

---

## 2. Four galaxy-composition directions

| Direction | Structure | Strength | Failure risk | Verdict |
|---|---|---|---|---|
| A — Human-Centric | humans + AI dominate; 2–4 rare alien peoples | lowest continuity cost | galaxy still feels narrow; species catalogue cosmetic | HOLD |
| B — Federation Mosaic | 8–12 major species with comparable political weight | strongest visible diversity | requires rewriting almost every institution and early scene | TOO DISRUPTIVE |
| C — Human-Majority Multi-Species | humans/posthumans are demographic/planning majority, but 6–8 core nonhuman species and 10–15 regional peoples are normal parts of the lattice | scale + continuity balance | risk of aliens becoming minorities who only decorate human history | **RECOMMENDED BASE** |
| D — Layered Deep-Time Galaxy | current multi-species society + extinct/isolated precursor civilizations + disputed ancient lineages | strongest mystery/archaeology | can make ancient aliens responsible for every technology | **RECOMMENDED OVERLAY** |

### Working proposal

Use **C + controlled D**.

- current society remains legible through existing human-centered opening;
- nonhuman people are neither secret nor shocking in the galaxy at large;
- the Academy opening can remain mostly human/posthuman for local demographic reasons without implying the galaxy is monocultural;
- later travel naturally reveals broader species diversity;
- extinct/precursor civilizations remain few and disputed, not universal master-builders.

---

## 3. Planning count envelope

Counts are planning capacity, not canon quotas.

### Tier S1 — Core intelligent species

Target planning band: **6–8 total current biological species**, including baseline humanity if counted as one.

Requirements:
- recurring named characters across multiple grand acts;
- more than one faction/culture per species;
- ordinary-life representation;
- distinctive biology with infrastructure consequences;
- military/economic roles not reducible to biology.

Reader expectation:
- remembers them across the series.

### Tier S2 — Regional major species / stable derived clades

Target planning band: **10–15**.

Requirements:
- strong regional presence or historical influence;
- 1–3 major arcs rather than whole-series prominence;
- enough ordinary-life detail to avoid costume-only appearance.

### Tier S3 — Rare, isolated, extinct, precursor or disputed peoples

Target planning band: **3–6**.

Functions:
- archaeology;
- migration/extinction history;
- lost language/interface;
- Archive provenance disputes;
- limited legacy-machine mysteries.

Rule:
- S3 does not equal “strongest species.” Extinction, isolation or loss must have material causes.

### Background diversity

Minor local clades, mixed communities and unnamed species can exist in crowd/world references, but do not receive full entries until they matter.

---

## 4. What counts as a species

Do not use one vague “race” bucket.

### BIO-1 — Independent biological species

- stable reproductive lineage;
- distinct evolutionary or engineered biological origin;
- persistent anatomical/physiological difference;
- not merely a nationality or cosmetic phenotype.

### BIO-2 — Human-derived clade

- descendants of humanity changed enough by long-term adaptation/engineering that medicine, reproduction or environment differs materially;
- may or may not be reproductively compatible with baseline humans.

### BIO-3 — Engineered biological lineage

- intentionally created heritable lineage;
- must obey G5 genetic-lineage rules and multi-generational uncertainty;
- cannot be morally or cognitively predetermined by genes.

### BIO-4 — Composite biological/synthetic lineage

- stable population whose ordinary embodiment includes inherited or developmental synthetic systems;
- personhood is not dependent on owning hardware.

Not species by default:
- cyborg;
- veteran with prosthetics;
- gene therapy recipient;
- military enhancement;
- profession;
- nation;
- house;
- religion;
- AI instance/class.

These belong to separate fields.

---

## 5. Species ≠ culture ≠ faction ≠ body modification

Every character/organization may have separate values for:

```text
species / biological lineage
current embodiment or augmentation
home region
culture
language
religion or ethics
citizenship
faction
class
profession
family/house
political ideology
```

Rules:

1. no core species maps to one faction.
2. no core faction maps to one species unless the faction's exclusionary structure is itself a plot fact.
3. every core species must show internal political disagreement.
4. at least one cross-species household, crew, workplace or institution appears before species politics becomes a major plot topic.
5. biology may constrain environments and tools; it may not dictate morality, intelligence, loyalty, courage or political ideology.

---

## 6. Required species-entry schema

Every S1/S2 entry must fill all fields below before canon promotion.

### A. Biological baseline

- body plan / limbs / locomotion;
- average size range and variation;
- preferred gravity range;
- atmosphere/pressure/temperature requirements;
- metabolism and food chemistry;
- sleep/rest cycle;
- sensory modalities;
- communication channels;
- lifespan and developmental stages;
- reproduction and parental investment;
- healing, disease and medical incompatibilities;
- acceleration/radiation tolerance;
- major within-species variation.

### B. Ecology and origin

- home environment;
- natural/engineered origin confidence;
- migration history;
- ecological dependencies;
- disasters/extinctions/bottlenecks;
- whether homeworld is politically central, symbolic, lost or irrelevant.

### C. Ordinary life

- housing and private space;
- food and communal eating;
- clothing/protection;
- sanitation;
- family/kinship;
- childhood and education;
- work;
- leisure/sport/art;
- mourning and death;
- disability and care;
- humor/taboo/body etiquette.

### D. Technology interface

- controls and displays;
- tool ergonomics;
- cockpit requirements;
- suit/environment gear;
- medicine;
- cybernetics/prosthetics;
- AI interaction;
- authentication/identity;
- standard compatibility and failure modes.

### E. Politics and history

- first sustained contact with other lattice peoples;
- colonization/war/treaty history;
- citizenship and discrimination;
- internal nations/factions;
- diaspora;
- class structure;
- major historical wounds and myths;
- what outsiders stereotype incorrectly.

### F. Military and logistics

- typical service roles;
- physiology-related tactical constraints only where real;
- ships/frame ergonomics;
- medical evacuation requirements;
- mixed-unit integration;
- supply burdens;
- surrender/POW/rescue implications.

### G. Story function

- first reader-facing reveal;
- first ordinary-life scene;
- first political conflict;
- first species-stereotype reversal;
- one benefit their biology/environment gives;
- one serious cost;
- one individual who contradicts the dominant cultural stereotype;
- long-term GA payoff.

---

## 7. Species-design lenses for the eventual roster

Do not begin by drawing heads. Begin by assigning **world functions**. Candidate design lenses:

1. **Gravity divergence** — high-g or low-g lineage affects body, architecture and maneuver craft.
2. **Atmospheric divergence** — different gas/pressure creates shared-space politics.
3. **Sensory divergence** — polarized light, vibration, EM or chemical senses change UI and evidence.
4. **Temporal biology** — sleep, maturation or lifespan changes contracts, education and command turnover.
5. **Distributed/colonial body plan** — person/body/legal identity questions without making them hive-mind villains.
6. **Aquatic/fluid-adapted lineage** — habitat, mobility and medical logistics differ substantially.
7. **Radiation/thermal adaptation** — frontier environments and maintenance work differ.
8. **Engineered lineage** — designed for a historical environment but now claims autonomy from creators.
9. **Symbiotic lineage** — personhood and medicine require two biological partners.
10. **Synthetic-development biological lineage** — grows with embedded manufactured structures.

Selection rule:
- each chosen core species must differ on at least **three consequential axes**, not just silhouette.

---

## 8. Human and posthuman position

Humanity remains a major lineage because the opening, Rian, Imperial history and existing social systems are strongly human-readable.

But “human” must not silently mean:
- default citizen;
- default cockpit forever;
- default medical body;
- default language;
- default family form;
- default legal person.

Human-derived groups can range from baseline-compatible adaptation to deeply divergent clades. Exact clades belong in [[posthuman-cybernetic-genetic-diversity-bible-v1]].

---

## 9. AI/composite persons relationship

AI/composite persons are not biological species for census taxonomy.

They still belong in the civilization codex because they can form:
- communities;
- kinship;
- cultures;
- political blocs;
- embodiment traditions;
- mixed households;
- migration patterns.

The codex therefore has two parallel indexes:

1. biological species/lineages;
2. non-biological personhood/civilization forms.

Never force AI diversity into animal-like species categories.

---

## 10. Multi-species infrastructure consequence

A species is not approved as S1 if the world cannot answer how they use:

- mixed-species ships;
- passenger seats/restraints;
- life support;
- toilets/sanitation;
- food storage;
- medical wards;
- prisons/detention;
- schools;
- public transport;
- emergency shelters;
- rescue craft;
- frame cockpits;
- military berthing;
- identification/security scanners;
- burial/mortuary systems.

The shared rules are owned by [[multispecies-infrastructure-rights-and-service-architecture-v1]].

---

## 11. Maneuver-frame consequence

Current canon says humanoid frames arise from neural mapping and industrial work-frame ecosystems and are not the only possible form.

The species layer strengthens this rule.

Controls:

- humanlike two-arm/two-leg frames may remain common because infrastructure and industrial standards converged around them;
- nonhuman pilots may use adapted cockpits, remote embodiments or species-specific chassis where justified;
- not every species deserves a separate silhouette lineage;
- a species-specific chassis exists only if shared hardware imposes a repeated operational cost large enough to justify independent manufacturing/support.

Possible historical implication, **not canonized**:
- one or more foundational prototype slots may have tested cross-body-plan control translation or nonhuman service ergonomics;
- 07's interoperability could later prove useful across species-specific service layers, but this must not retroactively make 07 a universal alien-machine master key.

---

## 12. Faction consequence

The faction harness already requires AI/nonhuman/alien civilization coverage.

New rule proposal:

> “species representation” is satisfied by autonomous people and institutions, not by giving every species a sovereign ethnostate.

A core species should normally have people in at least three of:

- Imperial institutions;
- Helix/industrial networks;
- independent/local governments;
- Neutral/route communities;
- religious/civic movements;
- military organizations;
- diasporas/mixed cities;
- species-majority local polities.

At least one species-majority polity may exist, but monocultural planets cannot be the default.

---

## 13. Archive / Legacy implications

Archive classification must distinguish:

- person;
- species/lineage;
- culture;
- title;
- collective/institution;
- biological ancestry;
- political affiliation.

Blind spot:
- identity compression becomes even more dangerous in a multi-species setting if the Archive merges titles, translation names or collective identities.

Potential payoff:
- a famous “alien hero” may turn out to be a title held by multiple species;
- a supposedly extinct people may survive as mixed descendants, not a secret pure-blood colony;
- “first contact” histories may conflict because trade, rescue and formal diplomatic recognition happened at different times.

Rule:
- do not make species mystery depend on blood-purity reveals.

---

## 14. Deep-time / precursor controls

Ancient/precursor species are allowed only under these controls:

1. no single precursor invented all important modern technology;
2. modern people independently invent and improve systems;
3. ancient artifacts often lose to current infrastructure in maintenance, production, networking and safety;
4. multiple ancient cultures can modify the same artifact across centuries;
5. extinction or disappearance has material and political history;
6. precursor status does not imply moral/intellectual superiority;
7. AXIOM origin remains HOLD.

---

## 15. Reveal ladder across GA1–GA10

This is an exposure proposal, not a scene-card change.

### GA1

- keep opening cast concentration intact;
- background evidence that nonhuman/posthuman citizens exist can appear through workers, records, media or equipment compatibility without new lore lecture;
- 07 remains the only principal machine.

### GA2

- mobile ship/route life is the natural first strong multi-species exposure;
- one or two nonhuman crew/client/community focals can demonstrate ordinary logistics before species politics.

### GA3

- Ardis production and city infrastructure makes multi-species service design materially relevant;
- mass-frame derivative tests ergonomic/public-standard choices.

### GA4

- imperial succession reveals that legitimacy crosses species, provinces, houses and offices; no “human crown owns alien subjects” simplification.

### GA5–7

- mixed fleets expose food, medicine, berthing, acceleration, evacuation and command-integration differences;
- species-majority formations may exist but coalition politics remains institutional.

### GA8

- Archive war introduces extinct/disputed peoples and translation/provenance problems;
- deep-time civilization material can rise without becoming a new genre.

### GA9

- preservation/classification systems risk ranking species-specific documentation, medicine and infrastructure as “nonstandard” and excluding people.

### GA10

- distributed standards must remain interoperable across biological and cultural difference; no final universal body template.

---

## 16. Blind-spot / Red-Team gate

Reject a proposed species if any of these remain true:

- description is mostly skin color/head shape;
- all members share one personality;
- species equals faction;
- biology explains morality/intelligence;
- combat advantage has no metabolic/logistical cost;
- reproduction is used as exotic shock without family/social design;
- infrastructure magically supports them everywhere;
- language difference vanishes without translation infrastructure;
- every named member is a warrior/noble;
- all ordinary labor is still implicitly human;
- humans remain universal medical/legal template with no consequence;
- alien technology is automatically superior;
- species exists only to give a new custom frame silhouette;
- sexual dimorphism or caste is copied directly into political destiny;
- mixed heritage is treated as power-up or purity plot by default.

---

## 17. Next design sequence

1. lock galaxy-composition direction at proposal level (C + D currently recommended);
2. build **species-role demand matrix** before names;
3. propose 6–8 S1 biological slots with distinct biology/ecology/story functions;
4. build multi-species infrastructure baseline;
5. build posthuman/cyborg lineages separately;
6. audit 612-system census for demographic allocation without changing total population;
7. derive factions, characters, ships and frames from role demand;
8. assign GA reveal windows;
9. run continuity/mystery/power-creep red team;
10. only then request author approval for named canon species.

## 18. Current ruling

> **APPROVED FOR FURTHER NONCANON DESIGN, NOT FOR CANON PROMOTION.**

The galaxy should gain a real species/civilization codex. The immediate task is not to invent twenty alien names, but to prove a diversified biological and civilizational ecology that survives infrastructure, law, military, economy, character and long-arc continuity tests.