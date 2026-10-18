"""ترجيحُ معنى كلّ جذرٍ من شبكة المالك بقواعد النبهاني (مرآةُ `Madlul/Tarjih.lean` على المودَعات المختومة).

المعاني (تعيين البنّاء، T1–T3):
  T1 الأوّل: جملةُ أصل ابن فارس في أوّل مادّة الجذر في المقاييس (R4 في jadwal_luzum).
  T2 المأخوذُ بعلاقة: كلُّ جملةٍ في مادّة الجذر في المقاييس فيها علامةُ الحمل على الأصل عند ابن فارس: «ومن الباب»، «ومنه»، «ومن ذلك»،
     «محمول على» — فالعلاقةُ مشهودةٌ بنصّه (والمجاز والنقل أولى من الاشتراك: ج3 س486–487).
  الوحدة: الأصلُ وما يليه من جمل حتّى أوّل علامة حمل (أمثلتُه المباشرة «من ذلك العقل…»)، وكلُّ علامة حملٍ وما يليها حتّى التالية.
  T3 القرينة: للمعنى قرينةٌ إن ذكرت وحدتُه جذرًا آخرَ من شبكة المالك (السياق) — القرينةُ الضيّقة؛ وبـ --lisan تتّسع: أو ذكره تفسيرٌ في
     مادّة الجذر في اللسان يشارك الوحدةَ جذرًا من مضمونها. والنتيجتان تُعرضان معًا (اختيارُ السعة تعيينٌ لا نصّ).
القرارُ `tarjih` نفسُه في Lean (مرآةٌ بالقاعدة لا بالمخرج).
**الحال: أداةُ استكشافٍ لا مقياس.** الوضعان (المقاييس T1–T3، و--lisan-maani بمفتاح المصدر S1–S4) لا يُعتمد مخرجُهما حكمًا: القرينةُ
في فقرات ابن فارس الطويلة كثيرةُ الصدفة، وأدلّةُ اللسان الحاسمة كثيرًا ما تأتي بلا «:» («ودرس الكتاب يدرسه … من ذلك، كأنه…»،
«ودرست الكتاب أدرسه درسا أي ذللته…») فلا يلتقطها نمطُ التفسير. فحكمُ «درس» في Lean مبنيٌّ على أسطرٍ مقروءةٍ يدويًّا بأرقامها. وتنبيه: الترجيحُ بالقرينة **تفسيرٌ للاستعمال** لا اختبارٌ لفرضيّة
الشبكة — اختيارُ المعنى المتّصل بالسياق ثمّ عدُّ الصلات به دَور؛ اختبارُ الفرضيّة يبقى على العُقَد بلا سياق (H3 في hiss.py).
التشغيل: MUDAA_DIR=<مجلّد> python3 -I shabaka/tarjih.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jadwal_luzum as J  # noqa: E402

SABAA = ["كتب", "درس", "قلم", "علم", "فهم", "طلب", "عقل"]
HAML = re.compile(r"ومن الباب|ومنه|ومن ذلك|محمول علي")


def tarjih(ms):
    """مرآةُ Tarjih.tarjih: ms قائمةُ (اسم، أوّل، علاقة، قرينة)."""
    aw = [m for m in ms if m[1]]
    if len(aw) == 1:
        a = aw[0]
        if all(m[1] or m[2] for m in ms):
            q = [m for m in ms if not m[1] and m[3]]
            if len(q) == 1:
                return ("mana", q[0][0])
            if not q:
                return ("mana", a[0])
            return ("mushtarak", [m[0] for m in q])
        rest = [m for m in ms if m[1] or not m[2]]
        q = [m for m in rest if m[3]]
        if len(q) == 1:
            return ("mana", q[0][0])
        return ("mushtarak", [m[0] for m in (q or rest)])
    if not aw:
        return ("laHukm", None)
    q = [m for m in aw if m[3]]
    if len(q) == 1:
        return ("mana", q[0][0])
    return ("mushtarak", [m[0] for m in (q or aw)])


def judhur(Jd, s, R):
    return {r for t in J.kalimat(s) for r in Jd.mursh(t)} - {R}


TAFSIR = re.compile(r"(?:^|[،,\s])((?:[\u0621-\u064A\u064B-\u0652]+ ?){1,2}): ([^:]+?)(?=$|[.؛]| [\u0621-\u064A\u064B-\u0652]+:)")
ALAQA = re.compile(r"من ذلك|كانه|ومنه|ومن هذا|مشتق")


def maani_lisan(Jd, R, jumal, asl_judhur, siyaq):
    """معاني اللفظ R نفسِه في اللسان بمفتاح سيبويه (S1–S4، الكتاب س247–251: المصدرُ يفرّق المعنى):
    S1 حدٌّ: من آخر حدٍّ «. ؛ :» إلى آخر التفسير، وفيه R بعينه (الفعلُ المجرّد أو مصدرُه بصورته) قبل النقطتين.
    S2 مفتاحُ المعنى: صيغُ R في الحدّ بعد مضارعه (يفعل/تفعل) — مصادرُه («يدرس دروسا» / «يدرسه درسا ودراسة»)؛ والحدودُ تتّحد معنًى
       بمصدرٍ مشترك، ولا تتّحد بالفعل وحده (هو اللفظُ المتّفق).
    S3 أوّلٌ: معنًى في تفسيره جذرٌ من جذور أصل ابن فارس؛ مأخوذٌ بعلاقة: في حدّه «من ذلك/كأنه/ومنه»؛ قرينة: في حدّه جذرٌ من السياق.
    S4 الحدُّ بلا مصدر يبقى معنًى وحده (لا يُضمّ تخمينًا)."""
    hudud = []
    for no, s, satr_at in jumal:
        for mm in TAFSIR.finditer(s):
            bnd = max(s.rfind(c, 0, mm.start(1)) for c in ".؛:")
            had = s[bnd + 1:mm.end(1)]
            tok = [J.norm(t) for t in J.kalimat(had)]
            if not any(J.qanun_sigha(t, R) == R or t == R for t in tok):
                continue
            mud = [i for i, t in enumerate(tok) if t[:1] in "يت" and R in Jd.mursh(t)]
            masadir = {J.qanun_sigha(t, R) for t in tok[mud[0] + 1:] if R in Jd.mursh(t)} if mud else set()
            G = mm.group(2)
            hudud.append({"satr": satr_at(mm.start(1)), "nass": (had + ": " + G)[:110], "masadir": masadir,
                          "tafsir": judhur(Jd, G, R), "alaqa": bool(ALAQA.search(J.norm(had + " " + G))),
                          "qarina": bool(judhur(Jd, had + " " + G, R) & siyaq)})
    # الاتّحاد بالمصدر المشترك
    maani = []
    for h in hudud:
        hit = [m for m in maani if h["masadir"] and m["masadir"] & h["masadir"]]
        if hit:
            m = hit[0]
            m["masadir"] |= h["masadir"]
            m["hudud"].append(h)
        else:
            maani.append({"masadir": set(h["masadir"]), "hudud": [h]})
    out = []
    for m in maani:
        taf = set().union(*[h["tafsir"] for h in m["hudud"]])
        out.append({"ism": f"{sorted(m['masadir']) or '-'} س{m['hudud'][0]['satr']}: {m['hudud'][0]['nass']}",
                    "awwal": bool(taf & asl_judhur), "alaqa": any(h["alaqa"] for h in m["hudud"]),
                    "qarina": any(h["qarina"] for h in m["hudud"])})
    return out


def main():
    D = os.environ.get("MUDAA_DIR")
    if not D:
        sys.exit("MUDAA_DIR غير معيَّن")
    S = J.sijill()
    for f in ("lisan.txt", "maqayis.txt"):
        if J.basma(os.path.join(D, f)) != S[f]["sha256"]:
            sys.exit(f"رُفض {f}: بصمته لا تطابق السجلّ")
    L = open(os.path.join(D, "lisan.txt"), encoding="utf-8").read().split("\n")
    M = open(os.path.join(D, "maqayis.txt"), encoding="utf-8").read().split("\n")
    ml = J.mawadd_lisan(L)
    mq, _ = J.mawadd_maqayis(M)
    Jd = J.Jadhr(ml)
    lisan = {}
    for R, _, body in ml:
        lisan.setdefault(R, []).extend(J.jumal(body))
    if "--lisan-maani" in sys.argv:
        import csv
        asl = {}
        with open(os.path.join(D, "luzum_mujam.tsv"), encoding="utf-8") as f:
            for r in list(csv.reader(f, delimiter="\t"))[1:]:
                if r[0] == "maqayis" and r[3] == "asl":
                    asl.setdefault(r[1], set()).add(r[4])
        for R in SABAA:
            siyaq = set(SABAA) - {R}
            ms = maani_lisan(Jd, R, lisan.get(R, []), asl.get(R, set()), siyaq)
            # الأوّل واحد: إن تعدّد ما يشارك الأصلَ بقي أوّلًا كلُّه (والترجيحُ يعدّه اشتراكًا)؛ والمأخوذُ ما لم يكن أوّلًا وفيه علاقة
            res = tarjih([(m["ism"], m["awwal"], (not m["awwal"]) and m["alaqa"], m["qarina"]) for m in ms])
            print(f"== {R}: {len(ms)} معنى (أوّل {sum(m['awwal'] for m in ms)}، بعلاقة {sum((not m['awwal']) and m['alaqa'] for m in ms)}، "
                  f"بقرينة {sum(m['qarina'] for m in ms)}) ← {res[0]}: {res[1] if res[0] != 'mushtarak' else len(res[1])}")
            for m in ms:
                print("    ", "أوّل" if m["awwal"] else ("علاقة" if m["alaqa"] else "    "), "قرينة" if m["qarina"] else "     ", m["ism"])
        return
    for R in SABAA:
        siyaq = set(SABAA) - {R}
        madda = [b for r, _, b in mq if r == R]
        if not madda:
            print(R, "لا مادّة في المقاييس")
            continue
        js = J.jumal(madda[0])
        # الوحدات: الأصلُ وما يليه من جمل حتّى أوّل علامة حمل؛ وكلُّ علامة حملٍ وما يليها حتّى التالية
        wahdat = [[js[0][0], js[0][1], None]]
        for no, s, satr_at in js[1:]:
            m = HAML.search(J.norm(s))
            if m:
                wahdat.append([satr_at(J.norm_map(s)[1][m.start()]), s, m])
            else:
                wahdat[-1][1] += " " + s
        ms = []
        for i, (no, s, m) in enumerate(wahdat):
            mad = judhur(Jd, s, R)
            q = bool(mad & siyaq)
            if not q and "--lisan" in sys.argv:
                for nl, gl, _ in lisan.get(R, []):
                    gj = judhur(Jd, gl, R)
                    if gj & mad and gj & siyaq:
                        q = True
                        break
            nau = "الأصل" if i == 0 else "مأخوذ"
            ms.append((f"{nau} س{no}: {s[:80]}", i == 0, i > 0, q))
        res = tarjih(ms)
        print(f"== {R}: {len(ms)} معنى، بقرينة {sum(m[3] for m in ms)} ← {res[0]}: {res[1] if res[0] != 'mushtarak' else len(res[1])}")
        for m in ms:
            print("   ", "قرينة" if m[3] else "     ", m[0])


if __name__ == "__main__":
    main()
