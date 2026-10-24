"""Adversarial fixture tests for the pinned NABT source boundary.

The fixture is authored here, independently of the production snapshot. Only
these tests inject its digest into the checker's private engine. Production
CLI callers cannot choose a lock, checkout root, upstream revision or digest.
"""

from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
from copy import deepcopy
from hashlib import sha1, sha256
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/check_nabt_vendor.py"
SPEC = importlib.util.spec_from_file_location("mashru_nabt_snapshot_checker", SCRIPT)
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class SnapshotFixtureTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.vendor = self.root / "integrations/nabt"
        self.lock = self.root / "integrations/nabt.lock.json"
        self.contents = {
            "LICENSE": b"Independent test fixture; no upstream authority.\n",
            "src/nabt/__init__.py": b"fixture = 1\n",
            "tools/show.py": b"#!/usr/bin/env python3\nprint('fixture')\n",
        }
        rows = []
        for name, content in self.contents.items():
            target = self.vendor / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
            executable = name == "tools/show.py"
            target.chmod(0o755 if executable else 0o644)
            rows.append({
                "path": name, "size": len(content), "sha256": sha256(content).hexdigest(),
                "git_blob_sha": sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest(),
                "mode": "100755" if executable else "100644",
            })
        self.document = {
            "schema": "mashru.nabt.snapshot.v1",
            "upstream": {
                "repository": "sonaiso/NABT",
                "commit": "f0064f0a4baab3cc816087a322aabc0c8fbb2d19",
                "tree": "63453db8c545403b22c137307bda64c9ac5656d9",
            },
            "selection": {"purpose": "independently authored test fixture"},
            "files": rows,
        }
        self.pin = self.write_lock(self.document)

    def write_lock(self, document):
        raw = json.dumps(document, ensure_ascii=False, sort_keys=True).encode("utf-8")
        self.lock.write_bytes(raw)
        self.lock.chmod(0o644)
        return sha256(raw).hexdigest()

    def verify(self, pin=None):
        return checker._verify_snapshot(self.root, self.pin if pin is None else pin)

    def rejected(self, code, pin=None):
        with self.assertRaises(checker.SnapshotError) as caught:
            self.verify(pin)
        self.assertEqual(caught.exception.code, code)
        self.assertEqual(caught.exception.report()["status"], "DEFER")
        return caught.exception

    def test_exact_independent_fixture_is_verified(self):
        result = self.verify()
        self.assertEqual(result["status"], "VERIFIED")
        self.assertEqual(result["files"], 3)
        self.assertEqual(result["bytes"], sum(map(len, self.contents.values())))
        self.assertEqual(result["lock_sha256"], self.pin)

    def test_equal_size_byte_change_is_rejected(self):
        (self.vendor / "src/nabt/__init__.py").write_bytes(b"fixture = 2\n")
        self.assertEqual(self.rejected("NABT_SNAPSHOT_DIGEST").path, "src/nabt/__init__.py")

    def test_size_change_is_rejected(self):
        (self.vendor / "LICENSE").write_bytes(b"truncated")
        self.rejected("NABT_SNAPSHOT_SIZE")

    def test_missing_declared_file_is_rejected(self):
        (self.vendor / "LICENSE").unlink()
        self.assertEqual(self.rejected("NABT_SNAPSHOT_MISSING").path, "LICENSE")

    def test_added_python_file_is_rejected(self):
        (self.vendor / "src/nabt/injected.py").write_text("raise RuntimeError('extra')\n")
        self.assertEqual(self.rejected("NABT_SNAPSHOT_EXTRA").path, "src/nabt/injected.py")

    def test_mode_change_is_rejected(self):
        (self.vendor / "tools/show.py").chmod(0o644)
        self.rejected("NABT_SNAPSHOT_MODE")

    def test_file_link_is_rejected_even_with_identical_bytes(self):
        target = self.vendor / "LICENSE"
        outside = self.root / "same-bytes"
        outside.write_bytes(target.read_bytes())
        target.unlink()
        target.symlink_to(outside)
        self.rejected("NABT_SNAPSHOT_SYMLINK")

    def test_linked_parent_is_rejected_even_with_identical_tree(self):
        target = self.vendor / "src"
        outside = self.root / "same-tree"
        target.rename(outside)
        target.symlink_to(outside, target_is_directory=True)
        self.rejected("NABT_SNAPSHOT_SYMLINK")

    def test_linked_vendor_root_is_rejected(self):
        outside = self.root / "same-snapshot"
        self.vendor.rename(outside)
        self.vendor.symlink_to(outside, target_is_directory=True)
        self.rejected("NABT_SNAPSHOT_SYMLINK")

    def test_linked_integration_parent_and_lock_are_rejected(self):
        for target_name in ("integrations/nabt.lock.json", "integrations"):
            with self.subTest(path=target_name):
                target = self.root / target_name
                backup = self.root / "saved"
                target.rename(backup)
                target.symlink_to(backup, target_is_directory=backup.is_dir())
                self.rejected("NABT_SNAPSHOT_SYMLINK")
                target.unlink()
                backup.rename(target)

    def test_changed_lock_cannot_reauthorize_changed_source(self):
        content = b"fixture = 2\n"
        (self.vendor / "src/nabt/__init__.py").write_bytes(content)
        changed = deepcopy(self.document)
        row = next(row for row in changed["files"] if row["path"] == "src/nabt/__init__.py")
        row.update(sha256=sha256(content).hexdigest(),
                   git_blob_sha=sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest())
        self.write_lock(changed)
        self.rejected("NABT_LOCK_DIGEST_MISMATCH")

    def test_duplicate_json_key_is_rejected_after_digest_binding(self):
        raw = self.lock.read_bytes().replace(b'"schema":', b'"schema":"fake","schema":', 1)
        self.lock.write_bytes(raw)
        self.rejected("NABT_LOCK_DUPLICATE_KEY", sha256(raw).hexdigest())

    def test_duplicate_inventory_path_is_rejected(self):
        changed = deepcopy(self.document)
        changed["files"].append(deepcopy(changed["files"][0]))
        self.rejected("NABT_LOCK_DUPLICATE_PATH", self.write_lock(changed))

    def test_traversal_absolute_and_noncanonical_paths_are_rejected(self):
        for name in ("../outside", "src/../../outside", "/tmp/outside", "./LICENSE", "src//x",
                     "src/./x", "C:/outside", "C:\\outside", "src\\x", "", "src/\nx"):
            with self.subTest(path=name):
                changed = deepcopy(self.document)
                changed["files"][0]["path"] = name
                self.rejected("NABT_LOCK_PATH", self.write_lock(changed))

    def test_wrong_repository_commit_and_tree_are_rejected(self):
        for key, value in (("repository", "unrelated/NABT"), ("commit", "0" * 40), ("tree", "0" * 40)):
            with self.subTest(field=key):
                changed = deepcopy(self.document)
                changed["upstream"][key] = value
                self.rejected("NABT_LOCK_UPSTREAM", self.write_lock(changed))

    def test_file_metadata_is_strictly_typed(self):
        for key, value in (("size", True), ("size", 1.0), ("size", -1), ("size", "1"),
                           ("sha256", "A" * 64), ("git_blob_sha", "0" * 39),
                           ("mode", 100644), ("mode", "120000")):
            with self.subTest(field=key, value=value):
                changed = deepcopy(self.document)
                changed["files"][0][key] = value
                self.rejected("NABT_LOCK_FILE_SCHEMA", self.write_lock(changed))

    def test_git_blob_identity_is_verified_independently_of_sha256(self):
        changed = deepcopy(self.document)
        changed["files"][0]["git_blob_sha"] = "0" * 40
        self.rejected("NABT_SNAPSHOT_GIT_BLOB", self.write_lock(changed))

    def test_only_documented_generated_paths_are_excluded(self):
        generated = ("formal/.lake/build/bin/probe", "src/nabt/__pycache__/cached.pyc",
                     "tools/old.pyc", "artifacts/local/run/report.json")
        for name in generated:
            target = self.vendor / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(b"generated output is not source evidence")
        self.assertEqual(self.verify()["files"], 3)
        (self.vendor / "artifacts/undeclared.json").write_text("{}")
        self.rejected("NABT_SNAPSHOT_EXTRA")

    def test_similar_names_are_not_ignored(self):
        for name in ("formal/.lake-suffix/source.py", "src/nabt/__pycache__x/source.py",
                     "artifacts/locality/source.py", "tools/old.pycx", "tools/empty.pyc/source.py"):
            with self.subTest(path=name):
                target = self.vendor / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("extra")
                self.rejected("NABT_SNAPSHOT_EXTRA")
                target.unlink()

    def test_generated_path_cannot_hide_a_link(self):
        outside = self.root / "cache"
        outside.mkdir()
        (self.vendor / "__pycache__").symlink_to(outside, target_is_directory=True)
        self.rejected("NABT_SNAPSHOT_SYMLINK")

    def test_declared_generated_file_is_rejected(self):
        changed = deepcopy(self.document)
        changed["files"][0]["path"] = "formal/.lake/source.py"
        self.rejected("NABT_LOCK_GENERATED_PATH", self.write_lock(changed))

    def test_empty_and_malformed_inventory_is_rejected(self):
        for value in ([], {}, None, True):
            with self.subTest(value=value):
                changed = deepcopy(self.document)
                changed["files"] = value
                self.rejected("NABT_LOCK_FILES", self.write_lock(changed))

    def test_extra_manifest_fields_and_unknown_schema_are_rejected(self):
        for mutation in (lambda doc: doc.update(approved=True),
                         lambda doc: doc.update(schema="uninstalled.snapshot.v1"),
                         lambda doc: doc.update(selection=[])):
            changed = deepcopy(self.document)
            mutation(changed)
            self.rejected("NABT_LOCK_SCHEMA", self.write_lock(changed))

    def test_non_json_constants_and_invalid_utf8_are_named(self):
        for raw in (b'{"x":NaN}', b'\xff', b'{"unterminated":'):
            with self.subTest(raw=raw):
                self.lock.write_bytes(raw)
                self.rejected("NABT_LOCK_JSON", sha256(raw).hexdigest())

    def test_cli_success_is_json_and_quiet_success_is_silent(self):
        for arguments in ([], ["--quiet"]):
            with self.subTest(arguments=arguments):
                stdout, stderr = io.StringIO(), io.StringIO()
                with patch.object(checker, "ROOT", self.root), patch.object(checker, "EXPECTED_LOCK_SHA256", self.pin):
                    with redirect_stdout(stdout), redirect_stderr(stderr):
                        status = checker.main(arguments)
                self.assertEqual(status, 0)
                self.assertEqual(stderr.getvalue(), "")
                if arguments:
                    self.assertEqual(stdout.getvalue(), "")
                else:
                    self.assertEqual(json.loads(stdout.getvalue())["status"], "VERIFIED")

    def test_cli_failure_is_named_json_even_when_quiet(self):
        (self.vendor / "LICENSE").unlink()
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch.object(checker, "ROOT", self.root), patch.object(checker, "EXPECTED_LOCK_SHA256", self.pin):
            with redirect_stdout(stdout), redirect_stderr(stderr):
                status = checker.main(["--quiet"])
        self.assertEqual(status, 3)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(json.loads(stderr.getvalue())["code"], "NABT_SNAPSHOT_MISSING")

    def test_cli_has_no_root_manifest_or_digest_override(self):
        for option in ("--root", "--manifest", "--expected-digest"):
            with self.subTest(option=option):
                result = subprocess.run([sys.executable, "-I", "-B", str(SCRIPT), option, "caller-value"],
                                        capture_output=True, text=True, timeout=15)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn("unrecognized arguments", result.stderr)


if __name__ == "__main__":
    unittest.main()
