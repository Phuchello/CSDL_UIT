# DANH BỘ HIỆN VẬT ĐỀ THI GIỮA KỲ IT004 (GK EXAM REGISTRY)

**Dự án:** `Phuchello/CSDL_UIT` — Module Giữa Kỳ (GK) IT004  
**Bản cập nhật:** Tháng 10/2024 (Kiểm định độc lập snapshot 2026)  
**Mục tiêu kiểm định:**  
Phân định tuyệt đối giữa **Đề thi Giữa kỳ Lý thuyết chính thức** với các hiện vật khác trong kho lưu trữ 31 hiện vật (Đề cuối kỳ, Đề thi thực hành máy, Đề cương ôn tập, Lab corpus). Tránh tuyệt đối sai lầm coi toàn bộ 31 hiện vật là "31 đề giữa kỳ".

---

## 1. Bảng Tổng Hợp Kiểm Định 31 Hiện Vật Toàn Dự Án

| Nhóm hiện vật | Mã loại | Số lượng | Danh sách Canonical Artifact ID | Kết luận thẩm định cho Module GK |
| :--- | :---: | :---: | :--- | :--- |
| **Đề thi Giữa kỳ Lý thuyết (Authentic Midterm)** | `exam` (MID) | **10** | `EXAM-2024-2025-HK1-MID-01`<br>`EXAM-2023-2024-HK1-MID-D1`<br>`EXAM-2023-2024-HK1-MID-D2`<br>`EXAM-2022-2023-HK1-MID-D2`<br>`EXAM-2019-2020-HK1-MID-D1`<br>`EXAM-2019-2020-HK1-MID-D2`<br>`EXAM-2018-2019-HK1-MID-D1`<br>`EXAM-2018-2019-HK1-MID-D2`<br>`EXAM-2017-2018-HK1-MID-D1`<br>`EXAM-2017-2018-HK1-MID-D2` | **TRỌNG TÂM NGHIÊN CỨU & MÔ PHỎNG** (Căn cứ thực chứng xây dựng ngân hàng đề) |
| **Tài liệu Ôn tập & Barem Giữa kỳ (GK Review & Rubrics)** | `review` | **3** | `REV-2024-10-01-EXP`<br>`REV-2024-DSQH-MID`<br>`REV-2024-K18-SOL` | **TÀI LIỆU THAM CHIẾU QUY CHUẨN** (Barem chấm, phân bổ điểm và ký pháp ĐSQH) |
| **Đề thi Cuối kỳ Lý thuyết (Final Exams)** | `exam` (FINAL) | **7** | `EXAM-2024-2025-HK1-FINAL-01`<br>`EXAM-2023-2024-HK1-FINAL-01`<br>`EXAM-2022-2023-HK1-FINAL-01`<br>`EXAM-2021-2022-HK1-FINAL-01`<br>`EXAM-2020-2021-HK1-FINAL-01`<br>`EXAM-2019-2020-HK1-FINAL-01`<br>`EXAM-2018-2019-HK1-FINAL-01` | **LOẠI KHỎI PHẠM VI GK** (Chứa Phụ thuộc hàm, Chuẩn hóa BCNF/3NF, Bảng tầm ảnh hưởng toàn diện — chỉ học ở nửa sau môn học) |
| **Đề thi Thực hành Máy (Practical Exams)** | `practical-exam` | **10** | `PRAC-2024-2025-HK1-302`<br>`PRAC-2024-2025-HK1-01`<br>`PRAC-2024-2025-HK1-02`<br>`PRAC-2023-2024-HK1-O117`<br>`PRAC-2023-2024-HK1-D04`<br>`PRAC-2023-2024-HK1-FINAL-01`<br>`PRAC-2022-2023-HK1-D04`<br>`PRAC-2022-2023-HK1-D03`<br>`PRAC-2020-2021-HK1-M18`<br>`PRAC-2013-2014-HK1-E181` | **LOẠI KHỎI PHẠM VI GK LÝ THUYẾT** (Kiểm tra kỹ năng gõ code T-SQL, Trigger trên SQL Server phòng máy) |
| **Hệ thống Mã nguồn Thực hành (Lab Corpus)** | `lab-corpus` | **1** | `LAB-QLBH-QLGV-CORPUS` | **LOẠI KHỎI PHẠM VI GK LÝ THUYẾT** (Mã nguồn 4 buổi thực hành QLBH & QLGV) |
| **TỔNG CỘNG HIỆN VẬT KHẢO SÁT** | - | **31** | - | **Chính xác 10 đề GK thật + 3 tài liệu ôn tập GK** |

---

## 2. Chi Tiết 10 Đề Thi Giữa Kỳ Lý Thuyết Thực Chứng (Authentic Midterm Registry)

### 1. `EXAM-2024-2025-HK1-MID-01`
- **Năm học / Học kỳ:** 2024–2025 / HK1 (Mới nhất)
- **Thời gian & Thang điểm:** 75 phút / 10 điểm (Tự luận, không tài liệu)
- **Độ tin cậy:** `HIGH`
- **Lược đồ CSDL:**
  - *Câu 1 (2.0 điểm):* Vẽ ERD Quản lý thông tin thiệt hại bão lũ và Tiếp nhận tiền ủng hộ cứu trợ thiên tai. Ánh xạ sang Lược đồ quan hệ.
  - *Câu 2 (8.0 điểm):* Lược đồ cứu trợ (`TINH`, `HO_THIET_HAI`, `DOT_CUU_TRO`, `PHIEU_NHAN`, `NHA_HAO_TAM`). Viết câu lệnh SQL DDL/UPDATE và 6 câu ĐSQH.
- **Quan sát đổi mới:** Tỷ lệ điểm ERD chuyển từ 2.5đ thành 2.0đ; phần ĐSQH và SQL chiếm 8.0đ.

### 2. `EXAM-2023-2024-HK1-MID-D1`
- **Năm học / Học kỳ:** 2023–2024 / HK1 (Đề 1 - CQ + CLC)
- **Thời gian & Thang điểm:** 75 phút / 10 điểm
- **Độ tin cậy:** `HIGH` (Bản quét gốc `DE-THI-GIUA-KY_CSDL_HK1_2023_2024.pdf`, Tr. 1–2)
- **Lược đồ CSDL:**
  - *Câu 1 (2.5 điểm):* ERD Phòng cháy chữa cháy Chung cư (Tòa nhà, Tầng, Căn hộ, Thiết bị/Dụng cụ PCCC, Đợt kiểm tra). Chuyển sang mô hình quan hệ xác định PK/FK.
  - *Câu 2 (7.5 điểm):* CSDL Cửa hàng hoa (`NHAVUON`, `SANPHAM`, `DONHANG`, `CTDH`, `GIAOHANG`).
    - SQL DDL / UPDATE (1.5 điểm): Tạo CHECK constraint `DAGIAO IN (0, 1)`, UPDATE tăng phí ship 10%.
    - ĐSQH (6.0 điểm - 6 câu): Lọc hoa hồng Đà Lạt, kết nối đơn hàng, Outer Join khách nhận hàng "nếu có", gom nhóm doanh thu theo nhà vườn, phép chia đặt tất cả sản phẩm, tìm nhà vườn có số lượng sản phẩm cung cấp nhiều nhất.

### 3. `EXAM-2023-2024-HK1-MID-D2`
- **Năm học / Học kỳ:** 2023–2024 / HK1 (Đề 2 - CQ + CLC)
- **Thời gian & Thang điểm:** 75 phút / 10 điểm
- **Độ tin cậy:** `HIGH` (Bản quét gốc `DE-THI-GIUA-KY_CSDL_HK1_2023_2024.pdf`, Tr. 3–4)
- **Lược đồ CSDL:**
  - *Câu 1 (2.5 điểm):* ERD Kiểm tra thiết bị báo cháy chung cư. Chuyển đổi mô hình quan hệ.
  - *Câu 2 (7.5 điểm):* CSDL Cửa hàng hoa (biến thể câu hỏi đối xứng với Đề 1).

### 4. `EXAM-2022-2023-HK1-MID-D2`
- **Năm học / Học kỳ:** 2022–2023 / HK1 (Đề 2)
- **Thời gian & Thang điểm:** 75 phút / 10 điểm
- **Độ tin cậy:** `HIGH` (Bản chép đề sinh viên `23520266_Homework5_CSDL.docx` + Studocu)
- **Lược đồ CSDL:** Quản lý Căn hộ chung cư & Trả góp (`CANHO`, `LOAICH`, `TRAGOP`, `HINHTHUCTG`, `KHACHHANG`).
- **Nội dung kiểm tra:** SQL/ĐSQH: Giá bán BETWEEN, kỳ hạn > 120 tháng ORDER BY DESC, gom nhóm đếm căn hộ, khách hàng mua cả 'penthouse' và 'duplex' (INTERSECT), mua tất cả căn hộ 'duplex' cao cấp (Phép chia $\div$).

### 5. `EXAM-2019-2020-HK1-MID-D1`
- **Năm học / Học kỳ:** 2019–2020 / HK1 (Đề 1)
- **Thời gian & Thang điểm:** 75 phút / 10 điểm
- **Độ tin cậy:** `MEDIUM-HIGH`
- **Lược đồ CSDL:** Thế vận hội Olympic (`VANDONGVIEN`, `THEVANHOI`, `NOIDUNGTHI`, `THAMGIA`).
- **Nội dung kiểm tra:** VĐV quốc tịch 'UK', Bắn cung tại 'Olympic Tokyo 2020', đếm huy chương vàng Nhật Bản, tham gia cả '100m bơi ngửa' và '200m tự do', VĐV Nữ Anh tham gia tất cả kỳ thế vận hội từ 2008 (Phép chia $\div$), VĐV đạt từ 2 HCV trở lên tại Rio 2016.

### 6. `EXAM-2019-2020-HK1-MID-D2`
- **Năm học / Học kỳ:** 2019–2020 / HK1 (Đề 2)
- **Thời gian & Thang điểm:** 75 phút / 10 điểm
- **Độ tin cậy:** `MEDIUM-HIGH`
- **Lược đồ CSDL:** Thế vận hội Olympic (Nữ 'JA', Điền kinh Rio 2016, HCB Trung Quốc 2012, bơi ngửa nhưng không tự do (EXCEPT), Nam Đức tham gia tất cả thế vận hội từ 2012, đạt >= 2 HCV Bắn cung).

### 7. `EXAM-2018-2019-HK1-MID-D1`
- **Năm học / Học kỳ:** 2018–2019 / HK1 (Đề 1)
- **Thời gian & Thang điểm:** 75 phút / 10 điểm
- **Độ tin cậy:** `MEDIUM-HIGH`
- **Lược đồ CSDL:** Quản lý Nhà cung cấp & Đơn đặt hàng (`NHACUNGCAP`, `MATHANG`, `DONDATHANG`, `CTDDH`, `CUNGCAP`).
- **Nội dung kiểm tra:** Đơn hàng Vinamilk > 1tr, tổng số lượng 'MH001' năm 2018, NCC cung cấp hàng Việt Nam mà không cung cấp hàng Trung Quốc (EXCEPT), đơn hàng đặt tất cả mặt hàng Vissan (Phép chia $\div$), mặt hàng có SL đặt nhiều nhất năm 2018.

### 8. `EXAM-2018-2019-HK1-MID-D2`
- **Năm học / Học kỳ:** 2018–2019 / HK1 (Đề 2)
- **Thời gian & Thang điểm:** 75 phút / 10 điểm
- **Độ tin cậy:** `MEDIUM-HIGH`
- **Lược đồ CSDL:** Quản lý Nhà cung cấp & Đơn đặt hàng (Biến thể Đề 2: NCC cung cấp từ 01/01/2018, tổng tiền 'MH014', NCC cung cấp hàng Mỹ không cung cấp hàng Hàn Quốc, đơn hàng đặt tất cả mặt hàng Vinamilk, mặt hàng có SL đặt ít nhất năm 2018).

### 9. `EXAM-2017-2018-HK1-MID-D1`
- **Năm học / Học kỳ:** 2017–2018 / HK1 (Đề 1)
- **Thời gian & Thang điểm:** 75 phút / 10 điểm
- **Độ tin cậy:** `MEDIUM-HIGH`
- **Lược đồ CSDL:** Quản lý Tài khoản Ngân hàng (`KHACHHANG`, `TAIKHOAN`, `LOAITK`, `GIAODICH`, `LOAIGD`).
- **Nội dung kiểm tra:** Tài khoản mở ngày 01/01/2017 ORDER BY SoDu ASC, gom nhóm tính tổng tiền từng loại GD, mở cả TK Tiết kiệm và Thanh toán (INTERSECT), giao dịch có số tiền lớn nhất tháng 12/2017, KH mở tất cả các loại tài khoản (Phép chia $\div$), loại TK được mở nhiều nhất năm 2016.

### 10. `EXAM-2017-2018-HK1-MID-D2`
- **Năm học / Học kỳ:** 2017–2018 / HK1 (Đề 2)
- **Thời gian & Thang điểm:** 75 phút / 10 điểm
- **Độ tin cậy:** `MEDIUM-HIGH`
- **Lược đồ CSDL:** Quản lý Tài khoản Ngân hàng (Giao dịch ngày 01/01/2017 ORDER BY SoTien DESC, tổng số dư từng loại TK, mở cả TK Thanh toán và Vay, TK mở tháng 12/2017 có số dư lớn nhất, TK thực hiện tất cả các loại giao dịch, KH có số lượng TK 'chưa kích hoạt' nhiều nhất).

---

## 3. Danh Mục 3 Tài Liệu Ôn Tập & Barem Điểm Bổ Trợ (GK Review Materials)

1. **`REV-2024-10-01-EXP`**: Phiếu bài tập lớp ngày 01/10/2024. Phần 1: ERD Xăng dầu. Phần 2: Tuyến xe khách (DDL ALTER/UPDATE + ĐSQH).
2. **`REV-2024-DSQH-MID`**: Đề cương ôn thi Giữa kỳ ĐSQH 2024 SV. 2 chuyên đề lớn: Bán xe máy trả góp (12 câu) và Nhà hàng White Palace (12 câu).
3. **`REV-2024-K18-SOL`**: Barem chấm chính thức Khóa 18 (2024). Định mức điểm chi tiết từng phần cho hội đồng chấm thi.
