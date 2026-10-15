/-
  Faahis/Main.lean — نقطة دخول الفاحص التنفيذيّ. الشرح والصيغة في Faahis/Lib.lean.
-/
import Faahis.Lib

def main (args : List String) : IO UInt32 := do
  let (sual?, badia, paths) := match args with
    | "--sual" :: b :: ps => (true, b, ps)
    | ps => (false, "", ps)
  if paths.isEmpty then
    IO.eprintln "الاستعمال: faahis <ملفّ>…  |  faahis --sual <بادئة> <ملفّ>…"; return 2
  let mut lines : Array String := #[]
  for p in paths do lines := lines ++ (← IO.FS.lines p)
  let h := (lines.toList.zipIdx 1).foldl (fun h (l, n) => qira h n l) {}
  let some isdar := h.isdar | IO.eprintln "لا إصدار للقاعدة"; return 1
  let b := bina h isdar
  if sual? then sualMain h b badia else faahis h b isdar
