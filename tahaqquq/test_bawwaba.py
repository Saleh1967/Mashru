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
