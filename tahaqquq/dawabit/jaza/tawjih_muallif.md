# توجيهُ البنّاء إلى مؤلّف الحالات (بنصّه)

النصُّ الذي أرسله البنّاء إلى الوكيل المؤلّف، منقولًا من سجلّ الجلسة بالأداة كما أُرسل، قبل أن يكتب المؤلّف شيئًا (طابعُ الأداة في السجلّ 2026-10-24T19:01:27Z، أي 22:01:27
بتوقيت عمّان). وفيه توجيهٌ إلى أنواعٍ من الحالات («separates prose from poetry»، «jussive vs indicative answer»). وحُفظ بعد التجميد بمراجعة
`murajii`، فهو ليس من الملفّات المجمَّدة في `tajmid.json`.

````text
You are the independent case author for a grammar test. You write the expected answers; someone else builds the code later and must not see your cases until their code is frozen. Your independence is the whole point, so follow the reading limits strictly.

READ ONLY these two things:
1. The spec: /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/jaza/mujallad/wasf.md (Arabic; it defines the case format, allowed values, the word→grade key, category quotas, and the freeze rule).
2. The source: /home/claude/mudaa_dir/sibawayhi.txt (Sibawayh's al-Kitab, OpenITI text). Scope is the chapter «هذا باب الجزاء», lines 9190–9304. You may read other lines of the same file for understanding, but every expected verdict must be grounded on a line inside 9190–9304; anything that chapter does not decide gets «لا_حكم».

DO NOT open, list, grep or read anything under /home/claude/mashru, any directory named wt-* in the scratchpad, any *.lean file, or any other file in the scratchpad besides the spec and the files you create. Do not use web search. Do not rely on grammar you know from elsewhere (Ibn Hisham, Ibn Malik, modern grammars) to set an expected value: the chapter's own wording decides, through the key table in the spec. If your outside knowledge disagrees with the chapter, follow the chapter and note it in `taliq`.

TASK
- Read the spec fully, then read lines 9190–9304 carefully (they are wrapped OpenITI lines starting with "~~" or "# "; PageV03Pxxx and msNNN are page markers inside lines).
- Write 30–40 cases to /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/jaza/mujallad/cases.json exactly in the spec's format, meeting the per-category minimums (≥8 موجب, ≥8 حد, ≥6 خارج, ≥6 عموم), no two cases with identical `dakhil`.
- Every `sanad.nass` must be a byte-exact substring of the cited line after stripping only the leading "~~" or "# " prefix, and must not span two lines. Prefer verbatim examples; mark constructed ones with "mithal_harfi": false. Cases where the chapter separates prose from poetry, or two surface forms of the same verb (e.g. jussive vs indicative answer), or says nothing, are especially wanted.
- Write a checker script /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/jaza/mujallad/fahs_cases.py (run it with `python3 -I`) that verifies: valid JSON; allowed values only; ids unique; quotas met; dakhil unique; every nass is a substring of its line (with the prefix rule); لا_حكم cases have empty sanad; mithal_harfi=true cases have the mithal (as written, no diacritics) inside one of their sanad lines' full text. Run it until it passes with exit 0.
- Then compute `sha256sum cases.json` and DO NOT modify cases.json after that.
- Also write /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/jaza/mujallad/taalif.md: what you read (files and line ranges), what you did not read, and any judgment calls on the key table — but WITHOUT listing case contents, examples or expected values (the builder may see this file before freezing code).

YOUR FINAL REPLY must contain ONLY: the sha256 of cases.json, the total case count, the count per category (موجب/حد/خارج/عموم), how many are verbatim (mithal_harfi=true), the checker's exit status, and the sha256 of fahs_cases.py and taalif.md. Do NOT include any case, example sentence, adat list, or expected value in your reply — the builder reads your reply and must stay blind to the gold.
````
