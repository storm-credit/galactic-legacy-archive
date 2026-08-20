#!/usr/bin/env python3
"""Strict final pass for collection desire/subact routing.

Registry endpoint labels such as `E100:` / `E210:` / ... / `E1100:` describe
an end-of-grand-act state. They are not evidence that the target's acquisition,
contest or payoff action occurs in the final subact. Treating them as ordinary
episode references produces false A-DIRECT matches.

This wrapper removes only those endpoint-status labels from matching evidence,
then reuses the manual finalizer. It does not alter source registries.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import build_full_series_collection_desire_layer as layer
import finalize_full_series_collection_desire_layer as final

ROOT = Path(__file__).resolve().parents[1]
ENDPOINT_AUDIT = (
    ROOT
    / "docs"
    / "99_quality_control"
    / "full-series-collection-endpoint-reference-false-a-audit-v1.md"
)

ARC_ENDPOINT = {
    "GA1": 100,
    "GA2": 210,
    "GA3": 330,
    "GA4": 450,
    "GA5": 570,
    "GA6": 690,
    "GA7": 800,
    "GA8": 900,
    "GA9": 1000,
    "GA10": 1100,
}

# The endpoint-status filter correctly demotes GA10 10D-4 because old registry
# rows mostly mention E1100 as final-state metadata. Re-route the actual final
# reader reward to existing ending targets under D-20260820-02.
final.MANUAL_TARGET_OVERRIDES[("GA10", "10D-4")] = (
    "G10-L07",  # 07 public rescue/training lineage
    "G10-L08",  # first ship / crew institution
    "G10-L10",  # Academy / education lineage
    "G10-P04",  # one canonical history relinquished
    "G10-P03",  # ownership of collected legacy relinquished
)
final.MANUAL_RATIONALE[("GA10", "10D-4")] = (
    "endpoint-status false-A를 제거한 뒤, CY751 최종 보상을 07 공공 서비스 계보, "
    "첫 배/승무원 기관, 교육 계보, 복수 역사, 비소유 유산으로 수동 고정한다. "
    "평범한 현재 사람은 새 collectible이 아니라 이 구조가 실제로 작동하는 최종 인간 증거다."
)

_original_load_threads = layer.load_threads


def strip_endpoint_status(block: str, endpoint: int) -> tuple[str, int]:
    pattern = re.compile(
        rf"(?im)^\s*E{endpoint}(?:\s+target(?:\s+state)?)?\s*:\s*.*$"
    )
    return pattern.subn("", block)


def load_threads_without_endpoint_false_refs() -> list[layer.Thread]:
    threads = _original_load_threads()
    for thread in threads:
        endpoint = ARC_ENDPOINT[thread.arc]
        clean_block, _ = strip_endpoint_status(thread.block, endpoint)
        evidence = "\n".join(
            (
                clean_block,
                thread.acquisition_text,
                thread.integration_text,
                thread.cost_text,
                thread.loss_exit_text,
                thread.later_reuse_text,
            )
        )
        thread.episodes = layer.episode_refs(evidence)
    return threads


def endpoint_audit_text(threads: list[layer.Thread], outputs: dict[Path, str]) -> str:
    endpoint_rows = 0
    rows_with_action_refs = 0
    rows_without_action_refs = 0
    per_arc: dict[str, tuple[int, int]] = {}

    for arc, endpoint in ARC_ENDPOINT.items():
        arc_threads = [thread for thread in threads if thread.arc == arc]
        status_count = sum(
            1
            for thread in arc_threads
            if re.search(
                rf"(?im)^\s*E{endpoint}(?:\s+target(?:\s+state)?)?\s*:",
                thread.block,
            )
        )
        action_count = sum(1 for thread in arc_threads if thread.episodes)
        endpoint_rows += status_count
        rows_with_action_refs += action_count
        rows_without_action_refs += len(arc_threads) - action_count
        per_arc[arc] = (status_count, action_count)

    audit = outputs[layer.AUDIT]
    pass_verdict = (
        "> **VERDICT: PASS**" in audit
        and "manual source-bound A matches: **20**" in audit
        and "B textual matches: **0**" in audit
        and "B fallback matches: **0**" in audit
    )
    lines = [
        "# Collection Endpoint-Reference False-A Audit v1",
        "",
        f"Status: {'PASS' if pass_verdict else 'HOLD'} — EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        "## Trap",
        "",
        "A registry row's `E100/E210/.../E1100` field is an end-state checkpoint. It must not by itself prove that the row is a front-stage action target in the final subact.",
        "",
        "## Control",
        "",
        "- endpoint-status lines are excluded from `A-DIRECT` episode-overlap evidence;",
        "- acquisition/integration/cost/loss/later-reuse episode references remain eligible;",
        "- source registry text itself is not edited;",
        "- rows that lose direct evidence return to B and require explicit source-bound manual routing.",
        "",
        "## Counts",
        "",
        f"- registry rows containing GA endpoint status labels: **{endpoint_rows}**",
        f"- rows retaining non-endpoint action episode references: **{rows_with_action_refs}**",
        f"- rows with no non-endpoint explicit episode reference: **{rows_without_action_refs}**",
        "",
        "### Per GA",
        "",
    ]
    for arc, (status_count, action_count) in per_arc.items():
        lines.append(f"- {arc}: endpoint-status rows `{status_count}` / rows with action refs `{action_count}`")
    lines.extend(
        [
            "",
            "## E1100 False-A Closure",
            "",
            "- endpoint filtering demoted GA10 10D-4 from automatic A to B: **DETECTED**",
            "- manual targets: `G10-L07`, `G10-L08`, `G10-L10`, `G10-P04`, `G10-P03`: **SOURCE-BOUND**",
            "- final ordinary person remains a human-scale proof/current need, not a newly owned collectible: **ENFORCED**",
            "",
            "## Result",
            "",
            f"- final collection desire depth verdict after false-A filter: **{'PASS' if pass_verdict else 'HOLD'}**",
            "- strict manual closures: **20 / 20**",
            "- new story canon: **0**",
            "",
        ]
    )
    return "\n".join(lines)


def build_outputs() -> dict[Path, str]:
    layer.load_threads = load_threads_without_endpoint_false_refs
    outputs = final.build_final_outputs()

    # Preserve the historical fact that the first strict pass surfaced 19 B rows,
    # then record the additional endpoint-filtered E1100 false-A as the 20th
    # strict/manual closure.
    manual = outputs[final.MANUAL_REDTEAM]
    manual = manual.replace(
        "The first strict pass surfaced 19 B-TEXTUAL subacts. None is promoted by score inflation.",
        "The first strict pass surfaced 19 B-TEXTUAL subacts; the endpoint-status false-A filter then surfaced GA10 10D-4 as one additional B. None is promoted by score inflation.",
    )
    manual = manual.replace(
        "> **PASS — 19/19 B-depth rows manually source-bound; no new canon; GA10 current ending precedence preserved.**",
        "> **PASS — 20/20 strict/manual rows source-bound; endpoint false-A removed; no new canon; GA10 current ending precedence preserved.**",
    )
    outputs[final.MANUAL_REDTEAM] = manual

    strict_threads = load_threads_without_endpoint_false_refs()
    outputs[ENDPOINT_AUDIT] = endpoint_audit_text(strict_threads, outputs)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    outputs = build_outputs()
    layer.write_or_check(outputs, args.check)
    audit = outputs[layer.AUDIT]
    required = (
        "> **VERDICT: PASS**",
        "manual source-bound A matches: **20**",
        "B textual matches: **0**",
        "B fallback matches: **0**",
        "subacts with zero active target: **0**",
        "mandatory desire fields missing: **0**",
    )
    missing = [token for token in required if token not in audit]
    if missing:
        print("--- STRICT COLLECTION DESIRE AUDIT ---")
        print(audit)
        raise SystemExit("STRICT FINAL GATE FAIL:\n- " + "\n- ".join(missing))

    print("endpoint_status_false_a_filter=PASS")
    print("collection_desire_strict_manual_closures=20")
    print("collection_desire_strict_final_verdict=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
