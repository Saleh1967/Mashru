"""فاحص حالات ضابط الضمير قبل التجميد (يُشغَّل بـ python3 -I).

الاستعمال: python3 -I fahs_cases.py [cases.json] [مجلد_المصادر]
القيم الافتراضية: cases.json بجوار السكربت، و/home/claude/mudaa_dir للمصدرين.
يخرج 0 إن مرّت الفحوص كلّها، و1 مع قائمة الأخطاء إن لم تمرّ.
"""
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CASES = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "cases.json")
SRC_DIR = sys.argv[2] if len(sys.argv) > 2 else "/home/claude/mudaa_dir"
WASF = os.path.join(HERE, "wasf.md")

SOURCES = {
    "قطر": ("qatr.txt", "2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d", range(124, 129)),
    "ألفية": ("alfiyya.txt", "13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0",
              [n for n in range(105, 120) if n != 108]),
}

FIELDS = {
    "amil": {"فعل_لواحد", "فعل_لاثنين", "ظن", "كان", "اسم", "لا_عامل"},
    "mawqi": {"يلي_العامل", "بعد_إلا", "ابتداء"},
    "qablahu": {"متكلم", "مخاطب", "غائب", "لا_شيء"},
    "rutba": {"متكلم", "مخاطب", "غائب"},
    "shakl": {"متصل", "منفصل"},
    "darura": {True, False},
}
FIA = {"موجب", "حد", "خارج", "عموم", "غموض"}
HUKM = {"مقبول", "خطأ", "لا_حكم"}
DARAJA = {"راجح", "مرجوح", "سواء", "بلا_درجة"}
KEYS = {"id", "fia", "mithal", "mithal_harfi", "dakhil", "hukm", "daraja", "zawj", "sanad", "taliq"}
HARAKAT = re.compile("[ً-ْٰ]")

errors = []


def err(msg):
    errors.append(msg)


def strip_prefix(line):
    for p in ("### | ", "~~", "# "):
        if line.startswith(p):
            return line[len(p):]
    return line


# --- المصادر: البصمة والأسطر ---
lines = {}
for masdar, (fname, sha, _) in SOURCES.items():
    path = os.path.join(SRC_DIR, fname)
    try:
        data = open(path, "rb").read()
    except OSError as e:
        err(f"لا يُقرأ المصدر {path}: {e}")
        continue
    got = hashlib.sha256(data).hexdigest()
    if got != sha:
        err(f"بصمة {fname} {got} لا تطابق المواصفة {sha}")
    lines[masdar] = data.decode("utf-8").split("\n")

# البصمتان في المواصفة نفسها
try:
    wasf = open(WASF, encoding="utf-8").read()
    for masdar, (fname, sha, _) in SOURCES.items():
        if sha not in wasf:
            err(f"بصمة {fname} ليست في wasf.md")
except OSError as e:
    err(f"لا تُقرأ المواصفة {WASF}: {e}")


def line_text(masdar, satr):
    return strip_prefix(lines[masdar][satr - 1])


# --- الملف ---
try:
    raw = open(CASES, "rb").read()
    cases = json.loads(raw.decode("utf-8"))
except Exception as e:  # noqa: BLE001
    print(f"خطأ: JSON غير صالح: {e}")
    sys.exit(1)

if not isinstance(cases, list):
    print("خطأ: الملفّ ليس قائمة")
    sys.exit(1)

ids = {}
for i, c in enumerate(cases):
    if not isinstance(c, dict):
        err(f"العنصر {i} ليس كائنًا")
        continue
    cid = c.get("id")
    if set(c.keys()) != KEYS:
        err(f"{cid}: المفاتيح {sorted(c.keys())} غير المطلوبة")
    if not isinstance(cid, str) or not re.fullmatch(r"D\d{2}", cid):
        err(f"العنصر {i}: id غير صالح {cid!r}")
    elif cid in ids:
        err(f"{cid}: id مكرّر")
    else:
        ids[cid] = c


def as_set(v):
    return frozenset(v) if isinstance(v, list) else frozenset([v])


dakhil_seen = {}
for cid, c in ids.items():
    fia = c.get("fia")
    if fia not in FIA:
        err(f"{cid}: fia غير مسموح {fia!r}")
    # dakhil
    d = c.get("dakhil")
    if not isinstance(d, dict) or set(d.keys()) != set(FIELDS):
        err(f"{cid}: حقول dakhil غير الستّة")
        d = {}
    for k, allowed in FIELDS.items():
        v = d.get(k)
        if k == "darura":
            if not isinstance(v, bool):
                err(f"{cid}: darura ليس منطقيًّا")
        elif v not in allowed:
            err(f"{cid}: {k} = {v!r} غير مسموح")
    if (d.get("mawqi") == "ابتداء") != (d.get("amil") == "لا_عامل"):
        err(f"{cid}: ابتداء لا يكون إلّا مع لا_عامل، ولا_عامل لا يكون إلّا في ابتداء")
    key = tuple(d.get(k) for k in FIELDS)
    if key in dakhil_seen:
        err(f"{cid}: المدخل نفسُه في {dakhil_seen[key]}")
    else:
        dakhil_seen[key] = cid
    # hukm / daraja
    h, dr = c.get("hukm"), c.get("daraja")
    if fia == "غموض":
        hl, dl = isinstance(h, list), isinstance(dr, list)
        if hl == dl:
            err(f"{cid}: غموض يحتاج قائمة في hukm أو في daraja (واحدة لا اثنتين)")
        if hl:
            if len(h) != 2 or len(set(h)) != 2 or not set(h) <= HUKM:
                err(f"{cid}: قائمة hukm غير صالحة {h!r}")
            if dr != "بلا_درجة":
                err(f"{cid}: hukm غير «مقبول» ودرجته ليست بلا_درجة")
        if dl:
            if h != "مقبول":
                err(f"{cid}: قائمة الدرجات تحتاج hukm = مقبول")
            if len(dr) != 2 or len(set(dr)) != 2 or not set(dr) <= DARAJA:
                err(f"{cid}: قائمة daraja غير صالحة {dr!r}")
    else:
        if h not in HUKM:
            err(f"{cid}: hukm غير مسموح {h!r}")
        if dr not in DARAJA:
            err(f"{cid}: daraja غير مسموحة {dr!r}")
        if h != "مقبول" and dr != "بلا_درجة":
            err(f"{cid}: hukm = {h} ودرجته ليست بلا_درجة")
    if fia == "موجب" and h != "مقبول":
        err(f"{cid}: موجب وحكمه غير مقبول")
    if fia == "حد" and h != "خطأ":
        err(f"{cid}: حد وحكمه غير خطأ")
    if (fia == "خارج") != (h == "لا_حكم"):
        err(f"{cid}: لا_حكم للفئة خارج وحدها، وخارج لا يكون إلّا لا_حكم")
    # sanad
    s = c.get("sanad")
    if not isinstance(s, list):
        err(f"{cid}: sanad ليس قائمة")
        s = []
    if h == "لا_حكم" and s:
        err(f"{cid}: لا_حكم وله سند")
    if h != "لا_حكم" and not s:
        err(f"{cid}: حكم بلا سند")
    full_lines = []
    for p in s:
        if not isinstance(p, dict) or set(p.keys()) != {"masdar", "satr", "nass"}:
            err(f"{cid}: قطعة سند غير صالحة {p!r}")
            continue
        m, n, t = p["masdar"], p["satr"], p["nass"]
        if m not in SOURCES:
            err(f"{cid}: masdar غير مسموح {m!r}")
            continue
        if not isinstance(n, int) or isinstance(n, bool) or n not in SOURCES[m][2]:
            err(f"{cid}: السطر {n!r} من {m} خارج النطاق")
            continue
        if not isinstance(t, str) or not t or "\n" in t:
            err(f"{cid}: nass فارغ أو يعبر سطرين")
            continue
        if m not in lines:
            continue
        lt = line_text(m, n)
        full_lines.append(lt)
        if t.encode("utf-8") not in lt.encode("utf-8"):
            err(f"{cid}: nass {t!r} ليس قطعة من {m} {n}")
    # mithal
    mt = c.get("mithal")
    if not isinstance(mt, str) or not mt.strip():
        err(f"{cid}: mithal فارغ")
        mt = ""
    if HARAKAT.search(mt):
        err(f"{cid}: mithal مشكول")
    mh = c.get("mithal_harfi")
    if not isinstance(mh, bool):
        err(f"{cid}: mithal_harfi ليس منطقيًّا")
    elif mh and not any(mt in lt for lt in full_lines):
        err(f"{cid}: mithal_harfi = true والمثال ليس في أسطر سنده")
    elif not mh and any(mt and mt in lt for lt in full_lines):
        err(f"{cid}: mithal_harfi = false والمثال بحروفه في أسطر سنده")
    # taliq
    tq = c.get("taliq")
    if not isinstance(tq, str) or not tq.strip() or "\n" in tq:
        err(f"{cid}: taliq ليس سطرًا واحدًا")

# --- الأزواج ---
pairs = set()
for cid, c in ids.items():
    z = c.get("zawj")
    if z is None:
        continue
    if z not in ids or z == cid:
        err(f"{cid}: zawj {z!r} ليس حالة أخرى")
        continue
    o = ids[z]
    if o.get("zawj") != cid:
        err(f"{cid}: الزوج {z} غير متبادل")
        continue
    d1, d2 = c.get("dakhil") or {}, o.get("dakhil") or {}
    diff = [k for k in FIELDS if d1.get(k) != d2.get(k)]
    if len(diff) != 1:
        err(f"{cid}–{z}: يختلفان في {len(diff)} حقل لا في حقل واحد {diff}")
    if as_set(c.get("hukm")) == as_set(o.get("hukm")) and as_set(c.get("daraja")) == as_set(o.get("daraja")):
        err(f"{cid}–{z}: لا يختلفان في الحكم ولا في الدرجة")
    pairs.add(frozenset((cid, z)))

# --- الأعداد ---
allc = list(ids.values())
n = len(allc)
if not 40 <= n <= 55:
    err(f"العدد {n} خارج 40–55")


def count(pred):
    return sum(1 for c in allc if pred(c))


for f, mn in (("موجب", 12), ("حد", 10), ("خارج", 5), ("عموم", 6), ("غموض", 2)):
    k = count(lambda c, f=f: c.get("fia") == f)
    if k < mn:
        err(f"الفئة {f}: {k} < {mn}")
for a in FIELDS["amil"]:
    k = count(lambda c, a=a: (c.get("dakhil") or {}).get("amil") == a)
    if k < 2:
        err(f"amil {a}: {k} < 2")
for mw in FIELDS["mawqi"]:
    k = count(lambda c, mw=mw: (c.get("dakhil") or {}).get("mawqi") == mw)
    if k < 2:
        err(f"mawqi {mw}: {k} < 2")
k = count(lambda c: (c.get("dakhil") or {}).get("shakl") == "منفصل")
if k < 12:
    err(f"منفصل: {k} < 12")
k = count(lambda c: (c.get("dakhil") or {}).get("darura") is True)
if k < 3:
    err(f"darura true: {k} < 3")
k = count(lambda c: (c.get("dakhil") or {}).get("qablahu") not in (None, "لا_شيء"))
if k < 12:
    err(f"qablahu غير لا_شيء: {k} < 12")
for dg in ("راجح", "مرجوح", "سواء"):
    k = count(lambda c, dg=dg: c.get("hukm") == "مقبول" and c.get("daraja") == dg)
    if k < 2:
        err(f"الدرجة {dg} متوقَّعة منفردةً في {k} < 2")
if len(pairs) < 6:
    err(f"الأزواج {len(pairs)} < 6")

if errors:
    for e in errors:
        print("خطأ:", e)
    print(f"لم يمرّ: {len(errors)} خطأ")
    sys.exit(1)

print(f"مرّ: {n} حالة، {len(pairs)} زوجًا")
sys.exit(0)
