#!/usr/bin/env python3
"""Shared source parsing for the Obsidian story-graph navigation layer.

Both the generator (``build_story_graph.py``) and the validator
(``validate_story_graph.py``) read the repository through this module, so the
two can never disagree about what the act maps, Context Packs, writer
activation overlays and Collection Desire maps actually say.

Nothing here creates story canon. Every value is read out of an existing
approved document; the graph layer only re-expresses navigation edges.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
GRAPH = DOCS / "_graph"

ACT_LETTERS = "abcd"
DASH = "[-‐‑‒–—]"

# ---------------------------------------------------------------------------
# Source file map — one authoritative file per Grand Act per layer.
# ---------------------------------------------------------------------------

GA_EPISODES = {
    1: (1, 100),
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

ACT_MAP_STEM = {
    1: "first-100-act-map-v2-consolidated",
    2: "ga2-episodes-101-210-act-map-v1",
    3: "ga3-episodes-211-330-act-map-v1",
    4: "ga4-episodes-331-450-act-map-v1",
    5: "ga5-episodes-451-570-act-map-v1",
    6: "ga6-episodes-571-690-act-map-v1",
    7: "ga7-episodes-691-800-act-map-v1",
    8: "ga8-episodes-801-900-act-map-v1",
    9: "ga9-episodes-901-1000-act-map-v1",
    10: "ga10-episodes-1001-1100-act-map-v1",
}

COLLECTION_REGISTRY_STEM = {
    1: "first-100-collectible-registry-v1",
    10: "ga10-final-collection-and-payoff-registry-v1",
}
for _n in range(2, 10):
    COLLECTION_REGISTRY_STEM[_n] = "ga%d-collection-registry-v1" % _n

CONTEXT_PACK_DIR = DOCS / "13_writing_harness" / "context_packs" / "generated"
ACTIVATION_DIR = DOCS / "13_writing_harness" / "context_packs" / "activation"
DESIRE_DIR = DOCS / "09_collection" / "generated" / "desire_subact"

CONTEXT_PACK_STEM = {
    1: "ga1-e011-e100-context-packs-v1",
    2: "ga2-e101-e210-context-packs-v1",
    3: "ga3-e211-e330-context-packs-v1",
    4: "ga4-e331-e450-context-packs-v1",
    5: "ga5-e451-e570-context-packs-v1",
    6: "ga6-e571-e690-context-packs-v1",
    7: "ga7-e691-e800-context-packs-v1",
    8: "ga8-e801-e900-context-packs-v1",
    9: "ga9-e901-e1000-context-packs-v1",
    10: "ga10-e1001-e1100-context-packs-v1",
}

ACTIVATION_STEM = {
    1: "ga1-e011-e100-writer-activation-v1",
    2: "ga2-e101-e210-writer-activation-v1",
    3: "ga3-e211-e330-writer-activation-v1",
    4: "ga4-e331-e450-writer-activation-v1",
    5: "ga5-e451-e570-writer-activation-v1",
    6: "ga6-e571-e690-writer-activation-v1",
    7: "ga7-e691-e800-writer-activation-v1",
    8: "ga8-e801-e900-writer-activation-v1",
    9: "ga9-e901-e1000-writer-activation-v1",
    10: "ga10-e1001-e1100-writer-activation-v1",
}

DESIRE_STEM = {}
for _n in range(1, 11):
    DESIRE_STEM[_n] = "ga%d-collection-desire-subact-map-v1" % _n

# E001-E010 predate the generated full-series layer; the manual packs outrank it.
MANUAL_CONTEXT_STEM = "ga1-e001-e010-context-pack-status-index-v1"
MANUAL_ACTIVATION_STEM = "full-series-context-writer-activation-manifest-v1"
GENERATED_CONTEXT_FLOOR = 11

CONTEXT_MANIFEST_STEM = "full-series-context-pack-generated-manifest-v1"
ACTIVATION_MANIFEST_STEM = "full-series-context-writer-activation-manifest-v1"
DESIRE_MANIFEST_STEM = "full-series-collection-desire-manifest-v1"
THREAD_INDEX = DESIRE_DIR / "full-series-collection-thread-index-v1.csv"

ENDING_AMENDMENT_STEM = "ga10-ending-reconciliation-canon-amendment-2026-08-20"
ENDING_CROSSWALK_STEM = "ga10-e1076-1100-ending-reconciliation-crosswalk-and-audit-v1"
ENDING_DECISION_STEM = "decision-log-addendum-2026-08-20-ga10-ending"

# Directories whose range-encoded filenames carry per-episode execution state.
STATE_SOURCE_DIRS = {
    "docs/10_story_architecture/detail": "episode design",
    "docs/09_collection/detail": "collection / loss state",
    "docs/06_law": "law / evidence state",
    "docs/07_military/operations": "operations state",
    "docs/08_institutions": "institution / authority state",
    "docs/99_quality_control/detail": "QC cross-audit",
}

# Manuscript trees. The graph must never link into published prose.
MANUSCRIPT_DIR_NAMES = ("manuscript", "manuscripts", "원고")


@dataclass
class Subact:
    ga: int
    act_letter: str          # a/b/c/d
    index: int               # 1..4
    subact_id: str           # "A1" (GA1) or "2A-1" (GA2+)
    title: str
    start: int
    end: int
    act_heading: str = ""    # exact act-map heading text for this subact
    desire_heading: str = ""
    clset_id: str = ""
    context_anchor: str = ""
    activation_anchor: str = ""
    state_sources: list = field(default_factory=list)

    @property
    def stem(self) -> str:
        return "graph-ga%02d-subact-%s%d" % (self.ga, self.act_letter, self.index)


@dataclass
class Act:
    ga: int
    letter: str              # a/b/c/d
    act_id: str              # "A" (GA1) or "2A" (GA2+)
    title: str
    start: int
    end: int
    heading: str = ""
    subacts: list = field(default_factory=list)

    @property
    def stem(self) -> str:
        return "graph-ga%02d-act-%s" % (self.ga, self.letter)


@dataclass
class GrandAct:
    ga: int
    start: int
    end: int
    acts: list = field(default_factory=list)

    @property
    def stem(self) -> str:
        return "graph-ga%02d-hub" % self.ga

    @property
    def spine_stem(self) -> str:
        return "graph-ga%02d-state-spine" % self.ga

    @property
    def subacts(self) -> list:
        return [s for a in self.acts for s in a.subacts]


class SourceError(RuntimeError):
    """Raised when an approved source no longer matches what the graph reads."""


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


ACT_RE_GA1 = re.compile(r"^# ACT ([A-D]) %s (.+?) / Episodes (\d+)%s(\d+)\s*$" % (DASH, DASH))
SUB_RE_GA1 = re.compile(r"^## ([A-D]\d) %s (.+?) / Episodes (\d+)%s(\d+)\s*$" % (DASH, DASH))
ACT_RE = re.compile(r"^# ACT (\d+[A-D]) %s (.+?) / Episodes (\d+)%s(\d+)\s*$" % (DASH, DASH))
SUB_RE = re.compile(
    r"^## \d+\. Subact (\d+[A-D]%s\d) %s (.+?) / Episodes (\d+)%s(\d+)\s*$" % (DASH, DASH, DASH)
)


def parse_act_map(ga: int) -> list:
    path = DOCS / "10_story_architecture" / ("%s.md" % ACT_MAP_STEM[ga])
    if not path.exists():
        raise SourceError("act map missing: %s" % path.relative_to(ROOT))
    act_re, sub_re = (ACT_RE_GA1, SUB_RE_GA1) if ga == 1 else (ACT_RE, SUB_RE)

    acts: list = []
    for line in read(path).splitlines():
        m = act_re.match(line)
        if m:
            acts.append(
                Act(ga=ga, letter=m.group(1)[-1].lower(), act_id=m.group(1),
                    title=m.group(2).strip(), start=int(m.group(3)), end=int(m.group(4)),
                    heading=line[2:].strip())
            )
            continue
        m = sub_re.match(line)
        if m:
            sub_id = m.group(1)
            letter = re.search(r"[A-D]", sub_id).group(0).lower()
            if not acts or acts[-1].letter != letter:
                raise SourceError("GA%d subact %s has no preceding ACT heading" % (ga, sub_id))
            acts[-1].subacts.append(
                Subact(ga=ga, act_letter=letter, index=int(sub_id[-1]), subact_id=sub_id,
                       title=m.group(2).strip(), start=int(m.group(3)), end=int(m.group(4)),
                       act_heading=line[3:].strip())
            )

    if len(acts) != 4:
        raise SourceError("GA%d act map yielded %d acts, expected 4" % (ga, len(acts)))
    for a in acts:
        if len(a.subacts) != 4:
            raise SourceError(
                "GA%d act %s yielded %d subacts, expected 4" % (ga, a.act_id, len(a.subacts))
            )
        if [s.index for s in a.subacts] != [1, 2, 3, 4]:
            raise SourceError("GA%d act %s subact numbering is not 1..4" % (ga, a.act_id))
    return acts


EPISODE_HEADING = re.compile(r"^## E(\d+) ")


def episode_headings(path: Path) -> dict:
    """episode number -> exact ``## `` heading text (Obsidian anchor target)."""
    if not path.exists():
        raise SourceError("missing execution source: %s" % path.relative_to(ROOT))
    out: dict = {}
    for line in read(path).splitlines():
        m = EPISODE_HEADING.match(line)
        if m:
            out[int(m.group(1))] = line[3:].strip()
    return out


DESIRE_HEADING = re.compile(r"^## (\S+) %s (.+?) / E(\d+)%sE(\d+)\s*$" % (DASH, DASH))
CLSET_RE = re.compile(r"^- `SET_EXECUTION_ID`: `([^`]+)`")


def desire_headings(ga: int) -> dict:
    """subact id -> (exact heading, CLSET id, first episode, last episode)."""
    path = DESIRE_DIR / ("%s.md" % DESIRE_STEM[ga])
    if not path.exists():
        raise SourceError("missing collection desire map: %s" % path.relative_to(ROOT))
    out: dict = {}
    pending: dict = {}
    current = None
    for line in read(path).splitlines():
        m = DESIRE_HEADING.match(line)
        if m:
            current = m.group(1)
            pending[current] = (line[3:].strip(), int(m.group(3)), int(m.group(4)))
            continue
        if current:
            c = CLSET_RE.match(line)
            if c and current not in out:
                heading, s, e = pending[current]
                out[current] = (heading, c.group(1), s, e)
    return out


RANGE_STEMS = [
    re.compile(r"^ga(\d+)-e(\d+)-(\d+)-"),
    re.compile(r"^ga(\d+)-episodes-(\d+)-(\d+)-"),
]


def range_documents() -> list:
    """(ga, start, end, stem, source-kind) for every range-encoded design doc."""
    out: list = []
    for rel_dir, kind in STATE_SOURCE_DIRS.items():
        d = ROOT / rel_dir
        if not d.exists():
            continue
        for p in sorted(d.glob("*.md")):
            for rx in RANGE_STEMS:
                m = rx.match(p.stem)
                if m:
                    out.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), p.stem, kind))
                    break
    # GA1 scene cards live directly in 10_story_architecture, not in detail/.
    for p in sorted((DOCS / "10_story_architecture").glob("ga1-episodes-*.md")):
        m = re.match(r"^ga1-episodes-(\d+)-(\d+)-", p.stem)
        if m and "noncanon" not in p.stem:
            out.append((1, int(m.group(1)), int(m.group(2)), p.stem, "episode design"))
    return out


def overlapping(docs: list, ga: int, start: int, end: int) -> list:
    seen: set = set()
    out: list = []
    for g, s, e, stem, kind in docs:
        if g == ga and s <= end and e >= start and stem not in seen:
            seen.add(stem)
            out.append((stem, kind))
    return out


def load_series() -> list:
    """Parse every approved source the graph depends on. Raises on drift."""
    docs = range_documents()
    series: list = []
    for ga in range(1, 11):
        acts = parse_act_map(ga)
        start, end = GA_EPISODES[ga]
        if acts[0].start != start or acts[-1].end != end:
            raise SourceError(
                "GA%d act map covers E%d-E%d, expected E%d-E%d"
                % (ga, acts[0].start, acts[-1].end, start, end)
            )
        context = episode_headings(CONTEXT_PACK_DIR / ("%s.md" % CONTEXT_PACK_STEM[ga]))
        activation = episode_headings(ACTIVATION_DIR / ("%s.md" % ACTIVATION_STEM[ga]))
        desires = desire_headings(ga)

        for act in acts:
            for sub in act.subacts:
                if sub.subact_id not in desires:
                    raise SourceError(
                        "GA%d subact %s has no Collection Desire entry" % (ga, sub.subact_id)
                    )
                heading, clset, ds, de = desires[sub.subact_id]
                if (ds, de) != (sub.start, sub.end):
                    raise SourceError(
                        "GA%d %s: act map says E%d-E%d, desire map says E%d-E%d"
                        % (ga, sub.subact_id, sub.start, sub.end, ds, de)
                    )
                sub.desire_heading = heading
                sub.clset_id = clset

                if sub.start >= GENERATED_CONTEXT_FLOOR:
                    if sub.start not in context:
                        raise SourceError(
                            "GA%d %s: no Context Pack entry for E%d" % (ga, sub.subact_id, sub.start)
                        )
                    if sub.start not in activation:
                        raise SourceError(
                            "GA%d %s: no writer activation entry for E%d"
                            % (ga, sub.subact_id, sub.start)
                        )
                    sub.context_anchor = context[sub.start]
                    sub.activation_anchor = activation[sub.start]

                sub.state_sources = overlapping(docs, ga, sub.start, sub.end)

        series.append(GrandAct(ga=ga, start=start, end=end, acts=acts))
    return series


def ordered_subacts(series: list) -> list:
    return [s for g in series for s in g.subacts]
