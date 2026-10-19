"""اختبارُ منفّذ القياس المسجَّل (`tahaqquq/qiyas_d.py`) ووضعِ القياس في القارئ (`qari --qiyas`) — على بياناتٍ مصنوعةٍ هنا
وكلماتٍ مختارة باليد، لا على المرجعين المحجوبين (لا يقرأ MUDAA_DIR أبدًا).

التوقّعاتُ مكتوبةٌ باليد مستقلّةً عن الشيفرة:
١. جدولُ بكوالتر للجذور: «ktb» ← كتب، «Alh» ← ءله (A همزة)، «qwl» ← قول؛ وحرفٌ خارجه خللٌ باسمه.
٢. الشطران: منفصلان، اتّحادُهما الكلّ، نصفٌ ونصف، وثابتان بالبذرة.
٣. قارئا MASAQ وQAC على ملفّين مصنوعين: الكلمةُ بمفتاحها وقطعها، وكلمةٌ اختلفت Word في صفّيها شذوذٌ لا يُقاس.
٤. الطبقات: ف2 (i) قطعةٌ واحدة ذاتُ جذر، (ii) أكثر، ولا طبقة لكلمةٍ بلا جذر أو بجذرٍ رباعيّ؛ ف3 «أ» بحركةٍ قصيرة، «ب» ممنوعٌ من
   الصرف، ولا طبقة لمعربٍ بعده لاحقة.
٥. العدّ على شطرٍ مصنوع بأعدادٍ محسوبةٍ باليد (التفصيل عند كلّ توقّع).
٦. البصمات: تُقبل المطابقة، ويُرفض الملفّ المغيَّر باسمه.
٧. الحراسة: مجلّدُ إخراجٍ داخل المستودع مرفوض، والشطرُ الثاني بلا --tasjil مرفوض.
٨. `qari --qiyas` على كلماتٍ باليد: الخلايا 4×الحامل+الحال (فهارسُ `Dal.hawamil`: ك8 ت18 ب26 ق7 ا2 ل13 ر15 ف25)، والقانونُ
   على الخلايا وبعد التسكين (كَتَبَ 1/1، وقَالْتُ 0/1 شاهدُ المالك qaltu، وبِ 1/0 بخانةٍ واحدة)، ومرشَّحُ الجذر، وحالُ الآخر،
   والإعرابُ المرشَّح (الفتحة نصب، والكسرة جرّ، والسكون «-»)؛ وغيرُ المشكول مرفوضٌ باسمه.
التشغيل: python3 -I tahaqquq/test_qiyas_d.py
"""
import csv
import hashlib
import json
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


# ١. جدولُ بكوالتر
assert Q.jidhr_arabi("ktb") == "كتب"
assert Q.jidhr_arabi("Alh") == "ءله"
assert Q.jidhr_arabi("qwl") == "قول"
assert Q.jidhr_arabi("$Er") == "شعر"
try:
    Q.jidhr_arabi("k'b")
    raise AssertionError("حرفٌ خارج الجدول قُبل")
except Q.Khalal:
    pass
najah("جدول بكوالتر للجذور")

# ٢. الشطران
ayat = [(1, i) for i in range(1, 11)] + [(2, i) for i in range(1, 5)]
s1, s2 = Q.shatr(ayat)
assert s1.isdisjoint(s2) and s1 | s2 == set(ayat) and len(s1) == 7 and len(s2) == 7, (s1, s2)
assert Q.shatr(list(reversed(ayat))) == (s1, s2)
assert Q.shatr(ayat, Q.BADHRA + 1) != (s1, s2)
najah("الشطران: منفصلان، تامّان، نصفان، ثابتان بالبذرة ومستقلّان عن ترتيب الإدخال")

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
    # الآية 1:1 — كَتَبَ (فعل مبنيّ)، رَبِّ (مجرور بالكسرة)، فَقُلْ (فاء + فعل)
    saff(1, 1, 1, 1, "كَتَبَ", "Stem", "مبني", "مبني", "الفتح"),
    saff(1, 1, 2, 1, "رَبِّ", "Stem", "معرب", "مجرور", "الكسرة"),
    saff(1, 1, 3, 1, "فَقُلْ", "Prefix", "مبني", "", ""),
    saff(1, 1, 3, 2, "فَقُلْ", "Stem", "مبني", "مبني", "السكون"),
    # الآية 1:2 — كِتَابُهُ (معرب بعده لاحقة: لا طبقة)، بِ (حرف وحده)، كلمةٌ شاذّة (Word مختلفة في صفّيها)
    saff(1, 2, 1, 1, "كِتَابُهُ", "Stem", "معرب", "مرفوع", "الضمة"),
    saff(1, 2, 1, 2, "كِتَابُهُ", "Suffix", "ضمير متصل", "", ""),
    saff(1, 2, 2, 1, "بِ", "Stem", "مبني", "مبني", "الكسرة"),
    saff(1, 2, 3, 1, "سَ", "Stem", "مبني", "مبني", ""),
    saff(1, 2, 3, 2, "سِ", "Stem", "مبني", "مبني", ""),
    # الآية 1:3 — أَحْمَدَ مجرورٌ بالفتحة (ممنوع من الصرف)، كِتَابٌ مرفوع بالضمة (تنوين)
    saff(1, 3, 1, 1, "أَحْمَدَ", "Stem", "معرب", "مجرور", "الفتحة (ممنوع من الصرف)"),
    saff(1, 3, 2, 1, "كِتَابٌ", "Stem", "معرب", "مرفوع", "الضمة"),
]
with open(os.path.join(tmp, "MASAQ.csv"), "w", encoding="utf-8-sig", newline="") as f:
    wr = csv.DictWriter(f, HEAD)
    wr.writeheader()
    wr.writerows(rows)
qac_txt = """# ترويسة
LOCATION\tFORM\tTAG\tFEATURES
(1:1:1:1)\tkataba\tV\tSTEM|POS:V|PERF|LEM:katab|ROOT:ktb|3MS
(1:1:2:1)\trab~i\tN\tSTEM|POS:N|LEM:rab~|ROOT:rbb|M|GEN
(1:1:3:1)\tfa\tREM\tPREFIX|f:REM+
(1:1:3:2)\tqulo\tV\tSTEM|POS:V|IMPV|LEM:qaAla|ROOT:qwl|2MS
(1:2:1:1)\tkita`bu\tN\tSTEM|POS:N|LEM:kita`b|ROOT:ktb|M|NOM
(1:2:1:2)\thu\tPRON\tSUFFIX|PRON:3MS
(1:2:2:1)\tbi\tP\tSTEM|POS:P|LEM:bi
(1:2:3:1)\tsa\tP\tSTEM|POS:P
(1:3:1:1)\t>aHomada\tPN\tSTEM|POS:PN|LEM:>aHomad|ROOT:Hmd|GEN
(1:3:2:1)\tkita`bN\tN\tSTEM|POS:N|LEM:kita`b|ROOT:ktb|M|NOM
"""
open(os.path.join(tmp, "qac.txt"), "w", encoding="utf-8").write(qac_txt)
masaq, shudhudh = Q.kalimat_masaq(os.path.join(tmp, "MASAQ.csv"))
assert shudhudh == [(1, 2, 3)], shudhudh
assert list(masaq) == [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), (1, 3, 1), (1, 3, 2)], list(masaq)
assert masaq[(1, 1, 3)]["word"] == "فَقُلْ" and [s["naw"] for s in masaq[(1, 1, 3)]["segs"]] == ["Prefix", "Stem"]
qac = Q.kalimat_qac(os.path.join(tmp, "qac.txt"))
assert qac[(1, 1, 3)] == [{"naw": "PREFIX", "jidhr": None}, {"naw": "STEM", "jidhr": "qwl"}], qac[(1, 1, 3)]
assert qac[(1, 2, 2)] == [{"naw": "STEM", "jidhr": None}]
najah("قارئا MASAQ وQAC على ملفّين مصنوعين، والشذوذ لا يُقاس")

# ٤. الطبقات
assert Q.tabaqa_jidhr(qac[(1, 1, 1)]) == ("i", "كتب")
assert Q.tabaqa_jidhr(qac[(1, 1, 3)]) == ("ii", "قول")
assert Q.tabaqa_jidhr(qac[(1, 2, 2)]) is None
assert Q.tabaqa_jidhr([{"naw": "STEM", "jidhr": "trjm"}]) is None
assert Q.tabaqa_irab(masaq[(1, 1, 2)]["segs"]) == ("a", "الجرّ")
assert Q.tabaqa_irab(masaq[(1, 3, 1)]["segs"]) == ("b", "الجرّ")
assert Q.tabaqa_irab(masaq[(1, 2, 1)]["segs"]) is None
assert Q.tabaqa_irab(masaq[(1, 1, 1)]["segs"]) is None
najah("طبقات ف2 وف3")

# ٥. العدّ على شطرٍ مصنوع (الآيات 1:1 و1:2 و1:3 كلّها) بمخرج قارئٍ مكتوبٍ هنا:
qari = Q.mukhrij_qari([
    "1:1:1\tQABUL\t32 72 104\t1\t1\t1\tكتب\t0\tالنصب",      # جذرٌ موافق (i)؛ مبنيٌّ فلا ف3
    "1:1:2\tQABUL\t60 107 106\t1\t1\t1\tربب\t2\tالجرّ",      # جذرٌ موافق (i)؛ ف3 «أ» موافق
    "1:1:3\tQABUL\t100 29 55\t1\t1\t1\tفقل\t3\t-",          # جذرٌ مخالف (ii): فقل/قول
    "1:2:1\tQABUL\t1 2 3\t0\t1\t0\t-\t1\tالرفع",            # فشلُ ف1 على الخلايا؛ لا طبقة ف3 (لاحقة)
    "1:2:2\tQABUL\t106\t1\t0\t0\t-\t2\tالجرّ",              # فشلُ ف1 بعد التسكين
    "1:3:1\tQABUL\t3 4 5\t1\t1\t1\t-\t0\tالنصب",            # ف3 «ب»: مرشَّح النصب، MASAQ جرّ ← خلاف
    "1:3:2\tRAFD\tحرف ليس في جدول المخارج: «x»",
])
N = Q.hisab(masaq, qac, qari, {(1, 1), (1, 2), (1, 3)})
assert N["f0"] == {"kalimat": 7, "maqbula": 6, "marfuda": 1, "asbab_alrafd": {"حرف ليس في جدول المخارج: «x»": 1}}, N["f0"]
assert (N["f1"]["dalOK"], N["f1"]["fashl"]) == (4, 2), N["f1"]
assert [x["mawdi"] for x in N["f1"]["qaimat_alfashl"]] == ["1:2:1", "1:2:2"]
assert N["f1"]["suwar_maqbula"] == 6 and N["f1"]["suwar_fashl"] == 2
# الآية 1:2: ثلاث كلمات في MASAQ قبل حذف الشاذّة ← بعده اثنتان، وفي QAC ثلاث ← غيرُ متساوية؛ 1:1 و1:3 متساويتان.
assert N["f2"]["ayat_mutasawiya"] == 2, N["f2"]
assert (N["f2"]["i"]["n"], N["f2"]["i"]["wifaq"], N["f2"]["ii"]["n"], N["f2"]["ii"]["wifaq"]) == (2, 2, 1, 0), N["f2"]
assert N["f2"]["khilaf_amthila"]["ii"] == [{"mawdi": "1:1:3", "kalima": "فَقُلْ", "murashshah": "فقل", "qac": "قول"}]
assert N["f3"]["a"] == {"n": 1, "wifaq": 1, "khilaf": 0, "la_hukm": 0, "nisbat_alwifaq_mimma_hukima": 1.0,
                        "wilson95": Q.wilson(1, 1)}, N["f3"]["a"]
assert (N["f3"]["b"]["n"], N["f3"]["b"]["khilaf"]) == (1, 1)
assert Q.wilson(0, 0) is None and Q.wilson(50, 100) == [0.4038, 0.5962]
# المؤهَّلون للعيّنة: ثلاثة في ف2 (1:1:1، 1:1:2، 1:1:3) واثنان في ف3 (1:1:2 «أ»، 1:3:1 «ب»).
assert sorted(N["muahhal"]) == [("1:1:1", "f2:i", "wifaq", "كتب", "كتب"), ("1:1:2", "f2:i", "wifaq", "ربب", "ربب"),
                                ("1:1:2", "f3:a", "wifaq", "الجرّ", "الجرّ"), ("1:1:3", "f2:ii", "khilaf", "فقل", "قول"),
                                ("1:3:1", "f3:b", "khilaf", "النصب", "الجرّ")], N["muahhal"]
ay = Q.ayyina_qayyis(N["muahhal"], 3)
assert len(ay) == 3 and set(ay) <= set(N["muahhal"]) and ay == Q.ayyina_qayyis(list(reversed(N["muahhal"])), 3)
assert sorted(Q.ayyina_qayyis(N["muahhal"])) == sorted(N["muahhal"])
najah("العدّ على شطرٍ مصنوع بأعدادٍ يدويّة (ف0–ف3)، وفترة ولسن (50/100: 0.4038–0.5962)، وعيّنة الفحص المستقلّ")

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

# ٧. الحراسة
env = dict(os.environ, MUDAA_DIR=tmp)
p = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "tahaqquq", "qiyas_d.py"), os.path.join(ROOT, "x")],
                   capture_output=True, text=True, env=env)
assert p.returncode == 2 and "داخل المستودع" in p.stdout, p.stdout
p = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "tahaqquq", "qiyas_d.py"), os.path.join(tmp, "out"),
                    "--shatr", "2"], capture_output=True, text=True, env=env)
assert p.returncode == 2 and "--tasjil" in p.stdout, p.stdout
najah("الحراسة: الإخراجُ داخل المستودع مرفوض، والشطر الثاني بلا تسجيلٍ لاحق مرفوض")

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
