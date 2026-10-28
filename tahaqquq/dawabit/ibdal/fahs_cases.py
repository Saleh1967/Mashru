#!/usr/bin/env python3
"""فاحصُ ملفّ الحالات لضابط «الإبدال: الواو والياء في الكلمة» (ألفيّة ابن مالك).

التشغيل:
    python3 -I fahs_cases.py <مجلّد المصدر> [مسار cases.json]

يفحص، على ما في المواصفة (wasf.md):
- بصمتَي المصدرين (alfiyya.txt، sibawayhi.txt).
- أنّ الملفّ JSON صحيح، قائمةٌ، ولكلّ حالةٍ الحقولُ التسعة وحدها بأنواعها وقيمها المسموحة.
- تفرّدَ المعرّفات (B ورقمان) والكلمات.
- شروطَ كتابة الكلمة المشكولة (حركةٌ أو سكونٌ على كلّ حرف إلّا الألف ومدَّ الواو بعد الضمّة والياء بعد الكسرة،
  والشدّةُ مع حركتها، والتنوين في الآخر، وألفُ تنوين النصب بعد الفتحتين، ولا مسافة ولا تطويل ولا ترقيم)،
  وأنّ في الكلمة واوًا أو ياءً أو ألفًا في غير أوّلها.
- اتّساقَ الفئة والحكم (وقائمةَ البديلين في الغموض)، و`badil` نصًّا غيرَ فارغ إذا وفقط إذا كان الحكم «ممنوع».
- الأزواجَ: متبادلة، والحكمان مختلفان، والكلمتان تختلفان بتعديلٍ واحد (حرفٍ أو علامة).
- السندَ: كلُّ قطعةٍ `masdar`=«ألفية» و`satr` في النطاق و`nass` قطعةٌ حرفيّة من السطر بعد حذف «# » وحدها، لا تعبر سطرين؛
  وحالةُ «خارج» بلا سند، وما سواها بسند.
- أنّ `mithal_harfi` يساوي: الكلمةُ بلا شكلٍ ولا «ال» واقعةٌ في نصّ أحد أسطر سندها.
- الأعدادَ: بين 40 و50 حالة، وحدودَ الفئات الدنيا، و3 حالاتٍ على الأقلّ لكلّ حكمٍ من الستّة (يُعيَّن الحكمُ من أوّل قطعةٍ
  في السند)، و6 أزواجٍ على الأقلّ.
يخرج 0 إن صحّ كلُّ ذلك، و1 إن وُجد خلل (ويطبع كلَّ خلل)، و2 لخطأ الاستعمال.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

SHA256 = {
    "alfiyya.txt": "13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0",
    "sibawayhi.txt": "a160f940bb194e6fe7e6655d2c7f28e41f1fc648c4c5e340cc4e42306d5cb625",
}
NITAQ = {1216, 1217, 1222, 1224, 1225, 1226, 1238, 1239}
HUQUL = ["id", "fia", "kalima", "mithal_harfi", "hukm", "badil", "zawj", "sanad", "taliq"]
FIAT = {"موجب", "حد", "عموم", "خارج", "غموض"}
AHKAM = {"ممنوع", "غير_ممنوع", "لا_حكم"}
BADILAN = {"ممنوع", "غير_ممنوع"}
HADD_FIA = {"موجب": 10, "حد": 10, "عموم": 8, "خارج": 5, "غموض": 2}
ADAD_ADNA, ADAD_AQSA = 40, 50
HADD_HUKM = 3
HADD_AZWAJ = 6

LETTERS = set("ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىي")
ALIFS = set("اىآ")
FATHA, DAMMA, KASRA = "َ", "ُ", "ِ"
FATHATAN, DAMMATAN, KASRATAN = "ً", "ٌ", "ٍ"
SHADDA, SUKUN = "ّ", "ْ"
VOWELS = {FATHA, DAMMA, KASRA}
TANWIN = {FATHATAN, DAMMATAN, KASRATAN}
MARKS = VOWELS | TANWIN | {SHADDA, SUKUN}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def units(word):
    """يقسم الكلمة وحداتٍ (حرف، علامات)، أو يرفع ValueError."""
    out = []
    for ch in word:
        if ch in LETTERS:
            out.append([ch, []])
        elif ch in MARKS:
            if not out:
                raise ValueError("علامةٌ قبل أوّل حرف")
            out[-1][1].append(ch)
        else:
            raise ValueError("محرفٌ غيرُ مسموح %r" % ch)
    return out


def haraka(marks):
    """الحركة أو التنوين أو السكون في وحدة، أو None."""
    v = [m for m in marks if m in VOWELS | TANWIN | {SUKUN}]
    return v[0] if v else None


def fahs_kitaba(word):
    """يعيد قائمة الخلل في كتابة الكلمة على شروط المواصفة."""
    err = []
    try:
        us = units(word)
    except ValueError as e:
        return [str(e)]
    if len(us) < 2:
        return ["كلمةٌ أقصرُ من حرفين"]
    n = len(us)
    for i, (l, ms) in enumerate(us):
        vs = [m for m in ms if m in VOWELS | TANWIN | {SUKUN}]
        sh = [m for m in ms if m == SHADDA]
        if len(vs) > 1 or len(sh) > 1:
            err.append("علاماتٌ متعدّدة على الحرف %d" % (i + 1))
            continue
        if sh and (not vs or vs[0] == SUKUN):
            err.append("شدّةٌ بلا حركة على الحرف %d" % (i + 1))
        if l in ALIFS:
            if ms:
                err.append("علامةٌ على الألف في الموضع %d" % (i + 1))
            continue
        if l == "ة" and (i != n - 1 or not vs or vs[0] == SUKUN):
            err.append("التاء المربوطة في غير الآخر أو بلا حركة")
        if vs and vs[0] in TANWIN:
            last = i == n - 1
            nasb_alif = (i == n - 2 and vs[0] == FATHATAN and us[n - 1][0] in {"ا", "ى"})
            if not (last or nasb_alif):
                err.append("تنوينٌ في غير الآخر على الحرف %d" % (i + 1))
        if not ms:
            prev = haraka(us[i - 1][1]) if i > 0 else None
            if l == "و" and prev == DAMMA:
                continue
            if l == "ي" and prev == KASRA:
                continue
            err.append("حرفٌ بلا حركةٍ ولا سكون في الموضع %d (%s)" % (i + 1, l))
    # ألفُ تنوين النصب بعد الفتحتين في الآخر فقط
    for i, (l, ms) in enumerate(us):
        if haraka(ms) == FATHATAN and i != n - 1:
            if not (i == n - 2 and us[n - 1][0] in {"ا", "ى"}):
                err.append("فتحتان في غير الآخر")
    if not any(l in {"و", "ي"} | ALIFS for l, _ in us[1:]):
        err.append("لا واو ولا ياء ولا ألف في غير أوّل الكلمة")
    return err


def mujarrad(word):
    """الكلمة بلا شكل وبلا «ال» في أوّلها."""
    b = "".join(ch for ch in word if ch not in MARKS)
    if b.startswith("ال") and len(b) > 3:
        b = b[2:]
    return b


def levenshtein(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def hukm_min_qita(q):
    """رقمُ الحكم (1–6 على ترقيم المواصفة) من قطعة سند."""
    s, t = q["satr"], q["nass"]
    if s == 1216:
        return 2 if "بواو" in t else 1
    if s == 1217:
        return 2
    if s == 1222:
        return 4 if "كموقن" in t else 3
    if s == 1224:
        return 4
    if s in (1225, 1226):
        return 5
    if s in (1238, 1239):
        return 6
    return None


def main(argv):
    if len(argv) not in (2, 3):
        print("الاستعمال: python3 -I fahs_cases.py <مجلّد المصدر> [cases.json]", file=sys.stderr)
        return 2
    src = Path(argv[1])
    cases_path = Path(argv[2]) if len(argv) == 3 else Path(__file__).resolve().parent / "cases.json"
    E = []

    for name, h in SHA256.items():
        p = src / name
        if not p.is_file():
            E.append("المصدر غائب: %s" % p)
            continue
        got = sha256(p)
        if got != h:
            E.append("بصمةُ %s %s لا تطابق %s" % (name, got, h))
    if E:
        for e in E:
            print("خلل:", e)
        return 1

    raw = (src / "alfiyya.txt").read_bytes().decode("utf-8")
    asTur = raw.split("\n")

    def nass_satr(n):
        s = asTur[n - 1]
        return s[2:] if s.startswith("# ") else s

    try:
        cases = json.loads(cases_path.read_bytes().decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
        print("خلل: لا يُقرأ ملفّ الحالات JSON:", e)
        return 1
    if not isinstance(cases, list):
        print("خلل: ملفّ الحالات ليس قائمة")
        return 1

    ids, kalimat = {}, {}
    for k, c in enumerate(cases):
        tag = c.get("id", "#%d" % k) if isinstance(c, dict) else "#%d" % k
        if not isinstance(c, dict):
            E.append("%s: ليست كائنًا" % tag)
            continue
        if list(c.keys()) != HUQUL and set(c.keys()) != set(HUQUL):
            E.append("%s: الحقول %s لا تطابق %s" % (tag, sorted(c.keys()), HUQUL))
            continue
        cid = c["id"]
        if not isinstance(cid, str) or not re.fullmatch(r"B\d{2}", cid):
            E.append("%s: معرّفٌ غيرُ صالح" % tag)
        elif cid in ids:
            E.append("%s: معرّفٌ مكرَّر" % cid)
        else:
            ids[cid] = c
        if c["fia"] not in FIAT:
            E.append("%s: فئةٌ غيرُ مسموحة %r" % (tag, c["fia"]))
        kal = c["kalima"]
        if not isinstance(kal, str) or not kal:
            E.append("%s: كلمةٌ فارغة" % tag)
        else:
            for e in fahs_kitaba(kal):
                E.append("%s: كتابة: %s" % (tag, e))
            if kal in kalimat:
                E.append("%s: الكلمة نفسُها في %s" % (tag, kalimat[kal]))
            kalimat[kal] = tag
        if not isinstance(c["mithal_harfi"], bool):
            E.append("%s: mithal_harfi ليس منطقيًّا" % tag)
        h = c["hukm"]
        fia = c["fia"]
        if fia == "غموض":
            if not (isinstance(h, list) and len(h) == 2 and set(h) == BADILAN):
                E.append("%s: حكمُ الغموض ليس قائمةَ البديلين" % tag)
        else:
            if not (isinstance(h, str) and h in AHKAM):
                E.append("%s: حكمٌ غيرُ مسموح %r" % (tag, h))
            elif fia in ("موجب", "خارج") and h != "غير_ممنوع":
                E.append("%s: الفئة %s تقتضي غير_ممنوع" % (tag, fia))
            elif fia == "حد" and h != "ممنوع":
                E.append("%s: الفئة حد تقتضي ممنوع" % tag)
        b = c["badil"]
        if h == "ممنوع":
            if not (isinstance(b, str) and b.strip()):
                E.append("%s: ممنوعٌ بلا بديل" % tag)
            else:
                for e in fahs_kitaba(b):
                    E.append("%s: كتابة البديل: %s" % (tag, e))
                if b == kal:
                    E.append("%s: البديلُ هو الكلمة" % tag)
        elif b is not None:
            E.append("%s: بديلٌ في غير ممنوع" % tag)
        z = c["zawj"]
        if z is not None and not isinstance(z, str):
            E.append("%s: zawj ليس نصًّا ولا null" % tag)
        t = c["taliq"]
        if not (isinstance(t, str) and t.strip() and "\n" not in t and "\r" not in t):
            E.append("%s: تعليقٌ فارغ أو أكثرُ من سطر" % tag)
        sanad = c["sanad"]
        if not isinstance(sanad, list):
            E.append("%s: السند ليس قائمة" % tag)
            continue
        if fia == "خارج" and sanad:
            E.append("%s: حالةُ خارج بسند" % tag)
        if fia != "خارج" and not sanad:
            E.append("%s: حالةٌ بلا سند" % tag)
        sanad_ok = True
        for q in sanad:
            if not (isinstance(q, dict) and set(q.keys()) == {"masdar", "satr", "nass"}):
                E.append("%s: قطعةُ سندٍ بحقولٍ غير masdar/satr/nass" % tag)
                sanad_ok = False
                continue
            if q["masdar"] != "ألفية":
                E.append("%s: masdar غير «ألفية»" % tag)
            s = q["satr"]
            if not (isinstance(s, int) and not isinstance(s, bool)) or s not in NITAQ:
                E.append("%s: السطر %r خارج النطاق" % (tag, s))
                sanad_ok = False
                continue
            nass = q["nass"]
            if not (isinstance(nass, str) and nass) or "\n" in nass:
                E.append("%s: nass فارغ أو يعبر سطرين" % tag)
                sanad_ok = False
                continue
            if nass.encode("utf-8") not in nass_satr(s).encode("utf-8"):
                E.append("%s: «%s» ليس قطعةً حرفيّةً من السطر %d" % (tag, nass, s))
                sanad_ok = False
        if sanad_ok and isinstance(kal, str) and isinstance(c["mithal_harfi"], bool):
            mj = mujarrad(kal)
            fihi = any(mj in nass_satr(q["satr"]) for q in sanad)
            if c["mithal_harfi"] != fihi:
                E.append("%s: mithal_harfi=%s والكلمة «%s» %s في أسطر سندها"
                         % (tag, c["mithal_harfi"], mj, "واقعةٌ" if fihi else "غيرُ واقعة"))

    # الأزواج
    azwaj = set()
    for cid, c in ids.items():
        z = c["zawj"]
        if z is None:
            continue
        if z == cid or z not in ids:
            E.append("%s: زوجٌ غيرُ موجود %r" % (cid, z))
            continue
        o = ids[z]
        if o["zawj"] != cid:
            E.append("%s: الزوج %s غيرُ متبادل" % (cid, z))
            continue
        if json.dumps(o["hukm"], ensure_ascii=False) == json.dumps(c["hukm"], ensure_ascii=False):
            E.append("%s: حكمُ زوجه %s مثلُ حكمه" % (cid, z))
        if isinstance(c["kalima"], str) and isinstance(o["kalima"], str):
            if levenshtein(c["kalima"], o["kalima"]) != 1:
                E.append("%s: لا تختلف عن زوجها %s بتعديلٍ واحد" % (cid, z))
        azwaj.add(tuple(sorted((cid, z))))

    # الأعداد
    n = len(cases)
    if not (ADAD_ADNA <= n <= ADAD_AQSA):
        E.append("عددُ الحالات %d خارج %d–%d" % (n, ADAD_ADNA, ADAD_AQSA))
    fia_adad = {f: 0 for f in FIAT}
    hukm_adad = {"ممنوع": 0, "غير_ممنوع": 0, "لا_حكم": 0, "البديلان": 0}
    qaida_adad = {i: 0 for i in range(1, 7)}
    for c in cases:
        if not isinstance(c, dict) or set(c.keys()) != set(HUQUL):
            continue
        if c["fia"] in fia_adad:
            fia_adad[c["fia"]] += 1
        h = c["hukm"]
        if isinstance(h, list):
            hukm_adad["البديلان"] += 1
        elif h in hukm_adad:
            hukm_adad[h] += 1
        if isinstance(c["sanad"], list) and c["sanad"] and isinstance(c["sanad"][0], dict) \
                and c["sanad"][0].get("satr") in NITAQ and isinstance(c["sanad"][0].get("nass"), str):
            r = hukm_min_qita(c["sanad"][0])
            if r:
                qaida_adad[r] += 1
    for f, m in HADD_FIA.items():
        if fia_adad[f] < m:
            E.append("الفئة %s: %d أقلّ من %d" % (f, fia_adad[f], m))
    for r, m in qaida_adad.items():
        if m < HADD_HUKM:
            E.append("الحكم %d: %d حالة أقلّ من %d" % (r, m, HADD_HUKM))
    if len(azwaj) < HADD_AZWAJ:
        E.append("الأزواج %d أقلّ من %d" % (len(azwaj), HADD_AZWAJ))

    if E:
        for e in E:
            print("خلل:", e)
        print("الخلل:", len(E))
        return 1
    print("الحالات:", n)
    print("الفئات:", json.dumps(fia_adad, ensure_ascii=False))
    print("الأحكام:", json.dumps(hukm_adad, ensure_ascii=False))
    print("لكلّ حكم (من أوّل قطعة سند):", json.dumps(qaida_adad, ensure_ascii=False))
    print("الأزواج:", len(azwaj))
    print("حرفيّ:", sum(1 for c in cases if c.get("mithal_harfi") is True))
    print("صحيح")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
