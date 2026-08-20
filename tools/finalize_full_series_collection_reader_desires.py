#!/usr/bin/env python3
"""Final source-bound reader-desire pass for the full-series collection layer.

Twenty-seven subacts have valid active targets but no labelled Goal/Discovery
field in their act-map block, so the generic builder falls back to target names.
That is sufficient for carrier lookup but not for reader-desire normalization.

This pass supplies only reader-intent phrasing derived from the existing act-map
mission/decision/outcome facts. It does not change active targets, events,
casualties, ownership, authority, ending allocation or story canon.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import build_full_series_collection_desire_layer as layer
import finalize_full_series_collection_desire_semantic_sets as semantic

ROOT = Path(__file__).resolve().parents[1]

# Fields: discovery, acquisition, synergy, cost, hook.
# Every phrase below is a compression of the owning act-map block, not a new
# event or new collectible.
OVERRIDES: dict[tuple[str, str], dict[str, str]] = {
    ("GA1", "A1"): {
        "discovery": "Rian is absent from the future record while Haren, the current 07 and the academy cell do not match the roles his memory expects.",
        "acquisition": "establish a bounded provisional cell/process and complete the first limited 07 operation without choosing a sacrificial victim.",
        "synergy": "current trust, route detail, present-body limits and the cell's separate roles become necessary to make the first operation work.",
        "cost": "Rian cannot treat future knowledge as present ownership or competence; the closed-choice/betrayal problem remains a live risk.",
        "hook": "the next desire is to learn who actually owns, maintains and authorizes the damaged 07 and its records.",
    },
    ("GA1", "A2"): {
        "discovery": "07 access is split across ownership, maintenance labor, tools and records, while Soma proves an administrative death record can be materially wrong.",
        "acquisition": "gain usable maintenance/record access and a more accurate map of rights without silently converting access into ownership.",
        "synergy": "Nera's technical rights, workshop labor, Serin's provenance work and 07 service operation become mutually necessary.",
        "cost": "access carries labor, punishment, provenance and claim exposure; an official record can no longer be treated as complete truth.",
        "hook": "external mission, medical, route and certification actors now determine what the cell can legitimately do with 07.",
    },
    ("GA1", "A3"): {
        "discovery": "mission insurance, medical stop authority, community guarantees, Service Authority A, Ern's independent objective and Helix safety all impose valid external limits.",
        "acquisition": "secure bounded service/medical/route access and working relationships without erasing Ern, Helix or current stakeholders' right to refuse.",
        "synergy": "the cell can operate only by combining medical, route, technical and service authority rather than relying on Rian's future answer alone.",
        "cost": "every useful outside relationship adds oversight, claim, refusal or control pressure.",
        "hook": "the first full powered test must prove whether this limited coalition survives when Rian's future-style operation causes real damage.",
    },
    ("GA1", "A4"): {
        "discovery": "Rian's future-style maneuver damages the current 07 and turns the betrayal test into a real question of responsibility rather than a theoretical choice.",
        "acquisition": "keep the cell and 07 mission-capable without solving the failure by assigning one traitor or sacrificial culprit.",
        "synergy": "shared consequence, repair, route planning and bounded authority convert the failed test into a White Dock-ready minimum state.",
        "cost": "07 remains worn and limited, and the cell carries responsibility for a method already visible to outsiders.",
        "hook": "White Dock begins with Ern already inside, shifting the desire from training survival to people/evidence/asset recovery under competing claims.",
    },
    ("GA1", "B1"): {
        "discovery": "White Dock turns recovery into a multi-claim crisis: trapped people, evidence, Ern's separate objective and 07 components cannot all be pursued as one prize.",
        "acquisition": "preserve enough people/evidence to return conditionally while learning that 07 itself is split among claimants rather than simply recovered.",
        "synergy": "Rian, Ern, Nera, Serin, Mia, Haren and local workers solve different rescue/evidence functions without becoming one owned team.",
        "cost": "the locked White Dock deaths and lasting damage remain, radiator loss shuts 07 down, and custody/testimony stay divided.",
        "hook": "Juno's impossible confession creates the next desire: distinguish a usable culprit story from the actual delegated system and guarantees behind it.",
    },
    ("GA1", "B2"): {
        "discovery": "hearing evidence and delegated-token replay undermine the convenient single-culprit story while Serin's own complicity and Juno's conditions remain real.",
        "acquisition": "replace secret disappearance with a small mutual guarantee and audited external placement that Juno can accept or refuse independently.",
        "synergy": "testimony, provenance, manifest/medical checks and student guarantees jointly constrain institutional removal.",
        "cost": "Serin self-exposes, transfer pressure accelerates and the new guarantee creates debt without recruiting Juno into Rian's team.",
        "hook": "with Juno on a separate path, the next concrete desire becomes rebuilding 07 through legitimate component claims before the deadline.",
    },
    ("GA1", "B3"): {
        "discovery": "the component deadline reveals that radiator, arm, sensor and certified manifold each have different safety, labor and ownership paths.",
        "acquisition": "recover a workable subset of 07 components through debt, shared use and evidence custody while deliberately abandoning an unsustainable certified part.",
        "synergy": "Helix diagnosis, worker/design claims, Academy use rights and Neutral evidence mirrors create a mixed reconstruction path.",
        "cost": "the manifold is lost, debt/inspection remain and the reconstructed 07 cannot become a clean fully owned machine.",
        "hook": "the physically false Imperial core receipt shifts the collection desire from parts to the missing core's real custody chain.",
    },
    ("GA1", "B4"): {
        "discovery": "the missing core's physical/legal custody and continuity-protocol diversion lead to a useful but exclusive Imperial protection offer.",
        "acquisition": "return the core under four-lock/shared custody and regain conditional 07 operation without making Rian the personal owner of the protection or machine.",
        "synergy": "team disclosure, witness protection, service-authority separation and inferior cooling allow a weaker but accountable 07 to function.",
        "cost": "the machine remains constrained and the visible fifth-answer method escapes the team's control.",
        "hook": "C-9's imitation turns the next desire toward the people, treatment system and grievance hidden behind the copied method.",
    },
    ("GA1", "C1"): {
        "discovery": "the imitation crisis contains real transfer/treatment/family grievances, consent boundaries, adapter provenance and clinically necessary hidden treatment—not a single fake-hero cause.",
        "acquisition": "separate the myth from the actual injured people and institutional/technical causes well enough to reach Black Ward without treating patients as targets to seize.",
        "synergy": "Mia's stop authority, provenance work, safety freezes and public myth correction keep care and investigation from collapsing into one rescue action.",
        "cost": "manual release causes injuries, Leta disappears from the public roster and dismantling the myth carries political cost.",
        "hook": "Black Ward is now a necessary care system and control system at once, creating the desire to learn what it genuinely saves and what it owns.",
    },
    ("GA1", "C2"): {
        "discovery": "Black Ward is a functioning hospital whose patients can reject outsider rescue, while treatment, research, identity and hardware control are separate layers.",
        "acquisition": "gain bounded patient representation, consent and provenance access without converting treatment access into extraction or strategic ownership.",
        "synergy": "rehabilitation, medical stop authority, patient representation and ORA-3's bounded source interface make care possible without one total controller.",
        "cost": "patients remain dependent, extraction can be refused and strategic use is stopped even when technically useful.",
        "hook": "ORA can identify sources but not supply complete memory, so the next desire becomes deciding how much identity/history may be recovered at current-person cost.",
    },
    ("GA1", "C3"): {
        "discovery": "ORA provides sources rather than complete memory, and current/old/new/sealed identity packages conflict with patient privacy and outside offers.",
        "acquisition": "preserve usable identity/provenance processes while allowing deletion, forgetting and Orvan's refusal to be restored or extracted.",
        "synergy": "aggregate publication, consent, medical dependency and bounded transfer rules let identity records serve current people without becoming a complete master archive.",
        "cost": "a strategic fragment is permanently lost, targets/data can escape and some identities still require continuing medicine.",
        "hook": "scarce treatment cycles and competing destinations make the next collection desire a workable multi-party care combination rather than fuller information.",
    },
    ("GA1", "C4"): {
        "discovery": "patients face different urgency, dependency and preferred risk while Helix, Neutral, adapters, 07 service and seizure pressure offer incompatible care paths.",
        "acquisition": "assemble a bounded mixed treatment/destination arrangement that keeps patients alive without giving any one provider total ownership.",
        "synergy": "patient choice, open bridge, Neutral berths, medical stop authority and limited Helix/adapter governance cover different parts of care.",
        "cost": "serious complications, distributed-delay harm and lost hostile/evidence opportunities remain; the school enters insolvency.",
        "hook": "the treatment solution exposes the academy's 30-day survival crisis, moving collection desire from patients to competing institutional futures.",
    },
    ("GA1", "D1"): {
        "discovery": "the closure clock exposes several materially different student/staff futures, and a single vote cannot represent the conditional preferences of the whole academy.",
        "acquisition": "build a usable conditional preference map and representative limits before covert transfer turns one sponsor's package into the default outcome.",
        "synergy": "screening, treatment, routes, emergency work and survey evidence make each package legible through lived service effects rather than slogans.",
        "cost": "there is no majority, vulnerable cases are exposed and the secret Imperial transfer accelerates the conflict.",
        "hook": "the next desire is to compare the five takeover/continuation packages by real capacity, autonomy and cost instead of future-hero value.",
    },
    ("GA1", "D2"): {
        "discovery": "Imperial, Helix, Independence, Neutral and internal/hybrid packages each provide real benefits while imposing different control, capacity and exit limits.",
        "acquisition": "identify a viable but bounded continuation arrangement without using Rian's rejected future-hero ranking to decide who or which package matters most.",
        "synergy": "defense, treatment, route capacity, funding and voluntary departures are compared as different functions rather than collapsed into one sponsor score.",
        "cost": "the hybrid remains underfunded, departures proceed and competing claims physically activate before agreement is complete.",
        "hook": "the packages now become armed operational fronts, so the next desire is to preserve people/records/choices when the school itself becomes the battlefield.",
    },
    ("GA1", "D3"): {
        "discovery": "six simultaneous fronts prove that the academy cannot save every zone, person, record and asset under separate claims and time limits.",
        "acquisition": "keep enough independent people, records and service functions alive to prepare a segmented response instead of surrendering everything to one seizure.",
        "synergy": "local actors, medical transfers, aggregate records, 07 combat and bounded centralized clinical action protect different fronts.",
        "cost": "locked deaths, serious injuries, workshop/record/capacity loss and unsaved zones remain; central command is shown to be genuinely faster in some cases.",
        "hook": "Rian can now take the central key, creating the final GA1 desire: use that power without turning emergency control into permanent ownership.",
    },
    ("GA1", "D4"): {
        "discovery": "central authority can save lives faster, but keeping it would turn emergency success into permanent control over people, records and assets.",
        "acquisition": "stop the mass seizure with bounded central use, then distribute authority into an underfunded charter and independent mission roles before master access expires.",
        "synergy": "segmented authority, local decisions, board/charter rules and separate external-mission roles preserve function after Rian relinquishes the key.",
        "cost": "slower distribution causes visible harm, funding stays short, losses and 07 wear remain, and some people leave under their own choices.",
        "hook": "the first distressed-ship/ghost-key contract turns the next desire into acquiring an operable ship and crew whose command cannot collapse back into Rian.",
    },
    ("GA2", "2A-4"): {
        "discovery": "the first real voyage combines delivery, rescue/tow, passenger/inspection and non-escalation obligations that the ship cannot satisfy at full tactical output simultaneously.",
        "acquisition": "complete enough of the voyage to earn route/insurance certification and slightly stronger crew trust without overriding valid captain/engineering/medical vetoes.",
        "synergy": "NAV-001, Q-001 and crew route/cargo/contract knowledge preserve an objective Rian did not prioritize while 07 remains only one tool in the mission.",
        "cost": "cargo/payment, a suspect target or another objective is lost; repair and debt/pay pressure worsen despite operational arrival.",
        "hook": "a salvage manifest ties the removed second-bay/service module to NR72-061, creating the ghost-parts collection desire.",
    },
    ("GA2", "2B-4"): {
        "discovery": "the recovered 061 collar/module can improve second-bay capacity or preserve relay-service value, but current claimants and future Silex needs prevent taking both benefits freely.",
        "acquisition": "install a partial modular service collar while retaining calibration capacity for Silex and recognizing worker/labor claims.",
        "synergy": "utility/rescue-frame support, relay-service use and old AUXILIA lineage become a flexible but incomplete shared capability.",
        "cost": "revenue share/transport/protection obligations remain and forged-system vulnerability persists in the regional supply chain.",
        "hook": "corridor-wide certification restrictions hit just as Doran community contracts freeze, shifting desire from module completion to preserving people's separate route choices.",
    },
    ("GA2", "2C-3"): {
        "discovery": "the community's chosen destinations can be erased in transit by identity checks, forged manifests, capture, seizure and route delay even after the choices were validly made.",
        "acquisition": "preserve the split convoy's ability to reach different destinations rather than turning protection into keeping everyone in one formation or ship.",
        "synergy": "local/Neutral/Independence captains and community members solve separate crises while the first ship protects only the highest-risk junction.",
        "cost": "one group is delayed, captured, stranded or forced back temporarily, and the ship loses cargo/payment or takes damage.",
        "hook": "the forged-component embargo now threatens several destination groups at once, making open-standard safety the next collection problem.",
    },
    ("GA2", "2D-3"): {
        "discovery": "Silex can be stabilized only by combining the first ship's relay service, 07, workshop/route network and provisional standard while Imperial, Helix, Independence, Neutral, workers and Ardis demand different control.",
        "acquisition": "open one limited Silex window without letting any faction turn emergency access into permanent monopoly or erase Ardis/local worker standing.",
        "synergy": "fleet approach, exterior repair/capture, interior calibration, authentication/evidence and evacuation operate as separate coordinated layers with local vetoes.",
        "cost": "a faction loses people/assets or the ship/module is badly damaged/sacrificed; the result is a limited window, not permanent repair.",
        "hook": "Ardis traffic arrives with imminent node/political collapse and a formal request/claim, converting the route reward into the GA3 city-scale obligation.",
    },
    ("GA3", "3D-2"): {
        "discovery": "distributed authorization delays a real response and proves that central Imperial command could likely have reduced the immediate loss.",
        "acquisition": "improve standing delegated rules and local autonomous response without using the failure as proof that Ardis must surrender permanent central control.",
        "synergy": "local defense/service actors, records, evacuation and standing rules act without waiting for Rian and expose spoof/delay causes.",
        "cost": "irreversible damage, named casualties and political backlash give central-takeover advocates a credible case.",
        "hook": "reduced thermal reserve and traffic pressure force one final high-risk joint A+B+C window.",
    },
    ("GA3", "3D-3"): {
        "discovery": "Ardis must run the limited A+B+C reference operation under attack while moving convoy/civilian traffic, denying seizure and preserving local authority.",
        "acquisition": "achieve a limited-throughput survival window without converting technical coordination into a single permanent emergency key or monopoly.",
        "synergy": "Custodians, civic/transit/foundry services, defense, Neutral audit, narrow Imperial coordination and local workers each own different operational decisions.",
        "cost": "ship/node/district damage and restricted future capacity remain, and political opposition gains a credible argument despite survival.",
        "hook": "with immediate survival secured, the next desire is to turn the emergency arrangement into a permanent local trust before victors capture it.",
    },
    ("GA5", "5A-3"): {
        "discovery": "a real attack shows centralized Protector orders are faster while shared authentication and mandate rules delay deployment.",
        "acquisition": "repel enough of the threat to establish standing defensive intent and an emergency authentication path without granting permanent unified fleet command.",
        "synergy": "P-001 commands one task group while FC-001 and a captain independently stabilize other fronts under standing rules.",
        "cost": "the delay costs cargo, workers, ship or lives, central-command advocates gain credibility and one ship defects or grounds.",
        "hook": "repair tender, missiles and payroll are now the binding constraint, shifting collection desire from combat ships to the support system that makes a fleet real.",
    },
    ("GA5", "5B-1"): {
        "discovery": "the mobile repair tender, engineers, payroll/family records and parts are more decisive to fleet survival than another combat hull and are exposed to competing claims/seizure.",
        "acquisition": "protect or recover enough tender and repair/pay capacity to keep the fleet operable without treating the support crews and records as prize cargo.",
        "synergy": "escort restraint, FC-004/yard route and repair triage, evidence and crew-integration concerns make support preservation the mission objective.",
        "cost": "convoy cargo is split or a combat ship is sacrificed/abandoned, and the tender is in worse condition than expected.",
        "hook": "limited repair capacity creates the next desire: decide transparently which ships return to service and which remain grounded.",
    },
    ("GA5", "5C-2"): {
        "discovery": "after a damaging provincial withdrawal, Talren/Civilian Chain must be protected with fewer ships while civilians still have multiple destinations and local commanders retain independent choices.",
        "acquisition": "preserve enough civilian/convoy movement to earn public legitimacy for the fleet charter without pretending the missing formation can be replaced costlessly.",
        "synergy": "escort, evacuation, route defense, misinformation response and an autonomous provincial/Crown success cover different pieces of the reduced-force mission.",
        "cost": "a military objective/depot position weakens and one convoy/group is delayed, lost or forced to change route.",
        "hook": "FC-005 challenges the coalition's legitimacy from the Outer Front, making earned local command the next relationship/authority target.",
    },
    ("GA5", "5D-2"): {
        "discovery": "a formation loses communication/authentication or receives conflicting orders, removing Rian's real-time command from the test of the Common Fleet Charter.",
        "acquisition": "prove that shared intent and standing rules can produce autonomous success without pretending ambiguity will never cause failure.",
        "synergy": "subordinate commanders choose independently across civilian, depot, provincial, Protector and Outer Front responsibilities.",
        "cost": "at least one success coexists with one failure/misinterpretation, casualties or lost ships/objective, and audit/blame begins before the campaign ends.",
        "hook": "Rian's remaining reserve/07/first ship cannot cover every front, so the next desire is who may decide where the last concentrated capacity goes.",
    },
    ("GA7", "7C-3"): {
        "discovery": "the disputed threshold is reached and H-001 must personally authorize or refuse D4 hard denial under uncertainty while local operators retain execution/refusal choices.",
        "acquisition": "prevent route/node capture and protect another strategic population/front without converting H-001's authority into a mythically consequence-free command.",
        "synergy": "H-001 owns the order, P-001 can argue but not automatically veto, and local captains/operators separately execute, delay or refuse during evacuation and fighting.",
        "cost": "the node/route is destroyed or severely degraded and incomplete evacuees/dependents suffer; the beat cannot end triumphantly.",
        "hook": "casualty/service reports and propaganda immediately attach the Blood Admiral name to H-001 and other denial incidents, creating the next accountability/record desire.",
    },
}

_original_source_field_pack = layer.source_field_pack


def source_field_pack(subact: layer.Subact, selected):
    fields = _original_source_field_pack(subact, selected)
    override = OVERRIDES.get((subact.arc, subact.code))
    if override:
        return dict(override)
    return fields


def mark_source_mode(text: str, arc: str) -> str:
    lines = text.splitlines()
    current_code = None
    output: list[str] = []
    heading_re = re.compile(r"^##\s+([^ ]+)\s+—")
    for line in lines:
        heading = heading_re.match(line)
        if heading:
            current_code = heading.group(1)
        output.append(line)
        if line.startswith("- `MATCH_DEPTH`: ") and current_code:
            mode = "MANUAL_SOURCE_BOUND" if (arc, current_code) in OVERRIDES else "SUBACT_EXPLICIT_OR_STRUCTURED"
            output.append(f"- `DESIRE_SOURCE_MODE`: `{mode}`")
    return "\n".join(output).rstrip() + "\n"


def build_outputs() -> dict[Path, str]:
    layer.source_field_pack = source_field_pack
    outputs = semantic.build_outputs()
    for path in list(outputs):
        match = re.match(r"ga(\d+)-collection-desire-subact-map-v1\.md$", path.name)
        if not match:
            continue
        arc = f"GA{int(match.group(1))}"
        outputs[path] = mark_source_mode(outputs[path], arc)
    # semantic balance must be measured after the final maps are marked; source
    # mode does not change set classification but regenerating the audit here
    # keeps one authoritative build path.
    outputs[semantic.SET_AUDIT] = semantic.set_audit_text(outputs)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = build_outputs()
    layer.write_or_check(outputs, args.check)
    audit = outputs[semantic.SET_AUDIT]
    if "Status: PASS — EXECUTION QC" not in audit:
        raise SystemExit("reader-desire finalizer produced failing set-family audit")
    print(f"reader_desire_manual_source_bound={len(OVERRIDES)}")
    print("reader_desire_finalizer=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
