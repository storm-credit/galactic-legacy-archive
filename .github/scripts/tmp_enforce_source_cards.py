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
    'REQUIRED_MANUSCRIPT_FIELDS = ("Status", "Episode", "Canon Check", "Publication")',
    'REQUIRED_MANUSCRIPT_FIELDS = ("Status", "Episode", "Source Cards", "Canon Check", "Publication")',
)

anchor = '''        (
            "C3 detects a manuscript with no publication field at all",
            [("manuscript/ga1/001-x-v2.md", "Status: REVISED\\n\\n# t\\n\\nbody")],
            "manuscripts",
            "C3",
        ),
'''
insert = anchor + '''        (
            "C3 requires Source Cards on current-schema manuscripts",
            [
                (
                    "manuscript/ga1/021-x-v1.md",
                    "Status: DRAFT\\nEpisode: E21\\nCanon Check: SELF-PASS\\n"
                    "Publication: NOT AUTHORIZED\\n\\n# 제21화 t\\n\\n" + "가" * 6000,
                )
            ],
            "manuscripts",
            "C3",
        ),
'''
rep(anchor, insert)

p.write_text(text, encoding='utf-8')
print('patched tools/validate_canon.py to require Source Cards')
