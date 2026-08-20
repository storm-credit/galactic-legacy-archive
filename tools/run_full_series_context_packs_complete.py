#!/usr/bin/env python3
"""Run the complete Context renderer while preserving the deep normalizer.

`build_full_series_context_packs_complete` overlays rendering/auditing on the
existing deep normalizer. Preserve that source normalizer before importing the
final overlay so fallback enrichment cannot recursively call itself.
"""

import build_full_series_context_packs_deep as deep

source_normalized = deep.normalized

import build_full_series_context_packs_complete as complete  # noqa: E402

# The final overlay intentionally reuses the previous normalization layer.
complete.deep.normalized = source_normalized

if __name__ == "__main__":
    raise SystemExit(complete.main())
