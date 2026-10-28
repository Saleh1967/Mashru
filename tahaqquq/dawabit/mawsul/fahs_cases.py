"""فاحص cases.json لضابط الموصول وصلته (على wasf.md).
الاستعمال: python3 -I fahs_cases.py <cases.json> <مجلد المصدرين>
يخرج 0 إن مرّ كلّ شيء، و1 إن وُجد خلل (ويطبع كلّ خلل)، و2 لخطأ في الاستدعاء.
"""
import hashlib, json, os, re, sys

BASMA = {
    "qatr.txt": "2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d",
    "alfiyya.txt": "13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0",
}
MASDAR = {"قطر": ("qatr.txt", 137, 143), "ألفية": ("alfiyya.txt", 146, 157)}

MAWSUL = ["الذي", "التي", "اللذان", "اللتان", "اللذين", "اللتين", "اللذيان", "اللتيان", "الذين",
          "اللذون", "الألى", "اللائي", "اللاتي", "اللات", "اللاء", "من", "ما", "أي", "أل", "ذو", "ذات",
          "ذوات", "ذا"]
MARJI = ["مفرد_مذكر", "مفرد_مؤنث", "مثنى_مذكر", "مثنى_مؤنث", "جمع_مذكر", "جمع_مؤنث"]
MAWDI = ["رفع", "نصب", "جر"]
LUGHA = ["غير_مذكورة", "طيئ"]
QABL = ["ما_الاستفهامية", "من_الاستفهامية", "غيرهما"]
SILA = ["جملة_خبرية", "جملة_إنشائية", "ظرف_تام", "ظرف_ناقص", "جار_مجرور_تام", "جار_مجرور_ناقص",
        "وصف_صريح", "اسم_تفضيل", "فعل_معرب", "لا_صلة"]
AID = ["ظاهر", "مستتر", "محذوف", "لا_عائد"]
AID_SIMA = MARJI + ["لا_عائد"]
FIA = ["موجب", "حد", "خارج", "عموم", "غموض"]
HUKM = ["مقبول", "خطأ", "لا_حكم"]
DARAJA_Q = ["قليل", "نزر", "لغة", "بلا_درجة"]
KEYS = ["id", "fia", "mithal", "mithal_harfi", "dakhil", "hukm", "daraja", "zawj", "sanad", "taliq"]
DKEYS = ["mawsul", "marji", "mawdi", "tashdid", "lugha", "qabl", "mulgha", "sila", "aid", "aid_sima"]
ENUM = {"mawsul": MAWSUL, "marji": MARJI, "mawdi": MAWDI, "lugha": LUGHA, "qabl": QABL, "sila": SILA,
        "aid": AID, "aid_sima": AID_SIMA}
MAWDI_LAFZ = {"اللذان", "اللتان", "اللذين", "اللتين", "اللذيان", "اللتيان", "الذين", "اللذون"}


def strip_prefix(line):
    for p in ("### | ", "~~", "# "):
        if line.startswith(p):
            return line[len(p):]
    return line


def main():
    if len(sys.argv) != 3:
        print("الاستعمال: fahs_cases.py <cases.json> <مجلد المصدرين>")
        return 2
    path, src = sys.argv[1], sys.argv[2]
    err = []

    def e(msg):
        err.append(msg)

    lines = {}
    for m, (fn, a, b) in MASDAR.items():
        raw = open(os.path.join(src, fn), "rb").read()
        h = hashlib.sha256(raw).hexdigest()
        if h != BASMA[fn]:
            e("بصمة %s %s لا تطابق المواصفة" % (fn, h))
        lines[m] = raw.decode("utf-8").split("\n")

    try:
        with open(path, "rb") as f:
            data = json.loads(f.read().decode("utf-8"))
    except Exception as x:  # noqa: BLE001
        print("JSON غير صالح:", x)
        return 1
    if not isinstance(data, list):
        print("الملفّ ليس قائمة")
        return 1

    byid = {}
    for i, c in enumerate(data):
        tag = c.get("id", "#%d" % i) if isinstance(c, dict) else "#%d" % i
        if not isinstance(c, dict) or list(c.keys()) != KEYS:
            e("%s: المفاتيح ليست %s" % (tag, KEYS))
            continue
        if not isinstance(c["id"], str) or not re.fullmatch(r"M\d\d", c["id"]):
            e("%s: id غير صالح" % tag)
        if c["id"] in byid:
            e("%s: id مكرّر" % tag)
        byid[c["id"]] = c
        fia = c["fia"]
        if fia not in FIA:
            e("%s: fia" % tag)
        if not isinstance(c["mithal"], str) or not c["mithal"] or "\n" in c["mithal"]:
            e("%s: mithal" % tag)
        if not isinstance(c["mithal_harfi"], bool):
            e("%s: mithal_harfi ليس منطقيًّا" % tag)
        if not isinstance(c["taliq"], str) or not c["taliq"].strip() or "\n" in c["taliq"]:
            e("%s: taliq ليس سطرًا واحدًا" % tag)
        d = c["dakhil"]
        if not isinstance(d, dict) or list(d.keys()) != DKEYS:
            e("%s: مفاتيح dakhil" % tag)
            continue
        for k, allowed in ENUM.items():
            if d[k] not in allowed:
                e("%s: %s=%r غير مسموح" % (tag, k, d[k]))
        for k in ("tashdid", "mulgha"):
            if not isinstance(d[k], bool):
                e("%s: %s ليس منطقيًّا" % (tag, k))
        if d["tashdid"] is True and not str(d["mawsul"]).endswith("ن"):
            e("%s: tashdid في لفظ لا ينتهي بنون" % tag)
        if d["mulgha"] is True and d["mawsul"] != "ذا":
            e("%s: mulgha في غير ذا" % tag)
        if (d["aid"] == "لا_عائد") != (d["aid_sima"] == "لا_عائد"):
            e("%s: aid_sima=لا_عائد إن وفقط إن aid=لا_عائد" % tag)
        # الحكم والدرجة
        h, dr = c["hukm"], c["daraja"]
        if fia == "غموض":
            if not (isinstance(h, list) or isinstance(dr, list)):
                e("%s: غموض بلا بديلين" % tag)
        else:
            if isinstance(h, list) or isinstance(dr, list):
                e("%s: قائمة في غير غموض" % tag)
        if isinstance(h, list):
            if len(h) != 2 or len(set(h)) != 2 or not set(h) <= {"مقبول", "خطأ"}:
                e("%s: hukm قائمة غير صالحة" % tag)
            if isinstance(dr, list):
                e("%s: قائمتان في hukm وdaraja" % tag)
            elif "مقبول" in h and dr not in DARAJA_Q:
                e("%s: daraja" % tag)
        else:
            if h not in HUKM:
                e("%s: hukm" % tag)
            if h == "مقبول":
                if isinstance(dr, list):
                    if len(dr) != 2 or len(set(dr)) != 2 or not set(dr) <= set(DARAJA_Q):
                        e("%s: daraja قائمة غير صالحة" % tag)
                elif dr not in DARAJA_Q:
                    e("%s: daraja" % tag)
            elif dr != "بلا_درجة":
                e("%s: daraja يجب بلا_درجة حين hukm=%s" % (tag, h))
        # الفئة والحكم
        want = {"موجب": "مقبول", "حد": "خطأ", "خارج": "لا_حكم"}.get(fia)
        if want and h != want:
            e("%s: فئة %s وحكم %r" % (tag, fia, h))
        if fia == "عموم" and h not in ("مقبول", "خطأ"):
            e("%s: عموم بلا حكم" % tag)
        # السند
        sn = c["sanad"]
        if not isinstance(sn, list):
            e("%s: sanad ليس قائمة" % tag)
            continue
        if h == "لا_حكم":
            if sn:
                e("%s: لا_حكم وله سند" % tag)
        elif not sn:
            e("%s: حكم بلا سند" % tag)
        full = []
        for p in sn:
            if not isinstance(p, dict) or sorted(p.keys()) != ["masdar", "nass", "satr"]:
                e("%s: قطعة سند بمفاتيح خاطئة" % tag)
                continue
            if p["masdar"] not in MASDAR:
                e("%s: masdar" % tag)
                continue
            fn, a, b = MASDAR[p["masdar"]]
            s = p["satr"]
            if not isinstance(s, int) or isinstance(s, bool) or not (a <= s <= b):
                e("%s: السطر %r خارج النطاق %d-%d" % (tag, s, a, b))
                continue
            t = strip_prefix(lines[p["masdar"]][s - 1])
            full.append(t)
            n = p["nass"]
            if not isinstance(n, str) or not n or "\n" in n:
                e("%s: nass فارغ أو يعبر سطرين" % tag)
            elif n.encode("utf-8") not in t.encode("utf-8"):
                e("%s: nass ليس قطعة من %s س%d: %r" % (tag, p["masdar"], s, n))
        present = any(c["mithal"] in t for t in full)
        if c["mithal_harfi"] is True and not present:
            e("%s: mithal_harfi=true والمثال ليس في أسطر السند" % tag)
        if c["mithal_harfi"] is False and present:
            e("%s: mithal_harfi=false والمثال بحروفه في سطر سند" % tag)

    if err:
        for x in err:
            print("خلل:", x)
        return 1

    # الأعداد والحدود
    cnt = lambda pred: sum(1 for c in data if pred(c))  # noqa: E731
    if not 45 <= len(data) <= 60:
        e("العدد %d خارج 45-60" % len(data))
    for f, mn in (("موجب", 14), ("حد", 12), ("خارج", 5), ("عموم", 6), ("غموض", 2)):
        if cnt(lambda c: c["fia"] == f) < mn:
            e("فئة %s أقلّ من %d" % (f, mn))
    for w in MAWSUL:
        if cnt(lambda c: c["dakhil"]["mawsul"] == w) < 1:
            e("اللفظ %s بلا حالة" % w)
    for v in MARJI:
        if cnt(lambda c: c["dakhil"]["marji"] == v) < 3:
            e("marji %s أقلّ من 3" % v)
    for v in MAWDI:
        if cnt(lambda c: c["dakhil"]["mawdi"] == v and c["dakhil"]["mawsul"] in MAWDI_LAFZ) < 3:
            e("mawdi %s في المثنى/الذين/اللذون أقلّ من 3" % v)
    for v in SILA:
        if cnt(lambda c: c["dakhil"]["sila"] == v) < 2:
            e("sila %s أقلّ من 2" % v)
    for v in AID:
        if cnt(lambda c: c["dakhil"]["aid"] == v) < 3:
            e("aid %s أقلّ من 3" % v)
    if cnt(lambda c: c["dakhil"]["tashdid"] is True) < 3:
        e("tashdid أقلّ من 3")
    if cnt(lambda c: c["dakhil"]["lugha"] == "طيئ") < 4:
        e("طيئ أقلّ من 4")
    if cnt(lambda c: c["dakhil"]["qabl"] != "غيرهما") < 4:
        e("qabl أقلّ من 4")
    if cnt(lambda c: c["dakhil"]["mulgha"] is True) < 2:
        e("mulgha أقلّ من 2")

    def has_daraja(c, v):
        dr = c["daraja"]
        return v in dr if isinstance(dr, list) else dr == v
    for v in ("قليل", "نزر", "لغة"):
        if cnt(lambda c: has_daraja(c, v)) < 1:
            e("الدرجة %s غير متوقَّعة في حالة" % v)
    # تكرار المدخل
    seen = {}
    for c in data:
        k = json.dumps(c["dakhil"], ensure_ascii=False, sort_keys=True)
        if k in seen:
            e("مدخل مكرّر: %s و%s" % (seen[k], c["id"]))
        seen[k] = c["id"]
    # الأزواج
    def verdict(c):
        return json.dumps([c["hukm"], c["daraja"]], ensure_ascii=False)
    pairs = 0
    for c in data:
        z = c["zawj"]
        if z is None:
            continue
        if z not in byid:
            e("%s: zawj %r غير موجود" % (c["id"], z))
            continue
        o = byid[z]
        if o["zawj"] != c["id"]:
            e("%s: zawj غير متبادل" % c["id"])
        if z == c["id"]:
            e("%s: zawj نفسه" % c["id"])
        diff = [k for k in DKEYS if c["dakhil"][k] != o["dakhil"][k]]
        if len(diff) != 1:
            e("%s↔%s: يختلفان في %d حقول" % (c["id"], z, len(diff)))
        if verdict(c) == verdict(o):
            e("%s↔%s: الحكم والدرجة سواء" % (c["id"], z))
        pairs += 1
    if pairs // 2 < 8:
        e("الأزواج %d أقلّ من 8" % (pairs // 2))

    if err:
        for x in err:
            print("خلل:", x)
        return 1
    print("سليم: %d حالة، %d زوجًا" % (len(data), pairs // 2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
