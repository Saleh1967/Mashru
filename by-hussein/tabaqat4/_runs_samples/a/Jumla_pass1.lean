/- Tabaqat4 — مولَّد آليًّا لـ «ذَهَبَ الْوَلَدُ» ؛ قالب Shahid_Ahmad.lean ؛ pass 1. Mashru يُستورَد ولا يُعدَّل. -/
import Jisr.Utur
import Aql.Isnad

namespace Tabaqat4
open Jisr.Utur Aql.Isnad Aql.Mirsat Aql.Azmina Aql.Makan

def jumla3 : Itar3 :=
  { jisr := { ud := Jisr.Mulhaqat.darabaZayd }, kalimat := [⟨[92, 4, 104], false, false⟩, ⟨[55, 112, 52, 69], true, true⟩], maani := [dhahab, walad],
    isnad := ⟨walad, .qabiliyya 10, .isnadiyya⟩ }

def mirsat : Mirsat := ⟨0, ⟨0, 0, 0⟩⟩
def dhat : Dhat := ⟨20, none⟩
def arad : Arad := .fiil 10 (-1) .saa none
def jumla4 : Jumla := .sughra dhat arad

#eval hukm3 jumla3
#eval ibtida3 jumla3
#eval (Dal.rakkib jumla3.kalimat).silsila
#eval (ajza jumla4).map rutba
#eval yastaghni jumla4
#eval zamanArad mirsat arad
#eval mawdiInda mirsat jumla4

end Tabaqat4
