/-
  Aql/WaqiShawahid.lean — شواهدُ الحكم على الدفعة الأولى من «الواقع المختوم» (`Aql/WaqiJadwal.lean`، مولَّدٌ من waqi_001.tsv).

  كلُّها «على الشاهد» (`decide +kernel` على الجدول المولَّد)، بالمعيار الموحَّد في `Nizam/Asas.lean`: 9 مبرهنات.
  * `adad`: 48 مشاهدة، 21 قياسًا و27 حكاية؛ و`ihsa`: على القضايا المتمايزة (44) مفهومٌ 21 ومعلومةٌ 23، ولا «لا حكم» (كلُّ قضيّةٍ مأخوذةٌ من صفّ).
  * `python_yahsub`: بايثون يُخرج 5 لـ print(2+3) — قياسٌ بالتشغيل، فمفهوم.
  * `lean_yaqbal_wa_yarud`: Lean يقبل «2 + 3 = 5» (خروج 0) ويردّ «2 + 3 = 6» (خروج 1) — قياسان، فمفهومان.
  * `basma_bihassatayn`: بصمةُ CLAUDE.md بحاسّتين (sha256sum وhashlib) متطابقتين — مفهوم.
  * `lean_isdar_mutawatir`: إصدارُ Lean 4.34.1 بحكاياتٍ من ثلاثة مصادر (lean-toolchain، lean، lake) — مفهومٌ بالتواتر (حدُّه اثنان، تعيين).
  * `python_isdar_tikrar`: إصدارُ بايثون بحكايتين من مصدرٍ واحد (python3 نفسه) — معلومة: التكرارُ لا يرفع.
  * `github_hikaya`: ما يرويه GitHub وحده (الفرع الافتراضيّ main) — معلومة؛ و`bila_mushahada`: «master» لا حكم، لا «ممتنع».
  * `jisr_haqiqi`: لو خُتم الجدولُ ببصمته «واقعًا مختومًا» ارتفع معنى «بايثون يُخرج 5» في `Maratib` إلى «مفهوم»، ولو سُجّل بالبصمة
    نفسها «معلوماتٍ سابقة» بقي «معلومة»؛ وهو اليوم مرشّح، فلا قيدَ له في سجلّ الفاحص (`Waqi.murashshah_la_yarfa`).
  بلا sorry ولا axiom ولا native_decide.
-/
import Aql.WaqiJadwal

namespace Waqi.Shawahid

open Waqi Waqi.Jadwal

/-- القضايا المتمايزة في الجدول. -/
def qadaya : List (String × String × String) := (jadwal.map fun r => (r.mawdu, r.sifa, r.qima)).eraseDups

def hukmQ (k : String × String × String) : Hukm := hukm jadwal k.1 k.2.1 k.2.2

theorem adad :
    jadwal.length = 48 ∧ (jadwal.filter (·.wajh == .qiyas)).length = 21 ∧
    (jadwal.filter (·.wajh == .hikaya)).length = 27 := by decide +kernel

theorem ihsa :
    qadaya.length = 44 ∧ (qadaya.map hukmQ).count .mafhum = 21 ∧ (qadaya.map hukmQ).count .maaluma = 23 ∧
    (qadaya.map hukmQ).count .laHukm = 0 := by decide +kernel

theorem python_yahsub : hukm jadwal "Python" "يُخرج لـ print(2+3)" "5" = .mafhum := by decide +kernel

theorem lean_yaqbal_wa_yarud :
    hukm jadwal "Lean" "رمزُ الخروج لـ «example : 2 + 3 = 5 := by decide»" "0" = .mafhum ∧
    hukm jadwal "Lean" "رمزُ الخروج لـ «example : 2 + 3 = 6 := by decide»" "1" = .mafhum := by decide +kernel

theorem basma_bihassatayn :
    hukm jadwal "ملفّ:CLAUDE.md@2608833" "بصمة sha256"
      "9579ffeab4b3caeb2a5989c7a73be043c2b594e5e6a5695abd47fef363faeb93" = .mafhum ∧
    (mutabiq jadwal "ملفّ:CLAUDE.md@2608833" "بصمة sha256"
      "9579ffeab4b3caeb2a5989c7a73be043c2b594e5e6a5695abd47fef363faeb93").map (·.hassa) = ["sha256sum", "python3-hashlib"] := by
  decide +kernel

theorem lean_isdar_mutawatir :
    hukm jadwal "Lean" "الإصدار" "4.34.1" = .mafhum ∧ fiihiQiyas (mutabiq jadwal "Lean" "الإصدار" "4.34.1") = false ∧
    (mutabiq jadwal "Lean" "الإصدار" "4.34.1").map (·.masdar) =
      ["lean-toolchain (ملفّ المستودع)", "lean (الأداة نفسها)", "lake (الأداة نفسها)"] := by decide +kernel

theorem python_isdar_tikrar :
    hukm jadwal "Python" "الإصدار" "3.13.16" = .maaluma ∧
    (mutabiq jadwal "Python" "الإصدار" "3.13.16").length = 2 := by decide +kernel

theorem github_hikaya :
    hukm jadwal "مستودع:Mashru" "الفرع الافتراضيّ" "main" = .maaluma ∧
    hukm jadwal "مستودع:Mashru" "الفرع الافتراضيّ" "master" = .laHukm := by decide +kernel

theorem jisr_haqiqi :
    (Maratib.martabatMaana 0 (Maratib.shuhudMutabara [(basma, .waqiMakhtum)]
      (shuhud basma jadwal "Python" "يُخرج لـ print(2+3)" "5"))).ism = "مفهوم" ∧
    (Maratib.martabatMaana 0 (Maratib.shuhudMutabara [(basma, .maalumatSabiqa)]
      (shuhud basma jadwal "Python" "يُخرج لـ print(2+3)" "5"))).ism = "معلومة" := by decide +kernel

end Waqi.Shawahid
