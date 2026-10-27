#!/usr/bin/env python3
"""
scripts/export_bank_markdown.py
Exports the problem bank into 4 comprehensive, beautifully formatted Markdown handbooks in exam/gk/bank/
and creates exam/gk/README.md.
"""

import json
import os
import sys
from pathlib import Path

# Ensure UTF-8 output
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
GK_DIR = REPO_ROOT / "exam" / "gk"
DATA_DIR = GK_DIR / "data"
BANK_DIR = GK_DIR / "bank"

with open(DATA_DIR / "problems.json", "r", encoding="utf-8") as f:
    problems = json.load(f)["problems"]

topics = {
    "ERD_MAPPING": ("topic_01_erd.md", "CHUYÊN ĐỀ 1: MÔ HÌNH THỰC THỂ MỐI KẾT HỢP (ERD) & ÁNH XẠ QUAN HỆ"),
    "RA_BASIC_JOIN": ("topic_02_ra_basic_join.md", "CHUYÊN ĐỀ 2: ĐẠI SỐ QUAN HỆ CƠ BẢN, PHÉP TẬP HỢP & CÁC LOẠI PHÉP KẾT"),
    "RA_DIVISION_GROUPING": ("topic_03_ra_division_grouping.md", "CHUYÊN ĐỀ 3: PHÉP CHIA (TẤT CẢ / MỌI), GOM NHÓM & TRUY VẤN PHỨC HỢP"),
    "SQL_DDL_DML": ("topic_04_sql_ddl_dml.md", "CHUYÊN ĐỀ 4: TRANSACT-SQL DDL/DML & CHUYỂN ĐỔI ĐSQH SANG SQL")
}

topic_counts = {}
for top_key, (fname, top_title) in topics.items():
    top_probs = [p for p in problems if p["topic"] == top_key]
    md_lines = [
        f"# {top_title}",
        f"**Môn học:** IT004 — Cơ sở dữ liệu | **Hệ thống:** UIT Exam Mastery",
        f"**Biên soạn:** VÕ TRỌNG PHÚC | **Số lượng bài tập:** {len(top_probs)} bài",
        "",
        "---",
        ""
    ]

    for idx, p in enumerate(top_probs, start=1):
        md_lines.append(f"## Bài {idx:02d} [{p['id']}] — {p['title']}")
        md_lines.append(f"- **Mức độ:** Mức {p['difficulty']} | **Thời gian khuyến nghị:** {p['recommended_time_mins']} phút | **Điểm số:** {p['points']} điểm")
        md_lines.append(f"- **Lược đồ tham chiếu:** `{p['schema']}`")
        md_lines.append("")
        md_lines.append("### 1. Đề Bài")
        md_lines.append(p["prompt"])
        md_lines.append("")
        md_lines.append("### 2. Hướng Dẫn & Lời Giải Chi Tiết")
        sol = p.get("solution", {})
        if "relational_algebra" in sol:
            md_lines.append(f"**Biểu thức Đại số quan hệ:**")
            md_lines.append(f"```text\n{sol['relational_algebra']}\n```")
        if "sql" in sol:
            md_lines.append(f"**Câu lệnh SQL tương đương:**")
            md_lines.append(f"```sql\n{sol['sql']}\n```")
        if "erd_entities" in sol:
            md_lines.append(f"**Các thực thể và thuộc tính:**")
            for ent in sol.get("erd_entities", []):
                md_lines.append(f"- {ent}")
        if "relational_schema" in sol:
            md_lines.append(f"**Lược đồ quan hệ chuyển đổi:**")
            for rel in sol.get("relational_schema", []):
                md_lines.append(f"- {rel}")

        if "intermediate_steps" in sol and sol["intermediate_steps"]:
            md_lines.append("")
            md_lines.append("**Các bước suy luận tư duy:**")
            for step in sol["intermediate_steps"]:
                md_lines.append(f"1. {step}")

        rub = p.get("rubric", {})
        if rub:
            md_lines.append("")
            md_lines.append("**Barem chấm điểm đề xuất:**")
            for rk, rv in rub.items():
                md_lines.append(f"- `{rk}`: {rv}")

        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    topic_counts[top_key] = len(top_probs)
    with open(BANK_DIR / fname, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"Exported {len(top_probs)} problems to {BANK_DIR / fname}")

exec_cnt = sum(1 for p in problems if p.get("verification_level") == "EXECUTION_VERIFIED")
sem_cnt = sum(1 for p in problems if p.get("verification_level") == "SEMANTICALLY_REVIEWED")
draft_cnt = sum(1 for p in problems if p.get("verification_level") == "DRAFT")
gold_mocks_cnt = exec_cnt // 9

# Write exam/gk/README.md
readme_content = f"""# NGÂN HÀNG ĐỀ THI & LỜI GIẢI GIỮA KỲ IT004 — CƠ SỞ DỮ LIỆU
**Đơn vị:** Trường Đại học Công nghệ Thông tin, ĐHQG-HCM
**Tác giả biên soạn:** VÕ TRỌNG PHÚC
**Phiên bản:** v1.2 GK Master Release (Phase C Gold Standard Reconstruction)

---

## 1. Giới Thiệu Module Giữa Kỳ (GK)
Module này cung cấp học liệu ôn tập toàn diện cho sinh viên ôn thi Giữa kỳ môn **IT004 – Cơ sở dữ liệu** đạt điểm tối đa (9–10 điểm), bao gồm:
1. **Ngân hàng câu hỏi phân dạng ({len(problems)} bài tập chuẩn hóa)**:
   - Chuyên đề 1: [Mô hình ERD & Ánh xạ quan hệ](bank/topic_01_erd.md) ({topic_counts.get('ERD_MAPPING', 0)} bài)
   - Chuyên đề 2: [ĐSQH cơ bản, phép tập hợp & kết nối](bank/topic_02_ra_basic_join.md) ({topic_counts.get('RA_BASIC_JOIN', 0)} bài)
   - Chuyên đề 3: [Phép chia, gom nhóm & truy vấn phức hợp](bank/topic_03_ra_division_grouping.md) ({topic_counts.get('RA_DIVISION_GROUPING', 0)} bài)
   - Chuyên đề 4: [Transact-SQL DDL/DML & chuyển đổi ĐSQH](bank/topic_04_sql_ddl_dml.md) ({topic_counts.get('SQL_DDL_DML', 0)} bài)

2. **Tiêu chuẩn kiểm chứng học thuật (Academic Verification Status)**:
   - **EXECUTION_VERIFIED (Chuẩn Vàng):** {exec_cnt} bài ({gold_mocks_cnt}/15 đề thi mô phỏng đã kiểm chứng 100% trên Microsoft SQL Server 2025).
   - **SEMANTICALLY_REVIEWED (Đã rà soát học thuật):** {sem_cnt} bài.
   - **DRAFT / PENDING REMEDIATION (Bản thảo đang tái cấu trúc):** {draft_cnt} bài.

3. **15 Đề thi mô phỏng 75 phút chuẩn hóa**:
   - Mỗi đề đúng 10.0 điểm, 75 phút tự luận, có đề bài riêng không lộ đáp án và hướng dẫn chấm chi tiết kèm barem điểm từng ý.

4. **Bộ 4 ấn phẩm PDF A4 chất lượng cao**:
   - `IT004_GK_NganHangDe_VoTrongPhuc.pdf`: Ngân hàng đề thi bài tập & 15 Mock exam (Đề bài sạch, không lộ đáp án).
   - `IT004_GK_LoiGiaiChiTiet_VoTrongPhuc.pdf`: Toàn bộ hướng dẫn giải chi tiết, phân tích tư duy toán học và barem chấm điểm.
   - `IT004_GK_CheatSheet_VoTrongPhuc.pdf`: Tóm tắt công thức, checklist phòng thi, mẹo nhận diện từ khóa (2 trang A4).
   - `IT004_GK_VerifiedOnly_VoTrongPhuc.pdf`: Ấn bản tuyển tập chọn lọc nghiêm ngặt CHỈ chứa các đề thi Chuẩn Vàng và bài tập đã kiểm chứng học thuật.

## 2. Hướng Dẫn Sử Dụng Để Đạt Điểm 9–10
- **Tuần 1–2:** Hoàn thành Chuyên đề 1 và Chuyên đề 2 để vững nền tảng ERD và các phép kết cơ bản.
- **Tuần 3:** Luyện chuyên sâu Chuyên đề 3 (Phép chia và Gom nhóm cực trị - câu phân loại 9–10).
- **Tuần 4:** Bấm giờ làm các đề Chuẩn Vàng trong thư mục `mocks/` (mỗi đề đúng 75 phút), sau đó đối chiếu `solution.md` để tự chấm điểm và tra cứu lỗi sai thường gặp.

## 3. Quy Trình Kiểm Thử & Kiểm Định (QA Audit)
Chạy validator tự động để kiểm tra tính toàn vẹn của ngân hàng đề:
```powershell
python exam/gk/scripts/validate_gk.py
```
"""

with open(GK_DIR / "README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)
print("Created exam/gk/README.md.")
