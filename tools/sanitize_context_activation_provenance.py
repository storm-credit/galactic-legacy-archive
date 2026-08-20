#!/usr/bin/env python3
"""Convert internal activation provenance brackets into plain non-link markers.

Source-bound Context normalization historically uses labels such as
``[DERIVED ...]`` and, in a few places, ``[[DERIVED ...]]`` as visual
provenance markers. Writer-activation fields also use square brackets for
causal structure (for example ``DELTA[...]``), so a nested provenance label can
accidentally produce ``[[...]]`` and be parsed by the repository validator as a
wikilink.

This script changes provenance syntax only. It never changes story/source text,
event order, deaths, relationships, authorities, numbers, or ending state.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVATION = ROOT / "docs" / "13_writing_harness" / "context_packs" / "activation"

# Workflow-only provenance labels emitted by the Context builders. They are not
# document names and therefore must never use Obsidian/GitHub wikilink syntax.
PSEUDO_PREFIXES = (
    "DERIVED ",
    "SEMANTIC ",
    "COST EVIDENCE ",
    "SHARED APPROVED SOURCE-STATE CARRIER",
    "HIGH-WATCH BAND CARRIER FAMILY",
    "APPROVED SECTION CARRIER EVIDENCE",
)

_PREFIX_RE = "|".join(re.escape(prefix) for prefix in PSEUDO_PREFIXES)
DOUBLE_MARKER = re.compile(rf"\[\[((?:{_PREFIX_RE})[^\]\n]*)\]\]", re.IGNORECASE)
SINGLE_MARKER = re.compile(rf"\[((?:{_PREFIX_RE})[^\]\n]*)\]", re.IGNORECASE)


def convert(text: str) -> tuple[str, int]:
    """Replace only known workflow provenance markers with ⟦...⟧.

    Double-bracket forms are converted first so the single-bracket pass cannot
    leave an outer square bracket behind. The second pass catches the more
    important nested case: ``DELTA[[DERIVED ...] fact]`` originates from a
    single provenance marker inside the causal-field brackets.
    """

    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return f"⟦{match.group(1).strip()}⟧"

    text = DOUBLE_MARKER.sub(repl, text)
    text = SINGLE_MARKER.sub(repl, text)
    return text, count


def unresolved_pseudo_markers(text: str) -> list[str]:
    bad: list[str] = []
    for pattern in (DOUBLE_MARKER, SINGLE_MARKER):
        for match in pattern.finditer(text):
            bad.append(match.group(0))
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
        for marker in unresolved_pseudo_markers(updated):
            failures.append(f"{path.relative_to(ROOT)}: {marker}")

    if failures:
        raise SystemExit("PSEUDO-PROVENANCE SANITIZE FAIL:\n- " + "\n- ".join(failures))

    print(f"activation_provenance_sanitized={converted}")
    print(f"activation_files_changed={changed_files}")
    print("pseudo_provenance_square_markers_remaining=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
