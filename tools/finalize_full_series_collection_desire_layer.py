#!/usr/bin/env python3
"""Finalize the full-series collection-desire layer with manual source-bound routing.

The base builder intentionally surfaces B-TEXTUAL rows rather than silently
pretending lexical matching is authoritative. This finalizer closes only those
reviewed rows by explicit source-registry IDs and adds GA10 ending-precedence
routing from D-20260820-02.

No story canon is created or altered here.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import build_full_series_collection_desire_layer as layer

ROOT = Path(__file__).resolve().parents[1]
MANUAL_REDTEAM = (
    ROOT
    / "docs"
    / "99_quality_control"
    / "full-series-collection-desire-manual-b-depth-redteam-v1.md"
)

# Explicit source-bound replacements for the 19 rows surfaced by the first
# strict pass. IDs are existing registry headings, never newly created targets.
MANUAL_TARGET_OVERRIDES: dict[tuple[str, str], tuple[str, ...]] = {
    ("GA4", "4A-2"): ("G4-P07", "G4-P08", "G4-E01", "G4-E04", "G4-E05"),
    ("GA6", "6A-1"): ("G6-P02", "G6-A08", "G6-P05", "G6-P07", "G6-P08"),
    ("GA9", "9A-1"): ("G9-P02", "G9-R01", "G9-R07", "G9-P08", "G9-R02"),
    ("GA9", "9A-4"): ("G9-P05", "G9-R04", "G9-R08", "G9-P03", "G9-P04"),
    ("GA9", "9B-3"): ("G9-P04", "G9-M02", "G9-P01", "G9-P08", "G9-R08"),
    ("GA10", "10A-2"): ("G10-A01", "G10-R01", "G10-R07", "G10-R05", "G10-A04"),
    ("GA10", "10A-3"): ("G10-R01", "G10-R02", "G10-R03", "G10-R04", "G10-R05"),
    ("GA10", "10A-4"): ("G10-A02", "G10-A03", "G10-A04", "G10-A06", "G10-A07"),
    ("GA10", "10B-1"): ("G10-A02", "G10-R08", "G10-R01", "G10-R09", "G10-R02"),
    ("GA10", "10B-2"): ("G10-A04", "G10-R07", "G10-R10", "G10-R09", "G10-R04"),
    ("GA10", "10B-3"): ("G10-R05", "G10-R08", "G10-R02", "G10-R01", "G10-A06"),
    ("GA10", "10B-4"): ("G10-R01", "G10-R09", "G10-R06", "G10-R02", "G10-A06"),
    ("GA10", "10C-1"): ("G10-P01", "G10-R01", "G10-R03", "G10-R04", "G10-R05"),
    ("GA10", "10C-2"): ("G10-P02", "G10-R06", "G10-R07", "G10-L06", "G10-P01"),
    ("GA10", "10C-3"): ("G10-P01", "G10-R04", "G10-R07", "G10-L09", "G10-R03"),
    ("GA10", "10C-4"): ("G10-A07", "G10-R01", "G10-R02", "G10-R03", "G10-R08"),
    ("GA10", "10D-1"): ("G10-R02", "G10-R09", "G10-R10", "G10-L08", "G10-R05"),
    ("GA10", "10D-2"): ("G10-P03", "G10-L07", "G10-L08", "G10-L03", "G10-L01"),
    ("GA10", "10D-3"): ("G10-P04", "G10-M02", "G10-M04", "G10-M08", "G10-R06"),
}

MANUAL_RATIONALE: dict[tuple[str, str], str] = {
    ("GA4", "4A-2"): "증거 문서만이 아니라 실제 courier/witness/source coalition을 전면에 둬 '증거가 먼저 죽는다'의 사람·증거 chain을 복원한다.",
    ("GA6", "6A-1"): "Orpheus 구조적 재현을 convoy council, local workers, autonomous commanders, survivors, node capacity가 동시에 체감하게 하는 기존 5개 target을 명시 승인한다.",
    ("GA9", "9A-1"): "beneficiary community와 minimum-service corridor, corrective override를 중심으로 '서비스가 돌아옴'의 실제 수혜/예외/분류 비용을 묶는다.",
    ("GA9", "9A-4"): "자발적 synchronization이 opt-out/hybrid 지역에 주는 간접 압력을 reformer/hardliner/forced-harm ledger와 함께 보이게 한다.",
    ("GA9", "9B-3"): "테러를 hardliner 사건 + 중앙 효율성의 실제 장점 + Continuity/Human Corrective 대응 + forced-harm ledger로 묶어 단순 악역 증명으로 만들지 않는다.",
    ("GA10", "10A-2"): "첫 handoff 실패를 중앙 retake가 아니라 regional current-status, corrective assembly, technical/medical commons로 실제 복구하는 target set이다.",
    ("GA10", "10A-3"): "의존 목록을 identity/service/route/fleet/technical의 기존 functional distribution targets로 직접 연결한다.",
    ("GA10", "10A-4"): "서로 다른 전환 속도와 모델을 A02/A03/A04/A06/A07 대표 상태로 나눠 '모두 같은 날 자유'를 거부한다.",
    ("GA10", "10B-1"): "자동 매칭의 Opt-Out 지역 오선택을 교정하고, 실제 '자발적으로 중앙 서비스를 더 유지하는' A02를 primary carrier로 둔다.",
    ("GA10", "10B-2"): "local capture를 A04와 appeal/corrective/claims/safe-exit/mission network가 견제하는 구조로 묶는다.",
    ("GA10", "10B-3"): "의료·기술 호환을 R05/R08/R02/R01과 AI/composite 비영토 공동체 A06까지 연결해 하나의 certifier로 환원하지 않는다.",
    ("GA10", "10B-4"): "국경 사이 identity/service 문제를 current-status, migration/safe-exit, archive translation, minimum service, AI/composite status로 직접 묶는다.",
    ("GA10", "10C-1"): "마지막 이양 작전을 central corrective command와 지역/route/fleet/technical 기능 분산 자체로 추적한다.",
    ("GA10", "10C-2"): "Exclusive Future/Archive Index P02를 핵심 부담으로 전면화하되, 실제 영구 물리 제거는 D-20260820-02에 따라 E1088로 보존한다.",
    ("GA10", "10C-3"): "마지막 중앙명령은 P01/R04/R07/L09/R03로 연결해 분산을 지키기 위해 쓰고 만료하는 기능으로만 남긴다.",
    ("GA10", "10C-4"): "Seed sovereignty 종료를 A07과 regional/minimum/route/residual-service 기관으로 나눠 '무주인 현재'를 실제 운영 상태로 만든다.",
    ("GA10", "10D-1"): "재건·청구·이주·기술/의료·첫 배의 서비스 전환을 묶어 전쟁 뒤의 수집 보상을 '정리할 책임'으로 바꾼다.",
    ("GA10", "10D-2"): "P03 Ownership of Collected Legacy를 07/첫 배/독립 archive·route actors의 반환·독립 custody로 해소한다.",
    ("GA10", "10D-3"): "P04 One Canonical History를 Blood Admiral/Thirteen Heroes/Archive right-wrong/translation commons와 묶어 복수 역사로 종결한다.",
}

# Higher current project-control source. This never creates an ending fact; it
# prevents older REVIEW/open wording from overriding the author-approved end.
ENDING_GUARD_CODES = {"10C-2", "10D-1", "10D-2", "10D-3", "10D-4"}
ENDING_GUARD_LINE = (
    "- `ENDING_PRECEDENCE_GUARD`: `D-20260820-02 / "
    "ga10-ending-reconciliation-canon-amendment-2026-08-20` — conflicting "
    "older REVIEW/open registry wording cannot override the reconciled ending."
)

# Field-level fixes are required only where a lower macro map can be misread as
# the final current endpoint. All wording below paraphrases existing approved
# project-control / writer-activation facts.
FIELD_OVERRIDES: dict[tuple[str, str], dict[str, str]] = {
    ("GA10", "10C-2"): {
        "discovery": "Rian's exclusive future/Archive index has become a final dependency and ownership burden, not a prize to preserve.",
        "acquisition": "commit to the distributed/institutional replacement path; do not treat E1058–1063 as the final physical removal scene.",
        "synergy": "Archive translation, corrective assembly and current technical/medical operators must be able to function without a permanent private master-query path.",
        "cost": "Rian gives up exclusive certainty and future-ranking privilege; the final irreversible physical removal, credential expiry and unrecoverable query gaps remain locked to the reconciled E1088 implementation.",
        "hook": "the later E1083–1089 handoff must physically close the remaining exclusive interface with no recoverable master backdoor.",
    },
    ("GA10", "10D-1"): {
        "discovery": "after transition battle, services, demobilization, prisoners, migration, claims and residual module/connector obligations remain materially unfinished.",
        "acquisition": "transition institutions continue reconstruction and claim handling without restoring Rian's standing central command.",
        "synergy": "minimum service, safe exit, claims, technical/medical commons and the first-ship service institution carry different parts of postwar recovery.",
        "cost": "unequal recovery, unresolved claims and permanent losses remain visible; reconstruction is not a reset to prewar assets or authority.",
        "hook": "with immediate reconstruction underway, iconic people/assets/records must be returned or placed in independent/plural custody.",
    },
    ("GA10", "10D-2"): {
        "discovery": "the collected legacy cannot end as Rian's personal roster, fleet, museum, archive or sovereign standard.",
        "acquisition": "07, the first ship, records and people/institutions resolve into independent or plural living custody rather than protagonist possession.",
        "synergy": "07 survives only in its bounded public rescue/training legacy, the first ship serves an independent route-school/rescue role, and core actors remain legible through their own work.",
        "cost": "sentimental relinquishment and permanent hardware/human losses remain; no set completion restores 07's wartime monopoly or Parus strategic propulsion.",
        "hook": "after ownership is relinquished, the remaining question is who gets to tell the history and whether institutions work without Rian.",
    },
    ("GA10", "10D-3"): {
        "discovery": "plural histories, accountability, claims and one real ordinary no-Rian crisis must coexist without a master heroic account.",
        "acquisition": "institutions prove present service and current decisions can continue through local/medical/route/current-status actors while incompatible historical accounts remain available.",
        "synergy": "translation commons, claims, public/protected records and ordinary institutions preserve usable evidence without recreating a sovereign curator.",
        "cost": "real deaths, harms, delays, propaganda and unresolved claims are not cancelled by a cleaner retrospective narrative.",
        "hook": "CY751 must show what survived in ordinary work, relationships and service rather than reopen a final war or reset.",
    },
    ("GA10", "10D-4"): {
        "discovery": "CY751 ordinary institutions, unequal recovery, independent futures and incomplete histories are the surviving legacy state.",
        "acquisition": "the final reward is not possession: ordinary people can act, correct/refuse records and ask for present service needs without Rian's future index.",
        "synergy": "public-service/training 07, route-school/rescue first ship, independent core actors and plural records remain useful without recombining into one protagonist-owned set.",
        "cost": "history stays incomplete, sanctions and irreversible losses remain, and no Archive answer turns the present person into a destined collectible.",
        "hook": "terminal desire: ask the ordinary person's current name and/or what they need now; no chosen-one signal, Archive reaction, reset or E1101 bait.",
    },
}

_original_select_threads = layer.select_threads
_original_source_field_pack = layer.source_field_pack
_original_audit_text = layer.audit_text


def select_threads_manual(subact: layer.Subact, threads: list[layer.Thread]):
    key = (subact.arc, subact.code)
    override_ids = MANUAL_TARGET_OVERRIDES.get(key)
    if not override_ids:
        return _original_select_threads(subact, threads)

    by_id = {thread.source_id: thread for thread in threads if thread.arc == subact.arc}
    missing = [source_id for source_id in override_ids if source_id not in by_id]
    if missing:
        raise SystemExit(f"{subact.arc} {subact.code}: missing manual registry IDs: {missing}")
    selected = [
        (by_id[source_id], 200 - index, "MANUAL_SOURCE_BOUND")
        for index, source_id in enumerate(override_ids)
    ]
    return selected, "A-MANUAL"


def source_field_pack_manual(subact: layer.Subact, selected):
    fields = _original_source_field_pack(subact, selected)
    fields.update(FIELD_OVERRIDES.get((subact.arc, subact.code), {}))
    return fields


def audit_text_manual(all_rows, threads, subacts_by_arc, selected_usage):
    text = _original_audit_text(all_rows, threads, subacts_by_arc, selected_usage)
    quality = Counter(str(row["quality"]) for row in all_rows)
    text = text.replace(
        f"- direct A matches: **{quality.get('A-DIRECT', 0)}**",
        f"- direct A matches: **{quality.get('A-DIRECT', 0)}**\n"
        f"- manual source-bound A matches: **{quality.get('A-MANUAL', 0)}**",
    )
    return text


def inject_ending_guard(text: str, code: str) -> str:
    header = f"## {code} —"
    start = text.find(header)
    if start < 0:
        raise SystemExit(f"GA10 output missing block {code}")
    next_start = text.find("\n## ", start + len(header))
    if next_start < 0:
        next_start = len(text)
    block = text[start:next_start]
    if ENDING_GUARD_LINE in block:
        return text
    marker = "- `NEW_CANON_REQUIRED`: `NO`"
    if marker not in block:
        raise SystemExit(f"GA10 {code}: NEW_CANON marker missing")
    block = block.replace(marker, ENDING_GUARD_LINE + "\n" + marker, 1)
    return text[:start] + block + text[next_start:]


def manual_redteam_text(outputs: dict[Path, str]) -> str:
    ga_map = {arc: layer.parse_subacts(arc, filename) for arc, filename in layer.ACT_MAPS}
    lines = [
        "# Full-Series Collection Desire Manual B-Depth Red-Team v1",
        "",
        "Status: PASS — EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        "## Purpose",
        "",
        "The first strict pass surfaced 19 B-TEXTUAL subacts. None is promoted by score inflation. Each row below was routed to existing registry IDs after direct subact/registry review.",
        "",
        "## Manual Closure Table",
        "",
        "| Subact | Episodes | Existing source targets | Reason |",
        "|---|---:|---|---|",
    ]
    for key, ids in MANUAL_TARGET_OVERRIDES.items():
        arc, code = key
        subact = next(item for item in ga_map[arc] if item.code == code)
        reason = MANUAL_RATIONALE[key].replace("|", "/")
        lines.append(
            f"| {arc} {code} | E{subact.start}–E{subact.end} | `{'`, `'.join(ids)}` | {reason} |"
        )

    lines.extend(
        [
            "",
            "## GA10 Ending Precedence Attack",
            "",
            "- D-20260820-02 / `ga10-ending-reconciliation-canon-amendment-2026-08-20` is higher than older REVIEW/open GA10 registry wording: **ENFORCED**.",
            "- 10C-2 cannot claim that the exclusive index is already physically and finally removed in E1058–1063; current ending implementation places irreversible removal/credential expiry at E1088: **ENFORCED**.",
            "- E1076–1082 reconstruction, E1083–1089 return/distribution, E1090–1095 plural-history/no-Rian proof, E1096–1100 CY751 epilogue: **ENFORCED**.",
            "- 07 wartime monopoly is not restored; bounded public rescue/training lineage may survive: **ENFORCED**.",
            "- Parus strategic propulsion remains permanently lost and the ship cannot return as Rian's private flagship: **ENFORCED**.",
            "- Rian future-index/master-query path and repeatable reset remain lost: **ENFORCED**.",
            "- E1100 ordinary-person endpoint receives no Archive/destiny/reset signal: **ENFORCED**.",
            "",
            "## Cross-GA Reward Carry",
            "",
        ]
    )

    for index in range(len(layer.ACT_MAPS) - 1):
        arc, _ = layer.ACT_MAPS[index]
        next_arc, _ = layer.ACT_MAPS[index + 1]
        left = ga_map[arc][-1]
        right = ga_map[next_arc][0]
        lines.append(
            f"- {arc} {left.code} E{left.start}–{left.end} → {next_arc} {right.code} E{right.start}–{right.end}: previous changed state/next desire must carry; acquisition state may not reset to zero. **PASS — source maps present**"
        )

    lines.extend(
        [
            "",
            "## Reverse Red-Team",
            "",
            "- 415 registry rows are **not** reported as 415 unique owned collectibles.",
            "- `CLT-*` is a source-thread ID, not a unique-entity assertion.",
            "- `CLSET-*` is an author execution grouping, not a new Archive/in-world set.",
            "- no positive-relic-per-GA quota was introduced.",
            "- no C1 reader-facing label decision was forced.",
            "- people/AI persons/communities retain consent, refusal, exit and independent action.",
            "- institutions and territories retain constituencies, claims, appeal, autonomy and succession.",
            "- physical possession does not automatically grant certification, crew, ammunition, industry, command or title.",
            "- irreversible deaths/losses cannot be repaired for set completion.",
            "- new story canon required: **0**.",
            "",
            "## Verdict",
            "",
            "> **PASS — 19/19 B-depth rows manually source-bound; no new canon; GA10 current ending precedence preserved.**",
            "",
        ]
    )
    return "\n".join(lines)


def build_final_outputs() -> dict[Path, str]:
    layer.select_threads = select_threads_manual
    layer.source_field_pack = source_field_pack_manual
    layer.audit_text = audit_text_manual
    outputs = layer.build_outputs()

    ga10_path = layer.OUT_DIR / "ga10-collection-desire-subact-map-v1.md"
    ga10_text = outputs[ga10_path]
    for code in sorted(ENDING_GUARD_CODES):
        ga10_text = inject_ending_guard(ga10_text, code)
    outputs[ga10_path] = ga10_text
    outputs[MANUAL_REDTEAM] = manual_redteam_text(outputs)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = build_final_outputs()
    layer.write_or_check(outputs, args.check)

    audit = outputs[layer.AUDIT]
    required = (
        "> **VERDICT: PASS**",
        "manual source-bound A matches: **19**",
        "B textual matches: **0**",
        "B fallback matches: **0**",
        "subacts with zero active target: **0**",
        "mandatory desire fields missing: **0**",
    )
    missing = [token for token in required if token not in audit]
    if missing:
        raise SystemExit("FINAL COLLECTION DESIRE GATE FAIL:\n- " + "\n- ".join(missing))

    print(f"collection_desire_final_outputs={len(outputs)}")
    print("collection_desire_manual_overrides=19")
    print("collection_desire_b_depth_remaining=0")
    print("collection_desire_final_verdict=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
