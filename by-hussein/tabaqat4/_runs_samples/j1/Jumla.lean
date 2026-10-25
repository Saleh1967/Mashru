/- Tabaqat4 — باب الجزاء ؛ مولَّد آليًّا ؛ pass 2. Mashru يُستورَد ولا يُعدَّل. -/
import Jisr.BabJaza

namespace Tabaqat4
open Jisr.BabJaza

def j : Jumla := ⟨"إن", .shartAwwalan, false, .mudariMajzum, .mudariMajzum⟩

theorem jaza_hukm : hukm j = ⟨.maqbul, .maqbul⟩ := by decide
theorem jaza_sinf : sinfOf j.adat = .jaza := by decide
#print axioms Tabaqat4.jaza_hukm
#print axioms Tabaqat4.jaza_sinf

end Tabaqat4
