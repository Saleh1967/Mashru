"""جلبُ المودَعات المختومة إلى مجلّدٍ (MUDAA_DIR) من مصادرها العامّة، وإعادةُ بناء المشتقّ منها، بلا ختمٍ جديد.

القاعدة (الدستور م9، م12؛ CLAUDE.md «المودَعات مختومة بالبصمة»): لا يدخل المجلّدَ ملفٌّ إلّا وبصمتُه بصمتُه المختومة في
`mudaat/sijill.json`؛ وما خالفها مرفوضٌ باسمه ولا يُكتب، وما لا مصدرَ معلومًا له يُسمّى «غائبًا» بمصدره المسجَّل. فالجلبُ لا
يغيّر السجلَّ ولا يختم شيئًا: يعيد بايتاتٍ خُتمت، والبصمةُ وحدها تشهد أنّها هي.

المصادر:
  * نصوصُ OpenITI على raw.githubusercontent.com: باليداع المسجَّل حيث سُجّل (lisan، maqayis، mukhassas)، وإلّا الفرعُ الرئيس
    والبصمةُ تحرسه.
  * مرفقاتُ المالك (a1.docx، a2.docx، badiha.docx) من تاريخ مستودعه العامّ hamil-hala-zaman-program بإيداعها.
  * تاجُ العروس من OpenITI، وQAC 0.4 من مرآة alstat/QuranTree.jl، وMASAQ ونصُّ التنزيل من corpora/ في Saleh1967/Alghanem — كلُّها بإيداعٍ مثبَّت.
  * المشتقّ: `luzum_mujam.tsv` بـ`shabaka/jadwal_luzum.py` على lisan وmaqayis المختومين، و`jins.tsv`/`mithal.tsv` بـ`scripts/bina_jadawil_rabt.py`.
  * وما سواها (مرفقاتُ المالك، والمراجعُ المحجوبة، وجداولُ البنّاء، والمرشَّحة) غائبٌ يُسمّى بمصدره المسجَّل.

التشغيل: python3 -I mudaat/jalb.py [<مجلّد>] [--mahalli <مجلّد مصادر>]
  المجلّدُ الافتراضيّ $MUDAA_DIR أو ~/mudaa_dir. و--mahalli يقرأ المصادرَ من مجلّدٍ محلّيّ بأسماء الملفّات (للاختبار، بلا شبكة).
  الخروج: 0 إن حضر كلُّ ما له مصدر، 1 إن رُفض شيءٌ أو تعذّر جلبُه.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

JADHR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = "https://raw.githubusercontent.com/OpenITI/"

OPENITI = {
    "lisan.txt": "0725AH/056df249d6619b428a78f1d69a8ab2851b97b0a6/data/0711IbnManzurIfriqi/0711IbnManzurIfriqi.LisanCarab/"
                 "0711IbnManzurIfriqi.LisanCarab.Shamela0001687-ara1.mARkdown",
    "maqayis.txt": "0400AH/5bb6966d8df2ed22b1bff5cdbe29bb9c24f3ca29/data/0395IbnFarisQazwini/0395IbnFarisQazwini.MucjamMaqayis/"
                   "0395IbnFarisQazwini.MucjamMaqayis.Shamela0021710-ara1",
    "mukhassas.txt": "0475AH/cc9beb0d9645e8cdce892556423b9926a127054f/data/0458IbnSidaMursi/0458IbnSidaMursi.Mukhassas/"
                     "0458IbnSidaMursi.Mukhassas.Shamela0003590-ara1",
    "qatr.txt": "0775AH/master/data/0761JamalDinIbnHisham/0761JamalDinIbnHisham.MatnQatrNada/0761JamalDinIbnHisham.MatnQatrNada.Shamela0011376-ara1",
    "mughni.txt": "0775AH/master/data/0761JamalDinIbnHisham/0761JamalDinIbnHisham.MughniLabib/0761JamalDinIbnHisham.MughniLabib.Shamela0006972-ara1",
    "alfiyya.txt": "0675AH/master/data/0672IbnMalik/0672IbnMalik.Alfiyya/0672IbnMalik.Alfiyya.Shamela0008522-ara1",
    "janadani.txt": "0750AH/master/data/0749BadrDinMisriMuradi/0749BadrDinMisriMuradi.JanaDani/0749BadrDinMisriMuradi.JanaDani.Shamela0026099-ara1",
    "sibawayhi.txt": "0200AH/master/data/0180Sibawayhi/0180Sibawayhi.KitabSibawayhi/0180Sibawayhi.KitabSibawayhi.JK006989-ara1",
}
# مرفقاتُ المالك في تاريخ مستودعه العامّ Saleh1967/hamil-hala-zaman-program (بالإيداع الذي أضافها؛ CLAUDE.md: «وُجدت في تاريخ
# hamil-hala-zaman-program وطابقت بصماتها المختومة»).
HAMIL = "https://raw.githubusercontent.com/Saleh1967/hamil-hala-zaman-program/"
MALIK = {
    "a1.docx": "b7abcad328db8a69349e02ef3e4ad4076b1a7486/%D8%A7%D9%84%D8%B4%D8%AE%D8%B5%D9%8A%D8%A9%20%D8%A7%D9%84%D8%A5%D8%B3%D9%84%D8%A7%D9%85%D9%8A%D8%A9%20"
               "%D8%A7%D9%84%D8%AC%D8%B2%D8%A1%20%D8%A7%D9%84%D8%A3%D9%88%D9%84%20%281%29.docx",
    "a2.docx": "b7abcad328db8a69349e02ef3e4ad4076b1a7486/%D8%A7%D9%84%D8%B4%D8%AE%D8%B5%D9%8A%D8%A9%20%D8%A7%D9%84%D8%A7%D8%B3%D9%84%D8%A7%D9%85%D9%8A%D8%A9%20"
               "%D8%A7%D9%84%D8%AC%D8%B2%D8%A1%20%D8%A7%D9%84%D8%AB%D8%A7%D9%84%D8%AB%20%D9%88%D8%B1%D8%AF%20%282%29.docx",
    "badiha.docx": "2bb18501598278bb3facac84e60cff5bb4b25219/%D8%B3%D8%B1%D8%B9%D8%A9%20%D8%A7%D9%84%D8%A8%D8%AF%D9%8A%D9%87%D8%A9.docx",
}
# مراجعُ ونصوصٌ في مستودعاتٍ عامّة (باليداع؛ والبصمةُ المختومة تحرسها):
#   QAC 0.4: مرآةُ alstat/QuranTree.jl التي يسمّيها سجلُّ المودَعات مرآةً ثانية؛ وMASAQ ونصُّ التنزيل: corpora/ في مستودع المالك Saleh1967/Alghanem.
ALGHANEM = "https://raw.githubusercontent.com/Saleh1967/Alghanem/9d8fa03a51f894416e0abaf3b6821c5ae6441dcd/corpora/"
UKHRA = {
    "taj.txt": RAW + "1225AH/4ec30fc763750fc1233d3774c4416b28c5c8b886/data/1205MurtadaZabidi/1205MurtadaZabidi.TajCarus/"
               "1205MurtadaZabidi.TajCarus.Shamela0007030-ara1",
    "quranic-corpus-morphology-0.4.txt": "https://raw.githubusercontent.com/alstat/QuranTree.jl/d7a0fe9c5c7138081aec6683d18e49f9a233d0dd/data/"
                                         "quranic-corpus-morphology-0.4.txt",
    "MASAQ.csv": ALGHANEM + "MASAQ.csv",
    "quran-simple-enhanced.txt": ALGHANEM + "quran-simple-enhanced.txt",
    # معجمُ التشكيل في A116 (Alghanem docs/tashkil/PREREG.md يسمّي بصمتَه)؛ خُتم 2026-11-20 بأمر المالك.
    "tashkil_mujam.tsv.gz": ALGHANEM + "tashkil/mujam.tsv.gz",
}
URL = {**{k: RAW + v for k, v in OPENITI.items()}, **{k: HAMIL + v for k, v in MALIK.items()}, **UKHRA}

FAKK = ("import gzip, os, shutil, sys; d = sys.argv[1]\n"
        "with gzip.open(os.path.join(d, 'tashkil_mujam.tsv.gz')) as i, open(os.path.join(d, 'tashkil_mujam.tsv'), 'wb') as o:\n"
        "    shutil.copyfileobj(i, o)")

MUSHTAQQ = {
    "luzum_mujam.tsv": (["lisan.txt", "maqayis.txt"], lambda d: [sys.executable, "-I", os.path.join(JADHR, "shabaka", "jadwal_luzum.py")],
                        lambda d: dict(os.environ, MUDAA_DIR=d)),
    "jins.tsv": ([], lambda d: [sys.executable, "-I", os.path.join(JADHR, "scripts", "bina_jadawil_rabt.py"), d], lambda d: None),
    "mithal.tsv": ([], lambda d: [sys.executable, "-I", os.path.join(JADHR, "scripts", "bina_jadawil_rabt.py"), d], lambda d: None),
    # فكُّ ضغط معجم التشكيل كما هو (بايتاتُه بلا تغيير)، ليقرأه وكيلُ `a116-tashkil` في Lean.
    "tashkil_mujam.tsv": (["tashkil_mujam.tsv.gz"], lambda d: [sys.executable, "-I", "-c", FAKK, d], lambda d: None),
    # نصّا ج1 وج3 كما تقرؤهما أسانيدُ الضوابط (test_sakk، test_athar_dabit، …): `pandoc -t plain --wrap=none` (pandoc 3.1.3) يعيد
    # بصمتيهما المكتوبتين في تلك الاختبارات بايتًا (قيس 2026-11-20). وpandoc غيرُ حاضرٍ أو بإصدارٍ آخر: «مرفوض» باسمه لا بديلَ له.
    "a1.txt": (["a1.docx"], lambda d: ["pandoc", "-t", "plain", "--wrap=none", os.path.join(d, "a1.docx"), "-o", os.path.join(d, "a1.txt")],
               lambda d: None),
    "a2.txt": (["a2.docx"], lambda d: ["pandoc", "-t", "plain", "--wrap=none", os.path.join(d, "a2.docx"), "-o", os.path.join(d, "a2.txt")],
               lambda d: None),
}


def basma(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def sijill():
    return json.load(open(os.path.join(JADHR, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]


def ijlib(milaf, d, mahalli):
    """يجلب ملفًّا من OpenITI إلى ملفٍّ مؤقّت ويعيد مساره، أو (None، سبب)."""
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".jalb_")
    os.close(fd)
    if mahalli:
        src = os.path.join(mahalli, milaf)
        if not os.path.exists(src):
            os.remove(tmp)
            return None, "لا مصدرَ محلّيّ"
        shutil.copyfile(src, tmp)
        return tmp, ""
    r = subprocess.run(["curl", "-sS", "-f", "--max-time", "900", "-o", tmp, URL[milaf]], capture_output=True, text=True)
    if r.returncode != 0:
        os.remove(tmp)
        return None, "تعذّر الجلب: " + r.stderr.strip()[-160:]
    return tmp, ""


def main(argv):
    mahalli = None
    if "--mahalli" in argv:
        i = argv.index("--mahalli")
        mahalli = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    d = argv[0] if argv else os.environ.get("MUDAA_DIR") or os.path.expanduser("~/mudaa_dir")
    os.makedirs(d, exist_ok=True)
    mk = {m["milaf"]: m for m in sijill() if m.get("hala") == "مختوم"}
    fashal = 0
    hadir = lambda f: os.path.exists(os.path.join(d, f)) and basma(os.path.join(d, f)) == mk[f]["sha256"]
    for milaf in URL:
        if milaf not in mk:
            print(f"مرفوض: {milaf} ليس مختومًا في السجلّ")
            fashal = 1
            continue
        if hadir(milaf):
            print(f"حاضر: {milaf} {mk[milaf]['sha256'][:12]}")
            continue
        tmp, sabab = ijlib(milaf, d, mahalli)
        if tmp is None:
            print(f"غائب: {milaf} ({sabab})")
            fashal = 1
            continue
        b = basma(tmp)
        if b != mk[milaf]["sha256"]:
            os.remove(tmp)
            print(f"مرفوض: {milaf} بصمةُ المجلوب {b[:12]} ليست المختومة {mk[milaf]['sha256'][:12]}؛ لم يُكتب")
            fashal = 1
            continue
        os.replace(tmp, os.path.join(d, milaf))
        print(f"جُلب: {milaf} {b[:12]} = المختوم")
    for milaf, (usul, amr, bia) in MUSHTAQQ.items():
        if milaf not in mk:
            print(f"مرفوض: {milaf} ليس مختومًا في السجلّ")
            fashal = 1
            continue
        if hadir(milaf):
            print(f"حاضر: {milaf} {mk[milaf]['sha256'][:12]}")
            continue
        naqis = [u for u in usul if not hadir(u)]
        if naqis:
            print(f"غائب: {milaf} (أصولُه غائبة: {'، '.join(naqis)})")
            fashal = 1
            continue
        try:
            r = subprocess.run(amr(d), cwd=JADHR, capture_output=True, text=True, env=bia(d))
        except FileNotFoundError as e:  # أداةُ التوليد (pandoc) غيرُ حاضرة
            print(f"مرفوض: {milaf} أداةُ توليده غائبة ({e.filename})")
            fashal = 1
            continue
        if not hadir(milaf):
            if os.path.exists(os.path.join(d, milaf)):
                os.remove(os.path.join(d, milaf))
            print(f"مرفوض: {milaf} لم يُعِده مولِّدُه ببصمته المختومة (خروج {r.returncode})")
            fashal = 1
            continue
        print(f"بُني: {milaf} {mk[milaf]['sha256'][:12]} = المختوم")
    ma_la_masdar = [f for f in mk if f not in URL and f not in MUSHTAQQ and not hadir(f)]
    for f in ma_la_masdar:
        print(f"غائبٌ بلا جلب: {f} — مصدرُه المسجَّل: {mk[f].get('masdar', '')[:110]}")
    murashshah = [m["milaf"] for m in sijill() if m.get("hala") == "مرشح"]
    if murashshah:
        print(f"مرشَّحةٌ لا تُجلب (غيرُ مختومة؛ بايتاتُها ليست في مستودع): {'، '.join(murashshah)}")
    print(f"الجلب: {sum(hadir(f) for f in list(URL) + list(MUSHTAQQ) if f in mk)} من {len(URL) + len(MUSHTAQQ)} حاضرٌ في {d}؛ "
          f"وبلا جلب {len(ma_la_masdar)}، ومرشَّحة {len(murashshah)}")
    return fashal


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
