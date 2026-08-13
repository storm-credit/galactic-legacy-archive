#!/usr/bin/env python3
"""Validate canon, links and manuscript contracts for the Galactic Legacy archive.

Companion to ``validate_design_data.py``, which only covers ``data/*.csv``.
This script covers the markdown side of the repository — the part where every
defect found on 2026-08-08 actually lived.

Each check maps to a real failure that passed through several review rounds
unnoticed, because the harness documents had no mechanical enforcement:

    C1  link integrity        — 840 references were inline code, and the
                                repaired links must not rot again.
    C2  retired canon names   — PR #99 renamed P-001 but left the canonical
                                lock document and the pronunciation authority
                                carrying the old name.
    C3  manuscript contract   — every manuscript must keep its header fields
                                and must not silently become publishable.
    C4  episode length        — D1 sets a 5,500-character floor including
                                spaces; nothing measured it.

Severity:

    ERROR   fails the build.
    WARN    reported, does not fail. Used where an author decision is still
            open, so the build does not sit red on a question nobody has
            answered yet.

Standard library only, so it runs in GitHub Actions and locally with no setup.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Findings quote Korean paths and canon names. Windows consoles default to cp949
# and would raise UnicodeEncodeError while printing them, so force UTF-8 output.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

SKIP_DIRS = {".git", ".obsidian", "node_modules"}
SKIP_FILES = {"환영합니다!.md"}

# --------------------------------------------------------------------------
# C2 — retired canonical names
# --------------------------------------------------------------------------
# Matched as whole phrases so unrelated tokens are not caught. `Cardo Verge`
# is a route location, not the protagonist, and must never be rewritten.

RETIRED_NAMES = [
    ("리안 카르도", "리안 칼데르", "P-001 rename, canonical-name-errata-005 / PR #99"),
    ("Rian Cardo", "Rian Calder", "P-001 rename, canonical-name-errata-005 / PR #99"),
    ("회랑새", "파루스", "first-ship rename, decision-log D-20260813-02"),
    ("Corridor Wren", "Parus", "first-ship rename, decision-log D-20260813-02"),
]

# Documents that are allowed to contain retired names, because their purpose is
# to record history. Matched against the POSIX path.
HISTORY_EXEMPT = (
    "docs/00_project/canonical-name-errata-",
    "docs/00_project/decision-log.md",
    "docs/07_style/noncanon-episode-1-close-third-sample-",
    "docs/99_quality_control/ga1-e1-v2-",
    "tools/validate_canon.py",
)

# v1 drafts predate the rename and are preserved as historical text per
# canonical-name-errata-005 propagation rule 4.
HISTORY_EXEMPT_PATTERNS = (re.compile(r"^manuscript/.*-v1\.md$"),)

# --------------------------------------------------------------------------
# C3 — manuscript contract
# --------------------------------------------------------------------------

# Two header schemas coexist in the repository. The v1 first drafts place the
# header *below* the title and use different field names; the v2 revision schema
# places it above and renames the fields. Legacy drafts are preserved as
# historical text, so the validator tolerates their schema but still enforces the
# one guarantee that must hold everywhere: nothing is publishable.
REQUIRED_MANUSCRIPT_FIELDS = ("Status", "Episode", "Canon Check", "Publication")
LEGACY_MANUSCRIPT_FIELDS = ("Status", "Publication Status", "POV", "Canon Basis")

# Either schema's publication field. Whichever exists must carry the block.
PUBLICATION_FIELDS = ("Publication", "Publication Status")

# Standing rule until the human/mobile reader test (issue #26) clears.
REQUIRED_PUBLICATION_VALUE = "NOT AUTHORIZED"

# How many leading lines to scan for header fields, so both layouts are found.
HEADER_SCAN_LINES = 20

# --------------------------------------------------------------------------
# C6 — entity note discipline
# --------------------------------------------------------------------------
# Entity notes are navigation hubs, not a second copy of canon. The failure mode
# is drift: the hub is convenient, so settings get written there and the project
# ends up with two sources for the same fact, violating CLAUDE.md section 3.
# These limits keep a hub a hub.

ENTITY_DIR = "docs/_entities/"
ENTITY_MAX_LINES = 60
ENTITY_BANNER_MARKER = "링크 허브"
ENTITY_EXPOSURE_SECTION = "## 독자 노출 상한"

# --------------------------------------------------------------------------
# C4 — episode length
# --------------------------------------------------------------------------

# D1 / decision-log D-20260806-01: floor 5,500 characters including spaces.
# [ASSUMPTION] pending platform and contest selection.
LENGTH_FLOOR_INCLUDING_SPACES = 5500

WIKILINK = re.compile(r"\[\[([^\]|#]+)")
HEADER_FIELD = re.compile(r"^([A-Za-z][A-Za-z ]*):\s*(.*)$")
EPISODE_FILE = re.compile(r"^\d{3}-.*\.md$")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.notes: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def note(self, message: str) -> None:
        self.notes.append(message)


def is_history_exempt(rel: str) -> bool:
    if rel.startswith(HISTORY_EXEMPT):
        return True
    return any(pattern.match(rel) for pattern in HISTORY_EXEMPT_PATTERNS)


def collect_markdown(root: Path) -> list[tuple[str, str]]:
    """Return (posix relative path, text) for every markdown file."""
    out: list[tuple[str, str]] = []
    for path in sorted(root.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        rel = path.relative_to(root).as_posix()
        out.append((rel, path.read_text(encoding="utf-8")))
    return out


def build_index(files: list[tuple[str, str]]) -> tuple[dict[str, list[str]], set[str]]:
    by_basename: dict[str, list[str]] = {}
    by_path: set[str] = set()
    for rel, _ in files:
        by_basename.setdefault(Path(rel).name, []).append(rel)
        by_path.add(rel[: -len(".md")])
    return by_basename, by_path


INLINE_CODE = re.compile(r"`[^`\n]*`")


def strip_code(text: str) -> str:
    """Remove fenced blocks and inline code spans.

    Documentation legitimately quotes link syntax — `CLAUDE.md` section 13 shows
    what a wikilink looks like — and those examples must not be resolved as real
    links. Anything inside backticks is an example, not a reference.
    """
    out: list[str] = []
    in_fence = False
    for line in text.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(INLINE_CODE.sub("", line))
    return "\n".join(out)


def check_links(files: list[tuple[str, str]], report: Report) -> int:
    """C1 — every wikilink must resolve to a real markdown file."""
    by_basename, by_path = build_index(files)
    total = 0
    for rel, text in files:
        for target in WIKILINK.findall(strip_code(text)):
            target = target.strip()
            if not target:
                continue
            total += 1
            hits = by_basename.get(target + ".md", [])
            # A bare name that several files answer to is ambiguous even when it
            # also happens to match a path. [[README]] resolved silently to the
            # repository README while ten entity notes meant the entity spec --
            # the link worked, pointed at the wrong document, and nothing said so.
            if "/" not in target and len(hits) > 1:
                report.error(
                    f"C1 {rel}: [[{target}]] is ambiguous — matches {', '.join(hits)}. "
                    f"Use the full path form."
                )
                continue
            if target in by_path:
                continue
            if len(hits) == 1:
                continue
            if len(hits) > 1:
                report.error(
                    f"C1 {rel}: [[{target}]] is ambiguous — matches {', '.join(hits)}. "
                    f"Use the full path form."
                )
            else:
                report.error(f"C1 {rel}: [[{target}]] does not resolve to any file")
    return total


def check_retired_names(files: list[tuple[str, str]], report: Report) -> int:
    """C2 — retired canonical names must not survive in active documents."""
    checked = 0
    for rel, text in files:
        if is_history_exempt(rel):
            continue
        checked += 1
        # A retired name inside backticks is being *named*, not used — the name
        # lock, the phonetics table and the rename decision all have to say which
        # name was retired. Stripping code spans is the same rule C1 uses for
        # quoted link syntax.
        prose = strip_code(text)
        for retired, replacement, reason in RETIRED_NAMES:
            if retired in prose:
                count = prose.count(retired)
                report.error(
                    f"C2 {rel}: retired name {retired!r} appears {count}x — "
                    f"use {replacement!r} ({reason})"
                )
    return checked


# --------------------------------------------------------------------------
# C7 — arc claims in proposed registries
# --------------------------------------------------------------------------
# A registry row says which grand act an item first appears in. Nothing used to
# verify that the arc exists, so a slot could be parked in an arc the series
# does not have, and the row would still read as a plan.

ARC_REGISTRIES = (
    "docs/06_hardware/named-hull-registry-and-naming-grammar-v1.md",
    "docs/06_hardware/maneuver-frame-lineup-master-architecture-v1.md",
    "docs/06_hardware/named-weapon-and-part-registry-v1.md",
    "docs/06_hardware/named-technology-lineage-registry-v1.md",
    "docs/09_collection/named-relic-and-provenance-registry-v1.md",
    "docs/02_world/named-place-and-corridor-registry-v1.md",
)
ARC_TOKEN = re.compile(r"\bGA(\d{1,2})\b")


def act_map_for(ga: int, stems: set[str]) -> str | None:
    if ga == 1:
        return next((s for s in stems if s.startswith("first-100-act-map")), None)
    prefix, suffix = f"ga{ga}-episodes-", "-act-map-v1"
    return next((s for s in stems if s.startswith(prefix) and s.endswith(suffix)), None)


def check_arc_claims(files: list[tuple[str, str]], report: Report) -> int:
    """C7 — every arc a registry row claims must have an act map."""
    stems = {rel.rsplit("/", 1)[-1][: -len(".md")] for rel, _ in files}
    checked = 0
    for rel, text in files:
        if rel not in ARC_REGISTRIES:
            continue
        seen: set[int] = set()
        for line in text.split("\n"):
            if not line.startswith("| "):
                continue
            for match in ARC_TOKEN.finditer(line):
                ga = int(match.group(1))
                if ga in seen:
                    continue
                seen.add(ga)
                checked += 1
                if not act_map_for(ga, stems):
                    report.error(
                        f"C7 {rel}: a row places an item in GA{ga}, which has no act map"
                    )
    return checked


# --------------------------------------------------------------------------
# C8 -- registries must count themselves correctly
# --------------------------------------------------------------------------
# CLAUDE.md section 15-7 asks for counts to be separated and verified. The
# faction registry still claimed 28 internal blocs when it had 24, and the only
# reason it surfaced was the generated catalogue disagreeing. A document that
# states a total about itself must agree with its own rows.

REGISTRY_COUNTS = (
    # path, row-id prefix pattern, phrase the document uses for its total
    ("docs/06_hardware/named-hull-registry-and-naming-grammar-v1.md", "S-", "등록부 총계"),
    ("docs/06_hardware/named-weapon-and-part-registry-v1.md", "A-", "명명 앵커"),
    ("docs/06_hardware/named-technology-lineage-registry-v1.md", "T-", "명명 계보"),
    ("docs/09_collection/named-relic-and-provenance-registry-v1.md", "R-", "명명 실물 유물"),
    ("docs/02_world/named-place-and-corridor-registry-v1.md", "N-", "명명 전면 장소"),
)

COUNT_CLAIM = re.compile(r"\*\*(\d+)\*\*")
NOT_REGISTERED = "등록 불가"


def check_registry_counts(files: list[tuple[str, str]], report: Report) -> int:
    """C8 -- the total a registry states about itself must match its rows."""
    by_path = dict(files)
    checked = 0
    for rel, prefix, phrase in REGISTRY_COUNTS:
        text = by_path.get(rel)
        if text is None:
            continue
        rows = sum(
            1 for line in text.split("\n")
            if (line.startswith(f"| {prefix}") or line.startswith(f"| `{prefix}"))
            # A row the registry marks as not registered is documentation, not
            # inventory: the hull table keeps NR72-061 visible precisely so a
            # reader can see it being excluded from the count.
            and NOT_REGISTERED not in line
        )
        claim = None
        for line in text.split("\n"):
            if phrase in line and line.startswith("|"):
                m = COUNT_CLAIM.search(line)
                if m:
                    claim = int(m.group(1))
                    break
        if claim is None:
            report.error(f"C8 {rel}: no stated total for {phrase!r}")
            continue
        checked += 1
        if claim != rows:
            report.error(
                f"C8 {rel}: states {claim} for {phrase!r} but has {rows} rows"
            )
    return checked


def parse_header(text: str) -> dict[str, str]:
    """Collect ``Key: value`` fields from the head of the file.

    Scans a fixed window rather than stopping at the title, because the v1
    drafts put their header below the title and the v2 schema puts it above.
    """
    header: dict[str, str] = {}
    for line in text.split("\n")[:HEADER_SCAN_LINES]:
        match = HEADER_FIELD.match(line)
        if match:
            header[match.group(1).strip()] = match.group(2).strip()
    return header


def episode_body(text: str) -> str:
    """Prose after the title, with any header lines and blanks removed.

    Header fields sitting below the title would otherwise be counted as prose
    and inflate the length measurement.
    """
    match = re.search(r"^#\s+.*$", text, flags=re.MULTILINE)
    if not match:
        return ""
    lines = text[match.end() :].split("\n")
    start = 0
    for index, line in enumerate(lines):
        if not line.strip():
            continue
        if HEADER_FIELD.match(line):
            start = index + 1
            continue
        break
    return "\n".join(lines[start:])


def is_legacy_draft(rel: str) -> bool:
    return rel.endswith("-v1.md")


def check_manuscripts(files: list[tuple[str, str]], report: Report) -> int:
    """C3 header contract (ERROR), C4 length floor (WARN), C5 schema drift (WARN)."""
    counted = 0
    for rel, text in files:
        if not rel.startswith("manuscript/"):
            continue
        if not EPISODE_FILE.match(Path(rel).name):
            continue
        counted += 1

        header = parse_header(text)
        legacy = is_legacy_draft(rel)

        # The publication block is the one guarantee enforced on every schema.
        publication_field = next((f for f in PUBLICATION_FIELDS if f in header), None)
        if publication_field is None:
            report.error(
                f"C3 {rel}: no publication field — one of {PUBLICATION_FIELDS} is "
                f"required so no manuscript can become publishable by omission"
            )
        elif header[publication_field] != REQUIRED_PUBLICATION_VALUE:
            report.error(
                f"C3 {rel}: {publication_field} is {header[publication_field]!r}; "
                f"must remain {REQUIRED_PUBLICATION_VALUE!r} until the human "
                f"reader test (issue #26) clears"
            )

        if legacy:
            missing = [f for f in LEGACY_MANUSCRIPT_FIELDS if f not in header]
            if missing:
                report.warn(
                    f"C5 {rel}: legacy draft missing {', '.join(missing)} — "
                    f"carries the v1 header schema"
                )
            else:
                report.warn(
                    f"C5 {rel}: uses the v1 header schema "
                    f"(Publication Status / Canon Basis, header below the title); "
                    f"migrate when the episode is revised to v2"
                )
        else:
            for field in REQUIRED_MANUSCRIPT_FIELDS:
                if field not in header:
                    report.error(f"C3 {rel}: missing required header field {field!r}")

        body = episode_body(text)
        including_spaces = len(body.replace("\n", "").strip())
        if including_spaces == 0:
            report.error(f"C3 {rel}: no episode body found under the title heading")
            continue

        if including_spaces < LENGTH_FLOOR_INCLUDING_SPACES:
            short = LENGTH_FLOOR_INCLUDING_SPACES - including_spaces
            pct = 100 * including_spaces / LENGTH_FLOOR_INCLUDING_SPACES
            report.warn(
                f"C4 {rel}: {including_spaces} chars including spaces — "
                f"{short} below the {LENGTH_FLOOR_INCLUDING_SPACES} floor ({pct:.0f}%)"
            )
    return counted


def check_entity_notes(files: list[tuple[str, str]], report: Report) -> int:
    """C6 — entity hubs must stay hubs, not become a second canon."""
    counted = 0
    for rel, text in files:
        if not rel.startswith(ENTITY_DIR):
            continue
        if Path(rel).name == "README.md":
            continue
        counted += 1

        if ENTITY_BANNER_MARKER not in text:
            report.error(
                f"C6 {rel}: missing the hub banner — every entity note must state "
                f"that it is a link hub and not a settings source"
            )

        line_count = len(text.strip().split("\n"))
        if line_count > ENTITY_MAX_LINES:
            report.error(
                f"C6 {rel}: {line_count} lines exceeds the {ENTITY_MAX_LINES}-line "
                f"budget — move the content into a canon document and link to it"
            )

        if not WIKILINK.search(strip_code(text)):
            report.error(
                f"C6 {rel}: no wikilink to a canon source — a hub that links "
                f"nowhere is a duplicate, not a hub"
            )

        if ENTITY_EXPOSURE_SECTION not in text:
            report.error(
                f"C6 {rel}: missing the {ENTITY_EXPOSURE_SECTION!r} section — "
                f"without it the hub becomes a spoiler surface"
            )
    return counted


# --------------------------------------------------------------------------
# Self test — proves each check actually fires.
# --------------------------------------------------------------------------


def selftest() -> int:
    cases: list[tuple[str, list[tuple[str, str]], str, str]] = [
        (
            "C1 detects an unresolvable wikilink",
            [("docs/a.md", "see [[does-not-exist]]")],
            "links",
            "C1",
        ),
        (
            "C1 accepts a resolvable wikilink",
            [("docs/a.md", "see [[b]]"), ("docs/b.md", "x")],
            "links",
            "",
        ),
        (
            "C1 rejects a bare name shared by several files",
            [("docs/a.md", "see [[README]]"),
             ("README.md", "x"),
             ("docs/_entities/README.md", "y")],
            "links",
            "C1",
        ),
        (
            "C1 accepts the full path form of a shared name",
            [("docs/a.md", "see [[docs/_entities/README]]"),
             ("README.md", "x"),
             ("docs/_entities/README.md", "y")],
            "links",
            "",
        ),
        (
            "C1 ignores wikilinks inside code fences",
            [("docs/a.md", "```\n[[does-not-exist]]\n```")],
            "links",
            "",
        ),
        (
            "C1 ignores wikilink syntax quoted as inline code",
            [("CLAUDE.md", "문서 참조는 `[[위키링크]]`로 쓴다")],
            "links",
            "",
        ),
        (
            "C8 detects a registry that miscounts itself",
            [("docs/06_hardware/named-weapon-and-part-registry-v1.md",
              "| 명명 앵커 | **3** |\n| A-001 | x |\n| A-002 | y |")],
            "counts",
            "C8",
        ),
        (
            "C8 accepts a registry whose stated total matches its rows",
            [("docs/06_hardware/named-weapon-and-part-registry-v1.md",
              "| 명명 앵커 | **2** |\n| A-001 | x |\n| A-002 | y |")],
            "counts",
            "",
        ),
        (
            "C7 detects a registry row placed in an arc with no act map",
            [("docs/06_hardware/named-hull-registry-and-naming-grammar-v1.md",
              "| S-001 | `FR44-207` | x | FR | 1 | GA11 | y | 제안 |")],
            "arcs",
            "C7",
        ),
        (
            "C7 accepts an arc that has an act map",
            [("docs/06_hardware/named-hull-registry-and-naming-grammar-v1.md",
              "| S-001 | `FR44-207` | x | FR | 1 | GA2 | y | 제안 |"),
             ("docs/10_story_architecture/ga2-episodes-101-210-act-map-v1.md", "x")],
            "arcs",
            "",
        ),
        (
            "C2 allows a retired name quoted as inline code",
            [("docs/05_characters/x.md", "폐기명 `Rian Cardo`는 쓰지 않는다")],
            "retired",
            "",
        ),
        (
            "C2 detects a retired name in an active document",
            [("docs/05_characters/x.md", "Rian Cardo commands")],
            "names",
            "C2",
        ),
        (
            "C2 exempts historical records",
            [("docs/00_project/decision-log.md", "Rian Cardo was renamed")],
            "names",
            "",
        ),
        (
            "C2 exempts v1 draft manuscripts",
            [("manuscript/ga1/002-x-v1.md", "리안 카르도")],
            "names",
            "",
        ),
        (
            "C2 does not flag the place name Cardo Verge",
            [("docs/02_world/x.md", "K-13/Cardo Verge to Lumen trunk")],
            "names",
            "",
        ),
        (
            "C3 detects a missing header field",
            [
                (
                    "manuscript/ga1/001-x-v2.md",
                    "Status: REVISED\nPublication: NOT AUTHORIZED\n\n# t\n\nbody",
                )
            ],
            "manuscripts",
            "C3",
        ),
        (
            "C3 detects a manuscript with no publication field at all",
            [("manuscript/ga1/001-x-v2.md", "Status: REVISED\n\n# t\n\nbody")],
            "manuscripts",
            "C3",
        ),
        (
            "C3 accepts the legacy v1 publication field name",
            [
                (
                    "manuscript/ga1/002-x-v1.md",
                    "# 제2화 t\n\nStatus: FIRST DRAFT\nPublication Status: NOT AUTHORIZED\n"
                    "POV: 리안 근접 3인칭\nCanon Basis: card\n\n" + "가" * 6000,
                )
            ],
            "manuscripts",
            "C5",
        ),
        (
            "C3 rejects an unauthorized legacy publication field",
            [
                (
                    "manuscript/ga1/002-x-v1.md",
                    "# 제2화 t\n\nStatus: FIRST DRAFT\nPublication Status: AUTHORIZED\n"
                    "POV: p\nCanon Basis: card\n\n" + "가" * 6000,
                )
            ],
            "manuscripts",
            "C3",
        ),
        (
            "C4 does not count header lines placed below the title as prose",
            [
                (
                    "manuscript/ga1/002-x-v1.md",
                    "# 제2화 t\n\nStatus: FIRST DRAFT\nPublication Status: NOT AUTHORIZED\n"
                    "POV: p\nCanon Basis: card\n\n" + "가" * 5600,
                )
            ],
            "manuscripts",
            "!C4",  # prose alone clears the floor, so no length warning may fire
        ),
        (
            "C3 detects an unauthorized publication flag",
            [
                (
                    "manuscript/ga1/001-x-v2.md",
                    "Status: REVISED\nEpisode: E1\nCanon Check: SELF-PASS\n"
                    "Publication: AUTHORIZED\n\n# t\n\nbody",
                )
            ],
            "manuscripts",
            "C3",
        ),
        (
            "C6 detects an entity note that dropped the hub banner",
            [
                (
                    "docs/_entities/characters/x.md",
                    "# x\n\n[[a]]\n\n## 독자 노출 상한\n\n- none",
                )
            ],
            "entities",
            "C6",
        ),
        (
            "C6 detects an entity note that grew past the line budget",
            [
                (
                    "docs/_entities/characters/x.md",
                    "링크 허브\n[[a]]\n## 독자 노출 상한\n" + "\n".join(["x"] * 70),
                )
            ],
            "entities",
            "C6",
        ),
        (
            "C6 detects an entity note with no canon link",
            [
                (
                    "docs/_entities/characters/x.md",
                    "링크 허브\n\n요약만 있다\n\n## 독자 노출 상한\n\n- none",
                )
            ],
            "entities",
            "C6",
        ),
        (
            "C6 detects a missing reader-exposure section",
            [("docs/_entities/characters/x.md", "링크 허브\n\n[[a]]\n")],
            "entities",
            "C6",
        ),
        (
            "C6 accepts a well-formed entity note",
            [
                (
                    "docs/_entities/characters/x.md",
                    "링크 허브\n\n요약\n\n[[core-canonical-names-and-voice-lock-v1]]\n"
                    "\n## 독자 노출 상한\n\n- 초반 공개 가능: 이름",
                )
            ],
            "entities",
            "",
        ),
        (
            "C6 ignores the entity directory README",
            [("docs/_entities/README.md", "설명 문서")],
            "entities",
            "",
        ),
        (
            "C4 warns on a short episode",
            [
                (
                    "manuscript/ga1/001-x-v2.md",
                    "Status: REVISED\nEpisode: E1\nCanon Check: SELF-PASS\n"
                    "Publication: NOT AUTHORIZED\n\n# t\n\nshort",
                )
            ],
            "manuscripts",
            "C4",
        ),
    ]

    failures = 0
    for name, files, check, expected in cases:
        report = Report()
        if check == "links":
            check_links(files, report)
        elif check == "names":
            check_retired_names(files, report)
        elif check == "entities":
            check_entity_notes(files, report)
        elif check == "arcs":
            check_arc_claims(files, report)
        elif check == "counts":
            check_registry_counts(files, report)
        else:
            check_manuscripts(files, report)

        found = report.errors + report.warnings
        if not expected:
            ok = not found
        elif expected.startswith("!"):
            ok = not any(item.startswith(expected[1:]) for item in found)
        else:
            ok = any(item.startswith(expected) for item in found)

        if ok:
            print(f"  PASS  {name}")
        else:
            failures += 1
            print(f"  FAIL  {name}: {found}")

    print()
    if failures:
        print(f"SELFTEST FAILED — {failures} of {len(cases)} cases")
        return 1
    print(f"SELFTEST PASSED — {len(cases)} cases")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--selftest",
        action="store_true",
        help="run the built-in check fixtures instead of scanning the repository",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="treat warnings as errors (use once open author decisions are settled)",
    )
    args = parser.parse_args()

    if args.selftest:
        return selftest()

    files = collect_markdown(ROOT)
    report = Report()

    link_count = check_links(files, report)
    name_scope = check_retired_names(files, report)
    episode_count = check_manuscripts(files, report)
    entity_count = check_entity_notes(files, report)
    arc_count = check_arc_claims(files, report)
    count_scope = check_registry_counts(files, report)

    report.note(f"markdown files scanned: {len(files)}")
    report.note(f"wikilinks resolved: {link_count}")
    report.note(f"documents checked for retired names: {name_scope}")
    report.note(f"episode manuscripts checked: {episode_count}")
    report.note(f"entity notes checked: {entity_count}")
    report.note(f"registry arc claims checked: {arc_count}")
    report.note(f"registries counting themselves: {count_scope}")

    if report.warnings:
        print("WARNINGS")
        for warning in report.warnings:
            print(f"- {warning}")
        print()

    if report.errors or (args.strict and report.warnings):
        print("CANON VALIDATION FAILED", file=sys.stderr)
        for error in report.errors:
            print(f"- {error}", file=sys.stderr)
        if args.strict:
            for warning in report.warnings:
                print(f"- (strict) {warning}", file=sys.stderr)
        return 1

    print("CANON VALIDATION PASSED")
    for note in report.notes:
        print(f"- {note}")
    if report.warnings:
        print(f"- warnings (not failing): {len(report.warnings)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
