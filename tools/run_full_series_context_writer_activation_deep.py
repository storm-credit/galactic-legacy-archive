#!/usr/bin/env python3
"""Run deep writer activation while preserving the base activation function."""

import build_full_series_context_writer_activation as base

_ORIGINAL_ACTIVATION = base.activation

import build_full_series_context_writer_activation_deep as deep  # noqa: E402


def safe_activation(card):
    current = base.activation
    base.activation = _ORIGINAL_ACTIVATION
    try:
        return deep.activation_deep(card)
    finally:
        base.activation = current


base.activation = safe_activation


def main():
    rc = base.main()
    if rc:
        return rc
    cards = base.semantic.base.load_sources()
    acts = [safe_activation(cards[ep]) for ep in range(11, 1101)]
    strict = base.ROOT / "docs" / "99_quality_control" / "full-series-context-writer-activation-false-a-redteam-v1.md"
    strict.write_text(deep.render_strict_audit(acts), encoding="utf-8")
    print(f"strict_false_a_audit={strict.relative_to(base.ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
