/- Tabaqat4 — مولَّد آليًّا لـ «كَتَبَ الطَّالِبُ الدَّرْسَ» ؛ قالب Shahid_Ahmad.lean ؛ pass 2. Mashru يُستورَد ولا يُعدَّل. -/
import Jisr.Utur
import Aql.Isnad

namespace Tabaqat4
open Jisr.Utur Aql.Isnad SLGE.Awwalan Dal Aql.Mirsat Aql.Azmina Aql.Makan

def kataba_m : Madlul := { haqiqa := 1001, khawass := [], alaqat := [], qabiliyyat := [], afrad := [], tim := true, ind := true }   -- مودَع مالك مضمَّن (OWNER_MUDAA)
def talib_m : Madlul := { haqiqa := 1002, khawass := [], alaqat := [], qabiliyyat := [1001], afrad := [], tim := false, ind := true }   -- مودَع مالك مضمَّن (OWNER_MUDAA)
def dars_m : Madlul := { haqiqa := 1003, khawass := [], alaqat := [], qabiliyyat := [], afrad := [], tim := false, ind := true }   -- مودَع مالك مضمَّن (OWNER_MUDAA)

def jumla3 : Itar3 :=
  { jisr := { ud := Jisr.Mulhaqat.daraba }, kalimat := [⟨[32, 72, 104], false, false⟩, ⟨[67, 64, 11, 54, 105], true, true⟩, ⟨[71, 68, 63, 80], true, true⟩], maani := [kataba_m, talib_m, dars_m],
    isnad := ⟨talib_m, .qabiliyya 1001, .isnadiyya⟩ }

def mirsat : Mirsat := ⟨0, ⟨0, 0, 0⟩⟩
def dhat : Dhat := ⟨1002, none⟩
def arad : Arad := .fiil 1001 (-1) .saa (some ⟨1003, none⟩)
def jumla4 : Jumla := .sughra dhat arad

theorem tabaqa1_kalimat : jumla3.kalimat = [⟨[32, 72, 104], false, false⟩, ⟨[67, 64, 11, 54, 105], true, true⟩, ⟨[71, 68, 63, 80], true, true⟩] := by decide
theorem tabaqa2_maani : jumla3.maani = [kataba_m, talib_m, dars_m] ∧ kataba_m.tim = true := by decide
theorem tabaqa3_hukm : hukm3 jumla3 = .murakhkhas := by decide +kernel
theorem tabaqa3_isnad : jumla3.isnad = ⟨talib_m, .qabiliyya 1001, .isnadiyya⟩ := by decide
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
