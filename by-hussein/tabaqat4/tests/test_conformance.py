# -*- coding: utf-8 -*-
"""T19 — مطابقة مخرجات الأداة مع مستودع Mashru نفسه (لا مع نسخة محفوظة منه).
تُشغَّل: python3 -I by-hussein/tabaqat4/tests/test_conformance.py
T19a  كلّ شاهد Kalima حرفيّ في Jisr/Utur.lean (يُقرأ من المصدر بسطحه في التعليق) → encode_word يعطي خلاياه وأعلامه بعينها
T19b  tests/conf/Conf.lean على Mashru: ours = dhahabaAlWalad by decide ، mumtani ، J16 ، halat.filter = [] ، المسلّمات ⊆ المسموح
إن انكسر أحدهما فالمستودع غيّر ترميزه أو شاهده أو ضابطه — ويُعلَن باسمه ، ولا يُخفَّف شرط."""
import os, re, sys, subprocess, shutil, unittest, unicodedata
from pathlib import Path
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'; sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent; TOOL = HERE.parent
sys.path.insert(0, str(TOOL))
from t4.dal import load_hawamil, encode_word   # noqa
from t4.core import AXIOMS_OK                  # noqa


def mashru_root() -> Path:
    env = os.environ.get('MASHRU_ROOT')
    if env: return Path(env)
    for p in TOOL.parents:
        if (p / 'lakefile.toml').exists() and (p / 'Dal' / 'Makharij.lean').exists(): return p
    raise SystemExit('MASHRU_ROOT_NOT_FOUND')


ROOT = mashru_root()
KALIMA_RE = re.compile(r'^def\s+(\w+)\s*:\s*Kalima\s*:=\s*⟨\[([^\]]*)\]\s*,\s*(true|false)\s*,\s*(true|false)\s*⟩\s*--\s*(\S+)', re.M)
AR = re.compile(r'^[ء-يً-ْٰ]+$')


def repo_witnesses():
    src = (ROOT / 'Jisr' / 'Utur.lean').read_text(encoding='utf-8')
    out = []
    for name, cells, wasl, al, surf in KALIMA_RE.findall(src):
        surf = unicodedata.normalize('NFC', surf.strip('؛،.,:'))
        if not AR.match(surf): continue
        vals = [eval(c.strip(), {'__builtins__': {}}, {}) for c in cells.split(',') if c.strip()]  # أعداد وضرب/جمع فقط من المصدر
        out.append((name, surf, vals, wasl == 'true', al == 'true'))
    return out


def lake_cmd():
    lake = shutil.which('lake') or (str(Path.home() / '.elan' / 'bin' / 'lake') if (Path.home() / '.elan' / 'bin' / 'lake').exists() else None)
    return lake


class T19(unittest.TestCase):
    def test_a_kalima_witnesses(self):
        haw = load_hawamil(ROOT); ws = repo_witnesses()
        self.assertGreaterEqual(len(ws), 10, 'KALIMA_WITNESSES_NOT_FOUND_IN_UTUR')
        bad = []
        for name, surf, cells, wasl, al in ws:
            k = encode_word(surf, haw)
            if (k.khalaya, k.wasl, k.al) != (cells, wasl, al):
                bad.append(f'{name} {surf}: ours={k.khalaya},{k.wasl},{k.al} repo={cells},{wasl},{al}')
        print(f'T19a KALIMA_WITNESSES = {len(ws) - len(bad)}/{len(ws)}' + (' ؛ ' + ' | '.join(bad) if bad else ''))
        self.assertEqual(bad, [])

    def test_b_conf_lean(self):
        lake = lake_cmd()
        if not lake: self.skipTest('LAKE_NOT_FOUND')
        env = dict(os.environ, PATH=str(Path(lake).parent) + os.pathsep + os.environ.get('PATH', ''))
        p = subprocess.run([lake, 'env', 'lean', str(HERE / 'conf' / 'Conf.lean')], cwd=str(ROOT), capture_output=True, text=True, timeout=900, env=env)
        out = p.stdout
        self.assertEqual(p.returncode, 0, 'CONF_LEAN_FAILED: ' + (p.stderr or p.stdout)[:800])
        lines = [l.strip() for l in out.splitlines() if l.strip()]
        evals = [l for l in lines if not l.startswith("'")]
        self.assertEqual(evals[0], 'none', f'J_GENERAL_CASE_NOW_IN_DAWABIT: {evals[0]}')
        self.assertTrue(evals[1].startswith('some ("J16"') and 'qabih' in evals[1], f'J16_MISMATCH: {evals[1]}')
        self.assertEqual(evals[2], '(Jisr.BabJaza.Daraja.maqbul, Jisr.BabJaza.Daraja.maqbul, Jisr.BabJaza.Daraja.qabih, Jisr.BabJaza.Daraja.maqbul)', f'HUKM_PAIR: {evals[2]}')
        self.assertEqual(evals[3], '[]', f'DAWABIT_INCONSISTENT_WITH_HUKM: {evals[3]}')
        ax = {}
        for l in lines:
            m = re.match(r"'(Conf\.\w+)' (?:depends on axioms: \[(.*)\]|does not depend on any axioms)", l)
            if m: ax[m.group(1)] = set(a.strip() for a in (m.group(2) or '').split(',') if a.strip())
        self.assertEqual(set(ax), {'Conf.ours_eq_repo', 'Conf.mumtani_from_repo', 'Conf.t4'}, f'AXIOMS_LINES: {ax}')
        for k, v in ax.items(): self.assertTrue(v <= set(AXIOMS_OK), f'{k} axioms {v}')
        print(f'T19b CONF_LEAN = PASS ؛ find?=({evals[0]} ، {evals[1]}) ؛ filter={evals[3]} ؛ axioms={ {k.split(".")[1]: sorted(v) for k, v in ax.items()} }')


if __name__ == '__main__':
    r = unittest.main(exit=False, verbosity=0).result
    ok = r.wasSuccessful() and not r.skipped
    print(f'TABAQAT4_CONFORMANCE_PASS = {"YES" if ok else "NO"} (ran={r.testsRun} failed={len(r.failures)+len(r.errors)} skipped={len(r.skipped)}) ؛ MASHRU_ROOT={ROOT}')
    sys.exit(0 if ok else 1)
