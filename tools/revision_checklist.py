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
    and the episode's closing line.

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

LENGTH_FLOOR = 5500                     # decision-log D-20260806-01
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


def review(path: Path, names: dict[str, set[str]]) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    prose = body_of(text)
    findings: list[str] = []

    chars = len(prose)
    if chars < LENGTH_FLOOR:
        findings.append(f"분량 {chars}자 — 하한 {LENGTH_FLOOR}자까지 {LENGTH_FLOOR - chars}자 부족")

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

    run = best = 0
    for s in sentences(prose):
        run = run + 1 if len(s) < SHORT_SENTENCE else 0
        best = max(best, run)
    if best > SHORT_RUN_LIMIT:
        findings.append(f"{SHORT_SENTENCE}자 미만 문장이 {best}개 연속 — §2-5 단문 남발")

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

    words = Counter(w for w in re.findall(r"[가-힣]{3,}", prose))
    if words:
        word, count = words.most_common(1)[0]
        if count >= 8:
            findings.append(f"'{word}'가 {count}회 반복 — 반복 표현 검토")

    lines = [l.strip() for l in prose.split("\n") if l.strip()]
    prompts = [
        "장면 목적: 이 회차의 각 장면이 무엇을 바꾸는가",
        "인과와 동기: 인물의 선택이 앞 회차에서 설명되는가",
        "전투 공간: 위치·거리·시야·관성·장비 상태가 따라가지는가 (§2-6)",
        "복선: 이 회차가 심거나 회수하는 것이 회수 장부에 있는가",
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
