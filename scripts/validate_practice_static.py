#!/usr/bin/env python3
"""Static semantic checks for the self-contained IT004 practice fixture."""
from pathlib import Path
import json
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
SQL = ROOT / "practice" / "sql"
EXPECTED_TABLES = {
    "tr_customers", "tr_products", "tr_orders", "tr_order_items",
    "tr_departments", "tr_employees", "tr_students", "tr_courses", "tr_results",
}
EXPECTED_COLUMNS = {
    "tr_customers": {"CustomerId", "FullName", "City", "RegisteredOn", "CreditLimit", "Segment"},
    "tr_products": {"ProductId", "ProductName", "Category", "Country", "Price", "Stock", "IsActive"},
    "tr_orders": {"OrderId", "CustomerId", "OrderDate", "Status"},
    "tr_order_items": {"OrderId", "ProductId", "Qty", "UnitPrice"},
}

def main():
    errors, notes = [], []
    required = ["00_create_training_db.sql", "01_schema.sql", "02_seed.sql",
                "03_queries_basic.sql", "04_queries_advanced.sql", "05_triggers.sql",
                "06_test_cases.sql", "reset.sql"]
    for name in required:
        if not (SQL / name).exists():
            errors.append("missing " + name)
    schema = (SQL / "01_schema.sql").read_text(encoding="utf-8") if (SQL / "01_schema.sql").exists() else ""
    schema_tables = set(re.findall(r"CREATE TABLE\s+dbo\.(tr_\w+)", schema, re.I))
    missing_tables = EXPECTED_TABLES - schema_tables
    if missing_tables:
        errors.append("schema missing tables: " + ", ".join(sorted(missing_tables)))
    for table, cols in EXPECTED_COLUMNS.items():
        block = re.search(r"CREATE TABLE\s+dbo\." + re.escape(table) + r"\s*\((.*?)\);", schema, re.I | re.S)
        if not block:
            continue
        got = set(re.findall(r"^\s*(\w+)\s+(?:CHAR|N?VARCHAR|INT|DATE|DATETIME2|DECIMAL|BIT)", block.group(1), re.I | re.M))
        if cols - got:
            errors.append(f"{table} missing columns: {', '.join(sorted(cols-got))}")
    seed = (SQL / "02_seed.sql").read_text(encoding="utf-8") if (SQL / "02_seed.sql").exists() else ""
    expected_inserts = {"tr_customers": 5, "tr_products": 7, "tr_orders": 5, "tr_order_items": 11,
                        "tr_departments": 2, "tr_employees": 4, "tr_students": 4, "tr_courses": 3, "tr_results": 9}
    for table, count in expected_inserts.items():
        match = re.search(r"INSERT INTO\s+dbo\." + table + r".*?VALUES\s*(.*?);", seed, re.I | re.S)
        if not match:
            errors.append("seed missing INSERT " + table)
            continue
        rows = len(re.findall(r"\([^()]*\)", match.group(1)))
        if rows != count:
            errors.append(f"seed {table}: expected {count} rows, found {rows}")
    trig = (SQL / "05_triggers.sql").read_text(encoding="utf-8") if (SQL / "05_triggers.sql").exists() else ""
    for name in ["trg_tr_departments_head_guard", "trg_tr_employees_head_guard"]:
        if name not in trig:
            errors.append("missing trigger " + name)
    for token in ["inserted", "deleted", "IF EXISTS", "THROW"]:
        if token.lower() not in trig.lower():
            errors.append("trigger script missing " + token)
    known_refs = EXPECTED_TABLES
    for name in ["03_queries_basic.sql", "04_queries_advanced.sql", "05_triggers.sql", "06_test_cases.sql"]:
        text = (SQL / name).read_text(encoding="utf-8") if (SQL / name).exists() else ""
        refs = set(re.findall(r"(?:FROM|JOIN|UPDATE|INTO|TABLE)\s+(?:dbo\.)?(tr_\w+)", text, re.I))
        unknown = {x.lower() for x in refs} - known_refs
        if unknown:
            errors.append(f"{name} unknown table refs: {', '.join(sorted(unknown))}")
    runtime = False
    sqlcmd = shutil.which("sqlcmd")
    if sqlcmd:
        try:
            probe = subprocess.run([sqlcmd, "-S", "localhost", "-E", "-C", "-b", "-Q", "SELECT 1"],
                                   capture_output=True, text=True, timeout=8)
            runtime = probe.returncode == 0
        except (OSError, subprocess.SubprocessError):
            runtime = False
    notes.append("SQL RUNTIME VALIDATION: " + ("AVAILABLE (sqlcmd detected)" if runtime else "NOT AVAILABLE"))
    result = {"status": "PASS" if not errors else "FAIL", "errors": errors, "notes": notes,
              "tables": sorted(schema_tables), "runtime_available": runtime}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if not errors else 1)

if __name__ == "__main__":
    main()
