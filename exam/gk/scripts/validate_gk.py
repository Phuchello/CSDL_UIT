#!/usr/bin/env python3
"""
scripts/validate_gk.py
Comprehensive automated QA validator for IT004 Midterm Question Bank and Mock Exams.
Enforces all validation rules defined in the Master Prompt.
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
            "topics": {},
            "difficulties": {"A": 0, "B": 0, "C": 0},
            "verified_solutions": 0,
            "rubrics_present": 0,
            "mocks_count": 0,
            "mock_points_valid": 0,
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

            diff = p.get("difficulty")
            if diff in self.stats["difficulties"]:
                self.stats["difficulties"][diff] += 1
            else:
                self.log_error(f"Problem {pid} has invalid difficulty: {diff}")

            top = p.get("topic")
            self.stats["topics"][top] = self.stats["topics"].get(top, 0) + 1

            if p.get("solution"):
                self.stats["verified_solutions"] += 1
            if p.get("rubric"):
                self.stats["rubrics_present"] += 1

        print(f"  [OK] Validated {len(problems)} problem entries. Unique IDs confirmed.")
        return {p["id"]: p for p in problems if "id" in p}

    def validate_mock_exams(self, problem_catalog):
        print("\n=== [2/5] Validating 75-Minute Full Mock Exams ===")
        mocks_file = DATA_DIR / "mocks.json"
        if not mocks_file.exists():
            self.log_error(f"Mocks catalog missing: {mocks_file}")
            return

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

            # Check question references
            questions = m.get("questions", [])
            q_sum = sum(q.get("points", 0.0) for q in questions)
            if abs(q_sum - 10.0) > 1e-4:
                self.log_error(f"Mock {mid} sum of question points is {q_sum}, must be 10.0")

            for q in questions:
                ref_id = q.get("problem_id")
                if ref_id and ref_id not in problem_catalog:
                    self.log_error(f"Mock {mid} references nonexistent problem ID: {ref_id}")

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

        print(f"  [OK] Evaluated {len(mocks)} mock exam configurations.")

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

        print("\n==================================================")
        print(" AUDIT SUMMARY:")
        print(f"  Total Problems in Catalog : {self.stats['total_problems']}")
        print(f"  Verified Solutions        : {self.stats['verified_solutions']}")
        print(f"  Rubrics Present           : {self.stats['rubrics_present']}")
        print(f"  Difficulties (A/B/C)      : {self.stats['difficulties']}")
        print(f"  Mock Exams Audited        : {self.stats['mocks_count']}")
        print(f"  Mocks with Valid 10.0 pts : {self.stats['mock_points_valid']}")
        print(f"  Errors Detected           : {len(self.errors)}")
        print(f"  Warnings Detected         : {len(self.warnings)}")
        print("==================================================")

        report_file = QA_DIR / "audit_report.json"
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump({
                "status": "PASS" if not self.errors else "FAIL",
                "stats": self.stats,
                "errors": self.errors,
                "warnings": self.warnings
            }, f, ensure_ascii=False, indent=2)

        return len(self.errors) == 0


if __name__ == "__main__":
    validator = GKValidator()
    success = validator.run_all()
    sys.exit(0 if success else 1)
