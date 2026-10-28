# CHUYÊN ĐỀ 2: ĐẠI SỐ QUAN HỆ CƠ BẢN, PHÉP TẬP HỢP & CÁC LOẠI PHÉP KẾT
**Môn học:** IT004 — Cơ sở dữ liệu | **Hệ thống:** UIT Exam Mastery
**Biên soạn:** VÕ TRỌNG PHÚC | **Số lượng bài tập độc lập:** 45 bài chuẩn hóa

---

## Bài 01 [RA-B01] — Lọc Đơn Lô Vắc-Xin Theo Hạn Sử Dụng & Đơn Giá
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `LOVACXIN(MALO, TENLO, TENVACXIN, NGAYSX, HSD, SOLIEU, DONGIA, MANCC)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã lô, tên lô và số liều của các lô vắc-xin có hạn sử dụng (HSD) trước ngày '2025-01-01' và đơn giá lớn hơn 200.000 VNĐ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MALO, TENLO, SOLIEU}(σ_{HSD < '2025-01-01' ∧ DONGIA > 200000}(LOVACXIN))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MALO, TENLO, SOLIEU
FROM LOVACXIN
WHERE HSD < '2025-01-01' AND DONGIA > 200000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Áp dụng phép chọn σ với điều kiện kết hợp AND: HSD < '2025-01-01' ∧ DONGIA > 200000.
1. Bước 2: Áp dụng phép chiếu π để trích xuất 3 thuộc tính cần thiết: MALO, TENLO, SOLIEU.

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra định dạng ngày chuỗi YYYY-MM-DD và giá trị DONGIA dạng số.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 02 [RA-B02] — Lọc Danh Sách Sinh Viên Thuộc Lớp & Điểm Xét Tuyển
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SINHVIEN(MSSV, HOTEN, NGAYSINH, PHAI, MALOP, DIEMXT)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã số sinh viên, họ tên và ngày sinh của các sinh viên nữ (PHAI = 'Nu') thuộc lớp 'HTTT2023' có điểm xét tuyển từ 26.0 trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MSSV, HOTEN, NGAYSINH}(σ_{PHAI = 'Nu' ∧ MALOP = 'HTTT2023' ∧ DIEMXT ≥ 26.0}(SINHVIEN))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MSSV, HOTEN, NGAYSINH
FROM SINHVIEN
WHERE PHAI = N'Nu' AND MALOP = 'HTTT2023' AND DIEMXT >= 26.0;
```

**Các bước suy luận tư duy:**
1. Bước 1: Chọn các bộ thỏa mãn đồng thời 3 vị từ: PHAI = 'Nu', MALOP = 'HTTT2023', DIEMXT ≥ 26.0.
1. Bước 2: Chiếu các thuộc tính MSSV, HOTEN, NGAYSINH.

**Phân tích trường hợp biên (Edge Cases):**
Cần phân biệt chữ hoa/thường trong chuỗi mã lớp và giá trị chuỗi tiếng Việt Unicode.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 03 [RA-B03] — Lọc Sản Phẩm Điện Tử Xuất Xứ Nhật Bản Hoặc Hàn Quốc
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SANPHAM(MASP, TENSP, DVT, NUOCSX, DONGIA)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã sản phẩm, tên sản phẩm và đơn giá của các sản phẩm có xuất xứ từ 'Nhat Ban' hoặc 'Han Quoc' có đơn giá dưới 5.000.000 VNĐ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MASP, TENSP, DONGIA}(σ_{(NUOCSX = 'Nhat Ban' ∨ NUOCSX = 'Han Quoc') ∧ DONGIA < 5000000}(SANPHAM))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MASP, TENSP, DONGIA
FROM SANPHAM
WHERE NUOCSX IN (N'Nhat Ban', N'Han Quoc') AND DONGIA < 5000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Đặt ngoặc vị từ tuyển (OR) để đảm bảo độ ưu tiên toán tử logic với phép hội (AND).
1. Bước 2: Chiếu các cột kết quả MASP, TENSP, DONGIA.

**Phân tích trường hợp biên (Edge Cases):**
Chú ý thứ tự ưu tiên của toán tử AND cao hơn OR trong biểu thức logic.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 04 [RA-B04] — Lọc Tài Khoản Ngân Hàng Số Dư Lớn Mở Năm 2024
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TAIKHOAN(SOTK, MAKH, MACN, SODU, NGAYMO, TRANGTHAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm số tài khoản và số dư của các tài khoản đang hoạt động (TRANGTHAI = 'Hoat dong') mở từ ngày '2024-01-01' có số dư từ 100.000.000 VNĐ trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{SOTK, SODU}(σ_{TRANGTHAI = 'Hoat dong' ∧ NGAYMO ≥ '2024-01-01' ∧ SODU ≥ 100000000}(TAIKHOAN))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT SOTK, SODU
FROM TAIKHOAN
WHERE TRANGTHAI = N'Hoat dong' AND NGAYMO >= '2024-01-01' AND SODU >= 100000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc dữ liệu theo 3 điều kiện trạng thái, mốc thời gian và số dư tối thiểu.
1. Bước 2: Chiếu 2 thuộc tính SOTK và SODU.

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra trường hợp SODU âm hoặc NULL nếu tài khoản bị khóa.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 05 [RA-B05] — Lọc Chuyến Bay Khởi Hành Từ Sân Bay Tân Sơn Nhất
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CHUYENBAY(MACB, SB_DI, SB_DEN, NGAYBAY, GIOBAY, GIAGOC, TRANGTHAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã chuyến bay, sân bay đến, ngày bay và giờ bay của các chuyến bay xuất phát từ 'SGN' hạ cánh tại 'HAN' hoặc 'DAD' trong tháng 12/2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MACB, SB_DEN, NGAYBAY, GIOBAY}(σ_{SB_DI = 'SGN' ∧ (SB_DEN = 'HAN' ∨ SB_DEN = 'DAD') ∧ NGAYBAY ≥ '2024-12-01' ∧ NGAYBAY ≤ '2024-12-31'}(CHUYENBAY))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MACB, SB_DEN, NGAYBAY, GIOBAY
FROM CHUYENBAY
WHERE SB_DI = 'SGN' AND SB_DEN IN ('HAN', 'DAD')
  AND NGAYBAY BETWEEN '2024-12-01' AND '2024-12-31';
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết hợp các vị từ lọc sân bay đi, sân bay đến và khoảng thời gian bằng phép AND/OR.
1. Bước 2: Chiếu 4 thuộc tính theo yêu cầu đề bài.

**Phân tích trường hợp biên (Edge Cases):**
Sử dụng BETWEEN tương đương với hai bất đẳng thức >= và <=.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 06 [RA-B06] — Lọc Hóa Đơn Giá Trị Cao Thanh Toán Bằng Thẻ Tín Dụng
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOADON(SOHD, MAKH, MANV, NGAYHD, TRIGIA, HINHTHUC_TT)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm số hóa đơn, ngày lập và trị giá của các hóa đơn có trị giá trên 20.000.000 VNĐ được thanh toán bằng 'The tin dung' lập trong quý 3 năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{SOHD, NGAYHD, TRIGIA}(σ_{TRIGIA > 20000000 ∧ HINHTHUC_TT = 'The tin dung' ∧ NGAYHD ≥ '2024-07-01' ∧ NGAYHD ≤ '2024-09-30'}(HOADON))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT SOHD, NGAYHD, TRIGIA
FROM HOADON
WHERE TRIGIA > 20000000 AND HINHTHUC_TT = N'The tin dung'
  AND NGAYHD >= '2024-07-01' AND NGAYHD <= '2024-09-30';
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định khoảng thời gian Quý 3 (từ 01/07/2024 đến 30/09/2024).
1. Bước 2: Lọc các hóa đơn thỏa mãn trị giá và hình thức thanh toán.
1. Bước 3: Chiếu các cột kết quả.

**Phân tích trường hợp biên (Edge Cases):**
Cần chú ý định nghĩa quý trong năm và chính xác ngày cuối tháng 9 (30 ngày).

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 07 [RA-B07] — Lọc Khách Hàng VIP Tại Khu Vực TP.HCM
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG(MAKH, HOTEN, DIACHI, THANHPHO, LOAIKH, DIEM_TICHLUY)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã khách hàng, họ tên và địa chỉ của các khách hàng xếp loại 'VIP' hoặc 'Kim Cuong' có địa chỉ tại thành phố 'TP.HCM' và có điểm tích lũy trên 1000.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAKH, HOTEN, DIACHI}(σ_{(LOAIKH = 'VIP' ∨ LOAIKH = 'Kim Cuong') ∧ THANHPHO = 'TP.HCM' ∧ DIEM_TICHLUY > 1000}(KHACHHANG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MAKH, HOTEN, DIACHI
FROM KHACHHANG
WHERE LOAIKH IN ('VIP', 'Kim Cuong') AND THANHPHO = N'TP.HCM' AND DIEM_TICHLUY > 1000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Chọn khách hàng thỏa mãn vị từ hạng thẻ, thành phố và điểm tích lũy.
1. Bước 2: Chiếu các thuộc tính cần hiển thị.

**Phân tích trường hợp biên (Edge Cases):**
Phép tuyển giữa 2 loại khách hàng phải đặt trong cặp ngoặc đơn.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 08 [RA-B08] — Lọc Phòng Học Dung Tích Lớn Có Trang Bị Máy Chiếu
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHONGHOC(MAPHONG, TOANHA, SUCCHUA, CO_MAYCHIEU, CO_MAYLANH)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã phòng và tòa nhà của các phòng học có sức chứa từ 80 chỗ trở lên, có máy chiếu (CO_MAYCHIEU = 1) và có máy lạnh (CO_MAYLANH = 1).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAPHONG, TOANHA}(σ_{SUCCHUA ≥ 80 ∧ CO_MAYCHIEU = 1 ∧ CO_MAYLANH = 1}(PHONGHOC))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MAPHONG, TOANHA
FROM PHONGHOC
WHERE SUCCHUA >= 80 AND CO_MAYCHIEU = 1 AND CO_MAYLANH = 1;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc dữ liệu phòng học thỏa mãn cả 3 tiêu chí kỹ thuật.
1. Bước 2: Chiếu MAPHONG, TOANHA.

**Phân tích trường hợp biên (Edge Cases):**
Thuộc tính cờ bit/boolean so sánh với 1 hoặc TRUE.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 09 [RA-B09] — Lọc Thuốc Kê Đơn Có Giá Bán Dưới 50.000 VNĐ
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THUOC(MATHUOC, TENTHUOC, HOATCHAT, DVT, DONGIA, LOAITHUOC)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã thuốc, tên thuốc, hoạt chất và đơn vị tính của các loại thuốc thuộc nhóm 'Ke don' có đơn vị tính là 'Vien' hoặc 'Vi' và đơn giá dưới 50.000 VNĐ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MATHUOC, TENTHUOC, HOATCHAT, DVT}(σ_{LOAITHUOC = 'Ke don' ∧ (DVT = 'Vien' ∨ DVT = 'Vi') ∧ DONGIA < 50000}(THUOC))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MATHUOC, TENTHUOC, HOATCHAT, DVT
FROM THUOC
WHERE LOAITHUOC = N'Ke don' AND DVT IN (N'Vien', N'Vi') AND DONGIA < 50000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc thuốc theo loại, đơn vị tính và giới hạn đơn giá.
1. Bước 2: Chiếu 4 thuộc tính yêu cầu.

**Phân tích trường hợp biên (Edge Cases):**
Phân biệt kiểu chuỗi tiếng Việt Unicode có dấu với ký tự N'...' trong SQL.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 10 [RA-B10] — Lọc Bác Sĩ Chuyên Khoa Có Học Vị Tiến Sĩ
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BACSI(MABS, HOTEN, CHUYENKHOA, HOCVI, NAM_KINHNGHIEM)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã bác sĩ, họ tên và số năm kinh nghiệm của các bác sĩ chuyên khoa 'Tim mach' hoặc 'Noi khoa' có học vị là 'Tien si' và kinh nghiệm trên 10 năm.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MABS, HOTEN, NAM_KINHNGHIEM}(σ_{(CHUYENKHOA = 'Tim mach' ∨ CHUYENKHOA = 'Noi khoa') ∧ HOCVI = 'Tien si' ∧ NAM_KINHNGHIEM > 10}(BACSI))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MABS, HOTEN, NAM_KINHNGHIEM
FROM BACSI
WHERE CHUYENKHOA IN (N'Tim mach', N'Noi khoa') AND HOCVI = N'Tien si' AND NAM_KINHNGHIEM > 10;
```

**Các bước suy luận tư duy:**
1. Bước 1: Áp dụng vị từ chọn chuyên khoa, học vị và năm kinh nghiệm.
1. Bước 2: Chiếu MABS, HOTEN, NAM_KINHNGHIEM.

**Phân tích trường hợp biên (Edge Cases):**
Cần phân biệt giữa học hàm (Giao su, Pho giao su) và học vị (Thac si, Tien si).

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 11 [RA-B11] — Kết Nối Bảng Đơn Hàng Và Khách Hàng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONHANG(MADON, MAKH, NGAYDAT, TONGTIEN), KHACHHANG(MAKH, TENKH, DIACHI, SDT)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã đơn hàng, ngày đặt, tên khách hàng và số điện thoại của các đơn hàng có tổng tiền từ 15.000.000 VNĐ trở lên được đặt trong tháng 11/2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MADON, NGAYDAT, TENKH, SDT}(σ_{TONGTIEN ≥ 15000000 ∧ NGAYDAT ≥ '2024-11-01' ∧ NGAYDAT ≤ '2024-11-30'}(DONHANG ⋈ KHACHHANG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT DH.MADON, DH.NGAYDAT, KH.TENKH, KH.SDT
FROM DONHANG DH
INNER JOIN KHACHHANG KH ON DH.MAKH = KH.MAKH
WHERE DH.TONGTIEN >= 15000000 AND DH.NGAYDAT BETWEEN '2024-11-01' AND '2024-11-30';
```

**Các bước suy luận tư duy:**
1. Bước 1: Thực hiện phép kết tự nhiên giữa DONHANG và KHACHHANG trên thuộc tính chung MAKH.
1. Bước 2: Lọc các bộ có tổng tiền thỏa mãn và ngày đặt trong tháng 11/2024.
1. Bước 3: Chiếu các thuộc tính MADON, NGAYDAT, TENKH, SDT.

**Phân tích trường hợp biên (Edge Cases):**
Có thể tối ưu hóa ĐSQH bằng cách lọc DONHANG trước khi kết nối.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 12 [RA-B12] — Kết Nối Đa Bảng Sinh Viên Đăng Ký Khóa Học Ngoại Ngữ
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOCVIEN(MAHV, HOTEN, SDT), DANGKY(MAHV, MALOP, NGAYDK), LOPHOC(MALOP, MAKH, PHONG), KHOAHOC(MAKH, TENKH, HOCPHI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết họ tên học viên và tên khóa học của các học viên đã nộp học phí tham gia các khóa học có học phí trên 5.000.000 VNĐ mở trong năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{HOTEN, TENKH}(σ_{HOCPHI > 5000000 ∧ NGAYDK ≥ '2024-01-01' ∧ NGAYDK ≤ '2024-12-31'}(HOCVIEN ⋈ DANGKY ⋈ LOPHOC ⋈ KHOAHOC))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT HV.HOTEN, KH.TENKH
FROM HOCVIEN HV
INNER JOIN DANGKY DK ON HV.MAHV = DK.MAHV
INNER JOIN LOPHOC LH ON DK.MALOP = LH.MALOP
INNER JOIN KHOAHOC KH ON LH.MAKH = KH.MAKH
WHERE KH.HOCPHI > 5000000 AND DK.NGAYDK BETWEEN '2024-01-01' AND '2024-12-31';
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối lần lượt 4 quan hệ theo các cặp khóa ngoại MAHV, MALOP, MAKH.
1. Bước 2: Chọn các bộ thỏa mãn điều kiện học phí và mốc thời gian đăng ký năm 2024.
1. Bước 3: Chiếu các thuộc tính HOTEN, TENSP (loại bỏ trùng lặp nếu cần).

**Phân tích trường hợp biên (Edge Cases):**
Khi kết 4 bảng, thứ tự kết nối cần tối ưu hóa bằng cách đẩy phép chọn xuống trước.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 13 [RA-B13] — Kết Nối Giảng Viên Và Lớp Học Phần Phụ Trách
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `GIANGVIEN(MAGV, HOTEN, MAKHOA), KHOA(MAKHOA, TENKHOA), LOPHOCPHAN(MALHP, MAGV, MAMH, HOCKY, NAMHOC)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã giảng viên, họ tên và mã lớp học phần do các giảng viên thuộc khoa 'He thong thong tin' phụ trách trong 'Hoc ky 1' năm học '2024-2025'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{GIANGVIEN.MAGV, HOTEN, MALHP}(σ_{TENKHOA = 'He thong thong tin' ∧ HOCKY = 1 ∧ NAMHOC = '2024-2025'}(GIANGVIEN ⋈ KHOA ⋈ LOPHOCPHAN))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT GV.MAGV, GV.HOTEN, LHP.MALHP
FROM GIANGVIEN GV
INNER JOIN KHOA K ON GV.MAKHOA = K.MAKHOA
INNER JOIN LOPHOCPHAN LHP ON GV.MAGV = LHP.MAGV
WHERE K.TENKHOA = N'He thong thong tin' AND LHP.HOCKY = 1 AND LHP.NAMHOC = '2024-2025';
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối GIANGVIEN với KHOA và LOPHOCPHAN theo MAGV và MAKHOA.
1. Bước 2: Lọc các bộ theo tên khoa, học kỳ và năm học.
1. Bước 3: Chiếu MAGV, HOTEN, MALHP.

**Phân tích trường hợp biên (Edge Cases):**
Cần bảo đảm khóa ngoại kết nối chính xác giữa 3 quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 14 [RA-B14] — Kết Nối Bệnh Nhân, Bác Sĩ Và Phiếu Khám Bệnh
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BENHNHAN(MABN, TENBN, DIACHI), BACSI(MABS, TENBS, CHUYENKHOA), PHIEUKHAM(MAPK, MABN, MABS, NGAYKHAM, CHANDOAN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm tên bệnh nhân, tên bác sĩ khám và chẩn đoán của các ca khám bệnh trong ngày '2024-11-15' do các bác sĩ khoa 'Tai mui hong' thực hiện.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{TENBN, TENBS, CHANDOAN}(σ_{NGAYKHAM = '2024-11-15' ∧ CHUYENKHOA = 'Tai mui hong'}(BENHNHAN ⋈ PHIEUKHAM ⋈ BACSI))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT BN.TENBN, BS.TENBS, PK.CHANDOAN
FROM PHIEUKHAM PK
INNER JOIN BENHNHAN BN ON PK.MABN = BN.MABN
INNER JOIN BACSI BS ON PK.MABS = BS.MABS
WHERE PK.NGAYKHAM = '2024-11-15' AND BS.CHUYENKHOA = N'Tai mui hong';
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối trung tâm PHIEUKHAM với BENHNHAN (qua MABN) và BACSI (qua MABS).
1. Bước 2: Lọc ngày khám và chuyên khoa bác sĩ.
1. Bước 3: Chiếu các trường tên bệnh nhân, tên bác sĩ, chẩn đoán.

**Phân tích trường hợp biên (Edge Cases):**
Phân biệt rõ hai thuộc tính tên có thể bị trùng tên cột.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 15 [RA-B15] — Kết Nối Đơn Hàng Và Phương Thức Vận Chuyển
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONHANG(MADON, MAKH, NGAYDAT, TONGTIEN), KHACHHANG(MAKH, HOTEN, QUAN), VANCHUYEN(MAVC, MADON, DONVI_VC, PHIVC, TRANGTHAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã đơn hàng, họ tên khách hàng và đơn vị vận chuyển của các đơn hàng giao đến quận 'Thu Duc' do đơn vị 'GiaoHangNhanh' đảm nhận có trạng thái 'Da giao'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{DONHANG.MADON, HOTEN, DONVI_VC}(σ_{QUAN = 'Thu Duc' ∧ DONVI_VC = 'GiaoHangNhanh' ∧ TRANGTHAI = 'Da giao'}(DONHANG ⋈ KHACHHANG ⋈ VANCHUYEN))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT DH.MADON, KH.HOTEN, VC.DONVI_VC
FROM DONHANG DH
INNER JOIN KHACHHANG KH ON DH.MAKH = KH.MAKH
INNER JOIN VANCHUYEN VC ON DH.MADON = VC.MADON
WHERE KH.QUAN = N'Thu Duc' AND VC.DONVI_VC = 'GiaoHangNhanh' AND VC.TRANGTHAI = N'Da giao';
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối 3 bảng qua MAKH và MADON.
1. Bước 2: Áp dụng các điều kiện lọc về quận, đơn vị giao hàng và trạng thái.
1. Bước 3: Chiếu các thuộc tính kết quả.

**Phân tích trường hợp biên (Edge Cases):**
Tránh nhập nhằng tên cột MADON giữa hai quan hệ DONHANG và VANCHUYEN.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 16 [RA-B16] — Kết Nối Bạn Đọc Mượn Sách Chuyên Ngành CNTT Năm 2023
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DOCGIA(MADG, HOTEN, KHOA), PHIEUMUON(MAPM, MADG, NGAYMUON), CTPM(MAPM, MACS), CUONSACH(MACS, MADS), DAUSACH(MADS, TENSACH, CHUYENNGANH, NAMSX)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã bạn đọc, họ tên và tên sách của các bạn đọc thuộc khoa 'Cong nghe Thong tin' đã mượn các cuốn sách thuộc chuyên ngành 'Tri tue Nhan tao' xuất bản năm 2023.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{DOCGIA.MADG, HOTEN, TENSACH}(σ_{KHOA = 'Cong nghe Thong tin' ∧ CHUYENNGANH = 'Tri tue Nhan tao' ∧ NAMSX = 2023}(DOCGIA ⋈ PHIEUMUON ⋈ CTPM ⋈ CUONSACH ⋈ DAUSACH))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT DG.MADG, DG.HOTEN, DS.TENSACH
FROM DOCGIA DG
INNER JOIN PHIEUMUON PM ON DG.MADG = PM.MADG
INNER JOIN CTPM ON PM.MAPM = CTPM.MAPM
INNER JOIN CUONSACH CS ON CTPM.MACS = CS.MACS
INNER JOIN DAUSACH DS ON CS.MADS = DS.MADS
WHERE DG.KHOA = N'Cong nghe Thong tin' AND DS.CHUYENNGANH = N'Tri tue Nhan tao' AND DS.NAMSX = 2023;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối dây chuyền 5 quan hệ qua các cặp khóa: MADG, MAPM, MACS, MADS.
1. Bước 2: Lọc theo khoa độc giả, chuyên ngành sách và năm xuất bản.
1. Bước 3: Chiếu các thuộc tính kết quả: MADG, HOTEN, TENSACH.

**Phân tích trường hợp biên (Edge Cases):**
Cần chỉ định rõ tiền tố DOCGIA.MADG do thuộc tính MADG có mặt ở cả hai bảng DOCGIA và PHIEUMUON.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 17 [RA-B17] — Kết Nối Suất Chiếu Phim Định Dạng IMAX Sau 18 Giờ
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIM(MAPHIM, TENPHIM, THELOAI), SUATCHIEU(MASC, MAPHIM, MAPHONG, NGAYCHIEU, GIOCHIEU), PHONGCHIEU(MAPHONG, TENPHONG, LOAIMANHINH)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã suất chiếu, tên phim và tên phòng chiếu của các suất chiếu phim thể loại 'Hanh dong' chiếu trên màn hình 'IMAX' sau '18:00:00' trong ngày '2024-10-20'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MASC, TENPHIM, TENPHONG}(σ_{THELOAI = 'Hanh dong' ∧ LOAIMANHINH = 'IMAX' ∧ GIOCHIEU > '18:00:00' ∧ NGAYCHIEU = '2024-10-20'}(PHIM ⋈ SUATCHIEU ⋈ PHONGCHIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT SC.MASC, P.TENPHIM, PC.TENPHONG
FROM SUATCHIEU SC
INNER JOIN PHIM P ON SC.MAPHIM = P.MAPHIM
INNER JOIN PHONGCHIEU PC ON SC.MAPHONG = PC.MAPHONG
WHERE P.THELOAI = N'Hanh dong' AND PC.LOAIMANHINH = 'IMAX'
  AND SC.GIOCHIEU > '18:00:00' AND SC.NGAYCHIEU = '2024-10-20';
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối SUATCHIEU với PHIM (qua MAPHIM) và PHONGCHIEU (qua MAPHONG).
1. Bước 2: Lọc các bộ thỏa mãn đồng thời thể loại, loại màn hình, giờ chiếu và ngày chiếu.
1. Bước 3: Chiếu MASC, TENPHIM, TENPHONG.

**Phân tích trường hợp biên (Edge Cases):**
Định dạng giờ so sánh chuỗi theo chuẩn ISO HH:MM:SS; kiểm tra ngày chiếu chính xác.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 18 [RA-B18] — Kết Nối Lô Hàng Nhập Khẩu Sữa Úc Đơn Giá Cao
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHACUNGCAP(MANCC, TENNCC, QUOCGIA), PHIEUNHAP(MAPN, MANCC, NGAYNHAP), CTPN(MAPN, MASP, SOLUONG, DONGIANHAP), SANPHAM(MASP, TENSP, LOAISP)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm tên nhà cung cấp, tên sản phẩm và đơn giá nhập của các sản phẩm thuộc loại 'Sua tuoi' do nhà cung cấp có xuất xứ từ 'Australia' cung ứng có đơn giá nhập trên 150.000 VNĐ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{TENNCC, TENSP, DONGIANHAP}(σ_{QUOCGIA = 'Australia' ∧ LOAISP = 'Sua tuoi' ∧ DONGIANHAP > 150000}(NHACUNGCAP ⋈ PHIEUNHAP ⋈ CTPN ⋈ SANPHAM))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT NCC.TENNCC, SP.TENSP, CT.DONGIANHAP
FROM NHACUNGCAP NCC
INNER JOIN PHIEUNHAP PN ON NCC.MANCC = PN.MANCC
INNER JOIN CTPN CT ON PN.MAPN = CT.MAPN
INNER JOIN SANPHAM SP ON CT.MASP = SP.MASP
WHERE NCC.QUOCGIA = 'Australia' AND SP.LOAISP = N'Sua tuoi' AND CT.DONGIANHAP > 150000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối liên hoàn 4 bảng qua MANCC, MAPN và MASP.
1. Bước 2: Lọc các bộ theo quốc gia nhà cung cấp, loại sản phẩm và ngưỡng đơn giá nhập.
1. Bước 3: Chiếu các thuộc tính cần thiết.

**Phân tích trường hợp biên (Edge Cases):**
Cần phân biệt giữa đơn giá nhập (DONGIANHAP) trong chi tiết phiếu và đơn giá bán trong danh mục sản phẩm.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 19 [RA-B19] — Kết Nối Lịch Hẹn Nha Khoa Bác Sĩ Chuyên Khoa I
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BENHNHAN(MABN, HOTEN, SDT), NHASI(MANS, TENNS, TRINHDOHOCVAN), LICHHEN(MALH, MABN, MANS, NGAYHEN, DICHVU, TRANGTHAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết họ tên bệnh nhân, tên nha sĩ và ngày hẹn của các cuộc hẹn dịch vụ 'Tay trang rang' do các nha sĩ có trình độ 'Chuyen khoa I' tiếp nhận và có trạng thái 'Da xac nhan'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{BENHNHAN.HOTEN, TENNS, NGAYHEN}(σ_{DICHVU = 'Tay trang rang' ∧ TRINHDOHOCVAN = 'Chuyen khoa I' ∧ TRANGTHAI = 'Da xac nhan'}(BENHNHAN ⋈ LICHHEN ⋈ NHASI))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT BN.HOTEN, NS.TENNS, LH.NGAYHEN
FROM LICHHEN LH
INNER JOIN BENHNHAN BN ON LH.MABN = BN.MABN
INNER JOIN NHASI NS ON LH.MANS = NS.MANS
WHERE LH.DICHVU = N'Tay trang rang' AND NS.TRINHDOHOCVAN = N'Chuyen khoa I' AND LH.TRANGTHAI = N'Da xac nhan';
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối LICHHEN với BENHNHAN và NHASI qua khóa ngoại MABN và MANS.
1. Bước 2: Lọc các cuộc hẹn thỏa mãn dịch vụ, trình độ nha sĩ và trạng thái đã xác nhận.
1. Bước 3: Chiếu BENHNHAN.HOTEN, TENNS, NGAYHEN.

**Phân tích trường hợp biên (Edge Cases):**
Tránh xung đột tên thuộc tính HOTEN giữa bảng BENHNHAN và NHASI.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 20 [RA-B20] — Kết Nối Chuyến Xe Giường Nằm Đi Đà Lạt Ban Đêm
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TUYENXE(MATUYEN, TENTUYEN, BEN_DI, BEN_DEN), XE(MAXE, BIENSO, LOAIXE), CHUYENXE(MACHUYEN, MATUYEN, MAXE, MATX, GIOXUATBEN), TAIXE(MATX, TENTX, HANG_BANG)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã chuyến xe, biển số xe và tên tài xế của các chuyến xe chạy tuyến có bến đến là 'Da Lat' bằng loại xe 'Giuong nam' xuất bến sau '22:00:00' do tài xế có bằng hạng 'E' lái.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MACHUYEN, BIENSO, TENTX}(σ_{BEN_DEN = 'Da Lat' ∧ LOAIXE = 'Giuong nam' ∧ GIOXUATBEN > '22:00:00' ∧ HANG_BANG = 'E'}(TUYENXE ⋈ CHUYENXE ⋈ XE ⋈ TAIXE))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT CX.MACHUYEN, X.BIENSO, TX.TENTX
FROM CHUYENXE CX
INNER JOIN TUYENXE TXE ON CX.MATUYEN = TXE.MATUYEN
INNER JOIN XE X ON CX.MAXE = X.MAXE
INNER JOIN TAIXE TX ON CX.MATX = TX.MATX
WHERE TXE.BEN_DEN = N'Da Lat' AND X.LOAIXE = N'Giuong nam'
  AND CX.GIOXUATBEN > '22:00:00' AND TX.HANG_BANG = 'E';
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối trung tâm CHUYENXE với TUYENXE, XE và TAIXE theo các khóa ngoại.
1. Bước 2: Lọc các chuyến xe thỏa mãn 4 vị từ: bến đến, loại xe, giờ xuất bến và hạng bằng lái.
1. Bước 3: Chiếu MACHUYEN, BIENSO, TENTX.

**Phân tích trường hợp biên (Edge Cases):**
Cần phân biệt bí danh giữa bảng TUYENXE và TAIXE khi viết truy vấn.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 21 [RA-B21] — Kết Nối Hợp Đồng Thuê Căn Hộ Cao Cấp Landmark
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TOANHA(MATN, TENTN, DIACHI), CANHO(MACAN, MATN, SOHIEUCAN, SOPHONGNGU, GIATHUE_THANG), HOPDONG(MAHD, MACAN, MAKH, NGAYKY, TIENCOC), KHACHHANG(MAKH, TENKH, SDT)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm tên khách hàng, số hiệu căn hộ và giá thuê của các hợp đồng thuê căn hộ có từ 3 phòng ngủ trở lên tại tòa nhà 'Landmark Plus' có giá thuê trên 25.000.000 VNĐ/tháng.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{TENKH, SOHIEUCAN, GIATHUE_THANG}(σ_{TENTN = 'Landmark Plus' ∧ SOPHONGNGU ≥ 3 ∧ GIATHUE_THANG > 25000000}(TOANHA ⋈ CANHO ⋈ HOPDONG ⋈ KHACHHANG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT KH.TENKH, CH.SOHIEUCAN, CH.GIATHUE_THANG
FROM HOPDONG HD
INNER JOIN CANHO CH ON HD.MACAN = CH.MACAN
INNER JOIN TOANHA TH ON CH.MATN = TH.MATN
INNER JOIN KHACHHANG KH ON HD.MAKH = KH.MAKH
WHERE TH.TENTN = 'Landmark Plus' AND CH.SOPHONGNGU >= 3 AND CH.GIATHUE_THANG > 25000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối liên hoàn 4 bảng qua MATN, MACAN và MAKH.
1. Bước 2: Lọc các bộ theo tên tòa nhà, số phòng ngủ tối thiểu và mức giá thuê tháng.
1. Bước 3: Chiếu TENKH, SOHIEUCAN, GIATHUE_THANG.

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra trường hợp hợp đồng đã hết hạn nếu bảng có thêm thuộc tính ngày kết thúc.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 22 [RA-B22] — Kết Nối Hóa Đơn Nhà Hàng Ẩm Thực Gọi Món Hải Sản Tại Bàn VIP
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANAN(MABAN, TENBAN, LOAIBAN), HOADON(MAHD, MABAN, NGAYLAP, TONGTIEN), CTHD(MAHD, MAMON, SOLUONG), MONAN(MAMON, TENMON, LOAIMON, DONGIA)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã hóa đơn, tên món ăn và đơn giá của các món ăn thuộc nhóm 'Hai san' được phục vụ tại các bàn thuộc loại 'VIP' có đơn giá trên 300.000 VNĐ trong ngày '2024-11-20'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{HOADON.MAHD, TENMON, DONGIA}(σ_{LOAIBAN = 'VIP' ∧ LOAIMON = 'Hai san' ∧ DONGIA > 300000 ∧ NGAYLAP = '2024-11-20'}(BANAN ⋈ HOADON ⋈ CTHD ⋈ MONAN))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT HD.MAHD, MA.TENMON, MA.DONGIA
FROM HOADON HD
INNER JOIN BANAN BA ON HD.MABAN = BA.MABAN
INNER JOIN CTHD CT ON HD.MAHD = CT.MAHD
INNER JOIN MONAN MA ON CT.MAMON = MA.MAMON
WHERE BA.LOAIBAN = 'VIP' AND MA.LOAIMON = N'Hai san'
  AND MA.DONGIA > 300000 AND HD.NGAYLAP = '2024-11-20';
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối BANAN, HOADON, CTHD và MONAN theo các khóa ngoại MABAN, MAHD, MAMON.
1. Bước 2: Lọc theo loại bàn VIP, loại món hải sản, đơn giá và ngày lập hóa đơn.
1. Bước 3: Chiếu các thuộc tính HOADON.MAHD, TENMON, DONGIA.

**Phân tích trường hợp biên (Edge Cases):**
Cần phân biệt mã hóa đơn HOADON.MAHD để tránh nhập nhằng giữa HOADON và CTHD.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 23 [RA-B23] — Kết Nối Khách Hàng Thay Pin Laptop Chính Hãng Dell
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG(MAKH, TENKH, SDT), THIETBI(MATB, MAKH, HIEUMAY, SERI), PHIEUBH(MAPBH, MATB, NGAYTIEPNHAN, TRANGTHAI), CT_BAOHANH(MAPBH, MALK, SOLUONG), LINHKIEN(MALK, TENLK, LOAILK, HANGSX)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm tên khách hàng, số điện thoại và số sê-ri máy của các khách hàng mang thiết bị hiệu 'Dell' đi thay linh kiện loại 'Pin' chính hãng do 'Dell' sản xuất trong quý 4 năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{TENKH, SDT, SERI}(σ_{HIEUMAY = 'Dell' ∧ LOAILK = 'Pin' ∧ HANGSX = 'Dell' ∧ NGAYTIEPNHAN ≥ '2024-10-01' ∧ NGAYTIEPNHAN ≤ '2024-12-31'}(KHACHHANG ⋈ THIETBI ⋈ PHIEUBH ⋈ CT_BAOHANH ⋈ LINHKIEN))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT KH.TENKH, KH.SDT, TB.SERI
FROM KHACHHANG KH
INNER JOIN THIETBI TB ON KH.MAKH = TB.MAKH
INNER JOIN PHIEUBH PBH ON TB.MATB = PBH.MATB
INNER JOIN CT_BAOHANH CT ON PBH.MAPBH = CT.MAPBH
INNER JOIN LINHKIEN LK ON CT.MALK = LK.MALK
WHERE TB.HIEUMAY = 'Dell' AND LK.LOAILK = 'Pin' AND LK.HANGSX = 'Dell'
  AND PBH.NGAYTIEPNHAN BETWEEN '2024-10-01' AND '2024-12-31';
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối 5 bảng từ KHACHHANG đến LINHKIEN theo quan hệ sở hữu và dịch vụ bảo hành.
1. Bước 2: Lọc theo hiệu máy, loại linh kiện, hãng sản xuất và khoảng thời gian quý 4.
1. Bước 3: Chiếu TENKH, SDT, SERI.

**Phân tích trường hợp biên (Edge Cases):**
Đẩy các phép chọn xuống từng quan hệ trước khi kết nối sẽ giúp tối ưu hóa đáng kể kích thước bảng trung gian.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 24 [RA-B24] — Kết Nối Học Viên Lớp IELTS Đã Hoàn Tất Học Phí
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOCVIEN(MAHV, HOTEN, EMAIL), BIENLAI(MABL, MAHV, MALOP, SOTIEN_NOP, NGAYTHU), LOPHOC(MALOP, MAKH, NGAYKHAIGIANG), KHOAHOC(MAKH, TENKH, HOCPHI_CHUAN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã học viên, họ tên và ngày khai giảng của các học viên đăng ký khóa học có tên 'IELTS Intensive 7.0' có biên lai nộp tiền bằng đúng học phí chuẩn của khóa học.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{HOCVIEN.MAHV, HOTEN, NGAYKHAIGIANG}(σ_{TENKH = 'IELTS Intensive 7.0' ∧ SOTIEN_NOP = HOCPHI_CHUAN}(HOCVIEN ⋈ BIENLAI ⋈ LOPHOC ⋈ KHOAHOC))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT HV.MAHV, HV.HOTEN, LH.NGAYKHAIGIANG
FROM HOCVIEN HV
INNER JOIN BIENLAI BL ON HV.MAHV = BL.MAHV
INNER JOIN LOPHOC LH ON BL.MALOP = LH.MALOP
INNER JOIN KHOAHOC KH ON LH.MAKH = KH.MAKH
WHERE KH.TENKH = 'IELTS Intensive 7.0' AND BL.SOTIEN_NOP = KH.HOCPHI_CHUAN;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối 4 bảng qua MAHV, MALOP, MAKH.
1. Bước 2: Lọc các bộ theo tên khóa học và điều kiện nộp đủ 100% học phí chuẩn.
1. Bước 3: Chiếu HOCVIEN.MAHV, HOTEN, NGAYKHAIGIANG.

**Phân tích trường hợp biên (Edge Cases):**
So sánh bằng giữa 2 cột thuộc tính khác bảng SOTIEN_NOP = HOCPHI_CHUAN trong vị từ chọn.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 25 [RA-B25] — Kết Nối Vận Đơn Hàng Hóa Tươi Sống Vận Chuyển Đi Tokyo
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `VANDON(MAVD, MACB, TENHANG, LOAIHANG, TRONGLUONG_KG), CHUYENBAY_CARGO(MACB, SOHIEU_BAY, SB_DEN, NGAYBAY)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã vận đơn, tên hàng và trọng lượng của các lô hàng thuộc loại 'Thuc pham tuoi song' được vận chuyển trên chuyến bay có sân bay đến là 'NRT' (Tokyo Narita) có trọng lượng trên 500 kg.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAVD, TENHANG, TRONGLUONG_KG}(σ_{LOAIHANG = 'Thuc pham tuoi song' ∧ SB_DEN = 'NRT' ∧ TRONGLUONG_KG > 500}(VANDON ⋈ CHUYENBAY_CARGO))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT VD.MAVD, VD.TENHANG, VD.TRONGLUONG_KG
FROM VANDON VD
INNER JOIN CHUYENBAY_CARGO CB ON VD.MACB = CB.MACB
WHERE VD.LOAIHANG = N'Thuc pham tuoi song' AND CB.SB_DEN = 'NRT' AND VD.TRONGLUONG_KG > 500;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối VANDON với CHUYENBAY_CARGO qua khóa ngoại MACB.
1. Bước 2: Lọc các lô hàng thực phẩm tươi sống bay đến sân bay NRT có trọng lượng vượt ngưỡng 500 kg.
1. Bước 3: Chiếu MAVD, TENHANG, TRONGLUONG_KG.

**Phân tích trường hợp biên (Edge Cases):**
Mã sân bay chuẩn IATA gồm 3 ký tự viết hoa (NRT là Tokyo Narita).

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 26 [RA-B26] — ĐSQH Kết Ngoài: Khách Hàng VIP Chưa Phát Sinh Đơn Hàng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG(MAKH, HOTEN, LOAIKH, SDT), DONDATHANG(MADON, MAKH, NGAYDAT, TONGTIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã khách hàng, họ tên và số điện thoại của các khách hàng có hạng thẻ 'VIP' nhưng chưa từng đặt bất kỳ đơn hàng nào trong hệ thống.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAKH, HOTEN, SDT}(σ_{LOAIKH = 'VIP' ∧ MADON IS NULL}(KHACHHANG ⟕ DONDATHANG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT KH.MAKH, KH.HOTEN, KH.SDT
FROM KHACHHANG KH
LEFT OUTER JOIN DONDATHANG DH ON KH.MAKH = DH.MAKH
WHERE KH.LOAIKH = 'VIP' AND DH.MADON IS NULL;
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng phép kết ngoài trái (Left Outer Join) KHACHHANG ⟕ DONDATHANG để giữ lại toàn bộ khách hàng kể cả khi không có đơn hàng tương ứng.
1. Bước 2: Lọc các khách hàng có hạng thẻ VIP và có MADON IS NULL (chứng minh chưa từng phát sinh đơn hàng).
1. Bước 3: Chiếu các thuộc tính MAKH, HOTEN, SDT.

**Phân tích trường hợp biên (Edge Cases):**
Cực kỳ quan trọng: Nếu đặt điều kiện DH.MADON IS NULL trong ON hoặc dùng INNER JOIN sẽ làm mất toàn bộ khách hàng chưa có đơn hàng! Điều kiện lọc thuộc tính bảng trái LOAIKH = 'VIP' có thể lọc trước hoặc đặt trong WHERE.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 27 [RA-B27] — ĐSQH Kết Ngoài: Giảng Viên Cơ Hữu Chưa Hướng Dẫn Khóa Luận
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `GIANGVIEN(MAGV, HOTEN, HOCVI, LOAI_HD), KHOALUAN(MAKL, MAGV_HD, TEN_KL, NAM_TN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã giảng viên, họ tên và học vị của các giảng viên có hợp đồng là 'Co huu' nhưng chưa hướng dẫn bất kỳ khóa luận tốt nghiệp nào trong năm '2024'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAGV, HOTEN, HOCVI}(σ_{LOAI_HD = 'Co huu' ∧ MAKL IS NULL}(GIANGVIEN ⟕ (σ_{NAM_TN = 2024}(KHOALUAN))))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT GV.MAGV, GV.HOTEN, GV.HOCVI
FROM GIANGVIEN GV
LEFT OUTER JOIN KHOALUAN KL ON GV.MAGV = KL.MAGV_HD AND KL.NAM_TN = 2024
WHERE GV.LOAI_HD = N'Co huu' AND KL.MAKL IS NULL;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc bảng khóa luận theo năm 2024 trước khi kết nối hoặc đưa điều kiện năm vào mệnh đề ON của LEFT JOIN.
1. Bước 2: Thực hiện phép kết trái GIANGVIEN ⟕ KHOALUAN_2024 để bảo toàn tất cả giảng viên cơ hữu.
1. Bước 3: Chọn các dòng có KL.MAKL mang giá trị NULL và chiếu MAGV, HOTEN, HOCVI.

**Phân tích trường hợp biên (Edge Cases):**
Lưu ý bẫy ngữ nghĩa: Không được đặt KL.NAM_TN = 2024 trong mệnh đề WHERE vì giá trị NULL sẽ bị triệt tiêu, biến câu truy vấn thành INNER JOIN.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 28 [RA-B28] — ĐSQH Kết Ngoài: Phòng Deluxe Chưa Được Thuê Trong Tháng 12
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHONG(MAPHONG, LOAIPHONG, GIA_NGAY), PHIEUTHUE(MAPT, MAPHONG, NGAYDEN, NGAYDI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các phòng thuộc loại 'Deluxe' chưa từng được khách thuê trong suốt tháng 12/2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAPHONG, GIA_NGAY}(σ_{LOAIPHONG = 'Deluxe' ∧ MAPT IS NULL}(PHONG ⟕ (σ_{NGAYDEN ≤ '2024-12-31' ∧ NGAYDI ≥ '2024-12-01'}(PHIEUTHUE))))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT P.MAPHONG, P.GIA_NGAY
FROM PHONG P
LEFT OUTER JOIN PHIEUTHUE PT ON P.MAPHONG = PT.MAPHONG
  AND PT.NGAYDEN <= '2024-12-31' AND PT.NGAYDI >= '2024-12-01'
WHERE P.LOAIPHONG = 'Deluxe' AND PT.MAPT IS NULL;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định tập các phiếu thuê có khoảng thời gian giao thoa với tháng 12/2024.
1. Bước 2: Kết trái bảng PHONG loại Deluxe với tập phiếu thuê trên.
1. Bước 3: Lọc các phòng có MAPT IS NULL (chưa từng được thuê) và chiếu MAPHONG, GIA_NGAY.

**Phân tích trường hợp biên (Edge Cases):**
Điều kiện giao thoa khoảng thời gian [A, B] và [C, D] là A <= D AND B >= C.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 29 [RA-B29] — ĐSQH Kết Ngoài: Sách Tin Học Chưa Từng Được Mượn
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SACH(MASACH, TENSACH, THELOAI, NAMSX), CTPHIEUMUON(MAPM, MASACH, NGAYTRA)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã sách, tên sách và năm xuất bản của các cuốn sách thuộc thể loại 'Khoa hoc may tinh' chưa từng được mượn lần nào trong thư viện.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MASACH, TENSACH, NAMSX}(σ_{THELOAI = 'Khoa hoc may tinh' ∧ MAPM IS NULL}(SACH ⟕ CTPHIEUMUON))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT S.MASACH, S.TENSACH, S.NAMSX
FROM SACH S
LEFT OUTER JOIN CTPHIEUMUON CT ON S.MASACH = CT.MASACH
WHERE S.THELOAI = N'Khoa hoc may tinh' AND CT.MAPM IS NULL;
```

**Các bước suy luận tư duy:**
1. Bước 1: Thực hiện phép kết trái giữa SACH và CTPHIEUMUON theo mã sách MASACH.
1. Bước 2: Lọc các cuốn sách thỏa mãn thể loại 'Khoa hoc may tinh' và MAPM IS NULL.
1. Bước 3: Chiếu MASACH, TENSACH, NAMSX.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các cuốn sách mới nhập chưa có bạn đọc mượn, CTPHIEUMUON.MAPM sẽ tự động nhận giá trị NULL trong phép kết trái.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 30 [RA-B30] — ĐSQH Kết Ngoài: Căn Hộ Đã Bàn Giao Nhưng Chưa Có Cư Dân Lưu Trú
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CANHO(MACAN, SOHIEUCAN, MATN, TRANGTHAI), CUDAN(MACD, MACAN, HOTEN, NGAYDENVANG)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã căn hộ, số hiệu căn hộ của các căn hộ có trạng thái 'Da ban giao' thuộc tòa nhà 'TN01' nhưng hiện chưa có bất kỳ cư dân nào đăng ký sinh sống.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MACAN, SOHIEUCAN}(σ_{TRANGTHAI = 'Da ban giao' ∧ MATN = 'TN01' ∧ MACD IS NULL}(CANHO ⟕ CUDAN))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT CH.MACAN, CH.SOHIEUCAN
FROM CANHO CH
LEFT OUTER JOIN CUDAN CD ON CH.MACAN = CD.MACAN
WHERE CH.TRANGTHAI = N'Da ban giao' AND CH.MATN = 'TN01' AND CD.MACD IS NULL;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết trái CANHO với CUDAN trên thuộc tính chung MACAN.
1. Bước 2: Lọc các bộ có trạng thái 'Da ban giao', mã tòa nhà 'TN01' và MACD IS NULL.
1. Bước 3: Chiếu MACAN, SOHIEUCAN.

**Phân tích trường hợp biên (Edge Cases):**
Ràng buộc toàn vẹn: Căn hộ chưa có cư dân thì các cột của bảng CUDAN đều là NULL.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 31 [RA-B31] — ĐSQH Kết Ngoài: Tuyến Xe Buýt Trục Chính Chưa Phân Công Tài Xế
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TUYENXE(MATUYEN, TENTUYEN, LOAITUYEN), PHANCONG(MAPC, MATUYEN, MATX, NGAY_PC)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã tuyến và tên tuyến của các tuyến xe buýt thuộc loại 'Truc chinh' chưa được phân công tài xế trong ngày '2024-11-01'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MATUYEN, TENTUYEN}(σ_{LOAITUYEN = 'Truc chinh' ∧ MAPC IS NULL}(TUYENXE ⟕ (σ_{NGAY_PC = '2024-11-01'}(PHANCONG))))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TXE.MATUYEN, TXE.TENTUYEN
FROM TUYENXE TXE
LEFT OUTER JOIN PHANCONG PC ON TXE.MATUYEN = PC.MATUYEN AND PC.NGAY_PC = '2024-11-01'
WHERE TXE.LOAITUYEN = N'Truc chinh' AND PC.MAPC IS NULL;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc dữ liệu phân công ngày 2024-11-01 trước khi kết ngoài trái.
1. Bước 2: Kết ngoài trái TUYENXE với phân công ngày đó.
1. Bước 3: Chọn các tuyến xe có MAPC IS NULL và loại tuyến trục chính.

**Phân tích trường hợp biên (Edge Cases):**
Đảm bảo các tuyến xe chưa phân công không bị loại bỏ khỏi kết quả.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 32 [RA-B32] — ĐSQH Kết Ngoài: Nhân Viên Kỹ Thuật Chưa Từng Nhận Khen Thưởng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHANVIEN(MANV, HOTEN, PHONGBAN, LUONGCB), KHENTHUONG(MAKT, MANV, SOTIEN_THUONG, NAM)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã nhân viên, họ tên và lương cơ bản của các nhân viên thuộc phòng 'Ky thuat' chưa từng nhận bất kỳ khoản tiền khen thưởng nào.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MANV, HOTEN, LUONGCB}(σ_{PHONGBAN = 'Ky thuat' ∧ MAKT IS NULL}(NHANVIEN ⟕ KHENTHUONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT NV.MANV, NV.HOTEN, NV.LUONGCB
FROM NHANVIEN NV
LEFT OUTER JOIN KHENTHUONG KT ON NV.MANV = KT.MANV
WHERE NV.PHONGBAN = N'Ky thuat' AND KT.MAKT IS NULL;
```

**Các bước suy luận tư duy:**
1. Bước 1: Thực hiện phép kết ngoài trái NHANVIEN ⟕ KHENTHUONG.
1. Bước 2: Lọc theo phòng ban 'Ky thuat' và điều kiện MAKT IS NULL.
1. Bước 3: Chiếu MANV, HOTEN, LUONGCB.

**Phân tích trường hợp biên (Edge Cases):**
Nếu dùng phép trừ: π_{MANV, HOTEN, LUONGCB}(σ_{PHONGBAN = 'Ky thuat'}(NHANVIEN)) - π_{MANV, HOTEN, LUONGCB}(NHANVIEN ⋈ KHENTHUONG) cho kết quả tương đương.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 33 [RA-B33] — ĐSQH Kết Ngoài: Khóa Học Chuyên Đề Chưa Có Học Viên Đăng Ký
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHOAHOC(MAKH, TENKH, HOCPHI, THELOAI), DANGKY_KH(MADK, MAKH, MAHV, NGAYDK)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã khóa học, tên khóa học và học phí của các khóa học thuộc thể loại 'Chuyen de nang cao' chưa có bất kỳ học viên nào đăng ký tham gia.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAKH, TENKH, HOCPHI}(σ_{THELOAI = 'Chuyen de nang cao' ∧ MADK IS NULL}(KHOAHOC ⟕ DANGKY_KH))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT KH.MAKH, KH.TENKH, KH.HOCPHI
FROM KHOAHOC KH
LEFT OUTER JOIN DANGKY_KH DK ON KH.MAKH = DK.MAKH
WHERE KH.THELOAI = N'Chuyen de nang cao' AND DK.MADK IS NULL;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết ngoài trái KHOAHOC với DANGKY_KH theo MAKH.
1. Bước 2: Lọc các bộ có THELOAI = 'Chuyen de nang cao' và MADK IS NULL.
1. Bước 3: Chiếu MAKH, TENKH, HOCPHI.

**Phân tích trường hợp biên (Edge Cases):**
Phép kết ngoài bảo toàn những khóa học mới mở trong danh mục.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 34 [RA-B34] — ĐSQH Kết Ngoài: Thiết Bị Y Tế Chưa Từng Qua Bảo Trì Định Kỳ
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THIETBI_YTE(MATB, TENTB, KHOAPHONG, NAMSX), LICHSU_BAOTRI(MABT, MATB, NGAYBT, KETQUA)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã thiết bị, tên thiết bị và khoa phòng của các thiết bị y tế sản xuất sau năm 2022 nhưng chưa từng ghi nhận bất kỳ lượt bảo trì nào.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MATB, TENTB, KHOAPHONG}(σ_{NAMSX > 2022 ∧ MABT IS NULL}(THIETBI_YTE ⟕ LICHSU_BAOTRI))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TB.MATB, TB.TENTB, TB.KHOAPHONG
FROM THIETBI_YTE TB
LEFT OUTER JOIN LICHSU_BAOTRI BT ON TB.MATB = BT.MATB
WHERE TB.NAMSX > 2022 AND BT.MABT IS NULL;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết ngoài trái THIETBI_YTE với LICHSU_BAOTRI qua MATB.
1. Bước 2: Lọc theo năm sản xuất > 2022 và điều kiện MABT IS NULL.
1. Bước 3: Chiếu MATB, TENTB, KHOAPHONG.

**Phân tích trường hợp biên (Edge Cases):**
Đảm bảo an toàn vận hành trang thiết bị bệnh viện bằng cách phát hiện thiết bị chưa bảo trì.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 35 [RA-B35] — ĐSQH Kết Ngoài: Nhà Cung Cấp Đã Ký Kết Nhưng Chưa Từng Giao Hàng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHACUNGCAP(MANCC, TENNCC, THANHPHO), DONDATHANG_NCC(MADON_NCC, MANCC, NGAYDAT, TRANGTHAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã nhà cung cấp, tên nhà cung cấp tại thành phố 'Ha Noi' chưa từng phát sinh bất kỳ đơn đặt hàng nào từ công ty.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MANCC, TENNCC}(σ_{THANHPHO = 'Ha Noi' ∧ MADON_NCC IS NULL}(NHACUNGCAP ⟕ DONDATHANG_NCC))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT NCC.MANCC, NCC.TENNCC
FROM NHACUNGCAP NCC
LEFT OUTER JOIN DONDATHANG_NCC DDH ON NCC.MANCC = DDH.MANCC
WHERE NCC.THANHPHO = N'Ha Noi' AND DDH.MADON_NCC IS NULL;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết ngoài trái NHACUNGCAP với DONDATHANG_NCC qua MANCC.
1. Bước 2: Lọc các nhà cung cấp ở Hà Nội có MADON_NCC IS NULL.
1. Bước 3: Chiếu MANCC, TENNCC.

**Phân tích trường hợp biên (Edge Cases):**
Phép kết trái giữ lại cả những nhà cung cấp mới ký hợp đồng nguyên tắc.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 36 [RA-B36] — ĐSQH Tự Kết Phân Cấp: Nhân Viên Có Lương Cao Hơn Quản Lý
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHANVIEN(MANV, HOTEN, LUONG, MA_QL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã nhân viên, họ tên nhân viên, tên người quản lý trực tiếp và mức chênh lệch lương của các nhân viên có lương cao hơn chính người quản lý trực tiếp của họ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{NV.MANV, NV.HOTEN, QL.HOTEN}(σ_{NV.LUONG > QL.LUONG}(ρ_{NV}(NHANVIEN) ⋈_{NV.MA_QL = QL.MANV} ρ_{QL}(NHANVIEN)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT NV.MANV, NV.HOTEN AS TEN_NV, QL.HOTEN AS TEN_QL
FROM NHANVIEN NV
INNER JOIN NHANVIEN QL ON NV.MA_QL = QL.MANV
WHERE NV.LUONG > QL.LUONG;
```

**Các bước suy luận tư duy:**
1. Bước 1: Dùng phép đổi tên ρ tạo 2 thể hiện độc lập: NV (nhân viên) và QL (quản lý trực tiếp).
1. Bước 2: Tự kết nối 2 thể hiện theo điều kiện NV.MA_QL = QL.MANV.
1. Bước 3: Chọn các bộ có NV.LUONG > QL.LUONG.
1. Bước 4: Chiếu NV.MANV, NV.HOTEN, QL.HOTEN.

**Phân tích trường hợp biên (Edge Cases):**
Loại trừ nhân viên cấp cao nhất (Tổng Giám đốc có MA_QL IS NULL) để tránh lỗi so sánh với NULL.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 37 [RA-B37] — ĐSQH Tự Kết: Chuyến Bay Khứ Hồi Giữa Hai Sân Bay Trong Cùng Ngày
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CHUYENBAY(MACB, HANG_BAY, SB_DI, SB_DEN, NGAYBAY, GIOBAY)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các cặp mã chuyến bay khứ hồi (chuyến đi và chuyến về) của cùng hãng bay 'Vietnam Airlines' bay giữa Hà Nội ('HAN') và TP.HCM ('SGN') trong cùng ngày '2024-12-25'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{CB1.MACB, CB2.MACB}(σ_{CB1.HANG_BAY = 'Vietnam Airlines' ∧ CB1.SB_DI = 'SGN' ∧ CB1.SB_DEN = 'HAN' ∧ CB2.SB_DI = 'HAN' ∧ CB2.SB_DEN = 'SGN' ∧ CB1.NGAYBAY = '2024-12-25' ∧ CB2.GIOBAY > CB1.GIOBAY}(ρ_{CB1}(CHUYENBAY) ⋈_{CB1.HANG_BAY = CB2.HANG_BAY ∧ CB1.NGAYBAY = CB2.NGAYBAY} ρ_{CB2}(CHUYENBAY)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT CB1.MACB AS CHUYEN_DI, CB2.MACB AS CHUYEN_VE
FROM CHUYENBAY CB1
INNER JOIN CHUYENBAY CB2 ON CB1.HANG_BAY = CB2.HANG_BAY AND CB1.NGAYBAY = CB2.NGAYBAY
WHERE CB1.HANG_BAY = 'Vietnam Airlines'
  AND CB1.SB_DI = 'SGN' AND CB1.SB_DEN = 'HAN'
  AND CB2.SB_DI = 'HAN' AND CB2.SB_DEN = 'SGN'
  AND CB1.NGAYBAY = '2024-12-25' AND CB2.GIOBAY > CB1.GIOBAY;
```

**Các bước suy luận tư duy:**
1. Bước 1: Đổi tên 2 thể hiện chuyến bay CB1 (chiều đi) và CB2 (chiều về).
1. Bước 2: Kết theo cùng hãng bay và cùng ngày bay.
1. Bước 3: Lọc chiều đi SGN -> HAN và chiều về HAN -> SGN kèm điều kiện giờ về CB2.GIOBAY > CB1.GIOBAY.
1. Bước 4: Chiếu mã 2 chuyến bay.

**Phân tích trường hợp biên (Edge Cases):**
Điều kiện giờ về sau giờ đi đảm bảo tính khả thi thực tế của hành trình khứ hồi.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 38 [RA-B38] — ĐSQH Tự Kết: Môn Học Có Số Tín Chỉ Lớn Hơn Môn Tiên Quyết
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `MONHOC(MAMH, TENMH, SOTC, MAMH_TQ)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã môn học, tên môn học và tên môn tiên quyết của các môn học có số tín chỉ lớn hơn số tín chỉ của chính môn học tiên quyết của nó.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MH.MAMH, MH.TENMH, TQ.TENMH}(σ_{MH.SOTC > TQ.SOTC}(ρ_{MH}(MONHOC) ⋈_{MH.MAMH_TQ = TQ.MAMH} ρ_{TQ}(MONHOC)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MH.MAMH, MH.TENMH AS TEN_MON, TQ.TENMH AS TEN_MON_TIENQUYET
FROM MONHOC MH
INNER JOIN MONHOC TQ ON MH.MAMH_TQ = TQ.MAMH
WHERE MH.SOTC > TQ.SOTC;
```

**Các bước suy luận tư duy:**
1. Bước 1: Đổi tên hai thể hiện: MH (môn học hiện tại) và TQ (môn tiên quyết).
1. Bước 2: Kết nối theo MH.MAMH_TQ = TQ.MAMH.
1. Bước 3: Lọc MH.SOTC > TQ.SOTC.
1. Bước 4: Chiếu các thuộc tính cần thiết.

**Phân tích trường hợp biên (Edge Cases):**
Các môn không có môn tiên quyết (MAMH_TQ IS NULL) sẽ tự động bị loại khỏi phép kết trong.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 39 [RA-B39] — ĐSQH Tự Kết: Sản Phẩm Cùng Loại Có Giá Bán Gấp Đôi
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SANPHAM(MASP, TENSP, LOAISP, GIABAN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các cặp mã sản phẩm (SP1, SP2) thuộc cùng một loại sản phẩm ('Dien thoai') sao cho giá bán của SP1 gấp từ 2 lần trở lên so với giá bán của SP2.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{SP1.MASP, SP2.MASP}(σ_{SP1.LOAISP = 'Dien thoai' ∧ SP1.GIABAN ≥ 2 * SP2.GIABAN}(ρ_{SP1}(SANPHAM) ⋈_{SP1.LOAISP = SP2.LOAISP ∧ SP1.MASP ≠ SP2.MASP} ρ_{SP2}(SANPHAM)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT SP1.MASP AS MASP_CAO, SP2.MASP AS MASP_THAP
FROM SANPHAM SP1
INNER JOIN SANPHAM SP2 ON SP1.LOAISP = SP2.LOAISP AND SP1.MASP <> SP2.MASP
WHERE SP1.LOAISP = N'Dien thoai' AND SP1.GIABAN >= 2 * SP2.GIABAN;
```

**Các bước suy luận tư duy:**
1. Bước 1: Đổi tên 2 thể hiện sản phẩm SP1 và SP2.
1. Bước 2: Kết theo cùng loại sản phẩm và mã khác nhau SP1.MASP ≠ SP2.MASP.
1. Bước 3: Lọc theo loại 'Dien thoai' và điều kiện giá SP1.GIABAN >= 2 * SP2.GIABAN.
1. Bước 4: Chiếu cặp mã sản phẩm.

**Phân tích trường hợp biên (Edge Cases):**
Bắt buộc có điều kiện SP1.MASP ≠ SP2.MASP để tránh tự so sánh một sản phẩm với chính nó.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 40 [RA-B40] — ĐSQH Tự Kết: Bác Sĩ Cùng Chuyên Khoa Có Thâm Niên Cao Hơn Trưởng Khoa
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BACSI(MABS, HOTEN, CHUYENKHOA, NAM_KINHNGHIEM, MABS_TRUONGKHOA)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã bác sĩ và họ tên của các bác sĩ có số năm kinh nghiệm cao hơn số năm kinh nghiệm của chính bác sĩ trưởng khoa phụ trách chuyên khoa đó.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{BS.MABS, BS.HOTEN}(σ_{BS.NAM_KINHNGHIEM > TK.NAM_KINHNGHIEM}(ρ_{BS}(BACSI) ⋈_{BS.MABS_TRUONGKHOA = TK.MABS} ρ_{TK}(BACSI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT BS.MABS, BS.HOTEN
FROM BACSI BS
INNER JOIN BACSI TK ON BS.MABS_TRUONGKHOA = TK.MABS
WHERE BS.NAM_KINHNGHIEM > TK.NAM_KINHNGHIEM;
```

**Các bước suy luận tư duy:**
1. Bước 1: Đổi tên 2 thể hiện bác sĩ: BS (bác sĩ thành viên) và TK (bác sĩ trưởng khoa).
1. Bước 2: Kết theo BS.MABS_TRUONGKHOA = TK.MABS.
1. Bước 3: Lọc BS.NAM_KINHNGHIEM > TK.NAM_KINHNGHIEM.
1. Bước 4: Chiếu BS.MABS, BS.HOTEN.

**Phân tích trường hợp biên (Edge Cases):**
Trưởng khoa có MABS_TRUONGKHOA là chính mình hoặc NULL tùy thiết kế cơ sở dữ liệu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 41 [RA-B41] — ĐSQH Phép Hợp (Union): Sinh Viên Đạt Học Bổng Kỳ 1 Hoặc Kỳ 2
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOCBONG_HK1(MSSV, HOTEN, DIEM_RL, TIEN_HB), HOCBONG_HK2(MSSV, HOTEN, DIEM_RL, TIEN_HB)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã số sinh viên và họ tên của các sinh viên được nhận học bổng khuyến khích học tập ở Học kỳ 1 HOẶC Học kỳ 2 trong năm học 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MSSV, HOTEN}(HOCBONG_HK1) ∪ π_{MSSV, HOTEN}(HOCBONG_HK2)
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MSSV, HOTEN FROM HOCBONG_HK1
UNION
SELECT MSSV, HOTEN FROM HOCBONG_HK2;
```

**Các bước suy luận tư duy:**
1. Bước 1: Chiếu hai thuộc tính MSSV và HOTEN trên cả hai quan hệ HOCBONG_HK1 và HOCBONG_HK2 để bảo đảm tính khả hợp (cùng bậc 2 và tương thích kiểu dữ liệu).
1. Bước 2: Áp dụng phép hợp (∪) để lấy tất cả sinh viên nhận học bổng ở ít nhất một trong hai kỳ, tự động loại bỏ các sinh viên trùng lặp nhận học bổng cả hai kỳ.

**Phân tích trường hợp biên (Edge Cases):**
Phép hợp trong ĐSQH thuần túy loại bỏ trùng lặp (tương đương UNION trong SQL, khác UNION ALL).

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 42 [RA-B42] — ĐSQH Phép Giao (Intersect): Khách Hàng Mua Cả Smart TV Và Loa Soundbar
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONHANG(MADON, MAKH, NGAYDAT), CTHD(MADON, MASP), SANPHAM(MASP, TENSP, LOAISP)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã khách hàng của những khách hàng đã mua cả sản phẩm thuộc loại 'Smart TV' VÀ sản phẩm thuộc loại 'Loa Soundbar' trong năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAKH}(σ_{LOAISP = 'Smart TV' ∧ NGAYDAT ≥ '2024-01-01'}(DONHANG ⋈ CTHD ⋈ SANPHAM)) ∩ π_{MAKH}(σ_{LOAISP = 'Loai Soundbar' ∧ NGAYDAT ≥ '2024-01-01'}(DONHANG ⋈ CTHD ⋈ SANPHAM))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT DH.MAKH
FROM DONHANG DH INNER JOIN CTHD CT ON DH.MADON = CT.MADON INNER JOIN SANPHAM SP ON CT.MASP = SP.MASP
WHERE SP.LOAISP = 'Smart TV' AND DH.NGAYDAT >= '2024-01-01'
INTERSECT
SELECT DH.MAKH
FROM DONHANG DH INNER JOIN CTHD CT ON DH.MADON = CT.MADON INNER JOIN SANPHAM SP ON CT.MASP = SP.MASP
WHERE SP.LOAISP = 'Loai Soundbar' AND DH.NGAYDAT >= '2024-01-01';
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập khách hàng mua Smart TV trong năm 2024.
1. Bước 2: Tìm tập khách hàng mua Loa Soundbar trong năm 2024.
1. Bước 3: Lấy giao (∩) của hai tập hợp trên để tìm khách hàng đồng thời thuộc cả hai nhóm.

**Phân tích trường hợp biên (Edge Cases):**
Hai biểu thức con phải cùng chiếu ra duy nhất thuộc tính MAKH để thỏa mãn điều kiện khả hợp.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 43 [RA-B43] — ĐSQH Phép Trừ (Except): Giảng Viên Dạy Lý Thuyết Nhưng Không Dạy Thực Hành
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `GIANGVIEN(MAGV, HOTEN, MAKHOA), LOPHOCPHAN(MALHP, MAGV, LOAI_LHP)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã giảng viên và họ tên của các giảng viên có tham gia giảng dạy lớp học phần lý thuyết (LOAI_LHP = 'Ly thuyet') nhưng KHÔNG tham gia giảng dạy bất kỳ lớp học phần thực hành nào (LOAI_LHP = 'Thuc hanh').

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{GIANGVIEN.MAGV, HOTEN}(σ_{LOAI_LHP = 'Ly thuyet'}(GIANGVIEN ⋈ LOPHOCPHAN)) - π_{GIANGVIEN.MAGV, HOTEN}(σ_{LOAI_LHP = 'Thuc hanh'}(GIANGVIEN ⋈ LOPHOCPHAN))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT GV.MAGV, GV.HOTEN
FROM GIANGVIEN GV INNER JOIN LOPHOCPHAN LHP ON GV.MAGV = LHP.MAGV
WHERE LHP.LOAI_LHP = 'Ly thuyet'
EXCEPT
SELECT GV.MAGV, GV.HOTEN
FROM GIANGVIEN GV INNER JOIN LOPHOCPHAN LHP ON GV.MAGV = LHP.MAGV
WHERE LHP.LOAI_LHP = 'Thuc hanh';
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập giảng viên phụ trách lớp lý thuyết: R1 = π_{MAGV, HOTEN}(σ_{LOAI_LHP = 'Ly thuyet'}(GIANGVIEN ⋈ LOPHOCPHAN)).
1. Bước 2: Tìm tập giảng viên phụ trách lớp thực hành: R2 = π_{MAGV, HOTEN}(σ_{LOAI_LHP = 'Thuc hanh'}(GIANGVIEN ⋈ LOPHOCPHAN)).
1. Bước 3: Lấy hiệu tập hợp R1 - R2 để thu được giảng viên chỉ dạy lý thuyết.

**Phân tích trường hợp biên (Edge Cases):**
Phép trừ không có tính giao hoán: R1 - R2 khác R2 - R1.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 44 [RA-B44] — ĐSQH Phép Trừ: Dược Phẩm Có Ở Kho Quận 1 Nhưng Hết Ở Kho Quận 5
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TONKHO(MAKHO, MATHUOC, SOLUONG_TON), KHO(MAKHO, TENKHO, QUAN), THUOC(MATHUOC, TENTHUOC)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã thuốc và tên thuốc của các loại thuốc có số lượng tồn kho lớn hơn 0 tại kho ở 'Quan 1' nhưng KHÔNG còn tồn kho (hoặc không lưu kho) tại kho ở 'Quan 5'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{THUOC.MATHUOC, TENTHUOC}(σ_{QUAN = 'Quan 1' ∧ SOLUONG_TON > 0}(THUOC ⋈ TONKHO ⋈ KHO)) - π_{THUOC.MATHUOC, TENTHUOC}(σ_{QUAN = 'Quan 5' ∧ SOLUONG_TON > 0}(THUOC ⋈ TONKHO ⋈ KHO))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT T.MATHUOC, T.TENTHUOC
FROM THUOC T INNER JOIN TONKHO TK ON T.MATHUOC = TK.MATHUOC INNER JOIN KHO K ON TK.MAKHO = K.MAKHO
WHERE K.QUAN = 'Quan 1' AND TK.SOLUONG_TON > 0
EXCEPT
SELECT T.MATHUOC, T.TENTHUOC
FROM THUOC T INNER JOIN TONKHO TK ON T.MATHUOC = TK.MATHUOC INNER JOIN KHO K ON TK.MAKHO = K.MAKHO
WHERE K.QUAN = 'Quan 5' AND TK.SOLUONG_TON > 0;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định danh mục thuốc còn hàng tại kho Quận 1.
1. Bước 2: Xác định danh mục thuốc còn hàng tại kho Quận 5.
1. Bước 3: Lấy hiệu tập hợp giữa danh mục Quận 1 trừ đi danh mục Quận 5.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm cả hai nhánh phép trừ chiếu cùng danh sách thuộc tính (MATHUOC, TENTHUOC).

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 45 [RA-B45] — ĐSQH Phép Giao: Bạn Đọc Vừa Là Sinh Viên Vừa Là Cán Bộ Nghiên Cứu
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DOCGIA_SINHVIEN(MADG, HOTEN, CCCD, KHOA), DOCGIA_CANBO(MADG, HOTEN, CCCD, PHONGBAN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã bạn đọc, họ tên và số căn cước công dân (CCCD) của những người vừa có thẻ bạn đọc sinh viên vừa có thẻ bạn đọc cán bộ trong cơ sở dữ liệu thư viện.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MADG, HOTEN, CCCD}(DOCGIA_SINHVIEN) ∩ π_{MADG, HOTEN, CCCD}(DOCGIA_CANBO)
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MADG, HOTEN, CCCD FROM DOCGIA_SINHVIEN
INTERSECT
SELECT MADG, HOTEN, CCCD FROM DOCGIA_CANBO;
```

**Các bước suy luận tư duy:**
1. Bước 1: Chiếu các thuộc tính nhận diện khả hợp (MADG, HOTEN, CCCD) trên cả hai bảng bạn đọc.
1. Bước 2: Áp dụng phép giao (∩) để tìm những người hiện diện ở cả hai danh mục.

**Phân tích trường hợp biên (Edge Cases):**
Thuộc tính KHOA và PHONGBAN khác nhau không thể tham gia trực tiếp vào phép giao; bắt buộc phải chiếu trước khi giao.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---
