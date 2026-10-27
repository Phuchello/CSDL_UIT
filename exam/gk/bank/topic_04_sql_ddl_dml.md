# CHUYÊN ĐỀ 4: TRANSACT-SQL DDL/DML & CHUYỂN ĐỔI ĐSQH SANG SQL
**Môn học:** IT004 — Cơ sở dữ liệu | **Hệ thống:** UIT Exam Mastery
**Biên soạn:** VÕ TRỌNG PHÚC | **Số lượng bài tập:** 30 bài

---

## Bài 01 [M01-Q2A] — Tạo Ràng Buộc CHECK Miền Giá Trị Trên CTPX và PHIEUXUAT
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `CTPX(MAPX, MALO, SOLIEUXUAT), PHIEUXUAT(MAPX, NGAYXUAT, TRANGTHAI, MADT)`

### 1. Đề Bài
Tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra thuộc tính SOLIEUXUAT trong CTPX phải là số nguyên dương (> 0), và thuộc tính TRANGTHAI trong PHIEUXUAT chỉ nhận một trong hai giá trị là 0 hoặc 1.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE CTPX ADD CONSTRAINT CK_CTPX_SOLIEUXUAT CHECK (SOLIEUXUAT > 0);

ALTER TABLE PHIEUXUAT ADD CONSTRAINT CK_PHIEUXUAT_TRANGTHAI CHECK (TRANGTHAI IN (0, 1));
```

**Các bước suy luận tư duy:**
1. Xác định bảng áp dụng: CTPX và PHIEUXUAT.
1. Dùng cú pháp ALTER TABLE ... ADD CONSTRAINT ... CHECK (...).
1. Điều kiện miền giá trị: SOLIEUXUAT > 0 và TRANGTHAI IN (0, 1).

**Barem chấm điểm đề xuất:**
- `syntax_alter_table`: 0.25đ
- `check_solieuxuat`: 0.25đ
- `check_trangthai`: 0.25đ

---

## Bài 02 [M01-Q2B] — Cập Nhật Tăng Đơn Giá Vắc-Xin Theo HSD Và Nhà Cung Cấp
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `LOVACXIN(MALO, TENLO, TENVACXIN, NGAYSX, HSD, SOLIEU, DONGIA, MANCC), NHACUNGCAP(MANCC, TENNCC, QUOCGIA, SDT)`

### 1. Đề Bài
Viết câu lệnh SQL cập nhật (UPDATE) tăng giá đơn vị (DONGIA) thêm 10% đối với các lô vắc-xin có hạn sử dụng (HSD) trong năm 2025 do nhà cung cấp có tên là 'AstraZeneca' cung cấp.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
UPDATE LOVACXIN
SET DONGIA = DONGIA * 1.1
FROM LOVACXIN LV
INNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC
WHERE YEAR(LV.HSD) = 2025 AND NCC.TENNCC = 'AstraZeneca';
```

**Các bước suy luận tư duy:**
1. Tính giá mới: DONGIA = DONGIA * 1.1.
1. Điều kiện lọc: YEAR(HSD) = 2025 và TENNCC = 'AstraZeneca'.
1. Cú pháp T-SQL UPDATE ... FROM ... INNER JOIN.

**Barem chấm điểm đề xuất:**
- `update_set_calculation`: 0.25đ
- `join_condition`: 0.25đ
- `where_filtering`: 0.25đ

---

## Bài 03 [M02-Q2A] — Tạo Ràng Buộc CHECK Miền Giá Trị Trên CANHO và THIETBI_PCCC
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `CANHO, THIETBI_PCCC`

### 1. Đề Bài
Tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra thuộc tính DIENTICH trong quan hệ CANHO phải lớn hơn 0 (> 0), và thuộc tính HANSUDUNG trong quan hệ THIETBI_PCCC phải lớn hơn hoặc bằng ngày lắp đặt (HANSUDUNG >= NGAYLAP). Cả hai thuộc tính đều không được mang giá trị NULL.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE CANHO ALTER COLUMN DIENTICH FLOAT NOT NULL;
ALTER TABLE CANHO ADD CONSTRAINT CK_CANHO_DIENTICH CHECK (DIENTICH > 0);

ALTER TABLE THIETBI_PCCC ALTER COLUMN HANSUDUNG DATE NOT NULL;
ALTER TABLE THIETBI_PCCC ADD CONSTRAINT CK_TB_HANSUDUNG CHECK (HANSUDUNG >= NGAYLAP);
```

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 04 [M02-Q2B] — Cập Nhật Tình Trạng Hết Hạn Trong CT_KIEMTRA Theo HSD
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `CT_KIEMTRA, THIETBI_PCCC`

### 1. Đề Bài
Viết câu lệnh SQL cập nhật tình trạng (TINHTRANG) trong quan hệ CT_KIEMTRA thành 'Hết hạn' cho tất cả các thiết bị được kiểm tra trong đợt kiểm tra có mã 'DKT01' mà thiết bị đó có hạn sử dụng (HANSUDUNG) trước ngày '01/06/2025'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
UPDATE CT
SET CT.TINHTRANG = N'Hết hạn'
FROM CT_KIEMTRA CT
INNER JOIN THIETBI_PCCC TB ON CT.MATB = TB.MATB
WHERE CT.MADOT = 'DKT01'
  AND TB.HANSUDUNG < '2025-06-01';
```

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 05 [SQL-D03] — Chuyển Đổi Phép Chia ĐSQH Sang Double NOT EXISTS Trong T-SQL
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG(MAKH, HOTEN), TAIKHOAN(SOTK, MAKH, MALTK), LOAITK(MALTK, TENLTK)`

### 1. Đề Bài
Viết câu truy vấn T-SQL bằng kỹ thuật tương quan hai lần lặp Double NOT EXISTS để tìm các khách hàng (MAKH, HOTEN) đã mở tất cả các loại tài khoản.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
SELECT KH.MAKH, KH.HOTEN
FROM KHACHHANG KH
WHERE NOT EXISTS (
    SELECT *
    FROM LOAITK LTK
    WHERE NOT EXISTS (
        SELECT *
        FROM TAIKHOAN TK
        WHERE TK.MAKH = KH.MAKH AND TK.MALTK = LTK.MALTK
    )
);
```

**Các bước suy luận tư duy:**
1. Nguyên lý: 'Không tồn tại loại tài khoản nào mà khách hàng KH đó KHÔNG mở'.
1. Vòng lặp ngoài duyệt qua từng KHACHHANG.
1. Vòng lặp giữa duyệt qua từng LOAITK.
1. Vòng lặp trong kiểm tra sự tồn tại trong TAIKHOAN.

**Barem chấm điểm đề xuất:**
- `double_not_exists_structure`: 0.50đ
- `correlation_matching`: 0.50đ

---

## Bài 06 [SQL-D27] — T-SQL DML Ràng Buộc Hệ Thống Tuyến Xe Buýt (Bài 27)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `TUYEN_XE, METRO`

### 1. Đề Bài
Tạo ràng buộc toàn vẹn kiểm tra tuyến xe buýt và metro.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
-- DRAFT solution for SQL-D27
```

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 07 [SQL-D28] — T-SQL Cập Nhật Trạng Thái Chuyến Xe Buýt (Bài 28)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `CHUYEN_XE`

### 1. Đề Bài
Cập nhật trạng thái chuyến xe buýt.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
-- DRAFT solution for SQL-D28
```

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 08 [SQL-D25] — T-SQL DML Ràng Buộc Trại Cứu Hộ Động Vật (Bài 25)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `DONG_VAT, CHUONG_TRAI`

### 1. Đề Bài
Tạo ràng buộc toàn vẹn kiểm tra thông tin chuồng trại và động vật.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
-- DRAFT solution for SQL-D25
```

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 09 [SQL-D26] — T-SQL Cập Nhật Khẩu Phần Ăn Trại Cứu Hộ (Bài 26)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `KHAU_PHAN`

### 1. Đề Bài
Cập nhật khẩu phần ăn động vật.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
-- DRAFT solution for SQL-D26
```

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 10 [SQL-D01] — Tạo Bảng Với Khóa Ngoại Kép & Ràng Buộc CHECK
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `CTPX(MAPX, MALO, SOLIEUXUAT)`

### 1. Đề Bài
Viết lệnh T-SQL CREATE TABLE tạo bảng CTPX với PK kép và CHECK số lượng > 0.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
CREATE TABLE CTPX (MAPX VARCHAR(10), MALO VARCHAR(10), SOLIEUXUAT INT CHECK(SOLIEUXUAT > 0), PRIMARY KEY(MAPX, MALO));
```

**Các bước suy luận tư duy:**
1. Cú pháp T-SQL
1. Mệnh đề WHERE lọc dữ liệu
1. Kiểm tra ràng buộc.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 11 [SQL-D11] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 11)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh UPDATE tăng/giảm giá trị của một quan hệ dựa trên thông tin kết nối từ quan hệ khác.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
UPDATE B1 SET B1.GIA = B1.GIA * 1.05 FROM BANG_A B1 INNER JOIN BANG_B B2 ON B1.ID = B2.ID WHERE B2.LOAI = 'VIP';
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 12 [SQL-D12] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 12)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh ALTER TABLE thêm ràng buộc CHECK kiểm tra giá trị cột số liệu phải dương và trạng thái hợp lệ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE BANG_12 ADD CONSTRAINT CK_BANG_12 CHECK (SOLUONG > 0 AND TRANGTHAI IN ('A', 'B'));
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 13 [SQL-D13] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 13)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh UPDATE tăng/giảm giá trị của một quan hệ dựa trên thông tin kết nối từ quan hệ khác.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
UPDATE B1 SET B1.GIA = B1.GIA * 1.05 FROM BANG_A B1 INNER JOIN BANG_B B2 ON B1.ID = B2.ID WHERE B2.LOAI = 'VIP';
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 14 [SQL-D14] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 14)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh ALTER TABLE thêm ràng buộc CHECK kiểm tra giá trị cột số liệu phải dương và trạng thái hợp lệ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE BANG_14 ADD CONSTRAINT CK_BANG_14 CHECK (SOLUONG > 0 AND TRANGTHAI IN ('A', 'B'));
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 15 [SQL-D15] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 15)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh UPDATE tăng/giảm giá trị của một quan hệ dựa trên thông tin kết nối từ quan hệ khác.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
UPDATE B1 SET B1.GIA = B1.GIA * 1.05 FROM BANG_A B1 INNER JOIN BANG_B B2 ON B1.ID = B2.ID WHERE B2.LOAI = 'VIP';
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 16 [SQL-D16] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 16)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh ALTER TABLE thêm ràng buộc CHECK kiểm tra giá trị cột số liệu phải dương và trạng thái hợp lệ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE BANG_16 ADD CONSTRAINT CK_BANG_16 CHECK (SOLUONG > 0 AND TRANGTHAI IN ('A', 'B'));
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 17 [SQL-D17] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 17)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh UPDATE tăng/giảm giá trị của một quan hệ dựa trên thông tin kết nối từ quan hệ khác.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
UPDATE B1 SET B1.GIA = B1.GIA * 1.05 FROM BANG_A B1 INNER JOIN BANG_B B2 ON B1.ID = B2.ID WHERE B2.LOAI = 'VIP';
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 18 [SQL-D18] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 18)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh ALTER TABLE thêm ràng buộc CHECK kiểm tra giá trị cột số liệu phải dương và trạng thái hợp lệ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE BANG_18 ADD CONSTRAINT CK_BANG_18 CHECK (SOLUONG > 0 AND TRANGTHAI IN ('A', 'B'));
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 19 [SQL-D19] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 19)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh UPDATE tăng/giảm giá trị của một quan hệ dựa trên thông tin kết nối từ quan hệ khác.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
UPDATE B1 SET B1.GIA = B1.GIA * 1.05 FROM BANG_A B1 INNER JOIN BANG_B B2 ON B1.ID = B2.ID WHERE B2.LOAI = 'VIP';
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 20 [SQL-D20] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 20)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh ALTER TABLE thêm ràng buộc CHECK kiểm tra giá trị cột số liệu phải dương và trạng thái hợp lệ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE BANG_20 ADD CONSTRAINT CK_BANG_20 CHECK (SOLUONG > 0 AND TRANGTHAI IN ('A', 'B'));
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 21 [SQL-D21] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 21)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh UPDATE tăng/giảm giá trị của một quan hệ dựa trên thông tin kết nối từ quan hệ khác.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
UPDATE B1 SET B1.GIA = B1.GIA * 1.05 FROM BANG_A B1 INNER JOIN BANG_B B2 ON B1.ID = B2.ID WHERE B2.LOAI = 'VIP';
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 22 [SQL-D22] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 22)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh ALTER TABLE thêm ràng buộc CHECK kiểm tra giá trị cột số liệu phải dương và trạng thái hợp lệ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE BANG_22 ADD CONSTRAINT CK_BANG_22 CHECK (SOLUONG > 0 AND TRANGTHAI IN ('A', 'B'));
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 23 [SQL-D23] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 23)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh UPDATE tăng/giảm giá trị của một quan hệ dựa trên thông tin kết nối từ quan hệ khác.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
UPDATE B1 SET B1.GIA = B1.GIA * 1.05 FROM BANG_A B1 INNER JOIN BANG_B B2 ON B1.ID = B2.ID WHERE B2.LOAI = 'VIP';
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 24 [SQL-D24] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 24)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh ALTER TABLE thêm ràng buộc CHECK kiểm tra giá trị cột số liệu phải dương và trạng thái hợp lệ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE BANG_24 ADD CONSTRAINT CK_BANG_24 CHECK (SOLUONG > 0 AND TRANGTHAI IN ('A', 'B'));
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 25 [M03-Q2A] — Tạo Ràng Buộc CHECK Miền Giá Trị Trên PHIEU_NHAN và DOT_CUUTRO
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `PHIEU_NHAN, DOT_CUUTRO`

### 1. Đề Bài
Tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra số tiền nhận (SOTIEN) trong bảng PHIEU_NHAN phải lớn hơn 0 (> 0), và ngày kết thúc đợt cứu trợ (NGAYKT) trong bảng DOT_CUUTRO phải lớn hơn hoặc bằng ngày bắt đầu (NGAYKT >= NGAYBD). Cả hai thuộc tính đều không được mang giá trị NULL.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE PHIEU_NHAN ALTER COLUMN SOTIEN DECIMAL(18, 2) NOT NULL;
ALTER TABLE PHIEU_NHAN ADD CONSTRAINT CK_PHIEUNHAN_SOTIEN CHECK (SOTIEN > 0);

ALTER TABLE DOT_CUUTRO ALTER COLUMN NGAYKT DATE NOT NULL;
ALTER TABLE DOT_CUUTRO ADD CONSTRAINT CK_DOTCUUTRO_NGAY CHECK (NGAYKT >= NGAYBD);
```

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 26 [M03-Q2B] — Cập Nhật Mức Độ Thiệt Hại Trong HO_DAN Thuộc Xã Hiệp Phước
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `HO_DAN, XA`

### 1. Đề Bài
Cập nhật mức độ thiệt hại (MUCDO_THIETHAI) thành 'Nặng' cho các hộ gia đình thuộc xã có tên (TENXA) là 'Hiệp Phước' và có số nhân khẩu (SONKHAU) từ 5 người trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
UPDATE HD
SET HD.MUCDO_THIETHAI = N'Nặng'
FROM HO_DAN HD
INNER JOIN XA X ON HD.MAXA = X.MAXA
WHERE X.TENXA = N'Hiệp Phước'
  AND HD.SONKHAU >= 5;
```

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 27 [M04-Q2A] — Tạo Ràng Buộc CHECK Miền Giá Trị Trên BE_CHUA
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `BE_CHUA`

### 1. Đề Bài
Tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra thuộc tính dung tích bể (DUNGTICH) trong bảng BE_CHUA phải lớn hơn 0 (> 0), và lượng nhiên liệu tồn (LUONG_TON) phải lớn hơn hoặc bằng 0 đồng thời không vượt quá dung tích của bể (0 <= LUONG_TON <= DUNGTICH). Cả hai thuộc tính đều không được mang giá trị NULL.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE BE_CHUA ALTER COLUMN DUNGTICH FLOAT NOT NULL;
ALTER TABLE BE_CHUA ADD CONSTRAINT CK_BECHUA_DUNGTICH CHECK (DUNGTICH > 0);

ALTER TABLE BE_CHUA ALTER COLUMN LUONG_TON FLOAT NOT NULL;
ALTER TABLE BE_CHUA ADD CONSTRAINT CK_BECHUA_LUONGTON CHECK (LUONG_TON >= 0 AND LUONG_TON <= DUNGTICH);
```

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 28 [M04-Q2B] — Cập Nhật Đơn Giá Tăng 5% Cho Xăng Khoáng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `NHIENLIEU`

### 1. Đề Bài
Viết câu lệnh SQL cập nhật tăng đơn giá niêm yết (DONGIA) thêm 5% cho tất cả các mặt hàng nhiên liệu thuộc phân loại (LOAINL) là 'Xăng khoáng' có đơn vị tính (DONVITINH) là 'Lít'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
UPDATE NHIENLIEU
SET DONGIA = DONGIA * 1.05
WHERE LOAINL = N'Xăng khoáng'
  AND DONVITINH = N'Lít';
```

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 29 [M05-Q2A] — Tạo Ràng Buộc CHECK Miền Giá Trị Trên HOPDONG
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `HOPDONG`

### 1. Đề Bài
Tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra tiền đặt cọc (TIENCOC) trong quan hệ HOPDONG phải lớn hơn hoặc bằng 0 (>= 0), và ngày kết thúc hợp đồng thuê (NGAYKT) phải sau ngày bắt đầu hiệu lực thuê (NGAYKT > NGAYBD). Cả hai thuộc tính đều không được mang giá trị NULL.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE HOPDONG ALTER COLUMN TIENCOC DECIMAL(18, 2) NOT NULL;
ALTER TABLE HOPDONG ADD CONSTRAINT CK_HOPDONG_TIENCOC CHECK (TIENCOC >= 0);

ALTER TABLE HOPDONG ALTER COLUMN NGAYKT DATE NOT NULL;
ALTER TABLE HOPDONG ADD CONSTRAINT CK_HOPDONG_NGAY CHECK (NGAYKT > NGAYBD);
```

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 30 [M05-Q2B] — Cập Nhật Trạng Thái Đang Thuê Cho Căn Hộ Có Hợp Đồng Năm 2024
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `CANHO, HOPDONG`

### 1. Đề Bài
Cập nhật trạng thái (TRANGTHAI) thành 'Đang thuê' cho tất cả các căn hộ có trong các hợp đồng thuê (HOPDONG) được ký trong năm 2024 mà ngày kết thúc hợp đồng (NGAYKT) từ ngày '2024-12-31' trở về sau.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
UPDATE CH
SET CH.TRANGTHAI = N'Đang thuê'
FROM CANHO CH
INNER JOIN HOPDONG HD ON CH.MACH = HD.MACH
WHERE HD.NGAYKY >= '2024-01-01' AND HD.NGAYKY <= '2024-12-31'
  AND HD.NGAYKT >= '2024-12-31';
```

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---
