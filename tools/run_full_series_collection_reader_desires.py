#!/usr/bin/env python3
"""Run the final reader-desire pass after wiring finalizer chaining correctly.

The manual-target finalizer wraps `source_field_pack` internally. Point that
wrapper's captured base function at the 27-row reader-intent override function
before building, so target routing, GA10 ending guards, strict endpoint filtering
and semantic set routing all remain active together.
"""

from __future__ import annotations

import argparse

import build_full_series_collection_desire_layer as layer
import finalize_full_series_collection_reader_desires as reader


def build_outputs():
    # `final.source_field_pack_manual()` calls `final._original_source_field_pack`.
    # Rebind that captured function before semantic->strict->manual finalization.
    reader.semantic.strict.final._original_source_field_pack = reader.source_field_pack
    return reader.build_outputs()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = build_outputs()
    layer.write_or_check(outputs, args.check)
    audit = outputs[reader.semantic.SET_AUDIT]
    if "Status: PASS — EXECUTION QC" not in audit:
        raise SystemExit("reader-desire chained finalizer produced failing set-family audit")
    print("reader_desire_finalizer_chain=PASS")
    print(f"reader_desire_manual_source_bound={len(reader.OVERRIDES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
