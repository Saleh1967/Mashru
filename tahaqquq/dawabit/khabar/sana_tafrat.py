# -*- coding: utf-8 -*-
"""يصنع نسخًا معيبةً من cases.json في tafrat_fahs/ ويشغّل الفاحص على كلٍّ منها.
الاستعمال: python3 -I sana_tafrat.py <مجلّد mujallad> <مجلّد المصدرين>
"""
import copy
import json
import os
import shutil
import subprocess
import sys

M = sys.argv[1]
SRC = sys.argv[2]
T = os.path.join(M, "tafrat_fahs")
os.makedirs(T, exist_ok=True)
base = json.load(open(os.path.join(M, "cases.json"), encoding="utf-8"))
byid = lambda d, k: next(c for c in d if c["id"] == k)  # noqa


def save(name, d, raw=None):
    p = os.path.join(T, name + ".json")
    with open(p, "w", encoding="utf-8") as f:
        if raw is not None:
            f.write(raw)
        else:
            json.dump(d, f, ensure_ascii=False, indent=1)
    return p


V = []


def var(name, fn):
    d = copy.deepcopy(base)
    fn(d)
    V.append((name, save(name, d), SRC))


V.append(("01_json_fasid", save("01_json_fasid", None, raw=json.dumps(base, ensure_ascii=False)[:-5]), SRC))
var("02_nass_mughayyar", lambda d: byid(d, "K01")["sanad"][0].update(nass=byid(d, "K01")["sanad"][0]["nass"].replace("قائم", "قاعد")))
var("03_dakhil_mukarrar", lambda d: byid(d, "K10").update(dakhil=copy.deepcopy(byid(d, "K02")["dakhil"])))
var("04_zawj_ghayr_mutabadil", lambda d: byid(d, "K01").update(zawj="K03"))
var("05_la_yantabiq_fi_muntabiq", lambda d: byid(d, "K01")["dakhil"].update(rabit="لا_ينطبق"))
var("06_qima_fi_ghayr_muntabiq", lambda d: byid(d, "K14")["dakhil"].update(rabit="ضمير"))
var("07_satr_kharij_nitaq", lambda d: byid(d, "K14")["sanad"][0].update(satr=163, nass="الخبر"))
var("08_qatr162_baad_hadd", lambda d: byid(d, "K40")["sanad"].append({"masdar": "قطر", "satr": 162, "nass": "وقد يتعدد"}))
var("09_la_hukm_bisanad", lambda d: byid(d, "K35")["sanad"].append(copy.deepcopy(byid(d, "K31")["sanad"][1])))
var("10_harfi_kadhib", lambda d: byid(d, "K02").update(mithal_harfi=True))
var("11_daraja_maa_khata", lambda d: byid(d, "K02").update(daraja="قليل"))
var("12_kharij_naqis", lambda d: d.__setitem__(slice(None), [c for c in d if c["fia"] != "خارج"]))
def _two(d):
    byid(d, "K02")["zawj"] = None
    byid(d, "K09")["zawj"] = None
    byid(d, "K01")["zawj"] = "K10"
    byid(d, "K10")["zawj"] = "K01"
var("13_zawj_hiqlan", _two)
def _same(d):
    byid(d, "K14")["zawj"] = "K15"
    byid(d, "K15")["zawj"] = "K14"
var("14_zawj_hukm_sawa", _same)
var("15_ghumud_bila_qaima", lambda d: byid(d, "K47").update(hukm="مقبول"))
var("16_qaima_fi_ghayr_ghumud", lambda d: byid(d, "K01").update(hukm=["مقبول", "خطأ"]))
var("17_id_mukarrar", lambda d: byid(d, "K57").update(id="K56"))
var("18_mithal_mashkul", lambda d: byid(d, "K02").update(mithal="زيدٌ عمرو قائم"))
var("19_fia_hukm", lambda d: byid(d, "K14").update(fia="حد"))
var("20_mawjib_naqis", lambda d: d.__setitem__(slice(None), [c for c in d if c["fia"] != "موجب"]))

# بصمة مصدرٍ معيبة
bad = os.path.join(T, "masadir_fasida")
os.makedirs(bad, exist_ok=True)
shutil.copyfile(os.path.join(SRC, "alfiyya.txt"), os.path.join(bad, "alfiyya.txt"))
b = bytearray(open(os.path.join(SRC, "qatr.txt"), "rb").read())
b[-1:] = b"\n\n" if b[-1:] == b"\n" else b + b"\n"
open(os.path.join(bad, "qatr.txt"), "wb").write(bytes(b))
V.append(("21_basma_fasida", os.path.join(M, "cases.json"), bad))

rejected = 0
for name, p, src in V:
    r = subprocess.run([sys.executable, "-I", os.path.join(M, "fahs_cases.py"), p, src],
                       capture_output=True, text=True)
    first = [l for l in r.stdout.splitlines() if l.startswith("خلل") or "غير صالح" in l][:1]
    print("%-28s exit=%d %s" % (name, r.returncode, first[0][:90] if first else ""))
    if r.returncode != 0:
        rejected += 1
print("رُفض %d من %d" % (rejected, len(V)))
sys.exit(0 if rejected == len(V) else 1)
