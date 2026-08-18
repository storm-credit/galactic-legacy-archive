# Continuity Issues — 연속성 모순 등록부

Status: CANON PROJECT CONTROL — LIVING REGISTRY
Owner Agents: X04 Continuity / O01 Canon
Last Reviewed: 2026-08-17
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
