# Local Action Space Audit — Minimum Action Agent OS 적용

Status: PROJECT CONTROL — 작업 방법론 계층 (도메인 정본 아님)
Owner Agent: A00 Novel PM Orchestrator
Last Reviewed: 2026-08-19
Depends On: [[specialist-routing-index]], [[orchestra]], [[specialist-roster]], [[agent-orchestra-registry-v1]], [[orchestra-v2-activation-rules]], [[agent-execution-contract-and-veto-policy-v1]], [[CLAUDE]]
Used By: 세션 착수 시 역할 라우팅, 신규 에이전트·스킬 추가 판단
Publication: NOT AUTHORIZED
Open Risks: 밴드 계층은 탐색 보조이며 정본 권한을 바꾸지 않는다 — 거부권과 게이트는 [[agent-execution-contract-and-veto-policy-v1]]가 그대로 보유한다

## 1. 이 문서가 하는 일과 하지 않는 일

`storm-credit/minimum-action-agent-os`를 **작업 방법론으로만** 적용한 결과를 기록한다.

**하지 않는 것**: 정본·스펙·원고·도구·연구설계 변경, 에이전트 삭제·축소, 등록부 구조 개편. [[agent-orchestra-registry-v1]]은 `CANON — FIXED SPECIALIST ROLE REGISTRY`이며 이 문서가 건드리지 않는다.

**하는 것**: reasoning node별 Local Action Space 실측과, 5를 넘는 곳에 밴드 색인을 얹는 것.

## 2. 감사 결과

기준: 한 reasoning node에서 **직접 선택 가능한** 행동 수 `<= 5`. 전체 에이전트 수에는 제한이 없다.

| # | 노드 | 직접 선택지 | 수 | 판정 |
|---|---|---|---:|---|
| A | 메인 세션 (프로젝트 선언분) | `.claude/` 부재 → 프로젝트 에이전트·스킬·MCP **0개**. `tools/` 15개 스크립트는 전부 Bash 하나 뒤에 있다 | 1 | **PASS** |
| **B** | **A00 산출물 라우팅 — [[specialist-routing-index]]** | **산출물 유형 29행 중 택1. `Status: CANON` · `Used By: All project work`로 이 저장소의 실제 1차 라우팅면이다** | **29** | **REVIEW** → §3에서 처리 |
| B' | A00 역할 라우팅 (등록부 활성화 규칙) | 산출물 유형 10행 중 택1 | 10 | **REVIEW** → §3에서 처리 |
| C | A00 패널 탐색 (등록부 8패널) | 8개 패널 | 8 | **REVIEW** → §3에서 처리 |
| D | 패널 내부 전문가 선택 | 패널당 6–10 | 6–10 | **PASS (근거 §4)** |
| E | 고정 실행 순서 (등록부 §10) | 10단계 — 선택이 아니라 순서 | — | **PASS** |
| F | 수집 오케스트라 (C1–C8) | 8개 — 선택이 아니라 범위 전체 팬아웃 | — | **PASS (근거 §4)** |
| G | 기체 디자인 오케스트라 (M01–M08) | 8개 — 동일 | — | **PASS (근거 §4)** |
| H | 라우팅표 행별 검토자 수 (6–8명이 대부분, `게임 참고 분석`은 `G01~G09, R07, O04`, `완성 회차 검토`는 `Q01~Q06 + 해당 분야 전문가`로 더 넓다) | 「주 담당과 필수 검토자를 **호출한다**」 — 폭과 무관하게 전원 호출 팬아웃이지 택1이 아니다 | — | **PASS (근거 §4)** |
| I | 기본 거부권 분야 8종 (활성화 규칙) | 해당 분야를 건드리면 자동 발동하는 트리거 조건 — 선택이 아니다 | — | **PASS** |
| J | 레거시 라우팅 — [[orchestra]] §4 Required Review Matrix | 산출물 10행 중 택1. `Status: CANON` · `Used By: All project phases`로 여전히 유효하다 | 10 | **REVIEW** → §3.4에서 처리 |
| K | [[specialist-roster]] 11개 부서 | 자체 라우팅표가 없다 — 정의 문서이며 진입은 [[specialist-routing-index]]를 거친다. 등록부 패널과 같은 부류 | — | **PASS** |

**핵심 판정**: 라우팅 문서들은 action space가 아니라 **routing table**이다. 등록부 §10이 실행 순서를 고정하고 §11이 전문가 집합을 결정하며, [[specialist-routing-index]]의 검토자 수도 택1이 아니라 전원 호출이다. **모델이 실제로 자유 선택하는 지점은 「이 산출물이 어느 유형인가」 하나뿐이고, 그 선택지가 29개다.**

> **정정 이력**: 이 감사의 1차 판정은 등록부(10행)만 보고 B를 처리했다. 독립 Critic(§8)이 [[specialist-routing-index]]가 `Used By: All project work`인 채로 29행을 들고 있다는 것을 잡았다. 이 저장소가 반복해 온 실패 — **찾은 문서로 판단하고 지배하는 문서로 판단하지 않는 것** — 이 감사 자체에서 재현됐다. 2차 검토에서는 레거시 라우팅면 두 곳([[orchestra]] §4, [[specialist-roster]])이 추가로 지적돼 J·K로 분류하고 §3.4에 배정했다. **라우팅면이 네 곳에 겹쳐 있다는 것 자체가 이 저장소의 구조적 부채이며**, 이 감사는 그것을 정리하지 않고 진입점만 하나로 모은다 — 정리는 정본 변경이라 작가 결정 영역이다.

## 3. 채택 수정 — 밴드 색인 하나

B·B'·C가 같은 원인이다. 최소 수정은 **[[specialist-routing-index]] 29행 · 등록부 활성화 10행 · 등록부 8패널을 같은 5개 밴드로 묶는 색인**이며, 적용 원칙 6의 순서 중 `Router 계층화`에 해당한다. 정본 표의 행·주 담당·검토자·권한은 하나도 바꾸지 않는다 — 진입점만 얹는다.

### 3.1 밴드별 산출물 (29행 전수 배정)

| 밴드 | [[specialist-routing-index]] 산출물 행 | 행 수 |
|---|---|---:|
| **B1 세계 규칙** | 회귀 규칙 · 원래 시간선 · 경제·산업 설정 · 작품 핵심 콘셉트 | 4 |
| **B2 사회·제도** | 세력 설정 · 적대세력 전략 · 제3세력 · 정치 사건 · 교도군사학교 · 군 계급·편제 | 6 |
| **B3 인물·서사** | 1000화 구조 · 대액트·액트 · 회차·장면 카드 · 복선·맥거핀 · 결말 · 영입 에피소드 · 정치 대화 · 감정 장면 | 8 |
| **B4 물성·작전** | 함대전 · 기체전 · 전용기 설계 · 함선 설계 · 무기·센서 · 전투 원고 | 6 |
| **B5 수집·감사** | 영웅 도감 · 희귀도·성장 · 팀 조합 · 게임 참고 분석 · 완성 회차 검토 | 5 |
| | **합계** | **29** |

배정 규칙: 행이 무엇을 **주로 구속하는가**로 나눴다. `작품 핵심 콘셉트`는 세계 규칙을 정하므로 B1, `전투 원고`는 원고이지만 전투 기하가 지배하므로 B4, `완성 회차 검토`는 감사이므로 B5다. 중복·누락 0.

### 3.2 밴드별 등록부 대응

| 밴드 | 등록부 활성화 행 | 등록부 패널 |
|---|---|---|
| **B1 세계 규칙** | world physics/route · economy | 6. Science, Infrastructure and Technology |
| **B2 사회·제도** | law/institution · culture/family | 5. Politics, Law, Society and Culture |
| **B3 인물·서사** | character/faction · act architecture | 3. Narrative Architecture · 4. Character and Human-Experience |
| **B4 물성·작전** | mecha/ship · military campaign | 7. Hardware and Maintenance · 8. Military and Security |
| **B5 수집·감사** | collection · final audit | 9. Collection and Progression · 2. Governance and Canon |

### 3.4 레거시 라우팅면 대응 ([[orchestra]] §4)

`orchestra.md`는 18 부서장 체계의 v1 라우팅표를 아직 `CANON`으로 들고 있다. [[specialist-routing-index]]가 같은 기능을 29행으로 더 세분해 수행하지만 **v1을 폐기하지 않았으므로 밴드에 함께 배정한다.** 두 표가 충돌하면 더 구체적인 29행 표가 이긴다 — CLAUDE.md §26의 정본 순서를 따른다.

| 밴드 | [[orchestra]] §4 산출물 행 |
|---|---|
| **B1 세계 규칙** | 핵심 콘셉트 · 세계관 규칙 |
| **B2 사회·제도** | 정치·경제 |
| **B3 인물·서사** | 인물 설정 · 장기 플롯 · 복선 장부 · 집필 하네스 |
| **B4 물성·작전** | 기체·함선 |
| **B5 수집·감사** | 수집 시스템 · 완성 원고 |

10행 전수 배정, 중복·누락 0.

### 3.3 사용법

1. 산출물을 보고 **밴드 하나** (5택1)
2. 밴드 안에서 **산출물 행 하나** (최대 8택1 — B3)
3. 그 행이 지정한 주 담당·필수 검토자를 **전원 호출** (선택 아님, 팬아웃)

1단계가 5 이하다. 2단계는 밴드당 4~8이며 B3만 8이다 — 이는 §4에 트레이드오프로 기록한다.

## 4. 5를 넘는데 그대로 두는 것 — 근거와 트레이드오프

OS의 `rules/local-action-space.md`는 5를 넘길 경우 **이유와 트레이드오프를 기록**하라고 요구한다.

**D — 패널 내부 6–10**: 자유 선택이 아니다. 활성화 규칙이 산출물 유형별로 필요한 전문가 집합을 이미 지정하므로 A00은 패널을 훑지 않고 지정된 집합을 받는다. 이를 5 이하로 쪼개려면 등록부 패널을 재편해야 하고, 그것은 CANON 변경이라 적용 원칙 1·9에 걸린다. **트레이드오프**: 활성화 규칙을 읽지 않고 패널만 보고 고르는 세션에서는 선택지가 6–10으로 노출된다. 완화책은 §3의 밴드 색인을 진입점으로 쓰는 것이다.

**B3 밴드 내부 8행**: 5를 넘는다. 더 쪼개면 밴드가 6개가 되어 1단계가 5를 넘고, 그쪽이 더 나쁘다 — 진입점이 매번 쓰이는 자리이기 때문이다. **트레이드오프**: 서사 작업에서 2단계 선택지가 8이다. 완화 근거는 이 8행이 서로 명확히 다른 산출물(구조·액트·장면카드·복선·결말·영입·대화·감정)이라 혼동 비용이 낮다는 것이다. 밴드를 6개로 늘리는 대안은 재검토 대상으로 남긴다.

**F·G — 오케스트라 8개**: 이것은 action space 문제가 아니다. OS는 *"peer choices the model can directly select from"*을 세라고 하는데, 두 오케스트라는 **범위 전체를 동시에 스폰하는 팬아웃**이지 8택1이 아니다. 게다가 독립성 자체가 산출물의 요건이다 — CLAUDE.md §15-3은 분야 패스가 서로의 결론을 보기 전에 독립 진단할 것을 요구하고, 라우터를 끼우면 그 속성이 깨진다. **트레이드오프**: 동시 실행 비용이 크다. 이미 CLAUDE.md §15-4가 동시 실행 한도로 통제한다.

## 5. 이미 있어서 새로 만들지 않은 것

OS 표준 워크플로 9단계 중 8단계가 이 저장소에 선행 존재한다. 적용 원칙대로 **보존하고 중복 생성하지 않았다.**

| OS 단계 | 이 저장소의 기존 근거 |
|---|---|
| 의도·결측 확인 | CLAUDE.md §3, §9-4 작가 인터뷰 |
| 맹점 훑기 | §3, §9-1 |
| 착수 전 함정 체크 | §9-2 |
| 4안 비교 | §9-3, Phase 2 |
| 본보기·레퍼런스 | §9-5, §2-4, [[prose-style-reference-shortlist-v1]] |
| 실행 | Phase 0–10 |
| 독립 평가 | §6 하네스 순서, §15-3 독립 감사, [[registry-redteam-2026-08-13]] |
| 하네스·수용 검사 | §13 자동 검증 C1–C11, `tools/validate_canon.py` |
| 상태·정본 갱신 | §2-10 [[decision-log]], §21 main 통합 |

메타 프롬프팅과 계획 이탈 기록도 §3·§9-6에 이미 있다. **신규 생성 0건.**

## 6. 안티패턴 점검

| 패턴 | 현 상태 |
|---|---|
| God Agent | 해당 없음 — 61역할이 분야별로 분리돼 있고 거부권이 분산 |
| Tool Swamp | 해당 없음 — `.claude/` 부재, 도구가 Bash 하나 뒤 |
| Agent Explosion | **경계 대상.** 61역할은 문서상 역할이며 자율 프로세스가 아니라고 등록부 §1이 명시. 실제 독립 실행은 증거가 있을 때만 주장 (§15-1) |
| Mega CLAUDE.md | **경계 대상.** CLAUDE.md가 25절이다. 이번 적용은 §26 한 절만 추가하고 OS 본문을 복사하지 않았다 |
| Groupthink Critic | 완화됨 — 독립 오케스트라를 별도 모델(Codex)로 실행한 기록이 [[registry-redteam-2026-08-13]] §5·§7에 있다 |
| Unrecorded plan drift | 해당 없음 — §9-6 |

## 7. 플러그인 설치 — 완료 (2026-08-19)

**설치됨**: `minimum-action-agent-os@storm-credit-agent-os` v0.1.1, user 스코프, enabled. 마켓플레이스는 이미 등록돼 있었고 플러그인만 설치했다.

검증: `claude plugin validate` 통과(경고 1건 — 마켓플레이스 description 없음, 비차단). 캐시 `0.1.1`에 자산 확인 — 스킬 `os-preflight`·`os-state`, 에이전트 `independent-critic`, 규칙 3종. 구버전 `0.1.0`은 orphaned 표시.

설치에 쓴 명령:

```bash
claude plugin marketplace add storm-credit/minimum-action-agent-os
claude plugin install minimum-action-agent-os@storm-credit-agent-os
```

**에이전트를 이 저장소에 복제하지 않는다** — 어댑터가 플러그인 배포를 권고하고, 복제는 중복 생성이다. 이 저장소의 `.claude/`는 계속 비어 있으며, 그래서 노드 A의 프로젝트 선언 action space는 여전히 0이다.

**적용 순서 주의**: OS 스킬은 §6 하네스와 §13 검증기를 대체하지 않는다. 정본 판정·게이트·C1–C11은 이 저장소가 계속 갖는다.
