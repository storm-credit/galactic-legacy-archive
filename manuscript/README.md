# manuscript/ — 원고 트리

Status: CANON PROJECT CONTROL
Effective Authority: PC
Story Canon Effect: NONE
Publication: NOT AUTHORIZED
Owner Agents: A00 PM / A11 Prose & Serialization / O02 Gates
Last Reviewed: 2026-08-22
Depends On: [[manuscript-production-workflow-v1]], [[gate1-korean-webnovel-pov-prose-calibration-v1]], [[decision-log]]
Used By: 원고 집필, C3/C4/C5 검사, [[episode-briefs]]
Open Risks: 재집필 배치 승인 범위가 아직 열려 있다

## 1. 현재 상태 — 비어 있음

2026-08-22 작가 결정 `D-20260822-01`로 **E1–E100 초고 전체를 폐기**했다. 이 폴더에 원고 파일은 없다.

폐기 직전 상태는 `70a2ebb577c48857af1d524c97b60c41baac89b1`이 보유한다. 121개 파일, 100회차, 약 69만 7천 자다. 복원이 필요하면:

```bash
git checkout 70a2ebb577c48857af1d524c97b60c41baac89b1 -- manuscript/
```

폐기 사유와 파급 범위는 [[decision-log]] `D-20260822-01`이 보유한다. 이 파일은 사유를 복제하지 않는다.

## 2. 폐기된 것과 남은 것

| | |
|---|---|
| 폐기 | E1–E100 원고 산문 전체 (v1·v2·v3) |
| 유지 | 세계관·설정집·액트맵·상세 회차 카드·Context Pack·Writer Activation·Collection Desire·손실/회수 장부 — **설계층은 하나도 건드리지 않았다** |

즉 다시 쓸 때 참조할 설계는 전부 그대로다. 버린 것은 그 설계를 문장으로 옮긴 결과물뿐이다.

## 3. 재집필 규칙

1. **폐기된 원고를 참조하지 않는다.** git 이력에 남아 있지만 문체·구성의 기준으로 삼지 않는다. 그러라고 버린 것이다.
2. 회차를 쓰기 전에 [[episode-briefs]]와 해당 서브액트 허브를 먼저 연다 — 액트맵·상세 카드·Context·Writer Activation·CLSET이 거기 모여 있다.
3. 집필 순서와 QC 순서는 [[manuscript-production-workflow-v1]]을 따른다. C4 분량 하한은 **사후 검사**이며 집필 목표가 아니다 (CLAUDE.md §20).
4. 파일명은 `NNN-제목-vN.md`, 위치는 `manuscript/gaN/`.
5. 헤더는 v2 스키마를 쓴다 — `Status`, `Episode`, `Source Cards`, `Canon Check`, `Publication`. `Publication: NOT AUTHORIZED`는 작가의 별도 승인 없이 바꾸지 않는다 (C3가 강제).
6. **원고 본문에 위키링크를 넣지 않는다** (CLAUDE.md §14-5). 링크는 헤더에만 쓴다.

## 4. 집필 승인 범위

재집필 배치 승인은 아직 정해지지 않았다. 작가가 범위를 정하면 [[decision-log]]에 기록하고 이 절을 갱신한다.

승인 없이 원고를 생산하지 않는다 — [[effective-canon-status-manifest-v1]] §5의 `BL` 조항이다.
