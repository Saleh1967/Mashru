"""اختبارات المخزن والفاحص التنفيذيّ. التوقّعات مكتوبة باليد من معنى كلّ حالة، لا من مخرَج الفاحص.

١. المخزن (makhzan.tsv): الفاحص يقبل الادّعاءات الـ240 كلّها (120 مطابقة + 120 تحت-العنوان)، ووسم كلٍّ 1
   («تقدير»)، وبصمة الملفّ هي المختومة في makhzan.sha256؛ وبلا سجلّ المودَعات تُرفض كلّها.
٢. fasid.tsv (البنية): صحيح يُقبل؛ قانون قبل مقدّماته يُرفض؛ أصل غير مودَع يُرفض؛ «مبرهن» على سند «تقدير» يُرفض؛
   قول لا تنتجه السلسلة يُرفض؛ وسم «رأي» أدنى من سنده يُقبل.
٣. fasid_qanun.tsv: قانون على غير هيئة قوانين القاعدة يُرفض خطأً، ويخرج الفاحص بغير صفر.
٤. fasid_ilmi.tsv: أصلٌ علميّ وسمه «مفحوص» يُقيَّد إلى «مقيس»؛ العقليّ لا يُقيَّد.
٥. السؤال: z6537 له حكمٌ واحد تحت-العنوان بخمس خطوات؛ وz1 ليس في العيّنة: «لا حكم»، لا نفي.
٦. fasid_idaa.tsv: «مبرهن» من مودَع مسجَّل يُقيَّد إلى «مطابق»؛ أصلٌ ببصمة غير مسجَّلة لا يُقبل؛ نوع مجهول خطأ.
٧. fasid_dalala.tsv (شواهد ج3 737): الإنسان→الحيوان تضمّنًا بسلسلة (وضع، مطابقة، جزء) يُقبل بقوّة 4؛
   الأسد→الشجاعة التزامًا بسلسلة (وضع، مطابقة، خارج، لزوم) يُقبل بقوّة 4؛ بلا لزوم يُرفض («اللزوم شرط»)؛
   تضمّنٌ يقفز فوق المطابقة يُرفض؛ «مبرهن» من الكتاب يُرفض؛ وثلاثة قوانين خارج القاعدة ترفضها الهيئة:
   تضمّن بلفظٍ آخر في النتيجة (سطر 7)، واسم مخترع (8)، ونتيجة لا توافق الاسم (9).
٨. maratib.tsv (الدستور م15–16): شاهدٌ واحد في مودَع «واقع مختوم» يجعل «الكوكب-النهاري» مفهومًا؛ وشاهدان في
   مودَع «معلومات سابقة» يتركان «طائر-خرافي» معلومة (التكرار لا يرفع)؛ القضيّتان من حيث هي؛ الفهرس 2/1/1.
   وفي المخزن الحقيقيّ لا مودَع واقعٍ مختوم، فكلّ المعاني معلومة.
٩. fasid_basma.tsv (سدّ البصمة الفارغة 2026-10-19): بصمةُ مودَعٍ فارغة، وقصيرة، و63 حرفًا، و65 حرفًا — أربعةُ أخطاء
   «بصمة ليست sha256»؛ و64 حرفًا تُقبل. وأصلٌ سندُه فارغ مع سجلٍّ غير فارغ لا يُقبل، فادّعاؤه مرفوض — شاهدُ سلامةٍ لا يميّز
   سدَّ البصمة الفارغة (السجلّ المقروء لا يحمل بصمةً فارغة أصلًا لشرط الطول؛ ودليلُ السدّ في Lean)؛ وأصلٌ سندُه يبدأ ببصمة
   المودَع السليم («وضع»، سقفُه مطابق) يُقبل ادّعاؤه بقوّة 4 («مطابق»).
١٠. التحميل المحقَّق (خطّة الإطلاق التجريبي P1-أ، 2026-10-22): الملفّ الأوّل سجلّ المودَعات وحده، والبقيّة محتوًى لا يحمل `mudaa`.
   فنُقلت أسطر `mudaa` من مُثُل الاختبار إلى سجلّات اختبارٍ (sijill_ikhtibar، sijill_maratib، fasid_naw_sijill،
   fasid_basma_sijill)، وحلّ محلّها في المحتوى تعليقٌ «#» بعددها فلم تتغيّر أرقام الأسطر المتوقَّعة. وتغيّر توقّعان باسمهما:
   «بلا سجلّ» صار سجلًّا فارغًا (os.devnull) لا غيابَ ملفّ، وأخطاءُ بصمة fasid_basma صارت أخطاءَ السجلّ «السجلّ، سطر …».
١١. fasid_haqn.tsv (هجوم أُعيد على 1bff783 فرفع المعنى إلى «مفهوم»): محتوًى يسجّل مودَع «واقع مختوم» مصطنعًا ويستشهد به.
   الفاحص يسمّيه خطأً ويُبقي مودَعات السجلّ 25؛ والسؤال لا يجيب (خروج 1، «خطأ تحميل»، لا «حكم» ولا «مفهوم»).
١٢. خطأ التحميل غيرُ «لا حكم»: fasid_qanun (قانون خارج القاعدة) كان السؤال عليه يخرج 0 بـ«لا حكم» من قاعدةٍ جزئيّة؛
   فصار يخرج 1 بـ«خطأ تحميل» ولا يطبع «لا حكم».
١٣. السجلّ لا يحمل إلّا `mudaa`: المخزن نفسه سجلًّا يُرفض كلُّ سطرٍ فيه باسمه، فلا مودَع.
١٤. القارئ يستهلك التحميل نفسه: على fasid_haqn يخرج 1 بـ«خطأ تحميل» ولا يقرأ الكلمة.
١٥. sahih_musawi.tsv: خطوة «a=» قضيّتها يحمل معناها «=» (شطرا بيت) تُقرأ ويُقبل ادّعاؤها بقوّة 1. كان المحلّل يقسم الخطوة على
   كلّ «=» فيرفضها «سلسلة لا تُقرأ»: سطرا makhzan_kamil 138997 و139031، وكان القارئ يُسقطهما بصمت حتّى صار التحميل محقَّقًا.
   (وما بقي مفتوحًا عن قصد: شاهدٌ بموضعٍ لا وجود له في دفعة واقعٍ مختومة، أو بصفٍّ لقضيّةٍ أخرى، ما زال يرفع المعنى —
   الحزمة P2 في الخطّة، لا هذه.)
١٦. sahih_tikrar_asl.tsv (س1، 2026-10-24): قضيّةٌ لها أصلان، فأوّلُهما أصلُها كما في `find?`. taht:zA:j1 أوّلُ أصلَيها بسندٍ
   مسجَّل فيُقبل ادّعاؤه بقوّة 1، وfi:j1:j2 أوّلُ أصلَيها بسندٍ غير مسجَّل فيُرفض ادّعاؤه وإن كان الثاني مسجَّلًا. (أنّ
   البحثَ في الجدول هو `find?` مبرهن: `jadwalUsul_find`، `bina_asl`، `bina_aslB`، `bina_aslW`؛ وهذا الاختبارُ يحرس
   «أوّلُ أصلٍ» من جهة التحميل، وطفرتُه P470: أصلٌ يحذف ما قبله لقضيّته عند التحميل.)
   ونموُّ الزمن (س1) في tahaqquq/test_sura.py، آخرَ اختبارات الطفرات.
التشغيل: python3 -I mawsua/test_mawsua.py
"""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXE = os.path.join(ROOT, ".lake", "build", "bin", "faahis")
QARI = os.path.join(ROOT, ".lake", "build", "bin", "qari")
SIJILL = os.path.join(ROOT, "mudaat", "sijill.tsv")


def m(name):
    return os.path.join(ROOT, "mawsua", name)


IKHTIBAR = m("sijill_ikhtibar.tsv")


def faahis(name, sijill):
    """الملفّ الأوّل سجلّ المودَعات، والثاني المحتوى."""
    p = subprocess.run([EXE, sijill, m(name)], capture_output=True, text=True)
    rows = [l.split("\t") for l in p.stdout.splitlines()]
    return p.returncode, rows


def ahkam(rows):
    return {int(r[0]): (r[1], r[2]) for r in rows if len(r) == 3 and r[0].isdigit()}


def sual(badia, name="makhzan.tsv", sijill=SIJILL):
    p = subprocess.run([EXE, "--sual", badia, sijill, m(name)], capture_output=True, text=True)
    return p.returncode, p.stdout.splitlines()


ok = 0
raw = open(os.path.join(ROOT, "mawsua", "makhzan.tsv"), "rb").read()
assert hashlib.sha256(raw).hexdigest() == open(os.path.join(ROOT, "mawsua", "makhzan.sha256")).read().strip(), \
    "المخزن تغيّرت بصمته"
ok += 1

code, rows = faahis("makhzan.tsv", SIJILL)
hukm = [r for r in rows if len(r) == 3 and r[0].isdigit()]
assert code == 0, "الفاحص رفض شيئًا من المخزن"
assert len(hukm) == 240 and all(r[1] == "مقبول" and r[2] == "1" for r in hukm), hukm[:3]
ok += 1

code, rows = faahis("makhzan.tsv", os.devnull)
hukm = [r for r in rows if len(r) == 3 and r[0].isdigit()]
assert code == 1 and len(hukm) == 240 and all(r[1] == "مرفوض" for r in hukm), hukm[:2]
ok += 1

code, rows = faahis("fasid.tsv", IKHTIBAR)
assert code == 1 and ahkam(rows) == {
    6: ("مقبول", "1"), 7: ("مرفوض", "سلسلة لا يقبلها الفاحص"), 8: ("مرفوض", "سلسلة لا يقبلها الفاحص"),
    9: ("مرفوض", "وسم فوق سنده"), 10: ("مرفوض", "سلسلة لا يقبلها الفاحص"), 11: ("مقبول", "1")}, ahkam(rows)
ok += 1

code, rows = faahis("fasid_qanun.tsv", IKHTIBAR)
assert code == 1 and any(r[0] == "خطأ" and "قانون خارج القاعدة" in r[1] for r in rows), rows
ok += 1

code, rows = faahis("fasid_ilmi.tsv", IKHTIBAR)
assert code == 1 and ahkam(rows) == {5: ("مرفوض", "وسم فوق سنده"), 6: ("مقبول", "2"), 7: ("مقبول", "3")}, ahkam(rows)
ok += 1

code, out = sual("taht:z6537:")
assert code == 0 and out[0].startswith("حكم (1)"), out
assert "taht:z6537:j290" in out[1] and out[1].endswith("تقدير"), out[1]
assert len([l for l in out[2:] if l.strip().startswith(("أصل", "قانون"))]) == 5, out
assert out[-2].strip() == "مرتبة القضيّة: من حيث هي" and out[-1] == "الفهرس: من حيث هي 1، معلومة 0، مفهوم 0", out[-2:]
ok += 1

code, out = sual("taht:z1:")
assert code == 0 and out == ["لا حكم: لا مدخل في المخزن يوافق «taht:z1:». الغياب ليس امتناعًا."], out
ok += 1

code, rows = faahis("fasid_idaa.tsv", IKHTIBAR)
assert code == 1 and ahkam(rows) == {5: ("مرفوض", "وسم فوق سنده"), 6: ("مقبول", "4"),
                                     7: ("مرفوض", "سلسلة لا يقبلها الفاحص")}, ahkam(rows)
ok += 1

code, rows = faahis("fasid_naw.tsv", m("fasid_naw_sijill.tsv"))
assert code == 1 and any(r[0] == "خطأ" and "نوع مودَع مجهول" in r[1] for r in rows), rows
ok += 1

code, rows = faahis("fasid_dalala.tsv", IKHTIBAR)
assert code == 1 and ahkam(rows) == {
    15: ("مقبول", "4"), 16: ("مقبول", "4"), 17: ("مرفوض", "سلسلة لا يقبلها الفاحص"),
    18: ("مرفوض", "سلسلة لا يقبلها الفاحص"), 19: ("مرفوض", "وسم فوق سنده")}, ahkam(rows)
akhta = sorted(int(r[1].split()[1].rstrip(":")) for r in rows if r[0] == "خطأ" and "قانون خارج القاعدة" in r[1])
assert akhta == [7, 8, 9], akhta
ok += 1

code, out = sual("mutabaqa:", name="maratib.tsv", sijill=m("sijill_maratib.tsv"))
assert code == 0 and out[0] == "حكم (2) بالقاعدة shahid-maratib:", out
assert "    المعنى «الكوكب-النهاري»: مفهوم (شواهد واقع: 1)" in out, out
assert "    المعنى «طائر-خرافي»: معلومة (لا شاهد واقعٍ مودَع)" in out, out
assert out.count("    مرتبة القضيّة: من حيث هي") == 2, out
assert out[-1] == "الفهرس: من حيث هي 2، معلومة 1، مفهوم 1", out[-1]
ok += 1

code, out = sual("mutabaqa:اللحم")
assert code == 0 and out[0] == "حكم (1) بالقاعدة mawsua-0.1:" and "قائل:أبو زيد" in out[2], out[:3]
assert any(l.endswith("معلومة (لا شاهد واقعٍ مودَع)") for l in out) and out[-1].endswith("مفهوم 0"), out
ok += 1

# بصمةُ المودَع sha256 (64 حرفًا) شرطُ دخوله السجلّ: الفارغةُ والقصيرة خطآن مسمّيان (Faahis/Lib.lean، سطر «mudaa»)؛
# وبه لا يبلغ قيدٌ فارغ aslMusajjal ولا shuhudMutabara ولا nawSanadMin من المنفّذ (سدّ البصمة الفارغة 2026-10-19).
code, rows = faahis("fasid_basma.tsv", m("fasid_basma_sijill.tsv"))
assert code == 1 and [r[1] for r in rows if r[0] == "خطأ"] == [f"السجلّ، سطر {i}: بصمة ليست sha256" for i in (1, 2, 3, 4)], rows
assert ahkam(rows) == {9: ("مرفوض", "سلسلة لا يقبلها الفاحص"), 10: ("مقبول", "4")}, ahkam(rows)
ok += 1

# ١١. هجوم السلطة: المحتوى لا يسجّل مودَعًا (muhtawa_la_yudif_mudaa، tahmil_mudaat). عددُ المودَعات عددُ أسطر mudaa في السجلّ.
N_SIJILL = sum(1 for l in open(SIJILL, encoding="utf-8") if l.startswith("mudaa\t"))
code, rows = faahis("fasid_haqn.tsv", SIJILL)
akhta = [r[1] for r in rows if r[0] == "خطأ"]
assert code == 1 and akhta == ["سطر 2: المحتوى لا يسجّل مودَعًا: السلطة في سجلّ المودَعات وحده"], rows
assert rows[-1][0].startswith(f"القاعدة mawsua-0.1: مودَعات {N_SIJILL}،"), rows[-1]
ok += 1
code, out = sual("mutabaqa:أسيا", name="fasid_haqn.tsv")
assert code == 1 and out[0] == "خطأ تحميل\tسطر 2: المحتوى لا يسجّل مودَعًا: السلطة في سجلّ المودَعات وحده", out
assert not any(l.startswith("حكم") or "مفهوم (" in l for l in out), out
ok += 1

# ١٢. خطأ التحميل غيرُ «لا حكم»: قانونٌ خارج القاعدة يوقف السؤال باسمه.
code, out = sual("taht:zA", name="fasid_qanun.tsv", sijill=IKHTIBAR)
assert code == 1 and out[0].startswith("خطأ تحميل\tسطر 3: قانون خارج القاعدة"), out
assert not any(l.startswith(("لا حكم", "حكم")) for l in out), out
ok += 1

# ١٣. السجلّ لا يحمل إلّا mudaa: المخزن سجلًّا — كلُّ سطرٍ غير فارغ فيه خطأٌ باسمه (وليس فيه mudaa)، ولا مودَع.
code, rows = faahis("makhzan.tsv", m("makhzan.tsv"))
akhta = [r[1] for r in rows if r[0] == "خطأ"]
ghayr_farigh = sum(1 for l in open(m("makhzan.tsv"), encoding="utf-8") if l.strip())
# والمخزن محتوًى بلا خطأ (البند ١ أعلاه)، فكلُّ الأخطاء أخطاءُ السجلّ.
assert code == 1 and len(akhta) == ghayr_farigh and all(e.startswith("السجلّ، سطر ") for e in akhta), (len(akhta), ghayr_farigh)
assert akhta[0] == "السجلّ، سطر 1: السجلّ لا يحمل إلّا مودَعات (mudaa)", akhta[:2]
assert rows[-1][0].startswith("القاعدة mawsua-0.1: مودَعات 0،"), rows[-1]
ok += 1

# ١٤. القارئ يستهلك التحميل نفسه: لا قراءة على تحميلٍ لم يتحقّق.
p = subprocess.run([QARI, SIJILL, m("fasid_haqn.tsv"), "ذَهَبَ"], capture_output=True, text=True)
out = p.stdout.splitlines()
assert p.returncode == 1 and out[0].startswith("خطأ تحميل\tسطر 2: المحتوى لا يسجّل مودَعًا"), out
assert not any(l.startswith("الكلمة: ") for l in out), out
ok += 1

# ١٥. «=» في معنى قضيّة الخطوة لا يكسرها.
code, rows = faahis("sahih_musawi.tsv", IKHTIBAR)
assert code == 0 and ahkam(rows) == {5: ("مقبول", "1")} and not any(r[0] == "خطأ" for r in rows), rows
ok += 1

# ١٦. الأصلُ المكرَّر: أوّلُ سطرٍ للقضيّة هو أصلُها.
code, rows = faahis("sahih_tikrar_asl.tsv", IKHTIBAR)
assert code == 1 and ahkam(rows) == {7: ("مقبول", "1"), 8: ("مرفوض", "سلسلة لا يقبلها الفاحص")}, rows
assert not any(r[0] == "خطأ" for r in rows), rows
ok += 1

print(f"{ok}/21")
