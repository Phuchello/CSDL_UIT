#!/usr/bin/env python3
"""
Validation script for IT004 Database Handbook repository.
Performs comprehensive checks on HTML structure, PDF metadata, page count, symbols, and repository safety.
"""

import hashlib
import os
from pathlib import Path
import re
import sys
from lxml import html
import pypdf

# Ensure standard UTF-8 console output
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "book" / "index.html"
CHAPTER_DIR = ROOT / "book" / "chapters"
PDF_PATH = ROOT / "dist" / "IT004_CSDL_UIT_CamNang_VoTrongPhuc.pdf"
KNOWLEDGE_MAP_SVG = ROOT / "assets" / "it004-knowledge-map.svg"

EXPECTED_SHA256 = "2fa50b54c553634c0408bfc6f5def71cf44e0961e5f74eea8198ece21821b25e"
EXPECTED_PAGES = 88
EXPECTED_TITLE = "IT004 – Cơ sở dữ liệu: Cẩm nang từ nền tảng đến Exam Mastery"
EXPECTED_AUTHOR = "Võ Trọng Phúc"
EXPECTED_SUBJECT = "IT004 – Cơ sở dữ liệu"

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


def validate():
    print("=== [1/6] Validating Chapter Sources ===")
    for ch in CHAPTERS:
        p = CHAPTER_DIR / ch
        assert p.exists(), f"Missing chapter: {ch}"
        print(f"  [OK] Found {ch}")

    print("\n=== [2/6] Validating HTML Assembly & Structure ===")
    assert INDEX_PATH.exists(), "book/index.html does not exist!"
    source = INDEX_PATH.read_text(encoding="utf-8")
    parser = html.HTMLParser(recover=True)
    doc = html.document_fromstring(source, parser=parser)
    assert not [e for e in parser.error_log if e.level_name == "FATAL"], "Fatal HTML parsing error"
    assert len(doc.xpath("/html/head")) == 1, "Missing /html/head"
    assert len(doc.xpath("/html/body")) == 1, "Missing /html/body"
    assert len(doc.xpath("//details")) == len(doc.xpath("//details[@open]")) == 33, "Not all 33 details are open"
    assert "NHANVIEN là quan hệ phụ trợ không thuộc lược đồ QLGV chuẩn" in source, "Missing Ex 13 framing"
    print("  [OK] HTML structure valid, 33/33 details open, schema framing verified")

    print("\n=== [3/6] Validating PDF Deliverable & Metadata ===")
    assert PDF_PATH.exists(), f"PDF deliverable missing at {PDF_PATH}"
    
    # Check SHA256
    h = hashlib.sha256()
    with open(PDF_PATH, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    actual_hash = h.hexdigest().lower()
    assert actual_hash == EXPECTED_SHA256, f"PDF SHA256 mismatch!\nExpected: {EXPECTED_SHA256}\nActual:   {actual_hash}"
    print(f"  [OK] PDF SHA256 matches approved release: {actual_hash}")

    # Check Metadata & Pages
    reader = pypdf.PdfReader(PDF_PATH, strict=True)
    assert len(reader.pages) == EXPECTED_PAGES, f"Page count mismatch: {len(reader.pages)} != {EXPECTED_PAGES}"
    meta = reader.metadata
    assert meta.title == EXPECTED_TITLE, f"Title mismatch: {meta.title}"
    assert meta.author == EXPECTED_AUTHOR, f"Author mismatch: {meta.author}"
    assert meta.subject == EXPECTED_SUBJECT, f"Subject mismatch: {meta.subject}"
    print(f"  [OK] PDF Page count: {len(reader.pages)} pages")
    print(f"  [OK] Title: {meta.title}")
    print(f"  [OK] Author: {meta.author}")
    print(f"  [OK] Subject: {meta.subject}")

    print("\n=== [4/6] Validating PDF Text & Mathematical Symbols ===")
    pages = [(page.extract_text() or "") for page in reader.pages]
    full_text = "\n".join(pages)
    assert all(len(t.strip()) > 100 for t in pages), "Found near-empty or blank page in PDF"
    for sym in ("π", "ρ", "∪", "⋈", "÷"):
        assert sym in full_text, f"Missing mathematical symbol in PDF: {sym}"
    print("  [OK] Mathematical and relational algebra symbols (π, ρ, ∪, ⋈, ÷) present")

    for num in range(1, 31):
        assert f"Câu {num}:" in full_text, f"Missing Exercise {num} in PDF"
    assert full_text.count("Lời giải chi tiết") >= 30, "Missing relational algebra solutions"
    print("  [OK] All 30/30 Relational Algebra exercises and detailed solutions verified")

    print("\n=== [5/6] Validating Final Section Ordering & Layout ===")
    def page_of(marker: str) -> int:
        return next(i for i, text in enumerate(pages, 1) if marker in text)

    assert page_of("Câu 13: (Ví dụ tổng quát)") == 39, "Ex 13 not on page 39"
    assert page_of("E. Recall Sheet - Ôn tập nhanh 1 trang") == 46, "Recall sheet not on page 46"
    assert "Recall Sheet" not in pages[44], "Orphan recall sheet title on page 45"
    assert "CREATE TABLE CTHD" not in pages[47], "CTHD split on page 48"
    assert all(m in pages[48] for m in ("CREATE TABLE CTHD", "FK_CTHD_HD", "FK_CTHD_SP")), "CTHD incomplete on page 49"
    
    order = [
        page_of("CHƯƠNG 7\nThực hành SQL Server"),
        page_of("Exam Playbook - Kỹ Năng Giải Đề Tốc Độ"),
        page_of("Cheat Sheet 6 Chương - Cứu Cánh Trước"),
        page_of("Nguồn tham khảo & Tài liệu đối chiếu"),
        page_of("IT004 – CƠ SỞ DỮ LIỆU"),
    ]
    assert order == [77, 83, 85, 87, 88], f"Unexpected section order: {order}"
    print("  [OK] Final section order verified: Ch7 (p77) -> Exam Playbook (p83) -> Cheat Sheet (p85) -> References (p87) -> Colophon (p88)")

    print("\n=== [6/6] Validating Repository Safety & Cleanliness ===")
    user_pat = r"C:\\" + r"Users\\"
    forbidden = [user_pat, r"/Users/", r"sk-[a-zA-Z0-9]{20,}", r"OPENAI_" + r"API_KEY", r"GEMINI_" + r"API_KEY"]
    
    for root, _, files in os.walk(ROOT):
        if ".git" in root or "dist" in root or "assets" in root or "node_modules" in root:
            continue
        for f in files:
            path = Path(root) / f
            if path == Path(__file__).resolve():
                continue
            content = path.read_text(encoding="utf-8", errors="ignore")
            for pat in forbidden:
                if re.search(pat, content, re.I):
                    assert False, f"Safety violation: Pattern '{pat}' found in {path.relative_to(ROOT)}"
    print("  [OK] Zero hardcoded private paths, zero leaked credentials in repository")

    assert KNOWLEDGE_MAP_SVG.exists(), f"Missing knowledge map SVG at {KNOWLEDGE_MAP_SVG}"
    print("  [OK] IT004 Knowledge Map SVG asset verified")

    print("\n==========================================")
    print("✅ ALL VALIDATION CHECKS PASSED (6/6)!")
    print("==========================================")


if __name__ == "__main__":
    validate()
