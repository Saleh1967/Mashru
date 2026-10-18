"""اختبارُ أطلس الجسور `Nizam/atlas.tsv` (م0 في `hawkama/البروتوكول.md`).

١. التمام: كلُّ وحدة Lean في المجلّدات (SLGE، Dal، Madlul، Jisr، Aql، Nizam، Faahis، Qari) صفٌّ واحدٌ في الأطلس، ولا صفَّ لوحدةٍ غير موجودة.
   فلا تُضاف وحدةٌ إلّا مسجَّلةً بطبقتها (البروتوكول §٥).
٢. الطبقةُ من القائمة المعلنة: T0…T11، أو ADAT (أداة)، أو NIZAM (النواة).
٣. عمودُ «في المحرّك» لقطةٌ معلنة، تُقارَن بحسابٍ مستقلٍّ من رسم الاستيراد (ما يصل إليه Qari.Main أو Faahis.Main):
   كلُّ وصلٍ جديدٍ بالمحرّك أو انقطاعٍ عنه يُفشل الاختبار حتّى يُحدَّث الأطلس عمدًا — فالربطُ لا يجري صامتًا.
٤. يطبع العدّ لكلّ طبقة: كم وحدةً فيها، وكم منها في المحرّك (مقيسٌ من المستودع نفسه).
التشغيل: python3 -I tahaqquq/test_atlas.py
"""
import collections
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ("SLGE", "Dal", "Madlul", "Jisr", "Aql", "Nizam", "Faahis", "Qari")
TABAQAT = {f"T{i}" for i in range(12)} | {"ADAT", "NIZAM"}
JUDHUR = ("Qari.Main", "Faahis.Main")


def wahdat():
    out = {}
    for d in DIRS:
        p = os.path.join(ROOT, d)
        if not os.path.isdir(p):
            continue
        for f in sorted(os.listdir(p)):
            if f.endswith(".lean"):
                src = open(os.path.join(p, f), encoding="utf-8").read()
                out[d + "." + f[:-5]] = re.findall(r"^import\s+([\w.]+)", src, flags=re.M)
    return out


def wusul(I):
    seen, st = set(), list(JUDHUR)
    while st:
        m = st.pop()
        if m in seen or m not in I:
            continue
        seen.add(m)
        st += I[m]
    return seen


def main():
    fails = []
    I = wahdat()
    rows = [l.split("\t") for l in open(os.path.join(ROOT, "Nizam", "atlas.tsv"), encoding="utf-8").read().split("\n")[1:] if l.strip()]
    names = [r[0] for r in rows]
    dup = [n for n, c in collections.Counter(names).items() if c > 1]
    if dup:
        fails.append(f"صفوفٌ مكرّرة: {dup}")
    naqis = sorted(set(I) - set(names))
    zaid = sorted(set(names) - set(I))
    if naqis:
        fails.append(f"وحداتٌ غير مسجَّلة في الأطلس: {naqis}")
    if zaid:
        fails.append(f"صفوفٌ لوحداتٍ غير موجودة: {zaid}")
    E = wusul(I)
    for r in rows:
        if len(r) != 4:
            fails.append(f"صفٌّ ناقص الأعمدة: {r}")
            continue
        m, t, f, _ = r
        if t not in TABAQAT:
            fails.append(f"طبقةٌ غير معلنة: {m} {t}")
        if f not in ("نعم", "لا"):
            fails.append(f"قيمةٌ غير معلنة في «في المحرّك»: {m} {f}")
        elif m in I and (f == "نعم") != (m in E):
            fails.append(f"تغيّر وصلُ {m} بالمحرّك (الأطلس: {f}، الحساب: {'نعم' if m in E else 'لا'}) — حدِّث الأطلس عمدًا")
    c = collections.Counter((r[1], r[2]) for r in rows if len(r) == 4)
    tab = sorted({r[1] for r in rows if len(r) == 4}, key=lambda t: (len(t), t))
    print("الطبقة: الوحدات / في المحرّك — " + "، ".join(f"{t}: {c[(t, 'نعم')] + c[(t, 'لا')]}/{c[(t, 'نعم')]}" for t in tab))
    if fails:
        print("\n".join(fails))
        print(f"الأطلس: {len(fails)} خلل")
        sys.exit(1)
    print(f"الأطلس: مرّ ({len(rows)} وحدة، في المحرّك {len(E & set(names))})")


if __name__ == "__main__":
    main()
