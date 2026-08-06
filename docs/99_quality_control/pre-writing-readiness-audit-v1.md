# Pre-Writing Readiness Audit v1

Status: REVIEW — AUDIT RECORD
Owner Agents: O02 Gates / O01 Canon / X01 Logic / X04 Continuity / L01 Prose
Last Reviewed: 2026-08-06
Depends On: 저장소 전체 정본 문서 (감사 방법: 7영역 병렬 정밀 감사 + 발견 항목별 독립 반증 검증, 도구 호출 405회)
Used By: `docs/00_project/pre-writing-gate-review-v1.md`
Open Risks: 본 감사는 AI 감사이며 인간 독자 검증(issue #26)을 대체하지 않는다.

## 0. 총평

> **S0: 0건 / S1: 2건(전량 작가 결정 대기) / S2: 13건(문서 정정 수준) / S3: 12건**

설계 자체의 모순으로 집필이 막히는 항목은 없다. S1 2건은 "설계 결함"이 아니라 "작가가 아직 결정하지 않은 사항"이며, S2는 대부분 2026-08-03 문서가 2026-08-04~05 상세설계 완료를 반영하지 못한 레지스트리 노후화다. 불변 정본 잠금(마스터키 부재, 하렌 제재, 린 오사, 5층 혈제독, 영구손실 7종)과 충돌하는 문서는 **발견되지 않았다**.

## 1. 시점 (POV) — READY

- 리안 근접 3인칭이 정본으로 확정: `docs/07_style/gate1-korean-webnovel-pov-prose-calibration-v1.md` §3 ("리안 근접 3인칭을 기본 정본 시점으로 채택한다"), §11 "CLOSE THIRD SELECTED".
- 1인칭은 작중 증언·일지·기록 단편에만 허용. 장면당 초점 인물 1명. 시리즈 전체 리안 POV 55~65% 목표까지 수치화.
- 비리안 POV 진입 조건과 "저비용 정보 공개 목적 회전 금지"는 gate1 §9; GA2+ 상세 카드가 씬 단위로 초점을 지정.
- 결함: `docs/13_writing_harness/prose-bible.md` §2가 여전히 "1인칭 또는 밀착 3인칭 중 샘플 테스트 후 고정"으로 서술(F-08, S2) — 확정 결정 미반영. 하네스만 읽는 집필자가 POV를 열린 문제로 오인할 수 있음.

## 2. 문체 — READY

- 중문장 기본 호흡, 단문은 충격·선택 예약: prose-bible §3, CLAUDE.md 절대규칙 5.
- 승인 문체 변형: "E1 v2 모바일형 근접 3인칭"(`docs/07_style/noncanon-episode-1-close-third-sample-v2-mobile.md`) — gate8 내부 평가 4종(4.42~4.75/5), 레드팀, AI 프록시 8세션 통과.
- 한계: 승인 근거가 전부 AI 프록시. 인간·실기기 검증은 `gate8-human-mobile-test-packet-v1.md` "READY — HUMAN RESULTS NOT YET COLLECTED"(F-09, S2). 인간 결과에 따라 E1~5 재수정 가능성이 override §4에 명시됨.

## 3. 정보 상한 — READY

- 리안이 아는 것: protagonist bible §5 + `rian-index-removal-memory-and-medical-state-v1.md` §2~5가 GA별로 정의(미래기억 불완전·압축·신체 비용).
- 독자가 알아도 되는 것: `m001-m020-early-clue-episode-ledger-v1.md`가 스레드당 3개 이상 복선 회차를 잠그고, §4가 E1~100에서 후기 용어("Authority F/G", "unrecorded connector" 등) 사용을 금지.
- 잔여(S3): E1 훅 "[미등록 서비스 권한이 응답했습니다.]"와 후기 금지 용어 사이 경계 판정 미기록(F-19); 보조 POV 씬의 단서 상한 규칙이 암묵적(F-20).

## 4. 회차 구조 — 조건부 READY (S1 1건)

- 회차 8요소 공식, 훅 회전, 금지 클리프행어 정책: storycraft-bible·prose-bible에 LOCKED.
- 대사 20~30% / 행동 45~60% / 설명 15~25% / UI 3~5% 미만: gate1 §5.
- **F-01 (S1, CONFIRMED)**: 회차당 분량은 "5,500~6,500자 진단 범위"뿐, 공백 포함/제외 기준이 저장소 어디에도 없고(전역 grep 무일치) 목표 플랫폼(문피아/카카오페이지/네이버시리즈)·공모전 선정 기록도 없음. project-charter는 2026년 9월 공모전 대응을 명시(잔여 약 1개월). 이 상태로는 E1~20에 이미 S1으로 걸려 있는 "출판 분량 압축 패스"의 목표치를 정할 수 없음. → 작가 결정 D1.

## 5. 장면 구조 — READY

- 한 장면 = 한 초점, 장면당 목표·갈등·상태변화·다음 문제 필수: 장면 카드 공유 제약 + production standard.
- E1~100 장면 카드 16파일 전량 실재, E21~45 변경은 `ga1-e21-45-continuity-change-record.md`로 봉합.
- 결함: `first-100-act-map-v2` A2/A3(E6~15) 한 줄 요약이 실제 카드와 불일치(F-05, S2 CONFIRMED — v2 E6="07 소유권"인데 실제 E6="열세 칸", E13="서비스 권한"인데 실제 "네라 비크, 사망" 등). 카드·초고가 옳고 요약이 낡음. 변경 기록 필요.

## 6. 전투 묘사 — READY (S0·S1 없음)

- 5단계 전투 스케일, S0~S6 센서 사다리, T0~T6 열대역, 탄약 기준선, 12개 하드 금지, 전투 전 10항목 캘리브레이션 체크리스트, 6범주 손실 스키마·비가산 편성 회계: `docs/07_military/` 4개 바이블에 LOCKED, 레드팀 S0=0.
- "독자 대면 전투는 3~7개 유의미 편성만 추적", 함수 언급 전 목표·지원·실패조건 명시.
- 액션 샘플 2종(white-dock, central-key)이 다이어그램·캘리브레이션 수치와 정합함을 확인.
- 잔여(S3): 함대급 교전 산문 샘플 부재 — 첫 함대전은 GA2 E122+이므로 GA2 B02-01 착수 전 비정본 샘플 1편 권장(F-21).

## 7. 기관·정치 묘사 — READY

- 회의장면 필수 상태변경 규칙(권한/증거/배분/관계/기한/접근/책임 중 1+), "10회차당 물리 임무" 규칙: production standard.
- 표결·차터 극화 검증: gate8 package-charter·central-key 샘플.
- 기록전쟁: 설계측 규율(번역모드·출처패널·진본성 규칙)은 충실. 전용 산문 샘플은 없음 — GA8(E801+) 착수 전 제작 권장(F-22, S3).

## 8. 설정 노출 — READY

- 회차당 Archive 표시 1클러스터 제한, 제국/격자/Seed 전면 설명 금지(장면 카드 공유 제약), 기술 묘사의 기능성 규칙(행동·위험·사회·심리), 시스템창=선택·갈등·미스터리·보상 장치(CLAUDE.md 절대규칙 8).
- E1~20 초고 감사에서 미래기억·기록공개 밀도가 S1로 지적되어 압축 패스 대상으로 특정됨(F-07과 연동).

## 9. 복선 관리 — READY (S2 각주 2건)

- M-001~M-020 결정적 회차·장소·POV·비용·제도변화 잠금(±2화 변경통제): `final-payoff-scene-ledger-locked-v1.md`.
- 조기 복선: `m001-m020-early-clue-episode-ledger-v1.md` (GA1 내 E1,2,3,4,6,7,8,11,13,18,19,20).
- **F-13 (S2, CONFIRMED)**: M-004(하렌) 결정 장면 E794 잠금이 errata-004의 판결 E783/CY 745-08과 약 11화 충돌 — ledger 자체의 ±2화 규칙 위반이며 변경 기록 없음. GA7 상세 카드가 우선함을 각주로 명기 필요.
- **F-14 (S2, CONFIRMED)**: `secondary-mystery-decoy-and-retirement-ledger-v1.md`의 Core relation 열이 구식 M-번호 사용(예: SM-03이 하렌을 M-003으로 표기하나 잠금본은 M-004). SM-01~03 활성 구간(E2~20)이 첫 배치와 직접 겹침 — 리매핑 또는 경고 헤더 필요. 질문/거짓답/실답/은퇴 열 자체는 정확.

## 10. 영구상태 반영 — READY (S2 1건)

- 5인 사망·영구손실: 회차·원인·행위주체성·애도 창·무반전 조항 명시. 25화 블록별 손실 상태표 + 부활 공격 레드팀이 부활 방지 메커니즘으로 작동.
- 시대별 권한 상태(17모듈·43커넥터·하렌 제재): `ga1-10-state-checkpoint-matrix-v1.md` + `ga1-10-operational-checkpoint-snapshots-v1.md`로 GA 경계·블록 단위 추적 가능.
- **F-12 (S2, CONFIRMED)**: 작가용 단일 손실 원장 `named-loss-and-irreversible-transformation-ledger-v1.md`(08-03판)가 구식 — (1) L-H05 'Rin Osa' 표기(정본 Lin Osa), (2) "하나의 장부"(정본은 네 개의 원장), (3) 세라트 현재 AI 3명 사망·아르디스 73t 봉인 모듈 누락, (4) 조사 창 E789~798(정본 E766~790, 판결 E783). "충돌 시 errata-004·GA7 상세가 통제" 부록 1절로 해소 가능.

## 11. 숫자·연대 정합성 — READY (대부분 일관)

- 하렌 제재(14개월/12년/영구/15년): 전역 grep 기준 상충 수치 없음. "serving sentence" 축약 약 40곳은 errata-004의 해석 규칙("제재 레짐 지속 의미")이 통제.
- 누적 인간 사망 20,996·세라트 AI 3명 분리 계상·17모듈(12/3/1/1)·43커넥터(32/9/2): 파일 간 일관.
- 에라타 전파: 001(메사 린) 완전, 003(승무원 42명) 완전, 004(하렌 연표) 완전. **002(도안 미르→미르 카오)는 미전파(F-04, S2 CONFIRMED)** — 에라타 발행(08-03) 이후 작성된 GA5 상세 파일 10여 개가 전부 구명 사용, 정본명 '미르 카오'는 저장소 전체에서 에라타 파일 포함 2곳뿐. 교차감사(S1=0 판정)가 이름 에라타 대조를 누락했음을 시사 — 교차감사 체크리스트에 이름 에라타 대조 추가 필요.
- 로마자 'Rin/Lin Osa' 혼재가 구형 파일 5곳 잔존(F-23, S3) — 한글 표기는 전 파일 일관.

## 12. 정본 충돌 위험 — 낮음 (구조 완비, 레지스트리 노후)

- 충돌 해소 사다리 2건(restoration §3, manifest §6), PC/WC/AS/FR/DD/NC/BL 등급 체계, "레거시 헤더보다 매니페스트 우선", "원고 문장은 정본을 만들 수 없다" 규칙 완비.
- 비정본 파일 방화벽: noncanon 샘플 6종 전부 NC 헤더 보유.
- E1~20 초고 지위: restoration §8의 명시적 supersede로 기계적으로는 해소되어 있으나, 구 상태문서(`ga1-e1-5-first-draft-status` 등)가 'CANON PROJECT CONTROL' 헤더를 유지해 오독 위험(F-06, S2) — NC 배너 주석 필요. 특히 e1-5-status의 'Locked Development Outcomes' 12건을 정본으로 오독하면 프로즈→정본 오염 발생.
- 레지스트리 노후(F-10, F-11, S2): manifest §3 "canonical name errata files" 문구가 003/004를 자구상 미포괄, manifest §4가 E101~1100을 여전히 'DD'로 기재, deliverables-index는 errata-001만 등재, decision-log 마지막 항목이 D-20260803-07(에라타 3건·상세설계 완결·게이트 상태 미기록 — CLAUDE.md 절대규칙 10 위반 상태).

## 13. S0~S3 통합 목록

검증 방법: 각 발견을 독립 검증자가 반증 시도(CONFIRMED = 반증 실패, DOWNGRADED = 부분 반증으로 심각도 하향, REFUTED = 기각·목록 제외).

### S0 — 없음

### S1 (첫 배치 착수 차단 — 전량 작가 결정 대기)

| ID | 발견 | 위치 | 해결 |
|---|---|---|---|
| F-01 | 플랫폼·공모전 미확정 + 자수 산정 기준 미정의 | gate1 §5, project-charter:17, revision-harness Pass 12 | **부분 해소(2026-08-06 작가 판정)**: 분량 상한 유연("더 길어도 상관없음") → 압축 패스는 밀도·반복 정리로 재정의, 본 항목 S1→S2 하향. 잔여: 플랫폼/공모전 선정·공백 기준은 출판 전 확정(`[ASSUMPTION]` 공백 포함·하한 5,500자) |
| F-02 | issue #26 지위 3문서 상호 모순(집필 전 vs 출판 전 블로커) — 핵심은 restoration §8의 supersede가 override의 재분류까지 무효화했는지의 해석 분기 | dry-audit §5 vs autonomous-override §4 vs restoration §4 | **해결 제안서 제출**: `docs/00_project/issue-26-status-resolution-proposal-v1.md` (출판 전 블로커로 신규 작가 판정, 위험 통제 6항). 작가 승인 대기 |

### S2 (첫 배치 중 필수 정정 — 문서 패치 수준)

| ID | 발견 | 위치 |
|---|---|---|
| F-03 | GA10 B10-03(E1051~1075) 설계 파일 8종이 `main`에 부재 — **원인 확정: PR #88(`Detail GA10 episodes 1051–1075 through the last central fleet`)이 OPEN 상태로 미병합**(브랜치 `agent/ga10-b10-03-e1051-1075-detail`에 카드 3파일·레드팀·수집상태·기관상태·캐스트·진행상태 실존, main 대비 ahead 8 / behind 1). 완료 선언 PR #89만 병합되어 "1,000/1,000" 주장이 main 기준 975/1,000. 해결 = PR #88 병합(재생산 불필요) 후 GA10 최종 교차감사의 B10-03 대상 실재 재확인 | docs/10_story_architecture/detail/ (e1044-1050 다음이 e1076-1085) / PR #88 |
| F-04 | 에라타-002 '미르 카오' GA5 상세설계 미전파 | ga5-vesper-opening-command 외 10여 파일 |
| F-05 | first-100-act-map-v2 A2/A3(E6~15) 요약 드리프트, 변경 기록 없음 | first-100-act-map-v2-consolidated.md |
| F-06 | E1~20 구 상태문서의 'CANON PROJECT CONTROL' 헤더 오독 위험 + 'Locked Development Outcomes' 오염 위험 | ga1-e1-5/e6-20-first-draft-status, manuscript/ga1/ 헤더 |
| F-07 | E1~20 초고 잔존 S1 5건(압축·미래기억 밀도·E14/E18 반복) 2차 패스 미실행 | ga1-e1-5/e6-20-first-draft-status |
| F-08 | prose-bible §2 POV '미확정' 서술 잔존 | docs/13_writing_harness/prose-bible.md §2 |
| F-09 | 인간·실기기 모바일 검증 미실행(승인 근거 전부 AI 프록시) | gate8-human-mobile-test-packet-v1.md §12 |
| F-10 | manifest §3/§4·deliverables-index 노후(에라타 003/004, E101~1100 완료 미반영) | effective-canon-status-manifest-v1.md |
| F-11 | decision-log가 2026-08-03 이후 정본 변경 미기록 | decision-log.md (마지막 D-20260803-07) |
| F-12 | named-loss ledger 구식(Lin Osa·네 원장·세라트 AI·아르디스 73t·조사 창) | docs/12_losses/named-loss-...-v1.md |
| F-13 | M-004 결정 장면 E794 vs 판결 E783 — ±2화 규칙 초과 충돌, 미기록 | final-payoff-scene-ledger-locked-v1.md |
| F-14 | secondary-mystery ledger Core relation 열 구식 M-번호 | secondary-mystery-decoy-and-retirement-ledger-v1.md |
| F-15 | continuity-issues.md 부재(revision-harness Pass 4 참조 대상) + S0~S4/S0~S3 등급 대응표 부재 | revision-harness.md:62 → `docs/99_quality_control/continuity-issues.md` 생성 필요 |

### S3 (개선 권장 — 차단 아님)

| ID | 발견 | 위치 |
|---|---|---|
| F-16 | 우선순위 사다리 이원화(restoration §3 7단계 vs manifest §6 6단계) | 두 PC 파일 상호 참조 부재 |
| F-17 | 비정본 샘플 보관 위치 규칙 불일치(experiments/ 규정 vs 실제 docs/07_style/) | prewriting-gate.md §1 |
| F-18 | first-20-causality-map-v1이 폐기 구조를 supersede 표시 없이 잔존(E1 프롤로그 구판) | first-20-causality-map-v1.md |
| F-19 | E1 훅 '미등록 서비스 권한' vs 후기 금지 용어 경계 판정 미기록 | m001-m020 원장 §4 |
| F-20 | 보조 POV 씬의 미스터리 단서 상한 규칙 암묵적 | gate1 §9 |
| F-21 | 함대전 산문 샘플 부재(GA2 B02-01 전 권장) | docs/07_style/ |
| F-22 | 기록전쟁 전용 산문 샘플 부재(GA8 전 권장) | docs/07_style/ |
| F-23 | 'Rin/Lin Osa' 로마자 혼재 구형 파일 5곳 | m001-m020 원장 E762 항목 외 |
| F-24 | 게이트 문서군(08-03판) 상태 서술 시효 경과 — 판정 자체는 유효 | dry-audit §10, evidence-matrix §8 |
| F-25 | E1~5 장면 카드가 비정본 딱지인 채 v2가 존재하지 않는 파일명(`ga1-episodes-1-5-scene-cards-v1.md`) 인용 | first-100-act-map-v2 A1절 |
| F-26 | 손실·payoff 장부의 의도적 OPEN 항목에 배치별 기한 매핑 없음(첫 영향 E139~150, GA2) | deferred-design-register 연결 필요 |
| F-27 | POV·문체 확정이 decision-log D-entry 미등재 | decision-log.md |

### 기각된 발견 (REFUTED — 기록 목적)

- "E1~20 지위의 PC 대 PC 충돌 미해소" → restoration §8의 명시적 supersede + manifest §3/§5로 기계적 해소 확인(오독 위험만 F-06으로 잔존).
- "작가 승인·정본화 절차 미정의" → 본 PR의 `manuscript-production-workflow-v1.md` §3.6/§3.8이 정의(신설 문서임을 명기).

## 14. 감사 한계

- 본 감사는 AI 수행이며 인간 독자 반응(issue #26)을 대체하지 않는다.
- E101~1100 상세 카드 975파일의 내용 전수 검사가 아니라, 게이트 관련 통제 문서·장부·경계 구간 표본 정밀 검사다. 기존 교차감사(PASS)를 전제로 하되 그 감사가 누락한 이름 에라타 대조(F-04)와 파일 실재 검사(F-03)를 보완했다.
