#!/usr/bin/env python3
"""Audit whether Writer Activation misses explicit relationship/emotion source labels.

No emotion is inferred from prose. This only detects episode-card fields whose
LABEL itself explicitly declares relationship/emotion/character-state content
while the current activation renders RELATIONSHIP_EMOTIONAL_DELTA as NONE.
Secondary `trust/standing` labels are kept as WATCH unless an exact source review
has established that the field is legal/institutional standing or an option name
rather than an emotional/interpersonal delta.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import build_full_series_context_packs_semantic as semantic
import audit_prewriting_redteam_v2 as red
import relationship_secondary_label_reconciliation as reviewed

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
    reviewed_non_emotional = []

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
                review_reason = reviewed.REVIEWED_NON_EMOTIONAL.get((ep, key))
                if review_reason:
                    reviewed_non_emotional.append((ep, key, value, card.source.name, review_reason))
                else:
                    secondary.append((ep, key, value, card.source.name))

    status = "FAIL" if strong or secondary else "PASS"
    lines = [
        "# Relationship Activation Source-Label Audit v1",
        "",
        f"Status: {status} — EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        f"- episodes scanned: **{len(cards)}/1090**",
        f"- explicit relationship/emotion/character-state labels missed while activation=NONE: **{len(strong)}**",
        f"- unresolved secondary trust/standing label WATCH: **{len(secondary)}**",
        f"- reviewed non-emotional secondary labels: **{len(reviewed_non_emotional)}/6**",
        "",
        "## Strong parser-gap queue",
        "",
    ]
    if strong:
        for ep, key, value, source in strong:
            lines.append(f"- E{ep:03d} `{key}` / `{source}` — {value[:520]}")
    else:
        lines.append("- NONE")
    lines += ["", "## Unresolved secondary label WATCH", ""]
    if secondary:
        for ep, key, value, source in secondary[:180]:
            lines.append(f"- E{ep:03d} `{key}` / `{source}` — {value[:360]}")
        if len(secondary) > 180:
            lines.append(f"- … {len(secondary)-180} additional secondary-label watches omitted from display")
    else:
        lines.append("- NONE")

    lines += ["", "## Source-reviewed non-emotional labels", ""]
    for ep, key, value, source, reason in reviewed_non_emotional:
        lines.append(f"- E{ep:03d} `{key}` / `{source}` — **KEEP OUT OF EMOTION DELTA**: {reason}. Source value: {value[:300]}")

    lines += [
        "",
        "## Ruling",
        "",
        "- strong parser/source-routing gap: **0 required for PASS**.",
        "- unresolved secondary trust/standing ambiguity: **0 required for PASS**.",
        "- legal/service standing and option labels must not be converted into invented feelings.",
        "- story-canon mutation: **0**.",
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
    if "Status: FAIL" in text:
        raise SystemExit("RELATIONSHIP SOURCE-LABEL GATE FAIL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
