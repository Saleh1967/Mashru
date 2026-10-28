"""فاحص cases.json قبل التجميد (ضابط أسماء الإشارة). يُشغَّل: python3 -I fahs_cases.py [مسار cases.json] [مجلّد المودَعات]
يخرج 0 إن سلم كلُّ شيء، و1 مع قائمة الأخطاء إن لم يسلم."""
import hashlib
import json
import os
import re
import sys

HUNA = os.path.dirname(os.path.abspath(__file__))
MASAR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HUNA, "cases.json")
MUDAA = sys.argv[2] if len(sys.argv) > 2 else "/home/claude/mudaa_dir"
WASF = os.path.join(HUNA, "wasf.md")

MASADIR = {
    "قطر": ("qatr.txt", "2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d", range(132, 136)),
    "ألفية": ("alfiyya.txt", "13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0",
              [137, 138, 139, 140, 142, 143, 144]),  # 141 علامة صفحة لا نصّ فيه
}
FIAT = ["موجب", "حد", "خارج", "عموم", "غموض"]
ASL = ["ذا", "ذي", "ذه", "تي", "ته", "تا", "ذان", "تان", "ذين", "تين", "أولاء", "أولى", "هنا", "ثم"]
MUSHAR = ["مفرد_مذكر", "مفرد_مؤنث", "مثنى_مذكر", "مثنى_مؤنث", "جمع_مذكر", "جمع_مؤنث", "مكان"]
MAWDI = ["رفع", "نصب", "جر"]
BUD = ["قريب", "بعيد"]
AHKAM = ["مقبول", "خطأ", "لا_حكم"]
HUQUL = ["id", "fia", "mithal", "mithal_harfi", "dakhil", "hukm", "zawj", "sanad", "taliq"]
HUQUL_D = ["asl", "mushar", "mawdi", "bud", "ha", "lam", "kaf"]
MUTHANNA = {"ذان", "تان", "ذين", "تين"}
ADNA = {"موجب": 12, "حد": 10, "خارج": 5, "عموم": 6, "غموض": 2}

akhta = []


def khata(m):
    akhta.append(m)


def jarrid(s):
    for b in ("### | ", "# ", "~~"):
        if s.startswith(b):
            return s[len(b):]
    return s


# ١. بصمتا المصدرين، ومطابقتهما لما في المواصفة.
asthur = {}
try:
    wasf = open(WASF, encoding="utf-8").read()
except OSError as e:
    wasf = ""
    khata("لا تُقرأ المواصفة: %s" % e)
for m, (ism, basma, _) in MASADIR.items():
    if basma not in wasf:
        khata("بصمة %s ليست في المواصفة" % ism)
    try:
        b = open(os.path.join(MUDAA, ism), "rb").read()
    except OSError as e:
        khata("لا يُقرأ %s: %s" % (ism, e))
        continue
    h = hashlib.sha256(b).hexdigest()
    if h != basma:
        khata("بصمة %s %s لا تطابق %s" % (ism, h, basma))
    asthur[m] = b.decode("utf-8").split("\n")

# ٢. JSON.
try:
    with open(MASAR, encoding="utf-8") as f:
        data = json.load(f)
except Exception as e:  # noqa: BLE001
    print("خطأ: ليس JSON صالحًا: %s" % e)
    sys.exit(1)
if not isinstance(data, list):
    print("خطأ: الجذر ليس قائمة")
    sys.exit(1)

# ٣. كلُّ حالة.
ids = {}
dakhilat = {}
for i, c in enumerate(data):
    w = "الحالة %d" % (i + 1)
    if not isinstance(c, dict):
        khata("%s ليست كائنًا" % w)
        continue
    if sorted(c.keys()) != sorted(HUQUL):
        khata("%s حقولها %s" % (w, sorted(c.keys())))
        continue
    cid = c["id"]
    if not isinstance(cid, str) or not re.fullmatch(r"I\d\d", cid):
        khata("%s id غير صالح: %r" % (w, cid))
        continue
    w = cid
    if cid in ids:
        khata("%s مكرَّر" % cid)
    ids[cid] = c
    if c["fia"] not in FIAT:
        khata("%s فئة غير مسموحة: %r" % (w, c["fia"]))
    if not isinstance(c["mithal"], str) or not c["mithal"].strip():
        khata("%s mithal فارغ" % w)
    elif re.search("[ً-ْٰ]", c["mithal"]):
        khata("%s mithal مشكول" % w)
    if not isinstance(c["mithal_harfi"], bool):
        khata("%s mithal_harfi ليس منطقيًّا" % w)
    if not isinstance(c["taliq"], str) or not c["taliq"].strip() or "\n" in c["taliq"]:
        khata("%s taliq ليس سطرًا واحدًا" % w)
    d = c["dakhil"]
    if not isinstance(d, dict) or sorted(d.keys()) != sorted(HUQUL_D):
        khata("%s dakhil حقوله غير السبعة" % w)
        continue
    for k, qiyam in (("asl", ASL), ("mushar", MUSHAR), ("mawdi", MAWDI), ("bud", BUD)):
        if d[k] not in qiyam:
            khata("%s %s غير مسموح: %r" % (w, k, d[k]))
    for k in ("ha", "lam", "kaf"):
        if not isinstance(d[k], bool):
            khata("%s %s ليس منطقيًّا" % (w, k))
    mift = json.dumps(d, ensure_ascii=False, sort_keys=True)
    if mift in dakhilat:
        khata("%s مدخلُه مكرَّر مع %s" % (w, dakhilat[mift]))
    dakhilat[mift] = cid
    # الحكم بالفئة.
    h = c["hukm"]
    if c["fia"] == "غموض":
        if not (isinstance(h, list) and len(h) == 2 and all(x in AHKAM for x in h) and h[0] != h[1]):
            khata("%s غموض بلا بديلين صالحين: %r" % (w, h))
    else:
        if h not in AHKAM:
            khata("%s حكم غير مسموح: %r" % (w, h))
        elif c["fia"] == "موجب" and h != "مقبول":
            khata("%s موجب حكمه %s" % (w, h))
        elif c["fia"] == "حد" and h != "خطأ":
            khata("%s حد حكمه %s" % (w, h))
        elif c["fia"] == "خارج" and h != "لا_حكم":
            khata("%s خارج حكمه %s" % (w, h))
        elif c["fia"] == "عموم" and h == "لا_حكم":
            khata("%s عموم بلا حكم" % w)
    # السند.
    sn = c["sanad"]
    if not isinstance(sn, list):
        khata("%s sanad ليس قائمة" % w)
        continue
    if h == "لا_حكم" and sn:
        khata("%s لا_حكم وله سند" % w)
    if h != "لا_حكم" and not sn:
        khata("%s حكمه بلا سند" % w)
    nusus = []
    for p in sn:
        if not isinstance(p, dict) or sorted(p.keys()) != ["masdar", "nass", "satr"]:
            khata("%s قطعة سند حقولها غير الثلاثة" % w)
            continue
        m, s, nass = p["masdar"], p["satr"], p["nass"]
        if m not in MASADIR:
            khata("%s مصدر غير مسموح: %r" % (w, m))
            continue
        if not isinstance(s, int) or isinstance(s, bool) or s not in MASADIR[m][2]:
            khata("%s السطر %r من %s خارج النطاق" % (w, s, m))
            continue
        if m not in asthur:
            continue
        satr = jarrid(asthur[m][s - 1])
        nusus.append(satr)
        if not isinstance(nass, str) or not nass or "\n" in nass:
            khata("%s nass فارغ أو يعبر سطرين" % w)
        elif nass not in satr:
            khata("%s nass ليس في %s س%d: %r" % (w, m, s, nass))
    if c["mithal_harfi"] is True and not any(isinstance(c["mithal"], str) and c["mithal"] in t for t in nusus):
        khata("%s mithal_harfi=true والمثال ليس في أسطر سنده" % w)

# ٤. الأزواج.
azwaj = set()
for cid, c in ids.items():
    z = c["zawj"]
    if z is None:
        continue
    if z not in ids or z == cid:
        khata("%s زوجه %r غير موجود" % (cid, z))
        continue
    o = ids[z]
    if o["zawj"] != cid:
        khata("%s زوجه %s غير متبادل" % (cid, z))
    if not (isinstance(c["dakhil"], dict) and isinstance(o["dakhil"], dict)):
        continue
    farq = [k for k in HUQUL_D if c["dakhil"].get(k) != o["dakhil"].get(k)]
    if len(farq) != 1:
        khata("%s و%s يختلفان في %d حقول %s" % (cid, z, len(farq), farq))
    if json.dumps(c["hukm"], ensure_ascii=False) == json.dumps(o["hukm"], ensure_ascii=False):
        khata("%s و%s حكمهما واحد" % (cid, z))
    azwaj.add(tuple(sorted((cid, z))))

# ٥. الأعداد.
n = len(data)
if not 40 <= n <= 50:
    khata("العدد %d خارج 40–50" % n)
hal = [c for c in ids.values() if isinstance(c.get("dakhil"), dict)]
for f, a in ADNA.items():
    k = sum(1 for c in hal if c["fia"] == f)
    if k < a:
        khata("الفئة %s: %d أقلّ من %d" % (f, k, a))
for a in ASL:
    if not any(c["dakhil"].get("asl") == a for c in hal):
        khata("الأصل %s بلا حالة" % a)
for m in MUSHAR:
    k = sum(1 for c in hal if c["dakhil"].get("mushar") == m)
    if k < 3:
        khata("المشار %s: %d أقلّ من 3" % (m, k))
for k_, a in (("ha", 5), ("lam", 6), ("kaf", 10)):
    k = sum(1 for c in hal if c["dakhil"].get(k_) is True)
    if k < a:
        khata("%s=true: %d أقلّ من %d" % (k_, k, a))
k = sum(1 for c in hal if c["dakhil"].get("bud") == "بعيد")
if k < 10:
    khata("بعيد: %d أقلّ من 10" % k)
for m in MAWDI:
    k = sum(1 for c in hal if c["dakhil"].get("mawdi") == m and c["dakhil"].get("asl") in MUTHANNA)
    if k < 3:
        khata("الموضع %s في المثنى: %d أقلّ من 3" % (m, k))
if len(azwaj) < 6:
    khata("الأزواج %d أقلّ من 6" % len(azwaj))

if akhta:
    for m in akhta:
        print("خطأ:", m)
    sys.exit(1)
print("سليم: %d حالة، %d زوجًا؛ الفئات %s؛ الحرفيّة %d" % (
    n, len(azwaj), {f: sum(1 for c in hal if c["fia"] == f) for f in FIAT},
    sum(1 for c in hal if c["mithal_harfi"] is True)))
sys.exit(0)
