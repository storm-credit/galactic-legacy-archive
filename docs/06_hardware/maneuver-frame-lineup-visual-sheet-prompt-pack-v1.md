# Maneuver Frame Lineup Visual Sheet Prompt Pack v1

Status: PROPOSED — NONCANON
Owner: M00 Visual PM
Last Reviewed: 2026-08-11
Depends On: [[maneuver-frame-lineup-master-architecture-v1]], [[lfx-01-axiom-visual-development-orchestra-audit-v1]], [[mecha-lineage-mark-and-evolution-naming-system-v1]]
Input References: user-provided `캐릭터시트1 (1).png`, `캐릭터시트2 (1).png`; AXIOM v11 body, v14 armored-neck and A/B head studies
Canon Promotion: NOT AUTHORIZED
Publication: NOT AUTHORIZED

## 1. Reference-Sheet Analysis

The two character sheets are used only for information architecture. Their character designs, decorative borders, illustration style and exact panel layout are not copied.

| Reference trait | Useful effect | Mecha-sheet adaptation | Do not copy |
|---|---|---|---|
| large primary portrait beside compact modules | subject identity is established before details | one large 3/4 key view plus smaller orthographic and mechanical panels | exact left/right split, floral border and anime rendering |
| identity/profile block | facts remain scannable | designation, role, lineage, size status and canon gate block | prose biography density inside generated art |
| expression row | consistent head identity under variation | sensor/visor operational-state row using one head geometry | character facial expressions or mascot treatment |
| full-body front/side/back | continuity and modeling control | strict orthographic front/side/back, same scale and neutral pose | decorative pose changes in orthographic views |
| outfit/design breakdown | materials and construction become collectible | head, neck, chest, hand, joint, backpack and weapon stowage callouts | isolated parts with no attachment or scale logic |
| color/tone block | palette is memorable and reproducible | material swatches with percentage hierarchy and finish labels | two-color palette or uniform gloss |
| abilities/poses | action promise is visible | mission sequence: approach, capture, rescue, recovery | unbounded superpower thumbnails |
| scale reference | grounds the design | human, cradle and hatch comparison | invented exact dimensions before 07 conflict is resolved |

### Layout decision

The mecha line uses a **landscape 16:9 technical board**, not the references' tall poster layout. Generate clean artwork without long text. Add typography and data labels in a separate layout pass to avoid unreadable AI text.

## 2. Shared Image-Generation Guardrails

Use these controls in every prompt:

- original hard-surface humanoid maneuver frames for a Korean space-opera setting;
- modern aerospace/industrial design, functional joints, clear maintenance access and believable weapon stowage;
- large primary armor masses 65%, service panels 27%, micro detail no more than 8%;
- no uniform surface greebling, random vents, random spikes, antique wear or all-over rust;
- no V crown, long central horn, paired demon horns, animal ears, red chin, human nose/mouth mask or bald round head;
- no angel wing backpack, bilateral feather-like wings, halo, magic circle or ornamental gold filigree;
- no direct reproduction of any existing published mecha-franchise design;
- no trademarks, logos, franchise names or fake paragraphs in the image;
- physically plausible neck rotation, collar clearance, sensor field, elbow/knee motion, cooling and service access;
- one stable machine scale within each comparison row;
- neutral studio lighting unless the prompt explicitly requests a key visual;
- labels limited to large `A`, `B`, `C`, `D` or machine codes; all detailed text added later.

## 3. Sheet 01: Four Portfolio Directions at a Glance

### Purpose

Compare lineup architecture before individual-machine polish. Each quadrant must differ in roster hierarchy, not just color or horns.

### Generation prompt

```text
Create a single landscape 16:9 professional mecha lineup comparison board, 3840x2160, divided into four equal clean quadrants labeled only A, B, C, D. Every quadrant contains exactly six machine silhouettes at the same visual scale. White-to-light-gray neutral studio background, thin technical divider lines, consistent 3/4 front camera at chest height, no decorative border and no long text.

SETTING: original Korean space-opera maneuver frames designed for boarding, capture, rescue, repair, relay and node control; they support fleets rather than replacing fleet warfare. Modern aerospace hard-surface construction, believable joints and maintenance access, no direct resemblance to an existing franchise.

A HERO-RIVAL SPINE: six figures arranged as protagonist, rival, enemy command machine, two mass units and one support machine. Strong individual silhouettes, but all grounded in practical storage and service limits. Emotional clarity and duel-readiness without tournament flamboyance.

B FACTION INDUSTRIAL GENOME: six representatives for the six core mass-service manufacturing families. Clearly different grayscale shape grammars: open-service gantry, imperial nested arches, certified hex cells, open industrial bridge, neutral rescue cradle and frontier rebuilt donor frame. The two rare interface/legacy families are reserved for the dedicated eight-lineage board. This quadrant must remain readable with color mentally removed.

C MISSION ECOSYSTEM: six machines shown as a functional chain: recon opens access, relay shares a bounded picture, breach secures a node, capture restrains, rescue evacuates people, recovery tows damaged hardware. Each role is expressed by chassis load paths, stance and tools, not a backpack swap.

D COLLECTOR CHRONICLE: six figures in a restrained lineage timeline: baseline mass unit, reversible mission fit, major rebuild, regional fork, true successor and separate legacy candidate. Show clear inherited motifs but no suffix-only recolor. The successor must have a new load frame and silhouette.

CMF: varied balanced palettes across the board; ceramic whites, graphite, titanium, cobalt, oxide green, safety yellow, vermilion and restrained cyan status lights. Avoid a dark monochrome board and avoid two-color machines. Large calm armor surfaces, exposed mechanical joints only where functional.

HARD NEGATIVES: no V-fin, no long forehead spike, no demon horns, no round bald android head, no human face mask, no winged backpack, no giant decorative gunblade, no impossible weapon storage, no glowing full-body transformation, no antique or steampunk finish, no franchise logos, no gibberish paragraphs.
```

### Pass criteria

1. A-D read as different portfolio strategies at thumbnail size.
2. B's six core manufacturing lineages remain distinguishable without color; all eight are tested on Sheet 02.
3. C communicates a sequence rather than six combat poses.
4. D distinguishes refit from successor.
5. No quadrant uses a horn or wing count as its main difference.

## 4. Sheet 02: Eight-Lineage Silhouette and CMF Board

### Purpose

Lock the manufacturing families before named hero machines. This is the most important originality test.

### Generation prompt

```text
Create a landscape 16:9 industrial design board showing eight original humanoid maneuver-frame manufacturing lineages in two rows of four. Each cell contains one neutral front 3/4 full-body machine, one small pure black silhouette thumbnail, and three rectangular material swatches. Clean light-gray studio background, identical camera, focal length and body scale in every cell. Labels only L01 through L08.

L01 OPEN SERVICE: narrow inspection core, large service hands, visible gantry void, slightly asymmetric tool-side mass; off-white, blue-gray, safety coral, neutral metal.
L02 IMPERIAL NESTED ARCH: low roof sensor, repeated inverted-U structural arches at chest and cuffs, aligned shoulders and knees; pearl gray, charcoal, gunmetal, tiny authority amber.
L03 HELIX CERTIFIED CELL: truncated hex sensor cassette, three joined service cells, 60-degree inspection windows, modular limbs; cool gray, oxide green, industrial orange, small cyan indicators.
L04 ARDIS OPEN BRIDGE: low wedge head, horizontal shoulder beam, open central maintenance bay, anchored ankles; titanium, cobalt, oxide red, safety yellow workshop marks.
L05 NEUTRAL RESCUE CRADLE: head protected inside collar, C-shaped shoulder voids, central rescue channel, broad structural forearms and low center of gravity; ivory, sea green, vermilion rescue marks, dark anti-glare panels.
L06 FRONTIER REBUILT: visible donor-frame scars, asymmetrical thermal coat, manual backup links, external anchor hardware; graphite, raw aluminum, stripped white heat coat, signal orange.
L07 CONTINUITY / PALIMPSEST INTERFACE: layered provenance plates, recessed sensor shutters, offset data spine, guarded tool ports; smoked white, dark nickel, muted red, aqua status light.
L08 ISOLATED LEGACY: athletic modern chassis with broken shear-line armor, dual cyan eyes under low armored brows, asymmetric notch, compact articulated armored neck, no shared mass-market parts; ceramic white 52%, graphite 29%, titanium 9%, crimson 9%, cyan light 1%.

All eight must have plausible necks, collars, hands, knees, cooling and maintenance seams. Large armor hierarchy 65/27/8. No pose theatrics and no weapons large enough to hide the body.

HARD NEGATIVES: no V crown, no central horn, no paired demon horns, no antenna forest, no red chin, no human mouth, no wing backpack, no color-only variation, no identical shared head, no direct franchise design, no logos or fake prose.
```

### Pass criteria

- 128 px: viewer identifies role family.
- 64 px: viewer identifies manufacturing lineage.
- L01 versus L04, L02 versus L08, and L03 versus L05 remain distinct.
- L08 remains unique after sword and color are hidden.

## 5. Sheet 03: Twelve Visual Comparison Representatives

### Selected representatives

`07`, `SOLVERN`, `VARDEN`, `CALDRIX`, `HEXAR`, `TESSAR`, `TORREL`, `BRAVIK`, `ARVET`, `DELVRIK`, `DRASEL`, and `AXIOM HOLD`.

This is a visual-diversity board, not the CSV's reader-tier `FRONT` list. It deliberately includes support and HOLD representatives to compare lineage identity.

### Generation prompt

```text
Create a wide 2:1 professional mecha catalog board with twelve original maneuver frames arranged in two rows of six. Each machine appears in a restrained neutral stance, full body, same scale and same 3/4 front camera. Under each machine leave a clean blank caption strip with only its code rendered in large simple characters. Light neutral background, precise hard-surface concept art, readable silhouette first, no action effects.

Use the eight lineage grammars from the project brief. Show two related machines as relatives through one or two repeated structural motifs, never by reusing the entire body. Mass units should be simpler and more serviceable than command or legacy machines. Support units must express function through arms, stance, cooling and cradle interfaces rather than only attached backpacks.

The twelve codes are: AUX-07, AD-OS-3.2, IR-B24-01, IR-C27-01, HX/SC-12.C4, HX/BR-21.C6, AD-WK-11.3, AD-DF-14.2, NA-RS-8-06, BRN-17/B3, CS-RD-19.2, LFX-01.

AXIOM visual constraints: modern white/crimson/graphite/titanium/cyan balance, A/B dual-eye face, low armored brow, visible compact articulated neck, angular mechanical jaw with no human mouth, athletic but armored proportions, strong header volume without horns, broken shear-line motif, physical sword shown stowed along a believable side or rear mount, compact carbine secondary. AXIOM must not dominate the board through size or wings.

HARD NEGATIVES: no existing franchise names, no franchise face topology, no V-fin, no long horn, no demon horns, no round bald head, no wing fan, no giant decorative sword, no impossible stowage, no antique finish, no monochrome dark palette, no gibberish descriptive text.
```

### Layout note

Do not ask the image model to render Korean names or descriptions. Add them in the production layout after selection:

```text
[working everyday name]
[formal code] · [role]
[PROPOSED — NONCANON]
```

## 6. Sheet 04: AXIOM Head-Neck Four Directions with Fixed Sword Reference

### Purpose

Resolve the remaining user concern: the preferred dual eyes and armored head need a visible neck, enough header presence, and less familiar franchise face topology. Sword geometry and storage remain identical in all four quadrants so this pass changes only the head-neck variable group.

### Four directions

| Direction | Head topology | Neck | Fixed sword reference | Risk |
|---|---|---|---|---|
| A. Split Brow | two low brow armor blocks separated by asymmetric notch | two-stage armored rotary collar | same straight blade and rear-hip mount | can become too familiar if cheeks form a classic mask |
| B. Shear Visor | dual eyes in one broken horizontal cavity, offset upper plate | exposed dark gimbal between white collar shells | same straight blade and rear-hip mount | may look too narrow at full-body scale |
| C. Service Crownless | broad upper skull with recessed service hatch, no upward fins | tallest visible neck, compact rear actuator | same straight blade and rear-hip mount | can look utilitarian rather than flagship |
| D. Offset Helm | one side plate longer, eyes remain balanced, asymmetric jaw guards | armored neck with one visible maintenance ring | same straight blade and rear-hip mount | asymmetry can become noisy |

### Generation prompt

```text
Create one square 2048x2048 head-neck design comparison sheet divided into four equal quadrants labeled A, B, C, D. Each quadrant contains a large 3/4 head and upper-chest view, a small front head thumbnail, a small side neck-clearance diagram, and the same small fixed sword-stowage silhouette. Same original AXIOM body language, palette, sword and rear-hip storage geometry in every quadrant; only head topology and neck treatment change.

Shared AXIOM constraints: dual cyan eyes, low armored brow, white ceramic primary armor, graphite internal frame, crimson load-line accents, cool titanium impact surfaces, compact but clearly visible articulated neck, mechanical jaw without human mouth, modern hard-surface flagship presence, strong head volume without horns. No long central spike, no V crown, no paired demon horns, no antenna forest, no round bald shell.

A SPLIT BROW: two low brow blocks with one asymmetric gap, faceted cheek guards that do not create a familiar colored-chin face, two-stage armored rotary collar.

B SHEAR VISOR: dual eyes inside one broken horizontal sensor cavity, offset upper skull plate, dark gimbal visible between white collar shells.

C SERVICE CROWNLESS: broad upper skull with recessed maintenance hatch and shallow side sensor tabs, tallest visible neck of the four with compact rear actuator, flagship but not ornamental.

D OFFSET HELM: balanced dual eyes under asymmetrical side plates, one jaw guard longer without becoming an animal face, armored neck with one visible maintenance ring.

FIXED REFERENCE IN EVERY QUADRANT: identical practical straight physical sword, identical guard, identical rear-hip mount and identical draw envelope. Do not redesign or relocate the sword in this pass.

Neutral light-gray studio, sharp product-concept lighting, no battle effects, no logos, no fake prose. Preserve 65/27/8 surface hierarchy. The four options must be materially different and not color variants.
```

### Recommended next pass

Generate this sheet before another AXIOM full-body key visual. Select one head/neck direction, apply only that variable group to the approved v11/v14 body baseline, then run a separate four-direction sword-storage pass.

## 7. Sheet 05: One-Machine Production Model Sheet Template

### Composition

Use this reusable layout after a candidate chassis is selected:

1. large 3/4 key view, 36% of board;
2. front/side/back orthographic row, 28%;
3. head/neck/chest/hand/joint callouts, 12%;
4. weapon stowed/draw/guard/maintenance sequence, 10%;
5. cradle, hatch and human scale, 6%;
6. CMF percentages and finish swatches, 4%;
7. status and approval strip, 4%.

### Reusable prompt

```text
Create a landscape 16:9 production-ready technical model sheet for one original humanoid maneuver frame. Use a large three-quarter hero view plus strict front, side and back orthographic views at identical scale. Include clean detail callouts for head and articulated neck, chest load path, shoulder clearance, hand grip, hip storage, knee actuator, lower-leg cooling, backpack/cradle interface and weapon stowage. Include a human silhouette and docking cradle for scale but do not invent numeric dimensions. Include material swatches without words. Neutral light-gray background, thin technical dividers, no decorative border, no fake paragraphs.

The machine must follow its supplied lineage silhouette and CMF grammar. Every visible seam must imply armor removal, service access, heat rejection or load transfer. Show no capability not present in the supplied machine brief. Show the weapon in stowed, draw, two-hand use and maintenance states. Make neck rotation and collar clearance visually plausible.

HARD NEGATIVES: no franchise resemblance, no horns or V crown, no human mouth mask, no ornamental wings, no random spikes, no full-body glow, no impossible weapon storage, no antique weathering, no uniform tiny panel lines, no unreadable text.
```

## 8. Result Inspection Checklist

### Content

- correct machine count and codes;
- no accidental new ability, transformation, pilot, faction or story event;
- no exact dimensions until the source conflict is resolved;
- 07 and AXIOM remain separate entities;
- AXIOM forms are not counted as new chassis.

### Mechanics

- neck rotates without cheek/collar collision;
- sensors can see past brow and shoulder armor;
- elbows, knees and hips can achieve the shown pose;
- hands can grip the weapon with guard clearance;
- weapon can be stored and drawn inside a believable cradle envelope;
- cooling, refueling and service panels are reachable.

### Visual identity

- 64 px silhouette family test passes;
- color is not the only differentiator;
- head is neither bald/round nor horn-dependent;
- palette uses at least primary armor, frame, impact metal, signal accent and emissive status layers;
- large surfaces remain calm and modern.

### Originality

- no direct match in silhouette, face topology, crest, color zoning and weapon placement to one reference design;
- at least three of those axes materially differ from any identified comparison;
- remove franchise names from the generation prompt itself;
- record rejected images and why they failed.

## 9. Gate

**READY FOR IMAGE TESTS — NONCANON**

- These prompts may generate comparison and model-sheet tests.
- Generated pixels do not create canon.
- AXIOM full-body finalization remains blocked on the head-neck-sword four-direction selection and author story decision.
- No canon change, manuscript approval, publication approval or PR merge is authorized.
