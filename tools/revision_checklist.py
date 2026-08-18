#!/usr/bin/env python3
"""Run the manuscript revision harness over an episode.

CLAUDE.md section 6 lists ten review steps for a finished draft. It has been
prose since the day it was written, which is why the gate scored it PARTIAL:
a checklist nobody can run is a checklist nobody runs.

This does the part a machine can do and says plainly which part it cannot.

Mechanical, reported as findings:

    length against the floor, header schema, the publication block,
    retired canon names, wikilinks leaking into published text,
    runs of very short sentences, proper-noun load against the registries'
    exposure ceilings, and the most repeated phrase.

Human, reported as prompts with the material pulled out:

    scene purpose, causality and motive, combat space, payoff placement,
    the episode's closing line, and the two narration axes that need ears:
    whether six voices survive covering the tags, and whether a clue line
    stays flat when read aloud.

    python tools/revision_checklist.py manuscript/ga1/001-*.md
    python tools/revision_checklist.py --all
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

LENGTH_FLOOR = 5500   # D-20260806-01; POST-HOC gate per D-20260816-01 -- never a writing target
SHORT_SENTENCE = 18                     # characters; below this counts as 단문
SHORT_RUN_LIMIT = 3                     # CLAUDE.md section 2-5
PUBLICATION_FIELDS = ("Publication", "Publication Status")
REQUIRED_PUBLICATION = "NOT AUTHORIZED"

RETIRED = ("리안 카르도", "Rian Cardo", "회랑새", "Corridor Wren")

# The reader-memory authority sets the budget, not the registries.
# reader-facing-terminology-phonetics-and-register-bible-v1 section 2, per episode.
# The registries used to carry their own per-scene ceilings; six local numbers
# summed to 21 against a canon budget of 4, which is why they were withdrawn.
FIRST_USE_BUDGET = 4          # total proper nouns in first-time use
ACTIVE_PLACES = 3
ACTIVE_ORGS = 3
NEW_TECH_TERMS = 2

# Names come from the anchor CSVs, which carry a clean `name` column. Reading
# the markdown tables instead pulled in column headers like 비용 and 이름 as if
# they were registry names.
ANCHOR_SOURCES = {
    "기체": "docs/06_hardware/data/maneuver-frame-lineup-proposed-index-v1.csv",
    "무기": "docs/06_hardware/data/anchor-fields-weapons-v1.csv",
    "함선": "docs/06_hardware/data/anchor-fields-hulls-v1.csv",
    "기술": "docs/06_hardware/data/anchor-fields-technologies-v1.csv",
    "유물": "docs/09_collection/data/anchor-fields-relics-v1.csv",
    "장소": "docs/02_world/data/anchor-fields-places-v1.csv",
}

SENTENCE_END = re.compile(r"[.!?。…]+[\s”\"']*|\n")
KOREAN_NAME = re.compile(r"[가-힣]{2,6}")


def registry_names() -> dict[str, set[str]]:
    """Reader-facing names per domain, from the anchor CSVs."""
    import csv

    out: dict[str, set[str]] = {}
    for domain, rel in ANCHOR_SOURCES.items():
        path = ROOT / rel
        names: set[str] = set()
        if path.exists():
            with path.open(encoding="utf-8-sig") as handle:
                for row in csv.DictReader(handle):
                    value = (row.get("name") or row.get("working_name_ko") or "").strip()
                    if value and value != "—" and len(value) >= 2 and "(" not in value:
                        names.add(value)
        out[domain] = names
    return out


def body_of(text: str) -> str:
    """Prose only: drop the header block so field text is not measured."""
    lines = text.split("\n")
    start = 0
    for i, line in enumerate(lines[:25]):
        if re.match(r"^[A-Za-z][A-Za-z ]*:", line):
            start = i + 1
    return "\n".join(lines[start:])


def sentences(prose: str) -> list[str]:
    return [s.strip() for s in SENTENCE_END.split(prose) if s and s.strip()]


def narration_runs(prose: str) -> int:
    """Longest run of short sentences inside one unbroken narration block.

    Section 2-5 forbids chopping the reader's breath with strings of short
    sentences. Two things are not that:

    - dialogue, which is short by nature;
    - narration lines separated by dialogue, which the reader receives as
      alternating rhythm, not as a run.

    So the run resets whenever a spoken line or a system block intervenes.
    Measuring without those resets failed every argument scene in the draft,
    which was the measurement's fault.
    """
    best = run = 0
    for line in prose.split("\n"):
        s = line.strip()
        if not s:
            continue
        if s.startswith("[") or "“" in s or "”" in s or '"' in s:
            run = 0
            continue
        for piece in SENTENCE_END.split(s):
            piece = piece.strip()
            if not piece:
                continue
            run = run + 1 if len(piece) < SHORT_SENTENCE else 0
            best = max(best, run)
    return best


# Grammatical staples. Repeating 있었다 is Korean, not a tic; the check exists
# to surface a distinctive word being leaned on.
REPETITION_STOPLIST = {
    "있었다", "없었다", "않았다", "이었다", "아니었다", "같았다", "보였다",
    "그것은", "그러나", "그리고", "하지만",
}
PRONUNCIATION_SOURCE = "docs/00_project/reader-facing-terminology-phonetics-and-register-bible-v1.md"
NARRATION_HARNESS = "docs/13_writing_harness/narration-harness-v1.md"

# A bracketed line is read in a machine voice, so anything the machine did not
# print must not wear brackets -- signs, labels, stencils, printed notices.
PHYSICAL_MARK_WORDS = (
    "표지판", "명찰", "각인", "인쇄", "게시", "팻말", "스텐실",
)
DIALOGUE_TAGS = ("말했다", "물었다", "답했다", "대답했다",
                 "덧붙였다", "중얼거렸다", "외쳤다", "속삭였다")
TAG_DOMINANCE = 0.55


def pronunciation_entries() -> set[str]:
    """Names the pronunciation dictionary already fixes (narration axis 4)."""
    out: set[str] = set()
    for rel in (PRONUNCIATION_SOURCE, NARRATION_HARNESS):
        path = ROOT / rel
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").split("\n"):
            if line.startswith("|"):
                cell = line.split("|")[1].strip().strip("`*")
                if cell and re.fullmatch(r"[가-힣][가-힣 /·0-9A-Za-z-]{0,20}", cell):
                    out.add(cell)
            if "발음 고정" in line or "한글 정본 표기를 따른다" in line:
                out.update(re.findall(r"[가-힣]{2,6}", line))
            for src, _dst in re.findall(r"`([^`]+?)\s*→\s*([^`]+?)`", line):
                out.add(src.strip())
    return out


def narration_findings(prose: str, names: dict) -> list:
    """narration-harness-v1 axes 2, 3 and 4, the machine-checkable parts."""
    out: list = []

    for line in prose.split("\n"):
        s = line.strip()
        if s.startswith("[") and s.endswith("]") and any(w in s for w in PHYSICAL_MARK_WORDS):
            out.append(f"물리 표식에 대괄호 — 낭독이 기계음으로 읽는다: {s[:40]}")

    known = pronunciation_entries()
    if known:
        # A name counts as used only at a word boundary. `n in prose` matched
        # the relic 리마 inside 허리마운트. Korean never prefix-compounds a
        # proper noun, so the preceding character must not be Hangul; the
        # following character may be a particle but not the middle of a word.
        josa = set("은는이가을를과와도의로에게서만까지부터라야며처럼보다")
        def _used(name: str) -> bool:
            start = 0
            while True:
                i = prose.find(name, start)
                if i < 0:
                    return False
                before = prose[i - 1] if i > 0 else " "
                after_i = i + len(name)
                after = prose[after_i] if after_i < len(prose) else " "
                if not ("가" <= before <= "힣") and (
                        not ("가" <= after <= "힣") or after in josa):
                    return True
                start = i + 1
        used = {n for ns in names.values() for n in ns if _used(n)}
        missing = sorted(n for n in used if n not in known)
        if missing:
            out.append("발음 사전 미등재 고유명 — 낭독이 임의 발음을 만든다: " + ", ".join(missing))

    counts = {tag: prose.count(tag) for tag in DIALOGUE_TAGS}
    tagged = sum(counts.values())
    if tagged >= 8:
        tag, top = max(counts.items(), key=lambda kv: kv[1])
        if top / tagged > TAG_DOMINANCE:
            out.append(
                f"대사 태그 {tagged}개 중 '{tag}'가 {top}개 ({top/tagged:.0%}) — "
                f"화자 구별이 태그에 실리지 않는다 (축 2)"
            )
    return out


ACT_MAP = "docs/10_story_architecture/first-100-act-map-v2-consolidated.md"
PAYOFF_LEDGER = "docs/11_mystery/series-payoff-ledger-v1.md"

SUBACT_HEAD = re.compile(r"^## (A\d+) — (.+?) / Episodes (\d+)[–-](\d+)\s*$")
EPISODE_HEAD = re.compile(r"^E(\d+):\s*$")
PLANT_WINDOW = re.compile(r"^### Plant — Episodes? (\d+)(?:[–-](\d+))?")
MYSTERY_HEAD = re.compile(r"^## (M-\d+) — (.+?)\s*$")


def act_map_entry(number: int) -> tuple[str, list[str]] | None:
    """(sub-act label, what the act map says this episode does)."""
    path = ROOT / ACT_MAP
    if not path.exists():
        return None
    subact = ""
    lines = path.read_text(encoding="utf-8").split("\n")
    for i, line in enumerate(lines):
        head = SUBACT_HEAD.match(line)
        if head:
            a, title, lo, hi = head.groups()
            subact = f"{a} 「{title}」 / {lo}–{hi}화"
            continue
        ep = EPISODE_HEAD.match(line.strip())
        if ep and int(ep.group(1)) == number:
            body = []
            for nxt in lines[i + 1:]:
                if nxt.startswith("- "):
                    body.append(nxt[2:].strip())
                elif body or nxt.strip():
                    break
            return subact, body
    return None


def active_clues(number: int) -> list[str]:
    """Mysteries whose plant window covers this episode."""
    path = ROOT / PAYOFF_LEDGER
    if not path.exists():
        return []
    out, current = [], ""
    for line in path.read_text(encoding="utf-8").split("\n"):
        head = MYSTERY_HEAD.match(line)
        if head:
            current = f"{head.group(1)} {head.group(2)}"
            continue
        window = PLANT_WINDOW.match(line)
        if window and current:
            lo = int(window.group(1))
            hi = int(window.group(2)) if window.group(2) else lo
            if lo <= number <= hi:
                out.append(current)
    return out


def review(path: Path, names: dict[str, set[str]]) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    prose = body_of(text)
    findings: list[str] = []

    chars = len(prose)
    if chars < LENGTH_FLOOR:
        # D-20260816-01 / CLAUDE.md section 20: the floor is a POST-HOC QC
        # gate, never a writing target. This report used to print the deficit
        # ("N자 부족"), and that number was read as an amount to fill -- which
        # is padding by instruction. So the finding names the gate and routes
        # a scene-complete-but-short draft to structural review instead of to
        # the keyboard.
        findings.append(
            f"분량 {chars}자 — C4 사후 게이트({LENGTH_FLOOR}자) 미달. "
            "채우지 말 것: 승인 장면카드의 생략·압축된 비트를 먼저 확인하고, "
            "비트가 전부 살아 있다면 STRUCTURAL LENGTH REVIEW로 보낸다 (§20)")

    header = "\n".join(text.split("\n")[:20])
    if not any(f"{f}:" in header for f in PUBLICATION_FIELDS):
        findings.append("출판 차단 필드가 없다")
    elif REQUIRED_PUBLICATION not in header:
        findings.append(f"출판 필드가 {REQUIRED_PUBLICATION!r}가 아니다")

    for name in RETIRED:
        if name in prose:
            findings.append(f"폐기된 정본명 {name!r}이 본문에 있다")

    if "[[" in prose:
        findings.append("원고 본문에 위키링크가 있다 (CLAUDE.md §14-5)")

    best = narration_runs(prose)
    if best > SHORT_RUN_LIMIT:
        findings.append(f"{SHORT_SENTENCE}자 미만 지문이 {best}개 연속 — §2-5 단문 남발")

    present: dict[str, list[str]] = {
        d: sorted(n for n in ns if n in prose) for d, ns in names.items()
    }
    total = sum(len(v) for v in present.values())
    if total > FIRST_USE_BUDGET:
        detail = "; ".join(f"{d} {', '.join(v)}" for d, v in present.items() if v)
        findings.append(
            f"등록 고유명 {total}개 등장 — 회차당 최초 사용 예산 {FIRST_USE_BUDGET} "
            f"(독자 기억 권위 §2): {detail}"
        )
    if len(present.get("장소", [])) > ACTIVE_PLACES:
        findings.append(f"활성 장소 {len(present['장소'])}개 — 예산 {ACTIVE_PLACES}")

    findings += narration_findings(prose, names)

    words = Counter(w for w in re.findall(r"[가-힣]{3,}", prose)
                    if w not in REPETITION_STOPLIST)
    if words:
        word, count = words.most_common(1)[0]
        if count >= 8:
            findings.append(f"'{word}'가 {count}회 반복 — 반복 표현 검토")

    lines = [l.strip() for l in prose.split("\n") if l.strip()]

    number = None
    m = re.search(r"^Episode:\s*E(\d+)", text, re.M)
    if m:
        number = int(m.group(1))
    elif re.match(r"^\d{3}-", path.name):
        number = int(path.name[:3])

    structure: list[str] = []
    if number is not None:
        entry = act_map_entry(number)
        if entry:
            subact, body = entry
            structure.append(f"서브액트: {subact}")
            for b in body:
                structure.append(f"액트맵이 이 회차에 요구하는 것: {b}")
        else:
            findings.append(f"E{number}가 액트맵에 없다 — 구조 밖 회차")
        clues = active_clues(number)
        if clues:
            structure.append("심기 구간이 열린 미스터리: " + " · ".join(clues))

    prompts = structure + [
        "장면 목적: 이 회차의 각 장면이 무엇을 바꾸는가",
        "인과와 동기: 인물의 선택이 앞 회차에서 설명되는가",
        "전투 공간: 위치·거리·시야·관성·장비 상태가 따라가지는가 (§2-6)",
        "복선: 이 회차가 심거나 회수하는 것이 회수 장부에 있는가",
        "낭독 축 2: 화자 표기를 가려도 여섯 명이 구별되는가",
        "낭독 축 5: 복선 문장을 평문 톤으로 읽어도 정보가 새지 않는가",
        f"엔딩 훅 — 마지막 줄: {lines[-1][:70] if lines else '(없음)'}",
    ]
    return findings, prompts


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    targets = (sorted((ROOT / "manuscript").rglob("*.md")) if args.all
               else [Path(p).resolve() for p in args.paths])
    if not targets:
        print("대상 원고가 없다. 경로를 주거나 --all 을 쓴다.")
        return 2

    names = registry_names()
    total = 0
    for path in targets:
        findings, prompts = review(path, names)
        total += len(findings)
        print(f"\n=== {path.relative_to(ROOT).as_posix()}")
        for f in findings:
            print(f"  - {f}")
        if not findings:
            print("  기계 검토 항목 이상 없음")
        print("  사람이 볼 것:")
        for p in prompts:
            print(f"    · {p}")
    print(f"\n원고 {len(targets)}편, 기계 검토 지적 {total}건")
    return 0


if __name__ == "__main__":
    sys.exit(main())
