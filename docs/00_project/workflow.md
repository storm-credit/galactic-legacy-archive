# End-to-End Workflow & Harness

Status: CANON
Owner Agent: A00 Novel PM Orchestrator
Last Reviewed: 2026-08-03
Depends On: `CLAUDE.md`, `orchestra.md`
Used By: All phases
Open Risks: Over-planning, analysis paralysis, document drift

## 1. Workflow Principle

이 프로젝트는 `설계 → 교차검증 → 스트레스 테스트 → 정본화 → 집필` 순서로 진행한다. 문서 수를 늘리는 것이 목적이 아니라, 실제 집필 시 판단을 반복하지 않아도 될 만큼 연결된 설계 체계를 만드는 것이 목적이다.

## 2. Phase Gates

### Gate 0 — Intent Lock

필수:
- 작품의 핵심 감정
- 주 독자층
- 장르 약속
- 금지 요소
- 공모전 목표
- 예상 분량과 연재 플랫폼 가정

출구 조건:
- 한 줄 소개, 5문장 소개, 1페이지 소개가 서로 모순되지 않는다.

### Gate 1 — Reference Deconstruction

필수:
- 한국 웹소설 최소 10편
- 해외 스페이스 오페라·메카·군사 SF 최소 10편
- 작품별 훅, 보상 주기, 전투 방식, 장면 길이, 수집 구조, 장기화 방식
- 닮으면 위험한 요소와 차별화 가능 요소

출구 조건:
- 참고작 문장을 복제하지 않고 구조적 효과만 설명할 수 있다.

### Gate 2 — Core Concept Lock

필수:
- 충분히 다른 디자인 시안 4개
- 평가 기준: 독창성, 대중성, 초반 흡입력, 1000화 확장성, 수집 재미, 정치·함대전 확장성
- 정본안과 폐기안의 이유

출구 조건:
- ‘왜 회귀인가’, ‘왜 제독인가’, ‘왜 다시 에이스로 시작하는가’, ‘왜 수집하는가’에 각각 한 문장으로 답한다.

### Gate 3 — World Rule Lock

필수:
- 이동, 통신, 에너지, AI, 메카, 함선, 생명유지, 사회, 경제, 법, 군사 규칙
- 각 기술의 비용·한계·악용 가능성

출구 조건:
- 주요 전쟁과 정치 구조가 기술 규칙에서 자연스럽게 발생한다.

### Gate 4 — Collection System Lock

필수:
- 8대 수집 범주
- 획득·해금·조합·상실·복원 규칙
- 세트, 실루엣, 도감 공개, 희귀도
- 사람의 자율성 보장 규칙

출구 조건:
- 수집품마다 최소 두 가지 이상의 서사 기능이 있다.

### Gate 5 — Character/Faction Lock

필수:
- 주인공의 전생과 현생 결핍
- 주요 라이벌 3명 이상
- 핵심 영웅군과 적대 세력
- 세력별 목표, 자원, 약점, 내부 분열

출구 조건:
- 주인공이 없어도 각 세력이 움직일 이유가 있다.

### Gate 6 — Macroplot Lock

필수:
- 결말 역산
- 8~10개 대액트
- 대액트별 3~6개 액트
- 액트별 2~5개 서브액트
- 각 층위의 목표·갈등·반전·보상·대가·다음 질문

출구 조건:
- 대액트 종료가 다음 대액트의 원인이 된다.
- 후반 확장이 단순한 적 체급 상승에 의존하지 않는다.

### Gate 7 — Payoff Lock

필수:
- 핵심 맥거핀
- 회귀의 진실
- 은하유산록의 정체
- 주인공 패배의 진짜 원인
- 결말에서 회수할 약속

출구 조건:
- 모든 대형 반전이 사전에 공정하게 단서화된다.

### Gate 8 — Writing Harness Lock

필수:
- 시점, 문장 호흡, 문단, 정보량, 전투, 풍경, 대사, 회차 엔딩 규칙
- 모바일 가독성 기준
- 금지 문체와 반복 표현 목록
- 장면 카드와 회차 카드 템플릿

출구 조건:
- 서로 다른 작성자가 같은 규칙으로 유사한 품질의 초안을 만들 수 있다.

### Gate 9 — Stress Test

필수:
- 모순 테스트
- 독자 이탈 테스트
- 유사작 비교 테스트
- 전력 인플레이션 테스트
- 1000화 반복 피로 테스트
- 결말 회수 테스트

출구 조건:
- 치명적 위험 0개, 중대 위험은 완화책과 담당자가 지정되어 있다.

### Gate 10 — Pre-Writing Gate

`docs/99_quality_control/prewriting-gate.md`의 모든 필수 항목이 PASS일 때만 본편 집필 브랜치를 생성한다.

## 3. Work Packet Format

모든 작업은 다음 형식으로 시작한다.

```markdown
# Work Packet
Goal:
Why Now:
Inputs:
Deliverables:
Owner Agent:
Required Reviewers:
Constraints:
Success Conditions:
Stop Conditions:
Downstream Documents:
```

## 4. Standard Agent Loop

1. 컨텍스트 덤핑: 관련 문서와 미결정 사항을 모은다.
2. 질문 생성: 결과를 크게 바꾸는 질문만 추린다.
3. 초안: 담당 에이전트가 산출한다.
4. 자기 비판: 가정, 약점, 누락, 편의주의를 표기한다.
5. 교차검토: 필수 리뷰어가 공격한다.
6. 수정: 비판을 반영하되 새 모순을 검사한다.
7. 정본화: A15가 연결과 상태를 확인한다.
8. PM 승인: A00이 CANON 또는 REWORK를 지정한다.
9. 다음 단계: 의존성이 충족된 작업을 자동 선택한다.

## 5. Change & Deviation Protocol

원래 계획과 달라지면 반드시 기록한다.

```markdown
Date:
Changed Item:
Original Plan:
Observed Problem:
Root Cause:
Alternatives Considered:
Decision:
Why This Decision:
Affected Documents:
New Risks:
Rollback Option:
```

계획 변경은 실패가 아니다. 기록 없는 변경이 실패다.

## 6. Anti-Analysis-Paralysis Rule

- 핵심 선택이 아닌 세부 명칭은 임시명으로 진행한다.
- 3회 이상 같은 논점이 반복되면 A00이 선택 기준을 세워 강제 결정한다.
- ‘완벽한 과학’보다 작품의 일관된 규칙을 우선한다.
- 설정이 플롯에 사용되지 않으면 보류함으로 이동한다.
- 1000화 전체를 회차 단위로 미리 쓰지 않는다. 대액트와 액트는 상세 설계하고, 서브액트는 가까운 구간부터 점진적으로 정밀화한다.

## 7. Automatic Next-Task Selection

A00은 다음 순서로 다음 작업을 고른다.

1. 현재 Gate를 막는 필수 문서
2. 다른 문서의 의존성이 가장 많은 결정
3. 가장 큰 치명적 위험
4. 공모전 초반 20화에 직접 영향을 주는 설계
5. 장기 결말과 회수에 영향을 주는 설계
6. 명칭·장식·부가 설정

## 8. Repository State Labels

- `DRAFT`: 담당 에이전트 초안
- `REVIEW`: 교차검토 중
- `REWORK`: 중대 문제로 재작업
- `CANON`: 현재 정본
- `DEPRECATED`: 폐기됐지만 변경 이력 보존
- `PARKED`: 플롯 사용처가 없어 보류

## 9. Completion Definition

‘끝까지 자동 진행’의 완료는 본편 1000화를 자동 생성한다는 뜻이 아니다. 다음 상태를 의미한다.

- 집필 전 모든 필수 설계 Gate 완료
- 첫 공모전 제출 구간을 쓸 수 있는 세부 비트 설계 완료
- 전체 대서사와 결말 회수 구조 완료
- 설정집과 집필 하네스가 CANON
- 미해결 위험과 가정이 명시됨
- 본편을 쓰기 시작해도 대형 설정을 즉흥적으로 다시 만들 필요가 없음
