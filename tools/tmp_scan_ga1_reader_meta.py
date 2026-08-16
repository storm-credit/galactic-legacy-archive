from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT_DIR = ROOT / "manuscript" / "ga1"
EP_RE = re.compile(r"^(\d{3})-")
META_RE = re.compile(r"(?<![A-Za-z0-9_])E\d{1,3}(?![A-Za-z0-9_])")

hits: list[tuple[str, int, str, str]] = []

for path in sorted(MANUSCRIPT_DIR.glob("*-v1.md")):
    match = EP_RE.match(path.name)
    if not match:
        continue
    episode = int(match.group(1))
    if not 21 <= episode <= 100:
        continue

    lines = path.read_text(encoding="utf-8").splitlines()
    body_started = False
    for lineno, line in enumerate(lines, 1):
        if line.startswith("# 제"):
            body_started = True
        if not body_started:
            continue

        kinds: list[str] = []
        if META_RE.search(line):
            kinds.append("EPISODE_META")
        if "Yori" in line:
            kinds.append("YORI")
        if "문제어" in line:
            kinds.append("TYPO")
        if "CLOSED" in line and "살아 있었다" in line:
            kinds.append("CLOSED_SURVIVAL")
        if kinds:
            hits.append((str(path.relative_to(ROOT)), lineno, ",".join(kinds), line))

print(f"READER_META_HITS={len(hits)}")
for path, lineno, kinds, line in hits:
    print(f"{kinds}\t{path}:{lineno}\t{line}")
