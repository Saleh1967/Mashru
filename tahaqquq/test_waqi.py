"""اختبار جدول «الواقع المختوم» (`waqi_001.tsv`، مرشّحٌ حتّى يأذن المالك بختمه) و«جدول التعريفات» (`taarifat.tsv`، «وضع»، مرشّح)،
ومطابقة `Aql/WaqiJadwal.lean` (مولَّد) و`Aql/WaqiShawahid.lean` لهما.

١. بلا مودَع (دائمًا) — مفحوص بطفرات:
   أ. المولِّد `scripts/bina_waqi.py` على جدولٍ صغيرٍ يكتبه الاختبار: السطرُ المتوقَّع مكتوبٌ هنا يدويًّا (بتهريب «"» و«\\»)، والبصمةُ
      بصمةُ بايتات الجدول الصغير؛ ووجهٌ مجهولٌ يُرفض. (P438)
   ب. قواعدُ الاستخراج في `scripts/rasd_waqi.py` على مدخلاتٍ يدويّة بتوقّعاتٍ يدويّة (منها: «kamil» يردّ ما كان أكثرَ من سطر). (P437)
   ج. الرصدُ على حواسَّ يضعها الاختبار: حاسّةٌ تخرج بغير صفرٍ تُرفض الدفعةُ باسمها ولا يُكتب شيءٌ في المجلّد — لا الجدول ولا مخرجُ الحاسّة
      الناجحة قبلها (P441؛ والكتابةُ بعد النجاح يحرسها هذا التأكيد بلا طفرةٍ تخصّها)؛ وحاسّتان ناجحتان تُكتبان بأعمدتهما؛ ودفعةٌ ثانيةٌ
      بصمةُ سابقتها ليست قيدًا مختومًا في السجلّ تُردّ بلا كتابة (P442).
   د. مرآةُ الحكم (مكتوبةٌ هنا مستقلّةً عن Lean) على جدولٍ يدويّ بأحكامٍ متوقَّعةٍ يدويًّا، قبل الختم وبعده — بلا طفرةٍ تخصّها: تُستعمل
      في ٢هـ لعدّ القضايا على الجدول الحقيقيّ.
   هـ. نصُّ `Aql/Waqi.lean` بلا تعليقات فيه قاعدةُ الحكم وشرطُ الختم وشرطُ الشواهد — فحصُ نصٍّ كاشفٌ لا حارس، والحراسةُ في Lean
      (P434–P436، P439–P440 تُفشل البناء).
٢. بالمودَع (MUDAA_DIR وفيه waqi_001.tsv وtaarifat.tsv؛ وإلّا خرج 0 بعد ١) — فحصٌ بالمودَع بلا طفرة (لا يُشغَّل في CI)، فلا يُوسم
   فوق ما دون «مفحوص»:
   أ. بصمتا الجدولين بصمتاهما في mudaat/sijill.json، بنوعيهما «واقع-مختوم» و«وضع».
   ب. المولِّد على waqi_001.tsv يعيد `Aql/WaqiJadwal.lean` بايتًا بايتًا.
   ج. كلُّ صفٍّ يطابق مدخلَه في سجلّ الحواسّ `HAWASS` (الأمرُ بقالبه، والحاسّة، والمصدر، والشيء، والخاصّة، والوجه، والقاعدة) — فلا صفَّ
      بيد؛ ومخرجُه الخامّ حاضرٌ باسم بصمته وبصمتُه تطابق، والقيمةُ تُستخرج منه بقاعدتها، ولا خروجَ بغير صفرٍ إلّا في قاعدة «khuruj».
   د. إعادةُ المشاهدة: الحواسُّ الحتميّة (قائمةٌ يدويّة: ما يقرأ الإيداعَ المرصود وحده، وتشغيلُ print(2+3)، وبرهانا Lean) تُعاد بأمرها
      المسجَّل حرفًا فيطابق مخرجُها البصمةَ المسجَّلة؛ ما لم يحضر الإيداعُ أو الأداةُ يُطبع «لم يُعَد».
   هـ. المرآةُ على الجدول الحقيقيّ تعطي أعدادَ `adad` و`ihsa` في `Aql/WaqiShawahid.lean`.
   و. التعريفات: ثلاثةٌ منها نصوصُها مكتوبةٌ هنا يدويًّا؛ وكلُّها تُستخرج ثانيةً من مصادرها بأسطرها فتطابق (بالقاعدة نفسها — مطابقةٌ لا
      توقّعٌ مستقلّ)، وبصماتُ المصادر، ودرجتُها «آحاد»، وصفوفُ الواقع المحال إليها؛ وملفُّ دستور الوكيل غيرُ مودَع: إن تغيّر طُبع ولم يُفشل.
التشغيل: python3 -I tahaqquq/test_waqi.py
"""
import glob
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bawwaba  # noqa: E402 — ماسحُ تعليقات Lean نفسُه الذي تستعمله البوّابة


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def bila_taaliq(path):
    s = open(os.path.join(ROOT, path), encoding="utf-8").read()
    return " ".join(bawwaba.bila_taaliq(s, bawwaba._taaliq_lean(s)).split())


rasd = load("rasd_waqi", "scripts/rasd_waqi.py")
bina = load("bina_waqi", "scripts/bina_waqi.py")
ok = 0

# ١أ: المولِّد على جدولٍ صغير
HEAD = "raqm\thassa\tamr\tmasdar\tmawdu\tsifa\tqima\twajh\tistikhraj\tbasmat_mukhraj\tkhuruj\twaqt\tdafa\tsabiq\n"
mini = (HEAD + '1\th1\tcmd\tمصدر"أ\tش\\ي\tخ\tق\tقياس\tkamil\t00\t0\tt\t1\t-\n'
        + '2\th2\tcmd\tم\tش\tخ\t5\tرواية\tkamil\t00\t0\tt\t2\t-\n').encode("utf-8")
lean = bina.wallid(mini).split("\n")
assert '  ⟨1, 1, "h1", "مصدر\\"أ", "ش\\\\ي", "خ", "ق", .qiyas⟩,' in lean, lean
assert '  ⟨2, 2, "h2", "م", "ش", "خ", "5", .riwaya⟩' in lean, lean
assert f'def basma : String := "{hashlib.sha256(mini).hexdigest()}"' in lean, lean
try:
    bina.wallid((HEAD + "1\th\tc\tم\tش\tخ\tق\tرأي\tkamil\t00\t0\tt\t1\t-\n").encode("utf-8"))
    raise AssertionError("وجهٌ مجهولٌ لم يُرفض")
except SystemExit:
    pass
ok += 1

# ١ب: قواعد الاستخراج
I = rasd.istakhrij
assert I("kamil", b"a\nb\n", 0) is None
assert I("kamil", b" x \n", 0) == "x"
assert I("awwal", b"\nfirst\nsecond\n", 0) == "first"
assert I("adad", b"a\n\nb\n", 0) == "2"
assert I("satran", b"Aql\nDal\n", 0) == "Aql،Dal"
assert I("adad_lahiqa:.lean", b"A.lean\nb.py\nc.lean\n", 0) == "2"
assert I("adad_fih:Co", b"x Co y\nz\nCo\n", 0) == "2"
assert I("adad_bidaya:#p", b"#p a\n x #p\n#p b\n", 0) == "2"
assert I("satr:X", b"a\nzzXzz\n", 0) == "zzXzz"
assert I("regex:v([0-9.]+)", b"leanprover/lean4:v4.34.1\n", 0) == "4.34.1"
assert I("json:mubarhanat", b'{"mubarhanat": 7}', 0) == "7"
assert I("khuruj", b"", 1) == "1"
ok += 1

# ١ج: الرصدُ على حواسَّ يضعها الاختبار
def rasd_ala(hawass):
    tmp = tempfile.mkdtemp()
    asli_h, asli_a = rasd.HAWASS, sys.argv
    rasd.HAWASS, sys.argv = hawass, ["rasd", tmp, "--commit", "0000000", "--dafa", "1"]
    try:
        rasd.main()
        return tmp, None
    except SystemExit as e:
        return tmp, str(e.code)
    finally:
        rasd.HAWASS, sys.argv = asli_h, asli_a


Q = rasd.QIYAS
tmp, khata = rasd_ala([("printf", "printf 'x\\n'", "م", "ش", "خ", Q, "kamil"), ("false", "false", "م", "ش", "خ2", Q, "adad")])
assert khata and "خرجت 1" in khata and "لا قياسَ من فشل" in khata, khata
assert os.listdir(tmp) == [], os.listdir(tmp)
shutil.rmtree(tmp)
tmp, khata = rasd_ala([("printf", "printf 'x\\n'", "م", "ش", "خ", Q, "kamil"), ("false", "false", "م", "ش", "رمز", Q, "khuruj")])
assert khata is None, khata
safs = open(os.path.join(tmp, "waqi_001.tsv"), encoding="utf-8").read().split("\n")
assert safs[1].split("\t")[:9] == ["1", "printf", "printf 'x\\n'", "م", "ش", "خ", "x", "قياس", "kamil"], safs[1]
assert safs[2].split("\t")[6] == "1" and safs[2].split("\t")[10] == "1", safs[2]
assert os.path.exists(os.path.join(tmp, "waqi_shawahid", hashlib.sha256(b"x\n").hexdigest()))
shutil.rmtree(tmp)
# دفعةٌ ثانية بلا بصمةِ سابقةٍ مختومة في السجلّ تُردّ، ولا يُكتب شيء
asli = sys.argv
tmp = tempfile.mkdtemp()
asli_h, rasd.HAWASS = rasd.HAWASS, [("printf", "printf 'x\n'", "م", "ش", "خ", Q, "kamil")]
sys.argv = ["rasd", tmp, "--commit", "0000000", "--dafa", "2", "--sabiq", "0" * 64]
try:
    rasd.main()
    khata = None
except SystemExit as e:
    khata = str(e.code)
finally:
    rasd.HAWASS, sys.argv = asli_h, asli
assert khata and "--sabiq" in khata and os.listdir(tmp) == [], khata
shutil.rmtree(tmp)
ok += 1

# ١د: مرآةُ الحكم (مستقلّةٌ عن Lean): الصفوفُ المختومة وحدها ترفع
def hukm(rows, m, s, q, makhtum):
    l = [r for r in rows if (r["mawdu"], r["sifa"], r["qima"]) == (m, s, q)]
    k = [r for r in l if makhtum(r)]
    if any(r["wajh"] == "قياس" for r in k):
        return "مفهوم"
    rw = [r for r in k if r["wajh"] == "رواية"]
    if any(a["masdar"] != b["masdar"] for a in rw for b in rw):
        return "مفهوم"
    return "لا حكم" if not l else "معلومة"


def row(m, s, q, w, src, dafa=1):
    return {"mawdu": m, "sifa": s, "qima": q, "wajh": w, "masdar": src, "dafa": dafa}


YADAWI = [row("م1", "خ", "ق", "قياس", "أ"), row("م2", "خ", "ق", "رواية", "أ"), row("م2", "خ", "ق", "رواية", "أ"),
          row("م3", "خ", "ق", "رواية", "أ"), row("م3", "خ", "ق", "رواية", "ب"), row("م5", "خ", "ق", "قياس", "أ", dafa=2)]
kull = lambda r: True
awwal = lambda r: r["dafa"] == 1
la = lambda r: False
assert hukm(YADAWI, "م1", "خ", "ق", kull) == "مفهوم" and hukm(YADAWI, "م1", "خ", "ق", la) == "معلومة"
assert hukm(YADAWI, "م2", "خ", "ق", kull) == "معلومة"
assert hukm(YADAWI, "م3", "خ", "ق", kull) == "مفهوم" and hukm(YADAWI, "م3", "خ", "ق", la) == "معلومة"
assert hukm(YADAWI, "م5", "خ", "ق", awwal) == "معلومة" and hukm(YADAWI, "م5", "خ", "ق", kull) == "مفهوم"
assert hukm(YADAWI, "م4", "خ", "ق", kull) == "لا حكم" and hukm(YADAWI, "م1", "خ", "ق2", kull) == "لا حكم"
ok += 1

# ١هـ: نصُّ القاعدة في Lean
src = bila_taaliq("Aql/Waqi.lean")
for s in ("let k := makhtuma sijill basmaOf l", "if fiihiQiyas k || tawatur k then .mafhum", "else if l.isEmpty then .laHukm",
          "else .maaluma", "a.wajh == .riwaya && b.wajh == .riwaya && a.masdar != b.masdar",
          "l.filter fun r => makhtum sijill (basmaOf r.dafa)", "if hukm sijill basmaOf T m s q = .mafhum then"):
    assert s in src, s
ok += 1

d = os.environ.get("MUDAA_DIR")
if not d or not os.path.exists(os.path.join(d, "waqi_001.tsv")):
    print(f"لم يُشغَّل على الجدولين (غير حاضرين؛ عيّن MUDAA_DIR وفيه waqi_001.tsv وtaarifat.tsv)؛ بلا مودَع {ok}/5")
    sys.exit(0)

# ٢أ: السجلّ
sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]


def qayd(milaf, naw):
    m = [x for x in sijill if x["milaf"] == milaf]
    assert len(m) == 1, (milaf, m)
    b = hashlib.sha256(open(os.path.join(d, milaf), "rb").read()).hexdigest()
    assert m[0]["sha256"] == b and m[0]["naw"] == naw and m[0]["hala"] in ("مختوم", "مرشح"), (milaf, m[0]["hala"])
    return m[0], b


qw, bw = qayd("waqi_001.tsv", "واقع-مختوم")
qt, bt = qayd("taarifat.tsv", "وضع")

# ٢ب: المولَّد بايتًا
data = open(os.path.join(d, "waqi_001.tsv"), "rb").read()
assert bina.wallid(data) == open(os.path.join(ROOT, "Aql", "WaqiJadwal.lean"), encoding="utf-8").read()

# ٢ج: كلُّ صفٍّ من سجلّ الحواسّ، ومخرجُه الخامّ واستخراجُه
lines = data.decode("utf-8").split("\n")
head = lines[0].split("\t")
rows = [dict(zip(head, l.split("\t"))) for l in lines[1:] if l]
assert len(rows) == len(rasd.HAWASS), (len(rows), len(rasd.HAWASS))


def qalib(s):
    return re.escape(s).replace(re.escape("{C}"), "[0-9a-f]{7,40}").replace(re.escape("{MUDAA}"), ".+").replace(
        re.escape("{DUSTUR}"), ".+")


for r, (hassa, amr, masdar, mawdu, sifa, wajh, qaida) in zip(rows, rasd.HAWASS):
    assert (r["hassa"], r["masdar"], r["sifa"], r["wajh"], r["istikhraj"]) == (hassa, masdar, sifa, wajh, qaida), r["raqm"]
    assert re.fullmatch(qalib(amr), r["amr"]) and re.fullmatch(qalib(mawdu), r["mawdu"]), r["raqm"]
    raw = open(os.path.join(d, "waqi_shawahid", r["basmat_mukhraj"]), "rb").read()
    assert hashlib.sha256(raw).hexdigest() == r["basmat_mukhraj"], r["raqm"]
    assert rasd.istakhrij(r["istikhraj"], raw, int(r["khuruj"])) == r["qima"], r["raqm"]
    assert r["khuruj"] == "0" or r["istikhraj"] == "khuruj", r["raqm"]

# ٢د: إعادةُ المشاهدة — الحواسُّ الحتميّة بيد المختبِر
HATMIYYA = {2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 26, 27, 28, 29, 32, 33, 45, 48, 49}
commit = rows[1]["qima"]
hadir = subprocess.run(["git", "cat-file", "-e", commit + "^{commit}"], cwd=ROOT, capture_output=True).returncode == 0
lean_hadir = shutil.which("lean") is not None
uida, lam = 0, []
for r in rows:
    if int(r["raqm"]) not in HATMIYYA:
        continue
    if (not hadir and "git" in r["amr"]) or (not lean_hadir and "lean" in r["amr"]):
        lam.append(r["raqm"])
        continue
    p = subprocess.run(["bash", "-c", r["amr"]], cwd=ROOT, capture_output=True)
    assert hashlib.sha256(p.stdout).hexdigest() == r["basmat_mukhraj"] and str(p.returncode) == r["khuruj"], r["raqm"]
    uida += 1

# ٢هـ: المرآةُ على الجدول الحقيقيّ وأعدادُ Lean
qadaya = list(dict.fromkeys((r["mawdu"], r["sifa"], r["qima"]) for r in rows))
qabl = [hukm(rows, *k, la) for k in qadaya]
bad = [hukm(rows, *k, kull) for k in qadaya]
shaw = bila_taaliq("Aql/WaqiShawahid.lean")
kwiya = sum(r["wajh"] == "قياس" for r in rows)
assert (f"jadwal.length = {len(rows)} ∧ (jadwal.filter (·.wajh == .qiyas)).length = {kwiya} ∧ "
        f"(jadwal.filter (·.wajh == .riwaya)).length = {len(rows) - kwiya}") in shaw, "adad"
assert (f"qadaya.length = {len(qadaya)} ∧ (qadaya.map (hukmQ qabl)).count .maaluma = {qabl.count('معلومة')} ∧ "
        f"(qadaya.map (hukmQ bad)).count .mafhum = {bad.count('مفهوم')} ∧ (qadaya.map (hukmQ bad)).count .maaluma = "
        f"{bad.count('معلومة')}") in shaw, "ihsa"
assert qabl.count("معلومة") == len(qadaya)

# ٢و: التعريفات
tdata = open(os.path.join(d, "taarifat.tsv"), "rb").read().decode("utf-8").split("\n")
thead = tdata[0].split("\t")
tarifat = {t["raqm"]: t for t in (dict(zip(thead, l.split("\t"))) for l in tdata[1:] if l)}
YADAWIYYA = {
    "1": "# المشروع: محرّك عربيّ مبرهن (الدال وحده ← المدلول وحده ← الدال والمدلول معًا ← العقلية ← الجواب)",
    "3": "المراحل بترتيبها: الدال وحده ← المدلول وحده ← الدال والمدلول معًا.",
    "19": "* لكلّ مودَع نوعٌ من أربعة: واقع-مختوم، وضع، معلومات-سابقة، مرجع-محجوب.",
}
for k, v in YADAWIYYA.items():
    assert tarifat[k]["taarif"] == v, k
raqmat = {r["raqm"]: r for r in rows}
dustur = sorted(glob.glob("/root/.claude/skills/synced/*/dustur-al-wakil/SKILL.md"))
tuida, tlam, taghayyar = 0, [], []
for t in tarifat.values():
    assert t["daraja"] == "آحاد", t["raqm"]
    m = re.fullmatch(r"(.*):L(\d+)(?:–(\d+))?", t["masdar"])
    assert m, t["masdar"]
    loc, a = m.group(1), int(m.group(2))
    b = int(m.group(3) or a)
    if loc.startswith("دستور الوكيل"):
        if not dustur:
            tlam.append(t["raqm"])
            continue
        src_bytes = open(dustur[0], "rb").read()
        if hashlib.sha256(src_bytes).hexdigest() != t["basmat_masdar"]:
            taghayyar.append(t["raqm"])
            continue
    elif loc.startswith("waqi_001.tsv الصفّ "):
        n = re.match(r"waqi_001.tsv الصفّ (\d+) ", loc).group(1)
        src_bytes = open(os.path.join(d, "waqi_shawahid", raqmat[n]["basmat_mukhraj"]), "rb").read()
    else:
        path, _, c = loc.rpartition("@")
        if not hadir:
            tlam.append(t["raqm"])
            continue
        if path.startswith((".claude/", "tahaqquq/", "mudaat/")):
            assert t["wadi"] == f"ملفّ المشروع ({path})", t["raqm"]
        src_bytes = subprocess.run(["git", "show", f"{c}:{path}"], cwd=ROOT, capture_output=True, check=True).stdout
    nass = " / ".join(x.lstrip() for x in src_bytes.decode("utf-8").split("\n")[a - 1:b])
    assert nass == t["taarif"] and hashlib.sha256(src_bytes).hexdigest() == t["basmat_masdar"], t["raqm"]
    assert t["basmat_waqi"] == bw, t["raqm"]
    for s in filter(lambda x: x != "-", t["shawahid_waqi"].split(",")):
        assert s in raqmat, (t["raqm"], s)
    tuida += 1
ok += 1

print(f"جدول الواقع المختوم ({qw['hala']}، {bw[:12]}…): {len(rows)} مشاهدة ({kwiya} قياسًا)، كلُّها من سجلّ الحواسّ، WaqiJadwal.lean "
      f"مخرجُ المولِّد بايتًا، والمخرجاتُ الخامّة ببصماتها، وأُعيدت {uida} مشاهدةً حتميّة فطابقت"
      + (f" (لم يُعَد: {'،'.join(lam)})" if lam else "")
      + f"؛ القضايا {len(qadaya)}: قبل الختم معلومة كلُّها، وبعده مفهوم {bad.count('مفهوم')} ومعلومة {bad.count('معلومة')}؛ "
      f"والتعريفات ({qt['hala']}، {bt[:12]}…): {len(tarifat)}، 3 منها بنصٍّ يدويّ، وأُعيد استخراجُ {tuida} من مصادرها فطابقت"
      + (f" (لم يُعَد: {'،'.join(tlam)})" if tlam else "")
      + (f" (تغيّر مصدرُها غيرُ المودَع: {'،'.join(taghayyar)})" if taghayyar else "") + f" — {ok}/6")
