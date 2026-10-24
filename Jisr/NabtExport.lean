import Jisr.Nabt
import Lean

/-!
Executable view of the actual native bridge definitions. This is a finite
conformance export, not an Arabic acquisition evaluation. Cell offsets are
declared cell offsets; no raw UTF-8 or Unicode alignment is inferred here.
-/

open Lean

namespace Jisr.NabtExport

open Jisr.NabtBridge

def cellRow (nativeAtom : Fin 116) : Json :=
  let native := Dal.fakk nativeAtom
  let canonicalAtom := cellToNabt native
  let canonical := Nabt.Cell.decode canonicalAtom
  Json.mkObj [
    ("mashru_atom", toJson nativeAtom.val),
    ("mashru_carrier_index", toJson native.hamil.val),
    ("mark", toJson native.hala.val),
    ("carrier", toJson (String.singleton (Dal.harf native.hamil))),
    ("nabt_atom", toJson canonicalAtom.val),
    ("nabt_carrier_index", toJson canonical.carrier.val),
    ("nabt_carrier", toJson (Nabt.canonicalCarriers.getD canonical.carrier.val "")),
    ("roundtrip_mashru_atom", toJson (Dal.n (cellFromNabt canonicalAtom)).val),
    ("roundtrip_nabt_atom", toJson (cellToNabt (cellFromNabt canonicalAtom)).val)]

def statusLabel : Nabt.LicensedDerivation.Status → String
  | .invalid => "INVALID"
  | .pending => "PENDING"
  | .conditionalLicensed => "CONDITIONAL_LICENSED"
  | .rejected => "REJECTED"

def nativeCase (name : String) (tree : NativeTree) : Json :=
  let report := Nabt.LicensedDerivation.assess exampleContext tree
  Json.mkObj [
    ("name", toJson name),
    ("status", toJson (statusLabel report.status)),
    ("conflict", toJson report.conflict)]

def methodLabel : Mawsua.Tariqa → String
  | .aqliyya => "aqliyya"
  | .ilmiyya => "ilmiyya"

def inquiryRow (method : Mawsua.Tariqa) (requested evidence : Mawsua.Wasm) : Json :=
  let checked := inquiryChecks exampleChecks requested evidence method
  let result := assessInquiry exampleChecks requested evidence method
  Json.mkObj [
    ("method", toJson (methodLabel method)),
    ("requested_rank", toJson requested.quwwa),
    ("evidence_rank", toJson evidence.quwwa),
    ("method_evidence_rank", toJson checked.evidenceRank),
    ("verdict", toJson result.verdict.label),
    ("authorized_rank", toJson result.authorizedRank)]

def inquiryRows : List Json :=
  ([.aqliyya, .ilmiyya] : List Mawsua.Tariqa).flatMap fun method =>
    Mawsua.Wasm.tartib.flatMap fun requested =>
      Mawsua.Wasm.tartib.map fun evidence => inquiryRow method requested evidence

def sourceRow : Json :=
  let canonical := sourceToNabt exampleSource
  let span : Nabt.UnitDiscovery.Span := ⟨17, 1, 2, 3, 1, 3⟩
  Json.mkObj [
    ("source_id", toJson canonical.sourceId),
    ("revision", toJson canonical.revision),
    ("scope_id", toJson canonical.scopeId),
    ("atomization_id", toJson canonical.atomizationId),
    ("coordinate_unit", toJson "declared_cell"),
    ("native_atoms", toJson (exampleSource.atoms.map (fun cell => (Dal.n cell).val))),
    ("canonical_atoms", toJson (canonical.atoms.map Fin.val)),
    ("restored_native_atoms", toJson
      ((sourceFromNabt canonical).atoms.map (fun cell => (Dal.n cell).val))),
    ("span_start", toJson span.start),
    ("span_stop", toJson span.stop),
    ("native_span_valid", toJson (Nabt.UnitDiscovery.validSpan exampleSource span)),
    ("canonical_span_valid", toJson (Nabt.UnitDiscovery.validSpan canonical span)),
    ("native_span_atoms", toJson
      ((Nabt.UnitDiscovery.spanAtoms exampleSource span).map (fun cell => (Dal.n cell).val))),
    ("canonical_span_atoms", toJson
      ((Nabt.UnitDiscovery.spanAtoms canonical span).map Fin.val))]

def report : Json :=
  let meaningResult := reviewMeaning exampleChecks .mafhus .mafhus .aqliyya
    [] 7 [⟨"unregistered-source", 0⟩]
  Json.mkObj [
    ("schema_version", toJson (1 : Nat)),
    ("bridge_id", toJson "mashru.nabt.bridge.v1"),
    ("scope", toJson "declared_cell_representation_and_conditional_evidence"),
    ("cell_count", toJson (116 : Nat)),
    ("cells", toJson ((List.finRange 116).map cellRow)),
    ("source", sourceRow),
    ("native_cases", toJson [
      nativeCase "source_atom" exampleFirst,
      nativeCase "join_without_evidence" (.join exampleTag exampleFirst exampleSecond),
      nativeCase "filtered_source_gap" (.join exampleTag exampleFirst exampleThird),
      nativeCase "same_ids_changed_content"
        (.atom { exampleSource with atoms := [⟨8, 0⟩] } [] ⟨8, 0⟩ [])]),
    ("inquiry_cases", toJson inquiryRows),
    ("inquiry_case_count", toJson inquiryRows.length),
    ("empty_world_registry", Json.mkObj [
      ("inquiry_verdict", toJson meaningResult.1.verdict.label),
      ("meaning_status", toJson meaningResult.2.ism),
      ("sealed_world_witness_added", toJson false)])]

end Jisr.NabtExport

def main (args : List String) : IO UInt32 := do
  if !args.isEmpty then
    IO.eprintln "Usage: nabtBridge (no arguments); emits the finite native bridge conformance view."
    return 2
  IO.println Jisr.NabtExport.report.compress
  return 0
