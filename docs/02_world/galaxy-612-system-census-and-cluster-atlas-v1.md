# 612-System Census & Cluster Atlas v1

Status: WORKING CANON DATASET
Owner Agents: T01 Astronomy / T02 Navigation / P01 Politics / P02 Political Economy / M01 Strategy / X01 Logic / X04 Continuity
Last Reviewed: 2026-08-03
Depends On: galaxy-node-fleet-economy-scale-v1, opening corridor, Ardis and GA8–GA10 atlases
Used By: route planning, regional politics, force allocation, trade, future scene cards and visual maps
Open Risks: exact stellar spectra/orbits and minor-system local history remain production detail

## 1. Census Lock

- inhabited systems: **612**
- registered population: **76.000 billion**
- irregular/mobile/stateless population: **approximately 6 billion**, tracked cross-region rather than assigned to one system
- primary node classes:
  - L0: 9 systems
  - L1: 46 systems
  - L2: 192 systems
  - L3: 365 systems
- macroregion allocation:
  - Core: 24 systems / 24.0 billion
  - Inner: 96 systems / 25.0 billion
  - Middle: 180 systems / 18.0 billion
  - Frontier: 312 systems / 9.0 billion

## 2. Cluster Lock

The 612 systems are grouped into **48 operational clusters**. A cluster is a planning region, not a sovereign state. It may contain several polities and more relays than inhabited systems.

- Core: 4 clusters
- Inner: 8 clusters
- Middle: 15 clusters
- Frontier: 21 clusters

## 3. Dataset Fields

`data/galaxy-612-system-census-v1.csv` contains:

- stable system ID;
- reader-facing or author-facing system name;
- macroregion and cluster;
- primary node class;
- registered population in millions;
- two economic/service specializations;
- governance at R0;
- route profile;
- GA10 transition seed;
- protected continuity notes.

## 4. Canon Rules

1. System IDs are stable even if a minor reader-facing name changes through errata.
2. Population values are author-side working figures and may move by ±10% through logged chronology, war or migration.
3. A system's governance label does not mean one faction controls every habitat or service.
4. One inhabited system may contain multiple active/dormant relays; `primary_node` is the highest strategically relevant node.
5. New routes must obey existing queue, distance, authentication and political rules.
6. A local arc may expand one census row into a full city/system bible without changing neighboring rows silently.
7. The census does not imply all 612 systems must appear in prose.
8. Known protected names and roles include Aurel Prime, Lumen, Kael, Brann, Neris, Marn, Silex, Ardis and K-13.

## 5. Population Interpretation

The population field counts recognized registered residents at R0. It excludes:

- mobile crews between systems;
- refugees not accepted into a registry;
- hidden habitats;
- temporary military concentrations;
- duplicate or contested identities;
- most short-term passengers.

The separate approximately 6 billion irregular/mobile figure exists to prevent the census from erasing people whose legal residence is unsettled.

## 6. Use in Story Architecture

- GA1 uses K-13 and the opening corridor.
- GA2 expands Lumen, Kael, Brann, Neris, Marn and Silex.
- GA3 centers Ardis Reach.
- GA4–GA7 activate additional Middle/Frontier clusters as succession and route wars expand.
- GA8 uses Palimpsest North/South and linked archive sites.
- GA9 compares Preservation models across Core, Inner, Middle and Frontier clusters.
- GA10 applies different transition seeds rather than one galaxy-wide decentralization outcome.

## 7. Completion Statement

> The known inhabited lattice now has a complete 612-row census and 48-cluster planning atlas.

Exact planets, moons, orbital elements, local governments and street-level locations remain expandable beneath each stable system row.