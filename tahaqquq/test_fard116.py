"""اختبارُ فرضيّة الـ116: `shabaka/fard116.py` و`Madlul/Fard116.lean` و`Madlul/Fard116Data.lean` و`Madlul/Fard116Shawahid.lean`.

١. نصُّ Lean (دائمًا): المبرهناتُ بأسمائها في الملفّين وفي Audit.lean.
٢. المرآةُ على مبرهنات المالك (دائمًا، بلا مودَع): عددُ ما ترخّصه مرآةُ الآلة في بايثون بطول 3 و4 و5 = ما في `SLGE/Root.lean`
   (`root3`، `root4`، `root5`) مقروءًا من نصّه — توقّعٌ مستقلٌّ عن الكود.
٣. حالاتٌ مكتوبةٌ يدويًّا من نصّ القانون (لا من المخرج): كتب، علم، قلق، مدد مرخَّصة؛ شجر (ج–ش)، أهل (ء–ه)، بمم (ب–م)، حعل (ع–ح)، سزز (ز–س)
   ممتنعة؛ «بغا» (الألفُ آخرًا حرفُ علّة) مرخَّصة؛ وفي التولّد: «زلزل» ثنائيٌّ مكرَّر، و«دحرج» مع {دحر} G1 لا G2، و«بحتر» مع {بتر، حتر} G2،
   و«مددت»-نحوه: إسقاطا الدالين يعطيان ثلاثيًّا واحدًا فليس G2.
٤. المودَعان (إن حضرا ببصمتيهما): يُعاد المخرجُ كلُّه في مجلّدٍ مؤقّت فيطابق `shabaka/out/fard116.json` وملفَّي Lean المولَّدين بالبايت،
   ونصوصُ القيود في أسطرها.
التشغيل: python3 -I tahaqquq/test_fard116.py
"""
import filecmp
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "shabaka"))
import fard116 as F  # noqa: E402
import jadwal_luzum as J  # noqa: E402

import numpy as np  # noqa: E402

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


# ---------- ١. نصّ Lean ----------
src = open(os.path.join(ROOT, "Madlul", "Fard116.lean"), encoding="utf-8").read()
shw = open(os.path.join(ROOT, "Madlul", "Fard116Shawahid.lean"), encoding="utf-8").read()
audit = open(os.path.join(ROOT, "Audit.lean"), encoding="utf-8").read()
for t in ("licB_iff", "runL_imtina", "runL_qabul", "licB_iff_spaced", "illa_la_tajawur", "tajB_eq", "spacedB_iff", "licF_eq",
          "illa_sawa", "licN3_eq", "harf3_arqam", "maanN3_eq", "azwajQanun_kulluha", "tamathul_mujaz", "jumhur_atwal",
          "kharita3", "kharita4", "ramz_arqam3"):
    check(f"theorem {t} " in src or f"theorem {t}\n" in src, f"المبرهنة {t} غائبة عن Fard116.lean")
    check(f"#print axioms Madlul.Fard116.{t}\n" in audit, f"المبرهنة {t} غير مدقّقة في Audit.lean")
shw_t = re.findall(r"^theorem (\w+)", shw, re.M)
check(len(shw_t) == 50, f"مبرهنات الشاهد {len(shw_t)} لا 50 (4 مخالِف، 14 زوجًا، 15 خارج القانون، 3 تماثل، 10 قيود، 4 تولّد)")
for t in shw_t:
    check(f"#print axioms Madlul.Fard116.Shawahid.{t}\n" in audit, f"المبرهنة {t} غير مدقّقة في Audit.lean")
check("sorry" not in src and "sorry" not in shw and "native_decide" not in src + shw, "sorry أو native_decide في Fard116")

# ---------- ٢. المرآةُ على مبرهنات المالك ----------
root = open(os.path.join(ROOT, "SLGE", "Root.lean"), encoding="utf-8").read()
for k in (3, 4, 5):
    m = re.search(rf"theorem root{k} : Mroot\.lev 3 0 {k} = (\d+)", root)
    check(m and F.adad_murakhkhas(k) == int(m.group(1)), f"مرآة الآلة بطول {k}: {F.adad_murakhkhas(k)} لا ما في root{k}")
import itertools  # noqa: E402
check(sum(F.murakhkhas(r) for r in itertools.product(range(29), repeat=3)) == 20430, "المرآة بالعدّ المباشر للثلاثيّ ليست 20430")

# ---------- ٣. حالاتٌ يدويّة ----------
HAL = {"كتب": True, "علم": True, "قلق": True, "مدد": True, "بغا": True, "شجر": False, "ءهل": False, "بمم": False,
       "حعل": False, "سزز": False, "دتر": False, "ظذف": False}
for w, exp in HAL.items():
    check(F.murakhkhas(F.ramz(w)) == exp, f"حكم الآلة على «{w}» ليس {exp}")
check(F.murakhkhas([2, 13, 27]) is False, "الألفُ أصلًا مرخَّصة")


def tw(quads, tris, k=4):
    A = np.array([F.ramz(q) for q in quads], dtype=np.int64)
    T = np.array([F.rmz(t) for t in tris], dtype=np.int64)
    g1, g2, gr = F.tawlid(A, T, k)
    return [bool(x) for x in g1], [bool(x) for x in g2], [bool(x) for x in gr]


g1, g2, gr = tw(["زلزل", "دحرج", "بحتر", "مددك"], ["زلز", "دحر", "بتر", "حتر", "مدك"])
check(gr == [True, False, False, False], f"التكرار abab: {gr}")
check(g1 == [True, True, True, True], f"G1: {g1}")
check(g2 == [False, False, True, False], f"G2 (مددك: الإسقاطان يعطيان «مدك» نفسه): {g2}")

# ---------- ٤. المودَعان ----------
D = os.environ.get("MUDAA_DIR")
hadir = bool(D) and all(os.path.isfile(os.path.join(D, f)) for f in ("lisan.txt", "maqayis.txt"))
if hadir:
    S = J.sijill()
    hadir = all(J.basma(os.path.join(D, f)) == S[f]["sha256"] for f in ("lisan.txt", "maqayis.txt"))
if hadir:
    with tempfile.TemporaryDirectory() as tmp:
        js = os.path.join(tmp, "fard116.json")
        r = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "shabaka", "fard116.py"), "--lean", "--lean-dir", tmp,
                            "--json", js], capture_output=True, text=True, env=dict(os.environ))
        check(r.returncode == 0, "fard116.py فشل: " + r.stderr[-400:])
        if r.returncode == 0:
            check(filecmp.cmp(js, os.path.join(ROOT, "shabaka", "out", "fard116.json"), shallow=False),
                  "shabaka/out/fard116.json لا يطابق إعادة البناء")
            for f in ("Fard116Data.lean", "Fard116Shawahid.lean"):
                check(filecmp.cmp(os.path.join(tmp, f), os.path.join(ROOT, "Madlul", f), shallow=False),
                      f"Madlul/{f} لا يطابق المولِّد")
    hal = "المودَعان حاضران"
else:
    hal = "المودَعان غائبان: فحوص النصّ والمرآة والحالات وحدها"

if fails:
    print("\n".join(fails))
    sys.exit(1)
print(f"فرضية الـ116: مرّ ({hal}؛ المرآة 20430/552078/14918778؛ الحالات {len(HAL)}؛ مبرهنات الشاهد {len(shw_t)})")
