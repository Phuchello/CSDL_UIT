#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Normalize metadata for IT004 Practical Handbook Phase C1 Design Proof PDF.
"""

from pathlib import Path
import pypdf

ROOT = Path(__file__).resolve().parent.parent
PDF_PATH = ROOT / "dist" / "proofs" / "IT004_CSDL_UIT_v1.1_Practice_DesignProof.pdf"

def main():
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Missing PDF at {PDF_PATH}")

    reader = pypdf.PdfReader(str(PDF_PATH))
    writer = pypdf.PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata({
        "/Title": "IT004 – Cơ sở dữ liệu",
        "/Author": "Võ Trọng Phúc",
        "/Subject": "IT004 – Cơ sở dữ liệu — Sổ tay thực hành",
        "/Producer": "pypdf",
    })

    with open(PDF_PATH, "wb") as f:
        writer.write(f)

    print(f"rewrote {PDF_PATH} ({PDF_PATH.stat().st_size} bytes, {len(reader.pages)} pages)")

if __name__ == "__main__":
    main()
