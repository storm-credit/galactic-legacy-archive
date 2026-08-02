# Story Architecture Rules

Status: CANON
Owner Agent: A09 Long-Form Story Architect
Last Reviewed: 2026-08-03
Depends On: Core concept, world rules, character bible
Used By: Macroplot, act maps, episode design, payoff ledger
Open Risks: Excessive hierarchy, repetitive escalation, overplanning distant episodes

## 1. Hierarchy

이 작품의 구조는 다음처럼 중첩된다.

```text
SERIES
└─ SAGA / 대서사
   └─ GRAND ACT / 대액트
      └─ ACT / 액트
         └─ SUBACT / 서브액트
            └─ EPISODE BLOCK / 회차 묶음
               └─ EPISODE / 개별 회차
                  └─ SCENE / 장면
```

큰 액트 안에 여러 작은 액트가 들어가는 방식이 맞다. 단, 작은 액트를 단순히 이어 붙이면 안 된다. 각 층위는 상위 층위의 질문에 부분적으로 답하면서 새로운 문제를 발생시켜야 한다.

## 2. Layer Definitions

### SERIES

작품 전체의 질문과 최종 변화.

- 질문 예시: 사람과 문명을 구한다는 명분으로 그들을 수집·배치할 권리가 주인공에게 있는가?
- 시작 상태: 혼자 싸우다 모든 것을 잃은 패전 제독
- 종료 상태: 타인의 선택을 통제하지 않고도 함께 싸울 질서를 만드는 지도자

### SAGA / 대서사

300~500화 이상을 묶을 수 있는 시대적 국면. 필요할 때만 사용한다.

예시:
- 교도제국 붕괴기
- 제국 계승전쟁기
- 은하 문명전쟁기

### GRAND ACT / 대액트

약 80~150화. 독립된 장편 한 권처럼 시작·중간·절정·후일담을 갖는다.

필수 항목:
- 주 무대
- 주인공의 사회적 위치
- 핵심 수집 범주
- 주요 적대 세력
- 액트 질문
- 중간 반전
- 최종 선택
- 획득 보상
- 지불한 대가
- 다음 대액트를 발생시키는 결과

대액트는 ‘더 강한 적’이 아니라 **주인공의 책임 범위가 커지는 변화**로 구분한다.

### ACT / 액트

약 15~40화. 하나의 구체적 목표와 장애를 해결한다.

예시:
- 폐기 훈련기 탈취
- 미래의 학살자 영입 여부
- 교도학원 내부 쿠데타
- 첫 우주선 확보

필수 구조:
1. 목표 설정
2. 접근 계획
3. 예상 밖 저항
4. 비용 증가
5. 선택 또는 반전
6. 결과와 후폭풍

### SUBACT / 서브액트

약 4~12화. 하나의 관계 변화, 작전 단계, 미스터리 질문, 수집품 획득 과정을 담당한다.

서브액트는 최소 하나를 변화시켜야 한다.
- 정보
- 관계
- 권력
- 자원
- 위치
- 위험
- 주인공의 믿음

### EPISODE BLOCK / 회차 묶음

2~5화. 모바일 독자가 짧은 기간에 완결감을 느끼는 최소 단위.

예시:
- 탐색 → 잠입 → 발견 → 탈출
- 도발 → 결투 → 패배 위기 → 역전
- 협상 → 조건 → 배신 → 재협상

### EPISODE / 회차

하나의 중심 질문을 제시하고 최소 하나의 상태를 바꾼다.

회차 종료 시 다음 중 하나를 남긴다.
- 새로운 위험
- 예상 밖 정체
- 선택 강요
- 보상 직전
- 관계 역전
- 기존 정보의 재해석

### SCENE / 장면

장면은 목적 없이 존재하지 않는다.

필수:
- 관점 인물의 즉시 목표
- 방해
- 전술 또는 감정적 선택
- 장면 전후 상태 변화
- 독자가 새로 얻는 것

## 3. Causal Chain Rule

각 층위는 다음 인과를 유지한다.

```text
이전 선택의 결과
→ 새로운 문제
→ 대응 계획
→ 예상 밖 저항
→ 더 비싼 선택
→ 승리 또는 실패
→ 되돌릴 수 없는 변화
→ 다음 층위의 원인
```

‘그리고 나서’만으로 이어지는 사건은 재설계한다. ‘그러므로’ 또는 ‘하지만’으로 연결되어야 한다.

## 4. Grand Act Card

```markdown
# Grand Act [번호] — [가제]
Status:
Episode Range:
Primary Arena:
Protagonist Rank/Role:
Core Reader Promise:
Primary Collection Category:
Opening Imbalance:
Central Question:
Primary Antagonist:
Acts:
Midpoint Reversal:
Darkest Cost:
Climax Choice:
Victory:
Price Paid:
Permanent Change:
Next Grand Act Trigger:
Foreshadowing Planted:
Payoffs Delivered:
Continuity Risks:
```

## 5. Act Card

```markdown
# Act [번호] — [가제]
Goal:
Deadline:
Opposition:
Resource Constraint:
Relationship Conflict:
Mystery Question:
Collection Reward:
False Victory:
Reversal:
Final Choice:
Outcome:
Cost:
Next Problem:
```

## 6. Subact Card

```markdown
# Subact [번호]
Episode Range:
Immediate Objective:
Location:
POV:
Entry State:
Key Beats:
Required Setup:
Payoff:
Character Shift:
Resource Shift:
Exit Hook:
```

## 7. Escalation Dimensions

장기 연재에서 모든 것을 화력으로만 키우지 않는다. 대액트마다 다음 축 가운데 2~4개만 주로 상승시킨다.

- 개인적 위험
- 지켜야 할 사람 수
- 정치적 책임
- 정보의 불확실성
- 적의 정당성
- 선택의 윤리적 비용
- 작전 공간의 규모
- 수집 대상의 범위
- 시간 압박
- 동료 간 불신
- 승리 후 후폭풍

## 8. Collection Integration Rule

수집 요소는 플롯과 분리된 보상 상자가 아니다.

모든 주요 수집 대상은 최소 다음 중 두 가지를 담당한다.
- 전투 방식 변화
- 인물 관계 변화
- 미스터리 단서
- 세력 균형 변화
- 새로운 지역 접근
- 주인공의 윤리적 선택
- 과거 역사 재해석
- 다음 액트의 원인

## 9. MacGuffin and Ending Recovery

맥거핀은 ‘중요하다고 말하는 물건’이 아니라 인물들이 서로 다른 이유로 추구하는 대상이다.

각 핵심 맥거핀은 다음 단계를 가진다.

1. 존재 또는 빈자리 암시
2. 잘못된 기능 설명
3. 최초 접촉
4. 소유권 갈등
5. 부분 기능 해방
6. 대가 또는 위험 공개
7. 역사적 의미 재해석
8. 주인공의 최종 사용 또는 폐기 선택
9. 결말에 남긴 변화

결말 회수는 최종 100화에 몰아서 처리하지 않는다. 대액트마다 부분 회수와 의미 갱신이 있어야 한다.

## 10. 1000-Episode Planning Resolution

- 전체 1000화: 대액트 수준으로 확정
- 다음 300화: 액트 수준으로 확정
- 다음 100화: 서브액트 수준으로 확정
- 다음 20화: 회차 비트 수준으로 확정
- 실제 집필 직전 5화: 장면 카드 수준으로 확정

먼 미래 회차를 지나치게 세밀하게 고정하지 않는다. 대신 결말, 핵심 회수, 대액트 전환점은 바꾸기 어렵게 정본화한다.

## 11. Failure Conditions

다음이면 구조를 재작업한다.

- 액트의 승패가 다음 액트에 아무 영향이 없다.
- 주인공이 모든 문제를 직접 해결한다.
- 적대자의 계획이 주인공을 기다리기만 한다.
- 새 수집품이 곧바로 이전 수집품을 무의미하게 만든다.
- 같은 유형의 대회·시험·공성전이 이름만 바뀌어 반복된다.
- 중간 목표가 결말과 연결되지 않는다.
- 회귀 지식이 언제나 정확하고 무제한이다.
- 대액트 종료 후 주인공의 책임과 세계 상태가 그대로다.
