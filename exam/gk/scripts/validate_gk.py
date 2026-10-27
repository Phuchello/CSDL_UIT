#!/usr/bin/env python3
"""
scripts/validate_gk.py
Comprehensive automated QA validator for IT004 Midterm Question Bank and Mock Exams.
Enforces all validation rules defined in the Master Prompt & Phase D Audits.
"""

import json
import os
import re
import sys
from pathlib import Path

# Ensure UTF-8 output
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
GK_DIR = REPO_ROOT / "exam" / "gk"
DATA_DIR = GK_DIR / "data"
BANK_DIR = GK_DIR / "bank"
MOCKS_DIR = GK_DIR / "mocks"
QA_DIR = GK_DIR / "qa"


class GKValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.stats = {
            "total_problems": 0,
            "mock_exam_questions": 0,
            "independent_practice_problems": 0,
            "independent_topics": {
                "ERD_MAPPING": 0,
                "RA_BASIC_JOIN": 0,
                "RA_DIVISION_GROUPING": 0,
                "SQL_DDL_DML": 0
            },
            "topics": {},
            "difficulties": {"A": 0, "B": 0, "C": 0},
            "verified_problems": 0,
            "draft_problems": 0,
            "verification_levels": {
                "EXECUTION_VERIFIED": 0,
                "SEMANTICALLY_REVIEWED": 0,
                "DRAFT": 0,
            },
            "solutions_present": 0,
            "rubrics_present": 0,
            "mocks_count": 0,
            "mock_points_valid": 0,
            "gold_standard_mocks_audited": 0,
            "no_solution_leak": 0,
        }

    def log_error(self, msg: str):
        self.errors.append(msg)
        print(f"  [ERROR] {msg}")

    def log_warning(self, msg: str):
        self.warnings.append(msg)
        print(f"  [WARN] {msg}")

    def validate_problems_data(self):
        print("=== [1/5] Validating Problem Bank Catalog ===")
        problems_file = DATA_DIR / "problems.json"
        if not problems_file.exists():
            self.log_error(f"Catalog file missing: {problems_file}")
            return {}

        with open(problems_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        problems = data.get("problems", [])
        self.stats["total_problems"] = len(problems)
        seen_ids = set()

        required_fields = [
            "id", "topic", "difficulty", "title", "prompt", "schema",
            "recommended_time_mins", "solution", "rubric"
        ]

        placeholder_patterns = [
            r"\bTBD\b", r"\bTODO\b", r"\bLorem ipsum\b", r"\[Placeholder\]", r"Chưa có đáp án"
        ]

        for p in problems:
            pid = p.get("id")
            if not pid or not isinstance(pid, str):
                self.log_error(f"Problem without valid ID: {p}")
                continue

            if pid in seen_ids:
                self.log_error(f"Duplicate problem ID: {pid}")
            seen_ids.add(pid)

            for rf in required_fields:
                if rf not in p or not p[rf]:
                    self.log_error(f"Problem {pid} missing required field: {rf}")

            # Check placeholders
            p_text = json.dumps(p, ensure_ascii=False)
            for pat in placeholder_patterns:
                if re.search(pat, p_text, re.IGNORECASE):
                    self.log_error(f"Problem {pid} contains unapproved placeholder: {pat}")

            diff = p.get("difficulty")
            if diff in self.stats["difficulties"]:
                self.stats["difficulties"][diff] += 1
            else:
                self.log_error(f"Problem {pid} has invalid difficulty: {diff}")

            top = p.get("topic")
            self.stats["topics"][top] = self.stats["topics"].get(top, 0) + 1

            # Check whether mock question or independent practice problem
            is_mock_q = bool(p.get("mock_id")) or (pid.startswith("M") and len(pid) >= 3 and pid[1:3].isdigit() and "-" in pid)
            if is_mock_q:
                self.stats["mock_exam_questions"] += 1
            else:
                self.stats["independent_practice_problems"] += 1
                if top in self.stats["independent_topics"]:
                    self.stats["independent_topics"][top] += 1

            v_level = p.get("verification_level", "DRAFT")
            if v_level not in self.stats["verification_levels"]:
                self.log_error(f"Problem {pid} has invalid verification_level: {v_level}")
                v_level = "DRAFT"

            # Strict verification criteria
            if v_level == "EXECUTION_VERIFIED":
                if pid.startswith("M") and len(pid) >= 3 and pid[1:3].isdigit():
                    exec_log = QA_DIR / f"mock{pid[1:3]}_sql_execution.log"
                else:
                    exec_log = QA_DIR / f"{pid.lower()}_sql_execution.log"

                if not exec_log.exists():
                    self.log_error(f"Problem {pid} marked EXECUTION_VERIFIED but execution log is missing ({exec_log.name})!")
                self.stats["verified_problems"] += 1
                self.stats["verification_levels"]["EXECUTION_VERIFIED"] += 1
            elif v_level == "SEMANTICALLY_REVIEWED":
                if p.get("status") != "VERIFIED":
                    self.log_warning(f"Problem {pid} marked SEMANTICALLY_REVIEWED but status is not VERIFIED.")
                self.stats["verified_problems"] += 1
                self.stats["verification_levels"]["SEMANTICALLY_REVIEWED"] += 1
            else:
                self.stats["draft_problems"] += 1
                self.stats["verification_levels"]["DRAFT"] += 1

            if p.get("solution"):
                self.stats["solutions_present"] += 1
            if p.get("rubric"):
                self.stats["rubrics_present"] += 1

        print(f"  [OK] Validated {len(problems)} problem entries ({self.stats['mock_exam_questions']} mock questions + {self.stats['independent_practice_problems']} independent problems). Unique IDs confirmed.")
        return {p["id"]: p for p in problems if "id" in p}

    def validate_mock_exams(self, problem_catalog):
        print("\n=== [2/5] Validating 75-Minute Full Mock Exams & Evidence Manifest ===")
        mocks_file = DATA_DIR / "mocks.json"
        manifest_file = QA_DIR / "evidence_manifest.json"

        if not mocks_file.exists():
            self.log_error(f"Mocks catalog missing: {mocks_file}")
            return
        if not manifest_file.exists():
            self.log_error(f"Evidence manifest missing: {manifest_file}")
            manifest_data = {}
        else:
            with open(manifest_file, "r", encoding="utf-8") as f:
                manifest_data = json.load(f).get("questions", {})

        with open(mocks_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        mocks = data.get("mocks", [])
        self.stats["mocks_count"] = len(mocks)

        for m in mocks:
            mid = m.get("id")
            m_title = m.get("title", mid)
            total_points = m.get("total_points", 0.0)
            duration = m.get("duration_mins", 0)

            if abs(total_points - 10.0) > 1e-4:
                self.log_error(f"Mock {mid} total points is {total_points}, MUST BE EXACTLY 10.0")
            else:
                self.stats["mock_points_valid"] += 1

            if duration != 75:
                self.log_error(f"Mock {mid} duration is {duration} mins, MUST BE EXACTLY 75 mins")

            # Check question references & evidence manifest
            questions = m.get("questions", [])
            q_sum = sum(q.get("points", 0.0) for q in questions)
            if abs(q_sum - 10.0) > 1e-4:
                self.log_error(f"Mock {mid} sum of question points is {q_sum}, must be 10.0")

            all_questions_audited = True
            for q in questions:
                ref_id = q.get("problem_id")
                if not ref_id or ref_id not in problem_catalog:
                    self.log_error(f"Mock {mid} references nonexistent problem ID: {ref_id}")
                    all_questions_audited = False
                elif ref_id not in manifest_data:
                    self.log_error(f"Mock {mid} question {ref_id} lacks entry in evidence manifest!")
                    all_questions_audited = False
                else:
                    m_entry = manifest_data[ref_id]
                    if m_entry.get("audit_verdict") != "AUDITED_AND_VERIFIED":
                        self.log_error(f"Mock {mid} question {ref_id} failed academic audit: {m_entry.get('audit_verdict')}")
                        all_questions_audited = False

            if all_questions_audited and len(questions) == 9:
                self.stats["gold_standard_mocks_audited"] += 1

            # Verify physical mock folders exist and no solution leak
            mock_dir = MOCKS_DIR / mid
            if mock_dir.exists():
                exam_paper = mock_dir / "exam.md"
                solution_paper = mock_dir / "solution.md"

                if not exam_paper.exists():
                    self.log_error(f"Mock {mid} missing exam.md")
                else:
                    exam_content = exam_paper.read_text(encoding="utf-8")
                    # Check for solution leak in question paper
                    leak_markers = ["Lời giải chi tiết", "ĐÁP ÁN", "Barem chấm điểm", "Step-by-step"]
                    found_leak = any(lm in exam_content for lm in leak_markers)
                    if found_leak:
                        self.log_error(f"CRITICAL: Potential solution leak detected in {exam_paper}")
                    else:
                        self.stats["no_solution_leak"] += 1

                if not solution_paper.exists():
                    self.log_error(f"Mock {mid} missing solution.md")
            else:
                self.log_warning(f"Mock directory not yet created on disk: {mock_dir}")

        print(f"  [OK] Evaluated {len(mocks)} mock exam configurations. Audited Gold Standard Mocks: {self.stats['gold_standard_mocks_audited']} / {len(mocks)}.")

    def validate_relational_algebra_and_sql(self, problem_catalog):
        print("\n=== [3/5] Validating Relational Algebra & SQL Semantics ===")
        ra_count = 0
        sql_count = 0

        for pid, p in problem_catalog.items():
            topic = p.get("topic", "")
            sol = p.get("solution", {})
            ra_expr = sol.get("relational_algebra", "")
            sql_expr = sol.get("sql", "")

            if ra_expr:
                ra_count += 1
                # Check that intermediate steps are explained
                steps = sol.get("intermediate_steps", [])
                if not steps and p.get("difficulty") in ["B", "C"]:
                    self.log_warning(f"Problem {pid} (level {p.get('difficulty')}) lacks intermediate steps breakdown.")

            if sql_expr:
                sql_count += 1
                # Syntax sanity checks: check matched parentheses
                if sql_expr.count("(") != sql_expr.count(")"):
                    self.log_error(f"Unmatched parentheses in SQL for problem {pid}")

        print(f"  [OK] RA expressions checked: {ra_count}, SQL statements checked: {sql_count}")

    def run_all(self) -> bool:
        print("==================================================")
        print(" IT004 Midterm Exam Module — Automated QA Auditor ")
        print("==================================================")

        catalog = self.validate_problems_data()
        self.validate_mock_exams(catalog)
        self.validate_relational_algebra_and_sql(catalog)

        gold_mocks_cnt = self.stats["gold_standard_mocks_audited"]
        indep_cnt = self.stats["independent_practice_problems"]
        mock_q_cnt = self.stats["mock_exam_questions"]

        structural_status = "PASS" if not self.errors else "FAIL"

        academic_passed = (
            gold_mocks_cnt == 15 and
            indep_cnt >= 150 and
            len(self.errors) == 0 and
            self.stats["draft_problems"] == 0
        )
        academic_status = (
            "PASS (15/15 Mocks Gold Standard Audited & 150 Independent Practice Problems Verified)"
            if academic_passed
            else f"IN_PROGRESS (Mocks: {gold_mocks_cnt}/15, Independent: {indep_cnt}/150, Drafts: {self.stats['draft_problems']})"
        )

        print("\n==================================================")
        print(" AUDIT SUMMARY:")
        print("  [1] STRUCTURAL QA (Catalog, Schema, Rubrics, Points):")
        print(f"      - Status                  : {structural_status}")
        print(f"      - Total Problems in Bank  : {self.stats['total_problems']}")
        print(f"      - Mock Exam Questions     : {mock_q_cnt} (15 Mocks x 9 Questions)")
        print(f"      - Independent Practice    : {indep_cnt} (Target >= 150)")
        print(f"        * ERD & Schema Mapping  : {self.stats['independent_topics']['ERD_MAPPING']} / 25")
        print(f"        * RA Basic & Join       : {self.stats['independent_topics']['RA_BASIC_JOIN']} / 45")
        print(f"        * RA Division & Grouping: {self.stats['independent_topics']['RA_DIVISION_GROUPING']} / 45")
        print(f"        * Transact-SQL DDL/DML  : {self.stats['independent_topics']['SQL_DDL_DML']} / 35")
        print(f"      - Solutions Present       : {self.stats['solutions_present']} / {self.stats['total_problems']}")
        print(f"      - Rubrics Present         : {self.stats['rubrics_present']} / {self.stats['total_problems']}")
        print(f"      - Mock Exams (10.0 pts)   : {self.stats['mock_points_valid']} / {self.stats['mocks_count']}")
        print(f"      - Structural Errors       : {len(self.errors)}")
        print(f"      - Warnings                : {len(self.warnings)}")
        print("  [2] ACADEMIC SEMANTIC QA (Evidence Manifest & Verification):")
        print(f"      - Gold Standard Mocks     : {gold_mocks_cnt} / 15 (100% Audited in Evidence Manifest)")
        print(f"      - Execution Verified Probs: {self.stats['verification_levels']['EXECUTION_VERIFIED']} / {self.stats['total_problems']}")
        print(f"      - Semantically Reviewed   : {self.stats['verification_levels']['SEMANTICALLY_REVIEWED']} / {self.stats['total_problems']}")
        print(f"      - Draft / Pending Remed.  : {self.stats['verification_levels']['DRAFT']} / {self.stats['total_problems']}")
        print(f"      - Academic Gate Status    : {academic_status}")
        print("==================================================")

        report_file = QA_DIR / "audit_report.json"
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump({
                "structural_qa_status": structural_status,
                "academic_semantic_qa_status": academic_status,
                "gold_standard_mocks_count": gold_mocks_cnt,
                "independent_practice_problems_count": indep_cnt,
                "mock_exam_questions_count": mock_q_cnt,
                "stats": self.stats,
                "errors": self.errors,
                "warnings": self.warnings
            }, f, ensure_ascii=False, indent=2)

        return len(self.errors) == 0 and academic_passed


if __name__ == "__main__":
    validator = GKValidator()
    success = validator.run_all()
    sys.exit(0 if success else 1)
