#!/usr/bin/env python3
"""Rewrite the final practical PDF with stable metadata and xref tables."""
from pathlib import Path
import os
import tempfile
import json
import pypdf

ROOT = Path(__file__).resolve().parent.parent
PDF_PATH = ROOT / "dist" / "IT004_CSDL_UIT_ThucHanh_VoTrongPhuc.pdf"

def main():
    if not PDF_PATH.exists():
        raise FileNotFoundError(PDF_PATH)
    reader = pypdf.PdfReader(str(PDF_PATH), strict=False)
    writer = pypdf.PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata({
        "/Title": "IT004 – Thực hành Cơ sở dữ liệu",
        "/Author": "Võ Trọng Phúc",
        "/Subject": "IT004 – Cơ sở dữ liệu — Sổ tay thực hành",
        "/Producer": "pypdf",
    })
    fd, temp_name = tempfile.mkstemp(prefix="it004-practice-", suffix=".pdf", dir=str(PDF_PATH.parent))
    os.close(fd)
    try:
        with open(temp_name, "wb") as out:
            writer.write(out)
        os.replace(temp_name, PDF_PATH)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
    check = pypdf.PdfReader(str(PDF_PATH), strict=True)
    print(f"rewrote {PDF_PATH} ({PDF_PATH.stat().st_size} bytes, {len(check.pages)} pages)")
    print(json.dumps({str(k): str(v) for k, v in (check.metadata or {}).items()}, ensure_ascii=True))

if __name__ == "__main__":
    main()
