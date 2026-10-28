# توجيهُ البنّاء إلى مؤلّف الحالات (بنصّه)

النصُّ الذي أرسله البنّاء إلى الوكيل المؤلّف، وطابقه بالأداة نصَّ أوّل رسالةٍ في سجلّ الوكيل (`agent-a46ac9ee236d275c9.jsonl`؛ أوّلُ طابعٍ فيه
2026-10-27T23:56:24Z، أي 02:56:24 بتوقيت عمّان 2026-10-28؛ وآخرُه 2026-10-28T00:16:25Z). وليس من الملفّات المجمَّدة في `tajmid.json`.

```text
You are the independent case author for a grammar test. You write the expected answers; someone else builds the code later and must not see your cases until their code is frozen. Your independence is the whole point, so follow the reading limits strictly.

READ ONLY these things:
1. The spec: /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/abniya/mujallad/wasf.md (Arabic; it defines the question — the verdict and degree of the scope on forming one pattern (صيغة) for an agent or patient noun (اسم الفاعل / اسم المفعول) from a verb, given as four analysed fields — the case format, allowed values, the word→value key, the scope line ranges, category quotas, and the freeze rule).
2. The two source files listed in the spec, in /home/claude/mudaa_dir/: alfiyya.txt and qatr.txt. Every expected verdict must be grounded on a line inside the scope ranges the spec gives; anything the scope does not decide gets «لا_حكم». You may read other lines of these same two files for understanding.

DO NOT open, list, grep or read anything under /home/claude/mashru, any other directory in /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad other than /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/abniya/mujallad, any *.lean file, any other file in /home/claude/mudaa_dir, or any file besides the spec, the two sources and the files you create in /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/abniya/mujallad. Do not use web search. Do not rely on grammar you know from elsewhere to set an expected value: the scope's own wording decides, through the key table in the spec. If your outside knowledge disagrees with the scope, follow the scope and note it in `taliq`. In particular, do not introduce distinctions the scope does not make (for example rules about these patterns from other chapters, from the الصفة المشبهة chapter of the Alfiyya (line 609 onward), from the parts of Qatr lines 358 and 365 about عمل or the مبالغة forms, or from other books); where the scope's unvowelled text leaves two readings, that is for the غموض category or for «لا_حكم», as the spec says.

TASK
- Read the spec fully, then read the scope ranges carefully (OpenITI lines start with "~~" or "# " or "### | "; PageVxxPxxx and msNNN are markers inside lines or alone on a line; a sentence may continue on the next line).
- Write the cases to /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/abniya/mujallad/cases.json exactly in the spec's format, meeting the spec's count range and all minimums in «ما يُطلب», with ids "B01", "B02", ….
- Every `sanad` piece must have `masdar`, `satr`, `nass`; `nass` must be a byte-exact substring of the cited line after stripping only a leading "~~", "# " or "### | " prefix, must not span two lines, and the cited line must be inside the scope for that source. Mark `mithal_harfi` true only if the `mithal` (as written, no diacritics) occurs inside one of its sanad lines' full text (after the same prefix stripping).
- Write a checker script /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/abniya/mujallad/fahs_cases.py (run it with `python3 -I`; it takes the path of cases.json and the directory of the two sources as arguments) that verifies: valid JSON; allowed values only (including the list forms of `hukm` and `daraja` for the غموض category, and `daraja` = «بلا_درجة» whenever hukm is not «مقبول»); ids unique; total count and every minimum in «ما يُطلب» met; no duplicate `dakhil`; every `zawj` is mutual, differs from its partner in exactly one dakhil field, and differs in hukm or daraja; every nass is a substring of its line (with the prefix rule) and its line is in scope; cases whose hukm is «لا_حكم» have empty sanad; mithal_harfi=true cases have the mithal inside one of their sanad lines' full text. It must also check the two source files' SHA-256 against the spec. Run it until it passes with exit 0. Also try a few deliberately broken copies of cases.json in /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/abniya/mujallad/tafrat_fahs/ and confirm the checker rejects each with a non-zero exit.
- Then compute `sha256sum cases.json` and DO NOT modify cases.json after that.
- Also write /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/abniya/mujallad/taalif.md: what you read (files and line ranges), what you did not read, anything the environment injected into your context without you opening it (disclose it fully, e.g. project instructions, memory snapshots, the user's email, attribution instructions, skill lists), and any judgment calls on the key table and on the scope of general statements — but WITHOUT listing case contents, examples or expected values (the builder may see this file before freezing code). If you searched for غموض cases and found none, say so there.

YOUR FINAL REPLY must contain ONLY: the sha256 of cases.json, the total case count, the count per category (موجب/حد/خارج/عموم/غموض), how many are verbatim (mithal_harfi=true), the checker's exit status (and how many broken copies it rejected), and the sha256 of fahs_cases.py and taalif.md. Do NOT include any case, example, list of forms, or expected value in your reply — the builder reads your reply and must stay blind to the gold. If you create helper files that contain case contents (data files, build scripts, broken copies), list their file names only (no contents) at the end of your reply, so the builder knows not to read them.
```

## رسالةُ الاستئناف (2026-10-28T00:14:17Z)

أُعيد تشغيلُ الآلة والمؤلّفُ يعمل، فأوقفته؛ واستأنفه البنّاءُ بهذه الرسالة بنصّها، وقد رأى قبلها أسماءَ ملفّات المجلّد وأحجامَها وأوقاتَها وحدها:

```text
The machine restarted while you were working, so your last command may not have finished. Your files in /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/abniya/mujallad/ are still there (bina_cases.py, cases.json, fahs_cases.py, wasf.md; no taalif.md yet). Please check where you were, finish the task exactly as originally instructed (same reading limits, same checker and broken-copy steps, compute sha256 of cases.json only when final and do not modify it after, write taalif.md), and give the same final reply format (hashes, counts, checker exit status, helper file names only).
```

## ما رآه البنّاء من سجلّ المؤلّف قبل دفع الشفرة (UTC)

لم يقرأ البنّاءُ سجلَّ المؤلّف وهو يعمل.
- **23:58Z–23:59:52Z:** كُتبت `Jisr/Abniya.lean` و`Jisr/AbniyaDabit.lean` والمولِّدُ والطفراتُ (أوقاتُ الملفّات)، قبل أن يعود المؤلّف.
- **بعد 00:16:25Z:** جوابُ المؤلّف الأخير (البصماتُ والأعداد وأسماءُ الملفّات المساعدة)، ثمّ بصماتُ ملفّات المجلّد، ومستخرِجُ السجلّ (`sijill_muallif.json`،
  الإصدار ٢ وحدُّه فيه)، ومطابقةُ أوّل رسالةٍ في السجلّ بالتوجيه، وأهدافُ أوامر «cd» في أوامر المؤلّف وحدها.

ولم يقرأ البنّاءُ `cases.json` ولا `taalif.md` ولا `fahs_cases.py` ولا `bina_cases.py` قبل دفع الشفرة؛ ونُسخت إلى هذا المجلّد بلا قراءة.

## حدُّ `sijill_muallif.json`

ما فيه بلا مجلّدٍ («/t»، «/t04_mukarrar.json»، «/bina_tafrat.py»، «/masadir_maghyira» …) نمطُ المسار المطلق مقطوعًا من مسارٍ نسبيٍّ داخل المجلّد
المسموح (`tafrat_fahs/…`)؛ وأسماءُ `t01_…` … `t18_…` محلولةٌ على `mujallad/` وهي في `tafrat_fahs/`؛ و`/home/claude/mudaa_dir` مجلّدُ المصدرين؛ و`majallidat_al_amal`
مجلّدُ الجلسة الرئيس (حقلُ cwd)، لا موضعَ قراءة: أهدافُ «cd» في أوامره مجلّدُ المصدرين ومجلّدُه وحدهما.

## سياقُ المؤلّف

حُقن في سياقه آليًّا ما يُحقن في كلّ وكيل (`CLAUDE.md` من مجلّد الجلسة الرئيس، ولقطةُ الذاكرة، وغيرُهما)، وإفصاحُه عنه في `taalif.md`.
