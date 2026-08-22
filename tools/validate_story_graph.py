#!/usr/bin/env python3
"""Validate the Obsidian story-graph navigation layer under docs/_graph/.

    python tools/validate_story_graph.py --selftest
    python tools/validate_story_graph.py

This validator checks navigation structure only. It never promotes or infers
story canon. The graph layer deliberately points at authoritative source
documents instead of copying story facts into navigation hubs.

Every check below exists because a specific failure mode already happened, or
because the hub layer can silently rot when a source is re-cut:

    G1  node inventory              233 nodes in the declared shape
    G2  parent/child reciprocity    a child claims a parent that owns it back
    G3  chronological chain         160 subacts form one unbroken previous/next line
    G4  orphan detection            every Act/Subact is reachable from its parent
    G5  wikilink resolution         every target resolves to a real markdown file
    G6  Grand-Act source binding    each node cites its own GA's act map/registry
    G7  execution-layer links       Context / Writer Activation / CLSET / State Spine
    G8  heading-anchor resolution   `[[file#heading]]` still matches a real heading
    G9  GA10 ending authority       GA10 D nodes cite the current ending amendment
    G10 workflow residue            no branch-only, write-scoped workflow survives
    G11 manuscript contamination    the graph never links into manuscript prose

`--selftest` proves each check actually fires. A check that cannot be shown to
fail on a crafted defect is the same as no check at all (CLAUDE.md section 13).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import story_graph_sources as S  # noqa: E402

ROOT = S.ROOT
GRAPH = S.GRAPH
WORKFLOWS = ROOT / ".github" / "workflows"

# The expected shape is derived from the act maps, not hardcoded a second time.
# A legitimate act-map re-cut then moves the generator and the validator
# together instead of needing two edits in lockstep.
FIXED_NODES = 2  # README + story-graph-root

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

# Wikilink target, keeping any `#heading` anchor and dropping any `|label`.
WIKI_RE = re.compile(r"\[\[([^\]]+)\]\]")
INLINE_CODE = re.compile(r"`[^`\n]*`")


def strip_code(text: str) -> str:
    out = []
    fence = False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            fence = not fence
            continue
        if not fence:
            out.append(INLINE_CODE.sub("", line))
    return "\n".join(out)


def links(text: str) -> list:
    """[(stem, anchor)] for every wikilink outside code."""
    out = []
    for raw in WIKI_RE.findall(strip_code(text)):
        target = raw.split("|")[0].strip()
        stem, _, anchor = target.partition("#")
        out.append((stem.strip(), anchor.strip()))
    return out


def targets(text: str) -> set:
    return {s for s, _ in links(text)}


# ---------------------------------------------------------------------------
# Checks. Each takes plain data and returns error strings, so `--selftest` can
# drive them with a crafted defect instead of a whole synthetic repository.
# ---------------------------------------------------------------------------

def expected_inventory(ga_count: int, act_count: int, subact_count: int) -> dict:
    return {
        ".": FIXED_NODES,
        "ga": ga_count,
        "acts": act_count,
        "subacts": subact_count,
        "state": ga_count + len(DOMAIN_HUBS),
    }


def check_inventory(counts: dict, total: int, expected: dict) -> list:
    """G1 — the graph must keep the shape its sources imply."""
    errors = []
    expected_total = sum(expected.values())
    if total != expected_total:
        errors.append("G1 node count: expected %d markdown files under docs/_graph, found %d"
                      % (expected_total, total))
    for group, want in expected.items():
        actual = counts.get(group, 0)
        if actual != want:
            errors.append("G1 node count: docs/_graph/%s expected %d, found %d"
                          % (group, want, actual))
    return errors


def check_parent_child(child: str, parent: str, parent_links: set) -> list:
    """G2 — a parent that a child claims must link the child back."""
    if child not in parent_links:
        return ["G2 parent/child: %s claims parent %s, but %s does not link it back"
                % (child, parent, parent)]
    return []


DECLARED_NEIGHBOUR = re.compile(r"^- (Previous|Next) Subact: (.+)$")
NO_NEIGHBOUR = "없음"


def declared_neighbours(text: str) -> tuple:
    """(previous, next) as the node itself declares them, or None at an end.

    Reading the declared fields matters. Membership in the node's whole link set
    is not the same claim: a hub could declare the wrong neighbour and still
    contain the right stem somewhere else on the page — a broken chain that
    reads as intact.
    """
    prev = nxt = None
    for line in strip_code(text).splitlines():
        m = DECLARED_NEIGHBOUR.match(line)
        if not m:
            continue
        tail = m.group(2).strip()
        value = None
        if not tail.startswith(NO_NEIGHBOUR):
            hit = re.match(r"\[\[([^\]|#]+)", tail)
            value = hit.group(1).strip() if hit else tail
        if m.group(1) == "Previous":
            prev = value
        else:
            nxt = value
    return prev, nxt


def check_chain(chain: list, declared: dict) -> list:
    """G3 — the subacts form one unbroken previous/next line, as declared."""
    errors = []
    for i, stem in enumerate(chain):
        prev, nxt = declared.get(stem, (None, None))
        want_prev = chain[i - 1] if i > 0 else None
        want_next = chain[i + 1] if i < len(chain) - 1 else None
        if prev != want_prev:
            errors.append("G3 chain break: %s declares previous %r, expected %r"
                          % (stem, prev, want_prev))
        if nxt != want_next:
            errors.append("G3 chain break: %s declares next %r, expected %r"
                          % (stem, nxt, want_next))
    return errors


def check_chain_ends(chain: list, doc_links: dict) -> list:
    """G3 — the last subact must hand the reader back to the series root."""
    if not chain:
        return []
    last = chain[-1]
    if "story-graph-root" not in doc_links.get(last, set()):
        return ["G3 chain end: final subact %s must return to story-graph-root" % last]
    return []


def check_orphans(expected: set, referenced: set) -> list:
    """G4 — every Act/Subact node must be referenced by some other graph node."""
    return ["G4 orphan node: %s is never linked from another graph node" % stem
            for stem in sorted(expected - referenced)]


def check_wikilinks(found: dict, by_stem: dict, by_path: set) -> list:
    """G5 — every wikilink target must resolve to exactly one markdown file."""
    errors = []
    for source, refs in sorted(found.items()):
        for stem, _ in refs:
            if "/" in stem:
                if stem not in by_path:
                    errors.append("G5 broken path link: %s -> [[%s]]" % (source, stem))
                continue
            hits = by_stem.get(stem, [])
            if not hits:
                errors.append("G5 broken wiki link: %s -> [[%s]]" % (source, stem))
            elif len(hits) > 1:
                errors.append("G5 ambiguous wiki link: %s -> [[%s]] matches %s; use the full path"
                              % (source, stem, ", ".join(hits)))
    return errors


def check_required(source: str, found: set, required: list) -> list:
    """G6/G7 — a node must cite the sources its own layer is bound to."""
    return ["%s missing link: %s -> [[%s]]" % (tag, source, stem)
            for tag, stem in required if stem not in found]


def check_anchors(source: str, refs: list, headings: dict) -> list:
    """G8 — `[[file#heading]]` must still match a heading in the target file."""
    errors = []
    for stem, anchor in refs:
        if not anchor:
            continue
        known = headings.get(stem)
        if known is None:
            continue  # G5 owns unresolvable targets
        if anchor not in known:
            errors.append("G8 stale anchor: %s -> [[%s#%s]] no longer matches a heading"
                          % (source, stem, anchor))
    return errors


ENDING_REQUIRED = (
    S.ENDING_AMENDMENT_STEM,
    S.ENDING_CROSSWALK_STEM,
    S.ENDING_DECISION_STEM,
)
# Endpoint facts the GA10 D nodes must not contradict, and stale placements
# they must not resurrect (CLAUDE.md section 12 propagation failure mode).
ENDING_STALE_CLAIMS = (
    "E1099",
    "CY748-01",
    "CY 748-01",
)


def check_ending_authority(source: str, found: set, text: str) -> list:
    """G9 — GA10 D nodes cite the current ending amendment and no stale endpoint.

    The history exemption is scoped to the line, not the document. A document-wide
    escape is permanently open the moment any boilerplate elsewhere in the node
    contains the word, which is how this check sat inert while looking green.
    """
    errors = []
    for stem in ENDING_REQUIRED:
        if stem not in found:
            errors.append("G9 ending authority: %s must link [[%s]]" % (source, stem))
    for line in strip_code(text).splitlines():
        marked = "이력" in line or "historical" in line.lower()
        for claim in ENDING_STALE_CLAIMS:
            if claim in line and not marked:
                errors.append(
                    "G9 ending drift: %s asserts stale endpoint %r without marking it history"
                    % (source, claim))
    return errors


BRANCH_ONLY_MARKERS = ("one-shot", "oneshot", "one_shot")

# The branch-only filename check is repository-wide: a one-shot sync job is
# never legitimate on main. The write/push checks are scoped to the story-graph
# gate on purpose — the full-series build workflows legitimately hold
# `contents: write` and push generated layers, and this validator does not own
# their policy.


def check_workflows(workflows: dict) -> list:
    """G10 — no branch-only push/persist workflow may survive into main."""
    errors = []
    for name, text in sorted(workflows.items()):
        stem = name.lower()
        if any(m in stem for m in BRANCH_ONLY_MARKERS):
            errors.append("G10 workflow residue: %s is a branch-only one-shot workflow; "
                          "remove it before merging (see PR #214 disposition)" % name)
            continue
        if "story-graph" not in stem and "story_graph" not in stem:
            continue
        if "contents: write" in text:
            errors.append("G10 workflow permission: %s requests contents: write; the story-graph "
                          "gate is read-only" % name)
        if "git push" in text:
            errors.append("G10 workflow residue: %s pushes commits; the story-graph gate must not "
                          "write to a branch" % name)
        if "github.event.pull_request.head.sha" not in text and "pull_request" in text:
            # actions/checkout defaults to the PR merge ref, which is the real head
            # under test; an explicit head_ref checkout is the branch-only pattern.
            if "ref: ${{ github.head_ref }}" in text:
                errors.append("G10 workflow target: %s checks out a named branch instead of the "
                              "pull-request head" % name)
    return errors


def check_manuscript_links(source: str, found: set, manuscript_stems: set) -> list:
    """G11 — the navigation graph must never link into manuscript prose."""
    return ["G11 manuscript contamination: %s links manuscript file [[%s]]" % (source, stem)
            for stem in sorted(found & manuscript_stems)]


# ---------------------------------------------------------------------------
# Repository run
# ---------------------------------------------------------------------------

HEADING_RE = re.compile(r"^#{1,6} (.+?)\s*$")


def headings_of(text: str) -> set:
    return {m.group(1).strip() for m in
            (HEADING_RE.match(line) for line in text.split("\n")) if m}


def run() -> int:
    errors: list = []

    if not GRAPH.exists():
        print("STORY GRAPH VALIDATION: FAIL")
        print("- G1 docs/_graph does not exist. Run: python tools/build_story_graph.py")
        return 1

    # --- repository index -------------------------------------------------
    by_stem: dict = {}
    by_path: set = set()
    heading_index: dict = {}
    manuscript_stems: set = set()
    for p in sorted(ROOT.rglob("*.md")):
        parts = p.relative_to(ROOT).parts
        if any(x in (".git", ".obsidian", "node_modules") for x in parts):
            continue
        rel = p.relative_to(ROOT).as_posix()
        by_stem.setdefault(p.stem, []).append(rel)
        by_path.add(rel[: -len(".md")])
        if parts[0] in S.MANUSCRIPT_DIR_NAMES:
            manuscript_stems.add(p.stem)

    graph_files = sorted(GRAPH.rglob("*.md"))
    text_of = {p: p.read_text(encoding="utf-8") for p in graph_files}
    for p, t in text_of.items():
        for stem, anchor in links(t):
            if not anchor or stem in heading_index:
                continue
            if "/" in stem:
                # Path-form links carry anchors too; keying only by bare stem
                # left them unchecked.
                target = ROOT / ("%s.md" % stem)
                if target.exists():
                    heading_index[stem] = headings_of(target.read_text(encoding="utf-8"))
                continue
            hits = by_stem.get(stem, [])
            if len(hits) == 1:
                heading_index[stem] = headings_of(
                    (ROOT / hits[0]).read_text(encoding="utf-8"))

    # --- approved sources -------------------------------------------------
    try:
        series = S.load_series()
    except S.SourceError as exc:
        print("STORY GRAPH VALIDATION: FAIL")
        print("- G6 approved source drift: %s" % exc)
        return 1
    chain = [s.stem for s in S.ordered_subacts(series)]
    acts = [a for g in series for a in g.acts]

    counts: dict = {}
    for p in graph_files:
        group = p.parent.relative_to(GRAPH).as_posix()
        counts[group] = counts.get(group, 0) + 1
    expected = expected_inventory(len(series), len(acts), len(chain))
    errors += check_inventory(counts, len(graph_files), expected)

    doc_links = {p.stem: targets(t) for p, t in text_of.items()}
    all_refs: set = set()
    for t in text_of.values():
        all_refs |= targets(t)

    found_links = {p.relative_to(ROOT).as_posix(): links(t) for p, t in text_of.items()}
    errors += check_wikilinks(found_links, by_stem, by_path)
    for p, t in text_of.items():
        rel = p.relative_to(ROOT).as_posix()
        errors += check_anchors(rel, links(t), heading_index)
        errors += check_manuscript_links(rel, targets(t), manuscript_stems)

    root_links = doc_links.get("story-graph-root", set())
    errors += check_required("story-graph-root", root_links,
                             [("G4", g.stem) for g in series]
                             + [("G4", h) for h in DOMAIN_HUBS])

    for g in series:
        ga_links = doc_links.get(g.stem, set())
        spine_links = doc_links.get(g.spine_stem, set())
        act_map = S.ACT_MAP_STEM[g.ga]
        registry = S.COLLECTION_REGISTRY_STEM[g.ga]

        errors += check_required(g.stem, ga_links, [
            ("G6", act_map), ("G6", registry), ("G7", g.spine_stem),
            ("G7", S.CONTEXT_PACK_STEM[g.ga]), ("G7", S.ACTIVATION_STEM[g.ga]),
            ("G7", S.DESIRE_STEM[g.ga]),
        ] + [("G4", a.stem) for a in g.acts])
        errors += check_parent_child(g.stem, "story-graph-root", root_links)

        errors += check_required(g.spine_stem, spine_links, [
            ("G6", act_map), ("G6", registry),
            ("G7", S.CONTEXT_PACK_STEM[g.ga]), ("G7", S.ACTIVATION_STEM[g.ga]),
            ("G7", S.DESIRE_STEM[g.ga]), ("G7", "episode-briefs"),
        ] + [("G4", h) for h in DOMAIN_HUBS])

        for a in g.acts:
            act_links = doc_links.get(a.stem, set())
            errors += check_required(a.stem, act_links, [
                ("G6", act_map), ("G6", registry),
                ("G7", g.stem), ("G7", g.spine_stem),
            ] + [("G4", s.stem) for s in a.subacts])
            errors += check_parent_child(a.stem, g.stem, ga_links)

            for s in a.subacts:
                sub_links = doc_links.get(s.stem, set())
                required = [
                    ("G6", act_map), ("G6", registry),
                    ("G7", g.stem), ("G7", a.stem), ("G7", g.spine_stem),
                    ("G7", S.DESIRE_STEM[g.ga]),
                    ("G7", "episode-briefs"),
                    ("G7", "context-pack-tangible-reader-memory-execution-spec-proposal-v1"),
                ]
                if s.context_anchor:
                    required += [("G7", S.CONTEXT_PACK_STEM[g.ga]),
                                 ("G7", S.ACTIVATION_STEM[g.ga])]
                else:
                    required += [("G7", S.MANUAL_CONTEXT_STEM),
                                 ("G7", S.MANUAL_ACTIVATION_STEM)]
                errors += check_required(s.stem, sub_links, required)
                errors += check_parent_child(s.stem, a.stem, act_links)

                sub_path = GRAPH / "subacts" / ("%s.md" % s.stem)
                if s.clset_id and sub_path.exists():
                    if s.clset_id not in text_of[sub_path]:
                        errors.append("G7 missing CLSET: %s does not name %s"
                                      % (s.stem, s.clset_id))
                if g.ga == 10 and a.letter == "d" and sub_path.exists():
                    errors += check_ending_authority(s.stem, sub_links, text_of[sub_path])

    declared = {}
    for sub in S.ordered_subacts(series):
        path = GRAPH / "subacts" / ("%s.md" % sub.stem)
        declared[sub.stem] = declared_neighbours(text_of[path]) if path in text_of else (None, None)
    errors += check_chain(chain, declared)
    errors += check_chain_ends(chain, doc_links)

    expected_nodes = {a.stem for g in series for a in g.acts} | set(chain)
    errors += check_orphans(expected_nodes, all_refs)

    for name in DOMAIN_HUBS:
        path = GRAPH / "state" / ("%s.md" % name)
        if not path.exists():
            errors.append("G1 missing domain hub: %s" % path.relative_to(ROOT).as_posix())
            continue
        body = text_of[path]
        if "NOT A" not in body and "QC BRIDGE ONLY" not in body:
            errors.append("G1 authority guard missing: %s" % path.relative_to(ROOT).as_posix())

    workflows = {}
    if WORKFLOWS.exists():
        workflows = {p.name: p.read_text(encoding="utf-8")
                     for p in sorted(WORKFLOWS.iterdir())
                     if p.suffix in (".yml", ".yaml")}
    errors += check_workflows(workflows)

    readme = GRAPH / "README.md"
    if readme.exists():
        guard = "다른 프로젝트의 `Volume` 또는 고정 `60 Subact` 구조를 가져오지 않는다"
        if guard not in readme.read_text(encoding="utf-8"):
            errors.append("G1 project-specific hierarchy guard missing from docs/_graph/README.md")

    if errors:
        print("STORY GRAPH VALIDATION: FAIL")
        for e in errors:
            print("- %s" % e)
        return 1

    # Everything printed below is counted from what was just validated. A summary
    # line that is a string literal reports the author's intention, not the
    # artifact — and the Context line was wrong exactly that way (158 generated
    # + 2 manual, never 160 generated).
    anchored = sum(1 for t in text_of.values() for _, a in links(t) if a)
    generated_ctx = manual_ctx = activation = clset = spine = 0
    for g in series:
        for a in g.acts:
            for sub in a.subacts:
                found = doc_links.get(sub.stem, set())
                if sub.context_anchor:
                    generated_ctx += S.CONTEXT_PACK_STEM[g.ga] in found
                    activation += S.ACTIVATION_STEM[g.ga] in found
                else:
                    manual_ctx += S.MANUAL_CONTEXT_STEM in found
                    activation += S.MANUAL_ACTIVATION_STEM in found
                clset += S.DESIRE_STEM[g.ga] in found
                spine += g.spine_stem in found
    final_act = series[-1].acts[-1]
    ending = sum(1 for sub in final_act.subacts
                 if set(ENDING_REQUIRED) <= doc_links.get(sub.stem, set()))
    manuscript_hits = sum(len(targets(t) & manuscript_stems) for t in text_of.values())

    print("STORY GRAPH VALIDATION: PASS")
    print("- markdown nodes under docs/_graph: %d" % len(graph_files))
    print("- grand-act hubs: %d / act hubs: %d / subact hubs: %d"
          % (len(series), len(acts), len(chain)))
    print("- GA state spines: %d / domain state hubs: %d" % (len(series), len(DOMAIN_HUBS)))
    print("- chronological subact chain: %d/%d unbroken" % (len(chain), len(chain)))
    print("- Context Pack links: %d generated + %d manual (E001-E010) = %d/%d"
          % (generated_ctx, manual_ctx, generated_ctx + manual_ctx, len(chain)))
    print("- Writer Activation links: %d/%d · CLSET links: %d/%d · state spine links: %d/%d"
          % (activation, len(chain), clset, len(chain), spine, len(chain)))
    print("- heading anchors resolved: %d/%d" % (anchored, anchored))
    print("- GA10 %s subacts citing the ending amendment: %d/%d"
          % (final_act.act_id, ending, len(final_act.subacts)))
    print("- manuscript links: %d · workflow files inspected: %d"
          % (manuscript_hits, len(workflows)))
    print("- exact story facts remain source-owned; the graph is navigation-only")
    return 0


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def selftest() -> int:
    cases = [
        ("G1 detects a node-count mismatch",
         lambda: check_inventory({".": 2, "ga": 10, "acts": 40, "subacts": 159, "state": 21},
                                 232, expected_inventory(10, 40, 160)),
         True),
        ("G1 accepts the shape its sources imply",
         lambda: check_inventory({".": 2, "ga": 10, "acts": 40, "subacts": 160, "state": 21},
                                 233, expected_inventory(10, 40, 160)),
         False),
        ("G1 follows the sources when an act map is legitimately re-cut",
         lambda: check_inventory({".": 2, "ga": 10, "acts": 40, "subacts": 200, "state": 21},
                                 273, expected_inventory(10, 40, 200)),
         False),
        ("G2 detects a parent that does not own the child back",
         lambda: check_parent_child("graph-ga02-act-a", "graph-ga02-hub", {"graph-ga02-act-b"}),
         True),
        ("G2 accepts a reciprocal parent/child pair",
         lambda: check_parent_child("graph-ga02-act-a", "graph-ga02-hub", {"graph-ga02-act-a"}),
         False),
        ("G3 detects a previous/next chain break",
         lambda: check_chain(["s1", "s2", "s3"],
                             {"s1": (None, "s2"), "s2": ("s1", None), "s3": ("s2", None)}),
         True),
        ("G3 detects a hub declaring the wrong neighbour",
         lambda: check_chain(["s1", "s2", "s3"],
                             {"s1": (None, "s3"), "s2": ("s1", "s3"), "s3": ("s2", None)}),
         True),
        ("G3 detects an end node that claims a neighbour it should not have",
         lambda: check_chain(["s1", "s2"],
                             {"s1": ("s0", "s2"), "s2": ("s1", None)}),
         True),
        ("G3 accepts an unbroken chain",
         lambda: check_chain(["s1", "s2"],
                             {"s1": (None, "s2"), "s2": ("s1", None)}),
         False),
        ("G3 detects a final subact that never returns to the root",
         lambda: check_chain_ends(["s1", "s2"], {"s1": {"s2"}, "s2": {"s1"}}),
         True),
        ("G3 accepts a final subact that returns to the root",
         lambda: check_chain_ends(["s1", "s2"], {"s1": {"s2"}, "s2": {"s1", "story-graph-root"}}),
         False),
        # The gap an independent audit found: membership in the whole link set is
        # not the declared field. This hub still contains the correct stem, but
        # declares the wrong next — the old check passed it.
        ("G3 catches a wrong declared next even when the correct stem appears elsewhere",
         lambda: check_chain(
             ["s1", "s2", "s3"],
             {"s1": (None, "s2"), "s2": ("s1", "s1"), "s3": ("s2", None)}),
         True),
        ("G3 reads the declared fields out of a real node body",
         lambda: [declared_neighbours(
             "- Previous Subact: [[graph-ga01-subact-d4]] (GA01 D4 / E93–E100)\n"
             "- Next Subact: [[graph-ga02-subact-a2]] (GA02 2A-2 / E108–E114)")
         ] if declared_neighbours(
             "- Previous Subact: [[graph-ga01-subact-d4]] (GA01 D4 / E93–E100)\n"
             "- Next Subact: [[graph-ga02-subact-a2]] (GA02 2A-2 / E108–E114)"
         ) != ("graph-ga01-subact-d4", "graph-ga02-subact-a2") else [],
         False),
        ("G3 reads the series-end sentinel as no neighbour",
         lambda: [] if declared_neighbours(
             "- Previous Subact: [[graph-ga10-subact-d3]] (GA10 10D-3 / E1090–E1095)\n"
             "- Next Subact: 없음 — 시리즈 종점, [[story-graph-root]]로 복귀"
         ) == ("graph-ga10-subact-d3", None) else ["sentinel misread"],
         False),
        ("G4 detects an orphaned Act/Subact node",
         lambda: check_orphans({"graph-ga03-act-c"}, set()),
         True),
        ("G4 accepts a referenced node",
         lambda: check_orphans({"graph-ga03-act-c"}, {"graph-ga03-act-c"}),
         False),
        ("G5 detects a broken wikilink",
         lambda: check_wikilinks({"a.md": [("does-not-exist", "")]}, {"b": ["docs/b.md"]}, set()),
         True),
        ("G5 detects an ambiguous bare-name wikilink",
         lambda: check_wikilinks({"a.md": [("README", "")]},
                                 {"README": ["README.md", "docs/_entities/README.md"]}, set()),
         True),
        ("G5 detects a broken full-path wikilink",
         lambda: check_wikilinks({"a.md": [("docs/_entities/nope", "")]}, {}, set()),
         True),
        ("G5 accepts a resolvable wikilink",
         lambda: check_wikilinks({"a.md": [("b", "")]}, {"b": ["docs/b.md"]}, set()),
         False),
        ("G6/G7 detects a node citing the wrong Grand Act source",
         lambda: check_required("graph-ga03-subact-a1", {"ga2-episodes-101-210-act-map-v1"},
                                [("G6", "ga3-episodes-211-330-act-map-v1")]),
         True),
        ("G7 detects a missing Context Pack link",
         lambda: check_required("graph-ga02-subact-a1", {"ga2-collection-registry-v1"},
                                [("G7", "ga2-e101-e210-context-packs-v1")]),
         True),
        ("G7 detects a missing Writer Activation link",
         lambda: check_required("graph-ga02-subact-a1", {"ga2-e101-e210-context-packs-v1"},
                                [("G7", "ga2-e101-e210-writer-activation-v1")]),
         True),
        ("G7 detects a missing CLSET / Collection Desire link",
         lambda: check_required("graph-ga02-subact-a1", set(),
                                [("G7", "ga2-collection-desire-subact-map-v1")]),
         True),
        ("G7 detects a missing State Spine link",
         lambda: check_required("graph-ga02-subact-a1", set(),
                                [("G7", "graph-ga02-state-spine")]),
         True),
        ("G7 accepts a node with every required execution link",
         lambda: check_required("graph-ga02-subact-a1",
                                {"ga2-e101-e210-context-packs-v1",
                                 "ga2-e101-e210-writer-activation-v1",
                                 "ga2-collection-desire-subact-map-v1",
                                 "graph-ga02-state-spine"},
                                [("G7", "ga2-e101-e210-context-packs-v1"),
                                 ("G7", "ga2-e101-e210-writer-activation-v1"),
                                 ("G7", "ga2-collection-desire-subact-map-v1"),
                                 ("G7", "graph-ga02-state-spine")]),
         False),
        ("G8 detects a heading anchor that no longer exists",
         lambda: check_anchors("graph-ga02-subact-a1",
                               [("ga2-e101-e210-context-packs-v1", "E101 — 옛 제목")],
                               {"ga2-e101-e210-context-packs-v1": {"E101 — 새 제목"}}),
         True),
        ("G8 accepts an anchor that still matches a heading",
         lambda: check_anchors("graph-ga02-subact-a1",
                               [("ga2-e101-e210-context-packs-v1", "E101 — 제목")],
                               {"ga2-e101-e210-context-packs-v1": {"E101 — 제목"}}),
         False),
        ("G9 detects a GA10 D node missing the ending amendment",
         lambda: check_ending_authority("graph-ga10-subact-d1", set(), "본문"),
         True),
        ("G9 detects a resurrected stale ending endpoint",
         lambda: check_ending_authority("graph-ga10-subact-d4", set(ENDING_REQUIRED),
                                        "M-019는 E1099에서 끝난다"),
         True),
        ("G9 accepts a stale endpoint marked as history on its own line",
         lambda: check_ending_authority("graph-ga10-subact-d4", set(ENDING_REQUIRED),
                                        "구 카드의 E1099 배치는 이력이며 정본이 아니다"),
         False),
        ("G9 still fires when 이력 sits on a different line than the stale claim",
         lambda: check_ending_authority(
             "graph-ga10-subact-d4", set(ENDING_REQUIRED),
             "- 구/신 배치 대조: 구 배치를 이력으로 보존한다\nM-019는 E1099에서 끝난다"),
         True),
        ("G10 detects a branch-only one-shot workflow",
         lambda: check_workflows({"one-shot-sync-story-graph-index.yml": "on: pull_request"}),
         True),
        ("G10 detects a story-graph workflow requesting write permission",
         lambda: check_workflows({"validate-story-graph.yml":
                                  "permissions:\n  contents: write\non:\n  pull_request:"}),
         True),
        ("G10 detects a story-graph workflow that pushes commits",
         lambda: check_workflows({"validate-story-graph.yml":
                                  "on:\n  pull_request:\nrun: git push origin HEAD"}),
         True),
        ("G10 detects a workflow checking out a named branch instead of the PR head",
         lambda: check_workflows({"validate-story-graph.yml":
                                  "on:\n  pull_request:\n    ref: ${{ github.head_ref }}"}),
         True),
        ("G10 accepts a read-only story-graph regression gate",
         lambda: check_workflows({"validate-story-graph.yml":
                                  "permissions:\n  contents: read\non:\n  pull_request:"}),
         False),
        ("G11 detects a graph node linking manuscript prose",
         lambda: check_manuscript_links("graph-ga01-subact-a1",
                                        {"001-역사에-없는-생도-v2"},
                                        {"001-역사에-없는-생도-v2"}),
         True),
        ("G11 accepts a graph node with no manuscript link",
         lambda: check_manuscript_links("graph-ga01-subact-a1",
                                        {"first-100-act-map-v2-consolidated"},
                                        {"001-역사에-없는-생도-v2"}),
         False),
    ]

    failures = 0
    for name, fn, should_fail in cases:
        got = fn()
        ok = bool(got) == should_fail
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
        if not ok:
            failures += 1
            print("        expected %s, got %r" % ("errors" if should_fail else "no errors", got))

    if failures:
        print("\nSELFTEST FAILED — %d of %d cases" % (failures, len(cases)))
        return 1
    print("\nSELFTEST PASSED — %d cases" % len(cases))
    return 0


def main(argv: list) -> int:
    if "--selftest" in argv:
        return selftest()
    return run()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
