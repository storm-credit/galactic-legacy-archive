# Context Window Handoff Protocol — 새 대화 인계 규칙

Status: CANON PROJECT CONTROL
Owner Agent: PM Orchestrator / Context Custodian
Last Reviewed: 2026-08-03
Depends On: `CLAUDE.md`, GitHub workflow, project status documents
Used By: every long-running AI work session
Open Risks: platform context capacity cannot be measured exactly; trigger conservatively before continuity degrades

## 1. Standing User Requirement

When the active conversation context appears close to exhaustion, the assistant must not continue until continuity becomes unreliable and must not leave completed work only inside the chat.

The assistant must:

1. stop at the nearest safe work boundary;
2. commit and push all completed repository work;
3. open and merge a pull request when conflict-free and appropriate;
4. verify the actual GitHub result rather than relying on an expected merge state;
5. prepare a complete prompt that can be pasted into a new ChatGPT window;
6. tell the user exactly what was pushed, the last verified commit/PR, current project state and next action.

This is a persistent project operating rule.

---

## 2. Trigger Condition

Start the handoff process conservatively when any of the following is true:

- the current conversation has become long enough that earlier project decisions may be lost;
- the assistant detects a meaningful risk of context truncation;
- a large new phase would be safer in a fresh window;
- tool outputs, branch history or current work state can no longer be summarized reliably from active context;
- the user explicitly requests a handoff.

Do not wait for the context window to fail.

---

## 3. Mandatory Pre-Handoff GitHub Procedure

Before giving the new-window prompt:

### A. Stop at a safe boundary

- finish the current coherent document or explicitly mark the partial file/state;
- do not begin a new major phase;
- list incomplete items and their exact status.

### B. Persist work

- create/update repository files for every completed design decision;
- record assumptions, red-team findings and open risks;
- commit to the active work branch;
- do not claim work was saved if it exists only in the conversation.

### C. Pull request and merge

- create a PR with scope, decisions, gate result and open items;
- fetch the PR again and check `mergeable`;
- merge when conflict-free and consistent with project rules;
- if merge is blocked, leave the PR open and clearly state the blocking reason and branch name.

### D. Verify, do not assume

After merge:

- fetch PR metadata and confirm `merged=true`;
- verify at least one critical created/updated file directly from `main`;
- report the actual merge commit SHA;
- correct any earlier mistaken status immediately.

---

## 4. Required New-Window Prompt Contents

The handoff prompt must be self-contained and include all of the following.

### Project identity

- repository URL;
- project title;
- the project’s current design/drafting gate;
- the rule that canonical prose is blocked unless the current gate permits it.

### Verified GitHub state

- current base branch;
- last verified merge commit SHA;
- recently merged/open PR numbers and purposes;
- active branch if any;
- unresolved issue numbers that affect the next task.

### Current canon state

- what is complete;
- what is only conditionally passed;
- what is still open;
- critical names, terms, episode ranges and decisions needed for the next task.

### Exact continuation task

- the single next major objective;
- the ordered substeps;
- expected files to create/update;
- required red-team and gate checks;
- whether the work should be merged automatically when complete.

### Mandatory operating constraints

- work as the novel PM orchestra and fixed specialist agents;
- inspect repository files before making assumptions;
- do not rewrite completed canon without change control;
- log deviations and reasons;
- use references only for structural analysis, never sentence-level imitation;
- continue automatically without unnecessary confirmation;
- push all completed work and verify the merge result;
- repeat this handoff protocol again before the new context window is exhausted.

---

## 5. Standard Prompt Skeleton

Use the following structure, replacing every placeholder with verified information.

```markdown
다음 GitHub 저장소를 기준으로 작업을 이어서 진행해줘.

저장소:
https://github.com/storm-credit/galactic-legacy-archive

프로젝트:
《은하유산록》 장편 SF 웹소설 설계도·설정집

## GitHub 검증 상태

- 기준 브랜치: main
- 마지막으로 실제 병합 확인한 커밋: `<MERGE_SHA>`
- 최근 병합 PR: `<PR NUMBERS AND PURPOSES>`
- 열린 PR/작업 브랜치: `<OPEN PR OR NONE>`
- 관련 이슈: `<ISSUE NUMBERS>`

반드시 GitHub에서 위 상태와 핵심 파일을 다시 확인한 뒤 진행해라. PR이 병합됐다고 추정하지 말고 `merged=true`와 main 파일 존재를 직접 확인해라.

## 현재 프로젝트 상태

`<COMPLETED / CONDITIONAL / OPEN STATUS>`

핵심 정본 결정:
- `<CANON DECISION 1>`
- `<CANON DECISION 2>`
- `<CANON DECISION 3>`

아직 금지된 작업:
- `<BLOCKED WORK>`

## 이번에 이어서 할 정확한 작업

목표:
`<NEXT OBJECTIVE>`

순서:
1. `<STEP 1>`
2. `<STEP 2>`
3. `<STEP 3>`
4. 레드팀 검토와 게이트 판정
5. 상태 문서 기록
6. PR 생성·검수·병합
7. main에서 merged=true와 핵심 파일 존재 검증

## 반드시 지킬 운영 규칙

- 단일 작가가 아니라 소설 PM 오케스트라로 작업한다.
- 필요한 전문 에이전트를 고정하고 각 전문영역을 깊게 검토한다.
- 저장소의 CLAUDE.md와 정본 상태 문서를 먼저 읽는다.
- 이미 확정된 설정은 임의로 변경하지 않는다.
- 변경이 필요하면 원안·변경안·이유·파급효과를 기록한다.
- 맹점 훑기와 반대 관점 레드팀을 반드시 수행한다.
- 한국 웹소설 참고는 구조·보상·리듬만 분석하고 문장을 모사하지 않는다.
- 불필요한 확인 질문 없이 자동으로 끝까지 진행한다.
- 완료된 작업은 반드시 GitHub에 푸시한다.
- 컨텍스트가 부족해지기 전에 이 규칙과 같은 새 창 인계 프롬프트를 만들고 마지막 커밋·PR·다음 작업을 사용자에게 보고한다.
```

---

## 6. User-Facing Handoff Report Format

The message to the user must clearly state:

- `푸시 완료` or `푸시 미완료 — reason`;
- branch name;
- PR number and actual merged/open state;
- verified merge commit SHA when merged;
- files or work package completed;
- unresolved work;
- one copy-ready new-window prompt.

Do not make the user reconstruct the continuation state from scattered messages.

---

## 7. Failure Conditions

The handoff fails if:

- completed work remains only in chat;
- the assistant says “merged” without verifying `merged=true`;
- the prompt omits the exact next task;
- the prompt depends on hidden context from the old conversation;
- open risks, blocked gates or incomplete files are presented as complete;
- the assistant continues major work after detecting serious context-loss risk without first persisting and handing off.

---

## 8. Current Rule Status

> **CANON — MANDATORY FOR ALL FUTURE LONG SESSIONS**

This protocol remains active even when the assistant appears to remember the project. The repository is the durable source of truth; conversation memory is supplementary.