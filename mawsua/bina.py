"""بناء مخزن الموسوعة (عيّنة أولى) من شبكة المخصّص، بصيغة يقرؤها الفاحص التنفيذيّ (Faahis/Main.lean).

لكلّ زوج في العيّنة ادّعاءان:
١. «اللفظ يدلّ على شرحه مطابقةً» (mutabaqa:لفظ:شرح)، وسلسلته: أصل wad:لفظ:شرح (وسمه «تقدير»: حكاية الوضع عن
   المخصّص بنسبتها، واستخراجها مقدَّر على عيّنة) ثمّ قانون «مطابقة-من-الوضع» (Aql/QawaninDalala.lean).
   الذرّات هي نصّ اللفظ والشرح بعد إبدال «:» و«|» (محجوزتان في الصيغة) بـ«؛» و«/»؛ والنصّ الأصليّ في السند.
٢. «اللفظ مذكور تحت العنوان الأعلى» (taht:z:j)، وسلسلته:
  أصل taht:z<زوج>:j<فصله>  (وسمه «تقدير»: إسناد الزوج إلى فصله استخراجٌ دقّته مقدّرة على عيّنة)
  ثم لكلّ درجة: أصل fi:j<ابن>:j<أب> (وسمه «مفحوص»: شجرة العناوين مختبرة في test_shabaka.py)
              وقانون تعدية (وسمه «مطابق»: قراءةٌ لبنية الكتاب).
فالوسم المعلَن «تقدير»، ولا يجوز أعلى منه: الفاحص يحسبه من السلسلة ويرفض ما علا.

البذرة ثابتة (SEED)، والعيّنة تُعاد بعينها. إن حضر المودَع (MUDAA_MUKHASSAS) فُحصت بصمته
وفُحص أنّ كلّ لفظ في العيّنة موجود في النصّ قرب إزاحته.
التشغيل: python3 -I mawsua/bina.py            → العيّنة (120 زوجًا) في makhzan.tsv (للاختبارات)
          python3 -I mawsua/bina.py --kull     → الأزواج كلّها في makhzan_kamil.tsv (للقارئ)
"""
import hashlib
import json
import os
import random
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "shabaka", "out")
SEED = 20261015
N = 120
ISDAR = "mawsua-0.1"


def load():
    a = json.load(open(os.path.join(OUT, "ajnas.json"), encoding="utf-8"))
    z = json.load(open(os.path.join(OUT, "azwaj.json"), encoding="utf-8"))
    return a["slot"], {j["id"]: j for j in a["ajnas"]}, z


def dharra(t):
    return t.replace("\t", " ").replace(":", "؛").replace("|", "/").strip()


def silsilat_aba(ajnas, j):
    out = []
    while ajnas[j]["parent"] is not None:
        p = ajnas[j]["parent"]
        out.append((j, p))
        j = p
    return out


def main():
    slot, ajnas, azwaj = load()
    txt = None
    mudaa = os.environ.get("MUDAA_MUKHASSAS")
    if mudaa and os.path.exists(mudaa):
        raw = open(mudaa, "rb").read()
        if hashlib.sha256(raw).hexdigest() != slot["sha256"]:
            sys.exit("المودَع تغيّرت بصمته: يُرفض")
        txt = raw.decode("utf-8")

    murashshah = [z for z in azwaj if z["lafz"].strip() and silsilat_aba(ajnas, z["jins"])]
    kull = "--kull" in sys.argv
    ayyina = murashshah if kull else random.Random(SEED).sample(murashshah, N)
    ism = "makhzan_kamil.tsv" if kull else "makhzan.tsv"

    qawanin, qidx, usul = [], {}, {}
    iddiaat = []
    ghaib = 0
    for z in ayyina:
        if txt is not None:
            o = z["off"]
            if z["lafz"].split()[-1] not in txt[max(0, o - 400): o + 400]:
                ghaib += 1
        sanad = f"{slot['sha256'][:12]}@{z['off']}/{z['page']}/{z['lafz']}"
        # ١. الدلالة: وضعٌ محكيّ ثمّ مطابقة
        wd = f"wad:{dharra(z['lafz'])}:{dharra(z['sharh'])}"
        mt = f"mutabaqa:{dharra(z['lafz'])}:{dharra(z['sharh'])}"
        usul.setdefault(wd, ("تقدير", sanad + (f"/قائل:{z['qail']}" if z.get("qail") else "/بلا-نسبة")))
        key = (wd, mt)
        if key not in qidx:
            qidx[key] = len(qawanin)
            qawanin.append(("مطابقة-من-الوضع", wd, mt))
        iddiaat.append((mt, "تقدير", f"a={wd}|q={qidx[key]}", sanad))
        # ٢. البنية: تحت العنوان الأعلى
        hadir = f"taht:z{z['id']}:j{z['jins']}"
        usul.setdefault(hadir, ("تقدير", sanad))
        steps = [f"a={hadir}"]
        for c, p in silsilat_aba(ajnas, z["jins"]):
            fi = f"fi:j{c}:j{p}"
            usul.setdefault(fi, ("مفحوص", f"{slot['sha256'][:12]}@{ajnas[c]['off']}/{ajnas[c]['title']}"))
            nat = f"taht:z{z['id']}:j{p}"
            key = (hadir, fi, nat)
            if key not in qidx:
                qidx[key] = len(qawanin)
                qawanin.append(("تعدية-الاحتواء", f"{hadir}|{fi}", nat))
            steps += [f"a={fi}", f"q={qidx[key]}"]
            hadir = nat
        iddiaat.append((hadir, "تقدير", "|".join(steps), sanad))

    lines = [f"isdar\t{ISDAR}"]
    lines += [f"qanun\t{ism}\t{muq}\t{n}\tمطابق" for (ism, muq, n) in qawanin]
    lines += [f"asl\t{p}\t{w}\t{s}" for p, (w, s) in usul.items()]
    lines += [f"iddia\t{p}\t{w}\t{k}\t{s}" for p, w, k, s in iddiaat]
    open(os.path.join(ROOT, "mawsua", ism), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"قوانين {len(qawanin)}، أصول {len(usul)}، ادّعاءات {len(iddiaat)}"
          + (f"، ألفاظ لم توجد قرب إزاحتها {ghaib}" if txt is not None else "، المودَع غير حاضر"))
    if txt is not None and ghaib:
        sys.exit(1)


if __name__ == "__main__":
    main()
