/-
  Jisr/QabiliyyaJins.lean — برهانُ الترخيص من خاصّة الجنس (أمر المالك 2026-10-28):
  «ذهابُ الولد مرخَّصٌ لأنّ الولدَ إنسانٌ والإنسانَ ينتقل» — نظريةً لا قائمةً مكتوبةً يدًا.

  الفجوة (القفزة): `Madlul/Tayin.lean` يبرهن أنّ الإنسانَ ينتقل وأنّ قابليّةَ الحركة تتبع الانتقال
  (`qabiliyya_tabi_khassa` :315) ، و`Jisr/Utur.lean` يودِع قابليّاتِ «الولد» قائمةً بيد الكاتب (`walad` :326).
  لا نظريةٌ تنقل خاصّةَ الجنس إلى قابليّة الكلمة. هذا الملفّ يسدُّ ذلك دون تعديل شيءٍ قائم.

  المبنيُّ عليه (مستورَدٌ لا مكرَّر): `Tayin.Qism/fusul/ramzQab/ilaMadlul/qabiliyya_tabi_khassa` ،
  `Jisr.Utur.Mahmul/hukmMadlul/waslMadlul/fiHuqul/nisabMahmul/Hukm` ، `Madlul.Wiratha` (الفصولُ من التوريث).
  الموضع: Jisr/ لأنّ البرهان يحتاج `hukmMadlul` (Jisr.Utur) فوق طبقة Madlul — بلا عكسٍ للطبقات (Utur لا يستورد Madlul.Tayin).

  الوسم: **ترخيص/معلومة لا «مفهوم»** (Aql/Maratib.lean:87 `la_mafhum_bila_waqi`).
  مدلولُ الكلمة هنا `ilaMadlul q` (قابليّاتُه مشتقّةٌ `(fusul q).qab.map ramzQab` ، لا قائمةٌ يدًا). لم يُمَسّ `walad` ولا `madlul_shawahid`.

  المسلّمات: `#print axioms` ⊆ {propext, Classical.choice, Quot.sound} (الفعليّ: propext).
-/
import Jisr.Utur
import Madlul.Wiratha

set_option autoImplicit false

namespace Jisr.QabiliyyaJins
open Jisr.Utur Madlul Madlul.Tayin SLGE.Awwalan

/-- الجنسُ مودَعٌ لا مستنتَج (أ): دالّةٌ من المدلول إلى قسمه بنصٍّ مودَع (تُجهَّز صفوفُها وتُعرَض على المالك ليختمها).
هنا معاملٌ حرٌّ: النظريةُ لا تفترض جدولًا بعينه. -/
abbrev Jins := Madlul → Option Qism

/-- مدلولُ الكلمة بوراثةِ جنسها (ب): قابليّاتُه مشتقّةٌ من فصول الجنس ، لا قائمةٌ مكتوبةٌ يدًا. -/
def madlulMin (jins : Jins) (m : Madlul) : Option Madlul := (jins m).map Tayin.ilaMadlul

/-- قابليّاتُ مدلول الجنس q = قابليّاتُ حركته مرمَّزةً (مشتقّةٌ من `fusul` ، التي هي من التوريث في Wiratha). -/
theorem qabiliyyat_ilaMadlul (q : Qism) :
    (Tayin.ilaMadlul q).qabiliyyat = (Tayin.fusul q).qab.map Tayin.ramzQab := rfl

/-- **(د) النظريةُ العامّة:** إن كان جنسُ الكلمة q ، وكان q ينتقل ذاتيًّا (الانتقالُ خاصّية) ، وكان e قابليّةَ حركةٍ لـ q بنصٍّ
(e في قابليّات حركة q) ، فإسنادُ تلك القابليّة إلى مدلولها الموروث **مرخَّص**. (قفزةُ الاستدلال مبرهنةٌ لا مطابَقةٌ على قائمة.) -/
theorem tarkhis_min_jins (jins : Jins) (m : Madlul) (q : Qism) (e : Nat) (dm : Madlul)
    (hj : jins m = some q)
    (hdm : madlulMin jins m = some dm)
    (_hi : (Tayin.fusul q).intiqal = .naam)
    (he : ((Tayin.fusul q).qab.map Tayin.ramzQab).contains e = true) :
    hukmMadlul ⟨dm, .qabiliyya e, .isnadiyya⟩ = .murakhkhas := by
  have hdmq : dm = Tayin.ilaMadlul q := by
    simp only [madlulMin, hj, Option.map_some] at hdm; exact (Option.some.inj hdm).symm
  subst hdmq
  have hi : ibtidaMadlul ⟨Tayin.ilaMadlul q, .qabiliyya e, .isnadiyya⟩ = true := by
    simp [ibtidaMadlul, Tayin.ilaMadlul, SLGE.Cat.roles]
  have hw : waslMadlul ⟨Tayin.ilaMadlul q, .qabiliyya e, .isnadiyya⟩ = .murakhkhas := by
    have hf : fiHuqul (Tayin.ilaMadlul q) (.qabiliyya e) = true := by
      simp only [fiHuqul, Tayin.ilaMadlul]; exact he
    simp only [waslMadlul, nisabMahmul, List.contains, List.elem, hf]; rfl
  simp only [hukmMadlul, hukmQayd, waqfMadlul, hi, hw, ofBool, damm, beq_self_eq_true, ite_true]

/-- **(د-عكس) الحافظُ لـم13:** قابليّةُ حركةٍ ليست في قابليّات الجنس ، بنسبةٍ إسناديّة ، ← **لا حكم** (لا ممتنع): غيابُ الشاهد
ليس امتناعًا. فما لا نصَّ له (كطيرانِ الولد) يبقى «لا حكم» كما في شاهد Utur. -/
theorem laHukm_bila_qabiliyya (q : Qism) (e : Nat)
    (he : ((Tayin.fusul q).qab.map Tayin.ramzQab).contains e = false) :
    hukmMadlul ⟨Tayin.ilaMadlul q, .qabiliyya e, .isnadiyya⟩ = .laHukm := by
  have hi : ibtidaMadlul ⟨Tayin.ilaMadlul q, .qabiliyya e, .isnadiyya⟩ = true := by
    simp [ibtidaMadlul, Tayin.ilaMadlul, SLGE.Cat.roles]
  have hw : waslMadlul ⟨Tayin.ilaMadlul q, .qabiliyya e, .isnadiyya⟩ = .laHukm := by
    have hf : fiHuqul (Tayin.ilaMadlul q) (.qabiliyya e) = false := by
      simp only [fiHuqul, Tayin.ilaMadlul]; exact he
    simp only [waslMadlul, nisabMahmul, List.contains, List.elem, hf]; rfl
  simp only [hukmMadlul, hukmQayd, waqfMadlul, hi, hw, ofBool, damm, beq_self_eq_true, ite_true]

/-- **النسبةُ تحسم أوّلًا:** القابليّةُ لا تحتمل الإضافة (nisabMahmul) ← ممتنعٌ ولو كان الكود في القابليّات. -/
theorem idafiyya_mumtani (q : Qism) (e : Nat) :
    hukmMadlul ⟨Tayin.ilaMadlul q, .qabiliyya e, .idafiyya⟩ = .mumtani := by
  have hw : waslMadlul ⟨Tayin.ilaMadlul q, .qabiliyya e, .idafiyya⟩ = .mumtani := by
    simp only [waslMadlul, nisabMahmul, List.contains, List.elem]; rfl
  have hq : hukmQayd ⟨Tayin.ilaMadlul q, .qabiliyya e, .idafiyya⟩ = .mumtani := by
    unfold hukmQayd; exact (damm_mumtani _ _).2 (Or.inr hw)
  unfold hukmMadlul; exact (damm_mumtani _ _).2 (Or.inl hq)

/-- **(و) على الشاهد (decide):** الحالاتُ المجمَّدة J01–J20 (`tahaqquq/dawabit/qabiliyya_jins/halat.json`): الإنسانُ/الحيوانُ يُرخَّص
لهما كلُّ قابليّات الحركة (11–15) إسنادًا ؛ وما خرج عنها (10، 16) لا حكم ؛ والجمادُ والنباتُ (لا قابليّةَ لهما) لا حكم ؛ والإضافةُ ممتنعة. -/
theorem shawahid_jins :
    -- J01..J05 الإنسان يُرخَّص له 11..15
    hukmMadlul ⟨Tayin.ilaMadlul .insan, .qabiliyya 11, .isnadiyya⟩ = .murakhkhas ∧
    hukmMadlul ⟨Tayin.ilaMadlul .insan, .qabiliyya 12, .isnadiyya⟩ = .murakhkhas ∧
    hukmMadlul ⟨Tayin.ilaMadlul .insan, .qabiliyya 13, .isnadiyya⟩ = .murakhkhas ∧
    hukmMadlul ⟨Tayin.ilaMadlul .insan, .qabiliyya 14, .isnadiyya⟩ = .murakhkhas ∧
    hukmMadlul ⟨Tayin.ilaMadlul .insan, .qabiliyya 15, .isnadiyya⟩ = .murakhkhas ∧
    -- J06,J07 خارج قابليّات الإنسان ← لا حكم
    hukmMadlul ⟨Tayin.ilaMadlul .insan, .qabiliyya 16, .isnadiyya⟩ = .laHukm ∧
    hukmMadlul ⟨Tayin.ilaMadlul .insan, .qabiliyya 10, .isnadiyya⟩ = .laHukm ∧
    -- J08,J09 الإضافة ممتنعة
    hukmMadlul ⟨Tayin.ilaMadlul .insan, .qabiliyya 11, .idafiyya⟩ = .mumtani ∧
    hukmMadlul ⟨Tayin.ilaMadlul .insan, .qabiliyya 16, .idafiyya⟩ = .mumtani ∧
    -- J10..J12 الحيوان يُرخَّص
    hukmMadlul ⟨Tayin.ilaMadlul .hayawan, .qabiliyya 12, .isnadiyya⟩ = .murakhkhas ∧
    hukmMadlul ⟨Tayin.ilaMadlul .hayawan, .qabiliyya 11, .isnadiyya⟩ = .murakhkhas ∧
    hukmMadlul ⟨Tayin.ilaMadlul .hayawan, .qabiliyya 15, .isnadiyya⟩ = .murakhkhas ∧
    -- J13,J14
    hukmMadlul ⟨Tayin.ilaMadlul .hayawan, .qabiliyya 16, .isnadiyya⟩ = .laHukm ∧
    hukmMadlul ⟨Tayin.ilaMadlul .hayawan, .qabiliyya 11, .idafiyya⟩ = .mumtani ∧
    -- J15,J16,J17 الجماد لا قابليّة له
    hukmMadlul ⟨Tayin.ilaMadlul .jamad, .qabiliyya 11, .isnadiyya⟩ = .laHukm ∧
    hukmMadlul ⟨Tayin.ilaMadlul .jamad, .qabiliyya 12, .isnadiyya⟩ = .laHukm ∧
    hukmMadlul ⟨Tayin.ilaMadlul .jamad, .qabiliyya 11, .idafiyya⟩ = .mumtani ∧
    -- J18,J19,J20 النبات لا قابليّة له
    hukmMadlul ⟨Tayin.ilaMadlul .nabat, .qabiliyya 11, .isnadiyya⟩ = .laHukm ∧
    hukmMadlul ⟨Tayin.ilaMadlul .nabat, .qabiliyya 13, .isnadiyya⟩ = .laHukm ∧
    hukmMadlul ⟨Tayin.ilaMadlul .nabat, .qabiliyya 13, .idafiyya⟩ = .mumtani := by
  decide

end Jisr.QabiliyyaJins
