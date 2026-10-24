#!/usr/bin/env python3
"""فاحص حالات «هذا باب الجزاء» قبل التجميد (يُشغَّل بـ python3 -I).

الاستعمال:
  python3 -I fahs_cases.py [cases.json] [sibawayhi.txt]
يخرج بـ 0 إن مرّت الفحوص كلّها، وبـ 1 مع قائمة الأخطاء إن لم تمرّ.
"""
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CASES = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "cases.json")
SOURCE = sys.argv[2] if len(sys.argv) > 2 else "/home/claude/mudaa_dir/sibawayhi.txt"
SOURCE_SHA = "a160f940bb194e6fe7e6655d2c7f28e41f1fc648c4c5e340cc4e42306d5cb625"
SCOPE = (9190, 9304)

FIA = {"موجب", "حد", "خارج", "عموم"}
TARTIB = {"شرط_أولا", "جواب_أولا"}
SHART = {"مضارع_مجزوم", "مضارع_مرفوع", "ماض"}
JAWAB = {
    "مضارع_مجزوم", "مضارع_مرفوع", "ماض",
    "فاء_اسمية", "فاء_مضارع_مرفوع", "فاء_مضارع_مجزوم", "فاء_غيرهما",
    "إذا_اسمية", "فاء_إذا", "اسمية", "واو", "ثم", "لام_قسم",
}
KALAM = {"مقبول", "قبيح", "خطأ", "لا_حكم"}
SHIR = {"مقبول", "قبيح", "خطأ", "لا_حكم", "غير_مسؤول"}
QUOTA = {"موجب": 8, "حد": 8, "خارج": 6, "عموم": 6}
KEYS = {"id", "fia", "mithal", "mithal_harfi", "dakhil", "kharij", "sanad", "taliq"}
DKEYS = {"adat", "tartib", "lam_qasam", "shart", "jawab"}
HARAKAT = re.compile("[ً-ْٰ]")

errors = []


def err(cid, msg):
    errors.append(f"{cid}: {msg}")


def strip_prefix(line):
    if line.startswith("~~"):
        return line[2:]
    if line.startswith("# "):
        return line[2:]
    return line


raw = open(SOURCE, "rb").read()
if hashlib.sha256(raw).hexdigest() != SOURCE_SHA:
    err("SOURCE", "بصمة المصدر لا تطابق المواصفة")
lines = raw.decode("utf-8").split("\n")


def line_text(n):
    return strip_prefix(lines[n - 1])


try:
    with open(CASES, "rb") as fh:
        cases = json.loads(fh.read().decode("utf-8"))
except Exception as e:  # noqa: BLE001
    print(f"JSON غير صالح: {e}")
    sys.exit(1)

if not isinstance(cases, list):
    print("الملفّ ليس قائمة")
    sys.exit(1)

ids = set()
dakhils = set()
count = {k: 0 for k in FIA}

for i, c in enumerate(cases):
    cid = c.get("id", f"#{i}") if isinstance(c, dict) else f"#{i}"
    if not isinstance(c, dict):
        err(cid, "ليست كائنًا")
        continue
    if set(c) != KEYS:
        err(cid, f"المفاتيح {sorted(set(c) ^ KEYS)}")
        continue
    if not re.fullmatch(r"J\d\d", c["id"]):
        err(cid, "صيغة id")
    if c["id"] in ids:
        err(cid, "id مكرّر")
    ids.add(c["id"])

    if c["fia"] not in FIA:
        err(cid, f"fia غير مسموح: {c['fia']}")
    else:
        count[c["fia"]] += 1

    m = c["mithal"]
    if not isinstance(m, str) or not m.strip():
        err(cid, "mithal فارغ")
    elif HARAKAT.search(m):
        err(cid, "mithal فيه تشكيل")
    if not isinstance(c["mithal_harfi"], bool):
        err(cid, "mithal_harfi ليس منطقيًّا")

    d = c["dakhil"]
    if not isinstance(d, dict) or set(d) != DKEYS:
        err(cid, "مفاتيح dakhil")
        continue
    if not isinstance(d["adat"], str) or not d["adat"].strip() or HARAKAT.search(d["adat"]):
        err(cid, "adat")
    elif len(d["adat"].split()) > 2:
        err(cid, "adat أكثر من كلمتين")
    if d["tartib"] not in TARTIB:
        err(cid, f"tartib: {d['tartib']}")
    if not isinstance(d["lam_qasam"], bool):
        err(cid, "lam_qasam ليس منطقيًّا")
    if d["shart"] not in SHART:
        err(cid, f"shart: {d['shart']}")
    if d["jawab"] not in JAWAB:
        err(cid, f"jawab: {d['jawab']}")
    key = json.dumps(d, ensure_ascii=False, sort_keys=True)
    if key in dakhils:
        err(cid, "dakhil مكرّر")
    dakhils.add(key)

    k = c["kharij"]
    if not isinstance(k, dict) or set(k) != {"kalam", "shir"}:
        err(cid, "مفاتيح kharij")
        continue
    if k["kalam"] not in KALAM:
        err(cid, f"kalam غير مسموح: {k['kalam']}")
    if k["shir"] not in SHIR:
        err(cid, f"shir غير مسموح: {k['shir']}")

    # اتّساق الفئة مع الحكم
    if c["fia"] == "خارج" and k["kalam"] != "لا_حكم":
        err(cid, "خارج وحكمه ليس لا_حكم")
    if c["fia"] != "خارج" and k["kalam"] == "لا_حكم":
        err(cid, "لا_حكم في غير خارج")
    if c["fia"] == "موجب" and k["kalam"] != "مقبول":
        err(cid, "موجب وكلامه غير مقبول")
    if c["fia"] == "حد" and k["kalam"] not in {"قبيح", "خطأ"}:
        err(cid, "حد وكلامه لا قبيح ولا خطأ")

    s = c["sanad"]
    if not isinstance(s, list):
        err(cid, "sanad ليس قائمة")
        continue
    if k["kalam"] == "لا_حكم":
        if s:
            err(cid, "حالة لا_حكم لها سند")
        if k["shir"] not in {"لا_حكم", "غير_مسؤول"}:
            err(cid, "لا_حكم في الكلام وحكمٌ في الشعر")
    else:
        if not s:
            err(cid, "حكمٌ بلا سند")
    for e in s:
        if not isinstance(e, dict) or set(e) != {"satr", "nass"}:
            err(cid, "عنصر سند")
            continue
        n, t = e["satr"], e["nass"]
        if not isinstance(n, int) or not (SCOPE[0] <= n <= SCOPE[1]):
            err(cid, f"السطر {n} خارج النطاق")
            continue
        if not isinstance(t, str) or not t:
            err(cid, f"nass فارغ في {n}")
            continue
        if "\n" in t:
            err(cid, f"nass يعبر سطرين في {n}")
        if t.encode("utf-8") not in line_text(n).encode("utf-8"):
            err(cid, f"nass ليس قطعةً من السطر {n}: {t}")

    if c["mithal_harfi"] is True:
        if not any(isinstance(e, dict) and isinstance(e.get("satr"), int)
                   and SCOPE[0] <= e["satr"] <= SCOPE[1]
                   and m in line_text(e["satr"]) for e in s):
            err(cid, "mithal_harfi=true والمثال ليس في سطرٍ من أسطر سنده")

    tq = c["taliq"]
    if not isinstance(tq, str) or not tq.strip() or "\n" in tq:
        err(cid, "taliq ليس سطرًا واحدًا")

n = len(cases)
if not (30 <= n <= 40):
    err("ALL", f"العدد {n} خارج 30–40")
for f, q in QUOTA.items():
    if count[f] < q:
        err("ALL", f"{f}: {count[f]} < {q}")

harfi = sum(1 for c in cases if isinstance(c, dict) and c.get("mithal_harfi") is True)
print(f"العدد {n}؛ " + "، ".join(f"{f} {count[f]}" for f in ["موجب", "حد", "خارج", "عموم"])
      + f"؛ حرفيّ {harfi}")
if errors:
    print("أخطاء:")
    for e in errors:
        print("  " + e)
    sys.exit(1)
print("مرّ")
sys.exit(0)
