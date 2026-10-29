import Nizam.Silsila

/-!
# أداةُ السلسلة (`silsila`)

تطبع سلسلةَ الشهادات (`Nizam/Silsila.lean`) لكلّ جملة: الجملةَ ثمّ كلماتِها ومقاطعَ تحصيل كلّ كلمة ثمّ إطاراتِها، كلُّ عقدةٍ بموضعها
وقاعدتها وحكم الفاحص (`Nizam.Shahada.hukm`) على شهادتها، ومقدّماتُها بنوعها وحالها الفعليّة وسندها. ويفحصها `tahaqquq/test_silsila.py`.
تنفيذيٌّ مستقلٌّ عن القارئ (`Qari/Main.lean`) فلا تتغيّر بصمتُه.

المدخل: سطرٌ لكلّ جملة «مفتاح⇥جملة مشكولة» (الفاصلُ بين الكلمات U+0020).
المخرج لكلّ جملة (حقولٌ مفصولةٌ بـ⇥):
- `مفتاح JUMLA ربط حكم مخرج بدائل قاعدة حدّ` — الربطُ `1` أو `0` (`Naqla.marbut`)، والبدائلُ مفصولةٌ بـ « | ».
- `مفتاح KALIMA رقم كلمة بداية-نهاية ربط حكم خلايا`.
- `مفتاح MAQTA رقم.رقم مقطع بداية-نهاية قاعدة حكم` — والموضعُ في الكلمة (مصدرُ المقطع حروفُ كلمته).
- `مفتاح ITAR رقم أدوار حكم_الستّة حكم_الفاحص`.
- `مفتاح MUQ عقدة نوع حال اسم سند` — لكلّ مقدّمة، والعقدةُ `jumla` أو `kalima i` أو `itar j`.
والحكم: `مرخص`، `معلق: …`، `ممتنع: …`، `لا_تنطبق: …`، `مدخل_فاسد: …`، `غير_مربوط`؛ والحال: `مشهود`، `منفي`، `لم_يفحص`.
-/

open Nizam.Shahada

def natijaIsm : Natija → String
  | .ghayrMarbut => "غير_مربوط"
  | .madkhalFasid x => "مدخل_فاسد: " ++ x
  | .mumtani x => "ممتنع: " ++ x
  | .laTantabiq x => "لا_تنطبق: " ++ x
  | .muallaq l => "معلق: " ++ " | ".intercalate l
  | .murakhkhas => "مرخص"

def nawIsm : Naw → String
  | .madkhal => "مدخل" | .shart => "شرط" | .mani => "مانع"

def halIsm : Hal → String
  | .mashhud => "مشهود" | .manfi => "منفي" | .ghayrMafhus => "لم_يفحص"

def hukmIsm : Jisr.Utur.Hukm → String
  | .murakhkhas => "مقبول" | .mumtani => "خطأ" | .laHukm => "لا_حكم"

def bitIsm (b : Bool) : String := if b then "1" else "0"

def muq (k uqda : String) (ms : List Muqaddima) : IO Unit :=
  for m in ms do IO.println s!"{k}\tMUQ\t{uqda}\t{nawIsm m.naw}\t{halIsm m.halFiil}\t{m.ism}\t{m.sanad}"

def silsila (k s : String) : IO Unit := do
  let t := s.toList
  let j := Nizam.Silsila.jumla t
  IO.println s!"{k}\tJUMLA\t{bitIsm j.marbut}\t{natijaIsm (hukm j)}\t{j.makhraj}\t{" | ".intercalate j.badail}\t{j.qaida.ism}\t{j.hadd}"
  muq k "jumla" j.muqaddimat
  for kw in Nizam.Silsila.kalimatM t do
    let n := Nizam.Silsila.uqdaK t kw
    let c := ",".intercalate (n.makhraj.map toString)
    IO.println s!"{k}\tKALIMA\t{kw.i + 1}\t{String.ofList kw.w}\t{n.mawdi.start}-{n.mawdi.stop}\t{bitIsm n.marbut}\t{natijaIsm (hukm n)}\t{c}"
    muq k s!"kalima {kw.i + 1}" n.muqaddimat
    for m in Dal.Tahsil.tahsil kw.w do
      let sh := Dal.Tahsil.shahada (Nizam.Silsila.masdarKalima kw.w kw.i) m
      IO.println s!"{k}\tMAQTA\t{kw.i + 1}.{m.i + 1}\t{String.ofList m.nass}\t{sh.mawdi.start}-{sh.mawdi.stop}\t{sh.qaida.ism}\t{natijaIsm (hukm sh)}"
  let us := Nizam.Silsila.uqadUtur t
  let hs := Nizam.Silsila.uturHukm t
  for (u, h, i) in us.zip (hs.zip (List.range us.length)) do
    IO.println s!"{k}\tITAR\t{i + 1}\t{u.makhraj}\t{hukmIsm h.2}\t{natijaIsm (hukm u)}"
    muq k s!"itar {i + 1}" u.muqaddimat

def main (args : List String) : IO UInt32 := do
  match args with
  | [path] =>
    for line in ← IO.FS.lines path do
      match line.splitOn "\t" with
      | [k, s] => silsila k s
      | _ => IO.println s!"{line}\tKHALAL\tسطرٌ ليس «مفتاح⇥جملة»"
    return 0
  | _ => IO.eprintln "الاستعمال: silsila <ملفّ: مفتاح⇥جملة>"; return 2
