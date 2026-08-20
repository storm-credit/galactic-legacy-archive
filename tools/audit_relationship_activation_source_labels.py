#!/usr/bin/env python3
"""Audit whether Writer Activation misses explicit relationship/emotion source labels.

No emotion is inferred from prose. This only detects episode-card fields whose
LABEL itself explicitly declares relationship/emotion/character-state content
while the current activation renders RELATIONSHIP_EMOTIONAL_DELTA as NONE.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import build_full_series_context_packs_semantic as semantic
import audit_prewriting_redteam_v2 as red

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "99_quality_control" / "relationship-activation-source-label-audit-v1.md"

RECOGNIZED = {
    "relationship/institution state",
    "relationship state",
    "institution state",
}
STRONG_LABEL = re.compile(
    r"(?:relationship|emotion|emotional|character state|character change|relationship change|relationship delta|institutional relationship)",
    re.I,
)
SECONDARY_LABEL = re.compile(r"(?:trust|loyalty|bond|standing|reputation|consent state)", re.I)


def build() -> str:
    cards = semantic.base.load_sources()
    acts = red.parse_activation()
    strong = []
    secondary = []

    for ep in range(11, 1101):
        act = acts.get(ep, {})
        if not act.get("RELATIONSHIP_EMOTIONAL_DELTA", "").startswith("NONE"):
            continue
        card = cards[ep]
        for key, values in sorted(card.fields.items()):
            if key in RECOGNIZED:
                continue
            value = " / ".join(v for v in values if v).strip()
            if not value:
                continue
            if STRONG_LABEL.search(key):
                strong.append((ep, key, value, card.source.name))
            elif SECONDARY_LABEL.search(key):
                secondary.append((ep, key, value, card.source.name))

    status = "FAIL" if strong else "PASS-WITH-WATCH"
    lines = [
        "# Relationship Activation Source-Label Audit v1",
        "",
        f"Status: {status} — EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        f"- episodes scanned: **{len(cards)}/1090**",
        f"- explicit relationship/emotion/character-state labels missed while activation=NONE: **{len(strong)}**",
        f"- secondary trust/standing label WATCH: **{len(secondary)}**",
        "",
        "## Strong parser-gap queue",
        "",
    ]
    if strong:
        for ep, key, value, source in strong:
            lines.append(f"- E{ep:03d} `{key}` / `{source}` — {value[:520]}")
    else:
        lines.append("- NONE")
    lines += ["", "## Secondary label WATCH", ""]
    if secondary:
        for ep, key, value, source in secondary[:180]:
            lines.append(f"- E{ep:03d} `{key}` / `{source}` — {value[:360]}")
        if len(secondary) > 180:
            lines.append(f"- … {len(secondary)-180} additional secondary-label watches omitted from display")
    else:
        lines.append("- NONE")
    lines += [
        "",
        "## Ruling",
        "",
        "- strong queue entries are parser/source-routing defects only; fix by recognizing the exact approved label, not by inventing emotion.",
        "- secondary WATCH is not enough to create an emotional beat; source review is required.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    text = build()
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            raise SystemExit("relationship activation label audit stale/missing")
    else:
        OUT.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
