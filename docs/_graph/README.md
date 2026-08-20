# Story Graph Navigation Layer — 옵시디언 서사 그래프 계층

Status: CANON FOR NAVIGATION / NOT A STORY OR SETTINGS SOURCE
Owner Agents: A00 PM / N02 Act Architecture / N03 Episode / O01 Canon / X04 Continuity
Last Reviewed: 2026-08-20
Depends On: [[architecture-rules]], [[1000-episode-grand-act-map-v1]], [[context-pack-tangible-reader-memory-execution-spec-proposal-v1]], [[docs/_entities/README]]
Used By: Obsidian Graph View, act/subact navigation, Context Pack preparation, continuity review
Open Risks: navigation hubs accidentally becoming a duplicate canon source; graph clutter from creating empty entity notes

## 1. Purpose

이 폴더는 이미 존재하는 정본·Approved Structure·상태 장부를 **옵시디언에서 실제로 탐색 가능한 그래프**로 연결한다.

이 계층은 새 사건·설정·인물·기체·함선·장소·권한을 만들지 않는다. 정확한 사실과 회차 범위는 기존 source document가 소유한다.

## 2. Effective graph path

```text
[[story-graph-root]]
→ Grand Act Hub
→ Act Hub
→ Subact Hub
├─→ authoritative Act-map
├─→ GA Collection Registry
├─→ episode design/index bridge
├─→ [[context-pack-tangible-reader-memory-execution-spec-proposal-v1]]
└─→ GA Current-State Spine
       → Domain-State Hub
       → registry / bible / entity note / loss-payoff source
```

GA1의 회차 bridge는 [[episode-briefs]]가 직접 회차/장면카드 링크를 제공한다.

GA2–GA10은 GA Current-State Spine에서 [[episodes-101-1100-detail-production-standard-and-batch-map-v1]]을 추가로 연결한다. 상세 episode-card는 원래 GA Act-map을 `Depends On`으로 참조하므로 Obsidian Graph/Backlinks에서 `Subact Hub → Act-map ← Detailed Episode Card` 경로가 형성된다.

상세 카드 파일명을 160개 Subact Hub에 중복 복사하지 않는다. 카드 배치가 재분할될 때 160개 허브가 조용히 낡는 것을 막기 위한 단일진실원칙이다.

현재 작품의 정식 hierarchy는 [[architecture-rules]]를 그대로 따른다. **다른 프로젝트의 `Volume` 또는 고정 `60 Subact` 구조를 가져오지 않는다.**

## 3. Physical Graph Size

현재 `docs/_graph/` Markdown 파일은 **233개**다.

- 규칙 README: 1
- Series Root: 1
- Grand Act Hubs: 10
- Act Hubs: 40
- Subact Hubs: 160
- GA Current-State Spines: 10
- Domain-State Hubs: 11

Subact는 GA01 A1부터 GA10 D4까지 previous/next 링크로 하나의 시간축 체인을 이룬다.

## 4. Node rules

1. Hub는 navigation only다. 새 story fact를 쓰지 않는다.
2. 부모와 자식은 서로 링크해 Obsidian backlink가 양방향으로 작동하게 한다.
3. Subact hub는 해당 GA의 Act-map, Collection Registry, Current-State Spine과 Context Pack 표준으로 연결한다.
4. Current-State Spine은 캐릭터·수집·기체·함선·무장·유물·기술·세력·장소·비주얼·손실/회수 domain hub로 fan-out한다.
5. exact entity note가 아직 없으면 새 사실을 만들지 않고 index/registry로 연결한다.
6. 197명 전원, 612성계 전부에 빈 엔티티 노트를 만들지 않는다. front-stage 승격 시에만 [[docs/_entities/README]] 규칙으로 개체 노트를 만든다.
7. 원고 본문에는 위키링크를 넣지 않는다.
8. Context Pack은 회차 집필 직전에 생성한다. 1,100개를 선생성하지 않는다.
9. Graph node가 더 최신이라는 이유로 Act-map, 상세카드, 상태장부, 손실장부, payoff ledger를 덮어쓰지 않는다.
10. 비주얼 graph는 설계 방향·독자 기억·anti-similarity guard를 연결하지만 exact face/hair/body/costume를 자동 정본화하지 않는다.

## 5. Current-State resolution

한 Subact/회차에서 현재 상태를 찾는 순서는 다음이다.

1. current author decision / Canon Amendment / Errata;
2. authoritative Act-map / exact detailed episode card;
3. GA Current-State Spine;
4. state checkpoint / operational snapshot;
5. GA Collection Registry;
6. domain registry/bible;
7. front-stage entity note if one exists;
8. loss/payoff/authority ledgers;
9. visual-memory/anti-similarity QC;
10. Context Pack execution fields.

Context Pack은 이 결과를 집필 가능한 형태로 번역할 뿐 상위 사실을 바꾸지 않는다.

## 6. Graph filters

노드 본문 첫 부분의 `Graph Node`, `GA`, `Act`, `Subact` 표기를 이용해 Obsidian 검색/필터를 적용한다.

추천 필터:
- `path:docs/_graph/ga`
- `path:docs/_graph/acts`
- `path:docs/_graph/subacts`
- `path:docs/_graph/state`

## 7. Validation

- `python tools/validate_story_graph.py`
- GitHub Actions: `.github/workflows/validate-story-graph.yml`
- QC record: [[obsidian-story-graph-deep-wiring-audit-2026-08-20]]

## 8. Root

- [[story-graph-root]]
