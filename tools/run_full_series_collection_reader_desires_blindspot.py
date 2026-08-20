#!/usr/bin/env python3
"""Run the Collection Desire finalizer with source-bound semantic blindspot fixes.

No new collectible, event or authority is created. The overrides below only
replace shorthand/administrative tokens that were not usable writer-facing
reader-desire language with sentences compressed from the owning approved
subact map.
"""

from __future__ import annotations

import run_full_series_collection_reader_desires as runner


runner.reader.OVERRIDES[("GA7", "7C-4")] = {
    "discovery": (
        "survivors, service-collapse evidence and affected-region claims must be preserved before federation, Continuity, State and Scorched narratives harden the incident into one convenient story."
    ),
    "acquisition": (
        "secure aid, records and claimant standing while H-001 accepts bounded emergency review, reparations and authority limits without using resignation or total guilt as an escape from specific responsibility."
    ),
    "synergy": (
        "survivor aid, preserved records, affected-region standing and emergency review keep material relief and accountability linked while victims retain the right to reject strategic abstraction."
    ),
    "cost": (
        "H-001's mandate is suspended or reduced or the coalition fractures, and personal relationships with PC/RF actors are damaged."
    ),
    "hook": (
        "evidence that several 'Blood Admiral' incidents occurred under different commanders, titles and timelines turns the next desire into a representative incident matrix and plural responsibility audit."
    ),
}


if __name__ == "__main__":
    raise SystemExit(runner.main())
