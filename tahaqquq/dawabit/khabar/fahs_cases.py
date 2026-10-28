# -*- coding: utf-8 -*-
"""فاحص ملفّ الحالات لضابط الخبر (المواصفة wasf.md).

الاستعمال: python3 -I fahs_cases.py <cases.json> <مجلّد qatr.txt وalfiyya.txt>
يخرج 0 إن مرّ كلُّ فحص، و1 إن فشل شيء (ويطبع كلَّ خلل)، و2 لخطأ في الاستدعاء.
"""
import hashlib
import itertools
import json
import os
import re
import sys

BASMAT = {
    "qatr.txt": "2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d",
    "alfiyya.txt": "13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0",
}
MASDAR_FILE = {"قطر": "qatr.txt", "ألفية": "alfiyya.txt"}
NITAQ = {"قطر": range(157, 163), "ألفية": range(177, 189)}
QATR_162_HADD = "وقد يتعدد"
PREFIXES = ("### | ", "# ", "~~")

NA = "لا_ينطبق"
FIA = ["موجب", "حد", "خارج", "عموم", "غموض"]
HUKM = ["مقبول", "خطأ", "لا_حكم"]
DARAJA = ["قليل", "بتأويل", "بلا_درجة"]
BINYA = ["مبتدأ_وخبر", "وصف_ومرفوعه"]
MB_FIELDS = ["jins", "khabar", "rabit", "marfu", "jaryan", "ifada"]
WS_FIELDS = ["itimad", "wasf_adad", "marfu_adad", "tahlil"]
DAKHIL_KEYS = ["binya"] + MB_FIELDS + WS_FIELDS
VALS = {
    "jins": ["ذات", "معنى"],
    "khabar": ["مفرد_جامد", "مفرد_مشتق", "جملة_اسمية", "جملة_فعلية", "ظرف_مكان", "ظرف_زمان", "جار_مجرور"],
    "rabit": ["ضمير", "اسم_اشارة", "اعادة_المبتدأ", "عموم", "هي_المبتدأ", "لا_رابط"],
    "marfu": ["مستكن", "بارز", "ظاهر", "لا_شيء"],
    "jaryan": ["لصاحبه", "لغيره"],
    "ifada": ["مفيد", "غير_مفيد"],
    "itimad": ["استفهام", "نفي", "لا_اعتماد"],
    "wasf_adad": ["مفرد", "مثنى", "جمع"],
    "marfu_adad": ["مفرد", "مثنى", "جمع"],
    "tahlil": ["فاعل_اغنى", "خبر_مقدم"],
}
CASE_KEYS = {"id", "fia", "mithal", "mithal_harfi", "dakhil", "hukm", "daraja", "zawj", "sanad", "taliq"}
SANAD_KEYS = {"masdar", "satr", "nass"}
TASHKIL = re.compile("[ً-ْٰ]")

# حدود «ما يُطلب»
JUMLA_MIN = (45, 60)
FIA_MIN = {"موجب": 14, "حد": 12, "خارج": 5, "عموم": 5, "غموض": 2}
BINYA_MIN = {"وصف_ومرفوعه": 12, "مبتدأ_وخبر": 30}
MB_VAL_MIN = {"khabar": 3, "rabit": 2, "marfu": 2, "jaryan": 2, "ifada": 2, "jins": 5}
WS_VAL_MIN = {"itimad": 3, "wasf_adad": 2, "marfu_adad": 2, "tahlil": 5}
AZWAJ_MIN = 8


def applies(binya, field, khabar):
    """هل ينطبق الحقل على هذا البناء ونوع الخبر؟"""
    if binya == "وصف_ومرفوعه":
        return field in WS_FIELDS
    if field in WS_FIELDS:
        return False
    if field in ("jins", "khabar"):
        return True
    if field == "rabit":
        return khabar in ("جملة_اسمية", "جملة_فعلية")
    if field == "marfu":
        return khabar in ("مفرد_جامد", "مفرد_مشتق")
    if field == "jaryan":
        return khabar == "مفرد_مشتق"
    if field == "ifada":
        return khabar == "ظرف_زمان"
    raise KeyError(field)


def mumkin_khabar(khabar):
    """عدد المداخل المتمايزة الممكنة لقيمةٍ من قيم khabar (لحساب الحدّ الأدنى الممكن)."""
    n = 1
    for f in MB_FIELDS:
        if f == "khabar":
            continue
        if applies("مبتدأ_وخبر", f, khabar):
            n *= len(VALS[f])
    return n


def strip_prefix(line):
    for p in PREFIXES:
        if line.startswith(p):
            return line[len(p):]
    return line


def main(argv):
    if len(argv) != 3:
        print("الاستعمال: python3 -I fahs_cases.py <cases.json> <مجلّد المصدرين>", file=sys.stderr)
        return 2
    path, src = argv[1], argv[2]
    errs = []
    notes = []

    def err(msg):
        errs.append(msg)

    # ١. بصمتا المصدرين
    LINES = {}
    for name, h in BASMAT.items():
        p = os.path.join(src, name)
        try:
            b = open(p, "rb").read()
        except OSError as e:
            err("لا يُقرأ المصدر %s: %s" % (p, e))
            continue
        got = hashlib.sha256(b).hexdigest()
        if got != h:
            err("بصمة %s %s لا تطابق المواصفة %s" % (name, got, h))
        LINES[name] = b.decode("utf-8").split("\n")

    # ٢. JSON
    try:
        with open(path, "rb") as f:
            raw = f.read()
        data = json.loads(raw.decode("utf-8"))
    except Exception as e:  # noqa
        print("JSON غير صالح: %s" % e)
        return 1
    if not isinstance(data, list):
        print("الملفّ ليس قائمة")
        return 1

    ids = {}
    for i, c in enumerate(data):
        tag = "عنصر %d" % i
        if not isinstance(c, dict):
            err("%s ليس كائنًا" % tag)
            continue
        if set(c.keys()) != CASE_KEYS:
            err("%s: المفاتيح %s" % (tag, sorted(c.keys())))
            continue
        cid = c["id"]
        if not isinstance(cid, str) or not re.fullmatch(r"K\d{2}", cid):
            err("%s: id غير صالح %r" % (tag, cid))
            continue
        if cid in ids:
            err("id مكرّر %s" % cid)
            continue
        ids[cid] = c

    good = []
    for cid, c in ids.items():
        ok = True
        fia = c["fia"]
        if fia not in FIA:
            err("%s: fia %r" % (cid, fia)); ok = False
        if not isinstance(c["mithal"], str) or not c["mithal"].strip():
            err("%s: mithal فارغ" % cid); ok = False
        elif TASHKIL.search(c["mithal"]):
            err("%s: mithal مشكول" % cid); ok = False
        if not isinstance(c["mithal_harfi"], bool):
            err("%s: mithal_harfi ليس منطقيًّا" % cid); ok = False
        if not isinstance(c["taliq"], str) or not c["taliq"].strip() or "\n" in c["taliq"] or "\r" in c["taliq"]:
            err("%s: taliq ليس سطرًا واحدًا" % cid); ok = False

        # الدخل
        d = c["dakhil"]
        if not isinstance(d, dict) or set(d.keys()) != set(DAKHIL_KEYS):
            err("%s: حقول dakhil" % cid); ok = False
            continue
        if d["binya"] not in BINYA:
            err("%s: binya %r" % (cid, d["binya"])); ok = False
            continue
        khabar = d["khabar"]
        if d["binya"] == "مبتدأ_وخبر" and khabar not in VALS["khabar"]:
            err("%s: khabar %r" % (cid, khabar)); ok = False
            continue
        for f in MB_FIELDS + WS_FIELDS:
            v = d[f]
            if applies(d["binya"], f, khabar):
                if v not in VALS[f]:
                    err("%s: %s=%r غير مسموح (الحقل ينطبق)" % (cid, f, v)); ok = False
            else:
                if v != NA:
                    err("%s: %s=%r والحقل لا ينطبق" % (cid, f, v)); ok = False

        # الحكم والدرجة
        h, r = c["hukm"], c["daraja"]
        hl, rl = isinstance(h, list), isinstance(r, list)
        if fia == "غموض":
            if not (hl or rl):
                err("%s: غموض بلا قائمة في hukm أو daraja" % cid); ok = False
            if hl and rl:
                err("%s: قائمتان معًا" % cid); ok = False
        else:
            if hl or rl:
                err("%s: قائمة في غير غموض" % cid); ok = False
        if hl:
            if len(h) != 2 or len(set(h)) != 2 or any(x not in HUKM for x in h):
                err("%s: قائمة hukm %r" % (cid, h)); ok = False
            elif "مقبول" in h:
                if r not in DARAJA:
                    err("%s: درجة البديل المقبول %r" % (cid, r)); ok = False
            else:
                if r != "بلا_درجة":
                    err("%s: daraja %r وليس في البديلين مقبول" % (cid, r)); ok = False
        else:
            if h not in HUKM:
                err("%s: hukm %r" % (cid, h)); ok = False
            elif h == "مقبول":
                if rl:
                    if len(r) != 2 or len(set(r)) != 2 or any(x not in DARAJA for x in r):
                        err("%s: قائمة daraja %r" % (cid, r)); ok = False
                elif r not in DARAJA:
                    err("%s: daraja %r" % (cid, r)); ok = False
            else:
                if r != "بلا_درجة":
                    err("%s: hukm %s وdaraja %r (يجب بلا_درجة)" % (cid, h, r)); ok = False
        # اتّساق الفئة والحكم
        if fia == "موجب" and h != "مقبول":
            err("%s: موجب وحكمه %r" % (cid, h)); ok = False
        if fia == "حد" and h != "خطأ":
            err("%s: حد وحكمه %r" % (cid, h)); ok = False
        if fia == "خارج" and h != "لا_حكم":
            err("%s: خارج وحكمه %r" % (cid, h)); ok = False
        if fia == "عموم" and h not in ("مقبول", "خطأ"):
            err("%s: عموم وحكمه %r" % (cid, h)); ok = False

        # السند
        s = c["sanad"]
        if not isinstance(s, list):
            err("%s: sanad ليس قائمة" % cid); ok = False
            s = []
        if h == "لا_حكم":
            if s:
                err("%s: لا_حكم وله سند" % cid); ok = False
        elif not s:
            err("%s: حكم بلا سند" % cid); ok = False
        full_lines = []
        for j, p in enumerate(s):
            if not isinstance(p, dict) or set(p.keys()) != SANAD_KEYS:
                err("%s: قطعة سند %d: المفاتيح" % (cid, j)); ok = False
                continue
            m, n, t = p["masdar"], p["satr"], p["nass"]
            if m not in MASDAR_FILE:
                err("%s: masdar %r" % (cid, m)); ok = False
                continue
            if not isinstance(n, int) or isinstance(n, bool) or n not in NITAQ[m]:
                err("%s: السطر %r خارج نطاق %s" % (cid, n, m)); ok = False
                continue
            if not isinstance(t, str) or not t or "\n" in t or "\r" in t:
                err("%s: nass فارغ أو يعبر سطرين" % cid); ok = False
                continue
            fl = LINES.get(MASDAR_FILE[m])
            if fl is None:
                ok = False
                continue
            line = strip_prefix(fl[n - 1])
            full_lines.append(line)
            if t not in line:
                err("%s: nass ليس قطعةً حرفيّةً من %s %d: %r" % (cid, m, n, t)); ok = False
                continue
            if m == "قطر" and n == 162:
                hadd = line.find(QATR_162_HADD)
                starts = [k for k in range(len(line)) if line.startswith(t, k)]
                if not any(k + len(t) <= hadd for k in starts):
                    err("%s: nass في قطر 162 بعد «وقد يتعدد»" % cid); ok = False
            if t.encode("utf-8") not in fl[n - 1].encode("utf-8"):
                err("%s: nass ليس قطعةً بالبايت" % cid); ok = False
        if isinstance(c["mithal"], str) and isinstance(c["mithal_harfi"], bool):
            present = any(c["mithal"] in L for L in full_lines)
            if c["mithal_harfi"] and not present:
                err("%s: mithal_harfi=true والمثال ليس في أسطر سنده" % cid); ok = False
            if not c["mithal_harfi"] and present:
                err("%s: mithal_harfi=false والمثال في أسطر سنده" % cid); ok = False
        if ok:
            good.append(c)

    # ٣. الأزواج
    npairs = 0
    for cid, c in ids.items():
        z = c["zawj"]
        if z is None:
            continue
        if not isinstance(z, str) or z not in ids or z == cid:
            err("%s: zawj %r غير موجود" % (cid, z))
            continue
        o = ids[z]
        if o["zawj"] != cid:
            err("%s: zawj %s غير متبادل" % (cid, z))
            continue
        if cid < z:
            npairs += 1
        if isinstance(c["dakhil"], dict) and isinstance(o["dakhil"], dict):
            diff = [k for k in DAKHIL_KEYS if c["dakhil"].get(k) != o["dakhil"].get(k)]
            if len(diff) != 1:
                err("%s/%s: يختلفان في %d حقلًا %s" % (cid, z, len(diff), diff))
        if c["hukm"] == o["hukm"] and c["daraja"] == o["daraja"]:
            err("%s/%s: الحكم والدرجة سواء" % (cid, z))

    # ٤. المداخل المكرّرة
    seen = {}
    for cid, c in ids.items():
        if not isinstance(c["dakhil"], dict):
            continue
        key = json.dumps(c["dakhil"], ensure_ascii=False, sort_keys=True)
        if key in seen:
            err("مدخل مكرّر: %s و%s" % (seen[key], cid))
        else:
            seen[key] = cid

    # ٥. الأعداد
    allc = list(ids.values())
    N = len(allc)
    if not (JUMLA_MIN[0] <= N <= JUMLA_MIN[1]):
        err("العدد %d خارج %s" % (N, JUMLA_MIN))
    for f, m in FIA_MIN.items():
        k = sum(1 for c in allc if c["fia"] == f)
        if k < m:
            err("فئة %s: %d < %d" % (f, k, m))
    for b, m in BINYA_MIN.items():
        k = sum(1 for c in allc if isinstance(c["dakhil"], dict) and c["dakhil"].get("binya") == b)
        if k < m:
            err("بناء %s: %d < %d" % (b, k, m))
    mb = [c for c in allc if isinstance(c["dakhil"], dict) and c["dakhil"].get("binya") == "مبتدأ_وخبر"]
    ws = [c for c in allc if isinstance(c["dakhil"], dict) and c["dakhil"].get("binya") == "وصف_ومرفوعه"]
    for f, m in MB_VAL_MIN.items():
        for v in VALS[f]:
            k = sum(1 for c in mb if c["dakhil"].get(f) == v)
            need = m
            if f == "khabar":
                cap = mumkin_khabar(v)
                if cap < m:
                    need = cap
                    notes.append("تنبيه: khabar=%s لا يقبل إلا %d مدخلًا متمايزًا (الحقول الأخرى لا تنطبق)، "
                                 "فالحدّ الأدنى %d في المواصفة غير ممكن مع منع المدخل المكرّر؛ فُحص على %d"
                                 % (v, cap, m, cap))
            if k < need:
                err("مبتدأ_وخبر: %s=%s في %d < %d" % (f, v, k, need))
    for f, m in WS_VAL_MIN.items():
        for v in VALS[f]:
            k = sum(1 for c in ws if c["dakhil"].get(f) == v)
            if k < m:
                err("وصف_ومرفوعه: %s=%s في %d < %d" % (f, v, k, m))
    for deg in ("قليل", "بتأويل"):
        k = sum(1 for c in allc if c["daraja"] == deg or (isinstance(c["daraja"], list) and deg in c["daraja"]))
        if k < 1:
            err("الدرجة %s غير متوقَّعة في أيّ حالة" % deg)
    if npairs < AZWAJ_MIN:
        err("الأزواج %d < %d" % (npairs, AZWAJ_MIN))

    for n in notes:
        print(n)
    if errs:
        for e in errs:
            print("خلل:", e)
        print("فشل: %d خللًا" % len(errs))
        return 1
    print("مرّ: %d حالة، %d زوجًا" % (N, npairs))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
