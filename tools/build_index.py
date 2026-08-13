#!/usr/bin/env python3
"""Generate the Obsidian entry point: docs/HOME.md and docs/_index/*.

Why this is generated rather than written by hand
-------------------------------------------------
680 documents, and the count moves every session. A hand-written table of
contents is wrong the moment a document is added, and a wrong index is worse
than none -- it is the same failure mode as a wrong wikilink.

So the index holds no settings of its own. It reads the repository, lists what
is there with each document's own title and status, and links. Canon stays in
the documents (CLAUDE.md section 3: one canonical document plus links, never a
copy).

    python tools/build_index.py            write the index
    python tools/build_index.py --check    fail if the index is out of date

One caveat, stated here because it is easy to be misled by it: these notes link
to nearly every document, so after they exist almost nothing is an orphan in
the raw graph. The connectivity table inside HOME.md therefore ignores the
index notes when it counts links. Real linkage progress is what the design
documents point at, not what the index sweeps up.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INDEX_DIR = DOCS / "_index"
HOME = DOCS / "HOME.md"

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

BANNER = (
    "> [!warning] 자동 생성 문서\n"
    "> `python tools/build_index.py`가 이 파일을 덮어씁니다. 여기에 설정을 쓰지 마십시오.\n"
    "> 정본은 링크가 가리키는 문서가 보유합니다.\n"
)

# 분야별 입구. (파일명, 제목, 설명, 해당 디렉터리들)
SECTIONS = [
    ("index-story", "줄거리와 플롯",
     "대액트 → 액트맵 → 회차 카드 순서. 회차 번호로 정렬되어 있어 위에서 아래로 읽으면 전개가 됩니다.",
     ["10_story_architecture", "11_mystery"]),
    ("index-characters", "인물",
     "정본 이름 잠금에 등록된 인물과, 인물·배역 설계 문서 전부.",
     ["05_characters"]),
    ("index-frames", "기체와 장비",
     "기체 계보, 함선, 무장, 생산 규격.",
     ["06_hardware"]),
    ("index-collection", "수집",
     "대액트별 수집 등록표와 수집 설계.",
     ["09_collection", "09_collection_system"]),
    ("index-factions", "세력",
     "제국·독립군·기업·학원과 세력 대칭 설계.",
     ["03_factions", "04_factions"]),
    ("index-world", "세계와 무대",
     "천문·항행·물리 규칙, 교도학원, 운용 상태 시트.",
     ["02_world", "03_academy", "03_systems", "01_concept", "01_timeline"]),
    ("index-craft", "집필 규격과 제도",
     "문체·낭독 하네스, 군사 교리, 법·제도, 손실 장부, 조사 자료.",
     ["07_style", "13_writing_harness", "07_military", "06_law",
      "08_institutions", "12_losses", "12_research"]),
    ("index-project", "프로젝트 운영",
     "게이트 기록, 감사, 결정 로그, 품질 관리.",
     ["00_project", "99_quality_control"]),
]

# 자주 여는 정본. 없으면 조용히 건너뜁니다.
QUICK_LINKS = [
    ("1000-episode-grand-act-map-v1", "1000화 대액트 지도"),
    ("first-100-act-map-v2-consolidated", "1~100화 액트맵 (정본)"),
    ("master-series-chronology-v1", "시리즈 연표"),
    ("core-canonical-names-and-voice-lock-v1", "인물 이름·음성 잠금"),
    ("canon-core-packet-v1", "정본 핵심 패킷"),
    ("prewriting-gate", "집필 개시 게이트"),
    ("decision-log", "결정 로그"),
    ("original-timeline-v1", "원래 시간선"),
]

LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


class Doc:
    def __init__(self, path: Path):
        self.path = path
        self.name = path.stem
        self.rel = path.relative_to(ROOT).as_posix()
        self.top = path.relative_to(DOCS).parts[0]
        text = path.read_text(encoding="utf-8")
        self.lines = text.split("\n")
        self.title = next((l[2:].strip() for l in self.lines[:5]
                           if l.startswith("# ")), self.name)
        status = next((l.split(":", 1)[1] for l in self.lines[:30]
                       if l.startswith("Status:")), "")
        self.status = status.strip().split(" — ")[0].split(" -- ")[0].strip()
        # [[dir/name#section|label]] -> name
        self.links = [m.split("|")[0].split("#")[0].strip().split("/")[-1]
                      for m in LINK_RE.findall(text)]

    # ga4-episodes-331-450-... -> (4, 331); first-100-act-map-... -> (1, 1)
    def episode_key(self):
        ga = re.match(r"ga(\d+)", self.name)
        ga_num = int(ga.group(1)) if ga else (1 if "first-100" in self.name else 99)
        eps = re.search(r"(?:episodes?|-e)[-]?(\d+)[-–](\d+)", self.name)
        start = int(eps.group(1)) if eps else 0
        return (ga_num, start, self.name)


def collect():
    skip = {"_index", "_catalog"}
    docs = []
    for p in sorted(DOCS.rglob("*.md")):
        parts = p.relative_to(DOCS).parts
        if parts[0] in skip or p.name in {"HOME.md", "CATALOG.md"}:
            continue
        docs.append(Doc(p))
    return docs


def table(rows, headers, align=None):
    align = align or ["---"] * len(headers)
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(align) + "|"]
    for r in rows:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def doc_rows(docs, duplicated=frozenset()):
    rows = []
    for d in docs:
        # CLAUDE.md section 11-3: a basename that exists in two directories
        # must be linked by full path, or the link is ambiguous.
        target = d.rel[:-3] if d.name in duplicated else d.name
        title = d.title.split(" — ")[0].split(" -- ")[0]
        if len(title) > 60:
            title = title[:57] + "…"
        rows.append(["[[%s|%s]]" % (target, d.name), title, d.status or "—"])
    return rows


def character_roster(docs):
    """The eight locked identities, read out of the lock document itself."""
    lock = next((d for d in docs
                 if d.name == "core-canonical-names-and-voice-lock-v1"), None)
    if lock is None:
        return None
    entities = {p.stem for p in (DOCS / "_entities" / "characters").glob("*.md")}
    rows = []
    for line in lock.lines:
        m = re.match(r"^###\s+([A-Z]-\d{3})\s+[—-]\s+(.+?)\s*/\s*(.+?)\s*$", line)
        if not m:
            continue
        ident, ko, en = m.groups()
        hub = ko.replace(" ", "-")
        rows.append([ident, "[[%s]]" % hub if hub in entities else ko, en])
    return rows


def build_section(key, title, blurb, dirs, docs, duplicated):
    picked = [d for d in docs if d.top in dirs]
    body = [BANNER, "", "# %s" % title, "", blurb, "",
            "정본 목록은 [[HOME]]에서 갈라집니다.", ""]

    if key == "index-characters":
        roster = character_roster(docs)
        if roster:
            body += ["## 정본 등록 인물", "",
                     "이름은 [[core-canonical-names-and-voice-lock-v1]]가 통제합니다. "
                     "링크가 걸린 이름은 개체 허브 노트가 있는 인물입니다.", "",
                     table(roster, ["ID", "이름", "표기"]), ""]

    if key == "index-frames":
        body += ["## 계수 규칙", "",
                 "기체 수를 세기 전에 CLAUDE.md §16-10을 확인하십시오. "
                 "색·무장·소프트웨어·가역 임무팩 변경은 새 기체가 아니라 상태로 셉니다. "
                 "등록표 행 수를 기체 수로 재사용하지 마십시오.", ""]
        hubs = sorted(p.stem for p in (DOCS / "_entities" / "frames").glob("*.md"))
        if hubs:
            body += ["## 개체 허브", "",
                     ", ".join("[[%s]]" % h for h in hubs), ""]

    if key == "index-story":
        picked.sort(key=lambda d: d.episode_key())
        for group, label in (("root", "설계 문서"), ("detail", "상세 회차 설계")):
            sub = [d for d in picked
                   if (d.path.parent.name == "detail") == (group == "detail")]
            if not sub:
                continue
            body += ["## %s (%d)" % (label, len(sub)), "",
                     table(doc_rows(sub, duplicated), ["문서", "제목", "상태"]), ""]
        return "\n".join(body).rstrip() + "\n"

    by_dir = defaultdict(list)
    for d in picked:
        by_dir[d.top].append(d)
    for top in dirs:
        if not by_dir[top]:
            continue
        body += ["## %s (%d)" % (top, len(by_dir[top])), "",
                 table(doc_rows(sorted(by_dir[top], key=lambda d: d.name), duplicated),
                       ["문서", "제목", "상태"]), ""]
    return "\n".join(body).rstrip() + "\n"


def build_home(docs):
    out_links = Counter()
    in_links = Counter()
    names = {d.name for d in docs}
    # Manuscripts live outside docs/ but are legitimate link targets, so a
    # design document that only points at episodes is not "silent".
    resolvable = names | {p.stem for p in ROOT.glob("manuscript/**/*.md")}
    for d in docs:
        for target in d.links:
            if target == d.name or target not in resolvable:
                continue
            out_links[d.name] += 1
            if target in names:
                in_links[target] += 1

    rows = []
    for key, title, _blurb, dirs in SECTIONS:
        n = sum(1 for d in docs if d.top in dirs)
        silent = sum(1 for d in docs if d.top in dirs and not out_links[d.name])
        rows.append(["[[%s|%s]]" % (key, title), str(n), str(silent)])

    total = len(docs)
    silent_total = sum(1 for d in docs if not out_links[d.name])
    orphan_total = sum(1 for d in docs if not in_links[d.name])

    body = [
        BANNER, "",
        "# 은하 유산 아카이브", "",
        "전생의 패전 제독이 교도군사학교 생도로 회귀하는 한국형 장편 스페이스 오페라의 "
        "설계 저장소입니다. 이 노트는 입구일 뿐이고, 설정과 플롯은 링크가 가리키는 "
        "문서가 보유합니다.", "",
        "## 분야별 입구", "",
        table(rows, ["분야", "문서", "나가는 링크 없음"], ["---", "---:", "---:"]), "",
        "## 연결 상태", "",
        "`나가는 링크 없음`은 그 문서의 `Depends On` / `Used By`가 아직 산문이라 "
        "그래프에 간선이 없다는 뜻입니다. 링크 패스가 닫아 가는 숫자입니다.", "",
        table([["전체 문서", str(total)],
               ["나가는 링크 없음", str(silent_total)],
               ["들어오는 링크 없음", str(orphan_total)]],
              ["항목", "수"], ["---", "---:"]), "",
        "이 표는 인덱스 노트가 만든 링크를 세지 않습니다. 인덱스는 거의 모든 문서를 "
        "가리키므로 포함하면 수치가 항상 0에 가깝게 나오고, 실제 진행도를 가립니다.", "",
        "## 자주 여는 정본", "",
    ]
    quick = [["[[%s|%s]]" % (n, label), n] for n, label in QUICK_LINKS if n in names]
    body += [table(quick, ["문서", "파일명"]), ""]
    return "\n".join(body).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="write nothing; exit 1 if the index is stale")
    args = ap.parse_args()

    docs = collect()
    seen = Counter(d.name for d in docs)
    duplicated = {n for n, c in seen.items() if c > 1}
    planned = {HOME: build_home(docs)}
    for key, title, blurb, dirs in SECTIONS:
        planned[INDEX_DIR / (key + ".md")] = build_section(
            key, title, blurb, dirs, docs, duplicated)

    stale = []
    for path, text in planned.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != text:
            stale.append(path)

    if args.check:
        for path in stale:
            print("STALE: %s" % path.relative_to(ROOT).as_posix())
        if stale:
            print("\n%d index file(s) out of date. Run: python tools/build_index.py"
                  % len(stale))
            return 1
        print("index is current (%d documents)" % len(docs))
        return 0

    INDEX_DIR.mkdir(exist_ok=True)
    for path, text in planned.items():
        path.write_text(text, encoding="utf-8", newline="\n")
    print("wrote %d index file(s) covering %d documents"
          % (len(planned), len(docs)))
    for path in sorted(planned):
        print("  " + path.relative_to(ROOT).as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
