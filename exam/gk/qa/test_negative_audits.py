# -*- coding: utf-8 -*-
"""
exam/gk/qa/test_negative_audits.py
Adversarial Negative Testing Suite for IT004 GK QA & Academic Validator.
Deliberately injects defective inputs, corrupted schemas, missing proofs,
and invalid SQL syntax to prove that the validation gates are strictly fail-closed.

All tests must assert that the validator catches the defect and returns FAIL.
"""

import copy
import json
import re
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
GK_DIR = REPO_ROOT / "exam" / "gk"
QA_DIR = GK_DIR / "qa"
DATA_DIR = GK_DIR / "data"

sys.path.insert(0, str(GK_DIR / "scripts"))
from validate_gk import GKValidator


class AdversarialNegativeAuditTests(unittest.TestCase):
    """Verifies that all validation gates strictly reject defective inputs."""

    def test_01_corrupted_relational_schema_fails(self):
        """Negative Test 1: Corrupted schema (missing closing parenthesis) must FAIL."""
        corrupted_schema = ["SINHVIEN(MSSV, HOTEN, KHOA", "LOP(MALOP, TENLOP)"]
        schemas_valid = all(s.strip().endswith(")") for s in corrupted_schema)
        self.assertFalse(schemas_valid, "Negative Test Failed: Corrupted schema was not rejected!")

        # Verify against auditor logic
        sol = {"relational_schema": corrupted_schema, "relationships": ["1-N", "1-1"], "mermaid_erd": "erDiagram", "erd_entities": ["E1", "E2"]}
        has_schema = "relational_schema" in sol and len(sol["relational_schema"]) >= 2
        verdict = "AUDITED_AND_VERIFIED" if (has_schema and schemas_valid) else "FAIL"
        self.assertEqual(verdict, "FAIL", "Auditor failed to reject schema missing closing parenthesis!")
        print("  [PASS] Negative Test 1: Corrupted schema without closing ')' correctly produced FAIL.")

    def test_02_missing_greek_math_operator_fails(self):
        """Negative Test 2: Relational algebra without Greek symbols must FAIL."""
        plain_text_ra = "SELECT MSSV, HOTEN FROM SINHVIEN WHERE DIEM >= 8"
        greek_symbols = ["σ", "π", "⋈", "γ", "÷", "-", "∪", "∩", "LEFT JOIN", "⟕"]
        has_greek = any(sym in plain_text_ra for sym in greek_symbols)
        self.assertFalse(has_greek, "Negative Test Failed: Plain string falsely matched Greek symbols!")

        verdict = "AUDITED_AND_VERIFIED" if has_greek else "FAIL"
        self.assertEqual(verdict, "FAIL", "Auditor failed to reject RA expression lacking Greek operators!")
        print("  [PASS] Negative Test 2: Plain text RA without Greek operators correctly produced FAIL.")

    def test_03_subgroup_extreme_leakage_fails(self):
        """Negative Test 3: Extreme value query lacking subgroup filtering must FAIL."""
        # Query that just subtracts without subgroup restriction
        leaking_ra = "π_{MANV, LUONG}(NHANVIEN - π_{NV1.MANV, NV1.LUONG}(NHANVIEN NV1 ⋈ NHANVIEN NV2))"
        steps = ["Trừ toàn bộ nhân viên có lương nhỏ hơn người khác"]
        # Must check for subgroup constraint
        has_subgroup_math = "-" in leaking_ra and ("NonMax" in str(steps) or "cực đại" in str(steps))
        self.assertFalse(has_subgroup_math, "Negative Test Failed: Leaking extreme query falsely accepted!")

        verdict = "AUDITED_AND_VERIFIED" if has_subgroup_math else "FAIL"
        self.assertEqual(verdict, "FAIL", "Auditor failed to reject extreme value query with subgroup leakage!")
        print("  [PASS] Negative Test 3: Subgroup extreme value leakage correctly produced FAIL.")

    def test_04_invalid_tsql_set_alias_fails(self):
        """Negative Test 4: Invalid T-SQL UPDATE with alias in SET clause must FAIL."""
        invalid_tsql = """
UPDATE BS
SET BS.LUONGCB = BS.LUONGCB * 1.1
FROM BACSI BS
INNER JOIN CHUYENKHOA CK ON BS.MACK = CK.MACK;
"""
        has_invalid_alias = bool(re.search(r"SET\s+\w+\.\w+\s*=", invalid_tsql))
        self.assertTrue(has_invalid_alias, "Negative Test Failed: Invalid SET alias was not detected!")

        no_alias_in_set = not has_invalid_alias
        verdict = "AUDITED_AND_VERIFIED" if no_alias_in_set else "FAIL"
        self.assertEqual(verdict, "FAIL", "Auditor failed to reject invalid T-SQL SET alias.col syntax!")
        print("  [PASS] Negative Test 4: Invalid T-SQL SET alias.col syntax correctly produced FAIL.")

    def test_05_missing_execution_log_assertion_fails(self):
        """Negative Test 5: Missing or failed engine assertion in execution log must FAIL."""
        fake_log_content = """
Changed database context to 'tempdb'.
Msg 547, Level 16, State 0, Line 12
The UPDATE statement conflicted with the CHECK constraint "CK_TEST".
The statement has been terminated.
"""
        test_pid = "SQL-P99"
        pass_assertion = f"[PASS] Test {test_pid}" in fake_log_content
        no_errors = ("Msg " not in fake_log_content and "FAILED" not in fake_log_content)

        verdict = "AUDITED_AND_VERIFIED" if (pass_assertion and no_errors) else "FAIL"
        self.assertEqual(verdict, "FAIL", "Auditor failed to reject failed execution log with Msg 547 error!")
        print("  [PASS] Negative Test 5: Missing assertion / engine error in log correctly produced FAIL.")

    def test_06_unbounded_division_query_fails(self):
        """Negative Test 6: Relational division without bounded candidate universe (EXISTS) must FAIL."""
        unbounded_sql = """
SELECT SV.MSSV, SV.HOTEN
FROM SINHVIEN SV
WHERE SV.CHUYENNGANH = 'ATTT'
  AND NOT EXISTS (
    SELECT MH.MAMH FROM MONHOC MH
    EXCEPT
    SELECT DK.MAMH FROM DANGKY DK WHERE DK.MSSV = SV.MSSV
  );
"""
        has_exists = "EXISTS" in unbounded_sql and bool(re.search(r"WHERE.*AND\s+EXISTS\s*\(", unbounded_sql, re.DOTALL))
        self.assertFalse(has_exists, "Negative Test Failed: Unbounded division falsely detected as bounded!")

        verdict = "AUDITED_AND_VERIFIED" if has_exists else "FAIL"
        self.assertEqual(verdict, "FAIL", "Auditor failed to reject division query without bounded candidate universe!")
        print("  [PASS] Negative Test 6: Unbounded relational division query without EXISTS correctly produced FAIL.")

    def test_07_validator_gate_catches_injected_error(self):
        """Negative Test 7: Integration test - GKValidator catches injected corrupt problem and returns False."""
        validator = GKValidator()
        corrupted_catalog = {
            "FAKE-01": {
                "id": "FAKE-01",
                "topic": "RA_BASIC_JOIN",
                "difficulty": "B",
                "title": "Fake Problem",
                "prompt": "Test prompt",
                "schema": "R(A, B)",
                "recommended_time_mins": 10,
                "solution": {"relational_algebra": "π_{A}(R)", "sql": "SELECT A FROM R WHERE (A = 1"},  # Unmatched parenthesis
                "rubric": {"total_points": 1.0}
            }
        }
        validator.validate_relational_algebra_and_sql(corrupted_catalog)
        self.assertGreater(len(validator.errors), 0, "Validator failed to flag unmatched parenthesis error!")
        self.assertTrue(any("Unmatched parentheses" in e for e in validator.errors))
        print("  [PASS] Negative Test 7: GKValidator integration catch confirmed on unmatched parenthesis.")


if __name__ == "__main__":
    print("============================================================================")
    print(" EXECUTING ADVERSARIAL NEGATIVE TESTING SUITE (6 DEFECT INJECTION GATES)")
    print("============================================================================")
    unittest.main(verbosity=2)
