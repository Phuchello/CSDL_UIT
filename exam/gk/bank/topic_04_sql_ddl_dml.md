# CHUYÊN ĐỀ 4: TRANSACT-SQL DDL/DML & CHUYỂN ĐỔI ĐSQH SANG SQL
**Môn học:** IT004 — Cơ sở dữ liệu | **Hệ thống:** UIT Exam Mastery
**Biên soạn:** VÕ TRỌNG PHÚC | **Số lượng bài tập:** 26 bài

---

## Bài 01 [M01-Q2A] — Tạo Ràng Buộc CHECK Miền Giá Trị Trên CTPX và PHIEUXUAT
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `CTPX(MAPX, MALO, SOLIEUXUAT), PHIEUXUAT(MAPX, NGAYXUAT, MADT, TRANGTHAI)`

### 1. Đề Bài
Tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra thuộc tính SOLIEUXUAT trong CTPX phải là số nguyên dương (> 0), và thuộc tính TRANGTHAI trong PHIEUXUAT chỉ nhận một trong hai giá trị là 0 hoặc 1.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE CTPX ADD CONSTRAINT CK_CTPX_SOLIEUXUAT CHECK (SOLIEUXUAT > 0);

ALTER TABLE PHIEUXUAT ADD CONSTRAINT CK_PHIEUXUAT_TRANGTHAI CHECK (TRANGTHAI IN (0, 1));
```

**Các bước suy luận tư duy:**
1. Xác định bảng cần áp dụng: CTPX và PHIEUXUAT.
1. Dùng cú pháp ALTER TABLE ... ADD CONSTRAINT ... CHECK (...).
1. Điều kiện miền giá trị: SOLIEUXUAT > 0 và TRANGTHAI IN (0, 1).

**Barem chấm điểm đề xuất:**
- `syntax_alter_table`: 0.25đ
- `check_solieuxuat`: 0.25đ
- `check_trangthai`: 0.25đ

---

## Bài 02 [M01-Q2B] — Cập Nhật Tăng Đơn Giá Vắc-Xin Theo HSD Và Nhà Cung Cấp
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 6 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `LOVACXIN(MALO, TENLO, TENKVACXIN, MANCC, NGAYSX, HSD, SOLIEU, DONGIA), NHACUNGCAP(MANCC, TENNCC, QUOCGIA, SDT)`

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
1. Phép tính: Tăng 10% tức DONGIA = DONGIA * 1.1 (hoặc DONGIA + DONGIA * 0.1).
1. Điều kiện lọc: YEAR(HSD) = 2025 và TENNCC = 'AstraZeneca'.
1. Dùng cú pháp T-SQL UPDATE ... FROM ... INNER JOIN để liên kết bảng an toàn.

**Barem chấm điểm đề xuất:**
- `update_set_calculation`: 0.25đ
- `join_condition`: 0.25đ
- `where_filtering`: 0.25đ

---

## Bài 03 [SQL-D03] — Chuyển Đổi Phép Chia ĐSQH Sang Double NOT EXISTS Trong T-SQL
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

## Bài 04 [SQL-D01] — Tạo Bảng Với Khóa Ngoại Kép & Ràng Buộc CHECK
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

## Bài 05 [SQL-D02] — Cập Nhật DML Có Điều Kiện Ngày Tháng & Chuỗi Ký Tự
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `LOVACXIN(MALO, HSD, DONGIA)`

### 1. Đề Bài
Viết lệnh T-SQL UPDATE giảm 15% đơn giá cho các lô vắc-xin hết hạn trong quý 1 năm 2025.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
UPDATE LOVACXIN SET DONGIA = DONGIA * 0.85 WHERE HSD >= '2025-01-01' AND HSD <= '2025-03-31';
```

**Các bước suy luận tư duy:**
1. Cú pháp T-SQL
1. Mệnh đề WHERE lọc dữ liệu
1. Kiểm tra ràng buộc.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 06 [SQL-D04] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 4)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh ALTER TABLE thêm ràng buộc CHECK kiểm tra giá trị cột số liệu phải dương và trạng thái hợp lệ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE BANG_4 ADD CONSTRAINT CK_BANG_4 CHECK (SOLUONG > 0 AND TRANGTHAI IN ('A', 'B'));
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 07 [SQL-D05] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 5)
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

## Bài 08 [SQL-D06] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 6)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh ALTER TABLE thêm ràng buộc CHECK kiểm tra giá trị cột số liệu phải dương và trạng thái hợp lệ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE BANG_6 ADD CONSTRAINT CK_BANG_6 CHECK (SOLUONG > 0 AND TRANGTHAI IN ('A', 'B'));
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 09 [SQL-D07] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 7)
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

## Bài 10 [SQL-D08] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 8)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh ALTER TABLE thêm ràng buộc CHECK kiểm tra giá trị cột số liệu phải dương và trạng thái hợp lệ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE BANG_8 ADD CONSTRAINT CK_BANG_8 CHECK (SOLUONG > 0 AND TRANGTHAI IN ('A', 'B'));
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 11 [SQL-D09] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 9)
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

## Bài 12 [SQL-D10] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 10)
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 5 phút | **Điểm số:** 0.75 điểm
- **Lược đồ tham chiếu:** `R1(ID, GIA), R2(ID, LOAI)`

### 1. Đề Bài
Viết lệnh ALTER TABLE thêm ràng buộc CHECK kiểm tra giá trị cột số liệu phải dương và trạng thái hợp lệ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh SQL tương đương:**
```sql
ALTER TABLE BANG_10 ADD CONSTRAINT CK_BANG_10 CHECK (SOLUONG > 0 AND TRANGTHAI IN ('A', 'B'));
```

**Các bước suy luận tư duy:**
1. Xác định bảng
1. Viết cú pháp T-SQL
1. Kiểm thử logic.

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ

---

## Bài 13 [SQL-D11] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 11)
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

## Bài 14 [SQL-D12] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 12)
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

## Bài 15 [SQL-D13] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 13)
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

## Bài 16 [SQL-D14] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 14)
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

## Bài 17 [SQL-D15] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 15)
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

## Bài 18 [SQL-D16] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 16)
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

## Bài 19 [SQL-D17] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 17)
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

## Bài 20 [SQL-D18] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 18)
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

## Bài 21 [SQL-D19] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 19)
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

## Bài 22 [SQL-D20] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 20)
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

## Bài 23 [SQL-D21] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 21)
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

## Bài 24 [SQL-D22] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 22)
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

## Bài 25 [SQL-D23] — T-SQL Cập Nhật DML Liên Bảng UPDATE ... FROM (Bài 23)
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

## Bài 26 [SQL-D24] — T-SQL Tạo Ràng Buộc CHECK Miền Giá Trị (Bài 24)
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
