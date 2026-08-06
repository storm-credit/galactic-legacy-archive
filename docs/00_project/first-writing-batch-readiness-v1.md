# First Writing Batch Readiness v1

Status: REVIEW — ACTIVATES ONLY AFTER PRE-WRITING GATE OPEN
Owner Agents: A00 PM / A11 Prose / O01 Canon / N03 Episode / X04 Continuity
Last Reviewed: 2026-08-06
Depends On: `docs/00_project/pre-writing-gate-review-v1.md`, `docs/00_project/manuscript-production-workflow-v1.md`, `docs/99_quality_control/pre-writing-readiness-audit-v1.md`
Used By: 게이트 개방 후 첫 배치 착수
Open Risks: 게이트 개방 전에는 어떤 항목도 실행되지 않는다. D1(플랫폼·자수)과 D3(E1~20 처리) 결정에 따라 §4 작업 내용이 달라진다.

## 1. 권장 첫 집필 범위

> **1차 배치: E1~5 (5회차)**

- D3 = (b) 개정 기반 채택 시: 기존 `manuscript/ga1/001~005-v1.md`를 바탕으로 개정 + 출판 분량 압축 2차 패스.
- D3 = (a) 재집필 채택 시: 장면 카드에서 신규 집필(기존 v1은 참고 폐기).
- 2차 배치 이후: E6~10 → E11~15 → E16~20 → (E21~45는 신규 초고).
- 근거: E1~5는 장면 카드·초고·연속성/음성 감사·레드팀 기록이 가장 두터운 구간이며, E1~5 감사가 압축 대상(E5 최강 압축, 미래기억 밀도)을 이미 특정해 두었다. 2026년 9월 공모전 대응상 최우선 구간이기도 하다.

## 2. 해당 범위의 필수 설계 파일 (집필 전 로드 목록)

### 2.1 통제·우선순위 (항상 최우선)

- `docs/00_project/design-only-scope-restoration-2026-08-03.md` — 정본 우선순위 사다리 §3
- `docs/00_project/effective-canon-status-manifest-v1.md` — 유효 등급, 레거시 헤더 무시 규칙
- `docs/00_project/canonical-name-errata-001.md` ~ `-004.md` (errata-002 이름은 E1~5 등장 인물 아님, 로드만)
- `docs/00_project/manuscript-production-workflow-v1.md` — 8단계 파이프라인

### 2.2 회차 설계 (E1~5)

- `docs/10_story_architecture/ga1-episodes-1-5-noncanon-scene-cards-v1.md` — 검증된 장면 순서 (proxy-signoff §3이 지정한 drafting input; F-25에 따라 지위 표기 정비 필요)
- `docs/10_story_architecture/ga1-episodes-1-20-beat-map-v1.md` — 회차 비트
- `docs/10_story_architecture/first-100-act-map-v2-consolidated.md` — 액트 맥락 (단, A2/A3 요약 드리프트 F-05 주의: 장면 카드가 우선)
- `docs/00_project/ga1-e1-5-first-draft-status-2026-08-03.md` + `docs/99_quality_control/ga1-e1-5-first-draft-continuity-voice-audit-v1.md` — 잔존 S1·압축 지침·삭제 금지 목록 (문서 지위는 NC, 감사 내용은 참조)

### 2.3 인물·기체·세계 상태 (E1 시점)

- `docs/05_characters/protagonist-p001-bible-v1.md` — 리안 (§5 정보 상한)
- `docs/05_characters/rian-index-removal-memory-and-medical-state-v1.md` — 미래기억 한계·신체 비용
- `docs/05_characters/core-canonical-names-and-voice-lock-v1.md` — 6인 이름·음성 잠금
- `docs/05_characters/hero-h001-bible-v1.md`, `docs/05_characters/instructor-i001-field-bible-v1.md`, `docs/05_characters/student-s001-data-cadet-bible-v1.md`, `docs/05_characters/student-m001-medical-rescue-bible-v1.md`
- `docs/03_academy/prison-military-academy-bible-v1.md`, `docs/03_academy/academy-scale-law-calibration-v1.md`
- `docs/03_systems/academy-and-07-opening-operational-state-v1.md` — 07·리안 개막 한계 (proxy-signoff §3 지정)
- `docs/06_hardware/first-frame-bible-v1.md` — 07
- `docs/05_characters/opening-institutional-representatives-v1.md`

### 2.4 문체·검수

- `docs/13_writing_harness/prose-bible.md` (§2 POV 서술은 구식 — gate1 §3 확정이 우선, F-08)
- `docs/07_style/gate1-korean-webnovel-pov-prose-calibration-v1.md` — POV·비율·리듬 정본
- `docs/07_style/noncanon-episode-1-close-third-sample-v2-mobile.md` — 승인 문체 캘리브레이션 기준(비정본)
- `docs/13_writing_harness/storycraft-bible.md`, `docs/13_writing_harness/revision-harness.md`

### 2.5 복선·상한

- `docs/11_mystery/m001-m020-early-clue-episode-ledger-v1.md` — E1~5 단서: E1, E2, E3, E4 (후기 용어 금지 §4)
- `docs/11_mystery/final-payoff-scene-ledger-locked-v1.md` — 조기 노출 금지 확인용
- `docs/11_mystery/secondary-mystery-decoy-and-retirement-ledger-v1.md` — SM-01~03 (Core relation 열은 구식 번호, F-14 리매핑 전까지 질문/답 열만 신뢰)
- `docs/12_losses/named-loss-and-irreversible-transformation-ledger-v1.md` (F-12 부록 정정 전까지 errata-004가 우선)

## 3. 등장인물·기관 상태 (E1 시점 잠금)

### 인물

- **리안**: 교정학원 신입 생도. 약하고 어리고 무면허. 미래기억은 감정적·전략적으로 존재하나 불완전·압축·신체 비용 동반. 현재 감각 정보가 항상 우선(근접 3인칭). 마스터키·권한·소유 없음(시리즈 전체 잠금과 정합).
- **07**: 폐기 대상 적색 밴드가 붙은 약체 훈련 프레임. 서비스 계보 단서 보유. 즉시 강화 금지("no 07 strengthening" — E1~5 감사 삭제 금지 목록).
- **브람 이도, 네라, 하렌, 세린, 미아**: 독립 행동·권한 유지(proxy-signoff §4). 즉시 충성·소유 금지.
- 첫 구조 대상은 리안의 미래기억에 없는 인물(E1 약속 — 장면 카드 Episode 1 promise).

### 기관

- 학원: 인력 공급·법·예산·항로 구조는 `academy-scale-law-calibration-v1.md` 기준. 개막 운영 상태는 `academy-and-07-opening-operational-state-v1.md`가 통제.
- 개막 기관 대표자: `opening-institutional-representatives-v1.md`.
- 백색 도크·중앙지휘 분절 지리는 E14+ 구간 — E1~5에서는 노출 상한 준수.

## 4. 회차별 목표 (요약 — 상세는 장면 카드가 정본)

| 회차 | 제목(카드 기준) | 핵심 목표 |
|---|---|---|
| E1 | 역사에 없는 생도 | 회귀 각성, 07 인지, 기억에 없는 첫 구조, 훅 "[미등록 서비스 권한이 응답했습니다.]" |
| E2 | 한 사람의 벌이 서른여섯 명에게 간다 | 연대 처벌 구조 = 학원 규칙·관계 압력 확립 |
| E3 | 조종사는 기체를 고칠 수 없다 | 정비·소유권 분리 = 세계 제약 확립 |
| E4 | 오르페우스의 빈칸 | 미래기억 불완전성의 첫 실증 |
| E5 | 다섯 번째 답의 시작 | 아크 질문 고정 + 다음 서브액트 유인 (E1~5 감사상 최강 압축 대상) |

각 회차 공통: 물리적 행동 1 + 관계/기관 변화 1 + 훅 1, Archive 표시 1클러스터 이하, 근접 3인칭, 대사 20~30%.

## 5. 작성 전 금지사항

1. 게이트 개방 선언(`Pre-Writing Gate를 OPEN한다...`) 이전 착수 금지.
2. 새 인물·새 세력·새 기술·새 죽음·새 권한·새 설정 사실 창작 금지 — 필요 시 변경 제안서 선행.
3. 영구손실·사망 목록 위반 금지(부활·복구·소급동의 일체).
4. 후기 용어(E101+ 전용) 지문·대사·UI 사용 금지 — m001-m020 원장 §4.
5. 07 조기 강화 금지, 즉시 충성·인물 소유 금지.
6. 기존 v1 초고의 'Locked Development Outcomes'를 정본 근거로 인용 금지(문서 지위 NC — 사실이 필요하면 장면 카드·바이블에서 재확인).
7. 삭제 금지 목록(브람/주노 비용, 독립 권한 구조) 훼손 금지 — 압축 패스 중에도 유지.
8. `Publication: NOT AUTHORIZED` 헤더 제거 금지.

## 6. 완료 판정 기준 (배치 단위)

1. E1~5 각 회차가 workflow §3의 8단계(작성→자체감사→설정대조→문체감사→훅감사→작가승인→수정→정본반영)를 통과.
2. 회차당 분량: 하한 약 5,500자(`[ASSUMPTION]` 공백 포함), **상한 유연**(작가 판정 2026-08-06 "더 길어도 상관없음"). 따라서 2차 패스는 분량 축소가 아니라 밀도·반복 정리(미래기억 밀도, E14/E18 반복, 청문 장면 길이)로 수행 — E1~5 감사의 삭제 금지 목록 유지 확인 포함.
3. 연속성 감사 PASS + `docs/99_quality_control/continuity-issues.md`(신설)에 미해결 S0/S1 없음.
4. 음성 감사 PASS(6인 음성 구별).
5. 훅 감사 PASS(회차말 구체적 다음 문제 + 직전 훅 즉시 회수, 훅 유형 반복표 갱신).
6. 복선 장부 갱신(심은 단서 등록, 조기 노출 없음 확인).
7. 잔존 S1 5건(F-07) 중 E1~5 해당분(압축·E5 밀도) 해소 및 상태문서 재감사 갱신.
8. **작가 승인 기록 존재** — 회차별 승인/수정지시/반려 중 '승인'.
9. 병행 항목(D2 채택 시): 인간/모바일 테스트(`gate8-human-mobile-test-packet-v1.md`, 최소 5인·절반 이상 폰 화면) 실행 결과 기록 — 출판 전 필수, 배치 완료 자체는 차단하지 않음.
10. 배치 회고 완료(훅 반복·음성 이탈·분량 편차·감사 지적 반복).
