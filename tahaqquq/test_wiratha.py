"""الوراثةُ الصنفيّة للملفّات: كلُّ ملفّ Lean مرخَّصٌ بالتدرّج ويحمل جيناته (البوّابة ٥خ٣؛ `hawkama/الوراثة_الصنفية.md`؛ `Nizam/Wiratha.lean`).

قولُ المالك في الجلسة (2026-11-01، 19:11 بتوقيت عمّان):
«الخل ان كل module يجب ان يكون بالترخيص الجبري المتدرج فكل module يخضع لقانون الوراثة والتوريث ويدخل في ال slot machine  وهو حامل جيناته الحسابية»
وقراءةُ «module» ملفَّ Lean اختيارُه، وقراءةُ «جيناته الحسابية» الحسابَ الصنفيَّ قراءةُ البنّاء تنتظر إمضاءه.

يفحص، بعد `lake build`:
١. المولَّد: `Nizam/WahdatJadwal.lean` مخرجُ `scripts/bina_wahdat.py` بايتًا.
٢. **محلّلُ رؤوس Lean نفسُه** (`Lean.Elab.parseImports`) على كلّ ملفٍّ في المشروع: الملفّاتُ هي ملفّاتُ الجدول، وما يستورده كلٌّ من المشروع صفُّه فيه.
   فالجدولُ لا يقوم على قراءة بايثون للرؤوس وحدها.
٣. **الجيناتُ على بيئة Lean:** لكلّ وحدةٍ في الجدول تستوردها البيئةُ، الثوابتُ التي نوعُها `SLGE.Hisab` فيها هي أسماءُ `jinatKhassa` لها بعينها،
   والخاصُّ منها داخل.
وما في `Nizam/Wiratha.lean` من تدرّجٍ وترخيصٍ ووراثةٍ يقرّره البناء.

**حدُّه:** وحداتُ التنفيذ (`Faahis.Main` و`Qari.*`) يفحصها ٢ وحده، لأنّ لكلٍّ منها `main` فلا تُستورد معًا؛ و٣ على ما سواها.

**حدُّ المولِّد:** يقرأ الرؤوسَ سطرًا سطرًا، فلا يرى استيرادًا بعد تعليقٍ في سطره (`/- … -/ import X`)؛ ويكشفه ٢.

الطفرات: P1577 (المولِّد يُسقط «واحدًا فوق» من الدرجة) وP1578 (المولِّد يُسقط ملفّات `Qari`) لـ ١، وP1579 (استيرادٌ بعد تعليقٍ في سطره، لا يراه
المولِّد) لـ ٢، وP1580 (حسابٌ صنفيٌّ في ملفٍّ لا تسمّيه `jinatKhassa`) لـ ٣؛ وP1581–P1585 على `Nizam/Wiratha.lean` للبناء. وقاتلُ كلٍّ من سجلّ
تشغيلها في `hawkama/الوراثة_الصنفية.md`.
التشغيل (بعد lake build): python3 -I tahaqquq/test_wiratha.py
"""
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ["Nabt", "SLGE", "Dal", "Madlul", "Jisr", "Aql", "Nizam", "Faahis", "Qari"]
TANFIDH = ("Faahis.Main", "Qari.")  # وحداتُ التنفيذ: لكلٍّ `main`
HADAF = os.path.join(ROOT, "Nizam", "WahdatJadwal.lean")


def malaffat():
    """كلُّ ملفّ Lean في المشروع: (الوحدة، المسار النسبيّ)."""
    out = []
    for d in DIRS:
        for dp, _, fs in os.walk(os.path.join(ROOT, d)):
            for f in fs:
                if f.endswith(".lean"):
                    rel = os.path.relpath(os.path.join(dp, f), ROOT)
                    out.append((rel[:-5].replace(os.sep, "."), rel))
    if os.path.exists(os.path.join(ROOT, "Nabt.lean")):
        out.append(("Nabt", "Nabt.lean"))
    return sorted(out)


def jadwal_lean():
    """صفوفُ `wahdat` من نصّ المولَّد: [(الاسم، [الأرقام])]."""
    src = open(HADAF, encoding="utf-8").read()
    m = re.search(r"def wahdat : List \(String × List Nat\) := \[\n(.*?)\n\]", src, re.S)
    rows = []
    for line in m.group(1).splitlines():
        k = re.fullmatch(r'  \("([^"]+)", \[([0-9, ]*)\]\),?', line)
        rows.append((k.group(1), [int(x) for x in k.group(2).split(", ")] if k.group(2) else []))
    return rows


def fahs_muwallad(fails):
    r = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "scripts", "bina_wahdat.py"), "--stdout"],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0 or r.stdout != open(HADAF, encoding="utf-8").read():
        fails.append("١ Nizam/WahdatJadwal.lean ليس مخرجَ scripts/bina_wahdat.py بايتًا")


FAHS = r'''
open Lean Elab Command

def malaffat : List (String × String) := MALAFFAT

-- ٢: محلّلُ رؤوس Lean نفسُه على كلّ ملفّ.
#eval show IO Unit from do
  let asma := malaffat.map (·.1)
  for (m, p) in malaffat do
    let src ← IO.FS.readFile p
    let (imps, _, _) ← Lean.Elab.parseImports src (some p)
    let ps := (imps.toList.map (·.module.toString)).filter (asma.contains ·)
    IO.println s!"ISTIRAD {m} {",".intercalate (ps.mergeSort (· ≤ ·)).eraseDups}"

-- ٣: الحساباتُ الصنفيّة في كلّ وحدة على البيئة، وأسماءُ `jinatKhassa`.
#eval show CommandElabM Unit from do
  let env ← getEnv
  let mut bi : Std.HashMap String (Array String) := {}
  for (n, ci) in env.constants.toList do
    if n.isInternal && !isPrivateName n then continue
    if ci.type.getAppFn.isConstOf ``SLGE.Hisab then
      if let some idx := env.getModuleIdxFor? n then
        let mod := (env.header.moduleNames[idx.toNat]!).toString
        let ism := if isPrivateName n then (privateToUserName n).toString else n.toString
        bi := bi.insert mod ((bi.getD mod #[]).push ism)
  for (m, _) in Nizam.WahdatJadwal.wahdat do
    let b := ((bi.getD m #[]).toList.mergeSort (· ≤ ·))
    let j := (((Nizam.Wiratha.jinatKhassa m).map (·.1)).mergeSort (· ≤ ·))
    if env.header.moduleNames.contains m.toName then
      logInfo m!"JIN {m} {",".intercalate b} | {",".intercalate j}"
'''


def wahdat_mustawrada():
    """الوحداتُ التي يستوردها ملفُّ الفحص: ما في الجدول إلّا وحدات التنفيذ."""
    return [m for m, _ in malaffat() if not m.startswith(TANFIDH)]


def fahs_lean(fails):
    mf = malaffat()
    rows = jadwal_lean()
    asma = [n for n, _ in rows]
    if [m for m, _ in mf] != asma:
        fails.append(f"٢ الملفّاتُ غيرُ الجدول: زائدة {sorted(set(m for m, _ in mf) - set(asma))}، ناقصة {sorted(set(asma) - set(m for m, _ in mf))}")
        return 0
    lst = "[" + ", ".join(f'("{m}", "{os.path.join(ROOT, p)}")' for m, p in mf) + "]"
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "FahsWiratha.lean")
        with open(p, "w", encoding="utf-8") as f:
            f.write("".join(f"import {m}\n" for m in wahdat_mustawrada()) + "import Lean\n" + FAHS.replace("MALAFFAT", lst))
        r = subprocess.run(["lake", "env", "lean", p], cwd=ROOT, capture_output=True, text=True, timeout=3600)
    out = r.stdout + r.stderr
    if r.returncode != 0 or "error" in out:
        fails.append("فحصُ Lean لم يجرِ:\n" + out[-1500:])
        return 0
    lean_imp = {m: (x.split(",") if x else []) for m, x in re.findall(r"^ISTIRAD (\S+) ?(\S*)$", out, re.M)}
    for i, (m, imps) in enumerate(rows):
        jadwal = sorted(asma[j] for j in imps)
        if lean_imp.get(m) != jadwal:
            fails.append(f"٢ {m}: محلّلُ Lean {lean_imp.get(m)}، والجدول {jadwal}")
    jin = re.findall(r"JIN (\S+) (\S*) \| (\S*)", out)
    nm = 0
    for m, b, j in jin:
        nm += 1
        if b != j:
            fails.append(f"٣ {m}: الحساباتُ في البيئة [{b}]، وjinatKhassa [{j}]")
    if nm != len(wahdat_mustawrada()):
        fails.append(f"٣ الوحداتُ المفحوصة {nm}، والمستوردة {len(wahdat_mustawrada())}")
    return len(lean_imp)


def main():
    fails = []
    fahs_muwallad(fails)
    n = fahs_lean(fails)
    for f in fails:
        print("FAIL:", f)
    if fails:
        print(f"الوراثةُ الصنفيّة: فشل ({len(fails)})")
        sys.exit(1)
    rows = jadwal_lean()
    print(f"الوراثةُ الصنفيّة: {len(rows)} ملفًّا، و{sum(len(x) for _, x in rows)} استيرادًا = محلّلُ رؤوس Lean ({n} ملفًّا)، "
          f"والحساباتُ الصنفيّة في البيئة = jinatKhassa")


if __name__ == "__main__":
    main()
