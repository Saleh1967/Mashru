"""الحسابُ الصنفيّ: أعدادُ آلات `SLGE.Machine` في المشروع تُحسب بالأصناف (البوّابة ٥خ٢؛ `hawkama/الحساب_الصنفي.md`).

قولُ المالك في الجلسة (2026-11-01، لفظُه ووقتُه 17:56 من ملخّص الجلسة بعد ضغطها؛ وصدرُ رسالته جملةُ البنّاء ألصقها):
«جيد موافق لكن يجب ان تجعل كل المشروع لا يعمل الا وفق هذا الحساب وان تجهز لعمل تكامل بن كل المبرهنات والاختبارات وفق حساب الجديد واعطيه منهج الحساب اسما والأهم تعمل توثيق»
وقراءةُ «كل المشروع» أنّها كلُّ عددٍ لما ترخّصه آلة (`SLGE.Machine`) قراءةُ البنّاء تنتظر إمضاءه.

يفحص، بعد `lake build`:
١. **على بيئة Lean نفسِها** (ملفٌّ مؤقّت يستورد وحدات المشروع ويقرأ ثوابتها، والخاصُّ منها داخل): (أ) لا يعود الجدولُ المحذوف بأسمائه الثلاثة
   (`SLGE.Machine.tab`، `tab_eq`، `row`)؛ (ب) لكلّ تعريفٍ نوعُه `SLGE.Machine` حسابٌ صنفيّ (ثابتٌ نوعُه `SLGE.Hisab <الآلة> q0`)، والآلاتُ هي السجلّ
   `ALAT` بعينه، والحسابُ المسجَّل من الحالة 0؛
   (ج) كلُّ مبرهنةٍ في قضيّتها تطبيقٌ تامٌّ لـ `Machine.lev` أو `Machine.C` على آلةٍ مغلقةٍ وأعدادٍ حرفيّة يبلغ برهانُها — في ثوابت المشروع —
   `SLGE.Hisab.lev_eq` أو `SLGE.Hisab.C_eq`، وفيها أعدادُ المالك كلُّها (`MUBARHANAT_AL_MALIK`).
٢. **على مرآة بايثون** (`tahaqquq/hisab_sinfi.py`): كلُّ عددٍ في قضايا المالك (`<آلة>.lev 3 0 <درجة> = <عدد>` في SLGE/Root.lean وLaw.lean
   وSyllable.lean) يساوي الاستنفادَ على المرآة، ويساوي العدَّ على صفوف الأصناف المقروءة من نصّ Lean. فالتوقّعُ نصُّ المالك، والمرآةُ منقولةٌ باليد
   من تعريفات Lean لا مولَّدةٌ منها، والصفوفُ نصُّ Lean. والصفوفُ وأعدادُ المالك يبرهنها Lean، فما يكشفه ٢ وحده فسادُ المرآة.

الطفرات: P1567 (أوائلُ الجذر `wilada_awwal` بـ decide لا بالحساب)، وP1568 (آلةٌ بلا حساب في `Dal/WiladaJumla.lean`)، وP1569 (على المرآة نفسِها:
تُسقط حرفًا من الزوائد)، وP1576 (الجدولُ المحذوف يعود باسمه `SLGE.Machine.row`). وقاتلُ كلٍّ من سجلّ تشغيلها في `hawkama/الحساب_الصنفي.md` §٤.
التشغيل (بعد lake build): python3 -I tahaqquq/test_hisab.py
"""
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tahaqquq"))
import hisab_sinfi as H  # noqa: E402

# سجلُّ الآلات: كلُّ تعريفٍ نوعُه SLGE.Machine في المشروع، ولكلٍّ حسابُه الصنفيّ.
ALAT = {
    "SLGE.Law.Mroot": "SLGE.Law.HisabJadhr.hisabJadhr",
    "SLGE.Law.Maug": "SLGE.Law.HisabZaid.hisabZaid",
    "SLGE.Law.Mword": "SLGE.Law.HisabKalima.hisabWaqf",
    "SLGE.Law.MwordWasl": "SLGE.Law.HisabKalima.hisabWasl",
    "SLGE.Law.Msent": "SLGE.Law.HisabJumla.hisabJumla",
    "SLGE.Law.Msyl": "SLGE.Law.HisabMaqta.hisabWaqf",
    "SLGE.Law.MsylWasl": "SLGE.Law.HisabMaqta.hisabWasl",
}

# أعدادُ المالك: يجب أن تكون بين ما يفحصه ١ج وأن تبلغ القانون.
MUBARHANAT_AL_MALIK = [
    "SLGE.Law.root3", "SLGE.Law.root4", "SLGE.Law.root5", "SLGE.Law.units1", "SLGE.Law.units2",
    "SLGE.Law.word_levels", "SLGE.Law.word_levels_wasl", "SLGE.Law.sent_levels",
    "SLGE.Law.sl0", "SLGE.Law.sl1", "SLGE.Law.sl2", "SLGE.Law.sl3", "SLGE.Law.slw1", "SLGE.Law.slw2", "SLGE.Law.slw3",
    "SLGE.Law.syl_levels",
]

DIRS = ("SLGE", "Dal", "Madlul", "Jisr", "Aql", "Nizam")

FAHS = r'''
open Lean Elab Command

namespace FahsHisab

def harfi? : Expr → Option Nat
  | .lit (.natVal n) => some n
  | .app (.app (.app (.const ``OfNat.ofNat _) _) (.lit (.natVal n))) _ => some n
  | .mdata _ e => harfi? e
  | _ => none

def adadHarfi (e : Expr) : Bool :=
  let f := e.getAppFn
  let as := e.getAppArgs
  (f.isConstOf ``SLGE.Machine.lev || f.isConstOf ``SLGE.Machine.C) && as.size == 4 &&
    !as[0]!.hasLooseBVars && !as[0]!.hasFVar && !as[0]!.hasMVar &&
    (as.toList.drop 1).all fun a => (harfi? a).isSome

def mashru (env : Environment) (n : Name) : Bool :=
  match env.getModuleIdxFor? n with
  | some i =>
    let r := (env.header.moduleNames[i.toNat]!).getRoot
    !(r == `Init || r == `Lean || r == `Std || r == `Lake)
  | none => true

def qima? : ConstantInfo → Option Expr
  | .thmInfo v => some v.value
  | .defnInfo v => some v.value
  | .opaqueInfo v => some v.value
  | _ => none

/-- يبلغ برهانُ الثابت (في ثوابت المشروع) إحدى المرساتين؟ والحالةُ: ما ثبت أنّه يبلغ، وما زير. -/
partial def yablugh (env : Environment) (anchors : NameSet) (n : Name) : StateM (NameSet × NameSet) Bool := do
  if anchors.contains n then return true
  let (naam, zira) ← get
  if naam.contains n then return true
  if zira.contains n then return false
  modify fun (a, b) => (a, b.insert n)
  let r ← match env.find? n with
    | some ci =>
      if !mashru env n then pure false else
      match qima? ci with
      | some v => v.getUsedConstants.anyM fun c => yablugh env anchors c
      | none => pure false
    | none => pure false
  if r then modify fun (a, b) => (a.insert n, b)
  return r

def fahs : CommandElabM Unit := do
  let env ← getEnv
  let anchors : NameSet := NameSet.empty |>.insert ``SLGE.Hisab.lev_eq |>.insert ``SLGE.Hisab.C_eq
  for n in [`SLGE.Machine.tab, `SLGE.Machine.tab_eq, `SLGE.Machine.row] do
    if env.contains n then logInfo m!"JADWAL {n}"
  let mut machines : Array Name := #[]
  let mut hisabs : Array (Name × Name) := #[]
  let mut counts : Array Name := #[]
  for (n, ci) in env.constants.toList do
    -- الخاصُّ (`private`) داخلٌ في الفحص؛ وما سواه من الأسماء الداخليّة (مساعداتُ المترجم) خارجه.
    if !mashru env n || (n.isInternal && !isPrivateName n) then continue
    let ty := ci.type
    if ty.isConstOf ``SLGE.Machine then
      if let .defnInfo _ := ci then machines := machines.push n
    if ty.getAppFn.isConstOf ``SLGE.Hisab && ty.getAppNumArgs == 2 then
      if let some m := ty.getAppArgs[0]!.constName? then
        hisabs := hisabs.push (m, n)
        logInfo m!"BIDAYA {n} {(harfi? ty.getAppArgs[1]!).getD 999999}"
    if let .thmInfo _ := ci then
      if (ty.find? adadHarfi).isSome then counts := counts.push n
  for m in machines do
    let hs := (hisabs.filter (·.1 == m)).map (·.2)
    logInfo m!"ALA {m} {hs.toList}"
  let mut st : NameSet × NameSet := ({}, {})
  for t in counts do
    let (ok, st') := (yablugh env anchors t).run st
    st := st'
    logInfo m!"ADAD {t} {if ok then "QANUN" else "BILA_QANUN"}"

end FahsHisab

#eval FahsHisab.fahs
'''


def wahdat():
    out = set()
    for d in DIRS:
        for dirpath, _, files in os.walk(os.path.join(ROOT, d)):
            for f in files:
                if f.endswith(".lean"):
                    rel = os.path.relpath(os.path.join(dirpath, f), ROOT)
                    out.add(rel[:-5].replace(os.sep, "."))
    for line in open(os.path.join(ROOT, "Audit.lean"), encoding="utf-8"):
        m = re.match(r"import (\S+)", line)
        if m:
            out.add(m.group(1))
    return sorted(out)


def fahs_lean(fails):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "FahsHisab.lean")
        with open(p, "w", encoding="utf-8") as f:
            f.write("".join(f"import {m}\n" for m in wahdat()) + "import Lean\n" + FAHS)
        r = subprocess.run(["lake", "env", "lean", p], cwd=ROOT, capture_output=True, text=True, timeout=3600)
    out = r.stdout + r.stderr
    if r.returncode != 0 or "error" in out:
        fails.append("فحصُ Lean لم يجرِ:\n" + out[-1500:])
        return 0, 0
    jadwal = re.findall(r"JADWAL (\S+)", out)
    for n in jadwal:
        fails.append(f"١أ عاد الجدولُ المحذوف: {n}")
    alat = {}
    for m in re.finditer(r"ALA (\S+) \[([^\]]*)\]", out):
        alat[m.group(1)] = [x.strip() for x in m.group(2).split(",") if x.strip()]
    for a, hs in sorted(alat.items()):
        if not hs:
            fails.append(f"١ب آلةٌ بلا حسابٍ صنفيّ: {a}")
    if set(alat) != set(ALAT):
        fails.append(f"١ب الآلاتُ في المشروع غيرُ السجلّ: زائدة {sorted(set(alat) - set(ALAT))}، ناقصة {sorted(set(ALAT) - set(alat))}")
    for a, h in ALAT.items():
        if a in alat and h not in alat[a]:
            fails.append(f"١ب حسابُ {a} المسجَّل {h} ليس بين حساباتها {alat[a]}")
    # الحسابُ المسجَّل من حالة الابتداء 0، وهي حالةُ أعداد المالك (`lev 3 0 j`).
    bidaya = dict(re.findall(r"BIDAYA (\S+) (\d+)", out))
    for a, h in ALAT.items():
        if bidaya.get(h) != "0":
            fails.append(f"١ب حسابُ {a} المسجَّل {h} ليس من الحالة 0 ({bidaya.get(h)})")
    adad = dict(re.findall(r"ADAD (\S+) (QANUN|BILA_QANUN)", out))
    for t, v in sorted(adad.items()):
        if v != "QANUN":
            fails.append(f"١ج عددٌ لا يمرّ بالحساب الصنفيّ: {t}")
    for t in MUBARHANAT_AL_MALIK:
        if adad.get(t) != "QANUN":
            fails.append(f"١ج عددُ المالك {t} ليس بين ما يمرّ بالحساب ({adad.get(t)})")
    return len(alat), len(adad)


def fahs_mirat(fails):
    aadad = H.aadad_al_malik()
    if len(aadad) < 23:
        fails.append(f"٢ أعدادُ المالك المقروءة {len(aadad)} أقلُّ من 23")
    for (ala, j, n) in aadad:
        d = H.lev_istinfad(ala, 3, j)
        s = H.lev_bil_sufuf(ala, 3, j)
        if not (n == d == s):
            fails.append(f"٢ {ala}.lev 3 0 {j}: المالك {n}، الاستنفادُ على المرآة {d}، الصفوف {s}")
    return len(aadad)


def main():
    fails = []
    n_alat, n_adad = fahs_lean(fails)
    n_mirat = fahs_mirat(fails)
    for f in fails:
        print("FAIL:", f)
    if fails:
        print(f"الحسابُ الصنفيّ: فشل ({len(fails)})")
        sys.exit(1)
    print(f"الحسابُ الصنفيّ: {n_alat} آلاتٍ لكلٍّ حسابٌ صنفيّ، و{n_adad} مبرهنةَ عددٍ كلُّها تمرّ بـ Hisab.lev_eq، "
          f"و{n_mirat} عددًا للمالك = الاستنفادُ على المرآة = صفوفُ الأصناف")


if __name__ == "__main__":
    main()
