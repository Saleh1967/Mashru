"""اختبار جدول القواعد (`qawaid.tsv`؛ مختومٌ بإذن المالك 2026-10-22، وكان مرشّحًا منذ 2026-10-21) — صفُّه الأوّل: الأسماء الستّة — ومطابقة `Jisr/QawaidJadwal.lean` (مولَّد)
و`Jisr/QawaidSitta.lean` له.

يُشغَّل على الجدول حين يحضر (MUDAA_DIR وفيه qawaid.tsv)؛ وإلّا أُجريت فحوصُ نصّ Lean وحدها وخرج 0.
١. بلا مودَع (دائمًا): صفوفُ `sitta` في QawaidJadwal.lean ستّةٌ بأسمائها وترتيب القطر L78–79 (أب، أخ، حم، هن، فم، ذو)، وخلاياها مفكوكةً بجدول
   المخارج `Dal/Makharij.hawamil` المقروء نصًّا هي الصورُ المكتوبة هنا يدويًّا حرفًا وحركة (SUWAR — توقّعٌ مستقلٌّ عن الجدول والمولِّد)، والقصرُ
   في أب وأخ وحم وحدها (الألفية L78 «وفي أب وتالييه»)، والصحبةُ في ذو وحده (L76)، والدرجاتُ بلفظ مصدرها (قصر>نقص «أشهر» في الثلاثة،
   ونقص>تمام «أحسن» و«الأفصح» في هن)؛ وفي
   QawaidSitta.lean: القوانينُ من `sitta` بوجوهها وأحوالها الثلاث، وشرطُ الإضافة والطلب والصحبة في المقدّمات،
   والحكمُ `hukm3` بعينه والقراءةُ فيه `qiraaSitta`، والمبرهناتُ المسمّاة موجودة — وهذا فحصُ نصٍّ لا سلوك (تأكيداتٌ تنسخ أسطر Lean)، والسلوكُ
   تفحصه Lean بمبرهنات الشاهد (`shawahid_sitta` وحدها تقتل P393، وP397 مع `mawadi_shawahid`؛ وP392 وP394 وP396 وP398 تقتلها Lean وهذه التأكيدات معًا)؛
   وفحصُ النصّ على النصّ بلا تعليقات (ماسحُ البوّابة `_taaliq_lean`، متداخلًا)، وفي جسم التصريح المسمّى — كاشفٌ لتغييرٍ عاديٍّ لا حارسٌ من التحايل
   (تصريحٌ مجاورٌ أو سابقٌ بالاسم نفسه في فضاءٍ آخر، أو شيفرةٌ تُبطل الشرطَ وتُبقي نصَّه، تمرّ)؛ والقتلُ في Lean: `mawadi_shawahid`،
   `shartMawdi_shurut`، `fiMawdi_wujud`، `fiMawdi_shartan`، `isdar_basma` تقتل P400–P406، و`asl_mawdi` تقتل P409 وP412–P413 — تثبيتًا لصيغ
   التعريفات لا حراسةً لـ`hukmSitta` (وسندُ ذلك بالمجموعة في ترويسة `Jisr/QawaidSitta.lean`: ترتيبُ التصريح لـP400–P403 وP405–P406، وأنّ
   `maqbulM` لا يقرأ الإصدار لـP404، واستنتاجٌ غيرُ مبرهنٍ في المستودع لـP409 وP412–P413)؛ وما يكشفه فحصُ النصّ هنا
   من تغييرٍ في `halat` و`qawanin` و`qanun` و`aslMawdi` و`qiraaSitta` تقتله Lean أيضًا في الطفرات المسجَّلة (P407–P413).
٢. بالمودَع: بصمةُ الجدول هي بصمتُه في mudaat/sijill.json (وإلّا رُفض باسمه)، ونوعُه «معلومات-سابقة»، وحالتُه مختوم أو مرشّح (تُطبع)؛ والمولِّد
   `scripts/bina_qawaid.py` على الجدول يعيد QawaidJadwal.lean بايتًا بايتًا (فالبصمةُ فيه بصمةُ الجدول).
٣. بالمودَع: اقتباساتُ عمود السند اثنان وأربعون (عدٌّ يدويٌّ صفًّا صفًّا: 8، 10، 5، 7، 5، 7)، كلٌّ بعمودٍ من الأعمدة المعلنة ومصدرٍ من الثلاثة، وكلٌّ
   في سطره أو أسطره من المودَع الحاضر بلفظه على النصّ الموصول (بلا بادئات OpenITI)؛ ووسمُ العمود قد يحمل قيدًا بين قوسين («العلّة (قراءة
   البنّاء)»، «الشاهد (بضميرٍ متّصل، لم يُبنَ)»، «الدرجة («كغد» نقصًا: قراءة البنّاء)»).
التشغيل: python3 -I tahaqquq/test_qawaid.py
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bawwaba  # noqa: E402 — ماسحُ تعليقات Lean (متداخلًا) نفسُه الذي تستعمله البوّابة
ISM = "جدول القواعد"

jadwal = open(os.path.join(ROOT, "Jisr", "QawaidJadwal.lean"), encoding="utf-8").read()
sitta_src = open(os.path.join(ROOT, "Jisr", "QawaidSitta.lean"), encoding="utf-8").read()
makharij = open(os.path.join(ROOT, "Dal", "Makharij.lean"), encoding="utf-8").read()

# ١: الصورُ بيد المختبِر (رفع، نصب، جرّ) بترتيب القطر L78–79 — مستقلّةٌ عن الجدول والمولِّد
SUWAR = [("أب", "أَبُو", "أَبَا", "أَبِي"), ("أخ", "أَخُو", "أَخَا", "أَخِي"), ("حم", "حَمُو", "حَمَا", "حَمِي"),
         ("هن", "هَنُو", "هَنَا", "هَنِي"), ("فم", "فُو", "فَا", "فِي"), ("ذو", "ذُو", "ذَا", "ذِي")]
QASR = {"أب", "أخ", "حم"}
SAHIB = {"ذو"}
DARAJA = {"أب": '[(.qasr, .naqs, "أشهر")]', "أخ": '[(.qasr, .naqs, "أشهر")]', "حم": '[(.qasr, .naqs, "أشهر")]',
          "هن": '[(.naqs, .tamam, "أحسن"), (.naqs, .tamam, "الأفصح")]', "فم": "[]", "ذو": "[]"}
HARAKAT = {"َ": 0, "ُ": 1, "ِ": 2, "ْ": 3}
MADD_BAD = {0: "ا", 1: "و", 2: "ي"}
# ٣: عدُّ الاقتباسات في كلّ صفٍّ يدويًّا
IQTIBASAT = {"أب": 8, "أخ": 10, "حم": 5, "هن": 7, "فم": 5, "ذو": 7}
AMIDA = ("التقسيم", "الحكم", "الشرط", "الدرجة", "الباب", "العلّة", "الاستعمال", "الشاهد", "وضعٌ آخر")
MASADIR = {"قطر الندى": "qatr.txt", "الألفية": "alfiyya.txt", "الكتاب": "sibawayhi.txt"}


def hawamil():
    m = re.search(r"def hawamil : List Char :=\s*\[(.*?)\]", makharij, re.S)
    h = re.findall(r"'(.)'", m.group(1))
    assert len(h) == 29, len(h)
    return h


def huruf_harakat(sura):
    """(حرف، حالة) لكلّ حرفٍ في الصورة: الهمزةُ على الألف همزة، وحرفُ المدّ بلا علامةٍ بعد حركته ساكن."""
    out = []
    for ch in sura:
        if ch in HARAKAT:
            out[-1] = (out[-1][0], HARAKAT[ch])
        else:
            if out and out[-1][1] is None:
                raise AssertionError(("حرفٌ بلا حركة", sura))
            ch = "ء" if ch in "أإ" else ch
            if out and MADD_BAD.get(out[-1][1]) == ch:
                out.append((ch, 3))
            else:
                out.append((ch, None))
    assert all(s is not None for _, s in out), sura
    return out


def sufuf_lean(text=None):
    """صفوف `sitta` من QawaidJadwal.lean نصًّا (أو من نصٍّ مولَّد): (الاسم، رفع، نصب، جرّ، قصر، صحبة، درجة)."""
    text = jadwal if text is None else text
    body = text[text.index("def sitta : List Saff :="):]
    out = []
    for m in re.finditer(r"⟨\"([^\"]+)\", \[([\d, ]*)\], \[([\d, ]*)\], \[([\d, ]*)\], (true|false), (true|false), (\[(?:[^\]\"]|\"[^\"]*\")*\])", body):
        cells = [[int(x) for x in g.split(", ")] for g in m.group(2, 3, 4)]
        out.append((m.group(1), *cells, m.group(5) == "true", m.group(6) == "true", m.group(7)))
    return out


def muwallid_masar(path):
    """مخرجُ المولِّد على ملفّ جدول."""
    return subprocess.run([sys.executable, "-I", os.path.join(ROOT, "scripts", "bina_qawaid.py"), path, "--stdout"],
                          capture_output=True, text=True, check=True).stdout


def muwallid(tsv_text):
    """مخرجُ المولِّد على جدولٍ مكتوب."""
    with tempfile.TemporaryDirectory() as t:
        f = os.path.join(t, "qawaid.tsv")
        open(f, "w", encoding="utf-8").write(tsv_text)
        return muwallid_masar(f)


def fahs_sufuf(rows):
    h = hawamil()
    assert [r[0] for r in rows] == [s[0] for s in SUWAR], [r[0] for r in rows]
    for (ism, raf, nasb, jarr, qasr, sahib, daraja), (_, *suwar) in zip(rows, SUWAR):
        for cells, sura in zip((raf, nasb, jarr), suwar):
            got = [(h[c // 4], c % 4) for c in cells]
            assert got == huruf_harakat(sura), ("الخلايا لا تطابق الصورة", ism, sura, got)
        assert qasr == (ism in QASR), (ism, qasr)
        assert sahib == (ism in SAHIB), (ism, sahib)
        assert daraja == DARAJA[ism], (ism, daraja)


def fahs_lean():
    fahs_sufuf(sufuf_lean())
    # المولِّدُ نفسُه بلا مودَع: جدولٌ يكتبه الاختبارُ من صوره اليدوية يُخرج الخلايا والأعلامَ المتوقَّعة
    daraja_nass = {DARAJA["أب"]: "قصر>نقص=أشهر", DARAJA["هن"]: "نقص>تمام=أحسن، نقص>تمام=الأفصح", "[]": "—"}
    tsv_text = "qaida\tism\traf\tnasb\tjarr\tqasr\tshart\tdaraja\tsanad\n" + "".join(
        "\t".join(["الأسماء الستّة", ism, r, n, j, "نعم" if ism in QASR else "لا", "إضافة، صحبة" if ism in SAHIB else "إضافة",
                   daraja_nass[DARAJA[ism]], "س"]) + "\n" for ism, r, n, j in SUWAR)
    fahs_sufuf(sufuf_lean(muwallid(tsv_text)))
    assert re.search(r'^def basma : String := "[0-9a-f]{64}"$', jadwal, re.M)
    # QawaidSitta: القاعدة والقوانين والحكم نصًّا — على النصّ بلا تعليقات (ماسحُ البوّابة `_taaliq_lean`، متداخلًا)، فحصُ نصٍّ لا سلوك
    s = sitta_src
    bila = bawwaba.bila_taaliq(s, bawwaba._taaliq_lean(s))

    def jism(ras):
        """التصريحُ `ras` (رأسُه في أوّل سطرٍ بحدّ اسم) حتّى أوّل سطرٍ يبدأ في عموده الأوّل."""
        m = re.search(rf"^{re.escape(ras)}(?=[\s:(])", bila, re.M)
        assert m, ras
        z = re.search(r"\n(?=\S)", bila[m.end():])
        return bila[m.start():m.end() + z.start()] if z else bila[m.start():]

    assert "sitta.flatMap fun s => (wujuh s).flatMap fun w => halat.map fun h => qanun s w h" in jism("def qawanin")
    assert "[1, 0, 2]" in jism("def halat")
    assert "if s.qasr then [.tamam, .qasr] else [.tamam]" in jism("def wujuh")
    q = jism("def qanun")
    assert "[.sura (suraBi s w h), .mudaf (suraBi s w h), .matlub h (suraBi s w h)] ++" in q and "(if s.sahib then [.sahib (suraBi s w h)] else [])" in q
    am = jism("def aslMawdi")
    assert "  | .sahib _ => false\n  | .murab _ _ => false" in am   # الصحبة والنتيجة لا تُقرآن
    assert "  | .matlub h c => nom && hs.contains h && c == w.khalaya" in am
    assert "Qaida.maqbulM qSitta (aslMawdi nom hs w mudaf) ⟨r.natija, silsila r⟩" in jism("def rukhsa")   # الفاحص بالمحتوى
    assert "(damm (ofBool (waslBase u && waslMl u && jisrMadlul u)) (damm (qiraaSitta u) (waslMadlul u.isnad))))" in jism("def hukmSitta")
    assert ("kullMawdi u (fun n hs w m => laIrabBilHarf n hs w m || rukhsa n hs w m || mawquf n hs w m) then .laHukm"
            in jism("def qiraaSitta"))
    for name in ("kullMawdi_mono", "qiraaSitta_min_qiraa", "hukmSitta_murakhkhas_thabit", "hukm3_shakl", "hukmSitta_shakl", "shakl_mumtani",
                 "shakl_laHukm_mumtani", "shakl_murakhkhas", "hukmQiraa_ne_mumtani", "hukmSitta_mumtani_thabit", "hukmSitta_kharij",
                 "raf_bi_qiraa", "mumtani_bi_qiraa", "natija_murab", "silsila_maqbula", "rukhsa_murakhkhasa", "la_tamdid", "suwar_sitta",
                 "sahib_la_yathbut", "sahib_muqaddima", "dhu_la_rukhsa", "qanun_raf_fi", "ghayr_sitta", "jadwal_jisrdal",
                 "shawahid_jisrdal", "abuK_jadwal", "shawahid_sitta", "daraja_wujuh", "shartMawdi_shurut", "fiMawdi_shartan", "mawadi_shawahid",
                 "fiMawdi_wujud", "isdar_basma", "asl_mawdi"):
        assert re.search(rf"^theorem {name}(?=[\s:(])", bila, re.M), name
    assert "sorry" not in s and "native_decide" not in s and not re.search(r"^axiom ", s, re.M)
    return sufuf_lean()


d = os.environ.get("MUDAA_DIR")
p = os.path.join(d, "qawaid.tsv") if d else None
if not p or not os.path.exists(p):
    fahs_lean()
    print("لم يُشغَّل على الجدول (غير حاضر؛ عيّن MUDAA_DIR وفيه qawaid.tsv)؛ الصفوف الستّة بخلاياها صورَها اليدوية والمولِّدُ يُخرجها منها، والقصرُ "
          "والصحبةُ والدرجات، ونصُّ Lean: القاعدةُ والقوانينُ والحكمُ والمبرهناتُ المسمّاة موجودة")
    sys.exit(0)

# ٢
sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
m = next(x for x in sijill if x["ism"] == ISM)
assert m["naw"] == "معلومات-سابقة" and m["hala"] in ("مختوم", "مرشح") and m["milaf"] == "qawaid.tsv", m
b = hashlib.sha256(open(p, "rb").read()).hexdigest()
assert b == m["sha256"], f"{ISM}: تغيّرت بصمته {b[:16]} ≠ {m['sha256'][:16]}"
rows = fahs_lean()
wallad = muwallid_masar(p)
assert wallad == jadwal, "Jisr/QawaidJadwal.lean ليس مخرجَ المولِّد على الجدول الحاضر"
assert f'def basma : String := "{b}"' in jadwal

# ٣
lines = [l for l in open(p, encoding="utf-8").read().split("\n") if l]
hdr = lines[0].split("\t")
tsv = [dict(zip(hdr, l.split("\t"))) for l in lines[1:]]
assert [r["ism"] for r in tsv] == [s[0] for s in SUWAR] and all(r["qaida"] == "الأسماء الستّة" for r in tsv)

nusus = {}


def mawsul(src, a, z):
    if src not in nusus:
        nusus[src] = open(os.path.join(d, MASADIR[src]), encoding="utf-8").read().split("\n")
    parts = []
    for ln in nusus[src][a - 1:z]:
        ln = re.sub(r"^(# |~~)", "", ln)
        parts.append(ln)
    return " ".join(parts)


pat = re.compile(r"^(" + "|".join(AMIDA) + r")(?: \([^)]*\))?: (" + "|".join(MASADIR) + r") س(\d+)(?:–(\d+))?: «([^»]+)»$")
kull = 0
for r in tsv:
    n = 0
    for seg in r["sanad"].split("؛ "):
        mm = pat.match(seg)
        assert mm, ("مقطعٌ خارج النمط", r["ism"], seg[:60])
        _, src, a, z, q = mm.groups()
        a = int(a)
        z = int(z) if z else a
        assert z >= a
        assert q in mawsul(src, a, z), (r["ism"], src, a, z, q[:40])
        n += 1
    assert n == IQTIBASAT[r["ism"]], (r["ism"], n)
    kull += n
assert kull == 42, kull
print(f"جدول القواعد ({m['hala']}، {b[:12]}…): 6 صفوف، وQawaidJadwal.lean مخرجُ المولِّد بايتًا، وخلاياه صورُه اليدوية، و{kull} اقتباسًا في "
      f"أسطرها من المودَعات")
