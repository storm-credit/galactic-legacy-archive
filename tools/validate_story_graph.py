#!/usr/bin/env python3
"""Validate the Obsidian story-graph navigation layer.

This validator checks navigation structure only. It never promotes or infers story canon.
The graph layer deliberately points to authoritative source documents instead of copying
story facts into navigation hubs.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "_graph"

DOMAIN_HUBS = [
    "graph-state-characters",
    "graph-state-collection",
    "graph-state-frames",
    "graph-state-ships",
    "graph-state-weapons-parts",
    "graph-state-relics-provenance",
    "graph-state-technology",
    "graph-state-factions-institutions",
    "graph-state-places-routes",
    "graph-state-visual-memory",
    "graph-state-loss-payoff-authority",
]

ACT_LETTERS = "abcd"
WIKI_RE = re.compile(r"\[\[([^\]|#]+)")
DETAIL_PRODUCTION_INDEX = "episodes-101-1100-detail-production-standard-and-batch-map-v1"


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def wiki_targets(content: str) -> set[str]:
    return {m.group(1).strip() for m in WIKI_RE.finditer(content)}


def check_contains(errors: list[str], path: Path, targets: list[str]) -> None:
    if not path.exists():
        errors.append(f"MISSING FILE: {path.relative_to(ROOT)}")
        return
    found = wiki_targets(text(path))
    for target in targets:
        if target not in found:
            errors.append(f"MISSING LINK: {path.relative_to(ROOT)} -> [[{target}]]")


def ga_source(ga: int) -> str:
    if ga == 1:
        return "first-100-act-map-v2-consolidated"
    ranges = {
        2: "101-210",
        3: "211-330",
        4: "331-450",
        5: "451-570",
        6: "571-690",
        7: "691-800",
        8: "801-900",
        9: "901-1000",
        10: "1001-1100",
    }
    return f"ga{ga}-episodes-{ranges[ga]}-act-map-v1"


def collection_source(ga: int) -> str:
    if ga == 1:
        return "first-100-collectible-registry-v1"
    if ga == 10:
        return "ga10-final-collection-and-payoff-registry-v1"
    return f"ga{ga}-collection-registry-v1"


def ordered_subacts() -> list[str]:
    return [
        f"graph-ga{ga:02d}-subact-{a}{n}"
        for ga in range(1, 11)
        for a in ACT_LETTERS
        for n in range(1, 5)
    ]


def validate_graph_link_targets(errors: list[str]) -> None:
    """Fail when a graph note points at a wiki target that does not exist in the repo.

    This resolves either an explicit repo-relative path or a unique Markdown stem.
    Ambiguous stems are accepted because the repository's canonical wiki-link lint owns
    ambiguity detection globally; this validator only catches missing graph targets.
    """

    markdown = list(ROOT.rglob("*.md"))
    stems: dict[str, list[Path]] = {}
    for p in markdown:
        stems.setdefault(p.stem, []).append(p)

    for graph_note in GRAPH.rglob("*.md"):
        for target in wiki_targets(text(graph_note)):
            if "/" in target:
                candidate = ROOT / f"{target}.md"
                if not candidate.exists():
                    errors.append(
                        f"BROKEN PATH LINK: {graph_note.relative_to(ROOT)} -> [[{target}]]"
                    )
            elif target not in stems:
                errors.append(
                    f"BROKEN WIKI LINK: {graph_note.relative_to(ROOT)} -> [[{target}]]"
                )


def main() -> int:
    errors: list[str] = []

    expected_graph_markdown = 233
    actual_graph_markdown = len(list(GRAPH.rglob("*.md")))
    if actual_graph_markdown != expected_graph_markdown:
        errors.append(
            f"GRAPH NODE COUNT: expected {expected_graph_markdown} markdown files, "
            f"found {actual_graph_markdown}"
        )

    root = GRAPH / "story-graph-root.md"
    check_contains(
        errors,
        root,
        [f"graph-ga{ga:02d}-hub" for ga in range(1, 11)] + DOMAIN_HUBS,
    )

    sequence = ordered_subacts()

    for ga in range(1, 11):
        ga_id = f"ga{ga:02d}"
        ga_hub = GRAPH / "ga" / f"graph-{ga_id}-hub.md"
        check_contains(
            errors,
            ga_hub,
            [f"graph-{ga_id}-act-{a}" for a in ACT_LETTERS]
            + [f"graph-{ga_id}-state-spine", ga_source(ga), collection_source(ga)],
        )

        state = GRAPH / "state" / f"graph-{ga_id}-state-spine.md"
        state_required = DOMAIN_HUBS + [
            ga_source(ga),
            collection_source(ga),
            "episode-briefs",
            "context-pack-tangible-reader-memory-execution-spec-proposal-v1",
            "ga1-10-state-checkpoint-matrix-v1",
            "ga1-10-operational-checkpoint-snapshots-v1",
        ]
        if ga >= 2:
            state_required.append(DETAIL_PRODUCTION_INDEX)
        check_contains(errors, state, state_required)

        for a in ACT_LETTERS:
            act = GRAPH / "acts" / f"graph-{ga_id}-act-{a}.md"
            check_contains(
                errors,
                act,
                [
                    f"graph-{ga_id}-hub",
                    f"graph-{ga_id}-state-spine",
                    ga_source(ga),
                ]
                + [f"graph-{ga_id}-subact-{a}{n}" for n in range(1, 5)],
            )

            for n in range(1, 5):
                stem = f"graph-{ga_id}-subact-{a}{n}"
                sub = GRAPH / "subacts" / f"{stem}.md"
                check_contains(
                    errors,
                    sub,
                    [
                        f"graph-{ga_id}-act-{a}",
                        ga_source(ga),
                        collection_source(ga),
                        f"graph-{ga_id}-state-spine",
                        "episode-briefs",
                        "context-pack-tangible-reader-memory-execution-spec-proposal-v1",
                    ],
                )
                if ga == 10 and a == "d":
                    check_contains(
                        errors,
                        sub,
                        ["ga10-ending-reconciliation-canon-amendment-2026-08-20"],
                    )

                # The 160 Subact nodes form one chronological navigation chain.
                idx = sequence.index(stem)
                targets = wiki_targets(text(sub)) if sub.exists() else set()
                if idx > 0 and sequence[idx - 1] not in targets:
                    errors.append(f"PREVIOUS LINK MISSING: {stem} -> {sequence[idx - 1]}")
                if idx < len(sequence) - 1 and sequence[idx + 1] not in targets:
                    errors.append(f"NEXT LINK MISSING: {stem} -> {sequence[idx + 1]}")
                if idx == len(sequence) - 1 and "story-graph-root" not in targets:
                    errors.append("SERIES-END LINK MISSING: final Subact must return to story-graph-root")

    # Domain hubs must remain navigation-only and must all exist.
    for name in DOMAIN_HUBS:
        path = GRAPH / "state" / f"{name}.md"
        if not path.exists():
            errors.append(f"MISSING DOMAIN HUB: {path.relative_to(ROOT)}")
            continue
        body = text(path)
        if "NOT A" not in body and "QC BRIDGE ONLY" not in body:
            errors.append(f"AUTHORITY GUARD MISSING: {path.relative_to(ROOT)}")

    # Every graph wiki link must lead to a real Markdown node/source.
    validate_graph_link_targets(errors)

    # Do not silently introduce the other project's Volume/60-Subact hierarchy.
    rules = text(GRAPH / "README.md")
    if "다른 프로젝트의 `Volume` 또는 고정 `60 Subact` 구조를 가져오지 않는다" not in rules:
        errors.append("PROJECT-SPECIFIC HIERARCHY GUARD missing from docs/_graph/README.md")

    if errors:
        print("STORY GRAPH VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("STORY GRAPH VALIDATION: PASS")
    print("- markdown files under docs/_graph: 233")
    print("- grand-act hubs: 10")
    print("- act hubs: 40")
    print("- subact hubs: 160")
    print("- GA state spines: 10")
    print("- domain state hubs: 11")
    print("- chronological Subact chain: 160/160")
    print("- GA2-GA10 episode-design index bridge: 9/9")
    print("- graph wiki targets: all resolvable")
    print("- exact story facts remain source-owned; graph is navigation-only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
