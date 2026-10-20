# CHUYÊN ĐỀ 3: PHÉP CHIA (TẤT CẢ / MỌI), GOM NHÓM & TRUY VẤN PHỨC HỢP
**Môn học:** IT004 — Cơ sở dữ liệu | **Hệ thống:** UIT Exam Mastery
**Biên soạn:** VÕ TRỌNG PHÚC | **Số lượng bài tập:** 52 bài

---

## Bài 01 [M01-Q2C4] — ĐSQH Gom Nhóm Tính Tổng Liều Vắc-Xin Xuất Theo Điểm Tiêm
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 7 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEUXUAT(MAPX, NGAYXUAT, MADT, TRANGTHAI), CTPX(MAPX, MALO, SOLIEUXUAT)`

### 1. Đề Bài
Tính tổng số liều vắc-xin xuất (SOLIEUXUAT) theo từng điểm tiêm (MADT) trong tháng 10 năm 2024. Thông tin hiển thị gồm: MADT, TONGLIEU.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R1 ← σ_{NGAYXUAT ≥ '01/10/2024' ∧ NGAYXUAT ≤ '31/10/2024'}(PHIEUXUAT)
R2 ← R1 ⋈_{R1.MAPX = CTPX.MAPX} CTPX
KQ ← _{MADT} γ _{SUM(SOLIEUXUAT) → TONGLIEU}(R2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT PX.MADT, SUM(CT.SOLIEUXUAT) AS TONGLIEU
FROM PHIEUXUAT PX
INNER JOIN CTPX CT ON PX.MAPX = CT.MAPX
WHERE MONTH(PX.NGAYXUAT) = 10 AND YEAR(PX.NGAYXUAT) = 2024
GROUP BY PX.MADT;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc phiếu xuất phát sinh trong tháng 10/2024 thành R1.
1. Bước 2: Kết nối R1 với CTPX qua MAPX để lấy số liều xuất.
1. Bước 3: Thực hiện phép gom nhóm γ theo thuộc tính MADT, tính hàm tổng SUM(SOLIEUXUAT) và đổi tên thành TONGLIEU.

**Barem chấm điểm đề xuất:**
- `time_filter_and_join`: 0.50đ
- `grouping_gamma_aggregate`: 0.50đ (Đúng thuộc tính gom nhóm và hàm SUM)

---

## Bài 02 [M01-Q2C5] — ĐSQH Phép Chia Tìm Điểm Tiêm Nhận Tất Cả Lô Vắc-Xin Của Moderna
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 9 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHACUNGCAP(MANCC, TENNCC, QUOCGIA, SDT), LOVACXIN(MALO, TENLO, TENKVACXIN, MANCC, NGAYSX, HSD, SOLIEU, DONGIA), DIEMTIEM(MADT, TENDT, QUAN, SUCCHUA, MATRP), PHIEUXUAT(MAPX, NGAYXUAT, MADT, TRANGTHAI), CTPX(MAPX, MALO, SOLIEUXUAT)`

### 1. Đề Bài
Tìm các điểm tiêm (MADT, TENDT) đã tiếp nhận tất cả các lô vắc-xin của nhà cung cấp có tên là 'Moderna' (TENNCC = 'Moderna').

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Moderna ← π_{MALO}(σ_{TENNCC = 'Moderna'}(NHACUNGCAP ⋈ LOVACXIN))
R_DiemTiem_Lo ← π_{MADT, MALO}(DIEMTIEM ⋈ PHIEUXUAT ⋈ CTPX)
R_Chia ← R_DiemTiem_Lo ÷ R_Moderna
KQ ← π_{MADT, TENDT}(R_Chia ⋈ DIEMTIEM)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT DT.MADT, DT.TENDT
FROM DIEMTIEM DT
WHERE NOT EXISTS (
    SELECT LV.MALO
    FROM LOVACXIN LV
    INNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC
    WHERE NCC.TENNCC = 'Moderna'
    EXCEPT
    SELECT CT.MALO
    FROM PHIEUXUAT PX
    INNER JOIN CTPX CT ON PX.MAPX = CT.MAPX
    WHERE PX.MADT = DT.MADT
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định tập mục tiêu (tập bị chia) R_Moderna: Chiếu lấy danh sách MALO thuộc nhà cung cấp 'Moderna'.
1. Bước 2: Xác định quan hệ tham gia R_DiemTiem_Lo: Chiếu lấy các cặp (MADT, MALO) thực tế đã xuất vắc-xin đến điểm tiêm.
1. Bước 3: Thực hiện phép chia hình thức R_Chia = R_DiemTiem_Lo ÷ R_Moderna. Kết quả trả về các MADT nhận đủ mọi MALO của Moderna.
1. Bước 4: Kết nối ngược với DIEMTIEM để lấy TENDT.

**Barem chấm điểm đề xuất:**
- `target_set_construction`: 0.25đ
- `candidate_relation_projection`: 0.25đ
- `division_operation`: 0.50đ (Đúng bản chất toán học của phép chia)

---

## Bài 03 [M01-Q2C6] — ĐSQH Tìm Điểm Tiêm Có Sức Chứa Lớn Nhất Tại Quận Thủ Đức
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DIEMTIEM(MADT, TENDT, QUAN, SUCCHUA, MATRP)`

### 1. Đề Bài
Cho biết điểm tiêm nào (MADT, TENDT) có sức chứa (SUCCHUA) lớn nhất trong số các điểm tiêm thuộc quận 'Thủ Đức'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R1 ← σ_{QUAN = 'Thủ Đức'}(DIEMTIEM)
R2 ← ρ_{DT1}(R1)
R3 ← ρ_{DT2}(R1)
R_KhongLonNhat ← π_{DT1.MADT}(R2 ⋈_{DT1.SUCCHUA < DT2.SUCCHUA} R3)
R_LonNhat ← π_{MADT}(R1) - R_KhongLonNhat
KQ ← π_{MADT, TENDT}(R_LonNhat ⋈ R1)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MADT, TENDT
FROM DIEMTIEM
WHERE QUAN = N'Thủ Đức'
  AND SUCCHUA = (SELECT MAX(SUCCHUA) FROM DIEMTIEM WHERE QUAN = N'Thủ Đức');
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc các điểm tiêm thuộc quận 'Thủ Đức' thành R1.
1. Bước 2: Phép tìm cực trị MAX trong ĐSQH bằng phương pháp loại trừ: Tự kết R1 với chính nó qua điều kiện SUCCHUA1 < SUCCHUA2.
1. Bước 3: Chiếu lấy DT1.MADT; đây là tập các điểm tiêm KHÔNG phải lớn nhất vì tồn tại điểm tiêm khác có sức chứa lớn hơn nó.
1. Bước 4: Lấy toàn bộ MADT của Thủ Đức trừ đi tập R_KhongLonNhat, thu được điểm tiêm có sức chứa lớn nhất (có thể có đồng hạng).

**Barem chấm điểm đề xuất:**
- `subquery_or_self_join`: 0.50đ
- `subtraction_or_max_logic`: 0.50đ

---

## Bài 04 [RA-D01] — ĐSQH Phép Chia Đơn Đặt Hàng Đặt Tất Cả Mặt Hàng Của 'Vinamilk'
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 9 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONDH(MADH, NGAYDH, MACC), CHITIET(MADH, MAMH, SOLUONG), CUNGCAP(MACC, MAMH), NHACC(MACC, TENCC)`

### 1. Đề Bài
Tìm các đơn đặt hàng (MADH) đã đặt tất cả các mặt hàng do nhà cung cấp có tên là 'Vinamilk' cung cấp.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Vinamilk ← π_{MAMH}(σ_{TENCC = 'Vinamilk'}(NHACC ⋈ CUNGCAP))
R_DH_MH ← π_{MADH, MAMH}(CHITIET)
KQ ← R_DH_MH ÷ R_Vinamilk
```
**Câu lệnh SQL tương đương:**
```sql
SELECT DH.MADH
FROM DONDH DH
WHERE NOT EXISTS (
    SELECT CC.MAMH
    FROM CUNGCAP CC
    INNER JOIN NHACC NC ON CC.MACC = NC.MACC
    WHERE NC.TENCC = 'Vinamilk'
    EXCEPT
    SELECT CT.MAMH
    FROM CHITIET CT
    WHERE CT.MADH = DH.MADH
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Tập chia R_Vinamilk là danh sách MAMH của NCC 'Vinamilk'.
1. Bước 2: Tập bị chia R_DH_MH là các cặp (MADH, MAMH) trong CHITIET.
1. Bước 3: Phép chia R_DH_MH ÷ R_Vinamilk cho ra MADH thỏa mãn.

**Barem chấm điểm đề xuất:**
- `division_algebra`: 0.50đ
- `equivalence_proof`: 0.50đ

---

## Bài 05 [RA-D03] — ĐSQH Gom Nhóm Doanh Thu Từng Sảnh Nhà Hàng White Palace
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 7 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SANH(MASANH, TENSANH, LOAIBAN, SUCCHUA), TIEC(MATIEC, MASANH, CHUTIEC, SOBAN, DONGIA)`

### 1. Đề Bài
Cho CSDL Nhà hàng: Tính tổng doanh thu theo từng sảnh tiệc. Thông tin hiển thị gồm: MASANH, TENSANH, DOANHTHU.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R1 ← SANH ⋈ TIEC
KQ ← _{MASANH, TENSANH} γ _{SUM(SOBAN * DONGIA) → DOANHTHU}(R1)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT S.MASANH, S.TENSANH, SUM(T.SOBAN * T.DONGIA) AS DOANHTHU
FROM SANH S
INNER JOIN TIEC T ON S.MASANH = T.MASANH
GROUP BY S.MASANH, S.TENSANH;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối sảnh với các tiệc được tổ chức tại sảnh.
1. Bước 2: Gom nhóm theo MASANH, TENSANH và tính SUM(SOBAN * DONGIA).

**Barem chấm điểm đề xuất:**
- `join_and_grouping`: 0.50đ
- `expression_calculation`: 0.50đ

---

## Bài 06 [RA-D02] — ĐSQH Phép Chia VĐV Tham Gia Tất Cả Kỳ Olympic Từ 2008
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `VDV(MAVDV, HOTEN, PHAI), THAMGIA(MAVDV, MATVH), THEVANHOI(MATVH, NAM)`

### 1. Đề Bài
Tìm VĐV Nữ (MAVDV, HOTEN) tham gia tất cả các kỳ thế vận hội từ năm 2008 tới nay.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Div ← R1 ÷ R2
KQ ← R_Div ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID FROM R1 WHERE NOT EXISTS (SELECT * FROM R2 WHERE NOT EXISTS (...));
```

**Các bước suy luận tư duy:**
1. Xác định tập chia
1. Xác định tập bị chia
1. Thực hiện phép chia hình thức hoặc gom nhóm.

**Barem chấm điểm đề xuất:**
- `division_grouping_logic`: 0.60đ
- `projection_result`: 0.40đ

---

## Bài 07 [RA-D04] — ĐSQH Tìm Loại Tài Khoản Được Mở Nhiều Nhất 2016
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TAIKHOAN(SOTK, MALTK, NGAYMO), LOAITK(MALTK, TENLTK)`

### 1. Đề Bài
Tìm loại tài khoản (MALTK, TENLTK) có số lượng tài khoản được mở nhiều nhất trong năm 2016.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Div ← R1 ÷ R2
KQ ← R_Div ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID FROM R1 WHERE NOT EXISTS (SELECT * FROM R2 WHERE NOT EXISTS (...));
```

**Các bước suy luận tư duy:**
1. Xác định tập chia
1. Xác định tập bị chia
1. Thực hiện phép chia hình thức hoặc gom nhóm.

**Barem chấm điểm đề xuất:**
- `division_grouping_logic`: 0.60đ
- `projection_result`: 0.40đ

---

## Bài 08 [RA-D05] — ĐSQH Gom Nhóm Đếm Số Đơn Hàng Theo Từng Khách Hàng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG(MAKH, HOTEN), DONHANG(MADH, MAKH, NGAYDH)`

### 1. Đề Bài
Tính tổng số đơn hàng đã đặt của từng khách hàng trong năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Div ← R1 ÷ R2
KQ ← R_Div ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID FROM R1 WHERE NOT EXISTS (SELECT * FROM R2 WHERE NOT EXISTS (...));
```

**Các bước suy luận tư duy:**
1. Xác định tập chia
1. Xác định tập bị chia
1. Thực hiện phép chia hình thức hoặc gom nhóm.

**Barem chấm điểm đề xuất:**
- `division_grouping_logic`: 0.60đ
- `projection_result`: 0.40đ

---

## Bài 09 [RA-D06] — ĐSQH Phép Chia Sinh Viên Học Tất Cả Các Môn Tiên Quyết
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SINHVIEN, KETQUA, MONTIENQUYET`

### 1. Đề Bài
Tìm sinh viên (MASV, HOTEN) đã hoàn thành tất cả các môn học tiên quyết của ngành.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Div ← R1 ÷ R2
KQ ← R_Div ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ID FROM R1 WHERE NOT EXISTS (SELECT * FROM R2 WHERE NOT EXISTS (...));
```

**Các bước suy luận tư duy:**
1. Xác định tập chia
1. Xác định tập bị chia
1. Thực hiện phép chia hình thức hoặc gom nhóm.

**Barem chấm điểm đề xuất:**
- `division_grouping_logic`: 0.60đ
- `projection_result`: 0.40đ

---

## Bài 10 [RA-D07] — ĐSQH Phép Chia (Tất Cả): Đơn Hàng & Mặt Hàng (Bài 7)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONHANG, CHITIET, MATHANG`

### 1. Đề Bài
Cho CSDL DONHANG, CHITIET, MATHANG. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: đơn hàng mua tất cả mặt hàng loại 'Điện tử'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 11 [RA-D08] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Bác Sĩ & Bệnh Nhân (Bài 8)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BACSI, PHUTRACH, BENHNHAN`

### 1. Đề Bài
Cho CSDL BACSI, PHUTRACH, BENHNHAN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 12 [RA-D09] — ĐSQH Phép Chia (Tất Cả): Học Viên & Khóa Học (Bài 9)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOCVIEN, DANGKY, KHOAHOC`

### 1. Đề Bài
Cho CSDL HOCVIEN, DANGKY, KHOAHOC. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: học viên hoàn thành tất cả khóa học nâng cao.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 13 [RA-D10] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Tàu & Cảng Biển (Bài 10)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TAU, CAPCANG, CANGBIEN`

### 1. Đề Bài
Cho CSDL TAU, CAPCANG, CANGBIEN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 14 [RA-D11] — ĐSQH Phép Chia (Tất Cả): Nhà Đầu Tư & Dự Án (Bài 11)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHA_DAUTU, GOPT_VON, DUAN`

### 1. Đề Bài
Cho CSDL NHA_DAUTU, GOPT_VON, DUAN. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: nhà đầu tư góp vốn vào tất cả dự án năng lượng xanh.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 15 [RA-D12] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Khách Hàng & Sảnh Tiệc (Bài 12)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACH, DATTIEC, SANHTIEC`

### 1. Đề Bài
Cho CSDL KHACH, DATTIEC, SANHTIEC. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 16 [RA-D13] — ĐSQH Phép Chia (Tất Cả): Độc Giả & Thể Loại Sách (Bài 13)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DOCGIA, MUONSACH, SACH, THELOAI`

### 1. Đề Bài
Cho CSDL DOCGIA, MUONSACH, SACH, THELOAI. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: độc giả đã mượn sách thuộc tất cả các thể loại khoa học.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 17 [RA-D14] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Điểm Tiêm & Vắc-Xin (Bài 14)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DIEMTIEM, PHIEUXUAT, CTPX, VACXIN`

### 1. Đề Bài
Cho CSDL DIEMTIEM, PHIEUXUAT, CTPX, VACXIN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 18 [RA-D15] — ĐSQH Phép Chia (Tất Cả): Đơn Hàng & Mặt Hàng (Bài 15)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONHANG, CHITIET, MATHANG`

### 1. Đề Bài
Cho CSDL DONHANG, CHITIET, MATHANG. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: đơn hàng mua tất cả mặt hàng loại 'Điện tử'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 19 [RA-D16] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Bác Sĩ & Bệnh Nhân (Bài 16)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BACSI, PHUTRACH, BENHNHAN`

### 1. Đề Bài
Cho CSDL BACSI, PHUTRACH, BENHNHAN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 20 [RA-D17] — ĐSQH Phép Chia (Tất Cả): Học Viên & Khóa Học (Bài 17)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOCVIEN, DANGKY, KHOAHOC`

### 1. Đề Bài
Cho CSDL HOCVIEN, DANGKY, KHOAHOC. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: học viên hoàn thành tất cả khóa học nâng cao.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 21 [RA-D18] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Tàu & Cảng Biển (Bài 18)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TAU, CAPCANG, CANGBIEN`

### 1. Đề Bài
Cho CSDL TAU, CAPCANG, CANGBIEN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 22 [RA-D19] — ĐSQH Phép Chia (Tất Cả): Nhà Đầu Tư & Dự Án (Bài 19)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHA_DAUTU, GOPT_VON, DUAN`

### 1. Đề Bài
Cho CSDL NHA_DAUTU, GOPT_VON, DUAN. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: nhà đầu tư góp vốn vào tất cả dự án năng lượng xanh.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 23 [RA-D20] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Khách Hàng & Sảnh Tiệc (Bài 20)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACH, DATTIEC, SANHTIEC`

### 1. Đề Bài
Cho CSDL KHACH, DATTIEC, SANHTIEC. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 24 [RA-D21] — ĐSQH Phép Chia (Tất Cả): Độc Giả & Thể Loại Sách (Bài 21)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DOCGIA, MUONSACH, SACH, THELOAI`

### 1. Đề Bài
Cho CSDL DOCGIA, MUONSACH, SACH, THELOAI. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: độc giả đã mượn sách thuộc tất cả các thể loại khoa học.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 25 [RA-D22] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Điểm Tiêm & Vắc-Xin (Bài 22)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DIEMTIEM, PHIEUXUAT, CTPX, VACXIN`

### 1. Đề Bài
Cho CSDL DIEMTIEM, PHIEUXUAT, CTPX, VACXIN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 26 [RA-D23] — ĐSQH Phép Chia (Tất Cả): Đơn Hàng & Mặt Hàng (Bài 23)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONHANG, CHITIET, MATHANG`

### 1. Đề Bài
Cho CSDL DONHANG, CHITIET, MATHANG. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: đơn hàng mua tất cả mặt hàng loại 'Điện tử'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 27 [RA-D24] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Bác Sĩ & Bệnh Nhân (Bài 24)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BACSI, PHUTRACH, BENHNHAN`

### 1. Đề Bài
Cho CSDL BACSI, PHUTRACH, BENHNHAN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 28 [RA-D25] — ĐSQH Phép Chia (Tất Cả): Học Viên & Khóa Học (Bài 25)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOCVIEN, DANGKY, KHOAHOC`

### 1. Đề Bài
Cho CSDL HOCVIEN, DANGKY, KHOAHOC. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: học viên hoàn thành tất cả khóa học nâng cao.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 29 [RA-D26] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Tàu & Cảng Biển (Bài 26)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TAU, CAPCANG, CANGBIEN`

### 1. Đề Bài
Cho CSDL TAU, CAPCANG, CANGBIEN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 30 [RA-D27] — ĐSQH Phép Chia (Tất Cả): Nhà Đầu Tư & Dự Án (Bài 27)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHA_DAUTU, GOPT_VON, DUAN`

### 1. Đề Bài
Cho CSDL NHA_DAUTU, GOPT_VON, DUAN. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: nhà đầu tư góp vốn vào tất cả dự án năng lượng xanh.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 31 [RA-D28] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Khách Hàng & Sảnh Tiệc (Bài 28)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACH, DATTIEC, SANHTIEC`

### 1. Đề Bài
Cho CSDL KHACH, DATTIEC, SANHTIEC. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 32 [RA-D29] — ĐSQH Phép Chia (Tất Cả): Độc Giả & Thể Loại Sách (Bài 29)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DOCGIA, MUONSACH, SACH, THELOAI`

### 1. Đề Bài
Cho CSDL DOCGIA, MUONSACH, SACH, THELOAI. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: độc giả đã mượn sách thuộc tất cả các thể loại khoa học.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 33 [RA-D30] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Điểm Tiêm & Vắc-Xin (Bài 30)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DIEMTIEM, PHIEUXUAT, CTPX, VACXIN`

### 1. Đề Bài
Cho CSDL DIEMTIEM, PHIEUXUAT, CTPX, VACXIN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 34 [RA-D31] — ĐSQH Phép Chia (Tất Cả): Đơn Hàng & Mặt Hàng (Bài 31)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONHANG, CHITIET, MATHANG`

### 1. Đề Bài
Cho CSDL DONHANG, CHITIET, MATHANG. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: đơn hàng mua tất cả mặt hàng loại 'Điện tử'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 35 [RA-D32] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Bác Sĩ & Bệnh Nhân (Bài 32)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BACSI, PHUTRACH, BENHNHAN`

### 1. Đề Bài
Cho CSDL BACSI, PHUTRACH, BENHNHAN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 36 [RA-D33] — ĐSQH Phép Chia (Tất Cả): Học Viên & Khóa Học (Bài 33)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOCVIEN, DANGKY, KHOAHOC`

### 1. Đề Bài
Cho CSDL HOCVIEN, DANGKY, KHOAHOC. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: học viên hoàn thành tất cả khóa học nâng cao.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 37 [RA-D34] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Tàu & Cảng Biển (Bài 34)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TAU, CAPCANG, CANGBIEN`

### 1. Đề Bài
Cho CSDL TAU, CAPCANG, CANGBIEN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 38 [RA-D35] — ĐSQH Phép Chia (Tất Cả): Nhà Đầu Tư & Dự Án (Bài 35)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHA_DAUTU, GOPT_VON, DUAN`

### 1. Đề Bài
Cho CSDL NHA_DAUTU, GOPT_VON, DUAN. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: nhà đầu tư góp vốn vào tất cả dự án năng lượng xanh.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 39 [RA-D36] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Khách Hàng & Sảnh Tiệc (Bài 36)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACH, DATTIEC, SANHTIEC`

### 1. Đề Bài
Cho CSDL KHACH, DATTIEC, SANHTIEC. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 40 [RA-D37] — ĐSQH Phép Chia (Tất Cả): Độc Giả & Thể Loại Sách (Bài 37)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DOCGIA, MUONSACH, SACH, THELOAI`

### 1. Đề Bài
Cho CSDL DOCGIA, MUONSACH, SACH, THELOAI. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: độc giả đã mượn sách thuộc tất cả các thể loại khoa học.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 41 [RA-D38] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Điểm Tiêm & Vắc-Xin (Bài 38)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DIEMTIEM, PHIEUXUAT, CTPX, VACXIN`

### 1. Đề Bài
Cho CSDL DIEMTIEM, PHIEUXUAT, CTPX, VACXIN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 42 [RA-D39] — ĐSQH Phép Chia (Tất Cả): Đơn Hàng & Mặt Hàng (Bài 39)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONHANG, CHITIET, MATHANG`

### 1. Đề Bài
Cho CSDL DONHANG, CHITIET, MATHANG. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: đơn hàng mua tất cả mặt hàng loại 'Điện tử'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 43 [RA-D40] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Bác Sĩ & Bệnh Nhân (Bài 40)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BACSI, PHUTRACH, BENHNHAN`

### 1. Đề Bài
Cho CSDL BACSI, PHUTRACH, BENHNHAN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 44 [RA-D41] — ĐSQH Phép Chia (Tất Cả): Học Viên & Khóa Học (Bài 41)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOCVIEN, DANGKY, KHOAHOC`

### 1. Đề Bài
Cho CSDL HOCVIEN, DANGKY, KHOAHOC. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: học viên hoàn thành tất cả khóa học nâng cao.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 45 [RA-D42] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Tàu & Cảng Biển (Bài 42)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TAU, CAPCANG, CANGBIEN`

### 1. Đề Bài
Cho CSDL TAU, CAPCANG, CANGBIEN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 46 [RA-D43] — ĐSQH Phép Chia (Tất Cả): Nhà Đầu Tư & Dự Án (Bài 43)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHA_DAUTU, GOPT_VON, DUAN`

### 1. Đề Bài
Cho CSDL NHA_DAUTU, GOPT_VON, DUAN. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: nhà đầu tư góp vốn vào tất cả dự án năng lượng xanh.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 47 [RA-D44] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Khách Hàng & Sảnh Tiệc (Bài 44)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACH, DATTIEC, SANHTIEC`

### 1. Đề Bài
Cho CSDL KHACH, DATTIEC, SANHTIEC. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 48 [RA-D45] — ĐSQH Phép Chia (Tất Cả): Độc Giả & Thể Loại Sách (Bài 45)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DOCGIA, MUONSACH, SACH, THELOAI`

### 1. Đề Bài
Cho CSDL DOCGIA, MUONSACH, SACH, THELOAI. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: độc giả đã mượn sách thuộc tất cả các thể loại khoa học.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 49 [RA-D46] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Điểm Tiêm & Vắc-Xin (Bài 46)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DIEMTIEM, PHIEUXUAT, CTPX, VACXIN`

### 1. Đề Bài
Cho CSDL DIEMTIEM, PHIEUXUAT, CTPX, VACXIN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 50 [RA-D47] — ĐSQH Phép Chia (Tất Cả): Đơn Hàng & Mặt Hàng (Bài 47)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONHANG, CHITIET, MATHANG`

### 1. Đề Bài
Cho CSDL DONHANG, CHITIET, MATHANG. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: đơn hàng mua tất cả mặt hàng loại 'Điện tử'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 51 [RA-D48] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Bác Sĩ & Bệnh Nhân (Bài 48)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BACSI, PHUTRACH, BENHNHAN`

### 1. Đề Bài
Cho CSDL BACSI, PHUTRACH, BENHNHAN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---

## Bài 52 [RA-D49] — ĐSQH Phép Chia (Tất Cả): Học Viên & Khóa Học (Bài 49)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOCVIEN, DANGKY, KHOAHOC`

### 1. Đề Bài
Cho CSDL HOCVIEN, DANGKY, KHOAHOC. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: học viên hoàn thành tất cả khóa học nâng cao.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));
```

**Các bước suy luận tư duy:**
1. Xác định tập mục tiêu hoặc thuộc tính gom nhóm
1. Thực hiện phép chia / gom nhóm
1. Chiếu kết quả.

**Barem chấm điểm đề xuất:**
- `logic_steps`: 0.60đ
- `correct_syntax`: 0.40đ

---
