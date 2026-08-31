# Kiểm Toán Tài Liệu Cục Bộ (Local Corpus Audit) — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31
**Mục đích:** Bóc tách, phân loại và đánh giá độ tin cậy của toàn bộ tài liệu nguồn cục bộ được đính kèm trong không gian làm việc.

---

## 1. Tổng Quan Các Tệp Đính Kèm Cục Bộ (Transport Attachments)

Tất cả 6 tệp đính kèm cục bộ đều ở trạng thái **TRUY CẬP THÀNH CÔNG (READABLE)**:

| Tên Tệp Vận Chuyển (Transport Attachment) | Định dạng | Dung lượng | Số trang / Khối | Tình trạng truy cập | Bản chất tài liệu |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `CSDL_UIT_LOCAL_LECTURES_PART1.pdf` | PDF | 6.85 MB | **262 trang PDF** | **READABLE** | Tập hợp slide bài giảng Chương 1, 2, 3 (GV Phan Nguyễn Thụy An & ThS. Dương Phi Long) |
| `CSDL_UIT_LOCAL_LECTURES_PART2.pdf` | PDF | 4.09 MB | **94 trang PDF** | **READABLE** | Tập hợp slide bài giảng Chương 5 (RBTV) và Chương 6 (PTH & Chuẩn hóa) (ThS. Dương Phi Long) |
| `CSDL_UIT_LOCAL_EXAMS_REVIEW.pdf` | PDF | 8.12 MB | **25 trang PDF** | **READABLE** | Tập hợp đề thi chính thức Giữa kỳ HK1 2023–2024, đáp án K18, bài tập ôn tập và bài tập lớn |
| `CSDL_UIT_LOCAL_LABS_AND_SQL.txt` | TXT | 114 KB | **7 khối mã nguồn** | **READABLE** | 6 tệp mã nguồn SQL Lab 01–04 thực hành và 1 tệp ghi chú phòng thi sinh viên |
| `QLBANHANG.xlsx` | XLSX | 25 KB | **5 trang tính** | **READABLE** | Tập dữ liệu chuẩn Microsoft Excel cho lược đồ Quản lý bán hàng (QLBH) |
| `23520266_Homework5_CSDL.docx` | DOCX | 28 KB | **533 đoạn văn** | **READABLE** | Tuyển tập bài tập và lời giải đề thi môn CSDL qua các năm 2017–2024 của sinh viên |

---

## 2. Danh Mục Các Nguồn Tài Liệu Gốc Đã Được Bóc Tách (Recovered Source Documents)

### A. Nhóm Slide Bài Giảng Chính Thức (Consolidated Lectures)

| Source ID | Tên tài liệu gốc | Tệp vận chuyển | Vị trí trang PDF | Authority Tier | Ownership | Giảng viên / Đơn vị | Chủ đề bao phủ | Phân loại & Ghi chú |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| `LOC-LEC-AN-CH01` | *Chương 1: Tổng quan Cơ sở dữ liệu* | `LECTURES_PART1.pdf` | 1–44 / 262 | **A** | UIT | GV. Phan Nguyễn Thụy An (Khoa HTTT) | Khái niệm CSDL, DBMS, File System vs DBMS, 3 mức ANSI/SPARC, các mô hình CSDL | Slide bài giảng UIT chuẩn; định nghĩa hình thức rõ ràng. |
| `LOC-LEC-AN-CH02` | *Chương 2: Mô hình dữ liệu quan hệ & ER* | `LECTURES_PART1.pdf` | 45–85 / 262 | **A** | UIT | GV. Phan Nguyễn Thụy An (Khoa HTTT) | Khái niệm Quan hệ, Bộ, Thuộc tính, Miền giá trị, Khóa (Superkey, Candidate, PK, FK), Ký hiệu ER, Ánh xạ ER $\rightarrow$ Relational | Có ví dụ ánh xạ Chuyên biệt hóa / Tổng quát hóa (Is-a). |
| `LOC-LEC-LONG-CH01` | *Tài liệu bài giảng: Chương 1 - Tổng quan* | `LECTURES_PART1.pdf` | 86–148 / 262 | **A** | UIT | ThS. Dương Phi Long (longdp@uit.edu.vn) | Dữ liệu thô vs Thông tin, File System, 4 đối tượng sử dụng, 4 nhóm ngôn ngữ (DDL, DML, SQL, DCL), 3 mức biểu diễn | Slide thiết kế hiện đại, giải thích chi tiết mức vật lý/logic/ngoài. |
| `LOC-LEC-LONG-CH02` | *Tài liệu bài giảng: Chương 2 - Mô hình dữ liệu quan hệ* | `LECTURES_PART1.pdf` | 149–203 / 262 | **A** | UIT | ThS. Dương Phi Long (longdp@uit.edu.vn) | E.F. Codd (1970), Thuộc tính, Quan hệ $R(A_1..A_n)$, Bộ $t \in R$, Thể hiện $T_R$, Tân từ $\|\|R\|\|$, Phép chiếu $R[X]$, Phân loại Khóa | Sử dụng lược đồ `SINHVIEN` - `LOP` minh họa trực quan. |
| `LOC-LEC-LONG-CH03` | *Tài liệu bài giảng: Chương 3 - Đại số quan hệ* | `LECTURES_PART1.pdf` | 204–262 / 262 | **A** | UIT | ThS. Dương Phi Long (longdp@uit.edu.vn) | Chọn $\sigma$, Chiếu $\pi$, Đổi tên $\rho$, Tích Đề-các $\times$, Kết Theta/Equi/Natural/Outer, Hội $\cup$, Giao $\cap$, Trừ $-$, Chia $\div$, Gom nhóm $\Im$ | Định nghĩa toán học chuẩn mực; có ví dụ chạy khô từng phép toán. |
| `LOC-LEC-LONG-CH05` | *Chương 5: Ràng buộc toàn vẹn trong CSDL* | `LECTURES_PART2.pdf` | 1–39 / 94 | **A** | UIT | ThS. Dương Phi Long (longdp@uit.edu.vn) | Khái niệm RBTV, Bối cảnh, Nội dung, Bảng tầm ảnh hưởng 3 thao tác, 7 phân loại RBTV, Đồ thị chu trình, Bảng tầm ảnh hưởng tổng hợp | Tài liệu nguồn tối thượng cho dạng bài RBTV tại UIT. |
| `LOC-LEC-LONG-CH06` | *Chương 6: Phụ thuộc hàm và dạng chuẩn* | `LECTURES_PART2.pdf` | 40–94 / 94 | **A** | UIT | ThS. Dương Phi Long (longdp@uit.edu.vn) | Tiên đề Armstrong (F1–F6), Bao đóng $F^+$ và $X^+$, Bài toán thành viên, Phủ tối thiểu $F_c$, Thuật toán tìm khóa (Ng, Tg, Tr), 1NF, 2NF, 3NF, BCNF | Thuật toán chuẩn mực UIT: phân loại tập nguồn Ng, trung gian Tg, treo Tr. |

---

### B. Nhóm Đề Thi & Ôn Tập (Consolidated Exams & Reviews)

| Source ID | Tên tài liệu gốc | Tệp vận chuyển | Vị trí trang PDF | Authority Tier | Ownership | Provenance Class | Học kỳ / Năm học | Chủ đề & Lược đồ kiểm tra |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `LOC-EXAM-2023-2024-MID-D1` | *Đề thi Giữa kỳ HK1 2023–2024 (Đề 1)* | `EXAMS_REVIEW.pdf` | 1–2 / 25 | **B** | UIT | `strong-provenance-local` | HK1 2023–2024 | • Câu 1 (2.5đ): PCCC Chung cư (ERD + Ánh xạ)<br>• Câu 2 (7.5đ): Cửa hàng hoa (`NHAVUON`, `SANPHAM`, `DONHANG`, `CTDH`, `GIAOHANG`) - SQL (CHECK, UPDATE) + 6 câu ĐSQH (Outer Join, Phép chia, Gom nhóm). |
| `LOC-EXAM-2023-2024-MID-D2` | *Đề thi Giữa kỳ HK1 2023–2024 (Đề 2)* | `EXAMS_REVIEW.pdf` | 3–4 / 25 | **B** | UIT | `strong-provenance-local` | HK1 2023–2024 | • Câu 1 (2.5đ): Thiết bị báo cháy & Phiếu kiểm tra<br>• Câu 2 (7.5đ): Cửa hàng hoa - SQL + 6 câu ĐSQH (Lọc ngày tháng, Phép trừ, Gom nhóm, Phép chia). |
| `LOC-EXAM-K18-2024-1-SOL` | *Đáp án Đề thi CSDL Khóa 18 (2024-1)* | `EXAMS_REVIEW.pdf` | 5–7 / 25 | **C** | Student / Review | `review-material` | 2024-1 (K18) | Bản giải tay chi tiết biểu điểm từng bước: ERD Tài khoản Ngân hàng (0.5đ/thực thể, 0.25đ/thuộc tính) và ĐSQH Giải đấu thể thao. |
| `LOC-REV-2024-10-01` | *Bài tập ôn luyện ngày 01/10/2024* | `EXAMS_REVIEW.pdf` | 8–11 / 25 | **B** | UIT | `strong-provenance-local` | 2024-2025 | • Bài 1: Quản lý bán xe máy trả góp (12 câu ĐSQH + 4 câu SQL DDL/UPDATE)<br>• Bài 2: Nhà hàng White Palace (`NHANVIEN`, `SANH`, `LOAITIEC`, `TIEC`, `PHUCVU` - 12 câu ĐSQH). |
| `LOC-REV-DSQH-2024` | *DSQH Ôn tập giữa kỳ 2024 SV* | `EXAMS_REVIEW.pdf` | 12–13 / 25 | **B** | UIT | `strong-provenance-local` | 2024-2025 | • Phần 1: ERD Quản lý xăng dầu<br>• Phần 2: Quản lý vé xe khách (`XE`, `TUYEN`, `KHACH`, `VEXE` - SQL DDL/DML + 11 câu ĐSQH). |
| `LOC-HW-23520266-1` | *Homework 1 - Vẽ ERD (SV 23520266)* | `EXAMS_REVIEW.pdf` | 14–19 / 25 | **C** | Student | `student-work` | 2024 | Bài tập vẽ ERD: Môn học - Đồ án - Sinh viên, Khách hàng - Hợp đồng - Trang phục, v.v. |
| `LOC-HW-23520266-2` | *Homework 2 - Ánh xạ ERD (SV 23520266)* | `EXAMS_REVIEW.pdf` | 20–25 / 25 | **C** | Student | `student-work` | 2024 | Ánh xạ ERD sang Lược đồ quan hệ: 7 bài toán thực tế (Xăng dầu, Xe khách, Bệnh viện COVID-19, v.v.). |

---

### C. Nhóm Mã Nguồn Thực Hành & Workbook Dữ Liệu

| Source ID | Tên tệp / Khối | Khối / Sheet | SHA-256 | Authority Tier | Ownership | Mục đích & Nội dung kỹ thuật |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| `LOC-SQL-LAB01` | `[Lab01]23520266-PhanHongDat.sql` | Block 1 | `d2dd8c44...` | **C** | Student | DDL tạo Database `QuanLyBanHang` & `QuanLyGiaoVu`, khai báo PK/FK, `ALTER TABLE`, thêm cột, đặt `CHECK` constraint. |
| `LOC-SQL-LAB02` | `[Lab02]23520266-PhanHongDat.sql` | Block 3 | `ae90300e...` | **C** | Student | DML `INSERT` toàn bộ dữ liệu mẫu QLBH & QLGV, lệnh `UPDATE`, các câu truy vấn cơ bản (WHERE, LIKE, BETWEEN, ORDER BY). |
| `LOC-SQL-LAB03` | `[Lab03]23520266-PhanHongDat.sql` | Block 4 | `e2cc9dc8...` | **C** | Student | Truy vấn nâng cao: `UNION`, `INTERSECT`, `EXCEPT`, phép chia bằng Double `NOT EXISTS`, `UPDATE` tính điểm trung bình học viên, xếp loại `CASE WHEN`. |
| `LOC-SQL-LAB04` | `[Lab04]23520266-PhanHongDat.sql` | Block 5 | `2d9e5c53...` | **C** | Student | Hàm kết hợp (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`), gom nhóm `GROUP BY / HAVING`, hàm xếp hạng `RANK() OVER()`, `TOP WITH TIES`. |
| `LOC-SQL-LAB04-ALL` | `[Lab04]23520266-Phan Hồng Đạt.sql` | Block 6 | `60c193ab...` | **C** | Student | Tệp tổng hợp toàn bộ 4 buổi thực hành Lab01 đến Lab04 trong một tệp duy nhất. |
| `LOC-NOTE-NHAP` | `nhap.txt` | Block 7 | `56b451be...` | **C** | Student | Ghi chú mẹo làm bài thi: toán tử `>= ALL`, `= ALL`, 2 cách viết phép chia (`NOT EXISTS` vs `COUNT / GROUP BY`), quy tắc tìm khóa và dạng chuẩn. |
| `LOC-XLSX-QLBH` | `QLBANHANG.xlsx` | 5 sheets | - | **B** | Course Artifact | Bảng tính dữ liệu mẫu chuẩn QLBH gồm `SANPHAM` (24 dòng), `HOADON` (23 dòng), `NHANVIEN` (5 dòng), `KHACHHANG` (10 dòng), `CTHD` (47 dòng). |
| `LOC-HW-23520266-5` | `23520266_Homework5_CSDL.docx` | 533 đoạn | - | **C** | Student / Reconstruction | Đề bài và bài giải SQL qua 6 năm đề thi UIT: 2017–2018 (Ngân hàng), 2018–2019 (Nhà cung cấp), 2019–2020 (Thế vận hội), 2020–2021 (Phòng khám), 2022–2023 (Xe trả góp), 2023–2024 (Đề tài nghiên cứu). |
