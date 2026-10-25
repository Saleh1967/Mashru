# توجيهُ البنّاء إلى مؤلّف الحالات (بنصّه)

النصُّ الذي أرسله البنّاء إلى الوكيل المؤلّف، منقولًا من سجلّ الوكيل بالأداة كما أُرسل (طابعُه 2026-10-25T04:23:54.544Z)، قبل أن يكتب المؤلّف شيئًا. وليس من الملفّات المجمَّدة في `tajmid.json`.

````text
You are the independent case author for a grammar test. You write the expected answers; someone else builds the code later and must not see your cases until their code is frozen. Your independence is the whole point, so follow the reading limits strictly.

READ ONLY these two things:
1. The spec: /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/fa/mujallad/wasf.md (Arabic; it defines the case format, allowed values, the word→value key, category quotas, and the freeze rule).
2. The source: /home/claude/mudaa_dir/sibawayhi.txt (Sibawayh's al-Kitab, OpenITI text). Scope is the chapter «هذا باب الفاء», lines 8914–9049. You may read other lines of the same file for understanding, but every expected verdict must be grounded on a line inside 8914–9049; anything the scope does not decide gets «لا_حكم».

DO NOT open, list, grep or read anything under /home/claude/mashru, any directory in /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad other than /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/fa/mujallad, any *.lean file, or any file besides the spec, the source and the files you create in /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/fa/mujallad. Do not use web search. Do not rely on grammar you know from elsewhere (other grammarians, modern grammars) to set an expected value: the scope's own wording decides, through the key table in the spec. If your outside knowledge disagrees with the scope, follow the scope and note it in `taliq`.

TASK
- Read the spec fully, then read lines 8914–9049 carefully (they are wrapped OpenITI lines starting with "~~" or "# "; PageVxxPxxx and msNNN are page markers inside lines).
- Write the cases to /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/fa/mujallad/cases.json exactly in the spec's format, meeting the spec's count range and per-category minimums ("ما يُطلب"), with ids starting with "F".
- Every `sanad.nass` must be a byte-exact substring of the cited line after stripping only the leading "~~" or "# " prefix, must not span two lines, and the cited line must be inside 8914–9049. Prefer verbatim examples; mark constructed ones with "mithal_harfi": false.
- Write a checker script /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/fa/mujallad/fahs_cases.py (run it with `python3 -I`) that verifies: valid JSON; allowed values only (including the list form for the غموض category where the spec allows it); ids unique; counts and quotas met; no duplicate `dakhil` within the same question type except as the spec allows; every nass is a substring of its line (with the prefix rule) and its line is in range; لا_حكم answers have empty sanad; mithal_harfi=true cases have the mithal (as written, no diacritics) inside one of their sanad lines' full text. Run it until it passes with exit 0. Also try a few deliberately broken copies of cases.json (outside /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/fa/mujallad is not allowed, so put them in /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/fa/mujallad/tafrat_fahs/) and confirm the checker rejects each with a non-zero exit.
- Then compute `sha256sum cases.json` and DO NOT modify cases.json after that.
- Also write /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/fa/mujallad/taalif.md: what you read (files and line ranges), what you did not read, anything the environment injected into your context without you opening it (disclose it), and any judgment calls on the key table and on the scope of general statements — but WITHOUT listing case contents, examples or expected values (the builder may see this file before freezing code).

YOUR FINAL REPLY must contain ONLY: the sha256 of cases.json, the total case count, the count per category (موجب/حد/خارج/عموم/غموض), how many are verbatim (mithal_harfi=true), the checker's exit status (and how many broken copies it rejected), and the sha256 of fahs_cases.py and taalif.md. Do NOT include any case, example sentence, list of particles or forms, or expected value in your reply — the builder reads your reply and must stay blind to the gold.

````
