"""يولّد `Nizam/WahdatJadwal.lean`: كلُّ وحدةٍ من حزمة lake في المشروع، وما تستورده منه، ودرجةُ اشتقاقه، وترتيبُ بنائه.

الملفّات: كلُّ `.lean` تحت `Nabt` و`SLGE` و`Dal` و`Madlul` و`Jisr` و`Aql` و`Nizam` و`Faahis` و`Qari`، و`Nabt.lean` (وهي وحداتُ حزمة lake في
`lakefile.toml`؛ يفحصه `tahaqquq/test_wiratha.py` ٢). والاستيرادُ أسطرُ `import X` في رأس الملفّ: يتخطّى الفارغَ وما أوّلُه `--` أو `/-` (ويُسقط معه ما بعده في سطره، ومنه `/- … -/ import X`)،
ويأخذ `import X` بكلمةٍ واحدةٍ بعدها (فـ`import A--c` اسمُه `A--c`، ليس في المشروع)، ويقف عند أوّل سطرٍ سواه (ومنه `import A -- c`
و`public import A`)؛
ويُعدّ منه ما كان ملفًّا في المشروع وحده. ودرجةُ الاشتقاق 0 لما لا يستورد من
المشروع شيئًا، وإلّا واحدٌ فوق أعلى ما يستورده. وترتيبُ البناء بالدرجة ثمّ بالرقم.

التشغيل: python3 -I scripts/bina_wahdat.py           (يكتب Nizam/WahdatJadwal.lean)
         python3 -I scripts/bina_wahdat.py --stdout  (يطبعه ولا يكتب؛ يستعمله tahaqquq/test_wiratha.py)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ["Nabt", "SLGE", "Dal", "Madlul", "Jisr", "Aql", "Nizam", "Faahis", "Qari"]
HADAF = os.path.join(ROOT, "Nizam", "WahdatJadwal.lean")


def malaffat():
    out = {}
    for d in DIRS:
        for dp, _, fs in os.walk(os.path.join(ROOT, d)):
            for f in fs:
                if f.endswith(".lean"):
                    p = os.path.join(dp, f)
                    out[os.path.relpath(p, ROOT)[:-5].replace(os.sep, ".")] = p
    p = os.path.join(ROOT, "Nabt.lean")
    if os.path.exists(p):
        out["Nabt"] = p
    return out


def istirad(path):
    """أسطرُ `import` في رأس الملفّ وحده."""
    out, kutla = [], 0
    for line in open(path, encoding="utf-8"):
        s = line.strip()
        if kutla:
            kutla += s.count("/-") - s.count("-/")
            continue
        if s.startswith("/-"):
            kutla = s.count("/-") - s.count("-/")
            continue
        if not s or s.startswith("--"):
            continue
        m = re.fullmatch(r"import\s+(\S+)", s)
        if not m:
            break
        out.append(m.group(1))
    return out


def jadwal():
    mf = malaffat()
    asma = sorted(mf)
    raqm = {m: i for i, m in enumerate(asma)}
    imp = [sorted(raqm[x] for x in set(istirad(mf[m])) if x in raqm) for m in asma]
    rutba = [None] * len(asma)

    def r(i, khat=()):
        if rutba[i] is None:
            if i in khat:
                raise SystemExit(f"دورٌ في الاستيراد عند {asma[i]}")
            rutba[i] = 0 if not imp[i] else 1 + max(r(j, khat + (i,)) for j in imp[i])
        return rutba[i]

    for i in range(len(asma)):
        r(i)
    tartib = sorted(range(len(asma)), key=lambda i: (rutba[i], i))
    return asma, imp, rutba, tartib


def nass():
    asma, imp, rutba, tartib = jadwal()
    L = ["/-",
         "  Nizam/WahdatJadwal.lean — مولَّدٌ من رؤوس وحدات حزمة lake في المشروع بـ `python3 -I scripts/bina_wahdat.py`؛ لا يُحرَّر يدويًّا.",
         "  يطابقه `tahaqquq/test_wiratha.py` بايتًا، ويطابق استيرادَه محلّلُ رؤوس Lean نفسُه. وقاعدتُه وترخيصُه في `Nizam/Wiratha.lean`.",
         f"  {len(asma)} ملفًّا، و{sum(len(x) for x in imp)} استيرادًا بينها، ودرجاتُ الاشتقاق من 0 إلى {max(rutba)}.",
         "-/",
         "",
         "namespace Nizam",
         "namespace WahdatJadwal",
         "",
         "/-- كلُّ ملفّ: اسمُ وحدته، وأرقامُ ما يستورده من المشروع؛ مرتّبةٌ بالاسم، والرقمُ موضعُ الوحدة في القائمة. -/",
         "def wahdat : List (String × List Nat) := ["]
    for i, m in enumerate(asma):
        L.append(f"  (\"{m}\", [{', '.join(map(str, imp[i]))}]){',' if i + 1 < len(asma) else ''}")
    L += ["]", "",
          "/-- درجةُ الاشتقاق لكلّ ملفّ بموضعه: 0 لما لا يستورد من المشروع شيئًا، وإلّا واحدٌ فوق أعلى ما يستورده. -/",
          f"def rutbaJadwal : List Nat := [{', '.join(map(str, rutba))}]", "",
          "/-- ترتيبُ البناء: بالدرجة ثمّ بالرقم. -/",
          f"def tartib : List Nat := [{', '.join(map(str, tartib))}]", "",
          "end WahdatJadwal",
          "end Nizam", ""]
    return "\n".join(L)


if __name__ == "__main__":
    t = nass()
    if "--stdout" in sys.argv:
        sys.stdout.write(t)
    else:
        open(HADAF, "w", encoding="utf-8").write(t)
        print(HADAF)
