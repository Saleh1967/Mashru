# -*- coding: utf-8 -*-
"""فاحصُ ملفّ الحالات قبل التجميد (ضابط أبنية اسمَي الفاعل والمفعول).

الاستعمال: python3 -I fahs_cases.py <cases.json> <مجلّد المصدرين>
يخرج 0 إن مرّ كلُّ فحص، و1 مع قائمة الأخطاء إن لم يمرّ.
"""
import hashlib
import json
import os
import re
import sys

BASAMAT = {
    "alfiyya.txt": "13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0",
    "qatr.txt": "2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d",
}
MASDAR_MILAF = {"ألفية": "alfiyya.txt", "قطر": "qatr.txt"}
NITAQ = {"ألفية": set(range(594, 608)), "قطر": {358, 365}}
# من سطرَي القطر: الصوغُ وحده في النطاق (المواصفة)، فالقطعةُ داخلَ هذين المقطعين
QATR_MAQTA = {358: "واسم الفاعل كضارب ومكرم", 365: "واسم المفعول، كمضروب ومكرم"}

FIAT = ["موجب", "حد", "خارج", "عموم", "غموض"]
FIL = ["فعل_مفتوح_العين", "فعل_مكسور_العين", "فعل_مضموم_العين", "غير_ثلاثي"]
TAADDI = ["متعد", "لازم"]
MATLUB = ["اسم_فاعل", "اسم_مفعول"]
SIGHA = ["فاعل", "فعل_مكسور_العين", "أفعل", "فعلان", "فعل_ساكن_العين", "فعيل",
         "فعل_مفتوح_العين", "مفعول", "مضارع_بميم_مكسور", "مضارع_بميم_مفتوح"]
HUKM = ["مقبول", "خطأ", "لا_حكم"]
DARAJAT_MAQBUL = ["قياس", "أولى", "قليل", "نقل", "بلا_درجة"]
MAFATIH = ["id", "fia", "mithal", "mithal_harfi", "dakhil", "hukm", "daraja", "zawj", "sanad", "taliq"]
HUQUL = ["fil", "taaddi", "matlub", "sigha"]
HADD_ADNA = {"موجب": 12, "حد": 10, "خارج": 5, "عموم": 4, "غموض": 2}
HARAKAT = re.compile("[ً-ٰٟ]")
BADIAT = ("### | ", "~~", "# ")


def jarrid(satr):
    for b in BADIAT:
        if satr.startswith(b):
            return satr[len(b):]
    return satr


def main(argv):
    if len(argv) != 3:
        print("الاستعمال: python3 -I fahs_cases.py <cases.json> <مجلّد المصدرين>")
        return 2
    akhta = []
    masar_cases, majallad = argv[1], argv[2]

    # بصمتا المصدرين
    asatr = {}
    for masdar, milaf in MASDAR_MILAF.items():
        p = os.path.join(majallad, milaf)
        try:
            b = open(p, "rb").read()
        except OSError as e:
            akhta.append("لا يُقرأ %s: %s" % (p, e))
            continue
        h = hashlib.sha256(b).hexdigest()
        if h != BASAMAT[milaf]:
            akhta.append("بصمة %s %s لا تطابق المواصفة %s" % (milaf, h, BASAMAT[milaf]))
        L = b.decode("utf-8").split("\n")
        asatr[masdar] = L
    if akhta:
        return natija(akhta)

    try:
        raw = open(masar_cases, "rb").read()
        data = json.loads(raw.decode("utf-8"))
    except Exception as e:  # JSON غير صالح أو ترميز غير UTF-8
        return natija(["JSON غير صالح: %s" % e])
    if not isinstance(data, list):
        return natija(["الملفّ ليس قائمة"])

    ids = {}
    for k, h in enumerate(data):
        w = "عنصر %d" % k
        if not isinstance(h, dict):
            akhta.append("%s ليس كائنًا" % w)
            continue
        if sorted(h.keys()) != sorted(MAFATIH):
            akhta.append("%s مفاتيحه %s" % (w, sorted(h.keys())))
            continue
        i = h["id"]
        if not isinstance(i, str) or not re.fullmatch(r"B\d{2}", i):
            akhta.append("%s: id غير صالح %r" % (w, i))
            continue
        if i in ids:
            akhta.append("id مكرّر %s" % i)
        ids[i] = h
    if akhta:
        return natija(akhta)

    for i, h in ids.items():
        fia = h["fia"]
        if fia not in FIAT:
            akhta.append("%s: fia غير مسموحة %r" % (i, fia))
        d = h["dakhil"]
        if not isinstance(d, dict) or sorted(d.keys()) != sorted(HUQUL):
            akhta.append("%s: dakhil حقوله غير الأربعة" % i)
        else:
            for haql, masmuh in (("fil", FIL), ("taaddi", TAADDI), ("matlub", MATLUB), ("sigha", SIGHA)):
                if d[haql] not in masmuh:
                    akhta.append("%s: %s غير مسموح %r" % (i, haql, d[haql]))
        # الحكم والدرجة
        hk, dr = h["hukm"], h["daraja"]
        if fia == "غموض":
            if isinstance(hk, list):
                if len(hk) != 2 or len(set(hk)) != 2 or any(x not in HUKM for x in hk):
                    akhta.append("%s: hukm القائمة غير صالحة %r" % (i, hk))
                elif not isinstance(dr, list) or len(dr) != 2:
                    akhta.append("%s: daraja يجب أن تكون قائمةً موازيةً لـhukm" % i)
                else:
                    for x, y in zip(hk, dr):
                        if x == "مقبول" and y not in DARAJAT_MAQBUL:
                            akhta.append("%s: درجة غير مسموحة %r" % (i, y))
                        if x != "مقبول" and y != "بلا_درجة":
                            akhta.append("%s: درجةٌ لغير المقبول %r" % (i, y))
            elif hk == "مقبول":
                if (not isinstance(dr, list) or len(dr) != 2 or len(set(dr)) != 2
                        or any(y not in DARAJAT_MAQBUL for y in dr)):
                    akhta.append("%s: غموضٌ بحكمٍ واحد يحتاج قائمةَ درجتين" % i)
            else:
                akhta.append("%s: غموضٌ بلا بديلين" % i)
        else:
            if fia == "موجب" and hk != "مقبول":
                akhta.append("%s: موجب حكمُه %r" % (i, hk))
            if fia == "حد" and hk != "خطأ":
                akhta.append("%s: حد حكمُه %r" % (i, hk))
            if fia == "خارج" and hk != "لا_حكم":
                akhta.append("%s: خارج حكمُه %r" % (i, hk))
            if fia == "عموم" and hk not in ("مقبول", "خطأ"):
                akhta.append("%s: عموم حكمُه %r" % (i, hk))
            if hk not in HUKM:
                akhta.append("%s: hukm غير مسموح %r" % (i, hk))
            elif hk == "مقبول":
                if dr not in DARAJAT_MAQBUL:
                    akhta.append("%s: daraja غير مسموحة %r" % (i, dr))
            elif dr != "بلا_درجة":
                akhta.append("%s: daraja لغير المقبول يجب بلا_درجة، وهي %r" % (i, dr))
        # المثال
        m = h["mithal"]
        if not isinstance(m, str) or not m.strip():
            akhta.append("%s: mithal فارغ" % i)
        elif HARAKAT.search(m):
            akhta.append("%s: mithal فيه تشكيل" % i)
        if not isinstance(h["mithal_harfi"], bool):
            akhta.append("%s: mithal_harfi ليست منطقيّة" % i)
        t = h["taliq"]
        if not isinstance(t, str) or not t.strip() or "\n" in t or "\r" in t:
            akhta.append("%s: taliq ليس سطرًا واحدًا" % i)
        # السند
        sanad = h["sanad"]
        if not isinstance(sanad, list):
            akhta.append("%s: sanad ليس قائمة" % i)
            continue
        la_hukm = (hk == "لا_حكم")
        if la_hukm and sanad:
            akhta.append("%s: لا_حكم وله سند" % i)
        if not la_hukm and not sanad:
            akhta.append("%s: حكمٌ بلا سند" % i)
        nusus_kamila = []
        for s in sanad:
            if not isinstance(s, dict) or sorted(s.keys()) != ["masdar", "nass", "satr"]:
                akhta.append("%s: قطعة سند حقولها غير masdar/satr/nass" % i)
                continue
            ms, sr, ns = s["masdar"], s["satr"], s["nass"]
            if ms not in MASDAR_MILAF:
                akhta.append("%s: masdar غير مسموح %r" % (i, ms))
                continue
            if not isinstance(sr, int) or isinstance(sr, bool):
                akhta.append("%s: satr ليس عددًا %r" % (i, sr))
                continue
            if sr not in NITAQ[ms]:
                akhta.append("%s: السطر %s %d خارج النطاق" % (i, ms, sr))
                continue
            if not isinstance(ns, str) or not ns or "\n" in ns:
                akhta.append("%s: nass فارغ أو يعبر سطرين" % i)
                continue
            kamil = jarrid(asatr[ms][sr - 1])
            if ns.encode("utf-8") not in kamil.encode("utf-8"):
                akhta.append("%s: nass ليس قطعةً من %s %d: %r" % (i, ms, sr, ns))
            if ms == "قطر" and ns not in QATR_MAQTA[sr]:
                akhta.append("%s: nass من القطر خارج مقطع الصوغ %d" % (i, sr))
            nusus_kamila.append(kamil)
        if isinstance(m, str) and isinstance(h["mithal_harfi"], bool):
            fiha = any(m in k for k in nusus_kamila)
            if h["mithal_harfi"] and not fiha:
                akhta.append("%s: mithal_harfi=true والمثال ليس في أسطر السند" % i)
            if not h["mithal_harfi"] and fiha:
                akhta.append("%s: mithal_harfi=false والمثال بحروفه في أسطر السند" % i)

    # الأزواج
    azwaj = 0
    for i, h in ids.items():
        z = h["zawj"]
        if z is None:
            continue
        if not isinstance(z, str) or z not in ids or z == i:
            akhta.append("%s: zawj غير صالح %r" % (i, z))
            continue
        o = ids[z]
        if o["zawj"] != i:
            akhta.append("%s: الزوج %s غير متبادل" % (i, z))
            continue
        if isinstance(h["dakhil"], dict) and isinstance(o["dakhil"], dict):
            farq = [k for k in HUQUL if h["dakhil"].get(k) != o["dakhil"].get(k)]
            if len(farq) != 1:
                akhta.append("%s/%s: يختلفان في %d حقل" % (i, z, len(farq)))
        if h["hukm"] == o["hukm"] and h["daraja"] == o["daraja"]:
            akhta.append("%s/%s: الحكم والدرجة سواء" % (i, z))
        azwaj += 1
    azwaj //= 2

    # المدخلات المكرّرة
    dakhilat = {}
    for i, h in ids.items():
        d = h["dakhil"]
        if isinstance(d, dict):
            key = tuple(d.get(k) for k in HUQUL)
            if key in dakhilat:
                akhta.append("%s و%s بالمدخل نفسه" % (dakhilat[key], i))
            dakhilat[key] = i

    # الأعداد
    n = len(ids)
    if not 40 <= n <= 55:
        akhta.append("العدد %d خارج 40–55" % n)
    for f, adna in HADD_ADNA.items():
        k = sum(1 for h in ids.values() if h["fia"] == f)
        if k < adna:
            akhta.append("الفئة %s: %d < %d" % (f, k, adna))
    for haql, qiyam, adna in (("sigha", SIGHA, 3), ("fil", FIL, 6), ("matlub", MATLUB, 10), ("taaddi", TAADDI, 8)):
        for v in qiyam:
            k = sum(1 for h in ids.values() if isinstance(h["dakhil"], dict) and h["dakhil"].get(haql) == v)
            if k < adna:
                akhta.append("%s=%s: %d < %d" % (haql, v, k, adna))
    for dr in ("قياس", "أولى", "قليل", "نقل"):
        k = sum(1 for h in ids.values() if h["hukm"] == "مقبول" and h["daraja"] == dr)
        if k < 1:
            akhta.append("الدرجة %s لا حالةَ لها" % dr)
    if azwaj < 8:
        akhta.append("الأزواج %d < 8" % azwaj)

    if not akhta:
        ihsa = {f: sum(1 for h in ids.values() if h["fia"] == f) for f in FIAT}
        harfi = sum(1 for h in ids.values() if h["mithal_harfi"])
        print("مرّ: %d حالة، %s، حرفيّ %d، أزواج %d" % (n, ihsa, harfi, azwaj))
    return natija(akhta)


def natija(akhta):
    if akhta:
        for a in akhta:
            print("خطأ:", a)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
