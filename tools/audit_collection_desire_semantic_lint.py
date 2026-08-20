#!/usr/bin/env python3
"""Semantic lint for generated Collection Desire packets.

Existing audits prove field presence, target bounds and adjacent duplication.
This lint catches writer-unusable internal registry shorthand that can still
satisfy those checks, for example backticked `C/G/L — ...` status facets in
NEXT_DESIRE. Source-native operational labels such as Window A/B/C are valid.
Concise but readable source phrases are WATCH, not automatic failures.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_DIR = ROOT / "docs" / "09_collection" / "generated" / "desire_subact"
OUT = ROOT / "docs" / "99_quality_control" / "full-series-collection-desire-semantic-lint-v1.md"

HEADER_RE = re.compile(r"^##\s+([^\s]+)\s+—\s+(.+?)\s+/\s+E(\d+)[–—-]E?(\d+)\s*$")
FIELD_RE = re.compile(r"^- `([^`]+)`: ?(.*)$")
REQUIRED = (
    "READER_DESIRE_MAIN",
    "DISCOVERY",
    "ACQUISITION_OR_CONNECTION",
    "SYNERGY_OR_USE",
    "COST_REFUSAL_OR_LOSS",
    "SET_ADVANCE_CONDITION",
    "NEXT_DESIRE",
)
STATUS_CODE = re.compile(r"`[A-Z](?:/[A-Z]){1,5}(?:\s+—[^`]*)?`")
PLACEHOLDER = re.compile(r"\b(?:TBD|TODO|PLACEHOLDER)\b", re.IGNORECASE)


def parse_maps():
    rows = []
    for path in sorted(MAP_DIR.glob("ga*-collection-desire-subact-map-v1.md")):
        arc = path.name.split("-", 1)[0].upper()
        current = None
        for line in path.read_text(encoding="utf-8").splitlines():
            h = HEADER_RE.match(line)
            if h:
                if current:
                    rows.append(current)
                current = {"arc": arc, "code": h.group(1), "title": h.group(2), "fields": {}}
                continue
            if current is None:
                continue
            f = FIELD_RE.match(line)
            if f:
                current["fields"][f.group(1)] = f.group(2).strip()
        if current:
            rows.append(current)
    return rows


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z가-힣][A-Za-z가-힣0-9'-]*", text)


def build() -> str:
    rows = parse_maps()
    findings = []
    watches = []
    for row in rows:
        for field in REQUIRED:
            value = row["fields"].get(field, "").strip()
            reasons = []
            if not value:
                reasons.append("missing")
            if value and STATUS_CODE.search(value):
                reasons.append("backticked-registry-status-token")
            if value and PLACEHOLDER.search(value):
                reasons.append("placeholder-token")
            if reasons:
                findings.append((row["arc"], row["code"], field, value, ", ".join(reasons)))
            elif value and len(value) <= 32 and len(words(value)) < 4:
                watches.append((row["arc"], row["code"], field, value))

    fail = len(rows) != 160 or bool(findings)
    verdict = "FAIL" if fail else "PASS"
    lines = [
        "# Full-Series Collection Desire Semantic Lint v1",
        "",
        f"Status: {verdict} — EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        f"- subacts scanned: **{len(rows)} / 160**",
        f"- writer-unusable semantic fields: **{len(findings)}**",
        f"- concise readable fields WATCH: **{len(watches)}**",
        "",
        "## Finding queue",
        "",
    ]
    if findings:
        for arc, code, field, value, reason in findings:
            lines.append(f"- `{arc} {code}` `{field}` — `{value}` — {reason}")
    else:
        lines.append("- NONE")
    lines.extend(["", "## Concise-field WATCH", ""])
    if watches:
        for arc, code, field, value in watches:
            lines.append(f"- `{arc} {code}` `{field}` — `{value}`")
    else:
        lines.append("- NONE")
    lines.extend([
        "",
        "## Gate",
        "",
        "A field can be structurally present and still be unusable for prose planning. Backticked registry status/category abbreviations are hard failures. Source-native labels such as Window A/B/C are preserved. A short but ordinary-language approved-source phrase is a WATCH only when its meaning remains clear in the owning subact.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text = build()
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            raise SystemExit("collection semantic lint stale/missing")
    else:
        OUT.write_text(text, encoding="utf-8")
    print(text)
    if "Status: PASS — EXECUTION QC" not in text:
        raise SystemExit("COLLECTION DESIRE SEMANTIC LINT FAIL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
