#!/usr/bin/env python3
"""Semantic set-family finalizer for the collection desire layer.

The first deterministic classifier intentionally favored EVENT whenever broad
words like record/war/history appeared. That is too shallow for final reader-
desire routing: relationship, functional and civilization completion can occur
inside an event-heavy act without becoming an Event Set.

This pass scores the five already-canonical Collection Bible set families from
the approved subact text and domain/kind evidence. It creates no new set family
or story fact.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

import build_full_series_collection_desire_layer as layer
import finalize_full_series_collection_desire_layer_strict as strict

ROOT = Path(__file__).resolve().parents[1]
SET_AUDIT = ROOT / "docs" / "99_quality_control" / "full-series-collection-set-family-semantic-balance-audit-v1.md"

FAMILIES = ("LINEAGE", "EVENT", "FUNCTIONAL", "RELATIONSHIP", "CIVILIZATION")

KEYWORDS = {
    "LINEAGE": (
        "lineage", "origin", "original", "ancestry", "design family", "service spine",
        "legacy object", "prototype", "authorship", "계보", "기원", "원형",
    ),
    "EVENT": (
        "evidence", "testimony", "inquiry", "verdict", "trial", "incident", "case",
        "investigation", "attack", "battle", "war", "crisis", "history", "record",
        "증거", "증언", "조사", "판결", "사건", "전투", "전쟁", "위기", "역사",
    ),
    "FUNCTIONAL": (
        "frame", "ship", "module", "weapon", "repair", "mission", "tool", "standard",
        "technical", "medical", "certifier", "workshop", "fleet", "service function",
        "기체", "함선", "모듈", "무기", "수리", "임무", "표준", "기술", "의료",
    ),
    "RELATIONSHIP": (
        "trust", "consent", "crew", "community", "ally", "rival", "relationship",
        "coalition", "representative", "patient", "worker", "family", "refusal", "care",
        "신뢰", "동의", "승무원", "공동체", "동맹", "경쟁", "관계", "대표", "환자", "노동자", "가족", "거절",
    ),
    "CIVILIZATION": (
        "region", "node", "city", "federation", "settlement", "civilization", "territory",
        "autonomy", "migration", "jurisdiction", "handoff", "reconstruction", "institution",
        "corridor", "route federation", "current-status", "지역", "노드", "도시", "연방", "정착", "문명", "영토", "자치", "이주", "재건",
    ),
}


def count_hits(low: str, words: tuple[str, ...]) -> int:
    return sum(1 for word in words if word in low)


def infer_set_types_semantic(domains: list[str], text: str, kinds: list[str]) -> list[str]:
    low = re.sub(r"\s+", " ", text.casefold())
    scores = Counter({family: 0 for family in FAMILIES})

    # Domain priors: the target domain says what kind of completion the reader
    # is tracking; event vocabulary alone must not erase it.
    if "C1" in domains:
        scores["RELATIONSHIP"] += 4
    if any(domain in domains for domain in ("C2", "C3", "C5", "C6")):
        scores["FUNCTIONAL"] += 4
    if "C8" in domains:
        scores["CIVILIZATION"] += 5
    if "C7" in domains:
        scores["CIVILIZATION"] += 2
        scores["RELATIONSHIP"] += 1
    if "C4" in domains:
        scores["EVENT"] += 2
        scores["LINEAGE"] += 1

    if "RELATIONSHIP" in kinds:
        scores["RELATIONSHIP"] += 3
    if any(kind in kinds for kind in ("CONTROL_CLAIM", "STATE_TRANSITION")):
        scores["CIVILIZATION"] += 1
    if "ENTITY" in kinds and any(domain in domains for domain in ("C2", "C3", "C5", "C6")):
        scores["FUNCTIONAL"] += 1

    # Keyword evidence. Relationship/civilization/functional words are more
    # discriminating than generic event words and therefore receive larger
    # weights. EVENT remains available for genuinely evidence/incident-driven
    # sets rather than functioning as a default sink.
    scores["LINEAGE"] += min(12, 4 * count_hits(low, KEYWORDS["LINEAGE"]))
    scores["EVENT"] += min(10, 2 * count_hits(low, KEYWORDS["EVENT"]))
    scores["FUNCTIONAL"] += min(15, 3 * count_hits(low, KEYWORDS["FUNCTIONAL"]))
    scores["RELATIONSHIP"] += min(15, 3 * count_hits(low, KEYWORDS["RELATIONSHIP"]))
    scores["CIVILIZATION"] += min(18, 3 * count_hits(low, KEYWORDS["CIVILIZATION"]))

    # Strong explicit cues.
    if any(term in low for term in ("lineage", "origin", "original frame", "service spine", "계보")):
        scores["LINEAGE"] += 5
    if any(term in low for term in ("testimony", "verdict", "inquiry", "evidence chain", "증언", "판결")):
        scores["EVENT"] += 5
    if any(term in low for term in ("repair", "mission configuration", "technical commons", "medical commons", "수리", "기술")):
        scores["FUNCTIONAL"] += 4
    if any(term in low for term in ("trust", "consent", "relationship", "crew institution", "신뢰", "동의", "관계")):
        scores["RELATIONSHIP"] += 5
    if any(term in low for term in ("autonomy", "federation", "regional", "reconstruction", "migration", "자치", "연방", "재건")):
        scores["CIVILIZATION"] += 5

    if not any(scores.values()):
        scores["EVENT"] = 1

    tie_priority = {
        "RELATIONSHIP": 5,
        "CIVILIZATION": 4,
        "FUNCTIONAL": 3,
        "LINEAGE": 2,
        "EVENT": 1,
    }
    ordered = sorted(FAMILIES, key=lambda family: (-scores[family], -tie_priority[family], FAMILIES.index(family)))
    positive = [family for family in ordered if scores[family] > 0]
    return positive or ["EVENT"]


def parse_primary_maps(outputs: dict[Path, str]) -> tuple[Counter[str], dict[str, list[str]]]:
    counts: Counter[str] = Counter()
    sequences: dict[str, list[str]] = {}
    for path, text in outputs.items():
        if not path.name.endswith("-collection-desire-subact-map-v1.md"):
            continue
        arc_match = re.match(r"(ga\d+)-", path.name)
        if not arc_match:
            continue
        arc = arc_match.group(1).upper()
        sequence: list[str] = []
        for match in re.finditer(r"^- `PRIMARY_SET_TYPE`: `([A-Z]+)`", text, flags=re.MULTILINE):
            family = match.group(1)
            counts[family] += 1
            sequence.append(family)
        sequences[arc] = sequence
    return counts, sequences


def longest_run(sequence: list[str]) -> tuple[str, int]:
    best_family = ""
    best = 0
    current_family = ""
    current = 0
    for family in sequence:
        if family == current_family:
            current += 1
        else:
            current_family = family
            current = 1
        if current > best:
            best_family = family
            best = current
    return best_family, best


def set_audit_text(outputs: dict[Path, str]) -> str:
    counts, sequences = parse_primary_maps(outputs)
    total = sum(counts.values())
    missing_families = [family for family in FAMILIES if counts[family] == 0]
    dominant_family, dominant_count = (counts.most_common(1)[0] if counts else ("NONE", 0))
    dominant_share = dominant_count / total if total else 1.0
    runs = {arc: longest_run(sequence) for arc, sequence in sequences.items()}
    max_run_arc, (max_run_family, max_run) = max(runs.items(), key=lambda item: item[1][1]) if runs else ("NONE", ("NONE", 0))

    # Completion requires all five canonical set families to be genuinely usable
    # as primary reader frames. A single family occupying >75% indicates the
    # classifier is still collapsing distinct desires into one bucket.
    fail = bool(total != 160 or missing_families or dominant_share > 0.75 or max_run > 12)
    verdict = "FAIL" if fail else "PASS"
    lines = [
        "# Full-Series Collection Set-Family Semantic Balance Audit v1",
        "",
        f"Status: {verdict} — EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        f"> **{verdict} — five canonical Collection Bible set families remain semantically distinct at subact level.**",
        "",
        "## Primary Set Distribution",
        "",
    ]
    for family in FAMILIES:
        lines.append(f"- {family}: **{counts[family]}**")
    lines.extend(
        [
            "",
            f"- dominant family: `{dominant_family}` = **{dominant_count}/{total} ({dominant_share:.1%})**",
            f"- missing primary families: **{', '.join(missing_families) if missing_families else 'NONE'}**",
            f"- longest same-primary run: **{max_run}** (`{max_run_arc}` / `{max_run_family}`)",
            "",
            "## Per-GA Longest Runs",
            "",
        ]
    )
    for arc in sorted(runs, key=lambda value: int(value[2:])):
        family, count = runs[arc]
        lines.append(f"- {arc}: `{family}` x **{count}**")
    lines.extend(
        [
            "",
            "## Ruling",
            "",
            "- all five set families appear as primary reader frames: **" + ("PASS" if not missing_families else "FAIL") + "**",
            "- no one family exceeds 75% of all subacts: **" + ("PASS" if dominant_share <= 0.75 else "FAIL") + "**",
            "- no same-primary run exceeds 12 subacts: **" + ("PASS" if max_run <= 12 else "FAIL") + "**",
            "- this classifier changes workflow grouping only; it does not alter act events, ownership, payoff timing or story canon: **ENFORCED**",
            "- new story canon required: **0**",
            "",
        ]
    )
    return "\n".join(lines)


def build_outputs() -> dict[Path, str]:
    layer.infer_set_types = infer_set_types_semantic
    outputs = strict.build_outputs()
    outputs[SET_AUDIT] = set_audit_text(outputs)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    outputs = build_outputs()
    layer.write_or_check(outputs, args.check)
    text = outputs[SET_AUDIT]
    if "Status: PASS — EXECUTION QC" not in text:
        print(text)
        raise SystemExit("COLLECTION SET-FAMILY SEMANTIC BALANCE GATE FAIL")
    print("collection_set_family_semantic_balance=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
