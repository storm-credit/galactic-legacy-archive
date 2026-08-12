# 세계관 01·02·03 연결성·회수 감사 (2026-08-13)

Status: QUALITY-CONTROL — DESIGN LINKAGE AUDIT
Owner Agents: A00 PM / A15 Canon / A16 Red Team / X04 Continuity
Last Reviewed: 2026-08-13
Depends On: [[CLAUDE]] §2-2 / §5 / §7 / §11-4, [[decision-log]]
Used By: 세계관 정비 작업, [[prewriting-gate]] 재검토
Open Risks: 본 감사 자체가 23개 고아 문서의 첫 인바운드 링크가 된다 — 재실행 시 이 문서를 참조자에서 제외해야 한다

---

## 0. 범위와 방법

대상은 번호대 01·02·03의 설계 문서 **56개**다.

| 디렉터리 | 문서 |
|---|---:|
| `01_concept` | 2 |
| `01_timeline` | 3 |
| `02_world` | 33 |
| `03_academy` | 6 |
| `03_factions` | 1 |
| `03_systems` | 11 |

집필 대상이 아니라 **설계도 점검**이다. 원고는 건드리지 않았다.

검사는 기계로 수행했고, 판정 전에 세 번 반증했다. 첫 시도에서 "56개 전부 `Owner Agent` 헤더 결손"이 나왔으나 이는 검사의 오류였다 — 문서들은 복수형 `Owner Agents:`를 쓴다. 마찬가지로 §5 3요소의 부재도 한글 키워드만으로 판정하지 않고 영문 대응어(`Plot Use`, `First Reveal`, `Final Payoff`, `Reveal Timing`, `Retrieval`)를 함께 탐색해 확인했다.

---

## 1. 결과 요약

| ID | 검사 | 결과 | 근거 규칙 |
|---|---|---|---|
| **W-01** | 플롯 사용처 / 최초 공개 시점 / 최종 회수 시점 | **0 / 56** | §2-2 (절대 규칙), §5 |
| **W-02** | 인바운드 참조 0인 문서 | **23 / 56 (41%)** | §7 중지 조건, §2-3 |
| **W-03** | `Depends On:` / `Used By:`가 위키링크 | **0 / 56** | §11-4 |
| **W-04** | `Status:` 값이 §5의 4종 안에 있음 | **0 / 56** (28종으로 분화) | §5 |
| W-05 | 헤더 6필드 완비 | 55 / 56 | §5 |

W-05만 양호하다. 나머지 넷은 전부 **연결과 회수**에 관한 것이고, 이 저장소가 CLAUDE.md에서 가장 강하게 선언한 축이다.

---

## 2. W-01 — §5 3요소가 한 문서에도 없다

CLAUDE.md §2-2는 절대 규칙이다.

> 설정을 만들 때 반드시 플롯 사용처와 회수 시점을 함께 기록한다.

§5는 설정 항목의 필수 요소로 `플롯 사용처`, `최초 공개 시점`, `최종 회수 시점`을 지정한다.

**56개 문서 중 이 세 항목을 가진 문서는 0개다.** 한글·영문 양쪽으로 확인했다.

### 왜 중요한가

§7 중지 조건의 첫 항목은 "핵심 설정이 플롯에서 사용되지 않는다"이다. 그런데 각 설정 문서가 자기 사용처를 기록하지 않으므로, **이 중지 조건을 판정할 근거가 문서 안에 없다.** 지금 상태에서 "이 설정은 플롯에서 쓰이는가"에 답하려면 저장소 전체를 사람이 읽어야 한다. 그것이 자동화되지 않는 한 §7은 선언으로만 존재한다.

이는 CLAUDE.md §13이 지적한 실패 양식과 같다 — 하네스가 문서로만 존재하고 강제하는 코드가 없으면 결함이 리뷰를 그대로 통과한다.

---

## 3. W-02 — 23개 문서를 아무것도 참조하지 않는다

위키링크, 파일명 산문 언급, 문서 제목 언급 **세 가지 모두**로 검사했고, 아래 23개는 세 검사 전부에서 0이었다.

### 02_world (12)

- [[census-anchor-and-scale-clarifications-v1]]
- [[fiscal-banking-industrial-input-output-bible-v1]]
- [[ga10-staged-distribution-and-transition-bible-v1]]
- [[ga5-theater-route-and-campaign-map-v1]]
- [[ga7-route-federation-and-denial-war-bible-v1]]
- [[ga9-preservation-regime-and-classification-bible-v1]]
- [[galaxy-612-system-census-and-cluster-atlas-v1]]
- [[imperial-core-and-succession-geography-v1]]
- [[minor-institutions-and-public-life-roster-v1]]
- [[orpheus-incident-original-and-current-packet-v1]]
- [[reproductive-genetic-and-continuity-medicine-bible-v1]]
- [[three-year-epilogue-regional-statistics-v1]]

### 03_systems (7)

- [[academy-and-07-operational-state-e73-100-v1]]
- [[academy-lockdown-07-and-pilot-state-e46-72-v1]]
- [[black-ward-medical-research-operational-state-v1]]
- [[black-ward-supply-freeze-neutral-corridor-v1]]
- [[operational-state-sheet-schema-v1]]
- [[orpheus-equal-assumption-plan-comparison-v1]]
- [[white-dock-operation-and-07-recovery-state-v1]]

### 03_academy (3)

- [[academy-closure-takeover-packages-v1]]
- [[academy-provisional-charter-authority-funding-v1]]
- [[academy-siege-force-and-front-state-v1]]

### 01_timeline (1)

- [[orpheus-34-hour-operation-ledger-v1]]

### 이 목록에서 가장 급한 것

**`03_systems`의 운영상태 문서 두 건이 바로 다음 집필 구간을 덮는다.**

- [[academy-lockdown-07-and-pilot-state-e46-72-v1]] — E46~72
- [[academy-and-07-operational-state-e73-100-v1]] — E73~100

배치 1(E1~5)이 닫힌 지금, 집필은 E6~20을 지나 곧 이 구간에 닿는다. 그 시점에 이 문서들이 장면 카드·회차 설계와 연결돼 있지 않으면, 집필 에이전트는 **이 문서가 있는 줄 모르고 같은 설정을 다시 만든다.** 이것이 §3이 금지하는 복제이고, 실제로 이 저장소에서 이미 한 번 일어났다 — 개명 전파 실패(§12 사례)와 같은 구조다.

또 하나 눈에 띄는 것은 [[white-dock-operation-and-07-recovery-state-v1]]이다. 백색 도크는 E5 종료 훅이 15일 뒤로 예고한 사건인데, 그 운영상태 문서를 아무것도 가리키지 않는다.

### 주의 — 백링크 0이 곧 "플롯 미사용"은 아니다

이 23개가 서사에서 안 쓰인다는 뜻이 아니다. 장면 카드나 회차 설계가 내용을 쓰면서 출처를 적지 않았을 수 있다. 그러나 §2-3(플롯을 만들 때 관련 설정 문서와 연결한다)과 §11-4(헤더가 계보 그래프의 간선이다)가 요구하는 것이 바로 그 기록이다. 그리고 W-01 때문에 문서 자체로도 사용 여부를 알 수 없다. **어느 쪽이든 지금은 확인 불가 상태다.**

---

## 4. W-03 — 계보 그래프의 간선이 전부 산문이다

§11-4는 명시한다.

> `Depends On:` / `Used By:` / `Source Cards:` 헤더도 위키링크로 적는다. 이 헤더가 문서 계보 그래프의 간선이다.

**56개 전부가 산문이다.** 52개는 두 필드 모두 링크가 없다.

실제 값의 형태:

```
Depends On: 612-system census, node economy scale and lattice physics
Used By: GA5 campaign design and route contest episodes
```

파일명이 아니라 개념 서술이므로 기계 변환이 불가능하다. 이는 PR #58·#69~#72에서 발견해 미해결로 남긴 부채와 **같은 종류이며 범위가 더 넓다.** 그 PR들은 38개 문서였고, 여기에 56개가 더 있다.

C1 검사는 이것을 잡지 못한다 — 깨진 링크가 아니라 **링크의 부재**이기 때문이다.

---

## 5. W-04 — 무엇이 정본인지 기계로 알 수 없다

§5는 상태값을 넷으로 지정한다.

```
Status: DRAFT | REVIEW | CANON | DEPRECATED
```

실제로는 **28종**이 쓰이고 있다. 상위 분포:

| 값 | 문서 수 |
|---|---:|
| `REVIEW` | 25 |
| `REVIEW — EXECUTION LOCK CANDIDATE` | 5 |
| 나머지 26종 | 각 1 |

나머지에는 `WORKING CANON — CENSUS INTERPRETATION`, `CANON FOR DESIGN / TEMPORAL MODEL NOT YET LOCKED`, `REVIEW — CANON LOCK CANDIDATE` 같은 자유 서술이 섞여 있다.

**평문 `CANON`인 문서가 하나도 없다.** `CANON v1`이 1건, `CANON FOR DESIGN`이 1건, `CANON CORRECTION — …`이 1건이다.

부가 설명 자체는 유용하다. 문제는 그것이 **상태값을 대체**했다는 점이다. 그 결과 "정본만 골라라", "DRAFT는 인용하지 마라" 같은 기본 질의를 기계로 처리할 수 없고, 후속 에이전트는 `WORKING CANON`과 `REVIEW — CANON LOCK CANDIDATE`의 권위 차이를 추측해야 한다.

---

## 6. 권고 (실행 아님 — 작가 결정 대기)

우선순위 순이다.

1. **E46~100 운영상태 2건을 먼저 연결한다.** 집필이 곧 닿고, 미연결 상태로 도달하면 설정 복제가 발생한다. 범위가 작아 즉시 처리 가능하다.
2. **`Status:` 값을 §5의 4종 + 부가 설명 형식으로 정규화한다.** 예: `Status: CANON — 세부 설명`. 검사 하나로 강제 가능하다.
3. **§5 3요소를 문서 하단 고정 절로 도입한다.** 56개 전부에 소급하는 것은 큰 작업이므로, 신규·개정 문서부터 의무화하고 기존 문서는 집필이 닿는 순서로 채우는 방식을 제안한다.
4. **`Depends On:` / `Used By:` 위키링크화.** 산문이라 기계 변환이 안 되므로 문서당 판단이 필요하다. 앞의 PR 부채 38건과 합쳐 한 번에 설계하는 편이 낫다.

## 7. 검사 자동화 제안

CLAUDE.md §13은 "검증기가 잡을 수 있는 종류의 결함을 사람이 리뷰로 막으려 하지 않는다"고 못 박는다. 위 넷 중 셋은 기계로 강제할 수 있다.

| 신규 검사 | 대상 | 제안 등급 |
|---|---|---|
| C7 | `Status:` 첫 토큰이 `DRAFT`/`REVIEW`/`CANON`/`DEPRECATED` 중 하나 | WARN → 정규화 후 ERROR |
| C8 | `docs/` 설계 문서의 인바운드 참조 0 검출 | WARN |
| C9 | `Depends On:` / `Used By:`에 위키링크 최소 1개 | WARN |

§13 규칙에 따라 각 검사는 `--selftest` 픽스처를 함께 갖춰야 한다. **검사가 실제로 발화하는지 증명하지 못하면 그 검사는 없는 것과 같다.**

---

## 8. 이 감사가 하지 않은 것

- 내용 모순 검사(연대·수치·지리 충돌)를 하지 않았다. 이번은 **연결성과 회수 장부** 축이다.
- 04~13 번호대와 `99_quality_control`은 범위 밖이다.
- 아무 문서도 수정하지 않았다. 본 문서만 추가했다.
