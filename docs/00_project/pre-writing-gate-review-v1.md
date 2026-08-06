# Pre-Writing Gate Review v1

Status: REVIEW — GATE DECISION SUPPORT
Owner Agents: A00 PM / O01 Canon / O02 Gates / X04 Continuity
Last Reviewed: 2026-08-06
Depends On: `docs/99_quality_control/prewriting-gate.md`, `docs/99_quality_control/prewriting-gate-dry-audit-2026-08-03.md`, `docs/99_quality_control/prewriting-gate-evidence-matrix-v2.md`, `docs/00_project/design-only-scope-restoration-2026-08-03.md`, `docs/00_project/context-handoff-detail-complete-after-e1100-2026-08-05.md`, `docs/99_quality_control/pre-writing-readiness-audit-v1.md`
Used By: 작가의 Pre-Writing Gate 개방 결정
Open Risks: 이 문서는 게이트를 열지 않는다. 개방은 작가의 명시 선언으로만 가능하다.

## 0. 검증 기록 (2026-08-06)

- PR #89: `state=MERGED`, `mergedAt=2026-08-05T15:18:23Z`, merge SHA `54f4ad870296b7d3d12dc3ade76d9a0fa47e58ef` — 기록과 일치, `main` HEAD 동일.
- 필수 파일 6종(`ga10-detail-progress-status-1000`, `detail-design-completion-status-1000`, `context-handoff-detail-complete-after-e1100`, `ga10-e1001-1100-final-cross-audit-v1`, `e101-1100-complete-detail-cross-audit-v1`, `canonical-haren-sanction-timeline-errata-004`) 모두 `main`에 존재.
- GitHub issue #26 (`[Gate 1] Run human mobile opening and voice blind tests`): **OPEN** — 인간/모바일 테스트 미실시.

## 1. 현재 게이트 상태

> **Pre-Writing Gate: CLOSED / Manuscript: BLOCKED** (유지 중)

- 정본 게이트 문서는 `docs/99_quality_control/prewriting-gate.md`(CANON).
- 2026-08-03 드라이 감사 판정: 내부 설계 준비 PASS / 인간 전달 검증 OPEN / Gate 10 FAIL·BLOCKED.
- 그 이후 변경: E101~1100 상세설계 완료 및 교차감사 PASS(2026-08-05, PR #89). 이는 Gate 6/9 증거를 강화했을 뿐, Gate 10 차단 요건(인간 검증 + 작가 명시 승인)은 하나도 해소하지 않았다.
- 따라서 게이트 폐쇄는 현재도 정당하다. 단, 남은 차단 요건은 "설계 부족"이 아니라 **작가 결정 사항**이다.

## 2. 정본 파일 계층 (요약)

유효 정본 우선순위는 `docs/00_project/design-only-scope-restoration-2026-08-03.md` §3과 `docs/00_project/effective-canon-status-manifest-v1.md` §6이 정의한다:

1. 작가 명시 지시 및 현행 프로젝트 통제 문서(PC) — 에라타 001~004 포함
2. 최종 정본 바이블(세계·인물·시스템)
3. 마스터 연표·운영 상태 시트·회수 장부
4. 액트맵·서브액트맵·확정 장면 카드
5. 레드팀 결정·승인된 변경 기록
6. 비정본 테스트 샘플(NC)
7. 사고성 원고 산출물(`manuscript/ga1/*-v1.md`) — **무권한**

원고 문장은 존재만으로 정본을 만들 수 없다. 매니페스트가 레거시 헤더보다 우선한다(§1). 회차 집필 시 로드할 정본 파일 목록은 `docs/00_project/first-writing-batch-readiness-v1.md` §2 참조.

## 3. 준비 완료 항목 (근거는 readiness audit 참조)

| 영역 | 상태 | 핵심 근거 |
|---|---|---|
| 시점·서술거리·정보 상한 | READY (LOCKED) | gate1 calibration §3·§9, protagonist bible §5, m001-m020 원장 |
| 문체·문장 리듬·대사 비율 | READY (LOCKED) | prose-bible, gate1 §5 (대사 20–30%/행동 45–60%/설명 15–25%/UI <5%) |
| 장면 규격·훅 정책 | READY (LOCKED) | storycraft-bible, prose-bible |
| 전투·함대전 묘사 규칙 | READY (LOCKED, S0=0) | military doctrine bible, weapons-sensors calibration, 손실 회계 3종 |
| 기관정치·기록전쟁 규칙 | READY (설계측) | production standard 회의장면 규칙, gate8 샘플 2종 |
| E1~100 설계 | READY | 장면 카드 16파일 + 운영상태 + E1~20 개발초고(비정본) |
| GA1→GA2 이음매 | READY | causal-transition-matrix, state-checkpoint-matrix, ga2-e101-107 카드와 필드 단위 일치 |
| 복선·사망·영구손실 장부 | READY (S2 각주 3건 필요) | payoff ledger locked, early-clue ledger, named-loss ledger |
| 검수·수정 절차 | READY | revision-harness 12패스 + `manuscript-production-workflow-v1.md`(본 PR 신설) |
| 정본 계층·에라타 전파 | READY (S2 정정 필요) | 에라타 001/003/004 전역 전파 확인; 002는 미전파(§4) |

## 4. 미확정 항목 (게이트와 무관하게 수정해야 할 문서 결함)

전량 `docs/99_quality_control/pre-writing-readiness-audit-v1.md`의 S2 목록. 대표 항목:

1. **GA10 B10-03(E1051~1075)이 `main`에 부재 — PR #88 미병합이 원인.** 설계·레드팀 파일 8종은 브랜치 `agent/ga10-b10-03-e1051-1075-detail`(PR #88, OPEN)에 실존한다. 완료 선언 PR #89만 병합되어 main 기준 실제 완료는 **975/1,000**. E1~100 집필은 막지 않으며, 해결은 PR #88 병합이다(재생산 불필요).
2. 에라타-002(도안 미르→미르 카오)가 GA5 상세설계 10여 파일에 미전파.
3. `first-100-act-map-v2` A2/A3(E6~15) 요약이 실제 장면 카드와 불일치(변경 기록 없음).
4. M-004 결정 장면(E794) vs 판결 연대(E783, errata-004) 충돌 — payoff ledger ±2화 규칙 위반, 미기록.
5. `named-loss ledger` 구식(Lin Osa 표기, 네 원장 구조, 세라트 AI 3명·아르디스 73t 누락).
6. `secondary-mystery ledger` Core relation 열이 구식 M-번호 사용(E2~20 복선 연결 오도 위험).
7. `prose-bible` §2가 POV를 미확정으로 서술(확정 결정 미반영).
8. manifest·deliverables-index·decision-log가 2026-08-04 이후 변경(에라타 3건, 상세설계 완결) 미등재.
9. `continuity-issues.md` 부재(revision-harness Pass 4가 참조).
10. E1~20 초고 잔존 S1 5건(출판 분량 압축 2차 패스 미실행).

## 5. 원고 집필 전 필수 결정 (작가만 결정 가능)

| ID | 결정 | 상태 (2026-08-06 갱신) |
|---|---|---|
| **D1** | 회차당 분량·자수 기준 + 플랫폼/공모전 선정 | **부분 결정.** 작가 판정: "5,500~6,500자 진단 범위보다 **더 길어도 상관없음**" → 분량 상한 유연 확정. 이에 따라 E1~20 "압축 2차 패스"(F-07)는 분량 축소가 아니라 **밀도·반복 정리 패스**로 재정의된다(미래기억 밀도, E14/E18 반복, 청문 장면 길이는 분량과 무관하게 유지되는 감사 지적). 잔여 항목은 집필 비차단으로 하향(S1→S2): 플랫폼/공모전 선정과 자수 산정 기준(공백 포함 여부)은 출판 전까지 확정. `[ASSUMPTION]` 확정 전 기본값 = 공백 포함, 회차 하한 5,500자 |
| **D2** | issue #26(인간/모바일 테스트)의 지위 확정 | **해결 제안서 제출** — `docs/00_project/issue-26-status-resolution-proposal-v1.md`. 제안: 출판 전 하드 블로커로 확정(과거 override 복권이 아닌 신규 작가 판정 방식), 첫 배치 병행 테스트 + 위험 통제 6항. 작가 승인 대기 |
| **D3** | 기존 `manuscript/ga1/` E1~20 비정본 초고 처리: (a) 재집필 (b) 개정 기반 승격 | **작가 지시로 보류 중** (2026-08-06 "아직 기다려"). 결정 전까지 기존 v1 파일은 비정본 유지, 접근 금지 아님·수정 금지 |
| **D4** | GA10 B10-03 처리: **PR #88 병합 승인** 여부. 브랜치가 main 대비 behind 1이므로 병합 전 충돌·정합(특히 progress-status-975 파일과 PR #89의 status-1000 파일 공존) 확인 필요. | 병합 승인 — 설계·레드팀 완료본이 이미 존재하므로 병합만으로 1,000/1,000이 실제가 됨. 집필 개시와는 독립 |

## 6. 권장 첫 집필 배치

- **범위: E1~5 (1배치 5회차)** — D3 결정에 따라 재집필 또는 개정+압축.
- 이유: (1) 장면 카드·초고·감사 기록이 가장 두터운 구간, (2) 공모전 대응상 최우선 구간, (3) E1~5 자체 감사가 이미 압축 대상(S1)을 특정해 둠.
- 상세 준비 상태는 `docs/00_project/first-writing-batch-readiness-v1.md`.

## 7. 게이트 개방 조건

게이트는 다음이 모두 갖춰졌을 때만 열린다:

1. D1~D3 결정이 기록됨(D4는 독립).
2. §4의 문서 결함 중 **첫 배치 구간(E1~20)에 직접 닿는 항목**(3, 6, 7, 9, 10번)의 정정 계획이 첫 배치 작업 목록에 편성됨 — 사전 완료가 아니라 편성이면 충분.
3. 작가가 아래 문장을 명시적으로 기록:

> `Pre-Writing Gate를 OPEN한다. 권장된 첫 집필 배치를 시작해.`

이 선언 전까지 AI는 감사·교정·집필준비 문서만 작성하며, 어떤 회차 본문도 쓰지 않는다. AI는 게이트를 대리 개방하지 않는다.

## 8. 최종 판정

> **CLOSED 유지.**
>
> 설계 준비도는 집필 가능 수준(S0=0, 집필 차단 S1은 전량 "작가 결정 대기" 성격)이다. 그러나 게이트 개방의 마지막 요건이 문서가 아니라 작가의 결정(D1~D3)과 명시 선언이므로, 본 리뷰는 게이트를 열지 않고 결정 패키지를 작가에게 회부한다.
>
> D1~D3이 기록되는 즉시 OPEN 권고로 전환 가능하다.
