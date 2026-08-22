# Organization-to-Frame-and-Ship Role-Demand Crosswalk v1

Status: PROPOSED — NONCANON
Effective Authority: NC — demand architecture only
Last Reviewed: 2026-08-19
Depends On: [[military-intermediate-organization-role-demand-matrix-v1]], [[knightly-service-order-archetypes-v1]], [[gray-layer-mercenary-pirate-and-illicit-network-archetypes-v1]], [[frontier-defense-garrison-reserve-and-emergency-force-architecture-v1]], [[maneuver-frame-lineup-master-architecture-v1]], [[frame-lineup-faction-coverage-gap-2026-08-13]]
Used By: maneuver-frame lineup revision, ship roster demand, manufacturing lineage design
Canon Promotion: NOT AUTHORIZED
Publication: NOT AUTHORIZED

---

## 0. Rule

This file does not create named machines.

It derives **role demand** from organizations before any chassis is approved.

A role demand can be satisfied by:
- an existing mass-production family;
- a mission variant;
- a cockpit/environment adaptation;
- a specialist frame;
- a new independent chassis only when the chassis gate passes.

---

## 1. Frame-role codes

- FR-SRV — service/rescue
- FR-UTL — utility/industrial
- FR-PAT — patrol/security
- FR-FLT — fleet maneuver
- FR-BRE — assault/breach
- FR-REC — recon/sensor
- FR-EW — electronic warfare
- FR-CMD — command/coordination
- FR-LNG — long-endurance/low-logistics
- FR-MED — medical/casualty support
- FR-ENV — extreme-environment/species-geometry adaptation
- FR-ELT — limited elite/custom

Ship-role codes:
- SH-CUT patrol/cutter
- SH-COR corvette/light escort
- SH-FRG frigate
- SH-DST destroyer
- SH-TRN transport
- SH-TND tender/mobile workshop
- SH-TUG tug/salvage
- SH-MED hospital/rescue
- SH-REC sensor/relay
- SH-CMD command/evidence

---

## 2. Organizational demand matrix

| Organization | Primary frame demand | Secondary demand | Unique chassis pressure | Primary ship demand | Notes |
|---|---|---|---|---|---|
| Provincial Regular Defense | FR-PAT, FR-FLT, FR-LNG | FR-REC, FR-CMD, FR-SRV | LOW/MED | SH-COR, SH-FRG, SH-TND | environment may justify one regional structural branch |
| Civic/Habitat Militia | FR-UTL, FR-PAT, FR-SRV | FR-MED | VERY LOW | SH-CUT, SH-TUG | should mostly reuse civilian/common designs |
| Imperial/State Garrison | FR-FLT, FR-PAT | FR-BRE, FR-REC, FR-CMD | LOW | SH-COR, SH-FRG, SH-DST | standardized state families dominate |
| Reserve Pool | FR-PAT, FR-FLT | FR-UTL | VERY LOW | SH-CUT, SH-COR, SH-TRN | older maintainable families matter |
| Household Guard | FR-PAT, FR-FLT | FR-CMD, FR-REC | LOW | SH-COR, SH-CMD | prestige ≠ unique chassis |
| Route Shield Order | FR-FLT, FR-SRV, FR-LNG | FR-REC, FR-CMD | LOW | SH-COR, SH-FRG, SH-TND, SH-MED | convoy + rescue identity |
| Node Custodian Order | FR-SRV, FR-BRE | FR-EW, FR-CMD, FR-REC | MED | SH-COR, SH-TND, SH-CMD | infrastructure-safe breach may justify specialist chassis |
| Witness/Custody Order | FR-PAT, FR-SRV | FR-MED, FR-REC | LOW | SH-CUT, SH-MED, SH-CMD | low-collateral focus |
| Expeditionary Service Order | FR-SRV, FR-UTL, FR-LNG | FR-FLT, FR-ENV | MED | SH-TRN, SH-TND, SH-COR, SH-TUG | multi-environment architecture pressure |
| House Retainer Corps | FR-PAT, FR-FLT | role-dependent | LOW | SH-CUT, SH-COR | mostly licensed models + house modifications |
| Contract Combat Company | FR-FLT, FR-LNG | FR-BRE, FR-REC | LOW | SH-COR, SH-TRN, SH-TND | repairability dominates |
| Security/Recovery Cooperative | FR-SRV, FR-PAT | FR-MED, FR-REC | LOW | SH-TUG, SH-CUT, SH-TND | recovery tools, not heavy war mass |
| Raider Flotilla | FR-FLT, FR-PAT | FR-BRE, FR-LNG | LOW | SH-COR, SH-TRN, SH-TND | captured/modified common chassis |
| Smuggler Network | FR-UTL, FR-SRV | FR-ENV | VERY LOW | SH-TRN, SH-CUT | hidden life-support and cargo variants |
| Black-Market Technical Network | no standing force | all as modification source | N/A | no standing demand | source of parts/variants, not clean lineup class |
| Rescue/Salvage Order | FR-SRV, FR-UTL, FR-MED | FR-LNG, FR-ENV | MED | SH-TUG, SH-MED, SH-TND | one strongest justification for noncombat specialist designs |
| Worker Defense Compact | FR-UTL, FR-SRV, FR-PAT | FR-FLT | LOW | SH-TUG, SH-CUT, SH-TND | industrial conversions/common service ancestry |
| Species-majority Regional Defense | role-dependent | FR-ENV | MED/HIGH only if geometry/environment structural | role-dependent | species identity alone is insufficient |
| Multi-species Corridor Service | FR-SRV, FR-MED, FR-ENV | FR-PAT, FR-LNG | MED | SH-MED, SH-TND, SH-TRN | universal rescue accommodation drives design |
| AI Custodian Force | FR-REC, FR-EW, FR-CMD | FR-SRV, remote craft | MED | SH-REC, SH-CMD, SH-TND | compute/power/logistics remain physical |
| Mission Trust Coalition | mixed | FR-CMD, FR-SRV | NONE by itself | all mixed | interoperability layer, not chassis family |

---

## 3. What this does to the current lineup gap

Prior QC found three broad classes at zero role demand:
- mercenary/pirate/black-market;
- AI/nonhuman/alien;
- religion/ideology/civic movement.

New audit correction:

### Mercenary/pirate gap — REAL HARDWARE DEMAND

This class genuinely creates missing demand in:
- maintainable long-endurance/common combat frames;
- recovery/capture configurations;
- mobile repair support;
- irregular cross-standard service.

But it does **not** justify many unique chassis.

### AI/nonhuman/alien gap — PARTLY REAL, PARTLY CONDITIONAL

AI/person communities create:
- recon/EW/command/service demand.

Biological species create an independent chassis only where:
- body geometry;
- control architecture;
- environment;
- structural load;
- life-support placement
force a chassis-level redesign.

Therefore “one alien species = one new mech line” is rejected.

### Religion/ideology/civic movement gap — NOT AUTOMATIC HARDWARE DEMAND

These groups may use:
- existing security/rescue frames;
- standard militia equipment;
- no armed equipment at all.

Their absence from a **faction** portfolio is a worldbuilding question, not automatically a frame-lineup defect.

This corrects the earlier assumption that every required faction class needs a dedicated machine slot.

---

## 4. Minimum modern production-family demands

Without naming models, the world needs enough reusable families to satisfy multiple organizations.

### PF-01 Common Patrol/Security Family
Users:
- provincial defense;
- militia;
- garrison;
- household guard;
- private security;
- custody order.

Must be:
- affordable;
- easy to train;
- docking/habitat safe;
- modest endurance.

### PF-02 Fleet Maneuver Mass Family
Users:
- Imperial/state fleet;
- provincial defense;
- knightly escorts;
- mercenary companies;
- raiders via surplus/capture.

Must be:
- scalable;
- carrier-compatible;
- robust formation networking.

### PF-03 Service/Rescue Family
Users:
- rescue orders;
- worker networks;
- militia;
- multi-species corridor service;
- expeditionary orders.

Strong candidate to carry open-service/AUXILIA-descended principles in some branch.

### PF-04 Frontier Low-Logistics Family
Users:
- provincial defense;
- expeditionary order;
- mercenary companies;
- remote settlements.

Must trade peak performance for:
- endurance;
- repairability;
- heterogeneous supply tolerance.

### PF-05 Assault/Breach Family
Users:
- regular military;
- node custodian specialists;
- some mercenary assault teams.

Must remain expensive/support-heavy so it does not replace general frames.

### PF-06 Recon/EW Family
Users:
- fleets;
- garrisons;
- AI custodian forces;
- private technical security.

May share structural chassis with PF-02 if independent-chassis gate fails.

### PF-07 Command/Coordination Family
Users:
- fleets;
- orders;
- mission trusts.

Likely limited production; network dependency must be visible.

### PF-08 Extreme-Environment / Nonstandard-Body Structural Family
Users:
- only populations/regions whose physiology/environment actually requires it.

This may become **several regional chassis**, but only after species physics are locked.

---

## 5. Specialist variant demands that should NOT create new chassis by default

- medical evacuation pack;
- custody/nonlethal kit;
- long-range fuel/heat pack;
- species cockpit insert where geometry permits;
- atmosphere/liquid environmental shell;
- ceremonial guard armor;
- pirate weapon modification;
- house heraldry;
- mercenary sensor package;
- rescue thermal shielding;
- reserve training software.

These are variants/configurations until proven otherwise.

---

## 6. Reader-facing lineup implication

The setting can support many organizations without exploding the number of named frames.

Recommended structure remains:

```text
small number of industrial production families
→ several mission/region derivatives
→ organization-specific configurations
→ very few true unique machines
```

A reader should recognize:
- “that is an Imperial fleet family”;
- “that mercenary unit uses old provincial frames”;
- “that order uses a rescue-derived specialist variant”;

without needing a new proper noun for every silhouette.

---

## 7. Prototype-program crosswalk

Potential hypothesis ancestry for production families:

| Production family | likely historical hypotheses |
|---|---|
| PF-01 Patrol/Security | H01, H06, H19 |
| PF-02 Fleet Maneuver | H02, H03, H09, H14, H19 |
| PF-03 Service/Rescue | H04, H07, H10, H17 |
| PF-04 Frontier Low-Logistics | H06, H08, H18, H20 |
| PF-05 Assault/Breach | H03, H05, H11 |
| PF-06 Recon/EW | H12, H13, H16 |
| PF-07 Command | H12, H14, H17 |
| PF-08 Extreme Environment | H02, H15, H20 + species-specific requirements |

Rule:
- these are ancestry hypotheses, not slot-number assignments.

---

## 8. Next gate before model naming

Before adding named chassis to the current proposed lineup:

1. map the existing 28 proposed models to PF-01…PF-08 and specialist variants;
2. identify duplicate models satisfying the same demand;
3. identify true empty production families;
4. apply species structural requirements after biology lock;
5. determine whether the candidate portfolio needs 32–40 entries or can meet demand with fewer reusable families plus variants;
6. only then name/add/remove models.

This prevents filling the old “+4 missing slots” mechanically.
