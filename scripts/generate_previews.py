#!/usr/bin/env python3
"""
Generate optimized preview images from the canonical PDF for GitHub showcase.
"""

from pathlib import Path
import sys
import pypdfium2 as pdfium
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
PDF_PATH = ROOT / "dist" / "IT004_CSDL_UIT_CamNang_VoTrongPhuc.pdf"
PREVIEW_DIR = ROOT / "assets" / "preview"

PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

if not PDF_PATH.exists():
    print(f"Error: Canonical PDF not found at {PDF_PATH}", file=sys.stderr)
    sys.exit(1)

pdf = pdfium.PdfDocument(PDF_PATH)
total_pages = len(pdf)
print(f"Loaded canonical PDF with {total_pages} pages.")

# 1. Generate Cover Image (Page 1)
cover_img = pdf[0].render(scale=2.0).to_pil().convert("RGB")
cover_out = PREVIEW_DIR / "cover.png"
cover_img.save(cover_out, optimize=True)
print(f"Saved cover preview: {cover_out} ({cover_img.width}x{cover_img.height})")

# 2. Generate Roadmap / Study Strategy Image (Page 6)
roadmap_img = pdf[5].render(scale=2.0).to_pil().convert("RGB")
roadmap_out = PREVIEW_DIR / "roadmap.png"
roadmap_img.save(roadmap_out, optimize=True)
print(f"Saved roadmap preview: {roadmap_out} ({roadmap_img.width}x{roadmap_img.height})")

# 3. Generate Handbook Showcase Montage (Pages 39, 49, 71)
# Page 39: Chapter 3 Relational Algebra (Ex 13 General Union)
# Page 49: Chapter 4 SQL DDL (CTHD Table definition)
# Page 71: Chapter 6 Functional Dependencies (3NF / BCNF Decomposition)
montage_pages = [39, 49, 71]
card_w = 400
card_h = 566  # roughly A4 ratio
spacing = 30
margin_x = 40
margin_y = 50

total_w = len(montage_pages) * card_w + (len(montage_pages) - 1) * spacing + margin_x * 2
total_h = card_h + margin_y * 2 + 50

# Canvas with subtle gradient or clean dark/neutral backdrop
canvas = Image.new("RGB", (total_w, total_h), "#0f172a")

draw = ImageDraw.Draw(canvas)

# Render each page with subtle drop shadow and border
for idx, p_num in enumerate(montage_pages):
    p_img = pdf[p_num - 1].render(scale=2.0).to_pil().convert("RGB")
    thumb = p_img.resize((card_w, card_h), Image.Resampling.LANCZOS)
    
    pos_x = margin_x + idx * (card_w + spacing)
    pos_y = margin_y + 35
    
    # Shadow
    shadow_box = Image.new("RGBA", (card_w + 16, card_h + 16), (0, 0, 0, 160))
    canvas.paste(shadow_box, (pos_x + 6, pos_y + 6), shadow_box)
    
    # Page Card
    canvas.paste(thumb, (pos_x, pos_y))

# Add Header Banner
title_text = "IT004 – CƠ SỞ DỮ LIỆU: CẨM NANG TỪ NỀN TẢNG ĐẾN EXAM MASTERY"
subtitle_text = "Bản xem trước các chuyên đề: Đại số quan hệ (Tr. 39) • T-SQL & Ràng buộc (Tr. 49) • Chuẩn hóa 3NF/BCNF (Tr. 71)"

# Simple centered text (or text line)
draw.text((margin_x, 20), title_text, fill="#38bdf8")
draw.text((margin_x, 42), subtitle_text, fill="#94a3b8")

montage_out = PREVIEW_DIR / "handbook-preview.png"
canvas.save(montage_out, optimize=True)
print(f"Saved handbook showcase preview: {montage_out} ({canvas.width}x{canvas.height})")

print("All preview assets generated successfully!")
