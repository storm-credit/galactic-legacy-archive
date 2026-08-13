#!/usr/bin/env python3
"""Validate the proposed noncanon frame-to-formation integration layer."""

from __future__ import annotations

import copy
import csv
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MECHA_INDEX = (
    ROOT
    / "docs"
    / "06_hardware"
    / "data"
    / "maneuver-frame-lineup-proposed-index-v1.csv"
)
MILITARY_DATA = ROOT / "docs" / "07_military" / "data"
DEPLOYMENT_FILE = MILITARY_DATA / "maneuver-frame-deployment-profile-proposed-v1.csv"
ADOPTION_FILE = MILITARY_DATA / "formation-frame-adoption-proposed-v1.csv"
CORE_FILE = MILITARY_DATA / "named-frame-core-proposed-index-v1.csv"

# Direction C, author decision D-20260813-03. Kept as a name rather than a
# literal so the next portfolio decision changes one line, not five.
PORTFOLIO_ROWS = 46
REGISTRY_FILE = (
    ROOT
    / "docs"
    / "07_military"
    / "front-stage-formation-registry-and-loss-accounting-v1.md"
)
ACCOUNTING_FILE = (
    ROOT / "docs" / "07_military" / "formation-accounting-clarifications-v1.md"
)
DEFERRED_FILE = ROOT / "docs" / "00_project" / "deferred-design-register-v2.md"
COMPLETION_FILE = (
    ROOT / "docs" / "00_project" / "detail-completion-status-2026-08-03.md"
)

FORMATION_PATTERN = re.compile(
    r"^\| ((?:IMP|HEL|IND|NEU|JNT)-[A-Z0-9-]+) \|", re.MULTILINE
)
DERIVED_IDS = {
    "JNT-ARD-03",
    "JNT-RTE-04",
    "JNT-FLT-05",
    "JNT-ORP-06",
    "JNT-REC-07",
    "JNT-TRN-08",
}
ADJACENT_IDS = {"JNT-K13-01", "JNT-HALL-02"}
EXPECTED_ROW_CLASS_COUNTS = {
    "SOURCE_FORMATION": 30,
    "DERIVED_MISSION_FORMATION": 6,
    "ADJACENT_MISSION_IDENTITY": 2,
}
EXPECTED_INVENTORY_COUNTS = {
    "AUTHOR_HOLD": 2,
    "CANON_EXISTING": 1,
    "PROPOSED_SLOT": 43,
}
EXPECTED_MANUFACTURING_COUNTS = {
    "HIGH_VOLUME_SERIES": 8,
    "LIMITED_RUN": 10,
    "LOW_VOLUME_SERIES": 25,
    "SINGLE_HULL": 1,
    "UNASSIGNED": 2,
}
EXPECTED_MISSION_ROLE_COUNTS = {
    "LINE_COMBAT": 14,
    "PROTAGONIST_MISSION": 1,
    "SERVICE_INDUSTRIAL": 12,
    "SPECIALIST": 17,
    "UNASSIGNED": 2,
}
EXPECTED_STORY_STATUS_COUNTS = {
    "HOLD_NO_HULL_STATUS": 2,
    "HULL_INSTANCE_LEDGER_ONLY": 44,
}

ALLOWED_SOLO_EFFECTS = {
    "ONE_LOCAL_POSITION_CAPTURE_OR_RESCUE_WINDOW",
    "NONE_LINE_UNIT",
    "LOCAL_RESCUE_ACCESS_ONLY",
    "LOCAL_REPAIR_ACCESS_ONLY",
    "ONE_LOCAL_COMMAND_HANDOFF_WINDOW",
    "BREACH_INSIDE_EXISTING_CAPTURE_WINDOW",
    "ONE_LOCAL_SENSOR_OR_CLASSIFICATION_WINDOW",
    "ONE_LOCAL_INTERCEPT_OR_DELAY",
    "LOCAL_RECOVERY_ACCESS_ONLY",
    "ONE_LOCAL_QUARANTINE_OR_EVIDENCE_WINDOW",
    "ONE_LOCAL_INTERDICTION_WINDOW",
    "LOCAL_WORK_ACCESS_ONLY",
    "ONE_LOCAL_ANCHOR_OR_BREACH_WINDOW",
    "LOCAL_RELAY_ACCESS_ONLY",
    "ONE_LOCAL_RESCUE_CORRIDOR",
    "LOCAL_MEDICAL_TRANSFER_ONLY",
    "ONE_LOCAL_ESCORT_OR_DELAY_WINDOW",
    "ONE_LOCAL_ANCHOR_OR_EXTRACTION_WINDOW",
    "ONE_LOCAL_AMBUSH_OR_DELAY_WINDOW",
    "LOCAL_SALVAGE_ACCESS_ONLY",
    "ONE_LOCAL_CUSTODY_OR_SEIZURE_WINDOW",
    "ONE_LOCAL_MAPPING_OR_ACCESS_WINDOW",
    "ONE_LOCAL_ISOLATION_OR_INTERFACE_WINDOW",
}

SUPPORT_TOKENS = {
    "CRADLE", "STANDARD_CRADLE", "SERVICE_CRADLE", "FLEET_CRADLE",
    "COMMAND_LINK", "HEAVY_CRADLE", "COOLING_TENDER", "SENSOR_NETWORK",
    "SECURE_CRADLE", "CERTIFIED_CRADLE", "HIGH_LICENSE_SERVICE",
    "WORK_CRADLE", "LOCAL_CRADLE", "ANCHOR_RIG", "RESCUE_CRADLE",
    "MEDICAL_CRADLE", "MODIFIED_CRADLE", "FRONTIER_CRADLE", "HEAVY_TOW",
    "MAINTAINERS", "COOLING", "COOLANT", "RECOVERY", "TOW", "MEDICAL",
    "SPARES", "SUPPLY", "ESCORT", "PARTS", "DATA_CUSTODY", "TOOLS",
    "AMMUNITION", "ENGINEERS", "RELAY_PARTS", "LIFE_SUPPORT",
    "INSPECTION", "AUTHORITY", "PROVENANCE_TEAM",
}

EXPECTED_CORE_SUPPORT = {
    "C01": "GA1_ACADEMY|GA2_EXTERNAL_CONTRACT_OR_FIXED_BASE|GA3_JNT_ARD_DECLARED_SOURCE_DETACHMENTS",
    "C02": "IND_VRK_SOURCE_CARRIER_BASE_AND_TOW",
    "C03": "HEL_CERT_SOURCE_CARRIER_SERVICE_AND_RECOVERY",
    "C04": "JNT_ARD_LOCAL_BASE_PLUS_SOURCE_DETACHMENTS",
    "C05": "IMP_CG_SOURCE_CARRIER_SECURE_YARD_AND_RECOVERY",
    "C06": "DECLARED_SOURCE_CARRIERS_TENDERS_MAINTENANCE_AND_RECOVERY",
    "C07": "NEU_MED_SOURCE_THEN_JNT_ORP_DECLARED_MEDICAL_CARRIER_AND_RECOVERY",
    "C08": "JNT_REC_DECLARED_SOURCE_CARRIERS_CUSTODY_TEAMS_AND_RECOVERY",
}
EXPECTED_CORE_COMPLETION = {
    "C01": "LOCAL_WINDOW_THEN_FLIGHT_LOCAL_TEAMS_AND_RECOVERY_COMPLETE",
    "C02": "LOCAL_EXTRACTION_WINDOW_THEN_ROUTE_FORMATION_COMPLETES",
    "C03": "LOCAL_CLASSIFICATION_WINDOW_THEN_EVIDENCE_AND_RECOVERY_COMPLETE",
    "C04": "FORMATION_OPENS_WINDOW_LOCAL_TEAMS_AND_RECOVERY_COMPLETE",
    "C05": "ONE_INTERCEPT_OR_COMMAND_WINDOW_THEN_PARENT_SQUADRON_COMPLETES",
    "C06": "ONE_DECISION_WINDOW_THEN_DELEGATED_FRONTS_AND_SUPPORT_COMPLETE",
    "C07": "CORRIDOR_WINDOW_THEN_CLINICAL_RESCUE_AND_PASSAGE_COMPLETE",
    "C08": "LOCAL_INTERFACE_WINDOW_THEN_WITNESS_CUSTODY_AND_RECOVERY_COMPLETE",
}
EXPECTED_CORE_ROLE_PAIRING = {
    "C01": "ACE_WING|SERVICE_RESCUE|SENSOR_CAPTURE|ROTATING_SPECIALIST",
    "C02": "ACE_WING|AMBUSH_EXTRACTION|SALVAGE_RECOVERY",
    "C03": "COMMAND_LINE|QUARANTINE_INTERDICTION|SERVICE_RECOVERY",
    "C04": "DEFENSE_WORK|ANCHOR_BREACH|RELAY_RECOVERY|ROTATING_SOURCE_PAIR",
    "C05": "COMMAND_LINE|INTERCEPT_SCREEN|RECON|HEAVY_BREACH",
    "C06": "ACE_WING|COMMAND_SENSOR|CAPTURE_RESCUE|SOURCE_ROTATION",
    "C07": "ESCORT_RESCUE|MEDICAL_TRANSFER|CORRIDOR_CONTROL|RECOVERY",
    "C08": "SECURITY_LOCAL|INTERFACE_EVIDENCE|RESCUE|ROTATING_WITNESS_PAIR",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def duplicates(values: list[str]) -> set[str]:
    counts = Counter(values)
    return {value for value, count in counts.items() if count > 1}


def registry_ids() -> list[str]:
    if not REGISTRY_FILE.exists():
        raise FileNotFoundError(REGISTRY_FILE)
    return FORMATION_PATTERN.findall(REGISTRY_FILE.read_text(encoding="utf-8-sig"))


def validate_control_text() -> list[str]:
    errors: list[str] = []
    required = {
        REGISTRY_FILE: "stable IDs for 36 front-stage formations/institutions",
        DEFERRED_FILE: "36 front-stage formation/institution IDs",
        COMPLETION_FILE: "36 front-stage formation/institution IDs",
    }
    for path, phrase in required.items():
        if not path.exists():
            errors.append(f"missing count-control document {path.relative_to(ROOT)}")
            continue
        if phrase not in path.read_text(encoding="utf-8-sig"):
            errors.append(
                f"count-control phrase missing from {path.relative_to(ROOT)}: {phrase}"
            )
    return errors


def validate(
    mecha_rows: list[dict[str, str]],
    deployment_rows: list[dict[str, str]],
    adoption_rows: list[dict[str, str]],
    core_rows: list[dict[str, str]],
    formation_ids: list[str],
    *,
    check_control_text: bool,
) -> list[str]:
    errors: list[str] = []

    if len(formation_ids) != 38 or len(set(formation_ids)) != 38:
        errors.append(
            f"registry must contain 38 unique identity rows, found {len(formation_ids)}"
        )
    if check_control_text:
        errors.extend(validate_control_text())

    if len(adoption_rows) != 38:
        errors.append(f"expected 38 adoption rows, found {len(adoption_rows)}")
    duplicate_adoption = duplicates([row["formation_id"] for row in adoption_rows])
    if duplicate_adoption:
        errors.append(f"duplicate adoption formation_id: {sorted(duplicate_adoption)}")
    adoption_ids = [row["formation_id"] for row in adoption_rows]
    if set(adoption_ids) != set(formation_ids):
        errors.append("adoption coverage must match all 38 registry identity rows")

    row_class_counts = Counter(row["row_class"] for row in adoption_rows)
    if row_class_counts != Counter(EXPECTED_ROW_CLASS_COUNTS):
        errors.append(f"row-class counts mismatch: {dict(row_class_counts)}")

    for row in adoption_rows:
        formation_id = row["formation_id"]
        expected_class = (
            "DERIVED_MISSION_FORMATION"
            if formation_id in DERIVED_IDS
            else "ADJACENT_MISSION_IDENTITY"
            if formation_id in ADJACENT_IDS
            else "SOURCE_FORMATION"
        )
        if row["row_class"] != expected_class:
            errors.append(
                f"{formation_id}: expected row_class {expected_class}, found {row['row_class']}"
            )
        if expected_class == "SOURCE_FORMATION":
            expected_inventory = "GLOBAL_HOLDINGS_SOURCE"
        elif expected_class == "DERIVED_MISSION_FORMATION":
            expected_inventory = "SOURCE_DETACHMENT_REQUIRED"
        else:
            expected_inventory = "NOT_FULL_FORMATION_NOT_ADDITIVE"
        if row["inventory_rule"] != expected_inventory:
            errors.append(
                f"{formation_id}: invalid inventory rule for {expected_class}"
            )
        if not row["adoption_profile"]:
            errors.append(f"{formation_id}: adoption profile is required")
        if "L08" in row["adoption_profile"]:
            errors.append(f"{formation_id}: L08 reserve cannot be assigned")
        if row["canon_status"] != "PROPOSED_NONCANON_MAPPING":
            errors.append(f"{formation_id}: adoption mapping must remain noncanon")

    if len(mecha_rows) != PORTFOLIO_ROWS:
        errors.append(f"expected {PORTFOLIO_ROWS} mecha index rows, found {len(mecha_rows)}")
    if len(deployment_rows) != PORTFOLIO_ROWS:
        errors.append(f"expected {PORTFOLIO_ROWS} deployment rows, found {len(deployment_rows)}")
    duplicate_deployment = duplicates([row["slot_id"] for row in deployment_rows])
    if duplicate_deployment:
        errors.append(f"duplicate deployment slot_id: {sorted(duplicate_deployment)}")
    mecha_slots = [row["slot_id"] for row in mecha_rows]
    deployment_slots = [row["slot_id"] for row in deployment_rows]
    if set(deployment_slots) != set(mecha_slots):
        errors.append(f"deployment coverage must match all {PORTFOLIO_ROWS} mecha slots")

    inventory_counts = Counter(row["inventory_state"] for row in deployment_rows)
    if inventory_counts != Counter(EXPECTED_INVENTORY_COUNTS):
        errors.append(f"inventory-state counts mismatch: {dict(inventory_counts)}")
    manufacturing_counts = Counter(
        row["manufacturing_scale"] for row in deployment_rows
    )
    if manufacturing_counts != Counter(EXPECTED_MANUFACTURING_COUNTS):
        errors.append(
            f"manufacturing-scale counts mismatch: {dict(manufacturing_counts)}"
        )
    mission_role_counts = Counter(
        row["mission_role_class"] for row in deployment_rows
    )
    if mission_role_counts != Counter(EXPECTED_MISSION_ROLE_COUNTS):
        errors.append(f"mission-role counts mismatch: {dict(mission_role_counts)}")
    story_status_counts = Counter(
        row["story_status_policy"] for row in deployment_rows
    )
    if story_status_counts != Counter(EXPECTED_STORY_STATUS_COUNTS):
        errors.append(f"story-status counts mismatch: {dict(story_status_counts)}")

    deployment_by_slot = {row["slot_id"]: row for row in deployment_rows}
    for slot in mecha_slots:
        row = deployment_by_slot.get(slot)
        if row is None:
            continue
        reserve = slot in {"M-027", "M-028"}
        if reserve:
            if (
                row["inventory_state"] != "AUTHOR_HOLD"
                or row["manufacturing_scale"] != "UNASSIGNED"
                or row["mission_role_class"] != "UNASSIGNED"
                or row["story_status_policy"] != "HOLD_NO_HULL_STATUS"
            ):
                errors.append(f"{slot}: reserve axes must remain unassigned author HOLD")
            if row["formal_layer"] != "HOLD" or row["normal_assignment"] != "NO_ASSIGNMENT":
                errors.append(f"{slot}: reserve cannot have a formation assignment")
            if row["named_core_eligibility"] != "NO":
                errors.append(f"{slot}: reserve cannot enter a named core")
            if row["solo_limit"] != "NO_COMBAT_CLAIM_HOLD":
                errors.append(f"{slot}: reserve cannot receive a combat claim")
            if any(row[field] != "HOLD" for field in ("allowed_solo_effect", "completion_actor", "support_gate")):
                errors.append(f"{slot}: reserve combat/support fields must remain HOLD")
            if row["canon_status"] != "HOLD_AUTHOR_DECISION":
                errors.append(f"{slot}: reserve mapping must remain author HOLD")
        else:
            if row["inventory_state"] not in {"CANON_EXISTING", "PROPOSED_SLOT"}:
                errors.append(f"{slot}: placed inventory state is invalid")
            if row["manufacturing_scale"] == "UNASSIGNED":
                errors.append(f"{slot}: placed manufacturing scale is required")
            if row["mission_role_class"] == "UNASSIGNED":
                errors.append(f"{slot}: placed mission role is required")
            if row["story_status_policy"] != "HULL_INSTANCE_LEDGER_ONLY":
                errors.append(f"{slot}: ace/legend status must remain in the hull ledger")
            if row["solo_limit"] != "NO_HEALTHY_SQUADRON_ANNIHILATION":
                errors.append(f"{slot}: solo-annihilation prohibition is required")
            for field in (
                "formal_layer",
                "normal_assignment",
                "allowed_solo_effect",
                "completion_actor",
                "support_gate",
            ):
                if not row[field] or row[field] == "HOLD":
                    errors.append(f"{slot}: placed deployment requires {field}")
            if row["allowed_solo_effect"] not in ALLOWED_SOLO_EFFECTS:
                errors.append(f"{slot}: invalid solo effect outside the bounded whitelist")
            support_parts = set(row["support_gate"].split("|"))
            if not support_parts or not support_parts <= SUPPORT_TOKENS:
                errors.append(f"{slot}: support gate contains unrecognized or decorative terms")
            collective_terms = (
                "FLIGHT", "SQUADRON", "TEAM", "CREW", "SUPPORT", "RECOVERY",
                "BASE", "FORMATION", "CHAIN", "ENGINEERS", "INTERPRETERS",
            )
            if not any(term in row["completion_actor"] for term in collective_terms):
                errors.append(f"{slot}: completion actor must name a collective/support layer")
            if row["canon_status"] != "PROPOSED_NONCANON_MAPPING":
                errors.append(f"{slot}: deployment mapping must remain noncanon")

    if len(core_rows) != 8:
        errors.append(f"expected 8 named-core candidates, found {len(core_rows)}")
    expected_core_ids = [f"C{number:02d}" for number in range(1, 9)]
    actual_core_ids = [row["core_id"] for row in core_rows]
    if actual_core_ids != expected_core_ids:
        errors.append("core ids must be ordered C01 through C08")
    duplicate_cores = duplicates(actual_core_ids)
    if duplicate_cores:
        errors.append(f"duplicate core_id: {sorted(duplicate_cores)}")

    formation_set = set(formation_ids)
    for row in core_rows:
        core_id = row["core_id"]
        parents = row["parent_identity_path"].split(">")
        unknown_parents = sorted(set(parents) - formation_set)
        if unknown_parents:
            errors.append(f"{core_id}: unknown parent identity {unknown_parents}")
        if "FLIGHT" not in row["formal_layer"]:
            errors.append(f"{core_id}: core must remain flight-strength")
        if row["inventory_rule"] not in {
            "SUBSET_NOT_ADDITIVE",
            "SUBSET_NOT_ADDITIVE_SOURCE_DEDUCTION_REQUIRED",
        }:
            errors.append(f"{core_id}: core must remain a non-additive subset")
        if any(parent in DERIVED_IDS for parent in parents) and "SOURCE_DEDUCTION_REQUIRED" not in row["inventory_rule"]:
            errors.append(f"{core_id}: derived parent requires source deduction")
        if core_id == "C01":
            if not any(parent not in ADJACENT_IDS for parent in parents):
                errors.append("C01: mature core requires a real operational parent formation")
            if "JNT-ARD-03" not in parents:
                errors.append("C01: GA3 test parent must remain JNT-ARD-03 unless re-approved")
            if "GA2_1_TO_3" not in row["core_size_policy"]:
                errors.append("C01: GA2 must remain limited to 1-3 mission assets")
            if "EXTERNAL_CONTRACT_OR_FIXED_BASE" not in row["support_source"]:
                errors.append("C01: GA2 support must remain external or fixed-base")
        elif row["core_size_policy"] != "6_TO_8":
            errors.append(f"{core_id}: mature core size must remain 6-8")
        if "M027" in row["chassis_reference_policy"].replace("-", "") or "M028" in row["chassis_reference_policy"].replace("-", ""):
            errors.append(f"{core_id}: HOLD reserve cannot be assigned")
        for field in ("role_pairing", "support_source", "completion_rule"):
            if not row[field] or row[field] == "HOLD":
                errors.append(f"{core_id}: core requires {field}")
        if row["support_source"] != EXPECTED_CORE_SUPPORT.get(core_id):
            errors.append(f"{core_id}: support source drifted from the audited proposal")
        if row["completion_rule"] != EXPECTED_CORE_COMPLETION.get(core_id):
            errors.append(f"{core_id}: completion rule drifted from the audited proposal")
        if row["role_pairing"] != EXPECTED_CORE_ROLE_PAIRING.get(core_id):
            errors.append(f"{core_id}: role pairing drifted from the audited proposal")
        if not row["public_identity_state"].startswith("HOLD_PUBLIC_NAME"):
            errors.append(f"{core_id}: public name must remain HOLD")
        if row["canon_status"] != "PROPOSED_NONCANON":
            errors.append(f"{core_id}: core must remain noncanon")

    for core_id in expected_core_ids:
        if not any(row["named_core_candidate"].startswith(core_id) for row in adoption_rows):
            errors.append(f"{core_id}: no adoption row references this core")

    return errors


def run_selftest(
    mecha_rows: list[dict[str, str]],
    deployment_rows: list[dict[str, str]],
    adoption_rows: list[dict[str, str]],
    core_rows: list[dict[str, str]],
    formation_ids: list[str],
) -> int:
    base_errors = validate(
        mecha_rows,
        deployment_rows,
        adoption_rows,
        core_rows,
        formation_ids,
        check_control_text=False,
    )
    if base_errors:
        print("FRAME FORMATION SELFTEST BLOCKED BY INVALID BASE", file=sys.stderr)
        for error in base_errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    fixtures: list[tuple[str, list[dict[str, str]], list[dict[str, str]], list[dict[str, str]], str]] = []

    def add_fixture(name: str, mutate, expected: str) -> None:
        deployment = copy.deepcopy(deployment_rows)
        adoption = copy.deepcopy(adoption_rows)
        cores = copy.deepcopy(core_rows)
        mutate(deployment, adoption, cores)
        fixtures.append((name, deployment, adoption, cores, expected))

    add_fixture("missing adoption", lambda _, a, __: a.pop(), "expected 38 adoption rows")
    add_fixture("wrong row class", lambda _, a, __: a[0].update(row_class="DERIVED_MISSION_FORMATION"), "expected row_class")
    add_fixture("derived owns inventory", lambda _, a, __: a[32].update(inventory_rule="GLOBAL_HOLDINGS_SOURCE"), "invalid inventory rule")
    add_fixture("missing profile", lambda _, a, __: a[0].update(adoption_profile=""), "adoption profile is required")
    add_fixture("missing deployment", lambda d, _, __: d.pop(), "deployment rows")
    add_fixture("reserve assigned", lambda d, _, __: d[26].update(normal_assignment="HERO_CORE"), "reserve cannot have a formation assignment")
    add_fixture("solo annihilation", lambda d, _, __: d[0].update(solo_limit="ALLOW_HEALTHY_SQUADRON_ANNIHILATION"), "solo-annihilation prohibition")
    add_fixture(
        "eleven of twelve mission kill",
        lambda d, _, __: d[0].update(allowed_solo_effect="MISSION_KILL_11_OF_12_FRAMES"),
        "invalid solo effect",
    )
    add_fixture(
        "decorative support",
        lambda d, _, __: d[0].update(support_gate="DECORATIVE"),
        "unrecognized or decorative",
    )
    add_fixture("duplicate core", lambda _, __, c: c[1].update(core_id="C01"), "core ids must be ordered")
    add_fixture("oversized core", lambda _, __, c: c[1].update(core_size_policy="9_TO_12"), "mature core size must remain 6-8")
    add_fixture("additive core", lambda _, __, c: c[1].update(inventory_rule="NEW_INVENTORY"), "non-additive subset")
    add_fixture(
        "hidden additive core",
        lambda _, __, c: c[1].update(inventory_rule="SUBSET_NOT_ADDITIVE_PLUS_SIX_NEW_HULLS"),
        "non-additive subset",
    )
    add_fixture("unknown parent", lambda _, __, c: c[1].update(parent_identity_path="JNT-FAKE-99"), "unknown parent identity")
    add_fixture("GA2 permanent core", lambda _, __, c: c[0].update(core_size_policy="GA1_1|GA2_6_TO_8|GA3_6_TO_8"), "GA2 must remain limited")
    add_fixture(
        "C01 missing operational parent",
        lambda _, __, c: c[0].update(parent_identity_path="JNT-K13-01>JNT-HALL-02"),
        "real operational parent formation",
    )
    add_fixture("no support bypass", lambda _, __, c: c[1].update(support_source="NO_SUPPORT"), "support source drifted")
    add_fixture("hero solo completion", lambda _, __, c: c[1].update(completion_rule="HERO_SOLO"), "completion rule drifted")
    add_fixture("crewless solo completion", lambda _, __, c: c[2].update(completion_rule="CREWLESS_SOLO_HERO"), "completion rule drifted")
    add_fixture("solo army pairing", lambda _, __, c: c[3].update(role_pairing="SOLO_HERO_ARMY"), "role pairing drifted")
    add_fixture("missing support", lambda _, __, c: c[1].update(support_source=""), "core requires support_source")
    add_fixture("reserve in core", lambda _, __, c: c[1].update(chassis_reference_policy="M027_HULL_INSTANCE"), "HOLD reserve cannot be assigned")
    add_fixture("public name promoted", lambda _, __, c: c[1].update(public_identity_state="APPROVED_PUBLIC_NAME"), "public name must remain HOLD")

    failures: list[str] = []
    for name, deployment, adoption, cores, expected in fixtures:
        fixture_errors = validate(
            mecha_rows,
            deployment,
            adoption,
            cores,
            formation_ids,
            check_control_text=False,
        )
        if not any(expected in error for error in fixture_errors):
            failures.append(f"{name}: expected error containing {expected!r}")

    if failures:
        print("FRAME FORMATION SELFTEST FAILED", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("FRAME FORMATION SELFTEST PASSED")
    print(f"- defect fixtures fired: {len(fixtures)}")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) > 1 or (argv and argv[0] != "--selftest"):
        print("usage: validate_frame_formation_integration.py [--selftest]", file=sys.stderr)
        return 2

    try:
        mecha_rows = read_csv(MECHA_INDEX)
        deployment_rows = read_csv(DEPLOYMENT_FILE)
        adoption_rows = read_csv(ADOPTION_FILE)
        core_rows = read_csv(CORE_FILE)
        formation_ids = registry_ids()
    except FileNotFoundError as exc:
        print(f"missing frame-formation input: {exc}", file=sys.stderr)
        return 1

    if argv == ["--selftest"]:
        return run_selftest(
            mecha_rows, deployment_rows, adoption_rows, core_rows, formation_ids
        )

    errors = validate(
        mecha_rows,
        deployment_rows,
        adoption_rows,
        core_rows,
        formation_ids,
        check_control_text=True,
    )
    if errors:
        print("FRAME FORMATION VALIDATION FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("FRAME FORMATION VALIDATION PASSED")
    print("- registered identities: 38; proposed adoption mapping 30 + 6 + 2")
    print("- working-canon summaries still state 36; the 36/38 discrepancy remains HOLD")
    print("- deployment samples: 46 = 44 placed + 2 author HOLD; not a portfolio target")
    print("- manufacturing scale and mission role are validated as separate axes")
    print("- named core candidates: 8, all non-additive flight-strength subsets")
    print("- GA2 protagonist capacity: 1-3 mission assets, external/fixed-base support")
    print("- healthy-squadron solo-annihilation claims: none")
    print("- AXIOM and successor assignments: HOLD")
    print("- canon promotions: none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
