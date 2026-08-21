#!/usr/bin/env python3
"""Reviewed secondary relationship-label classifications.

These labels contain words like trust/standing but do not declare an emotional
or interpersonal state change. They are option names, constituency membership,
legal standing, beneficiary/harmed claimant standing, or a current-status
warrant. Promoting them into RELATIONSHIP_EMOTIONAL_DELTA would fabricate an
emotional beat.
"""

from __future__ import annotations

REVIEWED_NON_EMOTIONAL: dict[tuple[int, str], str] = {
    (63, "local/patient trust"): "institutional option label for a slower current-right separation path; not a trust-emotion delta",
    (590, "members/standing"): "enumeration of participating constituencies/standing categories; not a relationship-state change",
    (789, "standing"): "procedural/legal standing bundle (notice, counsel, appeal, review-seat and identity-use rights); not emotion",
    (893, "beneficiary standing"): "beneficiary evidence/claim standing for service continuity gains; not interpersonal emotion",
    (893, "harmed standing"): "harmed-party claim standing retained by affected groups; not interpersonal emotion",
    (938, "current standing warrant"): "time-bounded current-status access warrant; legal/service standing, not emotional state",
}

assert len(REVIEWED_NON_EMOTIONAL) == 6
