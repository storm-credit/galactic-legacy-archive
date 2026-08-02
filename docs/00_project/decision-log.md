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

Status: ACCEPTED WITH OPEN DETAILS
Date: 2026-08-03
Decision Owner: User + A00

### Context

에이스 조종사는 초반 직접 전투와 기체 수집에 강하고, 제독은 장기 정치·함대·세력 운영 서사를 끌기 좋다.

### Decision

주인공은 전생에 에이스 출신 패전 제독이며, 회귀 후 교도군사학교 생도 또는 죄수 조종사로 다시 시작한다. 작품 초반에는 직접 출격하는 에이스, 중후반에는 전대장·함장·제독으로 책임 범위를 넓힌다.

### Reasons

- 초반 흡입력과 후반 확장성을 함께 확보한다.
- 영웅·기체·무기 수집을 주인공이 직접 경험한다.
- 전생의 실패와 현생의 성장 방향이 선명하다.

### Open Details

- 전생 최종 계급
- 실제 패전 책임
- 현생 첫 공식 계급
- 직접 출격과 지휘의 비율

### Affected Documents

- `docs/00_project/project-charter.md`
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

---

## D-20260803-04 — Fixed PM orchestra and harness

Status: ACCEPTED
Date: 2026-08-03
Decision Owner: User + A00

### Context

설정·플롯뿐 아니라 작문법, 전투 묘사, 풍경 묘사, 웹소설 연재법, 맥거핀과 결말 회수, 완성본 검토까지 일관된 체계가 필요하다.

### Decision

총괄 포함 18개 고정 역할과 필요 시 호출되는 전문 벤치를 운영한다. 집필 전 하네스와 완성 원고 revision harness를 분리한다.

### Consequences

- 담당과 교차검토 책임이 명확해진다.
- 문체 감독이 사건을 임의로 바꾸지 못하는 등 권한 경계를 적용한다.
- 모든 핵심 산출물은 맹점 레드팀과 정본 관리자의 검토를 받는다.

### Affected Documents

- `docs/00_project/orchestra.md`
- `docs/13_writing_harness/prose-bible.md`
- `docs/13_writing_harness/revision-harness.md`
