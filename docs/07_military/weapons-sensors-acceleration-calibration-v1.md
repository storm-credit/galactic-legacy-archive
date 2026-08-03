# Weapons, Sensors & Acceleration Calibration v1

Status: WORKING CANON — AUTHOR-SIDE PERFORMANCE ENVELOPES
Owner Agents: T04 Applied Physics / T06 Mecha Systems / H03 Weapons-Sensors-EW / H06 Combat Physics / M03 Fleet Operations / M04 Frame Tactics / M05 Logistics / X01 Logic / X04 Continuity
Last Reviewed: 2026-08-03
Depends On: lattice physics, military doctrine, technology eras, ship/frame class envelopes
Used By: every battle map, OOB sheet, damage ledger, ship/frame design and tactical scene card
Open Risks: individual named weapon variants may shift ±20% after hull-specific mass/thermal budgets are fixed

## 1. Interpretation Rule

These are author-side design envelopes, not reader-facing RPG statistics.

A quoted maximum is never automatic effective range. Effective performance depends on:

- target signature and aspect;
- observer baseline and sensor quality;
- relative velocity and acceleration uncertainty;
- communication/track sharing;
- ammunition and thermal state;
- countermeasures, debris and local infrastructure;
- legal rules of engagement and target identification;
- whether the objective must survive.

No battle may use a clean range number without recording the detection, classification and fire-control state that makes the shot possible.

## 2. Human and Crew Acceleration Envelope

| Regime | Unprotected/ordinary crew | Trained crew with couch/suit | Specialized pilot capsule | Typical duration |
|---|---:|---:|---:|---|
| comfortable continuous | 0.05–0.20 g | 0.10–0.35 g | 0.15–0.50 g | hours–days |
| combat sustained | 0.20–0.45 g | 0.35–0.80 g | 0.50–1.20 g | minutes–hours |
| emergency burn | 0.45–0.80 g | 0.8–1.8 g | 1.2–3.5 g | 10–180 s |
| pulse maneuver | unsafe | 2–4 g | 3–7 g | 0.5–8 s |
| injury/high-risk | >0.8 g | >4 g | >7 g | case-specific |

Rules:

- acceleration is measured along the crew load axis; lateral loads are more dangerous;
- injured, elderly, pediatric, unrestrained and medically dependent passengers have lower limits;
- repeated pulses accumulate injury and fatigue even when each pulse is survivable;
- artificial-gravity systems manage habitation and low maneuver loads but do not erase combat inertia;
- unmanned missiles and some drones may exceed human limits by an order of magnitude.

## 3. Ship Acceleration and Endurance

| Class | Economic cruise | Combat sustained | Emergency pulse | High-output endurance |
|---|---:|---:|---:|---|
| utility cutter | 0.03–0.10 g | 0.10–0.25 g | 0.4–0.9 g | 4–20 min |
| old utility escort / 회랑새 | 0.025–0.08 g | 0.08–0.20 g | 0.35–0.70 g | 3–12 min before thermal/drive limits |
| modern corvette/frigate | 0.05–0.16 g | 0.18–0.45 g | 0.7–1.4 g | 8–30 min |
| destroyer | 0.04–0.13 g | 0.15–0.38 g | 0.6–1.2 g | 8–25 min |
| cruiser | 0.025–0.09 g | 0.10–0.28 g | 0.4–0.9 g | 10–35 min |
| battleship/heavy carrier | 0.012–0.05 g | 0.05–0.16 g | 0.20–0.55 g | 10–40 min |
| tanker/repair/hospital ship | 0.01–0.05 g | 0.03–0.12 g | 0.15–0.35 g | 3–15 min |

Interpretation:

- smaller does not always mean faster; propellant fraction, radiator state, cargo and drive condition matter;
- a ship can accelerate hard and still be unable to turn its sensor/weapon geometry in time;
- emergency pulses consume maintenance life, reaction mass and crew health;
- 회랑새 may briefly match a healthier escort only by losing later maneuver or damaging systems.

## 4. Frame Mobility Envelope

| Frame role | Sustained free-flight | Short combat burst | Fine-control translation | Typical independent endurance |
|---|---:|---:|---:|---:|
| utility/rescue | 0.05–0.20 g | 0.4–1.2 g | millimeter–centimeter precision | 2–8 h work / 20–60 min combat |
| patrol/security | 0.10–0.35 g | 0.8–2.0 g | decimeter precision | 1–4 h |
| fleet maneuver | 0.20–0.60 g | 1.5–4.0 g | decimeter precision | 30–120 min |
| assault/breaching | 0.12–0.45 g | 1.0–3.0 g | lower due armor/tools | 20–90 min |
| recon/EW | 0.15–0.50 g | 1.2–3.5 g | high sensor/tag precision | 45–180 min |
| 07 mixed service configuration | 0.12–0.40 g | 1.0–3.2 g when healthy | centimeter-scale service control | 35–120 min depending modules |

Frame rules:

- a frame cannot cross strategic space without carrier/tender support;
- high-g maneuver spends propellant and heat budget faster than ammunition;
- debris, structures and line-of-sight often matter more than peak acceleration;
- pilot skill improves prediction, timing and control, not available thrust;
- 07's advantage is interoperability and task switching, not highest raw acceleration.

## 5. Sensor State Ladder

| State | Meaning | Typical decision allowed |
|---|---|---|
| S0 anomaly | unexplained energy/occlusion/statistical change | investigate or increase watch only |
| S1 detection | object/event exists | broad avoidance, cue another sensor |
| S2 track | position/velocity estimate maintained | maneuver relative to target |
| S3 classification | probable class/function/faction | prepare doctrine and ROE |
| S4 identification | specific hull/unit/identity with confidence | legal targeting, hail, claim |
| S5 fire-control solution | continuously updated intercept-quality track | weapon release |
| S6 terminal-quality | local/weapon seeker solution | final guidance or precision disabling shot |

Rules:

- shared tracks retain source confidence and latency;
- classification can be wrong while tracking is accurate;
- identity records do not prove current command or intent;
- a stealth target reduces classification/fire-control quality rather than becoming invisible;
- physical tags, close frames and local operators can produce better S5/S6 data than distant capital sensors.

## 6. Detection and Fire-Control Envelopes

Ranges are broad design bands for a cooperative or moderately emitting target in open space.

| Sensor mode | Detection band | Classification band | High-quality track/fire control |
|---|---:|---:|---:|
| passive thermal, ship-scale | 1–30 million km | 0.2–5 million km | rarely alone |
| active radar/lidar, ship-scale | 0.2–5 million km | 50,000–1,000,000 km | 10,000–300,000 km |
| distributed fleet baseline | 2–80 million km | 0.5–10 million km | 50,000–1,000,000 km |
| node/fixed-array support | 10–200 million km in prepared volume | 1–30 million km | 0.1–5 million km |
| frame local sensors | 500–200,000 km | 100–50,000 km | 10–20,000 km |
| physical tag/boarding sensor | contact–5,000 km | contact–2,000 km | contact–1,000 km |

Modifiers:

- drive burn: ×3–20 detectability;
- radiators exposed: ×2–8;
- cold/coasting target: ÷3–30;
- dense debris/industrial background: classification reduced by 1–3 ladder states;
- authenticated friendly telemetry: may provide S4/S5 but can be spoofed or stale;
- node denial removes large-baseline advantage and forces local search.

## 7. Weapon Families

### W1 — Defensive laser cluster

Role:
- missile/craft interception, sensor dazzling, exposed radiator/tool damage.

Envelope:
- reliable point defense: 10–2,000 km;
- fleet/capital high-energy defense: up to 5,000–12,000 km against bright predictable targets;
- precision damage against maneuvering armored ships declines sharply with range.

Costs:
- heat, optical damage, dwell time, line of sight.

### W2 — Kinetic close-defense guns

Role:
- terminal missile defense, frame/craft suppression, debris clearing.

Envelope:
- 1–300 km typical;
- 300–1,500 km for prepared streams against predictable approach.

Costs:
- ammunition, debris and friendly-fire geometry.

### W3 — Electromagnetic ship guns

Role:
- direct anti-ship, area denial, infrastructure breaching.

Envelope:
- practical maneuvering-target fire: 2,000–40,000 km;
- prepared/large target: 40,000–150,000 km;
- longer shots become prediction/area-denial, not precision hits.

Projectile velocity family:
- 20–180 km/s depending mount and projectile.

Costs:
- recoil management, barrel/rail wear, power and predictable firing signature.

### W4 — Guided kinetic/chemical missiles

Role:
- primary long-range anti-ship and saturation weapon.

Envelope:
- local tactical: 5,000–100,000 km;
- fleet engagement: 100,000–1,500,000 km;
- strategic/node-supported launch: up to several million km with long warning and uncertain terminal state.

Missile acceleration:
- sustained 5–30 g;
- terminal 20–120 g for short periods depending size.

Costs:
- expensive magazines, seeker/EW vulnerability, long time of flight, political escalation.

### W5 — Autonomous loiter/relay munitions

Role:
- sensor extension, ambush, route denial, communication relay, mine-like persistence.

Envelope:
- hours to weeks of local persistence;
- cannot make omniscient target decisions without current ROE and identification.

Costs:
- legal risk, spoofing, recovery and postwar contamination.

### W6 — Particle/charged-beam systems

Role:
- close-to-medium sensor/electronics/radiator disruption and specialized armor damage.

Envelope:
- 100–20,000 km depending focusing and local fields.

Costs:
- extreme power/heat, visible signature, atmospheric/habitat hazard.

### W7 — High-energy spinal laser/beam

Role:
- capital/infrastructure fire, fixed defense, anti-radiator or anti-sensor shot.

Envelope:
- 5,000–80,000 km for meaningful dwell on maneuvering military targets;
- farther against stations, radiators or predicted geometry.

Costs:
- aiming, thermal bloom/optics, charge/recycle time, exposes firing ship.

### W8 — Frame carbine/coil weapon

Role:
- local ship defense, frames, sensors, joints and exposed systems.

Envelope:
- 0.5–2,000 km normal;
- 2,000–10,000 km with shared fire control against predictable targets.

Costs:
- limited ammunition, recoil and collateral penetration.

### W9 — Frame missile/rocket pack

Role:
- short saturation, decoy, breaching and anti-craft.

Envelope:
- 5–50,000 km depending munition;
- frame usually cannot reload in free flight without support.

### W10 — Breaching/cutting/service tools

Role:
- disable, rescue, open hulls, isolate power/cooling, capture infrastructure.

Envelope:
- contact to tens of meters.

Strategic rule:
- often more valuable than destructive fire when the objective is a node, habitat, archive, ship or person.

### W11 — Electronic/cyber-physical attack

Role:
- degrade tracks, authentication, coordination and system trust.

Envelope:
- network path or local electromagnetic access required;
- cannot remotely invent physical permissions, operators or replacement parts.

### W12 — Node/route denial charge

Role:
- block, destabilize or threaten transition infrastructure.

Envelope:
- local physical placement plus timing/authority knowledge.

Costs:
- regional civilian consequences, long repair, legal responsibility and possible self-isolation.

## 8. Defensive Layers

1. intelligence and route avoidance;
2. emission discipline and deception;
3. distributed sensors and classification;
4. long-range interceptors;
5. electronic countermeasures and decoys;
6. escort missile/laser defense;
7. close-defense guns/frames;
8. armor, compartmentation and damage control;
9. rescue, repair and surrender/withdrawal.

A ship surviving one attack does not reset defenses. Missiles, decoys, coolant, optics, crew and compartments remain spent or damaged.

## 9. Thermal State Bands

| Band | Meaning | Consequence |
|---|---|---|
| T0 cold reserve | systems below normal readiness | slow response, low signature |
| T1 routine | normal patrol/industry | sustainable |
| T2 combat warm | sensors/weapons/drives active | hours possible with management |
| T3 high load | repeated weapons/burns | tens of minutes; radiators exposed |
| T4 critical | cooling margin nearly exhausted | weapons/drive choices become exclusive |
| T5 damage risk | local boiling, material/electronics degradation | shutdown or permanent damage likely |
| T6 casualty/failure | crew spaces or primary systems threatened | mission kill, abandon or sacrifice subsystem |

## 10. Ammunition and Sortie Baselines

- patrol cutter: 2–8 major missiles, 200–2,000 close-defense bursts;
- old utility escort: 4–16 major missiles depending conversion, limited reload machinery;
- modern frigate: 16–60 major missiles plus defense magazines;
- destroyer: 48–180 major missiles;
- cruiser: 120–500 mixed major missiles;
- capital arsenal/carrier: hundreds to low thousands across types, but replenishment is theater-scale;
- fleet frame: 1–6 major carried missiles or mission pods plus gun/tool magazines;
- service frame: usually 0–2 offensive pods; tools, tags and rescue stores take volume.

Rules:

- a missile count includes unavailable/damaged/mission-incompatible rounds separately;
- reload at sea requires tender, protected transfer and time;
- magazines are politically and economically traceable;
- a formation that fires most of its long-range magazine may remain intact but strategically unavailable.

## 11. Scene Calibration Checklist

Before every detailed battle, lock:

1. initial positions and relative velocity;
2. sensor state for each side;
3. objective and protected objects;
4. acceleration and passenger limits;
5. thermal band;
6. available ammunition/countermeasures;
7. node/fixed-array support;
8. communication delay and command authority;
9. withdrawal route;
10. damage and expenditure carried into the next scene.

## 12. Hard Prohibitions

- no visible target instantly becomes a fire-control solution;
- no frame crosses system-scale distance without carrier/support;
- no old escort wins a clean gunnery duel with a healthy modern heavy ship;
- no electronic attack replaces physical access, parts and operators;
- no capital weapon fires repeatedly without heat/recycle and signature cost;
- no destroyed magazine, radiator, crew section or drive heals between episodes;
- no exact battle number may override an already locked casualty, travel or asset state without change control.

## 13. Completion Ruling

> Exact baseline weapon, sensor and acceleration tables are no longer deferred.

Hull-specific loadouts and operation-specific states must be derived from this calibration before each battle.