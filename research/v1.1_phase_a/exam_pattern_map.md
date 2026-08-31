# Bản Đồ Mẫu Đề Thi Thực Chứng (Evidence-Driven Exam Pattern Map) — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31
**Nguyên tắc:** Cột `artifact_count` bắt buộc phải bằng chính xác số lượng mã định danh hiện vật đề thi duy nhất (`exam` hoặc `practical-exam`) được liệt kê trong hàng đó. Các tài liệu ôn tập (`review`) và hệ thống lab (`lab-corpus`) không được tính vào `artifact_count`. Mức độ tin cậy được thể hiện bằng các nhãn định tính chuẩn mực (`HIGH`, `MEDIUM-HIGH`, `MEDIUM`, `LOW`, `UNVERIFIED`).

---

## 1. Ma Trận Mẫu Câu Hỏi Đề Thi Theo Chuyên Đề

| Chuyên đề / Chương | Mẫu câu hỏi thực chứng (Observed Pattern) | Artifact Count | Năm học quan sát | Canonical Artifact IDs liệt kê | Source IDs liên kết | Mức độ tin cậy | Phân loại bằng chứng (Evidence Kind) |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: | :--- |
| **Ch1: Tổng quan CSDL** | • Phân biệt Hệ thống tập tin (File System) vs DBMS<br>• Kiến trúc 3 mức ANSI/SPARC & Tính độc lập dữ liệu logic/vật lý | **2** | 2020–2021, 2023–2024 | `EXAM-2020-2021-HK1-FINAL-01`, `EXAM-2023-2024-HK1-FINAL-01` | `LOC-LEC-AN-CH01`, `LOC-LEC-LONG-CH01`, `UIT-O01` | `MEDIUM-HIGH` | `OBSERVED IN EXAM ARTIFACT` + `COURSE SCOPE` |
| **Ch2: Mô hình ER & Quan hệ** | • Thiết kế mô hình ER từ ngữ cảnh thực tế (Entity, Relationship, Min-Max, Thuộc tính đa trị/đa hợp)<br>• Ánh xạ ER $\rightarrow$ Lược đồ quan hệ xác định rõ PK, FK (Quan hệ 1:1, 1:N, M:N, Is-a) | **4** | 2017–2018, 2023–2024 | `EXAM-2023-2024-HK1-MID-D1`, `EXAM-2023-2024-HK1-MID-D2`, `EXAM-2017-2018-HK1-MID-D1`, `EXAM-2017-2018-HK1-MID-D2` | `LOC-EXAM-2023-2024-MID-D1`, `LOC-EXAM-2023-2024-MID-D2`, `LOC-HW-23520266-5`, `LOC-LEC-LONG-CH02` | `HIGH` | `OBSERVED IN EXAM ARTIFACT` |
| **Ch3: Đại số quan hệ (ĐSQH)** | • Truy vấn cơ bản: Phép chọn $\sigma$, Phép chiếu $\pi$, Phép kết $\bowtie$, Phép đổi tên $\rho$<br>• Phép tập hợp: Hội $\cup$, Giao $\cap$, Trừ $-$<br>• Phép kết ngoài: Left/Right Outer Join $(\mathbin{⟕}, \mathbin{⟖})$<br>• Phép chia $\div$ (Bài toán "Tất cả" - Universal Condition)<br>• Gom nhóm & Tính toán: Phép gom nhóm $\Im$ kết hợp `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` | **9** | 2017–2018, 2018–2019, 2019–2020, 2022–2023, 2023–2024 | `EXAM-2023-2024-HK1-MID-D1`, `EXAM-2023-2024-HK1-MID-D2`, `EXAM-2022-2023-HK1-MID-D2`, `EXAM-2019-2020-HK1-MID-D1`, `EXAM-2019-2020-HK1-MID-D2`, `EXAM-2018-2019-HK1-MID-D1`, `EXAM-2018-2019-HK1-MID-D2`, `EXAM-2017-2018-HK1-MID-D1`, `EXAM-2017-2018-HK1-MID-D2` | `LOC-EXAM-2023-2024-MID-D1`, `LOC-EXAM-2023-2024-MID-D2`, `LOC-HW-23520266-5`, `LOC-LEC-LONG-CH03` | `HIGH` | `OBSERVED IN EXAM ARTIFACT` |
| **Ch4: Truy vấn SQL Server / T-SQL** | • Lệnh DDL: `CREATE TABLE`, `ALTER TABLE`, thêm/xóa cột, kiểu dữ liệu<br>• Khai báo ràng buộc: `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`<br>• Lệnh DML: `UPDATE` có điều kiện `WHERE`, tăng/giảm giá trị theo ngày tháng<br>• Truy vấn nâng cao: `JOIN`, `SELF JOIN`, Subquery, Correlated Subquery<br>• Phép chia SQL: Double `NOT EXISTS` vs `GROUP BY ... HAVING COUNT` | **13** | 2017–2018, 2018–2019, 2019–2020, 2020–2021, 2022–2023, 2023–2024, 2024–2025 | `EXAM-2023-2024-HK1-MID-D1`, `EXAM-2023-2024-HK1-MID-D2`, `EXAM-2023-2024-HK1-FINAL-01`, `EXAM-2022-2023-HK1-MID-D2`, `EXAM-2020-2021-HK1-FINAL-01`, `EXAM-2019-2020-HK1-MID-D1`, `EXAM-2019-2020-HK1-MID-D2`, `EXAM-2018-2019-HK1-MID-D1`, `EXAM-2018-2019-HK1-MID-D2`, `EXAM-2017-2018-HK1-MID-D1`, `EXAM-2017-2018-HK1-MID-D2`, `PRAC-2023-2024-HK1-O117`, `PRAC-2024-2025-HK1-302` | `LOC-EXAM-2023-2024-MID-D1`, `LOC-EXAM-2023-2024-MID-D2`, `LOC-HW-23520266-5`, `TECH-A01`, `TECH-A02`, `TECH-A07`, `TECH-A08` | `HIGH` | `OBSERVED IN EXAM ARTIFACT` + `OBSERVED IN PRACTICAL EXAM` |
| **Ch5: Ràng buộc toàn vẹn (RBTV)** | • Phân tích bối cảnh, phát biểu tân từ hình thức bằng biểu thức logic/toán học<br>• Lập Bảng tầm ảnh hưởng 3 thao tác (Thêm, Xóa, Sửa)<br>• Phân loại RBTV: Miền giá trị, Liên thuộc tính 1 QH, Liên bộ 1 QH, Tham chiếu, Liên thuộc tính nhiều QH, Thuộc tính tổng hợp, Chu trình<br>• Cài đặt RBTV bằng `CHECK` hoặc Trigger T-SQL an toàn đa dòng | **4** | 2020–2021, 2023–2024, 2024–2025 | `EXAM-2023-2024-HK1-FINAL-01`, `EXAM-2020-2021-HK1-FINAL-01`, `PRAC-2023-2024-HK1-O117`, `PRAC-2024-2025-HK1-302` | `LOC-LEC-LONG-CH05`, `LOC-HW-23520266-5`, `TECH-A03`, `TECH-A04`, `TECH-A05`, `TECH-A06` | `HIGH` | `OBSERVED IN EXAM ARTIFACT` + `OBSERVED IN PRACTICAL EXAM` |
| **Ch6: Phụ thuộc hàm & Chuẩn hóa** | • Tiên đề Armstrong & Chứng minh PTH ($F \vdash X \rightarrow Y$)<br>• Thuật toán tính bao đóng thuộc tính $X^+$, bài toán thành viên<br>• Tìm tất cả các khóa ứng viên (Phân tích tập nguồn $Ng$, trung gian $Tg$, treo $Tr$)<br>• Tìm phủ tối thiểu $F_c$ (3 bước)<br>• Kiểm tra dạng chuẩn cao nhất (1NF $\rightarrow$ 2NF $\rightarrow$ 3NF $\rightarrow$ BCNF)<br>• Phân rã bảo toàn phụ thuộc hàm và nối không mất thông tin (Lossless Join) | **2** | 2020–2021, 2023–2024 | `EXAM-2023-2024-HK1-FINAL-01`, `EXAM-2020-2021-HK1-FINAL-01` | `LOC-LEC-LONG-CH06`, `COM-C02`, `LOC-NOTE-NHAP` | `HIGH` | `OBSERVED IN EXAM ARTIFACT` |
| **Thực hành máy tập trung** | • Thi thực hành 90 phút trên Microsoft SQL Server trong môi trường phòng lab (không Internet, không tài liệu)<br>• Viết script DDL/DML, Trigger kiểm tra RBTV và truy vấn phức tạp | **2** | 2023–2024, 2024–2025 | `PRAC-2023-2024-HK1-O117`, `PRAC-2024-2025-HK1-302` | `LOC-SQL-LAB01` đến `LOC-SQL-LAB04-ALL`, `UIT-O06`, `UIT-O10` | `HIGH` | `OFFICIAL EXAM NOTICE` + `OBSERVED IN PRACTICAL EXAM` |

---

## 2. Top 5 Mẫu Đề Thi Có Tần Suất Quan Sát Cao Nhất (Top 5 Evidence-Based Patterns)

1. **Truy vấn SQL Server / T-SQL phân bậc (Quan sát trong 13 hiện vật đề thi qua 7 năm học)**:
   - Các câu hỏi trải dài từ lọc dữ liệu, kết nối bảng `JOIN`, gom nhóm `GROUP BY / HAVING`, truy vấn lồng `EXISTS / NOT EXISTS` đến bài toán phép chia và hàm xếp hạng.
   - *Hiện vật tiêu biểu*: `EXAM-2023-2024-HK1-MID-D1`, `EXAM-2023-2024-HK1-FINAL-01`, `PRAC-2024-2025-HK1-302`.

2. **Truy vấn Đại số quan hệ (Quan sát trong 9 hiện vật đề thi qua 5 năm học)**:
   - Viết biểu thức ĐSQH giải quyết các yêu cầu lọc, chiếu, kết nối, phép trừ và phép chia $\div$ cho các bài toán quản lý thực tế.
   - *Hiện vật tiêu biểu*: `EXAM-2023-2024-HK1-MID-D1`, `EXAM-2023-2024-HK1-MID-D2`, `EXAM-2019-2020-HK1-MID-D1`, `EXAM-2018-2019-HK1-MID-D1`, `EXAM-2017-2018-HK1-MID-D1`.

3. **Thiết kế ERD & Ánh xạ sang Lược đồ quan hệ (Quan sát trong 4 hiện vật đề thi qua 2 năm học + 2 tài liệu ôn tập)**:
   - Vẽ mô hình thực thể mối kết hợp đầy đủ bản số $(min, max)$ và chuyển đổi sang lược đồ quan hệ xác định rõ $PK, FK$.
   - *Hiện vật tiêu biểu*: `EXAM-2023-2024-HK1-MID-D1`, `EXAM-2023-2024-HK1-MID-D2`, `EXAM-2017-2018-HK1-MID-D1`, `EXAM-2017-2018-HK1-MID-D2`.

4. **Phân tích Ràng buộc toàn vẹn & Lập Bảng tầm ảnh hưởng 3 thao tác (Quan sát trong 4 hiện vật đề thi/thực hành)**:
   - Phát biểu tân từ bằng logic hình thức, lập Bảng tầm ảnh hưởng $(+, -, +(\text{cột}))$, và viết Trigger T-SQL an toàn đa dòng.
   - *Hiện vật tiêu biểu*: `EXAM-2023-2024-HK1-FINAL-01`, `EXAM-2020-2021-HK1-FINAL-01`, `PRAC-2023-2024-HK1-O117`, `PRAC-2024-2025-HK1-302`.

5. **Phụ thuộc hàm & Chuẩn hóa BCNF/3NF (Quan sát trong 2 hiện vật đề thi cuối kỳ + slide bài giảng)**:
   - Tính bao đóng thuộc tính, tìm tập khóa ứng viên qua phân tích tập nguồn $Ng$, trung gian $Tg$, treo $Tr$, xác định dạng chuẩn cao nhất và phân rã bảo toàn.
   - *Hiện vật tiêu biểu*: `EXAM-2023-2024-HK1-FINAL-01`, `EXAM-2020-2021-HK1-FINAL-01`.
