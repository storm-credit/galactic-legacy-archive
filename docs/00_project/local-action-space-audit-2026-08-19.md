# Local Action Space Audit — Minimum Action Agent OS 적용

Status: PROJECT CONTROL — 작업 방법론 계층 (도메인 정본 아님)
Owner Agent: A00 Novel PM Orchestrator
Last Reviewed: 2026-08-19
Depends On: [[specialist-routing-index]], [[orchestra]], [[specialist-roster]], [[agent-orchestra-registry-v1]], [[orchestra-v2-activation-rules]], [[agent-execution-contract-and-veto-policy-v1]], [[CLAUDE]]
Used By: 세션 착수 시 역할 라우팅, 신규 에이전트·스킬 추가 판단
Publication: NOT AUTHORIZED
Open Risks: 이 문서는 탐색·작업방법만 제어한다. Canon/Spec/Freeze, 거부권, 게이트, C1–C11은 기존 프로젝트 문서가 계속 보유한다.

---

## 1. 범위와 정본 경계

`storm-credit/minimum-action-agent-os`를 **작업 방법론으로만** 적용한다.

변경하지 않는 것:
- Canon / Spec / Freeze;
- 원고;
- 프로젝트 코드·연구설계;
- 고정 전문역할 명부;
- 기존 하네스와 C1–C11 검증기;
- 거부권과 정본 승격 권한.

변경 가능한 것은 오직 **reasoning node가 한 번에 직접 선택하는 행동의 노출 방식**이다.

프로젝트 정본 우선순위:
1. 작가의 현재 명시 지시;
2. 이 저장소의 Canon / Spec / Freeze / current status / decision records;
3. Minimum Action Agent OS 작업방법.

OS가 도메인 내용을 덮어쓰는 것은 금지한다.

---

## 2. 감사 입력 복구

이번 감사는 다음 현재 구조를 기준으로 한다.

- root `CLAUDE.md`;
- repository root와 `.claude/` 존재 여부;
- [[agent-orchestra-registry-v1]] — 고정 전문역할 61개;
- [[specialist-routing-index]] — 전 프로젝트 작업에 쓰이는 29행 상세 라우팅면;
- [[orchestra]] §4 — 레거시 10행 라우팅면;
- [[specialist-roster]] — 부서/역할 정의;
- [[orchestra-v2-activation-rules]];
- [[agent-execution-contract-and-veto-policy-v1]];
- 프로젝트 Canon / Freeze / gate / current-status / [[decision-log]] 계층;
- `CLAUDE.md` §6·§13·§15의 Harness / 독립감사 / C1–C11;
- `tools/` 검증 스크립트와 `validate_canon.py`;
- `storm-credit/minimum-action-agent-os`의 `AGENT_OS_SPEC.md`, `rules/local-action-space.md`, `adapters/claude-code.md`.

`.claude/`에 프로젝트 전용 Agent/Skill/MCP를 vendoring하지 않는다. 공통 OS는 user-scope plugin으로 사용한다.

---

## 3. 계산 규칙

한 reasoning node에서 모델이 **peer choice로 직접 선택할 수 있는 것**만 센다.

포함:
- Agent;
- Tool;
- Skill;
- MCP action;
- 기타 callable / router branch.

제외:
- 이미 선택된 라우팅 행이 자동으로 호출하는 필수 검토자 fan-out;
- 정해진 순서대로 전부 수행하는 단계;
- 내부 구현 세부;
- 현재 단계에서 아직 노출되지 않는 phase-gated action.

기본 목표:

> **Local Action Space <= 5**

5를 넘으면 순서대로 검토한다.
1. 불필요 Tool/action 제거;
2. 하나의 Skill/workflow로 묶기;
3. 역할/책임 분리;
4. Router 계층화;
5. 그래도 필요할 때만 예외와 tradeoff 기록.

전체 Agent 수는 제한하지 않는다.

---

## 4. Local Action Space Audit — 엄격 재감사

### 4.1 주요 reasoning node

| Node | 직접 보이는 Agent | 직접 보이는 Tool | 직접 보이는 Skill | MCP | 기타 callable | 총 선택지 | 판정 |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 착수 전 OS preflight | 0 | 0 | 1 (`os-preflight`) | 0 | 0 | **1** | **PASS** |
| R0 도메인 최상위 라우터 | 0 | 0 | 0 | 0 | 5개 밴드 | **5** | **PASS** |
| R1 B1 세계 규칙 | 0 | 0 | 0 | 0 | 4개 산출물 행 | **4** | **PASS** |
| R2 B2 사회·제도 | 0 | 0 | 0 | 0 | 2개 하위 라우터 | **2** | **PASS** |
| R2a 권력·세력 | 0 | 0 | 0 | 0 | 4개 산출물 행 | **4** | **PASS** |
| R2b 제도·편제 | 0 | 0 | 0 | 0 | 2개 산출물 행 | **2** | **PASS** |
| R3 B3 인물·서사 | 0 | 0 | 0 | 0 | 2개 하위 라우터 | **2** | **PASS** |
| R3a 구조·회수 | 0 | 0 | 0 | 0 | 5개 산출물 행 | **5** | **PASS** |
| R3b 인물 장면 | 0 | 0 | 0 | 0 | 3개 산출물 행 | **3** | **PASS** |
| R4 B4 물성·작전 | 0 | 0 | 0 | 0 | 2개 하위 라우터 | **2** | **PASS** |
| R4a 전투 실행 | 0 | 0 | 0 | 0 | 3개 산출물 행 | **3** | **PASS** |
| R4b 하드웨어 설계 | 0 | 0 | 0 | 0 | 3개 산출물 행 | **3** | **PASS** |
| R5 B5 수집·감사 | 0 | 0 | 0 | 0 | 5개 산출물 행 | **5** | **PASS** |
| E0 독립 평가 단계 | 1 (`independent-critic`) | 0 | 0 | 0 | 0 | **1** | **PASS** |
| S0 상태 변경 후 | 0 | 0 | 1 (`os-state`) | 0 | 0 | **1** | **PASS** |

### 4.2 자동 fan-out / 고정순서 노드

아래는 숫자가 많아 보여도 `N택1`이 아니라 **선택 후 자동 활성화되거나 전부 실행되는 집합**이다.

| Node | 직접 선택 가능한 Agent | Tool | Skill | 기타 callable | 직접 선택 합계 | 판정 |
|---|---:|---:|---:|---:|---:|---|
| 등록부 활성화 규칙의 필수 전문가 집합 | 0 | 0 | 0 | 자동 fan-out | 0 | **PASS** |
| 패널 내부 6–10 전문가 | 0 | 0 | 0 | 라우팅 행이 이미 결정 | 0 | **PASS** |
| 등록부 §10 고정 실행 10단계 | 0 | 0 | 0 | 고정 순서 | 0 | **PASS** |
| 수집 오케스트라 C1–C8 | 0 | 0 | 0 | 전 범위 fan-out | 0 | **PASS** |
| 기체 디자인 오케스트라 M01–M08 | 0 | 0 | 0 | 전 범위 fan-out | 0 | **PASS** |
| 행별 필수 검토자 6–11+ | 0 | 0 | 0 | 전원 호출 | 0 | **PASS** |
| 기본 거부권 8분야 | 0 | 0 | 0 | 조건 충족 시 자동 발동 | 0 | **PASS** |

규칙:
- 위 집합을 수동 `택1` 메뉴로 다시 노출하면 즉시 REVIEW로 되돌린다.
- 팬아웃 수 자체는 Local Action Space가 아니다.

### 4.3 Host runtime built-ins

Claude Code 자체의 Read/Edit/Bash 등 **호스트 내장 Tool 전체 개수는 이 저장소가 선언하거나 제한할 수 없다.** 따라서 저장소 수준 감사와 런타임 수준 감사를 분리한다.

- repository-declared / plugin-declared routing: 이 문서가 관리;
- host-runtime built-ins: 실제 실행 세션의 `os-preflight`에서 필요 도구만 사용하도록 최소화.

호스트가 필요 이상으로 많은 Tool을 동시에 peer choice로 노출하는 환경이라면 그 세션은 별도 `REVIEW` 대상이다. 저장소가 보지 못한 runtime action을 0개라고 주장하지 않는다.

---

## 5. 채택 라우터 — 29개 상세 행을 모두 <=5로 노출

### 5.1 최상위 5개 밴드

| 밴드 | 범위 | 다음 선택 수 |
|---|---|---:|
| **B1 세계 규칙** | 회귀·시간선·경제산업·핵심 콘셉트 | 4 |
| **B2 사회·제도** | 세력·정치·학교·군 편제 | 2개 하위 라우터 |
| **B3 인물·서사** | 구조·장면·복선·결말·인물 장면 | 2개 하위 라우터 |
| **B4 물성·작전** | 함대/기체전·전용기/함선/무기·전투원고 | 2개 하위 라우터 |
| **B5 수집·감사** | 도감·성장·팀·참고분석·완성회차 감사 | 5 |

### 5.2 B1 — 세계 규칙

직접 4택1:
1. 회귀 규칙;
2. 원래 시간선;
3. 경제·산업 설정;
4. 작품 핵심 콘셉트.

### 5.3 B2 — 사회·제도

첫 단계 2택1.

**B2a 권력·세력 — 4택1**
- 세력 설정;
- 적대세력 전략;
- 제3세력;
- 정치 사건.

**B2b 제도·편제 — 2택1**
- 교도군사학교;
- 군 계급·편제.

### 5.4 B3 — 인물·서사

첫 단계 2택1.

**B3a 구조·회수 — 5택1**
- 1000화 구조;
- 대액트·액트;
- 회차·장면 카드;
- 복선·맥거핀;
- 결말.

**B3b 인물 장면 — 3택1**
- 영입 에피소드;
- 정치 대화;
- 감정 장면.

### 5.5 B4 — 물성·작전

첫 단계 2택1.

**B4a 전투 실행 — 3택1**
- 함대전;
- 기체전;
- 전투 원고.

**B4b 하드웨어 설계 — 3택1**
- 전용기 설계;
- 함선 설계;
- 무기·센서.

### 5.6 B5 — 수집·감사

직접 5택1:
- 영웅 도감;
- 희귀도·성장;
- 팀 조합;
- 게임 참고 분석;
- 완성 회차 검토.

29행 전수 배정, 중복 0, 누락 0.

---

## 6. 다른 기존 라우팅면과의 관계

이 저장소에는 역사적으로 여러 라우팅 문서가 겹친다.

- [[specialist-routing-index]] — 가장 구체적인 29행;
- [[agent-orchestra-registry-v1]] 활성화 규칙 / 패널;
- [[orchestra]] §4 레거시 10행;
- [[specialist-roster]] 역할 정의.

이 문서는 이 정본 문서들을 삭제·폐기·재작성하지 않는다.

세션에서는 **§5의 bounded router 하나만 선택면으로 사용**하고, 나머지는 선택된 행의 담당·필수검토·권한을 조회하는 lookup source로 사용한다.

즉 네 개 문서를 동시에 `peer choice`로 노출하지 않는다.

충돌 시:
- 상세 산출물 매핑은 [[specialist-routing-index]] 우선;
- Canon/거부권/게이트는 각 상위 정본 프로젝트 제어 문서 우선;
- 이 OS 감사문서는 정본 권한을 바꾸지 않는다.

중복 라우팅 문서 자체는 구조적 부채지만, 이를 통합/폐기하는 것은 프로젝트 정본 구조 변경이므로 이번 적용 범위가 아니다.

---

## 7. OS plugin actions — phase gating

설치 상태:
- `minimum-action-agent-os@storm-credit-agent-os` v0.1.1;
- user scope;
- enabled;
- skills: `os-preflight`, `os-state`;
- agent: `independent-critic`;
- OS rule files은 plugin 쪽에 유지.

세 호출을 도메인 5-band와 동시에 같은 peer menu로 취급하지 않는다.

```text
P0 착수 전      -> os-preflight (필요한 비단순 작업에서만)
R0~R5 작업      -> bounded domain router
E0 독립 평가    -> independent-critic (material review가 필요할 때)
S0 상태 변경 후 -> os-state
```

이 phase gating을 깨고 `3 OS actions + 5 domain bands`를 한 노드에 동시에 노출하면 8개가 되므로 REVIEW다.

OS skill/agent는 기존 §6 Harness, §13 C1–C11, §15 독립 감사의 **보완재**다. 대체재가 아니다.

---

## 8. 기존 규칙 보존 / 중복 생성 0

다음은 이미 프로젝트에 있으므로 새 Agent/Rule/Skill을 만들지 않는다.

| 필요한 작업 원칙 | 기존 근거 |
|---|---|
| 사용자 의도·중요 미결정 확인 | CLAUDE.md §3, §9-4 |
| 맹점 훑기 | §3, §9-1 |
| 구현/설계 전 함정 체크 | §9-2 |
| 의미 있는 방향 4안 비교 | §9-3, Phase 2 |
| 본보기·레퍼런스 조사 | §9-5, §2-4 |
| 메타 프롬프팅 | 기존 작업규칙/오케스트레이션 |
| 독립 Critic / Red Team | §6, §15-3, A16, 기존 Red Team 기록 |
| Harness | §6·§13, `tools/validate_canon.py` 등 |
| 계획 이탈 기록 | §3, §9-6 |
| current status / canon update | [[decision-log]], §21 main 통합 |

신규 프로젝트 Agent: **0**
신규 프로젝트 Skill: **0**
Agent 제거: **0**
기존 61역할: **전부 유지**

---

## 9. 안티패턴 / 위험

### PASS
- God Agent로 통합하지 않음;
- 전체 Agent를 5개 이하로 축소하지 않음;
- OS 본문을 CLAUDE.md에 복제하지 않음;
- Canon/Spec/Freeze/원고를 OS가 덮어쓰지 않음;
- 기존 Harness를 OS로 교체하지 않음.

### 남은 위험

**RISK-01 — 라우팅 정본 중복**
- 4개 라우팅/역할 표면이 역사적으로 공존한다.
- 현재 해결: 하나의 bounded entrypoint만 선택면으로 사용.
- 장기 통합은 정본 구조 변경이므로 작가 결정 없이는 하지 않는다.

**RISK-02 — runtime built-in tool surface**
- 저장소만으로 Claude Code host tool 전체를 실측할 수 없다.
- 현재 해결: 세션별 preflight에서 task-relevant tool만 사용.

**RISK-03 — phase-gating 우회**
- OS skill/critic/state와 domain band를 한 화면에서 모두 peer action으로 취급하면 다시 >5가 된다.
- 현재 해결: P/R/E/S 단계별 호출 규칙.

---

## 10. 정정 이력과 Critic 기록

### 기존 PR #186 적용의 독립 Critic

기존 도입 작업은 별도 Codex 독립 검토를 두 차례 받았다.

1. 1차: **FAIL** — `specialist-routing-index` 29행을 놓친 것을 발견.
2. 수정 후 2차: **PASS WITH ISSUES** — 레거시 라우팅면 추가 확인 및 구조적 부채 기록.

그 결과 PR #186에서 5-band entrypoint와 adoption rule이 들어갔다.

### 2026-08-19 엄격 재감사에서 추가 발견

현재 세션이 사용자 지시의 `각 reasoning node <=5`를 문자 그대로 다시 계산하면서 다음을 발견했다.

- 기존 B2 = 6;
- 기존 B3 = 8;
- 기존 B4 = 6;
- 기존 문서는 B3만 예외로 기록하고 B2/B4를 누락;
- user-scope OS action과 domain bands도 phase gating 없이 같은 노드에 놓으면 합계가 커질 수 있음.

채택 수정:
- B2/B3/B4에 각각 **2-way 하위 router**를 추가;
- 모든 leaf node를 최대 5로 축소;
- OS plugin actions를 P0/E0/S0 단계로 분리;
- 역할, 담당자, 검토자, Canon 권한에는 변경 없음.

### 독립성 표기

이 문서에 기록된 PR #186의 Critic은 실제 별도 Codex 프로세스 기록이다.
현재 ChatGPT 런타임에는 `minimum-action-agent-os:independent-critic`를 직접 실행하는 callable이 노출되어 있지 않으므로, 이번 strict-cap 보정에 대해 **새 독립 프로세스를 실행했다고 주장하지 않는다.**

이번 보정은 숫자 전수배정과 `<=5` 산술 검증으로 자체 검증했다. 새 독립 Critic은 해당 callable이 있는 Claude Code 세션에서 이 파일과 diff만 전달해 재검증하는 것이 남은 품질 단계다.

---

## 11. 현재 판정

### Repository Integration Result

**PASS WITH ONE EXTERNAL-CRITIC FOLLOW-UP**

- Existing Structure Preserved: **YES**
- Domain Canon/Spec/Freeze changed: **NO**
- Manuscript changed: **NO**
- Project code/research design changed: **NO**
- Existing Agents kept: **61 / 61**
- Project Agents added: **0**
- Project Agents removed: **0**
- Project Skills added: **0**
- Local Action Space repository routing: **PASS, every selectable router/leaf <=5**
- Runtime host built-in tools: **session-level audit required**
- Existing independent Critic baseline: **FAIL -> PASS WITH ISSUES**
- Fresh independent Critic after this strict correction: **NOT CLAIMED / follow-up required in Claude Code runtime**

Recommended next step:
- run `minimum-action-agent-os:independent-critic` on this single-file correction in a Claude Code session;
- if no new issue, merge the narrow project-control change;
- do not refactor the 61-role registry or Canon routing documents merely to make the OS look cleaner.
