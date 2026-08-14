# D-20260814 — AXIOM Visual Canon Master

Status: ACCEPTED
Date: 2026-08-14
Decision Owner: User + A00
Canon Scope: VISUAL ONLY
Publication: NOT AUTHORIZED

## Context

AXIOM은 여러 세로형 재생성 과정에서 두상·비율·날개 구조가 흔들렸고, 장갑의 작은 붉은 점·랜덤 데칼을 줄이는 과정이 오히려 기체 정체성을 훼손하는 문제가 반복되었다.

사용자는 2026-08-14 대화에 직접 업로드한 `AXIOM_FINAL(9).png`를 기준으로 "이거먼저 엑시엄으로 정본"이라고 명시 승인했다.

## Decision

`AXIOM_FINAL(9).png`의 외형을 LFX-01 AXIOM의 **Visual Canon Master**로 채택한다.

승인 원본 지문:

- filename: `AXIOM_FINAL(9).png`
- SHA-256: `35b8e3a1ca9cbeb7d9831ccd0d0ac1027630859ef8b73b3d617faa4dde93af31`

잠금 범위:

- 두상과 헤드/목 실루엣
- 흉부·어깨·허리·다리 비율
- 후방 윙/추진 구조의 실루엣
- 흰색/적색/흑연색의 대형 색면 배치
- 제한된 청록 센서 포인트
- 무장·방패·윙의 시각적 정체성

## Important boundary

이 결정은 **시각 정본만 승인**한다. 이미지 내부의 생성 텍스트, 기체 수치, 제작사, 파일럿, 능력, 도입 시기, 획득 사건, 손실 상태 등은 별도 승인 없이 정본이 되지 않는다.

AXIOM의 entity/technical canon 상태는 별도 결정 전까지 기존 문서 통제를 유지한다.

## No-speckle rule

향후 AXIOM 파생 이미지에서 작은 빨간 점·랜덤 삼각형·짧은 색선·장식성 마이크로 데칼을 추가하지 않는다. 그러나 이를 제거하기 위해 승인 원본의 두상·비율·실루엣을 재설계해서는 안 된다.

## Consequences

- AXIOM은 이후 기체 수집 시트의 첫 Visual Canon 기준점이다.
- AXIOM을 다시 처음부터 생성해 대체하지 않는다.
- 후속 기체는 각자 역할·계보·실루엣을 독립 설계하며 AXIOM 복제품이나 단순 색놀이가 되지 않는다.
- 기체는 한 번에 하나씩 인덱스 순서로 검토·승인한다.

## Affected Documents

- `assets/collection/mecha/hold-lfx-01-axiom/README.md`
- `assets/collection/mecha/manifest.csv`
- `assets/collection/mecha/hold-lfx-01-axiom/prompt/axiom-clean-surface-lock-v1.md`
- `docs/06_hardware/` technical canon documents remain authoritative for non-visual facts

## Binary repository note

현재 세션의 GitHub 쓰기 인터페이스에는 대화 첨부 PNG를 파일 파라미터로 직접 전달하는 binary-upload 액션이 노출되지 않았다. 따라서 원본의 정확한 SHA-256과 목표 경로를 기록하며, GitHub에 PNG가 실제 저장됐다고 간주하지 않는다. 바이너리 업로드가 가능해질 때 위 해시와 일치하는 파일만 master 경로에 배치한다.
