# Species Codex Entry Schema & Promotion Gate v1

Status: PROPOSED — NONCANON
Effective Authority: NC
Owner Agents: T01 Astronomy/Ecology / T03 Habitat-Life Support / P03 Law / P05 Culture-Language / P06 Faction Systems / W06 Ordinary Life / H05 Medical Hardware / M05 Logistics / X01 Logic / X03 Ethics / X04 Continuity / X02 Reader Memory
Last Reviewed: 2026-08-19
Depends On: [[species-civilization-codex-master-architecture-v1]], [[species-role-demand-matrix-v1]], [[multispecies-infrastructure-rights-and-service-architecture-v1]], [[posthuman-cybernetic-genetic-diversity-bible-v1]], [[language-translation-and-intercultural-communication-architecture-v1]], [[planetary-ecology-biosphere-and-environmental-disaster-architecture-v1]]
Used By: every future S1/S2/S3 species entry, character/faction design, visual briefs, scene-card continuity audits
Canon Promotion: NOT AUTHORIZED
Publication: NOT AUTHORIZED
Open Risks: noun overload; one-trait species; biological determinism; hidden infrastructure cost; retroactive cast reassignment

## 1. Purpose

A species entry is approved only when it functions as a **world-system object**, not a concept-art caption.

A complete entry must let a writer answer all of the following without inventing new foundational rules during a scene:

- what the person physically needs;
- what other people notice first;
- how they eat, rest, travel, work and recover;
- how mixed public infrastructure accommodates them;
- how their biology affects but does not dictate politics;
- what common stereotype is wrong;
- what technology fails on them;
- what military/logistics cost follows;
- what ordinary-life scene makes them feel like people;
- when the reader should learn each layer.

## 2. Reader-Facing Tier Labels

### S1 — Core species

Requirements:
- recurring across multiple GAs;
- at least 4 named individuals across different occupations/politics before full-series completion;
- at least 2 ordinary-life scenes;
- at least 3 different institutional/faction contexts;
- visible infrastructure consequence;
- one stereotype reversal on page.

### S2 — Regional major species / stable clade

Requirements:
- meaningful in 1–3 GAs or one large region;
- at least 2 named individuals with different agendas;
- one ordinary-life scene;
- one concrete infrastructure/logistics consequence.

### S3 — Rare / isolated / extinct / disputed people

Requirements:
- archaeology/history/identity function;
- avoid “mystery equals stronger technology” shortcut;
- material explanation for isolation/extinction/disappearance;
- provenance confidence level.

## 3. Canonical Entry Header

Every future entry should begin with:

```markdown
# [Reader-facing species name] — Species Codex

Status:
Species ID:
Tier: S1 | S2 | S3
Biological Classification:
Reader-facing Name:
Self-name(s):
Major Exonyms:
First Reader Exposure:
First Ordinary-Life Exposure:
Primary Regions:
Population Band:
Homeworld/Origin Confidence:
Owner Agents:
Depends On:
Used By:
Open Risks:
```

Do not promote an entry with blank `Open Risks` merely to look complete.

## 4. One-Screen Reader Card

The first screen of an entry must be understandable without reading the full bible.

Required fields:

- **Silhouette:** one sentence.
- **Environment:** gravity / atmosphere / temperature in reader language.
- **Signature sense/body fact:** one memorable but bounded trait.
- **What they need on a ship:** one concrete requirement.
- **What outsiders get wrong:** one stereotype inversion.
- **Where the reader first meets them:** GA/region/role.
- **Why they matter to the larger galaxy:** one institutional/economic/history sentence.

Example structure only:

> Compact four-limbed people adapted to higher gravity. They tolerate load well but overheat easily and require more calories/cooling than their size suggests. Imperial recruiting posters stereotype them as assault troops; most live civilian lives, and their strongest political fights concern industrial injury and cockpit standards.

Do not copy this text into a final species by default.

## 5. Biological Baseline Block

### 5.1 Body plan

Record:
- symmetry;
- limb count and function;
- locomotion;
- resting posture;
- size range;
- mass range;
- body covering;
- major visible sexual/developmental dimorphism if any;
- within-species diversity.

### 5.2 Environment envelope

Record:
- preferred gravity;
- survivable gravity band and duration;
- atmospheric gases;
- pressure;
- temperature;
- humidity/fluid requirements;
- radiation sensitivity;
- light/noise/EM sensitivity.

Separate:
- comfortable;
- tolerable with discomfort;
- medically risky;
- immediately dangerous.

### 5.3 Metabolism

Record:
- food chemistry;
- water/fluid needs;
- oxygen/other respiratory demand;
- caloric range;
- waste products;
- fasting limits;
- common toxicity incompatibilities.

### 5.4 Perception

Record:
- visual spectrum;
- hearing/vibration;
- chemical sensing;
- touch/pressure;
- EM/electrical sensing if present;
- balance/orientation;
- information bandwidth limitations.

Rule:
- unusual sense does not equal perfect truth detection.

### 5.5 Life cycle

Record:
- gestation/development;
- juvenile stages;
- age of independent mobility;
- age of legal-capacity concern;
- average lifespan band;
- senescence pattern;
- reproduction frequency/cost;
- caregiving demand.

No social morality may be inferred from reproductive biology.

## 6. Medicine & Disability Block

Required:
- baseline vital signs;
- common emergency failure modes;
- anesthesia/sedation differences;
- transfusion/biologic compatibility;
- infection ecology;
- prosthetic/cybernetic interface;
- regenerative capacity if any;
- chronic disease patterns;
- occupational injury patterns;
- pregnancy/developmental medicine where applicable;
- death determination.

Disability rule:
- disability emerges from body + environment + interface + access;
- do not define one species as “naturally disabled” in another's habitat without also showing infrastructure politics.

## 7. Ordinary-Life Block

Every S1 must answer:

### Home
- sleep/rest furniture;
- private/public space;
- temperature/light/noise;
- domestic tools.

### Food
- what communal meals look like;
- smell/texture issues;
- cross-species food hazards;
- public kitchen adaptation.

### Sanitation
- waste handling;
- bathing/skin/fluid care;
- public sanitation interface.

### Family & childhood
- kinship does not have to follow reproductive pair;
- guardianship;
- schooling;
- age/status markers.

### Work
- jobs common because of history/economy;
- jobs stereotypically assigned because of biology;
- jobs they are wrongly excluded from.

### Leisure
- at least one sport/game/art form whose physical logic fits their body;
- at least one shared cross-species leisure practice.

### Grief/death
- body handling;
- memorial timing;
- legal-death mismatch;
- mixed-family implications.

## 8. Language & Communication Block

Record separately:

- self-language family;
- spoken/gesture/chemical/tactile channels;
- what can be rendered through standard audio/text;
- translation difficulty;
- common exonym;
- self-name pronunciation burden;
- formal address;
- title/name order;
- nonverbal signals humans commonly misread.

Reader control:
- one easy reader-facing species name;
- self-name appears only when emotionally/politically useful;
- no five unfamiliar nouns in one introduction scene.

## 9. Technology & Interface Block

Required systems:

- doors/handles;
- seats/restraints;
- suits;
- terminals;
- identification scanners;
- weapons/tool grips;
- industrial controls;
- medical beds;
- rescue pods;
- frame cockpit;
- ship duty station;
- personal computing/AI interface.

For each, classify:

- U0 universal/common standard works;
- U1 minor adapter;
- U2 dedicated module;
- U3 species-specific environment or chassis required.

A core species must have at least one U2/U3 issue or it risks being cosmetic.

## 10. Infrastructure Cost Block

Every S1/S2 needs a simple service-cost profile.

Record relative burden versus dominant general-purpose infrastructure:

- berth volume;
- life support;
- food storage;
- water/fluid;
- cooling/heating;
- medical inventory;
- rescue mass;
- sanitation;
- translation/accessibility;
- acceleration limitation.

Do not convert this into a game stat. The purpose is to force material consequences.

## 11. Political & Historical Block

Required distinctions:

- species history;
- cultures;
- states;
- diasporas;
- houses/families;
- corporations/guilds;
- religions/civic movements;
- military institutions.

Required historical questions:

1. Did they join lattice civilization by migration, conquest, treaty, trade, or preexisting coexistence?
2. What event outsiders call “first contact,” and why is that label disputed?
3. What legal status changed their history?
4. What material resource or route shaped their power?
5. What historical stereotype persists after conditions changed?
6. What internal disagreement matters more to them than species unity?
7. What historical harm did members of this species also inflict on others or on each other?

No pure-victim or pure-oppressor species.

## 12. Faction Distribution Gate

Before S1 promotion, prove credible presence in at least **three** distinct contexts from:

- Imperial civil institutions;
- Imperial military;
- Helix/industrial sphere;
- Neutral/route sphere;
- independent/local government;
- civic/religious organization;
- mercenary/gray economy;
- mixed working-class communities;
- academia/medical/research;
- species-majority polity.

At least one context must contradict the reader's first stereotype.

## 13. Military & Logistics Block

Record:

- acceleration envelope;
- EVA/suit needs;
- casualty evacuation;
- field medicine;
- ration burden;
- climate/berthing;
- training adaptation;
- command communication;
- POW/detention requirements;
- frame control translation;
- useful physiology;
- exploitable physiology.

Rule:
- physiology can shape doctrine, never determine loyalty or courage.

## 14. Mecha / Vehicle Block

Ask in order:

1. Can they use existing standard equipment with software/seat adaptation?
2. Is a dedicated cockpit enough?
3. Is a different manipulator/control mapping needed?
4. Does a repeated mission demand justify a separate frame lineage?
5. Can the supply chain sustain it?

Do **not** create species-specific hero machines just because visual design would be cool.

If separate chassis is approved, record:
- mission demand;
- industry;
- maintenance base;
- cross-compatibility;
- failure cost;
- who else uses it.

## 15. Ecology & Homeworld Block

For homeworld/origin environments record:

- star/orbit class only when story-relevant;
- gravity;
- atmosphere;
- water/fluid distribution;
- major biomes;
- producer/decomposer ecology;
- native hazards;
- domestication/agriculture;
- offworld invasive-species policy;
- whether biosphere is native, engineered, mixed or artificial;
- environmental disaster history.

No species gets a homeworld with only one city and one biome unless that is physically justified.

## 16. Stereotype Matrix

Every core entry must include at least four columns:

| Outsider stereotype | Why it arose | What is partly true | What it erases |
|---|---|---|---|

Minimum 3 rows.

Purpose:
- prevent species from becoming the stereotype while still allowing stereotypes to have historical causes.

## 17. Individual Diversity Matrix

Before S1 promotion design at least four **role slots**, not necessarily final named characters:

1. ordinary civilian/worker;
2. technical/professional expert;
3. political/institutional actor;
4. person who strongly contradicts the dominant stereotype.

Optional:
- antagonist;
- religious/civic leader;
- soldier;
- child/elder/dependent;
- mixed-family member.

The species cannot be introduced only through admirals and elite pilots.

## 18. Reveal Ladder

Every entry tracks information disclosure:

### R0 — visual/social recognition
- reader sees that this person is different without lecture.

### R1 — ordinary need
- food, rest, seat, suit, medical or communication difference.

### R2 — institutional consequence
- work, law, transport, military or service issue.

### R3 — historical/political disagreement
- internal diversity and contested history.

### R4 — deep origin
- evolutionary/engineered/precursor question if relevant.

Rule:
- R4 must not arrive before R1/R2 for S1 species. People before lore.

## 19. Similarity / Reference-Distance Gate

Before naming/promotion, compare against likely reference clusters:

- Star Wars species archetypes;
- Star Trek forehead/honor-warrior archetypes;
- Mass Effect species-role archetypes;
- Warhammer species morality essentialism;
- common aquatic, insectoid, reptilian, hive-mind, long-lived elder tropes.

Do not ask “is it similar at all?”
Ask:
- is body plan + culture + military role + politics reproduced one-to-one?
- is the memorable hook merely a reskin?
- does this species have a different material/social engine?

If two or more major axes map too neatly to one reference, redesign.

## 20. Biological Plausibility Gate

Minimum checks:

- body can support its mass under stated gravity;
- heat rejection matches metabolism/activity;
- sensory trait has range/noise limits;
- reproduction supports population history;
- lifespan and casualty history are compatible;
- environment needs can be supplied on ships;
- special advantage has costs;
- no conservation/physics-free trait without explicit technology.

If uncertain, mark `[ASSUMPTION]` rather than pseudo-certainty.

## 21. Continuity Gate

Before a species becomes effective canon:

- search all existing named characters potentially affected;
- search existing early crowd/world references;
- audit “human”, “humanity”, “people”, “citizens”, “crew”, “population” language;
- audit academy recruitment/medical standards;
- audit prison/detention;
- audit military berthing and uniforms;
- audit census wording;
- audit reproduction/medicine;
- audit GA1–10 scene cards for first-appearance timing.

No silent retroactive assignment.

## 22. Promotion Scorecard

All are required for S1:

| Axis | PASS condition |
|---|---|
| Biology | consequential + bounded + plausible |
| Ordinary life | home/food/work/family/leisure/death present |
| Infrastructure | at least one real cost/adaptation |
| Medicine | emergencies and incompatibilities defined |
| Language | reader-safe naming + translation limits |
| Politics | multiple internal positions |
| Factions | >=3 institutional contexts |
| Military | logistics and limits, no destiny doctrine |
| Technology | interface path defined |
| Ecology | origin/home environment materialized |
| Story | reveal ladder + GA payoff |
| Reader memory | introduction noun load controlled |
| Ethics | no biology=morality/intelligence |
| Continuity | no silent rewrite |
| Red team | S0/S1 blockers 0 |

S2 can use a reduced scope but must still pass biology, ordinary life, infrastructure, politics, story and continuity.

## 23. Rejection Conditions

Reject or downgrade a species concept if:

- its only distinction is face/skin/ears;
- it has one culture and one state;
- it is universally good/evil/honorable/merchant/warrior;
- its biology grants an unconditional combat advantage;
- it requires no different infrastructure despite supposedly extreme biology;
- it exists only to supply one hero machine;
- its entire species history is defined by humans;
- it exists only for a precursor mystery;
- it enters too late to feel foundational;
- its name/terminology overloads the early reader window.

## 24. Definition of Done

A species codex entry is `READY FOR AUTHOR CANON DECISION` only when:

1. one-screen card complete;
2. full biology complete;
3. ordinary life complete;
4. infrastructure/medicine complete;
5. faction/political spread complete;
6. logistics/technology complete;
7. ecology/origin complete;
8. reveal ladder assigned;
9. continuity impact listed;
10. similarity red team complete;
11. independent critic complete where available;
12. author-facing unresolved decisions isolated to a short list.

Until then it remains PROPOSED/NONCANON.
