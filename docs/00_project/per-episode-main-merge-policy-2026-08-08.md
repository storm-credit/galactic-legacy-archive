# Per-Episode Main Merge Policy — 2026-08-08

Status: CANON — PROJECT PROCESS
Decision ID: D-20260808-02
Decision Owner: Author
Effective Date: 2026-08-08
Publication: NOT AUTHORIZED

## Author Direction

원고는 독자가 GitHub에서 쉽게 확인할 수 있도록 회차별로 작성·검증이 끝날 때마다 `main`에 병합한다.

## Operating Rule

1. 원고 작업은 한 회차 단위로 진행한다.
2. 해당 회차의 구조·인과·동기, 정본·연속성, 문체·전투·대사, 훅·리텐션 검증을 실제로 수행한다.
3. 검증을 통과한 회차는 회차 전용 PR로 `main`에 병합한다.
4. 아직 검토하지 않은 다음 회차를 같은 병합에 묶지 않는다.
5. 관련 작법 기준·결정 기록·검수 보고서는 해당 회차와 함께 병합할 수 있다.
6. `main` 병합은 저장소 열람성과 진행 보존을 위한 것이며, 아래 상태를 자동으로 부여하지 않는다.
   - `AUTHOR-APPROVED`
   - 최종 정본 승격
   - 공개 승인
   - 출판 승인
7. 작가가 별도로 승인하지 않은 원고는 `Status: DRAFT` 또는 `REVISED`, `Canon Check` 상태, `Publication: NOT AUTHORIZED`를 유지한다.
8. 공개·출판·유료연재는 계속 차단하며 issue #26 인간·모바일 테스트는 출판 전 하드 블로커로 유지한다.

## Current Application

- E1 v2와 관련 기준·검수 기록만 별도 PR로 분리하여 `main`에 병합한다.
- 기존 PR #92의 E2~E5는 자동 승인하거나 함께 병합하지 않는다.
- 이후 E2부터도 회차별 작성·검증·병합 순서를 따른다.

## Superseding Interpretation

기존 문서의 “작가 승인 전 원고 PR 병합 금지”는 공개·출판 또는 `AUTHOR-APPROVED` 승격을 막기 위한 통제로 해석한다. 검증된 DRAFT/REVISED 원고의 회차별 `main` 병합은 본 작가 지시에 따라 허용한다.
