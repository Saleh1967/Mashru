/-
  Qari/Main.lean — القارئ: نصٌّ عربيٌّ مشكول ← خلايا (الدال وحده) ← القانون (ابتداء/وصل/وقف) ← المقاطع
  ← المخزن (المدلول): المنطوق (مطابقة وتضمّن) والمفهوم (التزام)، بمراتب المخرج ووسم كلّ قول.

  ما يُخمَّن: لا شيء. ما ليس في جدول المخارج أو لم يُودَع قرارُه يُرفض باسمه (الدستور م5):
  التاء المربوطة، الألف المقصورة، الحرف بلا حركة في غير آخر الكلمة، الألف المحرّكة في أوّل الكلمة.
  الوسائط المعلنة (مقرّرة هنا، مذكورة في المخرج):
  * مقاعد الهمزة (أ إ ؤ ئ) همزةُ قطع (ء = 0)؛ آ = همزة مفتوحة ثمّ ألف مدّ.
  * الألف المجرّدة في أوّل الكلمة (أو ٱ) همزةُ وصل: تُحذف ويُصلح الابتداء بـ `SLGE.Law.ibtidaForm`
    (فتحة مع «ال»، وإلّا بحسب حركة الثالث — وسيط المالك `waslHaraka`).
  * الشدّة: ساكنٌ ثمّ متحرّكٌ من الحامل نفسه. التنوين: حركةٌ ثمّ نون ساكنة (وألفُ التنوين بعد الفتحتين لا تُنطق).
  * الحرف الأخير بلا حركة: ساكنٌ للوقف. ا/و/ي بلا حركة في غير الأوّل: ساكنة (مدًّا أو غيرَه، والقانون يحكم).
  * البحث في المخزن باللفظ مجرَّدًا من الحركات كما يكتبه المعجم.
  التشغيل: qari <سجلّ المودَعات> <المخزن> <نصّ مشكول…>
-/
import Dal.Qanun
import Faahis.Lib

open Dal SLGE SLGE.Law QawaninDalala Qaida Mawsua

/-! ## ١. من الحروف إلى الخلايا -/

def harf? (c : Char) : Option Nat := hawamil.idxOf? c

def maqadAlhamza : List Char := ['أ', 'إ', 'ؤ', 'ئ']

structure Qiraa where
  khalaya   : List Nat := []       -- الرموز 4c+s
  wasl      : Bool := false        -- بدأت بهمزة وصل
  mulahazat : List String := []

/-- خلية: حامل وحالة. -/
def kh (c s : Nat) : Nat := 4 * c + s

/-- تحليل كلمة مشكولة إلى خلايا؛ الرفض باسمه. -/
def tahlil (w : String) : Except String Qiraa := do
  let cs := w.toList.filter (· != 'ـ')
  let n := cs.length
  let mut q : Qiraa := {}
  let mut i := 0
  let harakaOf (c : Char) : Option Nat :=
    if c == 'َ' then some 0 else if c == 'ُ' then some 1 else if c == 'ِ' then some 2 else if c == 'ْ' then some 3 else none
  let tanwinOf (c : Char) : Option Nat :=
    if c == 'ً' then some 0 else if c == 'ٌ' then some 1 else if c == 'ٍ' then some 2 else none
  while i < n do
    let c := cs[i]!
    let nxt := cs[i+1]?
    if c == 'ة' then throw "تاء مربوطة: تُقرأ هاءً في الوقف وتاءً في الوصل، ولم يُودَع قرارها"
    if c == 'ى' then throw "ألف مقصورة: لم يُودَع قرار رسمها"
    if i == 0 && (c == 'ا' || c == 'ٱ') then
      -- همزة وصل: إن كان للألف حركة فهي همزة قطع رُسمت بلا مقعد — تُرفض
      match nxt.bind harakaOf with
      | some _ => throw "ألف محرّكة في أوّل الكلمة: اكتب همزة القطع بمقعدها (أ/إ)، أو همزة الوصل بلا حركة"
      | none => q := { q with wasl := true }; i := i + 1
    else if c == 'آ' then
      q := { q with khalaya := q.khalaya ++ [kh 0 0, kh 2 3] }; i := i + 1
    else
      let hamil? : Option Nat := if maqadAlhamza.contains c then some 0 else harf? c
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
        let akhir := j ≥ n
        match haraka, tanwin with
        | some s, _ =>
          let cells := if sh then [kh h 3, kh h s] else [kh h s]
          q := { q with khalaya := q.khalaya ++ cells }
        | none, some s =>
          let cells := (if sh then [kh h 3] else []) ++ [kh h s, kh 14 3]
          q := { q with khalaya := q.khalaya ++ cells,
                        mulahazat := q.mulahazat ++ ["التنوين نون ساكنة (وسيط معلَن)"] }
          -- ألف التنوين بعد الفتحتين لا تُنطق
          if s == 0 && cs[j]? == some 'ا' then j := j + 1
        | none, none =>
          if akhir then
            q := { q with khalaya := q.khalaya ++ (if sh then [kh h 3, kh h 3] else [kh h 3]),
                          mulahazat := q.mulahazat ++ ["الحرف الأخير بلا حركة: عُدّ ساكنًا للوقف"] }
          else if h == 2 || h == 28 || h == 11 then
            q := { q with khalaya := q.khalaya ++ [kh h 3] }
          else throw s!"حرف بلا حركة في غير آخر الكلمة: «{c}» — النصّ غير مشكول"
        i := j
  if q.khalaya.isEmpty then throw "كلمة فارغة"
  if q.wasl then
    let isAl := q.khalaya.head? == some (kh 13 3)
    q := { q with khalaya := ibtidaForm isAl q.khalaya,
                  mulahazat := q.mulahazat ++ [s!"همزة الوصل أُصلحت بـ ibtidaForm (isAl={isAl})"] }
  return q

/-- تجريد اللفظ من الحركات للبحث في المخزن. -/
def mujarrad (w : String) : String :=
  String.ofList (w.toList.filter fun c => !(['َ','ُ','ِ','ْ','ّ','ً','ٌ','ٍ','ـ'].contains c))

def halaIsm (s : Nat) : String := match s with | 0 => "فتحة" | 1 => "ضمّة" | 2 => "كسرة" | _ => "سكون"

def khaliyaIsm (a : Nat) : String := s!"{Dal.harf ⟨a / 4 % 29, Nat.mod_lt _ (by decide)⟩}/{halaIsm (a % 4)}({a})"

def nawIsm : NawMaqta → String
  | .CV => "CV" | .CVV => "CVV" | .CVC => "CVC" | .CVVC => "CVVC" | .CVCC => "CVCC" | .CVVCC => "CVVCC"

/-! ## ٢. القراءة -/

def iqra (h : Hal) (b : Bina) (w : String) : IO Unit := do
  IO.println s!"الكلمة: {w}"
  match tahlil w with
  | .error e => IO.println s!"  مرفوضة باسمها: {e}"
  | .ok q =>
    IO.println s!"  الخلايا: {" ".intercalate (q.khalaya.map khaliyaIsm)}"
    for m in q.mulahazat do IO.println s!"  ملاحظة: {m}"
    let waqf := Fwaqf (run 0 q.khalaya)
    let wasl := Fwasl (run 0 q.khalaya)
    IO.println s!"  القانون (ابتداء/وصل/وقف): موقوفًا عليها {if waqf then "مرخَّصة" else "ممتنعة"}؛ في الوصل {if wasl then "مرخَّصة" else "ممتنعة"}"
    if waqf then
      match qatta q.khalaya with
      | some sy => IO.println s!"  المقاطع ({sy.length}): {" · ".intercalate (sy.map fun x => nawIsm (nawMaqta x))} — واحدٌ بمبرهنة qatta_wahid"
      | none => IO.println "  المقاطع: لم يُقسَّم (خلل في التقطيع التنفيذيّ؛ الوجود مبرهن في word_structure)"
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

def main (args : List String) : IO UInt32 := do
  match args with
  | sijill :: makhzan :: nass =>
    if nass.isEmpty then IO.eprintln "لا نصّ"; return 2
    let mut lines : Array String := #[]
    for p in [sijill, makhzan] do lines := lines ++ (← IO.FS.lines p)
    let h := (lines.toList.zipIdx 1).foldl (fun h (l, n) => qira h n l) {}
    let some isdar := h.isdar | IO.eprintln "لا إصدار للقاعدة"; return 1
    let b := bina h isdar
    let words := (" ".intercalate nass).splitOn " " |>.filter (· != "")
    for w in words do iqra h b w
    return 0
  | _ => IO.eprintln "الاستعمال: qari <سجلّ المودَعات> <المخزن> <نصّ مشكول…>"; return 2
