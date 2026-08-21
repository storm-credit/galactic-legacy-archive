#!/usr/bin/env python3
"""Reviewed source-active-pursuit reconciliation for Collection Desire routing.

This module contains workflow/QC routing only. Every ID below already exists in
an approved Collection registry. The reviewed selections reconcile explicit
`Active Pursuit Windows` / episode-facing registry promises with CLSET front
routing when the score-based selector favored adjacent supporting threads.

It does not create collectibles, change ownership, alter episode events, move
payoffs, or make people owned targets. Person/community IDs remain relationship
or authority states with refusal/exit rights.
"""

from __future__ import annotations

# Exact source-registry IDs, maximum five per subact. These are intentionally
# narrow: only rows manually cross-checked against the owning registry's
# Active Pursuit window and current subact reader desire are listed.
REVIEWED_SELECTIONS: dict[tuple[str, str], tuple[str, ...]] = {
    # GA1 — first-100 registry explicit pursuit windows.
    ("GA1", "A1"): (
        "P-001",  # H-001 / current relationship target
        "R-001",  # Betrayal-Trial Relay Fragment — explicit E1–5 pursuit
        "P-005",  # current instructor/field authority
        "I-001",  # student mutual/assembly seed
        "P-011",  # community focal network
    ),
    ("GA1", "A2"): (
        "P-002",  # H-002 / Nera — explicit E6–10 pursuit
        "F-001",  # 07 Core
        "F-002",  # Asymmetric Radiator Wing
        "F-010",  # H-002 Calibration Toolset
        "I-002",  # Open-Service Workshop Seed
    ),
    ("GA1", "A3"): (
        "P-006",  # E-001 / Ern independent objective — explicit E11–15 pursuit
        "R-004",  # Neutral Medical Protection Clause
        "F-011",  # Service Authority Key A
        "R-008",  # External Mission License path
        "P-011",  # community guarantee pressure
    ),
    ("GA1", "A4"): (
        "R-002",  # custody fragments
        "F-001",  # 07 core survival — explicit E16–20 pursuit
        "R-005",  # joint-custody path
        "P-008",  # Neutral claims/medical officer
        "I-001",  # student process carrier
    ),
    ("GA1", "B3"): (
        "F-002",  # radiator
        "F-003",  # manipulator arm
        "F-001",  # core continuity across E33–45 pursuit window
        "R-007",  # H-002 design-rights agreement
        "P-009",  # Helix technical/claim stakeholder
    ),
    ("GA1", "B4"): (
        "F-001",  # missing/returned core
        "R-007",  # design/maintenance rights remain active
        "R-008",  # external mission license — explicit E33–45 pursuit
        "R-012",  # multi-party custody/command scheme
        "P-007",  # Imperial observer/protection stakeholder
    ),
    ("GA1", "C3"): (
        "R-003",  # medical/admin death records
        "R-009",  # consent/data protocol
        "P-011",  # protector/community relationship — explicit E59–72 pursuit
        "F-013",  # Service Authority C protocol fragment
        "P-010",  # Black Ward witness interface
    ),
    ("GA1", "D3"): (
        "R-011",  # provisional joint-operation/protection charter
        "R-012",  # distributed keys/custody
        "F-001",  # restored but bounded 07
        "I-003",  # multi-party medical oversight
        "I-001",  # student assembly/representation carrier
    ),
    ("GA1", "D4"): (
        "R-011",  # grand-act institutional reward
        "R-012",  # distributed key scheme
        "F-001",  # bounded 07 operating state
        "I-003",  # oversight survives central-key relinquishment
        "I-005",  # external mission cell / GA2 handoff
    ),

    # GA2 — explicit Active Pursuit rows whose generated front selection had
    # dropped a named primary thread in favor of adjacent support texture.
    ("GA2", "2A-2"): (
        "G2-S02",  # command charter
        "G2-S11",  # multi-signature comms/identity overlay
        "G2-P01",  # captain
        "G2-P02",  # chief engineer
        "G2-P04",  # quartermaster/claims role
    ),
    ("GA2", "2A-4"): (
        "G2-R02",  # first mission/revenue contract
        "G2-R01",  # route/transit certification
        "G2-S12",  # recycler/passenger capacity branch
        "G2-S13",  # point-defense restoration branch
        "G2-I01",  # first-ship crew/mission trust
    ),
    ("GA2", "2B-1"): (
        "G2-G01",  # duplicate transponder
        "G2-R03",  # salvage joint-claim agreement
        "G2-G02",  # old crew/wage/rescue ledger
        "G2-P07",  # worker/standards council carrier
    ),
    ("GA2", "2B-4"): (
        "G2-S07",  # partial bay 2 / service collar
        "G2-G05",  # Service Authority D — explicit E154–160 pursuit
        "G2-G06",  # open-service lineage map
        "G2-S10",  # relay calibration package
        "G2-G03",  # genuine service collar core
    ),
}

RATIONALE: dict[tuple[str, str], str] = {
    ("GA1", "A1"): "E1–5 source pursuit explicitly includes R-001; generated routing had displaced it with adjacent institutional actors.",
    ("GA1", "A2"): "E6–10 source pursuit explicitly tracks H-002, F-001 and radiator/tool access; the score selector had over-fronted secondary arm/sensor/Helix texture.",
    ("GA1", "A3"): "E11–15 source pursuit explicitly includes E-001/Ern's independent objective alongside medical/service access.",
    ("GA1", "A4"): "E16–20 source pursuit explicitly keeps F-001/core survival in the foreground while joint custody is formed.",
    ("GA1", "B3"): "E33–45 pursuit requires component paths plus H-002 design rights and core continuity; the B3 reader desire is ownership-path comparison.",
    ("GA1", "B4"): "E33–45 pursuit continues through core custody into design rights and external mission licensing; B4 closes those rights rather than substituting unrelated parts texture.",
    ("GA1", "C3"): "E59–72 pursuit explicitly carries protector/community standing together with death records, consent and Authority C.",
    ("GA1", "D3"): "E85–100 source pursuit is charter + distributed keys + bounded 07 + medical oversight under live siege; a single assembly target was under-specified.",
    ("GA1", "D4"): "E85–100 completion must leave charter, split keys, bounded 07 and oversight operating after central authority is relinquished, with the external mission cell as handoff.",
    ("GA2", "2A-2"): "E108–114 source pursuit explicitly includes S11 authentication beside the command charter and licensed crew authority split.",
    ("GA2", "2A-4"): "E122–130 source pursuit is first contract + route certification + one capacity/defense tradeoff; the ghost transponder belongs to the hook into 2B rather than the main pursuit.",
    ("GA2", "2B-1"): "E131–137 source pursuit explicitly names duplicate transponder, salvage claim and old-crew ledger; G2-G02 had been dropped.",
    ("GA2", "2B-4"): "E154–160 source pursuit explicitly names partial Bay 2/relay module, Authority D and lineage map; G2-G05/G06 had been displaced by support texture.",
}

# These registry threads were manually reviewed and are intentionally not
# required as a 1–5 front-stage CLSET target. Their approved function is support
# evidence/tool texture inside a larger pursuit, not a separate reader quest.
ACCEPTED_SECONDARY_ORPHANS: dict[str, str] = {
    "CLT-GA1-F-007": "Thermal Cutter Lance is a dual-use tool acquired inside the E13–16 service/rescue package; the source Active Pursuit window names Authority A / Ern / medical terms rather than a separate cutter quest.",
    "CLT-GA1-F-012": "Service Authority Key B is a custody/continuity clue inside the E33–45 core-rights path; the source Active Pursuit window foregrounds core/components/design rights/license, not Key B as a separate chase.",
    "CLT-GA1-F-014": "Previous Technician Logs support lineage/provenance across several windows and remain deliberately fragmented; they are evidence inside component/core quests, not an independent acquisition quest.",
}
