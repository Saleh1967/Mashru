"""اختبارات خطّ الأساس: رفض التلف دون إسقاط الحدّ أو تعطيل التقرير.

التشغيل: python3 -I tahaqquq/test_bawwaba.py
"""
import contextlib
import io
import os
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bawwaba


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
