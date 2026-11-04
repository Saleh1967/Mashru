# توجيهُ البنّاء إلى مؤلّف الحالات (بنصّه)

النصُّ الذي أرسله البنّاء إلى الوكيل المؤلّف كما أُرسل (2026-11-04)، قبل أن يكتب المؤلّف شيئًا. وليس من الملفّات المجمَّدة في `tajmid.json`.

````text
You are the independent case author for a frozen control ("ضابط مجمَّد"). You write the expected answers; someone else builds the code later and must not see your cases until their code is frozen. Your independence is the whole point, so follow the reading limits strictly.

READ ONLY these two files, both in /tmp/claude-0/-home-user-Algebra/a8fa682b-f677-50d5-9cd9-f0e10bde786e/scratchpad/haml_jins/mujallad/ :
1. wasf.md — the spec (Arabic): case format, allowed values, the word→value key, category quotas, the freeze rule.
2. masdar.md — the source: 18 numbered lines of the owner's sayings and decisions and the builder's declared stipulations. Every expected verdict must be grounded on a numbered line of masdar.md; anything the scope does not decide gets «لا_حكم».

DO NOT open, list, grep or read anything under /home/user, anything under /tmp/claude-0/-home-user-Algebra/a8fa682b-f677-50d5-9cd9-f0e10bde786e/scratchpad other than .../haml_jins/mujallad, any *.lean or *.py file besides the one you create, or any other file. Do not use web search. Do not rely on grammar or ontology you know from elsewhere to set an expected value: the source's own wording decides, through the key table in the spec. If your outside knowledge disagrees with the source, follow the source and note it in `taliq`.

TASK
- Read wasf.md fully, then masdar.md carefully.
- Write the cases to /tmp/claude-0/-home-user-Algebra/a8fa682b-f677-50d5-9cd9-f0e10bde786e/scratchpad/haml_jins/mujallad/cases.json exactly in the spec's format, meeting the spec's count range and per-category minimums ("ما يُطلب"), with ids starting with "H".
- Every `sanad.nass` must be a byte-exact substring of the cited numbered line of masdar.md after stripping only the leading number, the dot and the following space; the cited line number must be in 1–18. Cases with hukm «لا_حكم» have an empty sanad and explain in taliq.
- Write a checker script /tmp/claude-0/-home-user-Algebra/a8fa682b-f677-50d5-9cd9-f0e10bde786e/scratchpad/haml_jins/mujallad/fahs_cases.py (run it with `python3 -I`, usage: `python3 -I fahs_cases.py [cases.json] [masdar.md]`, defaulting to the files beside it) that verifies: valid JSON; allowed values only (including the two-alternative list form for غموض); ids unique; counts and quotas met (including the sub-quotas inside حد and خارج); no duplicate `dakhil` except one غموض case; every nass is a substring of its line (with the prefix rule) and its line is in range; لا_حكم answers have empty sanad. Run it until it passes with exit 0. Also try a few deliberately broken copies of cases.json in /tmp/claude-0/-home-user-Algebra/a8fa682b-f677-50d5-9cd9-f0e10bde786e/scratchpad/haml_jins/mujallad/tafrat_fahs/ and confirm the checker rejects each with a non-zero exit.
- Then compute `sha256sum cases.json` and DO NOT modify cases.json after that.
- Also write /tmp/claude-0/-home-user-Algebra/a8fa682b-f677-50d5-9cd9-f0e10bde786e/scratchpad/haml_jins/mujallad/taalif.md (Arabic): what you read (files and line ranges), what you did not read, every file path you accessed with any tool, anything the environment injected into your context without you opening it (disclose it), and any judgment calls on the key table and on the scope of general statements — but WITHOUT listing case contents, examples or expected values (the builder may see this file before freezing code).

YOUR FINAL REPLY must contain ONLY: the sha256 of cases.json, the total case count, the count per category (موجب/حد/خارج/عموم/غموض), the checker's exit status (and how many broken copies it rejected), and the sha256 of fahs_cases.py and taalif.md. Do NOT include any case, example sentence, or expected value in your reply — the builder reads your reply and must stay blind to the gold.
````
