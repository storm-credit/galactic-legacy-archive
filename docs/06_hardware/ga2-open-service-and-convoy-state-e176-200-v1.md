# GA2 Open-Service & Convoy State v1 — E176–200

Status: WORKING CANON — TECHNICAL/OPERATIONAL LOCK
Owner Agents: T03 Life Support / T05 Technology History / T06 Mecha-Service / T07 Networks / H01 Production / H04 Maintenance / H05 Medical / H06 Damage / M03 Fleet / M05 Logistics / P02 Economy / P03 Law / G02 Counter-Collection / G05 Power Creep / X01 Logic / X03 Ethics / X04 Continuity
Last Reviewed: 2026-08-03
Depends On: Jena Mixed-Service Safety Annex, relay module, E151–175 state, technology/interoperability bible
Used By: [[ga2-e176-185-episode-cards-v1]], [[ga2-e186-193-episode-cards-v1]], [[ga2-e194-200-episode-cards-v1]], accident ledger and open-standard governance
Open Risks: exact reader-facing standard name may be shortened during prose phase; technical function is locked

## 1. E176 Opening Crisis

Helix has withdrawn warranty, remote diagnostics and insurer support from three mixed-standard coolant/filter assemblies used by independent convoy/service craft.

The three cases are intentionally different.

### Assembly A — `CF-A17` / held-back support craft

Function:
- coolant filter/isolation assembly for a small support craft carrying Ardis-bound filters, tools and two crew.

Physical finding:
- genuine seal microcrack and material swelling from an uncertified solvent/cleaning cycle;
- current operation may appear normal at low load;
- repeated heat/pressure cycling creates a real rupture risk.

Ruling:
- **physically unsafe until seal/body replacement and pressure test**.

Helix withdrawal:
- materially justified.

Cost:
- replacement unavailable locally without delay or open/local remanufacture.

### Assembly B — `CF-B09` / independent convoy tug

Function:
- coolant/filter controller used on a tug supporting DG-ARDIS cargo and route services.

Physical finding:
- hardware and current local test state within safe envelope;
- local firmware adds Jena Annex physical-state lines and audit hooks;
- no detected current defect.

Ruling:
- **physically safe enough for bounded operation, but contract/insurance/diagnostic support is withdrawn** because configuration is outside Helix’s certified image and liability model.

Helix withdrawal:
- legally/contractually defensible but coercive in effect.

### Assembly C — `CF-C22` / medical-and-rescue auxiliary

Function:
- filter/valve package supporting temporary medical/rescue loads and mixed old/new service interfaces.

Physical finding:
- hardware is acceptable only if operators use a new manual isolation sequence and a relay adapter;
- old procedure can leave one branch state unobserved;
- current crew lacks full training.

Ruling:
- **conditionally operable after adapter, training and supervised low-load test**.

Helix withdrawal:
- partly justified because current staff/procedure is insufficient; full replacement is not the only remedy.

## 2. Bounded Remedies

| Assembly | Required remedy | Time | Direct cost | Lost service/cargo |
|---|---|---:|---:|---|
| A17 | replace/remanufacture seal/body, material cleanout, full pressure cycle | 36–72 h | 28,000–52,000 BSC | one support craft and Ardis filters/tools delayed |
| B09 | independent witnessed test, insurer rider, bounded local diagnostics | 10–18 h | 11,000–24,000 | tug delay and higher premium |
| C22 | relay adapter, operator training, supervised staged test | 18–30 h | 17,000–33,000 | medical/rescue capacity temporarily reduced |

No single “open adapter” fixes all three.

## 3. Mixed-Service Relay Limits

Relay may:
- expose current state, source, confidence and missing data;
- compare physical readings with controller claims;
- translate stop/queue/capability messages;
- record audit and incident feedback;
- refuse a successful-sync declaration when state is unknown.

Relay may not:
- certify a component;
- assume liability;
- repair physical defects;
- replace trained operators;
- override vessel master, engineer, medical or user stop;
- grant route/insurance standing.

## 4. Open-Service Release 0.7

Working technical label:
- `OSR-0.7 — Open Service Relay profile`.

Reader-facing short form:
- `개방 서비스 규격` or `개방 정비 규격` depending context.

Purpose:
- allow mixed legacy/current machines to exchange bounded service state without one vendor’s complete control.

Core fields:
- component identity and provenance confidence;
- current physical state and independent sensor source;
- queued/current command state;
- safe operating envelope;
- stop and isolation authority;
- operator/training level;
- missing/unknown state;
- incident/version feedback.

Release levels:

| Level | Meaning | Allowed use |
|---|---|---|
| O0 | documentation/observation only | no operational command |
| O1 | supervised local service | low load, physical watchers, manual stop |
| O2 | bounded operational integration | tested hardware/procedure, trained staff, insurer/user approval |
| O3 | networked repeated operation | recurring audits, version control and institutional support |

At E186:
- most real deployments are O0/O1;
- public and sponsor language often falsely implies O2/O3.

## 5. Adoption Pressure

Drivers:
- Helix sanctions/withdrawals;
- shortage of certified parts and technicians;
- many mixed legacy/current systems;
- Jena Annex safety demand;
- independent workshops seek access and income;
- habitats/routes cannot wait for full replacement.

Risks:
- local forks;
- copied old profiles;
- missing physical-state instrumentation;
- inadequate training;
- pressure to remove warnings for throughput;
- insurers treating “open” as no-liability;
- sponsors promoting successful low-load tests as general approval.

## 6. Public Demonstration Site

Working site:
- `Lumen Service Transfer Platform 4`, a public relay/cargo/medical transfer platform used by independent craft and route service teams.

Operation at E193–195:
- demonstrate three mixed coolant/filter branches under OSR-0.7 O1/O2 transition;
- transfer cooling/service load between a route tug, medical auxiliary and platform buffer;
- support current passengers, medical stores and route cargo;
- public/insurer/Helix/worker/user observers present.

## 7. Accident Causal Chain

The accident is not caused by one evil saboteur or one foolish operator.

Locked chain:

1. original documentation does not describe one locally rebuilt bypass branch;
2. field modification changes valve/flow direction labeling;
3. crew training uses a newer certified procedure that assumes automatic queued-state discovery;
4. OSR-0.7 local fork receives stale cached state from one controller after reconnection;
5. physical-state sensor exists but is installed downstream of the critical branch;
6. sponsor schedule compresses the supervised hold period;
7. a competing adapter vendor removes or downgrades an `unknown branch state` warning to improve demonstration throughput and market position;
8. local operator sees apparently consistent successful state across two interfaces;
9. platform load transfers before physical branch confirmation;
10. pressure/temperature rise produces filter-body rupture and hot/chemical coolant release.

The competitor’s manipulation is real but not the sole cause.

## 8. Locked Accident Outcome — E195

No mass-fatality spectacle.

Casualties:
- 1 named permanent major injury: **오벨 나르**, Neris field maintainer/user-safety representative;
- 3 serious but nonpermanent injuries;
- 11 minor exposure/impact injuries;
- no confirmed death in the immediate accident.

Ovel Nar outcome:
- right forearm/hand lost beyond simple biological restoration at current local capacity;
- respiratory/chemical injury causes long-term endurance limits;
- later prosthetic/rehabilitation possible but does not restore prior field role automatically;
- retains testimony, compensation and governance agency;
- not transformed into an inspirational technician mascot.

Service consequences:
- platform branch shut for 9–16 days;
- route/cargo/medical transfers delayed;
- one medical shipment rerouted and partially spoiled/lost;
- OSR-0.7 deployments frozen pending review;
- Helix sanctions and insurer restrictions expand;
- independent workshops lose income and credibility;
- some systems return to vendor-controlled service because it is safer immediately.

## 9. Immediate Technical Outcome

- failed filter body and local controller preserved as evidence;
- relay correctly records some contradictions but cannot prevent the event because the critical physical state was absent/misplaced and warning was downgraded;
- 07/service teams assist isolation/rescue, not combat;
- no hidden automatic rollback or Reactor B solution;
- the public accident validates parts of Helix’s safety critique and parts of worker/user governance critique.

## 10. Governance Required After E195

Open standard cannot resume as a pure code/document release.

Required bodies/functions:
- worker/maintainer seat;
- user/habitat/route operator seat;
- medical/service-dependent representative when connected loads affect care;
- independent insurer/safety review;
- vendor/Helix technical participation where certified components are involved;
- version registry and fork provenance;
- training and role qualification;
- physical-state sensor-placement requirements;
- incident reporting and compensation fund;
- bounded O0–O3 deployment levels;
- right to stop without losing all future access/benefit.

## 11. E200 Target State

- accident cause published with source/confidence and unresolved liability portions;
- competing vendor manipulation identified and sanctioned, but not treated as sole cause;
- OSR-0.7 general deployment remains suspended;
- a narrower O0/O1 emergency-service profile is reauthorized at selected sites;
- Helix field/central factions disagree on cooperation;
- one real defective assembly replaced, one contract-blocked assembly gains bounded rider, one training-dependent assembly passes supervised use;
- grounded support craft partly returns to service, but convoy/service delay and losses remain;
- Ovel Nar survives with permanent injury and independent role in the new governance process;
- no combat upgrade, new frame or free module reward.

## 12. Completion Ruling

> E176–200 mixed-assembly distinctions, open-service release, public-failure causal chain, casualty envelope and governance requirements are locked for episode-card production.