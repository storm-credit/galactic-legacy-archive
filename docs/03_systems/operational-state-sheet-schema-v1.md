# Operational State Sheet Schema v1 — 함선·함대·노드·인구·보급 상태 기록 규격

Status: REVIEW — EXECUTION INFRASTRUCTURE
Owner Agents: O01 Canon / X04 Continuity / M03 Fleet / M05 Logistics / T03 Habitat / N03 Episode
Last Reviewed: 2026-08-03
Depends On: [[master-series-chronology-v1]], GA1–10 state checkpoints, route/fleet/node bibles
Used By: every mission, battle, evacuation, node operation and grand-act boundary
Open Risks: automation/validation scripts not yet implemented

## 1. Purpose

Every major operation receives a dated state sheet before scene cards or prose.
The sheet prevents:

- ammunition, heat, crew or passengers resetting between episodes;
- ships appearing at impossible locations;
- institutions gaining authority without keys/staff/recognition;
- population and medical capacity changing to fit a dilemma;
- hidden reinforcements or supplies solving a climax;
- battle damage disappearing after a hook.

A state sheet is operational truth for the design team, not necessarily reader-facing text.

---

## 2. Required Header

```yaml
state_id:
canon_date_start:
canon_date_end:
episode_range:
grand_act:
operation/location:
owner_agents:
previous_state_id:
next_state_id:
confidence:
status:
```

Confidence:
- `LOCKED`: figures/routes are fixed.
- `BAND`: approved numerical range.
- `PROVISIONAL`: structure fixed, number pending simulation.

---

## 3. Time and Communication

```yaml
time:
  local_reference:
  elapsed_hours:
  route_windows:
  message_sent:
  message_arrival:
  data_class:
  queue_or_authorization_delay:
```

Rules:
- record event time and information time separately.
- a commander cannot use a message before arrival.
- full sensor/medical/archive data may arrive after the short signed summary.
- time spent aligning, docking, repairing and treating is not skipped.

---

## 4. Location and Route

```yaml
location:
  node_system:
  local_orbit_or_district:
  valid_edges:
  damaged_edges:
  denied_edges:
  travel_time_priority:
  travel_time_civilian:
  destination_acceptance:
```

Rules:
- no unlisted stable direct edge.
- destination acceptance/berth/identity capacity is part of route feasibility.
- a route is not “open” if ship class, mass, authentication or recovery capacity cannot use it.

---

## 5. Ship State

For each front-stage ship:

```yaml
ship:
  registry:
  reader_name:
  class:
  location:
  title_holder:
  operating_charter:
  captain:
  mission_commander:
  crew_required_min:
  crew_available:
  crew_fatigue:
  passengers:
  medical_cases:
  cargo_modules:
  mass_band:
  propellant_percent:
  reactor_state:
  coolant_state:
  radiator_state:
  heat_reserve:
  acceleration_band:
  frame_bays:
  missiles:
  interceptors_decoys:
  point_defense_mounts:
  sensors_comms:
  structural_damage:
  legal_restrictions:
  next_required_maintenance:
```

Crew fatigue:
- Green: normal shifts.
- Amber: double shifts/reduced judgment.
- Red: unsafe sustained operation.
- Black: legally/physically unable to continue without relief.

Heat reserve:
- expressed as current operational band and the combination that would exhaust it, not an arbitrary energy bar.

---

## 6. Frame State

```yaml
frame:
  registry:
  pilot:
  physical_location:
  mission_role:
  structural_state:
  reactor_power:
  propellant:
  heat_state:
  ammunition_tools:
  sync_load:
  pilot_medical_state:
  launch_recovery_time:
  service_crew:
  authorization:
```

Rules:
- pilot state and machine state are separate.
- a repaired frame may remain unusable because pilot, cradle, keys or crew are unavailable.
- 07’s tools/service interfaces are tracked separately from weapons.

---

## 7. Fleet/Formation State

```yaml
formation:
  name:
  commander:
  mandate:
  combat_hulls_present:
  combat_hulls_ready:
  support_hulls_present:
  support_hulls_ready:
  frames_ready:
  missile_stock_band:
  repair_capacity:
  medical_rescue_capacity:
  command_latency:
  withdrawal_condition:
  local_obligations:
  cohesion:
```

Cohesion:
- `Unified`: one lawful/accepted mandate.
- `Contracted`: mission-specific alignment.
- `Conditional`: key formations may withdraw/refuse.
- `Fragmented`: orders interpreted separately.
- `Hostile Split`: active internal conflict.

Rule:
- reader-facing battle tracks 3–7 formations; state sheet may hold more.

---

## 8. Node/Habitat State

```yaml
node:
  name:
  class:
  active_spines_or_arrays:
  nominal_capacity_percent:
  current_safe_capacity_percent:
  next_windows:
  power_state:
  thermal_state:
  authentication_holders:
  physical_operator:
  traffic_controller:
  defense_coupling:
  structural_damage:
  service_dependencies:
  shutdown_or_denial_options:
```

Habitat:

```yaml
habitat:
  permanent_population:
  transient_population:
  life_support_days:
  food_days:
  water_air_state:
  advanced_medicine_days:
  power_heat_state:
  evacuation_capacity:
  shelter_medical_capacity:
  unrest_or_labor_state:
```

---

## 9. Population and Manifest

```yaml
population_group:
  name:
  count_band:
  registered:
  unregistered_or_contested:
  minors_dependents:
  critical_medical:
  caregivers:
  skilled_operators:
  transport_ready:
  destination_accepted:
  baggage_tools_mass:
  choice_or_representative:
  stranded_risk:
```

Rules:
- “civilians” is never one undifferentiated number.
- caregivers, operators, records and tools affect whether transported people survive after arrival.
- manifest changes require signer, reason, time and those displaced.

---

## 10. Supplies and Finance

```yaml
supplies:
  basic_food_days:
  medical_consumables_days:
  advanced_treatment_units:
  water_air_consumables:
  propellant:
  reactor_consumables:
  frame_parts:
  ship_parts:
  missiles_interceptors:
  currency_credit:
  payroll_due:
  insurance_claim_state:
```

Rule:
- money/credit cannot buy goods that are not physically reachable or politically released.
- mission revenue is recorded after damage, wages, claims and resupply, not as gross reward.

---

## 11. Authority and Records

```yaml
authority:
  physical_control:
  operational_control:
  legal_title:
  authentication_keys:
  mission_authority:
  medical_stop:
  technical_stop:
  passenger_consent:
  data_release:
  emergency_override:
  expiry_review:
```

Record state:

```yaml
records:
  official_summary:
  primary_sources:
  contested_sources:
  missing_sources:
  current_legal_effect:
  known_false_compression:
  correction_owner:
```

Rule:
- knowing truth does not itself transfer legal/physical authority.

---

## 12. Casualty and Damage Ledger

```yaml
losses:
  killed_confirmed:
  missing:
  captured:
  severe_injury:
  displaced:
  hulls_destroyed:
  hulls_abandoned:
  frames_lost:
  infrastructure_lost:
  records_person_states_lost:
  confidence_and_source:
```

Rules:
- initial estimates and final verified figures remain separate.
- corrections never erase physical harm.
- casualties include crews, workers, caregivers and downstream service deaths where causally supported.

---

## 13. Scene Dependency Fields

For every planned scene using the state:

```yaml
scene_dependency:
  starting_fact:
  character_belief:
  unavailable_information:
  choice_enabled:
  choice_blocked:
  state_changed:
  cost_carried_forward:
```

A scene fails the state harness if:
- it uses an unavailable asset/message;
- damage/supply/fatigue does not persist;
- an authority acts outside mandate without consequence;
- population/capacity numbers change without an event;
- the ending state cannot produce the next scene.

---

## 14. Version Control

- one state ID per operation phase, not every paragraph.
- changes after scene-card lock require a delta note.
- exact numbers may narrow inside an approved band, but cannot leave it without red-team review.
- any change affecting a CORE payoff, named death or final asset fate requires O01/O02 sign-off.

## 15. Gate Status

PASS as execution schema.

OPEN:
- machine-readable validator.
- automated timeline/route checker.
- exact GA snapshots and operation sheets.
