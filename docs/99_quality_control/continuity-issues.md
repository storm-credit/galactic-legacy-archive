# Continuity Issues — 연속성 모순 등록부

Status: CANON PROJECT CONTROL — LIVING REGISTRY
Owner Agents: X04 Continuity / O01 Canon
Last Reviewed: 2026-08-20
Depends On: [[revision-harness]] Pass 4, [[manuscript-production-workflow-v1]] §3.3
Used By: 모든 원고 검수 사이클
Open Risks: 없음 — 미해결 항목이 곧 위험 목록이다

## 사용 규칙

- 원고 검수 Pass 4(세계·정본 연속성)에서 발견된 모든 모순을 이 파일에 등록하고 수정 파급 범위를 기록한다.
- S0/S1 등록 시 해당 회차는 BLOCKED — 해소 전 작가 승인 요청 불가.
- 심각도 등급 대응: revision-harness는 S0~S4, 게이트 체계는 S0~S3을 사용한다. **S4(NOTE) = 게이트 체계의 기록성 노트**로 취급하며 차단력이 없다.

## 등록 양식

```markdown
### CI-{YYYYMMDD}-{NN}
- Episode/Location:
- Severity: S0 | S1 | S2 | S3 | S4
- Problem:
- Canon Source (충돌 근거 파일):
- Required Fix:
- Ripple (파급 범위):
- Status: OPEN | FIXED | WONTFIX(사유)
```

## 등록 항목

### CI-20260817-01
- Episode/Location: GA1 E1–5 / F-25 scene-card provenance
- Severity: S4
- Problem: [[ga1-episodes-1-5-noncanon-scene-cards-v1]]은 레거시 파일명·헤더에서 non-canon test material로 남아 있으나, 이후 통제 문서는 이 파일을 E1–5의 검증된 drafting input / exact cards로 참조하고 [[effective-canon-status-manifest-v1]]은 first-100 operational/scene-card design의 유효 권한을 AS(Approved Structure)로 규정한다. 이 둘을 구분하지 않으면 “집필 입력으로 승인된 구조”와 “파일 자체의 canonical manuscript/정본 문서 승격”을 같은 결정으로 오독할 수 있다.
- Canon Source (충돌 근거 파일): [[effective-canon-status-manifest-v1]] §2·§4·§6, [[first-writing-batch-readiness-v1]] §2.2·§4, [[first-100-act-map-v2-consolidated]] A1, [[ga1-episodes-1-5-noncanon-scene-cards-v1]] header
- Required Fix: provenance 해석만 정규화한다. E1–5의 승인된 scene-level 구조는 AS drafting authority로 사용하되, 별도 명시적 문서 승격 결정 없이 `ga1-episodes-1-5-noncanon-scene-cards-v1.md`의 파일명·레거시 헤더를 개명/승격하지 않는다. canonical manuscript 지위와 publication authorization은 별개다.
- Ripple (파급 범위): 없음. E1–5 원고의 `Source Cards`는 그대로 유지하고, 장면카드 본문·원고 산문·사건·수치·인물·권한·정본 설정은 변경하지 않는다.
- Status: FIXED

### CI-20260820-01
- Episode/Location: GA10 E1076–1100 / `ENDING-S1-01`
- Severity: S1
- Problem: 상위 정본인 [[master-series-chronology-v1]]과 [[ga10-episodes-1001-1100-act-map-v1]]은 E1076–1095를 CY748-03-25~07-31 main-story close, E1096–1100을 CY751 epilogue로 고정하고 E1083–1089에 iconic legacy return, E1090–1095에 plural history/accountability를 요구한다. 반면 2026-08-05 하위 상세카드는 E1076을 CY747-11에 시작해 E1100을 CY748-01-11에 끝내고, craft-title/ordinary-crisis/final-ledger를 E1100까지 밀어 상위 구조와 충돌했다.
- Canon Source (충돌 근거 파일): [[master-series-chronology-v1]] GA10 chronology, [[ga10-episodes-1001-1100-act-map-v1]] ACT 10D, [[final-payoff-scene-ledger-locked-v1]] M-001/M-002/M-003/M-004/M-012/M-017/M-019/M-020, [[ga1-10-operational-checkpoint-snapshots-v1]] GA10 main-end/epilogue snapshot
- Required Fix: 작가 승인 [[ga10-ending-reconciliation-canon-amendment-2026-08-20]]에 따라 Option C를 적용한다. 기존 유효 장부·손실·수치·책임 사실은 E1076–1095 안에 보존·재배치하고, E1083–1089 locked ownership sequence와 E1090–1095 no-Rian/history sequence를 복구하며, E1096–1100을 CY751-08-03 epilogue로 복원한다. M-019 final unlabeled-person scene은 author-approved change control로 E1099→E1100(+1) 이동해 M-020 E1100 proof와 결합한다.
- Ripple (파급 범위): [[ga10-e1076-1085-episode-cards-v1]], [[ga10-e1086-1093-episode-cards-v1]], [[ga10-e1094-1100-episode-cards-v1]], [[ga10-ending-reconciliation-canon-amendment-2026-08-20]], final endpoint interpretation for 07/파루스/Ern/core relationships, decision log. Named permanent losses, casualty totals, Haren sanctions, Rian index loss, story length 1100 and Publication gate are not relaxed.
- Status: FIXED — reconciled detailed cards and canon amendment produced; effective on merge of the same change set
