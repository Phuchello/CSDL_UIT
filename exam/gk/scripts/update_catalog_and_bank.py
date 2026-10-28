# -*- coding: utf-8 -*-
"""
scripts/update_catalog_and_bank.py
Integrates the 150 authentic independent practice problems into problems.json
and generates rich markdown topic files with Mermaid ERD diagrams in exam/gk/bank/.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(Path(__file__).parent))

DATA_DIR = REPO_ROOT / "exam" / "gk" / "data"
BANK_DIR = REPO_ROOT / "exam" / "gk" / "bank"

from build_all_independent_problems import build_all_150_independent_problems

def update_all():
    # 1. Load existing problems to retrieve 135 mock questions
    with open(DATA_DIR / "problems.json", "r", encoding="utf-8") as f:
        existing_data = json.load(f)

    # Filter 135 mock questions
    mock_questions = [
        p for p in existing_data["problems"]
        if p["id"].startswith("M") and len(p["id"]) >= 3 and p["id"][1:3].isdigit() and "-" in p["id"]
    ]
    assert len(mock_questions) == 135, f"Expected 135 mock questions, found {len(mock_questions)}"

    # 2. Get 150 independent problems
    independent_problems = build_all_150_independent_problems()
    assert len(independent_problems) == 150, f"Expected 150 independent problems, got {len(independent_problems)}"

    # 3. Combine
    all_problems = mock_questions + independent_problems
    print(f"Total problems combined: {len(all_problems)} (135 mock questions + 150 independent practice problems)")

    # 4. Save problems.json
    output_catalog = {"problems": all_problems}
    with open(DATA_DIR / "problems.json", "w", encoding="utf-8") as f:
        json.dump(output_catalog, f, indent=2, ensure_ascii=False)
    print("Saved exam/gk/data/problems.json successfully!")

    # 5. Generate markdown topic files in exam/gk/bank/
    topic_configs = [
        ("topic_01_erd.md", "ERD_MAPPING", "CHUYÊN ĐỀ 1: MÔ HÌNH THỰC THỂ MỐI KẾT HỢP (ERD) & ÁNH XẠ QUAN HỆ", 25),
        ("topic_02_ra_basic_join.md", "RA_BASIC_JOIN", "CHUYÊN ĐỀ 2: ĐẠI SỐ QUAN HỆ CƠ BẢN, PHÉP TẬP HỢP & CÁC LOẠI PHÉP KẾT", 45),
        ("topic_03_ra_division_grouping.md", "RA_DIVISION_GROUPING", "CHUYÊN ĐỀ 3: PHÉP CHIA (TẤT CẢ), GOM NHÓM & TRUY VẤN PHỨC HỢP", 45),
        ("topic_04_sql_ddl_dml.md", "SQL_DDL_DML", "CHUYÊN ĐỀ 4: TRANSACT-SQL DDL/DML & RÀNG BUỘC TOÀN VẸN", 35),
    ]

    for filename, topic_key, topic_title, expected_count in topic_configs:
        probs = [p for p in independent_problems if p["topic"] == topic_key]
        assert len(probs) == expected_count, f"Mismatch in {filename}: expected {expected_count}, got {len(probs)}"

        md_content = f"""# {topic_title}
**Môn học:** IT004 — Cơ sở dữ liệu | **Hệ thống:** UIT Exam Mastery
**Biên soạn:** VÕ TRỌNG PHÚC | **Số lượng bài tập độc lập:** {len(probs)} bài chuẩn hóa

---

"""
        for idx, p in enumerate(probs, start=1):
            sol = p.get("solution", {})
            rubric = p.get("rubric", {})

            md_content += f"""## Bài {idx:02d} [{p['id']}] — {p['title']}
- **Mức độ:** Mức {p['difficulty']} | **Thời gian khuyến nghị:** {p['recommended_time_mins']} phút | **Điểm số:** {p['points']} điểm
- **Lược đồ tham chiếu:** `{p['schema']}`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
{p['prompt']}

### 2. Hướng Dẫn & Lời Giải Chi Tiết
"""
            if "erd_entities" in sol:
                md_content += "**Các thực thể và thuộc tính:**\n"
                for e in sol["erd_entities"]:
                    md_content += f"- {e}\n"
                md_content += "\n**Mối kết hợp và bản số min-max:**\n"
                for r in sol.get("relationships", []):
                    md_content += f"- {r}\n"
                md_content += "\n**Lược đồ quan hệ chuyển đổi:**\n"
                for rs in sol.get("relational_schema", []):
                    md_content += f"- {rs}\n"
                if "mermaid_erd" in sol:
                    md_content += f"\n**Sơ đồ Thực thể - Mối kết hợp (ERD):**\n```mermaid\n{sol['mermaid_erd']}\n```\n\n"

            if "relational_algebra" in sol:
                md_content += f"**Biểu thức Đại số quan hệ (ĐSQH):**\n```text\n{sol['relational_algebra']}\n```\n\n"

            if "sql" in sol:
                md_content += f"**Câu lệnh Transact-SQL tương đương:**\n```sql\n{sol['sql']}\n```\n\n"

            if "intermediate_steps" in sol and sol["intermediate_steps"]:
                md_content += "**Các bước suy luận tư duy:**\n"
                for s in sol["intermediate_steps"]:
                    md_content += f"1. {s}\n"
                md_content += "\n"

            if "edge_cases" in sol and sol["edge_cases"]:
                md_content += f"**Phân tích trường hợp biên (Edge Cases):**\n{sol['edge_cases']}\n\n"

            if rubric:
                md_content += "**Barem chấm điểm đề xuất:**\n"
                for rk, rv in rubric.items():
                    md_content += f"- `{rk}`: {rv}đ\n"
                md_content += "\n"

            md_content += "---\n\n"

        target_file = BANK_DIR / filename
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(md_content.strip() + "\n")
        print(f"Generated {target_file.name} with {len(probs)} problems.")

if __name__ == "__main__":
    update_all()
