"""البند أ (همزة الوصل مع لامٍ مشدَّدة، التعديل الرابع): حالاتُ الموصولات المجمَّدة على `silsila`.

يفحص، بلا مودَع: المقطعُ الأوّل من 23 حالةً مجمَّدةً (مؤلّفٌ مستقلّ، `dawabit/al_lam_mushaddada/mawsul.json`،
بصمتُها في `tajmid_mawsul.json`) هو ما يتوقّعه تقسيمُ المؤلّف:
- `awwal_rule == hamzaWaslAl` ⇒ صنفُ المقطع الأوّل `hamzaWaslAl` وحكمُه «مرخص» (الموصولات، أل الشمسية والقمرية).
- `awwal_rule == harfHaraka` ⇒ صنفُه `harfHaraka` ومرخص (المشتّتات بهمزةٍ مقطوعة: أَلَّا، إِلَّا، أَحْمَد…).
- `hukm == معلق` ⇒ حكمُ المقطع «معلق» (الَّ وحدها: D7 بحالها).
- `hukm == مدخل_فاسد` ⇒ «مدخل_فاسد» (اَلْوَلَد: ألفٌ محرّكة).
والبصمةُ تُفحص فلا تتغيّر الحالاتُ صامتًا.

الطفرة: P1447 (حذفُ فرع التعديل الرابع من `lamBaad`) يقتلها هذا الاختبار (الموصولاتُ المفردة تعود «معلق»).
التشغيل: python3 -I tahaqquq/test_al_lam.py
"""
import hashlib
import json
import os
import subprocess
import sys

H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DW = os.path.join(H, "tahaqquq", "dawabit", "al_lam_mushaddada")
SIL = os.path.join(H, ".lake", "build", "bin", "silsila")
fails = 0


def tahaqqaq(cond, msg):
    global fails
    if not cond:
        fails += 1
        print("خلل:", msg)


halat = json.load(open(os.path.join(DW, "mawsul.json"), encoding="utf-8"))["halat"]
tajmid = json.load(open(os.path.join(DW, "tajmid_mawsul.json"), encoding="utf-8"))
sha = hashlib.sha256(open(os.path.join(DW, "mawsul.json"), "rb").read()).hexdigest()
tahaqqaq(sha == tajmid["mawsul.json"], "بصمةُ mawsul.json تغيّرت عن المجمَّد")

inp = "\n".join(f"{c['id']}\t{c['surface']}" for c in halat) + "\n"
tmp = os.path.join(H, "tahaqquq", "_al_lam_tmp.tsv")
open(tmp, "w", encoding="utf-8").write(inp)
out = subprocess.run([SIL, tmp], capture_output=True, text=True).stdout
os.remove(tmp)

first = {}
for ln in out.splitlines():
    f = ln.split("\t")
    if len(f) >= 7 and f[1] == "MAQTA" and f[2].endswith(".1"):
        first[f[0]] = (f[5].replace("Dal.Tahsil.", ""), f[6])

ok = 0
for c in halat:
    r, v = first.get(c["id"], ("?", "?"))
    exp_rule, exp_h = c["awwal_rule"], c["hukm"]
    if exp_h == "مرخص" and exp_rule == "hamzaWaslAl":
        good = r == "hamzaWaslAl" and v.startswith("مرخص")
    elif exp_h == "مرخص" and exp_rule == "harfHaraka":
        good = r == "harfHaraka" and v.startswith("مرخص")
    elif exp_h == "معلق":
        good = "معلق" in v
    elif exp_h == "مدخل_فاسد":
        good = v.startswith("مدخل_فاسد")
    else:
        good = False
    if good:
        ok += 1
    else:
        tahaqqaq(False, f"{c['id']} «{c['surface']}»: متوقَّع {exp_rule}/{exp_h}، وجاء {r}/{v}")

print(f"البند أ (الموصولات): {ok}/{len(halat)} — {'نجح' if fails == 0 else 'فشل ' + str(fails)}")
sys.exit(1 if fails else 0)
