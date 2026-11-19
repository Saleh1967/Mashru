#!/usr/bin/env python3
"""تجربةُ الجواب: المحوِّل من مخرج `rabt` إلى جواب المحرّك، والعدُّ بأصناف المواصفة (wasf.md §العدّ).

كُتب قبل الحالات، ولا يتغيّر بعدها إلّا إصلاحَ خللٍ يخالف نصَّ المواصفة يُعلَن في السجلّ التالي.

التشغيل: python3 -I tashghil.py <cases.json> <rabt> <jins.tsv> <mithal.tsv> <luzum.tsv> <natija.json> [--iltizam <sha>]
"""
import hashlib, json, os, re, subprocess, sys, tempfile

NAW = ("hukm", "fail", "irab", "jidhr", "quwwa")


def basma(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def shaghghil(rabt, jadawil, jumla):
    with tempfile.TemporaryDirectory() as d:
        f = os.path.join(d, "j.tsv")
        open(f, "w", encoding="utf-8").write("j\t" + jumla + "\n")
        jins, mithal, luzum = jadawil
        p = subprocess.run([rabt, "--jins", jins, "--mithal", mithal, luzum, f],
                           capture_output=True, text=True, timeout=600)
    if p.returncode != 0:
        raise SystemExit("rabt فشل: " + p.stderr[-500:])
    return p.stdout


def qira(out, jumla):
    """مخرجُ rabt لجملةٍ واحدة ← (الحكم، أسطر الجسم)."""
    hukm, jism = None, []
    for s in out.split("\n"):
        if s.startswith("j\t"):
            hukm = s.split("\t")[2].strip()
        elif hukm is not None and s.startswith("  "):
            jism.append(s)
    return hukm, jism


def jawab(naw, kalima, jumla, hukm, jism):
    """جوابُ المحرّك: مجموعةُ قيم، أو مجموعةٌ فارغة إن لم يُجب."""
    if naw == "hukm":
        return {hukm} if hukm in ("مقبول", "خطأ") else set()
    if hukm != "مقبول":
        return set()
    kalimat = jumla.split(" ")
    hadaf = kalimat[kalima - 1] if kalima else None
    out = set()
    for s in jism:
        if naw == "fail" and s.startswith("  الإسناد"):
            m = re.search(r"والمسند إليه «([^»]+)»", s)
            if m:
                out.add(m.group(1))
            elif "والمسند إليه ضميرٌ مستتر" in s:
                out.add("مستتر")
        elif naw == "irab" and s.startswith("  " + hadaf + "\t"):
            out.add(s.split("\t")[2].strip())
        elif naw == "jidhr" and s.startswith("  الدلالة: «" + str(hadaf) + "» مرشَّحُ جذره "):
            out.add(s.split("مرشَّحُ جذره ")[1].split(" ")[0])
        elif naw == "quwwa" and s.startswith("  القوّة: "):
            q = s[len("  القوّة: "):].split(" —")[0].strip()
            q = q.replace("خبرٌ مثبت", "خبر مثبت").replace("خبرٌ منفيّ", "خبر منفي")
            out.add(q)
    return out


def sinf(mutawaqqa, j):
    mt = set(mutawaqqa) if isinstance(mutawaqqa, list) else {mutawaqqa}
    if not j:
        return "نقص تغطية"
    if j == mt:
        return "صواب"
    if mt <= j or (mt & j):
        return "اختيار بلا مرجّح" if len(mt) == 1 else "خطأ"
    return "خطأ"


def main(a):
    cases_p, rabt, jins, mithal, luzum, out_p = a[:6]
    iltizam = a[a.index("--iltizam") + 1] if "--iltizam" in a else None
    cases = json.load(open(cases_p, encoding="utf-8"))
    nataij, ihsa = [], {}
    for c in cases:
        out = shaghghil(rabt, (jins, mithal, luzum), c["jumla"])
        hukm, jism = qira(out, c["jumla"])
        j = jawab(c["naw"], c.get("kalima"), c["jumla"], hukm, jism)
        s = sinf(c["mutawaqqa"], j)
        nataij.append({"id": c["id"], "naw": c["naw"], "jawab": sorted(j), "sinf": s})
        ihsa.setdefault(c["naw"], {}).setdefault(s, 0)
        ihsa[c["naw"]][s] += 1
    kull = {}
    for n in ihsa.values():
        for k, v in n.items():
            kull[k] = kull.get(k, 0) + v
    ajab = sum(v for k, v in kull.items() if k != "نقص تغطية")
    sijill = {
        "cases_sha256": basma(cases_p), "tashghil_sha256": basma(__file__),
        "rabt_sha256": basma(rabt), "jadawil_sha256": {os.path.basename(p): basma(p) for p in (jins, mithal, luzum)},
        "iltizam": iltizam, "kull": kull, "sawab_min_100": kull.get("صواب", 0),
        "sawab_mimma_ajab": [kull.get("صواب", 0), ajab], "ala_naw": ihsa, "nataij": nataij,
    }
    json.dump(sijill, open(out_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({"kull": kull, "ala_naw": ihsa}, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1:])
