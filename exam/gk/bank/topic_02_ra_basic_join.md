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

## Bài 26 [M12-Q2C1] — ĐSQH Lọc Phim Khoa Học Viễn Tưởng Thời Lượng Từ 120 Phút
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIM(MAPHIM, TENPHIM, THELOAI, THOILUONG, DAODIEN, NAMSX)`

### 1. Đề Bài
Liệt kê danh sách các bộ phim (MAPHIM, TENPHIM, THOILUONG, DAODIEN) thuộc thể loại 'Khoa học viễn tưởng' có thời lượng chiếu từ 120 phút trở lên (>= 120).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAPHIM, TENPHIM, THOILUONG, DAODIEN}(\sigma_{THELOAI = 'Khoa học viễn tưởng' \wedge THOILUONG \ge 120}(PHIM))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MAPHIM, TENPHIM, THOILUONG, DAODIEN FROM PHIM WHERE THELOAI = N'Khoa học viễn tưởng' AND THOILUONG >= 120;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{THELOAI = 'Khoa học viễn tưởng' \wedge THOILUONG \ge 120}(PHIM)
1. KQ = \pi_{MAPHIM, TENPHIM, THOILUONG, DAODIEN}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 27 [M13-Q2C1] — ĐSQH Lọc Tuyến Metro Có Cự Ly Từ 15 km Trở Lên
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TUYEN_XE(MATUYEN, TENTUYEN, LOAI_HINH, CULY_KM, GIAVE_LUOT)`

### 1. Đề Bài
Liệt kê danh sách các tuyến xe (MATUYEN, TENTUYEN, CULY_KM, GIAVE_LUOT) thuộc loại hình 'Tuyến Metro' có cự ly từ 15 km trở lên (>= 15).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MATUYEN, TENTUYEN, CULY_KM, GIAVE_LUOT}(\sigma_{LOAI_HINH = 'Tuyến Metro' \wedge CULY_KM \ge 15}(TUYEN_XE))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MATUYEN, TENTUYEN, CULY_KM, GIAVE_LUOT FROM TUYEN_XE WHERE LOAI_HINH = N'Tuyến Metro' AND CULY_KM >= 15;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{LOAI_HINH = 'Tuyến Metro' \wedge CULY_KM \ge 15}(TUYEN_XE)
1. KQ = \pi_{MATUYEN, TENTUYEN, CULY_KM, GIAVE_LUOT}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 28 [M13-Q2C2] — ĐSQH Kết Nối Phương Tiện Thuộc Tuyến Bến Xe Miền Đông Mới
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TUYEN_XE(MATUYEN, TENTUYEN, LOAI_HINH, CULY_KM, GIAVE_LUOT), PHUONGTIEN(MAPT, BIENSO, SOGHE, NAMSX, MATUYEN)`

### 1. Đề Bài
Cho biết danh sách các phương tiện (MAPT, BIENSO, SOGHE) đang phục vụ cho tuyến xe mang tên 'Bến Thành - Bến xe Miền Đông mới'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAPT, BIENSO, SOGHE}(\sigma_{TENTUYEN = 'Bến Thành - Bến xe Miền Đông mới'}(TUYEN_XE) \bowtie PHUONGTIEN)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT pt.MAPT, pt.BIENSO, pt.SOGHE FROM PHUONGTIEN pt JOIN TUYEN_XE tx ON pt.MATUYEN = tx.MATUYEN WHERE tx.TENTUYEN = N'Bến Thành - Bến xe Miền Đông mới';
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{TENTUYEN = 'Bến Thành - Bến xe Miền Đông mới'}(TUYEN_XE)
1. E_2 = E_1 \bowtie PHUONGTIEN
1. KQ = \pi_{MAPT, BIENSO, SOGHE}(E_2)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 29 [M13-Q2C3] — ĐSQH Kết Ngoài Danh Sách Trạm Dừng Và Lộ Trình Tuyến (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TRAM_DUNG(MATRAM, TENTRAM, DIACHI, QUAN_HUYEN), LOTRINH(MATUYEN, MATRAM, SOTHUTU, KHOANGCACH_KM)`

### 1. Đề Bài
Liệt kê thông tin tất cả các trạm dừng (MATRAM, TENTRAM, QUAN_HUYEN) cùng mã tuyến xe (MATUYEN), số thứ tự ghé trạm (SOTHUTU) đi qua trạm đó (nếu trạm dừng chưa có tuyến nào đi qua thì mang giá trị NULL).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MATRAM, TENTRAM, QUAN_HUYEN, MATUYEN, SOTHUTU}(TRAM_DUNG =\bowtie LOTRINH)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT td.MATRAM, td.TENTRAM, td.QUAN_HUYEN, lt.MATUYEN, lt.SOTHUTU FROM TRAM_DUNG td LEFT JOIN LOTRINH lt ON td.MATRAM = lt.MATRAM;
```

**Các bước suy luận tư duy:**
1. E_1 = TRAM_DUNG =\bowtie LOTRINH
1. KQ = \pi_{MATRAM, TENTRAM, QUAN_HUYEN, MATUYEN, SOTHUTU}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 30 [M14-Q2C1] — ĐSQH Lọc Đề Tài Cấp Nhà Nước Kinh Phí Từ 1 Tỷ Đồng Trở Lên
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DETAI(MADT, TENDT, CAP_QUANLY, KINHPHI, NGAYBD, NGAYKT, CHUNHIEM_DT)`

### 1. Đề Bài
Liệt kê danh sách các đề tài NCKH (MADT, TENDT, KINHPHI, NGAYBD) thuộc cấp quản lý 'Cấp Nhà nước' có tổng kinh phí từ 1.000.000.000 VNĐ (1 tỷ đồng) trở lên (>= 1000000000).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MADT, TENDT, KINHPHI, NGAYBD}(\sigma_{CAP_QUANLY = 'Cấp Nhà nước' \wedge KINHPHI \ge 1000000000}(DETAI))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MADT, TENDT, KINHPHI, NGAYBD FROM DETAI WHERE CAP_QUANLY = N'Cấp Nhà nước' AND KINHPHI >= 1000000000;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{CAP_QUANLY = 'Cấp Nhà nước' \wedge KINHPHI \ge 1000000000}(DETAI)
1. KQ = \pi_{MADT, TENDT, KINHPHI, NGAYBD}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 31 [M14-Q2C2] — ĐSQH Kết Nối Sản Phẩm Khoa Học Do GV01 Làm Chủ Nhiệm Đề Tài
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DETAI(MADT, TENDT, CAP_QUANLY, KINHPHI, NGAYBD, NGAYKT, CHUNHIEM_DT), SANPHAM_KH(MASP, TENSP, LOAISP, XEP_HANG, MADT)`

### 1. Đề Bài
Cho biết danh sách các sản phẩm khoa học (MASP, TENSP, LOAISP, XEP_HANG) được công bố từ các đề tài do giảng viên mang mã MAGV = 'GV01' làm chủ nhiệm đề tài.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MASP, TENSP, LOAISP, XEP_HANG}(\sigma_{CHUNHIEM_DT = 'GV01'}(DETAI) \bowtie SANPHAM_KH)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT sp.MASP, sp.TENSP, sp.LOAISP, sp.XEP_HANG FROM SANPHAM_KH sp JOIN DETAI dt ON sp.MADT = dt.MADT WHERE dt.CHUNHIEM_DT = 'GV01';
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{CHUNHIEM_DT = 'GV01'}(DETAI)
1. E_2 = E_1 \bowtie SANPHAM_KH
1. KQ = \pi_{MASP, TENSP, LOAISP, XEP_HANG}(E_2)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 32 [M15-Q2C1] — ĐSQH Lọc Các Loài Động Vật Cực Kỳ Nguy Cấp
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `LOAI_DONGVAT(MALOAI, TENLOAI, TEN_KHOAHOC, MUC_NGUYCAP)`

### 1. Đề Bài
Liệt kê danh sách các loài động vật (MALOAI, TENLOAI, TEN_KHOAHOC) có mức độ nguy cấp là 'Cực kỳ nguy cấp'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MALOAI, TENLOAI, TEN_KHOAHOC}(\sigma_{MUC_NGUYCAP = 'Cực kỳ nguy cấp'}(LOAI_DONGVAT))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MALOAI, TENLOAI, TEN_KHOAHOC FROM LOAI_DONGVAT WHERE MUC_NGUYCAP = N'Cực kỳ nguy cấp';
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{MUC_NGUYCAP = 'Cực kỳ nguy cấp'}(LOAI_DONGVAT)
1. KQ = \pi_{MALOAI, TENLOAI, TEN_KHOAHOC}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 33 [M15-Q2C2] — ĐSQH Kết Nối Cá Thể Thuộc Khu Bán Tự Nhiên Cát Tiên
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHU_BAOTON(MAKHU, TENKHU, DIENTICH_HA, NGUOI_PHUTRACH), DONGVAT(MADV, MALOAI, GIOITINH, CANNANG_KG, TINHTRANG_SK, MAKHU)`

### 1. Đề Bài
Cho biết danh sách các cá thể động vật (MADV, GIOITINH, CANNANG_KG, TINHTRANG_SK) thuộc phân khu bảo tồn có tên là 'Khu Bán Tự Nhiên Cát Tiên'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MADV, GIOITINH, CANNANG_KG, TINHTRANG_SK}(\sigma_{TENKHU = 'Khu Bán Tự Nhiên Cát Tiên'}(KHU_BAOTON) \bowtie DONGVAT)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT dv.MADV, dv.GIOITINH, dv.CANNANG_KG, dv.TINHTRANG_SK FROM DONGVAT dv JOIN KHU_BAOTON kb ON dv.MAKHU = kb.MAKHU WHERE kb.TENKHU = N'Khu Bán Tự Nhiên Cát Tiên';
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{TENKHU = 'Khu Bán Tự Nhiên Cát Tiên'}(KHU_BAOTON)
1. E_2 = E_1 \bowtie DONGVAT
1. KQ = \pi_{MADV, GIOITINH, CANNANG_KG, TINHTRANG_SK}(E_2)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 34 [M15-Q2C3] — ĐSQH Kết Ngoài Danh Sách Phân Khu Và Nhân Viên (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHU_BAOTON(MAKHU, TENKHU, DIENTICH_HA, NGUOI_PHUTRACH), NHANVIEN(MANV, HOTEN, CHUYENMON, LUONG, MAKHU)`

### 1. Đề Bài
Liệt kê thông tin tất cả các phân khu bảo tồn (MAKHU, TENKHU) cùng mã nhân viên (MANV), họ tên nhân viên (HOTEN) công tác tại phân khu đó (nếu phân khu chưa có nhân viên thì mang giá trị NULL).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAKHU, TENKHU, MANV, HOTEN}(KHU_BAOTON =\bowtie NHANVIEN)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT kb.MAKHU, kb.TENKHU, nv.MANV, nv.HOTEN FROM KHU_BAOTON kb LEFT JOIN NHANVIEN nv ON kb.MAKHU = nv.MAKHU;
```

**Các bước suy luận tư duy:**
1. E_1 = KHU_BAOTON =\bowtie NHANVIEN
1. KQ = \pi_{MAKHU, TENKHU, MANV, HOTEN}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 35 [RA-B46] — ĐSQH Kết Nối Đa Bảng: Căn Hộ & Tòa Nhà (Bài 46)
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

## Bài 36 [RA-B47] — ĐSQH Kết Ngoài Left Outer Join (Nếu Có): Khoa & Sinh Viên (Bài 47)
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

## Bài 37 [RA-B48] — ĐSQH Tự Kết Phân Cấp: Đơn Hàng & Khách (Bài 48)
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

## Bài 38 [RA-B49] — ĐSQH Phép Tập Hợp Giao/Trừ: Sách & Tác Giả (Bài 49)
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

## Bài 39 [RA-B50] — ĐSQH Lọc & Chiếu: Chuyến Bay & Phi Công (Bài 50)
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

## Bài 40 [RA-B51] — ĐSQH Kết Nối Đa Bảng: Phòng Khám & Bác Sĩ (Bài 51)
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

## Bài 41 [RA-B52] — ĐSQH Kết Ngoài Left Outer Join (Nếu Có): Tài Khoản & Giao Dịch (Bài 52)
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

## Bài 42 [RA-B53] — ĐSQH Tự Kết Phân Cấp: Lớp Học & Môn Học (Bài 53)
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

## Bài 43 [RA-B54] — ĐSQH Phép Tập Hợp Giao/Trừ: Xe Máy & Bảo Dưỡng (Bài 54)
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

## Bài 44 [RA-B55] — ĐSQH Lọc & Chiếu: Hóa Đơn & Nhân Viên (Bài 55)
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

## Bài 45 [RA-B56] — ĐSQH Kết Nối Đa Bảng: Căn Hộ & Tòa Nhà (Bài 56)
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

## Bài 46 [RA-B57] — ĐSQH Kết Ngoài Left Outer Join (Nếu Có): Khoa & Sinh Viên (Bài 57)
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

## Bài 47 [RA-B58] — ĐSQH Tự Kết Phân Cấp: Đơn Hàng & Khách (Bài 58)
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

## Bài 48 [RA-B59] — ĐSQH Phép Tập Hợp Giao/Trừ: Sách & Tác Giả (Bài 59)
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

## Bài 49 [M11-Q2C2] — ĐSQH Kết Nối Phiếu Xuất Cho Cửa Hàng The Coffee House Landmark 81
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

## Bài 50 [M11-Q2C3] — ĐSQH Kết Ngoài Danh Sách Khu Vực Và Cửa Hàng (Nếu Có)
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

## Bài 51 [M12-Q2C2] — ĐSQH Kết Nối Vé Xem Phim Tại Cụm Rạp CGV Landmark 81
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CUMRAP(MACR, TENCR, DIACHI, THANHPHO), PHONGCHIEU(MAPC, TENPHONG, SOGHETOI_DA, LOAIPHONG, MACR), SUATCHIEU(MASC, MAPHIM, MAPC, NGAYCHIEU, GIOCHIEU, GIAVE_CHUAN), VEXEM(MAVE, MASC, MAKH, SOGHE, GIAVE_THUC, TRANGTHAI)`

### 1. Đề Bài
Cho biết danh sách các vé xem phim (MAVE, SOGHE, GIAVE_THUC, TENCR) của các suất chiếu được tổ chức tại cụm rạp mang tên 'CGV Landmark 81'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAVE, SOGHE, GIAVE_THUC, TENCR}(\sigma_{TENCR = 'CGV Landmark 81'}(CUMRAP) \bowtie PHONGCHIEU \bowtie SUATCHIEU \bowtie VEXEM)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT vx.MAVE, vx.SOGHE, vx.GIAVE_THUC, cr.TENCR FROM VEXEM vx JOIN SUATCHIEU sc ON vx.MASC = sc.MASC JOIN PHONGCHIEU pc ON sc.MAPC = pc.MAPC JOIN CUMRAP cr ON pc.MACR = cr.MACR WHERE cr.TENCR = N'CGV Landmark 81';
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{TENCR = 'CGV Landmark 81'}(CUMRAP)
1. E_2 = E_1 \bowtie PHONGCHIEU \bowtie SUATCHIEU \bowtie VEXEM
1. KQ = \pi_{MAVE, SOGHE, GIAVE_THUC, TENCR}(E_2)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 52 [M12-Q2C3] — ĐSQH Kết Ngoài Danh Sách Cụm Rạp Và Phòng Chiếu (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CUMRAP(MACR, TENCR, DIACHI, THANHPHO), PHONGCHIEU(MAPC, TENPHONG, SOGHETOI_DA, LOAIPHONG, MACR)`

### 1. Đề Bài
Liệt kê thông tin tất cả các cụm rạp (MACR, TENCR) cùng mã phòng chiếu (MAPC), tên phòng chiếu (TENPHONG) trực thuộc cụm rạp đó (nếu cụm rạp chưa có phòng chiếu thì mang giá trị NULL).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MACR, TENCR, MAPC, TENPHONG}(CUMRAP =\bowtie PHONGCHIEU)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT cr.MACR, cr.TENCR, pc.MAPC, pc.TENPHONG FROM CUMRAP cr LEFT JOIN PHONGCHIEU pc ON cr.MACR = pc.MACR;
```

**Các bước suy luận tư duy:**
1. E_1 = CUMRAP =\bowtie PHONGCHIEU
1. KQ = \pi_{MACR, TENCR, MAPC, TENPHONG}(E_1)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 53 [M14-Q2C3] — ĐSQH Kết Ngoài Danh Sách Khoa Viện Và Đề Tài Chủ Nhiệm (Nếu Có)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHOA_VIEN(MAKV, TENKV, DIENTHOAI, TRUONGKHOA), GIANGVIEN(MAGV, HOTEN, HOCHAM, HOCVI, LUONG, MAKV), DETAI(MADT, TENDT, CAP_QUANLY, KINHPHI, NGAYBD, NGAYKT, CHUNHIEM_DT)`

### 1. Đề Bài
Liệt kê thông tin tất cả các khoa viện (MAKV, TENKV) cùng mã đề tài (MADT), tên đề tài (TENDT) do giảng viên trực thuộc khoa viện đó làm chủ nhiệm (nếu khoa viện chưa có đề tài nào thì mang giá trị NULL).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAKV, TENKV, MADT, TENDT}(KHOA_VIEN =\bowtie_{KHOA_VIEN.MAKV = GIANGVIEN.MAKV} (GIANGVIEN \bowtie_{GIANGVIEN.MAGV = DETAI.CHUNHIEM_DT} DETAI))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT kv.MAKV, kv.TENKV, dt.MADT, dt.TENDT FROM KHOA_VIEN kv LEFT JOIN GIANGVIEN gv ON kv.MAKV = gv.MAKV LEFT JOIN DETAI dt ON gv.MAGV = dt.CHUNHIEM_DT;
```

**Các bước suy luận tư duy:**
1. E_1 = GIANGVIEN \bowtie_{GIANGVIEN.MAGV = DETAI.CHUNHIEM_DT} DETAI
1. E_2 = KHOA_VIEN =\bowtie_{KHOA_VIEN.MAKV = E_1.MAKV} E_1
1. KQ = \pi_{MAKV, TENKV, MADT, TENDT}(E_2)

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
