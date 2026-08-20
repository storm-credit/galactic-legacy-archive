#!/usr/bin/env python3
"""Convert internal activation provenance pseudo-wikilinks into plain markers.

Some source-bound Context normalization labels historically use ``[[...]]`` as
visual brackets even though they are not document links. Writer-activation
output is validated as normal documentation, so those labels must not masquerade
as resolvable wikilinks.

This script changes syntax only, never story/source text semantics. It is also a
watched workflow input so edits here force regeneration + persisted sanitation.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVATION = ROOT / "docs" / "13_writing_harness" / "context_packs" / "activation"

PSEUDO_PREFIXES = (
    "DERIVED ",
    "SEMANTIC ",
    "COST EVIDENCE ",
    "SHARED APPROVED SOURCE-STATE CARRIER",
    "HIGH-WATCH BAND CARRIER FAMILY",
)

WIKILINK = re.compile(r"\[\[([^\]\n]+)\]\]")


def convert(text: str) -> tuple[str, int]:
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        body = match.group(1).strip()
        if body.upper().startswith(tuple(p.upper() for p in PSEUDO_PREFIXES)):
            count += 1
            return f"⟦{body}⟧"
        return match.group(0)

    return WIKILINK.sub(repl, text), count


def unresolved_pseudo_links(text: str) -> list[str]:
    bad = []
    for m in WIKILINK.finditer(text):
        body = m.group(1).strip()
        if body.upper().startswith(tuple(p.upper() for p in PSEUDO_PREFIXES)):
            bad.append(body)
    return bad


def main() -> int:
    changed_files = 0
    converted = 0
    failures: list[str] = []

    for path in sorted(ACTIVATION.glob("*.md")):
        original = path.read_text(encoding="utf-8")
        updated, count = convert(original)
        if count:
            path.write_text(updated, encoding="utf-8")
            changed_files += 1
            converted += count
        for body in unresolved_pseudo_links(updated):
            failures.append(f"{path.relative_to(ROOT)}: [[{body}]]")

    if failures:
        raise SystemExit("PSEUDO-WIKILINK SANITIZE FAIL:\n- " + "\n- ".join(failures))

    print(f"activation_provenance_sanitized={converted}")
    print(f"activation_files_changed={changed_files}")
    print("pseudo_wikilinks_remaining=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
