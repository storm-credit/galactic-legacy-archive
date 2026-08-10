#!/usr/bin/env python3
"""Build the noncanon collection-registry normalization index.

The source registries remain untouched. This tool preserves every source heading,
reuses the reviewed dry-run classifications where available, and marks all other
classifications as provisional until a domain specialist reviews them.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COLLECTION_DIR = ROOT / "docs" / "09_collection"
DATA_DIR = COLLECTION_DIR / "data"

REGISTRIES = [
    ("GA1", "first-100-collectible-registry-v1.md", 42),
    ("GA2", "ga2-collection-registry-v1.md", 45),
    ("GA3", "ga3-collection-registry-v1.md", 43),
    ("GA4", "ga4-collection-registry-v1.md", 40),
    ("GA5", "ga5-collection-registry-v1.md", 45),
    ("GA6", "ga6-collection-registry-v1.md", 40),
    ("GA7", "ga7-collection-registry-v1.md", 39),
    ("GA8", "ga8-collection-registry-v1.md", 36),
    ("GA9", "ga9-collection-registry-v1.md", 31),
    ("GA10", "ga10-final-collection-and-payoff-registry-v1.md", 54),
]

SOURCE_OUTPUT = DATA_DIR / "collection-normalization-full-source-rows-v1.csv"
EXPANDED_OUTPUT = DATA_DIR / "collection-normalization-full-expanded-records-v1.csv"
DRY_RUN_SOURCE = DATA_DIR / "collection-normalization-dry-run-source-rows-v1.csv"

ALLOWED_KINDS = {
    "ENTITY",
    "RELATIONSHIP",
    "CONTROL_CLAIM",
    "STATE_TRANSITION",
    "LOSS_OBLIGATION",
    "NARRATIVE_PROMISE",
    "SET",
}
KIND_ORDER = (
    "ENTITY",
    "RELATIONSHIP",
    "CONTROL_CLAIM",
    "STATE_TRANSITION",
    "LOSS_OBLIGATION",
    "NARRATIVE_PROMISE",
    "SET",
)
ALLOWED_DOMAINS = {f"C{i}" for i in range(1, 9)}

DOMAIN_TERMS = {
    "C1": (
        "person", "people", "cadet", "admiral", "commander", "captain",
        "engineer", "pilot", "officer", "leader", "delegate", "witness",
        "worker", "crew", "resident", "heir", "regent", "protector",
        "relationship", "survivor", "citizen",
    ),
    "C2": (
        "maneuver frame", "frame", "aux-07", "07호", "chassis", "cockpit",
        "combat configuration", "armor shell", "service frame",
    ),
    "C3": (
        "weapon", "module", "tool", "cutter", "carbine", "missile", "gun",
        "sword", "shield", "decoy", "countermeasure", "armament", "ammunition",
        "sensor package", "capture package",
    ),
    "C4": (
        "relic", "treasure", "artifact", "provenance", "memorial", "symbol",
        "archive fragment", "record fragment", "memory fragment", "forgery",
        "key", "log", "mirror", "seal", "insignia", "public story", "myth",
    ),
    "C5": (
        "ship", "hull", "vessel", "carrier", "destroyer", "flagship",
        "tender", "convoy", "fleet escort", "ghost ship", "life support",
    ),
    "C6": (
        "technology", "standard", "protocol", "system", "process", "design",
        "reactor", "engine", "calibration", "algorithm", "network", "tooling",
        "interoperability", "authentication", "infrastructure", "repair",
    ),
    "C7": (
        "institution", "authority", "council", "charter", "command", "office",
        "coalition", "federation", "directorate", "compact", "regime", "mandate",
        "legitimacy", "license", "law", "right", "claim", "governance",
        "assembly", "administration", "state", "custody", "succession",
    ),
    "C8": (
        "territory", "node", "route", "region", "world", "planet", "colony",
        "settlement", "corridor", "passage", "dock", "yard", "habitat",
        "civilization", "city", "community", "province", "system access",
    ),
}

SECTION_HINTS = {
    "People": "C1",
    "Relationship": "C1",
    "Frame": "C2",
    "Tools": "C3",
    "Module": "C3",
    "Relic": "C4",
    "Symbolic": "C4",
    "Ship": "C5",
    "Hull": "C5",
    "Technology": "C6",
    "Standard": "C6",
    "Institution": "C7",
    "Authority": "C7",
    "Governance": "C7",
    "Legal": "C7",
    "Territory": "C8",
    "Node": "C8",
    "Route": "C8",
    "Civilization": "C8",
}

# Specialist-reviewed source-level corrections. These do not assign entity IDs
# or promote canon; they only prevent support facilities from counting as frames.
DOMAIN_OVERRIDES = {
    "docs/09_collection/ga2-collection-registry-v1.md#G2-S06": ["C5", "C2"],
    "docs/09_collection/ga3-collection-registry-v1.md#G3-P09": ["C1", "C2"],
    "docs/09_collection/ga3-collection-registry-v1.md#G3-D02": ["C6", "C2"],
    "docs/09_collection/ga3-collection-registry-v1.md#G3-D04": ["C6", "C2"],
    "docs/09_collection/ga3-collection-registry-v1.md#G3-N03": ["C8", "C6"],
    "docs/09_collection/ga5-collection-registry-v1.md#G5-C03": ["C7"],
    "docs/09_collection/ga5-collection-registry-v1.md#G5-L02": ["C5", "C6"],
    "docs/09_collection/ga5-collection-registry-v1.md#G5-F06": ["C5", "C7"],
    "docs/09_collection/ga5-collection-registry-v1.md#G5-C02": ["C5", "C7"],
    "docs/09_collection/ga6-collection-registry-v1.md#G6-P06": ["C1", "C7", "C8"],
    "docs/09_collection/ga6-collection-registry-v1.md#G6-P07": ["C1", "C7", "C5"],
    "docs/09_collection/ga6-collection-registry-v1.md#G6-P08": ["C1", "C7"],
    "docs/09_collection/ga9-collection-registry-v1.md#G9-P07": ["C1", "C7"],
    "docs/09_collection/ga9-collection-registry-v1.md#G9-A06": ["C6"],
}

ENTITY_TERMS = (
    *DOMAIN_TERMS["C1"],
    *DOMAIN_TERMS["C2"],
    *DOMAIN_TERMS["C3"],
    *DOMAIN_TERMS["C4"],
    *DOMAIN_TERMS["C5"],
    "technology", "specification", "profile", "relay", "standard", "process",
    "council", "coalition", "federation", "directorate", "assembly",
    "administration", "institution", "office", "network",
    *DOMAIN_TERMS["C8"],
)

KIND_ADD_OVERRIDES = {
    "docs/09_collection/ga5-collection-registry-v1.md#G5-L02": ["ENTITY"],
    "docs/09_collection/ga6-collection-registry-v1.md#G6-P06": ["ENTITY", "RELATIONSHIP"],
    "docs/09_collection/ga6-collection-registry-v1.md#G6-P07": ["ENTITY", "RELATIONSHIP"],
    "docs/09_collection/ga6-collection-registry-v1.md#G6-P08": ["ENTITY", "RELATIONSHIP"],
    "docs/09_collection/ga9-collection-registry-v1.md#G9-P07": ["ENTITY", "RELATIONSHIP"],
    "docs/09_collection/ga6-collection-registry-v1.md#G6-A06": ["SET"],
    "docs/09_collection/ga7-collection-registry-v1.md#G7-A02": ["SET"],
    "docs/09_collection/ga3-collection-registry-v1.md#G3-R01": ["CONTROL_CLAIM"],
    "docs/09_collection/ga3-collection-registry-v1.md#G3-R03": ["CONTROL_CLAIM"],
    "docs/09_collection/ga3-collection-registry-v1.md#G3-R08": ["CONTROL_CLAIM"],
}
KIND_REMOVE_OVERRIDES = {
    "docs/09_collection/ga2-collection-registry-v1.md#G2-S02": ["ENTITY"],
    "docs/09_collection/ga2-collection-registry-v1.md#G2-S14": ["ENTITY", "RELATIONSHIP"],
    "docs/09_collection/ga5-collection-registry-v1.md#G5-C02": ["ENTITY"],
    "docs/09_collection/ga6-collection-registry-v1.md#G6-R06": ["ENTITY"],
    "docs/09_collection/ga7-collection-registry-v1.md#G7-I02": ["ENTITY"],
    "docs/09_collection/ga9-collection-registry-v1.md#G9-M04": ["ENTITY"],
    "docs/09_collection/ga6-collection-registry-v1.md#G6-A06": ["ENTITY"],
    "docs/09_collection/ga7-collection-registry-v1.md#G7-A02": ["ENTITY"],
}
RELATIONSHIP_TERMS = (
    "relationship", "alliance", "trust", "crew", "leader", "delegate",
    "representative", "coalition", "compact", "community", "citizen",
)
CLAIM_TERMS = (
    "right", "claim", "authority", "license", "charter", "mandate", "custody",
    "access", "title", "control", "record", "evidence", "authentication",
    "consent", "succession", "command", "protocol", "standard",
)
PROMISE_TERMS = (
    "future", "myth", "mystery", "payoff", "promise", "question", "origin",
    "principle", "narrative", "story", "identity", "precedent", "bridge",
)
SET_TERMS = (" set", "constellation", "lineage", "chain", "portfolio")


def contains(text: str, terms: tuple[str, ...]) -> bool:
    lowered = text.casefold()
    return any(
        re.search(
            rf"(?<![a-z0-9]){re.escape(term.casefold())}(?![a-z0-9])",
            lowered,
        )
        for term in terms
    )


def flatten(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def labelled(block: str, labels: tuple[str, ...]) -> str:
    lines = block.splitlines()
    captured: list[str] = []
    active = False
    for line in lines:
        stripped = line.strip()
        label_match = re.match(r"^([A-Za-z][A-Za-z0-9 /+&-]{1,48}):\s*(.*)$", stripped)
        if label_match:
            active = label_match.group(1).casefold() in {label.casefold() for label in labels}
            if active and label_match.group(2):
                captured.append(label_match.group(2))
            continue
        if active:
            if stripped.startswith("-"):
                captured.append(stripped[1:].strip())
            elif stripped:
                captured.append(stripped)
    return flatten(" ".join(captured))


def reviewed_dry_run() -> dict[str, dict[str, str]]:
    if not DRY_RUN_SOURCE.exists():
        return {}
    with DRY_RUN_SOURCE.open("r", encoding="utf-8-sig", newline="") as handle:
        return {row["source_key"]: row for row in csv.DictReader(handle)}


def parse_registry(arc: str, filename: str) -> list[dict[str, str]]:
    path = COLLECTION_DIR / filename
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    records: list[dict[str, str]] = []
    section = ""
    index = 0
    while index < len(lines):
        section_match = re.match(r"^#\s+[A-E]\.\s+(.+)$", lines[index])
        if section_match:
            section = section_match.group(1).strip()
            index += 1
            continue
        heading = re.match(r"^##\s+([A-Z0-9-]+)\s+—\s+(.+)$", lines[index])
        if not heading:
            index += 1
            continue
        source_line = index + 1
        source_id, title = heading.groups()
        body_start = index + 1
        index += 1
        while index < len(lines) and not re.match(r"^#{1,2}\s+", lines[index]):
            index += 1
        block = "\n".join(lines[body_start:index]).strip()
        relative = path.relative_to(ROOT).as_posix()
        records.append(
            {
                "source_key": f"{relative}#{source_id}",
                "source_file": relative,
                "source_line": str(source_line),
                "arc": arc,
                "section": section,
                "source_id": source_id,
                "title": title.strip(),
                "block": block,
            }
        )
    return records


def classify_domains(
    title: str,
    section: str,
    block: str,
    *,
    fallback: bool = True,
) -> list[str]:
    scores: Counter[str] = Counter()
    for domain, terms in DOMAIN_TERMS.items():
        for term in terms:
            if contains(title, (term,)):
                scores[domain] += 4
            if contains(block, (term,)):
                scores[domain] += 1
    for phrase, domain in SECTION_HINTS.items():
        if contains(section, (phrase,)):
            scores[domain] += 3
    if not scores:
        return ["C7"] if fallback else []
    maximum = max(scores.values())
    selected = [
        domain
        for domain, score in sorted(scores.items())
        if score >= 3 and score >= maximum - 3
    ]
    return selected[:4] or [scores.most_common(1)[0][0]]


def classify_kinds(title: str, section: str, block: str) -> list[str]:
    heading_context = f"{title}\n{section}"
    kinds: list[str] = []
    if contains(title, ENTITY_TERMS):
        kinds.append("ENTITY")
    if contains(heading_context, RELATIONSHIP_TERMS):
        kinds.append("RELATIONSHIP")
    if contains(heading_context, CLAIM_TERMS) or re.search(
        r"(?im)^(Acquire|Connection|Claim|Access):.*\b(custody|right|license|authority|claim|access)\b",
        block,
    ):
        kinds.append("CONTROL_CLAIM")
    if re.search(
        r"(?im)^(?:E(?:100|210|330|450|570|690|800|900|1000|1100)(?: target(?: state)?)?|State|Final|Final state|End state|Possible final state):",
        block,
    ) or re.search(r"`[TICGLR](?:\s|\b|—)", block):
        kinds.append("STATE_TRANSITION")
    if re.search(r"(?im)^(Cost|Loss|Exit|Failure|Risk|Burden|Sacrifice):", block):
        kinds.append("LOSS_OBLIGATION")
    if contains(heading_context, PROMISE_TERMS) or "Mystery" in section or "Payoff" in section:
        kinds.append("NARRATIVE_PROMISE")
    if contains(f" {heading_context}", SET_TERMS):
        kinds.append("SET")
    if not kinds:
        kinds.append("NARRATIVE_PROMISE")
    return [kind for kind in KIND_ORDER if kind in kinds]


def record_domains(kind: str, source_domains: list[str], title: str) -> list[str]:
    """Prevent source-level cross-domain tags from leaking into every split record."""
    primary = source_domains[0]
    if kind == "ENTITY":
        title_domains = classify_domains(title, "", "", fallback=False)
        matched = [domain for domain in title_domains if domain in source_domains]
        return [primary] + [domain for domain in matched if domain != primary]
    if kind == "RELATIONSHIP":
        anchors = [domain for domain in ("C1", "C7") if domain in source_domains]
        targets = [domain for domain in source_domains if domain not in {"C1", "C7"}]
        return anchors + targets or ["C7"]
    if kind == "CONTROL_CLAIM":
        return source_domains
    return source_domains


def host_candidate(source_file: str, source_id: str) -> str:
    if source_file.endswith("first-100-collectible-registry-v1.md"):
        match = re.fullmatch(r"F-(\d{3})", source_id)
        if match and 1 <= int(match.group(1)) <= 9:
            return "CANON:AUX-07"
    return "UNKNOWN"


def record_specs(
    source_key: str,
    kinds: list[str],
    domains: list[str],
    title: str,
) -> list[tuple[str, list[str], str]]:
    specs = [(kind, record_domains(kind, domains, title), "UNRESOLVED") for kind in kinds]
    if source_key.endswith("ga10-final-collection-and-payoff-registry-v1.md#G10-L07"):
        revised: list[tuple[str, list[str], str]] = []
        for kind, split_domains, slot in specs:
            if kind == "ENTITY":
                revised.append((kind, ["C2"], "CANON:AUX-07"))
                revised.append((kind, ["C6"], "OPEN_SERVICE_SPINE"))
            else:
                revised.append((kind, split_domains, slot))
        return revised
    return specs


def classify_desires(block: str, title: str, section: str) -> list[str]:
    full = f"{title}\n{section}\n{block}".casefold()
    phases: list[str] = []
    if any(term in full for term in ("tease", "trace", "rumor", "mystery", "identify", "reveal")):
        phases.append("DISCOVERY")
    if any(term in full for term in ("connection", "claim", "acquisition", "access", "custody", "license", "agreement")):
        phases.append("ACQUISITION")
    if any(term in full for term in ("integration", "use", "operation", "service", "coordination", "combination")):
        phases.append("SYNERGY")
    if any(term in full for term in ("target", "final", "legacy", "payoff", "end state", "e1100", "principle")):
        phases.append("COMPLETION_LEGACY")
    return phases or ["DISCOVERY"]


def main() -> int:
    reviewed = reviewed_dry_run()
    source_rows: list[dict[str, str]] = []
    expanded_rows: list[dict[str, str]] = []
    per_file: Counter[str] = Counter()
    next_record = 1

    for arc, filename, expected in REGISTRIES:
        parsed = parse_registry(arc, filename)
        if len(parsed) != expected:
            raise SystemExit(f"{filename}: expected {expected} entries, found {len(parsed)}")
        per_file[filename] = len(parsed)
        for parsed_row in parsed:
            source_number = len(source_rows) + 1
            source_row_id = f"NC-CL-S-{source_number:06d}"
            key = parsed_row["source_key"]
            review = reviewed.get(key)
            if review:
                domains = review["domain_tags"].split("|")
                kinds = review["entry_kinds"].split("|")
                reason = review["reason"]
                basis = "DRY_RUN_REVIEWED"
                flags = "PM_MERGE_REQUIRED"
            else:
                domains = classify_domains(parsed_row["title"], parsed_row["section"], parsed_row["block"])
                kinds = classify_kinds(parsed_row["title"], parsed_row["section"], parsed_row["block"])
                reason = "Automated provisional split; category-agent and PM semantic review required"
                basis = "HEURISTIC_PROVISIONAL"
                flags = "CATEGORY_REVIEW_REQUIRED|ENTITY_MERGE_REQUIRED"

            if key in DOMAIN_OVERRIDES:
                domains = DOMAIN_OVERRIDES[key]
                basis = "SPECIALIST_CORRECTED"
                flags = "PM_MERGE_REQUIRED|ENTITY_MERGE_REQUIRED"

            for kind in KIND_ADD_OVERRIDES.get(key, []):
                if kind not in kinds:
                    kinds.append(kind)
            for kind in KIND_REMOVE_OVERRIDES.get(key, []):
                if kind in kinds:
                    kinds.remove(kind)
            kinds = [kind for kind in KIND_ORDER if kind in kinds]

            if not set(domains) <= ALLOWED_DOMAINS:
                raise SystemExit(f"{key}: invalid domain tags {domains}")
            if not set(kinds) <= ALLOWED_KINDS:
                raise SystemExit(f"{key}: invalid entry kinds {kinds}")

            desires = classify_desires(parsed_row["block"], parsed_row["title"], parsed_row["section"])
            entry_ids: list[str] = []
            for kind, split_domains, subject_slot in record_specs(
                key, kinds, domains, parsed_row["title"]
            ):
                entry_id = f"NC-CL-R-{next_record:06d}"
                next_record += 1
                entry_ids.append(entry_id)
                expanded_rows.append(
                    {
                        "entry_id": entry_id,
                        "source_row_id": source_row_id,
                        "source_key": key,
                        "source_file": parsed_row["source_file"],
                        "source_line": parsed_row["source_line"],
                        "arc": parsed_row["arc"],
                        "section": parsed_row["section"],
                        "source_id": parsed_row["source_id"],
                        "title": parsed_row["title"],
                        "entry_kind": kind,
                        "primary_domain": split_domains[0],
                        "domain_tags": "|".join(split_domains),
                        "source_domain_tags": "|".join(domains),
                        "desire_phases": "|".join(desires),
                        "entity_id_candidate": "UNRESOLVED",
                        "subject_slot_candidate": subject_slot,
                        "subject_ids": "UNRESOLVED",
                        "host_id_candidate": host_candidate(parsed_row["source_file"], parsed_row["source_id"]),
                        "current_holder": "UNRESOLVED",
                        "canon_tier": "UNRESOLVED",
                        "classification_basis": basis,
                        "review_flags": flags,
                        "canon_promotion": "NONE",
                    }
                )

            block = parsed_row["block"]
            source_rows.append(
                {
                    "source_row_id": source_row_id,
                    "source_key": key,
                    "source_file": parsed_row["source_file"],
                    "source_line": parsed_row["source_line"],
                    "arc": parsed_row["arc"],
                    "section": parsed_row["section"],
                    "source_id": parsed_row["source_id"],
                    "title": parsed_row["title"],
                    "normalized_record_ids": "|".join(entry_ids),
                    "entry_kinds": "|".join(kinds),
                    "primary_domain": domains[0],
                    "domain_tags": "|".join(domains),
                    "desire_phases": "|".join(desires),
                    "record_states": "|".join(sorted(set(re.findall(r"`([TICGLR])(?:\s|\b|—)", block)))),
                    "acquisition_text": labelled(block, ("Connection", "Connection path", "Acquisition", "Acquire", "Claim", "Access", "Build")),
                    "integration_text": labelled(block, ("Integration", "Integration use", "Use", "Operation", "Function", "Build/use")),
                    "cost_text": labelled(block, ("Cost", "Burden", "Price")),
                    "loss_exit_text": labelled(block, ("Loss", "Loss/exit", "Loss/exit condition", "Loss/recovery", "Exit", "Exit/loss", "Failure", "Risk", "Sacrifice")),
                    "ending_text": labelled(block, ("E100", "E100 target state", "E210", "E210 target", "E330", "E330 target", "E450", "E570", "E690", "E690 target", "E800", "E900", "E1000", "E1100", "Target", "End State", "Final", "Final State", "Possible final state")),
                    "later_reuse_text": labelled(block, ("Later reuse", "Payoff", "Reinterpret")),
                    "entity_id_candidate": "UNRESOLVED",
                    "subject_ids": "UNRESOLVED",
                    "host_id_candidate": host_candidate(parsed_row["source_file"], parsed_row["source_id"]),
                    "current_holder": "UNRESOLVED",
                    "canon_tier": "UNRESOLVED",
                    "classification_basis": basis,
                    "classification_reason": reason,
                    "review_flags": flags,
                    "canon_promotion": "NONE",
                }
            )

    if len(source_rows) != 415:
        raise SystemExit(f"expected 415 source rows, found {len(source_rows)}")
    if len({row['source_key'] for row in source_rows}) != 415:
        raise SystemExit("duplicate source_key detected")

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for path, rows in ((SOURCE_OUTPUT, source_rows), (EXPANDED_OUTPUT, expanded_rows)):
        with path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)

    print("COLLECTION NORMALIZATION BUILD PASSED")
    print(f"- source rows: {len(source_rows)}")
    print(f"- expanded provisional records: {len(expanded_rows)}")
    print(f"- reviewed dry-run rows reused: {sum(row['classification_basis'] == 'DRY_RUN_REVIEWED' for row in source_rows)}")
    print(f"- specialist-corrected rows: {sum(row['classification_basis'] == 'SPECIALIST_CORRECTED' for row in source_rows)}")
    print(f"- heuristic rows requiring category review: {sum(row['classification_basis'] == 'HEURISTIC_PROVISIONAL' for row in source_rows)}")
    print(f"- registry counts: {dict(per_file)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
