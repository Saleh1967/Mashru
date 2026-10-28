import SLGE.Wad

/-!
# أبنيةُ اسمَي الفاعل والمفعول في الألفية (س594–607) والقطر (س358، س365)

**الطلب.** قولُ المالك 2026-10-28 (لفظُه ووقتُه، 00:33 بتوقيت عمّان، من ملخّص الجلسة بعد ضغطها): «يجب الاستفادة من ما لم نغطه وموجود في المراجع سواء
استنتجته انت او موجود في المرفق وعمل lean له شرط ان يكون متناسق ومتكامل ومترابط مع البرهان واالحساب وفق الدستور وأفضل الممارسات …
نفذ انت والوكلاء». واسما الفاعل والمفعول في Lean القائمة اسمان في جدول العوامل (`SLGE.Wad.amalF`، القطر L347) بلا حكمٍ على صوغهما؛ واختيارُ هذه
القطعة بعد الموصول، أوّلَ الصرف، ونطاقُها، قرارُ البنّاء.

**المصدر.** `alfiyya.txt` المختوم (`13b351a0…`) الأسطر 594–607 («أبنية الفاعلين والمفعولين»)، و`qatr.txt` المختوم (`2d9241be…`) السطران 358 و365
(مثالا الصوغ وحدهما). والاقتباساتُ في `asanid` قطعٌ حرفيّة، يفحصها `tahaqquq/test_abniya.py` على المودَعين موصولةَ الأسطر.

**المدخل** (حقولُ مواصفة الضابط المجمَّد `tahaqquq/dawabit/abniya/wasf.md` بأعيانها): بناءُ الماضي `Bina`، والتعدّي، والمطلوب (اسمُ الفاعل أو
اسمُ المفعول)، والصيغة `Sigha`. **والمدخلُ تحليلٌ يُعطى، لا مُخرَجُ قارئٍ من النصّ.**

**المخرج** `Jawab`: الحكم (`maqbul` أو `khata` أو `laHukm`)، والدرجةُ (`qiyas`، `awla`، `qalil`، `naql`، `bila`)؛ وحين لا يكون الحكمُ «مقبولًا»
فالدرجةُ `bila` (`ghayr_maqbul_bila`).

**الحكم** (`jawab`):
1. **اسمُ الفاعل من الثلاثيّ:**
   - «كفاعل صغ اسم فاعل إذا ... من ذي ثلاثة يكون كغذا» (س597): «فاعل» من فَعَلَ قياس، متعدّيًا أو لازمًا («غذا» فَعَلَ).
   - «وهو قليل في فعلت وفعل ... غير معدى» (س598): «فاعل» من فَعُلَ ومن فَعِلَ اللازم قليل؛ ومن فَعِلَ المتعدّي قياس (مفهومُ «غير معدى»).
   - «بل قياسه فعل» (س598) «وأفعل فعلان نحو أشر ... ونحو صديان ونحو الأجهر» (س599): «فَعِل» و«أفعل» و«فعلان» من فَعِلَ اللازم قياس.
   - «وفعل اولى وفعيل بفعل ... كالضخم والجميل» (س600): «فَعْل» و«فعيل» من فَعُلَ أولى؛ «وأفعل فيه قليل وفعل» (س601): «أفعل» و«فَعَل» منه قليل.
   - «وبسوى الفاعل قد يغنى فعل» (س601): لفَعَلَ صيغٌ غيرُ «فاعل» لا يسمّيها السطر، فالصفاتُ الستّ منه «لا حكم».
   - وما سوى ذلك خطأ: صيغةٌ لبناءٍ يذكر النطاقُ له غيرها.
2. **اسمُ الفاعل من غير الثلاثيّ:** «وزنة المضارع اسم فاعل ... من غير ذي الثلاث كالمواصل» «مع كسر متلو الأخير مطلقا ... وضم ميم زائد قد سبقا»
   (س602–603): «مضارع_بميم_مكسور» قياس، وما سواه خطأ.
3. **اسمُ المفعول:** «وإن فتحت منه ما كان انكسر ... صار اسم مفعول كمثل المنتظر» (س604): من غير الثلاثيّ «مضارع_بميم_مفتوح» قياس؛ «وفي اسم مفعول
   الثلاثي اطرد ... زنة مفعول كآت من قصد» (س605): من الثلاثيّ «مفعول» قياس؛ «وناب نقلا عنه ذو فعيل» (س606): «فعيل» من الثلاثيّ نقل؛ وما سوى
   ذلك خطأ.
4. والقطر: «واسم الفاعل كضارب ومكرم» (س358)، «واسم المفعول، كمضروب ومكرم» (س365) — أمثلةٌ بلا درجة، توافق الألفية فدرجتُها درجتُها (المواصفة).

**ما هو تعيينُ البنّاء** (لا نصُّ النطاق):
- «كغذا» فَعَلَ متعدّيًا أو لازمًا؛ و«فاعل» من فَعِلَ المتعدّي قياسٌ بمفهوم «غير معدى».
- «أفعل» و«فعلان» معطوفان على «فَعِل» قياسًا لفَعِلَ اللازم؛ و«والفعل جمل» فعلُ «الجميل» لا صيغةٌ جديدة.
- «قد يغنى» بلا تسميةٍ للصيغ «لا حكم» في الصفات الستّ من فَعَلَ؛ وفي «مفعول» و«المضارع بميم» منه خطأ.
- اسمُ المفعول من الثلاثيّ لا يقيّده النطاقُ بالتعدّي، ففيه اللازمُ والمتعدّي سواء؛ و«فعيل» نقلًا للثلاثيّ وحده («عنه»: عن «مفعول» الثلاثيّ).
- فَعُلَ في الحقل `taaddi` لا يغيّر شيئًا، والتعدّي لا يغيّر إلّا فَعِلَ (`taaddi_la_yughayyir`).

**الصلة بقطع Lean القائمة:**
- `amal_wad`: المطلوبان «اسم الفاعل» و«اسم المفعول» في `SLGE.Wad.amalF` (ما يعمل عمل فعله، القطر L347).

**المنهج.** شفرةُ هذا الملفّ كُتبت قبل أن يقرأ البنّاءُ حالاتِ الضابط، وجُمّدت الحالاتُ قبلها (`tahaqquq/dawabit/abniya/tajmid.json`؛
`hawkama/منهج_الضوابط.md`). ونتيجتُها على الضابط في `Jisr/AbniyaQiyas.lean`، لا هنا.

**المبرهنات** (بالمعيار الموحَّد في `Nizam/Asas.lean`)، وهي خواصُّ هذا التعيين على مجاله، لا قوانينُ في اللغة:
- تعريفيّة (7): `ghayr_thulathi_fail`، `ghayr_thulathi_mafool`، `mafool_thulathi`، `fail_min_fataha`، `taaddi_la_yughayyir`، `fail_mafool_la_yashtarikan`،
  `ghayr_maqbul_bila`. وبرهانُها فكُّ التعريفات وتفكيكُ الحالات.
- على الشاهد (2): `amal_wad`، `shawahid`.

**حدُّه.** المدخلُ تحليلٌ يُعطى؛ ولا صيغَ للمبالغة ولا للصفة المشبهة ولا لعملهما؛ ولا معنى للفعل (العيوبُ والألوانُ في «أشر» و«الأجهر» أمثلةٌ لا
شروط)؛ ولا وصلَ بقانون الجذر (`SLGE.Root`) ولا بالقارئ ولا بالمحرّك.
-/

namespace Jisr
namespace Abniya

/-- بناءُ الماضي. -/
inductive Bina | fataha | kasra | damma | ghayrThulathi
  deriving DecidableEq, Repr

inductive Taaddi | mutaaddi | lazim
  deriving DecidableEq, Repr

inductive Matlub | fail | mafool
  deriving DecidableEq, Repr

/-- الصيغة. -/
inductive Sigha
  | faail | faiil_k | afal | falan | fal_s | faiil | faal_f | mafuul | mudariMaksur | mudariMaftuh
  deriving DecidableEq, Repr

structure Dakhil where
  bina : Bina
  taaddi : Taaddi
  matlub : Matlub
  sigha : Sigha
  deriving DecidableEq, Repr

inductive Hukm | maqbul | khata | laHukm
  deriving DecidableEq, Repr

inductive Daraja | qiyas | awla | qalil | naql | bila
  deriving DecidableEq, Repr

structure Jawab where
  hukm : Hukm
  daraja : Daraja
  deriving DecidableEq, Repr

def maqbulJ (d : Daraja) : Jawab := ⟨.maqbul, d⟩
def khataJ : Jawab := ⟨.khata, .bila⟩
def laHukmJ : Jawab := ⟨.laHukm, .bila⟩

/-- الصفاتُ الستّ (صيغُ الثلاثيّ غيرُ «فاعل» و«مفعول»). -/
def Sigha.sifa : Sigha → Bool
  | .faiil_k | .afal | .falan | .fal_s | .faiil | .faal_f => true
  | _ => false

/-- اسمُ الفاعل من الثلاثيّ. -/
def failThulathi (b : Bina) (t : Taaddi) (s : Sigha) : Jawab :=
  match b, s with
  | .fataha, .faail => maqbulJ .qiyas
  | .fataha, s => if s.sifa then laHukmJ else khataJ
  | .kasra, .faail => if t = .mutaaddi then maqbulJ .qiyas else maqbulJ .qalil
  | .kasra, .faiil_k | .kasra, .afal | .kasra, .falan => if t = .lazim then maqbulJ .qiyas else khataJ
  | .damma, .faail => maqbulJ .qalil
  | .damma, .fal_s | .damma, .faiil => maqbulJ .awla
  | .damma, .afal | .damma, .faal_f => maqbulJ .qalil
  | _, _ => khataJ

/-- **الحكم.** -/
def jawab (d : Dakhil) : Jawab :=
  match d.matlub, d.bina with
  | .fail, .ghayrThulathi => if d.sigha = .mudariMaksur then maqbulJ .qiyas else khataJ
  | .fail, b => failThulathi b d.taaddi d.sigha
  | .mafool, .ghayrThulathi => if d.sigha = .mudariMaftuh then maqbulJ .qiyas else khataJ
  | .mafool, _ =>
    match d.sigha with
    | .mafuul => maqbulJ .qiyas
    | .faiil => maqbulJ .naql
    | _ => khataJ

/-! ## الأسانيد -/

/-- الأسانيد: (القاعدة، المصدر، من سطر، إلى سطر، القطعةُ حرفيّةً بعد وصل الأسطر بمسافة). -/
def asanid : List (String × String × Nat × Nat × String) :=
  [("faail", "alfiyya", 597, 597, "كفاعل صغ اسم فاعل إذا ... من ذي ثلاثة يكون كغذا"),
   ("qalil_faail", "alfiyya", 598, 598, "وهو قليل في فعلت وفعل ... غير معدى بل قياسه فعل"),
   ("kasra_lazim", "alfiyya", 599, 599, "وأفعل فعلان نحو أشر ... ونحو صديان ونحو الأجهر"),
   ("damma", "alfiyya", 600, 600, "وفعل اولى وفعيل بفعل ... كالضخم والجميل والفعل جمل"),
   ("damma_qalil", "alfiyya", 601, 601, "وأفعل فيه قليل وفعل ... وبسوى الفاعل قد يغنى فعل"),
   ("ghayr_thulathi", "alfiyya", 602, 603, "وزنة المضارع اسم فاعل ... من غير ذي الثلاث كالمواصل مع كسر متلو الأخير مطلقا ... وضم ميم زائد قد سبقا"),
   ("mafool_ghayr", "alfiyya", 604, 604, "وإن فتحت منه ما كان انكسر ... صار اسم مفعول كمثل المنتظر"),
   ("mafool_thulathi", "alfiyya", 605, 605, "وفي اسم مفعول الثلاثي اطرد ... زنة مفعول كآت من قصد"),
   ("faiil_naql", "alfiyya", 606, 606, "وناب نقلا عنه ذو فعيل ... نحو فتاة أو فتى كحيل"),
   ("qatr_fail", "qatr", 358, 358, "واسم الفاعل كضارب ومكرم."),
   ("qatr_mafool", "qatr", 365, 365, "واسم المفعول، كمضروب ومكرم.")]

/-! ## المبرهنات -/

/-- **اسمُ الفاعل من غير الثلاثيّ** زنةُ المضارع بميمٍ وكسرِ ما قبل الآخر، قياسًا، وما سواها خطأ. -/
theorem ghayr_thulathi_fail (t : Taaddi) (s : Sigha) :
    jawab ⟨.ghayrThulathi, t, .fail, s⟩ = (if s = .mudariMaksur then maqbulJ .qiyas else khataJ) := by
  rfl

/-- **اسمُ المفعول من غير الثلاثيّ** بفتحه، قياسًا، وما سواها خطأ. -/
theorem ghayr_thulathi_mafool (t : Taaddi) (s : Sigha) :
    jawab ⟨.ghayrThulathi, t, .mafool, s⟩ = (if s = .mudariMaftuh then maqbulJ .qiyas else khataJ) := by
  rfl

/-- **اسمُ المفعول من الثلاثيّ** «مفعول» قياسًا و«فعيل» نقلًا، أيًّا كان البناءُ والتعدّي، وما سواهما خطأ. -/
theorem mafool_thulathi (b : Bina) (t : Taaddi) (s : Sigha) (hb : b ≠ .ghayrThulathi) :
    jawab ⟨b, t, .mafool, s⟩ = (if s = .mafuul then maqbulJ .qiyas else if s = .faiil then maqbulJ .naql else khataJ) := by
  cases b <;> cases s <;> simp_all [jawab]

/-- **«فاعل» من فَعَلَ قياس**، متعدّيًا أو لازمًا. -/
theorem fail_min_fataha (t : Taaddi) : jawab ⟨.fataha, t, .fail, .faail⟩ = maqbulJ .qiyas := by
  rfl

/-- **التعدّي لا يغيّر الجوابَ إلّا في فَعِلَ.** -/
theorem taaddi_la_yughayyir (d : Dakhil) (t : Taaddi) (h : d.bina ≠ .kasra) :
    jawab { d with taaddi := t } = jawab d := by
  obtain ⟨b, t0, m, s⟩ := d
  cases b <;> cases m <;> cases s <;> simp_all [jawab, failThulathi]

/-- **لا صيغةَ تُقبل لاسم الفاعل واسم المفعول معًا من بناءٍ واحدٍ وتعدٍّ واحد**، إلّا «فعيل» من فَعُلَ (أولى فاعلًا، ونقلًا مفعولًا). -/
theorem fail_mafool_la_yashtarikan (b : Bina) (t : Taaddi) (s : Sigha)
    (h1 : (jawab ⟨b, t, .fail, s⟩).hukm = .maqbul) (h2 : (jawab ⟨b, t, .mafool, s⟩).hukm = .maqbul) :
    b = .damma ∧ s = .faiil := by
  cases b <;> cases t <;> cases s <;> simp_all [jawab, failThulathi, maqbulJ, khataJ, laHukmJ, Sigha.sifa]

/-- **ما ليس مقبولًا فدرجتُه `bila`.** -/
theorem ghayr_maqbul_bila (d : Dakhil) (h : (jawab d).hukm ≠ .maqbul) : (jawab d).daraja = .bila := by
  obtain ⟨b, t, m, s⟩ := d
  cases b <;> cases t <;> cases m <;> cases s <;> simp_all [jawab, failThulathi, maqbulJ, khataJ, laHukmJ, Sigha.sifa]

/-! ## الصلة بـ SLGE -/

/-- **المطلوبان في جدول ما يعمل عمل فعله** (`SLGE.Wad.amalF`، القطر L347). -/
theorem amal_wad :
    (SLGE.Wad.amalF.map (·.1)).contains "اسم الفاعل" = true ∧ (SLGE.Wad.amalF.map (·.1)).contains "اسم المفعول" = true := by
  decide

/-- **الشواهد** (تحليلُ البنّاء لأمثلة النطاق). -/
theorem shawahid :
    jawab ⟨.fataha, .mutaaddi, .fail, .faail⟩ = maqbulJ .qiyas ∧            -- غذا: غاذٍ؛ وضرب: ضارب
    jawab ⟨.kasra, .lazim, .fail, .faiil_k⟩ = maqbulJ .qiyas ∧              -- أشر
    jawab ⟨.kasra, .lazim, .fail, .falan⟩ = maqbulJ .qiyas ∧                -- صديان
    jawab ⟨.kasra, .lazim, .fail, .afal⟩ = maqbulJ .qiyas ∧                 -- الأجهر
    jawab ⟨.kasra, .lazim, .fail, .faail⟩ = maqbulJ .qalil ∧
    jawab ⟨.kasra, .mutaaddi, .fail, .faail⟩ = maqbulJ .qiyas ∧
    jawab ⟨.kasra, .mutaaddi, .fail, .faiil_k⟩ = khataJ ∧
    jawab ⟨.damma, .lazim, .fail, .fal_s⟩ = maqbulJ .awla ∧                 -- الضخم
    jawab ⟨.damma, .lazim, .fail, .faiil⟩ = maqbulJ .awla ∧                 -- الجميل
    jawab ⟨.damma, .lazim, .fail, .afal⟩ = maqbulJ .qalil ∧
    jawab ⟨.damma, .lazim, .fail, .faail⟩ = maqbulJ .qalil ∧
    jawab ⟨.damma, .lazim, .fail, .falan⟩ = khataJ ∧
    jawab ⟨.fataha, .lazim, .fail, .faiil⟩ = laHukmJ ∧
    jawab ⟨.fataha, .mutaaddi, .fail, .faal_f⟩ = laHukmJ ∧
    jawab ⟨.fataha, .lazim, .fail, .mafuul⟩ = khataJ ∧
    jawab ⟨.ghayrThulathi, .mutaaddi, .fail, .mudariMaksur⟩ = maqbulJ .qiyas ∧    -- المواصل؛ ومكرم
    jawab ⟨.ghayrThulathi, .mutaaddi, .fail, .faail⟩ = khataJ ∧
    jawab ⟨.ghayrThulathi, .mutaaddi, .mafool, .mudariMaftuh⟩ = maqbulJ .qiyas ∧  -- المنتظر؛ ومكرم
    jawab ⟨.ghayrThulathi, .mutaaddi, .mafool, .faiil⟩ = khataJ ∧
    jawab ⟨.fataha, .mutaaddi, .mafool, .mafuul⟩ = maqbulJ .qiyas ∧         -- مقصود؛ ومضروب
    jawab ⟨.fataha, .mutaaddi, .mafool, .faiil⟩ = maqbulJ .naql ∧           -- كحيل
    jawab ⟨.fataha, .mutaaddi, .mafool, .faail⟩ = khataJ := by
  decide

end Abniya
end Jisr
