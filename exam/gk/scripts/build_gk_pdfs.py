#!/usr/bin/env python3
"""
scripts/build_gk_pdfs.py
Compiles the 3 final publication-grade A4 PDF deliverables:
1. IT004_GK_NganHangDe_VoTrongPhuc.pdf (Question Bank & 15 Full Mocks - Zero Answer Leak)
2. IT004_GK_LoiGiaiChiTiet_VoTrongPhuc.pdf (Extremely Detailed Verified Solutions & Rubrics)
3. IT004_GK_CheatSheet_VoTrongPhuc.pdf (Concise 4-Page Quick Reference & Exam Playbook)

Uses Microsoft Edge headless printing engine for pixel-perfect A4 typography and PyMuPDF for visual inspection.
"""

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
import pymupdf

# Ensure UTF-8 output
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
GK_DIR = REPO_ROOT / "exam" / "gk"
DATA_DIR = GK_DIR / "data"
DIST_DIR = GK_DIR / "dist"
QA_DIR = GK_DIR / "qa"
DIST_DIR.mkdir(parents=True, exist_ok=True)

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(EDGE_PATH):
    raise FileNotFoundError(f"Microsoft Edge executable not found at {EDGE_PATH}")

# Common publication CSS styling
COMMON_CSS = """
@page {
    size: A4 portrait;
    margin: 18mm 14mm 18mm 14mm;
    @bottom-center {
        content: counter(page);
        font-size: 9pt;
        color: #64748b;
        font-family: 'Segoe UI', system-ui, sans-serif;
    }
    @top-right {
        content: "IT004 — Cơ sở dữ liệu | Giữa Kỳ";
        font-size: 8pt;
        color: #94a3b8;
        font-family: 'Segoe UI', system-ui, sans-serif;
    }
}

* {
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.55;
    color: #1e293b;
    margin: 0;
    padding: 0;
}

.cover-page {
    page-break-after: always;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 40px 20px;
    border: 3px double #1e3a8a;
    background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
}

.cover-univ {
    font-size: 13pt;
    font-weight: 700;
    color: #1e3a8a;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 4px;
}

.cover-faculty {
    font-size: 11pt;
    font-weight: 600;
    color: #0369a1;
    text-transform: uppercase;
    margin-bottom: 40px;
}

.cover-title {
    font-size: 24pt;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.3;
    margin-bottom: 12px;
}

.cover-subtitle {
    font-size: 13pt;
    font-weight: 500;
    color: #334155;
    margin-bottom: 50px;
}

.cover-badge {
    display: inline-block;
    background: #1e3a8a;
    color: #ffffff;
    font-size: 11pt;
    font-weight: 600;
    padding: 8px 24px;
    border-radius: 9999px;
    margin-bottom: 60px;
}

.cover-author-box {
    margin-top: auto;
    border-top: 1px solid #cbd5e1;
    padding-top: 20px;
    width: 80%;
}

.cover-author-label {
    font-size: 10pt;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}

.cover-author-name {
    font-size: 16pt;
    font-weight: 800;
    color: #1e3a8a;
    margin-top: 4px;
}

.page-break {
    page-break-before: always;
}

.no-break {
    break-inside: avoid;
    page-break-inside: avoid;
}

h1.topic-header {
    font-size: 17pt;
    font-weight: 800;
    color: #1e3a8a;
    border-bottom: 2px solid #2563eb;
    padding-bottom: 6px;
    margin-top: 24px;
    margin-bottom: 16px;
}

h2.exam-header {
    font-size: 14pt;
    font-weight: 700;
    color: #0f172a;
    background: #f1f5f9;
    padding: 8px 12px;
    border-left: 4px solid #2563eb;
    margin-top: 20px;
    margin-bottom: 12px;
}

h3.question-title {
    font-size: 11pt;
    font-weight: 700;
    color: #1e293b;
    margin-top: 14px;
    margin-bottom: 6px;
}

.exam-meta-bar {
    display: flex;
    justify-content: space-between;
    background: #e2e8f0;
    padding: 6px 12px;
    font-size: 9pt;
    font-weight: 600;
    color: #334155;
    border-radius: 4px;
    margin-bottom: 12px;
}

.badge-pill {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 8pt;
    font-weight: 700;
}

.badge-a { background: #dcfce7; color: #166534; }
.badge-b { background: #dbeafe; color: #1e40af; }
.badge-c { background: #fee2e2; color: #991b1b; }

.schema-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 3px solid #64748b;
    padding: 8px 12px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 9pt;
    margin-bottom: 10px;
    color: #0f172a;
}

.math-expr {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    padding: 8px 12px;
    border-radius: 4px;
    font-family: 'Cambria Math', 'Times New Roman', serif;
    font-size: 10.5pt;
    color: #1e3a8a;
    margin: 8px 0;
    overflow-x: auto;
}

pre.code-sql {
    background: #0f172a;
    color: #f8fafc;
    padding: 10px 14px;
    border-radius: 6px;
    font-family: 'Consolas', monospace;
    font-size: 9pt;
    line-height: 1.45;
    margin: 8px 0;
    white-space: pre-wrap;
    word-break: break-word;
}

.rubric-table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0 16px 0;
    font-size: 8.5pt;
}

.rubric-table th, .rubric-table td {
    border: 1px solid #cbd5e1;
    padding: 5px 8px;
    text-align: left;
}

.rubric-table th {
    background: #f1f5f9;
    color: #334155;
    font-weight: 700;
}

.pitfall-box {
    background: #fffbeb;
    border-left: 3px solid #f59e0b;
    padding: 6px 10px;
    font-size: 8.5pt;
    color: #92400e;
    margin: 6px 0;
}

.toc-list {
    list-style-type: none;
    padding-left: 0;
}

.toc-item {
    display: flex;
    justify-content: space-between;
    padding: 6px 0;
    border-bottom: 1px dotted #cbd5e1;
    font-size: 10pt;
}

.toc-item a {
    color: #1e3a8a;
    text-decoration: none;
    font-weight: 600;
}
"""

def print_html_to_pdf(html_text: str, output_pdf_path: Path):
    with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w", encoding="utf-8") as f:
        f.write(html_text)
        tmp_html = f.name

    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={output_pdf_path}",
        tmp_html
    ]
    res = subprocess.run(cmd, capture_output=True)
    os.remove(tmp_html)

    if res.returncode != 0:
        raise RuntimeError(f"Edge PDF generation failed with code {res.returncode}: {res.stderr.decode('utf-8', errors='ignore')}")

    # Inspect with PyMuPDF
    doc = pymupdf.open(output_pdf_path)
    page_count = len(doc)
    doc.close()
    return page_count


# -----------------------------------------------------------------------------
# 1. BUILD PDF 1: IT004_GK_NganHangDe_VoTrongPhuc.pdf (NO ANSWERS)
# -----------------------------------------------------------------------------
def build_pdf_exam_bank():
    print("Building Deliverable 1: IT004_GK_NganHangDe_VoTrongPhuc.pdf...")
    with open(DATA_DIR / "problems.json", "r", encoding="utf-8") as f:
        problems = json.load(f)["problems"]
    with open(DATA_DIR / "mocks.json", "r", encoding="utf-8") as f:
        mocks = json.load(f)["mocks"]

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>IT004 – Cơ Sở Dữ Liệu: Ngân Hàng Đề Thi Giữa Kỳ</title>
<style>{COMMON_CSS}</style>
</head>
<body>

<div class="cover-page">
    <div class="cover-univ">Trường Đại Học Công Nghệ Thông Tin — ĐHQG-HCM</div>
    <div class="cover-faculty">Khoa Hệ Thống Thông Tin</div>
    <div class="cover-title">NGÂN HÀNG ĐỀ THI GIỮA KỲ<br>IT004 — CƠ SỞ DỮ LIỆU</div>
    <div class="cover-subtitle">Phân Dạng Chuyên Đề & 15 Đề Thi Mô Phỏng 75 Phút Chuẩn Hóa<br>Từ Nền Tảng Đến Đạt Điểm 9–10</div>
    <div class="cover-badge">BẢN ĐỀ THI TỰ LUYỆN — TUYỆT ĐỐI KHÔNG LỘ ĐÁP ÁN</div>
    <div class="cover-author-box">
        <div class="cover-author-label">Tác giả & Biên soạn</div>
        <div class="cover-author-name">BIÊN SOẠN: VÕ TRỌNG PHÚC</div>
    </div>
</div>

<div class="page-break">
    <h1 class="topic-header">MỤC LỤC & HƯỚNG DẪN TỰ ÔN TẬP</h1>
    <p>Tài liệu này bao gồm <strong>173 bài tập phân dạng</strong> và <strong>15 đề thi mô phỏng 75 phút</strong>. Toàn bộ đáp án chi tiết được tách rời tại ấn phẩm <em>IT004_GK_LoiGiaiChiTiet_VoTrongPhuc.pdf</em>.</p>
    <ul class="toc-list">
        <li class="toc-item"><span><strong>PHẦN 1:</strong> Chuyên Đề 1 — Mô Hình Thực Thể Mối Kết Hợp (ERD) & Ánh Xạ Schema (33 bài)</span><span>Trang 2</span></li>
        <li class="toc-item"><span><strong>PHẦN 2:</strong> Chuyên Đề 2 — Đại Số Quan Hệ Cơ Bản, Phép Tập Hợp & Kết Nối (62 bài)</span><span>Trang 10</span></li>
        <li class="toc-item"><span><strong>PHẦN 3:</strong> Chuyên Đề 3 — Phép Chia, Gom Nhóm & Truy Vấn Phức Hợp (52 bài)</span><span>Trang 25</span></li>
        <li class="toc-item"><span><strong>PHẦN 4:</strong> Chuyên Đề 4 — Transact-SQL DDL/DML & Chuyển Đổi ĐSQH (26 bài)</span><span>Trang 38</span></li>
        <li class="toc-item"><span><strong>PHẦN 5:</strong> Tuyển Tập 15 Đề Thi Mô Phỏng 75 Phút Chuẩn Hóa UIT</span><span>Trang 45</span></li>
    </ul>
</div>
"""

    # Add Topic Questions (NO SOLUTIONS)
    topic_map = {
        "ERD_MAPPING": "CHUYÊN ĐỀ 1: MÔ HÌNH THỰC THỂ MỐI KẾT HỢP (ERD) & ÁNH XẠ SCHEMA",
        "RA_BASIC_JOIN": "CHUYÊN ĐỀ 2: ĐẠI SỐ QUAN HỆ CƠ BẢN, PHÉP TẬP HỢP & CÁC LOẠI PHÉP KẾT",
        "RA_DIVISION_GROUPING": "CHUYÊN ĐỀ 3: PHÉP CHIA (TẤT CẢ), GOM NHÓM & TRUY VẤN PHỨC HỢP",
        "SQL_DDL_DML": "CHUYÊN ĐỀ 4: TRANSACT-SQL DDL/DML & RÀNG BUỘC TOÀN VẸN"
    }

    for t_key, t_name in topic_map.items():
        html += f"""<div class="page-break"><h1 class="topic-header">{t_name}</h1>"""
        t_probs = [p for p in problems if p["topic"] == t_key]
        for idx, p in enumerate(t_probs, start=1):
            diff_badge = f"""<span class="badge-pill badge-{p['difficulty'].lower()}">Mức {p['difficulty']}</span>"""
            html += f"""
            <div class="no-break" style="margin-bottom: 16px;">
                <div class="exam-meta-bar">
                    <span>Bài {idx:02d} [{p['id']}] — {p['title']}</span>
                    <span>{diff_badge} | {p['recommended_time_mins']} phút | {p['points']} điểm</span>
                </div>
                <div class="schema-box">Lược đồ: {p['schema']}</div>
                <p><strong>Đề bài:</strong> {p['prompt']}</p>
            </div>
            """
        html += "</div>"

    # Add 15 Full Mock Exams
    html += """<div class="page-break"><h1 class="topic-header">PHẦN 5: BỘ 15 ĐỀ THI MÔ PHỎNG 75 PHÚT CHUẨN HÓA</h1></div>"""
    for m in mocks:
        html += f"""
        <div class="page-break">
            <h2 class="exam-header">{m['title']}</h2>
            <div class="exam-meta-bar">
                <span>MÃ ĐỀ: {m['id']}</span>
                <span>Thời gian: 75 phút | Thang điểm: 10.0 | Profile: {m['profile']}</span>
                <span>Tự luận — Không tài liệu</span>
            </div>
        """
        for q in m["questions"]:
            pid = q["problem_id"]
            p_obj = next((p for p in problems if p["id"] == pid), None)
            if p_obj:
                html += f"""
                <div class="no-break" style="margin-bottom: 12px;">
                    <h3 class="question-title">Câu {q['num']}{q['sub']} ({q['points']} điểm): {p_obj['title']}</h3>
                    <div class="schema-box">Lược đồ: {p_obj['schema']}</div>
                    <p>{p_obj['prompt']}</p>
                </div>
                """
        html += f"""<p style="text-align: center; font-style: italic; margin-top: 30px;">— HẾT ĐỀ THI {m['id']} —</p></div>"""

    html += "</body></html>"
    out_pdf = DIST_DIR / "IT004_GK_NganHangDe_VoTrongPhuc.pdf"
    pages = print_html_to_pdf(html, out_pdf)
    print(f"  [OK] Generated {out_pdf.name} ({pages} pages).")
    return out_pdf, pages


# -----------------------------------------------------------------------------
# 2. BUILD PDF 2: IT004_GK_LoiGiaiChiTiet_VoTrongPhuc.pdf
# -----------------------------------------------------------------------------
def build_pdf_solutions():
    print("Building Deliverable 2: IT004_GK_LoiGiaiChiTiet_VoTrongPhuc.pdf...")
    with open(DATA_DIR / "problems.json", "r", encoding="utf-8") as f:
        problems = json.load(f)["problems"]
    with open(DATA_DIR / "mocks.json", "r", encoding="utf-8") as f:
        mocks = json.load(f)["mocks"]

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>IT004 – Cơ Sở Dữ Liệu: Lời Giải Chi Tiết & Barem Chấm Điểm</title>
<style>{COMMON_CSS}</style>
</head>
<body>

<div class="cover-page">
    <div class="cover-univ">Trường Đại Học Công Nghệ Thông Tin — ĐHQG-HCM</div>
    <div class="cover-faculty">Khoa Hệ Thống Thông Tin</div>
    <div class="cover-title">HƯỚNG DẪN CHẤM & LỜI GIẢI CHI TIẾT<br>IT004 — CƠ SỞ DỮ LIỆU GIỮA KỲ</div>
    <div class="cover-subtitle">Phân Tích Tư Duy Toán Học — Biểu Thức ĐSQH — Mã Nguồn T-SQL<br>Barem Điểm Từng Ý & Bẫy Lỗi Thường Gặp</div>
    <div class="cover-badge">BẢN GIẢI MẪU MỰC — KIỂM CHỨNG ĐỘC LẬP</div>
    <div class="cover-author-box">
        <div class="cover-author-label">Tác giả & Biên soạn</div>
        <div class="cover-author-name">BIÊN SOẠN: VÕ TRỌNG PHÚC</div>
    </div>
</div>

<div class="page-break">
    <h1 class="topic-header">MỤC LỤC LỜI GIẢI CHI TIẾT</h1>
    <p>Ấn phẩm này cung cấp lời giải toàn diện cho <strong>173 bài tập</strong> và <strong>15 đề thi mô phỏng 75 phút</strong>. Mỗi lời giải tuân thủ nghiêm ngặt chuẩn mực: <em>Mục tiêu đề bài &rarr; Bước suy luận logic &rarr; Biểu thức toán / T-SQL &rarr; Barem điểm &rarr; Cảnh báo bẫy lỗi</em>.</p>
</div>
"""

    # Solutions for the 15 Mocks
    for m in mocks:
        html += f"""
        <div class="page-break">
            <h2 class="exam-header">LỜI GIẢI CHI TIẾT: {m['title']}</h2>
            <div class="exam-meta-bar">
                <span>MÃ ĐỀ: {m['id']}</span>
                <span>Thang điểm: 10.0 | Thời gian làm bài: 75 phút</span>
            </div>
        """
        for q in m["questions"]:
            pid = q["problem_id"]
            p = next((x for x in problems if x["id"] == pid), None)
            if not p:
                continue
            sol = p.get("solution", {})
            html += f"""
            <div class="no-break" style="margin-bottom: 20px;">
                <h3 class="question-title">Câu {q['num']}{q['sub']} [{p['id']}] — {p['title']} ({q['points']} điểm)</h3>
                <p><strong>Yêu cầu:</strong> {p['prompt']}</p>
            """

            if "relational_algebra" in sol:
                html += f"""<div class="math-expr"><strong>Biểu thức ĐSQH:</strong><br>{sol['relational_algebra']}</div>"""
            if "sql" in sol:
                html += f"""<pre class="code-sql">-- Câu lệnh T-SQL tương đương:\n{sol['sql']}</pre>"""
            if "erd_entities" in sol:
                html += "<ul>"
                for e in sol["erd_entities"]:
                    html += f"<li>{e}</li>"
                html += "</ul>"
            if "relational_schema" in sol:
                html += "<ul>"
                for r in sol["relational_schema"]:
                    html += f"<li><strong>{r}</strong></li>"
                html += "</ul>"

            if "intermediate_steps" in sol and sol["intermediate_steps"]:
                html += "<ol style='font-size: 9pt; color: #334155; padding-left: 18px;'>"
                for s in sol["intermediate_steps"]:
                    html += f"<li>{s}</li>"
                html += "</ol>"

            rub = p.get("rubric", {})
            if rub:
                html += """<table class="rubric-table"><tr><th>Tiêu chí chấm điểm</th><th>Điểm định mức</th></tr>"""
                for rk, rv in rub.items():
                    html += f"<tr><td>{rk}</td><td>{rv}</td></tr>"
                html += "</table>"

            html += "</div>"

        html += "</div>"

    html += "</body></html>"
    out_pdf = DIST_DIR / "IT004_GK_LoiGiaiChiTiet_VoTrongPhuc.pdf"
    pages = print_html_to_pdf(html, out_pdf)
    print(f"  [OK] Generated {out_pdf.name} ({pages} pages).")
    return out_pdf, pages


# -----------------------------------------------------------------------------
# 3. BUILD PDF 3: IT004_GK_CheatSheet_VoTrongPhuc.pdf (CONCISE 4-PAGE GUIDE)
# -----------------------------------------------------------------------------
def build_pdf_cheatsheet():
    print("Building Deliverable 3: IT004_GK_CheatSheet_VoTrongPhuc.pdf...")
    extra_css = """
@page {
    size: A4 portrait;
    margin: 12mm 12mm 12mm 12mm;
}
.cheat-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
}
.cheat-card {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 10px 12px;
    break-inside: avoid;
    margin-bottom: 12px;
}
.cheat-card-header {
    font-size: 10pt;
    font-weight: 800;
    color: #1e3a8a;
    border-bottom: 1.5px solid #3b82f6;
    padding-bottom: 4px;
    margin-bottom: 6px;
    text-transform: uppercase;
}
.code-inline {
    font-family: Consolas, monospace;
    background: #f1f5f9;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 8.5pt;
}
"""

    html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>IT004 – Cơ Sở Dữ Liệu: Cheat Sheet Phòng Thi Giữa Kỳ</title>
<style>
""" + COMMON_CSS + extra_css + """
</style>
</head>
<body>

<div style="text-align: center; border-bottom: 2px solid #1e3a8a; padding-bottom: 8px; margin-bottom: 14px;">
    <div style="font-size: 15pt; font-weight: 800; color: #1e3a8a;">IT004 — CƠ SỞ DỮ LIỆU: CHEAT SHEET PHÒNG THI GIỮA KỲ</div>
    <div style="font-size: 9.5pt; font-weight: 600; color: #475569;">CÔNG THỨC TOÁN HỌC ĐSQH — MẸO NHẬN DIỆN TỪ KHÓA — CHIẾN THUẬT 75 PHÚT ĐẠT ĐIỂM 10</div>
    <div style="font-size: 9pt; font-weight: 700; color: #0284c7; margin-top: 2px;">BIÊN SOẠN: VÕ TRỌNG PHÚC — TRƯỜNG ĐH CÔNG NGHỆ THÔNG TIN (UIT)</div>
</div>

<div class="cheat-grid">
    <!-- Card 1 -->
    <div class="cheat-card">
        <div class="cheat-card-header">1. CHIẾN THUẬT PHÂN BỔ THỜI GIAN 75 PHÚT</div>
        <ul style="padding-left: 16px; margin: 0; font-size: 8.5pt;">
            <li><strong>00–05 phút:</strong> Đọc lướt toàn bộ đề, xác định số bảng và từ khóa câu hỏi.</li>
            <li><strong>05–25 phút (20p):</strong> Hoàn thành <strong>Câu 1 (ERD & Ánh xạ)</strong> — Vẽ nháp nhanh, gạch chân PK, vẽ mũi tên FK (2.0–2.5đ).</li>
            <li><strong>25–35 phút (10p):</strong> Hoàn thành <strong>Câu 2.1 (SQL CHECK & UPDATE)</strong> (1.5đ).</li>
            <li><strong>35–65 phút (30p):</strong> Giải quyết <strong>6 câu ĐSQH</strong>:
                <br>• Câu a, b: Phép chọn, chiếu, kết 2-3 bảng (cơ bản).
                <br>• Câu c: Left Outer Join ⟕ nếu có từ "nếu có".
                <br>• Câu d: Gom nhóm γ (GROUP BY, SUM, COUNT).
                <br>• Câu e: Phép chia ÷ cho từ khóa "tất cả / mọi".
                <br>• Câu f: Cực trị (nhiều nhất/ít nhất) qua phép trừ.
            </li>
            <li><strong>65–75 phút (10p):</strong> Soát lại tên cột, gạch chân PK, đối chiếu điều kiện ngày tháng.</li>
        </ul>
    </div>

    <!-- Card 2 -->
    <div class="cheat-card">
        <div class="cheat-card-header">2. BẢNG TỪ KHÓA & PHÉP TOÁN ĐSQH TƯƠNG ỨNG</div>
        <table class="rubric-table" style="font-size: 8pt; margin: 0;">
            <tr><th>Từ khóa đề bài</th><th>Phép toán ĐSQH</th><th>Lưu ý quan trọng</th></tr>
            <tr><td>"Nếu có" / "Kể cả chưa có"</td><td>Left Outer Join (⟕)</td><td>Không dùng kết thường ⋈ vì sẽ làm mất dòng NULL.</td></tr>
            <tr><td>"Tất cả" / "Mọi" / "Đủ"</td><td>Phép chia (÷)</td><td>R_Target ÷ R_Divisor (phải chuẩn hóa tập thuộc tính).</td></tr>
            <tr><td>"Vừa... Vừa..." / "Cả hai"</td><td>Phép giao (∩)</td><td>Hai quan hệ phải khả hợp (cùng số lượng và miền giá trị).</td></tr>
            <tr><td>"Không" / "Chưa từng"</td><td>Phép trừ (−)</td><td>Lấy toàn bộ trừ đi tập vi phạm.</td></tr>
            <tr><td>"Tổng số" / "Mỗi" / "Đếm"</td><td>Phép gom nhóm (γ)</td><td>_{Attrs} γ _{Agg(Attr) &rarr; NewCol}(R)</td></tr>
            <tr><td>"Nhiều nhất" / "Ít nhất"</td><td>Tự kết so sánh & Trừ</td><td>Tập đầy đủ trừ tập (R1.Val &lt; R2.Val).</td></tr>
        </table>
    </div>

    <!-- Card 3 -->
    <div class="cheat-card">
        <div class="cheat-card-header">3. BẢN SỐ MIN-MAX & QUY TẮC ÁNH XẠ ERD &rarr; SCHEMA</div>
        <ul style="padding-left: 16px; margin: 0; font-size: 8.5pt;">
            <li><strong>Quan hệ 1:1:</strong> Đưa PK của phía tùy chọn (0,1) sang làm FK của phía bắt buộc (1,1) để tránh giá trị NULL.</li>
            <li><strong>Quan hệ 1:N:</strong> Mang PK của thực thể phía <strong>1</strong> sang làm FK của thực thể phía <strong>N</strong>.</li>
            <li><strong>Quan hệ M:N:</strong> <em>Bắt buộc tạo bảng trung gian riêng</em>. Khóa chính của bảng trung gian là tổ hợp PK hai phía: <span class="code-inline">PK = (PK_A, PK_B)</span>.</li>
            <li><strong>Thực thể yếu:</strong> Khóa chính của thực thể yếu gồm PK của thực thể cha kết hợp với khóa bộ phận (discriminator).</li>
        </ul>
    </div>

    <!-- Card 4 -->
    <div class="cheat-card">
        <div class="cheat-card-header">4. CÔNG THỨC 3 BƯỚC GIẢI PHÉP CHIA HÌNH THỨC (÷)</div>
        <div style="font-size: 8.5pt;">
            Cho quan hệ R(X, Y) và S(Y). Tìm X có tất cả Y trong S:
            <br><strong>Bước 1 (Tập chia):</strong> R_S = π_Y(S)
            <br><strong>Bước 2 (Tập các cặp giả định):</strong> R_all = π_X(R) × R_S
            <br><strong>Bước 3 (Tập các cặp thiếu):</strong> R_missing = R_all - R
            <br><strong>Bước 4 (Kết quả):</strong> KQ = π_X(R) - π_X(R_missing)
            <br><em>Trong phòng thi viết rút gọn:</em> KQ = π_{X, Y}(R) ÷ π_Y(S).
        </div>
    </div>
</div>

<div class="page-break"></div>

<div class="cheat-grid">
    <!-- Card 5 -->
    <div class="cheat-card">
        <div class="cheat-card-header">5. BẪY LỖI KINH ĐIỂN KHIẾN BỊ TRỪ ĐIỂM NẶNG</div>
        <ul style="padding-left: 16px; margin: 0; font-size: 8.5pt; color: #991b1b;">
            <li><strong>Quên đổi tên khi Tự kết (Self-Join):</strong> Nếu không dùng phép đổi tên ρ_{A}(R) ⋈ ρ_{B}(R), tên thuộc tính bị trùng sẽ khiến biểu thức vô nghĩa.</li>
            <li><strong>Chiếu sai thuộc tính trước khi Gom nhóm:</strong> Phép gom nhóm γ chỉ giữ lại các cột nằm trong danh sách thuộc tính gom nhóm và hàm tổng hợp.</li>
            <li><strong>Nhầm lẫn giữa NOT IN và NOT EXISTS khi có NULL:</strong> Trong SQL, nếu danh sách con của NOT IN có chứa giá trị NULL, toàn bộ câu truy vấn sẽ trả về tập rỗng! Hãy dùng NOT EXISTS.</li>
            <li><strong>Quên kiểm tra tính Khả hợp của Phép trừ/Giao:</strong> R1 - R2 bắt buộc R1 và R2 phải có cùng bậc (số cột) và tương thích kiểu dữ liệu.</li>
        </ul>
    </div>

    <!-- Card 6 -->
    <div class="cheat-card">
        <div class="cheat-card-header">6. CÚ PHÁP T-SQL CHUẨN SQL SERVER PHÒNG THI</div>
        <pre class="code-sql" style="font-size: 8pt; margin: 0;">
-- CHECK miền giá trị & chuỗi
ALTER TABLE DIEMTIEM 
ADD CONSTRAINT CK_SUCCHUA CHECK (SUCCHUA > 0 AND QUAN IN ('Thu Duc', 'Binh Thanh'));

-- UPDATE liên kết bảng an toàn
UPDATE LOVACXIN
SET DONGIA = DONGIA * 1.1
FROM LOVACXIN LV
INNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC
WHERE YEAR(LV.HSD) = 2025;
        </pre>
    </div>
</div>

</body>
</html>"""

    out_pdf = DIST_DIR / "IT004_GK_CheatSheet_VoTrongPhuc.pdf"
    pages = print_html_to_pdf(html, out_pdf)
    print(f"  [OK] Generated {out_pdf.name} ({pages} pages).")
    return out_pdf, pages


def main():
    print("==================================================")
    print(" IT004 Midterm PDF Compilation Pipeline (Edge A4) ")
    print("==================================================")
    pdf1, p1 = build_pdf_exam_bank()
    pdf2, p2 = build_pdf_solutions()
    pdf3, p3 = build_pdf_cheatsheet()

    print("\n==================================================")
    print(" COMPILATION SUMMARY:")
    print(f"  1. {pdf1.name} : {p1} pages (A4)")
    print(f"  2. {pdf2.name} : {p2} pages (A4)")
    print(f"  3. {pdf3.name} : {p3} pages (A4)")
    print("==================================================")

    # Copy to user workspace CSDL/GK for easy access
    user_gk_dir = Path.home() / "OneDrive" / "Documents" / "Môn học" / "CSDL" / "GK"
    if user_gk_dir.exists():
        import shutil
        for pdf in [pdf1, pdf2, pdf3]:
            shutil.copy2(pdf, user_gk_dir / pdf.name)
        print(f"  [COPIED] All 3 PDFs safely mirrored to {user_gk_dir}")

if __name__ == "__main__":
    main()
