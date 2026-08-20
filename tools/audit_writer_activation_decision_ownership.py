#!/usr/bin/env python3
"""Fail if writer activation conflates POV with decision ownership.

The project standard explicitly separates information route from authority.
A prior generator route promoted `decision + POV` to owner even when the exact
decision sentence was performed/refused by another actor. This audit bans that
route class and the old rendered owner phrase across E011-E1100.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACT_DIR = ROOT / "docs" / "13_writing_harness" / "context_packs" / "activation"
OUT = ROOT / "docs" / "99_quality_control" / "full-series-context-decision-owner-blindspot-audit-v1.md"

EP_RE = re.compile(r"^## E(\d{3,4})\b")
OWNER_RE = re.compile(r"^\*\*PRIMARY_DECISION_OWNER\*\*\s*$")
AUTH_RE = re.compile(r"^\*\*OWNER_ROUTE_AUTHORITY:\*\* `([^`]+)`")


def parse() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(ACT_DIR.glob("ga*-writer-activation-v1.md")):
        ep = None
        owner = ""
        auth = ""
        lines = path.read_text(encoding="utf-8").splitlines()
        i = 0
        while i < len(lines):
            m = EP_RE.match(lines[i])
            if m:
                if ep is not None:
                    rows.append({"ep": str(ep), "owner": owner, "auth": auth})
                ep = int(m.group(1))
                owner = ""
                auth = ""
                i += 1
                continue
            if ep is not None and OWNER_RE.match(lines[i]):
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines):
                    owner = lines[j].strip()
            am = AUTH_RE.match(lines[i])
            if ep is not None and am:
                auth = am.group(1)
            i += 1
        if ep is not None:
            rows.append({"ep": str(ep), "owner": owner, "auth": auth})
    return rows


def build() -> str:
    rows = parse()
    banned_auth = [r for r in rows if r["auth"] == "WORKFLOW-ROUTE FROM SOURCE POV + DECISION"]
    banned_phrase = [r for r in rows if r["owner"].startswith("POV/decision-carried current actor(s):")]
    missing = [r for r in rows if not r["owner"] or not r["auth"]]
    modes = Counter(r["auth"] for r in rows)
    fail = len(rows) != 1090 or banned_auth or banned_phrase or missing
    verdict = "FAIL" if fail else "PASS"
    lines = [
        "# Full-Series Context Decision-Owner Blindspot Audit v1",
        "",
        f"Status: {verdict} — EXECUTION QC",
        "Story Canon Effect: NONE",
        "Publication: NOT AUTHORIZED",
        "",
        f"- activation entries scanned: **{len(rows)} / 1090**",
        f"- banned `POV + decision => owner` authority routes: **{len(banned_auth)}**",
        f"- banned rendered `POV/decision-carried current actor(s)` owners: **{len(banned_phrase)}**",
        f"- missing owner/authority fields: **{len(missing)}**",
        "",
        "## Owner-route modes",
        "",
    ]
    for mode, count in modes.most_common():
        lines.append(f"- `{mode}`: **{count}**")
    lines.extend(["", "## Failure queue", ""])
    queue = sorted({int(r["ep"]) for r in banned_auth + banned_phrase + missing})
    if queue:
        lines.extend(f"- E{ep:03d}" for ep in queue)
    else:
        lines.append("- NONE")
    lines.extend([
        "",
        "## Ruling",
        "",
        "POV is an information route, not authority. A writer may use Rian close-third while another existing actor/institution owns the stop, refusal, sign-off or operational choice.",
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
            raise SystemExit("decision-owner blindspot audit stale/missing")
    else:
        OUT.write_text(text, encoding="utf-8")
    print(text)
    if "Status: PASS — EXECUTION QC" not in text:
        raise SystemExit("DECISION-OWNER BLINDSPOT GATE FAIL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
