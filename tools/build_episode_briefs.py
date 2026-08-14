#!/usr/bin/env python3
"""Generate the per-episode work order: docs/_index/episode-briefs.md.

Why this exists
---------------
Writing episode 6 meant opening the act map, the payoff ledger, the beat map
and the scene cards separately, and the first time round I opened only two of
them and missed what the act map asked for. The structure was there; it just
was not handed to the writer at the moment of writing.

So this assembles it. For every episode the act map knows about:

    which sub-act it belongs to and what that sub-act is called;
    what the act map says this episode does;
    which mysteries have an open plant window on it;
    the scene cards and beat map that cover it;
    the manuscript, its version and its length against the floor.

It is a routing table, not canon. Every line is a link back to the document
that owns the fact (CLAUDE.md section 3), which is also why it repairs the
graph: the act map, the ledgers and the cards stop being islands.

    python tools/build_episode_briefs.py            write the briefs
    python tools/build_episode_briefs.py --check    fail if out of date
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = DOCS / "_index" / "episode-briefs.md"

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

BANNER = (
    "> [!warning] 자동 생성 문서\n"
    "> `python tools/build_episode_briefs.py`가 이 파일을 덮어씁니다.\n"
    "> 여기에 설정을 쓰지 마십시오. 모든 항목은 원문 문서를 가리키는 링크입니다.\n"
)

LENGTH_FLOOR = 5500

ACT_MAP = DOCS / "10_story_architecture/first-100-act-map-v2-consolidated.md"
BEAT_MAP = DOCS / "10_story_architecture/ga1-episodes-1-20-beat-map-v1.md"
PAYOFF = DOCS / "11_mystery/series-payoff-ledger-v1.md"

SUBACT = re.compile(r"^## (A\d+) — (.+?) / Episodes (\d+)[–-](\d+)\s*$")
EPISODE = re.compile(r"^E(\d+):\s*$")
MYSTERY = re.compile(r"^## (M-\d+) — (.+?)\s*$")
PLANT = re.compile(r"^### Plant — Episodes? (\d+)(?:[–-](\d+))?")
CARD_FILE = re.compile(r"^ga1-episodes-(\d+)-(\d+)-.*scene-cards.*$")


def act_map_entries() -> dict[int, tuple[str, str, str, list[str]]]:
    """episode -> (act id, sub-act title, episode range, act-map bullets)."""
    out: dict[int, tuple[str, str, str, list[str]]] = {}
    if not ACT_MAP.exists():
        return out
    lines = ACT_MAP.read_text(encoding="utf-8").split("\n")
    aid = title = rng = ""
    for i, line in enumerate(lines):
        head = SUBACT.match(line)
        if head:
            aid, title, lo, hi = head.groups()
            rng = f"{lo}–{hi}"
            continue
        ep = EPISODE.match(line.strip())
        if not ep:
            continue
        body: list[str] = []
        for nxt in lines[i + 1:]:
            if nxt.startswith("- "):
                body.append(nxt[2:].strip())
            elif body or nxt.strip():
                break
        out[int(ep.group(1))] = (aid, title, rng, body)
    return out


def plant_windows() -> list[tuple[str, str, int, int]]:
    """(id, title, first episode, last episode) for every plant window."""
    out: list[tuple[str, str, int, int]] = []
    if not PAYOFF.exists():
        return out
    mid = mtitle = ""
    for line in PAYOFF.read_text(encoding="utf-8").split("\n"):
        head = MYSTERY.match(line)
        if head:
            mid, mtitle = head.groups()
            continue
        window = PLANT.match(line)
        if window and mid:
            lo = int(window.group(1))
            hi = int(window.group(2)) if window.group(2) else lo
            out.append((mid, mtitle, lo, hi))
    return out


def scene_cards() -> list[tuple[int, int, str]]:
    out = []
    for p in (DOCS / "10_story_architecture").glob("*scene-cards*.md"):
        m = CARD_FILE.match(p.stem)
        if m:
            out.append((int(m.group(1)), int(m.group(2)), p.stem))
    return sorted(out)


def manuscripts() -> dict[int, tuple[int, str, int]]:
    """episode -> (version, stem, prose length)."""
    out: dict[int, tuple[int, str, int]] = {}
    for p in sorted((ROOT / "manuscript").rglob("*.md")):
        m = re.match(r"^(\d{3})-(.*)-v(\d)$", p.stem)
        if not m:
            continue
        num, ver = int(m.group(1)), int(m.group(3))
        lines = p.read_text(encoding="utf-8").split("\n")
        start = 0
        for i, line in enumerate(lines[:25]):
            if re.match(r"^[A-Za-z][A-Za-z ]*:", line):
                start = i + 1
        length = len("\n".join(lines[start:]))
        if num not in out or ver > out[num][0]:
            out[num] = (ver, p.stem, length)
    return out


DOMAIN = {
    "hulls": ("함선", "named-hull-registry-and-naming-grammar-v1"),
    "weapons": ("무기·부품", "named-weapon-and-part-registry-v1"),
    "technologies": ("기술", "named-technology-lineage-registry-v1"),
    "relics": ("유물", "named-relic-and-provenance-registry-v1"),
    "factions": ("세력·기관", "named-faction-and-institution-registry-v1"),
    "places": ("장소·항로", "named-place-and-corridor-registry-v1"),
}


def arc_items(arc: str) -> list[tuple[str, str, str, str, str]]:
    """(domain, registry, id, name, plot use) for items first revealed in `arc`.

    The anchor CSVs are written because C9 refuses to pass without them, so
    this costs the writer nothing extra: register an item and it appears here.
    Granularity is the arc, not the episode -- `first_reveal` records `GA2`,
    never `E37`. Saying so is better than inventing an episode number.
    """
    out = []
    for path in sorted(ROOT.rglob("anchor-fields-*.csv")):
        key = re.sub(r"^anchor-fields-|-v\d+$", "", path.stem)
        label, registry = DOMAIN.get(key, (key, ""))
        for row in csv.DictReader(path.read_text(encoding="utf-8").splitlines()):
            if row.get("first_reveal", "").strip() == arc:
                out.append((label, registry, row["item_id"], row["name"],
                            row.get("plot_use", "").strip()))
    return sorted(out)


def render() -> str:
    acts = act_map_entries()
    windows = plant_windows()
    cards = scene_cards()
    scripts = manuscripts()

    done = sum(1 for v in scripts.values() if v[2] >= LENGTH_FLOOR)
    out = [
        "# 회차 작업지시서 — GA1",
        "",
        BANNER,
        "회차 하나를 쓰기 전에 열어야 하는 것을 한자리에 모은다. 액트맵·회수 장부·"
        "장면 카드·비트맵을 따로 여는 대신, 이 표가 그 순서대로 건네준다.",
        "",
        f"액트맵이 아는 회차 **{len(acts)}편** · 원고 존재 **{len(scripts)}편** · "
        f"하한({LENGTH_FLOOR:,}자) 충족 **{done}편**",
        "",
        f"정본: [[{ACT_MAP.stem}]] · [[{PAYOFF.stem}]] · [[{BEAT_MAP.stem}]]",
        "",
    ]

    items = arc_items("GA1")
    if items:
        out += [
            "---",
            "",
            f"## GA1에서 처음 등장하는 등록 항목 — {len(items)}건",
            "",
            "`first_reveal`이 기록하는 단위는 **대액트**이지 회차가 아니다. 어느 회차에 "
            "나오는지는 등록부가 모른다 — 그건 이 구간을 쓰면서 정해진다. 그래서 여기 "
            "모아 두고, 회차마다 반복하지 않는다.",
            "",
            "독자 기억 예산은 회차당 최초 사용 고유명 **0–4개**다 "
            "([[reader-facing-terminology-phonetics-and-register-bible-v1]] §2). "
            f"이 {len(items)}건을 100화에 배분하면 회차당 약 "
            f"{len(items) / 100:.1f}개이므로 예산 안에 들어간다.",
            "",
            "| 종류 | ID | 이름 | 무엇을 위해 있는가 |",
            "|---|---|---|---|",
        ]
        for label, registry, iid, name, use in items:
            link = f"[[{registry}]]" if registry else ""
            out.append(f"| {label} {link} | `{iid}` | **{name}** | {use} |")
        out.append("")

    current_act = None
    for num in sorted(acts):
        aid, title, rng, bullets = acts[num]
        if aid != current_act:
            current_act = aid
            out += ["---", "", f"## {aid} — 「{title}」 / {rng}화", ""]

        out.append(f"### E{num}")
        out.append("")
        if bullets:
            out.append("**액트맵이 요구하는 것**")
            out += [f"- {b}" for b in bullets]
            out.append("")

        open_now = [(i, t) for i, t, lo, hi in windows if lo <= num <= hi]
        if open_now:
            out.append("**심기 구간이 열린 미스터리**")
            out += [f"- `{i}` {t}" for i, t in open_now]
            out.append("")

        refs = []
        for lo, hi, stem in cards:
            if lo <= num <= hi:
                refs.append(f"장면 카드 [[{stem}]]")
        if num <= 20 and BEAT_MAP.exists():
            refs.append(f"비트 [[{BEAT_MAP.stem}]]")
        if refs:
            out.append("**설계 문서** — " + " · ".join(refs))
            out.append("")

        script = scripts.get(num)
        if script:
            ver, stem, length = script
            gap = LENGTH_FLOOR - length
            state = "하한 충족" if gap <= 0 else f"**{gap:,}자 부족**"
            out.append(f"**원고** — [[{stem}]] · v{ver} · {length:,}자 · {state}")
        else:
            out.append("**원고** — 없음")
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
                  f"Run: python tools/build_episode_briefs.py")
            return 1
        OUT.write_text(text, encoding="utf-8")
    print(f"  {OUT.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
