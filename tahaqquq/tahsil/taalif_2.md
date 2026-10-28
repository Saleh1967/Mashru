# taalif — log of the amendment-2 work on the oracle (2026-10-28, times UTC)

## Read (only files inside this directory)
- 19:08 Directory listing; spec.md (whole, including «التعديل الثاني» and the new rule 14ب text),
  oracle.py, boundary_src.py, NOTES.md, check_boundary.py, taalif_1.md.
- 19:09 Baseline run of check_boundary.py: 152 tahsil / 19 kalimat cases, 0 mismatches, exit 0.
- 19:09 Extracted the seven letters «و ف ب ك ل ت أ» of rule 14ب from spec.md as code points
  (U+0648 U+0641 U+0628 U+0643 U+0644 U+062A U+0623) to copy them exactly.

## Changed
- 19:09 oracle.py: added CHAIN_LETTERS (explicit \u escapes); in _is_14b replaced the old
  "prev's marks contain a short haraka" test by "every segment before the alif in its word has a head in
  CHAIN_LETTERS and its marks are exactly one of fatha/damma/kasra". The rule-15 lam bullet already asks
  for prev's actual verdict (_is_14b_at -> _classify), so it follows the narrowed 14ب with no further
  change. No rule name changed or was added; the next/lam-branch part of 14ب is untouched.
- 19:10 boundary_src.py: updated in place the two old cases whose expectation amendment 2 changes,
  A30 and A31 (alif hamzaWasl -> harfMadd [11]), labels marked "[amended-2]"; added 34 new hand-derived
  tahsil cases C1–C34 (each of the seven letters alone; chains of two and three; chain broken by an
  outside letter, shadda, sukun, dammatan, fathatan, two marks, no marks, إ, ء, a mark-headed segment, a
  tab; space resetting the chain; mid-word madd alif قَالْتُ / نَامْتُ / قَتَلَاسْ; literal-shape case بَاتْ;
  lam branch after chains of two and three; rule-15 lam after a 14ب / non-14ب alif) and 5 kalimat cases
  K11–K15. Regenerated boundary.json and boundary_kalimat.json (186 / 24 cases).
- 19:10 check_boundary.py run: 186 tahsil / 24 kalimat cases, 0 mismatches, exit 0. No mismatch appeared
  on the first run, so no decision between oracle and hand derivation was needed.
- 19:11 NOTES.md: appended section «التعديل الثاني» (B1–B7); earlier notes 1–15 and A1–A13 kept
  unchanged (B7 records which A-notes are superseded).
- 19:11 This file.
