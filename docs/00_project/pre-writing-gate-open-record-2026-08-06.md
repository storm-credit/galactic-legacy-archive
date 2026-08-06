# Pre-Writing Gate Open Record — 2026-08-06

Status: CANON PROJECT CONTROL — GATE DECISION RECORD
Owner Agents: A00 PM / O01 Canon / O02 Gates
Last Reviewed: 2026-08-06
Depends On: `docs/00_project/pre-writing-gate-review-v1.md`, `docs/99_quality_control/pre-writing-readiness-audit-v1.md`, `docs/00_project/issue-26-status-resolution-proposal-v1.md`
Used By: 첫 집필 배치(E1~5) 및 이후 모든 원고 생산
Open Risks: 출판·공개·유료연재는 여전히 차단 상태다. 본 기록은 초고 생산만 개방한다.

## 1. 작가 선언 (2026-08-06)

작가가 게이트 리뷰 v1의 결정 패키지(D1~D4)에 답하고 다음 개방 선언을 기록했다:

> **"Pre-Writing Gate를 OPEN한다. 권장된 첫 집필 배치를 시작해."**

## 2. 결정 기록

| ID | 결정 | 내용 |
|---|---|---|
| D1 | 회차 분량 | 5,500~6,500자 진단 범위보다 **더 길어도 무방**(상한 유연). 압축 패스는 밀도·반복 정리로 재정의. 플랫폼/공모전·공백 기준은 출판 전 확정(`[ASSUMPTION]` 공백 포함·하한 5,500자) |
| D2 | issue #26 지위 | **승인** — `issue-26-status-resolution-proposal-v1.md` 판정 발효. issue #26은 출판 전(pre-publication) 하드 블로커. 집필은 진행, 인간 테스트는 첫 배치와 병행, 위험 통제 6항 전부 유지 |
| D3 | E1~20 구초안 처리 | **개정 기반 사용** — `manuscript/ga1/*-v1.md` 20편을 개정 출발점으로 승격(v2 생산). 단 v1의 'Locked Development Outcomes'는 정본 근거로 인용 불가 유지 — 사실은 장면 카드·바이블에서 재확인 |
| D4 | 병합 | PR #90(게이트 리뷰·워크플로·낭독 규격), PR #88(GA10 E1051~1075 설계) 모두 병합 완료 → 설계 1,000/1,000 실제화 |

## 3. 게이트 사인오프 (prewriting-gate.md §13 양식)

```markdown
Gate Date: 2026-08-06
Overall Status: CONDITIONAL PASS
A00 PM Verdict: PASS for first-draft production; publication remains blocked
A15/O01 Canon Verdict: PASS — canon hierarchy intact, S0=0, locks verified
A16 Red Team Verdict: PASS with S2 patch list assigned to batch 1 (F-05/07/08/12/13/14/15)
A17 Contest/Retention Verdict: AI-proxy PASS; human test = pre-publication blocker per D2
S0 Count: 0
S1 Count: 0 (F-01 부분해소로 S2 하향, F-02 D2로 해소)
Known Assumptions: 자수 기준 공백 포함·하한 5,500자(플랫폼 확정 전 기본값)
First Draft Branch Authorized: YES
Authorized Scope: Batch 1 = Episodes 1–5 (revision of v1 drafts to v2); subsequent batches per first-writing-batch-readiness-v1.md
Publication Authorized: NO
Next Review Event: Batch 1 author approval + human/mobile test results (issue #26)
```

## 4. 발효 내용

1. Pre-Writing Gate: **OPEN (초고 생산 한정)**. `manuscript-production-workflow-v1.md`의 8단계 파이프라인 활성화.
2. 출판·공개·유료연재: **차단 유지** — 모든 원고 파일 `Publication: NOT AUTHORIZED` 헤더 의무.
3. issue #26: OPEN 유지, 첫 배치 병행 실행 대상(최소 5인, 절반 이상 폰 화면, 시료 = 개정 E1~2 + white-dock 샘플).
4. 첫 배치 작업 목록에 편성된 S2 패치: F-05(액트맵 요약 정정 기록), F-07(밀도·반복 정리 패스), F-08(prose-bible §2 — 본 기록과 함께 패치됨), F-12(손실 원장 부록), F-13(M-004 각주), F-14(SM 번호 리매핑), F-15(continuity-issues.md — 본 기록과 함께 생성됨).
5. `design-only-scope-restoration-2026-08-03.md`의 design-only 판정은 본 기록으로 **명시적으로 대체(supersede)**된다 — 단, 같은 문서의 §3 정본 우선순위 사다리와 "원고 문장은 정본을 만들 수 없다" 규칙은 계속 유효하다.

## 5. 회귀 조건

다음 중 하나 발생 시 게이트를 재폐쇄하고 리뷰를 재실행한다:

- 정본 설계와 원고 충돌이 반복적으로 S1 이상을 생성
- 인간 테스트에서 동일 항목 2회 이상 임계 미달
- 작가의 명시적 재폐쇄 지시
