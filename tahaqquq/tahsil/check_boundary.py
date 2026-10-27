"""Run oracle.tahsil on every hand-derived case in boundary.json (and oracle.kalimat on
boundary_kalimat.json, if present); print every mismatch.  Exit 0 iff none.
Run:  python3 -I check_boundary.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import oracle  # noqa: E402


def show(s):
    return "".join(c if 32 < ord(c) < 127 else "\\u%04x" % ord(c) for c in s)


def run(fname, fn):
    path = os.path.join(HERE, fname)
    if not os.path.exists(path):
        return 0, 0
    with open(path, encoding="utf-8") as f:
        cases = json.load(f)
    bad = 0
    for n, case in enumerate(cases):
        got = fn(case["nass"])
        if got != case["tawaqqu"]:
            bad += 1
            print("MISMATCH %s #%d %s  nass=%s" % (fname, n, case.get("label", ""), show(case["nass"])))
            exp = case["tawaqqu"]
            for k in range(max(len(got), len(exp))):
                g = got[k] if k < len(got) else None
                e = exp[k] if k < len(exp) else None
                if g != e:
                    print("   [%d] expected: %s" % (k, json.dumps(e, ensure_ascii=True)))
                    print("   [%d] oracle  : %s" % (k, json.dumps(g, ensure_ascii=True)))
    return len(cases), bad


def main():
    n1, b1 = run("boundary.json", oracle.tahsil)
    n2, b2 = run("boundary_kalimat.json", oracle.kalimat)
    print("tahsil: %d cases, %d mismatches; kalimat: %d cases, %d mismatches" % (n1, b1, n2, b2))
    return 0 if (b1 == 0 and b2 == 0 and n1 > 0) else 1


if __name__ == "__main__":
    sys.exit(main())
