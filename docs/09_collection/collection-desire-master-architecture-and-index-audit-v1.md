# Collection Desire Master Architecture and Index Audit v1

Status: PROPOSED — NONCANON
Owner Agents: A00 Collection Orchestrator / G01–G07 Collection Panel / O01 Canon / O02 Gate / X02 Reader Memory / X03 Ethics / X04 Continuity / X06 Coverage / A16 Red Team
Last Reviewed: 2026-08-09
Depends On: [[galactic-legacy-collection-bible-v1]], [[collection-category-authoring-templates-v1]], [[counter-collection-and-intelligence-war-bible-v1]], [[effective-canon-status-manifest-v1]], [[agent-orchestra-registry-v1]]
Used By: collection registry normalization, category design, set planning, reader-facing reward audits
Canon Promotion: NOT AUTHORIZED
Publication: NOT AUTHORIZED
Open Risks: registry rows mistaken for unique objects, rights treated as objects, reader-facing overload, category leakage, unapproved positive relic additions

## 1. Executive Ruling

현재 마스터 등록표에서 기계적으로 확인되는 항목 제목은 **415행**이다. 428은 수집 대상 수가 아니라 문서 안의 회차 번호·범위에서 나타난 숫자다.

그러나 `415행 = 서로 다른 수집품 415개`는 아니다. 등록표에는 다음이 함께 섞여 있다.

- 독립 실체: 인물, 기체, 함선, 조직, 장소.
- 부품·모듈: 독립 실체의 구성품 또는 운용 패키지.
- 상태 변화: 같은 대상의 발견·확보·복구·상실 단계.
- 권리·기록: 소유권, 운용권, 통행권, 헌장, 동의 기록, 기억 조각.
- 세트 슬롯: 여러 실체를 하나의 계보·사건·기능으로 묶는 완성 목표.

따라서 현재 병목은 **수량 부족이 아니라 의미 중복과 노출 우선순위**다. 기존 8개는 작가용 대상 도메인 태그로 충분하다. 독자 전면 도메인은 대액트별 1–2개를 권장 검토하되 승인 전 상한으로 강제하지 않는다. 기록·권리·기억은 별도 대상 카테고리가 아니라 각 대상에 붙는 **통제 facet**, 세트는 별도 메타 테이블로 운용하는 안을 권장한다.

> 권장 구조: **8개 작가용 대상 도메인 태그 + 행 종류 축 + 기록·권리·기억 통제 facet + 세트 메타 테이블**

이 문서는 설계안과 감사 결과다. 새 정본, 새 능력, 새 유물, 새 획득 사건을 승인하지 않는다.

---

## 2. Registry Count Audit

| Registry | Entry rows |
|---|---:|
| First 100 | 42 |
| GA2 | 45 |
| GA3 | 43 |
| GA4 | 40 |
| GA5 | 45 |
| GA6 | 40 |
| GA7 | 39 |
| GA8 | 36 |
| GA9 | 31 |
| GA10 | 54 |
| **Total** | **415** |

Audit notes:

- 제목 ID 기준 중복은 0건이지만, ID가 다르다고 의미상 별개 실체라는 뜻은 아니다.
- `detail/` 아래 상태·상세 문서 37개는 위 415행에 포함하지 않았다.
- [[first-100-collectible-registry-v1]] 서두의 `38 registered targets`와 실제 제목 42개가 불일치한다.
- `P-001`, `I-001` 등은 프로젝트의 인물·기관 코드와 수집 등록표 코드가 충돌한다.
- 개별 파일의 `REVIEW` 헤더와 실효 상태는 [[effective-canon-status-manifest-v1]]의 우선순위로 판정해야 한다.

### 2.1 Five counts that must not be conflated

| Count | Meaning | Use |
|---|---|---|
| Registry row count | 문서에 기록된 진행·보상 행 | 작업량·감사 범위 |
| Unique entity count | 실제로 서로 다른 사람·물건·조직·장소 | 정본 개체 수 |
| State row count | 동일 실체의 시점별 상태 | 연속성 추적 |
| Reader-visible target count | 해당 구간 독자가 의식해야 할 목표 | 기억 부하 통제 |
| Set count | 계보·사건·기능·관계·문명 완성 목표 | 장기 수집욕 설계 |

앞으로 “몇 개냐”를 보고할 때는 반드시 어느 개수인지 명시한다.

---

## 3. Pre-Implementation Trap Sweep

| Trap | Failure mode | Required control |
|---|---|---|
| 행 수를 콘텐츠 수로 오인 | 같은 기체의 코어·부품·열쇠·복구 단계가 각각 새 수집품처럼 부풀려짐 | 실체 ID와 상태 행 ID 분리 |
| 사람의 소유물화 | 영입·신뢰·동맹이 `획득/보유`로 축약됨 | C1 획득 동사를 관계·동의 중심으로 제한 |
| 세력·영토의 점령화 | 합법성·주민·서비스 책임이 사라짐 | C7/C8에 구성원·관할·동의·책임 필드 강제 |
| C2/C3/C6 중복 | 기체 부품, 모듈, 공정, 표준이 세 분야에 중복 등록됨 | `몸체/장착물/재현 지식` 판별 규칙 적용 |
| 유물/통제 facet 중복 | 유물과 실행 가능한 권리 문서가 혼합됨 | 물리 문서는 C4 실체가 될 수 있고 법적 효력은 별도 claim으로 연결 |
| C5 모듈 과다 | 함선 한 척이 수십 개 전면 목표로 보임 | 독자 전면은 함선·신뢰·핵심 기능만 노출 |
| 전면 카테고리 과다 | 8~12개 탭처럼 느껴져 수집욕보다 행정표가 됨 | 8개는 작가용 태그, 대액트별 독자 전면 1–2개를 비정본 권장치로 시험 |
| 거짓 완성 | 모든 칸을 채우면 갈등도 끝난다고 오해 | 완성 후에도 비용·정치·상실·새 의미 유지 |
| 자동 호환 | 새 부품·기술이 즉시 모든 기체·함선에 장착됨 | 인증·정비·훈련·냉각·인터페이스 비용 기록 |
| 정본 몰래 추가 | 빈 C4를 채우려고 새 유물을 사실처럼 추가 | 후보는 `[ASSUMPTION]` 또는 PROPOSED로만 기록 |
| 독자 기억 과부하 | 415행을 모두 전면 보상처럼 소개 | 구간별 활성 목표와 고유명사 상한 적용 |
| 상대 수집자 부재 | 주인공만 목록을 보고 순차 획득 | 경쟁자·기관·주민도 각자 다른 가치로 추구 |

---

## 4. Four Architecture Directions

| Direction | Structure | Strength | Failure risk | Verdict |
|---|---|---|---|---|
| A. Eight only | 기록·권리를 C4 또는 C7에 흡수 | 가장 단순함 | 유물·제도와 실행권이 뒤섞임 | 보류 |
| B. Nine equal categories | C9를 독립 수집 분야로 승격 | 권리·기록의 가시성 높음 | 전면 카테고리 팽창, 권리를 물건처럼 취급 | 비권장 |
| **C. Eight + typed facets** | 8개 작가용 태그, 행 종류, 통제 facet, 세트 표 | 대상·관계·상태·권리를 분리하고 기존 구조 보존 | 드라이런과 인덱스 정규화 필요 | **권장** |
| D. Four desires first | 발견·획득·조합·완성을 최상위로 두고 분야는 태그화 | 독자 심리 설명에 강함 | 정본·권리·전문가 라우팅이 불안정 | 분석용 보조축 |

### [ASSUMPTION A-01]

기록·권리·기억은 별도 카테고리 코드나 독점 1차 분류를 받지 않는다. 물리 문서 자체는 실체일 수 있지만 그 효력은 대상에 붙는 **claim/facet**으로 표현한다.

### [ASSUMPTION A-02]

기존 등록표 ID와 내용을 삭제하거나 개명하지 않는다. 새 인덱스는 별도 안정 ID와 별칭 맵을 제안할 뿐이다.

---

## 5. Domain Architecture

| Code | Author-side domain tag | Main subtypes | Valid acquisition verbs | Hard veto |
|---|---|---|---|---|
| C1 | 영웅·관계 | 조종사, 정비, 지휘, 의료·구조, 데이터·감사, 협상·문화, 경쟁자 | 만나다, 설득하다, 신뢰를 얻다, 동맹하다, 함께 복무하다 | 사람의 충성·감정·신분을 소유물로 표기 |
| C2 | 기체 | 계보·차체, 코어·제어, 추진, 센서·전자전, 장갑·생존, 정비·지원 | 발견하다, 복구하다, 인증하다, 배정받다, 운용권을 얻다 | 부품만으로 새 완성 기체처럼 계산 |
| C3 | 무기·부품 | 근접·공구, 원거리, 방어, 포획·구조, 센서·전자전, 군수·정비, 탄약·에너지 | 회수하다, 제작하다, 장착하다, 인증하다, 숙련하다 | 무상·무훈련·무정비 범용 호환 |
| C4 | 유물·보물 | 출처, 문화·의례, 항법, 상징·법통, 기억·상처, 파편·위조품 | 발굴하다, 해독하다, 반환하다, 보존하다, 의미를 복원하다 | 오래됐다는 이유만으로 전투 강화 아이템화 |
| C5 | 함선 | 선체·신뢰, 추진, 생명유지, 격납·정비, 임무 모듈, 항법·통신, 지휘체계 | 구조하다, 승계하다, 공동 운용하다, 개장하다, 신뢰를 회복하다 | 선원·청구권자·헌장을 선체 부속물로 처리 |
| C6 | 기술 | 이론, 시제품, 공정, 공구, 표준, 교육, 확산·거버넌스 | 이해하다, 재현하다, 검증하다, 표준화하다, 가르치다 | 설계도 한 장으로 산업·숙련·인증이 즉시 생성 |
| C7 | 세력·제도 | 군사, 시민서비스, 기업·산업, 학술·의료, 문화·종교, 반대·연방 | 인정받다, 가입하다, 협약하다, 대표성을 얻다, 개혁하다 | 조직·구성원 전체를 주인공의 자산으로 계산 |
| C8 | 영토·노드·문명 | 거주지·노드, 항로, 산업지대, 정착지, 행성·국가, 문명망, 생태계 | 도달하다, 통행권을 얻다, 서비스하다, 정착하다, 보호 협약을 맺다 | 주민 동의 없이 발견=영유·점령으로 처리 |

Domain tags are not exclusive. A 이동식 거주 함선은 C5와 C8, 제도화된 기술 표준은 C6와 C7처럼 복수 태그를 가질 수 있다. 단, 같은 등록표 행을 고유 실체 수에 중복 합산하지 않는다.

### 5.1 Entry-kind axis

| Entry kind | Meaning |
|---|---|
| `ENTITY` | 독립된 사람·물건·조직·장소 |
| `RELATIONSHIP` | 신뢰·동맹·회원·대표·경쟁 등 실체 사이의 간선 |
| `CONTROL_CLAIM` | 접근·보관·운용·통행·지휘·해석을 증명하거나 제한하는 권리·기록·기억 facet |
| `STATE_TRANSITION` | 식별·복구·인증·상실·분산 등 상태 변화 |
| `LOSS_OBLIGATION` | 영구손실, 유지부담, 배상, 서비스 책임 |
| `NARRATIVE_PROMISE` | 미스터리·신화·회수 약속처럼 아직 실체로 확정되지 않은 장기 슬롯 |
| `SET` | 계보·사건·기능·관계·문명 조합 목표 |

### 5.2 Boundary test

새 항목은 아래 순서로 한 번만 1차 분류한다.

1. 먼저 `entry_kind`를 판정한다. 행이 무엇을 서술하는지와 대상의 도메인을 섞지 않는다.
2. `ENTITY`이면 안정 실체 ID를 부여하고 필요한 C1–C8 복수 태그를 연결한다.
3. 장착물·코어·추진·함선 모듈은 무조건 C3로 강제하지 않는다. `host_id`, 독립 운용성, 독립 비용, 독립 상실 경로로 판단한다.
4. 물리 문서·키·유물과 그 법적·사회적 효력을 분리한다. 전자는 실체가 될 수 있고 후자는 `CONTROL_CLAIM`으로 대상에 연결한다.
5. 같은 대상의 진행 단계는 새 실체가 아니라 `STATE_TRANSITION`으로 기록한다.
6. 여러 항목의 조합 목표는 별도 세트 표에 기록한다.

### 5.2 Known category weaknesses

- C1: 인물·AI·공동체 대표가 혼재하며 `claimed` 언어가 위험하다.
- C2: 초반 등록표는 완성 기체보다 07호 구성품에서 시작해 모체 실체 행이 약하다.
- C2 evolution: [[mecha-lineage-mark-and-evolution-naming-system-v1]]은 원형·임무 사양·영구 개량·통합형·결전 사양·후계기를 구분하는 비정본 계보 제안이다. 승인 전 새 고유 기체 수로 합산하지 않는다.
- C3: 탄약·열·인증·교리·정비비가 무기 외형보다 덜 등록되어 있다.
- C4: 규칙은 강하지만 명시적 긍정 유물은 희박하고, 거짓 유물 해체 항목이 중심이다.
- C5: 선체보다 모듈 행이 많아 독자 전면 노출 시 기억 부하가 높다.
- C6: 개방표준의 최초 전면화 시점과 버전 관계가 문서 간 정리되지 않았다.
- C7: 조직 자체와 가입·대표권·헌장 상태를 분리해야 한다.
- C8: 장소 자체와 통행권·관할권·서비스 책임을 분리해야 한다.
- 통제 facet: C4 유물, C6 표준, C7 제도, C8 관할과 겹치므로 독립 카테고리나 고유 실체 수로 합산하지 않는다.

---

## 6. Collection Engine

한 항목은 하나의 숫자가 아니라 다음 다섯 층을 가진다.

1. **Entity**: 무엇 또는 누구인가.
2. **Control**: 누가 접근·보관·운용·의미를 통제하는가.
3. **Record State**: S0 빈칸부터 S8 완결까지 무엇을 아는가.
4. **Desire**: 발견·획득·조합·완성 중 이번 장면이 자극하는 욕구는 무엇인가.
5. **Set**: 더 큰 계보·사건·기능·관계·문명의 어느 빈칸인가.

### 6.1 Control layers

| Layer | Question |
|---|---|
| Discovery | 존재와 정체를 누가 알고 있는가? |
| Access | 누가 만나거나 열람하거나 접근할 수 있는가? |
| Custody | 물리적으로 누가 보관·보호하는가? |
| Operation | 누가 실제로 사용·지휘·정비할 수 있는가? |
| Meaning | 어느 공동체가 이름·역사·정당성을 해석하는가? |

다섯 층이 같은 주체에게 자동 귀속되지 않는다. 특히 문서·열쇠·암호를 얻어도 인물의 동의, 기체의 운용능력, 함선의 선원 신뢰, 영토의 주민 정당성은 자동 획득되지 않는다.

### 6.2 Desire loop

| Desire | Scene evidence | Required cost |
|---|---|---|
| Discovery | 실루엣, 빈칸, 모순 기록, 불완전 계보 | 오판 가능성, 조사 시간, 노출 위험 |
| Acquisition | 접촉, 협상, 구조, 복구, 인증 | 포기 대상, 책임, 유지비, 반대자 |
| Synergy | 사람·기체·무기·기술의 새 조합 | 훈련, 호환, 지휘 갈등, 자원 배분 |
| Completion | 세트의 누락 슬롯과 진실 회수 | 기존 해석 수정, 상실 인정, 정치적 결과 |

### 6.3 Set layer

| Set type | Example function | Completion must not mean |
|---|---|---|
| `SET-LIN` Lineage | 기체·기술·인물 계보 복원 | 최상위 전투력 자동 지급 |
| `SET-EVT` Event | 같은 사건의 상충 증언·기록 결합 | 단일 공식 기록으로 피해자 기억 삭제 |
| `SET-FUN` Functional | 임무 수행에 필요한 팀·장비·절차 조합 | 모든 상황의 만능 조합 |
| `SET-REL` Relationship | 신뢰·경쟁·책임망의 변화 | 인물의 영구 충성 고정 |
| `SET-CIV` Civilization | 항로·도시·제도·문화 연결 | 발견자의 영유권 인정 |

---

## 7. Stable Index Design

기존 ID는 역사적 출처 ID로 보존한다. 승인 전에는 일괄 개명하지 않는다.

### 7.1 Proposed identifiers

| Identifier | Format | Purpose |
|---|---|---|
| Normalized Entry ID | `CL-R-000001` | 실체·관계·상태·claim 등 정규화된 한 레코드 |
| Entity ID | `CL-E-0001` | 카테고리 변경에도 유지되는 의미상 고유 실체 |
| Source Key | `문서경로#P-001`, `문서경로#G2-S01` 등 | 충돌 없는 원문 추적 |
| State Row ID | `ST-GA02-E101-125-001` | 시점별 변화 |
| Claim ID | `CLM-RGT-0001`, `CLM-MEM-0001` | 대상에 연결되는 권리·기억·기록 facet |
| Set ID | `SET-LIN-001` 등 | 조합·완성 목표 |

### 7.2 Core master-index fields

```text
entry_id
source_key
entry_kind
subject_ids
host_id
domain_tags
canon_tier
reader_exposure_window
current_state_and_transition_event
desire_primary_and_secondary
acquisition_or_change_verb
cost_and_burden
integration_proof
refusal_or_loss_path
```

권리, 장비, 실체, 세트의 세부 필드는 각 확장 표에 둔다. 후기 DD 항목에 `final_state`를 필수로 요구하지 않는다.

### 7.3 Migration rules

1. 415행을 먼저 그대로 보존해 출처 인덱스를 만든다.
2. 각 행에 `entry_kind`를 태깅한다.
3. 하나의 출처 행이 여러 종류를 합치면 종류별 `entry_id`로 분리하되 모든 레코드에 같은 `source_key`를 보존한다. 따라서 `source row 1 → normalized record 1..n`이다.
4. 같은 실체를 가리키는 정규화 레코드에 하나의 `entity_id`를 부여한다.
5. 한 레코드는 복수 도메인 태그를 가질 수 있으나 고유 실체 수에는 한 번만 합산한다.
6. 부품은 독립 운용·독립 비용·독립 상실 경로가 있을 때만 별도 실체로 유지한다.
7. 별칭 맵으로 기존 ID와 새 ID를 양방향 추적한다.
8. First 100, GA8, GA10 드라이런은 [[collection-normalization-dry-run-first100-ga8-ga10-v1]]에서 완료했다. `원문 132행 보존`, `정본 승격 0`, `강제 단일분류 0`을 통과했으며 473개 임시 정규 레코드로 펼쳤다.
9. 의미 중복 제거 전에는 “고유 수집품 총수”를 발표하지 않는다.

---

## 8. Reader-Facing Load Budget

415행은 작가용 데이터베이스로는 감당 가능하지만 독자 전면 목표로는 과다하다.

| Scope | Proposed recommendation |
|---|---:|
| 한 장면의 주 수집 목표 | 1 |
| 한 에피소드의 주/보조 목표 | 주 1 + 보조 1 |
| 한 소구간의 활성 목표 | 3–5 |
| 한 대액트의 전면 도메인 | 권장 1–2, 승인 전 상한 아님 |
| 동시에 보이는 프레임·함선 진행 트랙 | 4–6 |
| 동시에 전면화하는 세력 | 3–5 |
| 한 정보 군집의 신규 고유명사 | 3–5 |
| 전면 세트 | 주 1 + 보조 1 |

Rules:

- 백그라운드 항목은 결과·비용·재사용이 생길 때만 다시 전면화한다.
- 새 항목은 기존 항목을 폐기하는 상위 등급 보상이 아니라 새 조합·책임·해석을 열어야 한다.
- 한 소구간에서 발견·획득·조합·완성을 전부 최고 강도로 반복하지 않는다.
- 완성 직전에는 빈칸 수보다 **무엇을 잃거나 인정해야 완성되는지**가 보여야 한다.

### [ASSUMPTION A-03]

의미 중복 제거 전까지 시리즈 전체 `anchor legacy` 목표 수는 잠그지 않는다. 415행을 먼저 재분류한 뒤 독자 전면 목표와 상태 행을 분리해 결정한다.

---

## 9. Category Audit Actions

| Packet | Scope | Output | Gate |
|---|---|---|---|
| P1 | 415행 보존·재키잉 | 출처 인덱스 + 별칭 맵 | 행 누락 0 |
| P2 | C1 사람·관계 | 소유 언어 제거, 동의·이탈 경로 보강 | X03 PASS |
| P3 | C2/C3/C6 | 모체 기체·부품·기술 경계표 | 중복 분류 0 또는 사유 기록 |
| P4 | C4/통제 facet | 긍정 유물과 실행 권리 구분 | 새 정본 추가 금지 |
| P5 | C5 | 선체·모듈·헌장·선원 신뢰 분리 | 전면 트랙 4–6 |
| P6 | C7/C8/통제 facet | 조직·장소와 가입·대표·통행·관할 분리 | 주민/구성원 주체성 보존 |
| P7 | 세트 | GA별 계보·사건·기능·관계·문명 세트 맵 | 주/보조 세트 상한 |
| P8 | 독자 경험 | 티즈·대가·조합·회수 리듬표 | 빈 보상·무료 획득 0 |

Known issue packets that need resolution before canon promotion:

- First 100 표제의 38 대 실제 42 불일치.
- 등록표 ID와 인물/기관 정본 ID 충돌.
- 07호 모체 실체와 구성품·복구 상태 행의 분리.
- 과거 CTF-13/07 수치와 현행 AUX-07 수치의 출처 우선순위 확인.
- C6 개방표준 전면화 시점과 OSR/응급 사양 버전 관계.
- C4 긍정 유물의 존재 여부. 새 유물 추가는 작가 승인 없이는 진행하지 않는다.

---

## 10. Important Author Decisions

아래 세 항목만 정본 또는 독자 전면 구조에 영향을 주는 실제 미결정이다.

1. [[collection-normalization-dry-run-first100-ga8-ga10-v1]] 결과를 보고 행 종류·facet·복수 태그 모델을 전체 415행에 확대할지.
2. C1 독자 전면 명칭을 `영웅`으로 유지할지, 사람의 소유물화를 줄이는 `인물·관계` 또는 `동료·관계`로 바꿀지.
3. 각 대액트에 최소 1개의 긍정적 C4 유물을 의무화할지. 이는 새 콘텐츠 추가이므로 자동 확정하지 않는다.

그 밖의 재키잉, 중복 태깅, 행·실체·상태 분리는 정본 변경 없이 진행 가능한 인덱스 정비다.

---

## 11. Stop Conditions

다음 중 하나라도 발생하면 이 설계를 CANON으로 승격하지 않는다.

- 415행 보존 여부를 증명하지 못한다.
- 사람·공동체·영토가 소유 가능한 보상으로 표현된다.
- 하나의 행이 실체인지 상태인지 권리인지 판별되지 않는다.
- C2/C3/C6 또는 물리 실체/통제 facet 중복을 조용히 이중 계산한다.
- 새 유물·기체·능력·기관을 작가 승인 없이 기존 정본처럼 추가한다.
- 제안된 독자 노출 예산을 사용자 승인 없이 정본 규칙이나 하드 상한으로 강제한다.
- 획득 비용·유지 부담·거절·상실 경로가 없다.
- 정본 승격·원고 승인·PR 병합을 이 문서가 대신한다.

## 12. Current Gate

**DRY RUN COMPLETE — READY FOR AUTHOR DIRECTION — NONCANON**

- 작가용 대상 도메인 수: 8개면 충분.
- 추가로 필요한 것: 새 분야가 아니라 행 종류 축, 기록·권리·기억 facet, 세트 메타 표.
- 등록표 규모: 415행. 의미상 고유 실체 수는 재분류 전 미확정.
- 표본 검증: First 100/GA8/GA10 원문 132행 보존, 임시 정규 레코드 473개, 정본 승격 0.
- 다음 결정: 이 구조를 전체 415행으로 확대할지 작가가 판단.
- 정본 변경: 없음.
- 원고 승인: 없음.
- PR 병합: 없음.

### 12.1 Full-orchestra continuation

The eight independent category passes, full 415-row structural expansion and adversarial integration audit are recorded in [[collection-orchestra-full-normalization-and-desire-matrix-v1]]. The current generated index preserves all source rows and expands them into noncanon typed work records. It does not establish a unique collectible count.

Current continuation gate:

`STRUCTURE PASS — SEMANTIC MERGE HOLD — CANON PROMOTION NOT AUTHORIZED — PUBLICATION NOT AUTHORIZED`
