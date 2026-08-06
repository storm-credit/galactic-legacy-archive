# Decision Log

Status: CANON
Owner Agent: A00 Novel PM Orchestrator
Last Reviewed: 2026-08-03
Depends On: None
Used By: All project documents
Open Risks: Unrecorded conversational decisions

## Decision Format

```markdown
## D-YYYYMMDD-NN — Title
Status: PROPOSED | ACCEPTED | REVERSED | SUPERSEDED
Date:
Decision Owner:

### Context

### Options Considered

### Decision

### Reasons

### Consequences

### Risks

### Affected Documents

### Reversal Condition
```

---

## D-20260803-01 — Design before manuscript

Status: ACCEPTED
Date: 2026-08-03
Decision Owner: User + A00

### Context

장기 SF 웹소설을 공모전과 1000화 이상 연재 가능 구조로 준비한다. 설정과 장기 플롯이 불완전한 상태에서 원고를 먼저 쓰면 후반 모순과 전면 개작 위험이 크다.

### Decision

설계도, 설정집, 수집 시스템, 결말 회수 구조, 집필 하네스, 검토 하네스가 Pre-Writing Gate를 통과하기 전 본편 원고를 작성하지 않는다.

### Consequences

- 초기 속도보다 장기 일관성을 우선한다.
- 비정본 샘플은 시점·문체·전투 전달 검증 목적으로만 허용한다.
- 본편 집필 브랜치는 별도 승인 후 생성한다.

### Risks

- 과도한 설계로 실제 집필이 지연될 수 있다.

### Mitigation

- 먼 미래는 대액트 수준, 가까운 구간만 장면 수준으로 정밀화한다.
- Anti-Analysis-Paralysis Rule을 적용한다.

### Affected Documents

- `CLAUDE.md`
- `docs/00_project/workflow.md`
- `docs/99_quality_control/prewriting-gate.md`

---

## D-20260803-02 — Protagonist identity

Status: ACCEPTED
Date: 2026-08-03
Decision Owner: User + A00

### Context

에이스 조종사는 초반 직접 전투와 기체 수집에 강하고, 제독은 장기 정치·함대·세력 운영 서사를 끌기 좋다.

### Decision

주인공은 전생에 에이스 출신 최후의 패전 제독이며, 회귀 후 17세 전후의 교도군사학교 죄수 생도로 다시 시작한다. 초반에는 직접 출격하는 에이스, 중후반에는 전대장·함장·제독으로 책임 범위를 넓힌다.

전생 패전은 단순 배신이 아니라 다음 네 원인이 겹친 결과로 고정한다.

1. 전술적 승리 뒤 제도와 통치 구조를 남기지 못함.
2. 뛰어난 영웅을 자기 지휘망에 집중해 후계 조직을 약화.
3. 수도 함대를 구하려 전략 노드와 피난선단을 포기한 `오르페우스 선택`.
4. 승자 기록과 유산록 원형이 편집한 정보를 최종 결전에서 신뢰.

### Reasons

- 초반 흡입력과 후반 확장성을 함께 확보한다.
- 영웅·기체·무기 수집을 주인공이 직접 경험한다.
- 전생의 실패가 ‘더 강해지기’가 아니라 ‘사람과 제도를 다르게 대하기’라는 현생 성장으로 연결된다.

### Consequences

- 주인공은 군사·조종에 강하지만 정치·과학·정비·외교를 독점하지 않는다.
- 직접 출격은 지휘 공백과 책임 비용을 만든다.
- 미래 인물을 전력으로만 계산하는 버릇이 핵심 내적 결함이 된다.

### Affected Documents

- `docs/01_concept/canon-core-packet-v1.md`
- 향후 character bible
- 향후 macroplot

---

## D-20260803-03 — Collection scope

Status: ACCEPTED
Date: 2026-08-03
Decision Owner: User + A00

### Context

단일 코어나 기체만이 아니라 다양한 장르의 수집욕을 자극하는 작품을 원한다.

### Decision

수집 범위를 영웅, 기체, 무기, 보물, 함선, 기술, 세력, 행성·문명으로 확장한다. 단, 모든 범주를 초반에 동시에 개방하지 않고 대액트별로 단계적으로 확장한다.

### Reasons

- 수집욕과 1000화 장기 확장을 동시에 확보한다.
- 개인 성장에서 함대·국가·문명 성장으로 자연스럽게 이동한다.

### Risks

- 도감 과잉, 인물의 아이템화, 기존 수집품 폐기, 독자 기억 부담

### Mitigation

- 영웅 자율성 규칙
- 수집 대상의 서사 기능 2개 이상
- 역할 기반 장비 설계
- 계층화된 도감과 세트
- 시즌별 전면 수집 범주 최대 2개

---

## D-20260803-04 — Fixed PM orchestra and harness

Status: ACCEPTED
Date: 2026-08-03
Decision Owner: User + A00

### Context

설정·플롯뿐 아니라 작문법, 전투 묘사, 풍경 묘사, 웹소설 연재법, 맥거핀과 결말 회수, 완성본 검토까지 일관된 체계가 필요하다.

### Decision

총괄 포함 18개 부서장 역할과 내용에 따라 자동 호출되는 세부 고정 전문가 셀을 운영한다. 집필 전 하네스와 완성 원고 revision harness를 분리한다.

### Consequences

- 담당과 교차검토 책임이 명확해진다.
- 문체 감독이 사건을 임의로 바꾸지 못하는 등 권한 경계를 적용한다.
- 모든 핵심 산출물은 맹점 레드팀과 정본 관리자의 검토를 받는다.

### Affected Documents

- `docs/00_project/orchestra.md`
- `docs/00_project/specialist-roster.md`
- `docs/13_writing_harness/prose-bible.md`
- `docs/13_writing_harness/storycraft-bible.md`
- `docs/13_writing_harness/revision-harness.md`

---

## D-20260803-05 — One-time regression and historical inertia

Status: ACCEPTED
Date: 2026-08-03
Decision Owner: User + T06 + A00

### Context

반복 타임루프는 죽음과 손실의 무게를 약화하고, 장기적으로 시행착오 최적화가 정치·수집·함대전보다 강해질 위험이 있다.

### Options Considered

- 반복 사망 회귀
- 다중 분기 세계선
- 단일 세계선 덮어쓰기
- 역사 관성형 단일 세계선
- 미래 기록 주입형

### Decision

주인공의 회귀는 단 한 번이다. 하나의 역사선이 이어지며 자원·계급·제도 같은 구조적 압력에는 관성이 있다. 주인공의 미래 기억은 개인 경험, 군사보고, 공식 역사, 유산록 기록이 섞인 불완전한 자료다.

B2 이상의 개입은 분기 장부에 등록하고 1차·2차·3차 영향을 추적한다. 개입할수록 관련 미래정보의 신뢰도가 하락하며 적대·제3세력도 관찰하고 학습한다.

### Consequences

- 실패와 죽음은 되돌릴 수 없다.
- 미래지식은 정답지가 아니라 검증해야 할 가설이다.
- 사건 하나를 막아도 구조적 원인이 남으면 다른 형태로 재발한다.

### Affected Documents

- `docs/02_world/regression-causality-harness.md`
- 향후 original timeline
- 향후 divergence ledger

### Reversal Condition

반복 루프가 작품의 핵심 주제와 수집·정치 엔진을 약화하지 않는다는 별도 4안 검증을 통과할 때만 재검토한다.

---

## D-20260803-06 — Strategic necessity of maneuver frames

Status: ACCEPTED FOR CONCEPT
Date: 2026-08-03
Decision Owner: M03 + M04 + H01 + T02 + A00

### Context

함선·미사일·드론이 존재하는 시대에 인간형 기체가 단순 미학으로만 존재하면 세계관이 붕괴한다.

### Decision

메카는 함대의 대체재가 아니다. 워프 격자와 거주·생산시설처럼 파괴하면 승자도 잃는 전략 노드를, 교란된 혼합환경 안에서 나포·구조·통제하기 위한 인간-기계 범용 기동 프레임이다.

- 함대가 개방 우주와 접근권을 장악한다.
- 기동 프레임이 노드 외벽·도크·통제시설을 장악한다.
- 보병·공병·기술팀이 점령과 복구를 완성한다.
- 인간형은 신경지도와 산업용 작업 프레임 생태계가 만든 표준이지 유일한 형태가 아니다.

### Consequences

- 개방 우주에서 메카 단독 출격은 비합리적이다.
- 전투는 파괴뿐 아니라 나포·구출·지연·통제 목적을 가진다.
- 장비 수집은 출력보다 임무 역할과 열·추진제·정비·소유권 교환을 만든다.

### Affected Documents

- `docs/02_world/mecha-strategic-necessity.md`
- `docs/02_world/lattice-war-physics-and-ai-law.md`

### Remaining Calibration

- 세력별 AI 예외
- 산업 비용과 정비 인원
- 행성전 변형
- 신경동조 부작용

---

## D-20260803-07 — Canon core direction

Status: ACCEPTED — CANON v1
Date: 2026-08-03
Decision Owner: User intent + R01 + N01 + A00

### Context

제독 중심, 에이스 중심, 교도학교 미션 중심, 균형형 네 방향을 초반 훅·수집·정치확장·장기 지속성·유사성 위험으로 비교했다.

### Decision

균형형 `Galactic Legacy Hybrid`를 정본 v1로 채택한다.

Internal formula:

> Ace-first interface / Admiral-first architecture / Mission-first opening / Legacy-collection long engine.

독자에게는 초반 `교도군사학교에서 다시 시작하는 회귀 에이스·영웅수집 SF`로 보이고, 책임 범위가 커질수록 `함대·제독·다극 정치 스페이스오페라`로 확장한다.

### Reasons

- 에이스전과 수집의 즉시 재미를 보존한다.
- 교도학교가 아직 영웅이 아닌 인물과 국가의 인간 자원화를 압축한다.
- 제독의 과거와 함대·정치 구조가 1000화 확장성을 제공한다.
- 유산록과 역사 분기가 네 장르를 하나의 인과로 묶는다.

### Consequences

- 첫 20화 전면 인물 5명 내외, 세력 5개, 주력 기체 1대, 무장 1개로 제한한다.
- 유산록은 소환·GPS·절대 감정 기능을 갖지 않는다.
- 첫 미래 영웅은 자동 영입되지 않으며 그의 비극을 만든 협박·책임전가 구조를 바꿔야 한다.
- 주인공·적대·제3세력은 서로 독립적으로 행동한다.

### Affected Documents

- `docs/01_concept/four-directions-comparison.md`
- `docs/01_concept/canon-core-packet-v1.md`
- 모든 후속 설계 문서

### Reversal Condition

비정본 초반 20화 비트 검증에서 핵심 약속이 5화 안에 드러나지 않거나 장르 과부하가 해소되지 않을 경우 표면 장르 순서를 재조정한다.

---

## D-20260806-01 — 회차 분량 상한 유연화

작가 판정: 회차당 분량은 5,500~6,500자 진단 범위보다 길어도 무방하다.

### Consequences

- E1~20 "출판 분량 압축 패스"를 밀도·반복 정리 패스로 재정의.
- 플랫폼/공모전 선정과 공백 포함 여부는 출판 전 확정 항목으로 하향(`[ASSUMPTION]` 공백 포함, 하한 5,500자).

### Affected Documents

- `docs/00_project/pre-writing-gate-review-v1.md`
- `docs/00_project/first-writing-batch-readiness-v1.md`

### Reversal Condition

플랫폼/공모전 규정 확정 시 해당 규정이 우선한다.

## D-20260806-02 — issue #26 출판 전 블로커 확정 (D2)

작가 승인: `docs/00_project/issue-26-status-resolution-proposal-v1.md` 발효. 인간/모바일 테스트는 출판 전 하드 블로커이며 초고 생산을 차단하지 않는다. 과거 override 문서는 비정본 유지 — 본 판정은 신규 작가 결정이다.

### Consequences

- 첫 배치 병행 인간 테스트(최소 5인, 절반 이상 폰 화면) 실행 의무.
- 출판·공개는 테스트 통과 전 차단, "인간 검증 완료" 주장 금지, issue #26 OPEN 유지.

### Affected Documents

- `docs/99_quality_control/prewriting-gate-dry-audit-2026-08-03.md` (주석)
- `docs/99_quality_control/prewriting-gate-evidence-matrix-v2.md` (주석)
- `docs/07_style/gate1-korean-webnovel-pov-prose-calibration-v1.md` (§12 개정 주석)

### Reversal Condition

인간 테스트 동일 항목 2회 이상 임계 미달 시 집필 중단 및 문체 캘리브레이션 재실행.

## D-20260806-03 — E1~20 구초안 개정 기반 채택 (D3)

작가 판정: `manuscript/ga1/*-v1.md` 20편을 개정 출발점으로 사용한다(v2 생산). v1의 'Locked Development Outcomes'는 정본 근거로 인용 불가 — 사실은 장면 카드·바이블에서 재확인.

### Affected Documents

- `manuscript/ga1/` (v2 파일 생산)
- `docs/00_project/first-writing-batch-readiness-v1.md`

## D-20260806-04 — Pre-Writing Gate 개방 (초고 생산 한정)

작가 선언: "Pre-Writing Gate를 OPEN한다. 권장된 첫 집필 배치를 시작해." 상세: `docs/00_project/pre-writing-gate-open-record-2026-08-06.md`. 출판은 계속 차단.

## D-20260806-05 — 소급 등재 (F-11 해소)

2026-08-03~05 사이 decision-log 미기록 정본 변경의 소급 기록:

- errata-002(도안 미르→미르 카오), errata-003(승무원 법정 최소 42명), errata-004(하렌 제재 연표 E783/CY745-08) 발행.
- E101~1100 상세설계 1,000편 완료 및 교차감사 PASS (PR #85~89, B10-03은 PR #88로 2026-08-06 병합).
- 근접 3인칭 POV·문체 하네스·E1 v2 모바일 변형 승인(gate1 §3·§11, 2026-08-03) — F-27 해소.
