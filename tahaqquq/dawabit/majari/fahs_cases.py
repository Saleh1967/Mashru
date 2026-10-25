#!/usr/bin/env python3
"""فاحص cases.json لضابط «هذا باب مجارى أواخر الكلم من العربية» (على wasf.md).

الاستعمال:
    python3 -I fahs_cases.py [cases.json] [sibawayhi.txt]

يخرج 0 إن مرّت الفحوص كلّها، و1 إن فشل فحصٌ (ويطبع كلَّ خللٍ باسمه)، و2 إن تعذّرت قراءة ملفّ.
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

SATR_MIN, SATR_MAX = 111, 233
N_MIN, N_MAX = 30, 40
QUOTA = {"موجب": 10, "حد": 5, "خارج": 5, "عموم": 4, "غموض": 2}
FIAT = set(QUOTA)
ASNAF = {
    "اسم_متمكن", "اسم_لا_ينصرف", "اسم_لا_ينصرف_معرف", "مثنى", "جمع_مذكر", "جمع_مؤنث",
    "مضارع", "مضارع_ساكن_الآخر", "مضارع_اثنين", "مضارع_جمع", "مضارع_مخاطبة", "مضارع_نسوة",
    "ماض", "أمر", "غير_متمكن",
}
MAWADI = {"رفع", "نصب", "جر", "جزم", "بلا_عامل"}
ALAMAT = {"ضمة", "فتحة", "كسرة", "سكون", "ألف", "واو", "ياء", "ثبات_النون", "حذف_النون", "حذف_الآخر"}
NAFY = {"لا_يكون", "لا_حكم"}
CASE_KEYS = {"id", "fia", "mithal", "mithal_harfi", "dakhil", "kharij", "sanad", "taliq"}
DAKHIL_KEYS = {"sinf", "lafz", "mawdi"}
TASHKIL = re.compile("[ً-ْٰ]")
ID_RE = re.compile(r"^M[0-9]{2}$")

errors = []


def err(where, msg):
    errors.append(f"{where}: {msg}")


def strip_prefix(line):
    if line.startswith("~~"):
        return line[2:]
    if line.startswith("# "):
        return line[2:]
    return None


def main():
    try:
        raw = open(SOURCE, "rb").read()
    except OSError as e:
        print(f"تعذّرت قراءة المصدر: {e}")
        return 2
    sha = hashlib.sha256(raw).hexdigest()
    if sha != SOURCE_SHA:
        err("المصدر", f"البصمة {sha} غير بصمة المواصفة")
    lines = raw.decode("utf-8").split("\n")

    def satr_text(n):
        s = lines[n - 1]
        if s.endswith("\r"):
            s = s[:-1]
        return strip_prefix(s)

    try:
        text = open(CASES, "rb").read().decode("utf-8")
    except (OSError, UnicodeDecodeError) as e:
        print(f"تعذّرت قراءة الحالات: {e}")
        return 2
    try:
        cases = json.loads(text)
    except json.JSONDecodeError as e:
        err("JSON", f"غير صالح: {e}")
        report()
        return 1
    if not isinstance(cases, list):
        err("JSON", "ليس قائمة")
        report()
        return 1

    ids = set()
    dakhils = {}
    counts = {f: 0 for f in FIAT}

    for i, c in enumerate(cases):
        w = f"#{i}"
        if not isinstance(c, dict):
            err(w, "العنصر ليس كائنًا")
            continue
        cid = c.get("id")
        if isinstance(cid, str):
            w = cid
        keys = set(c)
        if keys != CASE_KEYS:
            err(w, f"المفاتيح {sorted(keys ^ CASE_KEYS)} زائدة أو ناقصة")
        # id
        if not isinstance(cid, str) or not ID_RE.match(cid):
            err(w, f"id غير صالح: {cid!r}")
        elif cid in ids:
            err(w, "id مكرَّر")
        else:
            ids.add(cid)
        # fia
        fia = c.get("fia")
        if fia not in FIAT:
            err(w, f"fia غير مسموح: {fia!r}")
        else:
            counts[fia] += 1
        # mithal
        mithal = c.get("mithal")
        if not isinstance(mithal, str) or not mithal.strip():
            err(w, "mithal فارغ أو ليس نصًّا")
            mithal = ""
        elif TASHKIL.search(mithal):
            err(w, "mithal مشكول")
        mh = c.get("mithal_harfi")
        if not isinstance(mh, bool):
            err(w, "mithal_harfi ليس منطقيًّا")
        # dakhil
        d = c.get("dakhil")
        if not isinstance(d, dict) or set(d) != DAKHIL_KEYS:
            err(w, "dakhil ناقص أو زائد المفاتيح")
        else:
            sinf, lafz, mawdi = d.get("sinf"), d.get("lafz"), d.get("mawdi")
            if sinf not in ASNAF:
                err(w, f"sinf غير مسموح: {sinf!r}")
            if mawdi not in MAWADI:
                err(w, f"mawdi غير مسموح: {mawdi!r}")
            if not isinstance(lafz, str):
                err(w, "lafz ليس نصًّا")
            elif sinf == "غير_متمكن":
                if not lafz.strip():
                    err(w, "lafz فارغ مع غير_متمكن")
                elif TASHKIL.search(lafz):
                    err(w, "lafz مشكول")
            elif lafz != "":
                err(w, "lafz غير فارغ مع صنفٍ غير غير_متمكن")
            key = (sinf, lafz, mawdi)
            if key in dakhils:
                err(w, f"dakhil مكرَّر مع {dakhils[key]}")
            else:
                dakhils[key] = w
        # kharij
        k = c.get("kharij")
        alama = None
        if not isinstance(k, dict) or "alama" not in k:
            err(w, "kharij بلا alama")
        else:
            alama = k["alama"]
            if isinstance(alama, str):
                if alama not in NAFY:
                    err(w, f"alama نصٌّ غير مسموح: {alama!r}")
                if set(k) != {"alama"}:
                    err(w, "bina (أو غيره) حاضر مع لا_يكون/لا_حكم")
            elif isinstance(alama, list):
                if not alama:
                    err(w, "alama قائمة فارغة")
                for a in alama:
                    if a not in ALAMAT:
                        err(w, f"علامة غير مسموحة: {a!r}")
                if len(set(alama)) != len(alama):
                    err(w, "علامة مكرَّرة في القائمة")
                if set(k) != {"alama", "bina"}:
                    err(w, "kharij: مع القائمة يلزم bina وحده")
                elif not isinstance(k["bina"], bool):
                    err(w, "bina ليس منطقيًّا")
            else:
                err(w, "alama ليست قائمة ولا نصًّا")
        # fia ↔ alama
        if fia == "حد" and alama != "لا_يكون":
            err(w, "حد ومتوقَّعه غير لا_يكون")
        if fia == "خارج" and alama != "لا_حكم":
            err(w, "خارج ومتوقَّعه غير لا_حكم")
        if fia in ("موجب", "عموم") and not isinstance(alama, list):
            err(w, f"{fia} ومتوقَّعه ليس قائمة علامات")
        if fia == "غموض" and not (isinstance(alama, list) and len(alama) >= 2):
            err(w, "غموض بلا علامتين")
        if fia != "حد" and alama == "لا_يكون":
            err(w, "لا_يكون في غير فئة حد")
        if fia != "خارج" and alama == "لا_حكم":
            err(w, "لا_حكم في غير فئة خارج")
        # sanad
        s = c.get("sanad")
        sanad_texts = []
        if not isinstance(s, list):
            err(w, "sanad ليس قائمة")
            s = []
        if alama == "لا_حكم":
            if s:
                err(w, "لا_حكم وله سند")
        elif not s:
            err(w, "حكمٌ بلا سند")
        prev = 0
        for j, p in enumerate(s):
            pw = f"{w}.sanad[{j}]"
            if not isinstance(p, dict) or set(p) != {"satr", "nass"}:
                err(pw, "قطعة السند ناقصة أو زائدة المفاتيح")
                continue
            n, nass = p["satr"], p["nass"]
            if not isinstance(n, int) or isinstance(n, bool):
                err(pw, "satr ليس عددًا")
                continue
            if not (SATR_MIN <= n <= SATR_MAX):
                err(pw, f"السطر {n} خارج النطاق {SATR_MIN}–{SATR_MAX}")
                continue
            if n < prev:
                err(pw, "أسطر السند غير مرتّبة")
            prev = n
            st = satr_text(n)
            if st is None:
                err(pw, f"السطر {n} بلا بادئة «~~» أو «# »")
                continue
            sanad_texts.append(st)
            if not isinstance(nass, str) or not nass.strip():
                err(pw, "nass فارغ")
                continue
            if "\n" in nass or "\r" in nass:
                err(pw, "nass يعبر سطرين")
                continue
            if nass not in st:
                err(pw, f"nass ليس قطعةً حرفيّة من السطر {n}")
        # mithal_harfi
        if mh is True:
            if not sanad_texts:
                err(w, "mithal_harfi=true بلا سند")
            elif mithal and not any(mithal in t for t in sanad_texts):
                err(w, "mithal_harfi=true والمثال ليس في أيّ سطرٍ من أسطر السند")
        # taliq
        t = c.get("taliq")
        if not isinstance(t, str) or not t.strip():
            err(w, "taliq فارغ")
        elif "\n" in t or "\r" in t:
            err(w, "taliq أكثر من سطر")

    n = len(cases)
    if not (N_MIN <= n <= N_MAX):
        err("العدد", f"{n} خارج {N_MIN}–{N_MAX}")
    for f, q in QUOTA.items():
        if counts[f] < q:
            err("الحصص", f"{f}: {counts[f]} < {q}")

    report(n, counts)
    return 1 if errors else 0


def report(n=None, counts=None):
    if n is not None:
        print(f"الحالات: {n}")
        print("الفئات: " + "، ".join(f"{f} {counts[f]}" for f in QUOTA))
    if errors:
        print(f"فشل: {len(errors)} خلل")
        for e in errors:
            print("  - " + e)
    else:
        print("مرّ: كلّ الفحوص")


if __name__ == "__main__":
    sys.exit(main())
