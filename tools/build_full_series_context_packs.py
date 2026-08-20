#!/usr/bin/env python3
"""Build source-bound FULL Context Pack documents for E011–E1100.

This tool is a routing/execution compiler, not a story generator. It copies and
reorganizes already-approved episode-card material into the adopted Context Pack
execution schema. It never reads manuscript prose and never invents missing
story facts.

E001–E010 remain the manually audited effective packs registered in
`ga1-e001-e010-context-pack-status-index-v1.md`; generated coverage begins E011.

Usage:
  python tools/build_full_series_context_packs.py
  python tools/build_full_series_context_packs.py --check
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SRC = DOCS / "10_story_architecture"
DETAIL = SRC / "detail"
OUT = DOCS / "13_writing_harness" / "context_packs" / "generated"

# Most files use `# Episode N`; the standalone E525 card uses `## Episode 525`.
EP_HEAD = re.compile(r"^#{1,2}\s+Episode\s+(\d+)\s+—\s+(.+?)\s*$", re.M)
LABEL = re.compile(r"^([A-Za-z][A-Za-z0-9 /&()'’_.\-]{0,90}):\s*(.*)$")
GA1_FILE = re.compile(r"^ga1-episodes-(\d+)-(\d+)-.*scene-cards.*\.md$")
# Accept both range files (`...episode-cards-v1`) and singletons such as
# `ga5-e525-episode-card-v1.md`. Source coverage still hard-fails on duplicates.
DETAIL_FILE = re.compile(r"^ga(\d+)-e(\d+)(?:-(\d+))?-episode-cards?-v1\.md$")

# Current canonical production boundaries from
# episodes-101-1100-detail-production-standard-and-batch-map-v1.md.
GA_RANGES = {
    1: (11, 100),
    2: (101, 210),
    3: (211, 330),
    4: (331, 450),
    5: (451, 570),
    6: (571, 690),
    7: (691, 800),
    8: (801, 900),
    9: (901, 1000),
    10: (1001, 1100),
}

HIGH_WATCH = [
    (431, 438, "GA4 E431–438"),
    (716, 723, "GA7 E716–723"),
    (776, 783, "GA7 E776–783"),
    (784, 790, "GA7 E784–790"),
    (836, 843, "GA8 E836–843"),
    (851, 860, "GA8 E851–860"),
    (861, 868, "GA8 E861–868"),
    (926, 935, "GA9 E926–935"),
    (936, 943, "GA9 E936–943"),
]

MANUAL_E001_E010 = {
    1: "docs/00_project/ga1-e001-e010-context-pack-production-v1.md",
    2: "docs/00_project/ga1-e002-context-pack-refresh-v1.md",
    3: "docs/00_project/ga1-e003-context-pack-refresh-v1.md",
    4: "docs/00_project/ga1-e004-context-pack-refresh-v1.md",
    5: "docs/00_project/ga1-e005-context-pack-refresh-v1.md",
    6: "docs/00_project/ga1-e006-e010-context-pack-deep-v1.md",
    7: "docs/00_project/ga1-e006-e010-context-pack-deep-v1.md",
    8: "docs/00_project/ga1-e006-e010-context-pack-deep-v1.md",
    9: "docs/00_project/ga1-e006-e010-context-pack-deep-v1.md",
    10: "docs/00_project/ga1-e006-e010-context-pack-deep-v1.md",
}


@dataclass
class EpisodeCard:
    episode: int
    title: str
    source: Path
    raw: str
    fields: dict[str, list[str]]


def clean_lines(text: str) -> str:
    rows = []
    for raw in text.splitlines():
        s = raw.strip()
        if not s or s.startswith("---") or s.startswith("```"):
            continue
        if s.startswith("-"):
            s = s.lstrip("- ").strip()
        rows.append(s)
    return " ".join(rows)


def shorten(text: str, limit: int = 900) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if not text or len(text) <= limit:
        return text
    cut = text.rfind(". ", 0, limit)
    if cut < max(120, limit // 2):
        cut = text.rfind("; ", 0, limit)
    if cut < max(120, limit // 2):
        cut = limit
    return text[:cut].rstrip(" ;,.") + " … [source continues]"


def parse_fields(block: str) -> dict[str, list[str]]:
    fields: dict[str, list[str]] = defaultdict(list)
    current: str | None = None
    buf: list[str] = []

    def flush() -> None:
        nonlocal current, buf
        if current is not None:
            value = clean_lines("\n".join(buf))
            if value:
                fields[current].append(value)
        current = None
        buf = []

    for line in block.splitlines():
        if line.startswith("#"):
            flush()
            continue
        m = LABEL.match(line.strip())
        if m:
            flush()
            current = m.group(1).strip().lower()
            same = m.group(2).strip()
            if same:
                buf.append(same)
            continue
        if current is not None:
            buf.append(line)
    flush()
    return dict(fields)


def split_episodes(path: Path) -> list[EpisodeCard]:
    text = path.read_text(encoding="utf-8")
    hits = list(EP_HEAD.finditer(text))
    out = []
    for i, hit in enumerate(hits):
        lo = hit.start()
        hi = hits[i + 1].start() if i + 1 < len(hits) else len(text)
        block = text[lo:hi]
        out.append(EpisodeCard(
            episode=int(hit.group(1)),
            title=hit.group(2).strip(),
            source=path,
            raw=block,
            fields=parse_fields(block),
        ))
    return out


def load_sources() -> dict[int, EpisodeCard]:
    by_ep: dict[int, EpisodeCard] = {}
    duplicates: list[tuple[int, Path, Path]] = []

    ga1_files = [p for p in SRC.glob("ga1-episodes-*-scene-cards*.md") if GA1_FILE.match(p.name)]
    detail_files = [p for p in DETAIL.glob("ga*-e*-episode-card*.md") if DETAIL_FILE.match(p.name)]

    for p in sorted(ga1_files + detail_files):
        for card in split_episodes(p):
            if card.episode <= 10 or not 11 <= card.episode <= 1100:
                continue
            if card.episode in by_ep:
                duplicates.append((card.episode, by_ep[card.episode].source, p))
            else:
                by_ep[card.episode] = card

    if duplicates:
        lines = ["Duplicate episode-card ownership detected:"]
        for ep, a, b in duplicates:
            lines.append(f"  E{ep}: {a.relative_to(ROOT)} <> {b.relative_to(ROOT)}")
        raise RuntimeError("\n".join(lines))
    return by_ep


def vals(card: EpisodeCard, *names: str, limit_each: int = 700, max_items: int = 4) -> list[str]:
    out: list[str] = []
    for name in names:
        for v in card.fields.get(name.lower(), []):
            v = shorten(v, limit_each)
            if v and v not in out:
                out.append(v)
            if len(out) >= max_items:
                return out
    return out


def first(card: EpisodeCard, *names: str, default: str = "UNRESOLVED FROM APPROVED SOURCES") -> str:
    got = vals(card, *names, max_items=1)
    return got[0] if got else default


def bullets(items: list[str], unresolved: bool = True) -> str:
    if not items:
        return "- UNRESOLVED FROM APPROVED SOURCES" if unresolved else "- NONE"
    return "\n".join(f"- {x}" for x in items)


def hw_band(ep: int) -> str | None:
    for lo, hi, label in HIGH_WATCH:
        if lo <= ep <= hi:
            return label
    return None


def source_stem(card: EpisodeCard) -> str:
    return card.source.stem


def render_episode(card: EpisodeCard) -> str:
    visible = first(card, "visible goal", "goal")
    secondary = first(card, "hidden pressure", "obstacle", "pressure", "conflict", "opposition")

    opening = vals(card, "opening state", "physical state", "physical setup", "physical reality", max_items=2)
    places = vals(card, "location/time", "location", max_items=3, limit_each=450)
    anchor = opening + places
    changes = vals(card, "state change", "immediate result", "result", "outcome", "immediate outcome", max_items=5)
    costs = vals(card, "cost", "refusal", "opposition", max_items=4)
    reentry = vals(card, "carried state", "final hook", "end hook", max_items=3)
    actors = vals(card, "actors/goals", "actors", "actor goal", "actor goals", "front-stage actor", max_items=5)
    decisions = vals(card, "decisive choice", "decision", "choice", max_items=4)
    mystery = vals(card, "mystery state", "archive event", "clue", "clues", max_items=4)
    collection = vals(card, "collection state", max_items=3)
    relationship = vals(card, "relationship/institution state", "relationship state", "institution state", max_items=3)

    date = first(card, "date", default="UNRESOLVED FROM APPROVED SOURCES")
    pov = first(card, "pov / information source", "pov", default="UNRESOLVED FROM APPROVED SOURCES")
    specialists = first(card, "specialist panel", default="N/A — source card does not store a panel")
    band = hw_band(card.episode)

    missing = []
    if visible.startswith("UNRESOLVED"):
        missing.append("ACTIVE_DESIRE_MAIN exact wording")
    if not anchor:
        missing.append("PHYSICAL_ANCHOR exact carrier")
    if not changes:
        missing.append("STATE_CHANGE exact wording")
    if not costs:
        missing.append("COST_OR_REFUSAL exact wording")
    if not reentry:
        missing.append("REENTRY_ANCHOR exact wording")

    out = [
        f"## E{card.episode:03d} — {card.title}",
        "",
        "CONTEXT STATUS: **FULL — SOURCE-BOUND DEEP EXECUTION PACK**",
        f"Source Card: [[{source_stem(card)}]]",
        f"Date: {date}",
        f"POV / information source: {pov}",
        f"HIGH_WATCH_BAND: `{band or 'N/A'}`",
        "",
        "### Common six-field contract",
        "",
        "**ACTIVE_DESIRE_MAIN**  ", visible, "",
        "**ACTIVE_DESIRE_SECONDARY**  ", secondary, "",
        "**PHYSICAL_ANCHOR**", bullets(anchor), "",
        "**STATE_CHANGE**", bullets(changes), "",
        "**COST_OR_REFUSAL**", bullets(costs), "",
        "**REENTRY_ANCHOR**", bullets(reentry), "",
        "### Agency / authority evidence", "",
        "**CURRENT_ACTOR_GOAL_EVIDENCE**", bullets(actors), "",
        "**DECISION_EVIDENCE**", bullets(decisions), "",
        "**RIAN_CANNOT_OVERRIDE**  ",
        "Any technical, medical, legal, custody, record, local, affected-party or command authority explicitly owned by another actor/institution in the source card. Context compilation does not migrate that authority to Rian; exact owner evidence is the actor/decision material above and the higher canon/state documents.",
        "",
        "### Information / payoff ceiling", "",
        "**MYSTERY_OR_CLUE_SOURCE_STATE**", bullets(mystery, unresolved=False), "",
        "Formal clue/payoff accounting follows the highest locked mystery/payoff ledger. A lower card tag or open plant window may remain a teaser/setup but cannot be promoted into an earlier explanatory reveal by this Context Pack.",
        "",
        "### Carry ledgers", "",
        "**COLLECTION_STATE**", bullets(collection, unresolved=False), "",
        "**RELATIONSHIP_OR_INSTITUTION_STATE**", bullets(relationship, unresolved=False), "",
        f"**SPECIALIST_PANEL / SOURCE CHECK:** {specialists}", "",
        "### Unsupported exacts / source-precedence guard", "",
    ]

    if missing:
        out += [
            "The detailed card does not expose one or more values under the canonical label shape. This does **not** authorize invention:",
            *[f"- {m}: `UNRESOLVED FROM APPROVED SOURCES`" for m in missing],
        ]
    else:
        out.append("No mandatory Context slot requires a new fact from this card parse. Any prose-level exact number/name/layout not present in higher sources remains `UNRESOLVED FROM APPROVED SOURCES`.")

    out += ["", "`NEW_CANON_REQUIRED: NO`", ""]

    if band:
        face = actors[0] if actors else (pov if not pov.startswith("UNRESOLVED") else "UNRESOLVED FROM APPROVED SOURCES")
        asset = collection[0] if collection else (opening[0] if opening else "UNRESOLVED FROM APPROVED SOURCES")
        place = places[0] if places else "UNRESOLVED FROM APPROVED SOURCES"
        owner = decisions[0] if decisions else (actors[0] if actors else "UNRESOLVED FROM APPROVED SOURCES")
        abstracts = (mystery + relationship)[:2]
        out += [
            "### HIGH-WATCH addendum", "",
            f"`HIGH_WATCH_BAND: {band}`", "",
            f"**RECURRING_FACE:** {face}", "",
            f"**RECURRING_ASSET:** {asset}", "",
            f"**RECURRING_PLACE:** {place}", "",
            f"**CURRENT_OWNER_OF_DECISION:** {owner}", "",
            "**RIAN_CANNOT_OVERRIDE:** the non-Rian domain/affected-party authorities carried by the source card; if the decisive owner is not explicit, keep it unresolved rather than defaulting to Rian.", "",
            "**ABSTRACT_CONCEPTS_FOREGROUNDED:**", bullets(abstracts, unresolved=False), "",
            "`NEW_CANON_REQUIRED: NO`", "",
        ]

    out += [
        "### Context readiness", "",
        "`CONTEXT READY: YES — source-bound execution layer only`", "",
        "This readiness does **not** authorize manuscript drafting, author approval, publication or canon mutation.", "",
        "---", "",
    ]
    return "\n".join(out)


def render_ga(ga: int, cards: dict[int, EpisodeCard]) -> str:
    lo, hi = GA_RANGES[ga]
    selected = [cards[e] for e in range(lo, hi + 1)]
    source_names = sorted({c.source.stem for c in selected})
    sections = [render_episode(c) for c in selected]
    return "\n".join([
        f"# GA{ga} E{lo:03d}–E{hi:03d} Full Deep Context Packs v1",
        "",
        "Status: REVIEW — GENERATED SOURCE-BOUND PRODUCTION EXECUTION PACK",
        "Effective Authority: DERIVED PROJECT-CONTROL WORKFLOW/QC INPUT",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "Owner Agents: A00 PM / A11 Prose & Serialization / N03 Episode / X02 Reader Memory / X04 Continuity / O01 Canon",
        "Last Reviewed: 2026-08-20",
        "Depends On: [[full-series-context-first-production-directive-2026-08-20]], [[context-pack-tangible-reader-memory-execution-spec-proposal-v1]], current act/subact maps, chronology/state/loss/payoff ledgers, and the source episode cards listed per entry",
        "Used By: future manuscript preparation only after separate manuscript authorization",
        "Open Risks: generated reorganization cannot resolve a semantic contradiction in an upstream card; such conflicts belong in the companion blindspot audit/change-control path.",
        "",
        "> [!warning] Source-bound generated execution layer",
        "> This file reorganizes approved detailed-card material. It does not create story canon and must not be edited to invent missing facts. Fix/clarify the owning source or add an approved Context overlay instead.",
        "",
        f"Coverage: **{len(selected)}/{hi-lo+1} episodes**",
        f"Source card files: **{len(source_names)}**",
        "",
        *sections,
    ])


def manifest(cards: dict[int, EpisodeCard]) -> str:
    lines = [
        "# Full-Series Context Pack Generated Manifest v1", "",
        "Status: REVIEW — PROJECT-CONTROL STATUS MANIFEST",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "Last Reviewed: 2026-08-20",
        "Depends On: [[full-series-context-first-production-directive-2026-08-20]], [[context-pack-tangible-reader-memory-execution-spec-proposal-v1]]",
        "", "## Coverage", "",
        "| Range | Effective Context source | Coverage |",
        "|---|---|---:|",
        "| E001–E010 | manually audited files registered in [[ga1-e001-e010-context-pack-status-index-v1]] | 10/10 |",
    ]
    for ga, (lo, hi) in GA_RANGES.items():
        stem = f"ga{ga}-e{lo:03d}-e{hi:03d}-context-packs-v1"
        lines.append(f"| E{lo:03d}–E{hi:03d} | [[{stem}]] | {hi-lo+1}/{hi-lo+1} |")
    lines += [
        "",
        "Total effective Context target after generated files are current: **1100/1100 FULL**.", "",
        "E001–E010 manual packs outrank any historical PRELOAD/FORECAST text. Generated files begin at E011, so there is no generated/manual ambiguity for the first ten episodes.", "",
        "## Source-coverage invariants", "",
        f"- generated episode cards loaded: **{len(cards)}** (expected 1090 = E011–E1100)",
        "- duplicate episode source owner: **0 required**",
        "- missing episode source: **0 required**",
        "- manuscript prose used as source: **0**",
        "- generated story-canon mutation: **0**",
        "- manuscript authorization expansion: **0**", "",
        "## HIGH-WATCH bands", "",
    ]
    for _lo, _hi, label in HIGH_WATCH:
        lines.append(f"- {label}: generated entries carry the normalized HIGH-WATCH addendum; companion semantic audits remain authoritative for deeper carrier/authority review.")
    lines += [
        "", "## Completion semantics", "",
        "`1100/1100 FULL` means every episode has a source-bound execution packet. It does **not** by itself mean the semantic blindspot gate has passed. Manuscript work resumes only after the separate GA/cross-GA Context blindspot audits are merged and the full-series completion checkpoint is explicitly PASS.",
    ]
    return "\n".join(lines) + "\n"


def structural_audit(cards: dict[int, EpisodeCard]) -> str:
    missing = [e for e in range(11, 1101) if e not in cards]
    unexpected = sorted(e for e in cards if not 11 <= e <= 1100)
    high_watch_count = sum(1 for e in cards if hw_band(e))
    field_stats = defaultdict(int)
    for card in cards.values():
        if first(card, "visible goal", "goal").startswith("UNRESOLVED"):
            field_stats["main_desire_unresolved"] += 1
        if not vals(card, "opening state", "physical state", "physical setup", "physical reality", "location/time", "location", max_items=1):
            field_stats["anchor_unresolved"] += 1
        if not vals(card, "state change", "immediate result", "result", "outcome", "immediate outcome", max_items=1):
            field_stats["state_change_unresolved"] += 1
        if not vals(card, "cost", "refusal", "opposition", max_items=1):
            field_stats["cost_unresolved"] += 1
        if not vals(card, "carried state", "final hook", "end hook", max_items=1):
            field_stats["reentry_unresolved"] += 1

    lines = [
        "# Full-Series Context Pack Structural Audit v1", "",
        "Status: REVIEW — MACHINE-REPRODUCIBLE CONTEXT QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "Last Reviewed: 2026-08-20", "",
        "## Result", "",
        f"- source-bound generated cards: **{len(cards)} / 1090**",
        f"- missing E011–E1100 source owners: **{len(missing)}**",
        f"- unexpected episode ids: **{len(unexpected)}**",
        f"- HIGH-WATCH generated entries: **{high_watch_count}**",
        "- manuscript prose read by builder: **NO**",
        "- story facts generated by builder: **NO**", "",
        "## Field-shape diagnostics", "",
        f"- ACTIVE_DESIRE_MAIN exact-label fallback/unresolved: {field_stats['main_desire_unresolved']}",
        f"- PHYSICAL_ANCHOR source carrier unresolved: {field_stats['anchor_unresolved']}",
        f"- STATE_CHANGE exact-label fallback/unresolved: {field_stats['state_change_unresolved']}",
        f"- COST_OR_REFUSAL exact-label fallback/unresolved: {field_stats['cost_unresolved']}",
        f"- REENTRY_ANCHOR exact-label fallback/unresolved: {field_stats['reentry_unresolved']}", "",
        "An unresolved exact does not authorize invention; it is preserved as `UNRESOLVED FROM APPROVED SOURCES` for semantic review.", "",
        "## Hard fail conditions", "",
        "The builder exits non-zero before writing outputs if any E011–E1100 episode is missing or has duplicate source ownership. This prevents a visually complete but structurally incomplete 1100-episode Context layer.", "",
        "## Semantic audit still required", "",
        "Machine coverage cannot by itself verify clue timing, death/loss continuity, local authority, repeated narrative engine, or exact ending-amendment precedence. Those are handled by GA-level and cross-GA Context blindspot audits before the Context-first gate is declared complete.",
    ]
    if missing:
        lines += ["", "Missing episodes:", "- " + ", ".join(f"E{e}" for e in missing)]
    if unexpected:
        lines += ["", "Unexpected episodes:", "- " + ", ".join(f"E{e}" for e in unexpected)]
    return "\n".join(lines) + "\n"


def build_outputs() -> dict[Path, str]:
    cards = load_sources()
    missing = [e for e in range(11, 1101) if e not in cards]
    if missing:
        sample = ", ".join(f"E{e}" for e in missing[:30])
        more = " ..." if len(missing) > 30 else ""
        raise RuntimeError(f"Missing {len(missing)} episode-card sources: {sample}{more}")
    if len(cards) != 1090:
        raise RuntimeError(f"Expected 1090 generated episodes, found {len(cards)}")

    for ep, p in MANUAL_E001_E010.items():
        if not (ROOT / p).exists():
            raise RuntimeError(f"Manual E{ep:03d} Context source missing: {p}")

    outputs: dict[Path, str] = {}
    for ga, (lo, hi) in GA_RANGES.items():
        path = OUT / f"ga{ga}-e{lo:03d}-e{hi:03d}-context-packs-v1.md"
        outputs[path] = render_ga(ga, cards)
    outputs[OUT / "full-series-context-pack-generated-manifest-v1.md"] = manifest(cards)
    outputs[OUT / "full-series-context-pack-structural-audit-v1.md"] = structural_audit(cards)
    return outputs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    try:
        outputs = build_outputs()
    except Exception as exc:
        print(f"CONTEXT BUILD ERROR: {exc}", file=sys.stderr)
        return 1

    changed = []
    for path, text in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != text:
            changed.append(path)
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")

    if args.check and changed:
        print("Context outputs are stale/missing:")
        for p in changed:
            print(f"  {p.relative_to(ROOT).as_posix()}")
        return 1

    total = sum(1 for p in outputs if p.name.startswith("ga"))
    print(f"Generated/checked {total} GA Context files + manifest + structural audit")
    for p in outputs:
        print(f"  {p.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
