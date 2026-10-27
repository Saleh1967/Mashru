# توجيهُ مؤلّف العرّاف المستقلّ

**من البنّاء، بنصّه** (أُطلق وكيلًا عامًّا في الخلفيّة 2026-10-27، 12:44:22Z؛ وانتهى نحو 12:51Z بأوقات ملفّاته). و`spec.md` المذكورُ فيه هو
`wasf.md` هنا بايتًا (بصمتُهما واحدة، في `basamat.json`).

```
You are an independent test-oracle author. Read ONLY this specification file (Arabic):
/tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/tahsil/spec.md

Do NOT read any other file under /home/claude/mashru, /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad (except the spec and your own output directory), or any Lean/Python implementation of it. The point is an implementation written from the spec alone, so that disagreements reveal bugs on either side.

Write, in /tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad/tahsil/oracle/:
1. `oracle.py` — pure Python 3 stdlib, no imports beyond the standard library. Functions `tahsil(text: str) -> list[dict]` and `kalimat(text: str) -> list[dict]` exactly as the spec's output section describes. Use explicit code points (e.g. "َ") for every special character, not pasted glyphs, so the file is unambiguous. Keep it simple and literal to the spec: follow the numbered classification rules in order. The reason/rule names ("ism") must be copied character-for-character from the spec's «…» quotes (without the «» brackets).
2. `boundary.json` — at least 40 hand-derived cases: list of {"nass": str (use \u escapes), "tawaqqu": [expected tahsil output]} where you derive each expectation by reading the spec by hand (do not generate them by running your oracle). Cover every numbered rule (1–16) at least once, including edge cases: empty string, text starting with a mark, shadda before/after the vowel mark, two vowel marks, two shaddas, tanwin followed by alif, alif after waw-with-sukun at word end, lam after word-initial alif followed by a shadda letter, bare final letter, bare middle letter, hamza seats with marks, ة/ى/آ/ٱ, tatweel with and without marks, unknown characters (Latin letter, Arabic comma, tab), multiple spaces, a space carrying a mark, and ا/و/ي bare at word start vs inside a word.
3. `check_boundary.py` — runs oracle.tahsil on every boundary case and prints any mismatch with the hand-derived expectation; exit code 0 iff none.

Run check_boundary.py yourself. If a mismatch appears, decide from the spec text which side is wrong (your hand derivation or your code) and fix that side; record in a short `NOTES.md` every place where the spec was ambiguous to you and how you read it (this is important — ambiguities are findings, not things to smooth over).

Report back: the file list, the boundary-case count, the final check result, and the ambiguity notes verbatim.
```

**ما قرأه المؤلّف** (من سجلّ أدواته): `spec.md` وحده، ثمّ ملفّاتُه هو. وفي سياقه حُقن آليًّا (من صفوف سجلّه): لقطةُ الذاكرة، ووصفُ البيئة،
وقائمةُ المهارات، والتعليماتُ وفيها `CLAUDE.md` (بلا ذكرٍ لهذه القطعة، فهي لم تُكتب فيه بعدُ)، وسياقُ الجلسة وفيه بريدُ المستخدم، والتاريخ،
وتعليماتُ النسبة والجلسة. فقولُ وثائق هذا الطلب إنّه لم يقرأ إلّا المواصفة معناه أنّه لم يقرأ ملفًّا غيرها.

**ما رآه البنّاء وفي أيّ ترتيب** (بأوقات سجلّ الجلسة، UTC، 2026-10-27):
- 12:44:22 أُطلق المؤلّف، بعد أن كتب البنّاءُ المواصفة. و12:46:48 كتب البنّاءُ `Nizam/Shahada.lean`.
- 12:51:37 وصل تقريرُ المؤلّف، وفيه نصُّ ملاحظات الغموض في `NOTES.md` بأمثلتها المحلولة.
- 12:58:12 كتب البنّاءُ `Dal/Tahsil.lean` أوّلَ مرّة. وآخرُ تغييرٍ في قواعد التصنيف (`tasnifRas`) كان 13:03:14، وفُحص الملفّ بـ`lake env lean`
  بلا خطأ 13:03:50.
- 13:04:04 قرأ البنّاءُ الأسطرَ 1–80 من `oracle.py`: الثوابتَ، وجدولَ الحوامل، وأوّلَ أسماء الأحكام.
- 13:05:13 كتب أداةَ `tahsil`، و13:05:20 بناها وشغّلها على نصّين يدويّين.
- 13:05:52 قرأ `check_boundary.py`، وأوائلَ `boundary.json` و`boundary_kalimat.json`، والأسطرَ 80–287 من `oracle.py`.

ولم تتغيّر قواعدُ التصنيف بعد 13:04:04 إلّا في كتابة العلامات بصيغة `\u` بدل المحارف نفسِها، والمعنى واحد. وتغيّرت براهينُ بعده، وتغيّر الفاحص
العامّ في `Nizam/Shahada.lean` بعد المراجعة.

فالعرّافُ مستقلٌّ في كتابته، لا ضابطٌ مجمَّد: لم تُجمَّد حالاتُه في إيداعٍ قبل الشفرة. وقرأ البنّاءُ ملاحظاتِ الغموض قبل كتابة التصنيف، فاتّفاقُ
الأداة والعرّاف في مواضع الغموض ليس شاهدًا مستقلًّا. وهذه المواضع (`NOTES.md` 1–14؛ والخامسَ عشرَ عن صيغة ملفّ الحالات): العلامةُ أوّلَ النصّ من كلمته، والفراغُ وحده فاصل،
والعلامتان من جنسٍ واحد متعارضتان، والسكونُ علامةُ حركة (فالشدّةُ مع السكون خليّتان ساكنتان)، وترتيبُ الشدّة والحركة لا أثرَ له، وشروطُ لام
التعريف وحرفِ المدّ وألفي التنوين والجماعة كما قرأها، وتقديمُ القواعد ١–٣ على ٤، والتطويلُ والألفُ أوّلَ الكلمة مع الشدّة وحدها، وما ليس من العلامات الثماني حرفٌ ليس في الجدول،
وقراءتُه لملاحظة ما بعد القاعدة ١٦، وحدُّ الكلمة غيرُ شامل، وخلايا الكلمة غيرِ المرخَّصة مضمومة.
