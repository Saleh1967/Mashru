"""اختبارات خطّ الأساس والتثبيت: رفض التلف، وعدم إعلان نجاح Lean قبل تشغيله.

التشغيل: python3 -I tahaqquq/test_bawwaba.py
"""
import contextlib
import io
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
        self.env = dict(os.environ, HOME=str(self.home),
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
        self.executable(self.bin / "sh", """
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
        return subprocess.run(["/bin/bash", str(self.script)],
                              env=dict(self.env, **env), cwd=self.home,
                              capture_output=True, text=True, timeout=10)

    def test_bootstrap_success_without_toolchain_uses_archive(self):
        result = self.install()
        self.assertEqual(result.returncode, 0, result.stderr)
        calls = self.log.read_text()
        self.assertIn("releases/download/v4.34.1/lean-4.34.1-linux.zip", calls)
        self.assertIn("elan toolchain link leanprover/lean4:v4.34.1", calls)
        self.assertTrue((self.home / "linked").exists())

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

    def test_failed_extraction_does_not_report_success(self):
        result = self.install(EXTRACT_FAIL="1")
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("ثُبّت", result.stdout)

    def test_existing_standalone_install_needs_no_network(self):
        dest = self.home / ".lean" / "lean-4.34.1-linux" / "bin"
        shutil.copytree(self.home / "tools", dest)
        result = self.install()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.log.exists())

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

    def write(self, data):
        with open(self.path, "wb") as f:
            f.write(data)

    def gate(self, count=2):
        audit = "\n".join(f"'t{i}' does not depend on any axioms" for i in range(count))
        out, err = io.StringIO(), io.StringIO()

        def run(cmd, **kwargs):
            return (0, audit) if cmd[:3] == ["lake", "env", "lean"] else (0, "")

        with patch.object(bawwaba, "ROOT", self.tmp.name), \
                patch.object(bawwaba, "run", side_effect=run), \
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


if __name__ == "__main__":
    unittest.main()
