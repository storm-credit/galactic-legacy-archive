# 07 Physical Envelope Conflict Resolution Audit v1

Status: QUALITY-CONTROL — NONCANON CONFLICT AUDIT
Effective Authority: QC/NC
Owner Agents: A00 PM / O01 Canon / H01 Frame / H04 Maintenance / X01 Logic / X04 Continuity / A16 Red Team
Last Reviewed: 2026-08-20
Depends On: [[first-frame-bible-v1]], [[academy-and-07-opening-operational-state-v1]], `docs/_entities/frames/07호.md`, [[effective-canon-status-manifest-v1]]
Used By: future narrow 07 canon correction, model sheet, prototype provenance work
Canon Change: NOT AUTHORIZED
Publication: NOT AUTHORIZED

---

## 0. Conflict

Two current accepted sources carry different opening physical values.

### first-frame-bible-v1

`Physical Envelope`:
- Height: **10.8 m provisional**
- Operational mass: **41 t in opening configuration**

### academy-and-07-opening-operational-state-v1

`07 Physical Baseline`:
- Height: **11.6 m standing**
- Operational mass: **48–57 t depending training armor/tools**

### current entity hub

`docs/_entities/frames/07호.md` repeats:
- **11.6 m**
- **48–57 t**

and explicitly points to the opening operational-state sheet as the source for operational state/defects.

---

# 1. Repository propagation finding

Search result:
- `10.8 m / 41 t` is materially localized to the first-frame bible’s `provisional` Physical Envelope;
- `11.6 m / 48–57 t` is used by both the opening operational-state source and the current front-stage entity hub.

This is not a broad 50-file contradiction.

---

# 2. Four resolution options

## A — Current operational state supersedes old provisional envelope

Interpretation:
- 10.8 / 41 was early design calibration;
- later execution design fixed opening scene-ready values at 11.6 / 48–57;
- entity hub correctly reflects the later execution value.

Strength:
- best source/usage evidence;
- simplest;
- no invented historical explanation;
- preserves current scene staging and support calculations.

Weakness:
- requires a narrow correction note/update to first-frame bible later.

Verdict:
- **RECOMMENDED.**

---

## B — Original AUXILIA core versus current training configuration

Interpretation:
- 10.8 / 41 = old stripped/original service configuration;
- 11.6 / 48–57 = current Academy training armor/tools configuration.

Strength:
- both numbers become in-world true;
- fits Ship-of-Theseus history superficially.

Weakness:
- the first-frame bible explicitly calls 41 t `opening configuration`, not ancient/original configuration;
- would invent a new historical fact solely to rescue stale numbers;
- 0.8 m height change needs a real geometry explanation, not just armor mass.

Verdict:
- **REJECT unless later engineering design independently needs two envelopes.**

---

## C — Measurement-condition difference

Interpretation:
- one value excludes radiator/tool structures or uses cradle/stowed posture;
- another uses full standing operational configuration.

Strength:
- technically possible.

Weakness:
- current wording does not say this;
- 41 t versus 48–57 t is too large to hand-wave without specific modules;
- height is explicitly `standing` only in later source but `Height` in first source.

Verdict:
- **NOT RECOMMENDED AS RETROACTIVE PATCH.**

---

## D — Keep both unresolved

Strength:
- avoids editing.

Weakness:
- future model sheets, combat physics, transport/cradle and visual art cannot know which to use;
- unnecessary ambiguity on a front-stage machine.

Verdict:
- **REJECT FOR PRODUCTION.**

---

# 3. Source-precedence reasoning

This audit does not silently change canon, but current evidence favors Option A.

Reasons:
1. first-frame value is explicitly marked **provisional**;
2. opening operational-state sheet is an execution-oriented source used directly by E1–20;
3. current entity hub repeats 11.6 / 48–57 and cites the operational-state sheet;
4. no wider repository propagation of 10.8 / 41 was found in the quick exact-value search;
5. inventing a two-configuration historical explanation adds lore solely to preserve a provisional number.

Therefore the likely problem is **document drift**, not hidden dual configuration.

---

# 4. Recommended future narrow correction

If approved under change control:

### first-frame-bible Physical Envelope

Replace or annotate:
- `10.8 m provisional`
- `41 t in opening configuration`

with current execution baseline:
- `11.6 m standing`
- `48–57 t depending on training armor/tools`

and retain a correction-history note that the older provisional calibration was superseded by the opening operational-state lock.

Do not mass-edit historical audit files that quote old values unless they are actively used as authority.

---

# 5. What this does not change

No effect on:
- 07 service ancestry;
- AUXILIA provenance;
- prototype-slot interpretation;
- pilot count;
- opening defects;
- E1–20 events;
- power percentages;
- permanent losses;
- ownership/authority;
- weapon load;
- later 07 fate.

This is a physical-envelope normalization only.

---

# 6. Prototype-program interaction

Do **not** use 10.8 / 41 as a hidden “historical P-07 original configuration” in new prototype packets unless separately approved.

Reason:
- that would convert a likely stale provisional value into new canon history.

Historical Slot 07 physical envelope remains open and can differ from the current Academy hull only if a later engineering/provenance design has independent reason.

---

# 7. Severity

Suggested continuity severity:
- **S2 document/calibration drift**, not S0/S1 story contradiction.

Why:
- current execution source is clear;
- no known scene outcome depends on the smaller values;
- correction is narrow and does not alter plot.

Do not add to main `continuity-issues.md` from this NONCANON branch until a canon correction is actually proposed/authorized.

---

# 8. Current ruling

### Option A — later operational value supersedes provisional
**RECOMMENDED.**

### Current working value for new NONCANON calculations
**11.6 m / 48–57 t**, because that is the execution-state + entity-hub value.

### Rewrite first-frame bible now
**NO — canon change requires controlled narrow patch.**

### Invent original-vs-current explanation now
**NO.**

### Story impact
**NONE.**

> **PHYSICAL-ENVELOPE CONFLICT IS A NARROW S2 DRIFT, NOT A REASON TO INVENT NEW LORE.**
