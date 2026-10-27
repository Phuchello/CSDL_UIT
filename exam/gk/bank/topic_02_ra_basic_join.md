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
1. Bước 2: Chiếu 4 thuộc tính thông tin thuốc.

**Phân tích trường hợp biên (Edge Cases):**
Cần bảo đảm kiểm tra đúng ký tự tiếng Việt Unicode.

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
1. Bước 1: Lọc theo chuyên khoa, học vị và năm thâm niên công tác.
1. Bước 2: Chiếu các cột mã, họ tên và số năm kinh nghiệm.

**Phân tích trường hợp biên (Edge Cases):**
Chú ý gom nhóm điều kiện chuyên khoa bằng phép OR.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 11 [RA-B11] — Kết Nối Sinh Viên Và Kết Quả Thi Môn Cơ Sở Dữ Liệu
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SINHVIEN(MSSV, HOTEN, MALOP), MONHOC(MAMH, TENMH), KETQUA(MSSV, MAMH, DIEMTHI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã số sinh viên, họ tên sinh viên và điểm thi của các sinh viên có điểm thi môn 'Co so du lieu' từ 8.0 trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{SINHVIEN.MSSV, HOTEN, DIEMTHI}(σ_{TENMH = 'Co so du lieu' ∧ DIEMTHI ≥ 8.0}(SINHVIEN ⋈ KETQUA ⋈ MONHOC))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT SV.MSSV, SV.HOTEN, KQ.DIEMTHI
FROM SINHVIEN SV
INNER JOIN KETQUA KQ ON SV.MSSV = KQ.MSSV
INNER JOIN MONHOC MH ON KQ.MAMH = MH.MAMH
WHERE MH.TENMH = N'Co so du lieu' AND KQ.DIEMTHI >= 8.0;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối 3 quan hệ SINHVIEN, KETQUA và MONHOC theo các khóa ngoại tương ứng.
1. Bước 2: Chọn các bộ có tên môn học 'Co so du lieu' và điểm thi ≥ 8.0.
1. Bước 3: Chiếu MSSV, HOTEN, DIEMTHI.

**Phân tích trường hợp biên (Edge Cases):**
Cần phân biệt rõ thuộc tính MSSV thuộc SINHVIEN hay KETQUA để tránh nhập nhằng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 12 [RA-B12] — Kết Nối Khách Hàng Và Hóa Đơn Mua Sản Phẩm
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG(MAKH, HOTEN, DIACHI), HOADON(SOHD, MAKH, NGAYHD), CTHD(SOHD, MASP, SOLUONG), SANPHAM(MASP, TENSP, DONGIA)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết họ tên khách hàng và tên sản phẩm của các sản phẩm được khách hàng mua trong ngày '2024-10-20' với số lượng từ 5 trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{HOTEN, TENSP}(σ_{NGAYHD = '2024-10-20' ∧ SOLUONG ≥ 5}(KHACHHANG ⋈ HOADON ⋈ CTHD ⋈ SANPHAM))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT DISTINCT KH.HOTEN, SP.TENSP
FROM KHACHHANG KH
INNER JOIN HOADON HD ON KH.MAKH = HD.MAKH
INNER JOIN CTHD CT ON HD.SOHD = CT.SOHD
INNER JOIN SANPHAM SP ON CT.MASP = SP.MASP
WHERE HD.NGAYHD = '2024-10-20' AND CT.SOLUONG >= 5;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối chuỗi 4 quan hệ từ KHACHHANG đến SANPHAM.
1. Bước 2: Lọc hóa đơn phát sinh ngày 20/10/2024 có số lượng mua ≥ 5.
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

## Bài 16 [RA-B16] — ĐSQH Kết Nối Đa Bảng Nghiệp Vụ Số 16
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_A(MA_A, TEN_A, MA_B), BANG_B(MA_B, TEN_B, MA_C), BANG_C(MA_C, TEN_C, GIA_TRI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Truy vấn kết nối liên kết 3 bảng tìm dữ liệu thỏa điều kiện lọc nghiệp vụ tại kịch bản 16.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{TEN_A, TEN_B, GIA_TRI}(σ_{GIA_TRI > 16000}(BANG_A ⋈ BANG_B ⋈ BANG_C))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT A.TEN_A, B.TEN_B, C.GIA_TRI
FROM BANG_A A
INNER JOIN BANG_B B ON A.MA_B = B.MA_B
INNER JOIN BANG_C C ON B.MA_C = C.MA_C
WHERE C.GIA_TRI > 16000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Thực hiện phép kết nối tự nhiên qua các khóa ngoại MA_B và MA_C.
1. Bước 2: Lọc các bộ có giá trị lớn hơn ngưỡng quy định.
1. Bước 3: Chiếu các cột kết quả.

**Phân tích trường hợp biên (Edge Cases):**
Đảm bảo các khóa ngoại tham chiếu chính xác và không bị giá trị NULL làm mất dòng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 17 [RA-B17] — ĐSQH Kết Nối Đa Bảng Nghiệp Vụ Số 17
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_A(MA_A, TEN_A, MA_B), BANG_B(MA_B, TEN_B, MA_C), BANG_C(MA_C, TEN_C, GIA_TRI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Truy vấn kết nối liên kết 3 bảng tìm dữ liệu thỏa điều kiện lọc nghiệp vụ tại kịch bản 17.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{TEN_A, TEN_B, GIA_TRI}(σ_{GIA_TRI > 17000}(BANG_A ⋈ BANG_B ⋈ BANG_C))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT A.TEN_A, B.TEN_B, C.GIA_TRI
FROM BANG_A A
INNER JOIN BANG_B B ON A.MA_B = B.MA_B
INNER JOIN BANG_C C ON B.MA_C = C.MA_C
WHERE C.GIA_TRI > 17000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Thực hiện phép kết nối tự nhiên qua các khóa ngoại MA_B và MA_C.
1. Bước 2: Lọc các bộ có giá trị lớn hơn ngưỡng quy định.
1. Bước 3: Chiếu các cột kết quả.

**Phân tích trường hợp biên (Edge Cases):**
Đảm bảo các khóa ngoại tham chiếu chính xác và không bị giá trị NULL làm mất dòng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 18 [RA-B18] — ĐSQH Kết Nối Đa Bảng Nghiệp Vụ Số 18
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_A(MA_A, TEN_A, MA_B), BANG_B(MA_B, TEN_B, MA_C), BANG_C(MA_C, TEN_C, GIA_TRI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Truy vấn kết nối liên kết 3 bảng tìm dữ liệu thỏa điều kiện lọc nghiệp vụ tại kịch bản 18.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{TEN_A, TEN_B, GIA_TRI}(σ_{GIA_TRI > 18000}(BANG_A ⋈ BANG_B ⋈ BANG_C))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT A.TEN_A, B.TEN_B, C.GIA_TRI
FROM BANG_A A
INNER JOIN BANG_B B ON A.MA_B = B.MA_B
INNER JOIN BANG_C C ON B.MA_C = C.MA_C
WHERE C.GIA_TRI > 18000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Thực hiện phép kết nối tự nhiên qua các khóa ngoại MA_B và MA_C.
1. Bước 2: Lọc các bộ có giá trị lớn hơn ngưỡng quy định.
1. Bước 3: Chiếu các cột kết quả.

**Phân tích trường hợp biên (Edge Cases):**
Đảm bảo các khóa ngoại tham chiếu chính xác và không bị giá trị NULL làm mất dòng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 19 [RA-B19] — ĐSQH Kết Nối Đa Bảng Nghiệp Vụ Số 19
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_A(MA_A, TEN_A, MA_B), BANG_B(MA_B, TEN_B, MA_C), BANG_C(MA_C, TEN_C, GIA_TRI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Truy vấn kết nối liên kết 3 bảng tìm dữ liệu thỏa điều kiện lọc nghiệp vụ tại kịch bản 19.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{TEN_A, TEN_B, GIA_TRI}(σ_{GIA_TRI > 19000}(BANG_A ⋈ BANG_B ⋈ BANG_C))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT A.TEN_A, B.TEN_B, C.GIA_TRI
FROM BANG_A A
INNER JOIN BANG_B B ON A.MA_B = B.MA_B
INNER JOIN BANG_C C ON B.MA_C = C.MA_C
WHERE C.GIA_TRI > 19000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Thực hiện phép kết nối tự nhiên qua các khóa ngoại MA_B và MA_C.
1. Bước 2: Lọc các bộ có giá trị lớn hơn ngưỡng quy định.
1. Bước 3: Chiếu các cột kết quả.

**Phân tích trường hợp biên (Edge Cases):**
Đảm bảo các khóa ngoại tham chiếu chính xác và không bị giá trị NULL làm mất dòng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 20 [RA-B20] — ĐSQH Kết Nối Đa Bảng Nghiệp Vụ Số 20
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_A(MA_A, TEN_A, MA_B), BANG_B(MA_B, TEN_B, MA_C), BANG_C(MA_C, TEN_C, GIA_TRI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Truy vấn kết nối liên kết 3 bảng tìm dữ liệu thỏa điều kiện lọc nghiệp vụ tại kịch bản 20.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{TEN_A, TEN_B, GIA_TRI}(σ_{GIA_TRI > 20000}(BANG_A ⋈ BANG_B ⋈ BANG_C))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT A.TEN_A, B.TEN_B, C.GIA_TRI
FROM BANG_A A
INNER JOIN BANG_B B ON A.MA_B = B.MA_B
INNER JOIN BANG_C C ON B.MA_C = C.MA_C
WHERE C.GIA_TRI > 20000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Thực hiện phép kết nối tự nhiên qua các khóa ngoại MA_B và MA_C.
1. Bước 2: Lọc các bộ có giá trị lớn hơn ngưỡng quy định.
1. Bước 3: Chiếu các cột kết quả.

**Phân tích trường hợp biên (Edge Cases):**
Đảm bảo các khóa ngoại tham chiếu chính xác và không bị giá trị NULL làm mất dòng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 21 [RA-B21] — ĐSQH Kết Nối Đa Bảng Nghiệp Vụ Số 21
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_A(MA_A, TEN_A, MA_B), BANG_B(MA_B, TEN_B, MA_C), BANG_C(MA_C, TEN_C, GIA_TRI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Truy vấn kết nối liên kết 3 bảng tìm dữ liệu thỏa điều kiện lọc nghiệp vụ tại kịch bản 21.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{TEN_A, TEN_B, GIA_TRI}(σ_{GIA_TRI > 21000}(BANG_A ⋈ BANG_B ⋈ BANG_C))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT A.TEN_A, B.TEN_B, C.GIA_TRI
FROM BANG_A A
INNER JOIN BANG_B B ON A.MA_B = B.MA_B
INNER JOIN BANG_C C ON B.MA_C = C.MA_C
WHERE C.GIA_TRI > 21000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Thực hiện phép kết nối tự nhiên qua các khóa ngoại MA_B và MA_C.
1. Bước 2: Lọc các bộ có giá trị lớn hơn ngưỡng quy định.
1. Bước 3: Chiếu các cột kết quả.

**Phân tích trường hợp biên (Edge Cases):**
Đảm bảo các khóa ngoại tham chiếu chính xác và không bị giá trị NULL làm mất dòng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 22 [RA-B22] — ĐSQH Kết Nối Đa Bảng Nghiệp Vụ Số 22
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_A(MA_A, TEN_A, MA_B), BANG_B(MA_B, TEN_B, MA_C), BANG_C(MA_C, TEN_C, GIA_TRI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Truy vấn kết nối liên kết 3 bảng tìm dữ liệu thỏa điều kiện lọc nghiệp vụ tại kịch bản 22.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{TEN_A, TEN_B, GIA_TRI}(σ_{GIA_TRI > 22000}(BANG_A ⋈ BANG_B ⋈ BANG_C))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT A.TEN_A, B.TEN_B, C.GIA_TRI
FROM BANG_A A
INNER JOIN BANG_B B ON A.MA_B = B.MA_B
INNER JOIN BANG_C C ON B.MA_C = C.MA_C
WHERE C.GIA_TRI > 22000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Thực hiện phép kết nối tự nhiên qua các khóa ngoại MA_B và MA_C.
1. Bước 2: Lọc các bộ có giá trị lớn hơn ngưỡng quy định.
1. Bước 3: Chiếu các cột kết quả.

**Phân tích trường hợp biên (Edge Cases):**
Đảm bảo các khóa ngoại tham chiếu chính xác và không bị giá trị NULL làm mất dòng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 23 [RA-B23] — ĐSQH Kết Nối Đa Bảng Nghiệp Vụ Số 23
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_A(MA_A, TEN_A, MA_B), BANG_B(MA_B, TEN_B, MA_C), BANG_C(MA_C, TEN_C, GIA_TRI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Truy vấn kết nối liên kết 3 bảng tìm dữ liệu thỏa điều kiện lọc nghiệp vụ tại kịch bản 23.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{TEN_A, TEN_B, GIA_TRI}(σ_{GIA_TRI > 23000}(BANG_A ⋈ BANG_B ⋈ BANG_C))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT A.TEN_A, B.TEN_B, C.GIA_TRI
FROM BANG_A A
INNER JOIN BANG_B B ON A.MA_B = B.MA_B
INNER JOIN BANG_C C ON B.MA_C = C.MA_C
WHERE C.GIA_TRI > 23000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Thực hiện phép kết nối tự nhiên qua các khóa ngoại MA_B và MA_C.
1. Bước 2: Lọc các bộ có giá trị lớn hơn ngưỡng quy định.
1. Bước 3: Chiếu các cột kết quả.

**Phân tích trường hợp biên (Edge Cases):**
Đảm bảo các khóa ngoại tham chiếu chính xác và không bị giá trị NULL làm mất dòng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 24 [RA-B24] — ĐSQH Kết Nối Đa Bảng Nghiệp Vụ Số 24
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_A(MA_A, TEN_A, MA_B), BANG_B(MA_B, TEN_B, MA_C), BANG_C(MA_C, TEN_C, GIA_TRI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Truy vấn kết nối liên kết 3 bảng tìm dữ liệu thỏa điều kiện lọc nghiệp vụ tại kịch bản 24.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{TEN_A, TEN_B, GIA_TRI}(σ_{GIA_TRI > 24000}(BANG_A ⋈ BANG_B ⋈ BANG_C))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT A.TEN_A, B.TEN_B, C.GIA_TRI
FROM BANG_A A
INNER JOIN BANG_B B ON A.MA_B = B.MA_B
INNER JOIN BANG_C C ON B.MA_C = C.MA_C
WHERE C.GIA_TRI > 24000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Thực hiện phép kết nối tự nhiên qua các khóa ngoại MA_B và MA_C.
1. Bước 2: Lọc các bộ có giá trị lớn hơn ngưỡng quy định.
1. Bước 3: Chiếu các cột kết quả.

**Phân tích trường hợp biên (Edge Cases):**
Đảm bảo các khóa ngoại tham chiếu chính xác và không bị giá trị NULL làm mất dòng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 25 [RA-B25] — ĐSQH Kết Nối Đa Bảng Nghiệp Vụ Số 25
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_A(MA_A, TEN_A, MA_B), BANG_B(MA_B, TEN_B, MA_C), BANG_C(MA_C, TEN_C, GIA_TRI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Truy vấn kết nối liên kết 3 bảng tìm dữ liệu thỏa điều kiện lọc nghiệp vụ tại kịch bản 25.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{TEN_A, TEN_B, GIA_TRI}(σ_{GIA_TRI > 25000}(BANG_A ⋈ BANG_B ⋈ BANG_C))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT A.TEN_A, B.TEN_B, C.GIA_TRI
FROM BANG_A A
INNER JOIN BANG_B B ON A.MA_B = B.MA_B
INNER JOIN BANG_C C ON B.MA_C = C.MA_C
WHERE C.GIA_TRI > 25000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Thực hiện phép kết nối tự nhiên qua các khóa ngoại MA_B và MA_C.
1. Bước 2: Lọc các bộ có giá trị lớn hơn ngưỡng quy định.
1. Bước 3: Chiếu các cột kết quả.

**Phân tích trường hợp biên (Edge Cases):**
Đảm bảo các khóa ngoại tham chiếu chính xác và không bị giá trị NULL làm mất dòng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 26 [RA-B26] — ĐSQH Kết Ngoài Left Outer Join (Bảo Toàn NULL) Kịch Bản 26
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THUCTHE_CHINH(MA_TC, TEN_TC, KHUVUC), THUCTHE_PHU(MA_TP, MA_TC, NGAY_PHATSINH, SOTIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết thông tin thực thể chính và các bản ghi phụ thuộc nếu có (kể cả chưa có phát sinh giao dịch) tại trường hợp 26.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_TC, TEN_TC, MA_TP, SOTIEN}(σ_{KHUVUC = 'KhuVuc_26'}(THUCTHE_CHINH ⟕ THUCTHE_PHU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TC.MA_TC, TC.TEN_TC, TP.MA_TP, TP.SOTIEN
FROM THUCTHE_CHINH TC
LEFT OUTER JOIN THUCTHE_PHU TP ON TC.MA_TC = TP.MA_TC
WHERE TC.KHUVUC = 'KhuVuc_26';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng phép kết trái (Left Outer Join) giữa thực thể chính và thực thể phụ.
1. Bước 2: Lọc theo khu vực quy định trên bảng chính.
1. Bước 3: Chiếu các cột cần thiết, các thực thể chính chưa có giao dịch sẽ mang giá trị NULL ở cột thuộc bảng phụ.

**Phân tích trường hợp biên (Edge Cases):**
Lưu ý không đặt điều kiện lọc bảng phụ trong mệnh đề WHERE vì sẽ biến phép kết ngoài thành kết trong!

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 27 [RA-B27] — ĐSQH Kết Ngoài Left Outer Join (Bảo Toàn NULL) Kịch Bản 27
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THUCTHE_CHINH(MA_TC, TEN_TC, KHUVUC), THUCTHE_PHU(MA_TP, MA_TC, NGAY_PHATSINH, SOTIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết thông tin thực thể chính và các bản ghi phụ thuộc nếu có (kể cả chưa có phát sinh giao dịch) tại trường hợp 27.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_TC, TEN_TC, MA_TP, SOTIEN}(σ_{KHUVUC = 'KhuVuc_27'}(THUCTHE_CHINH ⟕ THUCTHE_PHU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TC.MA_TC, TC.TEN_TC, TP.MA_TP, TP.SOTIEN
FROM THUCTHE_CHINH TC
LEFT OUTER JOIN THUCTHE_PHU TP ON TC.MA_TC = TP.MA_TC
WHERE TC.KHUVUC = 'KhuVuc_27';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng phép kết trái (Left Outer Join) giữa thực thể chính và thực thể phụ.
1. Bước 2: Lọc theo khu vực quy định trên bảng chính.
1. Bước 3: Chiếu các cột cần thiết, các thực thể chính chưa có giao dịch sẽ mang giá trị NULL ở cột thuộc bảng phụ.

**Phân tích trường hợp biên (Edge Cases):**
Lưu ý không đặt điều kiện lọc bảng phụ trong mệnh đề WHERE vì sẽ biến phép kết ngoài thành kết trong!

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 28 [RA-B28] — ĐSQH Kết Ngoài Left Outer Join (Bảo Toàn NULL) Kịch Bản 28
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THUCTHE_CHINH(MA_TC, TEN_TC, KHUVUC), THUCTHE_PHU(MA_TP, MA_TC, NGAY_PHATSINH, SOTIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết thông tin thực thể chính và các bản ghi phụ thuộc nếu có (kể cả chưa có phát sinh giao dịch) tại trường hợp 28.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_TC, TEN_TC, MA_TP, SOTIEN}(σ_{KHUVUC = 'KhuVuc_28'}(THUCTHE_CHINH ⟕ THUCTHE_PHU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TC.MA_TC, TC.TEN_TC, TP.MA_TP, TP.SOTIEN
FROM THUCTHE_CHINH TC
LEFT OUTER JOIN THUCTHE_PHU TP ON TC.MA_TC = TP.MA_TC
WHERE TC.KHUVUC = 'KhuVuc_28';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng phép kết trái (Left Outer Join) giữa thực thể chính và thực thể phụ.
1. Bước 2: Lọc theo khu vực quy định trên bảng chính.
1. Bước 3: Chiếu các cột cần thiết, các thực thể chính chưa có giao dịch sẽ mang giá trị NULL ở cột thuộc bảng phụ.

**Phân tích trường hợp biên (Edge Cases):**
Lưu ý không đặt điều kiện lọc bảng phụ trong mệnh đề WHERE vì sẽ biến phép kết ngoài thành kết trong!

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 29 [RA-B29] — ĐSQH Kết Ngoài Left Outer Join (Bảo Toàn NULL) Kịch Bản 29
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THUCTHE_CHINH(MA_TC, TEN_TC, KHUVUC), THUCTHE_PHU(MA_TP, MA_TC, NGAY_PHATSINH, SOTIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết thông tin thực thể chính và các bản ghi phụ thuộc nếu có (kể cả chưa có phát sinh giao dịch) tại trường hợp 29.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_TC, TEN_TC, MA_TP, SOTIEN}(σ_{KHUVUC = 'KhuVuc_29'}(THUCTHE_CHINH ⟕ THUCTHE_PHU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TC.MA_TC, TC.TEN_TC, TP.MA_TP, TP.SOTIEN
FROM THUCTHE_CHINH TC
LEFT OUTER JOIN THUCTHE_PHU TP ON TC.MA_TC = TP.MA_TC
WHERE TC.KHUVUC = 'KhuVuc_29';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng phép kết trái (Left Outer Join) giữa thực thể chính và thực thể phụ.
1. Bước 2: Lọc theo khu vực quy định trên bảng chính.
1. Bước 3: Chiếu các cột cần thiết, các thực thể chính chưa có giao dịch sẽ mang giá trị NULL ở cột thuộc bảng phụ.

**Phân tích trường hợp biên (Edge Cases):**
Lưu ý không đặt điều kiện lọc bảng phụ trong mệnh đề WHERE vì sẽ biến phép kết ngoài thành kết trong!

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 30 [RA-B30] — ĐSQH Kết Ngoài Left Outer Join (Bảo Toàn NULL) Kịch Bản 30
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THUCTHE_CHINH(MA_TC, TEN_TC, KHUVUC), THUCTHE_PHU(MA_TP, MA_TC, NGAY_PHATSINH, SOTIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết thông tin thực thể chính và các bản ghi phụ thuộc nếu có (kể cả chưa có phát sinh giao dịch) tại trường hợp 30.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_TC, TEN_TC, MA_TP, SOTIEN}(σ_{KHUVUC = 'KhuVuc_30'}(THUCTHE_CHINH ⟕ THUCTHE_PHU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TC.MA_TC, TC.TEN_TC, TP.MA_TP, TP.SOTIEN
FROM THUCTHE_CHINH TC
LEFT OUTER JOIN THUCTHE_PHU TP ON TC.MA_TC = TP.MA_TC
WHERE TC.KHUVUC = 'KhuVuc_30';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng phép kết trái (Left Outer Join) giữa thực thể chính và thực thể phụ.
1. Bước 2: Lọc theo khu vực quy định trên bảng chính.
1. Bước 3: Chiếu các cột cần thiết, các thực thể chính chưa có giao dịch sẽ mang giá trị NULL ở cột thuộc bảng phụ.

**Phân tích trường hợp biên (Edge Cases):**
Lưu ý không đặt điều kiện lọc bảng phụ trong mệnh đề WHERE vì sẽ biến phép kết ngoài thành kết trong!

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 31 [RA-B31] — ĐSQH Kết Ngoài Left Outer Join (Bảo Toàn NULL) Kịch Bản 31
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THUCTHE_CHINH(MA_TC, TEN_TC, KHUVUC), THUCTHE_PHU(MA_TP, MA_TC, NGAY_PHATSINH, SOTIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết thông tin thực thể chính và các bản ghi phụ thuộc nếu có (kể cả chưa có phát sinh giao dịch) tại trường hợp 31.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_TC, TEN_TC, MA_TP, SOTIEN}(σ_{KHUVUC = 'KhuVuc_31'}(THUCTHE_CHINH ⟕ THUCTHE_PHU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TC.MA_TC, TC.TEN_TC, TP.MA_TP, TP.SOTIEN
FROM THUCTHE_CHINH TC
LEFT OUTER JOIN THUCTHE_PHU TP ON TC.MA_TC = TP.MA_TC
WHERE TC.KHUVUC = 'KhuVuc_31';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng phép kết trái (Left Outer Join) giữa thực thể chính và thực thể phụ.
1. Bước 2: Lọc theo khu vực quy định trên bảng chính.
1. Bước 3: Chiếu các cột cần thiết, các thực thể chính chưa có giao dịch sẽ mang giá trị NULL ở cột thuộc bảng phụ.

**Phân tích trường hợp biên (Edge Cases):**
Lưu ý không đặt điều kiện lọc bảng phụ trong mệnh đề WHERE vì sẽ biến phép kết ngoài thành kết trong!

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 32 [RA-B32] — ĐSQH Kết Ngoài Left Outer Join (Bảo Toàn NULL) Kịch Bản 32
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THUCTHE_CHINH(MA_TC, TEN_TC, KHUVUC), THUCTHE_PHU(MA_TP, MA_TC, NGAY_PHATSINH, SOTIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết thông tin thực thể chính và các bản ghi phụ thuộc nếu có (kể cả chưa có phát sinh giao dịch) tại trường hợp 32.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_TC, TEN_TC, MA_TP, SOTIEN}(σ_{KHUVUC = 'KhuVuc_32'}(THUCTHE_CHINH ⟕ THUCTHE_PHU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TC.MA_TC, TC.TEN_TC, TP.MA_TP, TP.SOTIEN
FROM THUCTHE_CHINH TC
LEFT OUTER JOIN THUCTHE_PHU TP ON TC.MA_TC = TP.MA_TC
WHERE TC.KHUVUC = 'KhuVuc_32';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng phép kết trái (Left Outer Join) giữa thực thể chính và thực thể phụ.
1. Bước 2: Lọc theo khu vực quy định trên bảng chính.
1. Bước 3: Chiếu các cột cần thiết, các thực thể chính chưa có giao dịch sẽ mang giá trị NULL ở cột thuộc bảng phụ.

**Phân tích trường hợp biên (Edge Cases):**
Lưu ý không đặt điều kiện lọc bảng phụ trong mệnh đề WHERE vì sẽ biến phép kết ngoài thành kết trong!

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 33 [RA-B33] — ĐSQH Kết Ngoài Left Outer Join (Bảo Toàn NULL) Kịch Bản 33
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THUCTHE_CHINH(MA_TC, TEN_TC, KHUVUC), THUCTHE_PHU(MA_TP, MA_TC, NGAY_PHATSINH, SOTIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết thông tin thực thể chính và các bản ghi phụ thuộc nếu có (kể cả chưa có phát sinh giao dịch) tại trường hợp 33.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_TC, TEN_TC, MA_TP, SOTIEN}(σ_{KHUVUC = 'KhuVuc_33'}(THUCTHE_CHINH ⟕ THUCTHE_PHU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TC.MA_TC, TC.TEN_TC, TP.MA_TP, TP.SOTIEN
FROM THUCTHE_CHINH TC
LEFT OUTER JOIN THUCTHE_PHU TP ON TC.MA_TC = TP.MA_TC
WHERE TC.KHUVUC = 'KhuVuc_33';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng phép kết trái (Left Outer Join) giữa thực thể chính và thực thể phụ.
1. Bước 2: Lọc theo khu vực quy định trên bảng chính.
1. Bước 3: Chiếu các cột cần thiết, các thực thể chính chưa có giao dịch sẽ mang giá trị NULL ở cột thuộc bảng phụ.

**Phân tích trường hợp biên (Edge Cases):**
Lưu ý không đặt điều kiện lọc bảng phụ trong mệnh đề WHERE vì sẽ biến phép kết ngoài thành kết trong!

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 34 [RA-B34] — ĐSQH Kết Ngoài Left Outer Join (Bảo Toàn NULL) Kịch Bản 34
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THUCTHE_CHINH(MA_TC, TEN_TC, KHUVUC), THUCTHE_PHU(MA_TP, MA_TC, NGAY_PHATSINH, SOTIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết thông tin thực thể chính và các bản ghi phụ thuộc nếu có (kể cả chưa có phát sinh giao dịch) tại trường hợp 34.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_TC, TEN_TC, MA_TP, SOTIEN}(σ_{KHUVUC = 'KhuVuc_34'}(THUCTHE_CHINH ⟕ THUCTHE_PHU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TC.MA_TC, TC.TEN_TC, TP.MA_TP, TP.SOTIEN
FROM THUCTHE_CHINH TC
LEFT OUTER JOIN THUCTHE_PHU TP ON TC.MA_TC = TP.MA_TC
WHERE TC.KHUVUC = 'KhuVuc_34';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng phép kết trái (Left Outer Join) giữa thực thể chính và thực thể phụ.
1. Bước 2: Lọc theo khu vực quy định trên bảng chính.
1. Bước 3: Chiếu các cột cần thiết, các thực thể chính chưa có giao dịch sẽ mang giá trị NULL ở cột thuộc bảng phụ.

**Phân tích trường hợp biên (Edge Cases):**
Lưu ý không đặt điều kiện lọc bảng phụ trong mệnh đề WHERE vì sẽ biến phép kết ngoài thành kết trong!

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 35 [RA-B35] — ĐSQH Kết Ngoài Left Outer Join (Bảo Toàn NULL) Kịch Bản 35
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THUCTHE_CHINH(MA_TC, TEN_TC, KHUVUC), THUCTHE_PHU(MA_TP, MA_TC, NGAY_PHATSINH, SOTIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết thông tin thực thể chính và các bản ghi phụ thuộc nếu có (kể cả chưa có phát sinh giao dịch) tại trường hợp 35.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_TC, TEN_TC, MA_TP, SOTIEN}(σ_{KHUVUC = 'KhuVuc_35'}(THUCTHE_CHINH ⟕ THUCTHE_PHU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TC.MA_TC, TC.TEN_TC, TP.MA_TP, TP.SOTIEN
FROM THUCTHE_CHINH TC
LEFT OUTER JOIN THUCTHE_PHU TP ON TC.MA_TC = TP.MA_TC
WHERE TC.KHUVUC = 'KhuVuc_35';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng phép kết trái (Left Outer Join) giữa thực thể chính và thực thể phụ.
1. Bước 2: Lọc theo khu vực quy định trên bảng chính.
1. Bước 3: Chiếu các cột cần thiết, các thực thể chính chưa có giao dịch sẽ mang giá trị NULL ở cột thuộc bảng phụ.

**Phân tích trường hợp biên (Edge Cases):**
Lưu ý không đặt điều kiện lọc bảng phụ trong mệnh đề WHERE vì sẽ biến phép kết ngoài thành kết trong!

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 36 [RA-B36] — ĐSQH Tự Kết Phân Cấp (Self-Join Đổi Tên) Kịch Bản 36
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHANVIEN(MANV, HOTEN, LUONG, MA_QL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các cặp bản ghi có mối quan hệ quản lý - cấp dưới hoặc phụ thuộc phân cấp tại tình huống 36.

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
1. Bước 1: Sử dụng phép đổi tên ρ để tạo hai thể hiện độc lập: NV (nhân viên) và QL (quản lý).
1. Bước 2: Tự kết hai thể hiện theo điều kiện NV.MA_QL = QL.MANV.
1. Bước 3: Chọn các cặp nhân viên có lương cao hơn lương của chính người quản lý trực tiếp.
1. Bước 4: Chiếu mã nhân viên, tên nhân viên và tên quản lý.

**Phân tích trường hợp biên (Edge Cases):**
Cần loại trừ các nhân viên là cấp cao nhất (MA_QL IS NULL) để tránh lỗi so sánh.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 37 [RA-B37] — ĐSQH Tự Kết Phân Cấp (Self-Join Đổi Tên) Kịch Bản 37
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHANVIEN(MANV, HOTEN, LUONG, MA_QL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các cặp bản ghi có mối quan hệ quản lý - cấp dưới hoặc phụ thuộc phân cấp tại tình huống 37.

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
1. Bước 1: Sử dụng phép đổi tên ρ để tạo hai thể hiện độc lập: NV (nhân viên) và QL (quản lý).
1. Bước 2: Tự kết hai thể hiện theo điều kiện NV.MA_QL = QL.MANV.
1. Bước 3: Chọn các cặp nhân viên có lương cao hơn lương của chính người quản lý trực tiếp.
1. Bước 4: Chiếu mã nhân viên, tên nhân viên và tên quản lý.

**Phân tích trường hợp biên (Edge Cases):**
Cần loại trừ các nhân viên là cấp cao nhất (MA_QL IS NULL) để tránh lỗi so sánh.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 38 [RA-B38] — ĐSQH Tự Kết Phân Cấp (Self-Join Đổi Tên) Kịch Bản 38
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHANVIEN(MANV, HOTEN, LUONG, MA_QL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các cặp bản ghi có mối quan hệ quản lý - cấp dưới hoặc phụ thuộc phân cấp tại tình huống 38.

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
1. Bước 1: Sử dụng phép đổi tên ρ để tạo hai thể hiện độc lập: NV (nhân viên) và QL (quản lý).
1. Bước 2: Tự kết hai thể hiện theo điều kiện NV.MA_QL = QL.MANV.
1. Bước 3: Chọn các cặp nhân viên có lương cao hơn lương của chính người quản lý trực tiếp.
1. Bước 4: Chiếu mã nhân viên, tên nhân viên và tên quản lý.

**Phân tích trường hợp biên (Edge Cases):**
Cần loại trừ các nhân viên là cấp cao nhất (MA_QL IS NULL) để tránh lỗi so sánh.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 39 [RA-B39] — ĐSQH Tự Kết Phân Cấp (Self-Join Đổi Tên) Kịch Bản 39
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHANVIEN(MANV, HOTEN, LUONG, MA_QL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các cặp bản ghi có mối quan hệ quản lý - cấp dưới hoặc phụ thuộc phân cấp tại tình huống 39.

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
1. Bước 1: Sử dụng phép đổi tên ρ để tạo hai thể hiện độc lập: NV (nhân viên) và QL (quản lý).
1. Bước 2: Tự kết hai thể hiện theo điều kiện NV.MA_QL = QL.MANV.
1. Bước 3: Chọn các cặp nhân viên có lương cao hơn lương của chính người quản lý trực tiếp.
1. Bước 4: Chiếu mã nhân viên, tên nhân viên và tên quản lý.

**Phân tích trường hợp biên (Edge Cases):**
Cần loại trừ các nhân viên là cấp cao nhất (MA_QL IS NULL) để tránh lỗi so sánh.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 40 [RA-B40] — ĐSQH Tự Kết Phân Cấp (Self-Join Đổi Tên) Kịch Bản 40
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHANVIEN(MANV, HOTEN, LUONG, MA_QL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các cặp bản ghi có mối quan hệ quản lý - cấp dưới hoặc phụ thuộc phân cấp tại tình huống 40.

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
1. Bước 1: Sử dụng phép đổi tên ρ để tạo hai thể hiện độc lập: NV (nhân viên) và QL (quản lý).
1. Bước 2: Tự kết hai thể hiện theo điều kiện NV.MA_QL = QL.MANV.
1. Bước 3: Chọn các cặp nhân viên có lương cao hơn lương của chính người quản lý trực tiếp.
1. Bước 4: Chiếu mã nhân viên, tên nhân viên và tên quản lý.

**Phân tích trường hợp biên (Edge Cases):**
Cần loại trừ các nhân viên là cấp cao nhất (MA_QL IS NULL) để tránh lỗi so sánh.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 41 [RA-B41] — ĐSQH Phép Toán Tập Hợp (Giao / Trừ Khả Hợp) Kịch Bản 41
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG_VIP(MAKH, HOTEN), KHACHHANG_MUA_HANG(MAKH, HOTEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đồng thời thỏa mãn cả hai tiêu chí hoặc thỏa mãn tiêu chí 1 nhưng chưa từng phát sinh tiêu chí 2 tại kịch bản 41.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAKH, HOTEN}(KHACHHANG_VIP) ∩ π_{MAKH, HOTEN}(KHACHHANG_MUA_HANG)
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MAKH, HOTEN FROM KHACHHANG_VIP
INTERSECT
SELECT MAKH, HOTEN FROM KHACHHANG_MUA_HANG;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kiểm tra tính khả hợp của hai quan hệ (cùng bậc 2 thuộc tính, cùng kiểu dữ liệu).
1. Bước 2: Áp dụng phép giao (∩) để tìm khách hàng vừa thuộc nhóm VIP vừa đã phát sinh mua hàng.

**Phân tích trường hợp biên (Edge Cases):**
Phép giao và trừ bắt buộc hai quan hệ tham gia phải có cùng tập thuộc tính hoặc chiếu về cùng danh sách thuộc tính khả hợp.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 42 [RA-B42] — ĐSQH Phép Toán Tập Hợp (Giao / Trừ Khả Hợp) Kịch Bản 42
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG_VIP(MAKH, HOTEN), KHACHHANG_MUA_HANG(MAKH, HOTEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đồng thời thỏa mãn cả hai tiêu chí hoặc thỏa mãn tiêu chí 1 nhưng chưa từng phát sinh tiêu chí 2 tại kịch bản 42.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAKH, HOTEN}(KHACHHANG_VIP) ∩ π_{MAKH, HOTEN}(KHACHHANG_MUA_HANG)
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MAKH, HOTEN FROM KHACHHANG_VIP
INTERSECT
SELECT MAKH, HOTEN FROM KHACHHANG_MUA_HANG;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kiểm tra tính khả hợp của hai quan hệ (cùng bậc 2 thuộc tính, cùng kiểu dữ liệu).
1. Bước 2: Áp dụng phép giao (∩) để tìm khách hàng vừa thuộc nhóm VIP vừa đã phát sinh mua hàng.

**Phân tích trường hợp biên (Edge Cases):**
Phép giao và trừ bắt buộc hai quan hệ tham gia phải có cùng tập thuộc tính hoặc chiếu về cùng danh sách thuộc tính khả hợp.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 43 [RA-B43] — ĐSQH Phép Toán Tập Hợp (Giao / Trừ Khả Hợp) Kịch Bản 43
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG_VIP(MAKH, HOTEN), KHACHHANG_MUA_HANG(MAKH, HOTEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đồng thời thỏa mãn cả hai tiêu chí hoặc thỏa mãn tiêu chí 1 nhưng chưa từng phát sinh tiêu chí 2 tại kịch bản 43.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAKH, HOTEN}(KHACHHANG_VIP) ∩ π_{MAKH, HOTEN}(KHACHHANG_MUA_HANG)
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MAKH, HOTEN FROM KHACHHANG_VIP
INTERSECT
SELECT MAKH, HOTEN FROM KHACHHANG_MUA_HANG;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kiểm tra tính khả hợp của hai quan hệ (cùng bậc 2 thuộc tính, cùng kiểu dữ liệu).
1. Bước 2: Áp dụng phép giao (∩) để tìm khách hàng vừa thuộc nhóm VIP vừa đã phát sinh mua hàng.

**Phân tích trường hợp biên (Edge Cases):**
Phép giao và trừ bắt buộc hai quan hệ tham gia phải có cùng tập thuộc tính hoặc chiếu về cùng danh sách thuộc tính khả hợp.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 44 [RA-B44] — ĐSQH Phép Toán Tập Hợp (Giao / Trừ Khả Hợp) Kịch Bản 44
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG_VIP(MAKH, HOTEN), KHACHHANG_MUA_HANG(MAKH, HOTEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đồng thời thỏa mãn cả hai tiêu chí hoặc thỏa mãn tiêu chí 1 nhưng chưa từng phát sinh tiêu chí 2 tại kịch bản 44.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAKH, HOTEN}(KHACHHANG_VIP) ∩ π_{MAKH, HOTEN}(KHACHHANG_MUA_HANG)
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MAKH, HOTEN FROM KHACHHANG_VIP
INTERSECT
SELECT MAKH, HOTEN FROM KHACHHANG_MUA_HANG;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kiểm tra tính khả hợp của hai quan hệ (cùng bậc 2 thuộc tính, cùng kiểu dữ liệu).
1. Bước 2: Áp dụng phép giao (∩) để tìm khách hàng vừa thuộc nhóm VIP vừa đã phát sinh mua hàng.

**Phân tích trường hợp biên (Edge Cases):**
Phép giao và trừ bắt buộc hai quan hệ tham gia phải có cùng tập thuộc tính hoặc chiếu về cùng danh sách thuộc tính khả hợp.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---

## Bài 45 [RA-B45] — ĐSQH Phép Toán Tập Hợp (Giao / Trừ Khả Hợp) Kịch Bản 45
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG_VIP(MAKH, HOTEN), KHACHHANG_MUA_HANG(MAKH, HOTEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đồng thời thỏa mãn cả hai tiêu chí hoặc thỏa mãn tiêu chí 1 nhưng chưa từng phát sinh tiêu chí 2 tại kịch bản 45.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAKH, HOTEN}(KHACHHANG_VIP) ∩ π_{MAKH, HOTEN}(KHACHHANG_MUA_HANG)
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MAKH, HOTEN FROM KHACHHANG_VIP
INTERSECT
SELECT MAKH, HOTEN FROM KHACHHANG_MUA_HANG;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kiểm tra tính khả hợp của hai quan hệ (cùng bậc 2 thuộc tính, cùng kiểu dữ liệu).
1. Bước 2: Áp dụng phép giao (∩) để tìm khách hàng vừa thuộc nhóm VIP vừa đã phát sinh mua hàng.

**Phân tích trường hợp biên (Edge Cases):**
Phép giao và trừ bắt buộc hai quan hệ tham gia phải có cùng tập thuộc tính hoặc chiếu về cùng danh sách thuộc tính khả hợp.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `selection_and_projection_correctness`: 0.4đ
- `join_condition_and_table_mapping`: 0.4đ
- `syntax_and_variable_naming`: 0.2đ

---
