#!/usr/bin/env python3
"""فاحص cases.json لضابط «الوقف في أواخر الكلم المتحركة في الوصل» على المواصفة wasf.md.

الاستعمال:  python3 -I fahs_cases.py [cases.json] [sibawayhi.txt]
يخرج 0 إن مرّ كلُّ فحص، و1 إن وُجد خلل (ويطبع كلَّ خلل)، و2 إن تعذّرت القراءة.
"""
import hashlib
import json
import os
import re
import sys

HUNA = os.path.dirname(os.path.abspath(__file__))
CASES = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HUNA, "cases.json")
SOURCE = sys.argv[2] if len(sys.argv) > 2 else "/home/claude/mudaa_dir/sibawayhi.txt"

BASMA_MASDAR = "a160f940bb194e6fe7e6655d2c7f28e41f1fc648c4c5e340cc4e42306d5cb625"
NITAQ = (17782, 17859)
ADAD = (25, 40)
HADD_ADNA = {"موجب": 8, "حد": 5, "خارج": 4, "عموم": 3, "غموض": 0}

FIAT = set(HADD_ADNA)
AKHIR = {"حرف_صحيح", "هاء_تأنيث", "تاء_جمع", "تاء_ملحقة", "ياء_قبلها_كسرة"}
TANWIN = {"منون", "غير_منون"}
QABL = {"متحرك", "ساكن"}
HARAKA = {"رفع_أو_ضم", "نصب_أو_فتح", "جر_أو_كسر"}
WAJH = {"ألف", "واو_أو_ياء", "إسكان", "إشمام", "روم", "تضعيف", "هاء", "تاء", "حذف_الياء", "إثبات_الياء"}
QIYAM_KALAM = {"مقبول", "لغة", "خطأ", "لا_حكم"}
QIYAM_SHIR = QIYAM_KALAM | {"غير_مسؤول"}
LA = {"لا_حكم", "غير_مسؤول"}

MAFATIH = {"id", "fia", "mithal", "mithal_harfi", "dakhil", "kharij", "sanad", "taliq"}
MAFATIH_DAKHIL = {"akhir", "tanwin", "qabl_akhir", "haraka", "wajh"}
MAFATIH_KHARIJ = {"kalam", "shir"}
TASHKIL = re.compile("[ً-ْٰ]")

khalal = []


def khata(cid, nass):
    khalal.append(f"{cid}: {nass}")


def qiyam_haql(cid, ism, q, masmuh, fia):
    """القيمة واحدةٌ من المسموح، أو قائمةُ بديلين مختلفين في «غموض» وحدها."""
    if isinstance(q, list):
        if fia != "غموض":
            khata(cid, f"{ism}: قائمةٌ في غير فئة غموض")
            return []
        if len(q) != 2 or len(set(q)) != 2:
            khata(cid, f"{ism}: قائمةُ غموض ليست بديلين مختلفين: {q}")
        for x in q:
            if not isinstance(x, str) or x not in masmuh:
                khata(cid, f"{ism}: قيمةٌ غير مسموحة في القائمة: {x!r}")
        return [x for x in q if isinstance(x, str)]
    if not isinstance(q, str) or q not in masmuh:
        khata(cid, f"{ism}: قيمةٌ غير مسموحة: {q!r}")
        return []
    return [q]


def main():
    try:
        masdar = open(SOURCE, "rb").read()
    except OSError as e:
        print(f"تعذّرت قراءة المصدر: {e}")
        return 2
    basma = hashlib.sha256(masdar).hexdigest()
    if basma != BASMA_MASDAR:
        khata("المصدر", f"البصمة {basma} غير بصمة المواصفة")
    asttur = masdar.split(b"\n")

    def satr_mujarrad(n):
        b = asttur[n - 1]
        if b.startswith(b"~~"):
            return b[2:]
        if b.startswith(b"# "):
            return b[2:]
        return b

    try:
        with open(CASES, "rb") as f:
            kham = f.read()
        kham.decode("utf-8")
        halat = json.loads(kham)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
        print(f"ملفّ الحالات غير صالح: {e}")
        return 1

    if not isinstance(halat, list):
        print("ملفّ الحالات ليس قائمة")
        return 1

    ids = set()
    dakhilat = {}
    adad_fia = {f: 0 for f in FIAT}

    for i, h in enumerate(halat):
        cid = h.get("id", f"#{i}") if isinstance(h, dict) else f"#{i}"
        if not isinstance(h, dict):
            khata(cid, "العنصر ليس كائنًا")
            continue
        if set(h) != MAFATIH:
            khata(cid, f"المفاتيح {sorted(h)} غير المطلوبة")
            continue
        if not isinstance(cid, str) or not re.fullmatch(r"W\d\d", cid):
            khata(cid, "id ليس «W» ورقمًا من خانتين")
        if cid in ids:
            khata(cid, "id مكرَّر")
        ids.add(cid)

        fia = h["fia"]
        if fia not in FIAT:
            khata(cid, f"فئةٌ غير مسموحة: {fia!r}")
            continue
        adad_fia[fia] += 1

        mithal = h["mithal"]
        if not isinstance(mithal, str) or not mithal.strip():
            khata(cid, "mithal فارغ")
            mithal = ""
        elif TASHKIL.search(mithal):
            khata(cid, "mithal مشكول")
        if not isinstance(h["mithal_harfi"], bool):
            khata(cid, "mithal_harfi ليس بوليانيًّا")

        d = h["dakhil"]
        if not isinstance(d, dict) or set(d) != MAFATIH_DAKHIL:
            khata(cid, "dakhil بمفاتيح غير المطلوبة")
            continue
        for ism, masmuh in (("akhir", AKHIR), ("tanwin", TANWIN), ("qabl_akhir", QABL),
                            ("haraka", HARAKA), ("wajh", WAJH)):
            if d[ism] not in masmuh:
                khata(cid, f"dakhil.{ism}: قيمةٌ غير مسموحة: {d[ism]!r}")
        mif = tuple(d[k] for k in sorted(MAFATIH_DAKHIL))
        if mif in dakhilat:
            khata(cid, f"المدخل نفسُه في {dakhilat[mif]}")
        else:
            dakhilat[mif] = cid

        k = h["kharij"]
        if not isinstance(k, dict) or set(k) != MAFATIH_KHARIJ:
            khata(cid, "kharij بمفاتيح غير المطلوبة")
            continue
        kalam = qiyam_haql(cid, "kalam", k["kalam"], QIYAM_KALAM, fia)
        shir = qiyam_haql(cid, "shir", k["shir"], QIYAM_SHIR, fia)
        if fia == "غموض" and not (isinstance(k["kalam"], list) or isinstance(k["shir"], list)):
            khata(cid, "غموض بلا قائمةِ بديلين")

        kullu_la = all(x in LA for x in kalam + shir) and bool(kalam)
        sanad = h["sanad"]
        if not isinstance(sanad, list):
            khata(cid, "sanad ليس قائمة")
            sanad = []

        # الفئة والحكم
        if fia == "خارج":
            if kalam != ["لا_حكم"] or not all(x in LA for x in shir):
                khata(cid, "خارج وحكمُه غيرُ «لا_حكم»")
        else:
            if "لا_حكم" in kalam and fia != "غموض":
                khata(cid, "«لا_حكم» في الكلام في غير خارج")
        if fia == "حد" and kalam != ["خطأ"]:
            khata(cid, "حد وحكمُ الكلام غيرُ «خطأ»")
        if fia == "موجب" and not set(kalam) <= {"مقبول", "لغة"}:
            khata(cid, "موجب وحكمُ الكلام غيرُ مقبول ولا لغة")

        # السند
        if kullu_la:
            if sanad:
                khata(cid, "حالة «لا_حكم» لها سند")
        elif not sanad:
            khata(cid, "حكمٌ بلا سند")
        asttur_sanad = []
        for j, s in enumerate(sanad):
            if not isinstance(s, dict) or set(s) != {"satr", "nass"}:
                khata(cid, f"قطعة السند {j} بمفاتيح غير المطلوبة")
                continue
            n, nass = s["satr"], s["nass"]
            if not isinstance(n, int) or isinstance(n, bool):
                khata(cid, f"قطعة السند {j}: satr ليس عددًا صحيحًا")
                continue
            if not (NITAQ[0] <= n <= NITAQ[1]):
                khata(cid, f"قطعة السند {j}: السطر {n} خارج النطاق")
                continue
            if not isinstance(nass, str) or not nass.strip():
                khata(cid, f"قطعة السند {j}: nass فارغ")
                continue
            if "\n" in nass or "\r" in nass:
                khata(cid, f"قطعة السند {j}: nass يعبر سطرين")
                continue
            satr = satr_mujarrad(n)
            if nass.encode("utf-8") not in satr:
                khata(cid, f"قطعة السند {j}: nass ليس قطعةً حرفيّةً من السطر {n}")
            asttur_sanad.append(asttur[n - 1].decode("utf-8"))

        # المثال الحرفيّ
        if mithal and isinstance(h["mithal_harfi"], bool):
            fihi = any(mithal in t for t in asttur_sanad)
            if h["mithal_harfi"] and not fihi:
                khata(cid, "mithal_harfi=true والمثال ليس في سطرٍ من أسطر السند")
            if not h["mithal_harfi"] and fihi:
                khata(cid, "mithal_harfi=false والمثال بحروفه في سطرٍ من أسطر السند")

        t = h["taliq"]
        if not isinstance(t, str) or not t.strip() or "\n" in t or "\r" in t:
            khata(cid, "taliq ليس سطرًا واحدًا غير فارغ")

    if not (ADAD[0] <= len(halat) <= ADAD[1]):
        khata("العدد", f"{len(halat)} خارج {ADAD[0]}–{ADAD[1]}")
    for f, adna in HADD_ADNA.items():
        if adad_fia[f] < adna:
            khata("الحصص", f"{f} {adad_fia[f]} دون {adna}")

    print(f"الحالات: {len(halat)}؛ " + "، ".join(f"{f} {adad_fia[f]}" for f in
          ("موجب", "حد", "خارج", "عموم", "غموض")))
    print("حرفيّة: " + str(sum(1 for h in halat if isinstance(h, dict) and h.get("mithal_harfi") is True)))
    if khalal:
        print(f"خلل ({len(khalal)}):")
        for x in khalal:
            print("  " + x)
        return 1
    print("سليم")
    return 0


if __name__ == "__main__":
    sys.exit(main())
