# taalif — log of the amendment-3 work on the oracle (2026-10-29, times UTC)

## Read (only files inside this directory)
- 23:28 Directory listing (`ls -la`, `wc -l`). Read in full: spec.md (including «التعديل الثالث»),
  oracle.py, NOTES.md, taalif_1.md, taalif_2.md, check_boundary.py, boundary_src.py. masadir/ was not
  needed: the rule text is self-contained, and no citation was used to decide anything.
- 23:28 Baseline: `python3 -I check_boundary.py` printed «tahsil: 186 cases, 0 mismatches; kalimat: 24
  cases, 0 mismatches» and exited 0.
- 23:28 Copied the pre-amendment oracle.py and boundary_src.py to `.pre3/` (inside this folder) as
  backups.
- 23:29 Extracted the fourteen «حروف اللام المدغمة» from spec.md as code points (U+0646 U+0631 U+062F
  U+062A U+0635 U+0637 U+0632 U+0633 U+0638 U+062B U+0630 U+0636 U+0634 U+0644) so they could be copied
  exactly.

## Changed
- 23:29 oracle.py:
  - Added these constants, all with explicit \u escapes: the eleven new sinf names, TANWIN_STATE,
    NUN_TANWIN = 59, LAM_LETTERS and TA_INDEX = 18. The constants carry asserts.
  - Added `_lam_tarif_after()`, the spec's «لامُ التعريف بعد المقطع k».
  - Rewrote rules 6, 8, 9, 10, 11, 12, 13, 14 and 14أ in `_classify` to follow amendment 3.
  - In rule 15: the lam branch now splits into lamMudgham and P, and two bullets were added for a
    non-awwal bare carrier or seat: harakaMinTanwin and sukunMuqaddar.
  - Unchanged: rules 1–5, 7, 14ب, 16, the cutting, the words, `kalimat`, and every rule name.
- 23:30 `python3 -I check_boundary.py` against the old expectations printed «tahsil: 186 cases, 54
  mismatches; kalimat: 24 cases, 6 mismatches» and exited 1.
  - Before this run I had derived by hand, from the spec, which old cases change. My list had 54
    segment cases and 6 word cases, the same counts.
- 23:31 boundary_src.py: updated the expectations of those 54 + 6 cases in place.
  - Each new value was hand-written as an old→new string pair in `.pre3/amend_existing.py` (31
    replacement blocks) and applied with `python3 -I .pre3/amend_existing.py boundary_src.py`.
  - Every changed label is marked «[amended-3]». `grep -c amended-3 boundary_src.py` gives 60.
  - Added helper constructors WA, MD, TM, AM, AK, TN, TNA, HT, SI, LM and SM.
- 23:31 Rebuilt the JSON the same way as before: `python3 -I boundary_src.py` printed «186 tahsil cases;
  24 kalimat cases». Then `python3 -I check_boundary.py` printed «… 0 mismatches … 0 mismatches» and
  exited 0.
- 23:32 boundary_src.py: added 68 new hand-derived segment cases (D1–D70, plus D27b; D33, D45 and D51
  were not used because existing cases already cover them) and 9 word cases (K16–K24).
  - They were written in `.pre3/new_cases.py` and applied with
    `python3 -I .pre3/new_cases.py boundary_src.py`. A constant DAL = U+062F was added.
  - Coverage:
    - hamzaWaslAl, including the failing variants
    - madda, with and without marks
    - ة with each short haraka and each tanwin, bare, and not final
    - ى after fatha, after fathatan, after other marks, not final, and with no prev
    - tanwin on carriers and seats: with and without shadda, followed by a bare ا or ى or by another
      segment, awwal+shadda, and with و/ي/ا heads
    - tanwinAlif: akhir, not akhir, and awwal
    - alifKhatt by rules 10, 12 and 13
    - rule 14 with a next «اً», and otherwise
    - shaddaIbtida with fatha, damma and kasra, with sukun only, and on seats
    - lamMudgham before letters in the 14, outside them (ق, ب), and after a 14ب chain
    - harakaMinTanwin after a bare carrier and after a seat
    - sukunMuqaddar in the middle of a word, at the end, and on a seat
    - a bare carrier that is awwal
- 23:32 `python3 -I boundary_src.py` printed «254 tahsil cases; 33 kalimat cases».
  `python3 -I check_boundary.py` printed «tahsil: 254 cases, 0 mismatches; kalimat: 33 cases, 0
  mismatches» and exited 0.
  - No mismatch appeared on the first run, so I never had to choose between the oracle and a hand
    derivation.
- 23:33 Checked that every SINF_* value in oracle.py occurs as `name` in spec.md: all 12 do.
- 23:33 NOTES.md: appended section «التعديل الثالث» with C1–C17. Earlier notes were kept.
  - I then reworded C15 and C16 so they are precise.
  - I checked C1's and C16's examples against the oracle with a one-line `python3 -c` and they agreed
    with the notes.
- 23:34 Wrote this file. Final run of check_boundary.py: exit 0, «tahsil: 254 cases, 0 mismatches;
  kalimat: 33 cases, 0 mismatches».

## Remark
`python3 -I -c "import oracle"` fails, because `-I` drops the current directory from sys.path. The
sinf-name check was therefore run without `-I`, from this directory, and imported only the local
oracle.py.
