# taalif — log of the amendment-1 work on the oracle (2026-10-28, times UTC)

## Read (only files inside this directory)
- 18:52 spec.md, oracle.py, NOTES.md, boundary_src.py, check_boundary.py (directory listing first).
- 18:52 Baseline run of check_boundary.py: 104 tahsil / 9 kalimat cases, 0 mismatches, exit 0.
- 18:53 Extracted the new rule name from spec.md as code points (to copy it exactly).

## Changed
- 18:54 oracle.py: added ISM_14A (explicit \u escapes, copied from the spec's «…»), SINF_WASL =
  "hamzaWasl", SHORT_HARAKAT; added rule 14أ and rule 14ب after rule 14 and before rule 15; widened the
  rule-15 lam bullet (prev is first-segment ا/ٱ, or prev's verdict is 14ب); factored the per-segment
  context into _ctx(); added _is_14b() and _is_14b_at(). Nothing else changed.
- 18:55 boundary_src.py: updated six old cases whose expectation the amendment changes (marked
  "[amended]"); added 48 new hand-derived tahsil cases (A1–A32, B1–B16) and 10 kalimat cases (K1–K10);
  regenerated boundary.json and boundary_kalimat.json.
- 18:56 check_boundary.py run: 151 / 19 cases, 0 mismatches, exit 0.
- 18:56 NOTES.md: appended section «التعديل الأوّل» (A1–A13); earlier notes kept.
- 18:57 Added case A32 (illustrates NOTES A7); regenerated; check_boundary.py: 152 / 19, 0 mismatches,
  exit 0.
- 18:57 This file.

## Remark (not a spec ambiguity)
The task said to use explicit \u escapes "as the existing file does", and oracle.py's docstring says the
same, but the existing oracle.py and boundary_src.py actually contain literal Arabic characters in their
string literals. The old code was left as it was; only the new constants use \u escapes. All rule names
in oracle.py were checked by script to occur verbatim among the spec's «…» quotes.
