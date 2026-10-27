# Notes: where spec.md was ambiguous to me, and how I read it

The oracle and the hand-derived cases follow the reading given here. Each item is a place where a
different reasonable implementation could disagree with mine.

1. **Mark-headed segment at text start belongs to a word.** A word is the longest run of segments
   whose head is not U+0020, so a segment headed by a mark (only possible at position 0) is in the
   word. So the next segment is not `awwal`, and its `prev` is the mark-headed segment, whose `marks`
   do not include its head. Example: `ًا` (fathatan, alif): the alif is not `awwal`, so
   rule 6 does not apply. Rule 12 does not fire either, because the fathatan is the prev's head and not
   in its marks. The alif falls to rule 15: `harfMadd [11]`. The other reading drops mark-headed
   segments from words, which would give rule 6 «قاعدة همزة الوصل».

2. **Only U+0020 separates words.** Tab, newline, NBSP U+00A0, the Arabic comma and every other
   foreign character are F segments (rule 3) inside the word. They change `awwal`, `akhir`, `prev` and
   `next` for their neighbours. Example: `بَ\tا` gives alif `harfMadd [11]`, while `بَ ا` gives
   alif P «قاعدة همزة الوصل». A space carrying a mark (rule 1 F) still separates words, because its
   head is a space.

3. **Rule 4 «أكثرُ من علامة حركة واحدة» is read as a count of code points.** So the same vowel twice
   (fatha, fatha) is F «علامتان متعارضتان», even though the marks do not conflict. The other
   reading counts distinct marks.

4. **Sukun is a «علامة حركة» (the spec defines it so).** This has consequences:
   - Rule 6: alif + sukun at word start is F «ألف محرّكة في أوّل الكلمة».
   - Rule 14 (shadda without a vowel mark) does not catch shadda + sukun. That falls to rule 16 with
     cells `[4h+3, 4h+3]`, the same cell twice (`بّْ` gives `[107, 107]`).
   - Mid-word alif + sukun is `harfHaraka [11]`, the same number as `harfMadd` alif.

5. **Rule 16 ignores the order of shadda and vowel.** With shadda the cells are `[4h+3, 4h+s]`,
   whether the shadda comes before or after the vowel mark in the text.

6. **Rule 15, lam bullet.**
   - I read «`prev` هو أوّلُ مقطعٍ في الكلمة» as: prev is the word's first segment, so the lam is
     second.
   - The condition looks only at prev's head (ا or ٱ), not at prev's marks or verdict. So `اَلشَّ`
     (alif with fatha, F by rule 6) still gives the lam P «قاعدة لام التعريف المدغمة».
   - `next` only needs a shadda among its marks. Next may itself be F, for example shadda with two
     vowels (rule 4).
   - When `next` does not exist (`ال`), the lam goes to the next bullet: P «قاعدة الحرف الأخير بلا
     حركة».
   - An alif and lam separated by a space do not trigger the bullet, because the lam is then `awwal`
     and has no prev.

7. **Rule 15, harfMadd bullet.** It applies to bare ا/و/ي that are not `awwal`, whatever the prev is
   and whether or not the letter is `akhir`. For example: after tatweel, after a tab, after a
   mark-headed segment, after a letter with dammatan (`بٌا` gives alif `[11]`), after waw with
   fatha. Only ا و ي count: not ى, not hamza seats.

8. **Rule 12 «وله prev في علاماته فتحتان».**
   - Fathatan must be in prev's marks, not its head (see 1).
   - Prev's own verdict does not matter. Prev is normally P «قاعدة التنوين».
   - Rule 12 does not require `akhir`: `بًاب` gives alif P «قاعدة ألف التنوين».

9. **Rule 13 «إمّا لا شيء وإمّا سكونٌ وحده».** I read this as: prev's marks are empty, or exactly
   one sukun. Shadda + sukun on the waw does not qualify, so the alif becomes `harfMadd`. «رأسُه و»
   means U+0648 only, not ؤ.

10. **The order of rules 1, 2, 3 before 4 matters for names.**
    - A space with two marks is «علامة على فاصل».
    - A text-initial mark followed by more marks is «علامة بلا حامل».
    - A foreign letter with marks is «حرف ليس في جدول المخارج», not «علامتان متعارضتان».
    - Rule 4 does run before rules 5, 8, 9 and 10: tatweel, آ or ة with two vowels is F
      «علامتان متعارضتان».

11. **Characters outside the eight marks.** Some Arabic characters are not among the eight marks:
    U+0670 superscript alef, U+0653 maddah above, U+0654/U+0655 hamza above/below, Quranic annotation
    marks, ZWNJ/ZWJ, Persian letters, presentation forms, decomposed sequences. None of them is a mark,
    so each starts its own segment and gets F «حرف ليس في جدول المخارج». It also leaves the letter
    before it bare: `بٰ` gives the ba F «حرف بلا حركة في غير آخر الكلمة», because the ٰ segment
    keeps the ba from being `akhir`. «لا تطبيع» is taken literally, so there is no NFC/NFD folding.

12. **Rule 5 and Rule 6 with shadda.** Shadda is an «علامة», so tatweel + shadda alone is P
    «قاعدة التطويل بعلامة». Alif or ٱ at word start with shadda only has no vowel mark, so it is P
    «قاعدة همزة الوصل».

13. **The parenthetical note after rule 16 (القواعد 6–14 لا يصل إليها رأسٌ خارج ما تذكره).** Rules 11
    and 14 mention no head. I read the note as a statement about which heads can reach which rules,
    not as an extra filter. The heads ـ ة ى آ ٱ are all used up by rules 5–10, so only table carriers
    and hamza seats reach rules 11–16. ء (table index 0) and the seats (h = 0) give identical cells.

14. **`kalimat` output.**
    - **`b`: «b: آخرُه».** This could be the inclusive last code point (b_last − 1) or the exclusive
      end (the last segment's `b`, which is how segments use `b`). I chose **the exclusive end** (=
      `b` of the last segment). An implementation using the inclusive end would differ by 1 on every
      word.
    - **`khalaya` of an unlicensed word.** «وخلاياها ضمُّ خلايا مقاطعها» is stated beside the
      licensing condition, not under it. I output the concatenation always, so P/F segments add
      nothing and L segments add theirs. The other reading outputs `[]` when the word is not
      licensed.
    - A word made only of a mark-headed F segment is still a word.
    - A word whose segments are all L but which has no cell (`ـ`) is not licensed.

15. **Format.** Each case in `boundary.json` carries an extra key, `"label"`, a short English
    description, besides `"nass"` and `"tawaqqu"`. A consumer expecting exactly two keys should
    ignore it.
