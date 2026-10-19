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
   «بصمة ليست sha256»؛ و64 حرفًا تُقبل. وأصلٌ سندُه فارغ مع سجلٍّ غير فارغ لا يُقبل، فادّعاؤه مرفوض؛ وأصلٌ سندُه يبدأ
   ببصمة المودَع السليم («وضع»، سقفُه مطابق) يُقبل ادّعاؤه بقوّة 4 («مطابق»).
التشغيل: python3 -I mawsua/test_mawsua.py
"""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXE = os.path.join(ROOT, ".lake", "build", "bin", "faahis")
SIJILL = os.path.join(ROOT, "mudaat", "sijill.tsv")


def faahis(name, sijill=True):
    files = ([SIJILL] if sijill and name == "makhzan.tsv" else []) + [os.path.join(ROOT, "mawsua", name)]
    p = subprocess.run([EXE] + files, capture_output=True, text=True)
    rows = [l.split("\t") for l in p.stdout.splitlines()]
    return p.returncode, rows


def ahkam(rows):
    return {int(r[0]): (r[1], r[2]) for r in rows if len(r) == 3 and r[0].isdigit()}


def sual(badia, name="makhzan.tsv", sijill=True):
    files = ([SIJILL] if sijill else []) + [os.path.join(ROOT, "mawsua", name)]
    p = subprocess.run([EXE, "--sual", badia] + files, capture_output=True, text=True)
    return p.returncode, p.stdout.splitlines()


ok = 0
raw = open(os.path.join(ROOT, "mawsua", "makhzan.tsv"), "rb").read()
assert hashlib.sha256(raw).hexdigest() == open(os.path.join(ROOT, "mawsua", "makhzan.sha256")).read().strip(), \
    "المخزن تغيّرت بصمته"
ok += 1

code, rows = faahis("makhzan.tsv")
hukm = [r for r in rows if len(r) == 3 and r[0].isdigit()]
assert code == 0, "الفاحص رفض شيئًا من المخزن"
assert len(hukm) == 240 and all(r[1] == "مقبول" and r[2] == "1" for r in hukm), hukm[:3]
ok += 1

code, rows = faahis("makhzan.tsv", sijill=False)
hukm = [r for r in rows if len(r) == 3 and r[0].isdigit()]
assert code == 1 and len(hukm) == 240 and all(r[1] == "مرفوض" for r in hukm), hukm[:2]
ok += 1

code, rows = faahis("fasid.tsv")
assert code == 1 and ahkam(rows) == {
    6: ("مقبول", "1"), 7: ("مرفوض", "سلسلة لا يقبلها الفاحص"), 8: ("مرفوض", "سلسلة لا يقبلها الفاحص"),
    9: ("مرفوض", "وسم فوق سنده"), 10: ("مرفوض", "سلسلة لا يقبلها الفاحص"), 11: ("مقبول", "1")}, ahkam(rows)
ok += 1

code, rows = faahis("fasid_qanun.tsv")
assert code == 1 and any(r[0] == "خطأ" and "قانون خارج القاعدة" in r[1] for r in rows), rows
ok += 1

code, rows = faahis("fasid_ilmi.tsv")
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

code, rows = faahis("fasid_idaa.tsv")
assert code == 1 and ahkam(rows) == {5: ("مرفوض", "وسم فوق سنده"), 6: ("مقبول", "4"),
                                     7: ("مرفوض", "سلسلة لا يقبلها الفاحص")}, ahkam(rows)
ok += 1

code, rows = faahis("fasid_naw.tsv")
assert code == 1 and any(r[0] == "خطأ" and "نوع مودَع مجهول" in r[1] for r in rows), rows
ok += 1

code, rows = faahis("fasid_dalala.tsv")
assert code == 1 and ahkam(rows) == {
    15: ("مقبول", "4"), 16: ("مقبول", "4"), 17: ("مرفوض", "سلسلة لا يقبلها الفاحص"),
    18: ("مرفوض", "سلسلة لا يقبلها الفاحص"), 19: ("مرفوض", "وسم فوق سنده")}, ahkam(rows)
akhta = sorted(int(r[1].split()[1].rstrip(":")) for r in rows if r[0] == "خطأ" and "قانون خارج القاعدة" in r[1])
assert akhta == [7, 8, 9], akhta
ok += 1

code, out = sual("mutabaqa:", name="maratib.tsv", sijill=False)
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
code, rows = faahis("fasid_basma.tsv")
assert code == 1 and [r[1] for r in rows if r[0] == "خطأ"] == [f"سطر {i}: بصمة ليست sha256" for i in (1, 2, 3, 4)], rows
assert ahkam(rows) == {9: ("مرفوض", "سلسلة لا يقبلها الفاحص"), 10: ("مقبول", "4")}, ahkam(rows)
ok += 1

print(f"{ok}/14")
