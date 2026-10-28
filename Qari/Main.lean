/-
  Qari/Main.lean — القارئ: نصٌّ عربيٌّ مشكول ← خلايا (الدال وحده) ← القانون (ابتداء/وصل/وقف) ← المقاطع
  ← المخزن (المدلول): المنطوق (مطابقة وتضمّن) والمفهوم (التزام)، بمراتب المخرج ووسم كلّ قول.
  والجملة: تركيب الكلمات في الوصل على آلة المالك `Msent` (Dal/Jumla.lean): سقوط همزة الوصل بإصلاحها الأدنى،
  وحدّ الكلمة 116 بين ما سواها؛ والتقطيع كلماتٍ صوتيّةً ومقاطعَ، صحيحٌ بالبناء وواحدٌ بمبرهنة المالك.

  ما يُخمَّن: لا شيء. ما ليس في جدول المخارج أو لم يُودَع قرارُه يُرفض باسمه (الدستور م5):
  الحرف بلا حركة في غير آخر الكلمة، الألف المحرّكة في أوّل الكلمة، والحرف الأخير بلا حركة في غير آخر الجملة
  (الوصل يحتاج حركته).
  والكلمةُ تُقرأ على تحصيلها (`Dal/QiraaTahsil.lean` على `Dal/Tahsil.lean`): تُقطع مقاطعَ بمواضعها بنقاط الرمز، فالمقطعُ المرخَّص
  خلاياه بعينها، والفاسدُ رفضٌ للكلمة باسم سببه (ومنه علامتان على حرفٍ واحد)، والمعلَّقُ باسم قاعدته وسيطُه من الوسائط أدناه
  (`wasitOf`)، أو رفضٌ باسمها إن لم يكن له وسيطٌ في موضعه (التطويلُ بعلامة، وهمزةُ الوصل في غير أوّل الكلمة أو بعلامة، والممدودةُ
  بعلامة، والمقصورةُ أوّلَ الكلمة أو بعلامةٍ بعد تنوين الفتح). ولكلّ خليّةٍ موضعُ مقطعها وأصلُها في المخرج (`qiraa_shahada`).
  قرارات الوقف والرسم من المودَعين «متن قطر الندى» (باب الوقف في الأفصح L440–447، وفصل همزة الوصل L449–453) و«ألفية ابن
  مالك» (باب الوقف L1131، L1136، L1142) — شاهدان مستقلّان. قرارا الوقف (ة، التنوين) على الموقوف عليه، وهو هنا آخرُ النصّ
  المعطى (وسيط معلَن: الوقف حيث ينتهي النصّ)؛ وقرارات الرسم (ى، ألف الجماعة) وهمزة الوصل في كلّ موضع:
  * التاء المربوطة في الوقف هاءٌ («على نحو رحمة بالهاء» L441؛ «في الوقف تا تأنيث الاسم ها جعل» L1142)، ساكنةٌ («وغيرها
    التأنيث من محرك سكنه» L1136)؛ وفي الوصل تاءٌ بحركتها.
  * التنوين في الوقف: بعد الفتح ألفٌ («رأيت زيدا بالألف» L442–443؛ «تنوينا إثر فتح اجعل ألفا» L1131)، وفي غيره حذفٌ
    («وتلو غير فتح احذفا» L1131) ويسكن الحرف (L1136). والألف المقصورة بعد تنوين الفتح («الفتى» L445) ألفُ التنوين.
  * الألف المقصورة ألفٌ رُسمت ياءً («وترسم الألف ياء إن تجاوزت الثلاثة … أو كان أصلها الياء» L444–445): تُقرأ ألفًا.
  * الألف بعد واو الجماعة تُكتب («وتكتب الألف بعد واو الجماعة كقالوا دون الأصلية» L443–444)؛ وأنّها لا تُنطق وسيطٌ معلَن. وهي في التحصيل
    ألفٌ (أو مقصورةٌ في الوسيط) مجرّدةٌ لا يليها شيء، بعد واوٍ مجرّدةٍ أو ساكنةٍ تليها؛ وبعد واوٍ مشدَّدةٍ بلا حركة حرفُ مدّ، وإن تلاها تطويلٌ
    مجرّد («قَالُواـ»، «قَالُوىـ») فألفٌ منطوقة.
  * حركة همزة الوصل وسيطُ المالك `waslHaraka` (ضمٌّ إن ضُمّ الثالث، وفتحٌ مع أل، وكسرٌ في الباقي)؛ شاهدُه في القطر أمثلةُ
    الأمر و«ال» («اقتل واغز واغزي بضمهن، واضرب وامشوا واذهب بكسر كالبواقي … والغلام وايمن الله في القسم بفتحهما» L449–453)؛
    وأسماءُ الفصل (اسم، است، ابن، امرئ، امرأة…) «بكسر» (L449) لا يشملها الوسيط: «امْرُؤٌ» يُخرجها بالضمّ — فجوةٌ معلَنة.
  الوسائط المعلنة، مذكورة في المخرج (ومنها ما صار قاعدةَ ترخيصٍ في `Dal/Tahsil.lean`: مقعدُ الهمزة، والشدّةُ مع الحركة، وحرفُ المدّ؛
  والباقي وسائطُ لمقاطع التحصيل المعلَّقة بأسماء قواعدها في `Dal/QiraaTahsil.lean`):
  * مقاعد الهمزة (أ إ ؤ ئ) همزةُ قطع (ء = 0)؛ آ = همزة مفتوحة ثمّ ألف مدّ.
  * الألف المجرّدة في أوّل الكلمة (أو ٱ) همزةُ وصل: تُحذف من الخلايا، وفي الابتداء تُصلح بـ `SLGE.Law.ibtidaForm`
    (فتحة مع «ال»، وإلّا بحسب حركة الثالث — وسيط المالك `waslHaraka`)؛ وفي الوصل تسقط بإصلاح المالك (Hamza.lean).
    ولا تكون إلّا قبل ساكن (Hamza.lean)؛ فألفٌ مجرّدة قبل متحرّك تُرفض باسمها.
  * لام التعريف بلا علامة قبل حرفٍ مشدّد: مدغمةٌ فيه، لا خلية لها (الشدّة في النصّ شاهدُ الإدغام).
  * الشدّة: ساكنٌ ثمّ متحرّكٌ من الحامل نفسه. التنوين في الوصل: حركةٌ ثمّ نون ساكنة (وألفُ التنوين بعد الفتحتين لا تُنطق).
  * الحرف الأخير بلا حركة في آخر الجملة: ساكنٌ للوقف. ا/و/ي بلا حركة في غير الأوّل: ساكنة (مدًّا أو غيرَه، والقانون يحكم)؛
    وهي في التحصيل حرفُ مدٍّ مرخَّص، والوسيطُ يُسكّنها كذلك في كلمةٍ هي واوٌ أو ياءٌ وحدها، وتحت شدّةٍ بلا حركة.
  * التطويلُ المجرّد مقطعٌ في التحصيل بلا خليّة (وكان القارئ يحذفه قبل القراءة): آخرَ الكلمة بعد التنوين أو التاء المربوطة أو الشدّة بلا
    حركة أو المقصورة لا يُعدّ في وسائطها («رَدّـ» آخرُها الدال)، وفي غير ذلك يفصل ما قبله عمّا بعده كأيّ مقطع (فـ«كَتَبـ» تُرفض على «ب»،
    و«كِتَابًـا» ألفُها بعده حرفُ مدّ، و«قَالُواـ» ألفُها منطوقة).
  * البحث في المخزن باللفظ مجرَّدًا من الحركات كما يكتبه المعجم.
  التشغيل: qari <سجلّ المودَعات> <المخزن> <نصّ مشكول…>
-/
import Dal.Jumla
import Dal.QiraaTahsil
import Faahis.Lib
import Nizam.Aqd
import Jisr.NassItar

open Dal SLGE SLGE.Law QawaninDalala Qaida Mawsua

/-! ## ١. من الحروف إلى الخلايا: على التحصيل (`Dal/QiraaTahsil.lean`) -/

structure Qiraa where
  khalaya   : List Nat := []       -- الرموز 4c+s بلا همزة الوصل
  wasl      : Bool := false        -- بدأت بهمزة وصل
  al        : Bool := false        -- همزتها همزة «أل» (لامٌ ساكنة أو مدغمة)
  mulahazat : List String := []
  /-- كلُّ خليّةٍ بموضع مقطعها في الكلمة وأصلِها: مقطعٌ مرخَّص، أو وسيطٌ لمقطعٍ معلَّقٍ باسم قاعدته (`qiraa_shahada`). -/
  mawadi    : List Dal.QiraaTahsil.KhaliyaQ := []

/-- تحليل كلمة مشكولة إلى خلايا على تحصيلها (`Dal.QiraaTahsil.qiraa`)؛ الرفض باسمه. `akhirJumla`: الكلمة آخر الجملة (فيجوز الوقف
    على ساكن). -/
def tahlil (w : String) (akhirJumla : Bool := true) : Except String Qiraa :=
  match Dal.QiraaTahsil.qiraa w.toList akhirJumla with
  | .ok r => .ok { khalaya := r.khalaya.map (·.raqm), wasl := r.wasl, al := r.al, mulahazat := r.mulahazat, mawadi := r.khalaya }
  | .error e => .error e

/-- الكلمة كما يسلّمها القارئ إلى التركيب (Dal/Jumla.lean). -/
def kalima (q : Qiraa) : Kalima := ⟨q.khalaya, q.wasl, q.al⟩

/-- تجريد اللفظ من الحركات للبحث في المخزن. -/
def mujarrad (w : String) : String :=
  String.ofList (w.toList.filter fun c => !(['َ','ُ','ِ','ْ','ّ','ً','ٌ','ٍ','ـ'].contains c))

def halaIsm (s : Nat) : String := match s with | 0 => "فتحة" | 1 => "ضمّة" | 2 => "كسرة" | _ => "سكون"

def khaliyaIsm (a : Nat) : String :=
  if a == 116 then "|" else s!"{Dal.harf ⟨a / 4 % 29, Nat.mod_lt _ (by decide)⟩}/{halaIsm (a % 4)}({a})"

def nawIsm : NawMaqta → String
  | .CV => "CV" | .CVV => "CVV" | .CVC => "CVC" | .CVVC => "CVVC" | .CVCC => "CVCC" | .CVVCC => "CVVCC"

def silsilaIsm (l : List Nat) : String := " ".intercalate (l.map khaliyaIsm)

/-- الخليّةُ بموضع مقطعها وأصلِها: مقطعٌ مرخَّص في التحصيل، أو وسيطُ القارئ لمقطعٍ معلَّقٍ باسم قاعدته. -/
def aslIsm (x : Dal.QiraaTahsil.KhaliyaQ) : String :=
  s!"{khaliyaIsm x.raqm} [{x.a},{x.b}) " ++ match x.asl with
    | .tahsil => "مقطعٌ مرخَّص"
    | .wasit q => s!"وسيطٌ لـ«{q}»"

/-! ## ٢أ. العقدُ الواحد (Nizam/Aqd.lean): الحكمُ بالمنفّذ البتّيّ `hukmB`، و`kull_ma_kull` تجعله حكمَ المواصفة -/

def nawAqdIsm : JadwalLuzum.Naw → String
  | .juz => "جزء" | .taraduf => "ترادف" | .luzum => "لزوم" | .kharij => "خارج" | .asl => "أصل"

def mujamIsm : JadwalLuzum.Mujam → String
  | .lisan => "لسان العرب" | .maqayis => "مقاييس اللغة"

def irabIsm : SLGE.Wad.Irab → String
  | .raf => "الرفع" | .nasb => "النصب" | .jarr => "الجرّ" | .jazm => "الجزم"

def jidhrIsm (r : Nat) : String := String.ofList ((Nizam.Aqd.fakkRamz r).map fun c => hawamil.getD c '?')

def siyaghIsm (b : Nat) : String :=
  let l := [(Jisr.Iqtiran.SighaFil.madin, "ماضٍ"), (.amr, "أمر"), (.mudari, "مضارع")].filter
    fun (s, _) => b.testBit (Nizam.Aqd.rutbaSigha s)
  if l.isEmpty then "لا مرشَّح" else " · ".intercalate (l.map (·.2))

def hukmAqdIsm : Nizam.Hukm Nizam.Aqd.Qiraa → String
  | .murakhkhas q => s!"مرخَّص (يحمل قراءتَه: مرشَّح الجذر «{jidhrIsm q.jidhr}»، {match q.haal with | some h => halaIsm h | none => "لا حال"}، صيغةُ الفعل إن كان فعلًا: {siyaghIsm q.sigha})"
  | .laHukm => "لا حكم"
  | .mumtani s => s!"ممتنع — {s}"

def allNaw : List JadwalLuzum.Naw := [.juz, .taraduf, .luzum, .kharij, .asl]

/-- الكلمةُ في العقد: القانونُ بجدول البتّات، والقراءة، والحكمُ لكلّ صفٍّ في مادّة جذرها، و«لا حكم» لكلّ نوعٍ لا صفَّ له. -/
def iqraAqd (l : List Nat) (wasl : Bool) : IO Unit := do
  -- حقولُ القانون والجذر والحال والصيغة لا تتعلّق بنوع العلاقة؛ تُقرأ من أيّ عقد.
  let A := Nizam.Aqd.Mashru .juz
  IO.println "  العقد الواحد (Nizam.Aqd؛ المبرهنة kull_ma_kull):"
  let qb := A.qanunB l
  let kama := Nizam.Aqd.kamaB l
  let baad := Nizam.Aqd.baadB l
  let qabul (b : Bool) : String := if b then "مقبولة" else "ممتنعة"
  IO.println s!"    القانون (إطار الدالّ dalOK = القانونان معًا، dalOK_taqatu؛ بجدول البتّات runB): {qabul qb} — على الخلايا كما هي (Fwaqf ∘ run): {qabul kama}؛ بعد تسكين الآخر (complete'): {qabul baad}"
  if !qb then
    let sabab := match Nizam.Aqd.hukmB A l 0 with
      | .mumtani s => s
      | _ => "؟"
    IO.println s!"    الحكم (hukmB): ممتنع — {sabab}، بأيّ مدلولٍ في كلّ عقدٍ Mashru (mumtani_asbab)"
    return
  let haal := match A.haalB l with
    | some h => s!"{halaIsm h} ({h})"
    | none => "لا حكم"
  IO.println s!"    القراءة (حقولُ العقد): حال الآخر {haal}؛ مرشَّحو صيغة الفعل إن كان فعلًا (Jisr.Iqtiran، قطر L65): {siyaghIsm (A.sighaB l)}"
  match A.haalB l with
  | some h =>
    match Nizam.Aqd.irabMurashshah h with
    | some r => IO.println s!"    حال الآخر إعرابًا إن كان معربًا والحركةُ حركةَ إعراب (Bridge.irabState، قطر الندى L77–78): {irabIsm r} — مرشَّح"
    | none => IO.println "    حال الآخر إعرابًا: لا حكم — السكونُ في الآخر وقفٌ أو جزمٌ أو بناء، أو حرفُ مدٍّ أو نونُ تنوينٍ أو هاءُ وقف (irabMurashshah_la_jazm)"
  | none => pure ()
  match A.jidhrB l with
  | none =>
    IO.println "    الجذر: لا حكم — الإسقاطُ لثلاث خاناتٍ حواملُها سالمة (لا ا ي و) وحدها (نطاقٌ معلَن)؛ فالحكم «لا حكم» بأيّ مدلول"
  | some r =>
    IO.println s!"    مرشَّح الجذر: «{jidhrIsm r}» (رمزُه {r} بحقول خمسة بتّات، fakk_ramz؛ حواملُه سالمةٌ بـ SoundR، jidhr_salim) — مرشَّحٌ لا هويّة: المزيدُ والأدواتُ والضمائرُ لا تُميَّز بعد"
    if wasl then
      IO.println "    ملاحظة العقد: في أوّلها همزةُ وصلٍ مُصلَحة — المرشَّحُ يشمل حرفًا زائدًا، فليس جذرًا"
    let rows := JadwalLuzum.jadwal.filter fun s => Nizam.Aqd.ramzNass s.a == r
    if !rows.isEmpty then
      IO.println s!"    الحكم بالشواهد (hukmB؛ JadwalLuzum، في مادّة الجذر لا في صيغة الكلمة):"
      for s in rows do
        let h := Nizam.Aqd.hukmB (Nizam.Aqd.Mashru s.naw) l (Nizam.Aqd.ramzNass s.b)
        IO.println s!"      {nawAqdIsm s.naw} ← «{s.b}» بلفظ «{s.w}»: {hukmAqdIsm h} ({mujamIsm s.mujam} س{s.satr})"
    let ghaib := allNaw.filter fun n => !rows.any (·.naw == n)
    if !ghaib.isEmpty then
      IO.println s!"    لا حكم بأيّ مدلول في: {" · ".intercalate (ghaib.map nawAqdIsm)} — لا صفَّ بها لمرشَّح الجذر «{jidhrIsm r}»؛ الغيابُ ليس امتناعًا (la_shahid_la_hukm)"

/-! ## ٢. قراءة الكلمة وحدها -/

def iqraKalima (h : Hal) (b : Bina) (w : String) (q : Qiraa) : IO Unit := do
  let l := ibtida (kalima q)
  IO.println s!"  الخلايا: {silsilaIsm l}"
  IO.println s!"  أصلُ الخلايا بمواضعها في الكلمة بنقاط الرمز (Dal.QiraaTahsil، qiraa_shahada{if q.wasl then "؛ بلا همزة الوصل" else ""}): {" · ".intercalate (q.mawadi.map aslIsm)}"
  for m in q.mulahazat do IO.println s!"  ملاحظة: {m}"
  if q.wasl then IO.println s!"  ملاحظة: همزة الوصل أُصلحت بـ ibtidaForm (isAl={q.al}) — حركتها وسيط المالك waslHaraka (شاهده قطر الندى L449–453)"
  let waqf := Fwaqf (run 0 l)
  let wasl := Fwasl (run 0 l)
  IO.println s!"  على الخلايا كما هي (موقوفًا عليها Fwaqf ∘ run: مكوّنُ القانون dalOK؛ وفي الوصل Fwasl ∘ run: ليس من القانون — وصلُ dalOK غيرُ فارغةٍ و run ≠ 96، wasl_ghayr_Fwasl): موقوفًا عليها {if waqf then "مرخَّصة" else "ممتنعة"}؛ في الوصل {if wasl then "مرخَّصة" else "ممتنعة"}"
  if waqf then
    match qatta l with
    | some sy => IO.println s!"  المقاطع ({sy.length}): {" · ".intercalate (sy.map fun x => nawIsm (nawMaqta x))} — واحدٌ بمبرهنة qatta_wahid"
    | none => IO.println "  المقاطع: لم يُقسَّم (خلل في التقطيع التنفيذيّ؛ الوجود مبرهن في word_structure)"
  iqraAqd l q.wasl
  -- المدلول من المخزن
  let key := mujarrad w
  let yuwafiq (p : Qadiyya) : Bool := match p with
    | .mutabaqa l _ | .tadammun l _ | .iltizam l _ => h.dh.ism l == key
    | _ => false
  let mantuq := h.iddiaat.filter fun (_, p, _, _, _) => match p with
    | .mutabaqa .. | .tadammun .. => yuwafiq p | _ => false
  let mafhum := h.iddiaat.filter fun (_, p, _, _, _) => match p with
    | .iltizam .. => yuwafiq p | _ => false
  IO.println s!"  المدلول باللفظ «{key}»:"
  if mantuq.isEmpty then IO.println "    المنطوق (مطابقة/تضمّن): لا مدخل في المخزن — لا حكم؛ الغياب ليس امتناعًا."
  else
    IO.println s!"    المنطوق (مطابقة/تضمّن): {mantuq.size}"
    for (_, p, _, ks, _) in mantuq do
      -- `maqbulA` هو `maqbul b.q` بعينه (`Qaida.maqbulA_eq` بـ `b.hq`)
      if maqbulA b.qs b.aslB ⟨p, ks⟩ then tatabbu h b ⟨p, ks⟩
      else IO.println s!"      {qadiyyaIsm h.dh p}: مرفوض — سلسلة لا يقبلها الفاحص"
  if mafhum.isEmpty then IO.println "    المفهوم (التزام): لا مدخل في المخزن — لا حكم."
  else
    IO.println s!"    المفهوم (التزام): {mafhum.size}"
    for (_, p, _, ks, _) in mafhum do
      if maqbulA b.qs b.aslB ⟨p, ks⟩ then tatabbu h b ⟨p, ks⟩
      else IO.println s!"      {qadiyyaIsm h.dh p}: مرفوض — سلسلة لا يقبلها الفاحص"

/-! ## ٣. الجملة في الوصل -/

def islahIsm : Islah → String
  | .la => "سقطت همزة الوصل بعد متحرّك بلا إصلاح (wasl_after_mover)"
  | .hadhfMadd => "سقطت همزة الوصل وحُذف المدّ قبلها لالتقاء الساكنين (wasl_after_madd)"
  | .tahrik => s!"سقطت همزة الوصل وحُرّك الساكن قبلها بال{halaIsm harakatIltiqa} لالتقاء الساكنين (wasl_after_closed؛ الحركة وسيط معلَن)"

def kalimaRaqm (ws : Array String) (i : Nat) : String := s!"الكلمة {i} «{ws.getD (i - 1) "?"}»"

def khalalIsm (ws : Array String) : Khalal → String
  | .mayyita i => s!"ممتنعة عند {kalimaRaqm ws i}: القانون يميت السلسلة في موضعها"
  | .laTusal i => s!"{kalimaRaqm ws i} لا توصل بما بعدها: آخرها ساكنان (الوقف لا الوصل)"
  | .laHukm i => s!"لا حكم عند {kalimaRaqm ws i}: همزة وصل بعد حالةٍ ليس عند المالك إصلاحٌ لها"
  | .farigha => "لا كلمات"

def iqraJumla (ws : Array String) (qs : Array Qiraa) : IO Unit := do
  IO.println s!"الجملة في الوصل ({ws.size} كلمات):"
  let n := rakkib (qs.toList.map kalima)
  for (i, s) in n.islahat do IO.println s!"  الوصل عند {kalimaRaqm ws i}: {islahIsm s}"
  IO.println s!"  السلسلة: {silsilaIsm n.silsila}"
  match n.khalal with
  | some k => IO.println s!"  القانون (آلة الجملة Msent): {khalalIsm ws k}"
  | none =>
    if Fwaqf (run 0 n.silsila) then
      IO.println "  القانون (آلة الجملة Msent): مرخَّصة موقوفًا على آخرها — لها تقطيع (jumla_murakhkhasa)"
      match qattaJumla n.silsila with
      | some S =>
        let ks := S.map fun w => "[" ++ " · ".intercalate (w.map fun x => nawIsm (nawMaqta x)) ++ "]"
        IO.println s!"  الكلمات الصوتية ({S.length}): {" ".intercalate ks} — واحدٌ بمبرهنة qattaJumla_wahid"
      | none => IO.println "  الكلمات الصوتية: لم تُقطَّع (خلل في التقطيع التنفيذيّ؛ الوجود مبرهن في sent_structure)"
    else IO.println "  القانون (آلة الجملة Msent): ممتنعة موقوفًا على آخرها (آخرها معلَّق على الوصل)"

/-- **وضعُ القياس** (التسجيل المسبق للمرحلة «د»: `hawkama/tasjil_qiyas_d.md`): لكلّ سطرٍ «مفتاح⇥كلمة» في الملفّ سطرٌ واحد
    بحقولٍ ثابتة، والكلمةُ وحدها موقوفًا عليها (`tahlil w true`):
    `مفتاح⇥RAFD⇥سبب الرفض`، أو
    `مفتاح⇥QABUL⇥الخلايا⇥على الخلايا (Fwaqf ∘ run 0)⇥بعد التسكين (Fwaqf ∘ run 0 ∘ waqfForm = complete')⇥قانون العقد⇥مرشَّح الجذر⇥حال الآخر⇥الإعراب المرشَّح`
    (القيم 0/1، و«-» لا حكم). لا يقرأ سجلًّا ولا مخزنًا. -/
def qiyas (path : String) : IO UInt32 := do
  let A := Nizam.Aqd.Mashru .juz
  let b (x : Bool) : String := if x then "1" else "0"
  for line in ← IO.FS.lines path do
    match line.splitOn "\t" with
    | [k, w] =>
      match tahlil w true with
      | .error e => IO.println s!"{k}\tRAFD\t{e}"
      | .ok q =>
        let l := ibtida (kalima q)
        let jidhr := match A.jidhrB l with | some r => jidhrIsm r | none => "-"
        let haal := match A.haalB l with | some h => toString h | none => "-"
        let irab := (((A.haalB l).bind Nizam.Aqd.irabMurashshah).map irabIsm).getD "-"
        IO.println s!"{k}\tQABUL\t{" ".intercalate (l.map toString)}\t{b (Fwaqf (run 0 l))}\t{b (Fwaqf (run 0 (waqfForm l)))}\t{b (A.qanunB l)}\t{jidhr}\t{haal}\t{irab}"
    | _ => IO.println s!"{line}\tKHALAL\tسطرٌ ليس «مفتاح⇥كلمة»"
  return 0

/-! ## من النصّ إلى الإطار (الحزمة P4، `Jisr/NassItar.lean`) -/

/-- كلماتُ الجملة خلايا في الوصل كلُّها (`tahlil w false`: الجملةُ تُقرأ في الوصل)، أو رفضُ أوّل كلمةٍ لا تُقرأ باسمه. -/
def kalimatJumla (s : String) : Except String (List Kalima) := do
  let ws := (s.splitOn " ").filter (· != "")
  if ws.isEmpty then throw "جملةٌ فارغة"
  let mut out : List Kalima := []
  for w in ws do
    match tahlil w false with
    | .error e => throw s!"«{w}»: {e}"
    | .ok q => out := out ++ [kalima q]
  return out

def bitIsm (x : Bool) : String := if x then "1" else "0"

/-- **وضعُ الخلايا:** لكلّ سطرٍ «مفتاح⇥جملة» سطرٌ واحد: `مفتاح⇥QABUL⇥كلمة|كلمة…` وكلُّ كلمةٍ «خلايا مفصولةٌ بفاصلة;وصل;أل»، أو
    `مفتاح⇥RAFD⇥السبب`. يقرؤه مولِّدُ حالات الضابط (`scripts/bina_dawabit_nass.py`). -/
def khalayaWad (path : String) : IO UInt32 := do
  for line in ← IO.FS.lines path do
    match line.splitOn "\t" with
    | [k, s] =>
      match kalimatJumla s with
      | .error e => IO.println s!"{k}\tRAFD\t{e}"
      | .ok ws =>
        let f (w : Kalima) : String := ",".intercalate (w.khalaya.map toString) ++ ";" ++ bitIsm w.wasl ++ ";" ++ bitIsm w.al
        IO.println s!"{k}\tQABUL\t{"|".intercalate (ws.map f)}"
    | _ => IO.println s!"{line}\tKHALAL\tسطرٌ ليس «مفتاح⇥جملة»"
  return 0

def dawrIsm : Jisr.NassItar.Dawr → String
  | .fil => "فعل" | .fail => "فاعل" | .maful => "مفعول_به" | .harfJarr => "حرف_جر" | .majrur => "مجرور"
  | .mudafIlayh => "مضاف_إليه"

def hukmNassIsm : Jisr.Utur.Hukm → String
  | .murakhkhas => "مقبول" | .mumtani => "خطأ" | .laHukm => "لا_حكم"

/-- **وضعُ الإطار:** لكلّ سطرٍ «مفتاح⇥جملة»: حكمُ الجملة (`hukmNass`)، ثمّ كلُّ إطارٍ تُخرجه القراءة (`itarat`) بأدواره وحكمه بصفّ
    الأسماء الستّة (`QawaidSitta.hukmSitta`)؛ أو `RAFD` وسببُه. -/
def itarWad (path : String) : IO UInt32 := do
  for line in ← IO.FS.lines path do
    match line.splitOn "\t" with
    | [k, s] =>
      match kalimatJumla s with
      | .error e => IO.println s!"{k}\tRAFD\t{e}"
      | .ok ws =>
        let itarat := (Jisr.NassItar.itarat ws).map fun x =>
          " ".intercalate (x.1.map dawrIsm) ++ ": " ++ hukmNassIsm (Jisr.QawaidSitta.hukmSitta x.2)
        let itarat := if itarat.isEmpty then "لا إطار في المجال" else " | ".intercalate itarat
        IO.println s!"{k}\t{hukmNassIsm (Jisr.NassItar.hukmNass ws)}\t{itarat}"
    | _ => IO.println s!"{line}\tKHALAL\tسطرٌ ليس «مفتاح⇥جملة»"
  return 0

def main (args : List String) : IO UInt32 := do
  match args with
  | ["--qiyas", path] => qiyas path
  | ["--khalaya", path] => khalayaWad path
  | ["--itar", path] => itarWad path
  | _ =>
  -- السجلُّ المعتمد (P1-ج): غيرُ `mudaat/sijill.tsv` المختوم خطأُ تحميلٍ إلّا بـ`--ikhtibar` معلَنًا.
  let (ikhtibar, args) := match args with
    | "--ikhtibar" :: r => (true, r)
    | r => (false, r)
  if ikhtibar then IO.eprintln "سجلُّ اختبار (--ikhtibar): السلطةُ غيرُ السجلّ المختوم"
  match args with
  | sijill :: makhzan :: nass =>
    if nass.isEmpty then IO.eprintln "لا نصّ"; return 2
    -- التحميل المحقَّق نفسُه الذي يستعمله الفاحص (Faahis/Lib.lean: `tahmil`، `muhaqqaq`): السجلّ سلطةٌ وحده،
    -- وخطأُ التحميل يُطبع باسمه ولا يُقرأ النصّ على قاعدةٍ جزئيّة.
    let h := tahmilMutamad ikhtibar (← IO.FS.lines sijill).toList (← IO.FS.lines makhzan).toList
    let h ← match muhaqqaq h with
      | .ok h => pure h
      | .error e =>
        for x in e do IO.println s!"خطأ تحميل\t{x}"
        IO.println s!"لا قراءة: التحميل لم يتحقّق ({e.size} خطأ)."
        return 1
    let some isdar := h.isdar | IO.eprintln "لا إصدار للقاعدة"; return 1
    let b := bina h isdar
    let words := ((" ".intercalate nass).splitOn " " |>.filter (· != "")).toArray
    let mut qs : Array Qiraa := #[]
    let mut kull := true
    for i in [0:words.size] do
      let w := words[i]!
      IO.println s!"الكلمة: {w}"
      match tahlil w (i + 1 == words.size) with
      | .error e => IO.println s!"  مرفوضة باسمها: {e}"; kull := false
      | .ok q => iqraKalima h b w q; qs := qs.push q
    if words.size ≥ 2 then
      if kull then iqraJumla words qs
      else IO.println s!"الجملة في الوصل ({words.size} كلمات): لم تُركَّب — فيها كلمة مرفوضة باسمها"
    return 0
  | _ => IO.eprintln "الاستعمال: qari [--ikhtibar] <سجلّ المودَعات> <المخزن> <نصّ مشكول…>"; return 2
