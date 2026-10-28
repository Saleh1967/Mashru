import Dal.Tahsil

/-!
# أداةُ التحصيل (`tahsil`)

تطبع تحصيلَ `Dal/Tahsil.lean` وشهادتَه لكلّ مقطع، ليقارنه `tahaqquq/test_tahsil.py` بالعرّاف المستقلّ وبالقارئ. ليست في المحرّك؛
والقارئ (`Qari/Main.lean`) يقرأ على التحصيل نفسِه منذ وصله به (`Dal/QiraaTahsil.lean`).

المدخل: سطرٌ لكلّ نصّ «مفتاح⇥نقاطُ رمزٍ عشريّةٌ مفصولةٌ بفراغ» (فلا يلتبس الفاصلُ ولا السطرُ الجديد بالنصّ).
المخرج لكلّ نصّ:
- لكلّ مقطع: `مفتاح⇥M⇥i⇥a⇥b⇥L|P|F⇥الصنف⇥الاسم⇥الخلايا⇥حكمُ الفاحص على شهادته`؛ والخلايا أرقامُ المالك (`Dal.n`) مفصولةً بفاصلة.
- لكلّ كلمة: `مفتاح⇥K⇥a⇥b⇥1|0⇥الخلايا`.
-/

open Dal.Tahsil

def sinfIsm : Sinf → String
  | .fasil => "fasil" | .tatwil => "tatwil" | .harfMadd => "harfMadd" | .harfHaraka => "harfHaraka" | .hamzaWasl => "hamzaWasl"

def khalayaIsm (ks : List Dal.Khaliya) : String := ",".intercalate (ks.map fun k => toString (Dal.n k).val)

def natijaIsm : Nizam.Shahada.Natija → String
  | .ghayrMarbut => "ghayrMarbut"
  | .madkhalFasid s => s!"madkhalFasid:{s}"
  | .mumtani s => s!"mumtani:{s}"
  | .laTantabiq s => s!"laTantabiq:{s}"
  | .muallaq l => s!"muallaq:{"|".intercalate l}"
  | .murakhkhas => "murakhkhas"

def hukmAmdida : Hukm → String
  | .L s ks => s!"L\t{sinfIsm s}\t\t{khalayaIsm ks}"
  | .P ism => s!"P\t-\t{ism}\t"
  | .F ism => s!"F\t-\t{ism}\t"

def nassMin (s : String) : List Char :=
  ((s.splitOn " ").filter (· != "")).map fun x => Char.ofNat x.toNat!

def main (args : List String) : IO UInt32 := do
  match args with
  | [path] =>
    for line in ← IO.FS.lines path do
      match line.splitOn "\t" with
      | [k, s] =>
        let t := nassMin s
        let src : Nabt.UnitDiscovery.Source Char := ⟨0, 0, 0, 0, t⟩
        for m in tahsil t do
          IO.println s!"{k}\tM\t{m.i}\t{m.a}\t{m.b}\t{hukmAmdida m.hukm}\t{natijaIsm (Nizam.Shahada.hukm (shahada src m))}"
        for w in kalimat t do
          IO.println s!"{k}\tK\t{w.a}\t{w.b}\t{if w.murakhkhasa then 1 else 0}\t{khalayaIsm w.khalaya}"
      | _ => IO.println s!"{line}\tKHALAL\tسطرٌ ليس «مفتاح⇥نصّ»"
    return 0
  | _ => IO.eprintln "الاستعمال: tahsil <ملفّ: مفتاح⇥نقاطُ رمزٍ عشريّة>"; return 2
