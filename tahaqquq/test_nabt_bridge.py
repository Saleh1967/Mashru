"""Independent finite expectations for the compiled native Mashru/NABT bridge.

Build with `lake build nabtBridge`, then run this file with Python. The configured
gate must build first. This test executes that Lean binary; it accepts neither a
saved JSON report nor a Python implementation as a substitute. Missing execution
is an explicit failure, never a skip.

The two alphabet spellings and rank matrices below are authored expectations.
The cell oracle uses spelling lookup and the four-state positional arithmetic;
it does not import the production conversion table. The source case uses declared
cell positions, not inferred UTF-8 offsets. Conditional licenses in these finite
cases do not establish Arabic acquisition or external-world correspondence.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import itertools
import json
import os
from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
EXECUTABLE = ROOT / ".lake" / "build" / "bin" / "nabtBridge"

# The native articulation ordering and the pinned NABT alphabetical ordering.
MASHRU_CARRIERS = tuple("ءهاعحغخقكجشيضلنرطدتزسصظذثفبمو")
NABT_CARRIERS = tuple("ابتثجحخدذرزسشصضطظعغفقكلمنهويء")

# Rows are requested ranks 0..6, columns evidence ranks 0..6. L=LICENSED,
# D=DEFER. The experimental method's maximum admitted label is maqis (2).
RANK_EXPECTATIONS = {
    "aqliyya": (
        "LLLLLLL", "DLLLLLL", "DDLLLLL", "DDDLLLL",
        "DDDDLLL", "DDDDDLL", "DDDDDDL",
    ),
    "ilmiyya": (
        "LLLLLLL", "DLLLLLL", "DDLLLLL", "DDDDDDD",
        "DDDDDDD", "DDDDDDD", "DDDDDDD",
    ),
}
METHOD_EVIDENCE_RANKS = {
    "aqliyya": (0, 1, 2, 3, 4, 5, 6),
    "ilmiyya": (0, 1, 2, 2, 2, 2, 2),
}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate export key: " + key)
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError("Non-JSON constant in bridge export: " + value)


class NativeNabtBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not EXECUTABLE.is_file() or not os.access(EXECUTABLE, os.X_OK):
            raise AssertionError(
                "NABT_BRIDGE_UNAVAILABLE: run lake build nabtBridge before "
                "python3 -I tahaqquq/test_nabt_bridge.py; no stored-report fallback is allowed"
            )
        before = sha256(EXECUTABLE.read_bytes()).hexdigest()
        cls.execution = subprocess.run([str(EXECUTABLE)], cwd=ROOT,
                                       capture_output=True, timeout=60)
        if cls.execution.returncode != 0 or cls.execution.stderr:
            raise AssertionError(
                "NABT_BRIDGE_EXECUTION_FAILED: exit=" + str(cls.execution.returncode)
                + "; stderr=" + cls.execution.stderr.decode("utf-8", errors="replace")
            )
        if not cls.execution.stdout or len(cls.execution.stdout) > 256 * 1024:
            raise AssertionError("NABT_BRIDGE_INVALID_EXPORT_SIZE")
        cls.report = json.loads(cls.execution.stdout, object_pairs_hook=unique_object,
                                parse_constant=reject_constant)
        after = sha256(EXECUTABLE.read_bytes()).hexdigest()
        if before != after:
            raise AssertionError("NABT_BRIDGE_CHANGED_DURING_EXECUTION")

    def test_export_schema_and_scope(self):
        self.assertEqual(set(self.report), {
            "schema_version", "bridge_id", "scope", "cell_count", "cells",
            "source", "native_cases", "inquiry_cases", "inquiry_case_count",
            "empty_world_registry",
        })
        self.assertIs(type(self.report["schema_version"]), int)
        self.assertEqual(self.report["schema_version"], 1)
        self.assertEqual(self.report["bridge_id"], "mashru.nabt.bridge.v1")
        self.assertEqual(self.report["scope"], "declared_cell_representation_and_conditional_evidence")

    def test_all_116_cells_match_the_independent_spelling_oracle(self):
        self.assertEqual(len(MASHRU_CARRIERS), 29)
        self.assertEqual(len(NABT_CARRIERS), 29)
        self.assertEqual(set(MASHRU_CARRIERS), set(NABT_CARRIERS))
        rows = self.report["cells"]
        self.assertIs(type(self.report["cell_count"]), int)
        self.assertEqual(self.report["cell_count"], 116)
        self.assertEqual(len(rows), 116)
        expected = []
        for native_index, carrier in enumerate(MASHRU_CARRIERS):
            canonical_index = NABT_CARRIERS.index(carrier)
            for mark in range(4):
                native_atom = 4 * native_index + mark
                canonical_atom = 4 * canonical_index + mark
                expected.append({
                    "mashru_atom": native_atom, "mashru_carrier_index": native_index,
                    "mark": mark, "carrier": carrier,
                    "nabt_atom": canonical_atom, "nabt_carrier_index": canonical_index,
                    "nabt_carrier": carrier, "roundtrip_mashru_atom": native_atom,
                    "roundtrip_nabt_atom": canonical_atom,
                })
        for row in rows:
            for field in ("mashru_atom", "mashru_carrier_index", "mark", "nabt_atom",
                          "nabt_carrier_index", "roundtrip_mashru_atom", "roundtrip_nabt_atom"):
                self.assertIs(type(row[field]), int, (field, row))
        self.assertEqual(rows, expected)
        self.assertEqual({row["nabt_atom"] for row in rows}, set(range(116)))
        self.assertEqual(rows[32]["carrier"], "ك")
        self.assertEqual(rows[32]["nabt_atom"], 84)
        self.assertNotEqual(rows[32]["mashru_atom"], rows[32]["nabt_atom"])

    def test_source_identity_and_declared_cell_span_are_preserved(self):
        source = self.report["source"]
        self.assertEqual(source, {
            "source_id": 17, "revision": 1, "scope_id": 2, "atomization_id": 3,
            "coordinate_unit": "declared_cell",
            "native_atoms": [32, 72, 104], "canonical_atoms": [84, 8, 4],
            "restored_native_atoms": [32, 72, 104],
            "span_start": 1, "span_stop": 3,
            "native_span_valid": True, "canonical_span_valid": True,
            "native_span_atoms": [72, 104], "canonical_span_atoms": [8, 4],
        })
        for field in ("source_id", "revision", "scope_id", "atomization_id", "span_start", "span_stop"):
            self.assertIs(type(source[field]), int)
        for field in ("native_atoms", "canonical_atoms", "restored_native_atoms",
                      "native_span_atoms", "canonical_span_atoms"):
            self.assertTrue(all(type(atom) is int for atom in source[field]))
        self.assertIs(source["native_span_valid"], True)
        self.assertIs(source["canonical_span_valid"], True)

    def test_native_composition_cannot_invent_evidence_adjacency_or_source_membership(self):
        rows = self.report["native_cases"]
        self.assertEqual(rows, [
            {"name": "source_atom", "status": "CONDITIONAL_LICENSED", "conflict": False},
            {"name": "join_without_evidence", "status": "PENDING", "conflict": False},
            {"name": "filtered_source_gap", "status": "INVALID", "conflict": False},
            {"name": "same_ids_changed_content", "status": "INVALID", "conflict": False},
        ])
        for row in rows:
            self.assertIs(row["conflict"], False)

    def test_all_98_inquiry_rows_obey_native_method_and_label_limits(self):
        rows = self.report["inquiry_cases"]
        self.assertIs(type(self.report["inquiry_case_count"]), int)
        self.assertEqual(self.report["inquiry_case_count"], 98)
        self.assertEqual(len(rows), 98)
        expected_domain = set(itertools.product(("aqliyya", "ilmiyya"), range(7), range(7)))
        seen = set()
        for row in rows:
            self.assertEqual(set(row), {"method", "requested_rank", "evidence_rank",
                                        "method_evidence_rank", "verdict", "authorized_rank"})
            for field in ("requested_rank", "evidence_rank", "method_evidence_rank", "authorized_rank"):
                self.assertIs(type(row[field]), int)
            key = row["method"], row["requested_rank"], row["evidence_rank"]
            self.assertIn(key, expected_domain)
            self.assertNotIn(key, seen)
            seen.add(key)
            method, requested, evidence = key
            expected_verdict = {"L": "LICENSED", "D": "DEFER"}[
                RANK_EXPECTATIONS[method][requested][evidence]]
            self.assertEqual(row["method_evidence_rank"], METHOD_EVIDENCE_RANKS[method][evidence], key)
            self.assertEqual(row["verdict"], expected_verdict, key)
            self.assertEqual(row["authorized_rank"], requested if expected_verdict == "LICENSED" else 0, key)
        self.assertEqual(seen, expected_domain)
        self.assertEqual(Counter(row["verdict"] for row in rows), {"LICENSED": 46, "DEFER": 52})

    def test_conditional_inquiry_does_not_create_a_sealed_world_witness(self):
        result = self.report["empty_world_registry"]
        self.assertEqual(result, {
            "inquiry_verdict": "LICENSED", "meaning_status": "معلومة",
            "sealed_world_witness_added": False,
        })
        self.assertIs(result["sealed_world_witness_added"], False)

    def test_export_is_recomputed_by_the_executable_and_rejects_arguments(self):
        repeated = subprocess.run([str(EXECUTABLE)], cwd=ROOT,
                                  capture_output=True, timeout=60)
        self.assertEqual(repeated.returncode, 0, repeated.stderr)
        self.assertEqual(repeated.stdout, self.execution.stdout)
        self.assertEqual(repeated.stderr, b"")
        invalid = subprocess.run([str(EXECUTABLE), "--report", "invented.json"], cwd=ROOT,
                                 capture_output=True, timeout=60)
        self.assertEqual(invalid.returncode, 2)
        self.assertEqual(invalid.stdout, b"")
        self.assertIn(b"Usage: nabtBridge", invalid.stderr)


if __name__ == "__main__":
    unittest.main()
