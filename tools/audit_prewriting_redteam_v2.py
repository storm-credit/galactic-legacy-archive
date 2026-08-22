#!/usr/bin/env python3
"""Second-pass hostile pre-writing execution audit.

This audit does not create story canon. It looks for places where already-approved
story architecture can still be mistranslated by the execution harness:

1. bounded decision-owner routes where the source decision sentence itself names
   a recoverable performer/signatory/refuser;
2. CLSET next-desire / episode-exit / next-subact semantic bridge weakness;
3. strong Collection set-family mismatches against active-target domains;
4. high-value registry threads never selected as an active subact target;
5. relationship-primary subacts whose episode activation never surfaces a
   relationship/institution delta;
6. long-window narrative-engine concentration that can feel repetitive even
   when immediate consecutive-run checks pass.

All queues are review/QC. A finding is not permission to invent a new actor,
relationship, collectible, event, authority, or emotional beat.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

import build_full_series_context_packs_semantic as semantic

ROOT = Path(__file__).resolve().parents[1]
ACT_DIR = ROOT / "docs" / "13_writing_harness" / "context_packs" / "activation"
MAP_DIR = ROOT / "docs" / "09_collection" / "generated" / "desire_subact"
THREAD_INDEX = MAP_DIR / "full-series-collection-thread-index-v1.csv"
OUT = ROOT / "docs" / "99_quality_control" / "prewriting-execution-redteam-v2-audit.md"

EP_HEADER = re.compile(r"^## E(\d{3,4})\b")
MAP_HEADER = re.compile(r"^##\s+([^\s]+)\s+—\s+(.+?)\s+/\s+E(\d+)[–—-]E?(\d+)\s*$")
MAP_FIELD = re.compile(r"^- `([^`]+)`: ?(.*)$")
TARGET_LINE = re.compile(r"^\s+- `(?P<thread>CLT-[^`]+)`\s+/\s+`[^`]+`\s+/\s+(?P<title>.+?)\s+—\s+")

INLINE_FIELDS = {
    "OWNER_ROUTE_AUTHORITY": re.compile(r"^\*\*OWNER_ROUTE_AUTHORITY:\*\*\s+`(.+?)`\s*$"),
    "DECISION_MODE": re.compile(r"^\*\*DECISION_MODE:\*\*\s+`(.+?)`\s*$"),
    "RELATIONSHIP_DELTA_AUTHORITY": re.compile(r"^\*\*RELATIONSHIP_DELTA_AUTHORITY:\*\*\s+`(.+?)`\s*$"),
    "NARRATIVE_ENGINE_FAMILY": re.compile(r"^\*\*NARRATIVE_ENGINE_FAMILY:\*\*\s+`(.+?)`\s*$"),
}
BLOCK_FIELDS = {
    "PRIMARY_DECISION_OWNER": "**PRIMARY_DECISION_OWNER**",
    "DECISION_BEAT": "**DECISION_BEAT**",
    "RELATIONSHIP_EMOTIONAL_DELTA": "**RELATIONSHIP_EMOTIONAL_DELTA**",
    "READER_PAYOFF_THIS_EP": "**READER_PAYOFF_THIS_EP**",
    "RETENTION_QUESTION_OR_CHANGED_CONDITION": "**RETENTION_QUESTION_OR_CHANGED_CONDITION**",
}

VERBS = (
    "keeps", "keep", "maps", "map", "orders", "order", "chooses", "choose",
    "votes", "vote", "refuses", "refuse", "rejects", "reject", "signs", "sign",
    "accepts", "accept", "authorizes", "authorize", "approves", "approve",
    "commits", "commit", "holds", "hold", "uses", "use", "opens", "open",
    "releases", "release", "separates", "separate", "isolates", "isolate",
    "decides", "decide", "selects", "select", "retains", "retain", "stays", "stay",
    "transmits", "transmit", "grants", "grant", "withholds", "withhold",
    "deploys", "deploy", "restores", "restore", "adopts", "adopt", "requests", "request",
    "leaves", "leave", "hands", "hand", "records", "record", "publishes", "publish",
    "agrees", "agree", "moves", "move", "routes", "route", "cancels", "cancel",
    "stops", "stop", "permits", "permit", "allows", "allow", "maintains", "maintain",
    "suspends", "suspend", "limits", "limit", "continues", "continue", "withdraws", "withdraw",
    "enters", "enter", "issues", "issue", "removes", "remove", "distributes", "distribute",
)
PERFORMER_RE = re.compile(r"^(.{1,120}?)\s+(" + "|".join(sorted(VERBS, key=len, reverse=True)) + r")\b", re.I)
GENERIC_BAD = {
    "it", "this", "that", "there", "one", "someone", "something", "the episode",
    "the approved episode", "the source", "a result", "an outcome", "the result",
}
ROLE_WORDS = {
    "crew", "workers", "worker", "board", "council", "captain", "engineer", "engineers",
    "medical", "team", "teams", "operators", "maintainers", "voters", "residents", "claimants",
    "custodians", "witnesses", "patients", "community", "assembly", "staff", "tribunal",
    "office", "representatives", "representative", "caregivers", "caregiver", "families", "family",
    "instructor", "trainee", "pilots", "pilot", "commanders", "commander", "locals", "local",
}

STOP = {
    "the", "and", "with", "that", "from", "into", "while", "current", "next", "this", "their",
    "without", "through", "becomes", "become", "under", "remains", "reader", "desire", "episode",
    "source", "existing", "people", "system", "must", "should", "will", "would", "could", "may",
    "then", "only", "after", "before", "where", "which", "what", "when", "whose", "also",
}

PHYSICAL_DOMAINS = {"C2", "C3", "C5", "C6"}
PHYSICAL_CUES = (
    "frame", "ship", "module", "weapon", "repair", "install", "technical", "medical", "workshop",
    "service capability", "configuration", "parts", "part", "hull", "drive", "propulsion", "engine",
    "기체", "함선", "모듈", "무기", "수리", "부품", "기술", "의료",
)
LINEAGE_CUES = ("lineage", "origin", "prototype", "authorship", "ancestry", "계보", "기원", "원형")
REL_CUES = ("trust", "consent", "relationship", "crew", "community", "refusal", "care", "신뢰", "동의", "관계", "공동체", "거절")
CIV_CUES = ("autonomy", "federation", "region", "node", "migration", "reconstruction", "jurisdiction", "자치", "연방", "지역", "노드", "이주", "재건")
HIGH_VALUE_TITLE = (
    "07", "parus", "파루스", "core", "frame", "ship", "hull", "module", "weapon", "relic", "seed",
    "archive", "node", "academy", "fleet", "admiral", "hero", "prototype", "lineage", "engine", "route",
    "코어", "기체", "함선", "모듈", "무기", "유물", "노드", "함대", "제독", "영웅", "계보",
)


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def clip(text: str, n: int = 220) -> str:
    text = clean(text).replace("|", "/")
    return text if len(text) <= n else text[: n - 1] + "…"


def tokens(text: str) -> set[str]:
    out = set()
    for token in re.findall(r"[A-Za-z가-힣][A-Za-z가-힣0-9'-]{2,}", (text or "").casefold()):
        if token not in STOP:
            out.add(token)
    return out


def parse_activation() -> dict[int, dict[str, str]]:
    episodes: dict[int, dict[str, str]] = {}
    for path in sorted(ACT_DIR.glob("ga*-writer-activation-v1.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        ep = None
        i = 0
        while i < len(lines):
            m = EP_HEADER.match(lines[i])
            if m:
                ep = int(m.group(1))
                episodes[ep] = {"source_file": path.name}
                i += 1
                continue
            if ep is None:
                i += 1
                continue
            stripped = lines[i].strip()
            for key, pattern in INLINE_FIELDS.items():
                mm = pattern.match(stripped)
                if mm:
                    episodes[ep][key] = mm.group(1).strip()
            for key, marker in BLOCK_FIELDS.items():
                if stripped == marker:
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines):
                        episodes[ep][key] = lines[j].strip()
            i += 1
    return episodes


def parse_maps() -> list[dict]:
    rows: list[dict] = []
    for path in sorted(MAP_DIR.glob("ga*-collection-desire-subact-map-v1.md")):
        arc = path.name.split("-", 1)[0].upper()
        current = None
        in_targets = False
        for line in path.read_text(encoding="utf-8").splitlines():
            h = MAP_HEADER.match(line)
            if h:
                if current:
                    rows.append(current)
                current = {
                    "arc": arc,
                    "code": h.group(1),
                    "title": h.group(2),
                    "start": int(h.group(3)),
                    "end": int(h.group(4)),
                    "fields": {},
                    "targets": [],
                }
                in_targets = False
                continue
            if current is None:
                continue
            f = MAP_FIELD.match(line)
            if f:
                current["fields"][f.group(1)] = f.group(2).strip()
                in_targets = f.group(1) == "ACTIVE_TARGETS"
                continue
            if line.startswith("- `ACTIVE_TARGETS`:"):
                in_targets = True
                continue
            if in_targets:
                t = TARGET_LINE.match(line)
                if t:
                    current["targets"].append((t.group("thread"), t.group("title").strip()))
                elif line and not line.startswith("  -") and not line.startswith(" "):
                    in_targets = False
        if current:
            rows.append(current)
    return rows


def load_threads() -> tuple[list[dict], dict[str, dict]]:
    rows = []
    by_thread = {}
    with THREAD_INDEX.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            rows.append(row)
            by_thread[row["collection_thread_id"]] = row
    return rows, by_thread


def extract_performer(decision: str) -> tuple[str | None, str]:
    text = clean(decision)
    if not text or text.startswith("NON-DISCRETE"):
        return None, ""
    # Ignore execution prefixes if one leaked into the displayed decision.
    text = re.sub(r"^\[[^\]]+\]\s*", "", text)
    first = re.split(r"(?<=[.!?])\s+|\s*;\s*", text, maxsplit=1)[0].strip()
    m = PERFORMER_RE.match(first)
    if not m:
        return None, ""
    actor = m.group(1).strip(" -,:`[]()")
    low = actor.casefold()
    if low in GENERIC_BAD or len(actor.split()) > 12:
        return None, ""
    if any(x in low for x in ("because ", "while ", " if ", " when ", " after ", " before ", " so that ")):
        return None, ""
    # Named/code performer = strongest. A concrete source role is still useful,
    # but is reported separately so it is not silently promoted to a named fact.
    named = bool(re.search(r"\b[A-Z]{1,5}-\d{1,4}\b", actor)) or bool(
        re.match(r"^[A-Z][A-Za-z'’-]+(?:\s+[A-Z][A-Za-z'’-]+){0,3}(?:\s+and\s+[A-Z][A-Za-z'’-]+(?:\s+[A-Z][A-Za-z'’-]+){0,3})?$", actor)
    )
    role = any(word in ROLE_WORDS for word in re.findall(r"[a-z]+", low))
    if not named and not role:
        return None, ""
    return actor, "NAMED/CODE" if named else "SOURCE-ROLE"


def owner_precision(cards, acts):
    named = []
    roles = []
    bounded = 0
    for ep, a in sorted(acts.items()):
        if a.get("OWNER_ROUTE_AUTHORITY") != "WORKFLOW-BOUNDED ROLE + SOURCE DECISION":
            continue
        bounded += 1
        performer, kind = extract_performer(a.get("DECISION_BEAT", ""))
        if not performer:
            continue
        row = (ep, performer, a.get("DECISION_BEAT", ""), cards[ep].source.name)
        (named if kind == "NAMED/CODE" else roles).append(row)
    return bounded, named, roles


def crosslayer_semantic(rows, acts):
    direct = []
    next_bridge = []
    watches = []
    ordered = sorted(rows, key=lambda r: (r["start"], r["end"]))
    for idx, row in enumerate(ordered):
        generated = [ep for ep in range(row["start"], row["end"] + 1) if ep >= 11 and ep in acts]
        if not generated:
            continue
        exit_ep = generated[-1]
        hook = acts[exit_ep].get("RETENTION_QUESTION_OR_CHANGED_CONDITION", "")
        next_desire = row["fields"].get("NEXT_DESIRE", "")
        overlap = tokens(hook) & tokens(next_desire)
        if overlap:
            direct.append((row, exit_ep, sorted(overlap)))
            continue
        nxt = ordered[idx + 1] if idx + 1 < len(ordered) else None
        if nxt:
            bundle = " ".join([
                nxt["title"],
                nxt["fields"].get("READER_DESIRE_MAIN", ""),
                nxt["fields"].get("DISCOVERY", ""),
                nxt["fields"].get("ACQUISITION_OR_CONNECTION", ""),
                " ".join(title for _, title in nxt["targets"]),
            ])
            bridge_overlap = tokens(hook) & tokens(bundle)
            next_desire_overlap = tokens(next_desire) & tokens(bundle)
            if bridge_overlap or next_desire_overlap:
                next_bridge.append((row, exit_ep, nxt, sorted(bridge_overlap | next_desire_overlap)))
                continue
        watches.append((row, exit_ep, hook, next_desire, nxt))
    return direct, next_bridge, watches


def set_family_mismatches(rows, threads):
    out = []
    for row in rows:
        primary = row["fields"].get("PRIMARY_SET_TYPE", "")
        target_rows = [threads[t] for t, _ in row["targets"] if t in threads]
        if not target_rows:
            continue
        domains = [tr["primary_domain"] for tr in target_rows if tr.get("primary_domain")]
        counts = Counter(domains)
        dom, cnt = counts.most_common(1)[0]
        share = cnt / len(domains) if domains else 0
        text = " ".join([
            row["title"],
            row["fields"].get("READER_DESIRE_MAIN", ""),
            row["fields"].get("DISCOVERY", ""),
            row["fields"].get("ACQUISITION_OR_CONNECTION", ""),
            row["fields"].get("SYNERGY_OR_USE", ""),
        ]).casefold()
        physical = dom in PHYSICAL_DOMAINS and share >= 0.67
        rel = dom == "C1" and share >= 0.67
        civ = dom == "C8" and share >= 0.67
        reason = None
        if physical and primary != "FUNCTIONAL" and any(cue in text for cue in PHYSICAL_CUES) and not any(cue in text for cue in LINEAGE_CUES):
            reason = f"physical targets {dom}={cnt}/{len(domains)} but primary={primary}"
        elif rel and primary != "RELATIONSHIP" and any(cue in text for cue in REL_CUES):
            reason = f"relationship targets C1={cnt}/{len(domains)} but primary={primary}"
        elif civ and primary != "CIVILIZATION" and any(cue in text for cue in CIV_CUES):
            reason = f"civilization targets C8={cnt}/{len(domains)} but primary={primary}"
        elif primary == "RELATIONSHIP" and domains and all(d in PHYSICAL_DOMAINS for d in domains) and any(cue in text for cue in PHYSICAL_CUES) and not any(cue in text for cue in REL_CUES):
            reason = "all active targets physical but primary=RELATIONSHIP"
        if reason:
            out.append((row, reason, domains))
    return out


def orphan_watch(thread_rows):
    orphans = []
    high = []
    for row in thread_rows:
        try:
            selected = int(row.get("selected_as_active_target_count") or 0)
        except ValueError:
            selected = 0
        if selected:
            continue
        orphans.append(row)
        kinds = set(filter(None, (row.get("entry_kinds") or "").split("|")))
        phases = set(filter(None, (row.get("desire_phases") or "").split("|")))
        explicit_subacts = bool((row.get("explicit_subacts") or "").strip())
        refs = [x for x in (row.get("explicit_episode_refs") or "").split("|") if x.strip()]
        title_low = (row.get("title") or "").casefold()
        high_kind = bool(kinds & {"NARRATIVE_PROMISE", "LOSS_OBLIGATION", "STATE_TRANSITION"})
        physical_chain = row.get("primary_domain") in PHYSICAL_DOMAINS and {"ACQUISITION", "SYNERGY"} <= phases and len(refs) >= 3
        title_flag = any(key in title_low for key in HIGH_VALUE_TITLE)
        if explicit_subacts and (high_kind or physical_chain or title_flag):
            high.append(row)
    return orphans, high


def relationship_cadence(rows, acts):
    watches = []
    for row in rows:
        if row["fields"].get("PRIMARY_SET_TYPE") != "RELATIONSHIP":
            continue
        eps = [ep for ep in range(row["start"], row["end"] + 1) if ep in acts]
        if len(eps) < 4:
            continue
        none_eps = []
        explicit_eps = []
        for ep in eps:
            value = acts[ep].get("RELATIONSHIP_EMOTIONAL_DELTA", "")
            if value.startswith("NONE"):
                none_eps.append(ep)
            else:
                explicit_eps.append(ep)
        share = len(none_eps) / len(eps)
        if share >= 0.80:
            watches.append((row, eps, none_eps, explicit_eps, share))
    return watches


def engine_windows(acts, window=20, threshold=0.65):
    episodes = sorted(acts)
    raw = []
    for i in range(0, len(episodes) - window + 1):
        span = episodes[i:i + window]
        if span[-1] - span[0] != window - 1:
            continue
        engines = Counter(acts[ep].get("NARRATIVE_ENGINE_FAMILY", "") for ep in span)
        fam, count = engines.most_common(1)[0]
        share = count / window
        if share >= threshold:
            raw.append((span[0], span[-1], fam, count, share))
    # Collapse heavily overlapping windows with the same dominant family.
    merged = []
    for item in raw:
        if merged and item[2] == merged[-1][2] and item[0] <= merged[-1][1] + 1:
            lo, hi, fam, count, share = merged[-1]
            merged[-1] = (lo, item[1], fam, max(count, item[3]), max(share, item[4]))
        else:
            merged.append(item)
    return merged


def build_report() -> str:
    cards = semantic.base.load_sources()
    acts = parse_activation()
    maps = parse_maps()
    thread_rows, threads = load_threads()

    bounded, owner_named, owner_roles = owner_precision(cards, acts)
    direct, bridged, semantic_watch = crosslayer_semantic(maps, acts)
    set_mismatch = set_family_mismatches(maps, threads)
    orphans, orphan_high = orphan_watch(thread_rows)
    rel_watch = relationship_cadence(maps, acts)
    engine_watch = engine_windows(acts)

    hard = []
    if len(cards) != 1090:
        hard.append(f"source-card coverage {len(cards)}/1090")
    if len(acts) != 1090:
        hard.append(f"activation coverage {len(acts)}/1090")
    if len(maps) != 160:
        hard.append(f"collection subact coverage {len(maps)}/160")
    if len(thread_rows) != 415:
        hard.append(f"collection thread coverage {len(thread_rows)}/415")

    # Strong execution defects: a source-named performer is recoverable while
    # the output still uses a generic bounded route, or a strong set/domain
    # mismatch exists. Other queues remain WATCH until source review.
    strong = len(owner_named) + len(set_mismatch)
    status = "FAIL" if hard or strong else "PASS-WITH-WATCH"

    lines = [
        "# Pre-Writing Execution Red-Team v2 Audit",
        "",
        f"Status: {status} — HOSTILE EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        "## Coverage",
        "",
        f"- source cards: **{len(cards)}/1090**",
        f"- writer activation episodes: **{len(acts)}/1090**",
        f"- Collection Desire subacts: **{len(maps)}/160**",
        f"- Collection source threads: **{len(thread_rows)}/415**",
        f"- hard coverage failures: **{len(hard)}**",
        "",
        "## 1. Decision-owner precision",
        "",
        f"- bounded role + source decision routes: **{bounded}**",
        f"- source-named/code performer recoverable from decision sentence: **{len(owner_named)}**",
        f"- concrete source-role performer recoverable: **{len(owner_roles)}**",
        "",
        "### Named/code performer queue — strong fix candidates",
        "",
    ]
    if owner_named:
        for ep, performer, decision, source in owner_named:
            lines.append(f"- E{ep:03d} `{performer}` / `{source}` — {clip(decision)}")
    else:
        lines.append("- NONE")
    lines += ["", "### Source-role performer queue — manual precision WATCH", ""]
    if owner_roles:
        for ep, performer, decision, source in owner_roles[:200]:
            lines.append(f"- E{ep:03d} `{performer}` / `{source}` — {clip(decision)}")
        if len(owner_roles) > 200:
            lines.append(f"- … {len(owner_roles)-200} additional role-level candidates omitted from display")
    else:
        lines.append("- NONE")

    lines += [
        "",
        "## 2. CLSET ↔ episode exit ↔ next-subact semantic bridge",
        "",
        f"- direct lexical bridges: **{len(direct)}**",
        f"- recovered via next-subact bundle: **{len(bridged)}**",
        f"- residual semantic WATCH: **{len(semantic_watch)}**",
        "",
        "### Residual WATCH queue",
        "",
    ]
    if semantic_watch:
        for row, exit_ep, hook, next_desire, nxt in semantic_watch:
            next_label = f"{nxt['arc']} {nxt['code']} {nxt['title']}" if nxt else "ENDPOINT"
            lines.append(
                f"- {row['arc']} {row['code']} E{exit_ep} → {next_label}: "
                f"NEXT=`{clip(next_desire, 150)}` / HOOK=`{clip(hook, 150)}`"
            )
    else:
        lines.append("- NONE")

    lines += [
        "",
        "## 3. Collection set-family strong mismatch",
        "",
        f"- strong set/domain mismatch candidates: **{len(set_mismatch)}**",
        "",
    ]
    if set_mismatch:
        for row, reason, domains in set_mismatch:
            target_names = ", ".join(title for _, title in row["targets"])
            lines.append(f"- {row['arc']} {row['code']} `{row['fields'].get('PRIMARY_SET_TYPE','')}` — {reason}; targets={clip(target_names, 180)}; domains={domains}")
    else:
        lines.append("- NONE")

    lines += [
        "",
        "## 4. Collection orphan audit",
        "",
        f"- never selected as active target: **{len(orphans)} / {len(thread_rows)}**",
        f"- high-value orphan WATCH: **{len(orphan_high)}**",
        "",
        "### High-value orphan WATCH",
        "",
    ]
    if orphan_high:
        for row in orphan_high:
            lines.append(
                f"- `{row['collection_thread_id']}` / {row['arc']} / {row['source_id']} / {row['title']} — "
                f"domain={row['primary_domain']} kinds={row['entry_kinds']} phases={row['desire_phases']} "
                f"episodes={row['explicit_episode_refs']} subacts={row['explicit_subacts']}"
            )
    else:
        lines.append("- NONE")

    lines += [
        "",
        "## 5. Relationship/emotional cadence",
        "",
        f"- RELATIONSHIP-primary subacts with >=80% episode delta NONE: **{len(rel_watch)}**",
        "",
    ]
    if rel_watch:
        for row, eps, none_eps, explicit_eps, share in rel_watch:
            lines.append(
                f"- {row['arc']} {row['code']} E{row['start']}–E{row['end']} — NONE {len(none_eps)}/{len(eps)} ({share:.0%}); explicit={explicit_eps or 'NONE'}; desire={clip(row['fields'].get('READER_DESIRE_MAIN',''), 170)}"
            )
    else:
        lines.append("- NONE")

    lines += [
        "",
        "## 6. Long-window narrative-engine concentration",
        "",
        f"- 20-episode windows with >=65% one engine, collapsed by overlap: **{len(engine_watch)}**",
        "",
    ]
    if engine_watch:
        for lo, hi, fam, count, share in engine_watch:
            lines.append(f"- E{lo:03d}–E{hi:03d}: `{fam}` peak={count}/20 ({share:.0%})")
    else:
        lines.append("- NONE")

    lines += [
        "",
        "## 7. Ruling",
        "",
        f"- strong execution defects requiring patch before final v2 PASS: **{strong}**",
        f"- hard coverage failures: **{len(hard)}**",
        "- orphan / relationship-cadence / long-engine / residual semantic queues are WATCH until source-level review; they do not authorize new canon.",
        "- manuscript prose is not a source for this audit.",
        "- new story canon required by the audit itself: **0**.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    text = build_report()
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            raise SystemExit("prewriting red-team v2 audit stale/missing")
    else:
        OUT.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
