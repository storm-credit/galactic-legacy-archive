# Collection Normalization Dry Run — First 100 / GA8 / GA10 v1

Status: PROPOSED — NONCANON
Owner Agents: A00 Collection Orchestrator / classification agents `019fe6e8-8c8b-7032-9972-f0d35ce4ff30`, `019fe6e8-8d09-7bf0-948f-fab4413e82eb`, `019fe6e8-8d7e-7b21-ba3d-e0923673fbab`
Last Reviewed: 2026-08-09
Depends On: [[collection-desire-master-architecture-and-index-audit-v1]], [[first-100-collectible-registry-v1]], [[ga8-collection-registry-v1]], [[ga10-final-collection-and-payoff-registry-v1]]
Canon Promotion: NOT AUTHORIZED
Publication: NOT AUTHORIZED

## 1. Scope and Result

서로 성격이 다른 세 등록표의 **원문 132행을 삭제·개명 없이 보존**하고, 각 행을 제안된 `entry_kind`와 C1–C8 도메인 태그로 분류했다.

| Source packet | Source rows | Rows requiring split |
|---|---:|---:|
| First 100 | 42 | 39 |
| GA8 | 36 | 31 |
| GA10 | 54 | 54 |
| **Total** | **132** | **124** |

- 원문 출처 키 고유성: 132/132.
- 제안 정규 레코드: 473.
- 정본 승격: 0.
- 원문 행 삭제·개명: 0.
- 강제 단일 분류: 0. 복합 행은 같은 `source_key`를 공유하는 복수 `entry_id`로 분리했다.
- 이 결과는 분류 가능성 검증이며, 실체 병합과 최종 `entity_id` 확정이 아니다.

## 2. Artifacts

- Source-row audit: `data/collection-normalization-dry-run-source-rows-v1.csv`
- Expanded normalized records: `data/collection-normalization-dry-run-expanded-records-v1.csv`

Source-row CSV는 132개 원문 행과 그 행에서 파생된 임시 레코드 ID 목록을 보여 준다. Expanded CSV는 `source row 1 → normalized record 1..n` 계약을 실제 행으로 펼친다.

## 3. Entry-Kind Frequency

| Entry kind | Source rows tagged |
|---|---:|
| `ENTITY` | 80 |
| `RELATIONSHIP` | 52 |
| `CONTROL_CLAIM` | 115 |
| `STATE_TRANSITION` | 78 |
| `LOSS_OBLIGATION` | 71 |
| `NARRATIVE_PROMISE` | 46 |
| `SET` | 31 |

한 원문 행에 여러 종류가 붙을 수 있으므로 합계는 132를 초과한다.

## 4. Domain Frequency

| Domain tag | Source rows tagged |
|---|---:|
| `C1` | 88 |
| `C2` | 18 |
| `C3` | 9 |
| `C4` | 9 |
| `C5` | 7 |
| `C6` | 79 |
| `C7` | 114 |
| `C8` | 36 |

도메인 역시 복수 태그다. 빈도가 낮다고 새 정본 항목을 채워 넣지 않는다.

## 5. Acceptance Checks

| Check | Result |
|---|---|
| 세 원문 파일의 대상 제목 수와 분류 행 수 일치 | PASS |
| 출처 키 누락·중복 | PASS — 0 |
| 허용되지 않은 `entry_kind` | PASS — 0 |
| C1–C8 밖 도메인 태그 | PASS — 0 |
| 복합 행의 복수 `entry_id` 생성 | PASS |
| 정본 승격·원고 승인·PR 병합 | PASS — 모두 0 |
| 사람·영토·기관의 소유물화 방지 | REVIEW REQUIRED during full semantic merge |

## 6. Interpretation

드라이런은 8개 작가용 대상 도메인만으로도 표본을 태깅할 수 있음을 보였다. 그러나 행 대부분이 실체·관계·권리·상태·손실을 동시에 서술하므로, 8개만으로 단일 분류하면 의미가 손실된다. 따라서 **8개 도메인 + 행 종류 축 + 통제 facet + 세트 표**가 현재 자료 구조에 더 적합하다.

## 7. Stop Conditions

다음 단계인 415행 전체 정규화는 작가가 구조 확대를 승인하기 전 자동으로 수행하지 않는다. 이 드라이런은 새 유물·기체·능력·기관을 만들지 않으며 기존 정본을 변경하지 않는다.

### Red-team correction

- `G10-P03 / Ownership of Collected Legacy`는 새로운 독립 실체가 아니라 기존 대상들의 관계·통제권·상태·손실·세트 결산이다. 초기 드라이런의 잘못된 `ENTITY` 레코드를 제거한 뒤 임시 레코드 ID를 `DRY-CL-R-000001`부터 `DRY-CL-R-000473`까지 다시 연속 부여했다.
