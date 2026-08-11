#!/usr/bin/env python3
"""Validate the noncanon role-demand and reuse-first portfolio proposal."""

from __future__ import annotations

import copy
import csv
import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COLLECTION_DATA = ROOT / "docs" / "09_collection" / "data"
ROLE_FILE = COLLECTION_DATA / "cast-role-asset-demand-proposed-v1.csv"
CENSUS_FILE = COLLECTION_DATA / "cast-semantic-census-summary-proposed-v1.csv"
CENSUS_ROWS_FILE = COLLECTION_DATA / "cast-role-tier-census-resolved-v1.csv"
CATEGORY_FILE = COLLECTION_DATA / "role-demand-category-bands-proposed-v1.csv"
DIRECTION_FILE = ROOT / "docs" / "06_hardware" / "data" / "maneuver-frame-portfolio-directions-proposed-v1.csv"
CROSSWALK_FILE = ROOT / "docs" / "06_hardware" / "data" / "maneuver-frame-role-demand-crosswalk-proposed-v1.csv"
MECHA_INDEX_FILE = ROOT / "docs" / "06_hardware" / "data" / "maneuver-frame-lineup-proposed-index-v1.csv"
AUDIT_FILE = ROOT / "docs" / "09_collection" / "role-demand-portfolio-count-audit-v1.md"
MECHA_ARCHITECTURE = ROOT / "docs" / "06_hardware" / "maneuver-frame-lineup-master-architecture-v1.md"

EXPECTED_ROLE_TIERS = [
    "PROTAGONIST",
    "CORE_ALLY",
    "CORE_ANTAGONIST_RIVAL",
    "RECURRING_SUPPORT",
    "IMPORTANT_EXTRA",
    "BACKGROUND_ROLE_GROUP",
]
EXPECTED_DOMAINS = [f"C{number}" for number in range(1, 9)]
EXPECTED_SOURCE_ROWS = {
    "C1": 155,
    "C2": 11,
    "C3": 16,
    "C4": 30,
    "C5": 28,
    "C6": 42,
    "C7": 112,
    "C8": 21,
}
EXPECTED_DIRECTIONS = ["A", "B", "C", "D"]
EXPECTED_DIRECTION_BANDS = {
    "A": ("26_TO_32", "18_TO_26", "32_TO_50", "65_TO_105"),
    "B": ("32_TO_40", "22_TO_30", "32_TO_50", "70_TO_110"),
    "C": ("40_TO_48", "26_TO_36", "36_TO_54", "80_TO_125"),
    "D": ("44_TO_58", "28_TO_40", "40_TO_58", "90_TO_140"),
}
EXPECTED_CATEGORY_BANDS = {
    "C1": ("170_TO_200_SERIES_CAST_ESTIMATE", "35_TO_60_BACKGROUND_ROLE_GROUPS", "RELATIONSHIP_POSITION_AND_EXIT_STATES_SEPARATE", "197_PERSONS_1_4_9_40_143_BY_TIER"),
    "C2": ("22_TO_30_READER_NAMED_MODELS", "8_TO_14_SHARED_SERVICE_MODEL_FAMILIES", "70_TO_110_REFIT_DAMAGE_MISSION_STATES", "32_TO_40_CANDIDATES_UNDER_DIRECTION_B_PENDING_CHASSIS_PROOF"),
    "C3": ("40_TO_64_NAMED_ANCHORS", "28_TO_42_STANDARD_EQUIPMENT_TYPES", "80_TO_120_AMMO_REFIT_OPERATION_LOSS_STATES", "HOLD_ROLE_ASSET_CROSSWALK"),
    "C4": ("24_TO_32_FRONT_ANCHORS", "12_TO_18_BACKGROUND_LEGACY_RECORD_LINES", "36_TO_54_DAMAGE_FORGERY_RESTORATION_CUSTODY_STATES", "HOLD_ROLE_ASSET_CROSSWALK"),
    "C5": ("32_TO_48_NAMED_HULLS", "18_TO_26_CLASS_FUNCTION_FAMILIES", "45_TO_75_REFIT_DAMAGE_DEDICATION_LOSS_STATES", "HOLD_ROLE_ASSET_CROSSWALK"),
    "C6": ("28_TO_40_FRONT_TECH_LINEAGES", "20_TO_32_BACKGROUND_TECH_GROUPS", "90_TO_140_VERSION_CERTIFICATION_PROCESS_STATES", "HOLD_ROLE_ASSET_CROSSWALK"),
    "C7": ("10_TO_12_CORE_ECOSYSTEMS|5_TO_8_ACTIVE_PER_ARC", "68_TO_82_PERSISTENT_ORGANIZATIONS", "10_TO_16_TEMPORARY_COALITIONS|32_TO_44_INTERNAL_FACTIONS", "HOLD_SEMANTIC_MERGE"),
    "C8": ("36_TO_44_FRONT_PLACE_LINEAGES", "12_TO_18_ROUTE_CORRIDORS|48_CLUSTERS_BACKGROUND", "80_TO_130_DAMAGE_OCCUPATION_RECOVERY_TRANSITION_STATES", "HOLD_ROLE_ASSET_CROSSWALK"),
}
EXPECTED_REUSE_CANDIDATES = {
    "FD-027": "M-001",
    "FD-028": "M-001",
    "FD-029": "M-014",
    "FD-030": "M-014",
    "FD-031": "M-005|M-009",
    "FD-032": "M-018",
    "FD-033": "M-006",
    "FD-035": "M-005",
    "FD-036": "M-011|M-017|M-023",
    "FD-037": "M-006|M-017",
    "FD-038": "M-005",
    "FD-039": "M-017",
    "FD-040": "M-018|M-020",
    "FD-041": "M-005",
    "FD-042": "M-020",
    "FD-043": "M-019",
    "FD-044": "M-020",
    "FD-045": "M-022",
    "FD-046": "M-017",
    "FD-047": "M-020",
    "FD-048": "M-020|M-024",
    "FD-049": "M-026",
    "FD-050": "M-024",
    "FD-051": "M-015|M-022",
    "FD-052": "M-002|M-003|M-004",
}
EXPECTED_REUSE_EVIDENCE_SHA256 = "ce40e71e2e6d3e2b81cd59595f86d3ae5263326314f2efc1335bb7770561c66c"
EXPECTED_REUSE_SEMANTIC_SHA256 = "1c0e2fb172eb24996f5282864097c0ba8f4a76f38a084409ecb6fa0ef5e8c8c7"
EXPECTED_ROLE_SEMANTIC_SHA256 = "8ab8a3ae8be63b88778dc019f7be46ae2a8e074c25c4fc7e69f9fc536e66b8fd"
EXPECTED_CENSUS_SEMANTIC_SHA256 = "fdff69c0bb14673f47903c301ac7e9cbfe188e318ba342e570efa591fc8eacc7"
EXPECTED_CROSSWALK_SEMANTIC_SHA256 = "e6fb2e2980b1b0ba13665ef0f5d9e79a1a105bd2402433a61986361dc0201cf6"
EXPECTED_DIRECTION_STATES = {
    "A": "ALTERNATIVE_RETAINED_AS_REUSE_METHOD",
    "B": "SELECTED_AUTHOR_DECISION_D_20260812_01_POST_CENSUS",
    "C": "ALTERNATIVE",
    "D": "ALTERNATIVE_HOLD",
}
EXPECTED_CENSUS_ROW_FIELDS = (
    "identity_key",
    "korean_name",
    "record_type",
    "final_tier",
    "faction_or_org",
    "tier_evidence",
    "source_docs",
    "alias_merge_hints",
)
EXPECTED_CENSUS_RECORD_TYPES = {
    "PERSON": 197,
    "OFFICE": 41,
    "GROUP": 73,
    "AI": 8,
    "EMBODIMENT": 3,
}
EXPECTED_CENSUS_PERSON_TIERS = {
    "PROTAGONIST": 1,
    "CORE_ALLY": 4,
    "CORE_ANTAGONIST_RIVAL": 9,
    "RECURRING_SUPPORT": 40,
    "IMPORTANT_EXTRA": 143,
}
ALLOWED_MAJOR_SYSTEMS = {
    "LOAD_FRAME",
    "POWER",
    "HEAT",
    "PROPULSION",
    "CONTROL",
    "COCKPIT_INTERFACE",
    "ARMOR_SUPPORT",
    "WEAPON_SUPPORT",
    "EXISTING_CANON_SYSTEMS",
}
EXPECTED_SIGNATURE_POLICY = {
    "PROTAGONIST": "1_REQUIRED",
    "CORE_ALLY": "0_TO_2",
    "CORE_ANTAGONIST_RIVAL": "8_TO_12",
    "RECURRING_SUPPORT": "5_TO_10",
    "IMPORTANT_EXTRA": "4_TO_9",
    "BACKGROUND_ROLE_GROUP": "NONE",
}
ALLOWED_CROSSWALK_ROLES = {
    "PROTAGONIST",
    "CORE_ALLY",
    "CORE_ANTAGONIST_RIVAL",
    "RECURRING_SUPPORT",
    "IMPORTANT_EXTRA",
    "FACTION_SHARED",
}
ALLOWED_MODEL_MANUFACTURING = {
    "SINGLE_HULL",
    "HIGH_VOLUME_SERIES",
    "LIMITED_RUN",
    "LOW_VOLUME_SERIES",
}
FORBIDDEN_CLAIMS = (
    "CANON_LEGEND",
    "AUTO_CANON",
    "ALL_LEGEND",
    "PERSONAL_FRAME_FOR_EVERYONE",
    "NO_SUPPORT",
    "HERO_SOLO",
    "CREWLESS_SOLO_HERO",
    "SOLO_HERO_ARMY",
)


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def check_resolved_census(census_rows: list[dict[str, str]]) -> list[str]:
    """Once the summary claims a resolved census, the row-level file must back it."""
    errors: list[str] = []
    if not CENSUS_ROWS_FILE.is_file():
        return ["resolved census claimed without the row-level cast-role-tier census file"]
    rows = read_csv(CENSUS_ROWS_FILE)
    missing_fields = set(EXPECTED_CENSUS_ROW_FIELDS) - set(rows[0] if rows else {})
    if missing_fields:
        return [f"cast-role-tier census is missing fields: {sorted(missing_fields)}"]

    keys = [row["identity_key"].strip() for row in rows]
    if len(set(keys)) != len(keys):
        errors.append("cast-role-tier census identity keys must be unique")
    if any(not key for key in keys):
        errors.append("cast-role-tier census rows require an identity key")

    types: dict[str, int] = {}
    tiers: dict[str, int] = {}
    for row in rows:
        record_type = row["record_type"].strip()
        types[record_type] = types.get(record_type, 0) + 1
        if not row["final_tier"].strip():
            errors.append(f"{row['identity_key']}: census row has no tier")
        if record_type == "PERSON":
            tiers[row["final_tier"].strip()] = tiers.get(row["final_tier"].strip(), 0) + 1
        if not row["source_docs"].strip():
            errors.append(f"{row['identity_key']}: census row has no source document")
        if not row["korean_name"].strip() and record_type == "PERSON":
            hint = row["alias_merge_hints"]
            if "표기 미확정" not in hint and "미명명" not in hint:
                errors.append(
                    f"{row['identity_key']}: a person without a canon Korean name must be marked 표기 미확정"
                )

    if types != EXPECTED_CENSUS_RECORD_TYPES:
        errors.append(f"cast-role-tier census record-type mix drifted: {types}")
    if tiers != EXPECTED_CENSUS_PERSON_TIERS:
        errors.append(f"cast-role-tier census person tier mix drifted: {tiers}")

    summary = {row["scope"]: row for row in census_rows}
    resolved = summary.get("REPOSITORY_WIDE_RESOLVED")
    if resolved is None:
        errors.append("resolved census requires a REPOSITORY_WIDE_RESOLVED summary scope")
    else:
        person_total = sum(EXPECTED_CENSUS_PERSON_TIERS.values())
        if f"{person_total}_PERSONS" not in resolved["deduplicated_identity_result"]:
            errors.append("resolved summary person count disagrees with the row-level census")
        if f"{len(rows)}_CENSUS_ROWS" != resolved["raw_records"]:
            errors.append("resolved summary row count disagrees with the row-level census")
    return errors


def parse_range(value: str) -> tuple[int, int]:
    match = re.fullmatch(r"(\d+)_TO_(\d+)", value)
    if not match:
        raise ValueError(value)
    low, high = map(int, match.groups())
    if low > high:
        raise ValueError(value)
    return low, high


def validate_reference(
    slot: str,
    field: str,
    value: str,
    errors: list[str],
    *,
    allowed_prefixes: tuple[str, ...] = (),
) -> None:
    if not value or value.startswith("HOLD"):
        errors.append(f"{slot}: {field} requires an exact source reference")
        return
    for reference in value.split("|"):
        match = re.fullmatch(r"(.+):(\d+)", reference)
        if not match:
            errors.append(f"{slot}: invalid {field} reference {reference!r}")
            continue
        relative, line_text = match.groups()
        if allowed_prefixes and not relative.startswith(allowed_prefixes):
            errors.append(f"{slot}: {field} must use an allowed source domain")
            continue
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"{slot}: missing {field} file {relative}")
            continue
        line = int(line_text)
        line_count = sum(1 for _ in path.open("r", encoding="utf-8-sig"))
        if line < 1 or line > line_count:
            errors.append(f"{slot}: {field} line {line} is outside {relative}")
            continue
        source_text = path.read_text(encoding="utf-8-sig").splitlines()[line - 1].strip()
        if not source_text or source_text.startswith("#"):
            errors.append(f"{slot}: {field} must cite a meaningful role sentence or registry row, not a heading")


def ga_number(value: str) -> int | None:
    if value == "E1-E20":
        return 1
    match = re.search(r"GA(\d+)", value)
    return int(match.group(1)) if match else None


def reference_ga_numbers(value: str) -> list[int]:
    numbers: list[int] = []
    for reference in value.split("|"):
        relative = reference.rsplit(":", 1)[0].lower()
        numbers.extend(
            int(match.group(1))
            for match in re.finditer(r"(?:^|[/_-])ga(\d+)(?=[/_-])", relative)
        )
    return numbers


def exact_reference_text(value: str) -> str | None:
    match = re.fullmatch(r"(.+):(\d+)", value)
    if not match:
        return None
    path = ROOT / match.group(1)
    if not path.is_file():
        return None
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    line = int(match.group(2))
    return lines[line - 1].strip() if 1 <= line <= len(lines) else None


def validate(
    role_rows: list[dict[str, str]],
    category_rows: list[dict[str, str]],
    direction_rows: list[dict[str, str]],
    crosswalk_rows: list[dict[str, str]],
    *,
    check_documents: bool,
) -> list[str]:
    errors: list[str] = []

    if [row["role_tier"] for row in role_rows] != EXPECTED_ROLE_TIERS:
        errors.append("role tiers must be ordered and complete")
    if len({row["role_tier"] for row in role_rows}) != len(role_rows):
        errors.append("role tiers must be unique")
    role_fields = tuple(role_rows[0]) if role_rows else ()
    role_payload = "".join(
        "|".join(row[field] for field in role_fields) + "\n" for row in role_rows
    )
    if hashlib.sha256(role_payload.encode()).hexdigest() != EXPECTED_ROLE_SEMANTIC_SHA256:
        errors.append("role-tier capacity semantics drifted from the reviewed source lock")
    census_resolved = False
    if not CENSUS_FILE.is_file():
        errors.append("missing cast semantic-census summary")
    else:
        census_rows = read_csv(CENSUS_FILE)
        census_fields = tuple(census_rows[0]) if census_rows else ()
        census_payload = "".join(
            "|".join(row[field] for field in census_fields) + "\n" for row in census_rows
        )
        if len(census_rows) != 6:
            errors.append("cast semantic-census summary must preserve six count scopes")
        if hashlib.sha256(census_payload.encode()).hexdigest() != EXPECTED_CENSUS_SEMANTIC_SHA256:
            errors.append("cast semantic-census counts drifted from the reviewed source lock")
        census_resolved = any(
            row["count_status"] == "RESOLVED_LOWER_BOUND" for row in census_rows
        )
        if census_resolved:
            census_errors = check_resolved_census(census_rows)
            errors.extend(census_errors)

    named_low = 0
    named_high = 0
    for row in role_rows:
        tier = row["role_tier"]
        if row["canon_status"] != "PROPOSED_NONCANON":
            errors.append(f"{tier}: role demand must remain noncanon")
        if row["personal_signature_frame_need"] != EXPECTED_SIGNATURE_POLICY.get(tier):
            errors.append(f"{tier}: personal signature-frame policy drifted")
        if not row["shared_asset_rule"] or row["shared_asset_rule"] in {
            "NONE",
            "HOLD",
            "PERSONAL_FRAME_FOR_EVERYONE",
        }:
            errors.append(f"{tier}: shared/reuse asset rule is required")
        if tier == "BACKGROUND_ROLE_GROUP":
            if row["named_frame_hull_story_slots"] != "NOT_INDIVIDUALLY_COUNTED":
                errors.append("background roles cannot receive individual frame slots")
            if "NO_INDIVIDUAL_CATALOG_PROMOTION" not in row["reader_memory_rule"]:
                errors.append("background roles require an anti-promotion memory rule")
            continue
        try:
            low, high = parse_range(row["named_frame_hull_story_slots"])
        except ValueError:
            errors.append(f"{tier}: invalid named frame-hull range")
            continue
        named_low += low
        named_high += high
    if (named_low, named_high) != (32, 50):
        errors.append(f"named frame-hull role slots must total 32-50, found {named_low}-{named_high}")

    if [row["domain_id"] for row in category_rows] != EXPECTED_DOMAINS:
        errors.append("category rows must be ordered C1 through C8")
    source_total = 0
    for row in category_rows:
        domain = row["domain_id"]
        try:
            source_rows = int(row["source_registry_rows"])
        except ValueError:
            errors.append(f"{domain}: source registry rows must be numeric")
            continue
        source_total += source_rows
        if source_rows != EXPECTED_SOURCE_ROWS.get(domain):
            errors.append(f"{domain}: source row count changed unexpectedly")
        if row["canon_status"] != "PROPOSED_NONCANON":
            errors.append(f"{domain}: category band must remain noncanon")
        if not row["agent_id"]:
            errors.append(f"{domain}: completed agent evidence is required")
        actual_category = (
            row["front_stage_band"],
            row["background_band"],
            row["state_variant_band"],
            row["working_capacity"],
        )
        if actual_category != EXPECTED_CATEGORY_BANDS.get(domain):
            errors.append(f"{domain}: category planning bands or HOLD gate drifted")
    if source_total != 415:
        errors.append(f"category source rows must total 415, found {source_total}")
    by_domain = {row["domain_id"]: row for row in category_rows}
    expected_c2 = "32_TO_40_CANDIDATES_UNDER_DIRECTION_B_PENDING_CHASSIS_PROOF"
    if by_domain.get("C2", {}).get("working_capacity") != expected_c2:
        errors.append("C2 working capacity must cite the selected direction and keep chassis proof pending")
    # C1 left the HOLD set once the row-level census resolved it; every other domain
    # still lacks a role/asset crosswalk and must stay on HOLD.
    expected_c1 = "197_PERSONS_1_4_9_40_143_BY_TIER"
    if by_domain.get("C1", {}).get("working_capacity") != expected_c1:
        errors.append("C1 working capacity must report the resolved census tier split")
    for hold_domain in ("C3", "C4", "C5", "C6", "C7", "C8"):
        if not by_domain.get(hold_domain, {}).get("working_capacity", "").startswith("HOLD"):
            errors.append(f"{hold_domain}: stable entity capacity must remain HOLD")

    if [row["direction_id"] for row in direction_rows] != EXPECTED_DIRECTIONS:
        errors.append("portfolio directions must be ordered A through D")
    for row in direction_rows:
        direction = row["direction_id"]
        try:
            base = int(row["base_demand_slots"])
            conditional = int(row["conditional_demand_slots"])
            total = int(row["total_capacity"])
        except ValueError:
            errors.append(f"{direction}: direction counts must be numeric")
            continue
        if (base, conditional, total) != (52, 6, 58):
            errors.append(f"{direction}: every direction must cover the same 52 plus 6 role-demand surface")
        actual_bands = tuple(
            row[field]
            for field in (
                "candidate_review_band",
                "reader_named_model_band",
                "named_hull_band",
                "form_state_band",
            )
        )
        for value in actual_bands:
            try:
                parse_range(value)
            except ValueError:
                errors.append(f"{direction}: invalid planning band {value!r}")
        if actual_bands != EXPECTED_DIRECTION_BANDS.get(direction):
            errors.append(f"{direction}: direction output bands drifted")
        try:
            _, candidate_high = parse_range(row["candidate_review_band"])
        except ValueError:
            pass
        else:
            if candidate_high > total:
                errors.append(f"{direction}: candidate-review envelope cannot exceed demand surface")
        if row["selection_state"] != EXPECTED_DIRECTION_STATES.get(direction):
            errors.append(f"{direction}: direction selection state drifted")
        if row["canon_status"] != "PROPOSED_NONCANON":
            errors.append(f"{direction}: portfolio direction must remain noncanon")
    selected = [row for row in direction_rows if row["selection_state"].startswith("SELECTED")]
    if not census_resolved and selected:
        errors.append("no portfolio count direction may be selected before the full role census")
    if census_resolved and len(selected) != 1:
        errors.append("exactly one portfolio direction must be selected once the census resolves")
    for row in selected:
        if "AUTHOR_DECISION" not in row["selection_state"]:
            errors.append(
                f"{row['direction_id']}: a selected direction must cite the author decision that chose it"
            )

    expected_ids = [f"FD-{number:03d}" for number in range(1, 59)]
    actual_ids = [row["demand_slot"] for row in crosswalk_rows]
    if actual_ids != expected_ids:
        errors.append("crosswalk ids must be ordered FD-001 through FD-058")
    if len(set(actual_ids)) != len(actual_ids):
        errors.append("crosswalk demand slots must be unique")
    anchors = [row["demand_anchor"] for row in crosswalk_rows]
    if len(set(anchors)) != len(anchors):
        errors.append("crosswalk demand anchors must be unique")
    crosswalk_fields = tuple(crosswalk_rows[0]) if crosswalk_rows else ()
    crosswalk_payload = "".join(
        "|".join(row[field] for field in crosswalk_fields) + "\n" for row in crosswalk_rows
    )
    if hashlib.sha256(crosswalk_payload.encode()).hexdigest() != EXPECTED_CROSSWALK_SEMANTIC_SHA256:
        errors.append("crosswalk role, faction, chronology, function and count semantics drifted")

    model_rows = [row for row in crosswalk_rows if row["capacity_state"] == "BASE_MODEL_CANDIDATE"]
    reuse_rows = [row for row in crosswalk_rows if row["capacity_state"] == "BASE_REUSE_PROFILE"]
    evidence_hold_rows = [row for row in crosswalk_rows if row["capacity_state"] == "EVIDENCE_HOLD"]
    conditional_rows = [row for row in crosswalk_rows if row["capacity_state"] == "CONDITIONAL_HOLD"]
    if (len(model_rows), len(reuse_rows), len(evidence_hold_rows), len(conditional_rows)) != (26, 25, 1, 6):
        errors.append(
            "crosswalk must contain 26 model candidates, 25 reviewed reuse profiles, 1 evidence HOLD and 6 conditional rows"
        )
    reuse_evidence_payload = "".join(
        f"{row['demand_slot']}|{row['canon_role_refs']}|{row['operation_refs']}\n"
        for row in reuse_rows
    )
    if hashlib.sha256(reuse_evidence_payload.encode()).hexdigest() != EXPECTED_REUSE_EVIDENCE_SHA256:
        errors.append("reuse role/operation evidence mapping drifted from the reviewed source lock")
    semantic_fields = (
        "demand_slot",
        "demand_anchor",
        "role_tier",
        "faction_ecology",
        "ga_window",
        "mission_domain",
        "canon_role_refs",
        "canon_role_quote_token",
        "operation_refs",
        "operation_quote_token",
        "reviewed_reuse_candidates",
        "reuse_assessment",
        "parent_formation_ecology",
        "support_ecology",
        "temporal_compatibility",
        "functional_compatibility",
        "cradle_compatibility",
        "cooling_recovery_compatibility",
    )
    reuse_semantic_payload = "".join(
        "|".join(row[field] for field in semantic_fields) + "\n" for row in reuse_rows
    )
    if hashlib.sha256(reuse_semantic_payload.encode()).hexdigest() != EXPECTED_REUSE_SEMANTIC_SHA256:
        errors.append("reuse function, host or support mapping drifted from the reviewed semantic lock")
    if len({row["reuse_assessment"] for row in reuse_rows}) != len(reuse_rows):
        errors.append("reuse profiles require distinct function-specific assessments")
    lineup_by_slot = {row["slot_id"]: row for row in read_csv(MECHA_INDEX_FILE)}

    for index, row in enumerate(crosswalk_rows, start=1):
        slot = row["demand_slot"]
        if row["role_tier"] not in ALLOWED_CROSSWALK_ROLES:
            errors.append(f"{slot}: unknown role tier")
        if any(forbidden in " ".join(row.values()).upper() for forbidden in FORBIDDEN_CLAIMS):
            errors.append(f"{slot}: forbidden promotion, solo or unsupported claim")

        if row["capacity_state"] in {"BASE_MODEL_CANDIDATE", "BASE_REUSE_PROFILE"}:
            for field in ("demand_anchor", "ga_window", "mission_domain", "parent_formation_ecology", "support_ecology"):
                if not row[field] or row[field] == "HOLD":
                    errors.append(f"{slot}: proposed demand row requires {field}")
            if row["canon_status"] != "PROPOSED_NONCANON_MAPPING":
                errors.append(f"{slot}: proposed demand mapping must remain noncanon")
        if row["capacity_state"] in {"BASE_MODEL_CANDIDATE", "BASE_REUSE_PROFILE", "EVIDENCE_HOLD"}:
            for reference_field, token_field in (
                ("canon_role_refs", "canon_role_quote_token"),
                ("operation_refs", "operation_quote_token"),
            ):
                source_text = exact_reference_text(row[reference_field])
                if source_text is None or row[token_field] != source_text:
                    errors.append(f"{slot}: {token_field} must exactly lock the cited source line")
            demand_ga = ga_number(row["ga_window"])
            operation_gas = reference_ga_numbers(row["operation_refs"])
            if demand_ga is not None and any(operation_ga > demand_ga for operation_ga in operation_gas):
                errors.append(f"{slot}: operation evidence occurs after the demand start GA")

        if row["capacity_state"] == "BASE_MODEL_CANDIDATE":
            validate_reference(slot, "canon_role_refs", row["canon_role_refs"], errors)
            validate_reference(slot, "operation_refs", row["operation_refs"], errors)
            expected_sample = f"M-{index:03d}"
            if row["sample_slot_ref"] != expected_sample:
                errors.append(f"{slot}: expected sample reference {expected_sample}")
            if row["manufacturing_scale"] not in ALLOWED_MODEL_MANUFACTURING:
                errors.append(f"{slot}: model candidate needs a physical manufacturing scale")
            if row["count_decision"] != "PROVISIONAL_MODEL_SLOT":
                errors.append(f"{slot}: model candidate must remain provisional")
            if row["story_status_policy"] != "HULL_INSTANCE_LEDGER_ONLY":
                errors.append(f"{slot}: model story status must remain in the hull ledger")
            if row["named_hull_policy"] not in {"FRONT_REQUIRED", "FRONT_CANDIDATE", "BACKGROUND_MODEL"}:
                errors.append(f"{slot}: invalid model named-hull policy")
            if row["reuse_failure_type"] != "PROPOSED_LOAD_FRAME_PLUS_TWO_MAJOR_SYSTEMS":
                errors.append(f"{slot}: model candidate requires a proposed reuse-failure type")
            if row["major_system_change_claim"] in {"", "NONE_NO_NEW_MODEL_CLAIM", "HOLD_MECHANICAL_PROOF"}:
                errors.append(f"{slot}: model candidate requires a major-system change claim")
            changed_systems = set(row["major_system_change_claim"].split("|"))
            unknown_systems = sorted(changed_systems - ALLOWED_MAJOR_SYSTEMS)
            if unknown_systems:
                errors.append(f"{slot}: unknown model major-system token(s) {unknown_systems}")
            host = lineup_by_slot.get(expected_sample)
            if host and row["major_system_change_claim"] != host["major_system_changes"]:
                errors.append(f"{slot}: model major-system claim must match the lineup index")
            if not row["reuse_or_model_reason"]:
                errors.append(f"{slot}: model candidate requires reuse_or_model_reason")
            expected_compatibility = {
                "temporal_compatibility": "CANDIDATE_REVEAL_MATCHES_DEMAND",
                "functional_compatibility": "CANDIDATE_REQUIRES_CHASSIS_GATE",
                "cradle_compatibility": "CANDIDATE_CRADLE_PROOF_IN_INDEX",
                "cooling_recovery_compatibility": "CANDIDATE_COOLING_PROOF_IN_INDEX",
            }
            for field, value in expected_compatibility.items():
                if row[field] != value:
                    errors.append(f"{slot}: model {field} must remain {value}")

        elif row["capacity_state"] == "BASE_REUSE_PROFILE":
            validate_reference(
                slot,
                "canon_role_refs",
                row["canon_role_refs"],
                errors,
                allowed_prefixes=("docs/05_characters/",),
            )
            validate_reference(
                slot,
                "operation_refs",
                row["operation_refs"],
                errors,
                allowed_prefixes=(
                    "docs/03_systems/",
                    "docs/07_military/",
                    "docs/10_story_architecture/",
                ),
            )
            if row["sample_slot_ref"] != "NONE_NEW_GAP":
                errors.append(f"{slot}: reuse profile must not claim a new sample model")
            candidates = row["reviewed_reuse_candidates"].split("|")
            if not candidates or any(not re.fullmatch(r"M-\d{3}", value) for value in candidates):
                errors.append(f"{slot}: reuse candidates must be explicit M-IDs")
            elif any(int(value[2:]) < 1 or int(value[2:]) > 26 for value in candidates):
                errors.append(f"{slot}: reuse candidates must resolve to M-001 through M-026")
            if row["reviewed_reuse_candidates"] != EXPECTED_REUSE_CANDIDATES.get(slot):
                errors.append(f"{slot}: reviewed reuse candidate mapping drifted")
            demand_ga = ga_number(row["ga_window"])
            for candidate in candidates:
                host = lineup_by_slot.get(candidate)
                if host is None:
                    continue
                reveal_ga = ga_number(host["first_reveal_window"])
                if demand_ga is None or reveal_ga is None or reveal_ga > demand_ga:
                    errors.append(f"{slot}: reuse candidate {candidate} is unavailable at demand start")
                for host_field in ("role", "cradle_and_carrier", "cooling_and_recovery"):
                    if not host[host_field] or "HOLD" in host[host_field]:
                        errors.append(f"{slot}: reuse host {candidate} lacks usable {host_field}")
            if not row["reuse_assessment"].startswith("REUSE_AS_"):
                errors.append(f"{slot}: reuse assessment must start REUSE_AS_")
            expected = {
                "reuse_failure_type": "NONE_REUSE_SUFFICIENT",
                "manufacturing_scale": "INHERIT_FROM_HOST",
                "major_system_change_claim": "NONE_NO_NEW_MODEL_CLAIM",
                "story_status_policy": "HOST_HULL_LEDGER_ONLY",
                "named_hull_policy": "NO_NEW_MODEL_NAME",
                "reuse_or_model_reason": "REUSE_SUFFICIENT_NO_INDEPENDENT_MODEL",
                "count_decision": "REUSE_PROFILE_NOT_NEW_MODEL",
                "temporal_compatibility": "PASS_HOST_AVAILABLE_BY_DEMAND_START",
                "functional_compatibility": "PASS_ROLE_OPERATION_HOST_MAPPING_REVIEWED",
                "cradle_compatibility": "PASS_INHERIT_HOST_CRADLE_AND_CERTIFICATION",
                "cooling_recovery_compatibility": "PASS_INHERIT_HOST_COOLING_AND_RECOVERY",
            }
            for field, value in expected.items():
                if row[field] != value:
                    errors.append(f"{slot}: reuse {field} must remain {value}")

        elif row["capacity_state"] == "EVIDENCE_HOLD":
            validate_reference(
                slot,
                "canon_role_refs",
                row["canon_role_refs"],
                errors,
                allowed_prefixes=("docs/05_characters/",),
            )
            validate_reference(
                slot,
                "operation_refs",
                row["operation_refs"],
                errors,
                allowed_prefixes=(
                    "docs/03_systems/",
                    "docs/07_military/",
                    "docs/10_story_architecture/",
                ),
            )
            if slot != "FD-034":
                errors.append(f"{slot}: only the reviewed FD-034 host-deployment gap may remain evidence HOLD")
            expected = {
                "sample_slot_ref": "NONE_NEW_GAP",
                "reviewed_reuse_candidates": "HOLD_NO_DEPLOYED_HOST",
                "reuse_assessment": "HOLD_ROLE_OPERATION_SUPPORTED_HOST_UNPROVEN",
                "reuse_failure_type": "HOLD_HOST_DEPLOYMENT_UNPROVEN",
                "manufacturing_scale": "UNASSIGNED",
                "major_system_change_claim": "HOLD_MECHANICAL_PROOF",
                "story_status_policy": "HOLD_NO_HULL_STATUS",
                "named_hull_policy": "HOLD",
                "parent_formation_ecology": "HOLD",
                "support_ecology": "HOLD",
                "count_decision": "EVIDENCE_HOLD_NOT_COUNTED",
                "canon_status": "PROPOSED_NONCANON_HOLD",
                "temporal_compatibility": "PASS_OPERATION_WITHIN_GA4",
                "functional_compatibility": "HOLD_HOST_FUNCTION",
                "cradle_compatibility": "HOLD_CRADLE",
                "cooling_recovery_compatibility": "HOLD_COOLING_RECOVERY",
            }
            for field, value in expected.items():
                if row[field] != value:
                    errors.append(f"{slot}: evidence HOLD {field} must remain {value}")
            if not row["reuse_or_model_reason"].startswith("ROLE_AND_OPERATION_EXIST_"):
                errors.append(f"{slot}: evidence HOLD requires the reviewed host-deployment reason")

        elif row["capacity_state"] == "CONDITIONAL_HOLD":
            expected_sample = "M-027" if index == 53 else "M-028" if index == 54 else "NONE"
            if row["sample_slot_ref"] != expected_sample:
                errors.append(f"{slot}: conditional sample reference drifted")
            expected = {
                "canon_role_refs": "HOLD_AUTHOR_DECISION",
                "operation_refs": "HOLD",
                "canon_role_quote_token": "HOLD",
                "operation_quote_token": "HOLD",
                "reuse_assessment": "CONDITIONAL_UNPROVEN",
                "reuse_failure_type": "HOLD_REUSE_FAILURE_NOT_PROVEN",
                "manufacturing_scale": "UNASSIGNED",
                "major_system_change_claim": "HOLD_MECHANICAL_PROOF",
                "story_status_policy": "HOLD_NO_HULL_STATUS",
                "named_hull_policy": "HOLD",
                "parent_formation_ecology": "HOLD",
                "support_ecology": "HOLD",
                "count_decision": "CONDITIONAL_NOT_COUNTED",
                "canon_status": "PROPOSED_NONCANON_HOLD",
                "temporal_compatibility": "HOLD_CHRONOLOGY",
                "functional_compatibility": "HOLD_FUNCTION",
                "cradle_compatibility": "HOLD_CRADLE",
                "cooling_recovery_compatibility": "HOLD_COOLING_RECOVERY",
            }
            for field, value in expected.items():
                if row[field] != value:
                    errors.append(f"{slot}: conditional {field} must remain {value}")
            if not (
                row["reuse_or_model_reason"].startswith("REQUIRES_")
                or row["reuse_or_model_reason"].startswith("OPENS_ONLY_IF_")
            ):
                errors.append(f"{slot}: conditional opening gate is required")
        else:
            errors.append(f"{slot}: invalid capacity state")

    if check_documents:
        required = {
            AUDIT_FILE: [
                "26 provisional model candidates + 25 reviewed reuse profiles + 1 evidence HOLD + 6 conditional HOLD rows",
                "HOLD — 35 UNNAMED PERSONS, FD-034 HOST EVIDENCE AND M-002–M-026 CHASSIS PROOF — NONCANON",
                "Direction B raises the envelope, it does not authorize a machine",
            ],
            MECHA_ARCHITECTURE: [
                "26 provisional model candidates, 25 reviewed reuse profiles, one evidence HOLD and six conditional HOLD rows",
                "HOLD — FULL CAST SEMANTIC CENSUS, FD-034 HOST EVIDENCE AND M-002–M-026 CHASSIS PROOF — NONCANON",
            ],
        }
        for path, phrases in required.items():
            if not path.exists():
                errors.append(f"missing control document: {path.relative_to(ROOT)}")
                continue
            text = path.read_text(encoding="utf-8-sig")
            for phrase in phrases:
                if phrase not in text:
                    errors.append(f"missing control phrase in {path.relative_to(ROOT)}: {phrase}")

    return errors


def run_selftest(
    role_rows: list[dict[str, str]],
    category_rows: list[dict[str, str]],
    direction_rows: list[dict[str, str]],
    crosswalk_rows: list[dict[str, str]],
) -> int:
    base_errors = validate(role_rows, category_rows, direction_rows, crosswalk_rows, check_documents=False)
    if base_errors:
        print("ROLE-DEMAND SELFTEST BLOCKED BY INVALID BASE", file=sys.stderr)
        for error in base_errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    fixtures = []

    def add_fixture(name: str, mutate, expected: str) -> None:
        roles = copy.deepcopy(role_rows)
        categories = copy.deepcopy(category_rows)
        directions = copy.deepcopy(direction_rows)
        crosswalk = copy.deepcopy(crosswalk_rows)
        mutate(roles, categories, directions, crosswalk)
        fixtures.append((name, roles, categories, directions, crosswalk, expected))

    add_fixture("missing role", lambda r, _, __, ___: r.pop(), "role tiers")
    add_fixture("person machine parity", lambda r, _, __, ___: r[4].update(named_frame_hull_story_slots="70_TO_110"), "must total 32-50")
    add_fixture("silent role-band inflation", lambda r, _, __, ___: r[3].update(series_planning_band="999"), "role-tier capacity semantics")
    add_fixture("delete sharing rule", lambda r, _, __, ___: r[1].update(shared_asset_rule="NONE"), "shared/reuse asset rule")
    add_fixture("missing category", lambda _, c, __, ___: c.pop(), "ordered C1 through C8")
    add_fixture("source drift", lambda _, c, __, ___: c[1].update(source_registry_rows="12"), "source row count changed")
    add_fixture("C2 model inflation", lambda _, c, __, ___: c[1].update(working_capacity="58_CANON_MODELS"), "category planning bands")
    add_fixture("weapon target zero", lambda _, c, __, ___: c[2].update(front_stage_band="0_TO_0"), "category planning bands")
    add_fixture("ship target inflation", lambda _, c, __, ___: c[4].update(front_stage_band="99999_TO_99999"), "category planning bands")
    add_fixture("missing direction", lambda _, __, d, ___: d.pop(), "ordered A through D")
    add_fixture("different demand surface", lambda _, __, d, ___: d[1].update(base_demand_slots="48"), "same 52 plus 6")
    add_fixture("wrong A band", lambda _, __, d, ___: d[0].update(candidate_review_band="44_TO_60"), "output bands drifted")
    add_fixture("candidate envelope above demand", lambda _, __, d, ___: d[3].update(candidate_review_band="44_TO_60"), "cannot exceed demand surface")
    add_fixture("wrong selection", lambda _, __, d, ___: (d[0].update(selection_state="ALTERNATIVE"), d[2].update(selection_state="SELECTED_ASSUMPTION")), "direction selection state drifted")
    add_fixture("second direction selected", lambda _, __, d, ___: d[0].update(selection_state="SELECTED_AUTHOR_DECISION_D_20260812_01_POST_CENSUS"), "exactly one portfolio direction")
    add_fixture("no direction selected", lambda _, __, d, ___: d[1].update(selection_state="ALTERNATIVE"), "exactly one portfolio direction")
    add_fixture("selection without author decision", lambda _, __, d, ___: d[1].update(selection_state="SELECTED_BY_AGENT_CONSENSUS"), "must cite the author decision")
    add_fixture("premature direction canon", lambda _, __, d, ___: d[0].update(canon_status="CANON"), "must remain noncanon")
    add_fixture("missing crosswalk", lambda _, __, ___, x: x.pop(), "FD-001 through FD-058")
    add_fixture("model mapping drift", lambda _, __, ___, x: x[0].update(sample_slot_ref="M-002"), "expected sample reference")
    add_fixture("model proof cleared", lambda _, __, ___, x: x[1].update(major_system_change_claim="NONE_NO_NEW_MODEL_CLAIM"), "major-system change claim")
    add_fixture("invented crosswalk systems", lambda _, __, ___, x: x[1].update(major_system_change_claim="LOAD_FRAME|BANANA|POTATO"), "unknown model major-system token")
    add_fixture("reuse claims new model", lambda _, __, ___, x: x[26].update(sample_slot_ref="M-027"), "must not claim a new sample")
    add_fixture("reuse assessment none", lambda _, __, ___, x: x[26].update(reuse_assessment="NONE"), "must start REUSE_AS_")
    add_fixture("duplicate reuse functions", lambda _, __, ___, x: x[27].update(reuse_assessment=x[26]["reuse_assessment"], functional_compatibility=x[26]["functional_compatibility"]), "distinct function-specific assessments")
    add_fixture("reuse candidate outside sample", lambda _, __, ___, x: x[27].update(reviewed_reuse_candidates="M-099"), "M-001 through M-026")
    add_fixture("reuse all one host", lambda _, __, ___, x: x[28].update(reviewed_reuse_candidates="M-001"), "reuse candidate mapping drifted")
    add_fixture("reuse timeline inversion", lambda _, __, ___, x: x[26].update(reviewed_reuse_candidates="M-003"), "unavailable at demand start")
    add_fixture("reuse manufacturing fork", lambda _, __, ___, x: x[28].update(manufacturing_scale="LIMITED_RUN"), "reuse manufacturing_scale")
    add_fixture("reuse chronology flag bypass", lambda _, __, ___, x: x[28].update(temporal_compatibility="PASS_ANYTIME"), "reuse temporal_compatibility")
    add_fixture("reuse cradle bypass", lambda _, __, ___, x: x[28].update(cradle_compatibility="NONE"), "reuse cradle_compatibility")
    add_fixture("reuse support drift", lambda _, __, ___, x: x[28].update(support_ecology="UNLIMITED_SUPPORT"), "semantic lock")
    add_fixture("reuse role-faction-function drift", lambda _, __, ___, x: x[31].update(role_tier="CORE_ANTAGONIST_RIVAL", faction_ecology="UNRELATED", mission_domain="UNRELATED"), "crosswalk role, faction, chronology, function")
    add_fixture("operation chronology inversion", lambda _, __, ___, x: x[31].update(ga_window="GA3"), "operation evidence occurs after the demand start GA")
    add_fixture("reuse counted as model", lambda _, __, ___, x: x[29].update(count_decision="PROVISIONAL_MODEL_SLOT"), "reuse count_decision")
    add_fixture("missing exact source", lambda _, __, ___, x: x[30].update(canon_role_refs="HOLD"), "exact source reference")
    add_fixture("missing source file", lambda _, __, ___, x: x[31].update(operation_refs="docs/07_military/missing.md:1"), "missing operation_refs file")
    add_fixture("title-only role source", lambda _, __, ___, x: x[26].update(canon_role_refs="docs/05_characters/instructor-i001-field-bible-v1.md:1"), "meaningful role")
    add_fixture("source quote drift", lambda _, __, ___, x: x[26].update(canon_role_quote_token="UNRELATED TITLE"), "must exactly lock")
    add_fixture("control file as role source", lambda _, __, ___, x: x[26].update(canon_role_refs="CLAUDE.md:1"), "allowed source domain")
    add_fixture("GA9 mapped to GA3 operation", lambda _, __, ___, x: x[49].update(operation_refs="docs/07_military/front-stage-formation-registry-and-loss-accounting-v1.md:50"), "evidence mapping drifted")
    add_fixture("evidence HOLD assigned a host", lambda _, __, ___, x: x[33].update(reviewed_reuse_candidates="M-014"), "evidence HOLD reviewed_reuse_candidates")
    add_fixture("all legendary", lambda _, __, ___, x: x[0].update(story_status_policy="ALL_LEGEND"), "forbidden promotion")
    add_fixture("conditional auto canon", lambda _, __, ___, x: x[52].update(count_decision="AUTO_CANON"), "conditional count_decision")
    add_fixture("conditional assigned", lambda _, __, ___, x: x[53].update(parent_formation_ecology="JNT_ARD"), "conditional parent_formation_ecology")

    failures: list[str] = []
    for name, roles, categories, directions, crosswalk, expected in fixtures:
        fixture_errors = validate(roles, categories, directions, crosswalk, check_documents=False)
        if not any(expected in error for error in fixture_errors):
            failures.append(f"{name}: expected error containing {expected!r}")

    # The resolved-census checks read the row-level file directly, so they need their own
    # fixtures. Each one deliberately breaks the on-disk census and must be caught.
    census_baseline = read_csv(CENSUS_FILE)
    census_defects: list[tuple[str, object, str]] = [
        ("census summary person drift",
         lambda rows: rows[5].update(deduplicated_identity_result="9999_PERSONS|41_OFFICE"),
         "person count disagrees"),
        ("census summary row drift",
         lambda rows: rows[5].update(raw_records="12_CENSUS_ROWS"),
         "row count disagrees"),
        ("census summary scope removed",
         lambda rows: rows[5].update(scope="REPOSITORY_WIDE_MINIMUM"),
         "REPOSITORY_WIDE_RESOLVED summary scope"),
    ]
    for name, mutate, expected in census_defects:
        rows = copy.deepcopy(census_baseline)
        mutate(rows)
        if not any(expected in error for error in check_resolved_census(rows)):
            failures.append(f"{name}: expected error containing {expected!r}")
    fixtures.extend([(name, [], [], [], [], expected) for name, _, expected in census_defects])

    # Prove the row-level census guards fire by pointing the checker at broken copies.
    census_rows_baseline = read_csv(CENSUS_ROWS_FILE)
    row_defects: list[tuple[str, object, str]] = [
        ("census duplicate identity",
         lambda rows: rows.append(dict(rows[0])),
         "identity keys must be unique"),
        ("census tier erased",
         lambda rows: rows[0].update(final_tier=""),
         "census row has no tier"),
        ("census source erased",
         lambda rows: rows[0].update(source_docs=""),
         "no source document"),
        ("census unmarked invented name",
         lambda rows: next(
             row for row in rows
             if row["record_type"] == "PERSON" and not row["korean_name"].strip()
         ).update(alias_merge_hints="looks fine"),
         "must be marked 표기 미확정"),
        ("census tier mix drift",
         lambda rows: next(
             row for row in rows if row["final_tier"] == "IMPORTANT_EXTRA"
         ).update(final_tier="CORE_ALLY"),
         "person tier mix drifted"),
    ]
    original_reader = globals()["read_csv"]
    for name, mutate, expected in row_defects:
        rows = copy.deepcopy(census_rows_baseline)
        mutate(rows)
        globals()["read_csv"] = lambda path, _rows=rows, _orig=original_reader: (
            _rows if path == CENSUS_ROWS_FILE else _orig(path)
        )
        try:
            found = check_resolved_census(census_baseline)
        finally:
            globals()["read_csv"] = original_reader
        if not any(expected in error for error in found):
            failures.append(f"{name}: expected error containing {expected!r}")
    fixtures.extend([(name, [], [], [], [], expected) for name, _, expected in row_defects])

    if failures:
        print("ROLE-DEMAND SELFTEST FAILED", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("ROLE-DEMAND SELFTEST PASSED")
    print(f"- defect fixtures fired: {len(fixtures)}")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) > 1 or (argv and argv[0] != "--selftest"):
        print("usage: validate_role_demand_portfolio.py [--selftest]", file=sys.stderr)
        return 2
    try:
        role_rows = read_csv(ROLE_FILE)
        category_rows = read_csv(CATEGORY_FILE)
        direction_rows = read_csv(DIRECTION_FILE)
        crosswalk_rows = read_csv(CROSSWALK_FILE)
    except FileNotFoundError as exc:
        print(f"missing role-demand input: {exc}", file=sys.stderr)
        return 1

    if argv == ["--selftest"]:
        return run_selftest(role_rows, category_rows, direction_rows, crosswalk_rows)

    errors = validate(role_rows, category_rows, direction_rows, crosswalk_rows, check_documents=True)
    if errors:
        print("ROLE-DEMAND PORTFOLIO VALIDATION FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("ROLE-DEMAND PORTFOLIO VALIDATION PASSED")
    print("- role tiers: 6; named frame-hull story slots: 32-50")
    print("- category source rows: 415 preserved across C1-C8")
    print("- phase-1 demand sample: 26 model candidates; 25 reviewed reuse profiles; 1 evidence HOLD; 6 conditional rows")
    print("- cast census resolved: 197 persons (1/4/9/40/143 by tier); 35 still lack a canon Korean name")
    print("- selected direction: B BALANCED_BRANCHING, 22-30 reader-named models, author decision D-20260812-01")
    print("- reuse-first remains the method; verified independent-model count still HOLD until chassis proof")
    print("- 28-row frame catalog remains a phase-1 sample, not a target")
    print("- exact C3-C8 role-derived counts plus total collectibles: HOLD")
    print("- canon promotions: none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
