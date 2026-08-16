from pathlib import Path

p = Path('tools/validate_canon.py')
text = p.read_text(encoding='utf-8')


def rep(old: str, new: str) -> None:
    global text
    n = text.count(old)
    if n != 1:
        raise SystemExit(f'expected block once, got {n}: {old[:120]!r}')
    text = text.replace(old, new, 1)

rep(
'''# v1 drafts predate the rename and are preserved as historical text per
# canonical-name-errata-005 propagation rule 4.
HISTORY_EXEMPT_PATTERNS = (re.compile(r"^manuscript/.*-v1\\.md$"),)
''',
'''# Historical manuscript exemption is determined from the actual header schema,
# not the filename suffix. Current production can legitimately create a first
# revision named ``-v1.md`` while using the current Status/Episode/Canon Check/
# Publication contract; those files must still receive retired-name checks.
''')

rep(
'''def is_history_exempt(rel: str) -> bool:
    if rel.startswith(HISTORY_EXEMPT):
        return True
    return any(pattern.match(rel) for pattern in HISTORY_EXEMPT_PATTERNS)
''',
'''def is_history_exempt(rel: str) -> bool:
    return rel.startswith(HISTORY_EXEMPT)
''')

rep(
'''    for rel, text in files:
        if is_history_exempt(rel):
            continue
        checked += 1
''',
'''    for rel, text in files:
        if is_history_exempt(rel):
            continue
        # Legacy manuscript text is retained as historical material, but a
        # current-schema manuscript must never become exempt merely because its
        # filename happens to end in ``-v1.md``.
        if rel.startswith("manuscript/") and manuscript_schema(parse_header(text)) == "legacy":
            continue
        checked += 1
''')

rep(
'''def is_legacy_draft(rel: str) -> bool:
    return rel.endswith("-v1.md")


def check_manuscripts(files: list[tuple[str, str]], report: Report) -> int:
''',
'''CURRENT_MANUSCRIPT_MARKERS = ("Episode", "Canon Check", "Publication")
LEGACY_MANUSCRIPT_MARKERS = ("Publication Status", "POV", "Canon Basis")


def manuscript_schema(header: dict[str, str]) -> str:
    """Return current, legacy, mixed or unknown from fields, never filename.

    First production drafts may legitimately be named ``-v1.md`` while already
    using the current workflow header. Schema identity therefore belongs to the
    header contract itself, not the revision suffix.
    """
    current = any(field in header for field in CURRENT_MANUSCRIPT_MARKERS)
    legacy = any(field in header for field in LEGACY_MANUSCRIPT_MARKERS)
    if current and legacy:
        return "mixed"
    if current:
        return "current"
    if legacy:
        return "legacy"
    return "unknown"


def check_manuscripts(files: list[tuple[str, str]], report: Report) -> int:
''')

rep(
'''        header = parse_header(text)
        legacy = is_legacy_draft(rel)

        # The publication block is the one guarantee enforced on every schema.
''',
'''        header = parse_header(text)
        schema = manuscript_schema(header)

        # The publication block is the one guarantee enforced on every schema.
''')

rep(
'''        if legacy:
            missing = [f for f in LEGACY_MANUSCRIPT_FIELDS if f not in header]
            if missing:
                report.warn(
                    f"C5 {rel}: legacy draft missing {', '.join(missing)} — "
                    f"carries the v1 header schema"
                )
            else:
                report.warn(
                    f"C5 {rel}: uses the v1 header schema "
                    f"(Publication Status / Canon Basis, header below the title); "
                    f"migrate when the episode is revised to v2"
                )
        else:
            for field in REQUIRED_MANUSCRIPT_FIELDS:
                if field not in header:
                    report.error(f"C3 {rel}: missing required header field {field!r}")
''',
'''        if schema == "legacy":
            missing = [f for f in LEGACY_MANUSCRIPT_FIELDS if f not in header]
            if missing:
                report.warn(
                    f"C5 {rel}: legacy draft missing {', '.join(missing)} — "
                    f"carries the legacy header schema"
                )
            else:
                report.warn(
                    f"C5 {rel}: uses the legacy header schema "
                    f"(Publication Status / POV / Canon Basis); migrate when "
                    f"the manuscript itself is revised to the current schema"
                )
        elif schema == "mixed":
            report.error(
                f"C3 {rel}: mixes current and legacy manuscript header fields — "
                f"use one schema consistently"
            )
        else:
            # Current or unknown manuscripts are held to the current production
            # contract. This prevents a partially broken current header from
            # silently falling back to the permissive legacy path.
            for field in REQUIRED_MANUSCRIPT_FIELDS:
                if field not in header:
                    report.error(f"C3 {rel}: missing required header field {field!r}")
''')

rep(
'''        (
            "C2 exempts v1 draft manuscripts",
            [("manuscript/ga1/002-x-v1.md", "리안 카르도")],
            "names",
            "",
        ),
''',
'''        (
            "C2 exempts legacy-schema draft manuscripts",
            [(
                "manuscript/ga1/002-x-v1.md",
                "# 제2화 t\\n\\nStatus: FIRST DRAFT\\nPublication Status: NOT AUTHORIZED\\n"
                "POV: p\\nCanon Basis: card\\n\\n리안 카르도",
            )],
            "names",
            "",
        ),
        (
            "C2 checks current-schema manuscripts even when filename is v1",
            [(
                "manuscript/ga1/021-x-v1.md",
                "Status: DRAFT\\nEpisode: E21\\nCanon Check: SELF-PASS\\n"
                "Publication: NOT AUTHORIZED\\n\\n# 제21화 t\\n\\n리안 카르도",
            )],
            "names",
            "C2",
        ),
''')

rep(
'''        (
            "C3 accepts the legacy v1 publication field name",
            [
                (
                    "manuscript/ga1/002-x-v1.md",
                    "# 제2화 t\\n\\nStatus: FIRST DRAFT\\nPublication Status: NOT AUTHORIZED\\n"
                    "POV: 리안 근접 3인칭\\nCanon Basis: card\\n\\n" + "가" * 6000,
                )
            ],
            "manuscripts",
            "C5",
        ),
''',
'''        (
            "C3 accepts the legacy v1 publication field name",
            [
                (
                    "manuscript/ga1/002-x-v1.md",
                    "# 제2화 t\\n\\nStatus: FIRST DRAFT\\nPublication Status: NOT AUTHORIZED\\n"
                    "POV: 리안 근접 3인칭\\nCanon Basis: card\\n\\n" + "가" * 6000,
                )
            ],
            "manuscripts",
            "C5",
        ),
        (
            "C5 accepts current schema even when the manuscript filename is v1",
            [
                (
                    "manuscript/ga1/021-x-v1.md",
                    "Status: DRAFT\\nEpisode: E21\\nCanon Check: SELF-PASS\\n"
                    "Publication: NOT AUTHORIZED\\n\\n# 제21화 t\\n\\n" + "가" * 6000,
                )
            ],
            "manuscripts",
            "!C5",
        ),
''')

p.write_text(text, encoding='utf-8')
print('patched tools/validate_canon.py')
