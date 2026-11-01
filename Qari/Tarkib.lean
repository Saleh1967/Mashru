/-
  Qari/Tarkib.lean — التنفيذيّ `tarkib`: قراءةُ الجملة بالعوامل (`Jisr.Tahlil`). لكلّ سطرٍ «مفتاح⇥جملة»:
  `مفتاح⇥الحكم⇥قراءة | قراءة …` (القراءاتُ المرخَّصة بأدوار وحداتها)، أو `مفتاح⇥RAFD⇥…` إن لم يقرأ القارئُ كلَّ كلماتها.
  وبـ`--tafsil`: كلُّ مرشَّحٍ بحكمه وإطاره.
-/
import Nizam.Silsila
import Jisr.Tahlil

open Jisr.Tahlil

def ismDawr : Dawr → String
  | .rabit => "رابط" | .jazim => "جازم" | .nasib => "ناصب" | .nafiya => "نافية" | .fil => "فعل" | .fail => "فاعل"
  | .maful => "مفعول_به" | .mubtada => "مبتدأ" | .khabar => "خبر" | .harfJarr => "حرف_جر" | .majrur => "مجرور"
  | .mudafIlayh => "مضاف_إليه" | .kharij => "خارج"

def ismHukm : Jisr.Utur.Hukm → String
  | .murakhkhas => "مقبول" | .mumtani => "خطأ" | .laHukm => "لا_حكم"

def satr (k s : String) (tafsil : Bool) : String :=
  let t := s.toList
  if !Nizam.Silsila.kullMaqrua t then s!"{k}\tRAFD\tكلمةٌ لم يقرأها القارئ"
  else
    let ws := Nizam.Silsila.kalimatDal t
    let qs := (adwarMaqbula ws).map fun ds => " ".intercalate (ds.map ismDawr)
    let r := s!"{k}\t{ismHukm (hukmJumla ws)}\t{" | ".intercalate qs}"
    if !tafsil then r
    else r ++ String.join ((murashshahun ws).map fun m =>
      s!"\n{k}\tMURASHSHAH\t{ismHukm (hukmM ws m)}\t{" ".intercalate (m.adwar.map (ismDawr ·.2))}\t{repr m.itar.ud.f}")

def main (args : List String) : IO UInt32 := do
  let (tafsil, args) := match args with | "--tafsil" :: r => (true, r) | r => (false, r)
  match args with
  | [path] =>
    for line in ← IO.FS.lines path do
      match line.splitOn "\t" with
      | [k, s] => IO.println (satr k s tafsil)
      | _ => IO.println s!"{line}\tKHALAL\tسطرٌ ليس «مفتاح⇥جملة»"
    return 0
  | _ => IO.eprintln "الاستعمال: tarkib [--tafsil] <ملفّ: مفتاح⇥جملة>"; return 2
