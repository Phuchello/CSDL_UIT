#!/usr/bin/env python3
"""Small D1 contract gate for the representative static site layer."""
from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "practice" / "sql" / "01_schema.sql"
SITE_JS = ROOT / "site" / "app.js"
SITE_HTML = ROOT / "site" / "index.html"
SITE_CSS = ROOT / "site" / "styles.css"
SOURCE_LEDGER = ROOT / "research" / "v1.1_phase_a" / "source_inventory.md"

failures: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        failures.append(message)


def schema_columns() -> dict[str, set[str]]:
    text = SCHEMA_PATH.read_text(encoding="utf-8")
    tables: dict[str, set[str]] = {}
    for match in re.finditer(r"CREATE TABLE\s+dbo\.(tr_\w+)\s*\((.*?)\n\);", text, re.I | re.S):
        table, body = match.groups()
        cols: set[str] = set()
        for line in body.splitlines():
            column = re.match(r"\s*([A-Za-z_]\w*)\s+[A-Za-z]", line)
            if column and column.group(1).upper() not in {"CONSTRAINT", "PRIMARY", "FOREIGN", "UNIQUE"}:
                cols.add(column.group(1))
        tables[table] = cols
    return tables


def alias_table_map(snippet: str, pseudo_tables: dict[str, str] | None = None) -> dict[str, str]:
    aliases = {
        alias: table
        for table, alias in re.findall(
            r"(?:FROM|JOIN)\s+dbo\.(tr_\w+)\s+AS\s+(\w+)",
            snippet,
            re.I,
        )
    }
    if pseudo_tables:
        aliases.update(pseudo_tables)
    return aliases


def check_alias_columns(snippet: str, tables: dict[str, set[str]], pseudo_tables: dict[str, str] | None = None) -> None:
    aliases = alias_table_map(snippet, pseudo_tables)
    for table in re.findall(r"dbo\.(tr_\w+)", snippet, re.I):
        require(table in tables, f"unknown canonical table: {table}")
    for alias, column in re.findall(r"(?<![/.])\b(\w+)\.(\w+)\b", snippet):
        if alias.lower() in {"dbo", "tr"}:
            continue
        table = aliases.get(alias)
        require(table is not None, f"unknown table alias: {alias}")
        if table is not None:
            require(column in tables[table], f"unknown column {alias}.{column} for {table}")


def alias_column_self_test(tables: dict[str, set[str]]) -> bool:
    before = len(failures)
    check_alias_columns("SELECT s.StudentId FROM dbo.tr_students AS s", tables)
    valid_ok = len(failures) == before
    before = len(failures)
    check_alias_columns("SELECT s.NotARealColumn FROM dbo.tr_students AS s", tables)
    invalid_detected = any("unknown column s.NotARealColumn" in item for item in failures[before:])
    del failures[before:]
    return valid_ok and invalid_detected


def source_url(source_id: str, ledger: str) -> str | None:
    line = next((line for line in ledger.splitlines() if f"**{source_id}**" in line), "")
    match = re.search(r"\((https?://[^)]+)\)", line)
    return match.group(1) if match else None


def rendered_source_url(source_id: str, app: str) -> str | None:
    marker = f'class="source-tier">{source_id}</span>'
    position = app.find(marker)
    if position < 0:
        return None
    match = re.search(r'<a href="([^"]+)"', app[position:position + 700])
    return match.group(1) if match else None


def main() -> int:
    schema = schema_columns()
    app = SITE_JS.read_text(encoding="utf-8")
    html = SITE_HTML.read_text(encoding="utf-8")
    css = SITE_CSS.read_text(encoding="utf-8")
    ledger = SOURCE_LEDGER.read_text(encoding="utf-8")

    lab_match = re.search(r'"lab-03":.*?(?=\n  errors:)', app, re.S)
    require(lab_match is not None, "Lab 03 route not found")
    lab = lab_match.group(0) if lab_match else ""
    lab_tables = {"tr_students", "tr_courses", "tr_results"}
    require(lab_tables.issubset(set(re.findall(r"dbo\.(tr_\w+)", lab))), "Lab 03 canonical table set is incomplete")
    require("tr_order_lines" not in lab and "tr_orders" not in lab, "Lab 03 contains a non-canonical order fixture")
    lab_aliases = alias_table_map(lab)
    lab_alias_resolution = all(lab_aliases.get(alias) == table for alias, table in {
        "s": "tr_students", "c": "tr_courses", "r": "tr_results"
    }.items())
    require(lab_alias_resolution, "Lab 03 alias-to-table resolution is incomplete")
    lab_before = len(failures)
    check_alias_columns(lab, schema)
    lab_column_contract = len(failures) == lab_before
    require("S001" in lab and "STATIC" in lab, "Lab 03 expected result is not marked STATIC")

    trigger_match = re.search(r'"multi-row-trigger":.*?(?=\n  closure:)', app, re.S)
    require(trigger_match is not None, "Multi-row trigger route not found")
    trigger = trigger_match.group(0) if trigger_match else ""
    require({"tr_departments", "tr_employees"}.issubset(set(re.findall(r"dbo\.(tr_\w+)", trigger))), "Trigger canonical table set is incomplete")
    require("TotalAmount" not in trigger and "tr_orders" not in trigger, "Trigger contains a non-canonical order fixture")
    first_trigger, second_trigger = (trigger.split("-- Employee DELETE/UPDATE", 1) + [""])[:2]
    first_aliases = alias_table_map(first_trigger, {"d": "tr_departments"})
    second_aliases = alias_table_map(second_trigger, {"d": "tr_employees", "i": "tr_employees"})
    trigger_alias_resolution = all(first_aliases.get(alias) == table for alias, table in {
        "d": "tr_departments", "e": "tr_employees"
    }.items()) and all(second_aliases.get(alias) == table for alias, table in {
        "d": "tr_employees", "i": "tr_employees", "dep": "tr_departments"
    }.items())
    require(trigger_alias_resolution, "Trigger alias-to-table resolution is incomplete")
    trigger_before = len(failures)
    check_alias_columns(first_trigger, schema, {"d": "tr_departments"})
    check_alias_columns(second_trigger, schema, {"d": "tr_employees", "i": "tr_employees"})
    trigger_column_contract = len(failures) == trigger_before
    require(all(token in trigger for token in ("unrelated UPDATE", "same-DeptId UPDATE", "deleting the current head", "multi-row UPDATE")), "Trigger expected-case coverage is incomplete")

    alias_self_test = alias_column_self_test(schema)
    require(alias_self_test, "validator negative alias self-test failed")

    ids = ["TECH-A04", "TECH-A05", "TECH-A06", "TECH-A07", "UIT-O02", "UIT-O06"]
    for source_id in ids:
        ledger_url = source_url(source_id, ledger)
        rendered_url = rendered_source_url(source_id, app)
        require(ledger_url is not None, f"missing source ID in ledger: {source_id}")
        require(rendered_url is not None, f"missing rendered source ID: {source_id}")
        require(ledger_url == rendered_url, f"URL mismatch for {source_id}")

    visible_forbidden = ("CSDL_UIT · v1.1 proof", "D1 architecture proof", "bản proof D1", "D1 representative note", "Phase A evidence", "D1 patch")
    visible_text = re.sub(r"<script[\s\S]*?</script>", "", html, flags=re.I)
    require(not any(marker.lower() in visible_text.lower() for marker in visible_forbidden), "internal build copy remains in visible shell")
    require(not any(marker.lower() in app.lower() for marker in visible_forbidden), "internal build copy remains in rendered note strings")

    route_names = {"", "theory", "practice", "exercises", "exam-patterns", "search", "errors", "cheat-sheets", "sources", "theory/division", "theory/double-not-exists", "theory/rbtv-impact", "theory/closure", "practice/multi-row-trigger", "practice/lab-03"}
    # Only inspect literal hash routes; the search renderer's template URL is
    # intentionally dynamic and cannot be classified statically here.
    hrefs = re.findall(r'href="#/([a-z0-9][^"#${}]*)"', html + app, re.I)
    bad_routes = sorted({href for href in hrefs if href not in route_names})
    require(not bad_routes, f"broken internal route(s): {', '.join(bad_routes)}")
    require("linear-gradient" not in css, "gradient remains in site CSS")
    require("search-input" in app and "normalizeText" in app and "aria-live=\"polite\"" in app, "static search contract is incomplete")
    require("@media (max-width: 760px)" in css and "nav-toggle" in html, "mobile navigation contract is incomplete")
    require(":focus-visible" in css and "skip-link" in html, "keyboard/focus contract is incomplete")

    alias_resolution = lab_alias_resolution and trigger_alias_resolution
    print(f"ALIAS → TABLE RESOLUTION: {'PASS' if alias_resolution else 'FAIL'}")
    print(f"LAB03 COLUMN CONTRACT: {'PASS' if lab_column_contract else 'FAIL'}")
    print(f"TRIGGER COLUMN CONTRACT: {'PASS' if trigger_column_contract else 'FAIL'}")
    print(f"VALIDATOR NEGATIVE SELF-TEST: {'PASS' if alias_self_test else 'FAIL'}")
    print(f"LAB03 FIXTURE CONTRACT: {'PASS' if not any('Lab 03' in x or 'canonical table set' in x or 'unknown canonical table' in x or 'unknown column' in x or 'unknown table alias' in x or 'order fixture' in x or 'expected result' in x for x in failures) else 'FAIL'}")
    print(f"TRIGGER FIXTURE CONTRACT: {'PASS' if not any('Trigger' in x or 'trigger' in x or 'unknown column' in x or 'unknown table alias' in x for x in failures) else 'FAIL'}")
    print(f"SOURCE-ID SYNC: {'PASS' if not any('source ID' in x or 'missing source' in x for x in failures) else 'FAIL'}")
    print(f"SOURCE-URL SYNC: {'PASS' if not any('URL mismatch' in x for x in failures) else 'FAIL'}")
    print(f"VISIBLE INTERNAL BUILD COPY: {sum(marker.lower() in (visible_text + app).lower() for marker in visible_forbidden)}")
    print(f"GRADIENT CHECK: {'PASS' if 'linear-gradient' not in css else 'FAIL'}")
    print(f"BROKEN INTERNAL ROUTES: {len(bad_routes)}")
    print(f"SEARCH: {'PASS' if 'static search contract is incomplete' not in failures else 'FAIL'}")
    print(f"MOBILE: {'PASS' if 'mobile navigation contract is incomplete' not in failures else 'FAIL'}")
    print(f"KEYBOARD / FOCUS: {'PASS' if 'keyboard/focus contract is incomplete' not in failures else 'FAIL'}")
    if failures:
        print("FAILURES:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
