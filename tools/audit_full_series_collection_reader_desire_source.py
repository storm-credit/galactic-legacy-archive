#!/usr/bin/env python3
"""Audit whether subact reader desire came from the subact or target-list fallback.

Final reader-desire normalization must not use a list of active registry target
titles as a substitute for the subact's actual reader desire. This audit scans
all generated GA maps and reports any exact target-title fallback.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_DIR = ROOT / "docs" / "09_collection" / "generated" / "desire_subact"
AUDIT = ROOT / "docs" / "99_quality_control" / "full-series-collection-reader-desire-source-audit-v1.md"

MAPS = [MAP_DIR / f"ga{i}-collection-desire-subact-map-v1.md" for i in range(1, 11)]
SUBACT_RE = re.compile(r"^##\s+(.+?)\s+/\s+E(\d+)[–-]E?(\d+)\s*$")
TARGET_RE = re.compile(r"^\s+- `CLT-[^`]+` / `[^`]+` / (.+?) — `[^`]+` score=\d+\s*$")


def parse_map(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        match = SUBACT_RE.match(line)
        if match:
            if current:
                rows.append(current)
            current = {
                "heading": match.group(1),
                "start": int(match.group(2)),
                "end": int(match.group(3)),
                "reader": "",
                "discovery": "",
                "targets": [],
            }
            continue
        if current is None:
            continue
        if line.startswith("- `READER_DESIRE_MAIN`: "):
            current["reader"] = line.split(": ", 1)[1]
        elif line.startswith("- `DISCOVERY`: "):
            current["discovery"] = line.split(": ", 1)[1]
        else:
            target = TARGET_RE.match(line)
            if target:
                current["targets"].append(target.group(1))
    if current:
        rows.append(current)
    return rows


def build_audit() -> str:
    all_rows: list[dict[str, object]] = []
    for path in MAPS:
        if not path.exists():
            raise SystemExit(f"missing map: {path.relative_to(ROOT)}")
        arc = path.name.split("-", 1)[0].upper()
        for row in parse_map(path):
            row["arc"] = arc
            all_rows.append(row)

    fallback: list[dict[str, object]] = []
    malformed: list[str] = []
    for row in all_rows:
        reader = str(row["reader"]).strip()
        discovery = str(row["discovery"]).strip()
        targets = list(row["targets"])
        if not reader or not discovery or not targets:
            malformed.append(f"{row['arc']} {row['heading']}")
            continue
        target_discovery = " / ".join(targets[:3])
        if discovery == target_discovery or reader.startswith(target_discovery + " →"):
            fallback.append(row)

    verdict = "PASS" if not fallback and not malformed and len(all_rows) == 160 else "HOLD"
    lines = [
        "# Full-Series Collection Reader-Desire Source Audit v1",
        "",
        f"Status: {verdict} — EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        f"> **{verdict} — reader desire must come from approved subact intent, not active-target title fallback.**",
        "",
        "## Coverage",
        "",
        f"- subacts scanned: **{len(all_rows)} / 160**",
        f"- exact target-title fallback subacts: **{len(fallback)}**",
        f"- malformed/missing desire packets: **{len(malformed)}**",
        "",
        "## Target-List Fallback Queue",
        "",
    ]
    if fallback:
        for row in fallback:
            lines.append(
                f"- `{row['arc']} {row['heading']}` E{row['start']}–E{row['end']} — discovery equals first active-target titles"
            )
    else:
        lines.append("- NONE")
    lines.extend(["", "## Malformed Queue", ""])
    if malformed:
        lines.extend(f"- {item}" for item in malformed)
    else:
        lines.append("- NONE")
    lines.extend(
        [
            "",
            "## Gate",
            "",
            "- final normalization requires target-list fallback = **0**",
            "- registry targets remain evidence/carriers; they do not replace the reader-facing desire sentence",
            "- new story canon required: **0**",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text = build_audit()
    if args.check:
        if not AUDIT.exists() or AUDIT.read_text(encoding="utf-8") != text:
            raise SystemExit("reader-desire source audit stale/missing")
    else:
        AUDIT.write_text(text, encoding="utf-8")
    print(text)
    if "Status: PASS — EXECUTION QC" not in text:
        raise SystemExit("READER-DESIRE SOURCE GATE HOLD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
