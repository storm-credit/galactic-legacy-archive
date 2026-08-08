# Canonical Name Errata 005 — P-001

Status: CANON OVERRIDE
Owner Agent: O01 Canon
Last Reviewed: 2026-08-08
Decision Authority: Author explicit instruction
Supersedes: P-001 reader-facing name in [[core-canonical-names-and-voice-lock-v1]], the unlocked identity field in [[protagonist-p001-bible-v1]], and every matching reader-facing reference in scene cards, manuscripts, indices and design documents

## Correction

Old reader-facing name:
- `리안 카르도 / Rian Cardo`.

Final canonical name:
- **`리안 칼데르 / Rian Calder`**.

Project code:
- `P-001` — unchanged.

Everyday call:
- `리안` — unchanged.

Korean pronunciation lock:
- `리안 칼데르`.
- Do not shorten the family name to `칼더`, `칼데`, or another variant.

## Decision Scope

This correction changes only the protagonist's reader-facing family name.

The following remain unchanged:
- given name `리안 / Rian`;
- P-001 identity, age, origin and legal status;
- former-life role and current-life progression;
- personality, voice, relationships, titles and authority limits;
- chronology, events, casualties, losses, mysteries and ending;
- all project codes and dependency links.

## Reason

- `카르도` had no established in-world etymology or plot function in the effective canon.
- the author judged `리안 카르도` insufficiently strong and memorable for the regression ace / defeated-admiral protagonist;
- `리안 칼데르` preserves the compact mixed-frontier naming pattern while giving later formal uses such as `칼데르 제독` a clearer and more forceful cadence;
- no retroactive family, nobility, regional, route or bloodline meaning is created by this rename.

## Propagation

1. All future prose, scene cards, bibles, maps, indices, dialogue audits and reader-facing metadata use `리안 칼데르 / Rian Calder`.
2. The active E1 v2 manuscript is updated at every full-name exposure.
3. Legacy design files, old manuscripts, audit records, merged PR descriptions and Git history may retain `리안 카르도 / Rian Cardo` as historical text; under the canon hierarchy those references are read as `리안 칼데르 / Rian Calder` unless the document explicitly discusses this rename.
4. Do not perform blind repository-wide replacement inside historical decision records, prior audit evidence or archived/noncanon drafts.
5. New full-name exposure must follow `D-20260808-01`: first formal introduction, identity confirmation, official record or responsibility attribution only; ordinary narration continues to use `리안`.

## Propagation Execution Record — 2026-08-08

개명 PR(#99)은 이 errata, [[decision-log]], [[effective-canon-status-manifest-v1]]만 갱신하고 **활성 정본 문서에는 전파되지 않았다.** 그 결과 다음 상태가 약 하루 동안 유지됐다.

- [[core-canonical-names-and-voice-lock-v1]] §2 Final Lock과 §11 Canon Status가 구명 `리안 카르도 / Rian Cardo`를 정본으로 표시
- [[reader-facing-terminology-phonetics-and-register-bible-v1]] §4 Protected Core Names(독자 기억·발음 권위)가 구명으로 등재 — **낭독 스킬이 구현되면 틀린 이름을 발음하게 되는 상태**
- [[master-series-chronology-v1]], [[ga1-10-state-checkpoint-matrix-v1]] 등 인물 표를 가진 상태 문서가 구명 유지
- GA1~GA10 활성 캐스트·작전·하드웨어 설계 문서 16개가 `Rian Cardo` 유지

Propagation §1이 요구한 범위를 실제로 집행했다.

- 활성 설계·정본 문서 **20개 파일 / 24건**을 `리안 칼데르 / Rian Calder`로 갱신
- 지명 `Cardo Verge`는 인물명이 아니므로 변경하지 않음 (2건)
- §3~§4에 따라 errata 문서, [[decision-log]], 비정본 문체 샘플, `manuscript/ga1/*-v1.md` 구초안은 역사 텍스트로 보존
- 재발 방지: `CLAUDE.md` §12 **개명 전파 규칙** 신설 — 정본 인물명 변경 시 잠금 문서·발음표·상태 표·활성 설계 문서를 같은 PR에서 갱신하도록 강제

## Canon Effect

Effective immediately, `리안 칼데르 / Rian Calder` is the only valid reader-facing canonical full name for P-001.
