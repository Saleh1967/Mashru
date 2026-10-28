# توجيهُ البنّاء إلى مؤلّف الحالات (بنصّه)

النصُّ الذي أرسله البنّاء إلى الوكيل المؤلّف، وطابقه بالأداة نصَّ أوّل رسالةٍ في سجلّ الوكيل (`agent-a1b0fa6c5080b0fe9.jsonl`؛ أوّلُ طابعٍ فيه
2026-10-28T00:42:51Z، وآخرُه 2026-10-28T01:03:03Z). وليس من الملفّات المجمَّدة في `tajmid.json`.

```text
You are the independent case author for a grammar test. You write the expected answers; someone else builds the code later and must not see your cases until their code is frozen. Your independence is the whole point, so follow the reading limits strictly.

READ ONLY these things:
1. The spec: /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/khabar/mujallad/wasf.md (Arabic; it defines the question — the verdict and degree of the scope on a nominal construction given as analysed fields, either a subject with its predicate (المبتدأ والخبر: what the subject denotes, the predicate type, the link of a sentence predicate, what a single-word predicate raises, whose meaning a derived predicate carries, whether a time predicate is informative) or a descriptive adjective with the noun it raises (الوصف ومرفوعه: what it leans on, the numbers, and the asked analysis) — the case format, allowed values, the word→value key, the rule for the two sources, the scope line ranges, category quotas, and the freeze rule).
2. The two source files listed in the spec, in /home/claude/mudaa_dir/: qatr.txt and alfiyya.txt. Every expected verdict must be grounded on a line inside the scope ranges the spec gives; anything the scope does not decide gets «لا_حكم». You may read other lines of these same two files for understanding.

DO NOT open, list, grep or read anything under /home/claude/mashru, any other directory in /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad other than /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/khabar/mujallad, any *.lean file, any other file in /home/claude/mudaa_dir, or any file besides the spec, the two sources and the files you create in /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/khabar/mujallad. Do not use web search. Do not rely on grammar you know from elsewhere to set an expected value: the scope's own wording decides, through the key table in the spec. If your outside knowledge disagrees with the scope, follow the scope and note it in `taliq`. In particular, do not introduce distinctions the scope does not make (for example rules from the parts of the chapter outside the scope — starting a sentence with an indefinite, the order of subject and predicate, deletion, multiple predicates — from other chapters, or from other books); where the scope's unvowelled text leaves two readings, that is for the غموض category or for «لا_حكم», as the spec says.

TASK
- Read the spec fully, then read the scope ranges carefully (OpenITI lines start with "~~" or "# " or "### | "; PageVxxPxxx and msNNN are markers inside lines or alone on a line; a sentence may continue on the next line).
- Write the cases to /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/khabar/mujallad/cases.json exactly in the spec's format, meeting the spec's count range and all minimums in «ما يُطلب», with ids "K01", "K02", ….
- Every `sanad` piece must have `masdar`, `satr`, `nass`; `nass` must be a byte-exact substring of the cited line after stripping only a leading "~~", "# " or "### | " prefix, must not span two lines, and the cited line must be inside the scope for that source (for Qatr line 162, before «وقد يتعدد»). Mark `mithal_harfi` true only if the `mithal` (as written, no diacritics) occurs inside one of its sanad lines' full text (after the same prefix stripping).
- Write a checker script /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/khabar/mujallad/fahs_cases.py (run it with `python3 -I`; it takes the path of cases.json and the directory of the two sources as arguments) that verifies: valid JSON; allowed values only, «لا_ينطبق» exactly in the fields that do not apply (per the spec's applicability rules), the list forms of `hukm` and `daraja` for the غموض category, and the `daraja` rule; ids unique; total count and every minimum in «ما يُطلب» met; no duplicate `dakhil`; every `zawj` is mutual, differs from its partner in exactly one dakhil field, and differs in hukm or daraja; every nass is a substring of its line (with the prefix rule) and its line is in scope; cases whose hukm is «لا_حكم» have empty sanad; mithal_harfi=true cases have the mithal inside one of their sanad lines' full text. It must also check the two source files' SHA-256 against the spec. Run it until it passes with exit 0. Also try a few deliberately broken copies of cases.json in /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/khabar/mujallad/tafrat_fahs/ and confirm the checker rejects each with a non-zero exit.
- Then compute `sha256sum cases.json` and DO NOT modify cases.json after that.
- Also write /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/khabar/mujallad/taalif.md: what you read (files and line ranges), what you did not read, anything the environment injected into your context without you opening it (disclose it fully, e.g. project instructions, memory snapshots, the user's email, attribution instructions, skill lists), and any judgment calls on the key table, on the two-source rule and on the scope of general statements — but WITHOUT listing case contents, examples or expected values (the builder may see this file before freezing code). If you searched for غموض cases and found none, say so there.

YOUR FINAL REPLY must contain ONLY: the sha256 of cases.json, the total case count, the count per category (موجب/حد/خارج/عموم/غموض), how many are verbatim (mithal_harfi=true), the checker's exit status (and how many broken copies it rejected), and the sha256 of fahs_cases.py and taalif.md. Do NOT include any case, example, list of forms, or expected value in your reply — the builder reads your reply and must stay blind to the gold. If you create helper files that contain case contents (data files, build scripts, broken copies), list their file names only (no contents) at the end of your reply, so the builder knows not to read them.
```

## ما رآه البنّاء من سجلّ المؤلّف قبل دفع الشفرة (UTC)

لم يقرأ البنّاءُ سجلَّ المؤلّف وهو يعمل.
- **00:44Z–00:59:50Z:** كُتبت `Jisr/Khabar.lean` و`Jisr/KhabarDabit.lean` والمولِّدُ والطفراتُ P1080–P1101 (أوقاتُ الملفّات؛ آخرُها `Jisr/Khabar.lean`
  00:59:50Z)، قبل أن ينتهي المؤلّف (01:03:03Z).
- **بعد 01:03:03Z:** جوابُ المؤلّف الأخير (البصماتُ والأعداد، وأنّ حدًّا أدنى في المواصفة لا يُستوفى، وأسماءُ الملفّات المساعدة)، ثمّ أسماءُ ملفّات المجلّد
  وأحجامُها وأوقاتُها وبصماتُها، وأسماءُ النسخ المكسورة في `tafrat_fahs/` (أسماؤها وحدها، وفيها وصفُ العيب لا مدخلُ حالة)، ومستخرِجُ السجلّ
  (`sijill_muallif.json`، الإصدار ٢ وحدُّه فيه)، ومطابقةُ أوّل رسالةٍ في السجلّ بالتوجيه، وسياقُ الأنماط الثلاثة الخارجة عن المسموح في أوامر المؤلّف
  (ثلاثون حرفًا قبل كلٍّ وبعده، والحروفُ العربيّة «؟» والأرقامُ «#» ومعرّفاتُ الحالات «K??»)، ومنه تفسيرُها في `tafsir_kharij`.

ولم يقرأ البنّاءُ `cases.json` ولا `taalif.md` ولا `fahs_cases.py` ولا `bina_cases.py` ولا `sana_tafrat.py` قبل دفع الشفرة؛ ونُسخت إلى هذا المجلّد
بلا قراءة. ولم يُودَع `tafrat_fahs/` (فيه `masadir_fasida/`، مجلّدُ مصدرين بايتاتُه مغيَّرة، والمودَعاتُ لا تُرفع إلى المستودع).

## سياقُ المؤلّف

حُقن في سياقه آليًّا ما يُحقن في كلّ وكيل (`CLAUDE.md` من مجلّد الجلسة الرئيس، ولقطةُ الذاكرة، وغيرُهما)، وإفصاحُه عنه في `taalif.md`.
