# GA4·GA7·GA8·GA9 Episode-Level Tangible Anchor & Collection-Desire Audit v1

Status: REVIEW — QC ONLY
Canon Promotion: NOT AUTHORIZED
Publication: NOT AUTHORIZED
Base: `main@0fd812b25e70ad83fe20fd267d9d19a2499d5632`
Scope: GA4 E331–450 + GA7 E691–800 + GA8 E801–900 + GA9 E901–1000 = **430 episodes**
Purpose: 기존 상세회차의 사건·수치·권한을 바꾸지 않고, 후반부 제도/기록/권한 갈등이 실제 원고에서 `사람 + 물리 자산 + 장소 + 눈에 보이는 변화`로 구현될 수 있는지 전수 재감사한다.

---

## 1. Scope Correction

착수 중 트리 빠른 집계에서 `52 detailed batches`라고 잘못 셌다. 최종 Cross-Audit dependency와 `docs/10_story_architecture/detail/` 실제 경로를 재대조한 정확한 수는 다음과 같다.

| Grand Act | Episodes | Detailed card files |
|---|---:|---:|
| GA4 | 120 | **17** |
| GA7 | 110 | **13** |
| GA8 | 100 | **12** |
| GA9 | 100 | **12** |
| **Total** | **430** | **54** |

이 문서는 **54/54 detailed card files를 직접 읽은 뒤의 판정**이다.

기존 최종 Cross-Audit의 구조/정합성 PASS는 유지한다. 이번 감사는 그 위에 reader-facing 실행 레이어만 추가한다.

---

## 2. HAPΔ Audit Rubric

각 묶음에 다음 네 앵커가 실제 카드에 존재하는지 본다.

### H — Human / Current Actor

- 이름 있는 사람 또는 현재 선택권을 가진 반복 역할/공동체.
- 몸, 일, 돌봄, 임금, 가족, 손실, 거부 등 현재 이해관계가 있어야 한다.
- 단순 `representative seat`만으로는 강한 H로 세지 않는다.

### A — Asset / Tangible Object

- 함선, 기체, 수리선, 화물, 의료물자, 릴레이, 정비부품, 실물 증거, 서비스 설비처럼 운반·수리·봉쇄·상실·사용 가능한 대상.
- 숫자만 있는 추상 `authority field`는 A가 아니다.

### P — Place / Operational Space

- 도크, 병원, 항로, 노드, 작업장, 피난구역, 선박, habitat, relay, Archive site 등 현재 행동이 일어나는 구체 공간.
- 은하 지도상의 추상 영역만으로는 약한 P다.

### Δ — Visible State Change

회차 말에 다음 중 하나가 실제로 달라져야 한다.

- 사람이 이동/부상/사망/서비스 회복/권리 상실·회복;
- 화물이 도착/손실/격리;
- 함선·기체가 손상/수리/지연/이탈;
- 노드·병원·항로·전력·냉각·급여·신분 서비스가 실제 작동/정지;
- 관계/명령이 실제 현장 선택을 바꿈.

`규칙이 제정되었다`만으로 Δ를 충족시키지 않는다. 규칙이 실제 사람/물건/장소의 상태를 바꾸는 장면이 함께 있어야 강한 Δ다.

### Verdict Levels

- **GOLD** — H/A/P/Δ가 모두 강하고 독자가 설명 없이 결과를 볼 수 있음.
- **PASS** — 최소 3축이 강하며 누락축이 앞뒤 회차의 강한 실행으로 보완됨.
- **WATCH** — 정합성은 PASS지만 여러 화 연속으로 문서·모델·회의·법리 표면이 H/A/P보다 앞설 위험.
- **HIGH WATCH** — 5화 이상 연속으로 실행 원고가 절차/표/분류 설명으로 기울 가능성이 큼. 새 사건이 아니라 execution overlay 필요.
- **BLOCK** — 사건 자체가 현재 변화로 번역되지 않음. **이번 감사에서 0건.**

---

## 3. GA4 E331–450 — 17/17

Overall: **HAPΔ PASS / NO NEW PLOT NEEDED**

GA4의 정치·계승 갈등은 실제로 화물·선박·병원·급여·증거 운반·릴레이 고장과 연결되어 있다. `왕관 없는 계승전`이 회의극으로만 설계된 것이 아니다.

| File range | Verdict | Tangible reason / risk |
|---|---|---|
| E331–337 | **GOLD** | 73t module, 8,400 worker/pay/care tranche, 312 identity proofs, B-2/B-4 sensor recovery, Parus/medical/evidence hulls |
| E338–345 | **GOLD** | 352t/144-person evidence window, Vesper lien, survivors/deaths, receipt strip, lost frame, mobile custody |
| E346–353 | **GOLD** | 1,240 records/86 urgent, 18,400 civil claims, 310k-service depot, Dor ships/frames, Isa service entries |
| E354–355 | **WATCH** | evidence/legal normalization가 전면. 앞뒤 실물 evidence chain을 원고에서 유지해야 함 |
| E356–360 | **WATCH** | compact/process design 비중 상승. E360 Graybridge 620k 실서비스 위기로 즉시 연결됨 |
| E361–368 | **GOLD — reference case** | 620k service envelope, hospitals, depots, 9 service ships, 1,180t cargo, 96 people, tug/operator damage |
| E369–376 | **GOLD** | 11 service + 8 armed ships, 1,460t/122 people, 97-second delayed stop, 2 deaths, medicine loss |
| E377–380 | **WATCH** | redesign/process 설명 구간. 직전 사망·손실과 다음 Glasswater mission을 반드시 표면에 유지 |
| E381–388 | **GOLD** | 12 vessels, 744t, 188 people, collar fault, 14 urgent unregistered patients, medicine loss |
| E389–396 | **GOLD** | 8 vessels/482t/176 people, Kano Riss, held vessels/people, legal-zone conflict materialized |
| E397–405 | **GOLD** | M-4 crisis, 13 service vessels/1,920t/174 people, 18 armed ships/46 frames, MUT-6, Yara Venn permanent death |
| E406–412 | **WATCH** | Sovereign Reference office design이 가장 절차적. budget→hospital/operator consequence를 장면 중심으로 |
| E413–420 | **PASS** | post-pilot fragmentation + 6 ships/280t/52 people; 구조 설명이 실서비스와 연결 |
| E421–430 | **GOLD** | K-5, 760k service envelope, 17 service vessels/2,360t/226 people, 21 armed ships/52 frames, thermal fault |
| E431–438 | **HIGH WATCH** | nomination/ratification/no-master-heir 법리 비중 최고. 인물·기존 K-5 현장 결과를 붙이지 않으면 추상화 |
| E439–444 | **WATCH** | final compact ratification/person selection. outside 8 armed ships/20 frames 등 물리 압력을 놓치지 말 것 |
| E445–450 | **GOLD** | final K-5 mission 5 vessels/126t/64 people, relay/service recovery, injury, outside armed ships/frames |

### GA4 Ruling

- 새 claimant, 새 기사단, 새 유물, 새 전투 **필요 없음**.
- E354–360 / E377–380 / E406–412 / E431–444만 실행 가드가 필요하다.
- `Graybridge E361–368` 수준이 이 시리즈의 정치/제도 갈등을 물질화하는 **GOLD 기준**이다.
- 원고에서 법리 설명을 줄이더라도 기존 화물/병원/배/작업자/릴레이 결과를 삭제하면 안 된다.

---

## 4. GA7 E691–800 — 13/13

Overall: **STRUCTURE PASS / TWO CONCENTRATED ABSTRACTION BANDS**

GA7은 항로전 자체가 매우 물질적이다. 위험은 전체 110화가 아니라 조사·판결 구간에 몰린다.

| File range | Verdict | Tangible reason / risk |
|---|---|---|
| E691–697 | **GOLD** | 48 corridors, holdout supply clocks, damaged relay, ships grounded by insurance, family movement |
| E698–706 | **GOLD** | 2,900t medicine, 14,800t food, 4,200t power parts, service ships, real deaths/harms |
| E707–715 | **GOLD** | 23 bodies but also 14 ships/8,900t/1,160 staff, corridor failure, vessel loss and deaths |
| E716–723 | **HIGH WATCH** | 212 documents/97 usable/29 strong matches 등 signature analysis가 회차 표면을 지배 |
| E724–732 | **WATCH** | one-person/office/key attribution. witness custody and E731 live correction이 물리 anchor 역할 |
| E733–740 | **PASS WITH WATCH** | E734 Ern physical firing reconstruction strong; D4 class/authority design 다시 추상화 |
| E741–745 | **PASS** | 7-corridor active crisis, 1.74m core +386k outer. office design보다 실제 countdown을 앞세워야 함 |
| E746–753 | **GOLD** | Haren accepts/signs; Lin Osa ordinary worker/caregiver; 6,700 people correction, 97-minute horizon |
| E754–765 | **GOLD** | 14 residual missions/11,600t, microcraft, outer blackout, Lin agency/death, 2,318 D4-linked deaths |
| E766–775 | **WATCH** | consequence/evidence/inquiry 단계. hospital/ship/compensation/current victim result를 표면에 유지 |
| E776–783 | **HIGH WATCH — strongest GA7 risk** | liability/sentence/model governance/judgment가 연속. H/A/P가 가장 약해질 가능성 |
| E784–790 | **HIGH WATCH** | federation/D1–D4/8-field architecture. 실제 live test는 E790 hook 이후 |
| E791–800 | **GOLD** | FB-01, 214,600 people, 17 vessels/6,400t, relays R-17/R-31, contact damage, deaths/injuries |

### GA7 Concentrated Risk Bands

**Band A — E716–740**
- 문제: 독자가 `서명/교리/열쇠/귀속`을 읽는 시간이 너무 길 수 있다.
- 정본 해결책은 이미 있음: Ern physical reconstruction, witness custody, live E731 denial correction.
- 필요한 건 새 사건이 아니라 **기존 증거를 누가 어디에서 실제로 다루는지**를 원고의 장면 표면으로 올리는 것.

**Band B — E766–790**
- 문제: D4 결과 뒤 법리·형량·제도설계가 25화 가까이 이어짐.
- 가장 위험한 E776–783은 `판결문`이 아니라 **Lin의 남은 장부, Haren의 현재 제약, 수리/보상/항로 실무가 실제로 달라지는 과정**으로 보여야 함.
- E784–790의 federation architecture는 잔여의무 자원이 실제로 비축/배치돼 있고 다른 임무에 못 쓰이는 비용을 원고에서 보여야 한다.

### GA7 Ruling

- Blood Admiral 구조 재설계 불필요.
- D4 수치/사망/책임 변경 불필요.
- 새 전투/새 사망/새 피해자 추가 금지.
- **실행형 브레인스토밍 필요: YES, 위 두 띠에 한정.**

---

## 5. GA8 E801–900 — 12/12

Overall: **DEEP / PHYSICAL OPEN & CLOSE / ABSTRACT MIDDLE**

| File range | Verdict | Tangible reason / risk |
|---|---|---|
| E801–810 | **GOLD** | living Serrat archive, Lumen/Orison, service users, substrate crisis, unauthorized snapshot, 3 AI permanent losses |
| E811–818 | **PASS** | grief/service recovery/48,600 users/142,600 objects. classification 많지만 current people and communities present |
| E819–825 | **GOLD/PASS** | 120-person physical cultural-return pilot, withdrawals, language corrections, compact in inhabited space |
| E826–835 | **WATCH** | four founding histories/effect comparison. E833 service lapse and E834 nine physical spaces are key anchors |
| E836–843 | **HIGH WATCH** | legal effect/translation/successor-liability analysis가 연속; physical archive/custodian visibility 약화 가능 |
| E844–850 | **PASS** | 42-minute service gap, queued credentials, serious deterioration, replacement settlement/Seed handoff |
| E851–860 | **HIGH WATCH — strongest GA8 risk** | 6,240 Seed objects, Seed-0~3, 48 cases, 2,400 sandbox items; 설정집처럼 읽힐 가능성 최고 |
| E861–868 | **HIGH WATCH** | care/unregistered/AI fork/language/nonstandard tech omission audit, 43 connectors, six-function split |
| E869–875 | **PASS** | Aven Rho front-stage + 94,200 user live test + Twelve Lanterns 13 nodes/2.94m people |
| E876–885 | **GOLD** | actual 18h Seed Bridge, node/service operations, credential distortion, 2.94m current result |
| E886–893 | **GOLD/PASS** | 30h operation, 13-node physical map, 1,946 deaths/3,760 harms, restricted/deletion ledger with actual action |
| E894–900 | **PASS** | restriction transfer, Aven finding, Rian refuses successor key, 13-institution coalition creates GA9 material cause |

### GA8 Concentrated Risk Bands

**Band A — E826–843**
- four histories를 `문헌 비교표`로만 쓰지 않는다.
- 이미 카드에 있는 current service, released objects, nine contested physical spaces, custodians and affected residents를 장면 중심으로 둔다.

**Band B — E851–868**
- 가장 큰 실행 위험.
- Seed archaeology는 새로운 초고대 던전을 추가하는 방식이 아니다.
- 기존 Palimpsest / maintenance / Continuity Assembly / inhabited archive settings의 **작업자·정비·격리·번역·서비스 현장**에서 보여준다.
- 48-case audit도 매 화 새 피해사례를 발명하지 않고 이미 소개된 community/service line을 반복 사용한다.
- Rian connector 발견은 선택받은 자 연출이 아니라 `one of 43`이 시각적으로도 유지되어야 한다.

### GA8 Ruling

- 새 Archive site 불필요.
- 28 proposed relics를 이 구간의 loot로 투입 금지.
- Seed 능력/권한 추가 금지.
- **물리·직업·생활 번역 오버레이만 필요.**

---

## 6. GA9 E901–1000 — 12/12

Overall: **REAL BENEFIT + REAL ADMINISTRATIVE HARM + STRONG PHYSICAL WAR ENDGAME**

| File range | Verdict | Tangible reason / risk |
|---|---|---|
| E901–910 | **PASS** | metrics-heavy but crews/families/maintenance/medical transfer/route users show real benefit |
| E911–918 | **WATCH** | credential/AI/technology/family/mobile/appeal/error/exit audits 연속; case list화 위험 |
| E919–925 | **PASS** | market pressure + 3 medical convoys + structural stop + actual death/harm ledger + Perfect Route state |
| E926–935 | **HIGH WATCH** | route→identity→insurance→maintenance→family→technology six-domain audit가 사례집처럼 이어질 위험 |
| E936–943 | **HIGH WATCH** | dedup→deaths→warrant→AI→clinic→parallel lane→insurance→prediction; 구조는 좋지만 반복 인물/공간 필요 |
| E944–950 | **GOLD/PASS** | coordinated attack, 19 ships delayed, crew deaths/injuries, rollback creates measurable service cost |
| E951–960 | **GOLD** | 22 corridors, central-key authorization, 524 craft ledger, local stops, bounded Rian command |
| E961–968 | **GOLD** | live assault, forged missions, repair readiness, 9 combat engagements, 14 service defense missions |
| E969–975 | **GOLD** | verified deaths/harms, 12 irrecoverable craft +47 long repair, 4h37m value, custody temptation |
| E976–985 | **GOLD** | 31-node/26m envelope, competing central orders, protected exit node, Aven architecture, service vs military separation |
| E986–993 | **GOLD** | 458 vs 308 craft + 70 neutral, fleet battle around service corridors, local stop, service forks, surrender, stabilization |
| E994–1000 | **PASS/GOLD** | eleven aftermath crises, 4,280 deaths/11,600 harms, fleet title split, 31 nodes, transitional custody |

### GA9 Concentrated Risk Bands

**Band A — E911–920**
- 시스템 감사를 새 사람 8명을 연속 소개하는 식으로 해결하지 않는다.
- 기존 beneficiary / AI / nonstandard engineering / mobile community를 반복해서 보여 `빠른 길이 누구에게 빠른가`를 체감시킨다.

**Band B — E926–943**
- GA9의 가장 큰 추상화 위험.
- 카드에 이미 있는 한 mobile settlement cluster, plural AI community, nonstandard clinic, outsider-linked crew/parallel lane 등을 여러 domain에서 **재사용**한다.
- 독자가 `route case`, `insurance case`, `clinic case`를 별개 단편으로 느끼기보다 **같은 사람들이 여섯 개 문을 차례로 통과하는 하나의 압박**으로 느끼게 한다.

E944 이후는 새 액션 보강 불필요. 이미 전쟁·함선·정비·서비스 손실이 충분하다.

### GA9 Ruling

- 중앙키/Perfect Route 재설계 불필요.
- 새 초병기/새 기체/새 적 세력 불필요.
- 새 수집품으로 후반 재미를 보충하면 오히려 실패.
- **기존 인물·배·클리닉·노드·수리시설을 반복 인식 앵커로 쓰는 것이 정답.**

---

## 7. Cross-GA Result

### Structural blockers

- HAPΔ BLOCK: **0**.
- 새 사건이 없어서 회차가 성립하지 않는 묶음: **0**.
- 수집욕을 위해 새 기체/유물/세력이 필요한 묶음: **0**.

### Concentrated HIGH WATCH

1. GA4 E431–438.
2. GA7 E716–723.
3. GA7 E776–783.
4. GA7 E784–790.
5. GA8 E836–843.
6. GA8 E851–860.
7. GA8 E861–868.
8. GA9 E926–935.
9. GA9 E936–943.

이 구간들은 **설계 결함이 아니라 원고 실행 위험**이다.

### Gold Reference Bands

후반부 제도/정치/권한을 소설로 보이게 만드는 기준 사례:

- GA4 E361–376 Graybridge/Meridian field tests.
- GA4 E381–405 Glasswater/M-4.
- GA4 E421–430 K-5.
- GA7 E698–715 route/service cascades.
- GA7 E746–765 Haren D4 + Lin Osa.
- GA7 E791–800 First Bridge.
- GA8 E801–825 living Serrat.
- GA8 E876–893 Twelve Lanterns live activation.
- GA9 E944–975 central-command live campaign.
- GA9 E976–1000 final competing-command campaign.

---

## 8. Required Execution Controls

No card rewrite is authorized by this audit. Context Pack / draft execution should enforce:

1. **5-episode HAPΔ rule** — most 5-episode windows show at least one strong H, A, P and visible Δ across the window.
2. **No >2 pure-procedure chain** — legal/model/classification scenes may continue longer only if a recurring current person/place/asset remains the visible carrier.
3. **Same-person consequence chaining** — abstract audits should reuse existing people/communities where possible rather than introduce a new exemplar every episode.
4. **Physical evidence handling** — evidence must have current custody, access, transport, damage, seal, terminal/workstation, ship/habitat location or other already-supported physical handling when relevant. Do not invent special relic tech.
5. **Old assets over new loot** — use familiar ships, frames, routes, clinics, workspaces and communities to carry late-series progression.
6. **Institutional change → service result** — whenever possible, same or next episode shows what happens to medicine, pay, repair, travel, identity, shelter, cargo or crew.
7. **Rian does not absorb causality** — central command may coordinate; local/affected actors retain stops, refusals and independent outcomes.
8. **Loss remains visible** — Lin, ship damage, permanent AI deaths, long-repair craft and other locked losses cannot become numbers only after their event.

---

## 9. Brainstorming / Questions Ruling

### Broad brainstorming

**STOP.**

- no new world layer needed;
- no new grand act needed;
- no new collection category needed;
- no new flagship/mecha/relic quota needed.

### Targeted execution brainstorming

**YES — only for the HIGH WATCH bands.**

Purpose:
- choose existing FACE / ASSET / PLACE carrier;
- decide what existing state change is seen on page;
- preserve recurring visual/sensory identity;
- reduce lecture density without changing event causality.

### Author questions needed now

**0 blocking questions.**

Exact new named focal, exact final visual, new canon event or changed casualty would require author approval, but none is required to continue this NONCANON execution overlay.

---

## 10. Final Verdict

> **GA4·GA7·GA8·GA9 430-EP TANGIBLE-ANCHOR DESIGN: PASS**
>
> **54/54 DETAILED CARD FILES AUDITED**
>
> **STRUCTURAL HAPΔ BLOCKERS: 0**
>
> **CONCENTRATED EXECUTION-RISK BANDS: 9**
>
> **NEW PLOT / NEW LORE / NEW LOOT REQUIRED: NO**
>
> **TARGETED EXECUTION OVERLAY REQUIRED: YES**
>
> **CANON CHANGE: 0**
>
> **MANUSCRIPT CHANGE: 0**
>
> **PUBLICATION: NOT AUTHORIZED**
