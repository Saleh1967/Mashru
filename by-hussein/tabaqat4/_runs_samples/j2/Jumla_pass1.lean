/- Tabaqat4 — باب الجزاء ؛ مولَّد آليًّا ؛ pass 1. Mashru يُستورَد ولا يُعدَّل. -/
import Jisr.BabJaza

namespace Tabaqat4
open Jisr.BabJaza

def j : Jumla := ⟨"إن", .shartAwwalan, false, .mudariMajzum, .mudariMarfu⟩

#eval (hukm j).kalam
#eval (hukm j).shir
#eval sinfOf j.adat

end Tabaqat4
