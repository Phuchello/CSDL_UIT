# Báo Cáo Tổng Hợp Nghiên Cứu Giai Đoạn A (Phase A Final Summary) — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31
**Mục đích:** Tổng kết toàn bộ kết quả thu thập, kiểm toán và đối chiếu nguồn tài liệu cục bộ, nguồn web công khai, và xác lập cơ sở chứng cứ vững chắc trước khi tiến hành Giai đoạn B (Triển khai).

> **QUAN TRỌNG**: KHÔNG BẮT ĐẦU TRIỂN KHAI GIAI ĐOẠN B (VIẾT SÁCH THỰC HÀNH, SỬA HANDBOOK LÝ THUYẾT, DỰNG QUARTZ) CHO ĐẾN KHI CÓ ĐÁNH GIÁ VÀ PHÊ DUYỆT CỦA HỘI ĐỒNG THẨM ĐỊNH (HUMAN MENTOR REVIEW).

---

## 1. Thống Kê Tổng Quan Bằng Chứng Thu Thập (Evidence Metrics)

| Hạng mục nguồn | Số lượng | Diễn giải & Phân loại thẩm quyền |
| :--- | :---: | :--- |
| **Tệp đính kèm cục bộ (Local Attachments)** | **6** | `CSDL_UIT_LOCAL_LECTURES_PART1.pdf`, `PART2.pdf`, `EXAMS_REVIEW.pdf`, `LABS_AND_SQL.txt`, `QLBANHANG.xlsx`, `Homework5.docx` |
| **Tài liệu gốc cục bộ được bóc tách (Recovered Docs)** | **17** | 7 slide bài giảng, 5 đề thi/ôn tập, 5 tệp script/workbook dữ liệu mẫu |
| **Slide bài giảng chính thức của Giảng viên UIT** | **7** | Slide GV Phan Nguyễn Thụy An (Ch1, Ch2) và ThS. Dương Phi Long (Ch1, Ch2, Ch3, Ch5, Ch6) (Tier A) |
| **Hiện vật đề thi & bài tập cục bộ (Local Exam/Review)** | **7** | Đề thi Giữa kỳ HK1 2023–2024 (Đề 1 & 2), Đáp án K18, 2 bộ bài tập ôn tập, 2 bài tập Homework (Tier B/C) |
| **Tệp mã nguồn thực hành Lab T-SQL** | **5** | 4 buổi Lab 01–04, 1 mega-script tổng hợp và 1 tệp ghi chú phòng thi sinh viên (Tier C) |
| **Nguồn Cổng thông tin & Khoa HTTT chính thức (UIT)** | **7** | Chương trình đào tạo, danh mục môn học, thông báo thi thực hành, lịch thi giữa kỳ (Tier A) |
| **Tài liệu kỹ thuật Microsoft Learn (Transact-SQL)** | **8** | DDL/DML, Trigger, `inserted`/`deleted`, Multi-row safety, `GROUP BY`, `EXISTS`, `UNION`, `VIEW` (Tier A) |
| **Giáo trình học thuật quốc tế & chuẩn mực** | **3** | *Database System Concepts* (Silberschatz), *Fundamentals of DB Systems* (Elmasri), Giáo trình CSDL UIT (Tier A) |
| **Kho lưu trữ GitHub cộng đồng sinh viên** | **4** | `UIT-DS/IT004.L19-Database`, `SeaW1nd/IT004-CSDL`, `HiImKing1509`, `phanxuanquang` (Tier C) |
| **Kho lưu trữ tài liệu cộng đồng (Studocu/Scribd)** | **4** | Studocu Course 131131, Course 545041, Scribd outlines (Tier C) |
| **Số đợt tìm kiếm web hệ thống (Search Batches)** | **8** | Đạt ngưỡng bão hòa tìm kiếm (Search Saturation Reached) |
| **Hiện vật Đề thi Chuẩn hóa (Canonical Artifacts)** | **14** | Hợp nhất và loại bỏ trùng lặp từ hơn 30 bản sao mirror trên mạng |
| **Các năm học có hiện vật kiểm chứng trực tiếp** | **8 năm** | 2016–2017, 2017–2018, 2018–2019, 2019–2020, 2020–2021, 2021–2022, 2022–2023, 2023–2024 |
| **Số lượng bản sao mirror trùng lặp đã gộp (Collapsed)** | **> 30** | Đã định danh và đối chiếu về các Canonical Artifact ID duy nhất |

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
- Phân bổ 76 câu hỏi có giải thích chi tiết theo 7 nhóm chuyên đề (Ch1 đến Ch6 + Đề thi tổng hợp).
- 100% câu hỏi gắn nhãn xuất xứ minh bạch (`verified-artifact`, `reconstructed-exam-pattern`, `original-practice`).

### D. Khuyến Nghị Kiến Trúc Vườn Tri Thức (Knowledge Garden)
- Sử dụng **Quartz (Static-First)** triển khai trên GitHub Pages: hỗ trợ đầy đủ Tìm kiếm tiếng Việt, Wikilinks 2 chiều, Đồ thị tri thức (Graph view), công thức toán LaTeX và giao diện tối giản, tải nhanh.

---

## 3. Danh Mục Các Hồ Sơ Nghiên Cứu Trong Thư Mục Này

1. [`local_corpus_audit.md`](local_corpus_audit.md): Báo cáo bóc tách chi tiết 6 tệp đính kèm cục bộ và 17 tài liệu nguồn gốc.
2. [`web_search_log.md`](web_search_log.md): Nhật ký 8 đợt tìm kiếm web và chứng nhận đạt ngưỡng bão hòa tìm kiếm.
3. [`artifact_registry.md`](artifact_registry.md): Bảng đăng ký 14 hiện vật đề thi chuẩn hóa từ năm 2016 đến 2024.
4. [`source_inventory.md`](source_inventory.md): Bảng kê toàn bộ 35 nguồn tài liệu học thuật với phân loại Authority Tier và Ownership.
5. [`exam_pattern_map.md`](exam_pattern_map.md): Ma trận mẫu câu hỏi thi thực chứng và Top 5 dạng bài có tần suất cao nhất.
6. [`practical_coverage_map.md`](practical_coverage_map.md): Bản đồ kỹ năng T-SQL và ma trận tiến trình Lab 01–04.
7. [`essay_bank_plan.md`](essay_bank_plan.md): Kế hoạch ngân hàng câu hỏi tự luận theo chuyên đề.
8. [`theory_editorial_audit.md`](theory_editorial_audit.md): Kiểm toán biên tập lý thuyết và định hướng thiết kế bìa sách.
9. [`source_gaps_and_conflicts.md`](source_gaps_and_conflicts.md): Hồ sơ xử lý xung đột học thuật và chính sách bản quyền.
10. [`knowledge_garden_architecture.md`](knowledge_garden_architecture.md): Thiết kế kiến trúc và cấu trúc cây thư mục Quartz.
