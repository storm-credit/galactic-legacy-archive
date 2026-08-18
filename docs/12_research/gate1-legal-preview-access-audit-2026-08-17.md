# Gate 1 Legal Preview Access Audit — 2026-08-17

Status: RESEARCH CONTROL — ACCESS AUDIT, NOT PROSE ANALYSIS
Owner Agents: A02 Market & Reference / R03 Korean Webnovel / O02 Gate
Last Reviewed: 2026-08-17
Depends On: [[reference-study-plan]], [[gate1-reference-baseline]], [[gate1-pattern-synthesis]], issue #3
Used By: issue #3 completion planning, legal-preview deep-read queue
Publication: NOT AUTHORIZED
Open Risks: official platform detail pages expose free-scope metadata, but this audit did not retrieve or store the actual free episode prose; sentence/paragraph analysis and exact E1–20 beat verification therefore remain open

## 1. Purpose

Issue #3 remained open because the public-source baseline did not prove exact first-five/first-twenty behavior or sentence/paragraph rhythm.

This audit separates two different questions that had been conflated:

1. **ACCESS** — does an official/legal platform currently expose enough free material to support the requested E1–5 / E1–20 study?
2. **DEEP-READ** — has the actual free prose been read and coded for hook, reward, paragraph rhythm, dialogue/exposition placement and action delivery?

A work may pass ACCESS while remaining OPEN for DEEP-READ.

## 2. Method and boundary

- Verified 2026-08-17 against official NAVER Series product pages.
- Recorded only platform-visible metadata such as free episode count, serial status and product identity.
- Did **not** copy paid prose.
- Did **not** infer sentence rhythm from synopsis copy, episode titles or catalog metadata.
- Did **not** treat “free on the platform” as “episode body successfully retrievable by the current research agent.”
- Current web retrieval exposes product/detail metadata reliably but does not expose the episode viewer body in a form suitable for responsible prose measurement.

Therefore this document is an **accessibility audit**, not completion evidence for the prose-analysis portion of issue #3.

## 3. Korean reference access matrix

| ID | Work | Official source | Current listed free scope | E1–5 legal scope | E1–20 legal scope | Agent body-text retrieval in this audit | Current research verdict |
|---|---|---|---:|---|---|---|---|
| K01 | 《배드 본 블러드》 | NAVER Series `productNo=10311211` | 25 episodes free | YES | YES | NO | ACCESS PASS / DEEP-READ OPEN |
| K02 | 《함장에서 제독까지》 | NAVER Series `productNo=5056372` | 25 episodes free | YES | YES | NO | ACCESS PASS / DEEP-READ OPEN |
| K03 | 《당신의 머리 위에》 | NAVER Series `productNo=1471661` | 26 episodes free | YES | YES | NO | ACCESS PASS / DEEP-READ OPEN |
| K04 | 《철수를 구하시오》 | NAVER Series `productNo=5275901` | 25 episodes free | YES | YES | NO | ACCESS PASS / DEEP-READ OPEN |
| K05 | 《납골당의 어린 왕자》 | NAVER Series `productNo=2470441` | 15 episodes free | YES | **NO on serial free count alone** | NO | ACCESS PARTIAL / DEEP-READ OPEN |
| K06 | 《퓨전펑크에서 살아가는 법》 | NAVER Series `productNo=11901728` | 25 episodes free | YES | YES | NO | ACCESS PASS / DEEP-READ OPEN |
| K07 | 《퓨전펑크의 전생자》 | NAVER Series `productNo=9707944` | 25 episodes free | YES | YES | NO | ACCESS PASS / DEEP-READ OPEN |
| K08 | 《픽 미 업!》 | NAVER Series `productNo=3202024` | 20 episodes free | YES | YES | NO | ACCESS PASS / DEEP-READ OPEN |
| K09 | 《게임 속 바바리안으로 살아남기》 | NAVER Series `productNo=6037518` | 25 episodes free | YES | YES | NO | ACCESS PASS / DEEP-READ OPEN |
| K10 | 《킬 더 드래곤》 | NAVER Series `productNo=5987441` | 25 episodes free | YES | YES | NO | ACCESS PASS / DEEP-READ OPEN |

### Official product URLs

- K01: `https://series.naver.com/novel/detail.series?productNo=10311211`
- K02: `https://series.naver.com/novel/detail.series?productNo=5056372`
- K03: `https://series.naver.com/novel/detail.series?productNo=1471661`
- K04: `https://series.naver.com/novel/detail.series?productNo=5275901`
- K05: `https://series.naver.com/novel/detail.series?productNo=2470441`
- K06: `https://series.naver.com/novel/detail.series?productNo=11901728`
- K07: `https://series.naver.com/novel/detail.series?productNo=9707944`
- K08: `https://series.naver.com/novel/detail.series?productNo=3202024`
- K09: `https://series.naver.com/novel/detail.series?productNo=6037518`
- K10: `https://series.naver.com/novel/detail.series?productNo=5987441`

## 4. Access result

### 4.1 First-five study

- **10 / 10** references currently list at least five free serial episodes.
- Therefore the first-five research requirement is not blocked by a paywall at the platform-access level.

### 4.2 First-twenty study

- **9 / 10** references currently list at least twenty free serial episodes.
- K05 《납골당의 어린 왕자》 lists 15 free serial episodes, so exact serial E1–20 cannot be claimed available from that listing alone.
- NAVER Series separately lists the K05 collected-volume edition with **volume 1 free**, but this audit does not assume how that volume maps to serial episode numbers. It may be investigated separately if needed.

### 4.3 What this changes

The remaining research gap is **not primarily “we do not know where legal samples exist.”** For nine of ten targets, the official platform currently advertises enough free serial scope to cover E1–20; all ten cover E1–5.

The gap is now narrower and more explicit:

> **actual legal-preview deep-read and coding have not been completed / recorded.**

## 5. What still cannot be marked complete

Do not close issue #3 based on this audit alone.

Still required if the original completion contract is kept literally:

1. read actual legal/public E1–5 prose for the selected sample set;
2. code each episode by opening hook, immediate problem, reward/cost, ending hook and information-release function;
3. for works with legal E1–20 scope, verify reward cadence from actual episode content rather than titles/synopses;
4. measure paragraph/sentence tendencies from the legal sample without storing or reproducing copyrighted passages;
5. record dialogue/exposition/action placement as abstract observations, not copied language;
6. update [[gate1-pattern-synthesis]] only where direct sample evidence supports or corrects the provisional baseline;
7. keep living-author imitation prohibited.

## 6. Minimum deep-read evidence schema

For each studied episode, store observations only:

```markdown
Work:
Episode:
Official/free source verified:
Opening function:
Immediate concrete problem:
POV / distance:
Paragraph tendency: short / medium / mixed + observational note
Dialogue placement:
Exposition placement:
Action-space clarity:
Primary reward / state change:
Cost / complication:
Ending hook type:
Proper-noun load:
Transferable principle:
Similarity / imitation risk:
```

Do **not** store full prose or long quotations.

## 7. Recommended sampling strategy

A literal 10-work × 20-episode prose study would be 200 episodes and is not necessary to answer every craft question with equal depth.

Use a two-tier sample unless the author explicitly requires exhaustive 200-episode coding:

### Tier A — all ten works, E1–5

- 50 episodes total.
- validates opening promise, first-five progression, terminology load and early ending hooks across the full Korean reference set.

### Tier B — role-selected E1–20 deep dives

Choose at least one strong reference per research function, with overlap allowed:

- space-opera / command growth: K02;
- SF problem-solving: K04;
- collection / roster retention: K08;
- future-knowledge tension / survival: K09;
- mecha / military-school pressure: K10;
- cyber/fusion world delivery: K06 or K07.

This keeps the research tied to the six tracks in [[reference-study-plan]] while avoiding pseudo-precision from mechanically coding every title.

## 8. Issue #3 status after this audit

> **PUBLIC-SOURCE BASELINE: COMPLETE**
>
> **LEGAL ACCESS DISCOVERY: PASS FOR E1–5 (10/10), PASS FOR E1–20 (9/10), PARTIAL FOR K05**
>
> **ACTUAL LEGAL-PREVIEW DEEP-READ: OPEN**
>
> **SENTENCE/PARAGRAPH RHYTHM VALIDATION: OPEN**
>
> **ISSUE #3: KEEP OPEN**

This audit does not change current manuscript authority, does not re-close the author-opened first-draft gate, and does not authorize publication.
