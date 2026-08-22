# GA1 E001–E020 Rewrite Audit — 2026-08-22

Status: CANONICAL QC RECORD
Effective Authority: WORKFLOW/QC — NOT A STORY SOURCE
Story Canon Effect: NONE
Publication: NOT AUTHORIZED
Owner Agents: A00 PM / A11 Prose & Serialization / N03 Episode / L02 POV / X04 Continuity / O01 Canon / X06 Red Team
Last Reviewed: 2026-08-22
Depends On: [[decision-log]], [[manuscript/README]], [[ga1-episodes-1-20-beat-map-v1]], [[ga1-e011-e020-context-pack-deep-v1]], [[ga1-e006-e010-context-pack-deep-v1]], [[gate1-korean-webnovel-pov-prose-calibration-v1]], [[reader-facing-terminology-phonetics-and-register-bible-v1]], [[m001-m020-early-clue-episode-ledger-v1]], [[academy-and-07-opening-operational-state-v1]]
Used By: E021 batch readiness, manuscript QA precedent, clue-ledger reconciliation
Open Risks: E001–E005 sit at 97–100% of the C4 floor and are referred to the author as a structural length question; three clue-ledger episode assignments disagree with the beat map and are referred to canon review

---

## 1. Scope

E1–E100 was retired entirely under `D-20260822-01`. `D-20260822-02` then opened the
rewrite batch to **E001–E020**. This record covers the production and audit of those
twenty episodes.

Execution was delegated to Codex 0.148.0 against fixed source briefs; source selection,
diagnosis, verification and every merge decision were made here.

| | |
|---|---:|
| 회차 | 20 |
| 본문 합계 | 약 116,000자 |
| 새 정본 | 0 |
| 본문 라틴문자 | 0 |
| 본문 작가측 코드 (M-/F-/R-) | 0 |
| 본문 위키링크 | 0 |
| `Publication: NOT AUTHORIZED` | 20/20 |
| `AUTHOR-APPROVED` | 미부여 |

---

## 2. 배치별로 드러난 실패와 교정

세 가지가 순서대로 드러났고, 각각 상시 브리프에 흡수돼 다음 배치에서 재발하지 않았다.

### 2.1 배치 1 — 승인 비트가 한 문장으로 압축됐다

초고 5편 중 4편이 하한 미달이었다. 원인은 문체가 아니었다. 승인 비트가 **서술 한 줄로 보고**돼 있었다.

- E001: 「눈에 띄지 않기 vs 부상 방지」 선택이 한 줄로 처리됐다. 카드는 이걸 장면으로 요구한다.
- E001: 결정적 잠금을 수행하는 브람이 자기 판단을 가진 사람이 아니라 손 한 쌍으로 읽혔다.
- E003: 제한 수리 경로와 그것이 뒤쪽 팀에 지우는 기회비용이 요약됐다.

**§20-5가 규정한 대로 문장을 늘리지 않고 비트를 복원했다.** 회차별로
`STAGED / COMPRESSED / ABSENT`를 판정한 뒤 압축·누락분만 장면으로 폈다.

복원 후 E003의 예:

> 카라가 바로 물었다. "그렇게 바꾸면 재시험 항목이 남습니까?"
> …
> 하렌은 배정표를 다시 봤다. "느려지면 뒤쪽 팀 기회가 줄어듭니다. 그 비용 없이 안전해졌다고 쓰면 안 됩니다."
> …
> 리안은 반사적으로 한 걸음 나서려 했다. "제가 타이밍을 보정하면—" / 미아의 시선이 먼저 그를 멈췄다.

허가권자가 허가 경계를 말로 긋고, 비용을 무는 사람이 이름을 얻고, 리안이 자기 기량으로 메우려는 시도가 먼저 차단된다. 브람은 리안이 가리킨 지점을 지우지 않고 그 옆에 다른 색 표식을 붙인다 — 틀린 것이 사라지는 대신 어디서 갈라졌는지가 남는다.

**교정**: 상시 브리프에 「비트를 요약하지 말고 장면으로 세울 것」 절을 추가했다. 거절·비용·권한 경계·보통 사람의 주체성을 나르는 비트가 가장 먼저 서술로 뭉개진다는 점을 명시했다. 배치 2 이후 복원 패스가 필요 없었다.

### 2.2 배치 2 — Context 팩의 언어가 산문으로 새어 나왔다

Context 팩은 영문이다. 그 어휘가 서술과 **대사에** 그대로 들어와, 한국어 문장 안에서 인물이 영어로 말했다.

> "공식 평가 요약에서는 어제 over-rotation correction이 리안 단독 조종 오류로 묶였고, current map correction 출처가 비어 있습니다. … 의료 점검 완료는 pending인데 접근 조건에서는 failure로 읽혔습니다."

E008 42건, E009 59건, E010 35건. [[reader-facing-terminology-phonetics-and-register-bible-v1]] §7은 서술에서 한국어 기능 축약형을 선호하고, §9는 독자 대면 기술어를 한국어로 열거하며, Layer C 작가측 코드는 「대사 설명이 되어서는 안 된다」고 못박는다. 이건 Layer C도 아닌 단순 미번역 원문 어휘였다.

**교정**: 10편 전체 한국어 표면 패스. 사건·권한·07 상태·단서 시점 불변, 6인 음성 잠금 유지, E009의 장면이 도는 두 기록 상태 구분과 미아의 「그 둘은 다릅니다」 보존. 결과 라틴 0.

E009가 5,820 → 5,218자로 줄어 삭제를 의심했으나 번역 때문이다. `over-rotation correction`(24자) → `과회전 보정`(6자)처럼 영문구가 훨씬 길다. 앞선 자수가 영문으로 부풀어 있었던 것이다. 이후 비트 복원으로 하한을 넘겼다.

**교정**: 브리프에 「본문 라틴문자 0」과 한국어 용어 목록을 상시 조항으로 넣었다. 배치 3·4는 처음부터 0이었다.

### 2.3 배치 3~4 — 첫 시도 통과

E011–E020은 복원 패스 없이 하한을 넘겼고 라틴·코드 누출이 없었다.

---

## 3. 전체 감사 (읽기전용)

20편이 완성된 뒤 독립 감사를 **읽기전용**으로 돌렸다. 감사자가 조용히 고치면 무엇이 틀렸는지 알 수 없기 때문이다.

### 3.1 통과 9항목

| 항목 | 판정 |
|---|---|
| 07 출력 곡선 (E5 저출력 → E8 35~45% → E16 55~65% → E17 30~40% → E20 45~55%) | 허용 상태 초과 0. E17 손상이 이후에도 유지됨 |
| 리안의 현재 신체 | 미래 기량이 청소년 신체 조건과 조종석 피드백을 지우지 않음 |
| 권한 | 리안의 월권 시도는 있으나 오류로 취급되고, 정지 권한 보유자가 실제로 정지시킴 |
| 연표 | CY 742-03-17 → 04-05 단조 |
| 음성 | 화자 표기를 가려도 6인 구별됨. 하렌·세린이 가장 근접하나 하렌은 사람·의무에서, 세린은 기록 유효성에서 말함 |
| 이름 | 미등재·폐기 이름 0 |
| 소유 금지 | 자동 충성·전리품 0 |
| 패딩 | 하드 실패 0 |
| 문체 하네스 | 단문 나열을 기본 리듬으로 쓴 구간 0 |

소유 금지 증거:

> "그놈을 얻었다고 생각하면, 그게 다음 거짓말입니다." (E020)
> "저희는 선배의 예비 명단이 아닙니다." (E015)
> "에른 바르카는 아직 그들을 모른다. 그리고 알 필요도 없다." (E012)

### 3.2 오탐 2건 — 기각

감사가 E012의 M-012와 E007/E008의 M-011을 **조기 공개**로 보고했다. 대조 결과 둘 다 오탐이며, 지시대로 고쳤으면 **승인 비트를 삭제할 뻔했다.**

- [[ga1-episodes-1-20-beat-map-v1]] Episode 8은 M-011을 배정하고 beat 3이 `no throne/weapon access appears`, beat 4가 `Rian's future expectation is contradicted`다. 원고는 이 비트를 그대로 구현했다.
- 같은 비트맵 Episode 12는 M-012를 배정하고, [[ga1-episodes-11-15-scene-cards-v1]] Scene 12.2가 `he is not helping Rian's cell, who are not yet present`를 명시하며 하렌에게 동기 논증을 준다.

**어긋난 것은 원고가 아니라 단서 장부의 회차 배정이다.** §4에 기록한다.

### 3.3 실제 결함 3건 — 수정

**F1 — 「완전 출력」이 100%로 읽힌다.** E013·E015가 E016 시퀀스를 완전 출력이라 불렀다. 승인 봉투는 55~65%이고 E016 산문 자체는 이를 지킨다. 전개 출력 개방/55~65 대역 표기로 교체. 현재 「완전 출력」 0건.

**F2 — 서술자가 에른의 동기를 확정했다.** E012 말미가 「에른 바르카는 리안의 셀을 구하러 움직인 것이 아니었다」를 서술자 판정으로 적었다. 카드는 그 해석을 **하렌의 주장**으로 준다. M-018(아카이브 기억 오염)에 따라 리안의 판독은 확정되지 않는다. 관측 사실(통로가 열렸고, 누군가 나갔고, 열리자마자 에른이 빠졌고, 셀은 그 자리에 없었다)은 남기고 해석을 방으로 돌려보냈다 — 하렌이 논증하고, 세린이 불확실 귀속으로 기록하고, 리안이 닫지 못한다. 독자는 판정이 아니라 관찰을 쥔 채 회차를 끝낸다.

**F3 — 같은 비트 형태가 반복된다.** 「리안이 미래지식으로 주장 → 담당 권한이 교정 → 세린이 좁은 기록으로 재구성 → 좁은 절차가 진행」이 기계처럼 느껴질 만큼 반복됐다. CLAUDE.md §7의 실패 조건(같은 유형이 이름만 바뀌어 반복)이다. E013·E017·E020에서 **결과·비용·거절·단서 상태를 그대로 둔 채 도달 방식만** 바꿨다 — E017은 리안이 보류한 구성 전제가 손상 비용이 떨어질 때까지 기록 공백으로 남고, E020은 카라의 절차 한계·하렌의 거부·세린의 기록 우려가 서로 갈라진 뒤에야 리안이 전면 공개한다.

---

## 4. 정본 검토로 올리는 것 — 단서 장부와 비트맵의 회차 불일치

[[m001-m020-early-clue-episode-ledger-v1]]의 단서 회차가 승인 구조와 어긋나는 사례가 이제 셋이다. 고치지 않고 기록한다 — 어느 쪽이 옳은지는 정본 판단이다.

| 단서 | 장부가 말하는 첫 단서 | 승인 구조가 배치한 곳 |
|---|---|---|
| M-011 | `E95` — 07의 제국 식별 열쇠가 서비스 층 하나만 연다 | 비트맵 Episode 8이 M-011을 배정하고 beat 3이 그 사실 자체를 요구 |
| M-012 | `E52`·`E53` — 에른의 사격 보류 | 비트맵 Episode 12와 E11–15 카드가 E11 훅·E12 장면에 배치. E21–26 Scene 22.2에도 별도 보류 사격이 있음 |
| M-016 | `E18` — 인증품이 즉시 사람을 살림 | E14 카드도 인증 이익 장면을 요구 (중첩, 충돌 아님) |

이미 [[ga1-e011-e020-context-pack-deep-v1]] §14가 M-012와 수집 등록표 3건을 같은 방식으로 올려 두었다. **원고는 비트맵을 따랐다** — 회차별 승인 구조가 그 회차의 실행 근거이기 때문이다.

O01 Canon / X04 Continuity 판단 사항.

---

## 5. C4 — E001~E005는 분량을 받아들인다

| 구간 | C4 |
|---|---|
| E006–E020 | 하한 통과 |
| E001–E005 | 5,308~5,478자 · 하한의 97~100% |

감사 판정은 **「승인 재료가 얇은 것이지 비트가 빠진 것이 아니다. 채우지 마라」**였다. 다섯 편 모두 Context 팩의 비트 커버리지를 확인했다 — E001 날짜·신체·07·브람·서비스등 훅, E002 아카이브 경고·하렌의 36인·임시 재시험, E003 네라 교정·서비스 커플러·제한 기립, E004 오르페우스 공백·의료 정지·기억 교정, E005 첫 탑승·공유 정지권·부분 구조·비용.

§20-6에 따라 **패딩하지 않았다.** C4는 ERROR가 아니라 WARN이므로 검증은 통과한다.

**작가 결정 대상**: ① 하한을 유지하고 E001–E005 장면 카드에 비트를 추가할지 ② 개막 5화에 한해 하한을 조정할지 ③ 현 상태로 둘지.

---

## 6. 실행 증거

| 명령 | 결과 |
|---|---|
| `validate_canon.py --selftest` | PASS — 39 cases |
| `validate_canon.py` | PASS — episode manuscripts checked: 20, C3 오류 0, C5 오류 0, C4 경고 5 |
| `validate_story_graph.py --selftest` | PASS — 39 cases |
| `validate_story_graph.py` | PASS |
| 나머지 생성물 `--check` | current |

---

## 7. 판정

> **GA1 E001–E020 v1: DRAFTED AND AUDITED**
>
> **NEW STORY CANON: 0 · LATIN SCRIPT IN PROSE: 0 · AUTHOR-SIDE CODES IN PROSE: 0**
>
> **CLUE-LEDGER EPISODE DRIFT: 3 CASES REFERRED TO O01/X04**
>
> **C4: E001–E005 REFERRED TO THE AUTHOR AS A STRUCTURAL LENGTH QUESTION**
>
> **AUTHOR-APPROVED: NOT GRANTED · PUBLICATION: NOT AUTHORIZED**

집필 승인(`D-20260822-02`)은 회차별 작가 승인과 다르다. 이 기록은 초고 생산과 감사만 판정하며, 공개·유료연재·출판은 별도 게이트다. issue #26 사람·모바일 검증은 출판 전 하드 블로커로 유지된다.
