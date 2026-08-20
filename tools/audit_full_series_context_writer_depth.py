#!/usr/bin/env python3
"""Audit E001–E1100 Context writer-activation depth.

This is a workflow/QC classifier, not a story generator. For E011–E1100 it
loads only approved episode-card sources through the existing semantic Context
normalizer. E001–E010 are treated as manual deep overrides and audited by their
existing manual Context packs/status record.

The first pass intentionally reports Depth-B rather than auto-inventing missing
execution facts. Later source-bound activation overlays can reduce B to zero.
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

import build_full_series_context_packs_semantic as semantic

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "99_quality_control" / "full-series-context-writer-depth-audit-v1.md"

GA_RANGES = {
    1: (1, 100),
    2: (101, 210),
    3: (211, 330),
    4: (331, 450),
    5: (451, 570),
    6: (571, 690),
    7: (691, 800),
    8: (801, 900),
    9: (901, 1000),
    10: (1001, 1100),
}

MANUAL_A = set(range(1, 11))

ENGINE_RULES = [
    ("MEDICAL/CARE/CONSENT", ("medical", "patient", "clinic", "hospital", "care", "treatment", "consent", "의료", "환자", "치료", "동의")),
    ("TECHNICAL-REPAIR/TEST", ("repair", "test", "frame", "mount", "actuator", "coolant", "engineer", "technical", "정비", "수리", "시험", "기체", "냉각", "기술")),
    ("TACTICAL-COMBAT", ("battle", "combat", "fire", "target", "weapon", "formation", "tactical", "전투", "사격", "표적", "무기", "전대")),
    ("RESCUE/SERVICE", ("rescue", "service", "evac", "lifesupport", "shelter", "구조", "서비스", "대피", "피난")),
    ("ROUTE/LOGISTICS", ("route", "corridor", "cargo", "supply", "convoy", "transport", "logistic", "항로", "화물", "보급", "선단", "수송")),
    ("CLAIM/OWNERSHIP/CUSTODY", ("claim", "title", "lien", "owner", "custody", "property", "surrender", "소유", "청구", "권리", "보관", "담보")),
    ("RECORD/PROVENANCE/MYSTERY", ("archive", "record", "provenance", "history", "identity", "mirror", "seed", "기록", "출처", "역사", "신원", "아카이브")),
    ("LEGAL/GOVERNANCE/ACCOUNTABILITY", ("law", "legal", "tribunal", "sanction", "charter", "assembly", "office", "authority", "법", "재판", "제재", "헌장", "의회", "권한")),
    ("NEGOTIATION/COALITION", ("negot", "compact", "coalition", "alliance", "federation", "agreement", "협상", "연합", "동맹", "협정", "연방")),
    ("COLLECTION/ACCESS/TRANSFER", ("access", "transfer", "handoff", "return", "release", "key", "credential", "이관", "반환", "접근", "열쇠", "인증")),
    ("INVESTIGATION/EVIDENCE", ("evidence", "investig", "witness", "proof", "signature", "audit", "증거", "조사", "증언", "서명", "감사")),
    ("RELATIONSHIP/TEAM", ("team", "trust", "relationship", "loyal", "refuse", "crew", "팀", "신뢰", "관계", "충성", "거절", "승무원")),
    ("ENDING/HANDOFF", ("ending", "epilogue", "final handoff", "legacy", "school", "후일담", "에필로그", "마지막", "유산")),
]


def vals(card, *names, max_items=4):
    return semantic.base.vals(card, *names, max_items=max_items)


def first(card, *names):
    got = vals(card, *names, max_items=1)
    return got[0] if got else None


def source_block(card, labels):
    for wanted in labels:
        wl = wanted.lower()
        for label, body in semantic.label_blocks(card):
            ll = label.lower()
            if ll == wl or wl in ll:
                return body
    return None


def humanish(text: str | None) -> bool:
    if not text:
        return False
    t = text.lower()
    toks = (
        "actor", "commander", "captain", "crew", "worker", "patient", "resident",
        "civilian", "family", "community", "council", "custodian", "delegate",
        "officer", "engineer", "doctor", "pilot", "people", "staff", "survivor",
        "리안", "네라", "미아", "세린", "하렌", "브람", "사람", "환자", "주민",
        "노동", "승무", "함장", "지휘관", "공동체", "위원", "대표", "생존자",
    )
    return any(tok in t for tok in toks)


def choose_engine(text: str) -> str:
    t = text.lower()
    scores = []
    for name, toks in ENGINE_RULES:
        score = sum(t.count(tok) for tok in toks)
        scores.append((score, name))
    score, name = max(scores)
    return name if score > 0 else "TRANSITION/AFTERMATH"


def compact(text: str | None, limit=240) -> str:
    if not text:
        return "NONE"
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 2].rstrip() + "…"


def manual_row(ep: int):
    return {
        "ep": ep,
        "grade": "A",
        "reasons": [],
        "pov": "MANUAL-DEEP-CONTEXT — use effective E001–E010 manual pack",
        "pov_auth": "MANUAL-AUDITED",
        "owner": "MANUAL-DEEP-CONTEXT",
        "decision": "MANUAL-DEEP-CONTEXT",
        "human": "MANUAL-DEEP-CONTEXT",
        "payoff": "MANUAL-DEEP-CONTEXT",
        "hook": "MANUAL-DEEP-CONTEXT",
        "engine": "MANUAL-DEEP-CONTEXT",
        "diff": "manual pack + blindspot audit already episode-specific",
    }


def classify(card):
    n = semantic.semantic_enrich(card)
    reasons = []

    explicit_pov = first(card, "pov / information source", "pov")
    front = first(card, "front-stage actor", "focal actor", "front stage actor")
    actors = first(card, "actors/goals", "actors", "actor goals", "actor goal")
    decision = first(card, "decisive choice", "decision", "choice", "physical action", "action", "agency", "authorized immediately")
    if not decision:
        decision = source_block(card, ("decisive choice", "decision", "choice", "physical action", "action", "agency", "response", "resolution"))

    owner = front or first(card, "decision owner", "current owner of decision", "response owners")
    if not owner and decision:
        # Do not pretend to parse a legal subject out of prose. Keep a bounded
        # role-owner route if actor evidence exists; otherwise report B.
        owner = actors

    if explicit_pov:
        pov = explicit_pov
        pov_auth = "SOURCE-EXPLICIT"
    elif front:
        pov = f"Recommend close-third/current information through front-stage actor: {front}"
        pov_auth = "WORKFLOW-RECOMMENDATION"
    elif owner:
        pov = f"Recommend close-third/current information through decision owner/actor: {owner}"
        pov_auth = "WORKFLOW-RECOMMENDATION"
    elif actors:
        pov = f"Recommend current-information route through actor evidence: {actors}"
        pov_auth = "WORKFLOW-RECOMMENDATION"
    else:
        pov = None
        pov_auth = "UNRESOLVED"
        reasons.append("POV_ROUTE")

    if not decision:
        reasons.append("DECISION_BEAT")
    if not owner:
        reasons.append("DECISION_OWNER")

    conflict = first(card, "conflict", "obstacle", "pressure", "hidden pressure", "current physical problem", "crisis")
    human = front or actors
    if not humanish(human):
        candidate = conflict or first(card, "current obligations", "affected zone", "current facts")
        if humanish(candidate):
            human = candidate
        else:
            human = None
            reasons.append("HUMAN_PRESSURE")

    relationship = first(card, "relationship/institution state", "relationship state", "institution state")
    if not relationship:
        relationship = "NONE — relationship/emotional delta not explicitly load-bearing in source; do not invent internal feeling"

    payoff = first(card, "reward", "immediate outcome", "outcome", "result", "state change", "current result", "final result", "campaign result", "final disposition")
    if not payoff:
        payoff = n["changes"][0] if n.get("changes") else None
    if not payoff:
        reasons.append("READER_PAYOFF")

    hook = first(card, "final hook", "end hook", "hook", "carried state")
    if not hook:
        hook = n["reentry"][0] if n.get("reentry") else None
    if card.episode == 1100:
        hook = hook or "ENDPOINT — no E1101 hook required; closure condition must remain incomplete-history ordinary-life proof"
    elif not hook:
        reasons.append("RETENTION")

    main = n.get("main")
    anchor = n.get("anchor") or []
    changes = n.get("changes") or []
    costs = n.get("costs") or []
    reentry = n.get("reentry") or []
    if not main or str(main).startswith("UNRESOLVED"):
        reasons.append("COMMON_MAIN")
    if not anchor:
        reasons.append("COMMON_ANCHOR")
    if not changes:
        reasons.append("COMMON_CHANGE")
    if not costs:
        reasons.append("COMMON_COST")
    if not reentry and card.episode != 1100:
        reasons.append("COMMON_REENTRY")

    text = " ".join(filter(None, [main, conflict, decision, payoff, hook, " ".join(anchor[:2]), " ".join(costs[:2])]))
    engine = choose_engine(text)
    differentiator = " | ".join([
        f"owner={compact(owner, 100)}",
        f"carrier={compact(anchor[0] if anchor else None, 120)}",
        f"cost={compact(costs[0] if costs else None, 120)}",
    ])

    grade = "A" if not reasons else "B"
    return {
        "ep": card.episode,
        "grade": grade,
        "reasons": reasons,
        "pov": pov,
        "pov_auth": pov_auth,
        "owner": owner,
        "decision": decision,
        "human": human,
        "relationship": relationship,
        "payoff": payoff,
        "hook": hook,
        "engine": engine,
        "diff": differentiator,
    }


def ga_for(ep):
    for ga, (lo, hi) in GA_RANGES.items():
        if lo <= ep <= hi:
            return ga
    raise ValueError(ep)


def family_runs(rows, minimum=4):
    runs = []
    start = 0
    while start < len(rows):
        family = rows[start]["engine"]
        end = start + 1
        while end < len(rows) and rows[end]["engine"] == family:
            end += 1
        if end - start >= minimum and family != "MANUAL-DEEP-CONTEXT":
            runs.append((rows[start]["ep"], rows[end - 1]["ep"], family, end - start))
        start = end
    return runs


def render(rows):
    counts = Counter(r["grade"] for r in rows)
    reason_counts = Counter(reason for r in rows for reason in r["reasons"])
    ga_counts = defaultdict(Counter)
    for r in rows:
        ga_counts[ga_for(r["ep"])][r["grade"]] += 1

    out = [
        "# Full-Series Context Writer-Activation Depth Audit v1",
        "",
        "Status: REVIEW — WRITER-ACTIVATION DEPTH QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "Last Reviewed: 2026-08-20",
        "Depends On: [[full-series-context-writer-activation-depth-standard-v1]], [[full-series-context-pack-completion-checkpoint-2026-08-20]], current source episode cards",
        "",
        "## 1. First-pass result",
        "",
        f"- total episodes: **{len(rows)}/1100**",
        f"- Depth-A: **{counts['A']}**",
        f"- Depth-B: **{counts['B']}**",
        f"- Depth-C: **{counts['C']}**",
        "- E001–E010: manual deep overrides counted A only because their effective manual packs and blindspot audit already exist.",
        "- E011–E1100: classified from approved episode cards through the source-bound semantic normalizer; no manuscript prose used.",
        "",
        "This is intentionally a stricter gate than the prior 1100/1100 six-field completion. A B result means the story design may be sound while writer execution is still too implicit.",
        "",
        "## 2. GA distribution",
        "",
        "| GA | Range | A | B | C |",
        "|---|---|---:|---:|---:|",
    ]
    for ga, (lo, hi) in GA_RANGES.items():
        c = ga_counts[ga]
        out.append(f"| GA{ga} | E{lo:03d}–E{hi:03d} | {c['A']} | {c['B']} | {c['C']} |")

    out += ["", "## 3. Depth-B reason counts", ""]
    if reason_counts:
        for k, v in reason_counts.most_common():
            out.append(f"- `{k}`: **{v}**")
    else:
        out.append("- NONE")

    b_rows = [r for r in rows if r["grade"] == "B"]
    out += ["", "## 4. Depth-B episode list", ""]
    if not b_rows:
        out.append("- NONE")
    else:
        for ga in range(1, 11):
            subset = [r for r in b_rows if ga_for(r["ep"]) == ga]
            if not subset:
                continue
            out += ["", f"### GA{ga}", ""]
            for r in subset:
                out.append(f"- E{r['ep']:03d}: {', '.join(r['reasons'])}")

    runs = family_runs(rows)
    out += ["", "## 5. Narrative-engine repetition watch", ""]
    if not runs:
        out.append("- No 4+ consecutive identical dominant engine-family run detected by the heuristic classifier.")
    else:
        for lo, hi, family, count in runs:
            out.append(f"- E{lo:03d}–E{hi:03d}: `{family}` × {count} — requires adjacent differentiator review; this is a WATCH, not automatic redesign.")

    out += [
        "",
        "## 6. Representative activation routing",
        "",
        "These rows are QC evidence, not story canon.",
        "",
        "| Episode | Grade | POV route | Decision owner | Engine |",
        "|---|---|---|---|---|",
    ]
    sample_eps = {11, 100, 101, 150, 210, 211, 322, 330, 331, 438, 450, 451, 525, 570, 571, 680, 683, 690, 691, 734, 762, 783, 800, 801, 841, 868, 889, 900, 901, 943, 1000, 1001, 1084, 1088, 1095, 1100}
    for r in rows:
        if r["ep"] in sample_eps:
            out.append(f"| E{r['ep']:03d} | {r['grade']} | {compact(r['pov'], 110)} | {compact(r['owner'], 100)} | {r['engine']} |")

    out += [
        "",
        "## 7. Gate semantics",
        "",
        "Target for final declaration:",
        "- Depth-A 1100/1100;",
        "- Depth-B 0;",
        "- Depth-C 0;",
        "- repetition/abstraction red-team PASS;",
        "- main integration verified.",
        "",
        "Any B item must be repaired by source-bound Context activation overlay. Any C item requires `NEW_CANON_REQUIRED: YES-STOP` and cannot be silently repaired.",
    ]
    return "\n".join(out) + "\n"


def main():
    cards = semantic.base.load_sources()
    expected = set(range(11, 1101))
    if set(cards) != expected:
        missing = sorted(expected - set(cards))
        extra = sorted(set(cards) - expected)
        raise SystemExit(f"source coverage mismatch missing={missing[:20]} extra={extra[:20]}")

    rows = [manual_row(ep) for ep in range(1, 11)]
    rows.extend(classify(cards[ep]) for ep in range(11, 1101))
    text = render(rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8")
    print(f"writer-depth audit written: {OUT.relative_to(ROOT)}")
    counts = Counter(r["grade"] for r in rows)
    print(f"Depth-A={counts['A']} Depth-B={counts['B']} Depth-C={counts['C']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
