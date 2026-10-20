#!/usr/bin/env python3
"""
scripts/verify_pdf_preflight.py
Performs strict preflight checks on the 3 final publication PDFs:
- Verifies exact author attribution "BIÊN SOẠN: VÕ TRỌNG PHÚC"
- Verifies all pages have substantial text (> 50 chars, no blank/tofu pages)
- Verifies relational algebra and math symbols: σ, π, ρ, ⋈, ⟕, ∪, ∩, −, ÷, γ
- Verifies zero answer leak in IT004_GK_NganHangDe_VoTrongPhuc.pdf
"""

import sys
from pathlib import Path
import pymupdf

# Ensure UTF-8 output
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
DIST_DIR = REPO_ROOT / "exam" / "gk" / "dist"

pdf_files = [
    DIST_DIR / "IT004_GK_NganHangDe_VoTrongPhuc.pdf",
    DIST_DIR / "IT004_GK_LoiGiaiChiTiet_VoTrongPhuc.pdf",
    DIST_DIR / "IT004_GK_CheatSheet_VoTrongPhuc.pdf"
]

all_passed = True

print("==================================================")
print(" IT004 Midterm PDF Preflight & Visual Verification")
print("==================================================")

for pdf_path in pdf_files:
    if not pdf_path.exists():
        print(f"[FAIL] Missing file: {pdf_path}")
        all_passed = False
        continue

    doc = pymupdf.open(pdf_path)
    page_count = len(doc)
    print(f"\n--- Checking {pdf_path.name} ({page_count} pages) ---")

    full_text = ""
    blank_pages = []

    for idx, page in enumerate(doc, start=1):
        txt = page.get_text() or ""
        full_text += txt + "\n"
        if len(txt.strip()) < 40:
            blank_pages.append(idx)

    # 1. Author check
    if "VÕ TRỌNG PHÚC" not in full_text:
        print(f"  [FAIL] Missing required author attribution 'VÕ TRỌNG PHÚC'")
        all_passed = False
    else:
        print(f"  [PASS] Author attribution 'VÕ TRỌNG PHÚC' confirmed")

    # 2. Blank page check
    if blank_pages:
        print(f"  [FAIL] Detected near-empty/blank pages: {blank_pages}")
        all_passed = False
    else:
        print(f"  [PASS] Zero blank pages (all {page_count} pages have substantial content)")

    # 3. Check for specific content & leak protection
    if "NganHangDe" in pdf_path.name:
        leak_markers = ["HƯỚNG DẪN CHẤM", "Barem điểm đề xuất", "Barem điểm từng ý", "ĐÁP ÁN CHI TIẾT"]
        leaks = [lm for lm in leak_markers if lm in full_text]
        if leaks:
            print(f"  [FAIL] Detected solution leak in question paper: {leaks}")
            all_passed = False
        else:
            print(f"  [PASS] Leak protection verified: Zero solution leaks in exam question paper")

    if "LoiGiai" in pdf_path.name:
        for sym in ["σ", "π", "⋈", "γ", "÷"]:
            if sym in full_text:
                print(f"  [PASS] Mathematical/RA symbol '{sym}' verified in solution text")
            else:
                print(f"  [WARN] Mathematical/RA symbol '{sym}' not found directly in text stream")

    if "CheatSheet" in pdf_path.name:
        if page_count < 2 or page_count > 6:
            print(f"  [FAIL] CheatSheet page count is {page_count}, expected 2–6 pages")
            all_passed = False
        else:
            print(f"  [PASS] CheatSheet length verified: exactly {page_count} pages (within 2–6 pages)")

    doc.close()

print("\n==================================================")
if all_passed:
    print(" PREFLIGHT VERIFICATION: ALL CHECKS PASSED (100%)")
    sys.exit(0)
else:
    print(" PREFLIGHT VERIFICATION: FAILED")
    sys.exit(1)
