/-
  Qari/Rabt.lean — التنفيذيّ `rabt`: السلسلةُ كاملةً على قراءة الجملة بالعوامل (`Nizam.Rabt`).
  `rabt <luzum_mujam.tsv> <ملفّ: مفتاح⇥جملة>`: لكلّ جملةٍ حكمُها (`Jisr.Tahlil.hukmJumla`)، ولكلّ قراءةٍ مرخَّصة جدولُ إعرابها (الدورُ والحالةُ
  والعامل والنسبة)، وإسنادُها، وقوّتُها، وإحالةُ ضمائرها (إلى ما سبقها في الملفّ)، ومنطوقُها، وقيدُها ومفهومُها على الودائع المرشَّحة،
  ودلالةُ ألفاظها على جدول اللزوم (كلُّ ادّعاءٍ بقبول الفاحص `Qaida.maqbul`). والجدولُ `luzum_mujam.tsv` مرشَّحٌ يحتاج ختمًا، ومكانُه MUDAA_DIR.
-/
import Nizam.Rabt
import Std.Data.HashMap

open Nizam.Rabt Jisr.Tahlil

def ismDawr : Dawr → String
  | .rabit => "رابط" | .jazim => "جازم" | .nasib => "ناصب" | .nafiya => "نافية" | .fil => "فعل" | .fail => "فاعل"
  | .maful => "مفعول_به" | .mubtada => "مبتدأ" | .khabar => "خبر" | .harfJarr => "حرف_جر" | .majrur => "مجرور"
  | .mudafIlayh => "مضاف_إليه" | .kharij => "خارج"

def ismHukm : Jisr.Utur.Hukm → String
  | .murakhkhas => "مقبول" | .mumtani => "خطأ" | .laHukm => "لا_حكم"

def ismHalaN : Nat → String
  | 0 => "نصب" | 1 => "رفع" | 2 => "جرّ" | 3 => "جزم" | _ => "؟"

def alama (c : Nat) : String :=
  if c < 116 then String.singleton (Dal.hawamil.getD (c / 4) ' ') ++
    (match c % 4 with | 0 => "َ" | 1 => "ُ" | 2 => "ِ" | _ => "ْ")
  else "؟"

def nassKhalaya (cs : List Nat) : String := String.join (cs.map alama)

structure Jumla where
  kalimat : List Nizam.Silsila.KalimaM
  dal : List Dal.Kalima

def nassWahda (j : Jumla) (w : Wahda) : String :=
  match j.dal[w.kalima]?, j.kalimat[w.kalima]? with
  | some k, some km => if k.khalaya == w.khalaya then String.ofList km.w else nassKhalaya w.khalaya
  | _, _ => nassKhalaya w.khalaya

def nassKalima (j : Jumla) (k : Nat) : String := (j.kalimat[k]?.map (String.ofList ·.w)).getD "؟"

def ismAmil (j : Jumla) (m : Murashshah) : Amil → String
  | .saff i => "«" ++ Nizam.Athar.lafz i ++ "» (صفّ " ++ toString i ++ " من جدول العوامل)"
  | .tajarrud => "التجرّد من الناصب والجازم (القطر L96)"
  | .fil k => "الفعل «" ++ ((m.adwar.find? fun p => p.2 == .fil && p.1.kalima == k).map (nassWahda j ·.1)).getD (nassKalima j k) ++
      "» (الألفية L312، L361)"
  | .ibtida => "الابتداء (الألفية L181)"
  | .mubtada k => "المبتدأ «" ++ nassKalima j k ++ "» (الألفية L181)"
  | .idafa k => "الإضافة إلى «" ++ nassKalima j k ++ "» (القطر L339)"
  | .bina => "—"
  | .kharij => "خارج المجال"

def ismHala : Hala → String
  | .zahira h => ismHalaN h
  | .mushtaraka h hs => ismHalaN h ++ " (علامتُها تحتمل " ++ ", ".intercalate (hs.map ismHalaN) ++ ")"
  | .muqaddara => "مقدَّرة"
  | .mahall h => "مبنيّ في محلّ " ++ ismHalaN h
  | .mabni => "مبنيّ"
  | .ghayrMatluba hs => "لا يطلب الموضعُ حالةً (" ++ ", ".intercalate (hs.map ismHalaN) ++ ")"
  | .laHala => "—"

def ismNisba : Option Jisr.Nisab.Nisba → String
  | some .isnadiyya => "إسناديّة" | some .taqyidiyya => "تقييديّة" | some .idafiyya => "إضافيّة" | none => "—"

def ismFeat (ft : SLGE.Maqam.Feat) : String :=
  (match ft.1 with | 1 => "متكلّم" | 2 => "مخاطَب" | _ => "غائب") ++ " " ++
  (if ft.2.1 == 1 then "مؤنّث" else "مذكّر") ++ " " ++ (match ft.2.2 with | 1 => "مثنّى" | 2 => "جمع" | _ => "مفرد")

def ismSura : Sura → String
  | .zahir => "ظاهر" | .bariz => "ضميرٌ بارزٌ متّصل" | .mustatar => "ضميرٌ مستتر"

def ismQayd : Jisr.MantuqMafhum.Qayd → String
  | .sifa => "الصفة" | .shart => "الشرط" | .ghaya => "الغاية" | .adad => "العدد" | .ism => "الاسم"

/-! ## جدولُ اللزوم المرشَّح -/

def nawOf : String → Option JadwalLuzum.Naw
  | "juz" => some .juz | "taraduf" => some .taraduf | "luzum" => some .luzum | "kharij" => some .kharij | "asl" => some .asl
  | _ => none

abbrev Jadwal := Std.HashMap String (Array JadwalLuzum.Saff)

def qiraJadwal (path : String) : IO Jadwal := do
  let mut t : Jadwal := {}
  for line in ← IO.FS.lines path do
    match line.splitOn "\t" with
    | m :: a :: w :: q :: b :: s :: _ =>
      match nawOf q, (if m == "lisan" then some JadwalLuzum.Mujam.lisan else if m == "maqayis" then some .maqayis else none),
          s.toNat? with
      | some n, some mj, some sn => t := t.insert a ((t.getD a #[]).push ⟨mj, a, w, n, b, sn⟩)
      | _, _, _ => pure ()
    | _ => pure ()
  return t

def ismMujam : JadwalLuzum.Mujam → String
  | .lisan => "اللسان" | .maqayis => "المقاييس"

/-- دلالاتُ جذرٍ بأنواعها: أوّلُ خمسةٍ من كلّ نوع (المقاييسُ أوّلًا)، وكلُّ ادّعاءٍ بقبول الفاحص على جدول صفوفه المعروضة. -/
def dalalat (t : Jadwal) (r : String) : List String :=
  let rows := (t.getD r #[]).toList
  let maq := rows.filter (·.mujam == .maqayis)
  let lis := rows.filter (·.mujam == .lisan)
  let naw (ns : List JadwalLuzum.Naw) (ism : String) : List String :=
    let all := (maq ++ lis).filter (ns.contains ·.naw)
    let shown := all.take 5
    if shown.isEmpty then []
    else
      let ok := shown.all fun x => Qaida.maqbul (JadwalLuzum.qaidaOf shown) (JadwalLuzum.aslB shown) (iddiaOf shown x)
      [s!"    {ism}: " ++ ", ".intercalate (shown.map fun x => s!"{x.b} ({ismMujam x.mujam} س{x.satr})") ++
        (if all.length > 5 then s!" … ({all.length} صفًّا)" else "") ++ (if ok then " [يقبلها الفاحص]" else " [يردّها الفاحص]")]
  naw [.taraduf] "مطابقة" ++ naw [.juz, .asl] "تضمّن" ++ naw [.luzum] "التزام" ++ naw [.kharij] "خارجٌ عن المدلول"

/-! ## الجملة -/

def wahdatIsm (m : Murashshah) : List Wahda := (m.adwar.filter fun p => p.1.naw == .ism).map (·.1)

def sharh (t : Jadwal) (j : Jumla) (nusus : Array (List String)) (qabl : List (Nat × Wahda)) (jn : Nat) (m : Murashshah) :
    List String :=
  let es := irab m
  let tab := es.map fun e =>
    s!"  {nassWahda j e.wahda}\t{ismDawr e.dawr}\t{ismHala e.hala}\tالعامل: {ismAmil j m e.amil}\tالنسبة: {ismNisba (nisba e.dawr)}"
  let (q, qs) := quwwaOf m
  let isn := match isnadOf m with
    | some i =>
      let mus := match i.musnad with | some v => "«" ++ nassWahda j v ++ "»" | none => "شبهُ الجملة"
      let il := match i.ilayh with
        | some v => "«" ++ nassWahda j v ++ "»"
        | none => ismSura i.sura ++ " (" ++ ismFeat i.ft ++ ")" ++
            (match i.wujub with | some true => " وجوبًا" | some false => " جوازًا" | none => "")
      [s!"  الإسناد (الكتاب س234–237): المسند {mus}، والمسند إليه {il}"]
    | none => []
  let ih := (ihalat qabl jn m).map fun i =>
    let r := match i.marji with
      | .hudur => "الحضور (المتكلّم أو المخاطَب)"
      | .murashshahun [] => "لا مرشَّحَ قبله"
      | .murashshahun l => "مرشَّحون بعدده (الأقربُ أوّلًا): " ++ "، ".intercalate ((l.take 3).map fun (p : Nat × Nat) =>
          "«" ++ ((if p.1 == jn then j.kalimat.map (fun (x : Nizam.Silsila.KalimaM) => String.ofList x.w) else nusus.getD p.1 []).getD p.2 "؟") ++ "» (الجملة " ++
            toString (p.1 + 1) ++ ")")
    s!"  الإحالة: «{nassKalima j i.kalima}» {ismSura i.sura} ({ismFeat i.ft}) ← {r}"
  let quyud := es.filterMap fun e =>
    match nisba e.dawr with
    | some .taqyidiyya => some ("«" ++ nassWahda j e.wahda ++ "» (" ++ ismDawr e.dawr ++ ")")
    | some .idafiyya => some ("«" ++ nassWahda j e.wahda ++ "» (" ++ ismDawr e.dawr ++ ")")
    | _ => none
  let mantuq := s!"  المنطوق: {Nizam.Athar.quwwaIsm q}" ++
    (match isnadOf m with
     | some i => "، إسنادُ " ++ (match i.musnad with | some v => "«" ++ nassWahda j v ++ "»" | none => "شبه الجملة") ++ " إلى " ++
         (match i.ilayh with | some v => "«" ++ nassWahda j v ++ "»" | none => ismSura i.sura)
     | none => "") ++
    (if quyud.isEmpty then "" else "، مقيَّدًا بـ " ++ "، ".intercalate quyud)
  let qd := match qaydR m with
    | some (k, w) => s!"  القيد: {ismQayd k} من «{nassWahda j w}» (Jisr.QaydMafhum.unsurQayd)"
    | none => "  القيد: لا قيدَ في البنية"
  let W := wadaMurashshaha m
  let mf := mafahim m W
  let mfs := if mf.isEmpty then ["  المفهوم (على الودائع المرشَّحة): لا مفهوم"]
    else mf.map fun f => match f.naw with
      | .mukhalafa _ => s!"  المفهوم (على الودائع المرشَّحة — تحتاج ختمًا): مخالفةُ {ismQayd f.lazim.1} (ج3 س566): نفيُ الحكم عند انتفاء {ismQayd f.lazim.1} «{nassKalima j f.lazim.2} {nassKalima j (f.lazim.2 + 1)}»"
      | _ => "  المفهوم: (غير المخالفة)"
  let haml := s!"  الودائعُ المرشَّحة (تحتاج ختمًا): الحملُ على الحقيقة اللغويّة {(W.haml.filter (· == .haqiqa .lughawiyya)).length} من {W.haml.length} كلمة، ولا أغلبَ ولا معطِّل؛ وعلى المختومة وحدها: المفهومُ معلَّقٌ بالحمل والأغلب والمعطِّل"
  let dal := es.flatMap fun e =>
    let rs := judhurWahda e.wahda
    if rs.isEmpty then []
    else rs.flatMap fun r =>
      (mafatih e.wahda r).flatMap fun k =>
        let ds := dalalat t k
        if ds.isEmpty then [] else [s!"  الدلالة: «{nassWahda j e.wahda}» جذرُه {k} (عنوانٌ في اللسان، وصفوفُه في جدول اللزوم المرشَّح)"] ++ ds
  ["  " ++ "قراءة: " ++ " ".intercalate (m.adwar.map (ismDawr ·.2))] ++ tab ++ isn ++
    [s!"  القوّة: {Nizam.Athar.quwwaIsm q} — {qs}"] ++ ih ++ [mantuq, qd] ++ mfs ++ [haml] ++ dal

def main (args : List String) : IO UInt32 := do
  match args with
  | [luzum, path] =>
    let t ← qiraJadwal luzum
    IO.println s!"# جدول اللزوم المرشَّح (يحتاج ختمًا): {t.size} جذرًا"
    let mut qabl : List (Nat × Wahda) := []
    let mut nusus : Array (List String) := #[]
    let mut jn := 0
    for line in ← IO.FS.lines path do
      match line.splitOn "\t" with
      | [k, s] =>
        let c := s.toList
        if !Nizam.Silsila.kullMaqrua c then IO.println s!"{k}\tRAFD\tكلمةٌ لم يقرأها القارئ"
        else
          let ws := Nizam.Silsila.kalimatDal c
          let j : Jumla := ⟨Nizam.Silsila.kalimatM c, ws⟩
          IO.println s!"{k}\t{s}\t{ismHukm (hukmJumla ws)}"
          let ms := maqbula ws
          for m in ms do
            for l in sharh t j nusus qabl jn m do IO.println l
          match ms.head? with
          | some m => qabl := qabl ++ (wahdatIsm m).map (jn, ·)
          | none => pure ()
        nusus := nusus.push ((Nizam.Silsila.kalimatM c).map (String.ofList ·.w))
        jn := jn + 1
      | _ => IO.println s!"{line}\tKHALAL\tسطرٌ ليس «مفتاح⇥جملة»"
    return 0
  | _ => IO.eprintln "الاستعمال: rabt <luzum_mujam.tsv> <ملفّ: مفتاح⇥جملة>"; return 2
