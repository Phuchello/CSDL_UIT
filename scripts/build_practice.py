#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compile IT004 Practical Handbook Phase C2 into a standalone index.html
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRACTICE_DIR = ROOT / "practice"
CHAPTERS_DIR = PRACTICE_DIR / "chapters"
OUTPUT_HTML = PRACTICE_DIR / "index.html"

CHAPTER_FILES = [
    "00_cover_toc.html",
    "01_environment_workflow.html",
    "02_ddl_dml_foundations.html",
    "03_basic_queries_and_joins.html",
    "04_aggregation_and_subqueries.html",
    "05_integrity_and_triggers.html",
    "09_lab01_ddl.html",
    "10_lab02_dml.html",
    "11_lab03_advanced.html",
    "12_lab04_analytics.html",
    "13_debugging_expanded.html",
    "14_appendices_exam.html",
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IT004 – Thực hành Cơ sở dữ liệu</title>
  <meta name="author" content="Võ Trọng Phúc">
  <meta name="subject" content="IT004 – Cơ sở dữ liệu — Sổ tay thực hành">
  <link rel="stylesheet" href="css/practice.css">
</head>
<body>
{body_content}
</body>
</html>
"""

def main():
    body_parts = []
    for fn in CHAPTER_FILES:
        fpath = CHAPTERS_DIR / fn
        if not fpath.exists():
            print(f"Error: Missing chapter file {fpath}", file=sys.stderr)
            sys.exit(1)
        content = fpath.read_text(encoding="utf-8")
        body_parts.append(content)

    full_html = HTML_TEMPLATE.format(body_content="\n\n".join(body_parts))
    OUTPUT_HTML.write_text(full_html, encoding="utf-8")
    print(f"Successfully compiled {len(CHAPTER_FILES)} practice chapters into {OUTPUT_HTML}")

if __name__ == "__main__":
    main()
