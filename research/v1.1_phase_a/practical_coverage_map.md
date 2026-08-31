# Bản Đồ Kỹ Năng Thực Hành SQL Server (Practical SQL Server Coverage Map) — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31
**Nguyên tắc:** Phân loại rõ ràng các tính năng T-SQL thành `CORE`, `OPTIONAL`, `HISTORICAL`, `UNSUPPORTED` dựa trên bằng chứng thực nghiệm từ mã nguồn Lab 01–04 cục bộ, đề thi thực hành chính thức và tài liệu chuẩn Microsoft Learn.

---

## 1. Ma Trận Kỹ Năng Thực Hành T-SQL (Skill Coverage Matrix)

| Kỹ năng / Lệnh T-SQL | Phân loại | Source IDs | Bằng chứng thực nghiệm | Độ tin cậy | Kế hoạch triển khai |
| :--- | :---: | :--- | :--- | :---: | :--- |
| **Cài đặt & Vận hành SSMS** | **CORE** | `UIT-O06`, `UIT-O10`, `GH-C02`, `LOC-SQL-LAB01` | Quy chế thi thực hành trên máy tập trung, kết nối LocalDB/SQL Express, gỡ lỗi kết nối | **Tuyệt đối (10/10)** | Hướng dẫn cấu hình môi trường, checklist 60 giây |
| **CREATE DATABASE / TABLE** | **CORE** | `LOC-SQL-LAB01`, `TECH-A01`, `GH-C02`, `COM-C08` | DDL tạo Database `QuanLyBanHang`, `QuanLyGiaoVu`; khai báo bảng và các thuộc tính | **Tuyệt đối (10/10)** | Chuyên đề DDL chuẩn mực |
| **Kiểu dữ liệu SQL Server** | **CORE** | `LOC-SQL-LAB01`, `TECH-A01`, `LOC-XLSX-QLBH` | `CHAR`, `VARCHAR`, `NVARCHAR`, `SMALLDATETIME`, `MONEY`, `NUMERIC(4,2)`, `TINYINT`, `INT`, `BIT` | **Tuyệt đối (10/10)** | Bảng tra cứu kiểu dữ liệu và bẫy lưu trữ |
| **PRIMARY KEY / FOREIGN KEY** | **CORE** | `LOC-SQL-LAB01`, `TECH-A01`, `LOC-EXAM-2023-2024-MID-D1` | Khóa chính đơn, khóa chính phức hợp (`CTHD(SOHD, MASP)`), khóa ngoại qua `ALTER TABLE ADD CONSTRAINT` | **Tuyệt đối (10/10)** | Chuyên đề Ràng buộc quan hệ |
| **CHECK / UNIQUE / DEFAULT** | **CORE** | `LOC-SQL-LAB01`, `TECH-A03`, `LOC-EXAM-2023-2024-MID-D1` | `CHECK (GIA >= 500)`, `CHECK (NGDK > NGSINH)`, `CHECK (DVT IN (...))`, `DEFAULT` | **Tuyệt đối (10/10)** | Chuyên đề RBTV khai báo |
| **DML: INSERT / UPDATE / DELETE** | **CORE** | `LOC-SQL-LAB02`, `LOC-SQL-LAB03`, `LOC-XLSX-QLBH` | Nạp dữ liệu 5 bảng QLBH, 7 bảng QLGV; `UPDATE` có tính toán giá trị, xóa dữ liệu an toàn | **Tuyệt đối (10/10)** | Chuyên đề Thao tác dữ liệu |
| **Truy vấn SELECT / WHERE / LIKE / IN / BETWEEN** | **CORE** | `LOC-SQL-LAB02`, `LOC-HW-23520266-5` | Lọc dữ liệu, chuỗi ký tự `LIKE 'B%01'`, so sánh đoạn `BETWEEN ... AND`, tập hợp `IN (...)` | **Tuyệt đối (10/10)** | Chuyên đề Truy vấn nền tảng |
| **Xử lý giá trị NULL & 3-Valued Logic** | **CORE** | `LOC-SQL-LAB02`, `TECH-A01`, `TXT-A03` | `IS NULL`, `IS NOT NULL`, bẫy so sánh `= NULL`, ảnh hưởng của `NULL` trong gom nhóm | **Cao (9.8/10)** | Bẫy thực chiến & Ngữ nghĩa toán học |
| **Sắp xếp ORDER BY** | **CORE** | `LOC-SQL-LAB02`, `LOC-SQL-LAB04`, `LOC-HW-23520266-5` | `ORDER BY NGHD ASC, TRIGIA DESC`, vị trí bắt buộc ở cuối câu truy vấn | **Tuyệt đối (10/10)** | Cú pháp chuẩn |
| **Phép kết JOIN (INNER, LEFT/RIGHT OUTER, FULL, SELF)** | **CORE** | `LOC-SQL-LAB02`, `LOC-SQL-LAB03`, `LOC-HW-23520266-5` | Kết nối nhiều bảng bằng `INNER JOIN ... ON`, tự kết (Self-Join) tìm quản lý, Outer Join bảo toàn dòng | **Tuyệt đối (10/10)** | Chuyên đề Kỹ thuật JOIN toàn diện |
| **Hàm kết hợp (COUNT, SUM, AVG, MIN, MAX)** | **CORE** | `LOC-SQL-LAB04`, `TECH-A02`, `LOC-HW-23520266-5` | `COUNT(*)`, `COUNT(DISTINCT MASP)`, `SUM(TRIGIA)`, `AVG(DIEM)`, tính doanh thu theo tháng | **Tuyệt đối (10/10)** | Chuyên đề Hàm tính toán |
| **Gom nhóm GROUP BY & HAVING** | **CORE** | `LOC-SQL-LAB04`, `TECH-A02`, `LOC-HW-23520266-5` | Gom nhóm theo nước SX, theo năm/tháng, điều kiện sau gom nhóm `HAVING COUNT(DISTINCT MASP) >= 4` | **Tuyệt đối (10/10)** | Chuyên đề Phân tích dữ liệu |
| **Truy vấn lồng & Correlated Subquery** | **CORE** | `LOC-SQL-LAB03`, `LOC-SQL-LAB04`, `TECH-A08` | `WHERE GIA = (SELECT MAX(GIA) FROM ...)`, `WHERE MAGV NOT IN (SELECT ...)` | **Tuyệt đối (10/10)** | Chuyên đề Subquery |
| **Phép chia SQL (Universal Queries)** | **CORE** | `LOC-SQL-LAB03`, `LOC-SQL-LAB04`, `LOC-NOTE-NHAP` | 2 phương pháp: Double `NOT EXISTS` (tuyệt đối chuẩn tắc) và `GROUP BY ... HAVING COUNT` | **Tuyệt đối (10/10)** | Chuyên đề Bài toán "Tất cả" |
| **Phép toán tập hợp (UNION, INTERSECT, EXCEPT)** | **CORE** | `LOC-SQL-LAB02`, `LOC-SQL-LAB03`, `TECH-A08` | Tương thích khả hợp, `UNION` gộp dòng, `INTERSECT` giao, `EXCEPT` trừ dữ liệu | **Tuyệt đối (10/10)** | Cầu nối ĐSQH $\rightarrow$ SQL |
| **Hàm xếp hạng (RANK() OVER, TOP WITH TIES)** | **CORE** | `LOC-SQL-LAB04`, `LOC-HW-23520266-5` | `RANK() OVER (ORDER BY DOANHSO DESC)`, `RANK() OVER (PARTITION BY NUOCSX ORDER BY GIA DESC)` | **Cao (9.8/10)** | Chuyên đề Xếp hạng & Top giá trị |
| **Cấu trúc rẽ nhánh CASE WHEN / IIF** | **CORE** | `LOC-SQL-LAB03`, `LOC-SQL-LAB01` | `CASE WHEN DIEMTB >= 9 THEN 'XS' ... END`, `IIF(DIEM BETWEEN 5 AND 10, 'Dat', 'Khong dat')` | **Cao (9.5/10)** | Chuyên đề Cập nhật phân loại |
| **DML Trigger & Bảng ảo inserted/deleted** | **CORE** | `LOC-LEC-LONG-CH05`, `TECH-A04`, `TECH-A05`, `TECH-A06` | Trigger kiểm tra ràng buộc liên bảng, kiểm tra an toàn đa dòng qua lệnh `JOIN inserted`/`deleted` | **Tuyệt đối (10/10)** | Chuyên đề Trigger thực chiến |
| **STORED PROCEDURE** | **OPTIONAL** | `TECH-A07`, `GH-C02`, `GH-C03`, `COM-C02` | Thủ tục lưu trữ có tham số đầu vào/đầu ra, gọi bằng `EXEC` | **Trung bình (7.5/10)** | Phụ lục mở rộng / Nâng cao |
| **VIEW** | **OPTIONAL** | `TECH-A10`, `GH-C02`, `TXT-A02` | `CREATE VIEW` lưu trữ câu truy vấn khung nhìn | **Trung bình (7.0/10)** | Phụ lục mở rộng |
| **USER-DEFINED FUNCTION (UDF)** | **HISTORICAL** | `GH-C02` | Hàm người dùng vô hướng / bảng (ít xuất hiện trong bài thi chính khóa) | **Thấp (5.0/10)** | Đọc thêm |
| **TRANSACTIONS & LOCKING** | **UNSUPPORTED** | - | Không nằm trong chuẩn đầu ra và đề thi môn IT004 | **Không áp dụng** | Loại khỏi phạm vi cẩm nang |

---

## 2. Bảng Tiến Trình Thực Hành Chi Tiết (Raw Lab Progression Matrix)

Dựa trên mã nguồn gốc được bóc tách từ `CSDL_UIT_LOCAL_LABS_AND_SQL.txt` và `QLBANHANG.xlsx`:

| Lab Session | Tệp nguồn / SHA-256 | Lược đồ CSDL | DDL & Ràng buộc | DML & Thao tác | Kỹ thuật truy vấn chính | Kỹ thuật nâng cao | Vấn đề & Lỗi điển hình trong code sinh viên |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Lab 01** | `[Lab01]...PhanHongDat.sql`<br>`SHA256: d2dd8c44...` | `QuanLyBanHang`<br>`QuanLyGiaoVu` | • `CREATE DATABASE`<br>• `CREATE TABLE` (12 bảng)<br>• `ALTER TABLE ADD CONSTRAINT PK/FK`<br>• `ALTER TABLE ADD/DROP/ALTER COLUMN`<br>• `CHECK` (DVT, GIA, SL, NGSINH, DIEM, HOCVI) | Không có DML trong Lab 01 | Chưa có SELECT | Ràng buộc miền giá trị phức hợp qua `IIF` | • Khai báo `NUMERIC(2,2)` cho điểm số gây lỗi tràn số khi điểm = 10 (cần sửa thành `NUMERIC(4,2)`). |
| **Lab 02** | `[Lab02]...PhanHongDat.sql`<br>`SHA256: ae90300e...` | `QuanLyBanHang`<br>`QuanLyGiaoVu` | Tái sử dụng DDL Lab 01 | • `INSERT INTO` 24 SP, 5 NV, 10 KH, 23 HD, 47 CTHD, 4 Khoa, 13 MH, 15 GV, 3 Lớp, 8 Điều kiện, 35 HV, 65 KQT<br>• `UPDATE` tăng/giảm giá, phân loại VIP | • `SELECT ... WHERE`<br>• `LIKE 'B%01'`, `BETWEEN`<br>• `ORDER BY`<br>• `INNER JOIN` 2–3 bảng<br>• `UNION`, `EXCEPT` | `SELECT * INTO SANPHAM1 FROM SANPHAM` (Sao lưu bảng) | • Chuỗi ngày tháng dạng `YYYY-MM-DD` cần thiết lập `SET DATEFORMAT YMD` để tránh lỗi xung đột văn hóa hệ thống. |
| **Lab 03** | `[Lab03]...PhanHongDat.sql`<br>`SHA256: e2cc9dc8...` | `QuanLyBanHang`<br>`QuanLyGiaoVu` | `ALTER TABLE KETQUATHI ADD DIEMTB NUMERIC(4,2)` | • `UPDATE` tăng hệ số lương trưởng khoa qua Subquery<br>• `UPDATE` tính DIEMTB lần thi sau cùng `MAX(LANTHI)`<br>• `UPDATE` xếp loại bằng `CASE WHEN` | • `UNION`, `INTERSECT`, `EXCEPT`<br>• Subquery `IN`, `NOT IN`<br>• Phép chia bằng Double `NOT EXISTS`<br>• Truy vấn ngày tháng `YEAR()`, `MONTH()` | • Double `NOT EXISTS` tìm hóa đơn mua tất cả SP Singapore<br>• Tìm học viên thi rớt môn CSDL lần 1 nhưng chưa thi lại | • Lỗi logic trong câu 15: nhầm lẫn giữa điều kiện `LANTHI > 3` và thi lần thứ 3 vẫn chưa đạt. |
| **Lab 04** | `[Lab04]...PhanHongDat.sql`<br>`SHA256: 2d9e5c53...` | `QuanLyBanHang`<br>`QuanLyGiaoVu` | Không thay đổi DDL | Thao tác truy vấn thống kê | • `COUNT(DISTINCT)`, `SUM`, `AVG`, `MIN`, `MAX`<br>• `GROUP BY` đơn/đa cột<br>• `HAVING COUNT(*) >= 4`<br>• Subquery tìm giá trị Max/Min | • `RANK() OVER (ORDER BY ... DESC)`<br>• `RANK() OVER (PARTITION BY ...)`<br>• `TOP 3 ... ORDER BY`<br>• Phép chia bằng `INTERSECT` đếm số môn đạt | • Viết `COUNT(DISTINCT GIA) >= 3` trong `HAVING` đòi hỏi dữ liệu phải có ít nhất 3 mức giá khác nhau. |
| **Lab 04 All** | `[Lab04]...Phan Hồng Đạt.sql`<br>`SHA256: 60c193ab...` | `QLBH` + `QLGV` | Tổng hợp toàn bộ DDL từ Lab 01 đến Lab 04 | Toàn bộ DML từ Lab 02–04 | Toàn bộ 44 câu QLBH và 35 câu QLGV | Tổng hợp toàn diện | Tệp tổng hợp hoàn chỉnh nhất của sinh viên, thể hiện toàn bộ vòng đời thực hành. |
