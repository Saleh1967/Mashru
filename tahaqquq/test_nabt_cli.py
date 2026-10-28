"""Executable boundary tests for Mashru's pinned NABT entry point.

These cases test transport, isolation, missing inputs and retained evidence
limits. They are authored interface tests, not Arabic acquisition measurements.
The small launcher fixtures test failure propagation without modifying the
installed snapshot. Real requests below execute the pinned implementation.
"""

from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
import marshal
import os
from pathlib import Path
import shutil
import subprocess
import struct
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / "scripts" / "nabt.py"
VENDOR = ROOT / "integrations" / "nabt"


def invoke(*arguments, cwd=None, env=None, entry=ENTRY):
    return subprocess.run([sys.executable, "-I", str(entry), *map(str, arguments)],
                          cwd=cwd, env=env, capture_output=True, text=True,
                          encoding="utf-8", timeout=45)


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")


class LauncherBoundaryTests(unittest.TestCase):
    def fixture(self, directory, *, checker="raise SystemExit(0)\n", body="raise SystemExit(0)\n"):
        root = Path(directory)
        (root / "scripts").mkdir()
        entry = root / "scripts/nabt.py"
        shutil.copyfile(ENTRY, entry)
        (root / "scripts/check_nabt_vendor.py").write_text(checker, encoding="utf-8")
        package = root / "integrations/nabt/src/nabt"
        package.mkdir(parents=True)
        (package / "__init__.py").write_text("", encoding="utf-8")
        (package / "__main__.py").write_text(body, encoding="utf-8")
        return entry

    def test_help_is_available_without_running_the_snapshot(self):
        result = invoke("--help")
        self.assertEqual(result.returncode, 0, result.stderr)
        for command in ("runtime", "recursive", "classical", "inquiry-conformance", "classical-conformance"):
            self.assertIn(command, result.stdout)

    def test_unknown_entry_is_rejected(self):
        result = invoke("not-an-entry")
        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid choice", result.stderr)

    def test_missing_checker_and_missing_tool_are_named_deferrals(self):
        with tempfile.TemporaryDirectory() as directory:
            entry = self.fixture(directory)
            tool = invoke("classical", "audit", entry=entry)
            self.assertEqual(tool.returncode, 3)
            self.assertEqual(json.loads(tool.stderr)["code"], "NABT_ENTRY_UNAVAILABLE")
            (Path(directory) / "scripts/check_nabt_vendor.py").unlink()
            checker = invoke("runtime", "--version", entry=entry)
            self.assertEqual(checker.returncode, 3)
            self.assertEqual(json.loads(checker.stderr)["code"], "NABT_CHECKER_UNAVAILABLE")

    def test_failed_integrity_check_blocks_execution(self):
        with tempfile.TemporaryDirectory() as directory:
            marker = Path(directory) / "executed"
            entry = self.fixture(
                directory,
                checker="import sys\nprint('snapshot damaged', file=sys.stderr)\nraise SystemExit(7)\n",
                body="from pathlib import Path\nPath('executed').write_text('bad')\n",
            )
            result = invoke("runtime", entry=entry, cwd=directory)
            self.assertEqual(result.returncode, 7)
            self.assertEqual(result.stdout, "")
            self.assertEqual(result.stderr, "snapshot damaged\n")
            self.assertFalse(marker.exists())

    def test_child_streams_status_and_literal_arguments_are_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            entry = self.fixture(directory, body=(
                "import json, sys\n"
                "print(json.dumps(sys.argv[1:]))\n"
                "print('child diagnostic', file=sys.stderr)\n"
                "raise SystemExit(6)\n"
            ))
            literal = "x; touch should-not-exist $(touch also-not-created)"
            result = invoke("runtime", literal, entry=entry, cwd=directory)
            self.assertEqual(result.returncode, 6)
            self.assertEqual(json.loads(result.stdout), [literal])
            self.assertEqual(result.stderr, "child diagnostic\n")
            self.assertFalse((Path(directory) / "should-not-exist").exists())
            self.assertFalse((Path(directory) / "also-not-created").exists())

    def test_valid_unchecked_bytecode_is_not_executed(self):
        with tempfile.TemporaryDirectory() as directory:
            entry = self.fixture(directory, body="from nabt.payload import value\nprint(value)\n")
            source = Path(directory) / "integrations/nabt/src"
            payload = source / "nabt/payload.py"
            payload.write_text("value = 'PINNED_SOURCE'\n", encoding="utf-8")
            metadata = payload.stat()
            cache = payload.parent / "__pycache__" / ("payload." + sys.implementation.cache_tag + ".pyc")
            cache.parent.mkdir()
            # This deliberately valid timestamp/size header makes Python accept
            # code unrelated to the source bytes. -B disables writes, not reads.
            header = struct.pack("<4sIII", importlib.util.MAGIC_NUMBER, 0,
                                 int(metadata.st_mtime) & 0xFFFFFFFF, metadata.st_size)
            malicious = compile("value = 'UNCHECKED_BYTECODE'\n", str(payload), "exec")
            cache.write_bytes(header + marshal.dumps(malicious))
            control = subprocess.run(
                [sys.executable, "-I", "-B", "-c",
                 "import sys; sys.path.insert(0, sys.argv[1]); from nabt.payload import value; print(value)",
                 str(source)], capture_output=True, text=True, timeout=15,
            )
            self.assertEqual(control.returncode, 0, control.stderr)
            self.assertEqual(control.stdout, "UNCHECKED_BYTECODE\n")
            protected = invoke("runtime", entry=entry, cwd=directory)
            self.assertEqual(protected.returncode, 0, protected.stderr)
            self.assertEqual(protected.stdout, "PINNED_SOURCE\n")
            self.assertEqual(protected.stderr, "")


    def test_sourceless_module_cannot_shadow_the_standard_library(self):
        # A sourceless dataclasses.pyc beside the package shadowed the standard
        # module before the import guard (2026-10-28). The fixture checker passes,
        # so only the guard stands between the planted bytecode and execution.
        with tempfile.TemporaryDirectory() as directory:
            entry = self.fixture(directory, body="import dataclasses\nprint('IMPORTED')\n")
            planted = Path(directory) / "integrations/nabt/src/dataclasses.pyc"
            header = struct.pack("<4sIII", importlib.util.MAGIC_NUMBER, 0, 0, 0)
            planted.write_bytes(header + marshal.dumps(compile("print('SHADOWED')", "x", "exec")))
            result = invoke("runtime", entry=entry, cwd=directory)
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn("SHADOWED", result.stdout + result.stderr)
            self.assertIn("NABT_SOURCELESS_MODULE: dataclasses", result.stderr)

    def test_module_outside_snapshot_and_stdlib_is_refused(self):
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            (Path(outside) / "unpinned_dependency.py").write_text("print('UNPINNED')\n", encoding="utf-8")
            entry = self.fixture(directory, body=(
                "import sys\nsys.path.append(sys.argv[1])\nimport unpinned_dependency\n"))
            result = invoke("runtime", outside, entry=entry, cwd=directory)
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn("UNPINNED", result.stdout)
            self.assertIn("NABT_MODULE_ORIGIN: unpinned_dependency", result.stderr)

    def test_standard_library_and_snapshot_imports_still_run(self):
        with tempfile.TemporaryDirectory() as directory:
            entry = self.fixture(directory, body=(
                "import dataclasses, json, unicodedata\nimport nabt\nprint(json.dumps('OK'))\n"))
            result = invoke("runtime", entry=entry, cwd=directory)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, '"OK"\n')


    def runner(self, entry):
        spec = importlib.util.spec_from_file_location("fixture_nabt_runner", entry)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_run_pinned_refuses_a_rejected_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            entry = self.fixture(directory, checker="import sys\nprint('damaged', file=sys.stderr)\nraise SystemExit(3)\n")
            with self.assertRaises(RuntimeError) as caught:
                self.runner(entry).run_pinned("print('RAN')", [])
            self.assertIn("NABT_SNAPSHOT_REJECTED: damaged", str(caught.exception))

    def test_run_pinned_reads_checked_source_not_valid_cached_bytecode(self):
        with tempfile.TemporaryDirectory() as directory:
            entry = self.fixture(directory)
            payload = Path(directory) / "integrations/nabt/src/nabt/payload.py"
            payload.write_text("value = 'PINNED_SOURCE'\n", encoding="utf-8")
            metadata = payload.stat()
            cache = payload.parent / "__pycache__" / ("payload." + sys.implementation.cache_tag + ".pyc")
            cache.parent.mkdir()
            header = struct.pack("<4sIII", importlib.util.MAGIC_NUMBER, 0,
                                 int(metadata.st_mtime) & 0xFFFFFFFF, metadata.st_size)
            cache.write_bytes(header + marshal.dumps(compile("value = 'UNCHECKED_BYTECODE'\n", str(payload), "exec")))
            result = self.runner(entry).run_pinned("from nabt.payload import value\nprint(value)", [])
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "PINNED_SOURCE\n")

    def test_run_pinned_applies_the_import_guard(self):
        with tempfile.TemporaryDirectory() as directory:
            entry = self.fixture(directory)
            planted = Path(directory) / "integrations/nabt/src/dataclasses.pyc"
            header = struct.pack("<4sIII", importlib.util.MAGIC_NUMBER, 0, 0, 0)
            planted.write_bytes(header + marshal.dumps(compile("print('SHADOWED')", "x", "exec")))
            result = self.runner(entry).run_pinned("import dataclasses\nprint('IMPORTED')", [])
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn("SHADOWED", result.stdout + result.stderr)
            self.assertIn("NABT_SOURCELESS_MODULE: dataclasses", result.stderr)


class PinnedNabtIntegrationTests(unittest.TestCase):
    def test_runtime_uses_pinned_source_from_another_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fake = root / "nabt"
            fake.mkdir()
            (fake / "__init__.py").write_text("raise RuntimeError('wrong import')\n")
            (fake / "__main__.py").write_text("print('untrusted package')\n")
            (root / "sitecustomize.py").write_text("raise RuntimeError('wrong site')\n")
            env = dict(os.environ, PYTHONPATH=directory)
            result = invoke("runtime", "--version", cwd=directory, env=env)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "0.16.0a1\n")
            self.assertEqual(result.stderr, "")

    def test_runtime_missing_source_retains_upstream_deferral(self):
        with tempfile.TemporaryDirectory() as directory:
            result = invoke("runtime", "read-derivation", "absent.txt", cwd=directory)
            self.assertEqual(result.returncode, 3, result.stderr)
            self.assertEqual(result.stdout, "")
            report = json.loads(result.stderr)
            self.assertEqual((report["status"], report["code"]), ("DEFER", "IO_ERROR"))

    def test_recursive_relative_paths_and_changed_source_replay(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source ; literal.txt"
            text = "كَتَبَ"
            source.write_text(text, encoding="utf-8")
            read = invoke("recursive", "read", source.name, "--source-id", "mashru_case", cwd=directory)
            self.assertEqual(read.returncode, 0, read.stderr or read.stdout[:2000])
            report = json.loads(read.stdout)
            self.assertEqual(report["source"]["raw_text"], text)
            self.assertEqual(report["source"]["source_id"], "mashru_case")
            self.assertFalse(report["grammar_certified"])
            self.assertFalse(report["acquisition_measured"])
            self.assertFalse(report["lexical_root_from_shape"])
            write_json(root / "report.json", report)
            verified = invoke("recursive", "verify", source.name, "--report", "report.json",
                              "--source-id", "mashru_case", cwd=directory)
            self.assertEqual(verified.returncode, 0, verified.stderr)
            self.assertTrue(json.loads(verified.stdout)["valid"])
            source.write_text("كَتَبَ ", encoding="utf-8")
            rejected = invoke("recursive", "verify", source.name, "--report", "report.json",
                              "--source-id", "mashru_case", cwd=directory)
            self.assertEqual(rejected.returncode, 2, rejected.stderr)
            self.assertEqual(json.loads(rejected.stdout)["code"], "RECURSIVE_SOURCE_REPLAY_MISMATCH")

    def test_classical_unknown_condition_stays_deferred(self):
        with tempfile.TemporaryDirectory() as directory:
            request = Path(directory) / "request.json"
            write_json(request, {
                "version": "nabt.classical-language-evidence.v1",
                "record_id": "qatr_inna_conditions", "claim_kind": "GRAMMAR_APPLICATION",
                "candidate": {"law_id": "qatr-inna-v1",
                              "inputs": {"operator": "inna", "form": "full", "ma": "unknown"},
                              "expected": {"options": []}, "target_text": "إنما زيد قائم"},
            })
            result = invoke("classical", "assess", request.name, cwd=directory)
            self.assertEqual(result.returncode, 3, result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(report["status"], "DEFER")
            self.assertTrue(report["source_attested"])
            self.assertEqual(report["actual"], {"options": []})
            self.assertIn("READING_OUTSIDE_FORMALIZED_RULE_SCOPE", report["residuals"])
            self.assertFalse(report["application_established"])
            self.assertFalse(report["external_event_established"])

    def test_inquiry_replay_does_not_certify_world_truth(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scope = {"domain": "mashru-cli-test", "referent": "record-1",
                     "time": "snapshot-1", "unit": "exact-text"}
            plan = {
                "version": "nabt.rational-inquiry.v1",
                "claim": {"claim_id": "literal-claim", "kind": "TEXT_CORRESPONDENCE",
                          "candidate": "سجل واحد", "scope": scope,
                          "origin_sources": [{"source_id": "proposal", "revision": 1}]},
                "formation": {"purpose": "فحص نقل النص", "interpretation": "النص وحده",
                              "inference": "مطابقة حرفية", "prior": []},
                "review": {"depth": "DEEP", "context": [], "conditions": [],
                           "alternatives": [{"alternative_id": "two", "candidate": "سجلان"}],
                           "limitations": ["لا رصد للواقع"], "unresolved": []},
                "requested_rank": 2,
            }
            sources = [
                {"source_id": "proposal", "revision": 1, "scope": deepcopy(scope),
                 "content": "ادعاء للفحص", "origin": "proposal-A", "parents": [],
                 "role": "MATERIAL", "active": True},
                {"source_id": "reference", "revision": 1, "scope": deepcopy(scope),
                 "content": "سجل واحد", "origin": "reference-B", "parents": [],
                 "role": "REFERENCE", "active": True},
            ]
            write_json(root / "plan.json", plan)
            write_json(root / "sources.json", sources)
            result = invoke("runtime", "inquire", "plan.json", "--sources", "sources.json", cwd=directory)
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(report["status"], "LICENSED")
            self.assertFalse(report["external_truth_certified"])
            self.assertEqual(report["world_truth"], "NOT_ESTABLISHED")
            write_json(root / "report.json", report)
            replay = invoke("runtime", "verify-inquiry", "report.json", "--plan", "plan.json",
                            "--sources", "sources.json", cwd=directory)
            self.assertEqual(replay.returncode, 0, replay.stderr)
            self.assertTrue(json.loads(replay.stdout)["valid"])
            sources[1]["content"] = "سجلان"
            write_json(root / "sources.json", sources)
            stale = invoke("runtime", "verify-inquiry", "report.json", "--plan", "plan.json",
                           "--sources", "sources.json", cwd=directory)
            self.assertEqual(stale.returncode, 2, stale.stderr)
            self.assertEqual(json.loads(stale.stdout)["reason"], "STALE_OR_FORGED_INQUIRY")

    def test_conformance_commands_forward_help_without_installing_lean(self):
        for command in ("inquiry-conformance", "classical-conformance"):
            with self.subTest(command=command):
                result = invoke(command, "--help")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("--lake", result.stdout)


if __name__ == "__main__":
    unittest.main()
