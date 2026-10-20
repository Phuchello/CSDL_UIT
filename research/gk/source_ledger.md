# BẢNG KÊ NGUỒN TÀI LIỆU GIỮA KỲ IT004 (GK SOURCE LEDGER)

**Dự án:** `Phuchello/CSDL_UIT` — Module Giữa Kỳ (GK) IT004  
**Biên soạn & Thẩm định:** Lead Academic Researcher & QA Auditor  
**Thời điểm khóa sổ:** Học kỳ 1, 2024–2025 / 2025–2026 Snapshot  
**Nguyên tắc pháp lý & Thẩm quyền:**  
Phân định rạch ròi 4 cấp độ thẩm quyền (`Tier A`: Quy chuẩn/Chính thức; `Tier B`: Bản scan/Đề thi gốc có nguồn gốc kiểm chứng; `Tier C`: Bản tái hiện cộng đồng/Sinh viên; `Tier D`: Lead chưa kiểm chứng). Tuân thủ nguyên tắc bản quyền: Không re-upload đề thi bên thứ ba; toàn bộ lời giải, bài tập mô phỏng và cheat sheet được biên soạn mới hoàn toàn.

---

## 1. Danh Mục Nguồn Nền Tảng & Quy Chuẩn (Tier A)

| Source ID | Tên tài liệu & Định danh gốc | Cơ quan / Nguồn phát hành | Vai trò học thuật | Tình trạng truy cập |
| :--- | :--- | :--- | :--- | :--- |
| **UIT-O01** | CTĐT Cử nhân HTTT / KHMT / KTPM / KTMT | Trường ĐH Công nghệ Thông tin – ĐHQG-HCM | Xác định chuẩn đầu ra môn IT004 (3 TC LT + 1 TC TH) | Truy cập công khai qua student.uit.edu.vn |
| **UIT-O02** | Danh mục môn học đại học & Đề cương IT004 | Khoa Hệ thống Thông tin — UIT | Phạm vi kiểm tra GK: ERD, Ánh xạ ER $\to$ Schema, ĐSQH, SQL cơ bản/nâng cao | Lưu trữ chính thức |
| **UIT-O11** | Thông báo quy chế & Lịch thi GK tập trung | Phòng Khảo thí & ĐBCL (OEP - UIT) | Quy định hình thức: Tự luận 75 phút, không sử dụng tài liệu | Công khai qua oep.uit.edu.vn |
| **LOC-LEC-CH01** | Bài giảng Chương 1: Tổng quan hệ CSDL | Giảng viên UIT (ThS. Đỗ Phúc Long, ThS. Nguyễn Đình Hiển) | Khái niệm DBMS, tính độc lập dữ liệu, 3 mức ANSI/SPARC | Tệp cục bộ `_BaiGiangLyThuyet_CSDL - B01_sv.pdf` |
| **LOC-LEC-CH02** | Bài giảng Chương 2: Mô hình thực thể & Mô hình quan hệ | Giảng viên UIT | Ký pháp ERD chuẩn UIT: Thực thể, Thuộc tính, Bản số $(min, max)$, Quy tắc ánh xạ 1:1, 1:N, M:N | Tệp cục bộ `_BaiGiangLyThuyet_CSDL - Chuong 2_MHDLQH - 2024-sv.pdf` |
| **LOC-LEC-CH03** | Bài giảng Chương 3: Đại số quan hệ (ĐSQH) | Giảng viên UIT | Định nghĩa 8 phép toán hình thức: $\sigma, \pi, \rho, \bowtie, \mathbin{⟕}, \cup, \cap, -, \div$ và phép gom nhóm $\gamma$ | Tệp cục bộ `Slide Lụm/DPL_Chuong 3 - Dai so Quan he.pdf` |
| **MS-TSQL-01** | Microsoft Learn: CREATE TABLE & Constraints | Microsoft Learn Transact-SQL Documentation | Cú pháp chuẩn SQL Server: PK, FK, CHECK, DEFAULT, NULL | https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql |
| **MS-TSQL-02** | Microsoft Learn: SELECT - GROUP BY & HAVING | Microsoft Learn Transact-SQL Documentation | Cơ chế gom nhóm và lọc theo hàm tổng hợp (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) | https://learn.microsoft.com/en-us/sql/t-sql/queries/select-group-by-transact-sql |
| **MS-TSQL-03** | Microsoft Learn: EXISTS & Double NOT EXISTS | Microsoft Learn Transact-SQL Documentation | Ngữ nghĩa phép chia trong SQL Server thông qua truy vấn con tương quan | https://learn.microsoft.com/en-us/sql/t-sql/language-elements/exists-transact-sql |
| **MS-TSQL-04** | Microsoft Learn: FROM - JOIN & OUTER JOIN | Microsoft Learn Transact-SQL Documentation | Ngữ nghĩa `LEFT / RIGHT OUTER JOIN`, phân biệt điều kiện đặt tại `ON` vs `WHERE` | https://learn.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql |

---

## 2. Danh Mục Hiện Vật Đề Thi & Barem Chấm Gốc (Tier B — Strong Provenance)

| Source ID | Tên hiện vật / Tệp lưu trữ | Học kỳ / Năm học | Cấu trúc & Lược đồ thực chứng | Mức độ tin cậy |
| :--- | :--- | :--- | :--- | :--- |
| **LOC-EXAM-2324-MID-D1** | `DE-THI-GIUA-KY_CSDL_HK1_2023_2024.pdf` (Tr. 1–2) | HK1 2023–2024 (Đề 1) | **Câu 1 (2.5đ):** ERD PCCC Chung cư & Ánh xạ Schema.<br>**Câu 2 (7.5đ):** CSDL Cửa hàng hoa (`NHAVUON`, `SANPHAM`, `DONHANG`, `CTDH`, `GIAOHANG`). DDL/UPDATE (1.5đ) + 6 câu ĐSQH (6.0đ). | `HIGH` (Bản quét đề thi chính thức UIT, Khoa HTTT) |
| **LOC-EXAM-2324-MID-D2** | `DE-THI-GIUA-KY_CSDL_HK1_2023_2024.pdf` (Tr. 3–4) | HK1 2023–2024 (Đề 2) | **Câu 1 (2.5đ):** ERD Báo cháy Chung cư & Ánh xạ Schema.<br>**Câu 2 (7.5đ):** CSDL Cửa hàng hoa (biến thể câu hỏi). DDL/UPDATE (1.5đ) + 6 câu ĐSQH (6.0đ). | `HIGH` (Bản quét đề thi chính thức UIT, Khoa HTTT) |
| **LOC-REV-2024-10-01** | `bai tap ngay 1_10_2024.pdf` (Tr. 1–2) | HK1 2024–2025 | **Phần 1:** ERD Quản lý Xăng dầu & Ánh xạ sang Lược đồ quan hệ.<br>**Phần 2:** CSDL Tuyến xe khách (`XE`, `TUYEN`, `KHACH`, `VEXE`). DDL ALTER/UPDATE + 5 câu ĐSQH. | `HIGH` (Phiếu ôn tập chính thức trên lớp của giảng viên) |
| **LOC-REV-DSQH-2024** | `DSQH_ontap_giuaky_2024_sv.pdf` (Tr. 1–4) | HK1 2024–2025 | **Bài 1:** CSDL Quản lý bán xe máy trả góp (12 câu ĐSQH bao quát Outer Join, Phép chia, Gom nhóm).<br>**Bài 2:** CSDL Quản lý nhà hàng White Palace (12 câu ĐSQH). | `HIGH` (Đề cương ôn tập Giữa kỳ chuẩn cho sinh viên) |
| **LOC-SOL-K18-2024** | `ĐÁP-ÁN-ĐỀ-THI-CSDL-KHÓA-18-2024-1.pdf` (Tr. 1–3) | Năm 2024 (Đợt 1 Khóa 18) | Bản quét barem điểm viết tay chính thức: Barem điểm chấm ERD (0.5đ/thực thể, 0.25đ/bản số, 0.25đ/thuộc tính) và ĐSQH (0.25đ/phép chọn, 0.25đ/phép kết, 0.5đ/phép chia). | `HIGH` (Barem chấm thi thực tế của hội đồng chấm) |
| **LOC-HW-ASSIGN-02** | `BT2/BT2(new).pdf` (Tr. 1–3) | HK1 2024–2025 | CSDL Quản lý Nghiên cứu Khoa học UIT (`PHONG`, `NV`, `DETAI`, `THAMGIA`, `BAIBAO`, `CONGBOBB`): 8 câu truy vấn nâng cao. | `HIGH` (Bài tập lớn chính thức Khoa HTTT) |

---

## 3. Danh Mục Bản Tái Hiện & Mirror Cộng Đồng (Tier C)

| Source ID | Tên tài liệu / Định danh | Nguồn gốc / Người đăng | Nội dung chứa đựng | Mức độ tin cậy |
| :--- | :--- | :--- | :--- | :--- |
| **LOC-HW-23520266-5** | `23520266_Homework5_CSDL.docx` (533 dòng) | Tác phẩm lưu trữ sinh viên Khóa 2023 | Chép lại đề thi và bài giải 6 năm liên tiếp (2017–2024): Ngân hàng, Nhà cung cấp, Olympic Tokyo/Rio, Bệnh nhân, Căn hộ trả góp, Đề tài NCKH. | `HIGH` (về đề bài) / `MEDIUM` (về lời giải sinh viên) |
| **COM-STU-2425-MID** | Studocu Document 133216780 / Mirror 142893193 | Sinh viên UIT chia sẻ (HK1 2024–2025) | Đề thi Giữa kỳ 2024–2025: Bão lũ cứu trợ thiên tai (ERD 2đ) + ĐSQH/SQL (8đ). | `HIGH` cho header và lược đồ |
| **COM-STU-2223-MID** | Studocu Document 41982736 | Sinh viên UIT chia sẻ (HK1 2022–2023) | Đề thi Giữa kỳ Đề 2 HK1 2022–2023 Lớp CQ+CLC: CSDL Mua bán xe máy trả góp. | `HIGH` |
| **GH-UIT-DS-L19** | GitHub: `UIT-DS/IT004.L19-Database` | Sinh viên Ban Học tập Khoa Khoa học Dữ liệu UIT | Tổng hợp slide bài giảng, đề thi mẫu giữa kỳ và cuối kỳ. | `MEDIUM-HIGH` |

---

## 4. Leads Hạn Chế Truy Cập / Cần Xác Minh Thêm (Tier D)

| Lead ID | URL / Tài liệu | Tình trạng kỹ thuật | Ghi chú xử lý |
| :--- | :--- | :--- | :--- |
| **LEAD-STU-2526-01** | Studocu `149604841` (csdl-2025-2026-hk1) | Trang bị chặn Cloudflare / Captcha 403 | Đánh dấu `ACCESS_LIMITED`. Giữ URL đối chiếu; không dùng làm căn cứ khẳng định cấu trúc đề năm 2025–2026. |
| **LEAD-STU-2122-01** | Studocu `106151828` / `74581029` | Trang yêu cầu Premium/Đăng nhập | Cần đối chiếu nội dung để tránh trùng lặp với bản Đề thi 2021–2022 đã có. |

---

## 5. Tuyên Bố Bản Quyền & Tính Độc Bản Học Thuật

1. **Không sao chép nguyên văn để thương mại hóa**: Mọi văn bản đề thi gốc trong tài liệu chỉ được sử dụng cho mục đích trích dẫn học thuật (Fair Use) và đối chiếu mẫu câu hỏi.
2. **100% Lời giải & Bộ đề ngân hàng là nguyên bản**: Toàn bộ ngân hàng câu hỏi (ERD, ĐSQH, SQL), lời giải chi tiết từng bước, phân tích tư duy, mã nguồn T-SQL kiểm thử và 15 đề mock thi thử 75 phút được biên soạn độc lập bởi **Võ Trọng Phúc**, đảm bảo tính toàn vẹn và độ tin cậy học thuật cao nhất.
