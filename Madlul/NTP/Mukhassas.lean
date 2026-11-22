/-
  Madlul/NTP/Mukhassas.lean — معالجُ NTP على شبكة المخصّص المختوم: العقدةُ وطريقُها إلى رأسها، والقائلون شهودًا، والتواترُ بالسجلّ وبالشجرة.

  الطلب: أمرُ المالك 2026-11-21 (13:57 بتوقيت عمّان): «انت مفوض بجعل mashru يعمل بشكل متكامل ومتناسق ومترابط ووفعال لتحقيق أقصى النتائج
  من ntp and ntl». والفجوةُ (مقروءةٌ في الجلسة): وكيلُ «صنّف» في `mudir` (`Nizam.Mudir.tasnifNTP`) يعمل على `NTP.Wasl.shabakaWasl`، إحدى عشرة
  عقدةً «شاهدٌ مبنيّ لا مودَع» بأعداد شهودٍ مفروضة، ويقبل بالسجلّ (`NTP.yuqbal`)؛ و`Madlul/NTP/Silsila.lean` و`SilsilaMaajim.lean` لا يبلغهما
  تنفيذيّ. وهنا تعمل دوالّهما المبرهنة على مودَعٍ مختوم.

  **المادّة:** `ntp_mukhassas.tsv` (`scripts/bina_ntp_mukhassas.py`): عقدُ شجرة المخصّص (1996) وأزواجُ «لفظ - شرح» (29622) كما يخرجها
  `shabaka/mukhassas_shabaka.py` من `mukhassas.txt` المختوم، ولكلٍّ إزاحةُ محرفه فيه. فالعقدةُ هنا عنوانُ ابن سيده بعينه (كتاب/باب/فصل/عنوان)
  لا قسمٌ من أقسام `Madlul.Tayin` (إنسان/حيوان/نبات/جماد): ربطُ الكتب بالأقسام بألفاظ عناوينها تصنيفٌ بكلمات العناوين (الدستور م14)، فلم يُبنَ.

  **الشاهد:** القائلُ المسمّى في الزوج («أبو زيد»، «صاحب العين»…)؛ وما لا قائلَ مسمًّى له («بلا نسبة صريحة»، «غيره»، «غير واحد») لا يُعدّ شاهدًا
  (`ghayrMusamma`). ورقمُ القائل في شجرة النقل `1000 + موضعه` في قائمة القائلين، وكتبُه لم تُقرأ مصادرُها (`shajaraQail`: `none`).

  ما هنا (مبرهنٌ لكلّ شبكة):
  ١. `masar`: طريقُ العقدة إلى رأسها بآبائها، أوّلُه هي (`masar_awwal`) وطولُه محدود (`masar_tul`).
  ٢. `qail_maftuh`: سلسلةُ كلّ قائلٍ مفتوحة؛ و`akbar_maftuh`: جماعةٌ كلُّ شهودها مفتوحو السلاسل لا تزيد على واحد؛ فـ**لا يدخل لفظٌ من المخصّص
     الشبكةَ بالتواتر على الشجرة** متى كانت العتبة اثنين فأكثر (`la_yuqbal_bi_shajara`) — حتى تُقرأ مصادرُ كتب القائلين.
  ٣. `adad_le_qailun`: العدُّ بالسجلّ لا يزيد على عدد القائلين المسمّين المتمايزين؛ والمرتبةُ ظنٌّ لا يقين (`rutba_zann`: عضويّةُ الجنس ليست وجودًا).
  ٤. على الشاهد (`shahid`، تسعةُ أسطرٍ من `ntp_mukhassas.tsv` بنصّها يطابقها `tahaqquq/test_ntp_mukhassas.py`): «البلجة» في «الحاجب» تحت
     «كتاب خلق الإنسان» بقائلٍ واحد؛ و«الفزع» بقائلَين مسمّيَين يُقبل بالسجلّ ولا يُقبل بالشجرة. (و«الإفزاع والخوف» أبوه في المخرج «كتاب
     النخل»: هذا ما يُخرجه المستخرِج من رؤوس OpenITI، ولم يُصلَح هنا.)

  حدود (معلنة): الاستخراجُ استخراجُ `mukhassas_shabaka.py` بضجيجه المعلن فيه (لفظٌ حتى ثلاث كلمات قبل الشرطة)؛ والأسماءُ المتعدّدة لقائلٍ واحد
  (أبو علي/الفارسي) لا تُدمج، فالعدُّ بالسجلّ قد يزيد بها، والعدُّ بالشجرة لا يتأثّر؛ والجماعةُ («الكلابيون») قائلٌ واحد. والبحثُ عن اللفظ بعد
  التجريد من الحركات مطابقةٌ تامّة، أو بزيادة «ال» أو حذفها (`badail`) لا غير.
  بلا sorry ولا axiom ولا native_decide.
-/
import Madlul.NTP.SilsilaMaajim

set_option autoImplicit false

namespace NTP
namespace Mukhassas
open NTP.Silsila

/-! ## ١. الشبكة -/

/-- عقدةُ جنسٍ: رقمُها، وأبوها، ونوعُ عنوانها، والعنوان، وإزاحةُ محرفه في `mukhassas.txt`. -/
structure Jins where
  raqm : Nat
  ab : Option Nat
  naw : String
  unwan : String
  mawdi : Nat
deriving Repr, DecidableEq

/-- زوجُ «لفظ - شرح»: رقمُه، وعقدتُه، ولفظُه، وقائلُه، وإزاحتُه. -/
structure Zawj where
  raqm : Nat
  jins : Nat
  lafz : String
  qail : String
  mawdi : Nat
deriving Repr, DecidableEq

structure Shabaka where
  ajnas : List Jins
  azwaj : List Zawj
deriving Repr

def jinsOf (sh : Shabaka) (n : Nat) : Option Jins := sh.ajnas.find? (·.raqm == n)

def abOf (sh : Shabaka) (n : Nat) : Option Nat := (jinsOf sh n).bind (·.ab)

/-- طريقُ العقدة إلى رأسها: هي ثمّ أبوها فأبوه، بوقود k. -/
def masar (sh : Shabaka) : Nat → Nat → List Nat
  | 0, n => [n]
  | k + 1, n => n :: (match abOf sh n with
      | some a => masar sh k a
      | none => [])

theorem masar_awwal (sh : Shabaka) (k n : Nat) : (masar sh k n).head? = some n := by
  cases k <;> simp [masar]

theorem masar_tul (sh : Shabaka) : ∀ k n, (masar sh k n).length ≤ k + 1
  | 0, n => by simp [masar]
  | k + 1, n => by
    simp only [masar]
    split
    · rename_i a _
      have := masar_tul sh k a
      simp only [List.length_cons]; omega
    · simp

/-- الأبُ في الطريق: إن كان للعقدة أبٌ فهو ثاني الطريق. -/
theorem masar_ab (sh : Shabaka) (k n a : Nat) (h : abOf sh n = some a) :
    masar sh (k + 1) n = n :: masar sh k a := by
  simp [masar, h]

/-- عمقُ شجرة المخصّص أربع درجات (رأس/كتاب ← باب ← فصل ← عنوان)؛ والوقودُ ثمانية يزيد عليه. -/
def waqudMasar : Nat := 8

/-! ## ٢. الشهود: القائلون المسمّون -/

/-- ما لا يُعدّ قائلًا مسمًّى. -/
def ghayrMusamma : List String := ["بلا نسبة صريحة", "غيره", "غير واحد"]

/-- البدائل: اللفظُ نفسُه، وبزيادة «ال» أو حذفها. -/
def badail (w : String) : List String :=
  if w.startsWith "ال" then [w, String.ofList (w.toList.drop 2)] else [w, "ال" ++ w]

theorem nafsuhu_badil (w : String) : w ∈ badail w := by
  unfold badail; split <;> simp

def azwajLafz (sh : Shabaka) (w : String) : List Zawj :=
  sh.azwaj.filter (fun z => (badail w).contains z.lafz)

/-- القائلون المسمّون المتمايزون في أزواجٍ، بترتيب ورودهم. -/
def qailun (zs : List Zawj) : List String :=
  (zs.map (·.qail)).filter (fun q => !ghayrMusamma.contains q) |>.eraseDups

/-- رقمُ القائل في شجرة النقل: فوق أرقام الكتب (أكبرُها 99 في `SilsilaMaajim.asma`). -/
def raqmQail (asma : List String) (q : String) : Nat := 1000 + asma.idxOf q

def shuhud (asma : List String) (zs : List Zawj) : List Shahid :=
  (qailun zs).map fun q => ⟨raqmQail asma q, q⟩

/-- شجرةُ النقل مع القائلين: أرقامُ الكتب كما في `SilsilaMaajim.shajara`، والقائلون لم تُقرأ مصادرُ كتبهم. -/
def shajaraQail : Shajara := fun n => if n < 1000 then SilsilaMaajim.shajara n else none

theorem qail_maftuh (k n : Nat) (h : 1000 ≤ n) : maftuh shajaraQail k n = true := by
  cases k with
  | zero => rfl
  | succ k =>
    have : ¬ n < 1000 := by omega
    simp [maftuh, shajaraQail, this]

theorem shuhud_qail (asma : List String) (zs : List Zawj) : ∀ s ∈ shuhud asma zs, 1000 ≤ s.masdar := by
  intro s hs
  simp only [shuhud, List.mem_map] at hs
  obtain ⟨q, _, rfl⟩ := hs
  simp [raqmQail]

/-! ## ٣. التواتر -/

/-- **جماعةٌ كلُّ شهودها مفتوحو السلاسل لا تزيد على واحد:** لا يستقلّ اثنان منهم (`maftuh_la_yustaqill`). -/
theorem akbar_maftuh (m : Shajara) (k f : Nat) (l : List Nat) (h : ∀ w ∈ l, maftuh m k w = true) :
    (akbar m k f l).length ≤ 1 := by
  have hp := akbar_mustaqill m k f l
  have hs := akbar_minha m k f l
  generalize akbar m k f l = r at hp hs
  match r, hp, hs with
  | [], _, _ => simp
  | [_], _, _ => simp
  | x :: y :: _, hp, hs =>
    have hxy := (List.pairwise_cons.1 hp).1 y (by simp)
    exact absurd hxy (maftuh_la_yustaqill m k x y (Or.inl (h x (hs x (by simp)))))

theorem adadS_maftuh (m : Shajara) (k : Nat) (ws : List Nat) (h : ∀ w ∈ ws, maftuh m k w = true) :
    adadS m k ws ≤ 1 :=
  akbar_maftuh m k ws.length ws h

/-- **لا يدخل لفظٌ من المخصّص الشبكةَ بالتواتر على الشجرة** متى كانت العتبة اثنين فأكثر: كتبُ القائلين لم تُقرأ مصادرُها. -/
theorem la_yuqbal_bi_shajara (K : Nat) (hK : 2 ≤ K) (asma : List String) (zs : List Zawj) (k : Nat) :
    yuqbalS K shajaraQail k (shuhud asma zs) = false := by
  have h1 := adadS_maftuh shajaraQail k ((shuhud asma zs).map (·.masdar)) (by
    intro w hw
    obtain ⟨s, hs, rfl⟩ := List.mem_map.1 hw
    exact qail_maftuh k s.masdar (shuhud_qail asma zs s hs))
  simp only [yuqbalS]
  have : ¬ K ≤ adadS shajaraQail k ((shuhud asma zs).map (·.masdar)) := by omega
  simp [this]

theorem length_mutamayyiz_le : ∀ l : List Nat, (mutamayyiz l).length ≤ l.length
  | [] => by simp [mutamayyiz]
  | x :: xs => by
    have := length_mutamayyiz_le xs
    unfold mutamayyiz
    split <;> simp <;> omega

/-- **العدُّ بالسجلّ لا يزيد على عدد القائلين المسمّين المتمايزين.** -/
theorem adad_le_qailun (asma : List String) (zs : List Zawj) : adad (shuhud asma zs) ≤ (qailun zs).length := by
  unfold adad
  have := length_mutamayyiz_le ((shuhud asma zs).map (·.masdar))
  simpa [shuhud] using this

/-- **عضويّةُ الجنس ظنٌّ لا يقين** مهما كثر القائلون (`Muallij.ghayr_wujud_la_yaqin`). -/
theorem rutba_zann (K c : Nat) : rutba K .taht c ≠ .yaqin :=
  ghayr_wujud_la_yaqin K c .taht (by decide)

/-! ## ٤. الجواب -/

def unwanOf (sh : Shabaka) (n : Nat) : String :=
  match jinsOf sh n with
  | some j => s!"{j.unwan} [{j.naw} {n} @{j.mawdi}]"
  | none => s!"[عقدة {n} لا عنوانَ لها]"

def ajnasLafz (zs : List Zawj) : List Nat := (zs.map (·.jins)).eraseDups

def asmaQailin (sh : Shabaka) : List String := (sh.azwaj.map (·.qail)).eraseDups

def ismRutba : Rutba → String
  | .laHukm => "لا حكم (لا شاهدَ مسمًّى)"
  | .zann q => s!"ظنٌّ بقوّة {q}"
  | .yaqin => "يقين"

/-- جوابُ «صنّف» من المخصّص. أوّلُه «لا حكم» ما لم يُقبل بالتواتر على الشجرة (فالوكيلُ «لا حكم» باسمه). -/
def jawab (sh : Shabaka) (w : String) : String :=
  let zs := azwajLafz sh w
  if zs.isEmpty then
    s!"لا حكم: لا لفظَ «{w}» في شبكة المخصّص المختوم ({sh.ajnas.length} عقدة، {sh.azwaj.length} زوجًا؛ بدائلُه {badail w}). الغيابُ ليس امتناعًا."
  else
    let asma := asmaQailin sh
    let sh' := shuhud asma zs
    let nS := adad sh'
    let nT := adadS shajaraQail SilsilaMaajim.waqud (sh'.map (·.masdar))
    let qbT := yuqbalS 2 shajaraQail SilsilaMaajim.waqud sh'
    let ras := if qbT then "مقبولٌ بالتواتر على الشجرة (K = 2)" else
      "لا حكم بالتواتر على الشجرة (K = 2): كتبُ القائلين لم تُقرأ مصادرُها (NTP.Mukhassas.la_yuqbal_bi_shajara)"
    let ajnas := ajnasLafz zs
    let masarat := ajnas.take 5 |>.map fun j =>
      s!"\tالطريق: {" › ".intercalate ((masar sh waqudMasar j).reverse.map (unwanOf sh))}"
    let ql := qailun zs
    s!"{ras}\n\tاللفظ «{w}» في المخصّص: {zs.length} زوجًا في {ajnas.length} عقدة (معلومةٌ سابقة، لا مفهوم: لا شاهدَ واقعٍ مودَع)\n" ++
    "\n".intercalate masarat ++ (if ajnas.length > 5 then s!"\n\t… و{ajnas.length - 5} عقدةً أخرى" else "") ++
    s!"\n\tالقائلون المسمّون ({ql.length}): {"، ".intercalate (ql.take 12)}" ++
    s!"\n\tالعدّ بالسجلّ (NTP.adad): {nS} — {if yuqbal 2 sh' then "يُقبل" else "لا يُقبل"} به عند K = 2؛ والعدّ بالشجرة (Silsila.adadS): {nT}" ++
    s!"\n\tالمرتبة (NTP.rutba، تحت): {ismRutba (rutba 2 .taht nS)}" ++
    s!"\n\tالمواضع (إزاحةُ المحرف في mukhassas.txt): {", ".intercalate ((zs.take 8).map fun z => toString z.mawdi)}"

/-! ## ٥. الشاهد: أسطرٌ من `ntp_mukhassas.tsv` بنصّها -/

def shahid : Shabaka where
  ajnas := [⟨2, none, "كتاب", "كتاب خلق الإنسان", 25218⟩, ⟨25, some 2, "عنوان", "الحاجب", 146681⟩,
            ⟨1138, none, "كتاب", "كتاب النخل", 2656563⟩, ⟨1312, some 1138, "عنوان", "الإفزاع والخوف", 3023496⟩]
  azwaj := [⟨1, 25, "البلجة", "ثابت", 147369⟩, ⟨2, 25, "البلدة", "ثابت", 147369⟩,
            ⟨20927, 1312, "الفزع", "بلا نسبة صريحة", 3023522⟩, ⟨20956, 1312, "الفزع", "أبو عبيد", 3026431⟩,
            ⟨21011, 1312, "الفزع", "أبو زيد", 3029391⟩]

/-- طريقُ «الحاجب» إلى رأسه «كتاب خلق الإنسان». -/
theorem shahid_masar : masar shahid waqudMasar 25 = [25, 2] := by decide +kernel

/-- «البلجة» في عقدةٍ واحدة بقائلٍ واحد، وتوجد بلا «ال» كذلك. -/
theorem shahid_balja :
    ajnasLafz (azwajLafz shahid "البلجة") = [25] ∧ qailun (azwajLafz shahid "بلجة") = ["ثابت"] := by decide +kernel

/-- «الفزع» بقائلَين مسمّيَين («بلا نسبة صريحة» لا يُعدّ): يُقبل بالسجلّ عند K = 2، ولا يُقبل بالشجرة. -/
theorem shahid_faza :
    qailun (azwajLafz shahid "الفزع") = ["أبو عبيد", "أبو زيد"] ∧
    yuqbal 2 (shuhud (asmaQailin shahid) (azwajLafz shahid "الفزع")) = true ∧
    yuqbalS 2 shajaraQail SilsilaMaajim.waqud (shuhud (asmaQailin shahid) (azwajLafz shahid "الفزع")) = false := by
  decide +kernel

end Mukhassas
end NTP
