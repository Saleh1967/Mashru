"""Process and reporting boundaries of the native NABT validation runner.

Small real subprocesses exercise failures and skipped-test rejection. Mocked
build commands test scheduling without claiming a Lean build or language
coverage result. No upstream source, fixture or test is replaced.
"""

from __future__ import annotations

import argparse
from contextlib import redirect_stdout
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("mashru_nabt_runner", ROOT / "scripts/check_nabt.py")
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class ValidationRunnerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.output = self.root / "run"
        self.output.mkdir()
        self.report = {"steps": [], "status": "RUNNING"}

    def step(self, code, *, tests=True):
        with redirect_stdout(io.StringIO()):
            return runner.run_step(self.report, self.output, "fixture",
                                   [sys.executable, "-I", "-B", "-c", code], self.root,
                                   dict(os.environ), tests=tests)

    def test_success_records_actual_exit_log_and_test_count(self):
        self.step("print('Ran 7 tests in 0.001s\\n\\nOK')")
        step = self.report["steps"][0]
        self.assertEqual((step["status"], step["returncode"], step["unittest_runs"], step["skipped"]),
                         ("PASSED", 0, [7], 0))
        self.assertTrue(Path(step["log"]).is_file())
        self.assertEqual(len(step["log_sha256"]), 64)

    def test_nonzero_subprocess_exit_is_retained_and_fails(self):
        with self.assertRaisesRegex(runner.CheckFailed, "NABT_COMMAND_FAILED"):
            self.step("import sys; print('actual failure'); sys.exit(7)", tests=False)
        step = json.loads((self.output / "manifest.json").read_text())["steps"][0]
        self.assertEqual((step["status"], step["returncode"]), ("FAILED", 7))
        self.assertIn("actual failure", Path(step["log"]).read_text())

    def test_zero_exit_with_skipped_tests_cannot_pass(self):
        with self.assertRaisesRegex(runner.CheckFailed, "NABT_TESTS_SKIPPED"):
            self.step("print(\"setUpClass (probe.Tests) ... skipped 'no binary'\\nRan 0 tests in 0.001s\\n\\nOK (skipped=1)\")")
        self.assertEqual(self.report["steps"][0]["status"], "FAILED")

    def test_zero_exit_without_test_execution_cannot_pass_a_test_step(self):
        with self.assertRaisesRegex(runner.CheckFailed, "NABT_TEST_SUMMARY_MISSING"):
            self.step("print('the tests were not executed')")

    def test_zero_test_summary_cannot_pass_even_beside_a_positive_suite(self):
        for summary in ("Ran 0 tests in 0.001s\\n\\nOK",
                        "Ran 3 tests in 0.001s\\nOK\\nRan 0 tests in 0.001s\\nOK"):
            with self.subTest(summary=summary), self.assertRaisesRegex(runner.CheckFailed, "NABT_ZERO_TEST_RUN"):
                self.step("print('" + summary + "')")

    def test_launch_failure_remains_in_the_manifest(self):
        with redirect_stdout(io.StringIO()), self.assertRaises(OSError):
            runner.run_step(self.report, self.output, "missing", [str(self.root / "no-executable")],
                            self.root, dict(os.environ))
        step = json.loads((self.output / "manifest.json").read_text())["steps"][0]
        self.assertEqual(step["status"], "FAILED")
        self.assertIn("No such file", step["error"])

    def test_unittest_counts_do_not_mistake_test_names_for_skips(self):
        text = "test_skips_all_analysis (Tests) ... ok\nRan 2 tests in 0.1s\nOK\nRan 3 tests in 0.2s\nOK\n"
        self.assertEqual(runner.test_counts(text), {"unittest_runs": [2, 3], "skipped": 0})

    def test_output_must_be_fresh_and_outside_snapshot(self):
        with self.assertRaises(FileExistsError):
            runner.output_directory(self.output)
        with patch.object(runner, "VENDOR", self.root / "vendor"):
            with self.assertRaisesRegex(runner.CheckFailed, "NABT_OUTPUT_INSIDE_SNAPSHOT"):
                runner.output_directory(self.root / "vendor/new")

    def test_make_paths_reject_shell_and_make_interpolation(self):
        for path in ("has space", "x;touch marker", "$(touch marker)", "x`id`", "x#recipe", "x\nnext"):
            with self.subTest(path=path), self.assertRaisesRegex(runner.CheckFailed, "NABT_UNSAFE_MAKE_PATH"):
                runner.safe_make_path(path)
        self.assertEqual(runner.safe_make_path("/tmp/safe-path.v1"), "/tmp/safe-path.v1")

    def test_temporary_cache_path_is_checked_before_entering_make_recipes(self):
        args = argparse.Namespace(lake="lake", qac=None, runtime_only=False)
        for cache in ("/tmp/with spaces/cache", "/tmp/$(touch injected)/cache"):
            with self.subTest(cache=cache), patch.object(runner.shutil, "which", return_value="/usr/bin/lake"), \
                    patch.object(runner.tempfile, "TemporaryDirectory") as temporary, \
                    patch.object(runner, "run_step", side_effect=AssertionError("unsafe cache reached a subprocess stage")) as steps:
                temporary.return_value.__enter__.return_value = cache
                with self.assertRaisesRegex(runner.CheckFailed, "NABT_UNSAFE_MAKE_PATH"):
                    runner.execute(args, self.output, self.report)
                steps.assert_not_called()

    def fake_pipeline(self, runtime_only=False, version="Lean (version 4.34.1, fixture)"):
        calls = []
        def fake_step(report, output, name, argv, cwd, env, *, tests=False):
            log = output / (name + ".log")
            if name.startswith("snapshot"):
                log.write_text(json.dumps({"status": "VERIFIED", "files": 3}))
            elif name == "lean-version":
                log.write_text(version)
            else:
                log.write_text("Ran 1 test in 0.01s\nOK\n")
            report["steps"].append({"name": name, "log": str(log), "status": "PASSED"})
            calls.append((name, argv, cwd, env, tests))
        args = argparse.Namespace(lake="lake", qac=None, runtime_only=runtime_only)
        with patch.object(runner, "ROOT", self.root), patch.object(runner, "VENDOR", self.root / "vendor"), \
                patch.object(runner.shutil, "which", return_value="/usr/bin/lake"), \
                patch.object(runner, "run_step", side_effect=fake_step):
            runner.execute(args, self.output, self.report)
        return calls

    def test_full_pipeline_builds_before_tests_and_runs_upstream_check_unchanged(self):
        with patch.dict(os.environ, {"MAKEFILES": "untrusted.mk", "MAKEFLAGS": "-n", "PYTHONOPTIMIZE": "1"}):
            calls = self.fake_pipeline()
        names = [call[0] for call in calls]
        self.assertLess(names.index("snapshot-before"), names.index("native-build"))
        self.assertLess(names.index("native-build"), names.index("upstream-build"))
        self.assertLess(names.index("upstream-build"), names.index("upstream-check"))
        self.assertEqual(names[-1], "snapshot-after")
        stage = next(call for call in calls if call[0] == "upstream-check")
        self.assertEqual(stage[1][-1], "check")
        self.assertIn("EVIDENCE_DIR=" + str(self.output / "evidence"), stage[1])
        self.assertNotIn("MAKEFILES", stage[3])
        self.assertNotIn("MAKEFLAGS", stage[3])
        self.assertNotIn("PYTHONOPTIMIZE", stage[3])
        self.assertTrue(stage[3]["NABT_RECURSIVE_BRIDGE_PROBE"].endswith("/recursiveBridgeProbe"))
        self.assertEqual(stage[3]["LEAN_NUM_THREADS"], "2")
        self.assertTrue(stage[4])

    def test_runtime_pipeline_builds_probe_prerequisites_but_omits_full_check(self):
        calls = self.fake_pipeline(runtime_only=True)
        names = [call[0] for call in calls]
        self.assertLess(names.index("upstream-build"), names.index("upstream-runtime"))
        self.assertNotIn("upstream-check", names)
        self.assertIn("upstream-integrity", names)
        for name in ("native-vendor", "native-cli", "native-bridge", "native-runner"):
            self.assertIn(name, names)

    def test_wrong_lean_version_stops_before_build(self):
        with self.assertRaisesRegex(runner.CheckFailed, "NABT_TOOLCHAIN_MISMATCH"):
            self.fake_pipeline(version="Lean (version 4.34.0, wrong fixture)")
        self.assertEqual([step["name"] for step in self.report["steps"]], ["snapshot-before", "lean-version"])

    def test_runtime_success_cannot_claim_full_parity(self):
        destination = self.root / "runtime-run"
        with patch.object(runner, "execute", return_value=None), redirect_stdout(io.StringIO()):
            code = runner.main(["--runtime-only", "--output", str(destination)])
        report = json.loads((destination / "manifest.json").read_text())
        self.assertEqual(code, 0)
        self.assertEqual(report["status"], "PASSED_RUNTIME_ONLY")
        self.assertFalse(report["full_parity"])
        self.assertEqual(report["formal_conformance"], "NOT_RUN")

    def test_failed_run_preserves_failure_and_never_marks_parity(self):
        destination = self.root / "failed-run"
        with patch.object(runner, "execute", side_effect=runner.CheckFailed("fixture build failed")), \
                redirect_stdout(io.StringIO()):
            code = runner.main(["--output", str(destination)])
        report = json.loads((destination / "manifest.json").read_text())
        self.assertEqual(code, 1)
        self.assertEqual(report["status"], "FAILED")
        self.assertFalse(report["full_parity"])
        self.assertIn("fixture build failed", report["error"])

    def test_generated_unmeasured_result_is_preserved(self):
        evidence = self.output / "evidence"
        evidence.mkdir()
        (evidence / "measurement.json").write_text(json.dumps({
            "status": "UNMEASURED", "gate_pass": True, "strict_pass": False,
            "unmeasured": 4, "scope": "authored fixture only",
        }))
        summary = runner.generated_reports(self.output)[0]["reported_summary"]
        self.assertEqual(summary["status"], "UNMEASURED")
        self.assertEqual(summary["unmeasured"], 4)
        self.assertFalse(summary["strict_pass"])


if __name__ == "__main__":
    unittest.main()
