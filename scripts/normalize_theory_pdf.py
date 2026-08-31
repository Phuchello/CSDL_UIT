"""Rewrite the deterministic theory PDF with one authoritative metadata dictionary."""

import os
from pathlib import Path

from pypdf import PdfReader, PdfWriter


PDF_PATH = Path(__file__).resolve().parents[1] / "dist" / "IT004_CSDL_UIT_LyThuyet_VoTrongPhuc.pdf"
TEMP_PATH = PDF_PATH.with_suffix(".normalized.pdf")


def main() -> None:
    reader = PdfReader(str(PDF_PATH))
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata(
        {
            "/Title": "IT004 – Cơ sở dữ liệu: Cẩm nang từ nền tảng đến Exam Mastery",
            "/Author": "Võ Trọng Phúc",
            "/Subject": "IT004 – Cơ sở dữ liệu",
        }
    )
    with TEMP_PATH.open("wb") as stream:
        writer.write(stream)
    os.replace(TEMP_PATH, PDF_PATH)
    print(f"rewrote {PDF_PATH} ({PDF_PATH.stat().st_size} bytes, {len(reader.pages)} pages)")


if __name__ == "__main__":
    main()
