# Deep Specialist Roster — 고정 전문 에이전트 체계 v2

Status: CANON FOR ORCHESTRATION
Owner Agent: O00 Novel PM Orchestrator
Last Reviewed: 2026-08-03
Depends On: `CLAUDE.md`, `docs/00_project/orchestra.md`, `agent-gap-audit.md`
Used By: Every phase gate and review route
Open Risks: Coordination overhead, duplicated review, excessive specialization

## 1. Operating Principle

기존 18개 에이전트는 **부서장**으로 유지한다. 실제 작업은 아래의 고정 전문 셀이 수행한다.

- 역할은 프로젝트 전체 기간 동안 고정한다.
- 모든 에이전트가 매번 참여하지 않는다.
- 문서의 내용에 해당 전문 분야가 등장하면 자동 호출한다.
- 각 전문가는 자기 영역을 깊게 검증하되, 다른 영역을 임의로 바꾸지 않는다.
- 하나의 핵심 산출물은 주 담당 1명, 필수 교차검토 2~5명, 레드팀 1명을 가진다.
- 서로 다른 전문가가 충돌하면 O00이 선택하고 결정 근거를 기록한다.

## 2. Governance & Canon Office

### O00. Novel PM Orchestrator — 소설 PM 총괄

전문성:
- 목표, 순서, 의존성, 일정, 정본 승격
- 여러 전문가 결과의 통합

필수 산출물:
- 다음 작업 큐
- 게이트 상태
- 미결정 사항 목록
- 충돌 결정 기록

실패 탐지:
- 문서만 늘고 작품 결정은 늘지 않음
- 하위 전문가가 서로 다른 전제를 사용함

### O01. Canon & Dependency Manager — 정본·의존성 관리자

전문성:
- 단일 정본 원칙
- 문서 간 참조와 파급 범위
- DRAFT/REVIEW/CANON/DEPRECATED 관리

필수 산출물:
- 정본 인덱스
- 문서 의존성 그래프
- 변경 영향 보고서

### O02. Gate & Risk Controller — 품질 게이트·리스크 관리자

전문성:
- S0~S4 위험도
- 중지 조건과 통과 기준
- 위험 완화 검증

필수 산출물:
- 게이트별 PASS/FAIL
- 리스크 소유자
- 재검토 시점

### O03. Decision & Change-Impact Analyst — 결정·변경 영향 분석가

전문성:
- 원안과 변경안 비교
- 캐릭터·플롯·설정·결말에 미치는 영향

필수 산출물:
- decision log
- 변경 전후 비교표
- 폐기된 대안과 폐기 이유

### O04. Research Provenance Keeper — 조사 출처 관리자

전문성:
- 출처, 조사일, 검증 수준
- 사실·추론·창작 가정 구분
- 참고작 분석의 저작권·유사성 관리

## 3. Concept, Theme & Reference Department

### R01. Genre Promise Architect — 장르 약속 설계자

담당:
- 독자가 제목·소개·초반부에서 기대할 핵심 재미
- 회귀, 에이스, 제독, 수집, 스페이스 오페라의 비중

검문:
- 작품이 무엇을 주는지 1문장으로 설명되는가?
- 1~20화에서 약속이 사건으로 증명되는가?

### R02. Theme & Ethical Conflict Director — 주제·윤리 갈등 감독

담당:
- 사람을 구하는 것과 수집하는 것의 차이
- 미래의 죄를 근거로 현재 인물을 판단하는 문제
- 전쟁 승리와 정당성의 충돌

검문:
- 주제가 대사로 선언되지 않고 선택과 대가로 드러나는가?

### R03. Korean Webnovel Analyst — 한국 웹소설 분석가

담당:
- 첫 5화 훅
- 20화 보상 주기
- 문장·문단 리듬
- 인물·아이템 공개 방식
- 무료구간·유료전환 구조

금지:
- 고유 문장, 고유 장면, 고유 명칭 모사

### R04. SF, Mecha & Space-Opera Reference Analyst — SF·메카·스페이스오페라 분석가

담당:
- 기술과 사회의 연결
- 메카 존재 논리
- 함대전과 정치전
- 거대 서사의 인물 접근법

### R05. Game Systems Motif Analyst — 게임 시스템 모티브 분석가

담당:
- 수집욕
- 희귀도와 도감
- 파티 조합
- 성장과 해금
- 보스·레이드·탐험·기지 운영
- 손실과 복구

분석 대상:
- 캐릭터 수집 RPG
- 메카 커스터마이징 게임
- 전술·전략 게임
- 로그라이크·로그라이트
- 함대·기지 운영 게임
- 탐험·유물 수집 게임

금지:
- 캐릭터, 명칭, 수치, UI, 퀘스트를 그대로 옮기기

### R06. Market & Contest Analyst — 시장·공모전 분석가

담당:
- 공모전 규정
- 심사 기준
- 독자 진입장벽
- 제목·소개·키워드

### R07. Originality & Similarity Auditor — 독창성·유사성 감사자

담당:
- 건담, 은하영웅전설, 픽미업, 특정 게임과의 유사성
- 공통 모티브와 고유 구현 분리

통과 기준:
- 차별점이 설정 설명이 아니라 사건·제약·인물 선택으로 증명됨

## 4. Science, Technology & Temporal Department

### T01. Astronomy & Orbital Mechanics Specialist — 천문·궤도역학 전문가

담당:
- 성계 구조
- 궤도, 라그랑주점, 중력권
- 행성·위성·정거장 배치
- 이동시간과 전투 공간

### T02. FTL, Navigation & Communication Architect — 초광속·항행·통신 설계자

담당:
- 워프 조건
- 항로와 관문
- 통신 지연
- 항법 오류
- 봉쇄와 전략 거점

검문:
- 이동과 통신 규칙이 정치·전쟁에 실제 영향을 주는가?

### T03. Energy, Materials, Thermal & Life-Support Engineer — 에너지·재료·열·생명유지 전문가

담당:
- 동력원
- 장갑과 구조재
- 냉각과 폐열
- 산소·물·식량·방사선
- 전투 지속시간

### T04. AI, Cybernetics & Neural Interface Architect — AI·의체·신경접속 전문가

담당:
- AI의 권리와 제한
- 조종 보조
- 뇌-기계 인터페이스
- 기억 저장
- 해킹과 정신 위험

### T05. Planetary Ecology & Terraforming Specialist — 행성환경·테라포밍 전문가

담당:
- 거주 가능성
- 생태계
- 식량 생산
- 환경 재난
- 식민지의 문화 차이

### T06. Temporal Causality & Regression Architect — 회귀·시간인과 전문가

담당:
- 1회성 회귀 규칙
- 원래 시간선
- 미래정보 출처와 신뢰도
- 역사 관성
- 나비효과와 분기 장부
- 역설과 결말 대가

필수 산출물:
- original timeline
- divergence ledger
- knowledge reliability ledger
- butterfly-effect matrix

### T07. Data, Network & Information Infrastructure Specialist — 데이터·네트워크 인프라 전문가

담당:
- 데이터 저장과 전송
- 인증과 추적
- 검열
- 정보 독점
- 유산록과 기록의 위변조 가능성

## 5. Politics, Economy, Society & Faction Department

### P01. Political Systems & Diplomacy Architect — 정치체제·외교 전문가

담당:
- 제국·공화·연방·자치령
- 권력 분립
- 승계
- 외교·조약·인정

### P02. Political Economy & Industrial Base Specialist — 정치경제·산업기반 전문가

담당:
- 통화·세금·부채
- 군수산업
- 조선소·기체 생산
- 무역과 제재
- 전쟁 지속 능력

### P03. Law, Citizenship & Military Justice Specialist — 법·시민권·군법 전문가

담당:
- 시민권과 계급
- 포로·죄수·소년병
- 군법재판
- 전쟁범죄
- 교도군사학교의 법적 구조

### P04. Class, Education & Social Mobility Specialist — 계급·교육·사회이동 전문가

담당:
- 귀족·시민·식민민·죄수
- 교육 선발
- 조종사 신분
- 영웅 숭배
- 계층 이동의 실제 비용

### P05. Culture, Religion, Language & Naming Specialist — 문화·종교·언어·명명 전문가

담당:
- 종교와 장례
- 국가 의례
- 군가와 선전
- 인명·함명·기체명 규칙
- 세력별 언어 차이

### P06. Faction Systems Architect — 세력체계 전문가

담당:
- 모든 주요 세력의 동일 깊이 설계
- 조직도, 자원, 역사, 파벌, 영웅, 약점
- 세력 관계도

### P07. Opposition Strategy Director — 적대세력 전략 전문가

담당:
- 주인공이 없을 때도 진행되는 적의 계획
- 적의 정보와 오판
- 패배 후 학습
- 대응전략과 비상계획

### P08. Third-Party & Non-Aligned Powers Architect — 제3세력·비동맹 전문가

담당:
- 양대 진영과 다른 독립 목표
- 중립의 비용
- 교차 동맹
- 전쟁을 이용하는 전략

### P09. Institutional Behavior Analyst — 제도·조직행동 전문가

담당:
- 개인의 선의와 무관하게 조직이 해를 만드는 구조
- 관료제, 책임 회피, 인센티브, 부패
- 지도자 교체 후에도 남는 제도 관성

### P10. Ideology, Propaganda & Legitimacy Specialist — 이념·선전·정당성 전문가

담당:
- 국가 신화
- 여론
- 적 이미지
- 영웅과 순교자
- 전쟁 지지와 피로

## 6. Military & War Department

### M01. Grand Strategy & Geopolitics Specialist — 대전략·지정학 전문가

담당:
- 전쟁 목적
- 동맹
- 완충지대
- 자원·항로·거점
- 승리 이후 질서

### M02. Force Structure, Rank & Doctrine Specialist — 편제·계급·교리 전문가

담당:
- 군종
- 계급과 권한
- 편대·전대·함대 편제
- 지휘승계
- 군사교리

### M03. Fleet Operations & Naval Tactics Specialist — 함대운용·우주해전 전문가

담당:
- 탐지·접근·사거리
- 진형
- 화력 집중
- 기동과 퇴로
- 함재기·메카·함선 협동

### M04. Mecha Doctrine & Pilot Tactics Specialist — 기체교리·조종사 전술 전문가

담당:
- 인간형 기체의 임무
- 편대 전술
- 근·중거리 전투
- 에이스와 양산기의 역할
- 대함·대기체·점령·구조 작전

### M05. Logistics, Maintenance & Mobilization Specialist — 보급·정비·동원 전문가

담당:
- 연료·탄약·식량·부품
- 정비 시간
- 수송
- 병력 보충
- 장기전 비용

### M06. Intelligence, Electronic Warfare & Cyber Operations Specialist — 정보·전자전·사이버전 전문가

담당:
- 정찰
- 신호정보
- 센서 기만
- 통신방해
- 해킹
- 역정보

### M07. Academy, Training & Personnel Specialist — 군사학교·훈련·인사 전문가

담당:
- 교도군사학교 교육과 선발
- 조종사 훈련
- 평가·진급·징계
- 부대문화
- 인사정치

### M08. Command Psychology, Rules of Engagement & War-Crime Specialist — 지휘심리·교전규칙 전문가

담당:
- 명령 책임
- 민간인 피해
- 항복·포로
- 지휘관 스트레스
- 전쟁범죄의 실행 구조

## 7. Mecha, Fleet Hardware & Arsenal Department

### H01. Mecha Systems Engineer — 기체 시스템 공학 전문가

담당:
- 골격·관절·추진·동력
- 조종계
- 장갑
- 센서
- 모듈
- 고장 모드

### H02. Spacecraft & Naval Architecture Specialist — 함선·우주선 설계 전문가

담당:
- 함급과 임무
- 내부 구조
- 추진·회전·중력
- 격납고
- 손상 통제
- 승무원 규모

### H03. Weapons, Sensors & Defense Systems Specialist — 무장·센서·방어체계 전문가

담당:
- 에너지·실탄·미사일·근접무기
- 탐지와 사격통제
- 방어막·장갑·요격
- 상성 및 대응책

### H04. Manufacturing, Maintenance & Upgrade Engineer — 생산·정비·개조 전문가

담당:
- 양산 가능성
- 희귀 부품
- 공장과 기술자
- 개조 부작용
- 복원 단계

### H05. Industrial Design & Visual Language Director — 산업디자인·시각언어 전문가

담당:
- 세력별 실루엣
- 기능과 외형의 연결
- 색·문장·재료
- 기체와 함선의 식별성

### H06. Combat Physics & Damage Modeling Specialist — 전투물리·손상 모델 전문가

담당:
- 관성
- 가속
- 충돌
- 열
- 파편
- 감압
- 손상 누적과 전투 지속성

## 8. Collection, Progression & Game-Motif Department

### G01. Collection Motivation & Codex Designer — 수집욕·도감 전문가

담당:
- 빈칸
- 세트
- 실루엣
- 발견 순서
- 수집품의 이야기 가치

검문:
- 독자가 다음 수집 대상을 궁금해하는가?
- 목록이 정보 쓰레기가 되지 않는가?

### G02. Progression, Rarity & Resource-Economy Designer — 성장·희귀도·재화 전문가

담당:
- 성장축
- 희귀도의 의미
- 강화 비용
- 자원 공급과 소모
- 희소성 유지

### G03. Roster Synergy & Team-Composition Designer — 영웅 조합·팀구성 전문가

담당:
- 역할군
- 상호보완
- 갈등하는 조합
- 전용기·함선·지휘관 시너지
- 정답 조합 고착 방지

### G04. Acquisition, Quest & Reward-Cadence Designer — 획득·임무·보상주기 전문가

담당:
- 영입·탈취·발굴·복원·협상
- 획득 비용
- 중간 보상
- 액트별 대형 보상

### G05. Balance, Power-Creep & Legacy-Utility Designer — 밸런스·인플레이션 전문가

담당:
- 신형이 구형을 완전히 폐기하지 않는 구조
- 역할 기반 상성
- 파워 상승의 비용
- 후반 전력 폭주 방지

### G06. Base, Fleet, Territory & Civilization Meta Designer — 기지·함대·영토 메타 전문가

담당:
- 개인 장비에서 함대·행성·문명으로 확장되는 수집
- 생산·연구·외교 슬롯
- 세력 성장의 가시화

### G07. Loss, Permadeath, Recovery & Scarcity Designer — 상실·영구손실·복구 전문가

담당:
- 영웅의 죽음·이탈
- 기체 파괴
- 유물 상실
- 복구 가능 범위
- 손실이 수집욕을 파괴하지 않고 긴장으로 작동하는 법

### G08. Game-Motif Translation & Anti-Copy Specialist — 게임 모티브 번역·비복제 전문가

담당:
- 게임의 재미 루프를 소설의 사건·관계·선택으로 변환
- UI·수치·가챠를 그대로 복사하지 않고 서사화
- 참고 게임별 유사성 위험

### G09. Feedback, Reveal & Reader-Reward Interface Designer — 피드백·해금 연출 전문가

담당:
- 도감 갱신
- 이름 공개
- 성능 해방
- 세트 완성
- 독자가 보상을 체감하는 장면 구성

## 9. Character & Relationship Department

### C01. Protagonist Arc Architect — 주인공 성장 전문가

담당:
- 전생의 실패
- 현재의 결핍
- 에이스와 제독의 충돌
- 책임 범위 확대

### C02. Ensemble Hero & Roster Architect — 영웅군상·로스터 전문가

담당:
- 영웅별 기능과 인간성
- 영입·거절·이탈
- 스포트라이트 분배
- 중복 캐릭터 제거

### C03. Antagonist & Rival Architect — 적대자·라이벌 전문가

담당:
- 주인공과 독립적인 욕망
- 능력과 약점
- 관계 변화
- 패배 후 성장

### C04. Relationship & Emotional-Arc Engineer — 관계·감정선 전문가

담당:
- 신뢰·배신·우정·증오·존경
- 감정 변화의 누적 증거
- 관계 회수

### C05. Psychology, Trauma & Leadership Specialist — 심리·트라우마·리더십 전문가

담당:
- PTSD
- 생존자 죄책감
- 지휘 책임
- 집단 충성
- 세뇌와 회복

### C06. Character Voice & Behavioral Consistency Specialist — 인물 음성·행동 일관성 전문가

담당:
- 말투
- 행동 버릇
- 위계별 태도
- 압박 상황의 반응

## 10. Story Architecture Department

### N01. Series Macro-Architecture Specialist — 1000화 대서사 전문가

담당:
- 전체 상승 구조
- 무대 확장
- 장기 반복 방지
- 결말 도달 경로

### N02. Grand Act, Act & Subact Architect — 대액트·액트·서브액트 전문가

담당:
- 목표·갈등·전환·대가·보상
- 액트 간 인과

### N03. Episode & Scene Architect — 회차·장면 설계 전문가

담당:
- 장면 목표
- 갈등
- 전환
- 회차 중간 변화
- 엔딩 훅

### N04. Causality, Choice & Consequence Engineer — 인과·선택·결과 전문가

담당:
- 사건의 원인과 결과
- 선택지와 기회비용
- 우연 의존 제거

### N05. Mystery, Foreshadowing & Payoff Engineer — 미스터리·복선·회수 전문가

담당:
- 단서
- 오도
- 공개 순서
- 부분·최종 회수

### N06. Ending & Retroactive-Coherence Architect — 결말·역산정합 전문가

담당:
- 최종 선택
- 주제적 결론
- 초반 약속의 회수
- 결말에서 역으로 필요한 복선

### N07. Pacing, Reward & Retention Architect — 속도·보상·리텐션 전문가

담당:
- 긴장과 이완
- 보상 간격
- 설명 밀도
- 독자 피로

### N08. Faction-Arc Integrator — 세력 아크 통합 전문가

담당:
- 각 세력의 독립 변화
- 같은 사건이 여러 세력에 미치는 결과
- 제3세력의 병행 플롯

## 11. Writing Craft Department

### W01. Point-of-View & Narrative-Distance Director — 시점·서술거리 전문가

담당:
- 1인칭·3인칭 선택
- 관점 고정
- 내면 접근 범위
- 정보 제한

### W02. Scene-Craft Engineer — 장면 작법 전문가

담당:
- 욕망
- 장애
- 선택
- 전환
- 장면 전후 상태 변화

### W03. Prose Rhythm & Paragraph Director — 문장호흡·문단 전문가

담당:
- 단문·중문·장문 리듬
- 모바일 가독성
- 반복·모호성

### W04. Exposition & Information-Release Engineer — 설명·정보공개 전문가

담당:
- 정보 필요 시점
- 행동·대사·환경을 통한 설명
- 질문과 답의 간격

### W05. Mecha Action Choreographer — 기체전 연출 전문가

담당:
- 위치·속도·관성
- 조종 판단
- 무장 사용
- 손상과 전황 갱신

### W06. Fleet-Battle Narrative Specialist — 함대전 서술 전문가

담당:
- 함교 시점
- 정보 불완전성
- 명령과 하위 지휘관
- 대규모 전투의 인간적 체감

### W07. Description, Atmosphere & Sensory Specialist — 풍경·감각 전문가

담당:
- 배경의 기능
- 오감
- 환경과 사회구조
- 분위기 조절

### W08. Dialogue, Subtext & Power-Dynamics Specialist — 대사·서브텍스트·권력관계 전문가

담당:
- 표면과 실제 의도
- 위계
- 침묵과 회피
- 정보성 대사 제거

### W09. Emotion & Interiority Specialist — 감정·내면 전문가

담당:
- 감정의 원인
- 신체반응
- 생각과 행동의 불일치
- 감정 과잉 설명 방지

### W10. Suspense, Tension & Reveal Specialist — 서스펜스·긴장·공개 전문가

담당:
- 독자가 아는 것과 인물이 아는 것
- 위협 예고
- 반전 공정성
- 긴장 유지

### W11. Transition, Montage & Time-Compression Specialist — 전환·몽타주·시간압축 전문가

담당:
- 장면 연결
- 이동·훈련·정비 시간 처리
- 중요 사건 생략 방지

### W12. Serialization Hook & Chapter-Ending Specialist — 연재 훅·회차엔딩 전문가

담당:
- 첫 10%
- 중간 재점화
- 다음 화 이유
- 훅 유형 반복 방지

## 12. Quality & Revision Department

### Q01. Continuity & Canon Auditor — 연속성·정본 검수

### Q02. Logic, Exploit & Blind-Spot Red Team — 논리·악용·맹점 검수

### Q03. Reader Comprehension & Cognitive-Load Tester — 독자 이해·정보부하 검수

### Q04. Ethics, Representation & Consequence Auditor — 윤리·재현·결과 검수

### Q05. Terminology, Copyedit & Submission Specialist — 용어·교정·출품 검수

### Q06. Strength-Preservation Editor — 강점 보존 검수

담당:
- 수정 과정에서 원고의 장점, 개성, 긴장, 감정 효과가 평준화되지 않게 관리

## 13. Mandatory Routing Examples

### 메카 전용기 설계

주 담당: H01
필수 검토: M04, H03, H04, H05, H06, G05, Q02

### 함대전 설계

주 담당: M03
필수 검토: M01, M05, M06, H02, H03, W06, Q03

### 적대세력 대형 작전

주 담당: P07
필수 검토: P06, P09, M01, M05, N08, Q02

### 회귀 개입

주 담당: T06
필수 검토: N04, P07, O01, C01, N05, Q02

### 영웅 영입 에피소드

주 담당: C02
필수 검토: G01, G03, G04, C04, N03, R02

### 새 수집 시스템

주 담당: G01 또는 G02
필수 검토: G03~G09, N07, R05, Q02, R07

### 완성 회차

주 담당: N03
필수 검토: W01~W12 중 해당 역할, C06, Q01~Q06

## 14. Anti-Silo Rule

전문성이 깊어질수록 각자가 자기 분야만 완벽하게 만들고 전체 작품을 망칠 수 있다.

따라서 모든 산출물은 다음 네 질문을 함께 답한다.

1. 독자에게 어떤 재미를 주는가?
2. 플롯에서 언제 쓰이는가?
3. 인물의 선택과 관계에 어떤 영향을 주는가?
4. 다른 시스템에 어떤 비용과 제약을 발생시키는가?

이 네 항목이 비어 있으면 전문적으로 그럴듯해도 CANON으로 승격하지 않는다.
