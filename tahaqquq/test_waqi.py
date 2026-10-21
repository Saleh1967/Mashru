"""اختبار جدول «الواقع المختوم» (`waqi_001.tsv`، مرشّحٌ حتّى يأذن المالك بختمه) و«جدول التعريفات» (`taarifat.tsv`، «وضع»، مرشّح)،
ومطابقة `Aql/WaqiJadwal.lean` (مولَّد) و`Aql/WaqiShawahid.lean` لهما.

١. بلا مودَع (دائمًا):
   أ. المولِّد `scripts/bina_waqi.py` على جدولٍ صغيرٍ يكتبه الاختبار: السطرُ المتوقَّع مكتوبٌ هنا يدويًّا (بتهريب «"» و«\\»)، والبصمةُ
      بصمةُ بايتات الجدول الصغير؛ ووجهٌ مجهولٌ يُرفض.
   ب. قواعدُ الاستخراج في `scripts/rasd_waqi.py` على مدخلاتٍ يدويّة بتوقّعاتٍ يدويّة (منها: «kamil» يردّ ما كان أكثرَ من سطر).
   ج. مرآةُ الحكم (مكتوبةٌ هنا مستقلّةً عن Lean) على جدولٍ يدويّ بأحكامٍ متوقَّعةٍ يدويًّا: قياسٌ مفهوم؛ حكايتان من مصدرٍ واحد معلومة؛
      حكايتان من مصدرين مفهوم؛ ولا صفّ لا حكم.
   د. نصُّ `Aql/Waqi.lean` بلا تعليقات فيه قاعدةُ الحكم بفروعها الثلاثة — فحصُ نصٍّ كاشفٌ لا حارس، والحراسةُ في Lean.
٢. بالمودَع (MUDAA_DIR وفيه waqi_001.tsv وtaarifat.tsv؛ وإلّا خرج 0 بعد ١):
   أ. بصمتا الجدولين بصمتاهما في mudaat/sijill.json، بنوعيهما «واقع-مختوم» و«وضع».
   ب. المولِّد على waqi_001.tsv يعيد `Aql/WaqiJadwal.lean` بايتًا بايتًا.
   ج. لكلّ صفّ: مخرجُه الخامّ حاضرٌ في waqi_shawahid باسم بصمته وبصمتُه تطابق، والقيمةُ تُستخرج منه بقاعدتها كما سُجّلت.
   د. **إعادةُ المشاهدة:** الحواسُّ الحتميّة (قائمةٌ يدويّة: ما يقرأ الإيداعَ المرصود وحده، وتشغيلُ print(2+3)، وبرهانا Lean) تُعاد بأمرها
      المسجَّل حرفًا، فيطابق مخرجُها البصمةَ المسجَّلة — ما لم يحضر الإيداعُ أو الأداةُ يُعدّ «لم يُعَد» ويُطبع.
   هـ. مرآةُ الحكم على الجدول الحقيقيّ تعطي أعدادَ `ihsa` و`adad` في `Aql/WaqiShawahid.lean` (القضايا المتمايزة 44: مفهوم 21، معلومة 23).
   و. كلُّ تعريفٍ في taarifat.tsv يُستخرج ثانيةً من مصدره بأسطره (git show <الإيداع>:<المسار>، أو ملفّ دستور الوكيل إن حضر، أو مخرجٍ
      خامّ) فيطابق، وبصمةُ المصدر تطابق، وصفوفُ الواقع المحال إليها موجودة.
التشغيل: python3 -I tahaqquq/test_waqi.py
"""
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


rasd = load("rasd_waqi", "scripts/rasd_waqi.py")
bina = load("bina_waqi", "scripts/bina_waqi.py")
ok = 0

# ١أ: المولِّد على جدولٍ صغير
HEAD = "raqm\thassa\tamr\tmasdar\tmawdu\tsifa\tqima\twajh\tistikhraj\tbasmat_mukhraj\tkhuruj\twaqt\tdafa\tsabiq\n"
mini = (HEAD + '1\th1\tcmd\tمصدر"أ\tش\\ي\tخ\tق\tقياس\tkamil\t00\t0\tt\t1\t-\n'
        + '2\th2\tcmd\tم\tش\tخ\t5\tحكاية\tkamil\t00\t0\tt\t1\t-\n').encode("utf-8")
lean = bina.wallid(mini)
assert '  ⟨1, "h1", "مصدر\\"أ", "ش\\\\ي", "خ", "ق", .qiyas⟩,' in lean.split("\n"), lean
assert '  ⟨2, "h2", "م", "ش", "خ", "5", .hikaya⟩' in lean.split("\n"), lean
assert f'def basma : String := "{hashlib.sha256(mini).hexdigest()}"' in lean.split("\n"), lean
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

# ١ج: مرآةُ الحكم (مستقلّةٌ عن Lean)
def hukm(rows, m, s, q):
    l = [r for r in rows if (r["mawdu"], r["sifa"], r["qima"]) == (m, s, q)]
    if any(r["wajh"] == "قياس" for r in l):
        return "مفهوم"
    h = [r for r in l if r["wajh"] == "حكاية"]
    if any(a["masdar"] != b["masdar"] for a in h for b in h):
        return "مفهوم"
    return "لا حكم" if not l else "معلومة"


def row(m, s, q, w, src):
    return {"mawdu": m, "sifa": s, "qima": q, "wajh": w, "masdar": src}


YADAWI = [row("م1", "خ", "ق", "قياس", "أ"), row("م2", "خ", "ق", "حكاية", "أ"), row("م2", "خ", "ق", "حكاية", "أ"),
          row("م3", "خ", "ق", "حكاية", "أ"), row("م3", "خ", "ق", "حكاية", "ب")]
assert hukm(YADAWI, "م1", "خ", "ق") == "مفهوم"
assert hukm(YADAWI, "م2", "خ", "ق") == "معلومة"
assert hukm(YADAWI, "م3", "خ", "ق") == "مفهوم"
assert hukm(YADAWI, "م4", "خ", "ق") == "لا حكم"
assert hukm(YADAWI, "م1", "خ", "ق2") == "لا حكم"
ok += 1

# ١د: نصُّ قاعدة الحكم في Lean
src = open(os.path.join(ROOT, "Aql", "Waqi.lean"), encoding="utf-8").read()
src = bawwaba.bila_taaliq(src, bawwaba._taaliq_lean(src))
for s in ("if fiihiQiyas l || tasdiq l then .mafhum", "else if l.isEmpty then .laHukm", "else .maaluma",
          "a.wajh == .hikaya && b.wajh == .hikaya && a.masdar != b.masdar"):
    assert s in src, s
ok += 1

d = os.environ.get("MUDAA_DIR")
if not d or not os.path.exists(os.path.join(d, "waqi_001.tsv")):
    print(f"لم يُشغَّل على الجدولين (غير حاضرين؛ عيّن MUDAA_DIR وفيه waqi_001.tsv وtaarifat.tsv)؛ بلا مودَع {ok}/4")
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

# ٢ج: المخرجاتُ الخامّة والاستخراج
lines = data.decode("utf-8").split("\n")
head = lines[0].split("\t")
rows = [dict(zip(head, l.split("\t"))) for l in lines[1:] if l]
for r in rows:
    raw = open(os.path.join(d, "waqi_shawahid", r["basmat_mukhraj"]), "rb").read()
    assert hashlib.sha256(raw).hexdigest() == r["basmat_mukhraj"], r["raqm"]
    assert rasd.istakhrij(r["istikhraj"], raw, int(r["khuruj"])) == r["qima"], r["raqm"]

# ٢د: إعادةُ المشاهدة — الحواسُّ الحتميّة بيد المختبِر
HATMIYYA = {2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 26, 27, 28, 29, 32, 33, 43, 46, 47}
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
ahkam = [hukm(rows, *k) for k in qadaya]
shaw = open(os.path.join(ROOT, "Aql", "WaqiShawahid.lean"), encoding="utf-8").read()
shaw = bawwaba.bila_taaliq(shaw, bawwaba._taaliq_lean(shaw))
kwiya = sum(r["wajh"] == "قياس" for r in rows)
assert (f"jadwal.length = {len(rows)} ∧ (jadwal.filter (·.wajh == .qiyas)).length = {kwiya}" in shaw
        and f"(jadwal.filter (·.wajh == .hikaya)).length = {len(rows) - kwiya}" in shaw), "adad"
assert (f"qadaya.length = {len(qadaya)} ∧ (qadaya.map hukmQ).count .mafhum = {ahkam.count('مفهوم')} ∧ "
        f"(qadaya.map hukmQ).count .maaluma = {ahkam.count('معلومة')}" in shaw), "ihsa"
assert hukm(rows, "Lean", "الإصدار", "4.34.1") == "مفهوم" and hukm(rows, "Python", "الإصدار", "3.13.16") == "معلومة"

# ٢و: التعريفات
tdata = open(os.path.join(d, "taarifat.tsv"), "rb").read().decode("utf-8").split("\n")
thead = tdata[0].split("\t")
tarifat = [dict(zip(thead, l.split("\t"))) for l in tdata[1:] if l]
raqmat = {r["raqm"] for r in rows}
byraqm = {r["raqm"]: r for r in rows}
dustur = sorted(__import__("glob").glob("/root/.claude/skills/synced/*/dustur-al-wakil/SKILL.md"))
tuida, tlam = 0, []
for t in tarifat:
    m = re.fullmatch(r"(.*):L(\d+)(?:–(\d+))?", t["masdar"])
    assert m, t["masdar"]
    loc, a = m.group(1), int(m.group(2))
    b = int(m.group(3) or a)
    if loc.startswith("دستور الوكيل"):
        if not dustur:
            tlam.append(t["raqm"])
            continue
        src_bytes = open(dustur[0], "rb").read()
    elif loc.startswith("waqi_001.tsv الصفّ "):
        n = re.match(r"waqi_001.tsv الصفّ (\d+) ", loc).group(1)
        src_bytes = open(os.path.join(d, "waqi_shawahid", byraqm[n]["basmat_mukhraj"]), "rb").read()
    else:
        path, _, c = loc.rpartition("@")
        if not hadir:
            tlam.append(t["raqm"])
            continue
        src_bytes = subprocess.run(["git", "show", f"{c}:{path}"], cwd=ROOT, capture_output=True, check=True).stdout
    nass = " / ".join(x.strip() for x in src_bytes.decode("utf-8").split("\n")[a - 1:b])
    assert nass == t["taarif"] and hashlib.sha256(src_bytes).hexdigest() == t["basmat_masdar"], t["raqm"]
    for s in filter(lambda x: x != "-", t["shawahid_waqi"].split(",")):
        assert s in raqmat, (t["raqm"], s)
    tuida += 1
ok += 1

print(f"جدول الواقع المختوم ({qw['hala']}، {bw[:12]}…): {len(rows)} مشاهدة ({kwiya} قياسًا)، WaqiJadwal.lean مخرجُ المولِّد بايتًا، "
      f"والمخرجاتُ الخامّة ببصماتها، وأُعيدت {uida} مشاهدةً حتميّة فطابقت" + (f" (لم يُعَد: {'،'.join(lam)})" if lam else "")
      + f"؛ القضايا {len(qadaya)}: مفهوم {ahkam.count('مفهوم')}، معلومة {ahkam.count('معلومة')}؛ "
      f"والتعريفات ({qt['hala']}، {bt[:12]}…): {len(tarifat)}، أُعيد استخراجُ {tuida} من مصادرها فطابقت"
      + (f" (لم يُعَد: {'،'.join(tlam)})" if tlam else "") + f" — {ok}/5")
