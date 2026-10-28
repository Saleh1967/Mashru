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

## التعديل الأوّل

Readings of the amended spec (rules 14أ, 14ب, the widened lam bullet of rule 15, sinf `hamzaWasl`).
Numbering restarts at A1. Each item is a place where another reasonable implementation could disagree.

A1. **14ب, lam branch: «وبعده في الكلمة مقطعٌ في علاماته شدّة».** I read «بعده» as referring to the
    lam (= `next` of the alif), and «مقطعٌ» as the segment *immediately* after the lam (the same shape as
    rule 15's lam bullet, which looks at the lam's `next`). The other reading is "some later segment in
    the word". Example `وَالكَتَّ` (bare lam, then كَ, then تَّ): my reading gives the alif `harfMadd [11]`
    and the lam F «حرف بلا حركة في غير آخر الكلمة»; the other reading gives the alif `hamzaWasl` (the lam
    is still F, because rule 15 needs the lam's own `next` to carry the shadda).

A2. **14ب, «`prev` في علاماته فتحةٌ أو ضمّةٌ أو كسرة».** Read as containment: prev's marks contain at least
    one of U+064E/U+064F/U+0650. Prev may also carry a shadda. Prev's own verdict is ignored, as in old
    note 8: a prev that is F by rule 4 (fatha+damma) or P by 14أ (word-initial shadda+kasra) still
    qualifies. Sukun, the tanwins, or no marks do not qualify (a mark-headed prev has no marks).

A3. **14ب, «علاماتُ `next` سكونٌ وحده».** Read as: next's marks are exactly one U+0652 and nothing else.
    Sukun+shadda (either order) does not qualify, so the alif stays `harfMadd`, and the next letter is
    rule 16 `[4h+3, 4h+3]` (old note 4).

A4. **14ب, next head «حاملٌ من الجدول أو مقعدُ همزة».** Taken literally: every table carrier, including
    ا, ء, و, ي. So `بَااْ` gives the first alif `hamzaWasl` (and the second, with sukun, `harfHaraka [11]`).
    ة ى آ ٱ ـ are not carriers, so before them 14ب does not fire.

A5. **14ب does not require prev to be a prefix.** The sanad speaks of «السابقة» (و ف ب ك ل), but the
    rule text only says «`prev` في علاماته فتحة أو ضمّة أو كسرة». I follow the rule text: any segment
    with a short haraka qualifies, also mid-word (e.g. `قَالْ…` would make that alif `hamzaWasl`, and
    `كَتَبَاسْ` too). A prefix-restricted implementation would differ there.

A6. **14ب head «ا».** Only U+0627. ٱ never reaches 14ب (rules 6/7 take it), أ is a seat and is not
    the wasl alif. A mid-word alif *with* sukun is not «بلا علامات», so it stays `harfHaraka [11]`.

A7. **Rule 15 lam bullet, «إمّا حكمُه بالقاعدة 14ب».** Read as: prev's actual verdict (the first matching
    rule for prev) is rule 14ب, i.e. prev is L `hamzaWasl` — not merely "prev meets 14ب's conditions".
    The two readings differ only when an earlier rule pre-empts 14ب for that alif, which can only be
    rule 12 (alif whose prev has fathatan, so the prev's marks also contain a short haraka and are F by
    rule 4), e.g. `بًَالشَّ`: my reading gives the alif P «قاعدة ألف التنوين» and the lam F «حرف بلا حركة
    في غير آخر الكلمة»; the conditions-only reading would give the lam P «قاعدة لام التعريف المدغمة».
    The first branch («أوّلُ مقطعٍ في الكلمة ورأسُه ا أو ٱ») still looks only at prev's head (old note 6).

A8. **14أ, «وفي `marks` شدّة».** Rule 14 comes first, so shadda alone at word start stays P
    «قاعدة الشدّة بلا حركة», and only shadda + one vowel mark reaches 14أ. Since sukun is a vowel mark
    (old note 4), word-initial shadda+sukun is 14أ. Shadda+tanwin is taken by rule 11 first.

A9. **14أ, `awwal`.** Inherits old notes 1 and 2: a letter after a text-initial mark-headed segment, or
    after a tab/NBSP/newline, is not `awwal`, so it stays rule 16 with two cells; a letter after a
    space that carries a mark (rule 1 F) is `awwal`, so it is 14أ.

A10. **14أ, head ا.** ا is a table carrier, but rule 6 takes every word-initial ا (and ٱ) first, so
     14أ never sees an alif: `اَّ` is F «ألف محرّكة في أوّل الكلمة». ء (index 0) and the four seats
     do reach 14أ.

A11. **«والقواعدُ 1–14 و15–16 سواها كما كانت».** The wording of rule 16 is unchanged, but its reachable
     inputs changed: a word-initial carrier with shadda+vowel no longer reaches rule 16. So six old
     boundary cases changed expectation (five former R16 cases that were word-initial with shadda, and
     `وَالشَّمْسِ`, whose alif is now `hamzaWasl` and whose lam is now P by the widened rule 15). I updated
     them in place (labels marked "[amended]") rather than deleting them. Old note 4's example `بّْ`
     → `[107, 107]` now holds only when the letter is not `awwal`; old note 6's last-but-one bullet
     context (lam after an alif that is not the first segment) now gives P «قاعدة لام التعريف المدغمة»
     when that alif is 14ب.

A12. **The parenthetical note now says «القواعدُ 6–14ب».** As in old note 13 I read it as a statement
     about reachability, not an extra filter; 14أ and 14ب state their own head conditions anyway.

A13. **`hamzaWasl` in output and in `kalimat`.** hukm "L", sinf "hamzaWasl", ism "", khalaya []. In a word
     it counts as L and contributes no cell; the word is licensed iff all its segments are L and some
     other segment has a cell (e.g. `وَالْأَرْضِ` → licensed, cells `[112, 55, 0, 63, 50]`).
