# LFX-01 AXIOM / 액시엄

Entity Status: PROPOSED — NONCANON
Visual Status: CANON — USER APPROVED
Visual Canon Scope: EXTERIOR DESIGN / SILHOUETTE / COLOR BLOCKING / HEAD / WING-BACKPACK / SHIELD-WEAPON VISUAL IDENTITY
Canon Promotion: USER AUTHORIZED 2026-08-14 (VISUAL ONLY)
Publication: NOT AUTHORIZED

## Purpose

AXIOM의 사용자 승인 비주얼 정본과 재현 규칙을 보관한다. **2026-08-14 사용자가 직접 업로드한 `AXIOM_FINAL(9).png`를 AXIOM 외형의 Visual Master로 승인했다.**

이 승인은 이미지에 포함된 임의 생성 텍스트·수치·소속·능력·파일럿·획득 시점·손실 상태를 정본화하지 않는다. 기술·서사 정본은 기존 프로젝트 통제 문서와 `docs/06_hardware/`가 계속 우선한다.

## Visual master fingerprint

- source filename: `AXIOM_FINAL(9).png`
- SHA-256: `35b8e3a1ca9cbeb7d9831ccd0d0ac1027630859ef8b73b3d617faa4dde93af31`
- role: **AXIOM VISUAL CANON MASTER**
- approval: explicit user approval, 2026-08-14

## Visual lock carried forward

후속 AXIOM 이미지와 표지·삽화·시트는 새로운 기체를 재설계하지 않는다. 아래 항목은 승인 원본을 기준으로 잠근다.

- original AXIOM head / neck silhouette
- original layered head armor and facial proportions
- original chest / shoulder / waist / leg proportions
- original rear wing / propulsion silhouette
- original large white / crimson / graphite color blocking
- restrained cyan sensor light
- weapon / shield / wing elements read as functional systems
- overall heroic but mechanical silhouette

### CLEAN ARMOR / NO SPECKLE rule

향후 파생 이미지에서는 장갑 표면에 랜덤 점박이를 추가하지 않는다. 단, 이 규칙을 적용한다는 이유로 승인된 원본 기체의 두상·비율·실루엣을 재설계하지 않는다.

금지:
- scattered tiny red dots
- isolated red triangles or squares
- random short red lines
- random orange warning specks
- decorative micro-decals scattered over white armor
- uniform noise-like greebling

허용:
- 큰 장갑 판 단위의 색면
- 구조적으로 필요한 패널 경계
- 실제 관절·정비 해치·냉각·하중 전달 구조
- 제한된 식별 마킹

## Asset layout

```text
hold-lfx-01-axiom/
├─ README.md
├─ reference/
│  └─ axiom-visual-master.png
├─ sheet/
│  └─ axiom-visual-master-sheet.png
└─ prompt/
   ├─ axiom-clean-surface-lock-v1.md
   └─ generation-rules.md
```

## Binary status

현재 연결된 GitHub 쓰기 인터페이스는 UTF-8 텍스트와 Git 객체 작성을 지원하지만, 대화에 첨부된 로컬 PNG를 파일 파라미터로 직접 전달하는 binary-upload 액션은 노출되어 있지 않다. 따라서 **정본 승인·해시·경로·재현 규칙은 Git에 기록 완료**하며, 원본 PNG 자체가 저장소에 실제 존재한다고 보고하지 않는다. 바이너리 업로드가 가능한 경로가 제공되면 위 SHA-256과 일치하는 원본만 `reference/axiom-visual-master.png`에 넣는다.

## Source control

- Visual identity: this file + user-approved master fingerprint
- Technical / narrative facts: project canon precedence + `docs/06_hardware/`
- Generated text inside any image: NOT CANON unless separately approved
