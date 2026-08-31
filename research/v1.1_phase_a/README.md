# Báo Cáo Tổng Hợp Nghiên Cứu Giai Đoạn A (Phase A Final Summary) — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31
**Mục đích:** Tổng kết snapshot chứng cứ đã thu thập, kiểm toán và đối chiếu từ nguồn tài liệu cục bộ và web công khai, đủ để định hướng triển khai Giai đoạn B.

> **RESEARCH SNAPSHOT STATUS: FROZEN FOR IMPLEMENTATION**
> **SNAPSHOT DATE: 2026-08-31**

Snapshot này xác nhận official UIT sources đã được rà soát; local corpus đã được ingest đầy đủ; Microsoft technical references đã được validate; nhiều GitHub/community repositories đã được review; các hiện vật đề thi/thực hành trực tiếp qua nhiều năm đã được lập chỉ mục; provenance và copyright boundaries đã được thiết lập. Cơ sở chứng cứ đủ để định hướng triển khai v1.1. `artifact_registry.md` vẫn có thể mở rộng khi xuất hiện evidence mới.

> “The registry is a high-coverage research snapshot, not a claim of exhaustive coverage of all materials on the Internet.”

> **QUAN TRỌNG**: KHÔNG BẮT ĐẦU TRIỂN KHAI GIAI ĐOẠN B (VIẾT SÁCH THỰC HÀNH, SỬA HANDBOOK LÝ THUYẾT, DỰNG QUARTZ) CHO ĐẾN KHI CÓ ĐÁNH GIÁ VÀ PHÊ DUYỆT CỦA HỘI ĐỒNG THẨM ĐỊNH (HUMAN MENTOR REVIEW).

---

## 1. Thống Kê Tổng Quan Bằng Chứng Thu Thập (Evidence Metrics)

| Hạng mục nguồn | Số lượng | Diễn giải & Phân loại thẩm quyền |
| :--- | :---: | :--- |
| **Tệp đính kèm cục bộ (Local Attachments)** | **6** | `CSDL_UIT_LOCAL_LECTURES_PART1.pdf` (262 tr), `PART2.pdf` (94 tr), `EXAMS_REVIEW.pdf` (25 tr), `LABS_AND_SQL.txt` (114 KB), `QLBANHANG.xlsx` (25 KB), `Homework5.docx` (28 KB) |
| **Tài liệu gốc cục bộ được bóc tách (Recovered Docs)** | **17** | 7 slide bài giảng, 5 đề thi/ôn tập, 5 tệp script/workbook dữ liệu mẫu |
| **Slide bài giảng chính thức của Giảng viên UIT** | **7** | Slide GV Phan Nguyễn Thụy An (Ch1, Ch2) và ThS. Dương Phi Long (Ch1, Ch2, Ch3, Ch5, Ch6) (Tier A) |
| **Hiện vật đề thi & bài tập cục bộ (Local Exam/Review)** | **8** | Đề thi Giữa kỳ HK1 2023–2024 (Đề 1 & 2), Đáp án K18, 2 bộ bài tập ôn tập, 3 bài tập Homework 1, 2, 5 (Tier B/C) |
| **Tệp mã nguồn thực hành Lab T-SQL & Dataset** | **7** | 4 buổi Lab 01–04, 1 mega-script tổng hợp, 1 tệp ghi chú phòng thi sinh viên, 1 workbook Excel QLBH (Tier B/C) |
| **Nguồn Cổng thông tin & Khoa HTTT chính thức (UIT)** | **7** | Chương trình đào tạo, danh mục môn học, thư viện, thông báo thi thực hành, lịch thi giữa kỳ (Tier A) |
| **Tài liệu kỹ thuật Microsoft Learn (Transact-SQL)** | **11** | DDL, GROUP BY, CHECK, Trigger, inserted/deleted, Multi-row safety, EXISTS, UNION, PROCEDURE, VIEW, FUNCTION (Tier A) |
| **Giáo trình học thuật quốc tế & chuẩn mực** | **3** | *Database System Concepts* (Silberschatz), *Fundamentals of DB Systems* (Elmasri), OpenStax RDBMS (Tier A) |
| **Kho lưu trữ GitHub cộng đồng sinh viên** | **4** | `UIT-DS/IT004.L19-Database`, `SeaW1nd/IT004-CSDL`, `HiImKing1509`, `phanxuanquang` (Tier C) |
| **Kho lưu trữ tài liệu cộng đồng (Studocu/Scribd)** | **13** | 4 nguồn cũ + 9 direct leads mới; chỉ 4 lead có đủ header để promote thành canonical artifact |
| **Tổng số nguồn trong Sổ đăng ký nguồn (`source_inventory.md`)** | **60** | Đầy đủ mã `source_id`, URL / vị trí trang, Authority Tier và Ownership |
| **Số đợt tìm kiếm web hệ thống (Search Batches)** | **17** | Nhật ký giữ nguyên 16 batch trước và bổ sung batch tiếp nhận/cross-check direct leads; không tuyên bố exhaustive Internet coverage |
| **Hiện vật Đề thi Lý thuyết / Tự luận (`exam`)** | **17** | 17 đề thi chuẩn hóa độc lập (Giữa kỳ & Cuối kỳ từ 2017 đến 2025) |
| **Hiện vật Đề thi Thực hành phòng máy (`practical-exam`)** | **10** | 6 hiện vật cũ + `PRAC-2024-2025-HK1-01`, `PRAC-2024-2025-HK1-02`, `PRAC-2023-2024-HK1-FINAL-01`, `PRAC-2022-2023-HK1-D03` |
| **Hiện vật Tài liệu Ôn tập & Bài tập lớn (`review`)** | **3** | `REV-2024-10-01-EXP`, `REV-2024-DSQH-MID`, `REV-2024-K18-SOL` |
| **Hiện vật Hệ thống Thực hành Chuẩn (`lab-corpus`)** | **1** | `LAB-QLBH-QLGV-CORPUS` (Lab 01–04 QLBH & QLGV) |
| **TỔNG SỐ HIỆN VẬT CHUẨN HÓA (TOTAL CANONICAL ARTIFACTS)** | **31** | 17 exam + 10 practical-exam + 3 review + 1 lab-corpus; toàn bộ được lập chỉ mục tại `artifact_registry.md` |
| **Các năm học có hiện vật kiểm chứng trực tiếp** | **9 năm** | 2013–2014, 2017–2018, 2018–2019, 2019–2020, 2020–2021, 2021–2022, 2022–2023, 2023–2024, 2024–2025 |

---

## 2. Khuyến Nghị Định Hướng Cho Giai Đoạn B (Recommendations for Implementation)

### A. Khuyến Nghị Hoàn Thiện Sách Lý Thuyết (Theory Handbook Editorial)
- **Chuẩn hóa thuật ngữ & ký hiệu**: Bổ sung ký hiệu phép chiếu $R[X]$ và phép gom nhóm $_{G}\Im_{F}(E)$ song song với ký hiệu quốc tế để sinh viên làm bài thi tự luận đạt điểm tuyệt đối.
- **Tái cấu trúc Chương 5**: Trình bày hệ thống theo 7 phân loại RBTV chuẩn mực của Khoa HTTT – UIT.
- **Tinh giản giọng văn**: Loại bỏ các từ ngữ mang tính tiếp thị ("Exam Mastery"), giữ phong cách sư phạm đĩnh đạc, rõ ràng.
- **Mỹ thuật Bìa sách**: Áp dụng bìa đồ họa mạng lưới quan hệ (Relational Schema Graph), chỉ gồm 3 dòng chữ: `IT004`, `CƠ SỞ DỮ LIỆU`, `BIÊN SOẠN: VÕ TRỌNG PHÚC`.

### B. Khuyến Nghị Xây Dựng Sách Thực Hành SQL Server (Practical Handbook)
- **Trọng tâm `CORE`**: Tập trung vào quy trình thực hành 4 buổi chuẩn hóa (`QLBH` & `QLGV`), làm chủ DDL, DML, `JOIN`, Subquery, Correlated Subquery, phép chia Double `NOT EXISTS` và DML Trigger an toàn đa dòng.
- **Tính năng `OPTIONAL`**: Đưa Stored Procedure và View vào phụ lục nâng cao.
- **Loại bỏ tính năng ngoài phạm vi**: Không đưa Transactions/Locking và User-Defined Functions phức tạp vào nội dung bắt buộc.

### C. Khuyến Nghị Xây Dựng Ngân Hàng Câu Hỏi Tự Luận (Tự Luận / Essay Bank)
- Phân bổ 80+ câu hỏi có giải thích chi tiết theo 7 nhóm chuyên đề (Ch1 đến Ch6 + Đề thi tổng hợp).
- 100% câu hỏi gắn nhãn xuất xứ minh bạch (`verified-artifact`, `reconstructed-exam-pattern`, `original-practice`).

### D. Khuyến Nghị Kiến Trúc Vườn Tri Thức (Knowledge Garden)
- Sử dụng **Quartz (Static-First)** triển khai trên GitHub Pages: hỗ trợ đầy đủ Tìm kiếm tiếng Việt, Wikilinks 2 chiều, Đồ thị tri thức (Graph view), công thức toán LaTeX và giao diện tối giản, tải nhanh.

---

## 3. Danh Mục Các Hồ Sơ Nghiên Cứu Trong Thư Mục Này

1. [`local_corpus_audit.md`](local_corpus_audit.md): Báo cáo bóc tách chi tiết 6 tệp đính kèm cục bộ và 17 tài liệu nguồn gốc.
2. [`web_search_log.md`](web_search_log.md): Nhật ký 17 đợt tìm kiếm/cross-check và trạng thái snapshot đóng băng cho triển khai.
3. [`artifact_registry.md`](artifact_registry.md): Bảng đăng ký 31 hiện vật chuẩn hóa (17 exam, 10 practical-exam, 3 review, 1 lab-corpus) cùng các lead chưa promote.
4. [`source_inventory.md`](source_inventory.md): Bảng kê toàn bộ 60 nguồn tài liệu học thuật/cộng đồng với phân loại Authority Tier và Ownership.
5. [`exam_pattern_map.md`](exam_pattern_map.md): Ma trận mẫu câu hỏi thi thực chứng với `artifact_count` đồng bộ cơ học.
6. [`practical_coverage_map.md`](practical_coverage_map.md): Bản đồ kỹ năng T-SQL và ma trận tiến trình Lab 01–04.
7. [`essay_bank_plan.md`](essay_bank_plan.md): Kế hoạch ngân hàng câu hỏi tự luận theo chuyên đề.
8. [`theory_editorial_audit.md`](theory_editorial_audit.md): Kiểm toán biên tập lý thuyết và định hướng thiết kế bìa sách.
9. [`source_gaps_and_conflicts.md`](source_gaps_and_conflicts.md): Hồ sơ xử lý xung đột học thuật và chính sách bản quyền.
10. [`knowledge_garden_architecture.md`](knowledge_garden_architecture.md): Thiết kế kiến trúc và cấu trúc cây thư mục Quartz.
11. [`validation_report.md`](validation_report.md): Báo cáo kiểm thử snapshot, URL, source/artifact IDs, counts, copyright và repository safety.
