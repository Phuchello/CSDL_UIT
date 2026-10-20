# BÁO CÁO NGHIÊN CỨU SÂU ĐỀ THI GIỮA KỲ IT004 — UIT (DEEP RESEARCH REPORT)

**Dự án:** `Phuchello/CSDL_UIT` — Module Giữa Kỳ (GK) IT004  
**Tác giả & Chủ nhiệm nghiên cứu:** Lead Academic Researcher & Exam-Content Engineer  
**Thời điểm công bố:** Học kỳ 1, 2024–2025 / Chuẩn bị Học kỳ 1, 2025–2026  
**Trạng thái kiểm định:** `GATE R1 AUDITED & VERIFIED`

---

## 1. Tóm Tắt Tổng Quan (Executive Summary)

Báo cáo này tổng kết kết quả nghiên cứu toàn diện từ các nguồn tài liệu chính thức của Trường Đại học Công nghệ Thông tin (UIT), Khoa Hệ thống Thông tin, các đề thi thực tế đã được số hóa qua 8 năm học (2017–2018 đến 2024–2025), slide bài giảng và barem chấm điểm của hội đồng thi.

### Phát hiện cốt lõi:
1. **Quy cách bài thi:** Đề thi Giữa kỳ Lý thuyết môn Cơ sở dữ liệu (IT004) là bài thi **Tự luận, 75 phút, không sử dụng tài liệu, thang điểm 10.0**.
2. **Cấu trúc thực chứng bất biến gồm 2 câu hỏi lớn:**
   - **Câu 1 (2.0 – 2.5 điểm):** Thiết kế mô hình Thực thể – Mối kết hợp (ERD) từ một kịch bản thế giới thực và chuyển đổi sang Mô hình Dữ liệu Quan hệ (xác định rõ PK và FK).
   - **Câu 2 (7.5 – 8.0 điểm):** Cho trước một Lược đồ quan hệ chuẩn (4–6 bảng); bao gồm 1 câu SQL DDL/DML (1.0 – 1.5đ) và 6 câu Đại số quan hệ (6.0 – 6.5đ) phân hóa theo phổ tư duy từ mức độ A (nhận biết, lọc đơn, kết nối cơ bản), B (thông hiểu, kết ngoài "nếu có", gom nhóm $\gamma$, phép tập hợp $\cup, \cap, -$) đến C (vận dụng cao, phép chia $\div$ cho điều kiện "tất cả", câu hỏi cực trị 9–10).
3. **Phạm vi kiến thức tuyệt đối:** Chỉ kiểm tra kiến thức thuộc Chương 1, Chương 2, Chương 3 và một phần ứng dụng T-SQL của Chương 4. Toàn bộ các chuyên đề Ràng buộc toàn vẹn nâng cao (Bảng tầm ảnh hưởng toàn diện), Phụ thuộc hàm, Bao đóng, Khóa ứng viên, Dạng chuẩn 3NF/BCNF và Trigger **thuộc 100% phạm vi Đề thi Cuối kỳ (Final Exam)** và không được phép đưa vào đề thi giữa kỳ.

---

## 2. Phương Pháp Nghiên Cứu & Bằng Chứng Nguồn (Methodology & Evidence Chain)

Quá trình nghiên cứu được triển khai đồng thời trên 3 bình diện:
- **Nghiên cứu Cục bộ (Local Workspace Research):** Khảo sát toàn văn các bản quét đề thi chính thức (`DE-THI-GIUA-KY_CSDL_HK1_2023_2024.pdf`), barem chấm điểm viết tay chính thức (`ĐÁP-ÁN-ĐỀ-THI-CSDL-KHÓA-18-2024-1.pdf`), tài liệu ôn tập trên lớp (`DSQH_ontap_giuaky_2024_sv.pdf`, `bai tap ngay 1_10_2024.pdf`), và tệp tổng hợp 6 năm đề thi của sinh viên khóa 2023 (`23520266_Homework5_CSDL.docx`).
- **Nghiên cứu Web Đa tầng (Multi-tier Web Deep Research):** Khảo sát cổng thông tin sinh viên UIT (`svuit.org`), các repository học tập của sinh viên các khóa trước (`UIT-DS/IT004.L19-Database`, `KevMi-UIT/IT004`, `SeaW1nd/IT004-CSDL`), các mirror đề thi trên Studocu và tài liệu Microsoft Learn về Transact-SQL.
- **Kiểm toán Hiện vật & Loại Trừ Mirror (Dedup & Integrity Audit):**
  - Rà soát toàn bộ 31 hiện vật trong `artifact_registry.md`.
  - Phân tách chính xác: **10 đề thi Giữa kỳ Lý thuyết thật**, **3 tài liệu ôn tập và barem Giữa kỳ**, **7 đề thi Cuối kỳ**, **10 đề thi Thực hành trên máy**, và **1 hệ thống lab corpus**.
  - Không tạo ra bất kỳ con số thống kê hoặc liên kết giả định nào. Các tài liệu bị chặn xác minh bot được phân loại rõ là `ACCESS_LIMITED / UNVERIFIED`.

---

## 3. Phân Tích Tiến Trình Đề Thi Giữa Kỳ Qua Các Thời Kỳ (Historical Trend Analysis)

Qua phân tích 10 đề thi giữa kỳ thực chứng từ 2017 đến 2024:
1. **Giai đoạn 2017–2020 (Mô hình Tập trung Truy vấn):**
   - Đề thi thường tập trung phần lớn vào truy vấn Đại số quan hệ và SQL trên các lược đồ quản lý kinh điển: Tài khoản Ngân hàng (2017–2018), Nhà cung cấp & Đơn hàng (2018–2019), Thế vận hội Olympic (2019–2020), Quản lý Khám bệnh (2020–2021).
   - Thường có 6 câu ĐSQH/SQL với phổ điểm phân bổ đều, luôn có 1 câu Phép chia ("tham gia tất cả các kỳ Olympic", "mở tất cả loại tài khoản") và 1 câu tìm đối tượng cực trị ("nhiều nhất", "ít nhất").
2. **Giai đoạn 2022–2024 (Chuẩn hóa Thiết kế ERD + Truy vấn Phân bậc):**
   - Đề thi chuyển hẳn sang cấu trúc 2 phần: Câu 1 bắt buộc là Xây dựng mô hình ERD và Ánh xạ sang Lược đồ quan hệ (chiếm 2.0 – 2.5 điểm).
   - Ngữ cảnh đề bài mang tính thời sự và gắn liền với thực tiễn kỹ thuật: Hệ thống Phòng cháy chữa cháy chung cư (2023–2024 Đề 1), Thiết bị báo cháy (2023–2024 Đề 2), Quản lý bán căn hộ trả góp (2022–2023 Đề 2).
   - Câu 2 luôn gồm 1 câu SQL DDL (tạo ràng buộc CHECK miền giá trị), 1 câu SQL DML (UPDATE tăng giá/phí có điều kiện), và 6 câu ĐSQH bao quát từ Outer Join ("nếu có") đến Phép chia và Gom nhóm.
3. **Giai đoạn 2024–2025 (Cập nhật Ngữ Cảnh Xã Hội & Tinh Chỉnh Phân Bổ Điểm):**
   - Xuất hiện đề thi về Quản lý thiệt hại do bão lũ & Cứu trợ thiên tai (`EXAM-2024-2025-HK1-MID-01`).
   - Tỷ lệ điểm ERD được ghi nhận ở mức 2.0 điểm, phần ĐSQH và SQL nâng lên 8.0 điểm.
   - Nhấn mạnh tính chặt chẽ trong ký pháp toán học của ĐSQH và khả năng chuyển đổi sang T-SQL an toàn.

---

## 4. Khung Thiết Kế Ngân Hàng Đề (Question Bank Architecture)

Để đáp ứng mục tiêu người học tự ôn luyện từ cơ bản đến đạt 9–10 điểm, Ngân hàng đề GK được phân thành **4 luồng chuyên đề độc lập**:

### Chuyên đề 1: Mô Hình ERD & Ánh Xạ Lược Đồ Quan Hệ (Mục tiêu $\ge$ 30 bài)
- Xây dựng ERD từ các ngữ cảnh phong phú: Khách sạn, Bệnh viện, Thư viện số, Vận chuyển Logistics, Sàn TMĐT, Chung cư, Bão lũ cứu trợ, Đăng ký học phần, Trạm cứu hộ động vật, Quản lý gara ô tô...
- Yêu cầu bắt buộc: Bảng phân tích Thực thể / Thuộc tính / Khóa; xác định Mối kết hợp; Bản số Min-Max $(0,1), (1,1), (0,N), (1,N)$; chuyển đổi mô hình quan hệ chỉ rõ PK, FK và các bảng trung gian.

### Chuyên đề 2: ĐSQH Cơ Bản, Phép Tập Hợp & Các Loại Phép Kết (Mục tiêu $\ge$ 55 bài)
- Phép chọn $\sigma$, Phép chiếu $\pi$, Phép đổi tên quan hệ/thuộc tính $\rho$.
- Phép tự kết (Self-Join) cho quan hệ đệ quy (quản lý, nhân viên cấp trên).
- Phép kết bằng $\bowtie$, Phép kết tự nhiên.
- Phép tập hợp: Hội $\cup$, Giao $\cap$, Trừ $-$ (điều kiện tương thích tập hợp).
- Phép kết ngoài: Left Outer Join $\mathbin{⟕}$, Right Outer Join $\mathbin{⟖}$ cho câu hỏi chứa từ khóa *"nếu có"*.

### Chuyên đề 3: Phép Chia (Tất Cả / Mọi), Gom Nhóm $\gamma$ & Truy Vấn Phức Hợp (Mục tiêu $\ge$ 45 bài)
- Phép chia $\div$ hình thức qua 3 bước đại số quan hệ: Tạo tập tích Descarte $\to$ Trừ tập thực tế $\to$ Chiếu lấy phần bù.
- Câu hỏi điều kiện âm: "Chưa từng", "Không có", "Chỉ mua duy nhất".
- Phép gom nhóm $\gamma$ với các hàm `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, gom nhóm lồng.
- Câu hỏi tìm cực trị 9–10: MAX, MIN, lớn nhất, nhỏ nhất, nhiều nhất, ít nhất qua phép tự kết và phép trừ.

### Chuyên đề 4: Transact-SQL DDL/DML & Chuyển Đổi ĐSQH $\leftrightarrow$ SQL (Mục tiêu $\ge$ 20 bài)
- Cú pháp chuẩn SQL Server: `CREATE TABLE`, `ALTER TABLE ... ADD CONSTRAINT ... CHECK`, `ALTER TABLE ... DROP COLUMN`.
- `UPDATE` có điều kiện phức hợp, xử lý ngày tháng `YEAR()`, `MONTH()`, chuỗi Unicode `N'...'`.
- Viết tương đương giữa ĐSQH và SQL: Subquery, Correlated Subquery, Double `NOT EXISTS` cho phép chia, `GROUP BY ... HAVING`.

---

## 5. Khung 15 Đề Thi Mô Phỏng 75 Phút (Full Mock Exams Blueprint)

Mỗi đề thi mô phỏng 75 phút được thiết kế độc lập, bảo đảm:
- **Chuẩn 10.0 điểm / 75 phút**, không trùng lặp ngữ cảnh;
- Cân đối tỷ lệ theo 2 Profile: **Profile A (ERD 2.5đ + SQL 1.5đ + ĐSQH 6.0đ)** và **Profile B (ERD 2.0đ + SQL 1.5đ + ĐSQH 6.5đ)**;
- Đề bài và Đáp án được **tách riêng biệt hoàn toàn** để người học tự làm bài trước khi tra cứu;
- Mỗi câu hỏi đều có hướng dẫn tư duy tự nhiên $\to$ biểu thức logic $\to$ biểu thức ĐSQH / T-SQL $\to$ Barem chấm điểm chi tiết $\to$ Bẫy lỗi thường gặp $\to$ Dữ liệu phản ví dụ (edge cases).

---

## 6. Kế Hoạch Chuyển Tiếp Sang Gate P1 (Next Action)

Sau khi Gate R1 được nghiệm thu, hệ thống bước ngay vào **Gate P1 — Gold Standard Pilot**:
1. Xây dựng **Đề Thi Mô Phỏng Số 01 (Mock 01 - 10đ / 75p)** hoàn chỉnh kèm Lời giải chi tiết mẫu mực chuẩn mực học thuật cao nhất.
2. Xây dựng **15 bài tập mẫu pilot** đại diện cho đủ 4 chuyên đề (ERD, Outer Join, Phép chia, Gom nhóm, T-SQL).
3. Biên soạn và build thử nghiệm bản PDF A4 Pilot bằng công cụ kết xuất chất lượng cao, kiểm tra kiểu chữ Unicode, công thức toán học và sơ đồ vector.
4. Chạy kiểm thử tự động toàn bộ fixture và checkpoint trước khi mở rộng quy mô toàn bộ ở Gate P2.
