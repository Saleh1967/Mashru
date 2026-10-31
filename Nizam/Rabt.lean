/-
  Nizam/Rabt.lean — ربطُ السلسلة على قراءة الجملة بالعوامل (`Jisr.Tahlil`): لكلّ قراءةٍ مرخَّصة جدولُ إعرابها (الدورُ والحالةُ والعامل)،
  ونِسَبُ أدوارها، وإسنادُها، وقوّتُها، وإحالةُ ضمائرها، وقيدُها ومفهومُها، ودلالةُ ألفاظها على جدول اللزوم.

  **الطلب:** قولُ المالك 2026-10-31 (12:48 بتوقيت عمّان، من ملخّص الجلسة بعد ضغطها): «… يوجد كود للعوامل لم يوظف … يوجد كود ياسر الإعراب لم
  يوظف يوجد كود للاسناد والمسند إليه لم يوظف الاسناد ولا التضمن ولا التقييد ويوجد كود للدلالة المطابقة ودلالة التضمن ودلالة ودلالة الالتزام لم
  توظف ويوجد كود للاحالة والاسماء المبنيات لم يوظف … وانت مفوض بالحل وليس التشخيص»؛ وفيه: «واما الإيداع والختم يمكن عمل تحفظ ولكن نكمل
  العمل ونضع ملاحظة ان الجدول مثلا للرسم يحتاج ختم». والتصميمُ وتعييناتُه قرارُ البنّاء.

  **العُقَد** (كلٌّ على قطعةٍ قائمة في المشروع):
  1. **العامل** (`amilOf`): الجازمُ والناصبُ وحرفُ الجرّ صفوفُ جدول العوامل المختوم (`Awamil.table`، بصفّ الوحدة)؛ والمضارعُ بلا ناصبٍ ولا
     جازم مرفوعٌ بالتجرّد (القطر L96 «يرفع المضارع خاليا من ناصب وجازم»؛ الألفية L883 «رفع مضارعا إذا يجرد من ناصب وجازم»)؛ والفاعلُ والمفعولُ
     بالفعل (الألفية L312 «وبعد فعل فاعل»، وL361 «فانصب به مفعوله»)؛ والمبتدأُ بالابتداء والخبرُ بالمبتدأ (الألفية L181 «ورفعوا مبتدأ بالابتدا ...
     كذاك رفع خبر بالمبتدا»)؛ والمضافُ إليه بالإضافة (القطر L339 «أو بإضافة إلى اسم»؛ الألفية L508 «والثاني اجرر»)؛ والماضي والأمرُ والحرفُ
     مبنيّة (القطر L55، L59).
  2. **الحالة** (`halaOf`): الحالةُ التي يطلبها موضعُ الوحدة في إطار المالك (`Tahlil.matlub`) وفي حالات خلاياها؛ والمقدَّرُ والمبنيُّ ومحلُّه.
  3. **النسبة** (`nisba`): تعيينُ `Jisr.Nisab.nisbaOf` على علاقات المالك (`Simat.semOf`) الذي أمضاه المالك 2026-10-16، والمضافُ إليه الإضافيّة
     (كـ`Nizam.Athar.nisbaDawr`).
  4. **الإسناد** (`isnadOf`): «هذا باب المسند والمسند إليه … فمن ذلك الاسم المبتدأ والمبنى عليه … ومثل ذلك يذهب عبد الله» (الكتاب س234–237):
     المسندُ الفعلُ أو الخبر، والمسندُ إليه الفاعلُ أو المبتدأ؛ والفاعلُ الضميرُ بارزٌ متّصل (لاحقةُ الفعل) أو مستتر — وجوبًا في المضارع للمتكلّم
     والمخاطب وجوازًا للغائب (القطر L124–125: «مستتر كالمقدر وجوبا في نحو "أقوم" و "تقوم" أو جوازا في نحو "زيد يقوم"»).
  5. **القوّة** (`quwwaOf`): من صفّ الصدر بعمود الأسلوب (`Nizam.Athar.quwwaSufuf`)، و«لن» و«لا» النافية نفيٌ بصورتي النفي في
     `Aql.Awwaliyyat.nafy` (الكتاب س9783–9787)، والأمرُ إنشاء (القطر L59: «ويعرف بدلالته على الطلب»)، وما سواها خبرٌ مثبت (`SakkJumla.awwal`).
  6. **الإحالة** (`ihalat`): ضميرُ المتكلّم والمخاطب إلى الحضور، والغائبُ إلى مرشَّحين قبله بمطابقة العدد (تعيينُ البنّاء: الجنسُ لا تحمله الحروف).
  7. **القيدُ والمفهوم** (`qaydR`، `mafahim`): عناصرُ البنية من الوحدات بأدوارها على `Jisr.QaydMafhum.unsurQayd` (الغايةُ من «إلى» حرفَ جرّ، والعددُ
     من المثنّى، والاسمُ من ذي الأداة والنكرة)، والجسرُ `Jisr.MantuqMafhum.jisr` بعد ربطه بالبنية (`bilBunya`) على ودائعَ تُعطى معاملًا.
     **والودائعُ المرشَّحة** (`wadaMurashshaha`) تحتاج ختمًا: الحملُ على الحقيقة اللغويّة لكلّ كلمةٍ جذرُها مشهود (`QawaninDalala.haml` بلا حقيقةٍ
     شرعيّةٍ ولا عرفيّةٍ مودَعة)، ولا خروجَ مخرجَ الأغلب، ولا نصَّ معطِّل.
  8. **الدلالة** (`iddiaOf`): صفُّ جدول اللزوم (`JadwalLuzum.Saff`) ادّعاءٌ بسلسلته على قاعدة الجدول نفسِه (`JadwalLuzum.qaidaOf`): الترادفُ مطابقة،
     والجزءُ والأصلُ تضمّن، والتعليلُ التزام. **ويقبله الفاحصُ لكلّ جدولٍ وكلّ صفٍّ فيه** (`iddia_maqbul`)، فهو صادقٌ في النموذج بفروض
     `QawaninDalala.salama` (`dalala_sadiqa`). والجدولُ في التنفيذيّ `rabt` هو `luzum_mujam.tsv` المرشَّح (`520dffc8…`، «يحتاج ختمًا»).

  **حدُّه:** العُقَدُ على القراءات المرخَّصة وحدها؛ والإحالةُ مرشَّحون لا تعيين؛ والودائعُ المرشَّحة فرضٌ معلَن؛ وجذرُ الاسم على أوزانٍ ثمانيةٍ تعيينًا.
-/
import Jisr.Tahlil
import Nizam.Athar
import Madlul.JadwalLuzum
import Aql.SalamaMaqbul

namespace Nizam
namespace Rabt

open Jisr.Tahlil (Wahda Dawr Naw Murashshah)

/-! ## ١. الإعراب: الدورُ والحالةُ والعامل -/

inductive Amil
  /-- صفٌّ في جدول العوامل. -/
  | saff (i : Nat)
  /-- التجرّدُ من الناصب والجازم. -/
  | tajarrud
  /-- الفعلُ في الكلمة k. -/
  | fil (k : Nat)
  | ibtida
  /-- المبتدأُ في الكلمة k. -/
  | mubtada (k : Nat)
  /-- المضافُ في الكلمة k. -/
  | idafa (k : Nat)
  | bina
  | kharij
  deriving DecidableEq, Repr

inductive Hala
  /-- حالةٌ ظاهرةٌ تنفرد بها خلاياها. -/
  | zahira (h : Nat)
  /-- حالةٌ يطلبها الموضع، وعلامتُها مشتركةٌ بين الحالات hs. -/
  | mushtaraka (h : Nat) (hs : List Nat)
  | muqaddara
  /-- مبنيٌّ في محلّ h. -/
  | mahall (h : Nat)
  | mabni
  /-- حالاتُ الخلايا ولا يطلب الموضعُ حالة. -/
  | ghayrMatluba (hs : List Nat)
  | laHala
  deriving DecidableEq, Repr

structure Irab where
  wahda : Wahda
  dawr : Dawr
  hala : Hala
  amil : Amil
  deriving Repr

/-- الوحدةُ الأولى في دورٍ من أدوار المرشَّح. -/
def wahdaFi (m : Murashshah) (d : Dawr) : Option Wahda := (m.adwar.find? (·.2 == d)).map (·.1)

/-- الصدرُ الجازمُ أو الناصب. -/
def sadrOf (m : Murashshah) : Option Wahda := (m.adwar.find? fun p => p.2 == .jazim || p.2 == .nasib).map (·.1)

/-- عاملُ الفعل: المضارعُ بصفّ الصدر أو بالتجرّد، والماضي والأمرُ مبنيّان. -/
def amilFil (m : Murashshah) (w : Wahda) : Amil :=
  if w.sima.1 == 1 then
    match sadrOf m with
    | some s => match s.saff with | some i => .saff i | none => .kharij
    | none => .tajarrud
  else .bina

/-- **العامل** في الوحدة بدورها، و`prev` الوحدةُ قبلها في النطق (الجارُّ قبل المجرور، والمضافُ قبل المضاف إليه). -/
def amilOf (m : Murashshah) (prev : Option Wahda) (p : Wahda × Dawr) : Amil :=
  match p.2 with
  | .fil => amilFil m p.1
  | .fail => match wahdaFi m .fil with | some v => .fil v.kalima | none => .kharij
  | .maful => match wahdaFi m .fil with | some v => .fil v.kalima | none => .kharij
  | .mubtada => .ibtida
  | .khabar => match wahdaFi m .mubtada with | some v => .mubtada v.kalima | none => .kharij
  | .majrur => match prev with | some j => (match j.saff with | some i => .saff i | none => .kharij) | none => .kharij
  | .mudafIlayh => match prev with | some x => .idafa x.kalima | none => .kharij
  | .kharij => .kharij
  | _ => .bina

def khanaOf (m : Murashshah) (w : Wahda) : Option (Wahda × Option Nat × Nat) := m.khanat.find? (·.1 == w)

/-- **الحالة:** المقدَّرةُ «مقدَّرة»؛ والفعلُ المبنيّ مبنيّ، والاسمُ والضميرُ المبنيّان في محلّ ما يطلبه موضعُه؛ والمعربُ بأوّل حالةٍ من حالات خلاياها يطلبها الموضع — ظاهرةً إن انفردت بها
    خلاياها، ومشتركةً إن احتملت غيرَها (المقصورُ والمنقوصُ والمضافُ إلى الياء والأمثلةُ الخمسة ونونُ النسوة). -/
def halaOf (m : Murashshah) (w : Wahda) : Hala :=
  match khanaOf m w with
  | none => .laHala
  | some x =>
    let ms := Jisr.Tahlil.matlub m x
    if w.taqdir then .muqaddara
    else if w.sima.2.2.2 then (if w.naw == .fil then .mabni else match ms.head? with | some h => .mahall h | none => .mabni)
    else match w.halat.find? (ms.contains ·) with
      | some h => if w.halat.length == 1 then .zahira h else .mushtaraka h w.halat
      | none => .ghayrMatluba w.halat

def irabAux (m : Murashshah) : Option Wahda → List (Wahda × Dawr) → List Irab
  | _, [] => []
  | prev, p :: r => ⟨p.1, p.2, halaOf m p.1, amilOf m prev p⟩ :: irabAux m (some p.1) r

/-- **جدولُ الإعراب** بترتيب النطق. -/
def irab (m : Murashshah) : List Irab := irabAux m none m.adwar

theorem irabAux_tamm (m : Murashshah) (prev : Option Wahda) (l : List (Wahda × Dawr)) :
    (irabAux m prev l).map (fun e => (e.wahda, e.dawr)) = l := by
  induction l generalizing prev with
  | nil => rfl
  | cons p r ih => simp only [irabAux, List.map_cons, ih]

/-- **الإعرابُ لا يُسقط وحدةً ولا يزيدها ولا يغيّر دورها.** -/
theorem irab_tamm (m : Murashshah) : (irab m).map (fun e => (e.wahda, e.dawr)) = m.adwar := irabAux_tamm m none m.adwar

theorem mem_irabAux (m : Murashshah) {prev : Option Wahda} {l : List (Wahda × Dawr)} {e : Irab} (h : e ∈ irabAux m prev l) :
    ∃ p ∈ l, ∃ q, e = ⟨p.1, p.2, halaOf m p.1, amilOf m q p⟩ := by
  induction l generalizing prev with
  | nil => cases h
  | cons p r ih =>
    simp only [irabAux, List.mem_cons] at h
    rcases h with h | h
    · exact ⟨p, List.mem_cons_self, prev, h⟩
    · obtain ⟨p', hp', q, he⟩ := ih h
      exact ⟨p', List.mem_cons_of_mem _ hp', q, he⟩

theorem wahdaFi_mem (m : Murashshah) (d : Dawr) {v : Wahda} (h : wahdaFi m d = some v) : (v, d) ∈ m.adwar := by
  unfold wahdaFi at h
  cases hf : m.adwar.find? (·.2 == d) with
  | none => rw [hf] at h; cases h
  | some x =>
    rw [hf] at h
    simp only [Option.map_some, Option.some.injEq] at h
    have hm := List.mem_of_find?_eq_some hf
    have hp := List.find?_some hf
    simp only [beq_iff_eq] at hp
    rw [← h, ← hp]
    exact hm

/-- العاملُ فعلٌ إذا كان في المرشَّح فعلٌ في تلك الكلمة. -/
theorem amilOf_fil (m : Murashshah) (q : Option Wahda) (p : Wahda × Dawr) (k : Nat) (h : amilOf m q p = .fil k) :
    ∃ v, (v, Dawr.fil) ∈ m.adwar ∧ v.kalima = k := by
  unfold amilOf at h
  split at h
  · unfold amilFil at h
    split at h
    · split at h
      · split at h <;> cases h
      · cases h
    · cases h
  all_goals first
    | (cases hv : wahdaFi m .fil with
        | none => rw [hv] at h; cases h
        | some v => rw [hv] at h; cases h; exact ⟨v, wahdaFi_mem m .fil hv, rfl⟩)
    | (split at h <;> (try split at h) <;> cases h)
    | cases h

/-- **العاملُ في الفاعل والمفعول فعلٌ في الجملة نفسِها:** كلُّ مدخلٍ في جدول الإعراب عاملُه فعلٌ في الكلمة k في المرشَّح فعلٌ في الكلمة k. -/
theorem amil_fil_fi_jumla (m : Murashshah) {e : Irab} (he : e ∈ irab m) {k : Nat} (ha : e.amil = .fil k) :
    ∃ v, (v, Dawr.fil) ∈ m.adwar ∧ v.kalima = k := by
  obtain ⟨p, _, q, rfl⟩ := mem_irabAux m he
  exact amilOf_fil m q p k ha

/-- **الحالةُ الظاهرةُ والمشتركة حالةٌ يطلبها الموضعُ ومن حالات الخلايا.** -/
theorem hala_matluba (m : Murashshah) (w : Wahda) {h : Nat} (hh : halaOf m w = .zahira h ∨ ∃ hs, halaOf m w = .mushtaraka h hs) :
    ∃ x ∈ m.khanat, x.1 = w ∧ h ∈ w.halat ∧ h ∈ Jisr.Tahlil.matlub m x := by
  unfold halaOf at hh
  cases hk : khanaOf m w with
  | none => rw [hk] at hh; simp at hh
  | some x =>
    rw [hk] at hh
    have hx := List.mem_of_find?_eq_some hk
    have hxw : x.1 = w := by simpa using List.find?_some hk
    dsimp only at hh
    by_cases ht : w.taqdir = true
    · simp [ht] at hh
    · simp only [ht, Bool.false_eq_true, ↓reduceIte] at hh
      by_cases hb : w.sima.2.2.2 = true
      · simp only [hb, ↓reduceIte] at hh
        revert hh
        split
        · simp
        · cases (Jisr.Tahlil.matlub m x).head? <;> simp
      · simp only [hb, Bool.false_eq_true, ↓reduceIte] at hh
        split at hh
        · rename_i h' hf
          have hh' : h' = h := by
            by_cases hl : (w.halat.length == 1) = true
            · simp only [hl, ↓reduceIte] at hh
              rcases hh with hh | ⟨hs, hh⟩
              · exact Hala.zahira.inj hh
              · cases hh
            · simp only [hl, Bool.false_eq_true, ↓reduceIte] at hh
              rcases hh with hh | ⟨hs, hh⟩
              · cases hh
              · exact (Hala.mushtaraka.inj hh).1
          subst hh'
          have hc := List.find?_some hf
          exact ⟨x, hx, hxw, List.mem_of_find?_eq_some hf, by simpa using hc⟩
        · simp at hh

/-! ## ٢. النِّسَب والإسناد -/

/-- رمزُ الدور في أطر المالك. -/
def ramz : Dawr → Option Nat
  | .mubtada => some 0 | .khabar => some 1 | .fil => some 2 | .fail => some 3 | .maful => some 4
  | .harfJarr => some 5 | .majrur => some 6 | _ => none

/-- **نسبةُ الدور** على علاقات المالك، والمضافُ إليه الإضافيّة. -/
def nisba (d : Dawr) : Option Jisr.Nisab.Nisba :=
  match d with
  | .mudafIlayh => some .idafiyya
  | _ => (ramz d).bind fun r => Jisr.Nisab.nisbaOf (SLGE.Simat.semOf r)

/-- المبتدأُ والخبرُ والفعلُ والفاعلُ إسناديّة، والمفعولُ تقييديّ، والمجرورُ والمضافُ إليه إضافيّان، والحروفُ عواملُ بلا نسبة. -/
theorem nisba_qiyam :
    [Dawr.mubtada, .khabar, .fil, .fail, .maful, .harfJarr, .majrur, .mudafIlayh, .rabit, .jazim, .nasib, .nafiya, .kharij].map nisba =
      [some .isnadiyya, some .isnadiyya, some .isnadiyya, some .isnadiyya, some .taqyidiyya, none, some .idafiyya, some .idafiyya,
       none, none, none, none, none] := by
  decide

inductive Sura | zahir | bariz | mustatar
  deriving DecidableEq, Repr

/-- الإسناد: المسندُ (الفعلُ أو الخبر؛ و`none` شبهُ الجملة خبرًا)، والمسندُ إليه الظاهر (أو لا شيء والفاعلُ ضمير)، وصورتُه، وسماتُه، والاستتارُ
    وجوبًا أو جوازًا (في المضارع وحده). -/
structure Isnad where
  musnad : Option Wahda
  ilayh : Option Wahda
  sura : Sura
  ft : SLGE.Maqam.Feat
  wujub : Option Bool
  deriving Repr

/-- لاحقةُ الفعل ضميرُ رفعٍ بارز: الماضي بغير الغائب المفرد وتاء التأنيث، والمضارعُ بألف الاثنين وواو الجماعة ونون النسوة وياء المخاطبة،
    والأمرُ بغير المفرد المذكّر. -/
def lahiqaFail (v : Wahda) : Bool :=
  let ft := v.sima.2.2.1
  if v.sima.1 == 0 then !(ft == (3, 0, 0) || ft == (3, 1, 0))
  else if v.sima.1 == 1 then ft.2.2 != 0 || ft == (2, 1, 0)
  else ft != (2, 0, 0)

def isnadOf (m : Murashshah) : Option Isnad :=
  match wahdaFi m .fil with
  | some v =>
    match wahdaFi m .fail with
    | some f => some ⟨some v, some f, .zahir, f.sima.2.2.1, none⟩
    | none =>
      let ft := v.sima.2.2.1
      if lahiqaFail v then some ⟨some v, none, .bariz, ft, none⟩
      else some ⟨some v, none, .mustatar, ft, if v.sima.1 == 1 then some (decide (ft.1 ≤ 2)) else none⟩
  | none =>
    match wahdaFi m .mubtada with
    | some mb => some ⟨wahdaFi m .khabar, some mb, .zahir, mb.sima.2.2.1, none⟩
    | none => none

/-- **في كلّ إسنادٍ فعليٍّ المسندُ هو الفعل،** والمسندُ إليه الظاهرُ إن كان هو الفاعل. -/
theorem isnad_fil (m : Murashshah) (v : Wahda) (hv : wahdaFi m .fil = some v) {i : Isnad} (hi : isnadOf m = some i) :
    i.musnad = some v ∧ i.ilayh = wahdaFi m .fail := by
  unfold isnadOf at hi
  rw [hv] at hi
  simp only at hi
  cases hf : wahdaFi m .fail with
  | some f => rw [hf] at hi; cases hi; exact ⟨rfl, rfl⟩
  | none =>
    rw [hf] at hi
    simp only at hi
    split at hi <;> cases hi <;> exact ⟨rfl, rfl⟩

/-! ## ٣. القوّة -/

open Jisr.SakkJumla (Quwwa)

/-- **قوّةُ القراءة** بسندها. -/
def quwwaOf (m : Murashshah) : Quwwa × String :=
  match m.adwar.find? (fun p => p.2 == .jazim || p.2 == .nasib || p.2 == .nafiya) with
  | some (s, d) =>
    if d == .nafiya then (.nafy, "«لا» نافيةً: «لا يفعل» صورةُ نفي المستقبل (Aql.Awwaliyyat.nafy؛ الكتاب س9787)")
    else match s.saff with
      | some 63 => (.nafy, "«لن»: «لن يفعل» صورةُ نفي المستقبل المنفَّس (Aql.Awwaliyyat.nafy؛ الكتاب س9787)")
      | some i => (Nizam.Athar.quwwaSufuf [i], "صفّ الجدول " ++ toString i ++ " بعمود الأسلوب (Nizam.Athar.quwwaSufuf)")
      | none => (.laHukm, "صدرٌ بلا صفّ")
  | none =>
    match wahdaFi m .fil with
    | some v =>
      if v.sima.1 == 2 then (.insha, "الأمرُ «بدلالته على الطلب» (القطر L59)")
      else (Jisr.SakkJumla.awwal ⟨.laShay, .laQawl, .laQawl, .amma⟩, "لا أداةَ في الصدر (Jisr.SakkJumla.awwal)")
    | none => (Jisr.SakkJumla.awwal ⟨.laShay, .laQawl, .laQawl, .amma⟩, "لا أداةَ في الصدر (Jisr.SakkJumla.awwal)")

/-- صورتا النفي في الأزمنة الخمسة: «لا يفعل» للمستقبل و«لن يفعل» للمنفَّس (`Aql.Awwaliyyat.nafy`). -/
theorem nafy_suwar : Aql.Awwaliyyat.nafy .mustaqbal = "لا يفعل" ∧ Aql.Awwaliyyat.nafy .mustaqbalMunaffas = "لن يفعل" := ⟨rfl, rfl⟩

/-! ## ٤. الإحالة -/

inductive Marji
  | hudur
  /-- مرشَّحون: (الجملة، الكلمة)، الأقربُ أوّلًا. -/
  | murashshahun (l : List (Nat × Nat))
  deriving DecidableEq, Repr

structure Ihala where
  kalima : Nat
  sura : Sura
  ft : SLGE.Maqam.Feat
  marji : Marji
  deriving Repr

/-- المرشَّحون للغائب: الأسماءُ الظاهرة قبله بعدده، الأقربُ أوّلًا (تعيين). -/
def murashshahunIhala (qabl : List (Nat × Wahda)) (ft : SLGE.Maqam.Feat) : List (Nat × Nat) :=
  ((qabl.filter fun p => p.2.naw == .ism && p.2.sima.2.2.1.2.2 == ft.2.2).map fun p => (p.1, p.2.kalima)).reverse

def marjiOf (qabl : List (Nat × Wahda)) (ft : SLGE.Maqam.Feat) : Marji :=
  if ft.1 ≤ 2 then .hudur else .murashshahun (murashshahunIhala qabl ft)

/-- **الإحالات في القراءة** `m` من الجملة `j`، و`qabl` أسماءُ ما قبلها: الفاعلُ الضميرُ (بارزًا أو مستترًا)، والضمائرُ المتّصلة المنصوبةُ والمجرورة. -/
def ihalat (qabl : List (Nat × Wahda)) (j : Nat) (m : Murashshah) : List Ihala :=
  let fail := match isnadOf m with
    | some i => match i.sura, i.musnad with
      | .zahir, _ => []
      | s, some v => [⟨v.kalima, s, i.ft, marjiOf qabl i.ft⟩]
      | _, none => []
    | none => []
  let damair := (List.range m.adwar.length).filterMap fun n =>
    match m.adwar[n]? with
    | some (w, _) =>
      if w.naw == .damir then
        let qablFi := ((m.adwar.take n).filter fun p => p.1.kalima != w.kalima).map fun p => (j, p.1)
        some ⟨w.kalima, .bariz, w.sima.2.2.1, marjiOf (qabl ++ qablFi) w.sima.2.2.1⟩
      else none
    | none => none
  fail ++ damair

/-- **ضميرُ المتكلّم والمخاطب يحيل إلى الحضور، والغائبُ إلى مرشَّحين بعدده.** -/
theorem marji_hudur (qabl : List (Nat × Wahda)) (ft : SLGE.Maqam.Feat) (h : ft.1 ≤ 2) : marjiOf qabl ft = .hudur := by
  unfold marjiOf; simp [h]

theorem murashshah_mutabiq (qabl : List (Nat × Wahda)) (ft : SLGE.Maqam.Feat) {p : Nat × Nat}
    (hp : p ∈ murashshahunIhala qabl ft) :
    ∃ w, (p.1, w) ∈ qabl ∧ w.kalima = p.2 ∧ w.naw = .ism ∧ w.sima.2.2.1.2.2 = ft.2.2 := by
  unfold murashshahunIhala at hp
  rw [List.mem_reverse, List.mem_map] at hp
  obtain ⟨⟨a, w⟩, hm, he⟩ := hp
  rw [List.mem_filter] at hm
  simp only [Bool.and_eq_true, beq_iff_eq] at hm
  cases he
  exact ⟨w, hm.1, rfl, hm.2.1, hm.2.2⟩

/-! ## ٥. القيدُ والمفهوم -/

open Jisr.QaydMafhum (Unsur unsurQayd)
open Jisr.MantuqMafhum (Qayd sinfOf Mudaa Mafhum jisr)

/-- عناصرُ البنية من الوحدة بدورها: حرفُ الجرّ بصفّه، والاسمُ مثنًّى (بابُ المثنّى) وبـ«ال» (ذو الأداة، المعرفةُ الخامسة) ونكرةً (اسمُ جنس). -/
def anasirWahda (w : Wahda) (d : Dawr) : List Unsur :=
  (if d == .harfJarr then (match w.saff with | some i => [Unsur.adat i] | none => []) else []) ++
  (if w.naw == .ism then
     (if w.sima.2.2.1.2.2 == 1 then [Unsur.bab .muthanna] else []) ++
     (if w.sima.2.1 == 1 then [Unsur.marifa 4] else if !w.idafa then [Unsur.ismJins] else [])
   else [])

def bunyaR (m : Murashshah) : List Unsur := m.adwar.flatMap fun p => anasirWahda p.1 p.2

def qaydat (m : Murashshah) : List (Qayd × Wahda) :=
  m.adwar.flatMap fun p => (anasirWahda p.1 p.2).filterMap fun u => (unsurQayd u).map (·, p.1)

/-- **قيدُ القراءة** بـ`Nizam.Athar.qaydMin`: أوّلُ قيدٍ له صنفُ مخالفة، وإلّا أوّلُ قيد. -/
def qaydR (m : Murashshah) : Option (Qayd × Wahda) := Nizam.Athar.qaydMin (qaydat m)

structure Wada where
  haml : List QawaninDalala.Mahmul
  aghlab : Bool
  muattil : Bool
  deriving Repr

def mudaaR (m : Murashshah) (W : Wada) : Mudaa Unit (Qayd × Nat) where
  kalimat := fun _ => W.haml
  qayd := fun _ => (qaydR m).map (·.1)
  mufhim := fun _ => false
  siyaqAdad := fun _ => false
  innama := fun _ => false
  aghlab := fun _ => W.aghlab
  muattil := fun _ => W.muattil
  naqid := fun _ => (qaydR m).map fun p => (p.1, p.2.kalima)
  muwafiq := fun _ => []
  iqtida := fun _ => []
  tanbih := fun _ => []
  ishara := fun _ => []

/-- **المفهوم:** جسرُ `MantuqMafhum` على المودَع بعد ربطه ببنية القراءة. -/
def mafahim (m : Murashshah) (W : Wada) : List (Mafhum Unit (Qayd × Nat)) :=
  jisr (Jisr.QaydMafhum.bilBunya (mudaaR m W) (fun _ => bunyaR m)) [()]

/-- **كلُّ مفهومِ مخالفةٍ تحمله وحدةٌ في دورها:** قيدُه يشهد له عنصرٌ من بنية وحدةٍ في القراءة (`QaydMafhum.mukhalafa_mashuda`). -/
theorem mafhum_wahda (m : Murashshah) (W : Wada) {f : Mafhum Unit (Qayd × Nat)} {k : SLGE.Madlul.Mukhalafa}
    (h : f ∈ mafahim m W) (hk : f.naw = .mukhalafa k) :
    ∃ p ∈ m.adwar, ∃ u ∈ anasirWahda p.1 p.2, ∃ q, unsurQayd u = some q ∧ sinfOf q = some k := by
  obtain ⟨q, u, _, hs, hu, hq⟩ := Jisr.QaydMafhum.mukhalafa_mashuda (mudaaR m W) (fun _ => bunyaR m) h hk
  simp only [bunyaR, List.mem_flatMap] at hu
  obtain ⟨p, hp, hu⟩ := hu
  exact ⟨p, hp, u, hu, q, hq, hs⟩

/-! ## ٦. الجذرُ والدلالة -/

open Jisr.Tahlil (Q Wazn wazn judhur mashhud kh)

/-- **أوزانُ جذع الاسم** (تعيينُ البنّاء): فَعْل وفَعَل وأخواتُهما، وفاعِل، وفَعال وفَعِيل وفَعُول، ومَفْعَل، ومَفْعُول، ومُفَعِّل. -/
def awzanIsm : List Wazn :=
  [([.any, .any, .any], [0, 1, 2]), ([.v, .h (kh 2 3), .v, .any], [0, 2, 3]),
   ([.v, .v, .h (kh 2 3), .any], [0, 1, 3]), ([.v, .v, .h (kh 11 3), .any], [0, 1, 3]), ([.v, .v, .h (kh 28 3), .any], [0, 1, 3]),
   ([.h (kh 27 0), .s, .v, .any], [1, 2, 3]), ([.h (kh 27 0), .s, .v, .h (kh 28 3), .any], [1, 2, 4]),
   ([.h (kh 27 1), .v, .sx, .v, .any], [1, 2, 4])]

/-- جذعُ الاسم: بلا «ال» ولا تنوين ولا علامة التثنية والجمع. -/
def jidhIsm (w : Wahda) : List Nat :=
  let a := if w.sima.2.1 == 1 then w.khalaya.drop 1 else w.khalaya
  let b := if a.getLast? == some 59 then a.dropLast else a
  if w.sima.2.2.1.2.2 != 0 then b.take (b.length - (if w.idafa then 1 else 2)) else b

def mashhudat (ws : List Wazn) (b : List Nat) : List (List Nat) :=
  ws.flatMap fun (p, ms) => if wazn b p then (judhur b ms).filter mashhud else []

/-- **جذورُ الوحدة المشهودة في عناوين اللسان:** الفعلُ بأوزانه (الماضي بلا لاحقته، والمضارعُ بلا سابقته ولواحقه، والأمر)، والاسمُ بأوزانه. -/
def judhurWahda (w : Wahda) : List (List Nat) :=
  let s := w.khalaya
  (match w.naw with
   | .fil =>
     if w.sima.1 == 0 then mashhudat Jisr.Tahlil.awzanMadi (s.take (s.length - Jisr.Tahlil.madiLahiqa w.sima.2.2.1))
     else if w.sima.1 == 1 then
       (List.range 3).flatMap fun n => mashhudat Jisr.Tahlil.awzanMudari ((s.drop 1).take (s.length - 1 - n))
     else (List.range 3).flatMap fun n => mashhudat Jisr.Tahlil.awzanAmr (s.take (s.length - n))
   | .ism => mashhudat awzanIsm (jidhIsm w)
   | _ => []).eraseDups

def harf (c : Nat) : Char := Dal.hawamil.getD c ' '

/-- الجذرُ نصًّا بحروف عناوين المعجم (`shabaka/jadwal_luzum.py` R1: الهمزةُ «ء»). -/
def jidhrNass (r : List Nat) : String := String.ofList (r.map harf)

/-- **مفاتيحُ الجذر في جدول اللزوم:** الجذرُ، وإن كان في خلايا الوحدة همزةٌ فهو بالهمزة مكانَ الواو المرمِّزة لها (`Tahlil.asl`: «الهمزةُ
    همزةٌ أو ألف»، والألفُ في العنوان تُرمَّز واوًا؛ وعنوانُ الجدول بالهمزة: `shabaka/jadwal_luzum.py` R1). -/
def mafatih (w : Wahda) (r : List Nat) : List String :=
  (if w.khalaya.any (· / 4 == 0) then
     [r] ++ (List.range r.length).filterMap (fun i => if r[i]? == some 28 then some (r.set i 0) else none)
   else [r]).eraseDups.map jidhrNass

open JadwalLuzum QawaninDalala

def raqmT (T : List Saff) (q : Qaida.Qanun Qadiyya) : Nat := (qaidaOf T).qawanin.idxOf q

/-- **ادّعاءُ الصفّ بسلسلته** على قاعدة الجدول: الترادفُ مطابقة، والجزءُ والأصلُ تضمّن، والتعليلُ التزام، والخارجُ مطابقةُ مدلول اللفظ. -/
def iddiaOf (T : List Saff) (r : Saff) : Qaida.Iddia Qadiyya :=
  let l := ism T (lafz r); let m := ism T (maana r); let b := ism T r.b
  match r.naw with
  | .taraduf => ⟨.mutabaqa l b, [.asl (.wad l b), .qanun (raqmT T (qMutabaqa l b))]⟩
  | .juz | .asl => ⟨.tadammun l b, [.asl (.wad l m), .qanun (raqmT T (qMutabaqa l m)), .asl (.juz b m),
      .qanun (raqmT T (qTadammun l m b))]⟩
  | .luzum => ⟨.iltizam l b, [.asl (.wad l m), .qanun (raqmT T (qMutabaqa l m)), .asl (.kharij b m), .asl (.luzum m b),
      .qanun (raqmT T (qIltizam l m b))]⟩
  | .kharij => ⟨.mutabaqa l m, [.asl (.wad l m), .qanun (raqmT T (qMutabaqa l m))]⟩

theorem qanun_raqm (T : List Saff) (r : Saff) (hr : r ∈ T) {q : Qaida.Qanun Qadiyya} (hq : q ∈ qawaninOf T r) :
    (qaidaOf T).qawanin[raqmT T q]? = some q := by
  have hm : q ∈ (qaidaOf T).qawanin := List.mem_flatMap.mpr ⟨r, hr, hq⟩
  have hl := List.idxOf_lt_length_of_mem hm
  unfold raqmT
  rw [List.getElem?_eq_getElem hl, List.getElem_idxOf hl]

theorem asl_sahih (T : List Saff) (r : Saff) (hr : r ∈ T) {p : Qadiyya} (hp : p ∈ aslOf T r) : aslB T p = true :=
  (aslB_iff T p).mpr ⟨r, hr, hp⟩

/-- **كلُّ ادّعاءٍ من صفٍّ يقبله الفاحص** (`Qaida.maqbul`) على قاعدة جدوله، لكلّ جدولٍ ولكلّ صفٍّ فيه. -/
theorem iddia_maqbul (T : List Saff) (r : Saff) (hr : r ∈ T) : Qaida.maqbul (qaidaOf T) (aslB T) (iddiaOf T r) = true := by
  unfold iddiaOf
  cases hn : r.naw <;>
  · simp only [Qaida.maqbul, Qaida.fahs, Qaida.tatbiq]
    have hA : ∀ p ∈ aslOf T r, aslB T p = true := fun p hp => asl_sahih T r hr hp
    have hQ : ∀ q ∈ qawaninOf T r, (qaidaOf T).qawanin[raqmT T q]? = some q := fun q hq => qanun_raqm T r hr hq
    simp only [aslOf, qawaninOf, hn, List.mem_cons, List.not_mem_nil, or_false, forall_eq_or_imp, forall_eq] at hA hQ
    simp only [hA, hQ, ite_true]
    simp [qMutabaqa, qTadammun, qIltizam]

/-- **والادّعاءُ صادقٌ في النموذج** بفروض `QawaninDalala.salama`: الأصولُ صادقة (`hA`، نقلٌ يُراجَع)، والاحتواءُ متعدٍّ. -/
theorem dalala_sadiqa {L α : Type} (W : Dalala.Wad L α) (Z : Dalala.Luzum α) (lf : Nat → L) (mn : Nat → Dalala.Maana α)
    (Fi Taht : Nat → Nat → Prop) (T : List Saff) (r : Saff) (hr : r ∈ T)
    (hA : ∀ a, aslB T a = true → tafsir W Z lf mn Fi Taht a)
    (htadiya : ∀ z c p, Taht z c → Fi c p → Taht z p) :
    tafsir W Z lf mn Fi Taht (iddiaOf T r).qawl :=
  SalamaMaqbul.maqbul_sadiq W Z lf mn Fi Taht (qaidaOf T) (aslB T) (iddiaOf T r) (qaidaOf_shakl T) hA htadiya
    (iddia_maqbul T r hr)

/-! ## ٧. الودائعُ المرشَّحة (تحتاج ختمًا) -/

/-- حملُ الكلمة: حقيقةٌ لغويّة إن شُهد جذرُها، بلا حقيقةٍ شرعيّةٍ ولا عرفيّةٍ مودَعة (مرشَّح)؛ وإلّا «لا حكم». -/
def hamlWahda (w : Wahda) : Mahmul :=
  haml .la .la (if !(judhurWahda w).isEmpty && !w.taqdir then .naam else .ghayr) false none false

def wadaMurashshaha (m : Murashshah) : Wada :=
  ⟨(m.adwar.filter fun p => p.1.naw == .fil || p.1.naw == .ism).map (hamlWahda ·.1), false, false⟩

/-- الحملُ المرشَّح حقيقةٌ لغويّةٌ أو «لا حكم»، لا مجازٌ ولا اشتراك. -/
theorem hamlWahda_qiyam (w : Wahda) : hamlWahda w = .haqiqa .lughawiyya ∨ hamlWahda w = .laHukm := by
  unfold hamlWahda
  split <;> decide

/-! ## ٨. الشواهد -/

open Jisr.Tahlil (lamW yaktubJ zaydun falyaktub wallahu bikulli shayin alimun murashshahun hukmM)

/-- القراءاتُ المرخَّصة بلا تكرار أدوار. -/
def maqbula (ws : List Dal.Kalima) : List Murashshah :=
  ((murashshahun ws).filter fun m => hukmM ws m == .murakhkhas).foldl
    (fun acc m => if acc.any (fun x => x.adwar.map (·.2) == m.adwar.map (·.2)) then acc else acc ++ [m]) []

def irabQiyam (m : Murashshah) : List (Dawr × Hala × Amil) := (irab m).map fun e => (e.dawr, e.hala, e.amil)

/-- **«لَمْ يَكْتُبْ زَيْدٌ»:** الجازمُ مبنيٌّ، والفعلُ مجزومٌ بصفّ «لم» (58)، والفاعلُ مرفوعٌ بالفعل؛ والقوّةُ نفي. -/
theorem shahid_lam :
    (maqbula [lamW, yaktubJ, zaydun]).map irabQiyam =
      [[(.jazim, .mabni, .bina), (.fil, .zahira 3, .saff 58), (.fail, .zahira 1, .fil 1)]] ∧
    (maqbula [lamW, yaktubJ, zaydun]).map (·|> quwwaOf |>.1) = [.nafy] := by
  decide +kernel

/-- **«فَلْيَكْتُبْ»:** الفعلُ مجزومٌ بلام الأمر (61)، والقوّةُ إنشاء (عمودُ الأسلوب «الطلب»)، والفاعلُ مستترٌ جوازًا يحيل إلى ما سبق. -/
theorem shahid_lamAmr :
    (maqbula [falyaktub]).map irabQiyam = [[(.rabit, .laHala, .bina), (.jazim, .mabni, .bina), (.fil, .zahira 3, .saff 61)]] ∧
    (maqbula [falyaktub]).map (·|> quwwaOf |>.1) = [.insha] ∧
    (maqbula [falyaktub]).map (fun m => (ihalat [] 0 m).map fun i => (i.sura, i.marji)) = [[(.mustatar, .murashshahun [])]] := by
  decide +kernel

/-- **«وَاللَّهُ بِكُلِّ شَيْءٍ عَلِيمٌ»:** المبتدأُ مرفوعٌ بالابتداء، والمجرورُ بالباء (40)، والمضافُ إليه بالإضافة، والخبرُ بالمبتدأ؛ والإسنادُ
    إلى «اللَّهُ»؛ والقوّةُ خبرٌ مثبت. -/
theorem shahid_ismiyya :
    (maqbula [wallahu, bikulli, shayin, alimun]).map (fun m => (irab m).map (·.amil)) =
      [[.bina, .ibtida, .bina, .saff 40, .idafa 1, .mubtada 0]] ∧
    (maqbula [wallahu, bikulli, shayin, alimun]).map (·|> quwwaOf |>.1) = [.ithbat] := by
  decide +kernel

/-- **الدلالةُ على صفوف «كتب» الأربعة في `JadwalLuzum.jadwal`:** كلُّ صفٍّ ادّعاءٌ يقبله الفاحص (`iddia_maqbul` على الشاهد): ترادفان مطابقةً لمعنى «علم»،
    وجزءٌ تضمّنًا لـ«علم»، وأصلُ ابن فارس تضمّنًا لـ«جمع». -/
theorem shahid_dalala :
    let T := jadwal.filter (·.a == "كتب")
    (T.map fun r => Qaida.maqbul (qaidaOf T) (aslB T) (iddiaOf T r)) = [true, true, true, true] ∧
    (T.map fun r => (iddiaOf T r).qawl) = [.mutabaqa 0 2, .mutabaqa 3 2, .tadammun 3 2, .tadammun 6 8] := by
  decide

end Rabt
end Nizam
