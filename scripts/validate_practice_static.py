#!/usr/bin/env python3
"""Static semantic checks for the self-contained IT004 practice fixture."""
from pathlib import Path
import html
import json
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
SQL = ROOT / "practice" / "sql"
CHAPTERS = ROOT / "practice" / "chapters"
LEDGER_DIR = ROOT / "research" / "v1.1_phase_a"
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
EXPECTED_SEED_ROWS = {
    "tr_customers": 5, "tr_products": 7, "tr_orders": 5, "tr_order_items": 11,
    "tr_departments": 2, "tr_employees": 4, "tr_students": 4, "tr_courses": 3,
    "tr_results": 9,
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

def enhanced_main():
    """Run the C2 correction-gate checks in addition to the legacy fixture checks."""
    errors, notes, checks = [], [], []

    def read(path):
        return path.read_text(encoding="utf-8") if path.exists() else ""

    def check(label, condition, detail):
        checks.append({"check": label, "status": "PASS" if condition else "FAIL"})
        if not condition:
            errors.append(detail)

    production_chapters = [
        "00_cover_toc.html", "01_environment_workflow.html", "02_ddl_dml_foundations.html",
        "03_basic_queries_and_joins.html", "04_aggregation_and_subqueries.html",
        "05_integrity_and_triggers.html", "09_lab01_ddl.html", "10_lab02_dml.html",
        "11_lab03_advanced.html", "12_lab04_analytics.html", "13_debugging_expanded.html",
        "14_appendices_exam.html",
    ]
    ledger_files = ["source_inventory.md", "artifact_registry.md",
                    "practical_coverage_map.md", "exam_pattern_map.md"]
    required_ids = {"B01", "B02", "B03", "B04", "B05", "A01", "A02", "A03", "A04", "A05", "A06", "A07",
                    "TOP-TIE", "TRG-A", "TRG-B", "TRG-C", "TRG-D", "TRG-E", "TRG-F", "TRG-G", "TRG-H"}
    token_re = re.compile(r"\b(?:UIT|TECH|LOC|PRAC|EXAM|GH|TXT)-[A-Za-z0-9][A-Za-z0-9-]*\b")

    required = ["00_create_training_db.sql", "01_schema.sql", "02_seed.sql", "03_queries_basic.sql",
                "04_queries_advanced.sql", "05_triggers.sql", "06_test_cases.sql", "reset.sql"]
    for name in required:
        check("file " + name, (SQL / name).exists(), "missing " + name)

    schema = read(SQL / "01_schema.sql")
    schema_tables = set(re.findall(r"CREATE TABLE\s+dbo\.(tr_\w+)", schema, re.I))
    lower_tables = {x.lower() for x in schema_tables}
    check("canonical tables", EXPECTED_TABLES <= lower_tables,
          "schema missing tables: " + ", ".join(sorted(EXPECTED_TABLES - lower_tables)))
    for table, cols in EXPECTED_COLUMNS.items():
        block = re.search(r"CREATE TABLE\s+dbo\." + re.escape(table) + r"\s*\((.*?)\);", schema, re.I | re.S)
        got = set(re.findall(r"^\s*([A-Za-z_]\w*)\s+(?:CHAR|N?VARCHAR|INT|DATE|DATETIME2|DECIMAL|BIT)",
                             block.group(1), re.I | re.M)) if block else set()
        missing = cols - got
        check("columns " + table, not missing,
              f"{table} missing columns: {', '.join(sorted(missing))}")

    seed = read(SQL / "02_seed.sql")
    for table, count in EXPECTED_SEED_ROWS.items():
        match = re.search(r"INSERT INTO\s+dbo\." + table + r".*?VALUES\s*(.*?);", seed, re.I | re.S)
        rows = len(re.findall(r"\([^()]*\)", match.group(1))) if match else -1
        check("seed rows " + table, rows == count,
              f"seed {table}: expected {count} rows, found {rows}")

    trig = read(SQL / "05_triggers.sql")
    for name in ["trg_tr_departments_head_guard", "trg_tr_employees_head_guard"]:
        check("trigger " + name, name.lower() in trig.lower(), "missing trigger " + name)
    for token in ["inserted", "deleted", "IF EXISTS", "THROW"]:
        check("trigger token " + token, token.lower() in trig.lower(), "trigger script missing " + token)

    known_refs = {x.lower() for x in EXPECTED_TABLES}
    for name in ["03_queries_basic.sql", "04_queries_advanced.sql", "05_triggers.sql", "06_test_cases.sql"]:
        sql_text = read(SQL / name)
        refs = {x.lower() for x in re.findall(r"(?:FROM|JOIN|UPDATE|INTO|TABLE)\s+(?:dbo\.)?(tr_\w+)", sql_text, re.I)}
        unknown = refs - known_refs
        check("table refs " + name, not unknown,
              f"{name} unknown table refs: {', '.join(sorted(unknown))}")

    production_text = "\n".join(read(CHAPTERS / name) for name in production_chapters)
    ledger_text = "\n".join(read(LEDGER_DIR / name) for name in ledger_files)
    unknown_tokens = sorted(set(token_re.findall(production_text)) - set(token_re.findall(ledger_text)))
    check("frozen provenance IDs", not unknown_tokens,
          "unknown source IDs: " + ", ".join(unknown_tokens))

    registry = read(ROOT / "practice" / "EXAMPLE_REGISTRY.md")
    registry_rows = {}
    for line in registry.splitlines():
        if not line.startswith("|") or line.startswith("| Example ID") or line.startswith("|---"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells:
            registry_rows.setdefault(cells[0], []).append(tuple(cells))
    registry_ids = set(registry_rows)
    check("registry required IDs", required_ids <= registry_ids,
          "registry missing IDs: " + ", ".join(sorted(required_ids - registry_ids)))
    conflicting = [key for key, rows in registry_rows.items() if len(set(rows)) > 1]
    check("registry duplicate consistency", not conflicting,
          "conflicting duplicate example IDs: " + ", ".join(sorted(conflicting)))
    for example_id in sorted(required_ids):
        # Trigger cases are printed as the compact A–H matrix; the registry
        # expands those anchors to TRG-A … TRG-H for runnable test scripts.
        anchor_ok = ("A–H" in production_text) if example_id.startswith("TRG-") else (re.search(r"\b" + re.escape(example_id) + r"\b", production_text) is not None)
        check("printed anchor " + example_id, anchor_ok,
              f"example {example_id} missing from production chapters")

    expected_fragments = {
        "B01": ["C001", "C002", "C003", "3"],
        "B02": ["2024-10-15", "2024-10-18", "1001", "1002", "1003", "1004", "4"],
        "A01": ["P001", "1200", "1"], "A03": ["P007", "1"],
        "A04": ["S001", "1"], "A05": ["S001", "1"],
    }
    for example_id, fragments in expected_fragments.items():
        haystack = " ".join(" ".join(row) for row in registry_rows.get(example_id, []))
        check("registry expected " + example_id, all(fragment in haystack for fragment in fragments),
              "registry expected values mismatch for " + example_id)
    check("B01 canonical query", all(fragment in production_text for fragment in ["Segment", "C001", "C002", "C003"]),
          "B01 printed projection is not the canonical A/B query")
    lab02 = read(CHAPTERS / "10_lab02_dml.html")
    lab02_plain = html.unescape(re.sub(r"<[^>]+>", " ", lab02))
    lab03_plain = html.unescape(re.sub(r"<[^>]+>", " ", read(CHAPTERS / "11_lab03_advanced.html")))
    check("B04 printed/runnable sync",
          bool(re.search(r"COUNT\s*\(\s*o\.OrderId\s*\)", lab02_plain))
          and bool(re.search(r"GROUP\s+BY\s+c\.CustomerId,\s*c\.FullName", lab02_plain))
          and all(fragment in lab02_plain for fragment in ["OrderCount", "C005", "OrderCount = 0"]),
          "B04 printed query must be LEFT JOIN + COUNT with C005 OrderCount = 0")
    check("A07 printed/runnable sync",
          bool(re.search(r"Stock\s*=\s*0", lab03_plain))
          and bool(re.search(r"Stock\s*<\s*10", lab03_plain))
          and all(fragment in lab03_plain for fragment in ["StockBand", "P001/P004/P007 = LOW"]),
          "A07 printed query must be the canonical StockBand projection")
    check("B05 ID clarity",
          all(fragment in lab02_plain for fragment in [
              "B05", "Self-Join", "Minh họa bổ sung", "UNION", "không mang mã B05"
          ]),
          "B05 must label the Self-Join as canonical and UNION as supplemental")
    check("A03 ID clarity",
          all(fragment in lab03_plain for fragment in [
              "Minh họa EXISTS", "không mang mã A03",
              "A03", "NOT EXISTS", "tr_order_items"
          ]),
          "A03 must label the unsold-product NOT EXISTS query separately")
    check("B02 half-open date", "2024-10-15" in production_text and "2024-10-18" in production_text
          and not re.search(r"2025-\d{2}-\d{2}", production_text),
          "B02 contains stale dates or is not [2024-10-15, 2024-10-18)")
    toc = read(CHAPTERS / "00_cover_toc.html")
    stale_toc_numbers = re.findall(r"\bTr\.\s*\d+\b", toc)
    check("TOC stale page numbers", not stale_toc_numbers,
          "TOC source retains stale page numbers: " + ", ".join(stale_toc_numbers))
    check("no unsupported set variants", not re.search(r"\b(?:INTERSECT|EXCEPT)\s+ALL\b", production_text, re.I),
          "INTERSECT ALL/EXCEPT ALL is not supported by this handbook")

    product_inserts = re.findall(r"INSERT INTO</span>\s+dbo\.tr_products\((.*?)\).*?VALUES</span>\s*(.*?)</pre>",
                                 lab02, re.I | re.S)
    product_error_ok = bool(product_inserts) and all("Country" in cols and "Stock" in cols for cols, _ in product_inserts)
    check("intentional product inserts", product_error_ok,
          "product error examples must include NOT NULL Country and Stock")

    reset = read(SQL / "reset.sql")
    lifecycle_ok = all(marker in schema for marker in ["DROP CONSTRAINT FK_tr_departments_head", "sys.foreign_keys"])
    lifecycle_ok = lifecycle_ok and "HeadEmployeeId = NULL" in seed and all(marker in reset for marker in [":r 01_schema.sql", ":r 02_seed.sql"])
    check("circular FK reset lifecycle", lifecycle_ok,
          "reset lifecycle must drop FK_tr_departments_head and null HeadEmployeeId before employee delete")
    check("no phantom enrollment table", "tr_enrollments" not in schema.lower(),
          "phantom tr_enrollments drop/reference remains in schema")
    check("trigger E boundary", "schema-level reject" in production_text and "DeptId" in production_text and "NOT NULL" in production_text,
          "trigger case E must be identified as schema-level NOT NULL rejection")

    runtime = False
    sqlcmd = shutil.which("sqlcmd")
    if sqlcmd:
        try:
            probe = subprocess.run([sqlcmd, "-S", "localhost", "-E", "-C", "-b", "-Q", "SELECT 1"],
                                   capture_output=True, text=True, timeout=8)
            runtime = probe.returncode == 0
        except (OSError, subprocess.SubprocessError):
            runtime = False
    notes.append("STATIC CONSISTENCY VALIDATION: " + ("PASS" if not errors else "FAIL"))
    notes.append("SQL RUNTIME VALIDATION: " + ("AVAILABLE (sqlcmd detected)" if runtime else "NOT AVAILABLE"))
    result = {"status": "PASS" if not errors else "FAIL", "errors": errors, "notes": notes,
              "checks": checks, "tables": sorted(schema_tables), "runtime_available": runtime,
              "production_chapters": production_chapters}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    enhanced_main()
