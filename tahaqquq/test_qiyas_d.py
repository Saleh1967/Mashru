"""اختبارُ منفّذ القياس المسجَّل (`tahaqquq/qiyas_d.py`) ووضعِ القياس في القارئ (`qari --qiyas`) — على بياناتٍ مصنوعةٍ هنا
وكلماتٍ مختارة باليد، لا على المرجعين المحجوبين (لا يقرأ MUDAA_DIR أبدًا).

التوقّعاتُ مكتوبةٌ باليد مستقلّةً عن الشيفرة:
١. جدولُ بكوالتر للجذور حرفًا حرفًا (28 حرفًا، و«A» همزة)؛ وحرفٌ خارجه خللٌ باسمه.
٢. ثوابتُ التسجيل (البذور، وأحجام العيّنتين، وحدّ الأمثلة، وبصمة الشطر الأوّل) بقيمها المكتوبة هنا، وكلٌّ منها في نصّ الوثيقة؛
   والشطران على 15 آية: منفصلان، تامّان، 7 ثمّ 8 (فقلبُهما يُرى)، ثابتان بالبذرة؛ وبصمةُ قائمة الآيات «سورة:آية» سطرًا سطرًا.
٣. قارئا MASAQ وQAC على ملفّين مصنوعين: الكلمةُ بمفتاحها وقطعها، وكلمةٌ اختلفت Word في صفّيها شذوذٌ لا يُقاس.
٤. الطبقات: ف2 (i) قطعةٌ واحدة ذاتُ جذرٍ صحيح، (ii) أكثر، ولا طبقة لكلمةٍ بلا جذر أو بجذرٍ رباعيّ أو معتلّ (w/y)؛ ف3 «أ» بحركةٍ
   قصيرة، «ب» ممنوعٌ من الصرف، «ج» ما سواهما، وصفُّ Other_i3rab لا يُعدّ قطعة، ولا طبقة لمعربٍ بعده لاحقة.
٥. العدّ على شطرٍ مصنوع بأعدادٍ محسوبةٍ باليد (التفصيل عند كلّ توقّع)، وفترةُ ولسن يدويًّا (بلا «-0.0»)، والعيّنتان معمّاتين
   (الفرضُ f2/f3 لا الطبقة) وأحكامُهما منفصلة، وعيّنةُ الأهليّة مطبَّقة، وحدُّ الأمثلة 25 على ثلاثين خلافًا.
٦. البصمات: تُقبل المطابقة، ويُرفض الملفّ المغيَّر باسمه.
٧. الحراسة على مستودع git مصنوع: الوثيقةُ غائبة، والإخراجُ داخل المستودع، والشجرةُ غير النظيفة، وHEAD غيرُ origin/main، والسكربتُ
   المغيَّر بعد التسجيل — كلٌّ يُرفض باسمه؛ والشطرُ الثاني لا يُقبل إلّا بملفٍّ في hawkama/ أُضيف بعد التسجيل؛ وiedad يتحقّق من البصمات
   قبل القراءة، ومن بصمة الشطر، ويختار الشطرَ المطلوب؛ والسطرُ الشاذّ من القارئ خلل.
٨. `qari --qiyas` على كلماتٍ باليد: الخلايا 4×الحامل+الحال (فهارسُ `Dal.hawamil`: ك8 ت18 ب26 ق7 ا2 ل13 ر15 ف25)، والقانونُ
   على الخلايا وبعد التسكين (كَتَبَ 1/1، وقَالْتُ 0/1 شاهدُ المالك qaltu، وبِ 1/0 بخانةٍ واحدة)، ومرشَّحُ الجذر، وحالُ الآخر،
   والإعرابُ المرشَّح (الفتحة نصب، والكسرة جرّ، والسكون «-»)؛ وغيرُ المشكول مرفوضٌ باسمه.
التشغيل: python3 -I tahaqquq/test_qiyas_d.py
"""
import csv
import hashlib
import json
import math
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tahaqquq"))
import qiyas_d as Q  # noqa: E402

nj = 0


def najah(msg):
    global nj
    nj += 1
    print(f"✓ {msg}")


# ١. جدولُ بكوالتر، مكتوبًا باليد حرفًا حرفًا
BW = {"A": "ء", "b": "ب", "t": "ت", "v": "ث", "j": "ج", "H": "ح", "x": "خ", "d": "د", "*": "ذ", "r": "ر", "z": "ز",
      "s": "س", "$": "ش", "S": "ص", "D": "ض", "T": "ط", "Z": "ظ", "E": "ع", "g": "غ", "f": "ف", "q": "ق", "k": "ك",
      "l": "ل", "m": "م", "n": "ن", "h": "ه", "w": "و", "y": "ي"}
assert len(BW) == 28
for c, a in BW.items():
    assert Q.jidhr_arabi(c) == a, c
assert Q.jidhr_arabi("ktb") == "كتب" and Q.jidhr_arabi("Amn") == "ءمن"
try:
    Q.jidhr_arabi("k'b")
    raise AssertionError("حرفٌ خارج الجدول قُبل")
except Q.Khalal:
    pass
najah("جدول بكوالتر للجذور (28 حرفًا يدويًّا)")

# ٢. ثوابتُ التسجيل والشطران
WATHIQA = open(os.path.join(ROOT, "hawkama", "tasjil_qiyas_d.md"), encoding="utf-8").read()
SHATR1 = "4210b6fb3fefc86d4d19be17b20bfe757e6d760417ac785d05c40e21e6a66e3b"
assert (Q.BADHRA, Q.BADHRA_QAYYIS, Q.BADHRA_AHLIYYA, Q.AYYINA_N, Q.AYYINA_AHLIYYA_N, Q.AMTHILA_HADD, Q.SHATR1_SHA256) == \
    (20261020, 20261021, 20261022, 100, 10, 25, SHATR1)
for x in ("20261020", "20261021", "20261022", SHATR1, "مئةَ حكمٍ", "عشرَ كلماتٍ من كلّ طبقة", "أوّلُ 25"):
    assert x in WATHIQA, x
# الترتيبُ عدديّ: 1:2 قبل 1:10 (ونصًّا تكون 1:10 أوّلًا)، وكلُّ سطرٍ ينتهي بسطرٍ جديد.
assert Q.basmat_shatr({(1, 10), (1, 2), (2, 7)}) == hashlib.sha256(b"1:2\n1:10\n2:7\n").hexdigest()
ayat = [(1, i) for i in range(1, 11)] + [(2, i) for i in range(1, 6)]
s1, s2 = Q.shatr(ayat)
assert s1.isdisjoint(s2) and s1 | s2 == set(ayat) and len(s1) == 7 and len(s2) == 8, (s1, s2)
assert Q.shatr(list(reversed(ayat))) == (s1, s2)
assert Q.shatr(ayat, Q.BADHRA + 1) != (s1, s2)
najah("ثوابت التسجيل بقيمها وفي الوثيقة، والشطران (7 ثمّ 8) ثابتان بالبذرة")

# ٣. قارئا المرجعين على ملفّين مصنوعين
tmp = tempfile.mkdtemp()
HEAD = ["ID", "Sura_No", "Verse_No", "Column5", "Word_No", "Word", "Without_Diacritics", "Segmented_Word", "Morph_tag",
        "Morph_type", "Punctuation_Mark", "Invariable_Declinable", "Syntactic_Role", "Possessive_Construct", "Case_Mood",
        "Case_Mood_Marker", "Phrase", "Phrasal_Function", "Notes"]


def saff(s, v, w, seg, word, naw, murab, irab, alama):
    return {"ID": "0", "Sura_No": str(s), "Verse_No": str(v), "Column5": str(w), "Word_No": str(seg), "Word": word,
            "Without_Diacritics": "", "Segmented_Word": "", "Morph_tag": "", "Morph_type": naw, "Punctuation_Mark": "",
            "Invariable_Declinable": murab, "Syntactic_Role": "", "Possessive_Construct": "", "Case_Mood": irab,
            "Case_Mood_Marker": alama, "Phrase": "", "Phrasal_Function": "", "Notes": ""}


rows = [
    # الآية 1:1 — كَتَبَ (فعل مبنيّ)، رَبِّ (مجرور بالكسرة)، فَخُذْ (فاء + فعل)
    saff(1, 1, 1, 1, "كَتَبَ", "Stem", "مبني", "مبني", "الفتح"),
    saff(1, 1, 2, 1, "رَبِّ", "Stem", "معرب", "مجرور", "الكسرة"),
    saff(1, 1, 3, 1, "فَخُذْ", "Prefix", "مبني", "", ""),
    saff(1, 1, 3, 2, "فَخُذْ", "Stem", "مبني", "مبني", "السكون"),
    # الآية 1:2 — كِتَابُهُ (معرب بعده لاحقة: لا طبقة)، بِ (حرف وحده)، كلمةٌ شاذّة (Word مختلفة في صفّيها)
    saff(1, 2, 1, 1, "كِتَابُهُ", "Stem", "معرب", "مرفوع", "الضمة"),
    saff(1, 2, 1, 2, "كِتَابُهُ", "Suffix", "ضمير متصل", "", ""),
    saff(1, 2, 2, 1, "بِ", "Stem", "مبني", "مبني", "الكسرة"),
    saff(1, 2, 3, 1, "سَ", "Stem", "مبني", "مبني", ""),
    saff(1, 2, 3, 2, "سِ", "Stem", "مبني", "مبني", ""),
    # الآية 1:3 — أَحْمَدَ مجرورٌ بالفتحة (ممنوع من الصرف)، كِتَابٌ مرفوع بالضمة (تنوين)
    saff(1, 3, 1, 1, "أَحْمَدَ", "Stem", "معرب", "مجرور", "الفتحة (ممنوع من الصرف)"),
    saff(1, 3, 2, 1, "كِتَابٌ", "Stem", "معرب", "مرفوع", "الضمة"),
    # الآية 1:4 — كِتَابَةٌ (مرفوع بالضمة: «أ»)، مُسْلِمُونَ (مرفوع بالواو: «ج»)، عَصًا (منصوب مقدَّر: «ج»، وآخرُ صفوفه Other_i3rab)،
    # قُلْتُ (مبنيّ)
    saff(1, 4, 1, 1, "كِتَابَةٌ", "Stem", "معرب", "مرفوع", "الضمة"),
    saff(1, 4, 2, 1, "مُسْلِمُونَ", "Stem", "معرب", "مرفوع", "الواو"),
    saff(1, 4, 3, 1, "عَصًا", "Stem", "معرب", "منصوب", "فتحة مقدرة"),
    saff(1, 4, 3, 2, "عَصًا", "Other_i3rab", "None", "", ""),
    saff(1, 4, 4, 1, "قُلْتُ", "Stem", "مبني", "مبني", "السكون"),
]
with open(os.path.join(tmp, "MASAQ.csv"), "w", encoding="utf-8-sig", newline="") as f:
    wr = csv.DictWriter(f, HEAD)
    wr.writeheader()
    wr.writerows(rows)
# QAC: الآية 1:4 فيها أربع كلمات بأرقام 1 و2 و3 و5 — عدّتُها كعدّة MASAQ، و1:4:4 ليس فيها.
qac_txt = """# ترويسة
LOCATION\tFORM\tTAG\tFEATURES
(1:1:1:1)\tkataba\tV\tSTEM|POS:V|PERF|LEM:katab|ROOT:ktb|3MS
(1:1:2:1)\trab~i\tN\tSTEM|POS:N|LEM:rab~|ROOT:rbb|M|GEN
(1:1:3:1)\tfa\tREM\tPREFIX|f:REM+
(1:1:3:2)\txu*o\tV\tSTEM|POS:V|IMPV|LEM:>axa*a|ROOT:Ax*|2MS
(1:2:1:1)\tkita`bu\tN\tSTEM|POS:N|LEM:kita`b|ROOT:ktb|M|NOM
(1:2:1:2)\thu\tPRON\tSUFFIX|PRON:3MS
(1:2:2:1)\tbi\tP\tSTEM|POS:P|LEM:bi
(1:2:3:1)\tsa\tP\tSTEM|POS:P
(1:3:1:1)\t>aHomada\tPN\tSTEM|POS:PN|LEM:>aHomad|ROOT:Hmd|GEN
(1:3:2:1)\tkita`bN\tN\tSTEM|POS:N|LEM:kita`b|ROOT:ktb|M|NOM
(1:4:1:1)\tkita`bapN\tN\tSTEM|POS:N|ROOT:ktb|F|NOM
(1:4:2:1)\tmusolimuwna\tN\tSTEM|POS:N|ROOT:slm|MP|NOM
(1:4:3:1)\taSFA\tN\tSTEM|POS:N|ROOT:ESw|ACC
(1:4:5:1)\tqulotu\tV\tSTEM|POS:V|ROOT:qwl|1S
"""
open(os.path.join(tmp, "qac.txt"), "w", encoding="utf-8").write(qac_txt)
masaq, shudhudh = Q.kalimat_masaq(os.path.join(tmp, "MASAQ.csv"))
assert shudhudh == [(1, 2, 3)], shudhudh
assert list(masaq) == [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), (1, 3, 1), (1, 3, 2), (1, 4, 1), (1, 4, 2),
                       (1, 4, 3), (1, 4, 4)], list(masaq)
assert masaq[(1, 1, 3)]["word"] == "فَخُذْ" and [s["naw"] for s in masaq[(1, 1, 3)]["segs"]] == ["Prefix", "Stem"]
qac = Q.kalimat_qac(os.path.join(tmp, "qac.txt"))
assert qac[(1, 1, 3)] == [{"naw": "PREFIX", "jidhr": None}, {"naw": "STEM", "jidhr": "Ax*"}], qac[(1, 1, 3)]
assert qac[(1, 2, 2)] == [{"naw": "STEM", "jidhr": None}] and (1, 4, 4) not in qac
najah("قارئا MASAQ وQAC على ملفّين مصنوعين، والشذوذ لا يُقاس")

# ٤. الطبقات
assert Q.tabaqa_jidhr(qac[(1, 1, 1)]) == ("i", "كتب")
assert Q.tabaqa_jidhr(qac[(1, 1, 3)]) == ("ii", "ءخذ")
assert Q.tabaqa_jidhr(qac[(1, 2, 2)]) is None
assert Q.tabaqa_jidhr([{"naw": "STEM", "jidhr": "trjm"}]) is None
assert Q.tabaqa_jidhr([{"naw": "STEM", "jidhr": "qwl"}]) is None
assert Q.tabaqa_jidhr([{"naw": "STEM", "jidhr": "bny"}]) is None
assert Q.tabaqa_irab(masaq[(1, 1, 2)]["segs"]) == ("a", "الجرّ")
assert Q.tabaqa_irab(masaq[(1, 3, 1)]["segs"]) == ("b", "الجرّ")
assert Q.tabaqa_irab(masaq[(1, 4, 2)]["segs"]) == ("c", "الرفع")
assert Q.tabaqa_irab(masaq[(1, 4, 3)]["segs"]) == ("c", "النصب")
assert Q.tabaqa_irab(masaq[(1, 2, 1)]["segs"]) is None
assert Q.tabaqa_irab(masaq[(1, 1, 1)]["segs"]) is None
najah("طبقات ف2 (والمعتلّ لا يُقاس) وف3 (و«ج»، وOther_i3rab ليس قطعة)")

# ٥. العدّ على شطرٍ مصنوع (الآيات 1:1–1:4 كلّها) بمخرج قارئٍ مكتوبٍ هنا:
qari = Q.mukhrij_qari([
    "1:1:1\tQABUL\t32 72 104\t1\t1\t1\tكتب\t0\tالنصب",      # جذرٌ موافق (i)؛ مبنيٌّ فلا ف3
    "1:1:2\tQABUL\t60 107 106\t1\t1\t1\tربب\t2\tالجرّ",      # جذرٌ موافق (i)؛ ف3 «أ» موافق
    "1:1:3\tQABUL\t100 25 95\t1\t1\t1\tفخذ\t3\t-",          # جذرٌ مخالف (ii): فخذ/ءخذ
    "1:2:1\tQABUL\t1 2 3\t0\t1\t0\t-\t1\tالرفع",            # فشلُ ف1 على الخلايا؛ لا طبقة ف3 (لاحقة)
    "1:2:2\tQABUL\t106\t0\t0\t0\t-\t2\tالجرّ",              # فشلُ ف1 بالمكوّنين كليهما
    "1:3:1\tQABUL\t3 4 5\t1\t1\t1\t-\t0\tالنصب",            # ف3 «ب»: مرشَّح النصب، MASAQ جرّ ← خلاف
    "1:3:2\tRAFD\tحرف ليس في جدول المخارج: «x»",
    "1:4:1\tQABUL\t6 7 8\t1\t1\t1\t-\t3\t-",                # ف3 «أ»: لا حكم (السكون)
    "1:4:2\tQABUL\t9 10 11\t1\t1\t1\t-\t0\tالنصب",          # ف3 «ج»: مرشَّح النصب، MASAQ رفع ← خلاف
    "1:4:3\tQABUL\t12 13\t1\t1\t1\t-\t3\t-",                # ف3 «ج»: لا حكم
    "1:4:4\tQABUL\t29 55 73\t1\t0\t1\tقلت\t1\tالرفع",       # فشلُ ف1 بعد التسكين وحده؛ ليست في QAC بموضعها (1:4 متساوية العدّة)؛ مبنيّة
])
N = Q.hisab(masaq, qac, qari, {(1, 1), (1, 2), (1, 3), (1, 4)})
assert N["f0"] == {"kalimat": 11, "maqbula": 10, "marfuda": 1, "asbab_alrafd": {"حرف ليس في جدول المخارج: «x»": 1}}, N["f0"]
# على الخلايا ردّ 1:2:1 و1:2:2، وبعد التسكين ردّ 1:2:2 و1:4:4، وكلاهما ردّا 1:2:2.
assert (N["f1"]["dalOK"], N["f1"]["fashl"], N["f1"]["fashl_ala_alkhalaya"], N["f1"]["fashl_baad_altaskin"],
        N["f1"]["fashl_kilahuma"]) == (7, 3, 2, 2, 1), N["f1"]
assert [x["mawdi"] for x in N["f1"]["qaimat_alfashl"]] == ["1:2:1", "1:2:2", "1:4:4"]
assert N["f1"]["suwar_maqbula"] == 10 and N["f1"]["suwar_fashl"] == 3
# صورُ ما قبله المكوّنان معًا (§٥ ف1): 1:1:1 و1:1:2 و1:1:3 و1:3:1 و1:4:1 و1:4:2 و1:4:3 — سبعُ كلماتٍ مختلفة الصور.
assert N["f1"]["suwar_dalOK"] == 7, N["f1"]["suwar_dalOK"]
# الآية 1:2: كلمتان في MASAQ بعد حذف الشاذّة، وثلاث في QAC ← غيرُ متساوية؛ و1:1 و1:3 و1:4 متساوية.
assert N["f2"]["ayat_mutasawiya"] == 3 and N["f2"]["laysa_fi_qac"] == 1, N["f2"]
assert (N["f2"]["i"]["n"], N["f2"]["i"]["wifaq"], N["f2"]["ii"]["n"], N["f2"]["ii"]["wifaq"]) == (2, 2, 1, 0), N["f2"]
assert N["f2"]["khilaf_amthila"]["ii"] == [{"mawdi": "1:1:3", "kalima": "فَخُذْ", "murashshah": "فخذ", "qac": "ءخذ"}]
# فترةُ ولسن 95% يدويًّا: 1/1 ← [0.2065، 1.0]؛ 0/1 ← [0.0، 0.7935]؛ 50/100 ← [0.4038، 0.5962].
assert (N["f3"]["a"]["n"], N["f3"]["a"]["wifaq"], N["f3"]["a"]["khilaf"], N["f3"]["a"]["la_hukm"]) == (2, 1, 0, 1), N["f3"]["a"]
assert N["f3"]["a"]["nisbat_alwifaq_mimma_hukima"] == 1.0 and N["f3"]["a"]["wilson95"] == [0.2065, 1.0], N["f3"]["a"]
assert (N["f3"]["b"]["n"], N["f3"]["b"]["khilaf"], N["f3"]["b"]["wilson95"]) == (1, 1, [0.0, 0.7935]), N["f3"]["b"]
assert (N["f3"]["c"]["n"], N["f3"]["c"]["wifaq"], N["f3"]["c"]["khilaf"], N["f3"]["c"]["la_hukm"]) == (2, 0, 1, 1), N["f3"]["c"]
assert Q.wilson(0, 0) is None and Q.wilson(50, 100) == [0.4038, 0.5962]
# 0/5 ← [0.0، 0.4345]، والحدُّ الأدنى صفرٌ موجب لا «-0.0».
assert Q.wilson(0, 5) == [0.0, 0.4345] and math.copysign(1, Q.wilson(0, 5)[0]) == 1
MUAHHAL = [("1:1:1", "f2:i", "wifaq", "كتب", "كتب"), ("1:1:2", "f2:i", "wifaq", "ربب", "ربب"),
           ("1:1:2", "f3:a", "wifaq", "الجرّ", "الجرّ"), ("1:1:3", "f2:ii", "khilaf", "فخذ", "ءخذ"),
           ("1:3:1", "f3:b", "khilaf", "النصب", "الجرّ"), ("1:4:1", "f3:a", "la_hukm", "-", "الرفع"),
           ("1:4:2", "f3:c", "khilaf", "النصب", "الرفع"), ("1:4:3", "f3:c", "la_hukm", "-", "النصب")]
assert sorted(N["muahhal"]) == MUAHHAL, sorted(N["muahhal"])
assert N["ahliyya"] == {"1:1:1": ["i", "-"], "1:1:2": ["i", "a"], "1:1:3": ["ii", "-"], "1:2:1": ["-", "-"],
                        "1:2:2": ["-", "-"], "1:3:1": ["-", "b"], "1:3:2": ["-", "-"], "1:4:1": ["-", "a"],
                        "1:4:2": ["-", "c"], "1:4:3": ["-", "c"], "1:4:4": ["-", "-"]}, N["ahliyya"]
mu, ah = Q.ayyina_qayyis(N["muahhal"], 3)
assert len(ah) == 3 and set(ah) <= set(MUAHHAL) and all(len(r) == 2 and r[1] in ("f2", "f3") for r in mu)
assert mu == [(r[0], r[1].split(":")[0]) for r in ah]
assert Q.ayyina_qayyis(list(reversed(N["muahhal"])), 3) == (mu, ah)
assert sorted(Q.ayyina_qayyis(N["muahhal"])[1]) == MUAHHAL
# عيّنةُ الأهليّة مطبَّقة: كلمةٌ من كلّ طبقة ومن غير المؤهَّلة (الطبقات هنا بأعضائها يدويًّا).
TABAQAT = {"f2:i": {"1:1:1", "1:1:2"}, "f2:ii": {"1:1:3"}, "f3:a": {"1:1:2", "1:4:1"}, "f3:b": {"1:3:1"},
           "f3:c": {"1:4:2", "1:4:3"}, "la": {"1:2:1", "1:2:2", "1:3:2", "1:4:4"}}
mu2, ah2 = Q.ayyina_ahliyya(N["ahliyya"], 1)
assert mu2 == sorted(mu2) and all(set(mu2) & ks for ks in TABAQAT.values()) and len(mu2) <= 6, mu2
assert ah2 == [(k, N["ahliyya"][k][0], N["ahliyya"][k][1]) for k in mu2]
assert Q.ayyina_ahliyya(N["ahliyya"])[0] == sorted(N["ahliyya"])
# حدُّ الأمثلة: ثلاثون خلافًا في «ب» تُعدّ كلُّها ويُسرد منها 25.
rows2 = [saff(2, 1, w, 1, "أَحْمَدَ", "Stem", "معرب", "مجرور", "الفتحة (ممنوع من الصرف)") for w in range(1, 31)]
with open(os.path.join(tmp, "M2.csv"), "w", encoding="utf-8-sig", newline="") as f:
    wr = csv.DictWriter(f, HEAD)
    wr.writeheader()
    wr.writerows(rows2)
m2, _ = Q.kalimat_masaq(os.path.join(tmp, "M2.csv"))
q2 = Q.mukhrij_qari([f"2:1:{w}\tQABUL\t3 4 5\t1\t1\t1\t-\t0\tالنصب" for w in range(1, 31)])
N2 = Q.hisab(m2, {}, q2, {(2, 1)})
assert N2["f3"]["b"]["khilaf"] == 30 and len(N2["f3"]["khilaf_amthila"]["b"]) == 25
# الصورُ المميّزة لا المواضع (§٥ ف1): «كَتَبَ» في ثلاثة مواضع قبلها المكوّنان، و«بِ» في موضعين ردّاها —
# فالمواضع 3 و2 والصور 1 و1، وصورُ ما قُبل ترميزُه 2.
rows3 = [saff(3, 1, w, 1, "كَتَبَ", "Stem", "مبني", "مبني", "الفتح") for w in (1, 2, 3)] + \
        [saff(3, 1, w, 1, "بِ", "Stem", "مبني", "مبني", "الكسرة") for w in (4, 5)]
with open(os.path.join(tmp, "M3.csv"), "w", encoding="utf-8-sig", newline="") as f:
    wr = csv.DictWriter(f, HEAD)
    wr.writeheader()
    wr.writerows(rows3)
m3, _ = Q.kalimat_masaq(os.path.join(tmp, "M3.csv"))
q3 = Q.mukhrij_qari([f"3:1:{w}\tQABUL\t32 72 104\t1\t1\t1\t-\t0\t-" for w in (1, 2, 3)] +
                    [f"3:1:{w}\tQABUL\t106\t0\t0\t0\t-\t2\t-" for w in (4, 5)])
N3 = Q.hisab(m3, {}, q3, {(3, 1)})
assert (N3["f1"]["dalOK"], N3["f1"]["fashl"]) == (3, 2), N3["f1"]
assert (N3["f1"]["suwar_dalOK"], N3["f1"]["suwar_fashl"], N3["f1"]["suwar_maqbula"]) == (1, 1, 2), N3["f1"]
najah("العدّ على شطرٍ مصنوع بأعدادٍ يدويّة (ف0–ف3)، وولسن يدويًّا، والعيّنتان معمّاتين، وحدّ الأمثلة 25، والصور المميّزة لا المواضع")

# ٦. البصمات
sij = os.path.join(tmp, "sijill.json")


def ktb_sijill(h_masaq):
    json.dump({"sijill": [
        {"milaf": "MASAQ.csv", "sha256": h_masaq, "hala": "مختوم", "naw": "مرجع-محجوب"},
        {"milaf": "quranic-corpus-morphology-0.4.txt", "sha256": hashlib.sha256(qac_txt.encode()).hexdigest(),
         "hala": "مختوم", "naw": "مرجع-محجوب"}]}, open(sij, "w", encoding="utf-8"))


os.rename(os.path.join(tmp, "qac.txt"), os.path.join(tmp, "quranic-corpus-morphology-0.4.txt"))
ktb_sijill(Q.basma(os.path.join(tmp, "MASAQ.csv")))
Q.tahaqquq_basamat(tmp, sij)
ktb_sijill("0" * 64)
try:
    Q.tahaqquq_basamat(tmp, sij)
    raise AssertionError("بصمةٌ مغيَّرة قُبلت")
except Q.Khalal as e:
    assert "MASAQ.csv" in str(e) and "بصمته" in str(e), e
najah("البصمات: المطابقة تُقبل والمغيَّرة تُرفض باسمها")

# ٧. الحراسة: hirasat على مستودعٍ مصنوع، وiedad على مرجعَين مصنوعَين، ومخرجٌ شاذّ من القارئ
repo = os.path.join(tmp, "repo")
os.makedirs(os.path.join(repo, "hawkama"))
os.makedirs(os.path.join(repo, "tahaqquq"))
GENV = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")


def g(*args):
    r = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True, env=GENV)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def ktb(path, txt):
    open(os.path.join(repo, path), "w", encoding="utf-8").write(txt)


def awdi(msg, *paths):
    g("add", *paths)
    g("commit", "-q", "-m", msg)
    g("update-ref", "refs/remotes/origin/main", "HEAD")


g("init", "-q")
ktb("hawkama/qadim.md", "قديم")
awdi("0", "hawkama/qadim.md")
H = lambda **kw: Q.hirasat(repo, kw.get("out", os.path.join(tmp, "out")), kw.get("n", 1), kw.get("tasjil"))
assert "غير مدموج" in H()
ktb(Q.WATHIQA, "وثيقة")
ktb(Q.SCRIPT, "سكربت")
awdi("tasjil", Q.WATHIQA, Q.SCRIPT)
assert H() is None
assert "داخل المستودع" in H(out=os.path.join(repo, "x"))
ktb("hawkama/zaid.md", "x")
assert "غير نظيفة" in H()
os.remove(os.path.join(repo, "hawkama", "zaid.md"))
ktb("hawkama/tasjil2.md", "تسجيلٌ لاحق")
ktb("tahaqquq/jadid.md", "خارج hawkama")
g("add", "hawkama/tasjil2.md", "tahaqquq/jadid.md")
g("commit", "-q", "-m", "laysa_ala_main")
assert "HEAD ليس origin/main" in H()
g("update-ref", "refs/remotes/origin/main", "HEAD")
assert H() is None
for t in (None, Q.WATHIQA, "hawkama/", "hawkama/qadim.md", "hawkama/la_wujud.md", "tahaqquq/qiyas_d.py", "tahaqquq/jadid.md"):
    assert "الشطرُ الثاني" in H(n=2, tasjil=t), t
assert H(n=2, tasjil="hawkama/tasjil2.md") is None
ktb(Q.SCRIPT, "سكربتٌ مغيَّر")
awdi("taghyir", Q.SCRIPT)
assert "تغيّرا" in H()
m3 = os.path.join(tmp, "m3")
os.makedirs(m3)
for src, dst in (("MASAQ.csv", "MASAQ.csv"), ("quranic-corpus-morphology-0.4.txt", "quranic-corpus-morphology-0.4.txt")):
    open(os.path.join(m3, dst), "wb").write(open(os.path.join(tmp, src), "rb").read())
ktb_sijill(Q.basma(os.path.join(m3, "MASAQ.csv")))
try:
    Q.iedad(m3, 1, sij)
    raise AssertionError("بصمةُ شطرٍ مخالفة قُبلت")
except Q.Khalal as e:
    assert "بصمةُ الشطر" in str(e), e
ayat_m = sorted({(k[0], k[1]) for k in masaq})
t1, t2 = Q.shatr(ayat_m)
b1 = Q.basmat_shatr(t1)
assert Q.iedad(m3, 1, sij, b1)[3] == t1 and Q.iedad(m3, 2, sij, b1)[3] == t2 and len(t1) == 2 and len(t2) == 2
ktb_sijill("0" * 64)
try:
    Q.iedad(m3, 1, sij, b1)
    raise AssertionError("iedad قرأ قبل البصمات")
except Q.Khalal as e:
    assert "بصمته" in str(e), e
try:
    Q.mukhrij_qari(["k\tKHALAL\tسطرٌ ليس «مفتاح⇥كلمة»"])
    raise AssertionError("سطرٌ شاذّ قُبل")
except Q.Khalal:
    pass
p = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "tahaqquq", "qiyas_d.py"), os.path.join(ROOT, "x")],
                   capture_output=True, text=True, env=dict(os.environ, MUDAA_DIR=tmp))
assert p.returncode == 2 and "داخل المستودع" in p.stdout, p.stdout
najah("الحراسة: hirasat بحالاتها على مستودعٍ مصنوع، وiedad (البصمات أوّلًا وبصمة الشطر واختيار الشطر)، والسطر الشاذّ")

# ٨. qari --qiyas على كلماتٍ باليد
qari_bin = os.path.join(ROOT, ".lake", "build", "bin", "qari")
madkhal = os.path.join(tmp, "madkhal.tsv")
open(madkhal, "w", encoding="utf-8").write("k1\tكَتَبَ\nk2\tقَالْتُ\nk3\tبِ\nk4\tرَبِّ\nk5\tفَقُلْ\nk6\tكِتَابٌ\nk7\tكتب\n")
o = subprocess.run([qari_bin, "--qiyas", madkhal], capture_output=True, text=True).stdout.splitlines()
assert o[0] == "k1\tQABUL\t32 72 104\t1\t1\t1\tكتب\t0\tالنصب", o[0]
f = o[1].split("\t")
assert f[:5] == ["k2", "QABUL", "28 11 55 73", "0", "1"] and f[6:] == ["-", "1", "الرفع"], o[1]
f = o[2].split("\t")
assert f[:5] == ["k3", "QABUL", "106", "1", "0"] and f[6:] == ["-", "2", "الجرّ"], o[2]
assert o[3] == "k4\tQABUL\t60 107 106\t1\t1\t1\tربب\t2\tالجرّ", o[3]
assert o[4] == "k5\tQABUL\t100 29 55\t1\t1\t1\tفقل\t3\t-", o[4]
assert o[5] == "k6\tQABUL\t34 72 11 107\t1\t1\t1\t-\t3\t-", o[5]
assert o[6].startswith("k7\tRAFD\tحرف بلا حركة في غير آخر الكلمة"), o[6]
assert Q.mukhrij_qari(o)["k5"]["jidhr"] == "فقل"
najah("qari --qiyas على سبع كلماتٍ باليد، وقارئ مخرجه")

print(f"{nj}/8")
