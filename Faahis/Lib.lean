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

  صيغة الملفّ (TAB بين الحقول):
    mudaa   <sha256>  <النوع: واقع-مختوم|وضع|معلومات-سابقة|مرجع-محجوب>  <الاسم>
    isdar   <الإصدار>
    qanun   <الاسم>  <مقدّمة|مقدّمة…>  <النتيجة>  <الوسم>
    asl     <القضيّة>  <الوسم>  <السند>  [<الطريقة: عقلي|علمي>]
    iddia   <القضيّة>  <الوسم المعلَن>  <خطوة|خطوة…>  <السند>
    shahid  <المعنى>  <بصمة>@<موضع>
  القضيّة: نوع:أ:ب حيث النوع أحد: wad juz kharij luzum mutabaqa tadammun iltizam fi taht.
  الخطوة: a=<قضيّة> أو q=<رقم القانون>. السند: <أوّل 12 من البصمة>@<الموضع>…
  التشغيل: faahis <ملفّ>…   |   faahis --sual <بادئة القضيّة> <ملفّ>…
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
      match t.splitOn "=" with
      | ["a", p] => let (d, q) := qadiyyaMin d p; (d, q.map fun q => ks ++ [.asl q])
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

/-! ## البناء -/

structure Bina where
  q    : Qaida.Qaida Qadiyya
  aslB : Qadiyya → Bool
  aslW : Qadiyya → Wasm
  qW   : Nat → Wasm
  asl? : Qadiyya → Option Asl
  shuhud : Nat → List ShahidWaqi

def bina (h : Hal) (isdar : String) : Bina :=
  let asl? (p : Qadiyya) : Option Asl := h.usul.find? (·.qadiyya == p)
  let sijill := (h.mudaat.map (·.1)).toList
  let nawSanad (s : String) : Idaa.Naw :=
    ((h.mudaat.find? (fun m => s.startsWith m.1)).map (·.2)).getD .marjaMahjub
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
