#!/usr/bin/env python3
"""Validate the proposed noncanon maneuver-frame lineup and its evidence matrix."""

from __future__ import annotations

import copy
import csv
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "docs" / "06_hardware" / "data"
INDEX_FILE = DATA_DIR / "maneuver-frame-lineup-proposed-index-v1.csv"
EVIDENCE_FILE = DATA_DIR / "maneuver-frame-lineup-evidence-matrix-v1.csv"
HARD_REJECT_FILE = DATA_DIR / "mecha-hard-reject-public-names-v1.txt"

# Direction C, author decision D-20260813-03 (supersedes D-20260812-01).
# 43 chassis slots + 07 + 2 author-decision reserves.
PORTFOLIO_ROWS = 46

EXPECTED_LINEAGE_COUNTS = {
    "L01": 6,
    "L02": 8,
    "L03": 6,
    "L04": 7,
    "L05": 5,
    "L06": 6,
    "L07": 6,
    "L08": 2,
}
EXPECTED_RECORD_COUNTS = {
    "VERIFIED_ENTITY": 1,
    "CHASSIS_SLOT": 43,
    "RESERVE_SLOT": 2,
}
# GA9 stays at zero by design: section 8 gives that arc reversible service and
# certification overlays, not new bodies. Direction C raised every other arc.
EXPECTED_FIRST_REVEAL_COUNTS = {
    "GA1": 4,
    "GA2": 6,
    "GA3": 7,
    "GA4": 4,
    "GA5": 7,
    "GA6": 4,
    "GA7": 2,
    "GA8": 5,
    "GA9": 0,
    "GA10": 4,
}

ALLOWED_STATUSES = {
    "CANON_ENTITY",
    "PROPOSED_EXPLICIT_SLOT",
    "PROPOSED_GENERIC_FRAMEWORK",
    "HOLD_AUTHOR_DECISION",
}
ALLOWED_BASIS_TYPES = {
    "DIRECT_CANON_ENTITY",
    "EXPLICIT_FRAMEWORK_SLOT",
    "EXPLICIT_LINEAGE_GENERIC_MODEL",
    "EXPLICIT_OPERATIONAL_FORCE_SLOT",
    "EXPLICIT_INDIVIDUAL_FUNCTION",
    "GENERIC_FORCE_FRAMEWORK",
    "USER_WORKING_DIRECTION_NO_CANON_EVENT",
    "PURE_RESERVE_NO_CANON_BASIS",
}
PROTECTED_CANON_TERMS = {
    "LIAN",
    "HAREN",
    "ERIN",
    "TALREN",
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
}

COLLECTION_FIELDS = {
    "discovery_clue",
    "acquisition_gate",
    "synergy_partner",
    "completion_legacy",
    "counter_collection_risk",
    "loss_cost",
}
LOGISTICS_FIELDS = {
    "scale_band",
    "cradle_and_carrier",
    "cooling_and_recovery",
    "maintenance_band",
}
NEW_FILES_EXCLUDED_FROM_COLLISION_SCAN = {
    ROOT / "docs" / "06_hardware" / "maneuver-frame-lineup-master-architecture-v1.md",
    ROOT / "docs" / "06_hardware" / "maneuver-frame-lineup-visual-sheet-prompt-pack-v1.md",
    ROOT / "docs" / "07_military" / "frame-formation-combat-and-collectibility-integration-audit-v1.md",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_hard_reject_names() -> set[str]:
    if not HARD_REJECT_FILE.exists():
        raise FileNotFoundError(HARD_REJECT_FILE)
    return {
        line.strip().upper()
        for line in HARD_REJECT_FILE.read_text(encoding="utf-8-sig").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def duplicates(values: list[str]) -> set[str]:
    counts = Counter(values)
    return {value for value, count in counts.items() if count > 1}


def edit_distance(left: str, right: str) -> int:
    previous = list(range(len(right) + 1))
    for left_index, left_char in enumerate(left, start=1):
        current = [left_index]
        for right_index, right_char in enumerate(right, start=1):
            current.append(
                min(
                    current[-1] + 1,
                    previous[right_index] + 1,
                    previous[right_index - 1] + (left_char != right_char),
                )
            )
        previous = current
    return previous[-1]


def first_reveal_ga(value: str) -> str | None:
    if value == "E1-E20" or value.startswith("GA1_"):
        return "GA1"
    match = re.match(r"GA(10|[2-9])(?:_|$)", value)
    return f"GA{match.group(1)}" if match else None


def ga_number(value: str) -> int | None:
    ga = first_reveal_ga(value)
    return int(ga[2:]) if ga else None


def parse_source_ref(value: str) -> tuple[Path, int] | None:
    try:
        relative_path, line_text = value.rsplit(":", 1)
        return ROOT / relative_path, int(line_text)
    except (ValueError, TypeError):
        return None


def source_line(value: str) -> tuple[str | None, str | None]:
    parsed = parse_source_ref(value)
    if parsed is None:
        return None, "invalid source reference"
    source_path, line_number = parsed
    if not source_path.exists():
        return None, f"missing source file {source_path}"
    lines = source_path.read_text(encoding="utf-8-sig").splitlines()
    if not 1 <= line_number <= len(lines):
        return None, "source line is out of range"
    return lines[line_number - 1], None


def existing_markdown_corpus() -> str:
    chunks: list[str] = []
    for path in ROOT.rglob("*.md"):
        if path in NEW_FILES_EXCLUDED_FROM_COLLISION_SCAN:
            continue
        chunks.append(path.read_text(encoding="utf-8-sig").upper())
    return "\n".join(chunks)


def normalized_public_name(value: str) -> str:
    return re.sub(r"[^A-Z0-9]+", " ", value.upper()).strip()


def contains_rejected_term(name: str, rejected_terms: set[str]) -> list[str]:
    normalized_name = normalized_public_name(name)
    padded_name = f" {normalized_name} "
    name_tokens = set(normalized_name.split())
    found: list[str] = []
    for term in rejected_terms:
        normalized_term = normalized_public_name(term)
        term_tokens = normalized_term.split()
        compact_term = "".join(term_tokens)
        phrase_match = f" {normalized_term} " in padded_name
        compact_token_match = len(term_tokens) > 1 and compact_term in name_tokens
        if phrase_match or compact_token_match:
            found.append(term)
    return sorted(found)


def validate(
    rows: list[dict[str, str]],
    evidence_rows: list[dict[str, str]],
    rejected_terms: set[str],
    *,
    scan_repository_names: bool,
) -> list[str]:
    errors: list[str] = []

    if len(rows) != PORTFOLIO_ROWS:
        errors.append(f"expected {PORTFOLIO_ROWS} portfolio rows, found {len(rows)}")
    if len(evidence_rows) != PORTFOLIO_ROWS:
        errors.append(f"expected {PORTFOLIO_ROWS} evidence rows, found {len(evidence_rows)}")

    lineage_counts = Counter(row["lineage_id"] for row in rows)
    if lineage_counts != Counter(EXPECTED_LINEAGE_COUNTS):
        errors.append(f"lineage counts mismatch: {dict(sorted(lineage_counts.items()))}")

    record_counts = Counter(row["record_type"] for row in rows)
    if record_counts != Counter(EXPECTED_RECORD_COUNTS):
        errors.append(f"record counts mismatch: {dict(sorted(record_counts.items()))}")

    for field in ("slot_id", "formal_code", "working_name_en", "working_name_ko"):
        repeated = duplicates([row[field] for row in rows])
        if repeated:
            errors.append(f"duplicate {field}: {sorted(repeated)}")

    repeated_evidence = duplicates([row["slot_id"] for row in evidence_rows])
    if repeated_evidence:
        errors.append(f"duplicate evidence slot_id: {sorted(repeated_evidence)}")

    expected_slots = [f"M-{number:03d}" for number in range(1, PORTFOLIO_ROWS + 1)]
    actual_slots = [row["slot_id"] for row in rows]
    if actual_slots != expected_slots:
        errors.append(f"slot ids must be ordered M-001 through M-{PORTFOLIO_ROWS:03d}")

    evidence_by_slot = {row["slot_id"]: row for row in evidence_rows}
    if set(evidence_by_slot) != set(actual_slots):
        errors.append("evidence coverage does not match portfolio slots")

    working_names = {row["working_name_en"].upper() for row in rows}

    for row in rows:
        slot = row["slot_id"]
        record_type = row["record_type"]
        evidence = evidence_by_slot.get(slot)
        if evidence is None:
            errors.append(f"{slot}: missing evidence row")
            continue

        if row["canon_status"] not in ALLOWED_STATUSES:
            errors.append(f"{slot}: invalid canon_status {row['canon_status']}")
        if row["canon_basis_type"] not in ALLOWED_BASIS_TYPES:
            errors.append(f"{slot}: invalid canon_basis_type {row['canon_basis_type']}")
        if row["canon_promotion"] != "NONE":
            errors.append(f"{slot}: canon_promotion must remain NONE")
        if not row["name_clearance"]:
            errors.append(f"{slot}: name clearance state is required")

        basis_line, basis_error = source_line(row["canon_basis_ref"])
        if basis_error:
            errors.append(f"{slot}: canon basis {basis_error}")
        elif evidence["basis_quote_token"].casefold() not in basis_line.casefold():
            errors.append(f"{slot}: canon basis quote token missing from cited line")
        if not evidence["basis_support_scope"]:
            errors.append(f"{slot}: basis_support_scope is required")

        public_name = row["working_name_en"].upper()
        rejected = contains_rejected_term(public_name, rejected_terms)
        if rejected:
            errors.append(f"{slot}: hard-reject name token(s) {rejected}")
        if public_name in PROTECTED_CANON_TERMS:
            errors.append(f"{slot}: working name collides with protected canon term")

        synergy_name_tokens = {
            token
            for token in re.findall(r"\b[A-Z][A-Z0-9-]{3,}\b", row["synergy_partner"])
            if token not in {"HOLD"}
        }
        unknown_synergy_names = sorted(synergy_name_tokens - working_names)
        if unknown_synergy_names:
            errors.append(
                f"{slot}: unresolved synergy machine name(s) {unknown_synergy_names}"
            )

        if record_type in {"VERIFIED_ENTITY", "CHASSIS_SLOT"}:
            for field in COLLECTION_FIELDS | LOGISTICS_FIELDS:
                if not row[field] or row[field] == "HOLD":
                    errors.append(f"{slot}: placed record requires {field}")
            if row["tech_basis"].startswith("HOLD_NEW_TECH"):
                errors.append(f"{slot}: placed record cannot depend on unapproved new tech")
            if evidence["tech_basis_ref"] == "HOLD":
                errors.append(f"{slot}: placed record requires a technical basis reference")
            else:
                tech_line, tech_error = source_line(evidence["tech_basis_ref"])
                if tech_error:
                    errors.append(f"{slot}: technical basis {tech_error}")
                elif evidence["tech_quote_token"].casefold() not in tech_line.casefold():
                    errors.append(f"{slot}: technical basis quote token missing from cited line")
            if not evidence["tech_support_scope"]:
                errors.append(f"{slot}: tech_support_scope is required")

        if record_type == "CHASSIS_SLOT":
            changed_systems = set(row["major_system_changes"].split("|"))
            if row["chassis_evidence"] != "PROPOSED_NEW_LOAD_FRAME":
                errors.append(f"{slot}: chassis slot requires proposed load-frame evidence")
            if "LOAD_FRAME" not in changed_systems or len(changed_systems) < 3:
                errors.append(
                    f"{slot}: chassis slot requires LOAD_FRAME plus two major-system changes"
                )
            unknown_systems = sorted(changed_systems - ALLOWED_MAJOR_SYSTEMS)
            if unknown_systems:
                errors.append(f"{slot}: unknown major-system change token(s) {unknown_systems}")
            if row["canon_status"] == "CANON_ENTITY":
                errors.append(f"{slot}: proposed chassis slot cannot be CANON_ENTITY")

        if record_type == "RESERVE_SLOT":
            if row["canon_status"] != "HOLD_AUTHOR_DECISION":
                errors.append(f"{slot}: reserve must remain HOLD_AUTHOR_DECISION")
            if not row["first_reveal_window"].startswith("HOLD"):
                errors.append(f"{slot}: reserve reveal window must remain HOLD")
            if evidence["tech_basis_ref"] != "HOLD":
                errors.append(f"{slot}: reserve technical basis must remain HOLD")

    opening_rows = [row for row in rows if row["first_reveal_window"] == "E1-E20"]
    if [row["slot_id"] for row in opening_rows] != ["M-001"]:
        errors.append("E1-E20 must expose only M-001 AUX-07")

    canon_rows = [row for row in rows if row["canon_status"] == "CANON_ENTITY"]
    if [row["slot_id"] for row in canon_rows] != ["M-001"]:
        errors.append("only M-001 may be labeled CANON_ENTITY")

    first_reveal_counts = Counter(
        ga
        for row in rows
        if row["record_type"] != "RESERVE_SLOT"
        for ga in [first_reveal_ga(row["first_reveal_window"])]
        if ga is not None
    )
    actual_reveal_counts = {
        ga: first_reveal_counts.get(ga, 0) for ga in EXPECTED_FIRST_REVEAL_COUNTS
    }
    if actual_reveal_counts != EXPECTED_FIRST_REVEAL_COUNTS:
        errors.append(f"first reveal counts mismatch: {actual_reveal_counts}")

    axiom = next((row for row in rows if row["formal_code"] == "LFX-01"), None)
    if axiom is None or axiom["record_type"] != "RESERVE_SLOT":
        errors.append("LFX-01 AXIOM must exist as a reserve slot")
    elif "PUBLIC_NAME_HOLD" not in axiom["name_clearance"]:
        errors.append("AXIOM public-name hold must be explicit")

    successor_reserve = next((row for row in rows if row["slot_id"] == "M-028"), None)
    if successor_reserve is None or successor_reserve["record_type"] != "RESERVE_SLOT":
        errors.append("M-028 must remain an author-decision reserve slot")
    elif (
        successor_reserve["formal_code"] != "HOLD"
        or successor_reserve["working_name_en"] != "[UNNAMED]"
        or successor_reserve["name_clearance"] != "PUBLIC_NAME_HOLD"
        or successor_reserve["evolution_relation"] != "INHERITANCE_HOLD"
    ):
        errors.append("M-028 successor code, name and inheritance must remain HOLD")

    front_rows = [row for row in rows if row["reader_tier"] == "FRONT"]
    if not 12 <= len(front_rows) <= 14:
        errors.append(f"front-stage count must be 12-14, found {len(front_rows)}")

    active_rows = [row for row in rows if row["record_type"] != "RESERVE_SLOT"]
    for index, left_row in enumerate(active_rows):
        left_ga = ga_number(left_row["first_reveal_window"])
        if left_ga is None:
            continue
        for right_row in active_rows[index + 1 :]:
            right_ga = ga_number(right_row["first_reveal_window"])
            if right_ga is None or abs(left_ga - right_ga) > 1:
                continue

            left_en = re.sub(r"[^A-Z]", "", left_row["working_name_en"].upper())
            right_en = re.sub(r"[^A-Z]", "", right_row["working_name_en"].upper())
            if left_en and right_en:
                if left_en[:2] == right_en[:2] or left_en[-3:] == right_en[-3:]:
                    errors.append(
                        f"active-name rhythm collision: {left_en} / {right_en}"
                    )
                elif edit_distance(left_en, right_en) <= 2:
                    errors.append(
                        f"active-name edit-distance collision: {left_en} / {right_en}"
                    )

            left_ko = left_row["working_name_ko"]
            right_ko = right_row["working_name_ko"]
            if left_ko and right_ko:
                if left_ko[0] == right_ko[0] and left_ko[-1] == right_ko[-1]:
                    errors.append(
                        f"active-Korean-name rhythm collision: {left_ko} / {right_ko}"
                    )
                elif edit_distance(left_ko, right_ko) <= 1:
                    errors.append(
                        f"active-Korean-name edit-distance collision: {left_ko} / {right_ko}"
                    )

    if scan_repository_names:
        corpus = existing_markdown_corpus()
        for row in rows:
            if row["record_type"] != "CHASSIS_SLOT":
                continue
            english = row["working_name_en"].upper()
            korean = row["working_name_ko"].upper()
            if re.search(rf"(?<![A-Z0-9]){re.escape(english)}(?![A-Z0-9])", corpus):
                errors.append(f"{row['slot_id']}: English working name already appears in repository")
            if korean and korean in corpus:
                errors.append(f"{row['slot_id']}: Korean working name already appears in repository")

    return errors


def run_selftest(
    rows: list[dict[str, str]],
    evidence_rows: list[dict[str, str]],
    rejected_terms: set[str],
) -> int:
    base_errors = validate(
        rows,
        evidence_rows,
        rejected_terms,
        scan_repository_names=False,
    )
    if base_errors:
        print("MECHA LINEUP SELFTEST BLOCKED BY INVALID BASE FIXTURE", file=sys.stderr)
        for error in base_errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    fixtures: list[tuple[str, list[dict[str, str]], list[dict[str, str]], str]] = []

    def add_fixture(name: str, mutate, expected: str) -> None:
        fixture_rows = copy.deepcopy(rows)
        fixture_evidence = copy.deepcopy(evidence_rows)
        mutate(fixture_rows, fixture_evidence)
        fixtures.append((name, fixture_rows, fixture_evidence, expected))

    add_fixture(
        "duplicate slot",
        lambda fixture, _: fixture[1].update(slot_id="M-001"),
        "duplicate slot_id",
    )
    add_fixture(
        "canon promotion",
        lambda fixture, _: fixture[1].update(canon_promotion="APPROVED"),
        "canon_promotion must remain NONE",
    )
    add_fixture(
        "missing collection field",
        lambda fixture, _: fixture[1].update(acquisition_gate=""),
        "placed record requires acquisition_gate",
    )
    add_fixture(
        "false chassis",
        lambda fixture, _: fixture[1].update(major_system_changes="LOAD_FRAME|CONTROL"),
        "LOAD_FRAME plus two major-system changes",
    )
    add_fixture(
        "invented major systems",
        lambda fixture, _: fixture[1].update(major_system_changes="LOAD_FRAME|BANANA|POTATO"),
        "unknown major-system change token",
    )
    add_fixture(
        "bad canon quote",
        lambda _, evidence: evidence[1].update(basis_quote_token="NOT ON SOURCE LINE"),
        "canon basis quote token missing",
    )
    add_fixture(
        "missing tech evidence",
        lambda _, evidence: evidence[1].update(tech_basis_ref="HOLD"),
        "placed record requires a technical basis reference",
    )
    add_fixture(
        "protected canon name",
        lambda fixture, _: fixture[1].update(working_name_en="TALREN"),
        "protected canon term",
    )
    add_fixture(
        "adjacent GA name collision",
        lambda fixture, _: fixture[10].update(
            working_name_en=fixture[5]["working_name_en"],
            working_name_ko=fixture[5]["working_name_ko"],
        ),
        "active-name",
    )
    add_fixture(
        "opening overload",
        lambda fixture, _: fixture[1].update(first_reveal_window="E1-E20"),
        "E1-E20 must expose only",
    )
    add_fixture(
        "reserve promotion",
        lambda fixture, _: fixture[26].update(record_type="CHASSIS_SLOT"),
        "record counts mismatch",
    )
    add_fixture(
        "premature successor identity",
        lambda fixture, _: fixture[27].update(
            formal_code="LFX-02",
            working_name_en="VECTIS",
            evolution_relation="INHERIT_AXIOM",
        ),
        "successor code, name and inheritance must remain HOLD",
    )
    add_fixture(
        "hard reject source",
        lambda fixture, _: fixture[1].update(working_name_en="PRIME"),
        "hard-reject name token",
    )
    add_fixture(
        "compact MK-II hard reject",
        lambda fixture, _: fixture[1].update(working_name_en="SOLVERN MKII"),
        "hard-reject name token",
    )
    add_fixture(
        "compact EX-S hard reject",
        lambda fixture, _: fixture[1].update(working_name_en="SOLVERN EXS"),
        "hard-reject name token",
    )
    add_fixture(
        "missing evidence row",
        lambda _, evidence: evidence.pop(1),
        "evidence rows",
    )
    add_fixture(
        "unresolved synergy name",
        lambda fixture, _: fixture[4].update(
            synergy_partner="NEVRIS recon|GHOSTER command"
        ),
        "unresolved synergy machine name",
    )

    failures: list[str] = []
    for name, fixture_rows, fixture_evidence, expected in fixtures:
        fixture_errors = validate(
            fixture_rows,
            fixture_evidence,
            rejected_terms,
            scan_repository_names=False,
        )
        if not any(expected in error for error in fixture_errors):
            failures.append(f"{name}: expected error containing {expected!r}")

    if failures:
        print("MECHA LINEUP SELFTEST FAILED", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("MECHA LINEUP SELFTEST PASSED")
    print(f"- defect fixtures fired: {len(fixtures)}")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) > 1 or (argv and argv[0] != "--selftest"):
        print("usage: validate_mecha_lineup.py [--selftest]", file=sys.stderr)
        return 2

    try:
        rows = read_csv(INDEX_FILE)
        evidence_rows = read_csv(EVIDENCE_FILE)
        rejected_terms = read_hard_reject_names()
    except FileNotFoundError as exc:
        print(f"missing mecha lineup input: {exc}", file=sys.stderr)
        return 1

    if argv == ["--selftest"]:
        return run_selftest(rows, evidence_rows, rejected_terms)

    errors = validate(
        rows,
        evidence_rows,
        rejected_terms,
        scan_repository_names=True,
    )
    if errors:
        print("MECHA LINEUP VALIDATION FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    lineage_counts = Counter(row["lineage_id"] for row in rows)
    front_count = sum(row["reader_tier"] == "FRONT" for row in rows)
    print("MECHA LINEUP VALIDATION PASSED")
    print("- verified canon entities: 1")
    print("- phase-1 noncanon placed sample slots: 43")
    print("- phase-1 author-decision sample reserves: 2")
    print(f"- manufacturing lineages: {len(lineage_counts)}")
    print(f"- phase-1 front-stage sample candidates: {front_count}")
    print("- reuse-first process preferred; Direction C 40-48 selected per D-20260813-03; independent-model count HOLD")
    print("- canon and technical quote tokens: matched")
    print("- adjacent-GA English/Korean name distance: passed")
    print("- E1-E20 principal-frame limit: AUX-07 only")
    print("- per-slot chassis/logistics/collection fields: present")
    print("- synergy machine-name references: resolved")
    print("- canon promotions: none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
