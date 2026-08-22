# Story Graph Navigation Layer — 옵시디언 서사 그래프 계층

Status: CANON FOR NAVIGATION / NOT A STORY OR SETTINGS SOURCE
Owner Agents: A00 PM / N02 Act Architecture / N03 Episode / O01 Canon / X04 Continuity
Last Reviewed: 2026-08-22
Depends On: [[architecture-rules]], [[1000-episode-grand-act-map-v1]], [[effective-canon-status-manifest-v1]], [[context-pack-tangible-reader-memory-execution-spec-proposal-v1]], [[docs/_entities/README]]
Used By: Obsidian Graph View, act/subact navigation, Context Pack preparation, continuity review
Open Risks: navigation hubs accidentally becoming a duplicate canon source; graph clutter from creating empty entity notes

> [!warning] 생성 문서 — 직접 편집하지 마십시오
> `python tools/build_story_graph.py`가 이 파일을 덮어씁니다.
> 이 노트는 탐색 허브이며 정본이 아닙니다. 사건·날짜·상태·권한은 링크된 정본이 소유합니다.

## 1. 목적

이 폴더는 이미 존재하는 정본·Approved Structure·실행층·상태 장부를 **옵시디언에서 실제로 탐색 가능한 그래프**로 연결한다.

이 계층은 새 사건·설정·인물·기체·함선·장소·권한을 만들지 않는다. 정확한 사실과 회차 범위는 기존 정본이 소유한다.

## 2. 볼트 여는 법

- **Vault root = 저장소 루트** (`galactic-legacy-archive/`). `docs/`를 볼트로 열면 `[[CLAUDE]]`와 `[[docs/_entities/README]]` 형태의 전체 경로 링크가 깨진다.
- 시작 문서: [[story-graph-root]]
- 색인 진입점: [[HOME]] · [[CATALOG]] · [[episode-briefs]]
- 필요한 커뮤니티 플러그인은 없다. 기본 Obsidian의 위키링크·백링크·그래프뷰만으로 전 경로가 동작한다.

## 3. 경로

```text
[[story-graph-root]]
→ Grand Act Hub (10)
→ Act Hub (40)
→ Subact Hub (160)
├─→ Act Map 해당 서브액트 표제
├─→ 상세 회차 설계 카드
├─→ Context Pack 해당 회차 / Writer Activation 해당 회차
├─→ Collection Desire CLSET 해당 서브액트
├─→ 구간 상태·손실·권한 문서
└─→ GA Current-State Spine
       → Domain-State Hub (11)
       → registry / bible / entity note / loss-payoff ledger
```

Subact는 GA01 A1부터 GA10 10D-4까지 previous/next 링크로 하나의 시간축 체인을 이룬다.

## 4. 물리 규모

`docs/_graph/` Markdown 파일은 **233개**다.

| 종류 | 수 |
|---|---:|
| 규약 README | 1 |
| Series Root | 1 |
| Grand Act Hub | 10 |
| Act Hub | 40 |
| Subact Hub | 160 |
| GA Current-State Spine | 10 |
| Domain-State Hub | 11 |

## 5. 노드 규칙

1. 허브는 탐색 전용이다. 새 story fact를 쓰지 않는다.
2. 부모와 자식은 서로 링크해 옵시디언 백링크가 양방향으로 작동하게 한다.
3. Subact 허브는 액트맵 표제·상세 카드·Context·Writer Activation·CLSET·GA 등록부·상태 척추·손실/회수 장부로 연결한다.
4. Current-State Spine은 인물·수집·기체·함선·무장·유물·기술·세력·장소·비주얼·손실/회수 도메인 허브로 fan-out한다.
5. exact entity note가 아직 없으면 새 사실을 만들지 않고 index/registry로 연결한다.
6. 197명 전원, 612성계 전부에 빈 엔티티 노트를 만들지 않는다. front-stage 승격 시에만 [[docs/_entities/README]] 규칙으로 개체 노트를 만든다.
7. **원고 본문에는 위키링크를 넣지 않는다.** 그래프는 원고 파일을 링크하지 않는다.
8. Graph node가 더 최신이라는 이유로 액트맵, 상세카드, 상태장부, 손실장부, payoff ledger를 덮어쓰지 않는다.
9. 비주얼 graph는 설계 방향·독자 기억·anti-similarity guard를 연결하지만 exact face/hair/body/costume를 자동 정본화하지 않는다.
10. 현재 작품의 정식 hierarchy는 [[architecture-rules]]를 그대로 따른다. **다른 프로젝트의 `Volume` 또는 고정 `60 Subact` 구조를 가져오지 않는다.**

## 6. 현재 상태 해석 순서

1. 작가의 현재 지시 / Canon Amendment / Errata;
2. 액트맵 / 해당 상세 회차 카드;
3. GA Current-State Spine이 가리키는 구간 상태 문서;
4. state checkpoint / operational snapshot;
5. GA 수집 등록부;
6. 도메인 registry/bible;
7. front-stage 엔티티 노트가 있으면 그것;
8. 손실/회수/권한 장부;
9. 비주얼·독자기억 QC;
10. Context Pack / Writer Activation 실행 필드.

Context Pack과 Writer Activation은 이 결과를 집필 가능한 형태로 번역할 뿐 상위 사실을 바꾸지 않는다.

GA10 E1076–E1100은 [[ga10-ending-reconciliation-canon-amendment-2026-08-20]]가 유효 정본이다.

## 7. 생성과 검증

```bash
python tools/build_story_graph.py          # 생성
python tools/build_story_graph.py --check  # 낡았으면 실패 (CI가 실행)
python tools/validate_story_graph.py --selftest
python tools/validate_story_graph.py
```

- 이 폴더의 모든 파일은 생성물이다. **직접 편집하지 않는다** — 다음 실행이 덮어쓴다.
- 액트맵·Context·Activation·CLSET을 바꾸면 같은 PR에서 재생성한다. CI의 `--check`가 강제한다.
- QC 기록: [[obsidian-story-graph-deep-wiring-audit-2026-08-22]]

## 8. 그래프 필터

노드 머리의 `Graph Node`, `GA`, `Act`, `Subact` 표기로 옵시디언 검색·필터를 적용한다.

- `path:docs/_graph/ga`
- `path:docs/_graph/acts`
- `path:docs/_graph/subacts`
- `path:docs/_graph/state`

## 9. 진입

- [[story-graph-root]]
