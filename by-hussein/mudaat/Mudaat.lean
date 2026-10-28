/- by-hussein/mudaat/Mudaat.lean — مولَّدٌ من مودَعات RATIFIED (D5) و RATIFIED_BY_RULE (D6). يُفحَص قائمًا بذاته. -/
import Jisr.Utur
namespace Mudaat
open Jisr.Utur SLGE.Awwalan Dal

def kataba_m : Madlul := { haqiqa := 1001, khawass := [], alaqat := [], qabiliyyat := [], afrad := [], tim := true, ind := true }   -- كَتَبَ (RATIFIED)
def kataba_mK : Kalima := ⟨[32, 72, 104], false, false⟩
def talib_m : Madlul := { haqiqa := 1002, khawass := [], alaqat := [], qabiliyyat := [1001], afrad := [], tim := false, ind := true }   -- الطَّالِبُ (RATIFIED)
def talib_mK : Kalima := ⟨[67, 64, 11, 54, 105], true, true⟩
def dars_m : Madlul := { haqiqa := 1003, khawass := [], alaqat := [], qabiliyyat := [], afrad := [], tim := false, ind := true }   -- الدَّرْسَ (RATIFIED)
def dars_mK : Kalima := ⟨[71, 68, 63, 80], true, true⟩

end Mudaat
