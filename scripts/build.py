#!/usr/bin/env python3
"""
Build script to compile individual chapter HTML files into the single canonical book/index.html.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
CHAPTER_DIR = ROOT / "book" / "chapters"
OUTPUT = ROOT / "book" / "index.html"

CHAPTERS = [
    "ch00_intro.html",
    "ch01_overview.html",
    "ch02_er_relational.html",
    "ch03_relational_algebra.html",
    "ch04_sql.html",
    "ch05_constraints.html",
    "ch06_fd_normalization.html",
    "ch07_practical.html",
    "exam_playbook.html",
    "cheat_sheet.html",
    "references.html",
]

HEAD = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IT004 – Cơ sở dữ liệu — Sổ tay lý thuyết</title>
  <meta name="author" content="Võ Trọng Phúc">
  <meta name="description" content="IT004 – Cơ sở dữ liệu — Sổ tay lý thuyết">
  <meta name="keywords" content="IT004, Cơ sở dữ liệu, Database, UIT, SQL Server, Đại số quan hệ, Võ Trọng Phúc">
  <link rel="stylesheet" href="css/book.css">
</head>
<body>
"""


def extract_fragment(path: Path) -> str:
    text = path.read_text(encoding="utf-8").strip()
    body = re.search(r"<body[^>]*>(.*?)</body>", text, re.I | re.S)
    if body:
        text = body.group(1).strip()
    # Ensure details elements remain expanded for print and complete online reading
    text = re.sub(r"<details(?![^>]*\bopen\b)", "<details open", text)
    return text


def build_book():
    parts = [HEAD]
    for name in CHAPTERS:
        chapter_path = CHAPTER_DIR / name
        if not chapter_path.exists():
            print(f"Error: Missing chapter file {chapter_path}", file=sys.stderr)
            sys.exit(1)
        parts.append(f"\n<!-- === {name} === -->\n")
        parts.append(extract_fragment(chapter_path))
        parts.append("\n")
    parts.append("</body>\n</html>\n")
    
    OUTPUT.write_text("".join(parts), encoding="utf-8")
    print(f"Successfully compiled {len(CHAPTERS)} chapters into {OUTPUT}")


if __name__ == "__main__":
    build_book()
