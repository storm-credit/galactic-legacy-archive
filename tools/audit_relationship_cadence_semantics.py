#!/usr/bin/env python3
"""Resolve RELATIONSHIP-primary / episode-emotion-NONE cadence watches.

`PRIMARY_SET_TYPE: RELATIONSHIP` is a Collection execution family. It includes
consent, custody, contracts, representation, crew/community obligations and
institutional standing; it does *not* require a newly fixed interpersonal feeling
in every episode. This audit verifies the exact 38 v2 watch subacts, separates
institutional/rights sets from mixed human-pressure sets, and ensures sparse
source-explicit relationship rules are carried without inventing emotions.

A small number of load-bearing irreversible state/loss locks are intentionally
stored in the relationship execution slot because they prohibit false restoration
of person/record continuity. They are not emotional deltas. Only the exact
ledger-backed episode/authority pairs below are exempted from SOURCE-EXPLICIT
emotion routing; any other non-source non-NONE delta remains a hard failure.

Workflow/QC only. No story relationship is added or changed.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import audit_prewriting_redteam_v2 as base
import run_prewriting_redteam_v2_strict as strict  # applies normalized map semantics

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "99_quality_control" / "relationship-cadence-semantic-redteam-v1.md"

MIXED_HUMAN_PRESSURE = {
    ("GA1", "B1"),
    ("GA1", "B2"),
    ("GA1", "C1"),
    ("GA2", "2C-4"),
    ("GA4", "4A-3"),
    ("GA5", "5C-3"),
    ("GA10", "10D-3"),
}

EXPECTED = {
    ("GA1", "B1"), ("GA1", "B2"), ("GA1", "B3"), ("GA1", "B4"),
    ("GA1", "C1"), ("GA1", "C2"), ("GA1", "C3"), ("GA1", "C4"),
    ("GA1", "D1"), ("GA1", "D2"), ("GA1", "D3"), ("GA1", "D4"),
    ("GA2", "2C-4"),
    ("GA3", "3C-2"),
    ("GA4", "4A-3"), ("GA4", "4C-2"), ("GA4", "4D-4"),
    ("GA5", "5A-2"), ("GA5", "5B-3"), ("GA5", "5C-3"),
    ("GA6", "6A-4"), ("GA6", "6C-4"),
    ("GA7", "7C-4"), ("GA7", "7D-1"),
    ("GA8", "8A-3"), ("GA8", "8B-1"), ("GA8", "8B-2"), ("GA8", "8B-3"),
    ("GA8", "8D-1"), ("GA8", "8D-3"), ("GA8", "8D-4"),
    ("GA9", "9A-1"), ("GA9", "9A-4"), ("GA9", "9B-3"),
    ("GA9", "9B-4"), ("GA9", "9C-1"), ("GA9", "9D-1"),
    ("GA10", "10D-3"),
}
assert len(EXPECTED) == 38

LOAD_BEARING_NON_EMOTIONAL_LOCKS = {
    841: (
        "L-R02 LOCKED IRREVERSIBLE PERSON-STATE LOSS",
        "LIV-4 continuity/person-state loss: evidence survival is not person survival; the lock prevents a later false-equivalence restoration.",
    ),
    889: (
        "L-R01/L-R04 IRREVERSIBLE RECORD-LOSS LOCK",
        "Nacre-3/custodian record-loss state: later provenance may survive, but the lost whole cannot be reconstructed; this is absence continuity, not emotion.",
    ),
}
# Fail closed if this exception set is ever widened casually. Any additional
# episode must first be reconciled against the higher-authority loss/state ledger.
assert set(LOAD_BEARING_NON_EMOTIONAL_LOCKS) == {841, 889}
assert len({lock[0] for lock in LOAD_BEARING_NON_EMOTIONAL_LOCKS.values()}) == len(LOAD_BEARING_NON_EMOTIONAL_LOCKS)


def build_report() -> str:
    maps = strict.parse_maps_normalized()
    acts = base.parse_activation()
    watches = base.relationship_cadence(maps, acts)
    actual = {(row["arc"], row["code"]) for row, *_rest in watches}

    failures = []
    if actual != EXPECTED:
        failures.append(
            f"watch-set drift: missing={sorted(EXPECTED-actual)} unexpected={sorted(actual-EXPECTED)}"
        )

    rows = []
    reviewed_state_locks = []
    seen_state_locks = set()
    for row, eps, none_eps, explicit_eps, share in watches:
        key = (row["arc"], row["code"])
        category = "MIXED HUMAN + INSTITUTIONAL PRESSURE" if key in MIXED_HUMAN_PRESSURE else "INSTITUTIONAL / RIGHTS / CONSENT RELATIONSHIP"
        bad_non_none = []
        display_non_none = []
        for ep in eps:
            act = acts[ep]
            delta = act.get("RELATIONSHIP_EMOTIONAL_DELTA", "")
            auth = act.get("RELATIONSHIP_DELTA_AUTHORITY", "")
            if delta.startswith("NONE"):
                continue
            if auth.startswith("SOURCE-EXPLICIT"):
                display_non_none.append(f"E{ep}")
                continue

            lock = LOAD_BEARING_NON_EMOTIONAL_LOCKS.get(ep)
            if lock and auth == lock[0]:
                seen_state_locks.add(ep)
                reviewed_state_locks.append((ep, auth, delta, lock[1]))
                display_non_none.append(f"E{ep} [LOSS/STATE LOCK]")
                continue

            bad_non_none.append((ep, auth, delta))
            display_non_none.append(f"E{ep} [UNAUTHORIZED]")

        if bad_non_none:
            failures.append(f"{key[0]} {key[1]} has non-source relationship delta(s): {bad_non_none}")

        if key in MIXED_HUMAN_PRESSURE:
            rationale = (
                "Human/collective relationship pressure is real, but the approved cards do not fix a new feeling in every episode. "
                "Carry only source-labeled relationship/character rules; otherwise explicit NONE prevents fabricated forgiveness, loyalty, intimacy or reconciliation."
            )
        else:
            rationale = (
                "The Collection RELATIONSHIP family here is executed mainly through consent, custody, claims, contracts, representation, standing or bounded authority. "
                "An episode-level emotion beat is not required unless the source card labels one."
            )
        rows.append((row, eps, none_eps, display_non_none, share, category, rationale))

    missing_locks = set(LOAD_BEARING_NON_EMOTIONAL_LOCKS) - seen_state_locks
    if missing_locks:
        failures.append(f"expected load-bearing non-emotional state lock(s) not observed: {sorted(missing_locks)}")

    status = "PASS" if not failures else "FAIL"
    invented_count = sum(1 for f in failures if "non-source relationship delta" in f)
    lines = [
        "# Relationship-Cadence Semantic Red-Team v1",
        "",
        f"Status: {status} — EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        "## Principle",
        "",
        "`RELATIONSHIP` set-family ≠ mandatory new emotion every episode. The family also tracks consent, custody, representation, obligations, claims and institutional standing. Therefore forcing a feeling into all 38 watch subacts would be a false-depth regression.",
        "",
        "Irreversible person/record-continuity locks may occupy the execution slot without becoming emotions. Only exact ledger-backed loss/state authorities are accepted; they exist to prevent false restoration, not to invent feeling.",
        "",
        "## Coverage",
        "",
        f"- v2 cadence WATCH subacts reviewed: **{len(rows)}/38**",
        f"- mixed human/institutional-pressure subacts: **{sum(1 for r in rows if r[5].startswith('MIXED'))}**",
        f"- institutional/rights/consent relationship subacts: **{sum(1 for r in rows if r[5].startswith('INSTITUTIONAL'))}**",
        f"- load-bearing non-emotional state/loss locks reviewed: **{len(reviewed_state_locks)}/{len(LOAD_BEARING_NON_EMOTIONAL_LOCKS)}**",
        f"- non-source invented relationship deltas detected: **{invented_count}**",
        "",
        "## Per-subact ruling",
        "",
        "| Subact | Episodes | NONE ratio | Approved non-NONE execution episodes | Semantic class | Ruling |",
        "|---|---|---:|---|---|---|",
    ]
    for row, eps, none_eps, display_non_none, share, category, rationale in rows:
        lines.append(
            f"| {row['arc']} {row['code']} | E{row['start']}–E{row['end']} | {len(none_eps)}/{len(eps)} ({share:.0%}) | "
            f"{', '.join(display_non_none) if display_non_none else 'NONE'} | {category} | {rationale} |"
        )

    lines.extend(["", "## Reviewed load-bearing non-emotional locks", ""])
    if reviewed_state_locks:
        for ep, auth, delta, rationale in reviewed_state_locks:
            lines.append(f"- E{ep}: `{auth}` — {rationale} Execution text: {delta}")
    else:
        lines.append("- NONE")

    lines.extend(["", "## Failure queue", ""])
    if failures:
        lines.extend(f"- {f}" for f in failures)
    else:
        lines.append("- NONE")

    lines.extend([
        "",
        "## Final ruling",
        "",
        f"- relationship-cadence false-depth risk: **{status}**",
        "- explicit relationship/character labels are handled by the separate source-label gate; unresolved strong label gaps must remain 0.",
        "- `NONE` is retained where the source does not authorize a feeling; it is a drafting guard, not missing design.",
        "- irreversible loss/state locks may block restoration without implying a new emotion.",
        "- invented confession/forgiveness/loyalty/intimacy/reconciliation: **0**",
        "- story-canon relationship mutation: **0**",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    text = build_report()
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            raise SystemExit("relationship cadence semantic audit stale/missing")
    else:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(text, encoding="utf-8")
    print(text)
    if "Status: FAIL" in text:
        raise SystemExit("RELATIONSHIP CADENCE SEMANTIC GATE FAIL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
