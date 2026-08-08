# Manuscript Production Workflow v1

Status: REVIEW — ACTIVATES ONLY AFTER PRE-WRITING GATE OPEN
Owner Agents: A00 PM / A11 Prose & Serialization / O01 Canon / O02 Gates / X04 Continuity
Last Reviewed: 2026-08-06
Depends On: [[revision-harness]], [[prose-bible]], [[storycraft-bible]], [[prewriting-gate]], [[design-only-scope-restoration-2026-08-03]]
Used By: 모든 정본 원고 배치 생산
Open Risks: 이 문서 자체는 집필을 승인하지 않는다. Pre-Writing Gate가 OPEN되기 전에는 어떤 단계도 실행되지 않는다.

## 0. 활성화 조건

이 워크플로는 다음 문장이 사용자에 의해 명시적으로 기록된 뒤에만 활성화된다.

> `Pre-Writing Gate를 OPEN한다. 권장된 첫 집필 배치를 시작해.`

그 전까지 이 문서는 절차 정의일 뿐이며, 어떤 원고 본문도 생산하지 않는다.
[[design-only-scope-restoration-2026-08-03]]의 design-only 판정이 이 문서보다 우선한다.

## 1. 역할

- **작가(사용자)**: 유일한 최종 승인자. 게이트 개방, 배치 승인, 회차 승인, 공개 승인은 모두 작가만 할 수 있다.
- **AI 오케스트라**: 초안 작성, 자체감사, 설정 대조, 문체감사, 훅 감사, 수정안 생성까지만 수행한다. 승인·공개·정본 승격을 스스로 선언하지 않는다.

## 2. 브랜치·파일 규약

- 배치당 1개 브랜치: `manuscript/ga1-e{시작}-{끝}-draft-v{n}` 형식.
- 원고 파일 위치: `manuscript/ga1/{회차번호 3자리}-{회차제목}-v{n}.md`.
- 기존 `manuscript/ga1/*-v1.md` 20편은 2026-08-03 판정에 따라 **비정본·범위외 산출물**이다. 새 정본 초안의 바탕으로 사용하지 않는다(참조 수준 활용 여부는 작가 결정 사항 — [[pre-writing-gate-review-v1]] 결정 D4 참조).
- 모든 원고 파일 머리에 상태 헤더를 둔다:

```markdown
Status: DRAFT | REVISED | AUTHOR-APPROVED
Episode: E{번호}
Source Cards: {장면 카드 파일 경로}
Canon Check: PENDING | PASS | FAIL
Publication: NOT AUTHORIZED
```

- `Publication: NOT AUTHORIZED`는 작가가 공개를 별도로 승인할 때까지 모든 파일에서 유지된다.

## 3. 회차 생산 파이프라인

각 회차는 다음 8단계를 순서대로 통과한다. 앞 단계가 FAIL이면 뒤 단계로 넘어가지 않는다
([[revision-harness]]의 Pass 순서를 따른다).

### 3.1 원고 작성

- 입력: 해당 회차 장면 카드, 운영 상태 시트, 인물 음성 잠금, 문체 캘리브레이션 파일.
- 규칙: 장면 카드의 사건·순서·상태 변화를 벗어나는 새 사실(새 인물, 새 죽음, 새 기술, 새 권한)을 만들지 않는다. 필요 시 작성 중단 후 변경 제안서를 먼저 낸다.
- 한 장면 = 한 초점 인물. Rian 근접 3인칭 기본.

### 3.2 자체감사 (구조·인과·동기)

- revision-harness Pass 1(장르 약속)·Pass 2(구조·인과)·Pass 3(인물 동기)을 실행한다.
- 출력: 삭제/병합 후보 장면, 원인·결과 누락, 잘못 배치된 정보 목록.

### 3.3 설정 대조 (정본 정합)

- revision-harness Pass 4(세계·연속성)·Pass 5(미스터리·회수)를 실행하되, 다음을 추가로 강제 대조한다:
  - [[named-loss-and-irreversible-transformation-ledger-v1]] — 영구손실 부활 금지.
  - [[ga1-10-state-checkpoint-matrix-v1]] — 해당 회차 시점의 권한·자산·인물 상태.
  - [[m001-m020-early-clue-episode-ledger-v1]] — 단서 노출 상한(정보 상한) 준수.
  - [[master-series-chronology-v1]] — 날짜·나이·경과시간.
  - errata 001~004 — 구버전 수치 사용 금지.
- 모순 발견 시 [[continuity-issues]]에 등록하고 S0/S1이면 해당 회차를 BLOCKED 처리한다. 해당 파일은 현재 저장소에 없으므로(readiness audit F-15) 첫 배치 착수 시 빈 등록부로 생성한다. revision-harness의 S0~S4 등급과 게이트 체계의 S0~S3 등급 대응(S4 = 게이트 체계의 기록성 노트)도 그 파일 머리에 명기한다.

### 3.4 문체감사

- revision-harness Pass 6(전투 논리)·Pass 7(묘사)·Pass 8(대사·음성)·Pass 9(문장 리듬)를 실행한다.
- 기준: [[prose-bible]], [[gate1-korean-webnovel-pov-prose-calibration-v1]], [[core-canonical-names-and-voice-lock-v1]].
- 단문 남발 금지, 중문장 기본 호흡, 기술 묘사의 기능성(행동·위험·사회·심리) 확인.

### 3.5 회차 훅 감사

- revision-harness Pass 10(연재 리텐션)·Pass 11(유사성)을 실행한다.
- 각 회차는 구체적 다음 문제로 끝나야 하며, 직전 회차 훅을 즉시 회수해야 한다.
- 훅 유형 반복표를 배치 단위로 유지한다.

### 3.6 작가 승인

- 회차별 감사 리포트(revision-harness §4 형식)와 함께 원고를 작가에게 제출한다.
- 작가 판정: `승인` / `수정 지시` / `반려`.
- AI는 작가 판정을 대행하거나 생략하지 않는다. 응답이 없으면 해당 회차는 DRAFT로 대기한다.

### 3.7 수정

- 작가 지시 반영 후 3.3(설정 대조)과 3.4(문체감사)를 재실행한다.
- No-Silent-Rewrite: 사건·설정·인물 의도를 조용히 바꾸지 않는다. 구조 변경은 문제와 대안을 먼저 제시한다.
- 강점으로 판정된 문장 효과는 수정 과정에서 보존한다.

### 3.8 정본 반영

- 배치 병합 조건(proxy-signoff §5 병합 규칙 계승):
  1. 배치 내 모든 회차 파일 존재;
  2. 연속성 감사 PASS;
  3. 음성 감사 PASS;
  4. S0 모순 0;
  5. 회차별 수정 노트 존재;
  6. `Publication: NOT AUTHORIZED` 유지;
  7. **작가 승인 기록 존재**.
- 병합 후 갱신 의무:
  - 원고에서 확정된 상태 변화 → 해당 운영 상태 시트에 반영;
  - 새로 심은 단서 → payoff ledger에 등록;
  - 설정 변경 발생 시 → [[decision-log]] + 영향 문서 갱신.
- 원고 문장은 존재만으로 정본이 되지 않는다. 설정 충돌 시 우선순위는 [[design-only-scope-restoration-2026-08-03]] §3의 정본 계층을 따른다(원고는 최하위).

## 4. 치명도 및 중지 규칙

- 치명도는 revision-harness §3의 S0~S4를 사용한다.
- S0 발견 시: 배치 전체 중지, 작가 보고, 설계 문서 수정 제안서 우선.
- S1 발견 시: 해당 회차 공개 불가, 배치 내 다른 회차는 진행 가능.
- 게이트 회귀 조건: 정본 설계 문서와 원고의 충돌이 반복적으로 S1 이상을 생성하면 집필을 중단하고 Pre-Writing Gate Review를 재실행한다.

## 5. 배치 리듬

- 1배치 = 5회차 (E1~5부터 시작, [[first-writing-batch-readiness-v1]] 참조).
- 배치 완료 후 다음 배치 시작 전에 배치 회고를 수행한다: 훅 반복, 음성 이탈, 분량 편차, 감사 지적 반복 여부.
- 액트 종료 시 revision-harness §6 액트 검토, 대액트 2개마다 §7 시리즈 검토를 실행한다.
