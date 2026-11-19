#!/usr/bin/env python3
# فحص cases.json لضابط «نواة التوليد» — يُشغَّل: python3 -I fahs_cases.py [cases.json] [masdar.md]
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CASES = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "cases.json")
MASDAR = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "masdar.md")

FIA = {"موجب", "حد", "خارج", "صورة", "غموض"}
JADHR = {"ك-س-ر", "ع-ل-م", "غائب"}
AMIL = ["الفاعلية", "المفعولية", "السببية", "المطاوعة", "الزمان_والمكان", "الآلة", "المبالغة"]
JINS = {"إنسان", "حيوان", "نبات", "جماد", "غائب"}
QAYD = {"صلب", "لا", "لا_حكم"}
HUKM = {"مرخَّص", "ممتنع", "لا_حكم", "لا_نواة", "لا_جنس"}
FIA_HUKM = {"موجب": {"مرخَّص"}, "حد": {"ممتنع"}, "خارج": {"لا_نواة", "لا_جنس"}, "صورة": {"لا_حكم"}}
SIGHA_RE = re.compile(r"^[ء-ي]+$")  # حروف عربية بلا تشكيل
MIN_N, MAX_N = 20, 36
LINE_MIN, LINE_MAX = 1, 34

errs = []
def err(msg): errs.append(msg)

# --- المصدر
lines = {}
try:
    with open(MASDAR, encoding="utf-8") as f:
        for raw in f.read().split("\n"):
            m = re.match(r"^(\d+)\. (.*)$", raw)
            if m:
                n = int(m.group(1))
                if n in lines: err(f"masdar: السطر {n} مكرّر")
                lines[n] = m.group(2)
except Exception as e:
    err(f"masdar: تعذّرت القراءة: {e}")
for n in range(LINE_MIN, LINE_MAX + 1):
    if n not in lines: err(f"masdar: السطر {n} غائب")

# --- JSON
try:
    with open(CASES, encoding="utf-8") as f:
        data = json.load(f)
except Exception as e:
    print(f"خطأ: JSON غير صالح: {e}"); sys.exit(1)
if not isinstance(data, list):
    print("خطأ: الجذر ليس قائمة"); sys.exit(1)

def is_str(x): return isinstance(x, str) and x != ""
ids, dakhils, ghumud_dup = set(), {}, 0
fia_count = {k: 0 for k in FIA}
amils, jadhrs, hukms = set(), set(), set()
had_inedam = had_jumud = had_ala_ghayr = False

for i, c in enumerate(data):
    tag = f"[{i}]"
    if not isinstance(c, dict): err(f"{tag} ليس كائنًا"); continue
    if set(c) != {"id", "fia", "dakhil", "kharij", "sanad", "taliq"}:
        err(f"{tag} حقول ناقصة أو زائدة: {sorted(c)}"); continue
    cid = c["id"]; tag = f"[{cid}]"
    if not (is_str(cid) and re.fullmatch(r"T\d{2}", cid)): err(f"{tag} id ليس على صورة Tnn")
    if cid in ids: err(f"{tag} id مكرّر")
    ids.add(cid)
    fia = c["fia"]
    if fia not in FIA: err(f"{tag} fia غير مسموحة: {fia}"); continue
    fia_count[fia] += 1
    d, k = c["dakhil"], c["kharij"]
    if not (isinstance(d, dict) and set(d) == {"jadhr", "amil", "jins"}): err(f"{tag} dakhil مشوّه"); continue
    if not (isinstance(k, dict) and set(k) == {"sigha", "mawruth", "qayd", "hukm"}): err(f"{tag} kharij مشوّه"); continue
    if d["jadhr"] not in JADHR: err(f"{tag} jadhr غير مسموح: {d['jadhr']}")
    if d["amil"] not in AMIL: err(f"{tag} amil غير مسموح: {d['amil']}")
    if d["jins"] not in JINS: err(f"{tag} jins غير مسموح: {d['jins']}")
    amils.add(d["amil"]); jadhrs.add(d["jadhr"])
    key = (d["jadhr"], d["amil"], d["jins"])
    if key in dakhils:
        prev = dakhils[key]
        if fia == "غموض" or prev == "غموض":
            ghumud_dup += 1
            if ghumud_dup > 1: err(f"{tag} أكثر من تكرار واحد للمدخل مع غموض")
        else:
            err(f"{tag} المدخل dakhil مكرّر")
    dakhils[key] = fia
    sig = k["sigha"]
    if not is_str(sig): err(f"{tag} sigha ليست نصًّا")
    elif sig != "لا_حكم" and not SIGHA_RE.match(sig.replace("ّ", "")): err(f"{tag} sigha فيها غير الحروف أو تشكيل غير الشدّة: {sig}")
    elif sig.count("ّ") > 1: err(f"{tag} أكثر من شدّة")
    mw = k["mawruth"]
    if not (isinstance(mw, list) and all(is_str(x) for x in mw)): err(f"{tag} mawruth ليست قائمة نصوص")
    if k["qayd"] not in QAYD: err(f"{tag} qayd غير مسموح: {k['qayd']}")
    h = k["hukm"]
    if fia == "غموض":
        if not (isinstance(h, list) and len(h) == 2 and all(x in HUKM for x in h) and h[0] != h[1]):
            err(f"{tag} غموض: hukm يجب أن يكون قائمة بديلين مختلفين مسموحين")
    else:
        if h not in HUKM: err(f"{tag} hukm غير مسموح: {h}")
        elif h not in FIA_HUKM[fia]: err(f"{tag} hukm {h} لا يوافق الفئة {fia}")
        else: hukms.add(h)
    # اتّساق الجذر الغائب والجنس الغائب (س28)
    if d["jadhr"] == "غائب":
        if not (h == "لا_نواة" and sig == "لا_حكم" and mw == [] and k["qayd"] == "لا_حكم"):
            err(f"{tag} جذر غائب يقتضي لا_نواة وصيغة لا_حكم وموروثًا فارغًا وقيدًا لا_حكم")
    else:
        if h == "لا_نواة": err(f"{tag} لا_نواة مع جذر في النواة")
        if sig == "لا_حكم": err(f"{tag} صيغة لا_حكم مع جذر في النواة")
        if d["jins"] == "غائب" and h != "لا_جنس": err(f"{tag} جنس غائب يقتضي لا_جنس")
        if d["jins"] != "غائب" and h == "لا_جنس": err(f"{tag} لا_جنس مع جنس في النواة")
    # السند
    sn = c["sanad"]
    if not isinstance(sn, list): err(f"{tag} sanad ليس قائمة"); sn = []
    if h == "لا_حكم":
        if sn != []: err(f"{tag} لا_حكم يقتضي سندًا فارغًا")
    elif not sn: err(f"{tag} حكمٌ بلا سند")
    nass_all = ""
    for j, s in enumerate(sn):
        if not (isinstance(s, dict) and set(s) == {"satr", "nass"}): err(f"{tag} sanad[{j}] مشوّه"); continue
        st, ns = s["satr"], s["nass"]
        if not (isinstance(st, int) and not isinstance(st, bool) and LINE_MIN <= st <= LINE_MAX):
            err(f"{tag} sanad[{j}] satr خارج 1–34: {st}"); continue
        if not is_str(ns): err(f"{tag} sanad[{j}] nass ليس نصًّا"); continue
        if st in lines and ns not in lines[st]: err(f"{tag} sanad[{j}] nass ليس قطعة من السطر {st}: {ns!r}")
        nass_all += ns + "\n"
    tl = c["taliq"]
    if not is_str(tl) or "\n" in tl: err(f"{tag} taliq ليس سطرًا واحدًا")
    # الحصص الفرعية داخل حد
    if fia == "حد":
        # بمفتاح المواصفة: «انعدام_العقل» ⇐ الحيوان، «الجمود_المطلق» ⇐ الجماد، وكلاهما من موانع ع-ل-م وحدَه
        if d["jadhr"] == "ع-ل-م" and d["jins"] == "حيوان" and "انعدام_العقل" in nass_all: had_inedam = True
        if d["jadhr"] == "ع-ل-م" and d["jins"] == "جماد" and "الجمود_المطلق" in nass_all: had_jumud = True
        if d["amil"] == "الآلة" and d["jins"] not in ("جماد", "غائب") and not (d["jadhr"] == "ع-ل-م" and d["jins"] == "حيوان"):
            had_ala_ghayr = True

# --- العدد والحصص
n = len(data)
if not (MIN_N <= n <= MAX_N): err(f"العدد {n} خارج [{MIN_N}, {MAX_N}]")
for f_, q in (("موجب", 3), ("حد", 5), ("خارج", 3), ("صورة", 5)):
    if fia_count[f_] < q: err(f"الفئة {f_}: {fia_count[f_]} < {q}")
if not had_inedam: err("حد: لا حالة بمانع «انعدام_العقل»")
if not had_jumud: err("حد: لا حالة بمانع «الجمود_المطلق»")
if not had_ala_ghayr: err("حد: لا حالة آلة في غير الجماد بلا مانع")
if "لا_نواة" not in hukms: err("خارج: لا حالة لا_نواة")
if "لا_جنس" not in hukms: err("خارج: لا حالة لا_جنس")
for a in AMIL:
    if a not in amils: err(f"العامل {a} لا يظهر")
for r in ("ك-س-ر", "ع-ل-م"):
    if r not in jadhrs: err(f"الجذر {r} لا يظهر")

if errs:
    print("فشل الفحص:"); [print(" -", e) for e in errs]; sys.exit(1)
print(f"نجح الفحص: {n} حالة؛ " + "، ".join(f"{k} {fia_count[k]}" for k in ("موجب", "حد", "خارج", "صورة", "غموض")))
sys.exit(0)
