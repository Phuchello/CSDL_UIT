# CHUYÊN ĐỀ 2: ĐẠI SỐ QUAN HỆ CƠ BẢN, PHÉP TẬP HỢP & CÁC LOẠI PHÉP KẾT
**Môn học:** IT004 — Cơ sở dữ liệu | **Hệ thống:** UIT Exam Mastery
**Biên soạn:** VÕ TRỌNG PHÚC | **Số lượng bài tập:** 62 bài

---

## Bài 01 [M01-Q2C1] — ĐSQH Lọc Lô Vắc-Xin Theo Tên Loại Và Năm Sản Xuất
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `LOVACXIN(MALO, TENLO, TENVACXIN, NGAYSX, HSD, SOLIEU, DONGIA, MANCC)`

### 1. Đề Bài
Liệt kê thông tin các lô vắc-xin (MALO, TENLO, SOLIEU, DONGIA) có tên loại vắc-xin là 'Pfizer-BioNTech' và được sản xuất trong năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R1 ← σ_{TENVACXIN = 'Pfizer-BioNTech' ∧ NGAYSX ≥ '01/01/2024' ∧ NGAYSX ≤ '31/12/2024'}(LOVACXIN)
KQ ← π_{MALO, TENLO, SOLIEU, DONGIA}(R1)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MALO, TENLO, SOLIEU, DONGIA
FROM LOVACXIN
WHERE TENVACXIN = 'Pfizer-BioNTech' AND YEAR(NGAYSX) = 2024;
```

**Các bước suy luận tư duy:**
1. Bước 1: Phép chọn σ trên quan hệ LOVACXIN với điều kiện TENVACXIN = 'Pfizer-BioNTech' và năm sản xuất 2024.
1. Bước 2: Phép chiếu π lấy đúng 4 thuộc tính yêu cầu: MALO, TENLO, SOLIEU, DONGIA.

**Barem chấm điểm đề xuất:**
- `selection_condition`: 0.50đ
- `projection_attributes`: 0.50đ

---

## Bài 02 [M01-Q2C2] — ĐSQH Kết Nối Điểm Tiêm Đã Tiếp Nhận Phiếu Xuất Ngày 15/10/2024
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DIEMTIEM(MADT, TENDT, DIACHI, QUAN, SUCCHUA), PHIEUXUAT(MAPX, NGAYXUAT, TRANGTHAI, MADT)`

### 1. Đề Bài
Cho biết danh sách các điểm tiêm (MADT, TENDT, QUAN) đã tiếp nhận (TRANGTHAI = 1) các phiếu xuất vắc-xin vào ngày '15/10/2024'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R1 ← σ_{NGAYXUAT = '15/10/2024' ∧ TRANGTHAI = 1}(PHIEUXUAT)
R2 ← DIEMTIEM ⋈ R1
KQ ← π_{MADT, TENDT, QUAN}(R2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT DISTINCT DT.MADT, DT.TENDT, DT.QUAN
FROM DIEMTIEM DT
INNER JOIN PHIEUXUAT PX ON DT.MADT = PX.MADT
WHERE PX.NGAYXUAT = '2024-10-15' AND PX.TRANGTHAI = 1;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc trên PHIEUXUAT với ngày xuất '15/10/2024' và TRANGTHAI = 1 (đã tiếp nhận).
1. Bước 2: Kết nối tự nhiên DIEMTIEM ⋈ R1 qua thuộc tính chung MADT.
1. Bước 3: Chiếu lấy MADT, TENDT, QUAN.

**Barem chấm điểm đề xuất:**
- `selection_with_trangthai`: 0.50đ
- `join_and_projection`: 0.50đ

---

## Bài 03 [M01-Q2C3] — ĐSQH Kết Ngoài Điểm Tiêm Quận Bình Thạnh Và Nhân Viên (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 7 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DIEMTIEM(MADT, TENDT, DIACHI, QUAN, SUCCHUA), NHANVIEN(MANV, HOTEN, CHUYENMON, SDT, MADT)`

### 1. Đề Bài
Liệt kê thông tin các điểm tiêm ở quận 'Bình Thạnh' (MADT, TENDT) và họ tên nhân viên y tế (HOTEN) đang công tác tại điểm tiêm đó nếu có.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R1 ← σ_{QUAN = 'Bình Thạnh'}(DIEMTIEM)
R2 ← R1 ⟕_{R1.MADT = NHANVIEN.MADT} NHANVIEN
KQ ← π_{MADT, TENDT, HOTEN}(R2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT DT.MADT, DT.TENDT, NV.HOTEN
FROM DIEMTIEM DT
LEFT OUTER JOIN NHANVIEN NV ON DT.MADT = NV.MADT
WHERE DT.QUAN = N'Bình Thạnh';
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc điểm tiêm ở quận Bình Thạnh thành R1.
1. Bước 2: Nhận diện từ khóa 'NẾU CÓ' -> Phải dùng Phép Kết Ngoài Trái (Left Outer Join ⟕) từ R1 sang NHANVIEN để không làm mất các điểm tiêm chưa có nhân viên công tác.
1. Bước 3: Chiếu lấy MADT, TENDT, HOTEN.

**Barem chấm điểm đề xuất:**
- `selection_condition`: 0.25đ
- `outer_join_recognition`: 0.50đ (Bắt buộc dùng ⟕)
- `projection`: 0.25đ

---

## Bài 04 [M02-Q2C1] — ĐSQH Lọc Thiết Bị PCCC Theo Loại Và Hạn Sử Dụng
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THIETBI_PCCC`

### 1. Đề Bài
Liệt kê danh sách các thiết bị PCCC (MATB, TENTB, VITRI_LAPDAT, HANSUDUNG) thuộc loại 'Bình chữa cháy bột' có hạn sử dụng (HANSUDUNG) trong năm 2025.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E1 ← σ_{LOAITB='Bình chữa cháy bột' ∧ HANSUDUNG ≥ '2025-01-01' ∧ HANSUDUNG ≤ '2025-12-31'}(THIETBI_PCCC)
KQ ← π_{MATB, TENTB, VITRI_LAPDAT, HANSUDUNG}(E1)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MATB, TENTB, VITRI_LAPDAT, HANSUDUNG FROM THIETBI_PCCC WHERE LOAITB = N'Bình chữa cháy bột' AND HANSUDUNG >= '2025-01-01' AND HANSUDUNG <= '2025-12-31';
```

**Các bước suy luận tư duy:**
1. Lọc thiết bị loại bình bột có HSD năm 2025
1. Chiếu các cột yêu cầu

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ
- `projection`: 0.25đ

---

## Bài 05 [M02-Q2C2] — ĐSQH Kết Nối Căn Hộ Ruby Tower Từ Tầng 10 Trở Lên
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CANHO, TANG, TOANHA`

### 1. Đề Bài
Cho biết danh sách các căn hộ (MACANHO, SOCANHO, DIENTICH) thuộc tòa nhà có tên 'Ruby Tower' và nằm ở các tầng có số thứ tự tầng (STTTANG) từ tầng 10 trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E_TN ← σ_{TENTN='Ruby Tower'}(TOANHA)
E_Tang ← σ_{STTTANG ≥ 10}(TANG)
KQ ← π_{MACANHO, SOCANHO, DIENTICH}(E_TN ⋈ E_Tang ⋈ CANHO)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT CH.MACANHO, CH.SOCANHO, CH.DIENTICH FROM CANHO CH JOIN TANG T ON CH.MATANG = T.MATANG JOIN TOANHA TN ON T.MATN = TN.MATN WHERE TN.TENTN = N'Ruby Tower' AND T.STTTANG >= 10;
```

**Các bước suy luận tư duy:**
1. Chọn tòa nhà Ruby Tower
1. Chọn tầng >= 10
1. Kết nối với căn hộ và chiếu

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ
- `projection`: 0.25đ

---

## Bài 06 [M02-Q2C3] — ĐSQH Kết Ngoài Tầng Tòa Nhà TN01 Và Thiết Bị PCCC (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TANG, THIETBI_PCCC`

### 1. Đề Bài
Liệt kê thông tin tất cả các tầng thuộc tòa nhà 'TN01' (MATANG, STTTANG) và danh sách các mã thiết bị PCCC (MATB), tên thiết bị (TENTB) được bố trí tại tầng đó nếu có.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E_Tang ← σ_{MATN='TN01'}(TANG)
KQ ← π_{MATANG, STTTANG, MATB, TENTB}(E_Tang ⟕ THIETBI_PCCC)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT T.MATANG, T.STTTANG, TB.MATB, TB.TENTB FROM TANG T LEFT OUTER JOIN THIETBI_PCCC TB ON T.MATANG = TB.MATANG WHERE T.MATN = 'TN01';
```

**Các bước suy luận tư duy:**
1. Chọn tầng thuộc tòa TN01
1. Kết ngoài trái với thiết bị PCCC

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ
- `projection`: 0.25đ

---

## Bài 07 [RA-B03] — ĐSQH Tự Kết Nối Phân Cấp Nhân Viên Và Người Quản Lý
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHANVIEN(MANV, HOTEN, PHAI, NGSINH, MA_NQL)`

### 1. Đề Bài
Cho lược đồ NHANVIEN(MANV, HOTEN, PHAI, NGSINH, MA_NQL). Liệt kê mã số và họ tên của nhân viên cùng họ tên của người quản lý trực tiếp của nhân viên đó.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
NV1 ← ρ_{NV}(NHANVIEN)
NV2 ← ρ_{QL}(NHANVIEN)
R ← NV1 ⋈_{NV.MA_NQL = QL.MANV} NV2
KQ ← π_{NV.MANV, NV.HOTEN, QL.HOTEN → TEN_QUANLY}(R)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT NV.MANV, NV.HOTEN, QL.HOTEN AS TEN_QUANLY
FROM NHANVIEN NV
INNER JOIN NHANVIEN QL ON NV.MA_NQL = QL.MANV;
```

**Các bước suy luận tư duy:**
1. Bước 1: Đổi tên hai bản sao của quan hệ NHANVIEN thành NV và QL để tránh xung đột thuộc tính.
1. Bước 2: Tự kết (Self-Join) qua điều kiện NV.MA_NQL = QL.MANV.
1. Bước 3: Chiếu lấy MANV, HOTEN của nhân viên và HOTEN của người quản lý.

**Barem chấm điểm đề xuất:**
- `rename_operation`: 0.50đ
- `self_join_and_projection`: 0.50đ

---

## Bài 08 [RA-B04] — ĐSQH Phép Giao Khách Hàng Mở Cả Hai Loại Tài Khoản
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 7 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG(MAKH, HOTEN), TAIKHOAN(SOTK, MAKH, MALTK), LOAITK(MALTK, TENLTK)`

### 1. Đề Bài
Cho CSDL Ngân hàng: Liệt kê khách hàng (MAKH, HOTEN) đã mở cả hai loại tài khoản: 'Tiết kiệm' và 'Thanh toán'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_TK ← π_{MAKH, HOTEN}(KHACHHANG ⋈ TAIKHOAN ⋈ σ_{TENLTK = 'Tiết kiệm'}(LOAITK))
R_TT ← π_{MAKH, HOTEN}(KHACHHANG ⋈ TAIKHOAN ⋈ σ_{TENLTK = 'Thanh toán'}(LOAITK))
KQ ← R_TK ∩ R_TT
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KH.MAKH, KH.HOTEN
FROM KHACHHANG KH
INNER JOIN TAIKHOAN TK ON KH.MAKH = TK.MAKH
INNER JOIN LOAITK LTK ON TK.MALTK = LTK.MALTK
WHERE LTK.TENLTK = N'Tiết kiệm'
INTERSECT
SELECT KH.MAKH, KH.HOTEN
FROM KHACHHANG KH
INNER JOIN TAIKHOAN TK ON KH.MAKH = TK.MAKH
INNER JOIN LOAITK LTK ON TK.MALTK = LTK.MALTK
WHERE LTK.TENLTK = N'Thanh toán';
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm danh sách khách hàng mở tài khoản Tiết kiệm.
1. Bước 2: Tìm danh sách khách hàng mở tài khoản Thanh toán.
1. Bước 3: Dùng phép giao ∩ giữa hai tập có cùng lược đồ thuộc tính (MAKH, HOTEN).

**Barem chấm điểm đề xuất:**
- `intersect_operands`: 0.50đ
- `set_intersection`: 0.50đ

---

## Bài 09 [M06-Q2C1] — ĐSQH Lọc Bệnh Nhân Nữ Thường Trú TP.HCM
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BENHNHAN(MABN, HOTEN, NGAYSINH, GIOITINH, DIACHI)`

### 1. Đề Bài
Liệt kê danh sách bệnh nhân (MABN, HOTEN, NGAYSINH, DIACHI) có giới tính Nữ và địa chỉ tại TP.HCM.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MABN, HOTEN, NGAYSINH, DIACHI}(\sigma_{GIOITINH = 'Nữ' \wedge DIACHI = 'TP.HCM'}(BENHNHAN))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MABN, HOTEN, NGAYSINH, DIACHI FROM BENHNHAN WHERE GIOITINH = N'Nữ' AND DIACHI = N'TP.HCM';
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{GIOITINH = 'Nữ' \wedge DIACHI = 'TP.HCM'}(BENHNHAN)
1. KQ = \pi_{MABN, HOTEN, NGAYSINH, DIACHI}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 10 [M06-Q2C2] — ĐSQH Kết Nối Phiếu Khám Của Chuyên Khoa Nhi Khoa
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEUKHAM(MAPK, NGAYKHAM, MABN, MABS, CHANDOAN), BACSI(MABS, HOTEN, HOCVI, MAKC, LUONG), CHUYENKHOA(MAKC, TENKHOA, TRUONGKHOA)`

### 1. Đề Bài
Cho biết danh sách phiếu khám (MAPK, NGAYKHAM, CHANDOAN, HOTEN) do bác sĩ thuộc chuyên khoa Nhi khoa thăm khám.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAPK, NGAYKHAM, CHANDOAN, HOTEN}(PHIEUKHAM \bowtie (BACSI \bowtie \sigma_{TENKHOA = 'Nhi khoa'}(CHUYENKHOA)))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT pk.MAPK, pk.NGAYKHAM, pk.CHANDOAN, bs.HOTEN FROM PHIEUKHAM pk JOIN BACSI bs ON pk.MABS = bs.MABS JOIN CHUYENKHOA ck ON bs.MAKC = ck.MAKC WHERE ck.TENKHOA = N'Nhi khoa';
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{TENKHOA = 'Nhi khoa'}(CHUYENKHOA)
1. E_2 = BACSI \bowtie E_1
1. E_3 = PHIEUKHAM \bowtie E_2
1. KQ = \pi_{MAPK, NGAYKHAM, CHANDOAN, HOTEN}(E_3)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 11 [M06-Q2C3] — ĐSQH Kết Ngoài Danh Sách Chuyên Khoa Và Bác Sĩ (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CHUYENKHOA(MAKC, TENKHOA, TRUONGKHOA), BACSI(MABS, HOTEN, HOCVI, MAKC, LUONG)`

### 1. Đề Bài
Liệt kê tất cả chuyên khoa (MAKC, TENKHOA) và thông tin bác sĩ (MABS, HOTEN) công tác tại chuyên khoa (nếu chưa có bác sĩ thì mang giá trị NULL).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAKC, TENKHOA, MABS, HOTEN}(CHUYENKHOA =\bowtie BACSI)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ck.MAKC, ck.TENKHOA, bs.MABS, bs.HOTEN FROM CHUYENKHOA ck LEFT JOIN BACSI bs ON ck.MAKC = bs.MAKC;
```

**Các bước suy luận tư duy:**
1. E_1 = CHUYENKHOA =\bowtie BACSI
1. KQ = \pi_{MAKC, TENKHOA, MABS, HOTEN}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 12 [M07-Q2C1] — ĐSQH Lọc Sinh Viên Thuộc Khoa Khoa Học Máy Tính
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DOCGIA(MADG, HOTEN, NGAYSINH, LOAIDG, MAKV), KHOAVIEN(MAKV, TENKV, NAMTL)`

### 1. Đề Bài
Liệt kê danh sách độc giả (MADG, HOTEN, NGAYSINH) có loại độc giả là Sinh viên và trực thuộc khoa viện Khoa học Máy tính.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MADG, HOTEN, NGAYSINH}(\sigma_{LOAIDG = 'Sinh viên' \wedge TENKV = 'Khoa học Máy tính'}(DOCGIA \bowtie KHOAVIEN))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT dg.MADG, dg.HOTEN, dg.NGAYSINH FROM DOCGIA dg JOIN KHOAVIEN kv ON dg.MAKV = kv.MAKV WHERE dg.LOAIDG = N'Sinh viên' AND kv.TENKV = N'Khoa học Máy tính';
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{LOAIDG = 'Sinh viên'}(DOCGIA)
1. E_2 = \sigma_{TENKV = 'Khoa học Máy tính'}(KHOAVIEN)
1. E_3 = E_1 \bowtie E_2
1. KQ = \pi_{MADG, HOTEN, NGAYSINH}(E_3)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 13 [M07-Q2C2] — ĐSQH Kết Nối Sách NXB Giáo Dục Được Mượn Bởi Độc Giả DG01
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEUMUON(MAPM, NGAYMUON, HANTRA, MADG, MATT, TRANGTHAI), CHITIET_MUON(MAPM, MASACH, NGAYTRA, TIENPHAT), SACH(MASACH, TENSACH, TACGIA, NXB, NAMXB, SOLUONGTON)`

### 1. Đề Bài
Cho biết danh sách các cuốn sách (MASACH, TENSACH, NXB) do NXB Giáo Dục ấn hành đã được mượn bởi độc giả có mã DG01.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MASACH, TENSACH, NXB}((\sigma_{MADG = 'DG01'}(PHIEUMUON) \bowtie CHITIET_MUON) \bowtie \sigma_{NXB = 'NXB Giáo Dục'}(SACH))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT s.MASACH, s.TENSACH, s.NXB FROM PHIEUMUON pm JOIN CHITIET_MUON ct ON pm.MAPM = ct.MAPM JOIN SACH s ON ct.MASACH = s.MASACH WHERE pm.MADG = 'DG01' AND s.NXB = N'NXB Giáo Dục';
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{MADG = 'DG01'}(PHIEUMUON)
1. E_2 = E_1 \bowtie CHITIET_MUON
1. E_3 = \sigma_{NXB = 'NXB Giáo Dục'}(SACH)
1. E_4 = E_2 \bowtie E_3
1. KQ = \pi_{MASACH, TENSACH, NXB}(E_4)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 14 [M07-Q2C3] — ĐSQH Kết Ngoài Danh Sách Khoa Viện Và Độc Giả (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHOAVIEN(MAKV, TENKV, NAMTL), DOCGIA(MADG, HOTEN, NGAYSINH, LOAIDG, MAKV)`

### 1. Đề Bài
Liệt kê thông tin tất cả các khoa viện (MAKV, TENKV) và danh sách độc giả (MADG, HOTEN) thuộc khoa viện (nếu chưa có độc giả nào thì mang giá trị NULL).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAKV, TENKV, MADG, HOTEN}(KHOAVIEN =\bowtie DOCGIA)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT kv.MAKV, kv.TENKV, dg.MADG, dg.HOTEN FROM KHOAVIEN kv LEFT JOIN DOCGIA dg ON kv.MAKV = dg.MAKV;
```

**Các bước suy luận tư duy:**
1. E_1 = KHOAVIEN =\bowtie DOCGIA
1. KQ = \pi_{MAKV, TENKV, MADG, HOTEN}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 15 [M08-Q2C1] — ĐSQH Lọc Sản Phẩm Điện Tử Giá Từ 10 Triệu
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SANPHAM(MASP, TENSP, LOAISP, GIANIEMYET, MAGH)`

### 1. Đề Bài
Liệt kê danh sách các sản phẩm (MASP, TENSP, GIANIEMYET) thuộc loại Điện tử có giá niêm yết từ 10.000.000 trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MASP, TENSP, GIANIEMYET}(\sigma_{LOAISP = 'Điện tử' \wedge GIANIEMYET \ge 10000000}(SANPHAM))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MASP, TENSP, GIANIEMYET FROM SANPHAM WHERE LOAISP = N'Điện tử' AND GIANIEMYET >= 10000000;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{LOAISP = 'Điện tử' \wedge GIANIEMYET \ge 10000000}(SANPHAM)
1. KQ = \pi_{MASP, TENSP, GIANIEMYET}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 16 [M08-Q2C2] — ĐSQH Kết Nối Đơn Hàng Khách Hà Nội Thanh Toán Ví Điện Tử
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONHANG(MADH, NGAYDAT, MAKH, HINHTHUCTT, TRANGTHAI), KHACHHANG(MAKH, HOTEN, DIACHI, HANGTHANHVIEN)`

### 1. Đề Bài
Cho biết danh sách các đơn hàng (MADH, NGAYDAT, HINHTHUCTT, HOTEN) của khách hàng tại Hà Nội thanh toán bằng Ví điện tử.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MADH, NGAYDAT, HINHTHUCTT, HOTEN}(\sigma_{HINHTHUCTT = 'Ví điện tử'}(DONHANG) \bowtie \sigma_{DIACHI = 'Hà Nội'}(KHACHHANG))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT dh.MADH, dh.NGAYDAT, dh.HINHTHUCTT, kh.HOTEN FROM DONHANG dh JOIN KHACHHANG kh ON dh.MAKH = kh.MAKH WHERE kh.DIACHI = N'Hà Nội' AND dh.HINHTHUCTT = N'Ví điện tử';
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{DIACHI = 'Hà Nội'}(KHACHHANG)
1. E_2 = \sigma_{HINHTHUCTT = 'Ví điện tử'}(DONHANG)
1. E_3 = E_1 \bowtie E_2
1. KQ = \pi_{MADH, NGAYDAT, HINHTHUCTT, HOTEN}(E_3)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 17 [M08-Q2C3] — ĐSQH Kết Ngoài Danh Sách Gian Hàng Và Sản Phẩm (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `GIANHANG(MAGH, TENGH, NGUOIDAIDIEN, THANHPHO), SANPHAM(MASP, TENSP, LOAISP, GIANIEMYET, MAGH)`

### 1. Đề Bài
Liệt kê thông tin tất cả các gian hàng (MAGH, TENGH) cùng danh mục sản phẩm (MASP, TENSP) (nếu chưa có sản phẩm nào thì mang giá trị NULL).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAGH, TENGH, MASP, TENSP}(GIANHANG =\bowtie SANPHAM)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT gh.MAGH, gh.TENGH, sp.MASP, sp.TENSP FROM GIANHANG gh LEFT JOIN SANPHAM sp ON gh.MAGH = sp.MAGH;
```

**Các bước suy luận tư duy:**
1. E_1 = GIANHANG =\bowtie SANPHAM
1. KQ = \pi_{MAGH, TENGH, MASP, TENSP}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 18 [M09-Q2C1] — ĐSQH Lọc Tuyển Thủ Xạ Thủ Thù Lao Từ 15 Triệu
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TUYENTHU(MATT, HOTEN, VITRI, MADOI, TIENLUONG)`

### 1. Đề Bài
Liệt kê danh sách các tuyển thủ (MATT, HOTEN, TIENLUONG) thi đấu vị trí Xạ thủ có thù lao từ 15.000.000 trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MATT, HOTEN, TIENLUONG}(\sigma_{VITRI = 'Xạ thủ' \wedge TIENLUONG \ge 15000000}(TUYENTHU))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MATT, HOTEN, TIENLUONG FROM TUYENTHU WHERE VITRI = N'Xạ thủ' AND TIENLUONG >= 15000000;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{VITRI = 'Xạ thủ' \wedge TIENLUONG \ge 15000000}(TUYENTHU)
1. KQ = \pi_{MATT, HOTEN, TIENLUONG}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 19 [M09-Q2C2] — ĐSQH Kết Nối Trận Đấu Có Đội UIT Hunters Tham Gia
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TRANDAU(MATRAN, NGAYDAU, VONGDAU, DIADIEM), THAMGIA_TRAN(MATRAN, MADOI, SOVANTHANG, TIENTHUONG, KETQUA), DOITHI(MADOI, TENDOI, MATRUONG, NGUOIQUANLY)`

### 1. Đề Bài
Cho biết danh sách các trận đấu (MATRAN, NGAYDAU, VONGDAU, TENDOI) có sự tham gia của đội UIT Hunters.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MATRAN, NGAYDAU, VONGDAU, TENDOI}((\sigma_{TENDOI = 'UIT Hunters'}(DOITHI) \bowtie THAMGIA_TRAN) \bowtie TRANDAU)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT td.MATRAN, td.NGAYDAU, td.VONGDAU, dt.TENDOI FROM TRANDAU td JOIN THAMGIA_TRAN tgt ON td.MATRAN = tgt.MATRAN JOIN DOITHI dt ON tgt.MADOI = dt.MADOI WHERE dt.TENDOI = N'UIT Hunters';
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{TENDOI = 'UIT Hunters'}(DOITHI)
1. E_2 = E_1 \bowtie THAMGIA_TRAN
1. E_3 = E_2 \bowtie TRANDAU
1. KQ = \pi_{MATRAN, NGAYDAU, VONGDAU, TENDOI}(E_3)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 20 [M09-Q2C3] — ĐSQH Kết Ngoài Danh Sách Trường Và Đội Tuyển (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TRUONG(MATRUONG, TENTRUONG, THANHPHO), DOITHI(MADOI, TENDOI, MATRUONG, NGUOIQUANLY)`

### 1. Đề Bài
Liệt kê thông tin tất cả các trường (MATRUONG, TENTRUONG) cùng danh sách đội thi (MADOI, TENDOI) (nếu chưa có đội nào thì mang giá trị NULL).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MATRUONG, TENTRUONG, MADOI, TENDOI}(TRUONG =\bowtie DOITHI)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT tr.MATRUONG, tr.TENTRUONG, dt.MADOI, dt.TENDOI FROM TRUONG tr LEFT JOIN DOITHI dt ON tr.MATRUONG = dt.MATRUONG;
```

**Các bước suy luận tư duy:**
1. E_1 = TRUONG =\bowtie DOITHI
1. KQ = \pi_{MATRUONG, TENTRUONG, MADOI, TENDOI}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 21 [M10-Q2C1] — ĐSQH Lọc Xe Toyota Sản Xuất Từ Năm 2022
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `XE(BIENSO, HANGXE, MODEL, NAMSX, MAKH)`

### 1. Đề Bài
Liệt kê danh sách các xe ô tô (BIENSO, HANGXE, MODEL, NAMSX) thuộc hãng Toyota có năm sản xuất từ năm 2022 trở lại đây.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{BIENSO, HANGXE, MODEL, NAMSX}(\sigma_{HANGXE = 'Toyota' \wedge NAMSX \ge 2022}(XE))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT BIENSO, HANGXE, MODEL, NAMSX FROM XE WHERE HANGXE = N'Toyota' AND NAMSX >= 2022;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{HANGXE = 'Toyota' \wedge NAMSX \ge 2022}(XE)
1. KQ = \pi_{BIENSO, HANGXE, MODEL, NAMSX}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 22 [M10-Q2C2] — ĐSQH Kết Nối Phiếu Bảo Dưỡng Do Thợ Trần Văn Mạnh Phụ Trách
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEU_BD(MAPHIEU, NGAYLAP, BIENSO, MATHO, TONGTIEN, TRANGTHAI), THO(MATHO, HOTEN, CHUYENMON, LUONG_CB)`

### 1. Đề Bài
Cho biết danh sách các phiếu bảo dưỡng (MAPHIEU, NGAYLAP, BIENSO, HOTEN) do thợ kỹ thuật Trần Văn Mạnh phụ trách.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAPHIEU, NGAYLAP, BIENSO, HOTEN}((\sigma_{HOTEN = 'Trần Văn Mạnh'}(THO)) \bowtie PHIEU_BD)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT pbd.MAPHIEU, pbd.NGAYLAP, pbd.BIENSO, t.HOTEN FROM PHIEU_BD pbd JOIN THO t ON pbd.MATHO = t.MATHO WHERE t.HOTEN = N'Trần Văn Mạnh';
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{HOTEN = 'Trần Văn Mạnh'}(THO)
1. E_2 = E_1 \bowtie PHIEU_BD
1. KQ = \pi_{MAPHIEU, NGAYLAP, BIENSO, HOTEN}(E_2)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 23 [M10-Q2C3] — ĐSQH Kết Ngoài Danh Sách Khách Hàng Và Xe Ô Tô (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG(MAKH, HOTEN, DIENTHOAI, DIACHI), XE(BIENSO, HANGXE, MODEL, NAMSX, MAKH)`

### 1. Đề Bài
Liệt kê thông tin tất cả khách hàng (MAKH, HOTEN) cùng danh sách xe (BIENSO, HANGXE) (nếu chưa có xe nào thì mang giá trị NULL).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAKH, HOTEN, BIENSO, HANGXE}(KHACHHANG =\bowtie XE)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT kh.MAKH, kh.HOTEN, x.BIENSO, x.HANGXE FROM KHACHHANG kh LEFT JOIN XE x ON kh.MAKH = x.MAKH;
```

**Các bước suy luận tư duy:**
1. E_1 = KHACHHANG =\bowtie XE
1. KQ = \pi_{MAKH, HOTEN, BIENSO, HANGXE}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 24 [RA-B01] — ĐSQH Lọc Đơn Lô Vắc-Xin Theo Hạn Sử Dụng
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `LOVACXIN(MALO, TENLO, HSD)`

### 1. Đề Bài
Liệt kê các lô vắc-xin (MALO, TENLO) có hạn sử dụng sau ngày '31/12/2025'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
π_{MALO, TENLO}(σ_{HSD > '31/12/2025'}(LOVACXIN))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MALO, TENLO FROM LOVACXIN WHERE HSD > '2025-12-31';
```

**Các bước suy luận tư duy:**
1. Xác định quan hệ tham gia
1. Áp dụng phép chọn/chiếu/kết
1. Chiếu thuộc tính đầu ra.

**Barem chấm điểm đề xuất:**
- `ra_logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 25 [M11-Q2C1] — ĐSQH Lọc Nguyên Liệu Hạt Cà Phê Có Đơn Giá Từ 200.000 Đ
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NGUYENLIEU(MANL, TENNL, LOAINL, DONGIA_CHUAN, DVT)`

### 1. Đề Bài
Liệt kê danh sách các nguyên liệu (MANL, TENNL, DONGIA_CHUAN, DVT) thuộc phân loại 'Hạt cà phê' có đơn giá chuẩn từ 200.000 VNĐ trở lên (>= 200000).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MANL, TENNL, DONGIA_CHUAN, DVT}(\sigma_{LOAINL = 'Hạt cà phê' \wedge DONGIA_CHUAN \ge 200000}(NGUYENLIEU))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MANL, TENNL, DONGIA_CHUAN, DVT FROM NGUYENLIEU WHERE LOAINL = N'Hạt cà phê' AND DONGIA_CHUAN >= 200000;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{LOAINL = 'Hạt cà phê' \wedge DONGIA_CHUAN \ge 200000}(NGUYENLIEU)
1. KQ = \pi_{MANL, TENNL, DONGIA_CHUAN, DVT}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 26 [RA-B34] — ĐSQH Phép Tập Hợp Giao/Trừ: Xe Máy & Bảo Dưỡng (Bài 34)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `XEMAY(MAXE, BIENSO, DONGXE), BAODUONG(MABD, MAXE, NGAYBD, CHIPHI)`

### 1. Đề Bài
Cho lược đồ XEMAY(MAXE, BIENSO, DONGXE), BAODUONG(MABD, MAXE, NGAYBD, CHIPHI). Tìm các đối tượng thỏa mãn điều kiện A nhưng không thỏa điều kiện B.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{ID}(σ_{A}(R)) - π_{ID}(σ_{B}(R))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID FROM R WHERE A EXCEPT SELECT ID FROM R WHERE B;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 27 [RA-B35] — ĐSQH Lọc & Chiếu: Hóa Đơn & Nhân Viên (Bài 35)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHANVIEN(MANV, HOTEN, CHUCVU), HOADON(MAHD, MANV, NGAYLAP)`

### 1. Đề Bài
Cho lược đồ NHANVIEN(MANV, HOTEN, CHUCVU), HOADON(MAHD, MANV, NGAYLAP). Viết biểu thức ĐSQH liệt kê danh sách hóa đơn do nhân viên chức vụ 'Thu ngân' lập.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{ID, TEN}(σ_{DIEUKIEN}(HóaĐơn))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID, TEN FROM HóaĐơn WHERE DIEUKIEN;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 28 [RA-B36] — ĐSQH Kết Nối Đa Bảng: Căn Hộ & Tòa Nhà (Bài 36)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TOANHA(MATOA, TENTOA, VITRI), CANHO(MACH, MATOA, DIENTICH, GIATHUE)`

### 1. Đề Bài
Cho lược đồ TOANHA(MATOA, TENTOA, VITRI), CANHO(MACH, MATOA, DIENTICH, GIATHUE). Viết biểu thức ĐSQH kết nối các quan hệ để tìm thông tin căn hộ diện tích > 80m2 tại tòa nhà 'Landmark'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(R1 ⋈ R2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R1 JOIN R2 ON R1.KEY = R2.KEY WHERE DIEUKIEN;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 29 [RA-B37] — ĐSQH Kết Ngoài Left Outer Join (Nếu Có): Khoa & Sinh Viên (Bài 37)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SINHVIEN(MASV, HOTEN, PHAI, MAKHOA), KHOA(MAKHOA, TENKHOA)`

### 1. Đề Bài
Cho lược đồ SINHVIEN(MASV, HOTEN, PHAI, MAKHOA), KHOA(MAKHOA, TENKHOA). Liệt kê danh sách các đối tượng và thông tin liên quan nếu có.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(R1 ⟕ R2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R1 LEFT OUTER JOIN R2 ON R1.KEY = R2.KEY;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 30 [RA-B38] — ĐSQH Tự Kết Phân Cấp: Đơn Hàng & Khách (Bài 38)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG(MAKH, HOTEN, DIACHI), DONHANG(MADH, MAKH, NGAYDH, TRIGIA)`

### 1. Đề Bài
Cho lược đồ KHACHHANG(MAKH, HOTEN, DIACHI), DONHANG(MADH, MAKH, NGAYDH, TRIGIA). Viết biểu thức ĐSQH tự kết (Self-Join) tìm đối tượng cùng nhóm.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(ρ_{A}(R) ⋈ ρ_{B}(R))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R A JOIN R B ON A.PID = B.ID;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 31 [RA-B39] — ĐSQH Phép Tập Hợp Giao/Trừ: Sách & Tác Giả (Bài 39)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SACH(MASACH, TENSACH, MATG, NXB), TACGIA(MATG, TENTG, QUOCTICH)`

### 1. Đề Bài
Cho lược đồ SACH(MASACH, TENSACH, MATG, NXB), TACGIA(MATG, TENTG, QUOCTICH). Tìm các đối tượng thỏa mãn điều kiện A nhưng không thỏa điều kiện B.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{ID}(σ_{A}(R)) - π_{ID}(σ_{B}(R))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID FROM R WHERE A EXCEPT SELECT ID FROM R WHERE B;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 32 [RA-B40] — ĐSQH Lọc & Chiếu: Chuyến Bay & Phi Công (Bài 40)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CHUYENBAY(MACB, SOHIEU, GIOBAY, NOIDI, NOIDEN), PHICONG(MAPC, HOTEN, MACB)`

### 1. Đề Bài
Cho lược đồ CHUYENBAY(MACB, SOHIEU, GIOBAY, NOIDI, NOIDEN), PHICONG(MAPC, HOTEN, MACB). Viết biểu thức ĐSQH liệt kê danh sách chuyến bay xuất phát từ 'SGN' đến 'HAN'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{ID, TEN}(σ_{DIEUKIEN}(ChuyếnBay))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID, TEN FROM ChuyếnBay WHERE DIEUKIEN;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 33 [RA-B41] — ĐSQH Kết Nối Đa Bảng: Phòng Khám & Bác Sĩ (Bài 41)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BACSI(MABS, HOTEN, CHUYENKHOA), PHONGKHAM(MAPK, TENPK, MABS_TRUONG)`

### 1. Đề Bài
Cho lược đồ BACSI(MABS, HOTEN, CHUYENKHOA), PHONGKHAM(MAPK, TENPK, MABS_TRUONG). Viết biểu thức ĐSQH kết nối các quan hệ để tìm thông tin bác sĩ chuyên khoa 'Tai-Mũi-Họng'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(R1 ⋈ R2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R1 JOIN R2 ON R1.KEY = R2.KEY WHERE DIEUKIEN;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 34 [RA-B42] — ĐSQH Kết Ngoài Left Outer Join (Nếu Có): Tài Khoản & Giao Dịch (Bài 42)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TAIKHOAN(SOTK, MAKH, SODU), GIAODICH(MAGD, SOTK, SOTIEN, NGAYGD)`

### 1. Đề Bài
Cho lược đồ TAIKHOAN(SOTK, MAKH, SODU), GIAODICH(MAGD, SOTK, SOTIEN, NGAYGD). Liệt kê danh sách các đối tượng và thông tin liên quan nếu có.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(R1 ⟕ R2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R1 LEFT OUTER JOIN R2 ON R1.KEY = R2.KEY;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 35 [RA-B43] — ĐSQH Tự Kết Phân Cấp: Lớp Học & Môn Học (Bài 43)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `MONHOC(MAMH, TENMH, SOTC), LOPHOC(MALOP, MAMH, HOCKY, NAM)`

### 1. Đề Bài
Cho lược đồ MONHOC(MAMH, TENMH, SOTC), LOPHOC(MALOP, MAMH, HOCKY, NAM). Viết biểu thức ĐSQH tự kết (Self-Join) tìm đối tượng cùng nhóm.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(ρ_{A}(R) ⋈ ρ_{B}(R))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R A JOIN R B ON A.PID = B.ID;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 36 [RA-B44] — ĐSQH Phép Tập Hợp Giao/Trừ: Xe Máy & Bảo Dưỡng (Bài 44)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `XEMAY(MAXE, BIENSO, DONGXE), BAODUONG(MABD, MAXE, NGAYBD, CHIPHI)`

### 1. Đề Bài
Cho lược đồ XEMAY(MAXE, BIENSO, DONGXE), BAODUONG(MABD, MAXE, NGAYBD, CHIPHI). Tìm các đối tượng thỏa mãn điều kiện A nhưng không thỏa điều kiện B.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{ID}(σ_{A}(R)) - π_{ID}(σ_{B}(R))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID FROM R WHERE A EXCEPT SELECT ID FROM R WHERE B;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 37 [RA-B45] — ĐSQH Lọc & Chiếu: Hóa Đơn & Nhân Viên (Bài 45)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHANVIEN(MANV, HOTEN, CHUCVU), HOADON(MAHD, MANV, NGAYLAP)`

### 1. Đề Bài
Cho lược đồ NHANVIEN(MANV, HOTEN, CHUCVU), HOADON(MAHD, MANV, NGAYLAP). Viết biểu thức ĐSQH liệt kê danh sách hóa đơn do nhân viên chức vụ 'Thu ngân' lập.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{ID, TEN}(σ_{DIEUKIEN}(HóaĐơn))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID, TEN FROM HóaĐơn WHERE DIEUKIEN;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 38 [RA-B46] — ĐSQH Kết Nối Đa Bảng: Căn Hộ & Tòa Nhà (Bài 46)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TOANHA(MATOA, TENTOA, VITRI), CANHO(MACH, MATOA, DIENTICH, GIATHUE)`

### 1. Đề Bài
Cho lược đồ TOANHA(MATOA, TENTOA, VITRI), CANHO(MACH, MATOA, DIENTICH, GIATHUE). Viết biểu thức ĐSQH kết nối các quan hệ để tìm thông tin căn hộ diện tích > 80m2 tại tòa nhà 'Landmark'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(R1 ⋈ R2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R1 JOIN R2 ON R1.KEY = R2.KEY WHERE DIEUKIEN;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 39 [RA-B47] — ĐSQH Kết Ngoài Left Outer Join (Nếu Có): Khoa & Sinh Viên (Bài 47)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SINHVIEN(MASV, HOTEN, PHAI, MAKHOA), KHOA(MAKHOA, TENKHOA)`

### 1. Đề Bài
Cho lược đồ SINHVIEN(MASV, HOTEN, PHAI, MAKHOA), KHOA(MAKHOA, TENKHOA). Liệt kê danh sách các đối tượng và thông tin liên quan nếu có.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(R1 ⟕ R2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R1 LEFT OUTER JOIN R2 ON R1.KEY = R2.KEY;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 40 [RA-B48] — ĐSQH Tự Kết Phân Cấp: Đơn Hàng & Khách (Bài 48)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG(MAKH, HOTEN, DIACHI), DONHANG(MADH, MAKH, NGAYDH, TRIGIA)`

### 1. Đề Bài
Cho lược đồ KHACHHANG(MAKH, HOTEN, DIACHI), DONHANG(MADH, MAKH, NGAYDH, TRIGIA). Viết biểu thức ĐSQH tự kết (Self-Join) tìm đối tượng cùng nhóm.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(ρ_{A}(R) ⋈ ρ_{B}(R))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R A JOIN R B ON A.PID = B.ID;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 41 [RA-B49] — ĐSQH Phép Tập Hợp Giao/Trừ: Sách & Tác Giả (Bài 49)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SACH(MASACH, TENSACH, MATG, NXB), TACGIA(MATG, TENTG, QUOCTICH)`

### 1. Đề Bài
Cho lược đồ SACH(MASACH, TENSACH, MATG, NXB), TACGIA(MATG, TENTG, QUOCTICH). Tìm các đối tượng thỏa mãn điều kiện A nhưng không thỏa điều kiện B.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{ID}(σ_{A}(R)) - π_{ID}(σ_{B}(R))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID FROM R WHERE A EXCEPT SELECT ID FROM R WHERE B;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 42 [RA-B50] — ĐSQH Lọc & Chiếu: Chuyến Bay & Phi Công (Bài 50)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CHUYENBAY(MACB, SOHIEU, GIOBAY, NOIDI, NOIDEN), PHICONG(MAPC, HOTEN, MACB)`

### 1. Đề Bài
Cho lược đồ CHUYENBAY(MACB, SOHIEU, GIOBAY, NOIDI, NOIDEN), PHICONG(MAPC, HOTEN, MACB). Viết biểu thức ĐSQH liệt kê danh sách chuyến bay xuất phát từ 'SGN' đến 'HAN'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{ID, TEN}(σ_{DIEUKIEN}(ChuyếnBay))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID, TEN FROM ChuyếnBay WHERE DIEUKIEN;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 43 [RA-B51] — ĐSQH Kết Nối Đa Bảng: Phòng Khám & Bác Sĩ (Bài 51)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BACSI(MABS, HOTEN, CHUYENKHOA), PHONGKHAM(MAPK, TENPK, MABS_TRUONG)`

### 1. Đề Bài
Cho lược đồ BACSI(MABS, HOTEN, CHUYENKHOA), PHONGKHAM(MAPK, TENPK, MABS_TRUONG). Viết biểu thức ĐSQH kết nối các quan hệ để tìm thông tin bác sĩ chuyên khoa 'Tai-Mũi-Họng'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(R1 ⋈ R2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R1 JOIN R2 ON R1.KEY = R2.KEY WHERE DIEUKIEN;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 44 [RA-B52] — ĐSQH Kết Ngoài Left Outer Join (Nếu Có): Tài Khoản & Giao Dịch (Bài 52)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TAIKHOAN(SOTK, MAKH, SODU), GIAODICH(MAGD, SOTK, SOTIEN, NGAYGD)`

### 1. Đề Bài
Cho lược đồ TAIKHOAN(SOTK, MAKH, SODU), GIAODICH(MAGD, SOTK, SOTIEN, NGAYGD). Liệt kê danh sách các đối tượng và thông tin liên quan nếu có.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(R1 ⟕ R2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R1 LEFT OUTER JOIN R2 ON R1.KEY = R2.KEY;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 45 [RA-B53] — ĐSQH Tự Kết Phân Cấp: Lớp Học & Môn Học (Bài 53)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `MONHOC(MAMH, TENMH, SOTC), LOPHOC(MALOP, MAMH, HOCKY, NAM)`

### 1. Đề Bài
Cho lược đồ MONHOC(MAMH, TENMH, SOTC), LOPHOC(MALOP, MAMH, HOCKY, NAM). Viết biểu thức ĐSQH tự kết (Self-Join) tìm đối tượng cùng nhóm.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(ρ_{A}(R) ⋈ ρ_{B}(R))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R A JOIN R B ON A.PID = B.ID;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 46 [RA-B54] — ĐSQH Phép Tập Hợp Giao/Trừ: Xe Máy & Bảo Dưỡng (Bài 54)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `XEMAY(MAXE, BIENSO, DONGXE), BAODUONG(MABD, MAXE, NGAYBD, CHIPHI)`

### 1. Đề Bài
Cho lược đồ XEMAY(MAXE, BIENSO, DONGXE), BAODUONG(MABD, MAXE, NGAYBD, CHIPHI). Tìm các đối tượng thỏa mãn điều kiện A nhưng không thỏa điều kiện B.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{ID}(σ_{A}(R)) - π_{ID}(σ_{B}(R))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID FROM R WHERE A EXCEPT SELECT ID FROM R WHERE B;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 47 [RA-B55] — ĐSQH Lọc & Chiếu: Hóa Đơn & Nhân Viên (Bài 55)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHANVIEN(MANV, HOTEN, CHUCVU), HOADON(MAHD, MANV, NGAYLAP)`

### 1. Đề Bài
Cho lược đồ NHANVIEN(MANV, HOTEN, CHUCVU), HOADON(MAHD, MANV, NGAYLAP). Viết biểu thức ĐSQH liệt kê danh sách hóa đơn do nhân viên chức vụ 'Thu ngân' lập.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{ID, TEN}(σ_{DIEUKIEN}(HóaĐơn))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID, TEN FROM HóaĐơn WHERE DIEUKIEN;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 48 [RA-B56] — ĐSQH Kết Nối Đa Bảng: Căn Hộ & Tòa Nhà (Bài 56)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TOANHA(MATOA, TENTOA, VITRI), CANHO(MACH, MATOA, DIENTICH, GIATHUE)`

### 1. Đề Bài
Cho lược đồ TOANHA(MATOA, TENTOA, VITRI), CANHO(MACH, MATOA, DIENTICH, GIATHUE). Viết biểu thức ĐSQH kết nối các quan hệ để tìm thông tin căn hộ diện tích > 80m2 tại tòa nhà 'Landmark'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(R1 ⋈ R2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R1 JOIN R2 ON R1.KEY = R2.KEY WHERE DIEUKIEN;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 49 [RA-B57] — ĐSQH Kết Ngoài Left Outer Join (Nếu Có): Khoa & Sinh Viên (Bài 57)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SINHVIEN(MASV, HOTEN, PHAI, MAKHOA), KHOA(MAKHOA, TENKHOA)`

### 1. Đề Bài
Cho lược đồ SINHVIEN(MASV, HOTEN, PHAI, MAKHOA), KHOA(MAKHOA, TENKHOA). Liệt kê danh sách các đối tượng và thông tin liên quan nếu có.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(R1 ⟕ R2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R1 LEFT OUTER JOIN R2 ON R1.KEY = R2.KEY;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 50 [RA-B58] — ĐSQH Tự Kết Phân Cấp: Đơn Hàng & Khách (Bài 58)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG(MAKH, HOTEN, DIACHI), DONHANG(MADH, MAKH, NGAYDH, TRIGIA)`

### 1. Đề Bài
Cho lược đồ KHACHHANG(MAKH, HOTEN, DIACHI), DONHANG(MADH, MAKH, NGAYDH, TRIGIA). Viết biểu thức ĐSQH tự kết (Self-Join) tìm đối tượng cùng nhóm.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{THUOCTINH}(ρ_{A}(R) ⋈ ρ_{B}(R))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT * FROM R A JOIN R B ON A.PID = B.ID;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 51 [RA-B59] — ĐSQH Phép Tập Hợp Giao/Trừ: Sách & Tác Giả (Bài 59)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SACH(MASACH, TENSACH, MATG, NXB), TACGIA(MATG, TENTG, QUOCTICH)`

### 1. Đề Bài
Cho lược đồ SACH(MASACH, TENSACH, MATG, NXB), TACGIA(MATG, TENTG, QUOCTICH). Tìm các đối tượng thỏa mãn điều kiện A nhưng không thỏa điều kiện B.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{ID}(σ_{A}(R)) - π_{ID}(σ_{B}(R))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID FROM R WHERE A EXCEPT SELECT ID FROM R WHERE B;
```

**Các bước suy luận tư duy:**
1. Xác định tập quan hệ
1. Phép toán đại số quan hệ
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic`: 0.60đ
- `syntax`: 0.40đ

---

## Bài 52 [M11-Q2C2] — ĐSQH Kết Nối Phiếu Xuất Cho Cửa Hàng The Coffee House Landmark 81
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CUAHANG(MACH, TENCH, DIACHI, MAKV, NAM_KYHD), PHIEUXUAT(MAPX, NGAYXUAT, MACH, TONGTIEN, TRANGTHAI)`

### 1. Đề Bài
Cho biết danh sách các phiếu xuất kho (MAPX, NGAYXUAT, TONGTIEN, TENCH) xuất cho cửa hàng mang tên 'The Coffee House Landmark 81'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAPX, NGAYXUAT, TONGTIEN, TENCH}(\sigma_{TENCH = 'The Coffee House Landmark 81'}(CUAHANG) \bowtie PHIEUXUAT)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT px.MAPX, px.NGAYXUAT, px.TONGTIEN, ch.TENCH FROM PHIEUXUAT px JOIN CUAHANG ch ON px.MACH = ch.MACH WHERE ch.TENCH = N'The Coffee House Landmark 81';
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{TENCH = 'The Coffee House Landmark 81'}(CUAHANG)
1. E_2 = E_1 \bowtie PHIEUXUAT
1. KQ = \pi_{MAPX, NGAYXUAT, TONGTIEN, TENCH}(E_2)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 53 [M11-Q2C3] — ĐSQH Kết Ngoài Danh Sách Khu Vực Và Cửa Hàng (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHUVUC(MAKV, TENKV, TRUONGVUNG), CUAHANG(MACH, TENCH, DIACHI, MAKV, NAM_KYHD)`

### 1. Đề Bài
Liệt kê thông tin tất cả các khu vực (MAKV, TENKV) cùng danh sách mã cửa hàng (MACH), tên cửa hàng (TENCH) trực thuộc khu vực đó (nếu khu vực chưa có cửa hàng thì mang giá trị NULL).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAKV, TENKV, MACH, TENCH}(KHUVUC =\bowtie CUAHANG)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT kv.MAKV, kv.TENKV, ch.MACH, ch.TENCH FROM KHUVUC kv LEFT JOIN CUAHANG ch ON kv.MAKV = ch.MAKV;
```

**Các bước suy luận tư duy:**
1. E_1 = KHUVUC =\bowtie CUAHANG
1. KQ = \pi_{MAKV, TENKV, MACH, TENCH}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 54 [M03-Q2C1] — ĐSQH Lọc Nhà Hảo Tâm Theo Loại Hình Cá Nhân
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHA_HAOTAM`

### 1. Đề Bài
Liệt kê danh sách các nhà hảo tâm (MANHT, TENNHT, SDT) thuộc loại hình 'Cá nhân'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E1 ← σ_{LOAIHINH='Cá nhân'}(NHA_HAOTAM)
KQ ← π_{MANHT, TENNHT, SDT}(E1)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MANHT, TENNHT, SDT FROM NHA_HAOTAM WHERE LOAIHINH = N'Cá nhân';
```

**Các bước suy luận tư duy:**
1. Lọc nhà hảo tâm có loại hình 'Cá nhân'
1. Chiếu các thuộc tính MANHT, TENNHT, SDT

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ
- `projection`: 0.25đ

---

## Bài 55 [M03-Q2C2] — ĐSQH Kết Nối Hộ Dân Cần Giờ Thiệt Hại Nặng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `XA, HO_DAN`

### 1. Đề Bài
Cho biết danh sách các hộ dân (MAHO, CHUHO, SONKHAU) thuộc huyện 'Cần Giờ' có mức độ thiệt hại là 'Nặng'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E_Xa ← σ_{HUYEN='Cần Giờ'}(XA)
E_Ho ← σ_{MUCDO_THIETHAI='Nặng'}(HO_DAN)
KQ ← π_{MAHO, CHUHO, SONKHAU}(E_Xa ⋈ E_Ho)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT HD.MAHO, HD.CHUHO, HD.SONKHAU FROM HO_DAN HD INNER JOIN XA X ON HD.MAXA = X.MAXA WHERE X.HUYEN = N'Cần Giờ' AND HD.MUCDO_THIETHAI = N'Nặng';
```

**Các bước suy luận tư duy:**
1. Lọc xã thuộc huyện Cần Giờ
1. Lọc hộ dân thiệt hại Nặng
1. Kết tự nhiên trên MAXA và chiếu kết quả

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `projection`: 0.30đ

---

## Bài 56 [M03-Q2C3] — ĐSQH Kết Ngoài Xã Thuộc Huyện Cần Giờ Và Hộ Dân (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `XA, HO_DAN`

### 1. Đề Bài
Liệt kê thông tin tất cả các xã thuộc huyện 'Cần Giờ' (MAXA, TENXA) và danh sách các mã hộ dân (MAHO), tên chủ hộ (CHUHO) trực thuộc xã đó nếu có.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E_XaCG ← σ_{HUYEN='Cần Giờ'}(XA)
KQ ← π_{MAXA, TENXA, MAHO, CHUHO}(E_XaCG ⟕ HO_DAN)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT X.MAXA, X.TENXA, HD.MAHO, HD.CHUHO FROM XA X LEFT OUTER JOIN HO_DAN HD ON X.MAXA = HD.MAXA WHERE X.HUYEN = N'Cần Giờ';
```

**Các bước suy luận tư duy:**
1. Lọc các xã thuộc huyện Cần Giờ
1. Kết ngoài trái với HO_DAN để bảo tồn xã chưa có hộ dân
1. Chiếu các cột yêu cầu

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `projection`: 0.30đ

---

## Bài 57 [M04-Q2C1] — ĐSQH Lọc Nhân Viên Bán Hàng Có Lương Từ 8 Triệu
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHANVIEN`

### 1. Đề Bài
Liệt kê danh sách các nhân viên (MANV, HOTEN, NGAYSINH, LUONG) có chức vụ là 'Nhân viên bán hàng' và có mức lương cơ bản từ 8,000,000 đồng trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E1 ← σ_{CHUCVU='Nhân viên bán hàng' ∧ LUONG ≥ 8000000}(NHANVIEN)
KQ ← π_{MANV, HOTEN, NGAYSINH, LUONG}(E1)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MANV, HOTEN, NGAYSINH, LUONG FROM NHANVIEN WHERE CHUCVU = N'Nhân viên bán hàng' AND LUONG >= 8000000;
```

**Các bước suy luận tư duy:**
1. Lọc nhân viên có chức vụ Nhân viên bán hàng và lương >= 8,000,000
1. Chiếu các thuộc tính MANV, HOTEN, NGAYSINH, LUONG

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ
- `projection`: 0.25đ

---

## Bài 58 [M04-Q2C2] — ĐSQH Kết Nối Hóa Đơn Chuyển Khoản Tại Bình Thạnh
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CUAHANG, HOADON`

### 1. Đề Bài
Cho biết danh sách các hóa đơn (MAHD, NGAYHD, HINHTHUC_TT, TENCH) được phát hành tại các cửa hàng xăng dầu thuộc quận 'Bình Thạnh' với hình thức thanh toán là 'Chuyển khoản'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E_CH ← σ_{QUAN='Bình Thạnh'}(CUAHANG)
E_HD ← σ_{HINHTHUC_TT='Chuyển khoản'}(HOADON)
KQ ← π_{MAHD, NGAYHD, HINHTHUC_TT, TENCH}(E_CH ⋈ E_HD)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT HD.MAHD, HD.NGAYHD, HD.HINHTHUC_TT, CH.TENCH FROM HOADON HD INNER JOIN CUAHANG CH ON HD.MACH = CH.MACH WHERE CH.QUAN = N'Bình Thạnh' AND HD.HINHTHUC_TT = N'Chuyển khoản';
```

**Các bước suy luận tư duy:**
1. Lọc cửa hàng thuộc quận Bình Thạnh
1. Lọc hóa đơn có hình thức thanh toán Chuyển khoản
1. Kết tự nhiên trên MACH và chiếu kết quả

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `projection`: 0.30đ

---

## Bài 59 [M04-Q2C3] — ĐSQH Kết Ngoài Cửa Hàng Xăng Dầu Và Bể Chứa (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CUAHANG, BE_CHUA`

### 1. Đề Bài
Liệt kê danh sách thông tin tất cả các cửa hàng xăng dầu (MACH, TENCH, QUAN) và mã các bể chứa (MABE), dung tích bể (DUNGTICH) trực thuộc cửa hàng đó (nếu cửa hàng chưa lắp đặt bể chứa nào thì thông tin bể chứa mang giá trị NULL).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{MACH, TENCH, QUAN, MABE, DUNGTICH}(CUAHANG ⟕ BE_CHUA)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT CH.MACH, CH.TENCH, CH.QUAN, BC.MABE, BC.DUNGTICH FROM CUAHANG CH LEFT OUTER JOIN BE_CHUA BC ON CH.MACH = BC.MACH;
```

**Các bước suy luận tư duy:**
1. Kết ngoài trái CUAHANG với BE_CHUA trên MACH để bảo tồn cửa hàng chưa có bể
1. Chiếu các cột MACH, TENCH, QUAN, MABE, DUNGTICH

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.30đ
- `projection`: 0.30đ

---

## Bài 60 [M05-Q2C1] — ĐSQH Lọc Khách Hàng Doanh Nghiệp
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG`

### 1. Đề Bài
Liệt kê danh sách các khách hàng (MAKH, HOTEN, SDT) thuộc phân loại khách hàng là 'Doanh nghiệp'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E1 ← σ_{LOAIKH='Doanh nghiệp'}(KHACHHANG)
KQ ← π_{MAKH, HOTEN, SDT}(E1)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MAKH, HOTEN, SDT FROM KHACHHANG WHERE LOAIKH = N'Doanh nghiệp';
```

**Các bước suy luận tư duy:**
1. Lọc khách hàng có loại hình Doanh nghiệp
1. Chiếu các thuộc tính MAKH, HOTEN, SDT

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ
- `projection`: 0.25đ

---

## Bài 61 [M05-Q2C2] — ĐSQH Kết Nối Căn Hộ Sky Garden Giá Thuê Từ 15 Triệu
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CANHO, TOANHA`

### 1. Đề Bài
Cho biết danh sách các căn hộ (MACH, SOPHONG, DIENTICH, TENTN) thuộc tòa nhà 'Sky Garden' có giá thuê chuẩn (GIATHUE_CHUAN) từ 15,000,000 đồng/tháng trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E_TN ← σ_{TENTN='Sky Garden'}(TOANHA)
E_CH ← σ_{GIATHUE_CHUAN ≥ 15000000}(CANHO)
KQ ← π_{MACH, SOPHONG, DIENTICH, TENTN}(E_TN ⋈ E_CH)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT CH.MACH, CH.SOPHONG, CH.DIENTICH, TN.TENTN FROM CANHO CH INNER JOIN TOANHA TN ON CH.MATN = TN.MATN WHERE TN.TENTN = N'Sky Garden' AND CH.GIATHUE_CHUAN >= 15000000;
```

**Các bước suy luận tư duy:**
1. Lọc tòa nhà tên Sky Garden
1. Lọc căn hộ có giá thuê chuẩn >= 15 triệu
1. Kết tự nhiên trên MATN và chiếu kết quả

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `projection`: 0.30đ

---

## Bài 62 [M05-Q2C3] — ĐSQH Kết Ngoài Tòa Nhà Chung Cư Và Căn Hộ (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TOANHA, CANHO`

### 1. Đề Bài
Liệt kê danh sách thông tin tất cả các tòa nhà chung cư (MATN, TENTN, DIACHI) và mã các căn hộ (MACH), số phòng ngủ (SOPHONG) thuộc tòa nhà đó (nếu tòa nhà chưa có căn hộ nào thì thông tin căn hộ mang giá trị NULL).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ ← π_{MATN, TENTN, DIACHI, MACH, SOPHONG}(TOANHA ⟕ CANHO)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT TN.MATN, TN.TENTN, TN.DIACHI, CH.MACH, CH.SOPHONG FROM TOANHA TN LEFT OUTER JOIN CANHO CH ON TN.MATN = CH.MATN;
```

**Các bước suy luận tư duy:**
1. Kết ngoài trái TOANHA với CANHO trên MATN để bảo tồn tòa nhà chưa có căn hộ
1. Chiếu các cột MATN, TENTN, DIACHI, MACH, SOPHONG

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.30đ
- `projection`: 0.30đ

---
