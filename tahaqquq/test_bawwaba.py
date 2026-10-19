"""اختبارات خطّ الأساس والتثبيت: رفض التلف، وعدم إعلان نجاح Lean قبل تشغيله؛ وحراسة قائمة الطفرات (٤أ).

التشغيل: python3 -I tahaqquq/test_bawwaba.py
"""
import contextlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bawwaba


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.home = Path(self.tmp.name)
        self.bin = self.home / "bin"
        self.bin.mkdir()
        self.downloads = self.home / "downloads"
        self.downloads.mkdir()
        self.env = dict(os.environ, HOME=str(self.home),
                        TMPDIR=str(self.downloads),
                        PATH=f"{self.bin}:/usr/bin:/bin")
        self.script = Path(__file__).resolve().parents[1] / "scripts" / "tathbit_lean.sh"
        self.log = self.home / "calls"
        self.executable(self.home / "tools" / "lean", 'echo "Lean (version 4.34.1, test)"')
        self.executable(self.home / "tools" / "lake", 'echo "Lake version test"')
        self.executable(self.home / "elan-fixture", """
echo "elan $*" >> "$HOME/calls"
case "$1 $2" in
  "toolchain install") exit 1 ;;
  "toolchain link") touch "$HOME/linked" ;;
  "default "*) exit 0 ;;
  *) exit 1 ;;
esac
""")
        self.executable(self.home / "proxy", """
[ -f "$HOME/linked" ] || exit 1
exec "$HOME/.lean/lean-4.34.1-linux/bin/$(basename "$0")" "$@"
""")
        self.executable(self.bin / "curl", """
echo "curl $*" >> "$HOME/calls"
case "$*" in
  *elan-init*) exit "${INIT_FAIL:-0}" ;;
  *lean-4.34.1-linux.zip*) exit "${ARCHIVE_FAIL:-0}" ;;
  *) exit 1 ;;
esac
""")
        self.executable(self.bin / "sha256sum", """
echo "checksum $*" >> "$HOME/calls"
cat >> "$HOME/calls"
exit "${CHECKSUM_FAIL:-0}"
""")
        self.executable(self.bin / "timeout", """
echo "timeout $*" >> "$HOME/calls"
if [ "${BOOTSTRAP_TIMEOUT:-0}" = 1 ] && [ "$2" = sh ]; then exit 124; fi
exec /usr/bin/timeout "$@"
""")
        self.executable(self.bin / "sh", """
echo "bootstrap-tmp $TMPDIR" >> "$HOME/calls"
mkdir -p "$TMPDIR/bootstrap-residue"
mkdir -p "$HOME/.elan/bin"
cp "$HOME/elan-fixture" "$HOME/.elan/bin/elan"
cp "$HOME/proxy" "$HOME/.elan/bin/lean"
cp "$HOME/proxy" "$HOME/.elan/bin/lake"
exit 0
""")
        self.executable(self.bin / "python3", """
echo extraction >> "$HOME/calls"
[ "${EXTRACT_FAIL:-0}" = 0 ] || exit 1
mkdir -p "$HOME/.lean/lean-4.34.1-linux/bin"
cp "$HOME/tools/"* "$HOME/.lean/lean-4.34.1-linux/bin/"
""")

    def executable(self, path, source):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("#!/bin/bash\n" + source + "\n", encoding="utf-8")
        path.chmod(0o755)

    def install(self, **env):
        result = subprocess.run(["/bin/bash", str(self.script)],
                                env=dict(self.env, **env), cwd=self.home,
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(list(self.downloads.iterdir()), [], "لم تُنظّف ملفات التنزيل")
        return result

    def test_bootstrap_success_without_toolchain_uses_archive(self):
        result = self.install()
        self.assertEqual(result.returncode, 0, result.stderr)
        calls = self.log.read_text()
        self.assertIn("releases/download/v4.34.1/lean-4.34.1-linux.zip", calls)
        self.assertIn("elan toolchain link leanprover/lean4:v4.34.1", calls)
        self.assertTrue((self.home / "linked").exists())
        self.assertLess(calls.index("checksum"), calls.index("extraction"))
        self.assertIn("3013aba02bb8bf31b1cf8c9d956d60fb95bb1c10920dfe91abcaa59cb461ddac", calls)
        self.assertIn("checksum --check --status", calls)
        self.assertIn("bootstrap-tmp " + str(self.downloads / "mashru-lean."), calls)

    def test_download_policy(self):
        result = self.install()
        self.assertEqual(result.returncode, 0, result.stderr)
        calls = self.log.read_text()
        downloads = [line for line in calls.splitlines() if line.startswith("curl ")]
        self.assertEqual(len(downloads), 2)
        for line in downloads:
            for flag in ("--proto =https", "--proto-redir =https", "--tlsv1.2",
                         "--connect-timeout 15", "--max-time 900",
                         "--retry 2", "--retry-max-time 1800"):
                self.assertIn(flag, line)
            self.assertIn(str(self.downloads / "mashru-lean."), line)
        self.assertIn("/9605b24b08cf68b78dce0014b6fa01be1f8e2cee/elan-init.sh", calls)
        for command in ("timeout 30 lean --version", "timeout 30 lake --version",
                        "timeout 180 sh ", "timeout 180 elan toolchain install ",
                        "timeout 30 elan toolchain link ", "timeout 30 elan default "):
            self.assertIn(command, calls)

    def test_bootstrap_timeout_uses_verified_archive(self):
        result = self.install(BOOTSTRAP_TIMEOUT="1")
        self.assertEqual(result.returncode, 0, result.stderr)
        calls = self.log.read_text()
        self.assertIn("checksum --check --status", calls)
        self.assertIn("extraction", calls)

    def test_checksum_failure_prevents_extraction(self):
        result = self.install(CHECKSUM_FAIL="1")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("بصمة أرشيف Lean غير مطابقة", result.stderr)
        self.assertNotIn("extraction", self.log.read_text())
        self.assertFalse((self.home / "linked").exists())
        self.assertNotIn("ثُبّت", result.stdout)

    def test_existing_broken_elan_uses_archive(self):
        path = self.home / ".elan" / "bin" / "elan"
        path.parent.mkdir(parents=True)
        shutil.copy(self.home / "elan-fixture", path)
        result = self.install()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.home / "linked").exists())

    def test_archive_without_elan(self):
        result = self.install(INIT_FAIL="1")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("extraction", self.log.read_text())
        self.assertNotIn("elan toolchain link", self.log.read_text())

    def test_failed_download_does_not_report_success(self):
        result = self.install(ARCHIVE_FAIL="1")
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("ثُبّت", result.stdout)
        self.assertNotIn("extraction", self.log.read_text())
        self.assertNotIn("checksum", self.log.read_text())

    def test_failed_extraction_does_not_report_success(self):
        result = self.install(EXTRACT_FAIL="1")
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("ثُبّت", result.stdout)

    def test_existing_standalone_install_needs_no_network(self):
        dest = self.home / ".lean" / "lean-4.34.1-linux" / "bin"
        shutil.copytree(self.home / "tools", dest)
        result = self.install()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("curl ", self.log.read_text())

    def test_path_persistence_failure_does_not_report_success(self):
        (self.home / ".bashrc").mkdir()
        result = self.install(INIT_FAIL="1")
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("ثُبّت", result.stdout)


class BaselineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        os.mkdir(os.path.join(self.tmp.name, "tahaqquq"))
        self.path = os.path.join(self.tmp.name, "tahaqquq", "khatt_asas.json")
        # بند ٤أ يقرأ قائمة الطفرات وأساسها؛ قائمتان فارغتان هنا فلا يؤثّر في اختبارات خطّ الأساس
        with open(os.path.join(self.tmp.name, "tahaqquq", "tafrat.json"), "w", encoding="utf-8") as f:
            f.write("[]")

    def write(self, data):
        with open(self.path, "wb") as f:
            f.write(data)

    def gate(self, count=2):
        audit = "\n".join(f"'t{i}' does not depend on any axioms" for i in range(count))
        out, err = io.StringIO(), io.StringIO()

        def run(cmd, **kwargs):
            return (0, audit) if cmd[:3] == ["lake", "env", "lean"] else (0, "")

        def git(*args):
            return (0, "asas\n") if args[0] == "merge-base" else (0, "[]")

        with patch.object(bawwaba, "ROOT", self.tmp.name), \
                patch.object(bawwaba, "run", side_effect=run), \
                patch.object(bawwaba, "git", side_effect=git), \
                patch.object(sys, "argv", ["bawwaba.py", "--bila-tafrat"]), \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            with self.assertRaises(SystemExit) as exit_result:
                bawwaba.main()
        return exit_result.exception.code, out.getvalue(), err.getvalue()

    def test_valid_baseline(self):
        self.write('{"mubarhanat": 2, "sabab": "شاهد"}\n \t'.encode())
        self.assertEqual(bawwaba.load_baseline(self.path), 2)
        self.assertEqual(self.gate()[0], 0)

    def test_corrupt_baseline_fails_closed(self):
        for data in (b'{"mubarhanat": 2}\n{"mubarhanat": 0}',
                     b'{"mubarhanat":', b"", b"\xff"):
            with self.subTest(data=data):
                self.write(data)
                code, out, err = self.gate()
                self.assertEqual(code, 2)
                self.assertIn("khatt_asas.json", out)
                self.assertIn("khatt_asas.json", err)
                self.assertNotIn("Traceback", err)
                self.assertIn("٦ الطفرات", out)

    def test_invalid_schema_fails_closed(self):
        for data in (b"[]", b"null", b"{}", b'{"mubarhanat": true}',
                     b'{"mubarhanat": -1}', b'{"mubarhanat": "2"}',
                     b'{"mubarhanat": 2.0}'):
            with self.subTest(data=data):
                self.write(data)
                self.assertEqual(self.gate()[0], 2)

    def test_missing_baseline_fails_closed(self):
        code, _, err = self.gate()
        self.assertEqual(code, 2)
        self.assertIn("khatt_asas.json", err)

    def test_theorem_count_must_not_decrease(self):
        self.write(b'{"mubarhanat": 3}')
        code, _, err = self.gate(count=2)
        self.assertEqual(code, 2)
        self.assertIn("من 3 إلى 2", err)

    def test_zero_baseline(self):
        self.write(b'{"mubarhanat": 0}')
        self.assertEqual(self.gate(count=0)[0], 0)


class TafratGuardTests(unittest.TestCase):
    """حراسة قائمة الطفرات (٤أ). التوقّعات مكتوبةٌ باليد من القاعدة: كلّ اسمٍ في الأساس حاضرٌ الآن أو مأذونٌ بحذفه."""

    def test_silent_drop_is_named(self):
        self.assertEqual(bawwaba.tafrat_naqisa(["P1_a", "P2_b", "P3_c"], ["P1_a", "P3_c", "P4_d"], []), ["P2_b"])

    def test_additions_are_free(self):
        self.assertEqual(bawwaba.tafrat_naqisa(["P1_a"], ["P1_a", "P2_b"], []), [])

    def test_ledger_permits_removal(self):
        self.assertEqual(bawwaba.tafrat_naqisa(["P1_a", "P2_b"], ["P1_a"], ["P2_b"]), [])

    def test_ledger_needs_reason_and_permission(self):
        for rec in ({"ism": "P2_b", "sabab": "x"}, {"ism": "P2_b", "idhn": "y"},
                    {"ism": "P2_b", "sabab": "x", "idhn": " "}, {"sabab": "x", "idhn": "y"}, "P2_b"):
            with self.subTest(rec=rec):
                with self.assertRaises(ValueError):
                    bawwaba.mahdhufa_maadhuna(json.dumps([rec]))
        self.assertEqual(bawwaba.mahdhufa_maadhuna(json.dumps([{"ism": "P2_b", "sabab": "x", "idhn": "y"}])), ["P2_b"])

    def test_malformed_list_is_rejected(self):
        for text in ("{}", '[{"min": "x"}]', '[{"ism": 7}]', "[1]"):
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    bawwaba.asmaa_tafrat(text)

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        os.mkdir(os.path.join(self.tmp.name, "tahaqquq"))
        with open(os.path.join(self.tmp.name, "tahaqquq", "khatt_asas.json"), "w", encoding="utf-8") as f:
            f.write('{"mubarhanat": 0}')

    def gate(self, asas, hali, ledger=None, merge_base_ok=True):
        t = os.path.join(self.tmp.name, "tahaqquq")
        # قيودٌ تامّةٌ يسلم نصُّها (٤ب): لكلّ اسمٍ سطرُ شيفرةٍ واحدٌ في ملفٍّ صغير
        with open(os.path.join(self.tmp.name, "X.lean"), "w", encoding="utf-8") as f:
            f.write("".join(f"def {n} := 1\n" for n in hali))
        with open(os.path.join(t, "tafrat.json"), "w", encoding="utf-8") as f:
            json.dump([{"ism": n, "milaf": "X.lean", "min": f"def {n} := 1", "ila": f"def {n} := 2"} for n in hali], f)
        if ledger is not None:
            with open(os.path.join(t, "tafrat_mahdhufa.json"), "w", encoding="utf-8") as f:
                json.dump(ledger, f)
        out, err = io.StringIO(), io.StringIO()

        def git(*args):
            if args[0] == "merge-base":
                return (0, "abc1234def\n") if merge_base_ok else (128, "")
            return (0, json.dumps([{"ism": n} for n in asas]))

        with patch.object(bawwaba, "ROOT", self.tmp.name), \
                patch.object(bawwaba, "run", return_value=(0, "")), \
                patch.object(bawwaba, "git", side_effect=git), \
                patch.object(sys, "argv", ["bawwaba.py", "--bila-tafrat"]), \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            with self.assertRaises(SystemExit) as exit_result:
                bawwaba.main()
        return exit_result.exception.code, out.getvalue(), err.getvalue()

    def test_gate_fails_on_silent_drop(self):
        code, out, err = self.gate(["P1_a", "P2_b"], ["P1_a"])
        self.assertEqual(code, 2)
        self.assertIn("P2_b", err)
        self.assertIn("٤أ قائمة الطفرات: الأساس abc1234 (2) ← الآن 1؛ غائبٌ بلا إذن 1", out)

    def test_gate_passes_when_all_kept(self):
        code, out, _ = self.gate(["P1_a"], ["P1_a", "P2_b"])
        self.assertEqual(code, 0)
        self.assertIn("غائبٌ بلا إذن 0", out)

    def test_gate_passes_with_permitted_removal(self):
        code, _, _ = self.gate(["P1_a", "P2_b"], ["P1_a"], [{"ism": "P2_b", "sabab": "حُذف الكود", "idhn": "المالك"}])
        self.assertEqual(code, 0)

    def test_gate_fails_closed_without_base(self):
        code, out, err = self.gate(["P1_a"], ["P1_a"], merge_base_ok=False)
        self.assertEqual(code, 2)
        self.assertIn("حراسة قائمة الطفرات", err)
        self.assertIn("لم تُقارَن بالأساس", out)
        self.assertNotIn("Traceback", err)


class TafraNassTests(unittest.TestCase):
    """نصُّ الطفرة (٤ب). الملفّات مكتوبةٌ باليد، والتوقّعاتُ من قراءة لغتها لا من الماسح: موضعُ كلّ «min» معروفٌ عند كتابته."""

    FI_TAALIQ = "«min» يقع في تعليق"
    ATHAR = "الطفرة لا تغيّر إلّا تعليقًا"
    LEAN = ("/- رأس: def f := 1 -/\n"
            "def f := 1 -- def g := 2\n"
            'def g := "-- ليس تعليقًا"\n'
            "/- خارج /- متداخل -/ ما زال تعليقًا -/\n"
            'def m := s!"{f "--"} نهاية"\n'
            'def r := r#"x"y"# -- خامٌ بعده تعليق\n'
            'def «a--b» := 1\n'
            "def q := 5 -- أوّل\n-- ثانٍ\n")
    HARF = "def k := '\"' -- كاف\n"                       # حرف '"' ثمّ تعليق
    FATHA = "def k := f h'\"' -- قاف\"\n"                 # h' اسمٌ، فما بعده نصٌّ لا حرف
    PY = ('"""وثيقة: x = 1"""\n'
          "x = 1  # y = 2\n"
          's = "# ليس تعليقًا"\n'
          "def f():\n"
          '    """توثيق الدالّة"""\n'
          '    return "قيمة"\n'
          'def g(): "توثيقٌ في سطر"\n'
          "\x0c\n"
          "z = 3  # بعد صفحة\n")
    PY_DOC = '"""الاستعمال: ابدأ"""\nimport sys\nsys.exit(__doc__)\n'
    SH = ('#!/bin/bash\n'
          'echo "# ليس" # تعليقُ السطر\n'
          'n=${#arr}\n'
          "echo $'it\\'s' # بعد اقتباس\n"
          'echo $(date)#وسم\n'
          "cat <<'EOF'\n"
          "It's # سطرُ بيانات\n"
          "EOF\n"
          "echo تم # تعليقٌ بعد الوثيقة\n")

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        for ism, nass in (("a.lean", self.LEAN), ("harf.lean", self.HARF), ("fatha.lean", self.FATHA),
                          ("b.lean", "def b := 1\n/- لم يُغلق\n"), ("a.py", self.PY), ("doc.py", self.PY_DOC),
                          ("bayad.lean", "-- def x := 1\ndef y := 2\n"), ("bayad.py", "x = 1\n# a\n# b\ny = 2\n"),
                          ("ism.lean", "def «a--b» := 17\n"), ("sifa.py", '"""Module doc"""\nimport m\nprint(m.g.__doc__)\n'),
                          ("qaws.sh", "(echo hi)#c-mu\necho $(date)#d-wasm\necho $((1))#e-wasm\n"),
                          ("tab.sh", "cat <<-EOF\n\tbayan # x-dakhil\n\tEOF\necho # baad-tab\n"),
                          ("str.sh", "cat <<<EOF # huna\necho z # baad-str\n"),
                          ("athar.lean", "def a := 5 -- x\n-- y\ndef b := 6\n"), ("izaha.py", "if x:\n    z = 0\n    # c\n    y = 1\n"),
                          ("a.sh", self.SH), ("a.tsv", "x\ty\nz\tw\n"), ("a.md", "x\n"),
                          ("raf.py", 'def f():\n    # """توثيقٌ مرفوع"""\n    return 1\n'),
                          ("raf.lean", "-- -- ملاحظةٌ مرفوعة\ndef a := 1\n"),
                          ("K.LEAN", "def k := 1\n"), ("a.txt", "x\n"), ("Makefile", "x:\n"), ("a.yml", "x: 1\n")):
            with open(os.path.join(self.tmp.name, ism), "w", encoding="utf-8") as f:
                f.write(nass)

    def ayb(self, milaf, min_, ila="تغيير"):
        return bawwaba.ayb_tafra({"ism": "P0_t", "milaf": milaf, "min": min_, "ila": ila}, self.tmp.name)

    def test_overlapping_occurrences_count(self):
        self.assertEqual(bawwaba.mawadi("aaa", "aa"), [0, 1])
        self.assertEqual(bawwaba.mawadi("abc", "x"), [])

    def test_once_exactly(self):
        self.assertIn("2 مرّة", self.ayb("a.lean", "def f := 1"))     # في الرأس وفي الشيفرة
        self.assertIn("0 مرّة", self.ayb("a.lean", "غائب"))
        self.assertIn("2 مرّة", self.ayb("a.py", "x = 1"))
        self.assertIsNone(self.ayb("a.tsv", "z\tw"))

    def test_lean_comments(self):
        self.assertEqual(self.ayb("a.lean", "def g := 2"), self.FI_TAALIQ)                 # سطريّ
        self.assertEqual(self.ayb("a.lean", "ما زال تعليقًا"), self.FI_TAALIQ)             # بعد إغلاق المتداخل
        self.assertEqual(self.ayb("a.lean", "خامٌ بعده تعليق"), self.FI_TAALIQ)           # بعد نصٍّ خامٍ فيه "
        self.assertIsNone(self.ayb("a.lean", "ليس تعليقًا"))                               # «--» في نصّ
        self.assertIsNone(self.ayb("a.lean", "نهاية"))                                     # نصٌّ مُدرَج فيه نصّ
        self.assertIsNone(self.ayb("a.lean", "a--b"))                                      # «--» في اسم «…»
        self.assertIsNone(self.ayb("ism.lean", ":= 17"))                                   # بعد اسمٍ «…» فيه «--»
        self.assertIsNone(self.ayb("a.lean", "-- def g := 2", "def g := 2"))              # رفعُ التعليق تغييرٌ في الشيفرة

    def test_uncommenting_needs_code_change(self):
        # استثناءُ رفع التعليق، وشرطُه في التوجيه «إذا كان الأثر تغييرًا تنفيذيًا حقيقيًا»؛ والمفحوصُ هنا نحويّ: رفعُ العلامة وما ظهر
        # يبقى توثيقًا أو تعليقًا لا يُقبل، ويُقبل إن صار الناتجُ نصًّا خارج التعليق. والأثرُ السلوكيّ لا يُفحص هنا (للبند ٦ بالقتل)
        self.assertEqual(self.ayb("raf.py", '# """توثيقٌ مرفوع"""', '"""توثيقٌ مرفوع"""'), self.FI_TAALIQ)
        self.assertEqual(self.ayb("raf.lean", "-- -- ملاحظةٌ مرفوعة", "-- ملاحظةٌ مرفوعة"), self.FI_TAALIQ)
        # ورفعُها إلى نصٍّ خارج التعليق يُقبل — ولو كان إسنادًا ميّتًا بلا أثرٍ سلوكيّ
        self.assertIsNone(self.ayb("raf.py", '# """توثيقٌ مرفوع"""', 'x = """توثيقٌ مرفوع"""'))

    def test_supported_extensions_are_declared(self):
        # «مع تعريف واضح للأنواع المدعومة»: الحصرُ مكتوبٌ هنا باليد، لا مقروءٌ من الشيفرة
        self.assertEqual(bawwaba.ANWA_MADUMA, {".lean", ".py", ".sh", ".tsv", ".json"})
        for milaf, min_ in (("K.LEAN", "def k"), ("a.txt", "x"), ("Makefile", "x:"), ("a.yml", "x: 1"), ("a.md", "x")):
            with self.subTest(milaf=milaf):
                self.assertIn("امتدادٌ لا تُعرف", self.ayb(milaf, min_))

    def test_lean_char_and_prime(self):
        self.assertEqual(self.ayb("harf.lean", "كاف"), self.FI_TAALIQ)                     # بعد حرف '"'
        self.assertIsNone(self.ayb("fatha.lean", "قاف"))                                   # h'"…" نصٌّ لا حرف

    def test_location_rule_survives_broken_mutant(self):
        # «min» كلُّه في تعليق، و«ila» يفتح تعليقًا لا يُغلق: يُرفض بموضعه وإن لم يُمسح المطفَّر
        self.assertEqual(self.ayb("a.lean", "ما زال تعليقًا", "ما /- زال"), self.FI_TAALIQ)
        self.assertEqual(self.ayb("a.py", "توثيق الدالّة", 'توثيق """ الدالّة'), self.FI_TAALIQ)

    def test_effect_rule(self):
        # «min» يبدأ في الشيفرة (5) والتغييرُ في التعليق وحده
        self.assertEqual(self.ayb("a.lean", "5 -- أوّل", "5 -- آخر"), self.ATHAR)

    def test_effect_rule_ignores_blank_lines(self):
        # «min» يبدأ في الشيفرة ويحذف سطرَ تعليقٍ لا غير: أثرُه لا يتعدّى التعليقَ والأسطرَ الفارغة
        self.assertEqual(self.ayb("athar.lean", "5 -- x\n-- y", "5 -- x"), self.ATHAR)
        # وإزاحةُ سطرٍ في بايثون معنى: تُقبل وإن وقع «min» في تعليقٍ وبياض
        self.assertIsNone(self.ayb("izaha.py", "# c\n    ", "# c\n"))

    def test_comment_spans_and_whitespace(self):
        # «min» يعبر تعليقين وبينهما سطرٌ جديد: في تعليق
        self.assertEqual(self.ayb("a.lean", "أوّل\n-- ثانٍ", "أوّل\n-- ثالث"), self.FI_TAALIQ)
        # «min» كلُّه في تعليق و«ila» يزيد سطرًا فارغًا لا غير: في تعليق (لا يُقبل لأنّ الباقي اختلف ببياض)
        self.assertEqual(self.ayb("bayad.lean", "def x := 1", "def x := 1\n"), self.FI_TAALIQ)
        self.assertEqual(self.ayb("bayad.py", "a\n# b", "q"), self.FI_TAALIQ)

    def test_broken_mutant_in_code_is_accepted(self):
        self.assertIsNone(self.ayb("a.lean", "def g := \"", "def g := /- \""))

    def test_unscannable_original_is_named(self):
        self.assertIn("تعذّر تعيين التعليق", self.ayb("b.lean", "def b := 1"))

    def test_python_comments_and_docstrings(self):
        self.assertEqual(self.ayb("a.py", "y = 2"), self.FI_TAALIQ)
        self.assertEqual(self.ayb("a.py", "توثيق الدالّة"), self.FI_TAALIQ)
        self.assertEqual(self.ayb("a.py", "توثيقٌ في سطر"), self.FI_TAALIQ)
        self.assertEqual(self.ayb("a.py", "بعد صفحة"), self.FI_TAALIQ)                    # بعد سطر \x0c
        self.assertIsNone(self.ayb("a.py", "ليس تعليقًا"))
        self.assertIsNone(self.ayb("a.py", "قيمة"))
        self.assertIsNone(self.ayb("doc.py", "ابدأ"))                                      # __doc__ مستعمَل: سلوك
        self.assertEqual(self.ayb("sifa.py", "Module doc"), self.FI_TAALIQ)                # m.g.__doc__ صفةٌ لا اسمٌ حرّ

    def test_sh_comments(self):
        self.assertEqual(self.ayb("a.sh", "تعليقُ السطر"), self.FI_TAALIQ)
        self.assertEqual(self.ayb("a.sh", "بعد اقتباس"), self.FI_TAALIQ)                  # بعد $'…\'…'
        self.assertEqual(self.ayb("a.sh", "تعليقٌ بعد الوثيقة"), self.FI_TAALIQ)          # بعد heredoc فيه '
        self.assertIsNone(self.ayb("a.sh", "ليس"))
        self.assertIsNone(self.ayb("a.sh", "arr"))
        self.assertIsNone(self.ayb("a.sh", "وسم"))                                         # $(date)#وسم كلمةٌ واحدة
        self.assertIsNone(self.ayb("a.sh", "سطرُ بيانات"))                                 # داخل الـheredoc بيانات
        self.assertEqual(self.ayb("qaws.sh", "c-mu"), self.FI_TAALIQ)                      # «#» بعد «)» عامل: تعليق
        self.assertIsNone(self.ayb("qaws.sh", "d-wasm"))                                   # بعد «$(…)»: الكلمة نفسُها
        self.assertIsNone(self.ayb("qaws.sh", "e-wasm"))                                   # بعد «$((…))»
        self.assertEqual(self.ayb("tab.sh", "baad-tab"), self.FI_TAALIQ)                  # بعد «<<-» بإغلاقٍ مُزاح
        self.assertIsNone(self.ayb("tab.sh", "x-dakhil"))
        self.assertEqual(self.ayb("str.sh", "huna"), self.FI_TAALIQ)                       # «<<<» ليس heredoc

    def test_malformed_entries(self):
        self.assertEqual(self.ayb("a.lean", ""), "«min» فارغ")
        self.assertIn("خارج المستودع", self.ayb("../a.lean", "x"))
        self.assertIn("خارج المستودع", self.ayb(os.path.join(self.tmp.name, "a.lean"), "x"))
        self.assertIn("امتدادٌ لا تُعرف", self.ayb("a.md", "x"))
        self.assertIn("تعذّرت قراءة", self.ayb("ghaib.lean", "x"))
        self.assertIsNotNone(self.ayb("a\x00.lean", "x"))
        self.assertIn("قيدٌ بلا", bawwaba.ayb_tafra({"ism": "P0", "milaf": "a.lean", "min": "x"}, self.tmp.name))
        self.assertIn("قيدٌ بلا", bawwaba.ayb_tafra("P0", self.tmp.name))

    def test_symlink_outside_is_rejected(self):
        with tempfile.TemporaryDirectory() as kharij:
            hadaf = os.path.join(kharij, "x.lean")
            with open(hadaf, "w", encoding="utf-8") as f:
                f.write("def v := 1\n")
            os.symlink(hadaf, os.path.join(self.tmp.name, "rabit.lean"))
            self.assertIn("خارج المستودع", self.ayb("rabit.lean", "def v := 1"))

    def test_duplicate_and_odd_names(self):
        t = {"ism": "P0_t", "milaf": "a.tsv", "min": "z\tw", "ila": "z\tv"}
        self.assertEqual(bawwaba.uyub_tafrat([t, dict(t)], self.tmp.name), ["P0_t: اسمٌ مكرَّر"])
        self.assertEqual(bawwaba.uyub_tafrat([t], self.tmp.name), [])
        self.assertEqual(len(bawwaba.uyub_tafrat([{"ism": ["x"]}, 7], self.tmp.name)), 2)   # لا TypeError

    def gate(self, tafrat_text, bila_tafrat=True):
        os.makedirs(os.path.join(self.tmp.name, "tahaqquq"), exist_ok=True)
        with open(os.path.join(self.tmp.name, "tahaqquq", "khatt_asas.json"), "w", encoding="utf-8") as f:
            f.write('{"mubarhanat": 0}')
        with open(os.path.join(self.tmp.name, "tahaqquq", "tafrat.json"), "w", encoding="utf-8") as f:
            f.write(tafrat_text)
        out, err = io.StringIO(), io.StringIO()

        def git(*args):
            return (0, "abc1234\n") if args[0] == "merge-base" else (0, "[]")

        argv = ["bawwaba.py", "--bila-tafrat"] if bila_tafrat else ["bawwaba.py"]
        with patch.object(bawwaba, "ROOT", self.tmp.name), \
                patch.object(bawwaba, "run", return_value=(0, "")), \
                patch.object(bawwaba, "git", side_effect=git), \
                patch.object(sys, "argv", argv), \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            with self.assertRaises(SystemExit) as exit_result:
                bawwaba.main()
        return exit_result.exception.code, out.getvalue(), err.getvalue()

    def test_gate_names_the_defect(self):
        code, out, err = self.gate(json.dumps([{"ism": "P0_taaliq", "milaf": "a.lean", "min": "def g := 2", "ila": "def g := 3"}]))
        self.assertEqual(code, 2)
        self.assertIn("٤ب نصوص الطفرات: 1 طفرة، معيبةٌ 1", out)
        self.assertIn("P0_taaliq: " + self.FI_TAALIQ, err)

    def test_gate_unreadable_list_is_named(self):
        code, out, err = self.gate("{}")
        self.assertEqual(code, 2)
        self.assertIn("٤ب نصوص الطفرات: لم تُفحص", out)
        self.assertNotIn("Traceback", err)

    def test_sweep_does_not_write_defective_mutation(self):
        with tempfile.TemporaryDirectory() as kharij:
            hadaf = os.path.join(kharij, "x.lean")
            with open(hadaf, "w", encoding="utf-8") as f:
                f.write("def v := 1\n")
            code, out, err = self.gate(json.dumps([{"ism": "P0_kharij", "milaf": hadaf, "min": "def v := 1",
                                                    "ila": "def v := 999"}]), bila_tafrat=False)
            with open(hadaf, encoding="utf-8") as f:
                self.assertEqual(f.read(), "def v := 1\n")
        self.assertEqual(code, 2)
        self.assertIn("P0_kharij (٤ب: الملفّ خارج المستودع", err)
        self.assertNotIn("Traceback", err)

    def test_sweep_judges_repository_not_copy(self):
        # رابطٌ رمزيّ داخل المستودع إلى ملفٍّ خارجه: النسخُ يجعله ملفًّا عاديًّا، فيُحكم على المستودع لا على النسخة
        with tempfile.TemporaryDirectory() as kharij:
            hadaf = os.path.join(kharij, "x.lean")
            with open(hadaf, "w", encoding="utf-8") as f:
                f.write("def v := 1\n")
            os.symlink(hadaf, os.path.join(self.tmp.name, "rabit.lean"))
            code, out, err = self.gate(json.dumps([{"ism": "P0_rabit", "milaf": "rabit.lean", "min": "def v := 1",
                                                    "ila": "def v := 999"}]), bila_tafrat=False)
            with open(hadaf, encoding="utf-8") as f:
                self.assertEqual(f.read(), "def v := 1\n")
        self.assertEqual(code, 2)
        self.assertIn("P0_rabit (٤ب: الملفّ خارج المستودع", err)


    def mash(self, fashil=None):
        """البند ٦ على طفرةٍ واحدةٍ سليمة، مع تسجيل ما يُشغَّل في النسخة؛ fashil: رقمُ اختبارٍ يفشل (من 0)."""
        with open(os.path.join(self.tmp.name, "m.lean"), "w", encoding="utf-8") as f:
            f.write("def m0 := 1\n")
        tafrat = [{"ism": "P0_m", "milaf": "m.lean", "min": "def m0 := 1", "ila": "def m0 := 2"}]
        os.makedirs(os.path.join(self.tmp.name, "tahaqquq"), exist_ok=True)
        with open(os.path.join(self.tmp.name, "tahaqquq", "khatt_asas.json"), "w", encoding="utf-8") as f:
            f.write('{"mubarhanat": 0}')
        with open(os.path.join(self.tmp.name, "tahaqquq", "tafrat.json"), "w", encoding="utf-8") as f:
            json.dump(tafrat, f)
        sijill = []

        def run(cmd, cwd=None, **kw):
            if cwd is not None and cwd != self.tmp.name:
                sijill.append(cmd[-1])
                if fashil is not None and cmd[-1] == bawwaba.IKHTIBARAT_TAFRAT[fashil]:
                    return (1, "")
            return (0, "")

        def git(*args):
            return (0, "abc1234\n") if args[0] == "merge-base" else (0, json.dumps(tafrat))

        out, err = io.StringIO(), io.StringIO()
        with patch.object(bawwaba, "ROOT", self.tmp.name), patch.object(bawwaba, "run", side_effect=run), \
                patch.object(bawwaba, "git", side_effect=git), patch.object(sys, "argv", ["bawwaba.py"]), \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            with self.assertRaises(SystemExit):
                bawwaba.main()
        return sijill, out.getvalue()

    def test_sweep_runs_every_test_in_order(self):
        sijill, out = self.mash()
        self.assertEqual(sijill, ["build"] + list(bawwaba.IKHTIBARAT_TAFRAT))
        self.assertIn("٦ الطفرات: قُتلت 0 من 1", out)

    def test_sweep_stops_at_first_failure(self):
        sijill, out = self.mash(fashil=2)
        self.assertEqual(sijill, ["build"] + list(bawwaba.IKHTIBARAT_TAFRAT[:3]))
        self.assertIn("٦ الطفرات: قُتلت 1 من 1", out)

    def test_sweep_list_matches_gate_tests(self):
        # كلُّ اختبارٍ يشغّله البند ٥ (سوى ما يحتاج مودَعًا بوسيط) يشغّله البند ٦ أيضًا
        import re
        src = open(bawwaba.__file__, encoding="utf-8").read()
        rais = src[src.index("def main():"):src.index('    if "--bila-tafrat" not in sys.argv:')]
        band5 = re.findall(r'run\(\[sys\.executable, "-I", "([^"]+)"\]\)', rais)
        self.assertEqual(sorted(band5), sorted(bawwaba.IKHTIBARAT_TAFRAT))

class TafratJuzTests(unittest.TestCase):
    """tahaqquq/tafrat_juz.py: الاستعمالُ الخاطئ يُسمّى ويخرج 2، بلا Traceback وقبل أيّ نسخ."""

    def juz(self, *names):
        with tempfile.TemporaryDirectory() as root:
            os.mkdir(os.path.join(root, "tahaqquq"))
            shutil.copy(os.path.join(os.path.dirname(__file__), "bawwaba.py"), os.path.join(root, "tahaqquq"))
            with open(os.path.join(root, "tahaqquq", "tafrat.json"), "w", encoding="utf-8") as f:
                json.dump([{"ism": ["ghayr", "nassi"]}, {"ism": "P0_a", "milaf": "a.lean", "min": "x", "ila": "y"}], f)
            p = subprocess.run([sys.executable, "-I", os.path.join(os.path.dirname(__file__), "tafrat_juz.py"), root, *names],
                               capture_output=True, text=True, timeout=60)
            return p.returncode, p.stdout + p.stderr

    def test_unknown_name_is_named(self):
        code, out = self.juz("P9_majhul")
        self.assertEqual(code, 2)
        self.assertIn("P9_majhul", out)
        self.assertNotIn("Traceback", out)

    def test_no_names_is_usage(self):
        code, out = self.juz()
        self.assertEqual(code, 2)
        self.assertIn("الاستعمال", out)

    def juz_lake(self, lake_sh, tafrat, milafat):
        """tafrat_juz.py على مستودعٍ صغير بـ lake مزيَّف في PATH ومهلةِ ثانية."""
        with tempfile.TemporaryDirectory() as root, tempfile.TemporaryDirectory() as bindir:
            os.mkdir(os.path.join(root, "tahaqquq"))
            shutil.copy(os.path.join(os.path.dirname(__file__), "bawwaba.py"), os.path.join(root, "tahaqquq"))
            with open(os.path.join(root, "tahaqquq", "tafrat.json"), "w", encoding="utf-8") as f:
                json.dump(tafrat, f)
            for ism, nass in milafat.items():
                if nass.startswith("->"):
                    os.symlink(nass[2:], os.path.join(root, ism))
                else:
                    with open(os.path.join(root, ism), "w", encoding="utf-8") as f:
                        f.write(nass)
            alama = os.path.join(bindir, "nudiya")
            with open(os.path.join(bindir, "lake"), "w", encoding="utf-8") as f:
                f.write("#!/bin/sh\ntouch " + alama + "\n" + lake_sh + "\n")
            os.chmod(os.path.join(bindir, "lake"), 0o755)
            env = dict(os.environ, PATH=bindir + os.pathsep + os.environ.get("PATH", ""), TAFRAT_JUZ_MUHLA="1")
            names = sorted({t["ism"] for t in tafrat if isinstance(t, dict)})
            p = subprocess.run([sys.executable, "-I", os.path.join(os.path.dirname(__file__), "tafrat_juz.py"), root, *names],
                               capture_output=True, text=True, timeout=120, env=env)
            return p.returncode, p.stdout + p.stderr, os.path.exists(alama)

    SALIMA = [{"ism": "P0_s", "milaf": "a.lean", "min": "def x := 1", "ila": "def x := 2"}]

    def test_timeout_is_not_a_kill(self):
        code, out, _ = self.juz_lake("sleep 5", self.SALIMA, {"a.lean": "def x := 1\n"})
        self.assertEqual(code, 3)
        self.assertIn("تجاوز المهلة", out)
        self.assertNotIn("قُتلت بـ", out)

    def test_build_error_names_the_file(self):
        code, out, _ = self.juz_lake('echo "error: a.lean:1:0: x"; exit 1', self.SALIMA, {"a.lean": "def x := 1\n"})
        self.assertEqual(code, 0)
        self.assertIn("قُتلت بـlake build (a.lean)", out)

    def test_symlink_judged_on_repository(self):
        with tempfile.TemporaryDirectory() as kharij:
            hadaf = os.path.join(kharij, "x.lean")
            with open(hadaf, "w", encoding="utf-8") as f:
                f.write("def x := 1\n")
            code, out, nudiya = self.juz_lake("exit 0", [dict(self.SALIMA[0], milaf="rabit.lean")], {"rabit.lean": "->" + hadaf})
            with open(hadaf, encoding="utf-8") as f:
                self.assertEqual(f.read(), "def x := 1\n")
        self.assertEqual(code, 1)
        self.assertIn("معيبة (٤ب)", out)
        self.assertFalse(nudiya)

    def test_duplicate_name_is_refused(self):
        code, out, nudiya = self.juz_lake("exit 0", self.SALIMA * 2, {"a.lean": "def x := 1\n"})
        self.assertEqual(code, 2)
        self.assertIn("مكرَّرة", out)
        self.assertFalse(nudiya)


if __name__ == "__main__":
    unittest.main()
