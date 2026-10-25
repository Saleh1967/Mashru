#!/usr/bin/env python3
"""فاحص cases.json لضابط «هذا باب الفاء» (على wasf.md).

الاستعمال: python3 -I fahs_cases.py [cases.json] [sibawayhi.txt]
يخرج 0 إن سلمت الحالات كلها، و1 مع قائمة الأخطاء إن لم تسلم، و2 لخطأ في الاستدعاء أو المصدر.
"""
import hashlib
import json
import re
import sys

HERE = "/tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/fa/mujallad"
CASES = sys.argv[1] if len(sys.argv) > 1 else HERE + "/cases.json"
SOURCE = sys.argv[2] if len(sys.argv) > 2 else "/home/claude/mudaa_dir/sibawayhi.txt"
SOURCE_SHA = "a160f940bb194e6fe7e6655d2c7f28e41f1fc648c4c5e340cc4e42306d5cb625"
LO, HI = 8914, 9049

FIA = ["موجب", "حد", "خارج", "عموم", "غموض"]
QUOTA = {"موجب": 8, "حد": 6, "خارج": 5, "عموم": 4, "غموض": 3}
SADR = {"واجب", "نفي_بلم", "نفي_بما_مضارع", "نفي_بما_ماض", "نفي_بلا", "نفي_اسمي", "نهي",
        "أمر", "استفهام", "عرض", "تمن", "ظن", "تشبيه_بنفي", "دعاء"}
MANA = {"سبب", "شركة", "قطع", "غير_معلن"}
IRAB = {"نصب", "رفع", "جزم"}
HUKM = {"مقبول", "ضعيف", "قبيح", "خطأ", "لا_حكم"}
SHIR_EXTRA = {"غير_مسؤول"}
RADD = {"ضعيف", "قبيح", "خطأ"}
KEYS = {"id", "fia", "mithal", "mithal_harfi", "dakhil", "kharij", "sanad", "taliq"}
TASHKIL = re.compile("[ً-ْٰ]")


def strip_prefix(line):
    if line.startswith("~~"):
        return line[2:]
    if line.startswith("# "):
        return line[2:]
    return line


def main():
    try:
        raw = open(SOURCE, "rb").read()
    except OSError as e:
        print("لا يُقرأ المصدر:", e)
        return 2
    if hashlib.sha256(raw).hexdigest() != SOURCE_SHA:
        print("بصمة المصدر لا تطابق المواصفة")
        return 2
    lines = raw.decode("utf-8").split("\n")
    # lines[i] هو السطر رقم i+1
    def satr(n):
        return strip_prefix(lines[n - 1].rstrip("\r"))

    errs = []
    try:
        data = json.loads(open(CASES, "rb").read().decode("utf-8"))
    except (OSError, ValueError, UnicodeDecodeError) as e:
        print("JSON غير صالح:", e)
        return 1
    if not isinstance(data, list):
        print("الملف ليس قائمة")
        return 1

    ids = set()
    dakhils = {}
    count = {f: 0 for f in FIA}
    for i, c in enumerate(data):
        where = "#%d" % i
        if not isinstance(c, dict):
            errs.append(where + ": ليس كائنًا")
            continue
        cid = c.get("id")
        where = str(cid)
        if set(c.keys()) != KEYS:
            errs.append(where + ": المفاتيح %s" % sorted(set(c.keys()) ^ KEYS))
            continue
        if not isinstance(cid, str) or not re.fullmatch(r"F\d{2}", cid):
            errs.append(where + ": id غير صالح")
        elif cid in ids:
            errs.append(where + ": id مكرَّر")
        ids.add(cid)

        fia = c["fia"]
        if fia not in FIA:
            errs.append(where + ": fia غير مسموحة")
        else:
            count[fia] += 1

        m = c["mithal"]
        if not isinstance(m, str) or not m.strip() or "\n" in m:
            errs.append(where + ": mithal فارغ أو متعدّد الأسطر")
        elif TASHKIL.search(m):
            errs.append(where + ": mithal فيه تشكيل")
        if not isinstance(c["mithal_harfi"], bool):
            errs.append(where + ": mithal_harfi ليس بوليًّا")

        d = c["dakhil"]
        if not isinstance(d, dict) or set(d.keys()) != {"sadr", "mana", "irab"}:
            errs.append(where + ": dakhil مفاتيحه غير صحيحة")
            continue
        if d["sadr"] not in SADR:
            errs.append(where + ": sadr غير مسموح")
        if d["mana"] not in MANA:
            errs.append(where + ": mana غير مسموح")
        if d["irab"] not in IRAB:
            errs.append(where + ": irab غير مسموح")
        key = (d["sadr"], d["mana"], d["irab"])
        if key in dakhils:
            errs.append(where + ": dakhil مكرَّر مع " + str(dakhils[key]))
        dakhils.setdefault(key, cid)

        k = c["kharij"]
        if not isinstance(k, dict) or set(k.keys()) != {"kalam", "shir"}:
            errs.append(where + ": kharij مفاتيحه غير صحيحة")
            continue
        has_list = False
        vals = []
        for fld, allowed in (("kalam", HUKM), ("shir", HUKM | SHIR_EXTRA)):
            v = k[fld]
            if isinstance(v, list):
                has_list = True
                if fia != "غموض":
                    errs.append(where + ": قائمة في %s خارج فئة غموض" % fld)
                if (len(v) != 2 or len(set(v)) != 2
                        or not all(isinstance(x, str) and x in HUKM and x != "لا_حكم" for x in v)):
                    errs.append(where + ": قائمة %s ليست بديلين مختلفين من المسموح" % fld)
                vals.extend(v if isinstance(v, list) else [])
            elif isinstance(v, str) and v in allowed:
                vals.append(v)
            else:
                errs.append(where + ": قيمة %s غير مسموحة" % fld)
        if fia == "غموض" and not has_list:
            errs.append(where + ": غموض بلا قائمة بديلين")

        kalam, shir = k["kalam"], k["shir"]
        la_hukm = (kalam == "لا_حكم" and shir in ("لا_حكم", "غير_مسؤول"))
        if fia == "خارج" and not la_hukm:
            errs.append(where + ": خارج ومتوقَّعه ليس لا_حكم")
        if fia == "موجب" and "مقبول" not in vals:
            errs.append(where + ": موجب بلا مقبول")
        if fia == "حد" and not (RADD & set(vals)):
            errs.append(where + ": حد بلا رد أو تضعيف أو تقبيح")

        s = c["sanad"]
        if not isinstance(s, list):
            errs.append(where + ": sanad ليس قائمة")
            continue
        if la_hukm and s:
            errs.append(where + ": لا_حكم وله سند")
        if not la_hukm and not s:
            errs.append(where + ": حكمٌ بلا سند")
        sanad_lines = []
        for p in s:
            if not isinstance(p, dict) or set(p.keys()) != {"satr", "nass"}:
                errs.append(where + ": قطعة سند مفاتيحها غير صحيحة")
                continue
            n, t = p["satr"], p["nass"]
            if not isinstance(n, int) or isinstance(n, bool) or not (LO <= n <= HI):
                errs.append(where + ": satr %r خارج النطاق" % (n,))
                continue
            if not isinstance(t, str) or not t or "\n" in t:
                errs.append(where + ": nass فارغ أو يعبر سطرًا")
                continue
            full = satr(n)
            if t not in full:
                errs.append(where + ": nass ليس في السطر %d: %s" % (n, t))
            sanad_lines.append(full)
        if c["mithal_harfi"] is True and isinstance(m, str):
            if not any(m in full for full in sanad_lines):
                errs.append(where + ": mithal_harfi=true والمثال ليس في سطر من أسطر السند")

        tq = c["taliq"]
        if not isinstance(tq, str) or not tq.strip() or "\n" in tq:
            errs.append(where + ": taliq فارغ أو متعدّد الأسطر")

    n = len(data)
    if not (30 <= n <= 40):
        errs.append("عدد الحالات %d خارج 30–40" % n)
    for f, q in QUOTA.items():
        if count[f] < q:
            errs.append("فئة %s: %d أقل من %d" % (f, count[f], q))

    if errs:
        for e in errs:
            print("خطأ:", e)
        print("مرفوض: %d خطأ" % len(errs))
        return 1
    print("سليم: %d حالة؛ %s" % (n, "، ".join("%s %d" % (f, count[f]) for f in FIA)))
    print("حرفي: %d" % sum(1 for c in data if c["mithal_harfi"] is True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
