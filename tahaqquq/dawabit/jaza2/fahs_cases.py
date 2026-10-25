#!/usr/bin/env python3
"""فاحص cases.json على المواصفة wasf.md. يُشغَّل: python3 -I fahs_cases.py [cases.json] [sibawayhi.txt]
يخرج 0 إن مرّ كلّ فحص، و1 مع سرد الأخطاء إن لم يمرّ، و2 إن تعذّرت القراءة."""
import hashlib
import json
import re
import sys
from collections import Counter

HUNA = __file__.rsplit("/", 1)[0]
CASES = sys.argv[1] if len(sys.argv) > 1 else HUNA + "/cases.json"
MASDAR = sys.argv[2] if len(sys.argv) > 2 else "/home/claude/mudaa_dir/sibawayhi.txt"
BASMA_MASDAR = "a160f940bb194e6fe7e6655d2c7f28e41f1fc648c4c5e340cc4e42306d5cb625"
AWWAL, AKHIR = 9305, 9652
ABWAB = [(9305, 9322), (9323, 9350), (9351, 9396), (9397, 9426), (9427, 9444),
         (9445, 9460), (9461, 9543), (9544, 9607), (9608, 9652)]

FIAT = {"موجب": 10, "حد": 8, "خارج": 5, "عموم": 5, "غموض": 3}
QABL = {"لا_شيء", "ناسخ", "ناسخ_مشغول", "حرف_ابتداء", "حرف_ابتداء_مفصول", "إذا_فجائية",
        "إذا_مضمر_بعدها", "لا", "لكن", "حرف_جر", "مضاف", "همزة", "قسم", "مبتدأ_ثم_قسم"}
ADAT_JAZA = {"من", "ما", "أي", "مهما", "متى", "حيثما", "أين", "أنى", "إن", "كلما", "الذي", "كل", "أن", "أما"}
ADAT_TALAB = {"طلب_أمر", "طلب_نهي", "طلب_استفهام", "طلب_تمن", "طلب_عرض", "معنى_أمر", "خبر_واجب"}
SHART = {"مضارع", "ماض", "لا_ينطبق"}
FIL = {"فعل_الشرط", "الجواب", "بين_المجزومين", "بعد_الجواب", "جواب_الطلب"}
RABIT = {"بلا", "فاء", "واو", "ثم", "أو"}
SURA = {"مجزوم", "مرفوع", "منصوب", "ماض", "منفي_بلم", "منفي_بلا_مجزوم"}
MANA = {"جزاء", "صلة", "حال", "بدل", "شركة", "ابتداء", "غير_معلن"}
HUKM = {"مقبول", "ضعيف", "قبيح", "خطأ", "لا_حكم", "غير_مسؤول"}
DAKHIL_KEYS = ["qabl", "adat", "shart", "fil", "rabit", "sura", "mana"]
MASMUH = {"qabl": QABL, "adat": ADAT_JAZA | ADAT_TALAB, "shart": SHART, "fil": FIL,
          "rabit": RABIT, "sura": SURA, "mana": MANA}
KEYS = {"id", "fia", "mithal", "mithal_harfi", "dakhil", "kharij", "sanad", "taliq"}
TASHKIL = re.compile("[ً-ْٰ]")


def satr_nazif(s):
    if s.startswith("~~"):
        return s[2:]
    if s.startswith("# "):
        return s[2:]
    return None


def main():
    akhta = []

    def khata(cid, m):
        akhta.append(f"{cid}: {m}")

    try:
        raw = open(MASDAR, "rb").read()
    except OSError as e:
        print("تعذّرت قراءة المصدر:", e)
        return 2
    if hashlib.sha256(raw).hexdigest() != BASMA_MASDAR:
        khata("المصدر", "البصمة لا تطابق المواصفة")
    asatr = raw.decode("utf-8").split("\n")  # asatr[n-1] هو السطر n

    try:
        data = json.loads(open(CASES, "rb").read().decode("utf-8"))
    except (OSError, ValueError, UnicodeDecodeError) as e:
        print("JSON غير صالح أو غير مقروء:", e)
        return 1
    if not isinstance(data, list):
        print("الملفّ ليس قائمة")
        return 1

    ids = Counter()
    dakhilat = Counter()
    fiat = Counter()
    abwab = Counter()
    for i, c in enumerate(data):
        if not isinstance(c, dict):
            khata(f"#{i}", "العنصر ليس كائنًا")
            continue
        cid = c.get("id", f"#{i}")
        if set(c.keys()) != KEYS:
            khata(cid, f"الحقول {sorted(c.keys())} لا تطابق {sorted(KEYS)}")
        if not isinstance(cid, str) or not re.fullmatch(r"B\d{2}", cid):
            khata(cid, "id ليس B ورقمين")
        ids[cid if isinstance(cid, str) else repr(cid)] += 1
        fia = c.get("fia")
        if not isinstance(fia, str) or fia not in FIAT:
            fia = repr(fia)
            khata(cid, f"فئة غير مسموحة {fia}")
        fiat[fia] += 1

        mithal = c.get("mithal")
        if not isinstance(mithal, str) or not mithal.strip():
            khata(cid, "mithal فارغ")
            mithal = ""
        elif TASHKIL.search(mithal):
            khata(cid, "mithal مشكول")
        harfi = c.get("mithal_harfi")
        if not isinstance(harfi, bool):
            khata(cid, "mithal_harfi ليس منطقيًّا")

        d = c.get("dakhil")
        if not isinstance(d, dict) or set(d.keys()) != set(DAKHIL_KEYS):
            khata(cid, "dakhil ناقص أو زائد")
            d = {}
        for k in DAKHIL_KEYS:
            if k in d and (not isinstance(d[k], str) or d[k] not in MASMUH[k]):
                khata(cid, f"dakhil.{k} = {d[k]!r} غير مسموح")
        if d:
            dakhilat[tuple(repr(d.get(k)) if not isinstance(d.get(k), str) else d.get(k) for k in DAKHIL_KEYS)] += 1
            if isinstance(d.get("adat"), str) and d.get("adat") in ADAT_TALAB:
                if d.get("shart") != "لا_ينطبق" or d.get("fil") != "جواب_الطلب":
                    khata(cid, "صدر الطلب يقتضي shart=لا_ينطبق وfil=جواب_الطلب")
            elif d.get("fil") == "جواب_الطلب":
                khata(cid, "جواب_الطلب بلا صدر طلب")

        k_ = c.get("kharij")
        if not isinstance(k_, dict) or set(k_.keys()) != {"kalam", "shir"}:
            khata(cid, "kharij ناقص أو زائد")
            k_ = {"kalam": None, "shir": None}
        qawaim = 0
        for f in ("kalam", "shir"):
            v = k_[f]
            if isinstance(v, list):
                qawaim += 1
                if fia != "غموض":
                    khata(cid, f"قائمة في {f} خارج فئة غموض")
                if len(v) != 2 or len(set(v)) != 2:
                    khata(cid, f"{f}: البديلان يجب أن يكونا اثنين مختلفين")
                for x in v:
                    if x not in HUKM - {"لا_حكم", "غير_مسؤول"}:
                        khata(cid, f"{f}: بديل غير مسموح {x!r}")
            elif v not in HUKM:
                khata(cid, f"{f} = {v!r} غير مسموح")
        if k_["kalam"] == "غير_مسؤول":
            khata(cid, "غير_مسؤول لـshir وحده")
        if fia == "غموض" and qawaim == 0:
            khata(cid, "غموض بلا قائمة بديلين")
        kalam = k_["kalam"]
        if fia == "موجب" and kalam != "مقبول":
            khata(cid, "موجب وكلامه غير مقبول")
        if fia == "حد" and (isinstance(kalam, list) or kalam not in {"ضعيف", "قبيح", "خطأ"}):
            khata(cid, "حد وكلامه ليس ردًّا أو تضعيفًا أو تقبيحًا")
        if fia == "عموم" and (isinstance(kalam, list) or kalam in {"لا_حكم", "غير_مسؤول"}):
            khata(cid, "عموم بلا حكم واحد")
        la_hukm = (kalam == "لا_حكم")
        if (fia == "خارج") != la_hukm:
            khata(cid, "خارج ⇔ kalam = لا_حكم")
        if k_["shir"] == "لا_حكم" and not la_hukm:
            khata(cid, "shir لا_حكم في حالة لها حكم")

        sanad = c.get("sanad")
        if not isinstance(sanad, list):
            khata(cid, "sanad ليس قائمة")
            sanad = []
        if la_hukm and sanad:
            khata(cid, "لا_حكم وله سند")
        if not la_hukm and not sanad:
            khata(cid, "حكمٌ بلا سند")
        nusus_kamila = []
        for s in sanad:
            if not isinstance(s, dict) or set(s.keys()) != {"satr", "nass"}:
                khata(cid, f"قطعة سند معيبة {s!r}")
                continue
            n, nass = s["satr"], s["nass"]
            if not isinstance(n, int) or isinstance(n, bool) or not (AWWAL <= n <= AKHIR):
                khata(cid, f"السطر {n!r} خارج النطاق {AWWAL}–{AKHIR}")
                continue
            nazif = satr_nazif(asatr[n - 1])
            if nazif is None:
                khata(cid, f"السطر {n} بلا بادئة ~~ أو «# »")
                continue
            nusus_kamila.append(nazif)
            if not isinstance(nass, str) or not nass or "\n" in nass:
                khata(cid, f"nass فارغ أو متعدّد الأسطر في {n}")
            elif nass.encode("utf-8") not in nazif.encode("utf-8"):
                khata(cid, f"nass ليس قطعة حرفيّة من السطر {n}: {nass!r}")
            for b, (a, z) in enumerate(ABWAB):
                if a <= n <= z:
                    abwab[b] += 1
        if harfi is True and mithal and not any(mithal in t for t in nusus_kamila):
            khata(cid, "mithal_harfi=true والمثال ليس في سطرٍ من أسطر سنده")

        t = c.get("taliq")
        if not isinstance(t, str) or not t.strip() or "\n" in t:
            khata(cid, "taliq ليس سطرًا واحدًا")

    for cid, k in ids.items():
        if k > 1:
            khata(cid, f"id مكرّر {k} مرّات")
    for dk, k in dakhilat.items():
        if k > 1:
            khata("المدخل", f"مكرّر {k} مرّات: {dk}")
    if not (35 <= len(data) <= 45):
        khata("العدد", f"{len(data)} خارج 35–45")
    for f, m in FIAT.items():
        if fiat[f] < m:
            khata("الفئات", f"{f}: {fiat[f]} أقلّ من {m}")
    for b, (a, z) in enumerate(ABWAB):
        if abwab[b] == 0:
            khata("الأبواب", f"لا سند في الباب {a}–{z}")

    if akhta:
        print("\n".join(akhta))
        print(f"أخطاء: {len(akhta)}")
        return 1
    print(f"مرّ: {len(data)} حالة؛ " + "، ".join(f"{f} {fiat[f]}" for f in FIAT)
          + f"؛ حرفيّة {sum(1 for c in data if c.get('mithal_harfi') is True)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
