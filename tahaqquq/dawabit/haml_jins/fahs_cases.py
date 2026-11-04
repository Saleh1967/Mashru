#!/usr/bin/env python3
# فحص ملفّ الحالات لضابط «الحمل من الجنس». الاستعمال: python3 -I fahs_cases.py [cases.json] [masdar.md]
import json, os, re, sys

JINS = {"إنسان", "حيوان", "نبات", "جماد", "غائب"}
QAB = {"السير", "الركض", "الجري", "الزحف", "القفز", "غائب"}
NISBA = {"إسنادية", "إضافية"}
HUKM = {"مرخَّص", "لا_حكم", "ممتنع", "لا_جنس", "لا_مثال"}
FIA = {"موجب", "حد", "خارج", "عموم", "غموض"}
MIN_TOTAL, MAX_TOTAL = 16, 30
QUOTA = {"موجب": 5, "حد": 4, "خارج": 3, "عموم": 2}

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    cases_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "cases.json")
    masdar_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(here, "masdar.md")
    errs = []
    E = errs.append

    try:
        with open(cases_path, "rb") as f:
            cases = json.loads(f.read().decode("utf-8"))
    except Exception as ex:
        print("خطأ: JSON غير صالح: %s" % ex); return 1
    if not isinstance(cases, list):
        print("خطأ: الملفّ ليس قائمة"); return 1

    lines = {}
    with open(masdar_path, "rb") as f:
        for raw in f.read().decode("utf-8").split("\n"):
            m = re.match(r"^(\d+)\. (.*)$", raw)
            if m:
                lines[int(m.group(1))] = m.group(2)

    ids, dakhils = set(), {}
    counts = {k: 0 for k in FIA}
    had_idafiya = had_la_yantaqil = 0
    kharij_h = set()
    ghumud_n = 0

    for i, c in enumerate(cases):
        tag = "حالة #%d" % i
        if not isinstance(c, dict):
            E("%s: ليست كائنًا" % tag); continue
        cid = c.get("id")
        tag = "حالة %s" % cid
        if not (isinstance(cid, str) and re.fullmatch(r"H\d{2}", cid)):
            E("%s: id غير صالح" % tag)
        if cid in ids:
            E("%s: id مكرّر" % tag)
        ids.add(cid)
        for k in ("id", "fia", "mithal", "dakhil", "kharij", "sanad", "taliq"):
            if k not in c:
                E("%s: الحقل %s مفقود" % (tag, k))
        extra = set(c) - {"id", "fia", "mithal", "dakhil", "kharij", "sanad", "taliq"}
        if extra:
            E("%s: حقول زائدة %s" % (tag, sorted(extra)))
        fia = c.get("fia")
        if fia not in FIA:
            E("%s: fia غير مسموح: %r" % (tag, fia)); fia = None
        else:
            counts[fia] += 1
        if not (isinstance(c.get("mithal"), str) and c["mithal"].strip()):
            E("%s: mithal فارغ" % tag)
        if not (isinstance(c.get("taliq"), str) and c["taliq"].strip() and "\n" not in c["taliq"]):
            E("%s: taliq ليس سطرًا واحدًا" % tag)
        d = c.get("dakhil")
        if not isinstance(d, dict) or set(d) != {"jins", "mithal_qab", "nisba"}:
            E("%s: dakhil ناقص أو زائد" % tag); d = {}
        if d.get("jins") not in JINS: E("%s: jins غير مسموح" % tag)
        if d.get("mithal_qab") not in QAB: E("%s: mithal_qab غير مسموح" % tag)
        if d.get("nisba") not in NISBA: E("%s: nisba غير مسموح" % tag)
        kh = c.get("kharij")
        if not isinstance(kh, dict) or set(kh) != {"hukm"}:
            E("%s: kharij يجب أن يحوي hukm وحده" % tag); h = None
        else:
            h = kh["hukm"]
        if fia == "غموض":
            ghumud_n += 1
            if not (isinstance(h, list) and len(h) == 2 and h[0] != h[1] and all(x in HUKM for x in h)):
                E("%s: غموض يتطلّب قائمة بديلين مختلفين مسموحين" % tag)
        else:
            if h not in HUKM:
                E("%s: hukm غير مسموح: %r" % (tag, h))
        if d:
            key = (d.get("jins"), d.get("mithal_qab"), d.get("nisba"))
            if key in dakhils:
                prev = dakhils[key]
                if not (fia == "غموض" or prev == "غموض"):
                    E("%s: dakhil مكرّر" % tag)
                elif (fia == "غموض") == (prev == "غموض"):
                    E("%s: dakhil مكرّر بين حالتي غموض" % tag)
            else:
                dakhils[key] = fia
        # sub-quotas
        if fia == "حد":
            if d.get("nisba") == "إضافية": had_idafiya += 1
            if d.get("jins") in ("جماد", "نبات"): had_la_yantaqil += 1
            if h == "مرخَّص": E("%s: حدّ لا يكون مرخَّصًا" % tag)
        if fia == "خارج":
            if h in ("لا_جنس", "لا_مثال"): kharij_h.add(h)
            else: E("%s: خارج متوقَّعه لا_جنس أو لا_مثال" % tag)
        if fia == "موجب" and h != "مرخَّص": E("%s: موجب متوقَّعه مرخَّص" % tag)
        if fia == "عموم" and h != "مرخَّص": E("%s: عموم متوقَّعه مرخَّص" % tag)
        # sanad
        s = c.get("sanad")
        if not isinstance(s, list):
            E("%s: sanad ليس قائمة" % tag); s = []
        if h == "لا_حكم":
            if s: E("%s: لا_حكم يجب أن يكون بلا سند" % tag)
        else:
            if not s: E("%s: سند فارغ" % tag)
        for j, it in enumerate(s):
            if not (isinstance(it, dict) and set(it) == {"satr", "nass"}):
                E("%s: سند #%d ناقص" % (tag, j)); continue
            n, t = it["satr"], it["nass"]
            if not (isinstance(n, int) and 1 <= n <= 18):
                E("%s: satr خارج 1–18" % tag); continue
            if n not in lines:
                E("%s: السطر %d غير موجود في المصدر" % (tag, n)); continue
            if not (isinstance(t, str) and t and t.encode("utf-8") in lines[n].encode("utf-8")):
                E("%s: nass ليس قطعة حرفيّة من السطر %d" % (tag, n))

    total = len(cases)
    if not (MIN_TOTAL <= total <= MAX_TOTAL):
        E("العدد %d خارج 16–30" % total)
    for k, q in QUOTA.items():
        if counts[k] < q: E("فئة %s: %d أقلّ من %d" % (k, counts[k], q))
    if had_idafiya < 1: E("حد: لا حالة بالنسبة الإضافيّة")
    if had_la_yantaqil < 1: E("حد: لا حالة بجنس لا ينتقل")
    if kharij_h != {"لا_جنس", "لا_مثال"}: E("خارج: يجب أن تجمع لا_جنس ولا_مثال معًا")
    if ghumud_n > 1: E("غموض: أكثر من حالة واحدة")

    print("العدد: %d — %s" % (total, " ".join("%s=%d" % kv for kv in counts.items())))
    for e in errs: print("خطأ: " + e)
    print("النتيجة: " + ("سليم" if not errs else "مرفوض (%d)" % len(errs)))
    return 0 if not errs else 1

if __name__ == "__main__":
    sys.exit(main())
