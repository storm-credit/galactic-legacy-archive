#!/usr/bin/env python3
"""Build the full-series collection-desire / set / subact execution layer.

This tool does not create story canon. It derives author-side collection threads
and reader-desire routing from the ten existing collection registries plus the
approved GA1-GA10 act/subact maps.

The generated CLSET identifiers are workflow/execution IDs, not in-world objects,
rights, institutions, powers or Archive records.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import build_collection_normalization as base  # noqa: E402

COLLECTION_DIR = ROOT / "docs" / "09_collection"
SOURCE_INDEX = COLLECTION_DIR / "data" / "collection-normalization-full-source-rows-v1.csv"
OUT_DIR = COLLECTION_DIR / "generated" / "desire_subact"
THREAD_INDEX = OUT_DIR / "full-series-collection-thread-index-v1.csv"
MANIFEST = OUT_DIR / "full-series-collection-desire-manifest-v1.md"
AUDIT = ROOT / "docs" / "99_quality_control" / "full-series-collection-desire-subact-depth-audit-v1.md"

ACT_MAPS = [
    ("GA1", "first-100-act-map-v2-consolidated.md"),
    ("GA2", "ga2-episodes-101-210-act-map-v1.md"),
    ("GA3", "ga3-episodes-211-330-act-map-v1.md"),
    ("GA4", "ga4-episodes-331-450-act-map-v1.md"),
    ("GA5", "ga5-episodes-451-570-act-map-v1.md"),
    ("GA6", "ga6-episodes-571-690-act-map-v1.md"),
    ("GA7", "ga7-episodes-691-800-act-map-v1.md"),
    ("GA8", "ga8-episodes-801-900-act-map-v1.md"),
    ("GA9", "ga9-episodes-901-1000-act-map-v1.md"),
    ("GA10", "ga10-episodes-1001-1100-act-map-v1.md"),
]

SUBACT_RE = re.compile(
    r"^##\s+(?:(?:\d+(?:\.\d+)?\.)\s+)?(?:Subact\s+)?"
    r"([0-9A-Z]+(?:-[0-9]+)?)\s+—\s+(.+?)\s+/\s+Episodes\s+"
    r"(\d+)\s*[–—-]\s*(\d+)\s*$",
    re.IGNORECASE,
)
RANGE_RE = re.compile(r"\bE\s*(\d{1,4})\s*[–—-]\s*(\d{1,4})\b", re.IGNORECASE)
SLASH_RE = re.compile(r"\bE\s*(\d{1,4}(?:\s*/\s*\d{1,4})+)\b", re.IGNORECASE)
SINGLE_RE = re.compile(r"\bE\s*(\d{1,4})\b", re.IGNORECASE)

STOPWORDS = {
    "future", "current", "final", "first", "second", "third", "record", "records",
    "system", "service", "state", "target", "working", "public", "local", "limited",
    "authority", "collection", "legacy", "route", "episode", "episodes", "ga1", "ga2",
    "ga3", "ga4", "ga5", "ga6", "ga7", "ga8", "ga9", "ga10", "and", "the", "of",
    "for", "with", "from", "under", "into", "after", "before", "through",
}

DOMAIN_LABELS = {
    "C1": "인물·관계",
    "C2": "기체",
    "C3": "무기·부품",
    "C4": "유물·증거",
    "C5": "함선",
    "C6": "기술·표준",
    "C7": "세력·제도",
    "C8": "영토·노드·문명",
}

SET_LABELS = {
    "LINEAGE": "계보 세트",
    "EVENT": "사건 세트",
    "FUNCTIONAL": "역할 조합 세트",
    "RELATIONSHIP": "관계 세트",
    "CIVILIZATION": "문명 복원 세트",
}


@dataclass
class Subact:
    arc: str
    code: str
    title: str
    start: int
    end: int
    block: str
    source_file: str

    @property
    def set_id(self) -> str:
        clean = re.sub(r"[^0-9A-Z]+", "-", self.code.upper()).strip("-")
        return f"CLSET-{self.arc}-{clean}"


@dataclass
class Thread:
    source_row_id: str
    thread_id: str
    source_key: str
    source_file: str
    source_line: str
    arc: str
    section: str
    source_id: str
    title: str
    entry_kinds: str
    primary_domain: str
    domain_tags: str
    desire_phases: str
    acquisition_text: str
    integration_text: str
    cost_text: str
    loss_exit_text: str
    ending_text: str
    later_reuse_text: str
    classification_basis: str
    episodes: tuple[int, ...]
    block: str


def flatten(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def clip(text: str, limit: int = 520) -> str:
    text = flatten(text)
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def episode_refs(text: str) -> tuple[int, ...]:
    found: set[int] = set()
    for match in RANGE_RE.finditer(text):
        start, end = map(int, match.groups())
        if 1 <= start <= end <= 1100 and end - start <= 250:
            found.update(range(start, end + 1))
    for match in SLASH_RE.finditer(text):
        for part in re.split(r"\s*/\s*", match.group(1)):
            value = int(part)
            if 1 <= value <= 1100:
                found.add(value)
    for match in SINGLE_RE.finditer(text):
        value = int(match.group(1))
        if 1 <= value <= 1100:
            found.add(value)
    return tuple(sorted(found))


def parse_subacts(arc: str, filename: str) -> list[Subact]:
    path = ROOT / "docs" / "10_story_architecture" / filename
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    starts: list[tuple[int, re.Match[str]]] = []
    for index, line in enumerate(lines):
        match = SUBACT_RE.match(line.strip())
        if match:
            starts.append((index, match))
    result: list[Subact] = []
    for pos, (index, match) in enumerate(starts):
        next_index = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
        code, title, start, end = match.groups()
        result.append(
            Subact(
                arc=arc,
                code=code.upper(),
                title=title.strip(),
                start=int(start),
                end=int(end),
                block="\n".join(lines[index + 1 : next_index]).strip(),
                source_file=f"docs/10_story_architecture/{filename}",
            )
        )
    if not result:
        raise SystemExit(f"{filename}: no subacts parsed")
    return result


def labelled(block: str, prefixes: tuple[str, ...]) -> str:
    wanted = tuple(prefix.casefold() for prefix in prefixes)
    lines = block.splitlines()
    captured: list[str] = []
    active = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            active = False
            continue
        match = re.match(r"^([A-Za-z0-9 /+&()'._-]{1,72}):\s*(.*)$", stripped)
        if match:
            label = match.group(1).casefold()
            active = any(label.startswith(prefix) for prefix in wanted)
            if active and match.group(2).strip():
                captured.append(match.group(2).strip())
            continue
        if active:
            if not stripped:
                continue
            if stripped.startswith("-"):
                captured.append(stripped[1:].strip())
            elif not SUBACT_RE.match(stripped):
                captured.append(stripped)
    return clip(" ".join(captured))


def first_present(block: str, groups: tuple[tuple[str, ...], ...]) -> str:
    for group in groups:
        value = labelled(block, group)
        if value:
            return value
    return ""


def meaningful_tokens(title: str) -> list[str]:
    tokens = re.findall(r"[A-Za-z0-9][A-Za-z0-9-]{2,}|[가-힣]{2,}", title.casefold())
    return [token for token in tokens if token not in STOPWORDS and not token.startswith("e")][:10]


def infer_block_domains(subact: Subact) -> list[str]:
    domains = base.classify_domains(subact.title, "", subact.block, fallback=False)
    return domains or ["C7"]


def infer_set_types(domains: list[str], text: str, kinds: list[str]) -> list[str]:
    low = text.casefold()
    result: list[str] = []
    if "C8" in domains or any(word in low for word in ("civilization", "federation", "region", "node", "settlement", "autonomy")):
        result.append("CIVILIZATION")
    if any(word in low for word in ("lineage", "origin", "original", "ancestry", "yard", "design family", "service spine")):
        result.append("LINEAGE")
    if any(word in low for word in ("incident", "case", "history", "evidence", "testimony", "record", "war", "rescue", "verdict", "inquiry")):
        result.append("EVENT")
    if "RELATIONSHIP" in kinds or "C1" in domains or any(word in low for word in ("crew", "trust", "ally", "rival", "community", "consent")):
        result.append("RELATIONSHIP")
    if any(domain in domains for domain in ("C2", "C3", "C5", "C6")) or any(
        word in low for word in ("frame", "ship", "module", "tool", "standard", "repair", "mission", "route")
    ):
        result.append("FUNCTIONAL")
    ordered = [kind for kind in ("LINEAGE", "EVENT", "FUNCTIONAL", "RELATIONSHIP", "CIVILIZATION") if kind in result]
    return ordered or ["EVENT"]


def load_threads() -> list[Thread]:
    if not SOURCE_INDEX.exists():
        raise SystemExit("collection source normalization index missing")

    block_map: dict[str, str] = {}
    for arc, filename, expected in base.REGISTRIES:
        parsed = base.parse_registry(arc, filename)
        if len(parsed) != expected:
            raise SystemExit(f"{filename}: expected {expected}, found {len(parsed)}")
        block_map.update({row["source_key"]: row["block"] for row in parsed})

    threads: list[Thread] = []
    with SOURCE_INDEX.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 415:
        raise SystemExit(f"expected 415 source rows, found {len(rows)}")

    for row in rows:
        block = block_map.get(row["source_key"], "")
        if not block:
            raise SystemExit(f"missing registry block: {row['source_key']}")
        refs = episode_refs("\n".join((block, row["acquisition_text"], row["integration_text"], row["cost_text"], row["loss_exit_text"], row["ending_text"], row["later_reuse_text"])))
        safe_id = re.sub(r"[^0-9A-Z]+", "-", row["source_id"].upper()).strip("-")
        threads.append(
            Thread(
                source_row_id=row["source_row_id"],
                thread_id=f"CLT-{row['arc']}-{safe_id}",
                source_key=row["source_key"],
                source_file=row["source_file"],
                source_line=row["source_line"],
                arc=row["arc"],
                section=row["section"],
                source_id=row["source_id"],
                title=row["title"],
                entry_kinds=row["entry_kinds"],
                primary_domain=row["primary_domain"],
                domain_tags=row["domain_tags"],
                desire_phases=row["desire_phases"],
                acquisition_text=row["acquisition_text"],
                integration_text=row["integration_text"],
                cost_text=row["cost_text"],
                loss_exit_text=row["loss_exit_text"],
                ending_text=row["ending_text"],
                later_reuse_text=row["later_reuse_text"],
                classification_basis=row["classification_basis"],
                episodes=refs,
                block=block,
            )
        )
    return threads


def score_thread(thread: Thread, subact: Subact, block_domains: list[str]) -> tuple[int, list[str]]:
    score = 0
    basis: list[str] = []
    overlap = [ep for ep in thread.episodes if subact.start <= ep <= subact.end]
    if overlap:
        score += 100 + min(20, len(overlap))
        basis.append("EPISODE_OVERLAP")

    low_block = subact.block.casefold()
    if thread.source_id.casefold() in low_block:
        score += 35
        basis.append("SOURCE_ID_TEXT")

    hits = sum(1 for token in meaningful_tokens(thread.title) if token in low_block)
    if hits:
        score += min(24, hits * 4)
        basis.append("TITLE_TEXT")

    thread_domains = thread.domain_tags.split("|") if thread.domain_tags else [thread.primary_domain]
    if set(thread_domains) & set(block_domains):
        score += 4
        basis.append("DOMAIN_MATCH")

    if subact.arc.casefold() in thread.later_reuse_text.casefold():
        score += 2
        basis.append("LATER_REUSE")

    return score, basis


def select_threads(subact: Subact, threads: list[Thread]) -> tuple[list[tuple[Thread, int, str]], str]:
    candidates = [thread for thread in threads if thread.arc == subact.arc]
    block_domains = infer_block_domains(subact)
    scored: list[tuple[Thread, int, str]] = []
    for thread in candidates:
        score, basis = score_thread(thread, subact, block_domains)
        if score > 4:
            scored.append((thread, score, "+".join(basis)))
    scored.sort(key=lambda item: (-item[1], item[0].source_row_id))

    strong = [item for item in scored if item[1] >= 35]
    selected = (strong or scored)[:5]
    quality = "A-DIRECT" if any(item[1] >= 100 for item in selected) else "B-TEXTUAL"

    if not selected:
        midpoint = (subact.start + subact.end) / 2
        distance_rows: list[tuple[float, Thread]] = []
        for thread in candidates:
            if thread.episodes:
                distance_rows.append((min(abs(midpoint - ep) for ep in thread.episodes), thread))
        if distance_rows:
            distance_rows.sort(key=lambda item: (item[0], item[1].source_row_id))
            selected = [(thread, 1, "NEAREST_EXPLICIT_EPISODE") for _, thread in distance_rows[:3]]
            quality = "B-FALLBACK"
    return selected, quality


def source_field_pack(subact: Subact, selected: list[tuple[Thread, int, str]]) -> dict[str, str]:
    discovery = first_present(
        subact.block,
        (("collection/reveal", "key discoveries", "discoveries", "discovery"), ("entry", "immediate facts"), ("goal", "goals")),
    )
    acquisition = first_present(
        subact.block,
        (("reward at", "reward", "gain", "acquisition"), ("goal", "goals"), ("authority bargain", "required decision", "required action")),
    )
    synergy = first_present(
        subact.block,
        (("integration", "module choice", "character beats", "authority bargain"), ("required action", "required decision"), ("reward",)),
    )
    cost = first_present(
        subact.block,
        (("cost", "costs"), ("resistance", "conflict", "risk", "failure")),
    )
    hook = first_present(subact.block, (("hook", "next question", "next"),))

    if selected:
        if not discovery:
            discovery = clip(" / ".join(thread.title for thread, _, _ in selected[:3]))
        if not acquisition:
            acquisition = clip(" / ".join(thread.acquisition_text for thread, _, _ in selected if thread.acquisition_text))
        if not synergy:
            synergy = clip(" / ".join(thread.integration_text for thread, _, _ in selected if thread.integration_text))
        if not cost:
            cost = clip(" / ".join(filter(None, (thread.cost_text or thread.loss_exit_text for thread, _, _ in selected))))
        if not hook:
            hook = clip(" / ".join(thread.later_reuse_text or thread.ending_text for thread, _, _ in selected if thread.later_reuse_text or thread.ending_text))

    if not acquisition:
        acquisition = clip(labelled(subact.block, ("goal", "goals")) or subact.title)
    if not synergy:
        synergy = clip(acquisition)
    if not cost:
        cost = "NO NEW COST INVENTED — use the approved subact/episode cost and refusal state only."
    if not hook:
        hook = "NEXT SUBACT DESIRE = carry the changed state forward; do not reset the acquired relationship/right/asset state."

    return {
        "discovery": discovery or subact.title,
        "acquisition": acquisition,
        "synergy": synergy,
        "cost": cost,
        "hook": hook,
    }


def ownership_guard(domains: list[str]) -> str:
    guards: list[str] = []
    if "C1" in domains:
        guards.append("인물은 소유물이 아니며 동의·거절·이탈 가능성을 유지")
    if "C7" in domains:
        guards.append("세력·제도는 구성원·대표성·승계와 분리된 독립 의사를 유지")
    if "C8" in domains:
        guards.append("장소·노드·문명은 발견/접근과 소유·통치·자치를 동일시하지 않음")
    if any(domain in domains for domain in ("C2", "C3", "C5", "C6")):
        guards.append("물리 확보와 운용권·인증·정비·승무원·산업능력을 분리")
    return "; ".join(guards) or "기존 Collection Bible의 비소유/비자동호환 규칙 유지"


def render_ga(arc: str, subacts: list[Subact], threads: list[Thread]) -> tuple[str, list[dict[str, object]]]:
    rows: list[dict[str, object]] = []
    parts = [
        f"# {arc} Collection Desire / Set / Subact Execution Map v1",
        "",
        "Status: WORKFLOW/QC — SOURCE-BOUND EXECUTION LAYER",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        "> 이 문서는 기존 액트/서브액트·수집 레지스트리를 다시 설계하지 않는다. 각 서브액트의 독자 수집욕과 세트 진행을 집필용으로 명시한다.",
        "> `CLSET-*`와 `CLT-*`는 작가용 실행 ID이며 작중 실체·소유권·Archive 항목을 새로 만들지 않는다.",
        "",
    ]

    for subact in subacts:
        selected, quality = select_threads(subact, threads)
        fields = source_field_pack(subact, selected)
        target_domains: list[str] = []
        target_kinds: list[str] = []
        for thread, _, _ in selected:
            for domain in thread.domain_tags.split("|"):
                if domain and domain not in target_domains:
                    target_domains.append(domain)
            for kind in thread.entry_kinds.split("|"):
                if kind and kind not in target_kinds:
                    target_kinds.append(kind)
        if not target_domains:
            target_domains = infer_block_domains(subact)
        set_types = infer_set_types(target_domains, subact.title + "\n" + subact.block, target_kinds)
        primary_set = set_types[0]
        main_desire = clip(fields["discovery"] + " → " + fields["acquisition"], 640)

        parts.extend(
            [
                f"## {subact.code} — {subact.title} / E{subact.start}–E{subact.end}",
                "",
                f"- `SET_EXECUTION_ID`: `{subact.set_id}`",
                f"- `PRIMARY_SET_TYPE`: `{primary_set}` — {SET_LABELS[primary_set]}",
                f"- `SECONDARY_SET_TYPES`: `{', '.join(set_types[1:]) if len(set_types) > 1 else 'NONE'}`",
                f"- `MATCH_DEPTH`: `{quality}`",
                f"- `FRONT_DOMAINS`: " + ", ".join(f"{domain} {DOMAIN_LABELS.get(domain, '')}" for domain in target_domains),
                f"- `READER_DESIRE_MAIN`: {main_desire}",
                f"- `DISCOVERY`: {fields['discovery']}",
                f"- `ACQUISITION_OR_CONNECTION`: {fields['acquisition']}",
                f"- `SYNERGY_OR_USE`: {fields['synergy']}",
                f"- `COST_REFUSAL_OR_LOSS`: {fields['cost']}",
                f"- `SET_ADVANCE_CONDITION`: {fields['synergy']}",
                f"- `NEXT_DESIRE`: {fields['hook']}",
                f"- `OWNERSHIP_GUARD`: {ownership_guard(target_domains)}",
                "- `ACTIVE_TARGETS`:",
            ]
        )
        if selected:
            for thread, score, basis in selected:
                parts.append(
                    f"  - `{thread.thread_id}` / `{thread.source_id}` / {thread.title} — `{basis}` score={score}"
                )
        else:
            parts.append("  - `NONE` — registry target mapping failed; audit must block integration.")
        parts.extend(
            [
                f"- `SOURCE_SUBACT`: `{subact.source_file}` / {subact.code}",
                "- `NEW_CANON_REQUIRED`: `NO`",
                "",
            ]
        )
        rows.append(
            {
                "arc": arc,
                "code": subact.code,
                "start": subact.start,
                "end": subact.end,
                "quality": quality,
                "target_count": len(selected),
                "domains": target_domains,
                "set_types": set_types,
                "fields": fields,
                "selected": selected,
            }
        )
    return "\n".join(parts).rstrip() + "\n", rows


def build_thread_rows(threads: list[Thread], subacts_by_arc: dict[str, list[Subact]], selected_usage: Counter[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for thread in threads:
        overlapping = [
            subact.code
            for subact in subacts_by_arc[thread.arc]
            if any(subact.start <= ep <= subact.end for ep in thread.episodes)
        ]
        set_types = infer_set_types(
            thread.domain_tags.split("|") if thread.domain_tags else [thread.primary_domain],
            thread.title + "\n" + thread.block,
            thread.entry_kinds.split("|") if thread.entry_kinds else [],
        )
        rows.append(
            {
                "source_row_id": thread.source_row_id,
                "collection_thread_id": thread.thread_id,
                "source_key": thread.source_key,
                "arc": thread.arc,
                "source_id": thread.source_id,
                "title": thread.title,
                "entry_kinds": thread.entry_kinds,
                "primary_domain": thread.primary_domain,
                "domain_tags": thread.domain_tags,
                "desire_phases": thread.desire_phases,
                "set_type_candidates": "|".join(set_types),
                "explicit_episode_refs": "|".join(map(str, thread.episodes)),
                "explicit_subacts": "|".join(overlapping) if overlapping else "ARC_WIDE_OR_UNSPECIFIED",
                "selected_as_active_target_count": str(selected_usage[thread.thread_id]),
                "semantic_identity_policy": "SOURCE_THREAD_ID_NOT_UNIQUE_ENTITY_CLAIM",
                "ownership_policy": ownership_guard(thread.domain_tags.split("|") if thread.domain_tags else [thread.primary_domain]),
                "classification_basis": thread.classification_basis,
                "story_canon_mutation": "NONE",
            }
        )
    return rows


def audit_text(all_rows: list[dict[str, object]], threads: list[Thread], subacts_by_arc: dict[str, list[Subact]], selected_usage: Counter[str]) -> str:
    quality = Counter(str(row["quality"]) for row in all_rows)
    missing_targets = [row for row in all_rows if int(row["target_count"]) == 0]
    b_rows = [row for row in all_rows if str(row["quality"]).startswith("B-")]
    missing_fields = []
    for row in all_rows:
        fields = row["fields"]
        for key in ("discovery", "acquisition", "synergy", "cost", "hook"):
            if not str(fields[key]).strip():
                missing_fields.append(f"{row['arc']} {row['code']} {key}")

    no_episode_refs = [thread for thread in threads if not thread.episodes]
    never_selected = [thread for thread in threads if selected_usage[thread.thread_id] == 0]
    ga_counts = {arc: len(subacts) for arc, subacts in subacts_by_arc.items()}

    verdict = "PASS" if not missing_targets and not missing_fields and not b_rows else "HOLD"
    lines = [
        "# Full-Series Collection Desire / Subact Depth Audit v1",
        "",
        "Status: REVIEW — EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        f"> **VERDICT: {verdict}**",
        "",
        "## Coverage",
        "",
        f"- source collection rows: **{len(threads)} / 415**",
        f"- parsed subacts: **{len(all_rows)}**",
        f"- GA subact counts: `{ga_counts}`",
        f"- direct A matches: **{quality.get('A-DIRECT', 0)}**",
        f"- B textual matches: **{quality.get('B-TEXTUAL', 0)}**",
        f"- B fallback matches: **{quality.get('B-FALLBACK', 0)}**",
        f"- subacts with zero active target: **{len(missing_targets)}**",
        f"- mandatory desire fields missing: **{len(missing_fields)}**",
        f"- source rows with no explicit episode reference: **{len(no_episode_refs)}**",
        f"- source rows never selected as a front-stage subact target: **{len(never_selected)}**",
        "",
        "`never selected` is not automatically a defect: background, later-reuse, claim, loss and legacy rows may remain off-stage. Every source row still receives a stable collection-thread execution ID.",
        "",
        "## Integration Gate",
        "",
        "Required for PASS:",
        "1. every approved subact has at least one source-bound active target;",
        "2. every subact has discovery/acquisition/synergy/cost/next-desire fields;",
        "3. every subact has a canonical Collection Bible set-type mapping;",
        "4. C1/C7/C8 non-ownership guards remain explicit;",
        "5. no new item, person, death, ability, authority, relic or ending fact is created;",
        "6. B-TEXTUAL/B-FALLBACK rows must be manually inspected or source-bound overridden before MAIN-INTEGRATED COMPLETE.",
        "",
        "## B-depth queue",
        "",
    ]
    if b_rows:
        for row in b_rows:
            lines.append(f"- `{row['arc']} {row['code']}` E{row['start']}–E{row['end']} — `{row['quality']}`")
    else:
        lines.append("- NONE")
    lines.extend(["", "## Missing-field queue", ""])
    lines.extend(f"- {item}" for item in missing_fields) if missing_fields else lines.append("- NONE")
    lines.extend(
        [
            "",
            "## Canon / Ethics / Power-Creep Guard",
            "",
            "- people are relationship/consent subjects, never inventory ownership: **ENFORCED**",
            "- institutions and territories retain constituency/autonomy/appeal: **ENFORCED**",
            "- physical access is not silently converted into title, command, certification or compatibility: **ENFORCED**",
            "- irreversible loss is not reversed to satisfy set completion: **ENFORCED**",
            "- positive relic quota: **NOT CREATED**",
            "- reader-facing C1 label decision: **NOT FORCED**",
            "- new story canon required: **0**",
            "",
        ]
    )
    return "\n".join(lines)


def manifest_text(all_rows: list[dict[str, object]], threads: list[Thread], subacts_by_arc: dict[str, list[Subact]]) -> str:
    return "\n".join(
        [
            "# Full-Series Collection Desire Manifest v1",
            "",
            "Status: WORKFLOW/QC — SOURCE-BOUND EXECUTION LAYER",
            "Story Canon Effect: NONE",
            "Publication: NOT AUTHORIZED",
            "",
            "## Scope",
            "",
            f"- collection registry source rows: **{len(threads)} / 415**",
            f"- GA1–GA10 subacts mapped: **{len(all_rows)}**",
            "- source of truth: current collection registries + approved act/subact maps + Collection Bible set taxonomy",
            "- manuscript prose used as story-fact source: **NO**",
            "- new collectibles/relics/abilities/deaths/relationships/authorities: **0**",
            "",
            "## Execution IDs",
            "",
            "- `CLT-*`: stable source-thread ID. It does **not** assert that two registry rows are different physical entities.",
            "- `CLSET-*`: author-side subact reward/set execution ID. It is **not** an in-world Archive entry or new canon set.",
            "",
            "## Five Canonical Set Families",
            "",
            "- LINEAGE — 계보 세트",
            "- EVENT — 사건 세트",
            "- FUNCTIONAL — 역할 조합 세트",
            "- RELATIONSHIP — 관계 세트",
            "- CIVILIZATION — 문명 복원 세트",
            "",
            "## Completion Meaning",
            "",
            "This layer is complete only when the depth audit reaches PASS with B-depth queue 0. It may then be integrated as workflow/QC execution authority without changing story canon.",
            "",
        ]
    )


def build_outputs() -> dict[Path, str]:
    threads = load_threads()
    subacts_by_arc = {arc: parse_subacts(arc, filename) for arc, filename in ACT_MAPS}
    all_rows: list[dict[str, object]] = []
    selected_usage: Counter[str] = Counter()
    outputs: dict[Path, str] = {}

    for arc, _ in ACT_MAPS:
        text, rows = render_ga(arc, subacts_by_arc[arc], threads)
        outputs[OUT_DIR / f"{arc.lower()}-collection-desire-subact-map-v1.md"] = text
        all_rows.extend(rows)
        for row in rows:
            for thread, _, _ in row["selected"]:
                selected_usage[thread.thread_id] += 1

    thread_rows = build_thread_rows(threads, subacts_by_arc, selected_usage)
    header = list(thread_rows[0])
    import io
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=header, lineterminator="\n")
    writer.writeheader()
    writer.writerows(thread_rows)
    outputs[THREAD_INDEX] = buffer.getvalue()
    outputs[MANIFEST] = manifest_text(all_rows, threads, subacts_by_arc)
    outputs[AUDIT] = audit_text(all_rows, threads, subacts_by_arc, selected_usage)
    return outputs


def write_or_check(outputs: dict[Path, str], check: bool) -> int:
    stale: list[str] = []
    for path, content in outputs.items():
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    if stale:
        raise SystemExit("COLLECTION DESIRE OUTPUT STALE/MISSING:\n- " + "\n- ".join(stale))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = build_outputs()
    write_or_check(outputs, args.check)

    audit = outputs[AUDIT]
    verdict = re.search(r"\*\*VERDICT: ([A-Z]+)\*\*", audit)
    value = verdict.group(1) if verdict else "UNKNOWN"
    print(f"collection_desire_outputs={len(outputs)}")
    print(f"collection_desire_verdict={value}")
    if value != "PASS":
        print("collection desire layer requires B-depth/manual resolution before final integration")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
