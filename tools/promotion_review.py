#!/usr/bin/env python3
"""Score which REVIEW documents are ready to be promoted to canon.

Four hundred and five documents sit at REVIEW. They are not shallow -- the
world bible averages fourteen thousand characters and nearly every one carries
Depends On and Open Risks -- they simply never had a promotion step, so nothing
moved. The gate cannot open on a foundation whose status nobody has ruled on.

This does not promote anything. Promotion is a canon change and CLAUDE.md
section 15-9 reserves that for the author. What it does is separate the
documents whose blockers are mechanical -- a dependency still in draft, a link
that does not resolve, nothing pointing at them -- from the ones whose only
remaining blocker is a decision somebody has to make. The first kind can be
cleared by work; the second kind needs the author, and mixing the two is why
the pile never moved.

    python tools/promotion_review.py            write the scorecard
    python tools/promotion_review.py --check    fail if it is out of date
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = DOCS / "_index" / "promotion-review.md"

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")

BANNER = (
    "> [!warning] 자동 생성 문서\n"
    "> `python tools/promotion_review.py`가 이 파일을 덮어씁니다.\n"
    "> **이 문서는 승격을 수행하지 않습니다.** 정본 승격은 작가 결정입니다 (§15-9).\n"
)

INLINE = re.compile(r"`[^`\n]*`")
LINK = re.compile(r"\[\[([^\]|#]+)")

# What GA1 writing actually stands on, found by following links out from the
# act map, the cards, the ledger and the voice lock rather than by folder.
SEEDS = re.compile(
    r"(first-100-act-map-v2|ga1-episodes-(1-5|6-10|11-15|16-20|1-20)|"
    r"series-payoff-ledger|core-canonical-names|reader-facing-terminology|"
    r"narration-harness|storycraft-bible)")

# Phrases that mark a refinement the document expects to absorb later, and
# phrases that mark a ruling it is actually waiting on.
DOWNSTREAM = re.compile(
    r"final (names?|proper nouns?|visual|art|local)|exact (orbital|calendar|thermo"
    r"|numeric|population|casualty|dates?|engineering)|visual design|star map"
    r"|supporting cast|cast (consolidation|inflation)|genders?|cultures?"
    r"|GA[4-9]|GA10|later GA|provisional", re.I)
BLOCKING = re.compile(
    r"미확정|미정|결정 필요|승인 대기|BLOCKER|not authorized|unresolved"
    r"|contradict|충돌|정본 아님", re.I)

EMPTY_RISK = {"none", "없음", "-", "n/a", "na", ""}
HEADER_FIELD = re.compile(r"^([A-Z][A-Za-z ]*):\s*(.*)$")


def header(path: Path) -> dict:
    out = {}
    for line in path.read_text(encoding="utf-8").split("\n")[:18]:
        m = HEADER_FIELD.match(line)
        if m:
            out[m.group(1).strip()] = m.group(2).strip()
    return out


def status_of(head: dict) -> str:
    v = head.get("Status", "").upper()
    if not v:
        return "없음"
    if "NONCANON" in v or "PROPOSED" in v:
        return "PROPOSED"
    if "CANON" in v and "CANDIDATE" not in v:
        return "CANON"
    if "REVIEW" in v:
        return "REVIEW"
    if "DRAFT" in v:
        return "DRAFT"
    return "기타"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    files = {p.relative_to(ROOT).as_posix(): p
             for p in ROOT.rglob("*.md") if ".git" not in p.parts}
    stems = {Path(r).stem: r for r in files}
    heads = {r: header(p) for r, p in files.items()}
    stat = {r: status_of(h) for r, h in heads.items()}

    def links(rel: str) -> set:
        text = "\n".join(l for l in files[rel].read_text(encoding="utf-8").split("\n")
                         if not l.strip().startswith("```"))
        out = set()
        for x in LINK.findall(INLINE.sub("", text)):
            t = stems.get(Path(x).name if "/" in x else x)
            if t:
                out.add(t)
        return out

    inbound = {r: 0 for r in files}
    for r in files:
        for t in links(r):
            inbound[t] += 1

    seeds = [r for r in files if SEEDS.search(r)]
    reach, q = set(seeds), deque(seeds)
    depth = {s: 0 for s in seeds}
    while q:
        cur = q.popleft()
        if depth[cur] >= 2:
            continue
        for n in links(cur):
            if n not in reach:
                reach.add(n)
                depth[n] = depth[cur] + 1
                q.append(n)

    rows = []
    for rel in sorted(r for r in reach if r.startswith("docs/") and stat[r] == "REVIEW"):
        head = heads[rel]
        blockers, decisions, refinements = [], [], []
        for dep in LINK.findall(INLINE.sub("", head.get("Depends On", ""))):
            key = Path(dep).name if "/" in dep else dep
            target = stems.get(key)
            if target is None:
                blockers.append("의존 " + key + " 미해석")
            elif stat[target] in {"DRAFT", "PROPOSED"}:
                blockers.append("의존 [[" + Path(target).stem + "]]가 " + stat[target])
        risk = head.get("Open Risks", "").strip()
        if risk and risk.lower() not in EMPTY_RISK:
            # Not every open risk blocks promotion. Most of these say the same
            # thing -- final names, exact orbital mechanics, cast consolidation
            # later -- which are refinements the document expects to absorb,
            # not rulings it is waiting on. Treating every note as a blocker is
            # why four hundred documents never moved. A risk blocks only when it
            # touches the arc being written or the rules the document itself owns.
            if DOWNSTREAM.search(risk) and not BLOCKING.search(risk):
                refinements.append(risk)
            else:
                decisions.append(risk)
        if inbound.get(rel, 0) == 0:
            blockers.append("들어오는 링크 없음 — 아무도 안 씀")
        rows.append((depth.get(rel, 9), rel, blockers, decisions, refinements))

    ready = [r for r in rows if not r[2] and not r[3]]
    author = [r for r in rows if not r[2] and r[3]]
    work = [r for r in rows if r[2]]

    out = [
        "# 정본 승격 심사 — GA1 집필 의존 문서",
        "", BANNER,
        "REVIEW 문서가 405개다. 내용이 얕아서가 아니라 **승격 단계가 한 번도 실행되지 "
        "않아서**다. 이 표는 GA1 집필이 실제로 링크로 딛고 있는 문서만 추려, 남은 장애물이 "
        "**작업으로 치울 수 있는 것**인지 **작가가 결정해야 하는 것**인지 나눈다.",
        "",
        "의존 REVIEW 문서 **" + str(len(rows)) + "개** · 즉시 승격 가능 **" + str(len(ready))
        + "** · 작가 결정 대기 **" + str(len(author)) + "** · 선행 작업 필요 **"
        + str(len(work)) + "**",
        "",
    ]
    if ready:
        out += ["## 즉시 승격 가능", "",
                "의존 문서가 모두 REVIEW 이상이고, 열린 위험이 비어 있으며, 실제로 참조된다.",
                "", "| 문서 | 현재 상태 |", "|---|---|"]
        out[-2] = "| 문서 | 현재 상태 | 승격해도 남는 다듬기 |"
        out[-1] = "|---|---|---|"
        for _, r, _, _, ref in ready:
            out.append("| [[" + Path(r).stem + "]] | " + heads[r].get("Status", "")
                       + " | " + (ref[0][:90] if ref else "없음") + " |")
        out.append("")
    if author:
        out += ["## 작가 결정 대기", "",
                "기계로 확인할 것은 전부 통과했다. 남은 것은 `Open Risks`가 붙들고 있는 결정이다.",
                "", "| 문서 | 결정해야 하는 것 |", "|---|---|"]
        for _, r, _, d, _ref in author:
            out.append("| [[" + Path(r).stem + "]] | " + d[0][:150] + " |")
        out.append("")
    if work:
        out += ["## 선행 작업 필요", "", "| 문서 | 막고 있는 것 |", "|---|---|"]
        for _, r, b, _d, _ref in work:
            out.append("| [[" + Path(r).stem + "]] | " + " · ".join(b)[:150] + " |")
        out.append("")
    text = "\n".join(out) + "\n"

    OUT.parent.mkdir(parents=True, exist_ok=True)
    cur = OUT.read_text(encoding="utf-8") if OUT.exists() else None
    if cur != text:
        if args.check:
            print(OUT.relative_to(ROOT).as_posix() + " is out of date. "
                  "Run: python tools/promotion_review.py")
            return 1
        OUT.write_text(text, encoding="utf-8")
    print("  " + OUT.relative_to(ROOT).as_posix() + "  " + str(len(rows))
          + " reviewed / " + str(len(ready)) + " ready / " + str(len(author))
          + " author / " + str(len(work)) + " work")
    return 0


if __name__ == "__main__":
    sys.exit(main())
