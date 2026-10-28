# -*- coding: utf-8 -*-
"""
scripts/build_all_independent_problems.py
Constructs all 150 remediated, authentic independent practice problems
and combines them with the 135 mock exam questions into problems.json.
Total catalog = 135 + 150 = 285 problems.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(Path(__file__).parent))

from remediation.erd_data import get_remediated_erd_problems
from remediation.ra_basic_data import get_remediated_ra_basic_problems
from remediation.ra_division_grouping_data import get_remediated_ra_division_grouping_problems
from remediation.sql_data import get_remediated_sql_problems

def build_all_150_independent_problems():
    independent_problems = []

    # 1. 25 ERD Problems (ERD-P01 .. ERD-P25)
    erd_probs = get_remediated_erd_problems()
    assert len(erd_probs) == 25, f"Expected 25 ERD problems, got {len(erd_probs)}"
    independent_problems.extend(erd_probs)

    # 2. 45 Basic RA & Join Problems (RA-B01 .. RA-B45)
    ra_b_probs = get_remediated_ra_basic_problems()
    assert len(ra_b_probs) == 45, f"Expected 45 RA Basic problems, got {len(ra_b_probs)}"
    independent_problems.extend(ra_b_probs)

    # 3. 45 Division, Grouping & Extremes Problems (RA-D01 .. RA-D45)
    ra_d_probs = get_remediated_ra_division_grouping_problems()
    assert len(ra_d_probs) == 45, f"Expected 45 RA Division & Grouping problems, got {len(ra_d_probs)}"
    independent_problems.extend(ra_d_probs)

    # 4. 35 SQL DDL/DML Problems (SQL-P01 .. SQL-P35)
    sql_probs = get_remediated_sql_problems()
    assert len(sql_probs) == 35, f"Expected 35 SQL problems, got {len(sql_probs)}"
    independent_problems.extend(sql_probs)

    assert len(independent_problems) == 150, f"Expected exactly 150 independent problems, got {len(independent_problems)}"
    return independent_problems

if __name__ == "__main__":
    probs = build_all_150_independent_problems()
    print(f"Successfully constructed {len(probs)} authentic independent practice problems!")
    by_topic = {}
    for p in probs:
        by_topic[p["topic"]] = by_topic.get(p["topic"], 0) + 1
    print("Breakdown by topic:", by_topic)
