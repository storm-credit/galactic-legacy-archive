# Obsidian Story Graph Deep Wiring Audit — 2026-08-22

Status: CANONICAL QC RECORD
Effective Authority: WORKFLOW/QC NAVIGATION ONLY — NOT A STORY OR SETTINGS SOURCE
Story Canon Effect: NONE
Publication: NOT AUTHORIZED
Owner Agents: A00 PM / N02 Act Architecture / N03 Episode / O01 Canon / X04 Continuity / X06 Red Team
Last Reviewed: 2026-08-22
Depends On: [[architecture-rules]], [[effective-canon-status-manifest-v1]], [[ga10-ending-reconciliation-canon-amendment-2026-08-20]], [[full-series-context-pack-generated-manifest-v1]], [[full-series-context-writer-activation-manifest-v1]], [[full-series-collection-desire-manifest-v1]], [[prewriting-execution-redteam-v2-final-verdict-2026-08-22]], [[docs/_graph/README]]
Used By: [[story-graph-root]], Obsidian vault navigation, Context Pack preparation, continuity review
Open Risks: heading-anchored links depend on Context/Activation/CLSET heading text; G8 is the regression gate that keeps them honest

---

## 1. 이 기록이 존재하는 이유

설계층은 이미 완료돼 있었다 — GA1~GA10, Act 40, Subact 160, E001–E1100 상세설계, Context 1100/1100, Writer Activation 1100/1100, Collection thread 415/415, CLSET 160/160, GA10 결말 재조정. **없었던 것은 설계가 아니라 그 사이를 잇는 클릭 가능한 간선이었다.**

작가가 "GA5 C2를 쓸 차례"라고 생각했을 때 열어야 하는 문서는 최소 여섯 개다 — 액트맵, 상세 회차 카드, Context Pack, Writer Activation, CLSET, 구간 상태·손실 문서. 저장소는 그 여섯 개를 모두 갖고 있었지만, **어느 문서에서도 나머지 다섯 개로 한 번에 갈 수 없었다.**

이 감사는 그 간선을 만들고, 간선이 조용히 낡지 않도록 기계로 잠근 기록이다.

---

## 2. PR #197을 그대로 병합하지 않은 이유

| 항목 | PR #197 (2026-08-20 작성) | 현재 `main` |
|---|---|---|
| 기준 | `behind_by=15`, `ahead_by=14`, `diverged` | 770c5aa |
| Context 전제 | 「Context Pack은 회차 집필 직전에 생성한다. 1,100개를 선생성하지 않는다」 | Context 1100/1100 · Writer Activation 1100/1100 완료 (PR #208·#210) |
| Collection 전제 | GA 등록부까지만 | Collection thread 415/415 · CLSET 160/160 완료 (PR #211) |
| Red-Team | 없음 | v2 S0/S1/S2 = 0/0/0 (PR #214·#216) |
| Subact 허브 내용 | 손으로 쓴 8줄 껍데기 — 회차 범위·Context·Activation·CLSET 링크 없음 | — |
| 임시 workflow | `one-shot-sync-story-graph-index.yml` (`contents: write` + `git push`) | — |

PR #197의 노드는 **작성 당시에는 맞았지만 지금은 실행층의 절반을 모른다.** 그대로 병합하면 160개 허브가 "Context는 아직 없다"는 전제 위에 서 있게 되고, 충돌 해결 과정에서 정본이 구 PR 쪽으로 되돌아갈 위험이 있었다.

따라서 최신 `main`에서 새 브랜치를 만들고, PR #197의 **유효 자산만** 이식했다.

### 이식한 것

- 폴더 구조 `docs/_graph/{ga,acts,subacts,state}`와 노드 명명 규칙;
- 233노드 shape (1 README + 1 Root + 10 GA + 40 Act + 160 Subact + 10 Spine + 11 Domain);
- 11개 Domain-State Hub의 라우팅 대상과 authority guard 문장;
- `tools/validate_story_graph.py`의 검사 골격 (노드 수, 부모/자식, 체인, 링크 해석);
- `_entities/README.md` §6 Story Graph 연결 규칙;
- `Volume` / 고정 `60 Subact` 타 프로젝트 계층 유입 금지 가드;
- read-only `validate-story-graph.yml`.

### 폐기한 것

- 손으로 쓴 233개 노드 본문 → **생성기로 대체** (§3);
- `one-shot-sync-story-graph-index.yml` → 삭제하고 그 효과(`build_index.py`의 `_graph` 제외)를 브랜치에 직접 커밋;
- `docs/_index/story-graph-navigation.md` → `_index/`는 생성 폴더이므로 손으로 쓴 노트를 두지 않고, `build_index.py`의 `QUICK_LINKS`에 [[story-graph-root]]를 넣어 [[HOME]]이 가리키게 함;
- README의 "Context Pack 1,100개를 선생성하지 않는다" 문장 (현재 상태와 반대).

PR #197은 **superseded**다. 대체 PR과 병합 SHA는 §9에 기록한다.

---

## 3. 왜 손으로 쓰지 않고 생성하는가

PR #197의 README는 상세 카드 파일명을 160개 허브에 넣지 않기로 했다. 이유는 타당했다 — 「카드 배치가 재분할될 때 160개 허브가 조용히 낡는 것을 막기 위한 단일진실원칙」.

**그 문제의 해법은 링크를 빼는 것이 아니라 손으로 쓰지 않는 것이다.** 저장소는 이미 같은 결론에 세 번 도달했다 — [[HOME]] (§17), [[CATALOG]] (§18), [[episode-briefs]] (§22). 인덱스를 손으로 쓰면 낡고, 생성하면 `--check`가 낡음을 CI 실패로 만든다.

```bash
python tools/build_story_graph.py          # 생성
python tools/build_story_graph.py --check  # 낡았으면 실패 (CI가 실행)
```

`tools/story_graph_sources.py`가 액트맵·Context·Activation·CLSET을 한 번 읽고, 생성기와 검증기가 **같은 파서를 공유한다.** 두 도구가 소스에 대해 서로 다른 이야기를 할 수 없다.

생성기는 소스가 어긋나면 파일을 쓰지 않고 즉시 실패한다:

- 액트맵이 GA당 4 Act / Act당 4 Subact를 만들지 않으면;
- 액트맵의 서브액트 회차 범위와 CLSET 맵의 범위가 다르면;
- 서브액트 첫 회차에 해당하는 Context/Activation 항목이 없으면;
- GA 액트맵의 전체 범위가 선언된 대액트 범위와 다르면.

---

## 4. 만들어진 간선

| 층 | 노드 | 각 노드가 여는 것 |
|---|---:|---|
| Series Root | 1 | 10 GA · 11 Domain · 실행층 장부 · 결말 정본 |
| Grand Act Hub | 10 | 액트맵 · GA 등록부 · Context · Activation · CLSET · 4 Act · State Spine |
| Act Hub | 40 | 액트맵 해당 ACT 표제 · 4 Subact (제목·회차·CLSET 표) |
| Subact Hub | 160 | 아래 §4.1 |
| GA State Spine | 10 | 구간 상태 문서 전부 + 11 Domain fan-out |
| Domain-State Hub | 11 | registry / bible / entity note / 손실·회수 장부 |

### 4.1 Subact Hub 한 개가 여는 것

- 계층: Series · Grand Act · Act · **previous / next Subact**
- 승인 구조: 액트맵의 **해당 서브액트 표제**, 회차 범위가 겹치는 **상세 회차 설계 카드**
- 집필 실행층: 해당 GA Context Pack의 **첫 회차 표제**, Writer Activation의 **첫 회차 표제**, [[episode-briefs]], Context 규격, [[manuscript-production-workflow-v1]]
- 수집욕: `CLSET-*` ID와 CLSET 맵의 **해당 서브액트 표제**, GA 수집 등록부, 전 시리즈 수집 장부
- 상태·손실·권한: GA State Spine, 회차 범위가 겹치는 collection/loss · operations · institution/authority · law/evidence · QC 문서, 시리즈 3대 장부
- GA10 D 4개: 결말 정본 3종 추가

### 4.2 계측

| 항목 | 값 |
|---|---:|
| `docs/_graph` Markdown 노드 | 233 |
| 총 위키링크 | 5,657 |
| 그래프 내부 간선 | 2,234 |
| 정본·실행층으로 나가는 링크 | 3,423 |
| 서로 다른 외부 대상 문서 | 378 |
| 표제 앵커 링크 (`[[file#heading]]`) | 676 |
| Context 링크가 붙은 Subact | 158 생성층 + 2 수동(E001–E010) = 160/160 |
| Writer Activation 링크가 붙은 Subact | 160/160 |
| CLSET 링크가 붙은 Subact | 160/160 |
| 회차범위 일치 상세 설계 카드가 붙은 Subact | 160/160 |
| **본문이 서로 다른 Subact 허브** | **160/160** |
| previous/next 체인 | GA01 A1 → GA10 10D-4, 끊김 0 |

`160/160 distinct` 는 §11-3(모든 Subact가 같은 형식의 빈 껍데기가 아닌가)에 대한 기계 답변이다. 각 허브는 자기 회차 범위에서 실제로 겹치는 문서만 링크하므로, 상태 문서 개수 분포가 1~10으로 갈라진다.

---

## 5. E001–E010 예외

[[full-series-context-pack-generated-manifest-v1]]에 따라 생성 Context는 E011부터 시작하고, E001–E010은 수동 FULL 팩이 우선한다. 따라서 GA1 A1(E1–E5)·A2(E6–E10) 두 허브만 [[ga1-e001-e010-context-pack-status-index-v1]]와 [[full-series-context-writer-activation-manifest-v1]](Depth-A override)를 가리킨다. 나머지 158개는 GA별 생성 Context/Activation의 첫 회차 표제를 가리킨다.

이 예외는 생성기와 검증기가 같은 상수(`GENERATED_CONTEXT_FLOOR = 11`)로 알고 있으며, 임의로 채운 값이 아니다.

---

## 6. 기계 검증

```bash
python tools/validate_story_graph.py --selftest   # 31 cases
python tools/validate_story_graph.py
python tools/build_story_graph.py --check
```

| ID | 검사 | 잡는 것 |
|---|---|---|
| G1 | 노드 인벤토리 | 233노드 shape 붕괴, domain hub 소실, authority guard 문장 소실 |
| G2 | 부모/자식 상호참조 | 자식이 주장한 부모가 자식을 되받지 않음 (백링크 단절) |
| G3 | 시간축 체인 | previous/next 끊김, 마지막 서브액트가 Root로 복귀하지 않음 |
| G4 | 고아 노드 | 어떤 그래프 노드도 가리키지 않는 Act/Subact |
| G5 | 위키링크 해석 | 깨진 링크, 모호한 동명 링크, 깨진 전체경로 링크 |
| G6 | 대액트 소스 결속 | 노드가 다른 GA의 액트맵·등록부를 인용 |
| G7 | 실행층 링크 | Context / Writer Activation / CLSET / State Spine / episode-briefs 누락 |
| G8 | 표제 앵커 해석 | Context·Activation·CLSET 표제가 바뀌어 앵커가 조용히 죽음 |
| G9 | GA10 결말 권위 | D구간이 결말 정본을 인용하지 않음, 구 배치(E1099·CY748-01) 부활 |
| G10 | workflow 잔류 | branch-only one-shot workflow, `contents: write`, `git push`, 브랜치명 checkout |
| G11 | 원고 오염 | 그래프가 `manuscript/` 산문 파일을 링크 |

**G8과 G9는 이 저장소가 실제로 겪은 실패 유형을 옮긴 것이다.** G8은 §22가 기록한 "구조는 있었는데 쓰는 순간 손에 쥐여지지 않았다"의 링크판이고, G9는 §12가 기록한 개명 미전파(PR #99가 errata만 갱신해 정본 잠금이 구명을 유지)의 결말판이다.

`--selftest` 31케이스가 **각 검사가 실제로 발화하는지** 증명한다. 발화를 증명하지 못하는 검사는 없는 것과 같다 (§13).

### 실행 결과 (2026-08-22)

| 명령 | 결과 |
|---|---|
| `validate_story_graph.py --selftest` | PASS — 31 cases |
| `validate_story_graph.py` | PASS |
| `build_story_graph.py --check` | current (233 nodes) |
| `validate_canon.py --selftest` | PASS — 39 cases |
| `validate_canon.py` | PASS |
| `build_index.py --check` | current |
| `build_catalog.py --check` | current |
| `build_census.py --check` | current |
| `build_open_questions.py --check` | current |
| `build_episode_briefs.py --check` | current (main에서 stale이던 것을 재생성) |
| `promotion_review.py --check` | current |

---

## 7. 맹점 훑기 / 레드팀

| # | 공격 | 판정 | 근거 |
|---:|---|---|---|
| 1 | Graph Hub가 두 번째 정본이 됐는가 | NO | 허브는 사건·날짜·상태를 서술하지 않는다. 본문은 링크·표제·회차 범위뿐이며, 회차 범위는 액트맵에서 읽어 온 값이다. 모든 노드에 `NOT A STORY SOURCE`와 해석 순서 5단계를 명시. |
| 2 | 설명 복제로 정본과 갈라질 위험 | NO | 정본 문장을 복사하지 않는다. 유일하게 재현되는 값(회차 범위·서브액트 제목·CLSET ID)은 매 실행마다 소스에서 다시 읽으며, 어긋나면 생성기가 실패한다. |
| 3 | 160개가 같은 빈 껍데기인가 | NO | 본문 해시 160/160 distinct. 상태 문서 개수 분포 1~10. |
| 4 | Context/Collection 링크가 실제 해당 범위를 가리키는가 | YES | Context/Activation은 서브액트 **첫 회차의 실제 표제**로 앵커되고, CLSET은 **해당 서브액트 표제**로 앵커된다. 앵커 문자열이 대상 파일의 표제와 일치하는지 G8이 검사한다(676개). 액트맵과 CLSET 맵의 회차 범위가 다르면 생성 자체가 실패한다. |
| 5 | GA1만 세밀하고 GA2–GA10은 형식적인가 | NO | GA당 Subact 16개로 균일. 상세 회차 카드 링크는 GA1 16/16, GA2–GA10 144/144. GA1이 오히려 카드 수가 적다(비정본 E1–5 샘플 제외). |
| 6 | 최신 GA10 결말 대신 과거 카드를 가리키는가 | NO | GA10 D 4개 허브 전부가 [[ga10-ending-reconciliation-canon-amendment-2026-08-20]]·결정 기록·crosswalk를 인용하고, E1076–1095 = CY748 본편 / E1096–1100 = CY751 에필로그를 명시한다. G9가 구 배치 부활을 차단한다. |
| 7 | 엔티티 노트 대량 생성으로 신호를 죽였는가 | NO | 새 엔티티 노트 0개. `docs/_entities`는 README 1개만 수정. 197명·612성계 placeholder 생성 없음. |
| 8 | Series → GA → Act → Subact → 실행층이 실제 클릭 가능한가 | YES | §8 경로 시험 참조. |
| 9 | 상세카드에서 상위로 돌아올 수 있는가 | YES | 상세 카드는 자기 `Depends On`으로 액트맵을 가리키고, 액트맵의 백링크 패널에 해당 Act/Subact 허브가 나타난다. 허브→카드 간선이 생겼으므로 카드의 백링크에서 허브로 역주행할 수 있다. |
| 10 | Obsidian에서는 열리지만 validator에서는 깨지는 링크 | NO | G5가 저장소 전체 stem·경로 색인으로 233노드의 5,657개 링크를 전부 해석한다. C1(validate_canon)도 같은 링크를 독립 검사한다. |
| 11 | 재실행 시 동일 결과인가 | YES | `--check`가 재실행 결과와 디스크를 바이트 비교한다. 시간·난수 입력 없음. |
| 12 | 새 canon·관계·사망·기술·권한을 조용히 만들었는가 | NO | §9 변경 감사 참조. |

### 남은 위험

- **표제 의존**: 676개 앵커는 Context/Activation/CLSET 표제 문자열에 묶인다. 표제가 바뀌면 앵커가 죽는다 — G8이 CI에서 실패로 만들지만, 고치는 방법은 표제를 되돌리는 것이 아니라 **그래프를 재생성하는 것**이다.
- **상세 카드 재분할**: 카드 파일명의 회차 범위가 바뀌면 링크 대상이 바뀐다. 재생성이 자동으로 따라간다.
- **`docs/_graph`는 고아 지표에서 제외된다**: §17의 인덱스와 같은 이유다. 그래프는 거의 모든 설계 문서를 가리키므로 포함하면 "들어오는 링크 없음"이 항상 0에 가깝게 나오고 실제 진행도를 가린다. `build_index.py`의 `skip`에 `_graph`를 추가했다.

---

## 8. Obsidian 사용성 — 실제 경로 시험

**Vault root = 저장소 루트** (`galactic-legacy-archive/`). `docs/`를 볼트로 열면 안 된다 — [[CLAUDE]], [[docs/_entities/README]], [[docs/_graph/README]] 형태의 링크가 깨진다.

**시작 문서**: `docs/_graph/story-graph-root.md` ([[story-graph-root]])

필수 커뮤니티 플러그인 없음. 기본 Obsidian의 위키링크·백링크·그래프뷰·검색만으로 아래 경로가 전부 동작한다.

| # | 경로 | 결과 |
|---:|---|---|
| 1 | Root → [[graph-ga01-hub]] → [[graph-ga01-act-a]] → [[graph-ga01-subact-a1]] | OK |
| 2 | Subact → 액트맵 해당 표제 (`first-100-act-map-v2-consolidated#A1 — 기록되지 않은 생도 / Episodes 1–5`) | OK |
| 3 | Subact → Context (GA1 A1은 수동 인덱스, GA2 2A-1은 `ga2-e101-e210-context-packs-v1#E101 — 배보다 먼저 도착한 빚`) | OK |
| 4 | Subact → Writer Activation | OK |
| 5 | Subact → CLSET (`ga2-collection-desire-subact-map-v1#2A-1 — 배보다 먼저 도착한 빚 / E101–E107`) | OK |
| 6 | Subact → [[graph-ga02-state-spine]] → Domain Hub → registry/bible | OK |
| 7 | [[graph-ga10-subact-d4]] → [[ga10-ending-reconciliation-canon-amendment-2026-08-20]] | OK |
| 8 | previous/next로 GA01 A1 → GA10 10D-4 완주 | OK, 끊김 0 |
| 9 | 상세 카드 → 백링크 패널 → 상위 Subact/Act 허브 | OK |

동명 basename 충돌은 저장소 전체에서 0건이었으므로 전체 경로 위키링크는 `docs/_entities/*`와 `docs/_graph/README` 두 경우에만 사용했다. 존재하지 않는 파일을 링크로 만든 곳은 없다(G5 = 0).

`.obsidian/` 개인 설정은 커밋하지 않는다.

---

## 9. 변경 감사

| 항목 | 값 |
|---|---:|
| 원고 파일 변경 | 0 |
| 원고 신규·수정·v3/v4 생성 | 0 |
| `AUTHOR-APPROVED` 승격 | 0 |
| 새 사건·반전·결말 | 0 |
| 기존 결말 변경 | 0 |
| 사망·생존 변경 | 0 |
| 관계 변경 | 0 |
| 영구 손실 복구 | 0 |
| 새 능력·기술·권한 | 0 |
| 액트맵·상세 회차 카드 변경 | 0 |
| Context Pack / Writer Activation / CLSET 내용 변경 | 0 |
| 새 엔티티 노트 | 0 |
| PR #188 NONCANON 종족·문명 승격 | 0 |
| PR #190 구 결말 S1 판정 복원 | 0 |
| `.obsidian/` 커밋 | 0 |
| 공개·출판 승인 | 0 |

정본 텍스트를 건드린 파일은 `docs/_entities/README.md` 한 개이며, 변경 내용은 §6 절 추가와 헤더 갱신뿐이다(설정 사실 없음).

`docs/_index/episode-briefs.md`는 PR #217 이후 stale이던 생성물을 재생성한 것이다(E005 v2 → v3 표기 1줄). §21-3에 따른 정리이며 원고 변경이 아니다.

---

## 10. 판정

> **OBSIDIAN STORY GRAPH: 233 NODES WIRED AND MACHINE-LOCKED**
>
> **PATH Series → GA → Act → Subact → Context / Activation / CLSET → State: CLICKABLE 160/160**
>
> **GA10 ENDING AUTHORITY: 2026-08-20 AMENDMENT, 4/4 D-SUBACTS**
>
> **STORY CANON CHANGE: 0 · MANUSCRIPT CHANGE: 0**
>
> **PR #197: SUPERSEDED**
>
> **PUBLICATION: NOT AUTHORIZED**

이 기록은 탐색 계층의 완성만 판정한다. 원고 승인, 공개, 유료연재는 별도 게이트이며 [[prewriting-execution-redteam-v2-final-verdict-2026-08-22]]의 권한 경계가 그대로 유지된다.
