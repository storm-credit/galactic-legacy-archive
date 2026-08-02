# Opening Region Route Graph v1 — GA1–3 고정 항로망

Status: REVIEW
Owner Agents: T01 Astronomy / T02 Navigation-Comms / M01 Grand Strategy / M03 Fleet Operations / P01 Politics / X04 Continuity
Last Reviewed: 2026-08-03
Depends On: galaxy-node-fleet-economy scale, academy map, 10-grand-act map
Used By: GA2 act map, first ship endurance, faction force table, communication clocks, GA3 launch
Open Risks: Final names and astronomical coordinates remain provisional; exact orbital mechanics require later calibration

## 1. Purpose

This graph fixes the first three grand acts to a concrete regional network so that:

- ships and messages cannot move at plot-convenient speed;
- a blocked node creates specific detours and economic effects;
- factions have limited local forces and reinforcement times;
- GA2 frontier missions build directly toward the GA3 node-city crisis;
- community relocation has several materially different destinations rather than one obvious safe haven.

All names are **working Korean-reader labels**. Final linguistic/cultural naming follows later phonetic testing.

---

## 2. Region Summary

Working region:
- `루멘 변경회랑 / Lumen Frontier Corridor`.

Political position:
- outer edge of an Imperial provincial lattice linked to Neutral and Independence routes.
- important enough for traffic and repair, not important enough for immediate Core fleet concentration.

Population in the mapped region:
- approximately 7.4–10.2 million permanent registered residents;
- approximately 0.6–1.1 million transient, stateless or mobile residents;
- most population concentrated at Lumen Gate, Ardis Node City and Kael Free Port.

Strategic functions:
- frontier agricultural/resource traffic;
- old shipyard and open-standard repair traditions;
- correctional/technical education at K-13;
- a secondary route toward Independence-held edge systems;
- one damaged alternative route capable of bypassing Lumen Gate if restored.

---

## 3. Route Graph — Simplified

```text
                                COREWARD
                                   |
                         [N01 Crownline V-4]
                                   |
                         1.1d P / 2.0d C
                                   |
 [N05 Vela Agriring] --- [N02 Lumen Gate L2] --- [N06 Orsen Medical]
        |                     |       \                   |
        |                     |        \                  |
    0.9/1.6d              0.7/1.2d   1.4/2.5d         0.8/1.5d
        |                     |          \                |
 [N07 Doran K-7]       [N03 K-13 Relay]  [N04 Kael Free Port L2]
        |                     |  \             | \
        |                     |   \            |  \
    1.3/2.4d              local   1.6/3.0d  0.8/1.4d  1.5/2.8d
        |                 [Academy/White] \     |        \
 [N08 Lysa Anchorage]                [N09 Brann Yard] [N10 Neris Belt]
        |                                  |              |
    1.8/3.5d                           0.9/1.8d        0.7/1.5d
        |                                  |              |
 [N11 Taris Shadow Route] -------- [N12 Silex Broken Relay] -------- [N13 Marn Graveyard]
            \                             |
             \                        1.6/3.2d damaged
              \                           |
               ---------------- [N14 Ardis Node City L2-candidate]
                                      |
                                EDGEWARD / GA3
```

Legend:
- `P`: military/medical priority operational travel including queue/alignment/recovery.
- `C`: ordinary charter/merchant travel under stable conditions.
- local Academy↔White Dock movement remains in-system, measured in minutes/hours as defined in the Academy map.
- a line means a recognized route; hidden/illegal micro-routes still require a known anchor and cannot ignore graph topology.

---

## 4. Node Register

### N01 — Crownline V-4 / 제국측 관문

Class:
- healthy L2 administrative/military gateway.

Population:
- 1.2–1.8 million across habitats and service settlements.

Control:
- Imperial provincial command with Helix logistics presence.

Function:
- Coreward reinforcements, identity authentication, fleet staging, high-grade parts.

GA2 role:
- source of warrants, inspectors and delayed military pressure.

Normal reinforcement to Lumen Gate:
- 1–2 days after departure, but political authorization and assembly add 3–12 days for meaningful task groups.

Communication:
- Lumen priority packet 5–12 hours.
- K-13 priority packet 10–24 hours through Lumen.

Constraint:
- provincial fleets cannot abandon Crownline’s other routes without exposing Coreward traffic.

### N02 — Lumen Gate

Class:
- established L2 regional node.

Population:
- 2.0–2.8 million.

Control:
- Imperial governor, merchant/industrial councils, Helix logistics, Neutral offices.

Function:
- dominant legal transit, customs, regional market and fleet logistics.

Dependency:
- Vela food, Brann/Neris parts, Crownline authentication, Ardis alternative capacity.

GA2 role:
- contracts, ship title/route permits, customs pressure, regional political background.

GA3 consequence:
- elites fear Ardis becoming an alternative route and political competitor.

### N03 — K-13 Relay / Academy System

Class:
- L3 relay attached to Academy Habitat 13, White Dock and Old Yard.

Population:
- 3,000 academy permanent + 0.2–0.5 million in surrounding civilian/industrial habitats and traffic-dependent settlements.

Control:
- mixed Imperial correction/node authority; White Dock separate civilian/industrial jurisdiction.

Function:
- education, repair, identity/transport records, local relay maintenance.

GA2 role:
- charter origin, first-ship berth, debt and crew recruitment.

Constraint:
- no heavy shipyard; major hull work must use Brann, Neris, Lumen or Kael.

### N04 — Kael Free Port

Class:
- L2-equivalent Neutral/merchant port formed by multiple linked habitats and route beacons.

Population:
- 1.1–1.7 million permanent + large transient traffic.

Control:
- Free Route Neutral Assembly member councils, insurers, ship cooperatives, local security.

Function:
- rescue, arbitration, insurance, mixed-jurisdiction trade, crew market.

GA2 role:
- first-ship registry/insurance, component auction, community relocation option, open-standard debate.

Constraint:
- member ships and councils do not obey one central commander.
- asylum, docking and insurance have capacity/guarantee rules.

### N05 — Vela Agricultural Ring

Class:
- L3 food/biomass production cluster.

Population:
- 0.45–0.75 million.

Control:
- provincial cooperatives and large supply-contract houses.

Function:
- food, biological materials, water-processing cultures.

GA2 role:
- convoy destination/source and leverage during route disruption.

Conflict:
- prefers stable Imperial/Helix contracts; fears frontier rebellion and open-standard accidents.

### N06 — Orsen Medical Habitat

Class:
- specialized L3 medical/biotech relay habitat.

Population:
- 0.22–0.38 million including patients and contract workers.

Control:
- Helix Human Performance Bloc, licensed hospitals, Imperial medical authority.

Function:
- neural treatment, prosthetics, pharmaceutical production, identity-linked care.

GA2 role:
- PC-003 treatment option, Black Ward supply chain, Helix pressure.

Constraint:
- advanced care requires authenticated identity/contract and proprietary supplies.

### N07 — Doran K-7 Cluster

Class:
- weak L3 habitat chain with irregular settlement status.

Population:
- 22,000–38,000 total; H-001’s protected community is one 28–44-person guarantee unit within it.

Control:
- provincial charter authority, local ration boards, informal route/community councils.

Function:
- low-end repair, cargo transfer, labor housing, agricultural support.

GA2 role:
- protected-community crisis and convoy origin.

Constraint:
- life support and legal status depend on bundled contracts through Lumen/Orsen/K-13.

### N08 — Lysa Refugee Anchorage

Class:
- temporary/semi-permanent L3 anchorage and habitat field.

Population:
- 70,000–180,000 fluctuating.

Control:
- mixed Neutral charities, local councils, Independence networks and private contractors.

Function:
- refugee processing, salvage labor, informal markets, route staging.

GA2 role:
- destination option that provides freedom but weak long-term capacity.

Constraint:
- politically divided and chronically underfunded.

### N09 — Brann Yard

Class:
- L3 industrial yard with older military/civilian construction docks.

Population:
- 0.32–0.55 million.

Control:
- Imperial charter corporation, worker guilds, Helix Manufacturing minority stake.

Function:
- medium ship overhaul, frame production, heavy structures.

GA2 role:
- first-ship repair and open-standard manufacturing conflict.

GA3 link:
- workers and capacity may support Ardis or Lumen depending contracts.

### N10 — Neris Workshop Belt

Class:
- distributed L3 belt of family/guild workshops and small habitats.

Population:
- 0.18–0.31 million.

Control:
- workshop guilds, debt houses, partial Helix certification.

Function:
- custom parts, salvage processing, black/gray market compatibility.

GA2 role:
- H-002 network, ghost components, dangerous copied adapters.

Constraint:
- uneven quality, feuds, limited heavy capacity.

### N11 — Taris Shadow Route

Class:
- unofficial route chain using low-capacity beacons and dormant reference points.

Population:
- no single center; approximately 40,000–90,000 mobile/hidden residents across route settlements.

Control:
- Independence localists/liberation cells, smugglers, community councils.

Function:
- evade Lumen customs, move people and evidence.

GA2 role:
- E-001 route and community escape option.

Cost:
- higher loss/repair risk, limited medicine/food, no guaranteed authentication.

Travel:
- Doran→Taris 1.8–3.5 days under good preparation.
- Taris→Ardis 2.5–5.0 days through irregular link, not shown as stable edge.

### N12 — Silex Broken Relay

Class:
- damaged L3 relay/old branch anchor.

Population:
- 12,000–35,000 workers/scavengers around outer facilities; core relay mostly evacuated.

Control:
- contested salvage authority, local crews, Helix claims, Independence interest.

Function:
- possible bypass between Brann/Neris/Taris and Ardis.

GA2 role:
- ghost-parts ship and open-standard war focal infrastructure.

Constraint:
- transition only in limited windows; misalignment causes damage/loss.

### N13 — Marn Graveyard

Class:
- former fleet/industrial debris and storage field around a dormant reference marker.

Population:
- 5,000–20,000 transient salvagers and security.

Control:
- fragmented salvage licenses, criminal/gray crews, Imperial war-claim registry, Helix lien.

Function:
- old hulls, 07 service-line parts, forged relic market.

GA2 role:
- “ghost parts ship” mystery and salvage set.

Constraint:
- radiation/debris/false signals; no reliable full node transition.

### N14 — Ardis Node City

Class:
- damaged high-capacity L3, candidate/recoverable L2.

Population:
- 1.4 million permanent + 120,000–220,000 stranded/transient at GA3 crisis.

Control:
- local council, Imperial governor/claims, worker/industrial blocs, Independence cells, Neutral traffic office.

Function:
- alternative corridor, repair/agricultural transfer, local frame production.

GA2 role:
- destination/market affected by open-standard conflict; target becomes strategically visible.

GA3 role:
- central node-city governance and siege.

Constraint:
- unstable phase reference, fragmented ownership and insufficient capital/parts.

---

## 5. Fixed Travel Edge Table

Times include normal approach, queue, transition and recovery but not days spent waiting for political authorization or cargo assembly.

| Edge | Priority | Chartered/Civilian | Damaged/contested condition |
|---|---:|---:|---|
| N01 Crownline ↔ N02 Lumen | 1.1 d | 2.0 d | 3–6 d under mobilization congestion |
| N02 Lumen ↔ N03 K-13 | 0.7 d | 1.2 d | 2–4 d if K-13 under audit/closure |
| N02 Lumen ↔ N04 Kael | 1.4 d | 2.5 d | 3–7 d with neutrality inspection |
| N02 Lumen ↔ N05 Vela | 0.8 d | 1.5 d | 2–4 d food convoy priority conflict |
| N02 Lumen ↔ N06 Orsen | 0.7 d | 1.3 d | 2–5 d medical identity quarantine |
| N05 Vela ↔ N07 Doran | 0.9 d | 1.6 d | 2–4 d during ration disputes |
| N07 Doran ↔ N08 Lysa | 1.3 d | 2.4 d | 3–6 d refugee congestion |
| N08 Lysa ↔ N11 Taris | 1.8 d | 3.5 d irregular | 4–8 d / route closure risk |
| N03 K-13 ↔ N09 Brann | 1.6 d | 3.0 d | 4–7 d heavy-tow/repair load |
| N04 Kael ↔ N09 Brann | 0.8 d | 1.4 d | 2–4 d insurance/yard queue |
| N04 Kael ↔ N10 Neris | 1.5 d | 2.8 d | 3–7 d customs/gray-market risk |
| N09 Brann ↔ N12 Silex | 0.9 d | 1.8 d | 3–9 d limited window |
| N10 Neris ↔ N13 Marn | 0.7 d | 1.5 d | 2–5 d debris/salvage traffic |
| N13 Marn ↔ N12 Silex | 0.8 d equivalent tug/courier | 1.7 d | no large-ship transition; physical route hazards |
| N12 Silex ↔ N14 Ardis | 1.6 d successful window | 3.2 d | 5–14 d or impossible if reference slips |
| N11 Taris ↔ N14 Ardis | 2.5 d ideal irregular | 5.0 d | 6–15 d / high failure and no insurance |

No unlisted stable direct edge exists in GA2.

---

## 6. Communication Delay Table

Small authenticated priority packet under healthy nodes:

| From | To | Typical delay |
|---|---|---:|
| K-13 | Lumen | 5–12 h |
| K-13 | Crownline | 12–30 h |
| K-13 | Kael | 10–24 h |
| Doran | K-13 | 12–30 h |
| Neris/Marn | K-13 | 1–3 d |
| Silex | K-13 | 2–6 d depending window |
| Ardis | K-13 | 3–8 d via Silex or 4–10 d via Taris/Kael chains |

Data classes:

- Class A: short signed order/identity proof — fastest.
- Class B: compressed report/medical request — moderate bandwidth.
- Class C: full sensor/maintenance/case archive — 2–10× longer or multiple windows.
- Class D: neural model, AI state, master evidence — physical courier strongly preferred.

Rule:
- a Class A summary may arrive days before its Class C evidence, letting political narratives harden first.

---

## 7. GA2 Route Use

### Episodes 101–130 — Debt-Bought Ship

Primary locations:
- N03 K-13 → N02 Lumen → N04 Kael → N09 Brann.

Purpose:
- title/insurance/crew/repair negotiation and first voyage.

Minimum travel consumed:
- 4–8 days priority movement plus inspections/yard time; narrative can cover several weeks through mission/repair pacing.

### Episodes 131–160 — Ghost Parts Ship

Primary locations:
- N04 Kael → N10 Neris → N13 Marn → N12 Silex → possible N09 Brann return.

Purpose:
- salvage, false legacy records, missing ship/component and open-service lineage.

Constraint:
- damaged routes and no instant return; help is days away.

### Episodes 161–185 — Protected-Community Convoy

Primary locations:
- N07 Doran, N05 Vela, N08 Lysa, N06 Orsen, N11 Taris and possible N14 Ardis destinations.

Purpose:
- community members choose different routes; convoy cannot keep everyone together.

Constraint:
- food/medical/identity routes conflict.

### Episodes 186–210 — Open-Standard War

Primary locations:
- N09 Brann, N10 Neris, N12 Silex, N14 Ardis, with Lumen/Helix sanctions.

Purpose:
- emergency compatibility standard spreads; accidents, embargo, sabotage and node-restoration politics.

End:
- Ardis adopts or requests the standard, making GA3 conflict inevitable.

---

## 8. Regional Reinforcement Clocks

### Imperial provincial force

- local cutters at Lumen/K-13: hours to 2 days.
- credible frigate/destroyer task group from Crownline: 5–14 days including authorization/assembly.
- major fleet concentration: 4–10 weeks and visible politically/logistically.

### Helix

- contract/security craft from Orsen/Lumen/Brann: 1–5 days.
- parts embargo/account freeze: hours to 2 days after signed order reaches node.
- major industrial/security response: 1–4 weeks.

### Independence

- local cells at Taris/Lysa/Doran: hours to days.
- coordinated regional flotilla: 1–3 weeks and uncertain compliance.
- large coalition: not possible in GA2 without exposing routes and political split.

### Neutral Assembly

- nearby rescue/courier response: 0.5–3 days depending contract/capacity.
- broader member mobilization: weeks, with no guaranteed common command.

---

## 9. Route-Break Consequences

If Lumen Gate closes:
- Crownline/Core access slows drastically.
- Kael/Brann/Neris traffic detours; food/medical prices rise.
- Silex/Ardis bypass becomes strategically valuable.

If Silex is restored:
- Ardis gains alternative corridor and bargaining power.
- Lumen, Helix and Imperial governor may resist or seek control.
- Independence and workshop networks gain legal route option.

If Doran contracts freeze:
- residents cannot simply walk to another node; evacuation requires vessels, slots, identity, supplies and destination acceptance.

If Kael denies insurance/berth:
- first ship may still travel but loses legal cargo/passenger access and cannot safely resupply many routes.

---

## 10. Continuity Checklist

Every GA2 movement record must specify:

- departure node and local berth.
- destination and route edge.
- authorization/queue class.
- departure/arrival time.
- ship acceleration/heat/repair state.
- communication sent and arrival time by data class.
- cargo/passengers and life-support endurance.
- faction control and inspection conditions.
- missed alternatives and detour cost.

## 11. Gate Status

PASS for:
- fixed 14-node opening graph.
- travel and communication classes.
- political/economic functions.
- GA2 route assignments and reinforcement clocks.
- GA3 causal launch.

OPEN:
- final names, coordinates and star types.
- detailed local orbital maps beyond K-13/White Dock.
- per-edge toll/price/capacity.
- route changes after GA2 interventions.
