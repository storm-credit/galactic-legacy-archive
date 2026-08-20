#!/usr/bin/env python3
"""Cross-check subact Collection Desire against episode writer activation.

Collection Desire is authored at 160-subact scale while writer activation is at
1100-episode scale. This bridge prevents both layers from passing separately
without the writer being able to see which CLSET desire each episode is serving.
It creates no story fact and changes no event/payoff timing.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_DIR = ROOT / "docs" / "09_collection" / "generated" / "desire_subact"
ACT_DIR = ROOT / "docs" / "13_writing_harness" / "context_packs" / "activation"
OUT = ROOT / "docs" / "99_quality_control" / "full-series-collection-context-crosslayer-audit-v1.md"

MAP_HEADER = re.compile(r"^##\s+([^\s]+)\s+—\s+(.+?)\s+/\s+E(\d+)[–—-]E?(\d+)\s*$")
FIELD = re.compile(r"^- `([^`]+)`: ?(.*)$")
EP_HEADER = re.compile(r"^## E(\d{3,4})\b")


def parse_subacts():
    rows = []
    for path in sorted(MAP_DIR.glob("ga*-collection-desire-subact-map-v1.md")):
        arc = path.name.split("-", 1)[0].upper()
        current = None
        for line in path.read_text(encoding="utf-8").splitlines():
            m = MAP_HEADER.match(line)
            if m:
                if current:
                    rows.append(current)
                current = {
                    "arc": arc,
                    "code": m.group(1),
                    "title": m.group(2),
                    "start": int(m.group(3)),
                    "end": int(m.group(4)),
                    "fields": {},
                }
                continue
            if current is None:
                continue
            f = FIELD.match(line)
            if f:
                current["fields"][f.group(1)] = f.group(2).strip()
        if current:
            rows.append(current)
    return rows


def parse_activation():
    episodes = {}
    for path in sorted(ACT_DIR.glob("ga*-writer-activation-v1.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        ep = None
        i = 0
        while i < len(lines):
            m = EP_HEADER.match(lines[i])
            if m:
                ep = int(m.group(1))
                episodes.setdefault(ep, {"payoff": "", "hook": ""})
                i += 1
                continue
            if ep is not None and lines[i].strip() in {"**READER_PAYOFF_THIS_EP**", "**RETENTION_QUESTION_OR_CHANGED_CONDITION**"}:
                key = "payoff" if "PAYOFF" in lines[i] else "hook"
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines):
                    episodes[ep][key] = lines[j].strip()
            i += 1
    return episodes


def tokens(text: str) -> set[str]:
    stop = {
        "the", "and", "with", "that", "from", "into", "while", "current", "next",
        "this", "their", "without", "through", "becomes", "become", "under", "remains",
        "reader", "desire", "episode", "source", "existing", "people", "system",
    }
    out = set()
    for token in re.findall(r"[A-Za-z가-힣][A-Za-z가-힣0-9'-]{2,}", text.casefold()):
        if token not in stop:
            out.add(token)
    return out


def short(text: str, n: int = 150) -> str:
    clean = re.sub(r"\s+", " ", text).strip().replace("|", "/")
    return clean if len(clean) <= n else clean[: n - 1] + "…"


def build() -> str:
    subacts = parse_subacts()
    acts = parse_activation()
    coverage = {ep: [] for ep in range(11, 1101)}
    hard = []
    semantic_watch = []
    detail = []

    for row in subacts:
        fields = row["fields"]
        set_id = fields.get("SET_EXECUTION_ID", "")
        desire = fields.get("READER_DESIRE_MAIN", "")
        next_desire = fields.get("NEXT_DESIRE", "")
        eps = list(range(row["start"], row["end"] + 1))
        generated_eps = [ep for ep in eps if ep >= 11]
        for ep in generated_eps:
            if ep in coverage:
                coverage[ep].append(f"{row['arc']} {row['code']}")
        missing_act = [ep for ep in generated_eps if ep not in acts]
        missing_payoff = [ep for ep in generated_eps if ep in acts and not acts[ep]["payoff"]]
        missing_hook = [ep for ep in generated_eps if ep in acts and not acts[ep]["hook"]]
        if not set_id or not desire or not next_desire or missing_act or missing_payoff or missing_hook:
            hard.append(
                f"{row['arc']} {row['code']} missing set/desire/activation data: "
                f"set={bool(set_id)} desire={bool(desire)} next={bool(next_desire)} "
                f"activation={missing_act} payoff={missing_payoff} hook={missing_hook}"
            )

        if generated_eps:
            first_ep = generated_eps[0]
            exit_ep = generated_eps[-1]
            entry_payoff = acts.get(first_ep, {}).get("payoff", "")
            exit_hook = acts.get(exit_ep, {}).get("hook", "")
            left = tokens(next_desire)
            right = tokens(exit_hook)
            overlap = sorted(left & right)
            if left and right and not overlap:
                semantic_watch.append(f"{row['arc']} {row['code']} E{exit_ep}: NEXT_DESIRE ↔ exit hook lexical overlap 0")
            activation_span = f"E{first_ep}–E{exit_ep} ({len(generated_eps)})"
        else:
            entry_payoff = "E001–E010 manual deep Context governs; generated activation overlay intentionally starts E011."
            exit_hook = "manual E001–E010 Context/hook audit applies."
            activation_span = "MANUAL E001–E010"

        detail.append(
            f"| {row['arc']} {row['code']} | E{row['start']}–E{row['end']} | {short(set_id, 34)} | "
            f"{activation_span} | {short(desire)} | {short(entry_payoff)} | {short(exit_hook)} |"
        )

    uncovered = [ep for ep, owners in coverage.items() if len(owners) == 0]
    overlap_eps = [ep for ep, owners in coverage.items() if len(owners) > 1]
    if uncovered:
        hard.append(f"episodes without exactly one CLSET subact link: {uncovered[:40]}" + ("…" if len(uncovered) > 40 else ""))
    if overlap_eps:
        hard.append(f"episodes with overlapping CLSET subact links: {overlap_eps[:40]}" + ("…" if len(overlap_eps) > 40 else ""))

    fail = len(subacts) != 160 or len(acts) != 1090 or bool(hard)
    verdict = "FAIL" if fail else "PASS"
    lines = [
        "# Full-Series Collection Desire ↔ Context Writer-Activation Cross-Layer Audit v1",
        "",
        f"Status: {verdict} — PRE-WRITING EXECUTION INTEGRATION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        f"- Collection subacts: **{len(subacts)} / 160**",
        f"- generated writer-activation episodes: **{len(acts)} / 1090**",
        f"- E011–E1100 episodes without exactly one CLSET range: **{len(uncovered)}**",
        f"- E011–E1100 episodes in overlapping CLSET ranges: **{len(overlap_eps)}**",
        f"- hard bridge failures: **{len(hard)}**",
        f"- semantic exit-hook lexical WATCH: **{len(semantic_watch)}** (review aid; not automatic canon failure)",
        "",
        "## Hard failure queue",
        "",
    ]
    lines.extend(f"- {item}" for item in hard) if hard else lines.append("- NONE")
    lines.extend(["", "## Semantic WATCH queue", ""])
    lines.extend(f"- {item}" for item in semantic_watch) if semantic_watch else lines.append("- NONE")
    lines.extend([
        "",
        "## Writer bridge table",
        "",
        "| Subact | Range | CLSET | Activation span | Reader desire | Entry payoff | Exit hook |",
        "|---|---|---|---|---|---|---|",
    ])
    lines.extend(detail)
    lines.extend([
        "",
        "## Ruling",
        "",
        "A manuscript episode must consume both its episode-level writer activation and the single CLSET subact packet covering that episode. The CLSET supplies the longer reader desire/set progression; the activation supplies the current episode payoff, decision ownership and next condition. Neither layer replaces canon sources.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text = build()
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            raise SystemExit("collection-context cross-layer audit stale/missing")
    else:
        OUT.write_text(text, encoding="utf-8")
    print(text.split("## Writer bridge table", 1)[0])
    if "Status: PASS — PRE-WRITING EXECUTION INTEGRATION QC" not in text:
        raise SystemExit("COLLECTION-CONTEXT CROSS-LAYER GATE FAIL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
