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

## التعديل الثاني

Readings of amendment 2 (rule 14ب's narrowed condition on what precedes the alif, and what depends on
14ب's verdict). Numbering restarts at B1. Earlier notes stand except where B7 says otherwise.

B1. **«وعلاماتُه علامةٌ واحدةٌ هي فتحةٌ أو ضمّةٌ أو كسرة».** Read as: the segment's `marks` are exactly one
    code point, and it is U+064E, U+064F or U+0650. Shadda is one of the eight marks, so a chain segment
    with shadda + fatha has two marks and breaks the chain. The other reading is "exactly one *vowel* mark,
    and it is short" (shadda allowed). Example `وَبَّاسْ`: mine gives the alif `harfMadd [11]`; the other
    gives `hamzaWasl`. Sukun, a tanwin, two marks, or no marks also break the chain (cases C15–C19).

B2. **«أ» in «و ف ب ك ل ت أ».** Only U+0623 (the seven code points are copied from the spec: U+0648
    U+0641 U+0628 U+0643 U+0644 U+062A U+0623). إ ؤ ئ and bare ء are not in the set, although rule 3 groups
    them with أ as hamza seats/carrier 0. Example `إِاسْ`: mine gives the alif `harfMadd [11]`; a
    "any hamza seat" reading gives `hamzaWasl`. Likewise ل is U+0644 only, ك is U+0643 only (not U+06A9).

B3. **Chain shape: length, order, repetition, which short haraka.** «كلُّ مقطعٍ قبله في كلمته» puts no limit
    on the number of segments, their order, or repeats, and «فتحةٌ أو ضمّةٌ أو كسرة» is not tied to the
    letter. So `وَلِتُاسْ`, `بُاسْ` and `وِ…` all qualify. The amendment's prose names grammatical functions
    (عطف، جرّ، قسم، استفهام), which would suggest fixed vowels (وَ فَ بِ كَ لِ/لَ تَ أَ) and a fixed order
    (أ before و/ف, these before the jarr letters, one of each). I follow the rule text, not the
    motivation. Example `بُاسْ` (C3): mine `hamzaWasl`; a fixed-vowel reading gives `harfMadd [11]`.

B4. **Shape, not lexicon.** The chain test looks only at heads and marks, so a mid-word madd alif whose
    preceding letters happen to all be from the seven still meets 14ب: `بَاتْ` gives the alif `hamzaWasl`
    and `كَتَبَاسْ` likewise. Only a word containing some letter outside the set before the alif (`قَالْتُ`,
    `نَامْتُ`, `قَتَلَاسْ`) is protected. A reading that requires the segments to be real prefixes (a lexical
    test) would give `بَاتْ` → `harfMadd [11]`. I chose the literal reading (case C29).

B5. **«كلُّ مقطعٍ قبله في كلمته» and non-letter segments.** Every segment of the word before the alif
    counts, including a text-initial mark-headed segment (old note 1) and a tab/NBSP/foreign segment (old
    note 2); their heads are not in the set, so they break the chain. A segment in an earlier word (across
    U+0020) does not count. Examples: `َوَاسْ` → alif `harfMadd [11]` (C23); `قَ وَاسْ` → alif `hamzaWasl`
    (C25). An implementation that skipped non-letter segments would give `hamzaWasl` for C23.

B6. **Rule 15 lam bullet, «إمّا حكمُه بالقاعدة 14ب», under the narrowed 14ب.** I keep note A7's reading (the
    prev alif's actual verdict is 14ب). With the new condition the two readings of A7 no longer differ:
    rule 12 needs a fathatan in prev's marks and rule 13 needs prev headed by و with no marks or sukun;
    a chain prev has exactly one short haraka, so neither can pre-empt an alif that meets 14ب, and rules
    6–11 and 14–14أ cannot reach a bare non-initial ا. So "verdict is 14ب" and "conditions of 14ب hold" now
    coincide. A7's example `بًَالشَّ` now fails 14ب's chain anyway (two marks), so under both readings the
    alif is P «قاعدة ألف التنوين» and the lam F «حرف بلا حركة في غير آخر الكلمة». Consequence: the lam
    bullet's second branch fires only after a chain alif (`وَبِالشَّمْسِ` → lam P «قاعدة لام التعريف
    المدغمة»); after a non-chain alif (`قَالشَّ`) the lam is F «حرف بلا حركة في غير آخر الكلمة».

B7. **Status of earlier notes.** «والقواعدُ سواها كما كانت في التعديل الأوّل»: only 14ب's prev condition
    changed; A1, A3, A4, A6 (next, lam branch, head) stand.
    - A2 (prev's marks *contain* a short haraka; prev's verdict ignored) is superseded by B1: two marks
      no longer qualify. Two old cases changed expectation and were updated in place, labels marked
      "[amended-2]": A30 (`بِّاسْ`, prev 14أ) and A31 (`بَُاسْ`, prev F by rule 4); their alif is now
      `harfMadd [11]`. Chain segments' verdicts are now always rule 16 with one cell, so "verdict
      ignored" has no remaining effect.
    - A5 (any prev, not only a prefix) is superseded: the rule text now names the seven letters. Its
      example `قَالْ…` is no longer `hamzaWasl`; `كَتَبَاسْ` still is (B4).
    - A4's example `بَااْ` still gives the first alif `hamzaWasl` (بَ is a chain of one).

## التعديل الثالث

Readings of amendment 3 (2026-10-29): rules 6, 8, 9, 10, 11, 12, 13, 14, 14أ and 15 gain L verdicts, and
the output has eleven new `sinf` names. Numbering restarts at C1. Earlier notes stand unless an item here
says otherwise. «حركةٌ قصيرة» is read throughout as U+064E/U+064F/U+0650. The spec's defined «الحالة
من التنوين» gives fathatan 0, dammatan 1, kasratan 2.

C1. **«لامُ التعريف بعد المقطع k» … «وإمّا لا شيء ومقطعٌ بعده في الكلمة في علاماته شدّة».**
    - Reading 1: «بعده» is the lam, and the segment meant is the one right after it.
    - Reading 2: any later segment in the word.
    - Implemented: reading 1, which is the same reading as note A1 for the lam branch of 14ب.
    - «سكونٌ وحده» means the lam's marks are exactly one U+0652; sukun+shadda does not count.
    - Example `الكَتَّ`: under reading 1 the alif is P «قاعدة همزة الوصل»; under reading 2 it is
      `hamzaWaslAl`.

C2. **Rule 6, «بلا علامات».** An alif or ٱ that carries a shadda only, with no vowel mark, is not bare. So
    it stays P «قاعدة همزة الوصل», even before a lam with sukun (case D9). The other reading counts only
    vowel marks.

C3. **Rule 6 ignores the lam's own verdict and anything after the lam.**
    - `hamzaWaslAl` depends only on the shape that the definition in C1 describes.
    - So the alif is `hamzaWaslAl` even when the lam is P «قاعدة لام التعريف المدغمة» (qaf or ba after
      it, cases D56 and D57) and when the shadda-bearing segment is F (rule 4).
    - The word «الْ» alone gives the alif `hamzaWaslAl`.

C4. **Rule 8 does not require `awwal`.**
    - A bare آ in the middle or at the end of a word is `madda [0, 11]` too (case D12).
    - Any mark makes it P, including shadda alone (case D13).

C5. **Rule 9, «علاماتُه علامةٌ واحدة: حركةٌ قصيرةٌ … أو تنوين».**
    - The marks must be exactly one code point, read the same way as B1. So shadda+fatha is P (case D21).
    - Sukun is a «علامة حركة» but not a «حركة قصيرة», so ة with sukun stays P (case A22).
    - A bare ة, or one that is not `akhir`, stays P.

C6. **Rule 10, «في علامات `prev` فتحة / فتحتان».**
    - Read as containment, the same way as old note 8. A prev with shadda+fatha qualifies, so the result
      is `alifMaqsura` (case D25).
    - The prev's own verdict is ignored.
    - If the prev's marks hold both a fatha and a fathatan (F by rule 4), the fatha branch, which is listed
      first, gives `alifMaqsura`.
    - A mark-headed prev has no marks, so the result is P (case D27b).
    - «له `prev`» is within the word, so ى after a space is P.

C7. **Rule 11, first branch: «وكلُّ مقطعٍ بعده في كلمته رأسُه ا أو ى بلا علامات».**
    - «بلا علامات» applies to both ا and ى.
    - Every later segment of the word must meet the condition, with no limit on how many. So `بًاا`
      gives tanwin, then `alifKhatt`, then `harfMadd` (case D39).
    - Any other segment after the head (a letter, a tab, an alif with a mark) makes it P.
    - «غيرُ ا وو وي» excludes only U+0627, U+0648 and U+064A. The excluded heads (cases D34–D36) and ء
      both follow the literal text: ء is a table carrier with h = 0.

C8. **Rule 11, «وليس (`awwal` وفي `marks` شدّة)».**
    - Only a word-initial carrier that has both shadda and tanwin is excluded; it stays P (cases B9 and
      R12).
    - A carrier that is not `awwal` and has shadda+tanwin gives three cells, `[4h+3, 4h+s, 59]`
      (case D31).

C9. **Rule 11, second branch (`tanwinAlif`).**
    - «`marks` فتحتان وحدهما» means exactly the one code point U+064B. Shadda+fathatan is P (case D43).
    - `awwal` is never reached here, because rule 6 takes every word-initial alif first (case D42, F).
    - So «وله `prev`» is always true at this point.

C10. **Rules 14 and 15, «`next` رأسُه ا وعلاماتُه فتحتان وحدهما وهو `akhir`».**
     - «وهو `akhir`» is read as the next segment being the last of the word. The current segment cannot
       be, since it has a next.
     - Fathatan alone means exactly one code point.

C11. **Rule 14 comes before 14أ.**
     - A word-initial carrier with shadda only, followed by a final «اً», is `harakaMinTanwin` with two
       cells `[4h+3, 4h]` (case D47). The half-shadda drop of 14أ does not apply here.
     - The alternative would treat it as 14أ, but 14أ needs a vowel mark, so that reading would leave it
       P.
     - Rule 14's guard «والرأسُ هنا حاملٌ أو مقعد» never rejects anything. Every head that reaches rule
       14 is a carrier or a seat, because ـ ة ى آ ٱ are all taken by rules 5–10. A bare word-initial ا is
       taken by rule 6.

C12. **Rule 14أ, «إن كان في `marks` حركةٌ قصيرةٌ بحالتها s».**
     - Sukun is not short, so word-initial shadda+sukun stays P «قاعدة الشدّة في أوّل الكلمة».
     - The order of shadda and haraka does not matter (old note 5).

C13. **Rule 12 and rule 13 become L `alifKhatt` unconditionally.**
     - The text keeps their old conditions and gives no fallback, so nothing that used to reach them
       stays P.
     - Rule 12 still ignores the prev's verdict. Under A32 the prev is F by rule 4 and the alif is still
       `alifKhatt`.

C14. **Rule 15, lam branch: «إن كان رأسُ `next` من حروف اللام المدغمة ← L … وإلّا ← P».**
     - Once the lam branch's own conditions hold (prev as before, and next has a shadda), the «وإلّا»
       here is P «قاعدة لام التعريف المدغمة» (cases D56, D57, D59). The lam does not go on to the
       `harakaMinTanwin`/`sukunMuqaddar` bullets.
     - When the conditions fail, the lam does go on to those bullets: `sukunMuqaddar [55]` (cases D8,
       A9–A11, C32–C34), or `harakaMinTanwin [52]` before «اً» (case D70).
     - The fourteen letters are the code points copied from the spec. ل counts, so ٱللَّه gives the lam
       `lamMudgham`.
     - The prev test still looks only at the first segment's head (ا/ٱ), as in old note 6. So `اَلشَّ`
       gives the lam `lamMudgham` while the alif is F.

C15. **Rule 15, `sukunMuqaddar` covers `akhir` too.**
     - «وإلّا إن كان الرأسُ حاملًا … وليس `awwal`» has no `akhir` condition. So every bare carrier or seat
       that is not word-initial is `sukunMuqaddar`, whether it is in the middle of the word or at the end
       (cases D64–D66 and the amended R15 cases).
     - P «قاعدة الحرف الأخير بلا حركة» remains only for a bare letter that is both `awwal` and `akhir`
       (a one-segment word).
     - F «حرف بلا حركة في غير آخر الكلمة» remains only for a bare word-initial letter in a longer word.
     - Bare ا/و/ي that are not `awwal` still go to `harfMadd` first («بعد فرع حرف المدّ كما كان»), so
       they are never `sukunMuqaddar` or `harakaMinTanwin` (case D69).

C16. **The tahsil of amendment 3 only reads the verdicts that earlier notes already read.**
     - The rule-15 lam branch reads the prev's 14ب verdict (note A7).
     - No new rule reads another segment's verdict: rules 10, 11 and 12 look at marks and heads only.
     - Hence rule 11 can give a carrier `tanwin` while a following ى is P. In `بًىا` the ba is
       `tanwin` (everything after it is a bare ا or ى), the ى is P because it is not `akhir`, and the
       final alif is `harfMadd` (its prev has no fathatan). The other reading, which would make the
       carrier's verdict depend on the ى's verdict, would give the ba P.

C17. **`kalimat`.** Licensing is unchanged.
     - `hamzaWaslAl`, `madda`, `taMarbuta`, `alifMaqsura`, `tanwin`, `tanwinAlif`, `harakaMinTanwin`,
       `shaddaIbtida` and `sukunMuqaddar` add their cells to the word.
     - `alifKhatt` and `lamMudgham` are L with no cell, like `hamzaWasl`.
     - Six old word cases changed expectation and are marked "[amended-3]".
