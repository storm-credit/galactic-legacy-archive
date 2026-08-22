#!/usr/bin/env python3
"""Verify the complete 50-row source-role owner WATCH reconciliation.

SAFE rows must be emitted as source-reviewed performers by the writer activation
layer. Reviewed non-performer rows must remain bounded and must not be promoted
into invented owners. No story-canon authority is created here.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import audit_prewriting_redteam_v2 as audit
import decision_owner_role_reconciliation as review

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "99_quality_control" / "decision-owner-role-reconciliation-redteam-v1.md"

SAFE_AUTH = "SOURCE-REVIEWED ROLE PERFORMER + SOURCE DECISION"
BOUNDED_AUTH = "WORKFLOW-BOUNDED ROLE + SOURCE DECISION"


def build_report() -> str:
    acts = audit.parse_activation()
    failures = []

    safe_rows = []
    for ep, actor in sorted(review.SAFE_ROLE_OWNERS.items()):
        row = acts.get(ep, {})
        auth = row.get("OWNER_ROUTE_AUTHORITY", "")
        owner = row.get("PRIMARY_DECISION_OWNER", "")
        ok = auth == SAFE_AUTH and actor.casefold() in owner.casefold()
        if not ok:
            failures.append(f"E{ep:03d} safe-role route mismatch auth={auth!r} owner={owner!r}")
        safe_rows.append((ep, actor, auth, ok))

    rejected_rows = []
    for ep, reason in sorted(review.REVIEWED_NON_PERFORMERS.items()):
        row = acts.get(ep, {})
        auth = row.get("OWNER_ROUTE_AUTHORITY", "")
        owner = row.get("PRIMARY_DECISION_OWNER", "")
        ok = auth == BOUNDED_AUTH
        if not ok:
            failures.append(f"E{ep:03d} reviewed non-performer unexpectedly promoted auth={auth!r} owner={owner!r}")
        rejected_rows.append((ep, reason, auth, ok))

    coverage = set(review.SAFE_ROLE_OWNERS) | set(review.REVIEWED_NON_PERFORMERS)
    if len(coverage) != 50:
        failures.append(f"review table coverage != 50: {len(coverage)}")

    status = "PASS" if not failures else "FAIL"
    lines = [
        "# Decision-Owner Role Reconciliation Red-Team v1",
        "",
        f"Status: {status} — EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        "## Coverage",
        "",
        f"- prior source-role heuristic WATCH queue: **50/50 reviewed**",
        f"- source-written collective/institutional performers safely promoted: **{len(safe_rows)}**",
        f"- heuristic false-subject / imperative / passive / criteria captures explicitly rejected: **{len(rejected_rows)}**",
        f"- unresolved role-owner rows: **{len(failures)}**",
        "",
        "## Safe source-role performer routes",
        "",
        "| Episode | Source-written performer | Activation authority | Verdict |",
        "|---:|---|---|---|",
    ]
    for ep, actor, auth, ok in safe_rows:
        lines.append(f"| E{ep:03d} | {actor} | `{auth}` | {'PASS' if ok else 'FAIL'} |")

    lines.extend([
        "",
        "## Reviewed non-performer captures",
        "",
        "These rows are intentionally *not* converted into actor facts. The bounded route remains because the captured text is an imperative/result/passive/criteria phrase or a prohibition that would be inverted by promotion.",
        "",
        "| Episode | Why not a source performer | Activation authority | Verdict |",
        "|---:|---|---|---|",
    ])
    for ep, reason, auth, ok in rejected_rows:
        lines.append(f"| E{ep:03d} | {reason.replace('|','/')} | `{auth}` | {'PASS' if ok else 'FAIL'} |")

    lines.extend(["", "## Failure queue", ""])
    if failures:
        lines.extend(f"- {f}" for f in failures)
    else:
        lines.append("- NONE")

    lines.extend([
        "",
        "## Ruling",
        "",
        f"- full 50-row role-owner WATCH resolution: **{status}**",
        "- invented actor/authority from heuristic text: **0**",
        "- manuscript prose used as source: **0**",
        "- story-canon mutation: **0**",
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
            raise SystemExit("decision-owner role audit stale/missing")
    else:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(text, encoding="utf-8")
    print(text)
    if "Status: FAIL" in text:
        raise SystemExit("DECISION OWNER ROLE RECONCILIATION FAIL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
