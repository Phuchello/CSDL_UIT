# Danh Bộ Hiện Vật Đề Thi & Bài Tập Chuẩn Hóa (Canonical Artifact Registry) — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31
**Nguyên tắc:** Phân tách rạch ròi giữa 4 loại hiện vật (`exam`, `practical-exam`, `review`, `lab-corpus`). Mỗi hiện vật chuẩn hóa đều liệt kê chi tiết bản gốc cục bộ và các bản sao mirror thực tế để chứng minh tính khử trùng lặp một cách cơ học và minh bạch.

---

## 1. Thống Kê Hiện Vật Chuẩn Hóa Theo Loại Hình (Artifact Summary Counts)

- **Đề thi Lý thuyết / Tự luận (Canonical Exam Artifacts)**: **11**
- **Đề thi Thực hành phòng máy (Canonical Practical Exam Artifacts)**: **2**
- **Tài liệu Ôn tập & Bài tập lớn (Review Artifacts)**: **3**
- **Hệ thống Mã nguồn Thực hành Chuẩn (Lab Corpus)**: **1**
- **TỔNG SỐ HIỆN VẬT CHUẨN HÓA (TOTAL CANONICAL ARTIFACTS)**: **17**

---

## 2. Danh Bộ Chi Tiết Các Hiện Vật Chuẩn Hóa

### A. Nhóm Đề Thi Lý Thuyết / Tự Luận (`exam`) — 11 Hiện Vật

#### 1. `EXAM-2023-2024-HK1-MID-D1`
- **Năm học / Học kỳ**: 2023–2024 / HK1
- **Loại hiện vật**: `exam` (Đề thi Giữa kỳ - Đề 1)
- **Môn học / Thời gian**: IT004 – Cơ sở dữ liệu (CQ + CLC) / 75 phút
- **Provenance Class**: `strong-provenance-local`
- **Bản sao cục bộ (Local Copy)**: `LOC-EXAM-2023-2024-MID-D1` (`CSDL_UIT_LOCAL_EXAMS_REVIEW.pdf`, Tr. 1–2)
- **Bản sao Web (Document-Level Mirrors)**:
  - Mirror 1: [Studocu IT004 Midterm Exam Preview](https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/co-so-du-lieu/de-thi-giua-ky-mon-co-so-du-lieu-khoa-he-thong-thong-tin/81121063) (Header: Khoa HTTT, Môn CSDL CQ+CLC, 75 phút)
- **Lược đồ CSDL**: PCCC Chung cư (ERD) + Cửa hàng hoa (`NHAVUON`, `SANPHAM`, `DONHANG`, `CTDH`, `GIAOHANG`)
- **Nội dung kiểm tra**: Câu 1: Xây dựng ERD và ánh xạ sang lược đồ quan hệ (2.5đ); Câu 2: SQL DDL/UPDATE (1.5đ) + 6 câu ĐSQH (6.0đ).
- **Mức độ tin cậy**: `HIGH` (Hiện vật cục bộ có đầy đủ tiêu đề, mã đề, chuẩn đầu ra G1, G2).

#### 2. `EXAM-2023-2024-HK1-MID-D2`
- **Năm học / Học kỳ**: 2023–2024 / HK1
- **Loại hiện vật**: `exam` (Đề thi Giữa kỳ - Đề 2)
- **Môn học / Thời gian**: IT004 – Cơ sở dữ liệu (CQ + CLC) / 75 phút
- **Provenance Class**: `strong-provenance-local`
- **Bản sao cục bộ (Local Copy)**: `LOC-EXAM-2023-2024-MID-D2` (`CSDL_UIT_LOCAL_EXAMS_REVIEW.pdf`, Tr. 3–4)
- **Bản sao Web (Document-Level Mirrors)**:
  - Mirror 1: Studocu Course 131131 (Bản lưu trữ đề 2)
- **Lược đồ CSDL**: Báo cháy Chung cư & Phiếu kiểm tra (ERD) + Cửa hàng hoa (`NHAVUON`, `SANPHAM`, `DONHANG`, `CTDH`, `GIAOHANG`)
- **Nội dung kiểm tra**: Câu 1: ERD và ánh xạ (2.5đ); Câu 2: SQL DDL/UPDATE (1.5đ) + 6 câu ĐSQH phân bậc (6.0đ).
- **Mức độ tin cậy**: `HIGH` (Hiện vật cục bộ đầy đủ tiêu đề trường, khoa, thời gian làm bài).

#### 3. `EXAM-2023-2024-HK1-FINAL-01`
- **Năm học / Học kỳ**: 2023–2024 / HK1
- **Loại hiện vật**: `exam` (Đề thi Cuối kỳ)
- **Môn học / Thời gian**: IT004 – Cơ sở dữ liệu / 90 phút (Ngày thi: 09/01/2024)
- **Provenance Class**: `community-mirror` / `student-reconstruction`
- **Bản sao cục bộ (Local Copy)**: `LOC-HW-23520266-5` (Đoạn 469–533 trong `23520266_Homework5_CSDL.docx`)
- **Bản sao Web (Document-Level Mirrors)**:
  - Mirror 1: [Studocu IT004 Final Exam 2023-2024](https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/co-so-du-lieu/de-thi-cuoi-ky-co-so-du-lieu-hoc-ky-1-nam-2023-2024/81121063) (Preview xác nhận ngày thi 09/01/2024, 90 phút)
- **Lược đồ CSDL**: Đề tài nghiên cứu khoa học (`DETAI`, `GIANGVIEN`, `THAMGIA_DT`, `BAOBAO`) + Quan hệ phổ quát $R(U)$
- **Nội dung kiểm tra**: Viết câu lệnh SQL (JOIN, NOT EXISTS, GROUP BY/HAVING), phát biểu RBTV và bài toán Chuẩn hóa BCNF.
- **Mức độ tin cậy**: `MEDIUM-HIGH` (Khớp giữa bài tập sinh viên và bản xem trước Studocu có ngày thi cụ thể).

#### 4. `EXAM-2022-2023-HK1-MID-D2`
- **Năm học / Học kỳ**: 2022–2023 / HK1
- **Loại hiện vật**: `exam` (Đề thi Giữa kỳ - Đề 2)
- **Môn học / Thời gian**: IT004 – Cơ sở dữ liệu / 75 phút
- **Provenance Class**: `student-reconstruction` / `community-mirror`
- **Bản sao cục bộ (Local Copy)**: `LOC-HW-23520266-5` (Đoạn 414–468)
- **Bản sao Web (Document-Level Mirrors)**:
  - Mirror 1: [Studocu Đề thi giữa kỳ CSDL HK1 2022-2023](https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/co-so-du-lieu/de-thi-giua-ky-csdl-hk1-2022-2023-lop-cq-clc/41982736)
  - Mirror 2: GitHub repo `SeaW1nd/IT004-CSDL` (Thư mục đề thi)
- **Lược đồ CSDL**: Quản lý mua bán xe máy trả góp (`KHACHHANG`, `LOAIXE`, `XEMAY`, `LOAIHINHTG`, `TRAGOP`)
- **Nội dung kiểm tra**: 6 câu truy vấn SQL lồng nhau, sắp xếp `ORDER BY KYHAN DESC`, và lọc dữ liệu.
- **Mức độ tin cậy**: `MEDIUM-HIGH` (Bản chép đề của sinh viên được đối chiếu với liên kết trực tiếp trên Studocu).

#### 5. `EXAM-2020-2021-HK1-FINAL-01`
- **Năm học / Học kỳ**: 2020–2021 / HK1
- **Loại hiện vật**: `exam` (Đề thi Cuối kỳ - Đề 1)
- **Môn học / Thời gian**: IT004 – Cơ sở dữ liệu / 90 phút
- **Provenance Class**: `student-reconstruction`
- **Bản sao cục bộ (Local Copy)**: `LOC-HW-23520266-5` (Đoạn 365–413)
- **Bản sao Web (Document-Level Mirrors)**:
  - Mirror 1: Scribd Document `IT004-De-Thi-Cuoi-Ky-2020-2021`
  - Mirror 2: GitHub repo `UIT-DS/IT004.L19-Database`
- **Lược đồ CSDL**: Quản lý khám bệnh (`BACSI`, `PHONGKHAM`, `BENHNHAN`, `KHAMBENH`, `TOATHUOC`)
- **Nội dung kiểm tra**: Truy vấn SQL gom nhóm, đếm số lượt khám `COUNT(MAKB)`, truy vấn `WHERE NOT EXISTS`, và ràng buộc toàn vẹn.
- **Mức độ tin cậy**: `MEDIUM` (Dựa trên bản chép đề và giải bài tập của sinh viên trong Homework 5).

#### 6. `EXAM-2019-2020-HK1-MID-D1`
- **Năm học / Học kỳ**: 2019–2020 / HK1
- **Loại hiện vật**: `exam` (Đề thi Giữa kỳ - Đề 1)
- **Môn học / Thời gian**: IT004 – Cơ sở dữ liệu / 75 phút
- **Provenance Class**: `student-reconstruction`
- **Bản sao cục bộ (Local Copy)**: `LOC-HW-23520266-5` (Đoạn 275–316)
- **Bản sao Web (Document-Level Mirrors)**:
  - Mirror 1: GitHub repo `UIT-DS/IT004.L19-Database` (Thư mục DeThi)
  - Mirror 2: Studocu Course 131131
- **Lược đồ CSDL**: Quản lý Thế vận hội (`VANDONGVIEN`, `THEVANHOI`, `NOIDUNGTHI`, `THAMGIA`)
- **Nội dung kiểm tra**: 6 câu ĐSQH/SQL: VĐV quốc tịch 'UK', thi Bắn cung tại Olympic Tokyo 2020, huy chương vàng Nhật Bản, phép giao 2 nội dung thi, phép chia VĐV tham gia tất cả các kỳ thế vận hội từ 2008.
- **Mức độ tin cậy**: `MEDIUM-HIGH` (Nội dung đề bài chi tiết, cấu trúc chuẩn mực UIT).

#### 7. `EXAM-2019-2020-HK1-MID-D2`
- **Năm học / Học kỳ**: 2019–2020 / HK1
- **Loại hiện vật**: `exam` (Đề thi Giữa kỳ - Đề 2)
- **Môn học / Thời gian**: IT004 – Cơ sở dữ liệu / 75 phút
- **Provenance Class**: `student-reconstruction`
- **Bản sao cục bộ (Local Copy)**: `LOC-HW-23520266-5` (Đoạn 317–364)
- **Bản sao Web (Document-Level Mirrors)**:
  - Mirror 1: GitHub repo `UIT-DS/IT004.L19-Database`
- **Lược đồ CSDL**: Quản lý Thế vận hội (`VANDONGVIEN`, `THEVANHOI`, `NOIDUNGTHI`, `THAMGIA`)
- **Nội dung kiểm tra**: 6 câu ĐSQH/SQL: VĐV Nữ quốc tịch 'JA', thi Điền kinh Rio 2016, huy chương bạc Trung Quốc 2012, phép trừ nội dung thi, phép chia VĐV Nam người Đức tham gia tất cả thế vận hội từ 2012.
- **Mức độ tin cậy**: `MEDIUM-HIGH` (Bản đề đối xứng hoàn hảo với Đề 1).

#### 8. `EXAM-2018-2019-HK1-MID-D1`
- **Năm học / Học kỳ**: 2018–2019 / HK1
- **Loại hiện vật**: `exam` (Đề thi Giữa kỳ - Đề 1)
- **Môn học / Thời gian**: IT004 – Cơ sở dữ liệu / 75 phút
- **Provenance Class**: `student-reconstruction`
- **Bản sao cục bộ (Local Copy)**: `LOC-HW-23520266-5` (Đoạn 157–227)
- **Bản sao Web (Document-Level Mirrors)**:
  - Mirror 1: Studocu Course 131131
  - Mirror 2: Scribd Document `De-Thi-CSDL-2018-2019`
- **Lược đồ CSDL**: Quản lý Nhà cung cấp & Đơn đặt hàng (`NHACUNGCAP`, `MATHANG`, `DONDATHANG`, `CTDDH`)
- **Nội dung kiểm tra**: Đơn hàng nhà cung cấp 'Vinamilk' > 1.000.000đ, tổng số lượng mặt hàng 'MH001', NCC cung cấp hàng VN nhưng không cung cấp hàng TQ, gom nhóm theo năm, phép chia đơn hàng đặt tất cả mặt hàng của 'Vissan'.
- **Mức độ tin cậy**: `MEDIUM-HIGH` (Khảo sát chi tiết 2 cách giải: phép trừ vs truy vấn lồng).

#### 9. `EXAM-2018-2019-HK1-MID-D2`
- **Năm học / Học kỳ**: 2018–2019 / HK1
- **Loại hiện vật**: `exam` (Đề thi Giữa kỳ - Đề 2)
- **Môn học / Thời gian**: IT004 – Cơ sở dữ liệu / 75 phút
- **Provenance Class**: `student-reconstruction`
- **Bản sao cục bộ (Local Copy)**: `LOC-HW-23520266-5` (Đoạn 228–274)
- **Bản sao Web (Document-Level Mirrors)**:
  - Mirror 1: Studocu Course 131131
- **Lược đồ CSDL**: Quản lý Nhà cung cấp & Đơn đặt hàng (`NHACUNGCAP`, `MATHANG`, `DONDATHANG`, `CTDDH`)
- **Nội dung kiểm tra**: NCC cung cấp 'MH0001' từ 01/01/2018, tổng thành tiền 'MH014' từ 'NCC007', NCC cung cấp hàng Mỹ nhưng không cung cấp hàng Hàn Quốc, phép chia đơn hàng đặt tất cả mặt hàng của 'Vinamilk'.
- **Mức độ tin cậy**: `MEDIUM-HIGH` (Bản đề đối xứng chuẩn với Đề 1).

#### 10. `EXAM-2017-2018-HK1-MID-D1`
- **Năm học / Học kỳ**: 2017–2018 / HK1
- **Loại hiện vật**: `exam` (Đề thi Giữa kỳ - Đề 1)
- **Môn học / Thời gian**: IT004 – Cơ sở dữ liệu / 75 phút
- **Provenance Class**: `student-reconstruction`
- **Bản sao cục bộ (Local Copy)**: `LOC-HW-23520266-5` (Đoạn 57–106)
- **Bản sao Web (Document-Level Mirrors)**:
  - Mirror 1: Studocu Course 131131
  - Mirror 2: Scribd Archive
- **Lược đồ CSDL**: Quản lý Tài khoản Ngân hàng (`KHACHHANG`, `TAIKHOAN`, `LOAITK`, `GIAODICH`, `LOAIGD`)
- **Nội dung kiểm tra**: Tài khoản mở ngày 01/01/2017 sắp xếp tăng dần, tổng tiền theo loại GD, khách hàng mở cả 2 loại TK tiết kiệm và thanh toán, phép chia KH mở tất cả các loại TK, loại TK mở nhiều nhất năm 2016.
- **Mức độ tin cậy**: `MEDIUM-HIGH` (Đầy đủ cấu trúc câu 1.2 từ a đến f).

#### 11. `EXAM-2017-2018-HK1-MID-D2`
- **Năm học / Học kỳ**: 2017–2018 / HK1
- **Loại hiện vật**: `exam` (Đề thi Giữa kỳ - Đề 2)
- **Môn học / Thời gian**: IT004 – Cơ sở dữ liệu / 75 phút
- **Provenance Class**: `student-reconstruction`
- **Bản sao cục bộ (Local Copy)**: `LOC-HW-23520266-5` (Đoạn 107–156)
- **Bản sao Web (Document-Level Mirrors)**:
  - Mirror 1: Studocu Course 131131
- **Lược đồ CSDL**: Quản lý Tài khoản Ngân hàng (`KHACHHANG`, `TAIKHOAN`, `LOAITK`, `GIAODICH`, `LOAIGD`)
- **Nội dung kiểm tra**: Giao dịch ngày 01/01/2017 giảm dần số tiền, tổng số dư theo loại TK, KH mở cả 2 loại TK thanh toán và vay, phép chia TK thực hiện tất cả loại GD, KH có số lượng TK 'chưa kích hoạt' nhiều nhất.
- **Mức độ tin cậy**: `MEDIUM-HIGH` (Bản đề đối xứng hoàn chỉnh).

---

### B. Nhóm Đề Thi Thực Hành Phòng Máy (`practical-exam`) — 2 Hiện Vật

#### 12. `PRAC-2023-2024-HK1-O117`
- **Năm học / Học kỳ**: 2023–2024 / HK1
- **Loại hiện vật**: `practical-exam` (Đề thi Thực hành - Lớp O117)
- **Môn học / Thời gian**: IT004 – Cơ sở dữ liệu / 90 phút
- **Provenance Class**: `community-mirror`
- **Bản sao Web (Document-Level Mirrors)**:
  - Mirror 1: [Studocu IT004.O117 Practical Exam Preview](https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/co-so-du-lieu/it004o117-de-1-de-thi-thuc-hanh-csdl/110260821) (Header: Trường ĐH CNTT, Môn CSDL, Lớp IT004.O117, 90 phút)
- **Nội dung kiểm tra**: Viết script T-SQL tạo bảng, tạo khóa chính/ngoại, viết câu lệnh INSERT, Trigger kiểm tra ràng buộc toàn vẹn, và 4 câu truy vấn nâng cao.
- **Mức độ tin cậy**: `HIGH` (Bản xem trước tài liệu có đầy đủ tiêu đề chính thức của trường).

#### 13. `PRAC-2024-2025-HK1-302`
- **Năm học / Học kỳ**: 2024–2025 / HK1
- **Loại hiện vật**: `practical-exam` (Đề thi Thực hành - Đề 302)
- **Môn học / Thời gian**: IT004 – Cơ sở dữ liệu / 90 phút
- **Provenance Class**: `community-mirror`
- **Bản sao Web (Document-Level Mirrors)**:
  - Mirror 1: [Studocu Practical Exam 302 Preview](https://www.studocu.vn/vn/document/university-of-information-technology/co-so-du-lieu/it004-th2425-de-thi-thuc-hanh-co-so-du-lieu-302/149081939)
- **Nội dung kiểm tra**: Tạo bảng, khóa chính, ràng buộc CHECK, Trigger cập nhật dữ liệu tự động, và truy vấn thống kê gom nhóm.
- **Mức độ tin cậy**: `HIGH` (Đề thi thực hành máy có mã đề 302, khớp với thông báo thi của Khoa HTTT `UIT-O06`).

---

### C. Nhóm Tài Liệu Ôn Tập & Bài Tập Lớn (`review`) — 3 Hiện Vật

#### 14. `REV-2024-10-01-EXP`
- **Năm học / Học kỳ**: 2024–2025 / HK1
- **Loại hiện vật**: `review` (Bài tập ôn luyện chuyên sâu ngày 01/10/2024)
- **Provenance Class**: `strong-provenance-local`
- **Bản sao cục bộ (Local Copy)**: `LOC-REV-2024-10-01` (`CSDL_UIT_LOCAL_EXAMS_REVIEW.pdf`, Tr. 8–11)
- **Lược đồ CSDL**: Quản lý bán xe máy trả góp (12 câu ĐSQH + 4 câu SQL DDL/UPDATE) + Nhà hàng White Palace (`NHANVIEN`, `SANH`, `LOAITIEC`, `TIEC`, `PHUCVU` - 12 câu ĐSQH).
- **Mức độ tin cậy**: `HIGH` (Bài tập chính thức của lớp CSDL UIT).

#### 15. `REV-2024-DSQH-MID`
- **Năm học / Học kỳ**: 2024–2025 / HK1
- **Loại hiện vật**: `review` (Đề cương ôn thi giữa kỳ ĐSQH 2024 SV)
- **Provenance Class**: `strong-provenance-local`
- **Bản sao cục bộ (Local Copy)**: `LOC-REV-DSQH-2024` (`CSDL_UIT_LOCAL_EXAMS_REVIEW.pdf`, Tr. 12–13)
- **Lược đồ CSDL**: Phần 1: Quản lý Xăng dầu (ERD); Phần 2: Quản lý Vé xe khách (`XE`, `TUYEN`, `KHACH`, `VEXE` - 3 câu SQL DDL/DML + 11 câu ĐSQH).
- **Mức độ tin cậy**: `HIGH` (Đề cương ôn tập chính thức do giảng viên/bộ môn biên soạn).

#### 16. `REV-2024-K18-SOL`
- **Năm học / Học kỳ**: 2024 / K18 (Đợt 1)
- **Loại hiện vật**: `review` (Bản giải đáp án đề thi CSDL Khóa 18)
- **Provenance Class**: `review-material`
- **Bản sao cục bộ (Local Copy)**: `LOC-EXAM-K18-2024-1-SOL` (`CSDL_UIT_LOCAL_EXAMS_REVIEW.pdf`, Tr. 5–7)
- **Lược đồ CSDL**: ERD Khách hàng - Tài khoản - Giao dịch + ĐSQH & SQL Quản lý giải đấu thể thao.
- **Nội dung**: Bản viết tay chi tiết barem điểm chấm thi (0.5đ/thực thể, 0.25đ/thuộc tính, 0.25đ/phép chiếu).
- **Mức độ tin cậy**: `MEDIUM-HIGH` (Cung cấp góc nhìn thực tế về barem chấm thi của giám khảo).

---

### D. Nhóm Hệ Thống Mã Nguồn Thực Hành Chuẩn (`lab-corpus`) — 1 Hiện Vật

#### 17. `LAB-QLBH-QLGV-CORPUS`
- **Loại hiện vật**: `lab-corpus` (Hệ thống thực hành SQL Server 4 buổi chuẩn hóa)
- **Provenance Class**: `strong-provenance-local`
- **Bản sao cục bộ (Local Copies)**:
  - `LOC-SQL-LAB01`: `[Lab01]23520266-PhanHongDat.sql` (SHA256: `d2dd8c44...`)
  - `LOC-SQL-LAB02`: `[Lab02]23520266-PhanHongDat.sql` (SHA256: `ae90300e...`)
  - `LOC-SQL-LAB03`: `[Lab03]23520266-PhanHongDat.sql` (SHA256: `e2cc9dc8...`)
  - `LOC-SQL-LAB04`: `[Lab04]23520266-PhanHongDat.sql` (SHA256: `2d9e5c53...`)
  - `LOC-SQL-LAB04-ALL`: `[Lab04]23520266-Phan Hồng Đạt.sql` (SHA256: `60c193ab...`)
  - `LOC-NOTE-NHAP`: `nhap.txt` (SHA256: `56b451be...`)
  - `LOC-XLSX-QLBH`: `QLBANHANG.xlsx` (5 sheets chuẩn: `SANPHAM`, `HOADON`, `NHANVIEN`, `KHACHHANG`, `CTHD`)
- **Bản sao Web (Document-Level Mirrors)**:
  - Mirror 1: [GitHub SeaW1nd/IT004-CSDL](https://github.com/SeaW1nd/IT004-CSDL)
  - Mirror 2: [GitHub HiImKing1509/IT004_Database](https://github.com/HiImKing1509/IT004_Database)
  - Mirror 3: [GitHub UIT-DS/IT004.L19-Database](https://github.com/UIT-DS/IT004.L19-Database)
- **Nội dung**: Toàn bộ hệ thống 44 câu truy vấn QLBH và 35 câu truy vấn QLGV cùng 14 ràng buộc CHECK/Trigger.
- **Mức độ tin cậy**: `HIGH` (Bộ dữ liệu thực hành xuyên suốt của UIT).
