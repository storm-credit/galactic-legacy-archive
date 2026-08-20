#!/usr/bin/env python3
"""Run deep writer activation while preserving the base activation function.

The runner also normalizes high-signal card labels that appear in later locked
operation cards (`Independent decision`, `Decision process`, and combined
`POV/decision owner(s)`). This prevents a participant/location line from being
mistaken for the actual decision beat.

Critical irreversible-loss and final-transfer episodes additionally receive a
workflow-only dominant-engine override so keyword frequency cannot classify a
technical sacrifice as a relationship episode or a record-person loss as generic
service. The event/decision facts still come only from approved sources.
"""

import build_full_series_context_writer_activation as base

_ORIGINAL_ACTIVATION = base.activation
_ORIGINAL_SOURCE_DECISION = base.source_decision
_ORIGINAL_SOURCE_POV = base.source_pov


def enhanced_source_decision(card):
    value = base.first(
        card,
        "independent decision",
        "decision process",
        "final decision",
        "current decision",
        "medical decision",
        "technical decision",
        "command decision",
        "decisive choice",
        "decision",
        "choice",
        "physical action",
        "action",
        "agency",
        "authorized immediately",
    )
    if value:
        return value, "SOURCE-EXPLICIT-DECISION"
    value = base.source_block(
        card,
        (
            "independent decision",
            "decision process",
            "final decision",
            "current decision",
            "decisive choice",
            "decision",
            "choice",
            "physical action",
            "action",
            "agency",
            "response",
            "resolution",
        ),
    )
    if value:
        return value, "SOURCE-BLOCK-DECISION"
    return None, "NON-DISCRETE"


def enhanced_source_pov(card):
    return base.first(
        card,
        "pov / decision owner",
        "pov/decision owner",
        "pov / decision owners",
        "pov/decision owners",
        "pov / information source",
        "pov",
    )


base.source_decision = enhanced_source_decision
base.source_pov = enhanced_source_pov

import build_full_series_context_writer_activation_deep as deep  # noqa: E402

# Workflow/QC labels only; the underlying event and loss facts remain governed
# by the episode card + named-loss/final-payoff/ending ledgers.
deep.SPECIAL_ENGINE.update({
    150: "TECHNICAL-REPAIR/TEST",      # Jena Ark accident/agency
    322: "TACTICAL-COMBAT",            # Toma Cal command-station sacrifice
    680: "MEDICAL/CARE/CONSENT",       # Ella Savin patient/medical separation
    683: "TACTICAL-COMBAT",            # Ardo Rev two-command hold
    684: "TECHNICAL-REPAIR/TEST",      # Parus propulsion + Vera permanent injury
    762: "MEDICAL/CARE/CONSENT",       # Lin Osa downstream care/route consequence
    841: "RECORD/PROVENANCE/MYSTERY",  # LIV-4 person/evidence fracture
    889: "RECORD/PROVENANCE/MYSTERY",  # Nacre-3 permanent record loss
    1084: "COLLECTION/ACCESS/TRANSFER",# 07 unique combat custody/fate split
    1085: "TECHNICAL-REPAIR/TEST",     # public technical commons / Nera limit
    1088: "ENDING/HANDOFF",            # Rian exclusive-index removal
})


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
