# LFX-01 AXIOM / 액시엄

Status: PROPOSED — NONCANON
Visual Status: USER-SELECTED BASELINE / REFERENCE-LOCKED
Canon Promotion: NOT AUTHORIZED
Publication: NOT AUTHORIZED

## Purpose

AXIOM의 사용자 선택 비주얼 기준과 생성 프롬프트를 함께 보관한다. 이 폴더의 이미지·프롬프트가 이름·능력·파일럿·수치·획득 시점·손실 상태를 자동으로 정본화하지 않는다.

## Visual master rule

AXIOM 후속 이미지는 새로운 기체를 재설계하지 않는다. 사용자 선택 원본 AXIOM의 실루엣과 주요 구조를 기준으로 재현하고, 사용자가 별도로 승인한 변경만 적용한다.

### Locked identity

- original AXIOM head / neck silhouette 유지
- original chest, shoulder, waist, leg proportions 유지
- original rear wing / propulsion silhouette 유지
- original large white / crimson / graphite color blocking 유지
- restrained cyan sensor light only
- hero-machine presence without copying a published mecha franchise
- weapon / shield / wing elements must read as functional systems rather than decoration

### CLEAN ARMOR / NO SPECKLE lock

장갑 표면의 작은 색점과 랜덤 장식을 디자인 디테일로 사용하지 않는다.

금지:
- scattered tiny red dots
- isolated red triangles or squares
- random short red lines
- random orange warning specks
- decorative micro-decals scattered over white armor
- uniform greebling or noise-like panel marks
- dot-like accent distribution across shoulders, arms, hips or legs

허용:
- 큰 장갑 판 단위의 명확한 색면
- 구조적으로 필요한 패널 경계
- 실제 관절·정비 해치·냉각·하중 전달을 설명하는 선
- 제한된 번호/식별 마킹

원칙: **가까이서는 정교한 기계 구조, 멀리서는 깨끗하고 명확한 대형 색면과 실루엣**.

## Asset layout

```text
hold-lfx-01-axiom/
├─ README.md
├─ reference/
│  └─ axiom-visual-master.*
├─ sheet/
│  └─ axiom-clean-surface-sheet-v1.*
└─ prompt/
   ├─ axiom-clean-surface-lock-v1.md
   └─ generation-rules.md
```

The repository connector used in this session supports text writes directly; binary image files must be attached/uploaded through a binary-capable path before they can appear under `reference/` and `sheet/`. The prompt and lock metadata are authoritative for future generation until the binary reference is committed.

## Source control

Canonical or proposed technical facts remain controlled by `docs/06_hardware/`, especially the AXIOM visual-development audit and lineup architecture. Generated text inside an image is never canon by itself.
