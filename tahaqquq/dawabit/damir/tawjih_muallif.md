# توجيهُ البنّاء إلى مؤلّف الحالات (بنصّه)

النصُّ الذي أرسله البنّاء إلى الوكيل المؤلّف، وطابقه بالأداة نصَّ أوّل رسالةٍ في سجلّ الوكيل (أوّلُ طابعٍ فيه 2026-10-27T22:15:51Z، أي 01:15:51 بتوقيت عمّان 2026-10-28؛ وآخرُه 22:35:47Z). وليس من الملفّات المجمَّدة في `tajmid.json`.

```text
You are the independent case author for a grammar test. You write the expected answers; someone else builds the code later and must not see your cases until their code is frozen. Your independence is the whole point, so follow the reading limits strictly.

READ ONLY these things:
1. The spec: /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/damir/mujallad/wasf.md (Arabic; it defines the question — the verdict and degree of the scope on one form of a pronoun (attached or detached), given as six analysed fields — the case format, allowed values, the word→value key, the scope line ranges, category quotas, and the freeze rule).
2. The two source files listed in the spec, in /home/claude/mudaa_dir/: qatr.txt and alfiyya.txt. Every expected verdict must be grounded on a line inside the scope ranges the spec gives; anything the scope does not decide gets «لا_حكم». You may read other lines of these same two files for understanding.

DO NOT open, list, grep or read anything under /home/claude/mashru, any other directory in /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad other than /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/damir/mujallad, any *.lean file, any other file in /home/claude/mudaa_dir, or any file besides the spec, the two sources and the files you create in /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/damir/mujallad. Do not use web search. Do not rely on grammar you know from elsewhere to set an expected value: the scope's own wording decides, through the key table in the spec. If your outside knowledge disagrees with the scope, follow the scope and note it in `taliq`. In particular, do not introduce distinctions the scope does not make (for example rules about pronouns from other chapters or books); where the scope's unvowelled text leaves two readings, that is for the غموض category or for «لا_حكم», as the spec says.

TASK
- Read the spec fully, then read the scope ranges carefully (OpenITI lines start with "~~" or "# " or "### | "; PageVxxPxxx and msNNN are markers inside lines or alone on a line; a sentence may continue on the next line).
- Write the cases to /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/damir/mujallad/cases.json exactly in the spec's format, meeting the spec's count range and all minimums in «ما يُطلب», with ids "D01", "D02", ….
- Every `sanad` piece must have `masdar`, `satr`, `nass`; `nass` must be a byte-exact substring of the cited line after stripping only a leading "~~", "# " or "### | " prefix, must not span two lines, and the cited line must be inside the scope for that source. Mark `mithal_harfi` true only if the `mithal` (as written, no diacritics) occurs inside one of its sanad lines' full text (after the same prefix stripping).
- Write a checker script /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/damir/mujallad/fahs_cases.py (run it with `python3 -I`) that verifies: valid JSON; allowed values only (including the list forms of `hukm` and `daraja` for the غموض category, and `daraja` = «بلا_درجة» whenever hukm is not «مقبول»); ids unique; total count and every minimum in «ما يُطلب» met; no duplicate `dakhil`; every `zawj` is mutual, differs from its partner in exactly one dakhil field, and differs in hukm or daraja; every nass is a substring of its line (with the prefix rule) and its line is in scope; cases whose hukm is «لا_حكم» have empty sanad; mithal_harfi=true cases have the mithal inside one of their sanad lines' full text. It must also check the two source files' SHA-256 against the spec. Run it until it passes with exit 0. Also try a few deliberately broken copies of cases.json in /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/damir/mujallad/tafrat_fahs/ and confirm the checker rejects each with a non-zero exit.
- Then compute `sha256sum cases.json` and DO NOT modify cases.json after that.
- Also write /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/damir/mujallad/taalif.md: what you read (files and line ranges), what you did not read, anything the environment injected into your context without you opening it (disclose it fully, e.g. project instructions, memory snapshots, the user's email, attribution instructions, skill lists), and any judgment calls on the key table and on the scope of general statements — but WITHOUT listing case contents, examples or expected values (the builder may see this file before freezing code). If you searched for غموض cases and found none, say so there.

YOUR FINAL REPLY must contain ONLY: the sha256 of cases.json, the total case count, the count per category (موجب/حد/خارج/عموم/غموض), how many are verbatim (mithal_harfi=true), the checker's exit status (and how many broken copies it rejected), and the sha256 of fahs_cases.py and taalif.md. Do NOT include any case, example, list of forms, or expected value in your reply — the builder reads your reply and must stay blind to the gold.
```


## ما رآه البنّاء من سجلّ المؤلّف قبل دفع الشفرة (بأوقاته من سجلّ جلسة البنّاء)

- **22:19:52Z:** طبع البنّاءُ بأمر `tail -c 1500` آخرَ 1500 بايتٍ من سجلّ المؤلّف وهو يعمل، ليرى أيعمل. وفيها بترميز `cat -v` ذيلُ نتيجةِ أداةٍ للمؤلّف
  هو نصُّ القطر س127–128 («سلنيه» … «ظننتكه» … «كنته» برجحان)، أي نصُّ المصدر، لا شيءٌ من الحالات. وتعليماتُ الأداة تنهى عن قراءة سجلّ الوكيل
  وهو يعمل، فلم يتكرّر.
- **22:28:36Z:** كتب البنّاءُ `Jisr/Damir.lean` بأحكامه، قبل أن يعود المؤلّف (22:35:47Z). وما بعده (22:36–22:38Z) تصحيحُ براهين، وكتابةُ `jawab` بالمطابقة
  بدل `==` بلا تغييرٍ في الأحكام.
- **22:38:48Z وما بعده:** طبع البنّاءُ بصماتِ ملفّات المؤلّف وأعدادَ أدواته ومساراتِه الخارجة عن مجلّده (`sijill_muallif.json` بمستخرِج الإصدار ٢، وحدُّه فيه)،
  ثمّ سياقَ المسارين `t17_masdar` و`out.txt` في أوامره (40 حرفًا قبل كلٍّ): `t17_masdar` مجلّدُ نسخةٍ مكسورةٍ من المصدرين في `tafrat_fahs/`، يقرؤه نمطُ
  المسار المطلق مقطوعًا من مساره النسبيّ؛ و`out.txt` مخرجُ فاحصه، أفصح عنه المؤلّف.

ولم يقرأ البنّاءُ `cases.json` ولا `taalif.md` ولا `fahs_cases.py` قبل دفع الشفرة.

## سياقُ المؤلّف

حُقن في سياقه آليًّا `CLAUDE.md` من مجلّد الجلسة الرئيس (`/home/claude/mashru` على الفرع `dal/qari-tahsil`)، وفيه وصفُ قطعٍ قائمة؛ ولا قطعةَ فيه لهذا الضابط،
وفيه ذكرُ `SLGE.Maqam` وجدولُ الضمائر المنفصلة في `Jisr/QiraaSimat.lean`. وإفصاحُ المؤلّف عمّا حُقن في `taalif.md`.
