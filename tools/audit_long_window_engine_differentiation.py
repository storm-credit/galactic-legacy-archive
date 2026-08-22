#!/usr/bin/env python3
"""Adversarial audit for the six long-window dominant-engine WATCH ranges.

A long arc may legitimately keep one engine family (medical, combat, route,
accountability, record, custody). The failure mode is not concentration itself;
it is repeated scene logic: same decision, same cost, same payoff, same next
question. This audit therefore checks source-bound activation content inside the
six v2 windows instead of relabeling engines merely to improve a percentage.

Workflow/QC only. It does not change story events or engine labels.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

import audit_prewriting_redteam_v2 as base
import run_prewriting_redteam_v2_strict as strict  # normalized map semantics

ROOT = Path(__file__).resolve().parents[1]
ACT_DIR = ROOT / "docs" / "13_writing_harness" / "context_packs" / "activation"
OUT = ROOT / "docs" / "99_quality_control" / "long-window-narrative-engine-differentiation-redteam-v1.md"

RANGES = [
    (43, 81, "MEDICAL/CARE/CONSENT", "GA1 Black Ward/current-person arc: access → treatment/privacy → deletion/identity correction → transfer/supply/triage. Care remains the domain, but the human choice and material cost change."),
    (532, 559, "TACTICAL-COMBAT", "GA5 Outer Front/common-fleet campaign: negotiation/charter handoff → multi-front allocation → isolated/autonomous formation decisions → civilian/route consequences. Combat is the arena, not one repeated battle solution."),
    (684, 713, "ROUTE/LOGISTICS", "GA6→GA7 hinge: Orpheus convergence/evacuation lanes transition into post-crisis route access and Blood-Admiral-era traffic obligations. The repeated route engine carries different owners and obligations across the grand-act boundary."),
    (766, 797, "LEGAL/GOVERNANCE/ACCOUNTABILITY", "GA7 accountability arc: representative incident selection → plural responsibility/evidence → affected-party standing → bounded authority/reparation consequences. Governance concentration is intentional; verdict ownership and proof burdens move."),
    (822, 892, "RECORD/PROVENANCE/MYSTERY", "GA8 record war: inhabited archives/custodians → AI/witness/composite consent → mirror/source failure → plural rights/compression rules → bounded activation. Record work stays dominant while what counts as person, evidence, tool and authority changes."),
    (1006, 1025, "CLAIM/OWNERSHIP/CUSTODY", "GA10 transition opening: residual central dependencies and asset/rights handoffs are decomposed into current custody, service, route, technical/medical and regional obligations. Custody remains the engine while the receiving authority and cost vary."),
]

EP_HEADER = re.compile(r"^## E(\d{3,4})\b")
BLOCK_MARKERS = {
    "SCENE_CAUSAL_CHAIN": "**SCENE_CAUSAL_CHAIN**",
    "HUMAN_PRESSURE_CARRIER": "**HUMAN_PRESSURE_CARRIER**",
    "ENGINE_DIFFERENTIATOR": "**ENGINE_DIFFERENTIATOR**",
}
INLINE = {
    "HUMAN_ROUTE_AUTHORITY": re.compile(r"^\*\*HUMAN_ROUTE_AUTHORITY:\*\*\s+`(.+?)`\s*$"),
}
STOP = {"the","and","with","that","this","from","into","under","current","source","approved","episode","without","through","rather","than","must","will","only","while","their","they","them","then","next"}


def tokens(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z가-힣][a-z가-힣0-9'-]{2,}", (text or "").casefold()) if t not in STOP}


def jaccard(a: str, b: str) -> float:
    aa, bb = tokens(a), tokens(b)
    if not aa and not bb:
        return 1.0
    if not aa or not bb:
        return 0.0
    return len(aa & bb) / len(aa | bb)


def extra_activation() -> dict[int, dict[str, str]]:
    out: dict[int, dict[str, str]] = {}
    for path in sorted(ACT_DIR.glob("ga*-writer-activation-v1.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        ep = None
        i = 0
        while i < len(lines):
            h = EP_HEADER.match(lines[i])
            if h:
                ep = int(h.group(1))
                out.setdefault(ep, {})
                i += 1
                continue
            if ep is None:
                i += 1
                continue
            s = lines[i].strip()
            for key, pat in INLINE.items():
                m = pat.match(s)
                if m:
                    out[ep][key] = m.group(1)
            for key, marker in BLOCK_MARKERS.items():
                if s == marker:
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines):
                        out[ep][key] = lines[j].strip()
            i += 1
    return out


def subact_by_episode():
    mapping = {}
    for row in strict.parse_maps_normalized():
        for ep in range(row["start"], row["end"] + 1):
            mapping[ep] = f"{row['arc']} {row['code']}"
    return mapping


def cost_class(extra: dict[str, str]) -> str:
    diff = extra.get("ENGINE_DIFFERENTIATOR", "")
    m = re.search(r"cost-class=([^;]+)", diff)
    if m:
        return m.group(1).strip()
    causal = extra.get("SCENE_CAUSAL_CHAIN", "")
    m = re.search(r"COST\[([^\]]+)\]", causal)
    return (m.group(1).strip()[:90] if m else "UNPARSED")


def build_report() -> str:
    acts = base.parse_activation()
    extra = extra_activation()
    subacts = subact_by_episode()
    failures = []
    results = []

    for lo, hi, family, rationale in RANGES:
        eps = [ep for ep in range(lo, hi + 1) if acts.get(ep, {}).get("NARRATIVE_ENGINE_FAMILY") == family]
        if not eps:
            failures.append(f"E{lo:03d}–E{hi:03d}: no episodes found for expected family {family}")
            continue

        decision_texts = [acts[ep].get("DECISION_BEAT", "") for ep in eps]
        payoff_texts = [acts[ep].get("READER_PAYOFF_THIS_EP", "") for ep in eps]
        hook_texts = [acts[ep].get("RETENTION_QUESTION_OR_CHANGED_CONDITION", "") for ep in eps]
        combined = [" ".join((decision_texts[i], payoff_texts[i], hook_texts[i])) for i in range(len(eps))]
        adjacent = [jaccard(combined[i-1], combined[i]) for i in range(1, len(combined))]
        avg_j = sum(adjacent) / len(adjacent) if adjacent else 0.0
        max_j = max(adjacent) if adjacent else 0.0

        exact_decision_dupes = len(decision_texts) - len(set(decision_texts))
        exact_payoff_dupes = len(payoff_texts) - len(set(payoff_texts))
        exact_hook_dupes = len(hook_texts) - len(set(hook_texts))
        subact_set = sorted({subacts.get(ep, "UNMAPPED") for ep in eps})
        owners = {acts[ep].get("PRIMARY_DECISION_OWNER", "") for ep in eps}
        owner_auth = Counter(acts[ep].get("OWNER_ROUTE_AUTHORITY", "") for ep in eps)
        human_auth = Counter(extra.get(ep, {}).get("HUMAN_ROUTE_AUTHORITY", "") for ep in eps)
        costs = Counter(cost_class(extra.get(ep, {})) for ep in eps)

        # Hostile threshold: a concentrated family is a false-depth failure only
        # when the underlying decision/payoff/retention chain also collapses.
        # We require cross-subact movement, no exact repeated decision beat, and
        # reasonably low adjacent semantic overlap across the combined scene aim.
        local_fail = []
        if len(subact_set) < 2:
            local_fail.append("dominant family does not cross at least two approved subacts")
        if exact_decision_dupes:
            local_fail.append(f"exact decision duplicates={exact_decision_dupes}")
        if avg_j > 0.55:
            local_fail.append(f"average adjacent decision+payoff+hook Jaccard too high={avg_j:.2f}")
        if len(owners) < 4:
            local_fail.append(f"decision-owner routing diversity too low={len(owners)}")
        if len(costs) < 2:
            local_fail.append(f"cost diversity too low={len(costs)}")
        if local_fail:
            failures.append(f"E{lo:03d}–E{hi:03d}: " + "; ".join(local_fail))

        # Representative start/middle/end dominant-family episodes.
        picks = sorted({eps[0], eps[len(eps)//2], eps[-1]})
        reps = []
        for ep in picks:
            reps.append((
                ep,
                subacts.get(ep, "UNMAPPED"),
                acts[ep].get("DECISION_BEAT", "")[:180],
                acts[ep].get("READER_PAYOFF_THIS_EP", "")[:180],
                cost_class(extra.get(ep, {})),
            ))

        results.append({
            "lo": lo, "hi": hi, "family": family, "rationale": rationale, "eps": eps,
            "subacts": subact_set, "owners": len(owners), "owner_auth": owner_auth,
            "human_auth": human_auth, "costs": costs, "avg_j": avg_j, "max_j": max_j,
            "decision_dupes": exact_decision_dupes, "payoff_dupes": exact_payoff_dupes,
            "hook_dupes": exact_hook_dupes, "reps": reps, "local_fail": local_fail,
        })

    status = "PASS" if not failures else "FAIL"
    lines = [
        "# Long-Window Narrative-Engine Differentiation Red-Team v1",
        "",
        f"Status: {status} — EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        "## Standard",
        "",
        "Dominant-engine concentration is not repaired by cosmetic relabeling. It passes only if approved subacts, decision ownership, cost, payoff and retention movement remain differentiated. The six windows below are the exact v2 long-window WATCH ranges.",
        "",
        "## Window results",
        "",
        "| Window | Dominant family episodes | Approved subacts crossed | Distinct owner routes | Distinct cost classes | Avg adjacent semantic overlap | Exact decision dupes | Verdict |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for r in results:
        lines.append(
            f"| E{r['lo']:03d}–E{r['hi']:03d} `{r['family']}` | {len(r['eps'])}/{r['hi']-r['lo']+1} | {len(r['subacts'])} | {r['owners']} | {len(r['costs'])} | {r['avg_j']:.2f} | {r['decision_dupes']} | {'FAIL' if r['local_fail'] else 'PASS-DIFFERENTIATED'} |"
        )

    for r in results:
        lines.extend([
            "",
            f"## E{r['lo']:03d}–E{r['hi']:03d} — `{r['family']}`",
            "",
            f"Source-level rationale: {r['rationale']}",
            "",
            f"- approved subacts crossed: {', '.join(r['subacts'])}",
            f"- owner authority modes: {dict(r['owner_auth'])}",
            f"- human-route authority modes: {dict(r['human_auth'])}",
            f"- cost classes: {dict(r['costs'])}",
            f"- exact payoff duplicates: {r['payoff_dupes']}; exact retention duplicates: {r['hook_dupes']}",
            f"- adjacent semantic overlap avg/max: {r['avg_j']:.2f}/{r['max_j']:.2f}",
            "",
            "Representative source-bound activation points:",
        ])
        for ep, subact, decision, payoff, cost in r["reps"]:
            lines.append(f"- E{ep:03d} / {subact} / cost `{cost}` — decision: {decision} / payoff: {payoff}")
        if r["local_fail"]:
            lines.append("- **FAIL reasons:** " + "; ".join(r["local_fail"]))
        else:
            lines.append("- **RULING: PASS-DIFFERENTIATED** — keep the dominant family; do not cosmetically relabel it.")

    lines.extend(["", "## Failure queue", ""])
    if failures:
        lines.extend(f"- {f}" for f in failures)
    else:
        lines.append("- NONE")

    lines.extend([
        "",
        "## Final ruling",
        "",
        f"- six long-window engine WATCH ranges reviewed: **{len(results)}/6**",
        f"- unresolved repetitive-engine windows: **{len(failures)}**",
        "- cosmetic engine relabels introduced: **0**",
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
            raise SystemExit("long-window engine audit stale/missing")
    else:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(text, encoding="utf-8")
    print(text)
    if "Status: FAIL" in text:
        raise SystemExit("LONG-WINDOW ENGINE DIFFERENTIATION GATE FAIL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
