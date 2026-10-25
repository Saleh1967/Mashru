#!/usr/bin/env python3
"""فاحص ملفّ الحالات لضابط «نفي الفعل» على المواصفة wasf.md.

الاستعمال:
    python3 -I fahs_cases.py [cases.json] [sibawayhi.txt]

يخرج 0 إن مرّ كلّ فحص، و1 إن وُجد خلل (ويطبع كلّ خللٍ باسمه)، و2 إن تعذّرت قراءة المدخلات.
"""
import hashlib
import json
import os
import re
import sys

HUNA = os.path.dirname(os.path.abspath(__file__))
MASDAR_IFTIRADI = "/home/claude/mudaa_dir/sibawayhi.txt"
BASMA_MASDAR = "a160f940bb194e6fe7e6655d2c7f28e41f1fc648c4c5e340cc4e42306d5cb625"
NITAQ = (9755, 9787)

NAW = {"نفي", "ولي"}
FIA = {"موجب", "حد", "خارج", "عموم", "غموض"}
JIHA = {"نفي", "إثبات"}
HAL = {"حال", "غير_واقع", "غير_معلن"}
SIYAQ = {"قسم", "جواب_هل", "غير_معلن"}
YALI = {"فعل", "اسم_ثم_فعل", "اسم"}
HUKM_KALAM = {"مقبول", "مرجوح", "قبيح", "خطأ", "لا_حكم"}
HUKM_SHIR = HUKM_KALAM | {"غير_مسؤول"}
LA_HUKM = "لا_حكم"
GHAYR_MASUL = "غير_مسؤول"

HUDUD = {"kull": (18, 30), "نفي": 12, "ولي": 4,
         "موجب": 6, "حد": 3, "خارج": 3, "عموم": 2, "غموض": 2}

MAFATIH = {"id", "naw", "fia", "mithal", "mithal_harfi", "dakhil", "kharij", "sanad", "taliq"}
DAKHIL_NAFY = {"jiha", "sura", "hal", "siyaq"}
DAKHIL_WALY = {"harf", "yali"}

TASHKIL = re.compile("[ً-ْٰـ]")  # الحركات والتنوين والشدّة والسكون والألف الخنجرية والتطويل
MUDARI_MUJARRAD = re.compile("^[أتني]فعل$")
TARMIZ = re.compile(r"PageV\d+P\d+|ms\d+|%")


def iqra_masdar(masar):
    b = open(masar, "rb").read()
    basma = hashlib.sha256(b).hexdigest()
    asatir = b.split(b"\n")
    return basma, asatir


def jarrid(satr_b):
    """يحذف بادئة السطر «~~» أو «# » وحدها، ويردّ النصّ بايتاتٍ."""
    if satr_b.startswith(b"~~"):
        return satr_b[2:]
    if satr_b.startswith(b"# "):
        return satr_b[2:]
    return satr_b


def sawwi(nass):
    """يحذف ترميز OpenITI (علامات الشطر % ومعلّمات الصفحة والمخطوط) ويوحّد البياض — لفحص المثال الحرفيّ وحده."""
    return re.sub(r"\s+", " ", TARMIZ.sub(" ", nass)).strip()


def fahs(masar_halat, masar_masdar):
    akhta = []

    def khata(hala_id, rasala):
        akhta.append(f"[{hala_id}] {rasala}")

    # --- المصدر
    try:
        basma, asatir = iqra_masdar(masar_masdar)
    except OSError as e:
        print(f"تعذّرت قراءة المصدر: {e}")
        return 2
    if basma != BASMA_MASDAR:
        akhta.append(f"[المصدر] بصمته {basma} لا تطابق بصمة المواصفة")

    # --- الحالات: UTF-8 وJSON
    try:
        kham = open(masar_halat, "rb").read()
    except OSError as e:
        print(f"تعذّرت قراءة الحالات: {e}")
        return 2
    try:
        nass_halat = kham.decode("utf-8")
    except UnicodeDecodeError as e:
        print(f"[الملفّ] ليس UTF-8: {e}")
        return 1
    try:
        halat = json.loads(nass_halat)
    except json.JSONDecodeError as e:
        print(f"[الملفّ] ليس JSON صالحًا: {e}")
        return 1
    if not isinstance(halat, list):
        print("[الملفّ] ليس قائمة JSON")
        return 1

    ids = set()
    dakhil_mara = {}
    add = {"نفي": 0, "ولي": 0, "موجب": 0, "حد": 0, "خارج": 0, "عموم": 0, "غموض": 0}

    for i, h in enumerate(halat):
        hid = h.get("id", f"#{i}") if isinstance(h, dict) else f"#{i}"
        if not isinstance(h, dict):
            khata(hid, "العنصر ليس كائنًا")
            continue
        if set(h.keys()) != MAFATIH:
            khata(hid, f"المفاتيح {sorted(h.keys())} غير المطلوبة {sorted(MAFATIH)}")
            continue

        # id
        if not (isinstance(h["id"], str) and re.fullmatch(r"N\d{2}", h["id"])):
            khata(hid, "id ليس «N» ورقمًا من خانتين")
        if h["id"] in ids:
            khata(hid, "id مكرّر")
        ids.add(h["id"])

        naw, fia = h["naw"], h["fia"]
        if naw not in NAW:
            khata(hid, f"naw غير مسموح: {naw}")
            continue
        if fia not in FIA:
            khata(hid, f"fia غير مسموح: {fia}")
            continue
        add[naw] += 1
        add[fia] += 1

        # mithal
        if not (isinstance(h["mithal"], str) and h["mithal"].strip()):
            khata(hid, "mithal فارغ أو ليس نصًّا")
        elif TASHKIL.search(h["mithal"]):
            khata(hid, "mithal فيه تشكيل")
        if not isinstance(h["mithal_harfi"], bool):
            khata(hid, "mithal_harfi ليس منطقيًّا")

        # taliq
        if not (isinstance(h["taliq"], str) and h["taliq"].strip()):
            khata(hid, "taliq فارغ")
        elif "\n" in h["taliq"] or "\r" in h["taliq"]:
            khata(hid, "taliq أكثر من سطر")

        d, k = h["dakhil"], h["kharij"]
        if not isinstance(d, dict) or not isinstance(k, dict):
            khata(hid, "dakhil أو kharij ليس كائنًا")
            continue

        la_hukm = None  # هل جواب الحالة «لا حكم» كلّه

        if naw == "نفي":
            if set(d.keys()) != DAKHIL_NAFY:
                khata(hid, f"مفاتيح dakhil {sorted(d.keys())}")
                continue
            if d["jiha"] not in JIHA:
                khata(hid, f"jiha غير مسموحة: {d['jiha']}")
            if d["hal"] not in HAL:
                khata(hid, f"hal غير مسموحة: {d['hal']}")
            if d["siyaq"] not in SIYAQ:
                khata(hid, f"siyaq غير مسموح: {d['siyaq']}")
            sura = d["sura"]
            if not (isinstance(sura, str) and sura.strip()):
                khata(hid, "sura فارغة")
            else:
                if TASHKIL.search(sura):
                    khata(hid, "sura فيها تشكيل")
                if "فعل" not in sura:
                    khata(hid, "sura ليست بلفظ «فعل»")
                if d["hal"] != "غير_معلن" and not MUDARI_MUJARRAD.match(sura):
                    khata(hid, "hal غير «غير_معلن» لصورةٍ ليست مضارعًا مجرّدًا")
            if set(k.keys()) != {"suwar"}:
                khata(hid, f"مفاتيح kharij {sorted(k.keys())}")
                continue
            suwar = k["suwar"]
            if suwar == LA_HUKM:
                la_hukm = True
                if fia != "خارج":
                    khata(hid, "«لا_حكم» في فئةٍ غير «خارج»")
            elif isinstance(suwar, list):
                la_hukm = False
                if fia == "خارج":
                    khata(hid, "فئة «خارج» ومتوقّعها ليس «لا_حكم»")
                if not suwar:
                    khata(hid, "suwar قائمة فارغة")
                if not all(isinstance(s, str) and s.strip() for s in suwar):
                    khata(hid, "في suwar عنصرٌ ليس نصًّا غير فارغ")
                else:
                    if len(set(suwar)) != len(suwar):
                        khata(hid, "suwar فيها تكرار")
                    for s in suwar:
                        if TASHKIL.search(s):
                            khata(hid, f"صورة فيها تشكيل: {s}")
                        if "فعل" not in s:
                            khata(hid, f"صورة ليست بلفظ «فعل»: {s}")
                        if s == LA_HUKM:
                            khata(hid, "«لا_حكم» داخل قائمة")
                if fia == "غموض" and len(suwar) < 2:
                    khata(hid, "«غموض» بأقلّ من بديلين")
            else:
                khata(hid, "suwar ليست قائمةً ولا «لا_حكم»")
        else:  # ولي
            if set(d.keys()) != DAKHIL_WALY:
                khata(hid, f"مفاتيح dakhil {sorted(d.keys())}")
                continue
            harf = d["harf"]
            if not (isinstance(harf, str) and harf.strip()):
                khata(hid, "harf فارغ")
            elif TASHKIL.search(harf):
                khata(hid, "harf فيه تشكيل")
            if d["yali"] not in YALI:
                khata(hid, f"yali غير مسموح: {d['yali']}")
            if set(k.keys()) != {"kalam", "shir"}:
                khata(hid, f"مفاتيح kharij {sorted(k.keys())}")
                continue

            def qima(v, masmuh, ism):
                if isinstance(v, list):
                    if fia != "غموض":
                        khata(hid, f"{ism} قائمةٌ في غير «غموض»")
                        return []
                    if len(v) < 2 or len(set(map(str, v))) != len(v):
                        khata(hid, f"{ism}: قائمة «غموض» بأقلّ من بديلين أو بتكرار")
                    for x in v:
                        if x not in masmuh or x in (LA_HUKM, GHAYR_MASUL):
                            khata(hid, f"{ism}: بديل غير مسموح: {x}")
                    return list(v)
                if v not in masmuh:
                    khata(hid, f"{ism} غير مسموح: {v}")
                return [v]

            kalam = qima(k["kalam"], HUKM_KALAM, "kalam")
            shir = qima(k["shir"], HUKM_SHIR, "shir")
            if fia == "غموض" and not (isinstance(k["kalam"], list) or isinstance(k["shir"], list)):
                khata(hid, "«غموض» من النوع الثاني بلا قائمة بديلين")
            la_hukm = (kalam == [LA_HUKM] and shir in ([LA_HUKM], [GHAYR_MASUL]))
            if fia == "خارج" and not la_hukm:
                khata(hid, "فئة «خارج» ومتوقّعها ليس «لا_حكم»")
            if fia != "خارج" and LA_HUKM in kalam:
                khata(hid, "«لا_حكم» في الكلام في فئةٍ غير «خارج»")

        # dakhil بلا تكرار في النوع نفسه
        mifta = (naw, json.dumps(d, ensure_ascii=False, sort_keys=True))
        if mifta in dakhil_mara:
            khata(hid, f"dakhil مكرّر مع {dakhil_mara[mifta]}")
        else:
            dakhil_mara[mifta] = h["id"]

        # sanad
        sanad = h["sanad"]
        if not isinstance(sanad, list):
            khata(hid, "sanad ليس قائمة")
            continue
        if la_hukm and sanad:
            khata(hid, "حالة «لا_حكم» لها سند")
        if la_hukm is False and not sanad:
            khata(hid, "حالة بحكمٍ بلا سند")
        nusus_kamila = []
        arqam = []
        for q in sanad:
            if not (isinstance(q, dict) and set(q.keys()) == {"satr", "nass"}):
                khata(hid, f"قطعة سند بمفاتيح غير «satr» و«nass»: {q}")
                continue
            satr, nass = q["satr"], q["nass"]
            if not (isinstance(satr, int) and not isinstance(satr, bool)):
                khata(hid, f"satr ليس عددًا صحيحًا: {satr}")
                continue
            if not (NITAQ[0] <= satr <= NITAQ[1]):
                khata(hid, f"السطر {satr} خارج النطاق {NITAQ[0]}–{NITAQ[1]}")
                continue
            if not (isinstance(nass, str) and nass.strip()):
                khata(hid, f"nass فارغ في السطر {satr}")
                continue
            if "\n" in nass or "\r" in nass:
                khata(hid, f"nass يعبر سطرين في السطر {satr}")
                continue
            satr_b = jarrid(asatir[satr - 1])
            if nass.encode("utf-8") not in satr_b:
                khata(hid, f"nass ليس قطعةً بالبايت من السطر {satr}: «{nass}»")
            arqam.append(satr)
            nusus_kamila.append(asatir[satr - 1].decode("utf-8"))
        if arqam:
            if len(set(arqam)) != len(arqam):
                khata(hid, "سطرٌ مكرّر في السند")
            if arqam != sorted(arqam) or arqam[-1] - arqam[0] != len(arqam) - 1:
                khata(hid, f"أسطر السند ليست متتاليةً تصاعديًّا: {arqam}")

        # المثال الحرفي
        if h["mithal_harfi"] is True and isinstance(h["mithal"], str):
            m = h["mithal"]
            if not any(m in n or m in sawwi(n) for n in nusus_kamila):
                khata(hid, f"mithal_harfi صحيح والمثال «{m}» ليس في سطرٍ من أسطر السند")
        elif h["mithal_harfi"] is False and isinstance(h["mithal"], str):
            if any(h["mithal"] in n for n in nusus_kamila):
                print(f"تنبيه [{hid}]: المثال «{h['mithal']}» في سطرٍ من السند وهو موسوم مركّبًا")

    # الأعداد
    kull = len(halat)
    if not (HUDUD["kull"][0] <= kull <= HUDUD["kull"][1]):
        akhta.append(f"[الأعداد] عدد الحالات {kull} خارج {HUDUD['kull']}")
    for ism in ("نفي", "ولي", "موجب", "حد", "خارج", "عموم", "غموض"):
        if add[ism] < HUDUD[ism]:
            akhta.append(f"[الأعداد] «{ism}» {add[ism]} أقلّ من {HUDUD[ism]}")

    print(f"الحالات: {kull}؛ " + "، ".join(f"{x}: {add[x]}" for x in add))
    if akhta:
        for a in akhta:
            print("خلل:", a)
        print(f"النتيجة: مرفوض ({len(akhta)} خلل)")
        return 1
    print("النتيجة: مقبول")
    return 0


if __name__ == "__main__":
    halat = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HUNA, "cases.json")
    masdar = sys.argv[2] if len(sys.argv) > 2 else MASDAR_IFTIRADI
    sys.exit(fahs(halat, masdar))
