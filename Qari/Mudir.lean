import Nizam.Mudir
import Lean

/-!
# التنفيذيُّ `mudir` — مديرُ الوكلاء (وكيل NTP)

يتلقّى برومبتًا ويجيب عنه أو ينفّذه بوكلاء Mashru القائمين، بدوالّ النواة المبرهنة في `Nizam/Mudir.lean` بأعيانها:
القسمةُ `qismOf`، والقرارُ `qarar`، والخطّةُ `khitta`، ونتيجةُ الخطوة `natijaKhatwa`، والجامعةُ `natijaJamia`، والتصديقُ `tasdiqOf`،
ومعالجُ NTP `tasnifNTP`. فما يُطبع قرارًا وخطّةً ونتيجةً هو ما بُرهن عليه؛ وما يقوله كلُّ وكيلٍ فعلى وكيله وبراهينه.

الاستعمال:
  mudir [--qanat malik|wakil|majhul] [--isal <ملفّ>] [--iqtirahat <مجلّد>] <نصّ…>
  mudir --tahaqquq <ملفّ الإيصال>

* القناةُ بلا تعيينٍ «majhul»: لا مقامَ فلا أمر (قرارُ المالك ٢). والمالكُ يعيّنها لنفسه في الطرفيّة.
* الوكلاءُ تنفيذيّاتٌ في `.lake/build/bin` تحت جذر المستودع (`MASHRU_JADHR`، وإلّا المجلّدُ الحاليّ)، ومدخلاتُهم `mudaat/sijill.tsv`
  و`mawsua/makhzan_kamil.tsv` من المستودع نفسِه. ومعالجُ NTP والمتعلّمُ في هذه العمليّة.
* المتعلّمُ يكتب اقتراحًا في `--iqtirahat` (وإلّا `artifacts/local/mudir/iqtirahat`، وهو مُتجاهَلٌ في git)، ولا يمسّ `mudaat/` ولا `mawsua/`.
* الإيصال (`--isal`): JSON بالنصّ والقناة والقرار والخطّة، ولكلّ خطوةٍ خروجُها وبصمةُ مخرجها (sha256 بأداة النظام `sha256sum`) ونتيجتُها.
  و`--tahaqquq` يعيد التشغيلَ من النصّ والقناة المسجَّلين وحدهما (مجلّدُ اقتراحاتٍ مؤقّت)، ويطابق القرارَ والخطّةَ والبصمات.
* الخروج: 0 حكمٌ صدر، 1 لا حكم، 2 رفض، 3 خطأ؛ و4 لاستعمالٍ فاسد أو إيصالٍ لا يطابق.
-/

open Nizam.Mudir Lean

namespace MudirTanfidhi

def ismQanat : Qanat → String
  | .malik => "malik" | .wakil => "wakil" | .majhul => "majhul"

def qanatMin : String → Option Qanat
  | "malik" => some .malik | "wakil" => some .wakil | "majhul" => some .majhul | _ => none

def ismQism : Nizam.Hukm Nizam.Talab.Qism → String
  | .murakhkhas .amr => "أمر" | .murakhkhas .iltimas => "التماس" | .murakhkhas .sual => "سؤال"
  | .laHukm => "لا حكم (لا مقام)" | .mumtani s => s!"ممتنع: {s}"

def ismAmr : Amr → String
  | .iqra => "اقرأ" | .aarib => "أعرب" | .tatabba => "تتبّع" | .isal => "اسأل" | .ifhas => "افحص"
  | .sannif => "صنّف" | .taallam => "تعلّم" | .aard => "اعرض"

def ismMahzur : Mahzur → String
  | .idmaj => "ادمج" | .ikhtim => "اختم" | .ihdhif => "احذف" | .idfa => "ادفع"

def ismRafd : Rafd → String
  | .farigh => "لا نصّ"
  | .bilaMaqam a => s!"«{ismAmr a}» أمرٌ بلا مقام: القناةُ مجهولة، فطلبُ «افعل» لا حكم (Nizam.Talab.qisma، قرار المالك ٢)"
  | .ghayrMurakhkhas k a => s!"«{ismAmr a}» لا يرخّصه قسمُ «{ismQism (.murakhkhas k)}» (Nizam.Mudir.ruhsa: الالتماسُ يقرأ ولا يقترح)"
  | .mahzur m => s!"«{ismMahzur m}» سلطةُ المالك في الجلسة، لا يرخّصها المدير لأيّ قناة (CLAUDE.md، «السلطة»)"
  | .bilaHujja a => s!"«{ismAmr a}» يحتاج نصًّا بعده"

def ismQarar : Qarar → String
  | .tanfidh a x => s!"تنفيذ «{ismAmr a}»" ++ (if x.isEmpty then "" else s!" على «{x}»")
  | .qiraa n => s!"قراءة «{n}» (لا أمرَ في السجلّ بأوّل لفظه)"
  | .rafd r => s!"رفض: {ismRafd r}"

def ismNatija : Natija → String
  | .najah => "حكمٌ صدر" | .laHukm => "لا حكم" | .rafd => "رفضٌ باسمه" | .khata => "خطأ تنفيذ"

def khurujNatija : Natija → UInt32
  | .najah => 0 | .laHukm => 1 | .rafd => 2 | .khata => 3

def ismTasdiq : Tasdiq → String
  | .laHukmBilaShahid => "خبر: لا شاهدَ واقعٍ مودَع في هذه الخطّة، فلا حكم على مطابقته للواقع (الغيابُ ليس تكذيبًا)"
  | .ghayrQabil => "إنشاء: لا يُصدَّق ولا يُكذَّب؛ ولا أمرَ بلفظه في سجلّ المدير، فلا تنفيذ"
  | .laHukm => "قوّةُ الجملة لا حكم، فلا سؤالَ عن واقعها"

structure Bia where
  jadhr : String
  iqtirahat : String

def bin (b : Bia) (n : String) : String := b.jadhr ++ "/.lake/build/bin/" ++ n

def basma (s : String) : IO String := do
  let (h, p) ← IO.FS.createTempFile
  h.putStr s; h.flush
  let o ← IO.Process.output { cmd := "sha256sum", args := #[p.toString] }
  IO.FS.removeFile p
  return (o.stdout.splitOn " ").headD ""

def jumlaFile (x : String) : IO System.FilePath := do
  let (h, p) ← IO.FS.createTempFile
  h.putStr s!"j\t{x}\n"; h.flush
  return p

def tashghil (b : Bia) (cmd : String) (args : Array String) : IO (Nat × String) := do
  try
    let o ← IO.Process.output { cmd := cmd, args := args, cwd := some b.jadhr }
    return (o.exitCode.toNat, o.stdout ++ (if o.stderr.isEmpty then "" else "\n[stderr] " ++ o.stderr))
  catch e => return (127, s!"تعذّر تشغيل الوكيل «{cmd}»: {e}")

/-- خطوةٌ واحدة: الوكيلُ وحجّتُه ← (الخروج، المخرج). -/
def khatwa (b : Bia) (nass : String) (k : Khatwa) : IO (Nat × String) := do
  let sj := "mudaat/sijill.tsv"
  let mk := "mawsua/makhzan_kamil.tsv"
  match k.wakil with
  | .qari => tashghil b (bin b "qari") #[sj, mk, k.hujja]
  | .tarkib | .athar | .silsila =>
    let f ← jumlaFile k.hujja
    let r ← tashghil b (bin b k.wakil.ism) #[f.toString]
    IO.FS.removeFile f
    return r
  | .faahisSual => tashghil b (bin b "faahis") #["--sual", k.hujja, sj, mk]
  | .faahis => tashghil b (bin b "faahis") #[sj, mk]
  | .muallij => return (0, tasnifNTP k.hujja)
  | .mutaallim =>
    let ism := (← basma k.hujja).take 16
    IO.FS.createDirAll b.iqtirahat
    let p := b.iqtirahat ++ "/" ++ ism ++ ".tsv"
    IO.FS.writeFile p (s!"nass\t{k.hujja}\nqanat\tmalik\nbarumbt\t{nass}\n" ++
      "hal\tمقترح — لا يدخل المخزن ولا يُختم إلّا بإذن المالك (mudaat/idaa.py sajjil … --idhn)\n")
    return (0, s!"اقتراحُ إيداعٍ مكتوب: {ism}.tsv (في مجلّد الاقتراحات؛ لم يُمسّ mudaat/ ولا mawsua/)")

structure Sijill where
  khatwa : Khatwa
  khuruj : Nat
  makhraj : String
  basma : String
  natija : Natija

def quwwaMin (s : String) : Option String :=
  (s.splitOn "\n").findSome? fun l =>
    match l.splitOn "\t" with
    | _ :: "QUWWA" :: q :: _ => some q
    | _ => none

def sijillAwamirNass : String :=
  "\n".intercalate (sijillAwamir.map fun (l, f) =>
    match f with
    | .murakhkhas a => s!"  {l}\t← {ismAmr a} ({match a.nawAthar with | .qiraa => "قراءة" | .iqtirah => "اقتراح، للمالك وحده"})"
    | .mahzur m => s!"  {l}\t← محظور ({ismMahzur m}): سلطةُ المالك في الجلسة")

def shaghghil (b : Bia) (q : Qanat) (nass : String) : IO (Qarar × Array Sijill × Natija) := do
  let qr := qarar q nass
  let mut out : Array Sijill := #[]
  for k in khitta qr do
    let (c, m) ← khatwa b nass k
    out := out.push ⟨k, c, m, ← basma m, natijaKhatwa k.wakil c m⟩
  return (qr, out, natijaJamia qr (out.toList.map (·.natija)))

def ithbat (q : Qanat) (nass : String) (qr : Qarar) (ss : Array Sijill) (n : Natija) : Json :=
  Json.mkObj [
    ("schema", "mashru.mudir.isal.v1"),
    ("nass", nass), ("qanat", ismQanat q), ("qarar", toString (repr qr)),
    ("khitta", Json.arr (ss.map fun s => Json.mkObj [
      ("wakil", s.khatwa.wakil.ism), ("hujja", s.khatwa.hujja), ("khuruj", s.khuruj),
      ("basma", s.basma), ("natija", ismNatija s.natija)])),
    ("natija", ismNatija n)]

def qassBayad (s : String) : String := String.ofList (s.toList.reverse.dropWhile Char.isWhitespace).reverse

def arqam : List String := ["١", "٢", "٣", "٤", "٥", "٦", "٧", "٨", "٩"]

def tibaa (q : Qanat) (nass : String) (qr : Qarar) (ss : Array Sijill) (n : Natija) : IO Unit := do
  IO.println s!"المدير (Nizam.Mudir) — القناة: {ismQanat q} · قسمُ طلب «افعل» منها: {ismQism (qismOf q)}"
  IO.println s!"البرومبت: {nass}"
  IO.println s!"القرار: {ismQarar qr}"
  IO.println s!"الخطّة ({ss.size}): {" ← ".intercalate (ss.toList.map (·.khatwa.wakil.ism))}"
  IO.println "## ما فحصته الآلة"
  IO.println "- القرارُ والخطّةُ والنتيجةُ الجامعة بدوالّ Nizam.Mudir المبرهنة (Audit.lean، قسم Mudir)."
  for (s, i) in ss.toList.zip (List.range ss.size) do
    IO.println s!"- {arqam.getD i (toString (i+1))}. {s.khatwa.wakil.ism} «{s.khatwa.hujja}» · خروج {s.khuruj} · بصمة المخرج {s.basma.take 16} · {ismNatija s.natija}"
  IO.println "## الجواب"
  match qr with
  | .tanfidh .aard _ => IO.println s!"سجلُّ الأوامر (Nizam.Mudir.sijillAwamir)، والأمرُ لفظُه الأوّل مجرَّدًا من الحركات:\n{sijillAwamirNass}"
  | _ => pure ()
  for (s, i) in ss.toList.zip (List.range ss.size) do
    IO.println s!"### {arqam.getD i (toString (i+1))}. {s.khatwa.wakil.ism}"
    IO.println (qassBayad s.makhraj)
  IO.println "## ما بقي باسمه"
  match qr with
  | .rafd r => IO.println s!"- {ismRafd r}. لم يُشغَّل وكيل (Nizam.Mudir.rafd_la_khitta)."
  | .qiraa _ =>
    match ss.toList.head? >>= (fun s => quwwaMin s.makhraj) with
    | some w => IO.println s!"- قوّةُ الجملة في athar: «{w}» ← {ismTasdiq (tasdiqOf w)}."
    | none => IO.println "- لا سطرَ قوّةٍ في مخرج athar."
  | .tanfidh .aarib _ =>
    IO.println "- rabt (السلسلةُ كاملةً بجدول اللزوم) لم يدخل الخطّة: جدولُه luzum_mujam.tsv مودَعٌ في MUDAA_DIR لا في المستودع."
  | .tanfidh .sannif _ =>
    IO.println "- الشبكةُ NTP.Wasl.shabakaWasl شاهدٌ مبنيّ (أعدادُ شهوده مفروضة)، لا مودَعٌ مختوم."
  | .tanfidh .taallam _ =>
    IO.println "- الاقتراحُ لا يصير معلومةً سابقة حتّى يودعه المالك ويختمه بإذنه."
  | _ => pure ()
  for s in ss do
    if s.natija == .khata then IO.println s!"- خطأ تنفيذ في {s.khatwa.wakil.ism} (خروج {s.khuruj}): لا يُخفيه نجاحُ غيره (khata_yaghlib)."
  IO.println s!"النتيجة الجامعة: {ismNatija n}"

def tahaqquq (b : Bia) (p : String) : IO UInt32 := do
  let t ← IO.FS.readFile p
  let some j := (Json.parse t).toOption | IO.println "إيصالٌ لا يُقرأ JSON"; return 4
  let some nass := (j.getObjValAs? String "nass").toOption | IO.println "إيصالٌ بلا nass"; return 4
  let some qs := (j.getObjValAs? String "qanat").toOption | IO.println "إيصالٌ بلا qanat"; return 4
  let some q := qanatMin qs | IO.println s!"قناةٌ مجهولة في الإيصال: {qs}"; return 4
  let tmp := (← IO.FS.createTempDir).toString
  let (qr, ss, n) ← shaghghil { b with iqtirahat := tmp } q nass
  let jadid := ithbat q nass qr ss n
  let mut farq : Array String := #[]
  if (j.getObjValAs? String "qarar").toOption != some (toString (repr qr)) then farq := farq.push "القرار"
  if (j.getObjValAs? String "natija").toOption != some (ismNatija n) then farq := farq.push "النتيجة الجامعة"
  let qadim := ((j.getObjValAs? (Array Json) "khitta").toOption).getD #[]
  let hadith := ((jadid.getObjValAs? (Array Json) "khitta").toOption).getD #[]
  if qadim.size != hadith.size then farq := farq.push s!"عدد الخطوات ({qadim.size} ← {hadith.size})"
  for (a, i) in (qadim.toList.zip hadith.toList).zip (List.range qadim.size) do
    if a.1.compress != a.2.compress then farq := farq.push s!"الخطوة {i + 1}"
  if farq.isEmpty then
    IO.println s!"الإيصال يطابق إعادةَ التشغيل: القرار والخطّة ({hadith.size}) والبصمات والنتيجة ({ismNatija n})."
    return 0
  else
    IO.println s!"الإيصال لا يطابق إعادةَ التشغيل في: {", ".intercalate farq.toList}"
    return 4

end MudirTanfidhi

open MudirTanfidhi in
def main (args : List String) : IO UInt32 := do
  let jadhr := (← IO.getEnv "MASHRU_JADHR").getD (← IO.currentDir).toString
  let b0 : Bia := ⟨jadhr, jadhr ++ "/artifacts/local/mudir/iqtirahat"⟩
  let rec ahlil (q : Qanat) (isal : Option String) (b : Bia) : List String → IO UInt32
    | "--tahaqquq" :: p :: [] => tahaqquq b p
    | "--qanat" :: v :: r =>
      match qanatMin v with
      | some q' => ahlil q' isal b r
      | none => do IO.eprintln s!"قناةٌ مجهولة: «{v}» (malik|wakil|majhul)"; return 4
    | "--isal" :: p :: r => ahlil q (some p) b r
    | "--iqtirahat" :: d :: r => ahlil q isal { b with iqtirahat := d } r
    | ws => do
      let nass ← if ws.isEmpty then (do let s ← (← IO.getStdin).readToEnd; pure (qassBayad (String.ofList (s.toList.dropWhile Char.isWhitespace)))) else pure (" ".intercalate ws)
      let (qr, ss, n) ← shaghghil b q nass
      tibaa q nass qr ss n
      if let some p := isal then IO.FS.writeFile p ((ithbat q nass qr ss n).pretty ++ "\n")
      return khurujNatija n
  ahlil .majhul none b0 args
