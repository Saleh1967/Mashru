/- Tabaqat4 — مولَّد آليًّا لـ «ذَهَبَ وَلَدٌ» ؛ قالب Shahid_Ahmad.lean ؛ pass 2. Mashru يُستورَد ولا يُعدَّل. -/
import Jisr.Utur
import Aql.Isnad

namespace Tabaqat4
open Jisr.Utur Aql.Isnad Aql.Mirsat Aql.Azmina Aql.Makan

def jumla3 : Itar3 :=
  { jisr := { ud := Jisr.Mulhaqat.jaaRajul }, kalimat := [⟨[92, 4, 104], false, false⟩, ⟨[112, 52, 69, 59], false, false⟩], maani := [dhahab, walad],
    isnad := ⟨walad, .qabiliyya 10, .isnadiyya⟩ }

def mirsat : Mirsat := ⟨0, ⟨0, 0, 0⟩⟩
def dhat : Dhat := ⟨20, none⟩
def arad : Arad := .fiil 10 (-1) .saa none
def jumla4 : Jumla := .sughra dhat arad

theorem tabaqa1_kalimat : jumla3.kalimat = [⟨[92, 4, 104], false, false⟩, ⟨[112, 52, 69, 59], false, false⟩] := by decide
theorem tabaqa2_maani : jumla3.maani = [dhahab, walad] ∧ dhahab.tim = true := by decide
theorem tabaqa3_hukm : hukm3 jumla3 = .murakhkhas := by decide +kernel
theorem tabaqa3_isnad : jumla3.isnad = ⟨walad, .qabiliyya 10, .isnadiyya⟩ := by decide
theorem tabaqa4_ajza : (ajza jumla4).map rutba = [.mahkum, .hakim] := by decide
theorem tabaqa4_kalam : yastaghni jumla4 = true := by decide
theorem tabaqa4_zaman : zamanArad mirsat arad = some .madi := by decide
theorem tabaqa4_mawdi : mawdiInda mirsat jumla4 = ⟨0, 0, 0⟩ := by decide
theorem tabaqa4_thabat : zamanArad ⟨mirsat.an + 5, mirsat.huna⟩ (arad.naql 5) = zamanArad mirsat arad :=
  thabat_naql_arad mirsat 5 ⟨0, 0, 0⟩ arad
#print axioms Tabaqat4.tabaqa1_kalimat
#print axioms Tabaqat4.tabaqa2_maani
#print axioms Tabaqat4.tabaqa3_hukm
#print axioms Tabaqat4.tabaqa3_isnad
#print axioms Tabaqat4.tabaqa4_ajza
#print axioms Tabaqat4.tabaqa4_kalam
#print axioms Tabaqat4.tabaqa4_zaman
#print axioms Tabaqat4.tabaqa4_mawdi
#print axioms Tabaqat4.tabaqa4_thabat

end Tabaqat4
