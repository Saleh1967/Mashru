"""خريطةُ التوظيف: ما يبلغه التنفيذيُّ من وحدات Lean، وما يستعمله الكودُ من المودَعات، وما يُجلب منها على CI.

سندُه أمرُ المالك 2026-11-21 (13:57 بتوقيت عمّان): «لا اريد ان تبقي اي مختوم او مودع او جدول او lean خارج التوظيف مطلقا».
فالتوظيفُ هنا مقيسٌ بالكود لا بعناوين الملفّات:
  * وحدةُ Lean موظَّفةٌ إن بلغها جذرُ تنفيذيٍّ في lakefile.toml (`[[lean_exe]] root`) بسلسلة `import`؛ وما سواها نظريٌّ لا يحسب به تنفيذيّ.
  * المودَعُ موظَّفٌ إن ذُكر اسمُ ملفّه في كود (‎.py أو ‎.lean أو ‎.sh أو ‎.yml) خارج سجلّاته (sijill.json وsijill.tsv وFaahis/SijillMakhtum.lean)؛
    ويُجلب على CI إن كان له رابطٌ أو مولِّدٌ في mudaat/jalb.py (URL وMUSHTAQQ)، وإلّا فبايتاتُه عند المالك وحده.
الخريطة tahaqquq/tawzif.json مولَّدةٌ لا تُحرَّر يدويًّا؛ و`--check` يطابقها بالمولَّد. والبوّابة (٥خ٤) تمنع زيادةَ غير الموظَّف عن خطّ أساسه.
التشغيل: python3 -I scripts/bina_tawzif.py [--check] [--jadhr <مجلّد>]
"""
import json
import os
import re
import sys
import tomllib

JADHR_ASLI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIJILLAT = {os.path.join("mudaat", "sijill.json"), os.path.join("mudaat", "sijill.tsv"), os.path.join("Faahis", "SijillMakhtum.lean")}
IMTIDADAT = (".py", ".lean", ".sh", ".yml")
TUKHTA = {".git", ".lake", ".mudaa", "__pycache__", "artifacts"}
IMPORT = re.compile(r"^import\s+(\S+)", re.M)


def masar_wahda(jadhr, wahda):
    return os.path.join(jadhr, *wahda.split(".")) + ".lean"


def lakefile(jadhr):
    t = tomllib.load(open(os.path.join(jadhr, "lakefile.toml"), "rb"))
    maktabat = [l["name"] for l in t.get("lean_lib", [])]
    tanfidhiyyat = {e["name"]: e["root"] for e in t.get("lean_exe", [])}
    return maktabat, tanfidhiyyat


def wahdat_maktaba(jadhr, maktabat):
    """وحداتُ المكتبات: كلُّ ‎.lean تحت مجلّد مكتبةٍ (وجذرُها إن وُجد)، لا integrations ولا tahaqquq."""
    out = set()
    for m in maktabat:
        if os.path.exists(os.path.join(jadhr, m + ".lean")):
            out.add(m)
        for root, ds, fs in os.walk(os.path.join(jadhr, m)):
            ds[:] = [d for d in ds if d not in TUKHTA]
            for f in fs:
                if f.endswith(".lean"):
                    out.add(os.path.relpath(os.path.join(root, f), jadhr)[:-5].replace(os.sep, "."))
    return out


def istirad(jadhr, wahda):
    p = masar_wahda(jadhr, wahda)
    if not os.path.exists(p):
        return []
    return IMPORT.findall(open(p, encoding="utf-8").read())


def mablugh(jadhr, judhur):
    seen, st = set(), list(judhur)
    while st:
        x = st.pop()
        if x in seen or not os.path.exists(masar_wahda(jadhr, x)):
            continue
        seen.add(x)
        st += istirad(jadhr, x)
    return seen


def milaffat_kod(jadhr):
    for root, ds, fs in os.walk(jadhr):
        ds[:] = [d for d in ds if d not in TUKHTA]
        for f in fs:
            if f.endswith(IMTIDADAT):
                p = os.path.relpath(os.path.join(root, f), jadhr)
                if p not in SIJILLAT:
                    yield p


def jalb_mutah(jadhr):
    """أسماءُ الملفّات التي لها رابطٌ أو مولِّدٌ في jalb.py (URL وMUSHTAQQ)، بقراءة مفاتيح القاموسين نصًّا."""
    p = os.path.join(jadhr, "mudaat", "jalb.py")
    if not os.path.exists(p):
        return set()
    src = open(p, encoding="utf-8").read()
    asma = set()
    for qamus in ("OPENITI", "MALIK", "UKHRA", "MUSHTAQQ"):
        m = re.search(rf"^{qamus} = \{{(.*?)^\}}", src, re.M | re.S)
        if m:
            asma |= set(re.findall(r'^\s*"([^"]+)":', m.group(1), re.M))
    return asma


def wallid(jadhr):
    maktabat, tanfidhiyyat = lakefile(jadhr)
    wahdat = wahdat_maktaba(jadhr, maktabat)
    bulugh = {e: mablugh(jadhr, [r]) for e, r in tanfidhiyyat.items()}
    kull = set().union(*bulugh.values()) if bulugh else set()
    lean = {w: sorted(e for e, s in bulugh.items() if w in s) for w in sorted(wahdat)}
    sijill = json.load(open(os.path.join(jadhr, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
    nusus = {p: open(os.path.join(jadhr, p), encoding="utf-8", errors="replace").read() for p in milaffat_kod(jadhr)}
    mutah = jalb_mutah(jadhr)
    mudaat = {}
    for m in sijill:
        f = m["milaf"]
        mudaat[f] = {"ism": m["ism"], "hala": m["hala"], "naw": m["naw"],
                     "yujlab": f in mutah,
                     "mustamil": sorted(p for p, t in nusus.items() if f in t and not p.endswith("jalb.py"))}
    ghayr_lean = sorted(w for w in wahdat if w not in kull)
    ghayr_mudaa = sorted(f for f, v in mudaat.items() if not v["mustamil"])
    la_yujlab = sorted(f for f, v in mudaat.items() if not v["yujlab"])
    return {
        "_": "مولَّدٌ بـ python3 -I scripts/bina_tawzif.py؛ لا يُحرَّر يدويًّا.",
        "khulasa": {
            "wahdat": len(wahdat), "muwazzafa": len(wahdat) - len(ghayr_lean), "ghayr_muwazzafa": len(ghayr_lean),
            "mudaat": len(mudaat), "mudaat_ghayr_mustamala": len(ghayr_mudaa), "mudaat_la_tujlab": len(la_yujlab),
            "tanfidhiyyat": {e: len(s) for e, s in sorted(bulugh.items())},
        },
        "ghayr_muwazzafa": ghayr_lean,
        "mudaat_ghayr_mustamala": ghayr_mudaa,
        "mudaat_la_tujlab": la_yujlab,
        "lean": lean,
        "mudaat": mudaat,
    }


def nass(jadhr):
    return json.dumps(wallid(jadhr), ensure_ascii=False, indent=1) + "\n"


def main(argv):
    jadhr = argv[argv.index("--jadhr") + 1] if "--jadhr" in argv else JADHR_ASLI
    out = os.path.join(jadhr, "tahaqquq", "tawzif.json")
    n = nass(jadhr)
    if "--check" in argv:
        ok = os.path.exists(out) and open(out, encoding="utf-8").read() == n
        print("مطابق" if ok else "tawzif.json لا يطابق المولَّد (python3 -I scripts/bina_tawzif.py)")
        return 0 if ok else 1
    open(out, "w", encoding="utf-8").write(n)
    k = json.loads(n)["khulasa"]
    print(f"الوحدات {k['wahdat']}: موظَّفة {k['muwazzafa']}، غيرُ موظَّفة {k['ghayr_muwazzafa']}؛ "
          f"المودَعات {k['mudaat']}: غيرُ مستعملة {k['mudaat_ghayr_mustamala']}، لا تُجلب {k['mudaat_la_tujlab']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
