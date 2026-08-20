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
→ [[episode-briefs]] / exact episode-card source
→ [[context-pack-tangible-reader-memory-execution-spec-proposal-v1]]
→ GA Current-State Spine
→ Domain-State Hub
→ registry / bible / entity note / loss-payoff source
```

현재 작품의 정식 hierarchy는 [[architecture-rules]]를 그대로 따른다. 다른 프로젝트의 `Volume` 또는 고정 `60 Subact` 구조를 가져오지 않는다.

## 3. Node rules

1. Hub는 navigation only다. 새 story fact를 쓰지 않는다.
2. 부모와 자식은 서로 링크해 Obsidian backlink가 양방향으로 작동하게 한다.
3. Subact hub는 해당 GA의 Current-State Spine과 Context Pack 표준으로 연결한다.
4. Current-State Spine은 캐릭터·수집·기체·함선·무장·유물·기술·세력·장소·비주얼·손실/회수 domain hub로 fan-out한다.
5. exact entity note가 아직 없으면 새 사실을 만들지 않고 index/registry로 연결한다.
6. 197명 전원, 612성계 전부에 빈 엔티티 노트를 만들지 않는다. front-stage 승격 시에만 [[docs/_entities/README]] 규칙으로 개체 노트를 만든다.
7. 원고 본문에는 위키링크를 넣지 않는다.
8. Context Pack은 회차 집필 직전에 생성한다. 1,100개를 선생성하지 않는다.

## 4. Graph filters

노드 본문 첫 부분의 `Graph Node`, `GA`, `Act`, `Subact` 표기를 이용해 Obsidian 검색/필터를 적용한다.

추천 필터:
- `path:docs/_graph/ga`
- `path:docs/_graph/acts`
- `path:docs/_graph/subacts`
- `path:docs/_graph/state`

## 5. Root

- [[story-graph-root]]
