#!/usr/bin/env python3
"""Generate the per-item catalogue: docs/CATALOG.md and docs/_catalog/*.

Why this exists
---------------
The index (tools/build_index.py) answers "which documents are there". It does
not answer "which characters, frames, hulls and collectibles are there" -- and
that is the question the author actually asks. 680 documents hold roughly 800
named items between them, and until now the only way to see them item by item
was to open the registries one at a time.

Why it is generated
-------------------
The same reason the index is. A hand-written catalogue is wrong the moment a
slot is added, and a wrong catalogue is worse than none. So this reads the
machine-readable sources and lists what is in them:

    docs/06_hardware/data/maneuver-frame-lineup-proposed-index-v1.csv
    docs/06_hardware/named-hull-registry-and-naming-grammar-v1.md
    docs/05_characters/core-canonical-names-and-voice-lock-v1.md
    docs/09_collection/*registry*.md

The catalogue holds no canon of its own -- name, one line of context, status
and a link back to the document that owns the fact (CLAUDE.md section 3).

    python tools/build_catalog.py            write the catalogue
    python tools/build_catalog.py --check    fail if it is out of date
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CAT_DIR = DOCS / "_catalog"
CATALOG = DOCS / "CATALOG.md"

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

BANNER = (
    "> [!warning] 자동 생성 문서\n"
    "> `python tools/build_catalog.py`가 이 파일을 덮어씁니다. 여기에 설정을 쓰지 마십시오.\n"
    "> 정본은 각 항목이 가리키는 문서가 보유합니다.\n"
)

FRAME_CSV = DOCS / "06_hardware/data/maneuver-frame-lineup-proposed-index-v1.csv"
HULL_DOC = DOCS / "06_hardware/named-hull-registry-and-naming-grammar-v1.md"
NAME_LOCK = DOCS / "05_characters/core-canonical-names-and-voice-lock-v1.md"
CENSUS_CSV = DOCS / "09_collection/data/cast-role-tier-census-resolved-v1.csv"

# ---------------------------------------------------------------- characters


def read_characters() -> list[tuple[str, str, str]]:
    """(id, name, role line) for every locked canonical name."""
    out: list[tuple[str, str, str]] = []
    lines = NAME_LOCK.read_text(encoding="utf-8").split("\n")
    section = ""
    for i, line in enumerate(lines):
        if line.startswith("## ") and "Final Lock" in line:
            section = line[3:].split("—")[0].strip()
        m = re.match(r"^### ([A-Z][A-Z0-9-]*-\d+) — (.+?) / (.+)$", line)
        if not m:
            continue
        role = ""
        for nxt in lines[i + 1 : i + 12]:
            if nxt.startswith("###") or nxt.startswith("## "):
                break
            stripped = nxt.strip("- ").strip()
            if stripped and not stripped.endswith(":"):
                role = stripped.rstrip(".")
                break
        out.append((m.group(1), m.group(2).strip(), f"{section} · {role}" if role else section))
    return out


def read_census() -> list[tuple[str, str]]:
    if not CENSUS_CSV.exists():
        return []
    rows = list(csv.DictReader(CENSUS_CSV.open(encoding="utf-8-sig")))
    key = next((k for k in rows[0] if "tier" in k.lower()), None)
    count = next((k for k in rows[0] if "count" in k.lower() or "resolved" in k.lower()), None)
    if not key:
        return []
    return [(r[key], r.get(count, "")) for r in rows]


# -------------------------------------------------------------------- frames


def read_frames() -> list[dict[str, str]]:
    return list(csv.DictReader(FRAME_CSV.open(encoding="utf-8-sig")))


# --------------------------------------------------------------------- hulls

HULL_ROW = re.compile(
    r"^\| (S-\d+) \| `([^`]+)` \| \*?\*?([^|*]+?)\*?\*? \| (\w+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$"
)


def read_hulls() -> list[tuple[str, ...]]:
    out = []
    faction = ""
    for line in HULL_DOC.read_text(encoding="utf-8").split("\n"):
        if line.startswith("### 4."):
            faction = line.split(" ", 2)[2].strip()
        m = HULL_ROW.match(line)
        if m:
            out.append((*[g.strip() for g in m.groups()], faction))
    return out


# ---------------------------------------------------------------- collection

ITEM = re.compile(r"^## (G\d+-[A-Z]+\d+|[A-Z]\d+-[A-Z0-9]+) — (.+)$")
SECTION = re.compile(r"^# ([A-Z])\. (.+)$")


def read_collection() -> dict[str, list[tuple[str, str, str]]]:
    """{registry stem: [(id, title, section)]}"""
    out: dict[str, list[tuple[str, str, str]]] = {}
    for path in sorted((DOCS / "09_collection").glob("*registry*.md")):
        items: list[tuple[str, str, str]] = []
        section = ""
        for line in path.read_text(encoding="utf-8").split("\n"):
            sm = SECTION.match(line)
            if sm:
                section = sm.group(2).strip()
                continue
            im = ITEM.match(line)
            if im:
                items.append((im.group(1), im.group(2).strip(), section))
        if items:
            out[path.stem] = items
    return out


# --------------------------------------------------------------------- write


def page(title: str, intro: str, body: list[str]) -> str:
    return "\n".join([f"# {title}", "", BANNER, intro, "", *body, ""])


def build() -> dict[Path, str]:
    pages: dict[Path, str] = {}

    chars = read_characters()
    body = ["| ID | 이름 | 위치 |", "|---|---|---|"]
    body += [f"| `{cid}` | **{name}** | {role} |" for cid, name, role in chars]
    body += ["", f"정본: [[core-canonical-names-and-voice-lock-v1]] · 총 {len(chars)}명 잠금.",
             "", "이 아래로 배역 시트 60여 종이 대액트별로 나뉘어 있다 — [[index-characters]].",
             "역할 센서스 197명(주인공 1 / 핵심 아군 4 / 적수·라이벌 9 / 반복 조연 40 / 중요 단역 143)의",
             "근거는 [[role-demand-portfolio-count-audit-v1]]에 있다."]
    pages[CAT_DIR / "catalog-characters.md"] = page(
        "인물 — 정본 잠금 이름", "이름이 잠긴 인물 전원. 설정은 각 인물 바이블이 보유한다.", body)

    frames = read_frames()
    by_lin: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in frames:
        by_lin[r["lineage_id"]].append(r)
    body = []
    for lin in sorted(by_lin):
        body += [f"## {lin}", "", "| 슬롯 | 형식 | 이름 | 역할 | 첫 공개 | 등급 | 상태 |",
                 "|---|---|---|---|---|---|---|"]
        for r in by_lin[lin]:
            ko = r["working_name_ko"] or "—"
            body.append(
                f"| `{r['slot_id']}` | `{r['formal_code']}` | **{ko}** / {r['working_name_en']} "
                f"| {r['role']} | {r['first_reveal_window']} | {r['reader_tier']} | {r['canon_status']} |")
        body.append("")
    body += [f"총 {len(frames)}행 — 정본 실체 1, 섀시 슬롯 43, 작가 결정 예비 2.",
             "밴드와 근거: [[maneuver-frame-lineup-master-architecture-v1]] · 결정: [[decision-log]] D-20260813-03."]
    pages[CAT_DIR / "catalog-frames.md"] = page(
        "기체 — 슬롯 전체", "제조 계보별 기동 프레임. `PROPOSED — NONCANON`이 기본이며 07호만 정본이다.", body)

    hulls = read_hulls()
    by_fac: dict[str, list[tuple[str, ...]]] = defaultdict(list)
    for h in hulls:
        by_fac[h[-1]].append(h)
    body = []
    for fac in by_fac:
        body += [f"## {fac}", "", "| ID | 선적번호 | 통칭 | 급수 | 탑재 | 첫 등장 | 근거 | 상태 |",
                 "|---|---|---|---|---|---|---|---|"]
        for h in by_fac[fac]:
            body.append("| `%s` | `%s` | **%s** | %s | %s | %s | %s | %s |" % h[:8])
        body.append("")
    body += [f"총 {len(hulls)}행 — 정본 1척, 제안 39척, 선체 아님 1건.",
             "급수·탑재 정원과 명명 문법: [[named-hull-registry-and-naming-grammar-v1]]."]
    pages[CAT_DIR / "catalog-hulls.md"] = page(
        "함선 — 명명 선체 전체", "진영별 명명 선체. 어근이 그 세력이 정통성을 어디서 끌어오는지 드러낸다.", body)

    coll = read_collection()
    total = sum(len(v) for v in coll.values())
    body = []
    for stem, items in coll.items():
        body += [f"## [[{stem}]]", "", "| ID | 항목 | 절 |", "|---|---|---|"]
        body += [f"| `{i}` | {t} | {s} |" for i, t, s in items]
        body.append("")
    body += [f"총 {total}개 항목. **항목 수는 실체 수가 아니다** — 한 줄은 실체일 수도, 관계·권리·상태 변화·상실 부담·회수 약속·세트 목표일 수도 있다.",
             "등재 종류 7축과 분야 8개(C1–C8): [[collection-desire-master-architecture-and-index-audit-v1]]."]
    pages[CAT_DIR / "catalog-collection.md"] = page(
        "수집 — 등록 항목 전체", "대액트별 수집 등록표의 항목을 한 줄씩 편 것.", body)

    home = [
        "| 분야 | 항목 수 | 카탈로그 |",
        "|---|---:|---|",
        f"| 인물 (정본 잠금) | {len(chars)} | [[catalog-characters]] |",
        f"| 기체 | {len(frames)} | [[catalog-frames]] |",
        f"| 함선 | {len(hulls)} | [[catalog-hulls]] |",
        f"| 수집 등록 항목 | {total} | [[catalog-collection]] |",
        "",
        "## 아직 항목 단위로 없는 것",
        "",
        "무기·부품(C3), 유물·보물(C4), 기술(C6), 세력·제도(C7), 영토·노드(C8)는 대액트별 등록표 안에",
        "섞여 있고 독립 등록부가 없다. 위 수집 카탈로그에서 절 이름으로 찾을 수는 있으나,",
        "기체·함선처럼 기계가 읽는 표를 아직 갖지 않는다.",
        "",
        "문서 단위 입구는 [[HOME]]이다. 이 카탈로그는 문서가 아니라 **항목**을 센다.",
    ]
    pages[CATALOG] = page("CATALOG — 항목 단위 목록", "저장소가 이름을 붙인 것 전부를 분야별로 편 목록.", home)
    return pages


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    CAT_DIR.mkdir(parents=True, exist_ok=True)
    pages = build()
    stale = []
    for path, text in pages.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != text:
            stale.append(path)
            if not args.check:
                path.write_text(text, encoding="utf-8")
        print(f"  {path.relative_to(ROOT).as_posix()}")
    if args.check and stale:
        print(f"\n{len(stale)} catalogue file(s) out of date. Run: python tools/build_catalog.py")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
