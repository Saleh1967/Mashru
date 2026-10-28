/- Tabaqat4 — مولَّد آليًّا لـ «كَتَبَ الطَّالِبُ الدَّرْسَ» ؛ قالب Shahid_Ahmad.lean ؛ pass 1. Mashru يُستورَد ولا يُعدَّل. -/
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

#eval hukm3 jumla3
#eval ibtida3 jumla3
#eval (Dal.rakkib jumla3.kalimat).silsila
#eval (ajza jumla4).map rutba
#eval yastaghni jumla4
#eval zamanArad mirsat arad
#eval mawdiInda mirsat jumla4

end Tabaqat4
