#!/usr/bin/env python3
"""Generate the Obsidian story-graph navigation layer under docs/_graph/.

    python tools/build_story_graph.py            write the graph
    python tools/build_story_graph.py --check    fail if the graph is out of date

The graph is generated, never hand-edited. Every edge is read out of an
approved source by ``story_graph_sources``; if an act map, Context Pack,
writer-activation overlay or Collection Desire map is re-cut, regenerating
re-points every node instead of leaving them silently stale. The node count is
derived from the act maps, never asserted.

The graph holds no story facts. It is a thin navigation surface over documents
that already own the facts (CLAUDE.md section 3, single source of truth).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import story_graph_sources as S  # noqa: E402

ROOT = S.ROOT
GRAPH = S.GRAPH
LAST_REVIEWED = "2026-08-22"

BANNER = (
    "> [!warning] 생성 문서 — 직접 편집하지 마십시오\n"
    "> `python tools/build_story_graph.py`가 이 파일을 덮어씁니다.\n"
    "> 이 노트는 탐색 허브이며 정본이 아닙니다. 사건·날짜·상태·권한은 링크된 정본이 소유합니다."
)

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

SERIES_LEDGERS = [
    "series-payoff-ledger-v1",
    "final-payoff-scene-ledger-locked-v1",
    "named-loss-and-irreversible-transformation-ledger-v1",
]

STATE_CHECKPOINTS = [
    "ga1-10-state-checkpoint-matrix-v1",
    "ga1-10-operational-checkpoint-snapshots-v1",
]

DETAIL_PRODUCTION_INDEX = "episodes-101-1100-detail-production-standard-and-batch-map-v1"

BOUNDARY = (
    "이 허브는 새 사건·인물·기체·함선·권한·기술·관계·사망·손실을 만들지 않는다. "
    "충돌하면 ① 작가의 현재 지시 ② 정본·개정·errata ③ 액트맵과 상세 회차 카드 "
    "④ 상태·손실·회수 장부 ⑤ 실행층(Context/Activation/CLSET) 순서로 해석한다."
)


def link(stem: str, anchor: str = "", label: str = "") -> str:
    target = "%s#%s" % (stem, anchor) if anchor else stem
    return "[[%s|%s]]" % (target, label) if label else "[[%s]]" % target


def header(title: str, fields: list) -> list:
    out = ["# %s" % title, ""]
    out += ["%s: %s" % (k, v) for k, v in fields]
    out += ["", BANNER, ""]
    return out


def write(path: Path, lines: list, produced: dict) -> None:
    body = "\n".join(lines).rstrip() + "\n"
    produced[path] = body


# ---------------------------------------------------------------------------
# Domain-state hubs — static routing tables over existing registries/bibles.
# ---------------------------------------------------------------------------

DOMAIN_HUB_SPEC = {
    "graph-state-characters": (
        "Graph State Hub — Characters",
        "NOT A CHARACTER SOURCE",
        ["index-characters", "docs/_entities/README", "core-canonical-names-and-voice-lock-v1",
         "ga1-10-state-checkpoint-matrix-v1", "ga1-10-operational-checkpoint-snapshots-v1",
         "grand-act-character-faction-matrix-v1"],
        ["collection-desire-and-reader-memory-completion-scorecard-2026-08-20",
         "reference-deconstruction-and-anti-similarity-collection-v1",
         "reference-similarity-and-ending-blindspot-sweep-v1"],
        "정확한 외형은 승인된 비주얼 문서와 작가 결정이 소유한다. 이 허브는 외형 사실을 만들지 않는다.",
    ),
    "graph-state-collection": (
        "Graph State Hub — Collection / Reader Desire",
        "NOT A COLLECTION SOURCE",
        ["index-collection", "collection-desire-master-architecture-and-index-audit-v1",
         "galactic-legacy-collection-bible-v1", "full-series-collection-desire-manifest-v1"],
        ["collection-desire-and-reader-memory-completion-scorecard-2026-08-20"],
        "발견 → 획득·연결 → 사용·조합 → 비용·거절·손실 → 다음 욕망의 경로를 추적한다. "
        "정확한 목표 상태는 GA 등록부와 장면·상태 문서가 소유한다.",
    ),
    "graph-state-frames": (
        "Graph State Hub — Maneuver Frames",
        "NOT A HARDWARE SOURCE",
        ["index-frames", "maneuver-frame-lineup-master-architecture-v1",
         "frame-formation-combat-and-collectibility-integration-audit-v1",
         "docs/_entities/frames/07호"],
        [],
        "섀시·계보·현재 운용 상태·소유권·손상·정비·독자 인지를 링크된 정본으로 추적한다. "
        "이 허브에서 새 기체를 만들지 않는다.",
    ),
    "graph-state-ships": (
        "Graph State Hub — Ships / Hulls",
        "NOT A SHIP SOURCE",
        ["index-craft", "named-hull-registry-and-naming-grammar-v1", "first-ship-bible-v1",
         "ga1-10-operational-checkpoint-snapshots-v1"],
        [],
        "선체 권원·custody, 승조 권한, 추진, 손상, 내부·서비스 역할, 영구 손실을 정본에서 추적한다.",
    ),
    "graph-state-weapons-parts": (
        "Graph State Hub — Weapons / Parts",
        "NOT AN ITEM SOURCE",
        ["named-weapon-and-part-registry-v1", "index-collection",
         "counter-collection-and-intelligence-war-bible-v1"],
        ["collection-desire-and-reader-memory-completion-scorecard-2026-08-20"],
        "기능·탑재체·호환·인증·custody·손상·비용을 추적한다. 후보 행은 이 허브를 통해 정본이 되지 않는다.",
    ),
    "graph-state-relics-provenance": (
        "Graph State Hub — Relics / Provenance / Records",
        "NOT A RELIC SOURCE",
        ["named-relic-and-provenance-registry-v1", "index-collection",
         "series-payoff-ledger-v1", "final-payoff-scene-ledger-locked-v1"],
        [],
        "물리 객체, 유래, 정당한 보관자, 청구, 해석 변화, 회수를 분리해 추적한다. "
        "기록·권리는 자동으로 전리품이 되지 않는다.",
    ),
    "graph-state-technology": (
        "Graph State Hub — Technology / Lineage",
        "NOT A TECHNOLOGY SOURCE",
        ["named-technology-lineage-registry-v1", "technology-era-and-interoperability-bible-v1",
         "index-collection"],
        [],
        "이론 → 시제·공정 → 검증 → 인증 → 교육·확산 → 거버넌스를 추적한다. "
        "설계도만으로 산업 능력이 생기지 않는다.",
    ),
    "graph-state-factions-institutions": (
        "Graph State Hub — Factions / Institutions",
        "NOT A FACTION SOURCE",
        ["index-factions", "named-faction-and-institution-registry-v1",
         "faction-succession-culture-visual-identity-matrix-v1",
         "ga1-10-state-checkpoint-matrix-v1"],
        [],
        "구성원, 권한 범위, 승계, 내부 분파, 서비스, 강제력의 그림자, 현재 제도 상태를 추적한다. "
        "제도를 지도자 한 명으로 축약하지 않는다.",
    ),
    "graph-state-places-routes": (
        "Graph State Hub — Places / Routes / Nodes",
        "NOT A WORLD SOURCE",
        ["index-world", "named-place-and-corridor-registry-v1", "master-series-chronology-v1",
         "ga1-10-operational-checkpoint-snapshots-v1"],
        [],
        "장소 기능, 관할, 서비스 상태, 손상, 항로 접근, 일상 담지자를 추적한다. "
        "발견·접근을 소유·통치·자치와 동일시하지 않는다.",
    ),
    "graph-state-visual-memory": (
        "Graph State Hub — Visual / Reader Memory",
        "QC BRIDGE ONLY",
        ["visual-language-costume-architecture-and-concept-brief-v1",
         "faction-succession-culture-visual-identity-matrix-v1"],
        ["collection-desire-and-reader-memory-completion-scorecard-2026-08-20",
         "reference-deconstruction-and-anti-similarity-collection-v1",
         "reference-similarity-and-ending-blindspot-sweep-v1"],
        "전면 대상은 실루엣·재질·동작·감각 앵커·흉터·재등장으로 추적 가능해야 한다. "
        "정확한 얼굴·머리·체형·의상·일러스트 구성은 승인된 소스와 작가 잠금이 통제한다.",
    ),
    "graph-state-loss-payoff-authority": (
        "Graph State Hub — Loss / Payoff / Authority",
        "NOT A STATE SOURCE",
        ["series-payoff-ledger-v1", "final-payoff-scene-ledger-locked-v1",
         "named-loss-and-irreversible-transformation-ledger-v1",
         "m001-m020-early-clue-episode-ledger-v1",
         "ga1-10-state-checkpoint-matrix-v1", "ga1-10-operational-checkpoint-snapshots-v1",
         "continuity-issues"],
        [S.ENDING_AMENDMENT_STEM, S.ENDING_CROSSWALK_STEM, S.ENDING_DECISION_STEM],
        "영구 손실, 현재 권한 보유자, 거부된 권한, 회수 시점, 미해결 청구, 연속성 충돌을 추적한다. "
        "이 허브는 영구 손실을 복구하거나 권한을 이전할 수 없다.",
    ),
}


def build_domain_hubs(produced: dict) -> None:
    for stem, (title, guard, routes, qc, note) in DOMAIN_HUB_SPEC.items():
        lines = header(title, [
            ("Status", "CANON FOR NAVIGATION / %s" % guard),
            ("Graph Node", "DOMAIN STATE"),
            ("Last Reviewed", LAST_REVIEWED),
        ])
        lines += ["## 정본 경로", ""]
        lines += ["- %s" % link(r) for r in routes]
        if qc:
            lines += ["", "## QC / 독자 기억 가드", ""]
            lines += ["- %s" % link(r) for r in qc]
        lines += ["", "## 경계", "", note, "", BOUNDARY, "",
                  "## 상위", "", "- %s" % link("story-graph-root")]
        write(GRAPH / "state" / ("%s.md" % stem), lines, produced)


# ---------------------------------------------------------------------------
# Nodes
# ---------------------------------------------------------------------------

def build_root(series: list, produced: dict) -> None:
    lines = header("Story Graph Root — 《은하유산록》", [
        ("Status", "CANON FOR NAVIGATION / NOT A STORY SOURCE"),
        ("Graph Node", "SERIES ROOT"),
        ("Last Reviewed", LAST_REVIEWED),
        ("Source Authority", " · ".join(
            link(x) for x in ["architecture-rules", "1000-episode-grand-act-map-v1",
                              "master-series-chronology-v1", "effective-canon-status-manifest-v1"])),
    ])
    lines += ["옵시디언 볼트를 저장소 루트에서 열고 이 노트에서 시작한다. "
              "여기서 대액트 → 액트 → 서브액트 → 실행층(Context / Writer Activation / CLSET) → "
              "현재 상태로 내려간다.", "",
              "## Grand Acts", "",
              "| GA | Episodes | Hub | Act Map | Collection | State |",
              "|---|---:|---|---|---|---|"]
    for g in series:
        lines.append("| GA%02d | E%d–E%d | %s | %s | %s | %s |" % (
            g.ga, g.start, g.end, link(g.stem),
            link(S.ACT_MAP_STEM[g.ga]), link(S.COLLECTION_REGISTRY_STEM[g.ga]),
            link(g.spine_stem)))
    lines += ["", "## 시간축", "",
              "%d개 서브액트는 %s(GA%02d %s)부터 %s(GA%02d %s)까지 previous/next 한 줄로 이어진다." % (
                  sum(len(g.subacts) for g in series),
                  link(series[0].acts[0].subacts[0].stem), series[0].ga,
                  series[0].acts[0].subacts[0].subact_id,
                  link(series[-1].acts[-1].subacts[-1].stem), series[-1].ga,
                  series[-1].acts[-1].subacts[-1].subact_id),
              "",
              "## 현재 상태 도메인 허브", ""]
    lines += ["- %s" % link(x) for x in DOMAIN_HUBS]
    lines += ["", "## 실행층 정본", "",
              "- Context 규격: %s" % link("context-pack-tangible-reader-memory-execution-spec-proposal-v1"),
              "- Context 생성 장부: %s" % link(S.CONTEXT_MANIFEST_STEM),
              "- Writer Activation 장부: %s" % link(S.ACTIVATION_MANIFEST_STEM),
              "- Collection Desire / CLSET 장부 (%d 서브액트): %s" % (
                  sum(len(g.subacts) for g in series), link(S.DESIRE_MANIFEST_STEM)),
              "- 회차 작업지시서: %s" % link("episode-briefs"),
              "- 원고 생산 워크플로: %s" % link("manuscript-production-workflow-v1"),
              "- 게이트·정본 상태: %s · %s" % (
                  link("effective-canon-status-manifest-v1"),
                  link("prewriting-execution-redteam-v2-final-verdict-2026-08-22")),
              "", "## 결말 정본", "",
              "GA10 D구간(E1076–E1100)의 유효 결말은 %s와 그 결정 기록 %s가 소유한다. "
              "구 카드의 결말 배치는 %s가 이력으로 보존한다." % (
                  link(S.ENDING_AMENDMENT_STEM), link(S.ENDING_DECISION_STEM),
                  link(S.ENDING_CROSSWALK_STEM)),
              "", "## 경계", "", BOUNDARY, "",
              "- 그래프 규약: %s" % link("docs/_graph/README"),
              "- 저장소 입구: %s · %s" % (link("HOME"), link("CATALOG")),
              "- 검증 기록: %s" % link("obsidian-story-graph-deep-wiring-audit-2026-08-22")]
    write(GRAPH / "story-graph-root.md", lines, produced)


def build_ga_hub(g, series: list, produced: dict) -> None:
    prev = "graph-ga%02d-hub" % (g.ga - 1) if g.ga > 1 else ""
    nxt = "graph-ga%02d-hub" % (g.ga + 1) if g.ga < 10 else ""
    lines = header("Graph GA%02d Hub — E%d–E%d" % (g.ga, g.start, g.end), [
        ("Status", "CANON FOR NAVIGATION / NOT A STORY SOURCE"),
        ("Graph Node", "GRAND ACT"),
        ("GA", "%02d" % g.ga),
        ("Episodes", "E%d–E%d (%d)" % (g.start, g.end, g.end - g.start + 1)),
        ("Last Reviewed", LAST_REVIEWED),
    ])
    lines += ["## 정본 소스", "",
              "- Act Map: %s" % link(S.ACT_MAP_STEM[g.ga]),
              "- 대서사 지도: %s" % link("1000-episode-grand-act-map-v1"),
              "- 수집 등록부: %s" % link(S.COLLECTION_REGISTRY_STEM[g.ga]),
              "- 현재 상태: %s" % link(g.spine_stem),
              "", "## Acts", "",
              "| Act | 제목 | Episodes | Hub | Subacts |",
              "|---|---|---:|---|---|"]
    for a in g.acts:
        subs = " · ".join(link(s.stem, label=s.subact_id) for s in a.subacts)
        lines.append("| %s | %s | E%d–E%d | %s | %s |" % (
            a.act_id, a.title, a.start, a.end, link(a.stem), subs))
    lines += ["", "## 실행층", "",
              "- Context Pack: %s" % link(S.CONTEXT_PACK_STEM[g.ga]),
              "- Writer Activation: %s" % link(S.ACTIVATION_STEM[g.ga]),
              "- Collection Desire / CLSET: %s" % link(S.DESIRE_STEM[g.ga]),
              "- 회차 작업지시서: %s" % link("episode-briefs")]
    if g.ga == 1:
        lines.append("- E001–E010 수동 Context: %s" % link(S.MANUAL_CONTEXT_STEM))
    else:
        lines.append("- 상세설계 배치 지도: %s" % link(DETAIL_PRODUCTION_INDEX))
    if g.ga == 10:
        lines += ["", "## 결말 정본", "",
                  "- %s" % link(S.ENDING_AMENDMENT_STEM),
                  "- %s" % link(S.ENDING_CROSSWALK_STEM),
                  "- %s" % link(S.ENDING_DECISION_STEM)]
    lines += ["", "## 탐색", "", "- Series: %s" % link("story-graph-root")]
    if prev:
        lines.append("- Previous Grand Act: %s" % link(prev))
    if nxt:
        lines.append("- Next Grand Act: %s" % link(nxt))
    lines += ["", "## 경계", "", BOUNDARY]
    write(GRAPH / "ga" / ("%s.md" % g.stem), lines, produced)


def build_act_hub(g, a, produced: dict) -> None:
    idx = g.acts.index(a)
    lines = header("Graph GA%02d Act %s Hub — %s" % (g.ga, a.act_id, a.title), [
        ("Status", "CANON FOR NAVIGATION / NOT A STORY SOURCE"),
        ("Graph Node", "ACT"),
        ("GA", "%02d" % g.ga),
        ("Act", a.act_id),
        ("Episodes", "E%d–E%d (%d)" % (a.start, a.end, a.end - a.start + 1)),
        ("Last Reviewed", LAST_REVIEWED),
    ])
    lines += ["## 정본 소스", "",
              "- Act Map: %s" % link(S.ACT_MAP_STEM[g.ga], a.heading),
              "- 수집 등록부: %s" % link(S.COLLECTION_REGISTRY_STEM[g.ga]),
              "- 현재 상태: %s" % link(g.spine_stem),
              "", "## Subacts", "",
              "| Subact | 제목 | Episodes | Hub | CLSET |",
              "|---|---|---:|---|---|"]
    for s in a.subacts:
        lines.append("| %s | %s | E%d–E%d | %s | `%s` |" % (
            s.subact_id, s.title, s.start, s.end, link(s.stem), s.clset_id))
    lines += ["", "## 탐색", "",
              "- Series: %s" % link("story-graph-root"),
              "- Grand Act: %s" % link(g.stem)]
    if idx > 0:
        lines.append("- Previous Act: %s" % link(g.acts[idx - 1].stem))
    if idx < len(g.acts) - 1:
        lines.append("- Next Act: %s" % link(g.acts[idx + 1].stem))
    lines += ["", "## 경계", "", BOUNDARY]
    write(GRAPH / "acts" / ("%s.md" % a.stem), lines, produced)


def build_subact_hub(g, a, s, chain: list, produced: dict) -> None:
    pos = chain.index(s)
    lines = header("Graph GA%02d Subact %s Hub — %s" % (g.ga, s.subact_id, s.title), [
        ("Status", "CANON FOR NAVIGATION / NOT A STORY SOURCE"),
        ("Graph Node", "SUBACT"),
        ("GA", "%02d" % g.ga),
        ("Act", a.act_id),
        ("Subact", s.subact_id),
        ("Episodes", "E%d–E%d (%d)" % (s.start, s.end, s.end - s.start + 1)),
        ("CLSET", "`%s`" % s.clset_id),
        ("Last Reviewed", LAST_REVIEWED),
    ])

    lines += ["## 계층", "",
              "- Series: %s" % link("story-graph-root"),
              "- Grand Act: %s" % link(g.stem),
              "- Act: %s" % link(a.stem)]
    if pos > 0:
        p = chain[pos - 1]
        lines.append("- Previous Subact: %s (GA%02d %s / E%d–E%d)"
                     % (link(p.stem), p.ga, p.subact_id, p.start, p.end))
    else:
        lines.append("- Previous Subact: 없음 — 시리즈 시작점")
    if pos < len(chain) - 1:
        n = chain[pos + 1]
        lines.append("- Next Subact: %s (GA%02d %s / E%d–E%d)"
                     % (link(n.stem), n.ga, n.subact_id, n.start, n.end))
    else:
        lines.append("- Next Subact: 없음 — 시리즈 종점, %s로 복귀" % link("story-graph-root"))

    lines += ["", "## 승인 구조 (Approved Structure)", "",
              "- Act Map: %s" % link(S.ACT_MAP_STEM[g.ga], s.act_heading)]
    design = [x for x in s.state_sources if x[1] == "episode design"]
    if design:
        lines += ["- 상세 회차 설계: %s" % " · ".join(link(x[0]) for x in design)]
    elif g.ga >= 2:
        lines += ["- 상세설계 배치 지도: %s" % link(DETAIL_PRODUCTION_INDEX)]

    lines += ["", "## 집필 실행층 (E%d–E%d)" % (s.start, s.end), ""]
    if s.context_anchor:
        lines += ["- Context Pack: %s" % link(S.CONTEXT_PACK_STEM[g.ga], s.context_anchor,
                                              "%s → E%d" % (S.CONTEXT_PACK_STEM[g.ga], s.start)),
                  "- Writer Activation: %s" % link(S.ACTIVATION_STEM[g.ga], s.activation_anchor,
                                                   "%s → E%d" % (S.ACTIVATION_STEM[g.ga], s.start))]
    else:
        lines += ["- Context Pack: %s (E001–E010은 수동 FULL 팩이 생성층보다 우선한다)"
                  % link(S.MANUAL_CONTEXT_STEM),
                  "- Writer Activation: %s (E001–E010 Depth-A override)"
                  % link(S.MANUAL_ACTIVATION_STEM)]
    lines += ["- 회차 작업지시서: %s" % link("episode-briefs"),
              "- Context 규격: %s" % link("context-pack-tangible-reader-memory-execution-spec-proposal-v1"),
              "- 원고 워크플로: %s" % link("manuscript-production-workflow-v1")]

    lines += ["", "## 수집욕 / CLSET", "",
              "- `%s`: %s" % (s.clset_id, link(S.DESIRE_STEM[g.ga], s.desire_heading,
                                               "%s → %s" % (S.DESIRE_STEM[g.ga], s.subact_id))),
              "- GA 수집 등록부: %s" % link(S.COLLECTION_REGISTRY_STEM[g.ga]),
              "- 전 시리즈 수집 장부: %s" % link(S.DESIRE_MANIFEST_STEM),
              "- 도메인 허브: %s · %s" % (link("graph-state-collection"),
                                          link("graph-state-relics-provenance")),
              "",
              "발견 → 획득·연결 → 사용·조합 → 비용·거절·손실 → 다음 욕망의 순서는 CLSET 항목이 소유한다. "
              "사람·공동체·영토는 소유물이 아니며 동의·거절·이탈 가능성을 유지한다."]

    lines += ["", "## 현재 상태 · 손실 · 회수 · 권한", "",
              "- GA 상태 척추: %s" % link(g.spine_stem)]
    for kind in ("collection / loss state", "operations state",
                 "institution / authority state", "law / evidence state", "QC cross-audit"):
        rows = [x[0] for x in s.state_sources if x[1] == kind]
        if rows:
            lines.append("- %s: %s" % (kind, " · ".join(link(r) for r in rows)))
    lines.append("- 시리즈 장부: %s" % " · ".join(link(x) for x in SERIES_LEDGERS))
    lines.append("- 도메인 허브: %s" % link("graph-state-loss-payoff-authority"))

    if g.ga == 10 and a.letter == "d":
        # Links only. The chronology lock, the 07 / 파루스 / Ern endpoints, the
        # relationship architecture and the M-019 placement are story facts; a
        # navigation hub that restates them becomes a second canon the moment the
        # amendment is re-cut (CLAUDE.md section 3, and the section 12 propagation
        # failure). Name what the source owns; do not copy what it says.
        lines += ["", "## 결말 정본 (E1076–E1100)", "",
                  "- 유효 정본: %s" % link(S.ENDING_AMENDMENT_STEM),
                  "- 결정 기록: %s" % link(S.ENDING_DECISION_STEM),
                  "- 구/신 배치 대조: %s" % link(S.ENDING_CROSSWALK_STEM),
                  "",
                  "연표 잠금, 07·파루스·Ern의 최종 상태, 핵심 관계 구조, M-019 배치는 "
                  "위 정본이 소유한다. 이 허브는 그 내용을 재서술하지 않는다. "
                  "구 상세 카드의 배치는 대조 문서가 이력으로 보존한다."]

    lines += ["", "## 경계", "", BOUNDARY]
    write(GRAPH / "subacts" / ("%s.md" % s.stem), lines, produced)


def build_state_spine(g, produced: dict) -> None:
    lines = header("GA%02d Current-State Spine — E%d–E%d" % (g.ga, g.start, g.end), [
        ("Status", "CANON FOR NAVIGATION / NOT A STATE SOURCE"),
        ("Graph Node", "GA STATE SPINE"),
        ("GA", "%02d" % g.ga),
        ("Episodes", "E%d–E%d" % (g.start, g.end)),
        ("Last Reviewed", LAST_REVIEWED),
    ])
    lines += ["## 이 구간의 정본", "",
              "- Act Map: %s" % link(S.ACT_MAP_STEM[g.ga]),
              "- 수집 등록부: %s" % link(S.COLLECTION_REGISTRY_STEM[g.ga]),
              "- Context Pack: %s" % link(S.CONTEXT_PACK_STEM[g.ga]),
              "- Writer Activation: %s" % link(S.ACTIVATION_STEM[g.ga]),
              "- Collection Desire / CLSET: %s" % link(S.DESIRE_STEM[g.ga]),
              "- 회차 작업지시서: %s" % link("episode-briefs"),
              "- Context 규격: %s" % link("context-pack-tangible-reader-memory-execution-spec-proposal-v1")]
    if g.ga == 1:
        lines.append("- E001–E010 수동 Context: %s" % link(S.MANUAL_CONTEXT_STEM))
    else:
        lines.append("- 상세설계 배치 지도: %s" % link(DETAIL_PRODUCTION_INDEX))
    lines += ["- 전 구간 상태 체크포인트: %s" % " · ".join(link(x) for x in STATE_CHECKPOINTS),
              "- 시리즈 연표: %s" % link("master-series-chronology-v1")]

    docs = S.range_documents()
    rows = S.overlapping(docs, g.ga, g.start, g.end)
    grouped = {}
    for stem, kind in rows:
        grouped.setdefault(kind, []).append(stem)
    lines += ["", "## 구간 상태 문서", ""]
    for kind in ("episode design", "collection / loss state", "operations state",
                 "institution / authority state", "law / evidence state", "QC cross-audit"):
        if kind in grouped:
            lines += ["**%s**" % kind, ""]
            lines += ["- %s" % link(x) for x in grouped[kind]]
            lines.append("")

    lines += ["## 도메인 fan-out", ""]
    lines += ["- %s" % link(x) for x in DOMAIN_HUBS]
    lines += ["", "## 탐색", "",
              "- Series: %s" % link("story-graph-root"),
              "- Grand Act: %s" % link(g.stem),
              "- Acts: %s" % " · ".join(link(a.stem, label=a.act_id) for a in g.acts)]
    if g.ga == 10:
        lines += ["", "## 결말 정본", "",
                  "- %s" % link(S.ENDING_AMENDMENT_STEM),
                  "- %s" % link(S.ENDING_CROSSWALK_STEM)]
    lines += ["", "## 경계", "", BOUNDARY]
    write(GRAPH / "state" / ("%s.md" % g.spine_stem), lines, produced)


README = """# Story Graph Navigation Layer — 옵시디언 서사 그래프 계층

Status: CANON FOR NAVIGATION / NOT A STORY OR SETTINGS SOURCE
Owner Agents: A00 PM / N02 Act Architecture / N03 Episode / O01 Canon / X04 Continuity
Last Reviewed: {reviewed}
Depends On: [[architecture-rules]], [[1000-episode-grand-act-map-v1]], [[effective-canon-status-manifest-v1]], [[context-pack-tangible-reader-memory-execution-spec-proposal-v1]], [[docs/_entities/README]]
Used By: Obsidian Graph View, act/subact navigation, Context Pack preparation, continuity review
Open Risks: navigation hubs accidentally becoming a duplicate canon source; graph clutter from creating empty entity notes

{banner}

## 1. 목적

이 폴더는 이미 존재하는 정본·Approved Structure·실행층·상태 장부를 **옵시디언에서 실제로 탐색 가능한 그래프**로 연결한다.

이 계층은 새 사건·설정·인물·기체·함선·장소·권한을 만들지 않는다. 정확한 사실과 회차 범위는 기존 정본이 소유한다.

## 2. 볼트 여는 법

- **Vault root = 저장소 루트** (`galactic-legacy-archive/`). `docs/`를 볼트로 열면 `[[CLAUDE]]`와 `[[docs/_entities/README]]` 형태의 전체 경로 링크가 깨진다.
- 시작 문서: [[story-graph-root]]
- 색인 진입점: [[HOME]] · [[CATALOG]] · [[episode-briefs]]
- 필요한 커뮤니티 플러그인은 없다. 기본 Obsidian의 위키링크·백링크·그래프뷰만으로 전 경로가 동작한다.

## 3. 경로

```text
[[story-graph-root]]
→ Grand Act Hub ({gas})
→ Act Hub ({acts})
→ Subact Hub ({subacts})
├─→ Act Map 해당 서브액트 표제
├─→ 상세 회차 설계 카드
├─→ Context Pack 해당 회차 / Writer Activation 해당 회차
├─→ Collection Desire CLSET 해당 서브액트
├─→ 구간 상태·손실·권한 문서
└─→ GA Current-State Spine
       → Domain-State Hub (11)
       → registry / bible / entity note / loss-payoff ledger
```

Subact는 {first}부터 {last}까지 previous/next 링크로 하나의 시간축 체인을 이룬다.

## 4. 물리 규모

`docs/_graph/` Markdown 파일은 **{total}개**다. 이 수는 액트맵에서 파생한다 — 손으로 유지하지 않는다.

| 종류 | 수 |
|---|---:|
| 규약 README | 1 |
| Series Root | 1 |
| Grand Act Hub | {gas} |
| Act Hub | {acts} |
| Subact Hub | {subacts} |
| GA Current-State Spine | {gas} |
| Domain-State Hub | {domains} |

## 5. 노드 규칙

1. 허브는 탐색 전용이다. 새 story fact를 쓰지 않는다.
2. 부모와 자식은 서로 링크해 옵시디언 백링크가 양방향으로 작동하게 한다.
3. Subact 허브는 액트맵 표제·상세 카드·Context·Writer Activation·CLSET·GA 등록부·상태 척추·손실/회수 장부로 연결한다.
4. Current-State Spine은 인물·수집·기체·함선·무장·유물·기술·세력·장소·비주얼·손실/회수 도메인 허브로 fan-out한다.
5. exact entity note가 아직 없으면 새 사실을 만들지 않고 index/registry로 연결한다.
6. 197명 전원, 612성계 전부에 빈 엔티티 노트를 만들지 않는다. front-stage 승격 시에만 [[docs/_entities/README]] 규칙으로 개체 노트를 만든다.
7. **원고 본문에는 위키링크를 넣지 않는다.** 그래프는 원고 파일을 링크하지 않는다.
8. Graph node가 더 최신이라는 이유로 액트맵, 상세카드, 상태장부, 손실장부, payoff ledger를 덮어쓰지 않는다.
9. 비주얼 graph는 설계 방향·독자 기억·anti-similarity guard를 연결하지만 exact face/hair/body/costume를 자동 정본화하지 않는다.
10. 현재 작품의 정식 hierarchy는 [[architecture-rules]]를 그대로 따른다. **다른 프로젝트의 `Volume` 또는 고정 `60 Subact` 구조를 가져오지 않는다.**

## 6. 현재 상태 해석 순서

1. 작가의 현재 지시 / Canon Amendment / Errata;
2. 액트맵 / 해당 상세 회차 카드;
3. GA Current-State Spine이 가리키는 구간 상태 문서;
4. state checkpoint / operational snapshot;
5. GA 수집 등록부;
6. 도메인 registry/bible;
7. front-stage 엔티티 노트가 있으면 그것;
8. 손실/회수/권한 장부;
9. 비주얼·독자기억 QC;
10. Context Pack / Writer Activation 실행 필드.

Context Pack과 Writer Activation은 이 결과를 집필 가능한 형태로 번역할 뿐 상위 사실을 바꾸지 않는다.

GA10 E1076–E1100은 [[{ending}]]가 유효 정본이다.

## 7. 생성과 검증

```bash
python tools/build_story_graph.py          # 생성
python tools/build_story_graph.py --check  # 낡았으면 실패 (CI가 실행)
python tools/validate_story_graph.py --selftest
python tools/validate_story_graph.py
```

- 이 폴더의 모든 파일은 생성물이다. **직접 편집하지 않는다** — 다음 실행이 덮어쓴다.
- 액트맵·Context·Activation·CLSET을 바꾸면 같은 PR에서 재생성한다. CI의 `--check`가 강제한다.
- QC 기록: [[obsidian-story-graph-deep-wiring-audit-2026-08-22]]

## 8. 그래프 필터

노드 머리의 `Graph Node`, `GA`, `Act`, `Subact` 표기로 옵시디언 검색·필터를 적용한다.

- `path:docs/_graph/ga`
- `path:docs/_graph/acts`
- `path:docs/_graph/subacts`
- `path:docs/_graph/state`

## 9. 진입

- [[story-graph-root]]
"""


def build(produced: dict) -> None:
    series = S.load_series()
    chain = S.ordered_subacts(series)
    build_root(series, produced)
    build_domain_hubs(produced)
    for g in series:
        build_ga_hub(g, series, produced)
        build_state_spine(g, produced)
        for a in g.acts:
            build_act_hub(g, a, produced)
            for s in a.subacts:
                build_subact_hub(g, a, s, chain, produced)
    gas = len(series)
    acts = sum(len(g.acts) for g in series)
    subacts = len(chain)
    write(GRAPH / "README.md",
          README.format(reviewed=LAST_REVIEWED, banner=BANNER,
                        ending=S.ENDING_AMENDMENT_STEM,
                        gas=gas, acts=acts, subacts=subacts,
                        domains=len(DOMAIN_HUBS),
                        total=2 + gas + acts + subacts + gas + len(DOMAIN_HUBS),
                        first="GA%02d %s" % (series[0].ga, chain[0].subact_id),
                        last="GA%02d %s" % (series[-1].ga, chain[-1].subact_id),
                        ).rstrip().split("\n"),
          produced)


def main(argv: list) -> int:
    check = "--check" in argv
    produced: dict = {}
    build(produced)

    existing = set(GRAPH.rglob("*.md")) if GRAPH.exists() else set()
    stale = sorted(existing - set(produced))
    changed = []
    for path, body in sorted(produced.items()):
        if not path.exists() or path.read_text(encoding="utf-8") != body:
            changed.append(path)

    if check:
        if changed or stale:
            print("story graph is out of date. Run: python tools/build_story_graph.py")
            for p in changed[:10]:
                print("  changed: %s" % p.relative_to(ROOT).as_posix())
            if len(changed) > 10:
                print("  ... and %d more" % (len(changed) - 10))
            for p in stale:
                print("  orphaned: %s" % p.relative_to(ROOT).as_posix())
            return 1
        print("story graph is current (%d nodes)" % len(produced))
        return 0

    for p in stale:
        p.unlink()
    for path, body in sorted(produced.items()):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
    print("wrote %d story-graph nodes under docs/_graph" % len(produced))
    if stale:
        print("removed %d orphaned node(s)" % len(stale))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
