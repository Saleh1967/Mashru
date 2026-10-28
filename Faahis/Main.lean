/-
  Faahis/Main.lean — نقطة دخول الفاحص التنفيذيّ. الشرح والصيغة في Faahis/Lib.lean.
  الملفّ الأوّل سجلُّ المودَعات (السلطة)، والبقيّة محتوًى (`tahmil`). والسؤال لا يجيب إلّا على حالٍ محقَّقة
  (`muhaqqaq`): خطأُ التحميل يُطبع باسمه ويخرج بغير صفر، ولا يُسقَط بصمت.
-/
import Faahis.Lib

def istimal : String :=
  "الاستعمال: faahis [--ikhtibar] <سجلّ المودَعات> <ملفّ المحتوى>…  |  faahis [--ikhtibar] --sual <بادئة> <سجلّ المودَعات> <ملفّ المحتوى>…"

def main (args0 : List String) : IO UInt32 := do
  -- السجلُّ المعتمد (P1-ج): غيرُ `mudaat/sijill.tsv` المختوم خطأُ تحميلٍ إلّا بـ`--ikhtibar` معلَنًا (`tahmilMutamad`، `mutamad_salim`).
  let (ikhtibar, args) := match args0 with
    | "--ikhtibar" :: r => (true, r)
    | r => (false, r)
  if ikhtibar then IO.eprintln "سجلُّ اختبار (--ikhtibar): السلطةُ غيرُ السجلّ المختوم"
  let (sual?, badia, paths) := match args with
    | "--sual" :: b :: ps => (true, b, ps)
    | ps => (false, "", ps)
  match paths with
  | sj :: ps@(_ :: _) =>
    let sijill ← IO.FS.lines sj
    let mut muhtawa : Array String := #[]
    for p in ps do muhtawa := muhtawa ++ (← IO.FS.lines p)
    let h := tahmilMutamad ikhtibar sijill.toList muhtawa.toList
    if sual? then
      match muhaqqaq h with
      | .error e =>
        for x in e do IO.println s!"خطأ تحميل\t{x}"
        IO.println s!"لا جواب: التحميل لم يتحقّق ({e.size} خطأ). وخطأُ التحميل غيرُ «لا حكم»."
        return 1
      | .ok h =>
        let some isdar := h.isdar | IO.eprintln "لا إصدار للقاعدة"; return 1
        sualMain h (bina h isdar) badia
    else
      let some isdar := h.isdar | IO.eprintln "لا إصدار للقاعدة"; return 1
      faahis h (bina h isdar) isdar
  | _ => IO.eprintln istimal; return 2
