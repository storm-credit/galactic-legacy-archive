#!/usr/bin/env python3
"""Semantic source-block completion for full-series Context Packs.

This is the final *non-generative* normalization layer. It exists because some
approved detailed cards use close-state / action / result labels rather than the
new Context-Pack labels. The layer may only copy or re-route text already in the
owning episode card. It does not consult manuscript prose and does not invent
story facts.

The pass is intentionally conservative:
- explicit Context fields from earlier builders win;
- unresolved fields may be filled only from source label blocks or concrete
  lines in the same approved episode card;
- physical anchor means a tangible object/place/person-state OR a concrete
  work-system carrier (claim file, panel, route key, service ledger, etc.);
- any remaining mandatory unresolved field hard-fails the build.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict

import build_full_series_context_packs_complete as complete

base = complete.base
ROOT = complete.ROOT
_ORIGINAL_ENRICH = complete.enrich

LABEL_RE = re.compile(r"^([A-Za-z][A-Za-z0-9 /&()'’_.\-]{0,90}):\s*(.*)$")

# Work-system carriers count as tangible execution anchors when the episode is
# about law/records/institutions rather than a vehicle or room. These tokens do
# not create facts; they only decide which already-written source line to route.
CARRIER_TOKENS = (
    "ship", "hull", "craft", "convoy", "escort", "fleet", "tender", "frame",
    "route", "corridor", "relay", "node", "berth", "dock", "yard", "station",
    "cargo", "parts", "ammunition", "oxygen", "power", "thermal", "medical",
    "hospital", "patient", "crew", "worker", "people", "household", "shelter",
    "habitat", "record", "ledger", "register", "claim", "file", "evidence",
    "document", "archive", "panel", "hearing", "office", "key", "credential",
    "queue", "council", "assembly", "trust", "compact", "charter", "fund",
    "restriction", "sanction", "service", "operator", "captain", "formation",
    "mirror", "interface", "module", "engine", "propulsion", "clinic",
)

MAIN_LABELS = (
    "goal", "visible goal", "mission goal", "final disposition", "campaign result",
    "named locked loss", "final personal finding", "final convoy result",
    "immediate regional effects", "final event", "final ga6 state", "final ga state",
    "current obligations", "crisis", "decision packet includes", "placement",
)

ANCHOR_LABELS = (
    "current physical problem", "physical cause", "physical result", "action split",
    "action", "operation", "outcome", "current result", "current facts", "state",
    "final disposition", "final convoy result", "final mission arithmetic",
    "campaign result", "immediate regional effects", "current obligations",
    "affected zone", "crisis", "response owners", "placement", "separate authority fields",
    "decision packet includes", "final sanctions", "separate institutional/civil findings",
    "authorized immediately", "final event", "current packet candidate", "candidate",
)

COST_LABELS = (
    "cost", "foreseeable cost", "risk", "still contested", "final ga6 state",
    "final ga state", "final event", "outcome", "current result", "campaign result",
    "immediate regional effects", "final sanctions", "separate institutional/civil findings",
    "physical result", "current physical problem", "crisis",
)

COST_TOKENS = (
    "dead", "death", "injur", "lost", "loss", "damage", "delay", "deplet",
    "remain", "partial", "unstable", "missing", "captur", "risk", "scarcity",
    "underfund", "fragment", "slower", "restriction", "ban", "reparation",
    "contested", "unresolved", "refus", "exposed", "debt", "burden", "expire",
)


def _clean(text: str) -> str:
    return base.shorten(base.clean_lines(text), 1000)


def label_blocks(card):
    """Parse label blocks from the episode body without depending on card schema."""
    rows = card.raw.splitlines()
    blocks = []
    current_label = None
    current = []

    def flush():
        nonlocal current_label, current
        if current_label is not None:
            body = _clean("\n".join(current))
            if body:
                blocks.append((current_label, body))
        current_label = None
        current = []

    for raw in rows:
        stripped = raw.strip()
        if stripped.startswith("#"):
            flush()
            continue
        m = LABEL_RE.match(stripped)
        if m:
            flush()
            current_label = m.group(1).strip()
            if m.group(2).strip():
                current.append(m.group(2).strip())
        elif current_label is not None:
            current.append(raw)
    flush()
    return blocks


def _block_by_label(card, preferred):
    blocks = label_blocks(card)
    for wanted in preferred:
        wl = wanted.lower()
        for label, body in blocks:
            ll = label.lower()
            if ll == wl or wl in ll:
                return f"[{label}] {body}"
    return None


def _concrete_block(card):
    blocks = label_blocks(card)
    # Prefer execution-shaped blocks that visibly carry the work into a scene.
    for wanted in ANCHOR_LABELS:
        wl = wanted.lower()
        for label, body in blocks:
            ll = label.lower()
            if (ll == wl or wl in ll) and any(tok in body.lower() for tok in CARRIER_TOKENS):
                return f"[{label}] {body}"
    # Then any labeled source block containing a concrete/work-system carrier.
    for label, body in blocks:
        if any(tok in body.lower() for tok in CARRIER_TOKENS):
            return f"[{label}] {body}"
    # Last source-bound fallback: a literal line carrying a concrete token.
    lines = []
    for raw in card.raw.splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        if any(tok in s.lower() for tok in CARRIER_TOKENS):
            lines.append(s)
        if len(lines) >= 5:
            break
    if lines:
        return "[SOURCE LINES] " + _clean("\n".join(lines))
    return None


def _cost_block(card):
    blocks = label_blocks(card)
    for wanted in COST_LABELS:
        wl = wanted.lower()
        for label, body in blocks:
            ll = label.lower()
            if ll == wl or wl in ll:
                if any(tok in body.lower() for tok in COST_TOKENS) or "cost" in ll or "risk" in ll:
                    return f"[{label}] {body}"
    for label, body in blocks:
        if any(tok in body.lower() for tok in COST_TOKENS):
            return f"[{label}] {body}"
    lines = []
    for raw in card.raw.splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        if any(tok in s.lower() for tok in COST_TOKENS):
            lines.append(s)
        if len(lines) >= 4:
            break
    if lines:
        return "[SOURCE COST/BURDEN LINES] " + _clean("\n".join(lines))
    return None


def semantic_enrich(card):
    n = _ORIGINAL_ENRICH(card)
    derived = list(n.get("derived", []))

    if n["main"].startswith("UNRESOLVED"):
        block = _block_by_label(card, MAIN_LABELS)
        if not block:
            block = _concrete_block(card)
        if block:
            n["main"] = "[SEMANTIC SOURCE-BLOCK EPISODE FUNCTION; no new fact] " + block
            derived.append("ACTIVE_DESIRE_MAIN_SEMANTIC")

    if not n["anchor"]:
        block = _concrete_block(card)
        if block:
            n["anchor"] = ["[SEMANTIC SOURCE-BLOCK CARRIER; exact approved episode evidence] " + block]
            derived.append("PHYSICAL_ANCHOR_SEMANTIC")

    if not n["costs"]:
        block = _cost_block(card)
        if block:
            n["costs"] = ["[SEMANTIC SOURCE-BLOCK COST/BURDEN; do not inflate beyond source] " + block]
            derived.append("COST_OR_REFUSAL_SEMANTIC")

    n["derived"] = derived
    return n


# Rebind the complete renderer/audit to the semantic pass. complete.render_episode
# and complete.structural_audit resolve `enrich` from the module namespace at
# runtime, so rebinding here updates both without duplicating renderer code.
complete.enrich = semantic_enrich
base.render_episode = complete.render_episode
base.structural_audit = complete.structural_audit


def readiness(cards):
    failed = defaultdict(list)
    for ep, card in sorted(cards.items()):
        n = semantic_enrich(card)
        checks = {
            "ACTIVE_DESIRE_MAIN": n["main"].startswith("UNRESOLVED"),
            "PHYSICAL_ANCHOR": not n["anchor"],
            "STATE_CHANGE": not n["changes"],
            "COST_OR_REFUSAL": not n["costs"],
            "REENTRY_ANCHOR": not n["reentry"],
        }
        for field, bad in checks.items():
            if bad:
                failed[field].append(ep)
    return failed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    try:
        outputs = base.build_outputs()
        cards = base.collect_cards()
        failed = readiness(cards)
    except Exception as exc:
        print(f"SEMANTIC CONTEXT BUILD ERROR: {exc}", file=sys.stderr)
        return 1

    if failed:
        print("SEMANTIC CONTEXT GATE FAIL: mandatory fields remain unresolved", file=sys.stderr)
        for field, episodes in failed.items():
            print(f"  {field}: " + ", ".join(f"E{x}" for x in episodes), file=sys.stderr)
        return 1

    changed = []
    for path, text in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != text:
            changed.append(path)
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")

    if args.check and changed:
        print("Semantic Context outputs are stale/missing:")
        for path in changed:
            print(f"  {path.relative_to(ROOT).as_posix()}")
        return 1

    print("Semantic full-series Context gate PASS: mandatory unresolved = 0")
    for path in outputs:
        print(f"  {path.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
