/-
  Aql/Waqi.lean — جدولُ «الواقع المختوم»: المشاهدةُ صفًّا، والحكمُ الثلاثيُّ عليها، وقانونُ النموّ.

  **القرار.** قولُ المالك في الجلسة (2026-10-22، 01:57 بتوقيت عمّان): «اعطيني وفق الدستور جدولا قابلة للنمو وفق المعلومات
  السابقة المنظمة الاولية يكون نواة للتوسع التلقائي بالتعلم … جدول الواقع المختوم من الأساس ما هو الوكيل وما هو جيت هب وما
  هوmashru وما مكوناته وما تعريفاته وما إطار عمله وكيف تتم عملياته وما هو بايثون وما هو الدستور». وصوغُ المشاهدة ووجهيها
  والحكمِ عليها وحدِّ الاستقلال تعيينُ البنّاء (يُعرض على المالك).

  **السند** (الدستور كما في `CLAUDE.md` ودستور الوكيل):
  * م12: لا مودَع بلا نوع، والأنواعُ أربعة: واقعٌ مختوم، وضع، معلوماتٌ سابقة، مرجعٌ محجوب (`Idaa.Naw`).
  * م14: الأركانُ الأربعة: الواقع (مودَعٌ مختوم ببصمته)، والحسّ (مدخلٌ ينقله بلا تخمين)، والمعلوماتُ السابقة، والدماغ.
  * م15–م16: «مفهوم» معنًى له واقعٌ مودَعٌ مشهود — محسوسٌ في الواقع المختوم، أو مسلَّمٌ به بتواتر شهودٍ مستقلّين؛ ولا يرفع
    التكرارُ معلومةً إلى مفهوم؛ والغيابُ ليس امتناعًا (`Maratib.la_mafhum_bila_waqi`، `Maratib.takrar_la_yarfa`).

  **التعيين** (رأي البنّاء):
  * الحاسّةُ أداةٌ مسجَّلةٌ بأمرها الحرفيّ (الحسّ في م14)، والمشاهدةُ صفٌّ: الحاسّة، ومصدرُ ما نقلته، والشيء، والخاصّة،
    والقيمة كما خرجت، ووجهُها. وفي المودَع معها بصمةُ المخرج الخامّ ووقتُ المشاهدة (لا تدخل الحكمَ هنا).
  * **وجهان:** «قياس» ما حسبته الحاسّةُ من البايتات أو شوهد من تشغيلٍ أُجري (بصمةُ ملفّ، مخرجُ أمرٍ شُغِّل)؛ و«حكاية» ما
    يرويه مصدرٌ عن نفسه أو عن غيره (وصفُ أداةٍ نفسَها، بياناتُ مستودعٍ يرويها خادمُه). وهو على هيئة الحكاية والمضمون في
    `Idaa.Wajh` (ج3 729)، لا هو بعينه.
  * **الحكم** على قضيّةٍ (شيء، خاصّة، قيمة): «مفهوم» إن طابقها قياس، أو حكايتان من مصدرين مختلفين (حدُّ الاستقلال اثنان،
    كـ `Hawass.tasdiq` — تعيينٌ)؛ و«معلومة» إن طابقها ما دون ذلك؛ و«لا حكم» إن لم يطابقها شيء — لا «ممتنع»: لا عالمَ مغلق.
  * **النموّ:** المودَعُ يزيد ولا يُحرَّر (دفعةٌ جديدة تُختم بإذن المالك وتُضاف إلى السجلّ)؛ فلا يُنزل النموُّ حكمًا (`numuw_la_yunzil`).

  **ما ثبت** (بالمعيار الموحَّد في `Nizam/Asas.lean`): 12 مبرهنة —
  * لكلّ (8): `laHukm_iff`، `qiyas_mafhum`، `hikayatan_mafhum`، `numuw_la_yunzil`، `numuw_yahfaz_mafhum`، `sijill_numuw`،
    `jisr_maratib`، `murashshah_la_yarfa`.
  * تعريفيّة (4): `la_hukm_bila_mushahada`، `mafhum_iff`، `tikrar_la_yarfa`، `mutabiq_append`.
  وشواهدُ الجدول الحقيقيّ في `Aql/WaqiShawahid.lean` على المولَّد `Aql/WaqiJadwal.lean`.
  بلا sorry ولا axiom ولا native_decide.
-/
import Aql.Maratib

namespace Waqi

/-- وجهُ المشاهدة: «قياس» ما حُسب أو شوهد تشغيلُه، و«حكاية» ما رواه مصدر. -/
inductive Wajh | qiyas | hikaya
deriving DecidableEq, Repr

/-- صفُّ المشاهدة. `raqm` موضعُه في المودَع، فشاهدُه `⟨بصمة المودَع، raqm⟩`. -/
structure Mushahada where
  raqm : Nat
  hassa : String
  masdar : String
  mawdu : String
  sifa : String
  qima : String
  wajh : Wajh
deriving DecidableEq, Repr

/-- الحكمُ الثلاثيّ (م15): لا «ممتنع» فيه. -/
inductive Hukm | mafhum | maaluma | laHukm
deriving DecidableEq, Repr

/-- رتبةُ الحكم: لا حكم < معلومة < مفهوم. -/
def Hukm.rutba : Hukm → Nat
  | .laHukm => 0
  | .maaluma => 1
  | .mafhum => 2

/-- الصفوفُ المطابقة لقضيّة (شيء، خاصّة، قيمة). -/
def mutabiq (T : List Mushahada) (mawdu sifa qima : String) : List Mushahada :=
  T.filter fun r => r.mawdu == mawdu && r.sifa == sifa && r.qima == qima

/-- قياسٌ مطابق. -/
def fiihiQiyas (l : List Mushahada) : Bool := l.any fun r => r.wajh == .qiyas

/-- حكايتان من مصدرين مختلفين (حدُّ الاستقلال اثنان — تعيينٌ). -/
def tasdiq (l : List Mushahada) : Bool :=
  l.any fun a => l.any fun b => a.wajh == .hikaya && b.wajh == .hikaya && a.masdar != b.masdar

/-- **الحكم على قضيّة من جدول المشاهدات.** -/
def hukm (T : List Mushahada) (mawdu sifa qima : String) : Hukm :=
  let l := mutabiq T mawdu sifa qima
  if fiihiQiyas l || tasdiq l then .mafhum
  else if l.isEmpty then .laHukm
  else .maaluma

/-! ## ١. الحكم -/

/-- **لا حكمَ بلا مشاهدة** — لا «ممتنع»: الغيابُ ليس نفيًا (م16). -/
theorem la_hukm_bila_mushahada (T : List Mushahada) (m s q : String) (h : mutabiq T m s q = []) :
    hukm T m s q = .laHukm := by
  simp [hukm, h, fiihiQiyas, tasdiq]

/-- «لا حكم» إذا وفقط إذا لم يطابق القضيّةَ صفّ. -/
theorem laHukm_iff (T : List Mushahada) (m s q : String) :
    hukm T m s q = .laHukm ↔ mutabiq T m s q = [] := by
  constructor
  · intro h
    unfold hukm at h
    cases hl : mutabiq T m s q with
    | nil => rfl
    | cons r rs =>
      rw [hl] at h
      by_cases hc : (fiihiQiyas (r :: rs) || tasdiq (r :: rs)) = true
      · simp [hc] at h
      · simp [hc] at h
  · exact la_hukm_bila_mushahada T m s q

/-- «مفهوم» إذا وفقط إذا طابقها قياسٌ أو صدّقتها حكايتان من مصدرين. -/
theorem mafhum_iff (T : List Mushahada) (m s q : String) :
    hukm T m s q = .mafhum ↔ (fiihiQiyas (mutabiq T m s q) || tasdiq (mutabiq T m s q)) = true := by
  unfold hukm
  by_cases hc : (fiihiQiyas (mutabiq T m s q) || tasdiq (mutabiq T m s q)) = true
  · simp [hc]
  · simp only [hc]
    by_cases he : (mutabiq T m s q).isEmpty = true <;> simp [he]

/-- **القياسُ يرفع إلى مفهوم:** صفٌّ مطابقٌ وجهُه قياس. -/
theorem qiyas_mafhum (T : List Mushahada) (r : Mushahada) (hr : r ∈ T) (hq : r.wajh = .qiyas) :
    hukm T r.mawdu r.sifa r.qima = .mafhum := by
  rw [mafhum_iff]
  have hm : r ∈ mutabiq T r.mawdu r.sifa r.qima := by simp [mutabiq, hr]
  have : fiihiQiyas (mutabiq T r.mawdu r.sifa r.qima) = true :=
    List.any_eq_true.mpr ⟨r, hm, by simp [hq]⟩
  simp [this]

/-- **حكايتان من مصدرين مختلفين ترفعان إلى مفهوم** (تواترٌ بحدّ اثنين — تعيين). -/
theorem hikayatan_mafhum (T : List Mushahada) (a b : Mushahada) (ha : a ∈ T) (hb : b ∈ T)
    (hwa : a.wajh = .hikaya) (hwb : b.wajh = .hikaya) (hs : b.mawdu = a.mawdu) (hf : b.sifa = a.sifa)
    (hv : b.qima = a.qima) (hd : a.masdar ≠ b.masdar) :
    hukm T a.mawdu a.sifa a.qima = .mafhum := by
  rw [mafhum_iff]
  have hma : a ∈ mutabiq T a.mawdu a.sifa a.qima := by simp [mutabiq, ha]
  have hmb : b ∈ mutabiq T a.mawdu a.sifa a.qima := by simp [mutabiq, hb, hs, hf, hv]
  have : tasdiq (mutabiq T a.mawdu a.sifa a.qima) = true := by
    unfold tasdiq
    exact List.any_eq_true.mpr ⟨a, hma, List.any_eq_true.mpr ⟨b, hmb, by simp [hwa, hwb, hd]⟩⟩
  simp [this]

/-- **التكرارُ لا يرفع** (م16): حكايةٌ واحدة مكرَّرةً من مصدرها نفسه تبقى معلومة. -/
theorem tikrar_la_yarfa (r : Mushahada) (hw : r.wajh = .hikaya) (n : Nat) :
    hukm (List.replicate (n + 1) r) r.mawdu r.sifa r.qima = .maaluma := by
  have hm : mutabiq (List.replicate (n + 1) r) r.mawdu r.sifa r.qima = List.replicate (n + 1) r := by
    simp [mutabiq]
  unfold hukm
  simp only [hm]
  have h1 : fiihiQiyas (List.replicate (n + 1) r) = false := by simp [fiihiQiyas, hw]
  have h2 : tasdiq (List.replicate (n + 1) r) = false := by simp [tasdiq]
  simp [h1, h2]

/-! ## ٢. النموّ -/

theorem mutabiq_append (T T' : List Mushahada) (m s q : String) :
    mutabiq (T ++ T') m s q = mutabiq T m s q ++ mutabiq T' m s q := by
  simp [mutabiq]

/-- **النموُّ لا يُنزل حكمًا:** إضافةُ مشاهداتٍ لا تخفض رتبةَ أيّ قضيّة. -/
theorem numuw_la_yunzil (T T' : List Mushahada) (m s q : String) :
    (hukm T m s q).rutba ≤ (hukm (T ++ T') m s q).rutba := by
  have hq : fiihiQiyas (mutabiq T m s q) = true → fiihiQiyas (mutabiq (T ++ T') m s q) = true := by
    intro h
    rw [mutabiq_append]
    simp only [fiihiQiyas, List.any_append, Bool.or_eq_true] at h ⊢
    exact Or.inl h
  have ht : tasdiq (mutabiq T m s q) = true → tasdiq (mutabiq (T ++ T') m s q) = true := by
    intro h
    rw [mutabiq_append]
    simp only [tasdiq, List.any_eq_true] at h ⊢
    obtain ⟨a, ha, b, hb, hab⟩ := h
    exact ⟨a, List.mem_append_left _ ha, b, List.mem_append_left _ hb, hab⟩
  have he : (mutabiq T m s q).isEmpty = false → (mutabiq (T ++ T') m s q).isEmpty = false := by
    intro h
    rw [mutabiq_append]
    cases hl : mutabiq T m s q with
    | nil => simp [hl] at h
    | cons _ _ => rfl
  unfold hukm
  by_cases h1 : (fiihiQiyas (mutabiq T m s q) || tasdiq (mutabiq T m s q)) = true
  · have h1' : (fiihiQiyas (mutabiq (T ++ T') m s q) || tasdiq (mutabiq (T ++ T') m s q)) = true := by
      simp only [Bool.or_eq_true] at h1 ⊢
      exact h1.elim (fun h => Or.inl (hq h)) (fun h => Or.inr (ht h))
    simp [h1, h1']
  · simp only [h1]
    by_cases h2 : (mutabiq T m s q).isEmpty = true
    · simp only [h2, ite_true, Hukm.rutba]
      exact Nat.zero_le _
    · have h2' : (mutabiq T m s q).isEmpty = false := by simpa using h2
      have h3 := he h2'
      simp only [h2', h3]
      by_cases h4 : (fiihiQiyas (mutabiq (T ++ T') m s q) || tasdiq (mutabiq (T ++ T') m s q)) = true
      · simp [h4, Hukm.rutba]
      · simp [h4, Hukm.rutba]

/-- ما كان مفهومًا يبقى مفهومًا بالنموّ. -/
theorem numuw_yahfaz_mafhum (T T' : List Mushahada) (m s q : String) (h : hukm T m s q = .mafhum) :
    hukm (T ++ T') m s q = .mafhum := by
  have := numuw_la_yunzil T T' m s q
  rw [h] at this
  cases hh : hukm (T ++ T') m s q <;> simp_all [Hukm.rutba]

/-- **نموُّ السجلّ لا يُسقط شاهدًا:** ما اعتُبر من الشواهد بسجلٍّ يبقى معتبرًا إذا زيد السجلّ (`Maratib.shuhudMutabara`). -/
theorem sijill_numuw (sijill more : List (String × Idaa.Naw)) (sh : List Maratib.ShahidWaqi) (s : Maratib.ShahidWaqi)
    (h : s ∈ Maratib.shuhudMutabara sijill sh) : s ∈ Maratib.shuhudMutabara (sijill ++ more) sh := by
  simp only [Maratib.shuhudMutabara, List.mem_filter, List.any_append, Bool.or_eq_true] at h ⊢
  exact ⟨h.1, Or.inl h.2⟩

/-! ## ٣. الجسر إلى مراتب المخرج (`Aql/Maratib.lean`) -/

/-- شواهدُ القضيّة في مودَعٍ بصمتُه `F`: موضعُ كلّ صفٍّ مطابق. -/
def shuhud (F : String) (T : List Mushahada) (m s q : String) : List Maratib.ShahidWaqi :=
  (mutabiq T m s q).map fun r => ⟨F, r.raqm⟩

/-- **الجسر:** قضيّةٌ لها صفٌّ مطابقٌ في جدولٍ خُتم «واقعًا مختومًا» ببصمةٍ غيرِ فارغة يرتفع معناها في `Maratib` إلى «مفهوم»
    (`hF`: البصمةُ بادئةُ نفسها، يُقضى بـ decide على البصمة المعيَّنة). -/
theorem jisr_maratib (F : String) (hne : F ≠ "") (hF : F.startsWith F = true) (T : List Mushahada)
    (m s q : String) (r : Mushahada) (hr : r ∈ mutabiq T m s q) (i : Nat) :
    (Maratib.martabatMaana i (Maratib.shuhudMutabara [(F, .waqiMakhtum)] (shuhud F T m s q))).ism = "مفهوم" := by
  have he : F.isEmpty = false := by
    cases h : F.isEmpty
    · rfl
    · exact absurd (String.isEmpty_iff.mp h) hne
  have hall : Maratib.shuhudMutabara [(F, .waqiMakhtum)] (shuhud F T m s q) = shuhud F T m s q := by
    simp only [Maratib.shuhudMutabara, shuhud]
    rw [List.filter_eq_self]
    intro w hw
    simp only [List.mem_map] at hw
    obtain ⟨_, _, rfl⟩ := hw
    simp [he, hF]
  rw [hall]
  have hne' : shuhud F T m s q ≠ [] := by
    simp only [shuhud, ne_eq, List.map_eq_nil_iff]
    intro h; rw [h] at hr; simp at hr
  cases hs : shuhud F T m s q with
  | nil => exact absurd hs hne'
  | cons w ws => simp [Maratib.martabatMaana, Maratib.Mukhraj.ism]

/-- **المرشَّح لا يرفع:** ما لم يُختم الجدولُ (فلا قيدَ «واقع مختوم» في السجلّ) يبقى كلُّ معنًى «معلومة»، أيًّا كانت مشاهداتُه. -/
theorem murashshah_la_yarfa (sijill : List (String × Idaa.Naw)) (hs : ∀ b ∈ sijill, b.2 ≠ .waqiMakhtum)
    (F : String) (T : List Mushahada) (m s q : String) (i : Nat) :
    Maratib.martabatMaana i (Maratib.shuhudMutabara sijill (shuhud F T m s q)) = .maaluma i :=
  Maratib.la_mafhum_bila_waqi sijill hs i (shuhud F T m s q)

end Waqi
