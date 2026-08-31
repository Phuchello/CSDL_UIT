# Báo Cáo Kiểm Thử Toàn Vẹn Giai Đoạn A (Phase A Validation Report) — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31
**Mục đích:** Báo cáo kiểm thử cơ học, tính toán số liệu và kiểm tra chéo toàn bộ các hồ sơ nghiên cứu Giai đoạn A trước khi bàn giao cho Hội đồng thẩm định (Mentor).

---

SOURCE IDS:
PASS

UNDEFINED SOURCE IDS:
None (Tất cả 51 `source_id` được tham chiếu trong toàn bộ thư mục `research/v1.1_phase_a/` đều được định nghĩa tường minh tại `source_inventory.md`).

MIS-MAPPED SOURCE IDS:
None (Toàn bộ các tham chiếu Microsoft `TECH-A01` đến `TECH-A11` đã được chuẩn hóa: `TECH-A07` dành riêng cho EXISTS/Subquery, `TECH-A08` dành cho UNION/Set Operators, `TECH-A09` dành cho PROCEDURE, `TECH-A10` dành cho VIEW, `TECH-A11` dành cho FUNCTION; không còn hiện tượng gán nhầm mã nguồn kỹ thuật).

CANONICAL ARTIFACT IDS:
PASS

DUPLICATE ARTIFACT IDS:
None (Toàn bộ 17 Canonical Artifact IDs: `EXAM-*` (11), `PRAC-*` (2), `REV-*` (3), `LAB-*` (1) là duy nhất, không trùng lặp).

EXAM ARTIFACT COUNTS:
PASS

ROWS WITH COUNT MISMATCH:
None (Trong `exam_pattern_map.md` và `essay_bank_plan.md`, `artifact_count` của từng hàng bằng chính xác số lượng ID hiện vật đề thi duy nhất `EXAM-*` hoặc `PRAC-*` được liệt kê trong hàng đó; tài liệu `REV-*` và `LAB-*` không làm tăng `artifact_count`).

DIRECT EXAM URL COVERAGE:
Đầy đủ các liên kết trực tiếp cấp tài liệu (Document-level URLs) cho các hiện vật đề thi công khai:
- `PRAC-2023-2024-HK1-O117`: https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/co-so-du-lieu/it004o117-de-1-de-thi-thuc-hanh-csdl/110260821
- `EXAM-2023-2024-HK1-FINAL-01`: https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/co-so-du-lieu/de-thi-cuoi-ky-co-so-du-lieu-hoc-ky-1-nam-2023-2024/81121063
- `PRAC-2024-2025-HK1-302`: https://www.studocu.vn/vn/document/university-of-information-technology/co-so-du-lieu/it004-th2425-de-thi-thuc-hanh-co-so-du-lieu-302/149081939
- `EXAM-2022-2023-HK1-MID-D2`: https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/co-so-du-lieu/de-thi-giua-ky-csdl-hk1-2022-2023-lop-cq-clc/41982736
- `EXAM-2023-2024-HK1-MID-D1`: https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/co-so-du-lieu/de-thi-giua-ky-mon-co-so-du-lieu-khoa-he-thong-thong-tin/81121063

SEARCH SATURATION:
PASS (Hoàn thành 12 đợt tìm kiếm hệ thống; 4 đợt liên tiếp BATCH-09, BATCH-10, BATCH-11, BATCH-12 thỏa mãn điều kiện 0 nguồn mới, 0 hiện vật mới, 0 năm học mới, 0 chủ đề mới).

LOCAL PAGE-RANGE CONSISTENCY:
PASS (Khớp chính xác số trang PDF và vị trí phân đoạn: `PART1.pdf` = 262 trang, `PART2.pdf` = 94 trang, `EXAMS_REVIEW.pdf` = 25 trang, `LABS_AND_SQL.txt` = 114 KB, `QLBANHANG.xlsx` = 25 KB, `Homework5.docx` = 28 KB).

README METRIC CONSISTENCY:
PASS (Tất cả số liệu thống kê trong `README.md` khớp 100% với `source_inventory.md` và `artifact_registry.md`).

COPYRIGHT SAFETY:
PASS (Không có tệp PDF bài giảng, ảnh scan đề thi, tệp Word/Excel cá nhân nào được đưa vào staging hay commit lên GitHub; chỉ lưu trữ siêu dữ liệu và tóm lược độc lập).

REPOSITORY SAFETY:
PASS (Chỉ thao tác trên `Phuchello/CSDL_UIT` tại nhánh `v1.1-editorial-practice`; tuyệt đối không chạm vào `Phuchello/phuchello` hoặc nhánh `main`).
