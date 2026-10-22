/-
  Faahis/Lib.lean — الفاحص التنفيذيّ (المكتبة المشتركة بين faahis وqari): يقرأ سجلّ المودَعات والمخزن، ويُجري عليهما الدوالّ المبرهنة نفسها.

  * القضايا قضايا الدلالة الأولى `QawaninDalala.Qadiyya` على معرّفات؛ الألفاظ والمعاني والعناوين تُرقَّم عند القراءة.
  * القاعدة مغلقة: لا يُقبل قانون إلّا إن كان مثالًا لقوانين Aql/QawaninDalala.lean (`shakl`)؛
    وسلامتها بالنسبة إلى نموذج المدلول مبرهنة (`salama`)، وتدرّجها (`shakl_mutadarrija`).
  * القبول = `Qaida.maqbul` (`maqbul_murakhkhas`)؛ الوسم المحسوب = `Mawsua.quwwatSilsila` على وسم الأصل بعد
    قيد طريقته (`Mawsua.qayd`) وقيد نوع مودَعه (`Idaa.qaydMudaa`)؛ لا أصل إلّا من مودَع مسجَّل (`Idaa.aslMusajjal`).
  * السؤال (`--sual`): المخزن يُبنى بـ `Makhzan.udkhul`، ويُسأل بـ `Mawsua.sual`؛ وكلّ قولٍ يُطبع بسلسلته وبمراتب
    مخرجه الثلاث (`Maratib.mukhraj`): القضيّة «من حيث هي»، ومعانيها «معلومة» أو «مفهوم» بشواهد واقعٍ في مودَع
    «واقع مختوم» وحده (`Maratib.shuhudMutabara`).

  الملفّان (TAB بين الحقول؛ والسطر الفارغ والسطر أوّلُه «#» يُتجاوزان):
  * سجلُّ المودَعات (الملفّ الأوّل) لا يحمل إلّا أسطر `mudaa`؛ وهو السلطة وحده (`tahmil`، `tahmil_mudaat`).
  * المحتوى (بقيّة الملفّات) يحمل ما سوى `mudaa`؛ وسطرُ `mudaa` فيه خطأٌ باسمه (`muhtawa_la_yudif_mudaa`).
    mudaa   <sha256>  <النوع: واقع-مختوم|وضع|معلومات-سابقة|مرجع-محجوب>  <الاسم>      (في السجلّ وحده)
    isdar   <الإصدار>
    qanun   <الاسم>  <مقدّمة|مقدّمة…>  <النتيجة>  <الوسم>
    asl     <القضيّة>  <الوسم>  <السند>  [<الطريقة: عقلي|علمي>]
    iddia   <القضيّة>  <الوسم المعلَن>  <خطوة|خطوة…>  <السند>
    shahid  <المعنى>  <بصمة>@<موضع>
  القضيّة: نوع:أ:ب حيث النوع أحد: wad juz kharij luzum mutabaqa tadammun iltizam fi taht.
  الخطوة: a=<قضيّة> أو q=<رقم القانون>. السند: <أوّل 12 من البصمة>@<الموضع>…
  التشغيل: faahis <سجلّ> <محتوى>…   |   faahis --sual <بادئة القضيّة> <سجلّ> <محتوى>…
-/
import Std.Data.HashMap
import Aql.Qaida
import Aql.Mawsua
import Aql.Idaa
import Aql.QawaninDalala
import Aql.Maratib

open Qaida Mawsua QawaninDalala Maratib

/-! ## القراءة -/

def wasmMin : String → Option Wasm
  | "رأي" => some .ray
  | "تقدير" => some .taqdir
  | "مقيس" => some .maqis
  | "مفحوص" => some .mafhus
  | "مطابق" => some .mutabaq
  | "مبرهن-على-الشاهد" => some .mubarhanShahid
  | "مبرهن" => some .mubarhan
  | _ => none

def wasmIsm : Nat → String
  | 0 => "رأي" | 1 => "تقدير" | 2 => "مقيس" | 3 => "مفحوص"
  | 4 => "مطابق" | 5 => "مبرهن-على-الشاهد" | _ => "مبرهن"

def nawMin : String → Option Idaa.Naw
  | "واقع-مختوم" => some .waqiMakhtum
  | "وضع" => some .wad
  | "معلومات-سابقة" => some .maalumatSabiqa
  | "مرجع-محجوب" => some .marjaMahjub
  | _ => none

def tariqaMin : String → Option Tariqa
  | "عقلي" => some .aqliyya
  | "علمي" => some .ilmiyya
  | _ => none

def bad12 (s : String) : String := String.ofList (s.toList.take 12)

/-- جدول المعرّفات: كلّ ذرّة (لفظ، معنى، عنوان) رقمٌ عند أوّل ورود. -/
structure Dhurrat where
  asma : Array String := #[]
  arqam : Std.HashMap String Nat := {}

def Dhurrat.raqm (d : Dhurrat) (s : String) : Dhurrat × Nat :=
  match d.arqam[s]? with
  | some n => (d, n)
  | none =>
    let ⟨asma, arqam⟩ := d
    let n := asma.size
    (⟨asma.push s, arqam.insert s n⟩, n)

def Dhurrat.ism (d : Dhurrat) (n : Nat) : String := d.asma.getD n s!"#{n}"

/-- قراءة قضيّة. جدول المعرّفات يُعاد دائمًا (ولو فشلت القراءة) ليبقى فريد المرجع. -/
def qadiyyaMin (d : Dhurrat) (s : String) : Dhurrat × Option Qadiyya :=
  match s.splitOn ":" with
  | [k, a, b] =>
    let (d, x) := d.raqm a
    let (d, y) := d.raqm b
    let q : Option Qadiyya := match k with
      | "wad" => some (.wad x y) | "juz" => some (.juz x y) | "kharij" => some (.kharij x y)
      | "luzum" => some (.luzum x y) | "mutabaqa" => some (.mutabaqa x y) | "tadammun" => some (.tadammun x y)
      | "iltizam" => some (.iltizam x y) | "fi" => some (.fi x y) | "taht" => some (.taht x y)
      | _ => none
    (d, q)
  | _ => (d, none)

def qadiyyaIsm (d : Dhurrat) : Qadiyya → String
  | .wad a b => s!"wad:{d.ism a}:{d.ism b}" | .juz a b => s!"juz:{d.ism a}:{d.ism b}"
  | .kharij a b => s!"kharij:{d.ism a}:{d.ism b}" | .luzum a b => s!"luzum:{d.ism a}:{d.ism b}"
  | .mutabaqa a b => s!"mutabaqa:{d.ism a}:{d.ism b}" | .tadammun a b => s!"tadammun:{d.ism a}:{d.ism b}"
  | .iltizam a b => s!"iltizam:{d.ism a}:{d.ism b}" | .fi a b => s!"fi:{d.ism a}:{d.ism b}"
  | .taht a b => s!"taht:{d.ism a}:{d.ism b}"

def qadayaMin (d : Dhurrat) (s : String) : Dhurrat × Option (List Qadiyya) :=
  (s.splitOn "|").foldl (fun (d, acc) t =>
    match acc with
    | none => (d, none)
    | some qs =>
      let (d, q) := qadiyyaMin d t
      (d, q.map fun q => qs ++ [q])) (d, some [])

def khatawatMin (d : Dhurrat) (s : String) : Dhurrat × Option (List (Khatwa Qadiyya)) :=
  (s.splitOn "|").foldl (fun (d, acc) t =>
    match acc with
    | none => (d, none)
    | some ks =>
      -- «a=» رأسٌ والباقي قضيّةٌ قد يحمل معناها «=» (شطرا بيتٍ في شرح المعجم: سطرا makhzan_kamil 138997 و139031،
      -- كانا خطأَي «سلسلة لا تُقرأ» يُسقطهما القارئ بصمت حتّى صار التحميلُ محقَّقًا)
      match t.splitOn "=" with
      | "a" :: baqi@(_ :: _) => let (d, q) := qadiyyaMin d ("=".intercalate baqi); (d, q.map fun q => ks ++ [.asl q])
      | ["q", i] => (d, i.toNat?.map fun i => ks ++ [.qanun i])
      | _ => (d, none)) (d, some [])

structure Asl where
  qadiyya : Qadiyya
  wasm    : Wasm
  tariqa  : Tariqa
  sanad   : String

structure Hal where
  dh      : Dhurrat := {}
  mudaat  : Array (String × Idaa.Naw) := #[]
  isdar   : Option String := none
  qawanin : Array (Qanun Qadiyya × Wasm) := #[]
  usul    : Array Asl := #[]
  iddiaat : Array (Nat × Qadiyya × Wasm × List (Khatwa Qadiyya) × String) := #[]
  shawahid : Array (Nat × ShahidWaqi) := #[]
  akhta   : Array String := #[]

def khata (h : Hal) (n : Nat) (s : String) : Hal :=
  let ⟨dh, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta⟩ := h
  ⟨dh, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta.push s!"سطر {n}: {s}"⟩

/-- قراءة سطر. الحال تُفكّك إلى حقولها فتبقى مصفوفاتها فريدة المرجع وتُضاف إليها في مكانها
    (لا نسخَ للمصفوفة عند كلّ سطر). -/
def qira (h0 : Hal) (n : Nat) (line : String) : Hal :=
  let ⟨dh, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta⟩ := h0
  if line.isEmpty then ⟨dh, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta⟩ else
  match line.splitOn "\t" with
  | ["mudaa", basma, naw, _] =>
    match nawMin naw with
    | some k => if basma.length == 64 then ⟨dh, mudaat.push (bad12 basma, k), isdar, qawanin, usul, iddiaat, shawahid, akhta⟩
                else ⟨dh, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta.push s!"سطر {n}: بصمة ليست sha256"⟩
    | none => ⟨dh, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta.push s!"سطر {n}: نوع مودَع مجهول (الدستور م12)"⟩
  | ["isdar", v] => ⟨dh, mudaat, some v, qawanin, usul, iddiaat, shawahid, akhta⟩
  | ["qanun", ism, ms, nat, w] =>
    let (d, muq) := qadayaMin dh ms
    let (d, nat) := qadiyyaMin d nat
    match muq, nat, wasmMin w with
    | some muq, some nat, some w =>
      let r : Qanun Qadiyya := ⟨ism, muq, nat⟩
      if shakl r then ⟨d, mudaat, isdar, qawanin.push (r, w), usul, iddiaat, shawahid, akhta⟩
      else ⟨d, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta.push s!"سطر {n}: قانون خارج القاعدة: {ism}"⟩
    | _, _, _ => ⟨d, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta.push s!"سطر {n}: قانون لا يُقرأ"⟩
  | ["asl", p, w, s] | ["asl", p, w, s, _] =>
    let t : Option String := match line.splitOn "\t" with | [_, _, _, _, t] => some t | _ => none
    let (d, q) := qadiyyaMin dh p
    match q, wasmMin w, (t.map tariqaMin).getD (some .aqliyya) with
    | some q, some w, some t => ⟨d, mudaat, isdar, qawanin, usul.push ⟨q, w, t, s⟩, iddiaat, shawahid, akhta⟩
    | none, _, _ => ⟨d, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta.push s!"سطر {n}: قضيّة لا تُقرأ"⟩
    | _, _, _ => ⟨d, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta.push s!"سطر {n}: وسم أو طريقة مجهولة"⟩
  | ["iddia", p, w, ks, s] =>
    let (d, q) := qadiyyaMin dh p
    let (d, ks) := khatawatMin d ks
    match q, wasmMin w, ks with
    | some q, some w, some ks => ⟨d, mudaat, isdar, qawanin, usul, iddiaat.push (n, q, w, ks, s), shawahid, akhta⟩
    | _, _, none => ⟨d, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta.push s!"سطر {n}: سلسلة لا تُقرأ"⟩
    | _, _, _ => ⟨d, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta.push s!"سطر {n}: ادّعاء لا يُقرأ"⟩
  | ["shahid", m, s] =>
    match s.splitOn "@" with
    | [b, pos] =>
      match pos.toNat? with
      | some pos => let (d, x) := dh.raqm m; ⟨d, mudaat, isdar, qawanin, usul, iddiaat, shawahid.push (x, ⟨b, pos⟩), akhta⟩
      | none => ⟨dh, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta.push s!"سطر {n}: موضع الشاهد ليس رقمًا"⟩
    | _ => ⟨dh, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta.push s!"سطر {n}: شاهد لا يُقرأ"⟩
  | _ => ⟨dh, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta.push s!"سطر {n}: سجلّ لا يُعرف"⟩

/-! ## التحميل المحقَّق: السلطة من سجلّ المودَعات وحده (خطّة الإطلاق التجريبي، الحزمة P1-أ)

  كان الفاحص والقارئ يصلان أسطر الملفّات كلّها في سيلٍ واحد، فيقبلان سطر `mudaa` من أيّ ملفّ: محتوًى يُفحص كان يستطيع
  أن يسجّل لنفسه مودَعًا «واقعًا مختومًا» ببصمةٍ مصطنعة، ثمّ يستشهد به فيرفع معنًى إلى «مفهوم» (أُعيدت التجربة على
  1bff783؛ مثالُه `mawsua/fasid_haqn.tsv`). فصار للسطر مصدر: السجلُّ لا يحمل إلّا `mudaa` (`sijill_la_muhtawa`)، والمحتوى لا يحمل
  `mudaa` (`tahmil_mudaat`). وخطأُ التحميل يُسلَّم إلى الواجهات باسمه (`muhaqqaq`) فلا تجيب على قاعدةٍ جزئيّة بصمت.
  وما لا يسدّه هذا القسم: شاهدُ `shahid` بموضعٍ في مودَعٍ مسجَّلٍ حقًّا يُقبل بلا فحصٍ لوجود الموضع ولا لقضيّته، فيرفع معنًى إلى
  «مفهوم» من المحتوى (P2-أ)؛ والسجلّ هو الملفّ الذي يمرّره المستدعي أوّلًا، لا يُفحص أنّه `mudaat/sijill.tsv` المختوم (P1-ج). -/

/-- مصدرُ السطر: سجلُّ المودَعات (السلطة)، أو المحتوى الذي يُفحص. -/
inductive Masdar | sijill | muhtawa
deriving DecidableEq, Repr

/-- رأسُ السطر: حقلُه الأوّل قبل أوّل TAB. -/
def raas (line : String) : String := (line.splitOn "\t").headD ""

/-- سطرٌ يُتجاوز: فارغٌ، أو تعليقٌ أوّلُه «#». -/
def mutajawaz (line : String) : Bool := line.isEmpty || line.startsWith "#"

/-- قراءةُ سطرٍ بحسب مصدره: السجلُّ لا يحمل إلّا `mudaa`، والمحتوى لا يحمل `mudaa`؛ وما سوى ذلك `qira` نفسُها. -/
def qiraMin (m : Masdar) (h : Hal) (n : Nat) (line : String) : Hal :=
  if mutajawaz line then h
  else match m with
    | .sijill =>
      if raas line == "mudaa" then qira h n line
      else khata h n "السجلّ لا يحمل إلّا مودَعات (mudaa)"
    | .muhtawa =>
      if raas line == "mudaa" then khata h n "المحتوى لا يسجّل مودَعًا: السلطة في سجلّ المودَعات وحده"
      else qira h n line

/-- **لا يزيد `qira` المودَعاتِ إلّا من سطر `mudaa`**: سطرٌ رأسُه غيرُه يترك المودَعات كما هي. -/
theorem qira_mudaat (h : Hal) (n : Nat) (line : String) (hr : raas line ≠ "mudaa") :
    (qira h n line).mudaat = h.mudaat := by
  obtain ⟨dh, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta⟩ := h
  unfold raas at hr
  unfold qira
  by_cases he : line.isEmpty = true
  · simp only [he, ite_true]
  · simp only [he, Bool.false_eq_true, ite_false]
    generalize line.splitOn "\t" = parts at hr ⊢
    split
    · simp at hr
    all_goals (repeat' split) <;> rfl

theorem khata_mudaat (h : Hal) (n : Nat) (s : String) : (khata h n s).mudaat = h.mudaat := by
  cases h; rfl

/-- **سطرُ المحتوى لا يسجّل مودَعًا**، أيًّا كان. -/
theorem muhtawa_la_yudif_mudaa (h : Hal) (n : Nat) (line : String) :
    (qiraMin .muhtawa h n line).mudaat = h.mudaat := by
  unfold qiraMin
  by_cases hm : mutajawaz line = true
  · simp only [hm, ite_true]
  · simp only [hm, Bool.false_eq_true, ite_false]
    by_cases hr : raas line = "mudaa"
    · simp only [hr, beq_self_eq_true, ite_true, khata_mudaat]
    · have : (raas line == "mudaa") = false := by simpa using hr
      simp only [this, Bool.false_eq_true, ite_false]
      exact qira_mudaat h n line hr

/-- ما يحمله المحتوى من الحال: الإصدار والقوانين والأصول والادّعاءات والشواهد (لا المودَعات ولا الأخطاء ولا جدول المعرّفات). -/
def Hal.muhtawa (h : Hal) :
    Option String × Array (Qanun Qadiyya × Wasm) × Array Asl ×
      Array (Nat × Qadiyya × Wasm × List (Khatwa Qadiyya) × String) × Array (Nat × ShahidWaqi) :=
  (h.isdar, h.qawanin, h.usul, h.iddiaat, h.shawahid)

/-- **سطرُ `mudaa` لا يحمل محتوى**: `qira` عليه لا تغيّر إصدارًا ولا قانونًا ولا أصلًا ولا ادّعاءً ولا شاهدًا. -/
theorem qira_mudaa_muhtawa (h : Hal) (n : Nat) (line : String) (hr : raas line = "mudaa") :
    (qira h n line).muhtawa = h.muhtawa := by
  obtain ⟨dh, mudaat, isdar, qawanin, usul, iddiaat, shawahid, akhta⟩ := h
  unfold raas at hr
  unfold qira
  by_cases he : line.isEmpty = true
  · simp only [he, ite_true]
  · simp only [he, Bool.false_eq_true, ite_false]
    generalize line.splitOn "\t" = parts at hr ⊢
    split <;> (try simp at hr) <;> (repeat' split) <;> rfl

/-- **سطرُ السجلّ لا يحمل محتوى**، أيًّا كان. -/
theorem sijill_la_yahmil_muhtawa (h : Hal) (n : Nat) (line : String) :
    (qiraMin .sijill h n line).muhtawa = h.muhtawa := by
  unfold qiraMin
  by_cases hm : mutajawaz line = true
  · simp only [hm, ite_true]
  · simp only [hm, Bool.false_eq_true, ite_false]
    by_cases hr : raas line = "mudaa"
    · simp only [hr, beq_self_eq_true, ite_true]
      exact qira_mudaa_muhtawa h n line hr
    · have : (raas line == "mudaa") = false := by simpa using hr
      simp only [this, Bool.false_eq_true, ite_false]
      cases h; rfl

/-- التحميلُ من مصدرٍ واحد، بترقيم أسطره من 1. -/
def tahmilMin (m : Masdar) (h : Hal) (lines : List String) : Hal :=
  (lines.zipIdx 1).foldl (fun h (l, n) => qiraMin m h n l) h

/-- **المحتوى كلُّه لا يسجّل مودَعًا**: أيًّا كانت أسطره، تبقى مودَعات الحال كما كانت قبله. -/
theorem tahmil_muhtawa_mudaat (h : Hal) (lines : List String) :
    (tahmilMin .muhtawa h lines).mudaat = h.mudaat := by
  unfold tahmilMin
  generalize lines.zipIdx 1 = ps
  induction ps generalizing h with
  | nil => rfl
  | cons p ps ih => simp only [List.foldl_cons]; rw [ih, muhtawa_la_yudif_mudaa]

/-- **السجلُّ كلُّه لا يحمل محتوى**: أيًّا كانت أسطره، يبقى محتوى الحال كما كان قبله. -/
theorem tahmil_sijill_muhtawa (h : Hal) (lines : List String) :
    (tahmilMin .sijill h lines).muhtawa = h.muhtawa := by
  unfold tahmilMin
  generalize lines.zipIdx 1 = ps
  induction ps generalizing h with
  | nil => rfl
  | cons p ps ih => simp only [List.foldl_cons]; rw [ih, sijill_la_yahmil_muhtawa]

/-- **السجلُّ لا يحمل إلّا `mudaa`**: تحميلُه وحده لا يُدخل إصدارًا ولا قانونًا ولا أصلًا ولا ادّعاءً ولا شاهدًا. -/
theorem sijill_la_muhtawa (lines : List String) :
    (tahmilMin .sijill {} lines).muhtawa = (none, #[], #[], #[], #[]) := by
  rw [tahmil_sijill_muhtawa]; rfl

/-- التحميل: السجلُّ أوّلًا (وأخطاؤه تُسمّى «السجلّ»)، ثمّ المحتوى؛ ولكلٍّ ترقيمُه. -/
def tahmil (sijill muhtawa : List String) : Hal :=
  let h0 := tahmilMin .sijill {} sijill
  tahmilMin .muhtawa { h0 with akhta := h0.akhta.map ("السجلّ، " ++ ·) } muhtawa

/-- **المودَعاتُ مودَعاتُ السجلّ وحده**: لا يغيّرها المحتوى أيًّا كان. -/
theorem tahmil_mudaat (sijill muhtawa : List String) :
    (tahmil sijill muhtawa).mudaat = (tahmilMin .sijill {} sijill).mudaat := by
  unfold tahmil
  rw [tahmil_muhtawa_mudaat]

/-- **بلا سجلّ لا مودَع**، أيًّا كان المحتوى. ومنه، استنتاجًا لا مبرهنةً على `bina`: لا أصلَ يُقبل (`Idaa.sijill_faregh`)،
    ولا شاهدَ يرفع معنًى إلى «مفهوم» (`Maratib.la_mafhum_bila_waqi`). -/
theorem bila_sijill_la_mudaa (muhtawa : List String) : (tahmil [] muhtawa).mudaat = #[] := by
  rw [tahmil_mudaat]; rfl

/-- ما يُسلَّم إلى الواجهات: الحالُ إن خلت من أخطاء التحميل، وإلّا الأخطاءُ بأسمائها — وخطأُ التحميل غيرُ «لا حكم». -/
def muhaqqaq (h : Hal) : Except (Array String) Hal :=
  if h.akhta.isEmpty then .ok h else .error h.akhta

/-- لا تُسلَّم حالٌ فيها خطأ تحميل. -/
theorem muhaqqaq_salim (h h' : Hal) (hk : muhaqqaq h = .ok h') : h' = h ∧ h.akhta = #[] := by
  unfold muhaqqaq at hk
  split at hk
  · rename_i he; cases hk; exact ⟨rfl, Array.isEmpty_iff.mp he⟩
  · cases hk

/-! ## البناء -/

structure Bina where
  q    : Qaida.Qaida Qadiyya
  aslB : Qadiyya → Bool
  aslW : Qadiyya → Wasm
  qW   : Nat → Wasm
  asl? : Qadiyya → Option Asl
  shuhud : Nat → List ShahidWaqi

/-- المودَعُ يطابق السند: بصمتُه غيرُ فارغة، والسندُ يبدأ بها. -/
def mutabiqSanad (s : String) (m : String × Idaa.Naw) : Bool := !m.1.isEmpty && s.startsWith m.1

/-- مودَعُ السند: أوّلُ مودَعٍ مسجَّلٍ يطابق السندَ (`mutabiqSanad`). -/
def mudaaSanad? (mudaat : Array (String × Idaa.Naw)) (s : String) : Option (String × Idaa.Naw) :=
  mudaat.toList.find? (mutabiqSanad s)

/-- نوعُ مودَعِ السند (سقفُ وسمه): نوعُ `mudaaSanad?`، وإلّا «مرجع محجوب» (أدنى السقوف). -/
def nawSanadMin (mudaat : Array (String × Idaa.Naw)) (s : String) : Idaa.Naw :=
  ((mudaaSanad? mudaat s).map (·.2)).getD .marjaMahjub

/-- **مودَعُ السند يُوجد حيث يُقبل السند، لا غير**: وجودُ `mudaaSanad?` هو قبولُ `Idaa.aslMusajjal` للسند على بصمات
    المودَعات نفسِها. -/
theorem nawSanad_aslMusajjal (mudaat : Array (String × Idaa.Naw)) (s : String) :
    (mudaaSanad? mudaat s).isSome =
      Idaa.aslMusajjal (fun _ : Unit => some s) (mudaat.toList.map (·.1)) () := by
  unfold mudaaSanad? Idaa.aslMusajjal
  apply Bool.eq_iff_iff.mpr
  rw [List.find?_isSome, List.any_eq_true]
  constructor
  · rintro ⟨m, hm, hp⟩; exact ⟨m.1, List.mem_map_of_mem hm, hp⟩
  · rintro ⟨b, hb, hp⟩
    obtain ⟨m, hm, rfl⟩ := List.mem_map.mp hb
    exact ⟨m, hm, hp⟩

/-- **لا سقفَ فوق «مرجع محجوب» إلّا لسندٍ مقبول**: إن أعطى `nawSanadMin` نفسُه سندًا نوعًا غيرَ «مرجع محجوب» فـ
    `Idaa.aslMusajjal` يقبله. (والعكسُ لا يلزم: سندٌ مقبولٌ مودَعُه «مرجع محجوب» نوعُه «مرجع محجوب».) -/
theorem nawSanad_sanad (mudaat : Array (String × Idaa.Naw)) (s : String)
    (h : nawSanadMin mudaat s ≠ .marjaMahjub) :
    Idaa.aslMusajjal (fun _ : Unit => some s) (mudaat.toList.map (·.1)) () = true := by
  rw [← nawSanad_aslMusajjal]
  unfold nawSanadMin at h
  cases hm : mudaaSanad? mudaat s with
  | none => rw [hm] at h; exact absurd rfl h
  | some m => rfl

/-- **السندُ الفارغ لا يأخذ نوعًا** (على الشاهد): سندٌ فارغٌ مع سجلٍّ فيه بصمةٌ سليمةٌ وأخرى فارغة يبقى «مرجع محجوب». -/
theorem nawSanad_sanad_farigh : nawSanadMin #[("", .wad), ("abc", .wad)] "" = .marjaMahjub := by
  decide +kernel

/-- **القيدُ الفارغ لا يعطي سندًا نوعَه** (على الشاهد): قيدٌ فارغٌ من نوع «وضع» قبل القيد الحقيقيّ لا يرفع سندًا من «مرجع
    محجوب» إلى سقف «وضع». -/
theorem nawSanad_basma_farigha :
    nawSanadMin #[("", .wad), ("abc", .marjaMahjub)] "abc@1" = .marjaMahjub ∧
    nawSanadMin #[("abc", .wad)] "abc@1" = .wad := by
  decide +kernel

def bina (h : Hal) (isdar : String) : Bina :=
  let asl? (p : Qadiyya) : Option Asl := h.usul.find? (·.qadiyya == p)
  let sijill := (h.mudaat.map (·.1)).toList
  let nawSanad (s : String) : Idaa.Naw := nawSanadMin h.mudaat s
  { q := ⟨isdar, (h.qawanin.map (·.1)).toList⟩
    aslB := fun p => Idaa.aslMusajjal (fun x => (asl? x).map (·.sanad)) sijill p
    aslW := fun p => ((asl? p).map fun a => qayd a.tariqa (Idaa.qaydMudaa (nawSanad a.sanad) a.wasm)).getD .ray
    qW := fun i => ((h.qawanin[i]?).map (·.2)).getD .ray
    asl? := asl?
    shuhud := fun m => shuhudMutabara h.mudaat.toList ((h.shawahid.filter (·.1 == m)).map (·.2)).toList }

def tatabbu (h : Hal) (b : Bina) (c : Iddia Qadiyya) : IO Unit := do
  let d := h.dh
  IO.println s!"  القول: {qadiyyaIsm d c.qawl}  — وسمه المحسوب: {wasmIsm (quwwatSilsila b.aslW b.qW c.silsila)}"
  for k in c.silsila do
    match k with
    | .asl p =>
      match b.asl? p with
      | some a => IO.println s!"    أصل  {qadiyyaIsm d p}  [{wasmIsm (b.aslW p).quwwa}]  سند: {a.sanad}"
      | none => IO.println s!"    أصل  {qadiyyaIsm d p}  [غير مودَع]"
    | .qanun i =>
      match h.qawanin[i]? with
      | some (r, w) =>
        IO.println s!"    قانون {i} «{r.ism}»: {" + ".intercalate (r.muqaddimat.map (qadiyyaIsm d))} ⊢ {qadiyyaIsm d r.natija}  [{wasmIsm w.quwwa}]"
      | none => IO.println s!"    قانون {i}  [غير موجود]"
  -- مراتب المخرج الثلاث (م15)
  for x in mukhraj b.shuhud c.qawl do
    match x with
    | .minHaythuHiya _ => IO.println s!"    مرتبة القضيّة: من حيث هي"
    | .maaluma m => IO.println s!"    المعنى «{d.ism m}»: معلومة (لا شاهد واقعٍ مودَع)"
    | .mafhum m sh _ => IO.println s!"    المعنى «{d.ism m}»: مفهوم (شواهد واقع: {sh.length})"

def faahis (h : Hal) (b : Bina) (isdar : String) : IO UInt32 := do
  let mut marfud := 0
  for (n, p, w, ks, _) in h.iddiaat do
    let quwwa := quwwatSilsila b.aslW b.qW ks
    if !(maqbul b.q b.aslB ⟨p, ks⟩) then
      IO.println s!"{n}\tمرفوض\tسلسلة لا يقبلها الفاحص"; marfud := marfud + 1
    else if w.quwwa > quwwa then
      IO.println s!"{n}\tمرفوض\tوسم فوق سنده"; marfud := marfud + 1
    else
      IO.println s!"{n}\tمقبول\t{quwwa}"
  for e in h.akhta do IO.println s!"خطأ\t{e}"
  IO.println s!"القاعدة {isdar}: مودَعات {h.mudaat.size}، قوانين {h.qawanin.size}، أصول {h.usul.size}، ادّعاءات {h.iddiaat.size}، مرفوض {marfud}، أخطاء {h.akhta.size}"
  return (if marfud == 0 && h.akhta.isEmpty then 0 else 1)

def sualMain (h : Hal) (b : Bina) (badia : String) : IO UInt32 := do
  let s := h.iddiaat.foldl (fun (s : Makhzan b.q b.aslB) (_, p, _, ks, sn) =>
    s.udkhul ⟨⟨p, ks⟩, sn⟩) (Makhzan.faregh b.q b.aslB)
  match sual s (fun p => (qadiyyaIsm h.dh p).startsWith badia) with
  | .laHukm =>
    IO.println s!"لا حكم: لا مدخل في المخزن يوافق «{badia}». الغياب ليس امتناعًا."
    return 0
  | .hukm j _ =>
    IO.println s!"حكم ({j.iddiaat.length}) بالقاعدة {b.q.isdar}:"
    for c in j.iddiaat do tatabbu h b c
    let (a, m, f) := ihsa (j.iddiaat.flatMap fun c => mukhraj b.shuhud c.qawl)
    IO.println s!"الفهرس: من حيث هي {a}، معلومة {m}، مفهوم {f}"
    return 0
