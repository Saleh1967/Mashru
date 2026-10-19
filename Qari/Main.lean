/-
  Qari/Main.lean — القارئ: نصٌّ عربيٌّ مشكول ← خلايا (الدال وحده) ← القانون (ابتداء/وصل/وقف) ← المقاطع
  ← المخزن (المدلول): المنطوق (مطابقة وتضمّن) والمفهوم (التزام)، بمراتب المخرج ووسم كلّ قول.
  والجملة: تركيب الكلمات في الوصل على آلة المالك `Msent` (Dal/Jumla.lean): سقوط همزة الوصل بإصلاحها الأدنى،
  وحدّ الكلمة 116 بين ما سواها؛ والتقطيع كلماتٍ صوتيّةً ومقاطعَ، صحيحٌ بالبناء وواحدٌ بمبرهنة المالك.

  ما يُخمَّن: لا شيء. ما ليس في جدول المخارج أو لم يُودَع قرارُه يُرفض باسمه (الدستور م5):
  الحرف بلا حركة في غير آخر الكلمة، الألف المحرّكة في أوّل الكلمة، والحرف الأخير بلا حركة في غير آخر الجملة
  (الوصل يحتاج حركته).
  قرارات الوقف والرسم من المودَعين «متن قطر الندى» (باب الوقف في الأفصح L440–447، وفصل همزة الوصل L449–453) و«ألفية ابن
  مالك» (باب الوقف L1131، L1136، L1142) — شاهدان مستقلّان. قرارا الوقف (ة، التنوين) على الموقوف عليه، وهو هنا آخرُ النصّ
  المعطى (وسيط معلَن: الوقف حيث ينتهي النصّ)؛ وقرارات الرسم (ى، ألف الجماعة) وهمزة الوصل في كلّ موضع:
  * التاء المربوطة في الوقف هاءٌ («على نحو رحمة بالهاء» L441؛ «في الوقف تا تأنيث الاسم ها جعل» L1142)، ساكنةٌ («وغيرها
    التأنيث من محرك سكنه» L1136)؛ وفي الوصل تاءٌ بحركتها.
  * التنوين في الوقف: بعد الفتح ألفٌ («رأيت زيدا بالألف» L442–443؛ «تنوينا إثر فتح اجعل ألفا» L1131)، وفي غيره حذفٌ
    («وتلو غير فتح احذفا» L1131) ويسكن الحرف (L1136). والألف المقصورة بعد تنوين الفتح («الفتى» L445) ألفُ التنوين.
  * الألف المقصورة ألفٌ رُسمت ياءً («وترسم الألف ياء إن تجاوزت الثلاثة … أو كان أصلها الياء» L444–445): تُقرأ ألفًا.
  * الألف بعد واو الجماعة تُكتب («وتكتب الألف بعد واو الجماعة كقالوا دون الأصلية» L443–444)؛ وأنّها لا تُنطق وسيطٌ معلَن.
  * حركة همزة الوصل وسيطُ المالك `waslHaraka` (ضمٌّ إن ضُمّ الثالث، وفتحٌ مع أل، وكسرٌ في الباقي)؛ شاهدُه في القطر أمثلةُ
    الأمر و«ال» («اقتل واغز واغزي بضمهن، واضرب وامشوا واذهب بكسر كالبواقي … والغلام وايمن الله في القسم بفتحهما» L449–453)؛
    وأسماءُ الفصل (اسم، است، ابن، امرئ، امرأة…) «بكسر» (L449) لا يشملها الوسيط: «امْرُؤٌ» يُخرجها بالضمّ — فجوةٌ معلَنة.
  الوسائط المعلنة (مقرّرة هنا، مذكورة في المخرج):
  * مقاعد الهمزة (أ إ ؤ ئ) همزةُ قطع (ء = 0)؛ آ = همزة مفتوحة ثمّ ألف مدّ.
  * الألف المجرّدة في أوّل الكلمة (أو ٱ) همزةُ وصل: تُحذف من الخلايا، وفي الابتداء تُصلح بـ `SLGE.Law.ibtidaForm`
    (فتحة مع «ال»، وإلّا بحسب حركة الثالث — وسيط المالك `waslHaraka`)؛ وفي الوصل تسقط بإصلاح المالك (Hamza.lean).
    ولا تكون إلّا قبل ساكن (Hamza.lean)؛ فألفٌ مجرّدة قبل متحرّك تُرفض باسمها.
  * لام التعريف بلا علامة قبل حرفٍ مشدّد: مدغمةٌ فيه، لا خلية لها (الشدّة في النصّ شاهدُ الإدغام).
  * الشدّة: ساكنٌ ثمّ متحرّكٌ من الحامل نفسه. التنوين في الوصل: حركةٌ ثمّ نون ساكنة (وألفُ التنوين بعد الفتحتين لا تُنطق).
  * الحرف الأخير بلا حركة في آخر الجملة: ساكنٌ للوقف. ا/و/ي بلا حركة في غير الأوّل: ساكنة (مدًّا أو غيرَه، والقانون يحكم).
  * البحث في المخزن باللفظ مجرَّدًا من الحركات كما يكتبه المعجم.
  التشغيل: qari <سجلّ المودَعات> <المخزن> <نصّ مشكول…>
-/
import Dal.Jumla
import Faahis.Lib
import Nizam.Aqd

open Dal SLGE SLGE.Law QawaninDalala Qaida Mawsua

/-! ## ١. من الحروف إلى الخلايا -/

def harf? (c : Char) : Option Nat := hawamil.idxOf? c

def maqadAlhamza : List Char := ['أ', 'إ', 'ؤ', 'ئ']

structure Qiraa where
  khalaya   : List Nat := []       -- الرموز 4c+s بلا همزة الوصل
  wasl      : Bool := false        -- بدأت بهمزة وصل
  al        : Bool := false        -- همزتها همزة «أل» (لامٌ ساكنة أو مدغمة)
  mulahazat : List String := []

/-- خلية: حامل وحالة. -/
def kh (c s : Nat) : Nat := 4 * c + s

def harakaOf (c : Char) : Option Nat :=
  if c == 'َ' then some 0 else if c == 'ُ' then some 1 else if c == 'ِ' then some 2 else if c == 'ْ' then some 3 else none

def tanwinOf (c : Char) : Option Nat :=
  if c == 'ً' then some 0 else if c == 'ٌ' then some 1 else if c == 'ٍ' then some 2 else none

def alama (c : Char) : Bool := c == 'ّ' || (harakaOf c).isSome || (tanwinOf c).isSome

/-- هل الحرف الذي يبدأ في الموضع `i` تليه شدّة بين علاماته؟ -/
def mushaddad (cs : List Char) (i : Nat) : Bool :=
  (cs.drop (i + 1)).takeWhile alama |>.contains 'ّ'

/-- تحليل كلمة مشكولة إلى خلايا؛ الرفض باسمه. `akhirJumla`: الكلمة آخر الجملة (فيجوز الوقف على ساكن). -/
def tahlil (w : String) (akhirJumla : Bool := true) : Except String Qiraa := do
  let cs := w.toList.filter (· != 'ـ')
  let n := cs.length
  let mut q : Qiraa := {}
  let mut i := 0
  while i < n do
    let c0 := cs[i]!
    let nxt := cs[i+1]?
    -- الألف المقصورة ألفٌ (قطر الندى L444–445)
    let c := if c0 == 'ى' then 'ا' else c0
    if c0 == 'ى' then
      q := { q with mulahazat := q.mulahazat ++ ["الألف المقصورة ألفٌ رُسمت ياءً (قطر الندى L444–445)"] }
    if i == 0 && (c == 'ا' || c == 'ٱ') then
      -- همزة وصل: إن كان للألف حركة فهي همزة قطع رُسمت بلا مقعد — تُرفض
      match nxt.bind harakaOf with
      | some _ => throw "ألف محرّكة في أوّل الكلمة: اكتب همزة القطع بمقعدها (أ/إ)، أو همزة الوصل بلا حركة"
      | none => q := { q with wasl := true }; i := i + 1
    else if c == 'آ' then
      q := { q with khalaya := q.khalaya ++ [kh 0 0, kh 2 3] }; i := i + 1
    else
      -- التاء المربوطة: تاءٌ في الوصل، وهاءٌ ساكنة في الوقف (قطر الندى L441، الألفية L1142)
      let hamil? : Option Nat :=
        if c == 'ة' then some (if akhirJumla then 1 else 18)
        else if maqadAlhamza.contains c then some 0 else harf? c
      match hamil? with
      | none => throw s!"حرف ليس في جدول المخارج: «{c}»"
      | some h =>
        -- اقرأ العلامات التالية
        let mut j := i + 1
        let mut haraka : Option Nat := none
        let mut sh := false
        let mut tanwin : Option Nat := none
        while j < n do
          let m := cs[j]!
          if m == 'ّ' then sh := true; j := j + 1
          else match harakaOf m with
            | some s => haraka := some s; j := j + 1
            | none => match tanwinOf m with
              | some s => tanwin := some s; j := j + 1
              | none => break
        -- آخر الكلمة: لا حرف بعد العلامات، أو ألفُ التنوين وحدها بعد الفتحتين (ألفًا أو ألفًا مقصورة: «الفتى» L445)
        let akhir := j ≥ n || (tanwin == some 0 && (cs[j]? == some 'ا' || cs[j]? == some 'ى') && j + 1 ≥ n)
        let bilaAlama := haraka.isNone && !sh && tanwin.isNone
        if c == 'ة' && !akhir then
          throw "تاء مربوطة في غير آخر الكلمة"
        else if c == 'ة' && akhirJumla then
          -- الوقف على التاء المربوطة بالهاء الساكنة؛ وما عليها من حركة أو تنوين يسقط في الوقف
          q := { q with khalaya := q.khalaya ++ [kh 1 3],
                        mulahazat := q.mulahazat ++ ["الوقف على التاء المربوطة بالهاء (قطر الندى L441، الألفية L1142) ساكنةً (الألفية L1136)"] }
        else if tanwin.isSome && akhir && akhirJumla then
          -- الوقف على التنوين: بعد الفتح ألفٌ، وفي غيره حذفٌ فيسكن الحرف
          let s := tanwin.getD 0
          let cells := (if sh then [kh h 3] else []) ++ (if s == 0 then [kh h 0, kh 2 3] else [kh h 3])
          q := { q with khalaya := q.khalaya ++ cells,
                        mulahazat := q.mulahazat ++ [if s == 0
                          then "الوقف على التنوين بعد الفتح بالألف (قطر الندى L442–443، الألفية L1131)"
                          else "الوقف على التنوين بحذفه وتسكين الحرف (الألفية L1131، L1136)"] }
          if s == 0 && (cs[j]? == some 'ا' || cs[j]? == some 'ى') then j := j + 1
        else if q.wasl && q.khalaya.isEmpty && c == 'ل' && bilaAlama && !akhir && mushaddad cs j then
          -- لام التعريف المدغمة في المشدّد بعدها
          q := { q with al := true,
                        mulahazat := q.mulahazat ++ ["لام التعريف مدغمة في المشدّد بعدها، لا خلية لها (وسيط معلَن)"] }
        else if c == 'ا' && bilaAlama && akhir && q.khalaya.getLast? == some (kh 28 3) then
          q := { q with mulahazat := q.mulahazat ++ ["الألف بعد واو الجماعة تُكتب (قطر الندى L443–444) ولا تُنطق (وسيط معلَن)"] }
        else
          match haraka, tanwin with
          | some s, _ =>
            let cells := if sh then [kh h 3, kh h s] else [kh h s]
            q := { q with khalaya := q.khalaya ++ cells }
          | none, some s =>
            let cells := (if sh then [kh h 3] else []) ++ [kh h s, kh 14 3]
            q := { q with khalaya := q.khalaya ++ cells,
                          mulahazat := q.mulahazat ++ ["التنوين في الوصل نون ساكنة (وسيط معلَن)"] }
            -- ألف التنوين بعد الفتحتين (ألفًا أو ألفًا مقصورة) لا تُنطق في الوصل
            if s == 0 && (cs[j]? == some 'ا' || cs[j]? == some 'ى') then j := j + 1
          | none, none =>
            if h == 2 || h == 28 || h == 11 then
              q := { q with khalaya := q.khalaya ++ [kh h 3] }
            else if akhir then
              if akhirJumla then
                q := { q with khalaya := q.khalaya ++ (if sh then [kh h 3, kh h 3] else [kh h 3]),
                              mulahazat := q.mulahazat ++ ["الحرف الأخير بلا حركة: عُدّ ساكنًا للوقف"] }
              else throw s!"الحرف الأخير بلا حركة في غير آخر الجملة: «{c}» — الوصل يحتاج حركته"
            else throw s!"حرف بلا حركة في غير آخر الكلمة: «{c}» — النصّ غير مشكول"
        i := j
  if q.khalaya.isEmpty then throw "كلمة فارغة"
  if q.wasl && !sakinAwwal q.khalaya then
    throw "ألف مجرّدة قبل متحرّك: ليست همزة وصل (همزة الوصل لا تكون إلّا قبل ساكن — Hamza.lean)؛ اكتب همزة القطع بمقعدها (أ/إ)"
  if q.wasl && isAl q.khalaya then q := { q with al := true }
  return q

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
  | .murakhkhas q => s!"مرخَّص (يحمل قراءتَه: الجذر «{jidhrIsm q.jidhr}»)"
  | .laHukm => "لا حكم"
  | .mumtani s => s!"ممتنع — {s}"

def allNaw : List JadwalLuzum.Naw := [.juz, .taraduf, .luzum, .kharij, .asl]

/-- الكلمةُ في العقد: القانونُ بجدول البتّات، والقراءة، والحكمُ لكلّ صفٍّ في مادّة جذرها، و«لا حكم» لكلّ نوعٍ لا صفَّ له. -/
def iqraAqd (l : List Nat) : IO Unit := do
  -- حقولُ القانون والجذر والحال والصيغة لا تتعلّق بنوع العلاقة؛ تُقرأ من أيّ عقد.
  let A := Nizam.Aqd.Mashru .juz
  IO.println "  العقد الواحد (Nizam.Aqd؛ المبرهنة kull_ma_kull):"
  let qb := A.qanunB l
  IO.println s!"    القانون بجدول البتّات runB (موقوفًا عليها): {if qb then "مقبولة" else "ممتنعة"} — هو run بعينه (runB_run)"
  if !qb then
    IO.println s!"    الحكم: ممتنع — {Nizam.Aqd.sababQanun}، بأيّ مدلولٍ في كلّ نوع"
    return
  let haal := match A.haalB l with
    | some h => s!"{halaIsm h} ({h})"
    | none => "لا حكم"
  IO.println s!"    القراءة: حال الآخر {haal}؛ مرشَّحو الصيغة (Jisr.Iqtiran، قطر L65): {siyaghIsm (A.sighaB l)}"
  match A.haalB l with
  | some h =>
    match Nizam.Aqd.irabMin h with
    | some r => IO.println s!"    حال الآخر إعرابًا إن كان معربًا (Bridge.irabState، قطر الندى L77): {irabIsm r} — مرشَّح؛ الإعرابُ والبناءُ من الباب في المعجم: لا حكم هنا"
    | none => pure ()
  | none => pure ()
  match A.jidhrB l with
  | none =>
    IO.println "    الجذر: لا حكم — الإسقاطُ للكلمة ذات الخانات الثلاث وحدها (نطاقٌ معلَن)؛ فالحكم «لا حكم» بأيّ مدلول"
  | some r =>
    IO.println s!"    الجذر: «{jidhrIsm r}» (رمزُه {r} بحقول خمسة بتّات؛ يُفكّ بـ fakk_ramz)"
    let rows := JadwalLuzum.jadwal.filter fun s => Nizam.Aqd.ramzNass s.a == r
    if !rows.isEmpty then
      IO.println s!"    الحكم بالشواهد (JadwalLuzum؛ في مادّة الجذر لا في صيغة الكلمة):"
      for s in rows do
        let h := Nizam.Aqd.hukmB (Nizam.Aqd.Mashru s.naw) l (Nizam.Aqd.ramzNass s.b)
        IO.println s!"      {nawAqdIsm s.naw} ← «{s.b}» بلفظ «{s.w}»: {hukmAqdIsm h} ({mujamIsm s.mujam} س{s.satr})"
    let ghaib := allNaw.filter fun n => !rows.any (·.naw == n)
    if !ghaib.isEmpty then
      IO.println s!"    لا حكم بأيّ مدلول في: {" · ".intercalate (ghaib.map nawAqdIsm)} — لا صفَّ بها في مادّة «{jidhrIsm r}»؛ الغيابُ ليس امتناعًا (la_shahid_la_hukm)"

/-! ## ٢. قراءة الكلمة وحدها -/

def iqraKalima (h : Hal) (b : Bina) (w : String) (q : Qiraa) : IO Unit := do
  let l := ibtida (kalima q)
  IO.println s!"  الخلايا: {silsilaIsm l}"
  for m in q.mulahazat do IO.println s!"  ملاحظة: {m}"
  if q.wasl then IO.println s!"  ملاحظة: همزة الوصل أُصلحت بـ ibtidaForm (isAl={q.al}) — حركتها وسيط المالك waslHaraka (شاهده قطر الندى L449–453)"
  let waqf := Fwaqf (run 0 l)
  let wasl := Fwasl (run 0 l)
  IO.println s!"  القانون (ابتداء/وصل/وقف): موقوفًا عليها {if waqf then "مرخَّصة" else "ممتنعة"}؛ في الوصل {if wasl then "مرخَّصة" else "ممتنعة"}"
  if waqf then
    match qatta l with
    | some sy => IO.println s!"  المقاطع ({sy.length}): {" · ".intercalate (sy.map fun x => nawIsm (nawMaqta x))} — واحدٌ بمبرهنة qatta_wahid"
    | none => IO.println "  المقاطع: لم يُقسَّم (خلل في التقطيع التنفيذيّ؛ الوجود مبرهن في word_structure)"
  iqraAqd l
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
      if maqbul b.q b.aslB ⟨p, ks⟩ then tatabbu h b ⟨p, ks⟩
      else IO.println s!"      {qadiyyaIsm h.dh p}: مرفوض — سلسلة لا يقبلها الفاحص"
  if mafhum.isEmpty then IO.println "    المفهوم (التزام): لا مدخل في المخزن — لا حكم."
  else
    IO.println s!"    المفهوم (التزام): {mafhum.size}"
    for (_, p, _, ks, _) in mafhum do
      if maqbul b.q b.aslB ⟨p, ks⟩ then tatabbu h b ⟨p, ks⟩
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

def main (args : List String) : IO UInt32 := do
  match args with
  | sijill :: makhzan :: nass =>
    if nass.isEmpty then IO.eprintln "لا نصّ"; return 2
    let mut lines : Array String := #[]
    for p in [sijill, makhzan] do lines := lines ++ (← IO.FS.lines p)
    let h := (lines.toList.zipIdx 1).foldl (fun h (l, n) => qira h n l) {}
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
  | _ => IO.eprintln "الاستعمال: qari <سجلّ المودَعات> <المخزن> <نصّ مشكول…>"; return 2
