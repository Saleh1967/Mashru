# tabaqat4 — جملة مشكولة ← Mashru (كما هو) ← تقرير الطبقات الأربع

```
TOOL_ROOT   = <mashru>/by-hussein/tabaqat4/        (يكتب هنا فقط ، أو في --out)
MASHRU      = READ_ONLY — يُستورَد في Lean ويُقرأ جدولُ حوامله ، ولا يُعدَّل ملفٌ ولا يُشغَّل lake build عليه
HOKOM       = اختياري (--hokom) عبر hokom_adapter.py ، رتبة «تقدير» ، يُعرَض ولا يُستهلك
CLEAN_CODE  = غير مستعمل (قرار المالك 2026-10-24)
PYTHON      = stdlib فقط ؛ LEAN عبر elan الموجود (`source ~/.elan/env`)
```

## التشغيل

```bash
cd /Users/husseinhiyassat/mashru
source ~/.elan/env
python3 by-hussein/tabaqat4/run.py "ذَهَبَ الْوَلَدُ"
python3 by-hussein/tabaqat4/run.py "ذَهَبَ الْوَلَدُ" --hokom            # مع تقدير Hokom (يلزم hokom_adapter.py)
python3 by-hussein/tabaqat4/run.py "ذَهَبَ الْوَلَدُ" --an 0 --izaha -1  # المرساة وإزاحة الحدث (افتراض الشاهد)
python3 -I by-hussein/tabaqat4/tests/test_tabaqat4.py                 # T1..T8
```

المخرجات في `by-hussein/tabaqat4/_runs/<sha8>/`: `taqrir.html` (الواجهة المفهومة) ، `taqrir.md` ، `taqrir.json` ، `Jumla_pass1.lean` ، `Jumla.lean` ، `lean_*_stdout.txt`.

## المراحل

```
S0  هوية المدخل     NFC ، sha256 ، رفض غير المشكول (NASS_GHAYR_MASHKUL)
S1  التقطيع         مراسٍ W-<sha8>-<idx> ؛ الترقيم يُسقَط مُعلَنًا
S2  الدالّ          خلايا n=4·حامل+حالة بجدول Dal/Makharij.lean المقروء وقت التشغيل ؛ كلّ تحويل باسمه (AL_FLAG ، AL_SHAMSIYYA ، SHADDA ، TANWIN ، HAMZA_FORM ، MADD…)
S3  تقدير Hokom     اختياري ؛ لا يُستهلك
S4  المدلول         من qamus.json المقيَّد بتعريفات Mashru (Jisr/Utur.lean) ؛ الغائب → NO_SEALED_MADLUL
S5  معًا            نوعان مغلَّفان: [فعل ماضٍ + فاعل بأل]→Mulhaqat.darabaZayd ، [فعل ماضٍ + فاعل منوَّن]→Mulhaqat.jaaRajul ؛ غيرهما OUT_OF_EXECUTED_PATH
S6  العقل           Mirsat ⟨an, ⟨0,0,0⟩⟩ ، Dhat ⟨حقيقة الفاعل⟩ ، Arad .fiil ⟨حقيقة الفعل⟩ izaha .saa none — افتراضات معلَنة
S7  البرهان         pass1: #eval القيم ← pass2: نظريات by decide على القيم المرصودة + #print axioms ⊆ {propext, Classical.choice, Quot.sound}
S8  الوسم           سلّم Mashru: مبرهن › مبرهن على الشاهد › مطابَق › مفحوص › مقيس › تقدير › رأي
```

## ما لا يُدَّعى

- لا صحّة لغوية خارجية ؛ المدلول لا يُولَّد ؛ نوعان من الجمل فقط ؛ المرساة والإزاحة والإسناد الدلالي موروثة من `Shahid_Ahmad.lean` (ت3/ت4/ت5) معلَنةً.
- «مبرهن على الشاهد» = نظرية مرّت على هذه الجملة بعينها ؛ ليست «مبرهن» عامًّا.
- التوسّع الحقيقي يأتي من إيداع مدلولات مختومة جديدة في Mashru (قرار مالك وقانون) ، لا من هذه الأداة.
