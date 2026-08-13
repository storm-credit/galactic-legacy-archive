#!/usr/bin/env python3
"""Collect every open question the repository is carrying.

The pre-writing gate asks that undecided items and assumptions are not hidden.
They were not hidden -- every document carries an `Open Risks:` header, and
`[ASSUMPTION]` markers sit where CLAUDE.md section 3 asks for them. But there
was no way to see them together, so "what is still undecided here" could only
be answered by opening 700 files.

This reads the headers and lists them. It holds no judgement of its own: the
risk text belongs to the document that wrote it.

    python tools/build_open_questions.py            write the list
    python tools/build_open_questions.py --check    fail if it is out of date
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = DOCS / "_index" / "open-questions.md"

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

BANNER = (
    "> [!warning] 자동 생성 문서\n"
    "> `python tools/build_open_questions.py`가 이 파일을 덮어씁니다.\n"
    "> 미결정 내용은 각 문서의 `Open Risks:` 헤더가 보유합니다. 여기서 고치지 마십시오.\n"
)

SKIP_DIRS = {"_index", "_catalog"}
ASSUMPTION = re.compile(r"\[ASSUMPTION[^\]]*\]")
# Risk headers that only say "none" are not open questions.
EMPTY = {"none", "없음", "-", "n/a", "na"}


def link_target(path: Path) -> str:
    """Bare stem, or the full path when several files share the basename.

    C1 rejects an ambiguous bare wikilink, and a generator that emits one is
    the fastest way to break the graph for every document it touches.
    """
    same = [q for q in ROOT.rglob(path.name) if ".git" not in q.parts]
    if len(same) > 1:
        return path.relative_to(ROOT).as_posix()[: -len(".md")]
    return path.stem


def collect() -> tuple[dict[str, list[tuple[str, str]]], list[tuple[str, int]]]:
    risks: dict[str, list[tuple[str, str]]] = defaultdict(list)
    assumptions: list[tuple[str, int]] = []
    for path in sorted(DOCS.rglob("*.md")):
        parts = path.relative_to(DOCS).parts
        if parts[0] in SKIP_DIRS or path.name in {"HOME.md", "CATALOG.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        count = len(ASSUMPTION.findall(text))
        if count:
            assumptions.append((link_target(path), count))
        for line in text.split("\n")[:20]:
            if not line.startswith("Open Risks:"):
                continue
            body = line.split(":", 1)[1].strip()
            if body.lower() in EMPTY or not body:
                break
            risks[parts[0]].append((link_target(path), body))
            break
    return risks, assumptions


def render() -> str:
    risks, assumptions = collect()
    total = sum(len(v) for v in risks.values())
    out = [
        "# 미결정과 가정 — 저장소 전체",
        "",
        BANNER,
        "게이트 §12는 미결정과 가정이 숨겨져 있지 않을 것을 요구한다. 숨겨져 있지는 않았고,",
        "한자리에 모여 있지 않았을 뿐이다. 이 목록이 그 자리다.",
        "",
        f"`Open Risks`를 가진 문서 **{total}개** · `[ASSUMPTION]` 표기를 가진 문서 "
        f"**{len(assumptions)}개**",
        "",
    ]
    if assumptions:
        out += ["## 명시적 가정 `[ASSUMPTION]`", "",
                "답이 없어 합리적 기본값으로 진행한 항목이다 (CLAUDE.md §3).", "",
                "| 문서 | 표기 수 |", "|---|---:|"]
        out += [f"| [[{stem}]] | {n} |" for stem, n in sorted(assumptions, key=lambda x: -x[1])]
        out.append("")
    out += ["## 분야별 열린 위험", ""]
    for section in sorted(risks):
        out += [f"### {section} — {len(risks[section])}건", "", "| 문서 | 열린 위험 |", "|---|---|"]
        for stem, body in risks[section]:
            out.append(f"| [[{stem}]] | {body} |")
        out.append("")
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    text = render()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    current = OUT.read_text(encoding="utf-8") if OUT.exists() else None
    if current != text:
        if args.check:
            print(f"{OUT.relative_to(ROOT).as_posix()} is out of date. "
                  f"Run: python tools/build_open_questions.py")
            return 1
        OUT.write_text(text, encoding="utf-8")
    print(f"  {OUT.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
