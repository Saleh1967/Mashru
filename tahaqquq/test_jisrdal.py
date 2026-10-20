"""اختبار جدول الجسر إلى الدالّ (مرشّح حتّى يُختم) ومطابقة `Jisr/JisrDal.lean` (و`Jisr/JisrDalUtur.lean`) له (الإعراب بالحروف والتقدير وجرّ الممنوع
بالفتحة والمجهول).

يُشغَّل على الجدول حين يحضر (MUDAA_DIR وفيه jisr_dal.tsv)؛ وإلّا أُجريت فحوصُ نصّ Lean وحدها وخرج 0.
١. بصمةُ الجدول الحاضر هي بصمتُه في mudaat/sijill.json (وإلّا رُفض باسمه)، ونوعُه «معلومات-سابقة»، وحالتُه مختوم أو مرشّح (تُطبع).
٢. توقّعاتٌ مستقلّة: 18 صفًّا — 12 بابًا، 4 قواعد، 2 شاهدان؛ 71 اقتباسًا من قطر الندى بأسطرها (عدٌّ يدويّ)؛ وكلُّ «…» في عمود الشاهد إمّا
   قراءةُ البنّاء/تعيينه وإمّا على نمط «قطر الندى سN: «…»» موجودٌ في سطره في المودَع الحاضر بلفظه.
٣. Lean من النصّ (لا عبر Lean): `Bab` منشئاتُه الاثنا عشر (بترتيب Lean؛ وأبوابُ الجدول الاثنا عشر بترتيب الجدول — ترتيبان معلَنان)، و`HukmDal` ثلاثيّ
   (muayyan/muhtamal/laHukm)؛ في `hukmKhaliya`: الأسماء الستّة بالواو رفعًا والألف نصبًا والياء جرًّا، والممنوع فتحتُه محتمَلةٌ نصبًا وجرًّا، والأمثلة
   بالنون رفعًا؛ وفي `hukm` حدُّ 116؛ وفي `majhul`: كسرٌ للماضي وفتحٌ للمضارع، ورفضُ حرف العلّة الساكن، والمشاركةُ في الماضي وحده.
٤. أرقامُ الحوامل في JisrDal.lean (ا، ي، ن، و) هي مواضعُها في جدول المخارج `Dal/Makharij.hawamil` المقروء نصًّا — توقّعٌ مستقلّ من الملفّ
   الآخر لا من JisrDal نفسه.
٥. كلُّ اسمٍ في عمود mirat_lean معرَّفٌ في JisrDal.lean أو JisrDalUtur.lean باسمه الكامل (والمنقوطُ منشئٌ في فضاء نوعه).
٦. شواهدُ Lean (`shawahid` تُقرأ نصًّا): الأزواجُ (لفظ، سطر) الاثنان والثلاثون هي بعينها القائمةُ المكتوبة هنا يدويًّا من القطر (SHAWAHID — توقّعٌ
   مستقلّ يُقتل به تغييرُ سطرٍ في Lean بلا مودَع)؛ وخلايا كلّ شاهدٍ مفكوكةً حروفًا بجدول المخارج هي حروفُ لفظه (همزةُ الوصل والقطع والألف
   صنفٌ واحد، والشدّةُ خليتان — الحروفُ وحدَها: حركاتُ الخلايا غيرِ المقروءة لا يفحصها الاختبار، معلَنٌ في Lean)؛ وبحضور المودَع لفظُ كلّ شاهدٍ
   (بلا حركات) في سطره؛ وأعدادُ Lean (32، 20 معيَّنًا) هي أعدادُ الجدول.
التشغيل: python3 -I tahaqquq/test_jisrdal.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISM = "جدول الجسر إلى الدالّ"

lean = open(os.path.join(ROOT, "Jisr", "JisrDal.lean"), encoding="utf-8").read()
lean_utur = open(os.path.join(ROOT, "Jisr", "JisrDalUtur.lean"), encoding="utf-8").read()
makharij = open(os.path.join(ROOT, "Dal", "Makharij.lean"), encoding="utf-8").read()

# ٦: الشواهد الاثنان والثلاثون (لفظ، سطر القطر) — عدٌّ يدويّ من المودَع، مستقلّ عن Lean
SHAWAHID = [("زيد", 76), ("زيد", 76), ("بزيد", 77), ("يقوم", 76), ("يقوم", 76), ("يقم", 77), ("ذو", 79), ("أخا", 385), ("أبي", 130),
            ("الزيدان", 82), ("فعلين", 115), ("بشرطين", 358), ("الزيدون", 82), ("مفسدين", 320), ("للمسلمين", 285), ("الهندات", 226),
            ("السموات", 87), ("بأفضل", 87), ("بالأفضل", 88), ("تفعلان", 89), ("تفعلوا", 90), ("تفعلوا", 90), ("يغز", 91), ("يخش", 91),
            ("يرم", 91), ("يخشى", 93), ("يدعو", 94), ("يدعو", 95), ("القاضي", 93), ("القاضي", 94), ("غلامي", 92), ("الفتى", 92)]
HARAKAT = re.compile("[ً-ْ]")
SINF_ALIF = {"ا": "ا", "أ": "ا", "إ": "ا", "آ": "ا", "ء": "ا", "ى": "ا"}


def block(start, end):
    a = lean.index(start)
    return lean[a:lean.index(end, a)]


def munshiat_of(typ):
    return re.findall(r"\| (\w+)", block(f"inductive {typ}", "deriving"))


def hawamil_makharij():
    m = re.search(r"def hawamil : List Char :=\s*\[(.*?)\]", makharij, re.S)
    hawamil = re.findall(r"'(.)'", m.group(1))
    assert len(hawamil) == 29, len(hawamil)
    return hawamil


def shawahid_lean():
    """(اللفظ، السطر، الخلايا) لكلّ شاهد في `def shawahid` نصًّا؛ الخلايا بأزواج (حرف، حالة) من `kh h s` بأسماء الحوامل."""
    consts = {name: int(re.search(rf"^def {name} : Nat := (\d+)", lean, re.M).group(1)) for name in ("alif", "ya", "nun", "waw")}
    out = []
    for m in re.finditer(r"⟨\"([^\"]+)\", (\d+), \.\w+(?: \w+)?, \[([^\]]*)\]", block("def shawahid :", "\n\n")):
        cells = [(consts.get(h, h), int(s)) for h, s in re.findall(r"kh (\w+) (\d)", m.group(3))]
        out.append((m.group(1), int(m.group(2)), [(int(h), s) for h, s in cells]))
    return out


def huruf_lafz(lafz):
    """حروفُ اللفظ بلا حركات، والشدّةُ تضاعف ما قبلها، وصنفُ الألف واحد."""
    out = []
    for ch in lafz:
        if ch == "ّ":
            out.append(out[-1])
        elif "ً" <= ch <= "ْ":
            continue
        else:
            out.append(SINF_ALIF.get(ch, ch))
    return out


def fahs_lean():
    assert munshiat_of("Bab") == ["mufrad", "filSahih", "maqsur", "manqus", "mudafLiYa", "sitta", "muthanna", "jamMudhakkar", "jamMuannath",
                                  "mamnu", "amthila", "mudariMutall"], munshiat_of("Bab")
    assert munshiat_of("HukmDal") == ["muayyan", "muhtamal", "laHukm"]
    h = block("def hukmKhaliya ", "\n\n")
    assert "else if harf c == waw then .muayyan .raf else if harf c == alif then .muayyan .nasb" in h
    assert "else if harf c == ya then .muayyan .jarr else .laHukm" in h
    assert "| .mamnu false => match hala c with\n      | 1 => .muayyan .raf | 0 => .muhtamal [.nasb, .jarr] | _ => .laHukm" in h
    assert "| .amthila => if harf c == nun then .muayyan .raf else if illaSakin c then .muhtamal [.nasb, .jazm] else .laHukm" in h
    assert "| .maqsur => if harf c == alif && hala c == 3 then .muhtamal [.raf, .nasb, .jarr] else .laHukm" in h
    assert "| some c => if c < 116 then hukmKhaliya b l c else .laHukm" in block("def hukm ", "\n\n")
    mj = block("def majhul ", "\n\n")
    assert "(if madi then 2 else 0)" in mj and "if sababMajhul madi g l ≠ [] then none" in mj and "musharik (sigaFiliyya madi g)" in mj
    # LC06: أسبابُ رفض المجهول مسمّاةٌ بترتيبها، والمضارعُ دون أربع خلايا مرفوض، والآخرُ المشدَّد مرفوض
    sm = block("def sababMajhul ", "\n\n")
    assert "(if l.length < mawdiMusharik (sigaFiliyya madi g) + 3 then [.qasir]" in sm
    assert "else if !madi && l.length < 4 then [.mudariDunArba] else []) ++" in sm
    assert "(if madi then (if (akhir l).map hala != some 0 then [.madiGhayrMaftuh] else [])" in sm
    assert "else (if (akhir l).map hala != some 1 then [.mudariGhayrMarfu] else [])) ++" in sm
    assert "(if mudaafAkhir l then [.mudaafAkhir] else []) ++" in sm and "(if l.any illaSakin then [.illaSakin] else [])" in sm
    assert "| c :: d :: _ => harf d == harf c && hala d == 3" in block("def mudaafAkhir ", "\n\n")
    assert munshiat_of("SababMajhul") == ["qasir", "mudariDunArba", "madiGhayrMaftuh", "mudariGhayrMarfu", "mudaafAkhir", "illaSakin"], \
        munshiat_of("SababMajhul")
    assert munshiat_of("SababDal") == ["farigh", "fawqHadd", "laYaqbaluhuBab"], munshiat_of("SababDal")
    sd = block("def sababDal ", "\n\n")
    assert "| none => some .farigh" in sd
    assert "| some c => if c < 116 then (if hukmKhaliya b l c = .laHukm then some .laYaqbaluhuBab else none) else some .fawqHadd" in sd
    assert "def sigaFiliyya (madi : Bool) (g : Siga) : Siga := if madi then g else .basit" in lean
    # ٤: الحوامل من جدول المخارج نصًّا
    hawamil = hawamil_makharij()
    for name, ch in (("alif", "ا"), ("ya", "ي"), ("nun", "ن"), ("waw", "و")):
        val = int(re.search(rf"^def {name} : Nat := (\d+)", lean, re.M).group(1))
        assert val == hawamil.index(ch), (name, val, hawamil.index(ch))
    for name in ("harf_fakk", "khaliya_malik", "hawamil_huruf", "asliyya_tuqabil", "maqsur_la_yuayyin", "mudaf_la_yuayyin", "yayn_la_yufarriq",
                 "manqus_fatha_zahira", "mamnu_fatha", "mamnu_bi_al", "amthila_nun", "sitta_hamil", "farIyaBab_malik", "farIya_kull",
                 "shawahid_hukm", "muwafiq_farIya", "majhul_huruf", "majhul_tul", "majhul_dun_116", "majhul_marfud", "shawahid_majhul",
                 "intilaq_wasl", "hukm_laHukm_sabab", "majhul_none_iff", "shawahid_sabab", "shahid_aqd_mudkhal"):
        assert re.search(rf"^theorem {name}\b", lean, re.M), name
    for name in ("mufrad_halaIrab", "mufrad_tanwin"):
        assert re.search(rf"^theorem {name}\b", lean_utur, re.M), name
    assert "import Jisr.Utur" not in lean and "import Jisr.JisrDal\nimport Jisr.Utur" in lean_utur   # لا دور: Utur فوق الجسر
    # ٦: الشواهد نصًّا
    sh = shawahid_lean()
    assert [(w, n) for w, n, _ in sh] == SHAWAHID, [(w, n) for w, n, _ in sh if (w, n) not in SHAWAHID]
    for w, _, cells in sh:
        huruf = [SINF_ALIF.get(hawamil[h], hawamil[h]) for h, s in cells]
        assert huruf == huruf_lafz(w), ("الخلايا لا تطابق اللفظ", w, "".join(huruf))
        assert all(s < 4 for _, s in cells)
    th = block("theorem shawahid_hukm", "by decide")
    assert "shawahid.length = 32" in th and ".length = 20" in th
    return sh


d = os.environ.get("MUDAA_DIR")
p = os.path.join(d, "jisr_dal.tsv") if d else None
if not p or not os.path.exists(p):
    fahs_lean()
    print("لم يُشغَّل على الجدول (غير حاضر؛ عيّن MUDAA_DIR وفيه jisr_dal.tsv)؛ فحص نصّ Lean: الأبواب والحكم الثلاثيّ وحدّ 116 وقواعد الستّة والممنوع "
          "والأمثلة والمجهول وأرقام الحوامل من جدول المخارج والمبرهنات المسمّاة و32 شاهدًا بأسطرها اليدوية وخلاياها حروفَ ألفاظها موجودة")
    sys.exit(0)


def tsv(path):
    lines = [l for l in open(path, encoding="utf-8").read().split("\n") if l and not l.startswith("#")]
    hdr = lines[0].split("\t")
    return [dict(zip(hdr, l.split("\t"))) for l in lines[1:]]


def segs(cell):
    out, cur, depth, i = [], "", 0, 0
    while i < len(cell):
        c = cell[i]
        if c == "«":
            depth += 1
        elif c == "»":
            depth -= 1
        if depth == 0 and cell.startswith("؛ ", i):
            out.append(cur)
            cur = ""
            i += 2
            continue
        cur += c
        i += 1
    out.append(cur)
    return out


sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
m = next(x for x in sijill if x["ism"] == ISM)
assert m["naw"] == "معلومات-سابقة" and m["hala"] in ("مختوم", "مرشح"), m
b = hashlib.sha256(open(p, "rb").read()).hexdigest()
assert b == m["sha256"], f"{ISM}: تغيّرت بصمته {b[:16]} ≠ {m['sha256'][:16]}"
hala = m["hala"]
ok = 1

# ٢
rows = tsv(p)
assert len(rows) == 18, len(rows)
by = {}
for r in rows:
    by.setdefault(r["naw"], []).append(r)
assert {k: len(v) for k, v in by.items()} == {"bab": 12, "qaida": 4, "shahid": 2}, {k: len(v) for k, v in by.items()}
qatr = None
qp = os.path.join(d, "qatr.txt")
if os.path.exists(qp):
    qatr = open(qp, encoding="utf-8").read().split("\n")
pat = re.compile(r"(?:(قطر الندى) )?س(\d+)(?:–\d+)?: «([^»]+)»")
iqt = kull = 0
for r in rows:
    s0 = None
    for seg in segs(r["shahid"]):
        if "«" not in seg:
            continue
        if seg.startswith(("قول المالك", "قراءة البنّاء", "تعيين البنّاء")):
            continue
        found = pat.findall(seg)
        assert len(found) == seg.count("«"), ("اقتباس خارج النمط فلا يُفحص", r["ramz"], seg[:60])
        for s, ln, q in found:
            if s:
                s0 = s
            assert s0 == "قطر الندى", (ln, q[:30], "اقتباس بلا مصدر")
            kull += 1
            if qatr is not None:
                assert q in qatr[int(ln) - 1], (ln, q[:40])
                iqt += 1
assert kull == 71, kull   # توقّع مستقلّ (عدٌّ يدويّ صفًّا صفًّا)
iqt_bayan = f"{iqt} اقتباسًا في سطره من {kull}" if qatr is not None else "لم تُفحص الاقتباسات (القطر غير حاضر)"
ok += 1

# ٣، ٤
sh = fahs_lean()
babs = [r["ramz"] for r in by["bab"]]
assert babs == ["المفرد المنصرف", "الفعل الصحيح", "الأسماء الستّة", "المثنّى", "جمع المذكر السالم", "جمع المؤنث السالم", "الممنوع من الصرف",
                "الأمثلة الخمسة", "المضارع المعتلّ الآخر", "المقصور", "المنقوص", "المضاف إلى الياء"], babs
ok += 2   # ٣ و٤ كلاهما في fahs_lean

# ٥
asma = set()
for r in rows:
    for ident in [x.strip() for x in r["mirat_lean"].split(";") if x.strip()]:
        if ident != "(لم يُبنَ)":
            asma.add(ident)
both = lean + "\n" + lean_utur
for ident in asma:
    if "." in ident:
        typ, c = ident.split(".", 1)
        found = (f"inductive {typ}" in lean and c in munshiat_of(typ)) or re.search(rf"^def {re.escape(ident)}\b", both, re.M)
    else:
        found = re.search(rf"^(def|theorem|structure|inductive) {re.escape(ident)}\b", both, re.M)
    assert found, f"اسم في الجدول لا تعريف له في Lean بهذا الاسم الكامل: {ident}"
ok += 1

# ٦: صفّ الشواهد يذكر 20 معيَّنًا و12 محتمَلة = 32 كلّها بلفظ القطر؛ وكلّ شاهدٍ لفظُه في سطره من المودَع
s_row = by["shahid"][0]
assert "المعيَّن 20" in s_row["qima"] and "المحتمَل 12" in s_row["qima"] and "32 كلّها بلفظ القطر" in s_row["qima"], s_row["qima"]
fi_satr = 0
if qatr is not None:
    for w, n, _ in sh:
        assert HARAKAT.sub("", w) in qatr[n - 1], ("شاهد ليس في سطره", w, n)
        fi_satr += 1
    assert fi_satr == 32
ok += 1
print(f"{ok}/6 — 18/18 صفًّا ({hala})، {iqt_bayan}، الأبواب الاثنا عشر والحكم الثلاثيّ وحدّ 116 وقواعد الستّة والممنوع والأمثلة والمجهول في Lean "
      f"مطابقة، أرقام الحوامل من جدول المخارج، {len(asma)} اسمًا معرَّفًا، 32 شاهدًا بأسطرها اليدوية وخلاياها حروفَ ألفاظها، {fi_satr} منها في سطره")
