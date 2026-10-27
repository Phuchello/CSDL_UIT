# CHUYÊN ĐỀ 3: PHÉP CHIA (TẤT CẢ / MỌI), GOM NHÓM & TRUY VẤN PHỨC HỢP
**Môn học:** IT004 — Cơ sở dữ liệu | **Hệ thống:** UIT Exam Mastery
**Biên soạn:** VÕ TRỌNG PHÚC | **Số lượng bài tập:** 52 bài

---

## Bài 01 [M01-Q2C4] — ĐSQH Gom Nhóm Tính Tổng Liều Vắc-Xin Đã Tiếp Nhận Theo Điểm Tiêm
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DIEMTIEM(MADT, TENDT, DIACHI, QUAN, SUCCHUA), PHIEUXUAT(MAPX, NGAYXUAT, TRANGTHAI, MADT), CTPX(MAPX, MALO, SOLIEUXUAT)`

### 1. Đề Bài
Tính tổng số liều vắc-xin đã tiếp nhận (SOLIEUXUAT, với TRANGTHAI = 1) theo từng điểm tiêm (MADT) trong tháng 10 năm 2024. Thông tin hiển thị gồm: MADT, TONGLIEU.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R1 ← σ_{NGAYXUAT ≥ '01/10/2024' ∧ NGAYXUAT ≤ '31/10/2024' ∧ TRANGTHAI = 1}(PHIEUXUAT)
R2 ← R1 ⋈ CTPX
KQ ← _{MADT} γ _{SUM(SOLIEUXUAT) → TONGLIEU}(R2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT PX.MADT, SUM(CT.SOLIEUXUAT) AS TONGLIEU
FROM PHIEUXUAT PX
INNER JOIN CTPX CT ON PX.MAPX = CT.MAPX
WHERE PX.NGAYXUAT >= '2024-10-01' AND PX.NGAYXUAT <= '2024-10-31' AND PX.TRANGTHAI = 1
GROUP BY PX.MADT;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc phiếu xuất phát sinh trong tháng 10/2024 và đã tiếp nhận thực tế (TRANGTHAI = 1).
1. Bước 2: Kết nối với CTPX qua MAPX để lấy số lượng liều xuất SOLIEUXUAT.
1. Bước 3: Thực hiện phép gom nhóm γ theo MADT và tính tổng SUM(SOLIEUXUAT) đổi tên thành TONGLIEU.

**Barem chấm điểm đề xuất:**
- `filtering_and_join`: 0.50đ
- `grouping_and_aggregation`: 0.50đ

---

## Bài 02 [M01-Q2C5] — ĐSQH Phép Chia Tìm Điểm Tiêm Đã Tiếp Nhận Tất Cả Lô Vắc-Xin Của Moderna
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHACUNGCAP(MANCC, TENNCC, QUOCGIA, SDT), LOVACXIN(MALO, TENLO, TENVACXIN, NGAYSX, HSD, SOLIEU, DONGIA, MANCC), DIEMTIEM(MADT, TENDT, DIACHI, QUAN, SUCCHUA), PHIEUXUAT(MAPX, NGAYXUAT, TRANGTHAI, MADT), CTPX(MAPX, MALO, SOLIEUXUAT)`

### 1. Đề Bài
Tìm các điểm tiêm (MADT, TENDT) đã tiếp nhận thực tế (TRANGTHAI = 1) tất cả các lô vắc-xin của nhà cung cấp có tên là 'Moderna' (TENNCC = 'Moderna').

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Moderna ← π_{MALO}(σ_{TENNCC = 'Moderna'}(NHACUNGCAP ⋈ LOVACXIN))
R_DT_Lo ← π_{MADT, MALO}((σ_{TRANGTHAI = 1}(PHIEUXUAT)) ⋈ CTPX)
R_Chia ← R_DT_Lo ÷ R_Moderna
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
    WHERE PX.MADT = DT.MADT AND PX.TRANGTHAI = 1
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Tập chia): Lấy tất cả MALO của nhà cung cấp 'Moderna'.
1. Bước 2 (Tập bị chia): Lấy các cặp (MADT, MALO) thực tế đã tiếp nhận (TRANGTHAI = 1).
1. Bước 3 (Phép chia): Thực hiện R_DT_Lo ÷ R_Moderna để tìm các MADT nhận đủ mọi lô.
1. Bước 4: Kết nối với DIEMTIEM để lấy TENDT.

**Barem chấm điểm đề xuất:**
- `dividing_set`: 0.25đ
- `divided_set_with_trangthai`: 0.25đ
- `division_and_result`: 0.50đ

---

## Bài 03 [M01-Q2C6] — ĐSQH Tìm Điểm Tiêm Có Sức Chứa Lớn Nhất Tại Quận Thủ Đức
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 9 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DIEMTIEM(MADT, TENDT, DIACHI, QUAN, SUCCHUA)`

### 1. Đề Bài
Cho biết điểm tiêm nào (MADT, TENDT) có sức chứa (SUCCHUA) lớn nhất trong số các điểm tiêm thuộc quận 'Thủ Đức' (xét cả trường hợp có nhiều điểm tiêm đồng hạng lớn nhất).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R1 ← σ_{QUAN = 'Thủ Đức'}(DIEMTIEM)
R2 ← ρ_{D1}(R1)
R3 ← ρ_{D2}(R1)
R_KoMax ← π_{D1.MADT}(R2 ⋈_{D1.SUCCHUA < D2.SUCCHUA} R3)
R_Max ← π_{MADT}(R1) - R_KoMax
KQ ← π_{MADT, TENDT}(R_Max ⋈ R1)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT MADT, TENDT
FROM DIEMTIEM
WHERE QUAN = N'Thủ Đức'
  AND SUCCHUA = (SELECT MAX(SUCCHUA) FROM DIEMTIEM WHERE QUAN = N'Thủ Đức');
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc điểm tiêm ở quận Thủ Đức thành R1.
1. Bước 2: Tự kết R1 so sánh bé hơn để tìm các điểm tiêm không phải lớn nhất (R_KoMax).
1. Bước 3: Dùng phép trừ tìm cực trị R_Max = R1 - R_KoMax (đảm bảo giữ lại toàn bộ các điểm tiêm đồng hạng).
1. Bước 4: Chiếu lấy MADT, TENDT.

**Barem chấm điểm đề xuất:**
- `self_join_inequality`: 0.50đ
- `set_difference_and_projection`: 0.50đ

---

## Bài 04 [M02-Q2C4] — ĐSQH Gom Nhóm Đếm Tổng Số Thiết Bị PCCC Theo Tòa Nhà
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 7 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TOANHA, TANG, THIETBI_PCCC`

### 1. Đề Bài
Tính tổng số lượng thiết bị PCCC (TONG_THIETBI) được bố trí tại mỗi tòa nhà. Thông tin hiển thị gồm: MATN, TENTN, TONG_THIETBI.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E1 ← TOANHA ⋈ TANG ⋈ THIETBI_PCCC
KQ ← _{MATN, TENTN}γ_{COUNT(MATB) → TONG_THIETBI}(E1)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT TN.MATN, TN.TENTN, COUNT(TB.MATB) AS TONG_THIETBI FROM TOANHA TN JOIN TANG T ON TN.MATN = T.MATN JOIN THIETBI_PCCC TB ON T.MATANG = TB.MATANG GROUP BY TN.MATN, TN.TENTN;
```

**Các bước suy luận tư duy:**
1. Kết nối 3 quan hệ để có thông tin tòa nhà và thiết bị
1. Gom nhóm theo tòa nhà và tính tổng

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ
- `projection`: 0.25đ

---

## Bài 05 [M02-Q2C5] — ĐSQH Phép Chia Tìm Đợt Kiểm Tra Đã Kiểm Tra Tất Cả Đầu Báo Khói
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DOT_KIEMTRA, CT_KIEMTRA, THIETBI_PCCC`

### 1. Đề Bài
Tìm các đợt kiểm tra (MADOT, NGAYKT, NGUOIKT) đã tiến hành kiểm tra tất cả các thiết bị PCCC thuộc loại 'Đầu báo khói'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R ← π_{MADOT, MATB}(CT_KIEMTRA)
S ← π_{MATB}(σ_{LOAITB='Đầu báo khói'}(THIETBI_PCCC))
R_KQ ← R ÷ S
KQ ← π_{MADOT, NGAYKT, NGUOIKT}(R_KQ ⋈ DOT_KIEMTRA)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT DK.MADOT, DK.NGAYKT, DK.NGUOIKT FROM DOT_KIEMTRA DK WHERE NOT EXISTS (SELECT * FROM THIETBI_PCCC TB WHERE TB.LOAITB = N'Đầu báo khói' AND NOT EXISTS (SELECT * FROM CT_KIEMTRA CT WHERE CT.MADOT = DK.MADOT AND CT.MATB = TB.MATB)) AND EXISTS (SELECT * FROM CT_KIEMTRA WHERE MADOT = DK.MADOT);
```

**Các bước suy luận tư duy:**
1. Xác định quan hệ R(MADOT, MATB)
1. Xác định tập chia S(MATB) gồm các đầu báo khói
1. Thực hiện phép chia R / S
1. Kết nối lấy thông tin chi tiết đợt kiểm tra

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ
- `projection`: 0.25đ

---

## Bài 06 [M02-Q2C6] — ĐSQH Tìm Tòa Nhà Có Số Lượng Căn Hộ Nhiều Nhất
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 8 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TOANHA, TANG, CANHO`

### 1. Đề Bài
Tìm thông tin tòa nhà (MATN, TENTN, SOTANG) có số lượng căn hộ nhiều nhất trong khu chung cư (bảo toàn tất cả các tòa nhà nếu có đồng hạng lớn nhất).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_Dem ← _{MATN}γ_{COUNT(MACANHO) → SOCAN}(TANG ⋈ CANHO)
R_NhoHon ← π_{R1.SOCAN}(σ_{R1.SOCAN < R2.SOCAN}(ρ_{R1}(R_Dem) × ρ_{R2}(R_Dem)))
R_Max ← π_{SOCAN}(R_Dem) - R_NhoHon
KQ ← π_{MATN, TENTN, SOTANG}(TOANHA ⋈ R_Dem ⋈ R_Max)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT TOP 1 WITH TIES TN.MATN, TN.TENTN, TN.SOTANG, COUNT(CH.MACANHO) AS SOCAN FROM TOANHA TN JOIN TANG T ON TN.MATN = T.MATN JOIN CANHO CH ON T.MATANG = CH.MATANG GROUP BY TN.MATN, TN.TENTN, TN.SOTANG ORDER BY COUNT(CH.MACANHO) DESC;
```

**Các bước suy luận tư duy:**
1. Gom nhóm tính số căn hộ từng tòa
1. Tìm giá trị không cực đại bằng tích Descartes
1. Lấy giá trị lớn nhất bảo toàn đồng hạng
1. Chiếu thông tin tòa nhà

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.35đ
- `projection`: 0.25đ

---

## Bài 07 [RA-D01] — ĐSQH Phép Chia Đơn Đặt Hàng Đặt Tất Cả Mặt Hàng Của 'Vinamilk'
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

## Bài 08 [RA-D03] — ĐSQH Gom Nhóm Doanh Thu Từng Sảnh Nhà Hàng White Palace
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

## Bài 09 [M06-Q2C4] — ĐSQH Gom Nhóm Tính Tổng Tiền Dịch Vụ Theo Phiếu Khám Tháng 10/2024
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEUKHAM(MAPK, NGAYKHAM, MABN, MABS, CHANDOAN), CHITIET_DV(MAPK, MADV, SOLUONG, DONGIA_THU, KETQUA)`

### 1. Đề Bài
Tính tổng số tiền dịch vụ cận lâm sàng đã chỉ định (TONG_TIEN_DV) của từng phiếu khám lập trong tháng 10/2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAPK, NGAYKHAM, TONG_TIEN_DV}(E_1 \bowtie \gamma_{MAPK, \text{SUM}(THANHTIEN) \to TONG_TIEN_DV}(E_2))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT pk.MAPK, pk.NGAYKHAM, SUM(ct.SOLUONG * ct.DONGIA_THU) AS TONG_TIEN_DV FROM PHIEUKHAM pk JOIN CHITIET_DV ct ON pk.MAPK = ct.MAPK WHERE pk.NGAYKHAM >= '2024-10-01' AND pk.NGAYKHAM <= '2024-10-31' GROUP BY pk.MAPK, pk.NGAYKHAM;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYKHAM \ge '2024-10-01' \wedge NGAYKHAM \le '2024-10-31'}(PHIEUKHAM)
1. E_2 = \pi_{MAPK, SOLUONG * DONGIA_THU \to THANHTIEN}(CHITIET_DV)
1. E_3 = \gamma_{MAPK, \text{SUM}(THANHTIEN) \to TONG_TIEN_DV}(E_2)
1. E_4 = E_1 \bowtie E_3
1. KQ = \pi_{MAPK, NGAYKHAM, TONG_TIEN_DV}(E_4)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 10 [M06-Q2C5] — ĐSQH Phép Chia Tìm Phiếu Khám Chỉ Định Tất Cả Dịch Vụ Chẩn Đoán Hình Ảnh
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEUKHAM(MAPK, NGAYKHAM, MABN, MABS, CHANDOAN), CHITIET_DV(MAPK, MADV, SOLUONG, DONGIA_THU, KETQUA), DICHVU_KHAM(MADV, TENDV, LOAIDV, DONGIA)`

### 1. Đề Bài
Tìm các phiếu khám (MAPK, NGAYKHAM, MABN) đã được chỉ định tất cả các dịch vụ y tế thuộc phân loại Chẩn đoán hình ảnh.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAPK, NGAYKHAM, MABN}((\pi_{MAPK, MADV}(CHITIET_DV) \div \pi_{MADV}(\sigma_{LOAIDV = 'Chẩn đoán hình ảnh'}(DICHVU_KHAM))) \bowtie PHIEUKHAM)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT pk.MAPK, pk.NGAYKHAM, pk.MABN FROM PHIEUKHAM pk WHERE EXISTS (SELECT 1 FROM CHITIET_DV ct WHERE ct.MAPK = pk.MAPK) AND NOT EXISTS (SELECT 1 FROM DICHVU_KHAM dv WHERE dv.LOAIDV = N'Chẩn đoán hình ảnh' AND NOT EXISTS (SELECT 1 FROM CHITIET_DV ct WHERE ct.MAPK = pk.MAPK AND ct.MADV = dv.MADV));
```

**Các bước suy luận tư duy:**
1. R = \pi_{MAPK, MADV}(CHITIET_DV)
1. S = \pi_{MADV}(\sigma_{LOAIDV = 'Chẩn đoán hình ảnh'}(DICHVU_KHAM))
1. E_{DIV} = R \div S
1. KQ = \pi_{MAPK, NGAYKHAM, MABN}(E_{DIV} \bowtie PHIEUKHAM)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 11 [M06-Q2C6] — ĐSQH Cực Trị Tìm Bác Sĩ Có Lượt Khám Nhiều Nhất Tháng 10/2024
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BACSI(MABS, HOTEN, HOCVI, MAKC, LUONG), PHIEUKHAM(MAPK, NGAYKHAM, MABN, MABS, CHANDOAN)`

### 1. Đề Bài
Tìm bác sĩ (MABS, HOTEN, HOCVI) đã thực hiện số lượng phiếu khám bệnh nhiều nhất trong tháng 10/2024 (bảo toàn tất cả các bác sĩ nếu đồng hạng).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MABS, HOTEN, HOCVI, SO_LUOT_KHAM}((E_{DEM} - \pi_{MABS, SO_LUOT_KHAM}(E_{DEM} \bowtie_{SO_LUOT_KHAM < SO_LUOT_KHAM2} \rho_{MABS2, SO_LUOT_KHAM2}(E_{DEM}))) \bowtie BACSI)
```
**Câu lệnh SQL tương đương:**
```sql
WITH ThongKe AS (SELECT MABS, COUNT(MAPK) AS SO_LUOT_KHAM FROM PHIEUKHAM WHERE NGAYKHAM >= '2024-10-01' AND NGAYKHAM <= '2024-10-31' GROUP BY MABS) SELECT bs.MABS, bs.HOTEN, bs.HOCVI, tk.SO_LUOT_KHAM FROM BACSI bs JOIN ThongKe tk ON bs.MABS = tk.MABS WHERE tk.SO_LUOT_KHAM = (SELECT MAX(SO_LUOT_KHAM) FROM ThongKe);
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYKHAM \ge '2024-10-01' \wedge NGAYKHAM \le '2024-10-31'}(PHIEUKHAM)
1. E_{DEM} = \gamma_{MABS, \text{COUNT}(MAPK) \to SO_LUOT_KHAM}(E_1)
1. E_{NHO_HON} = \pi_{MABS, SO_LUOT_KHAM}(E_{DEM} \bowtie_{SO_LUOT_KHAM < SO_LUOT_KHAM2} \rho_{MABS2, SO_LUOT_KHAM2}(E_{DEM}))
1. E_{MAX} = E_{DEM} - E_{NHO_HON}
1. KQ = \pi_{MABS, HOTEN, HOCVI, SO_LUOT_KHAM}(E_{MAX} \bowtie BACSI)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 12 [M07-Q2C4] — ĐSQH Gom Nhóm Tính Tổng Tiền Phạt Năm 2024 Theo Độc Giả
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEUMUON(MAPM, NGAYMUON, HANTRA, MADG, MATT, TRANGTHAI), CHITIET_MUON(MAPM, MASACH, NGAYTRA, TIENPHAT), DOCGIA(MADG, HOTEN, NGAYSINH, LOAIDG, MAKV)`

### 1. Đề Bài
Tính tổng số tiền phạt phát sinh (TONG_TIEN_PHAT) theo từng độc giả (MADG, HOTEN) đối với các lượt mượn trong năm 2024 có phát sinh tiền phạt (TIENPHAT > 0).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MADG, HOTEN, TONG_TIEN_PHAT}((\gamma_{MADG, \text{SUM}(TIENPHAT) \to TONG_TIEN_PHAT}(E_1 \bowtie \sigma_{TIENPHAT > 0}(CHITIET_MUON))) \bowtie DOCGIA)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT dg.MADG, dg.HOTEN, SUM(ct.TIENPHAT) AS TONG_TIEN_PHAT FROM PHIEUMUON pm JOIN CHITIET_MUON ct ON pm.MAPM = ct.MAPM JOIN DOCGIA dg ON pm.MADG = dg.MADG WHERE pm.NGAYMUON >= '2024-01-01' AND pm.NGAYMUON <= '2024-12-31' AND ct.TIENPHAT > 0 GROUP BY dg.MADG, dg.HOTEN;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYMUON \ge '2024-01-01' \wedge NGAYMUON \le '2024-12-31'}(PHIEUMUON)
1. E_2 = \sigma_{TIENPHAT > 0}(CHITIET_MUON)
1. E_3 = E_1 \bowtie E_2
1. E_4 = \gamma_{MADG, \text{SUM}(TIENPHAT) \to TONG_TIEN_PHAT}(E_3)
1. E_5 = E_4 \bowtie DOCGIA
1. KQ = \pi_{MADG, HOTEN, TONG_TIEN_PHAT}(E_5)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 13 [M07-Q2C5] — ĐSQH Phép Chia Tìm Độc Giả Mượn Tất Cả Sách Của Tác Giả Nguyễn Nhật Ánh
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEUMUON(MAPM, NGAYMUON, HANTRA, MADG, MATT, TRANGTHAI), CHITIET_MUON(MAPM, MASACH, NGAYTRA, TIENPHAT), SACH(MASACH, TENSACH, TACGIA, NXB, NAMXB, SOLUONGTON), DOCGIA(MADG, HOTEN, NGAYSINH, LOAIDG, MAKV)`

### 1. Đề Bài
Tìm các độc giả (MADG, HOTEN, LOAIDG) đã từng mượn tất cả các cuốn sách của tác giả Nguyễn Nhật Ánh.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MADG, HOTEN, LOAIDG}((\pi_{MADG, MASACH}(PHIEUMUON \bowtie CHITIET_MUON) \div \pi_{MASACH}(\sigma_{TACGIA = 'Nguyễn Nhật Ánh'}(SACH))) \bowtie DOCGIA)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT dg.MADG, dg.HOTEN, dg.LOAIDG FROM DOCGIA dg WHERE EXISTS (SELECT 1 FROM PHIEUMUON pm JOIN CHITIET_MUON ct ON pm.MAPM = ct.MAPM WHERE pm.MADG = dg.MADG) AND NOT EXISTS (SELECT 1 FROM SACH s WHERE s.TACGIA = N'Nguyễn Nhật Ánh' AND NOT EXISTS (SELECT 1 FROM PHIEUMUON pm2 JOIN CHITIET_MUON ct2 ON pm2.MAPM = ct2.MAPM WHERE pm2.MADG = dg.MADG AND ct2.MASACH = s.MASACH));
```

**Các bước suy luận tư duy:**
1. R = \pi_{MADG, MASACH}(PHIEUMUON \bowtie CHITIET_MUON)
1. S = \pi_{MASACH}(\sigma_{TACGIA = 'Nguyễn Nhật Ánh'}(SACH))
1. E_{DIV} = R \div S
1. KQ = \pi_{MADG, HOTEN, LOAIDG}(E_{DIV} \bowtie DOCGIA)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 14 [M07-Q2C6] — ĐSQH Cực Trị Tìm Sách Có Lượt Mượn Nhiều Nhất Năm 2024
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEUMUON(MAPM, NGAYMUON, HANTRA, MADG, MATT, TRANGTHAI), CHITIET_MUON(MAPM, MASACH, NGAYTRA, TIENPHAT), SACH(MASACH, TENSACH, TACGIA, NXB, NAMXB, SOLUONGTON)`

### 1. Đề Bài
Tìm cuốn sách (MASACH, TENSACH, TACGIA) có số lượt mượn nhiều nhất trong năm 2024 (bảo toàn tất cả các cuốn sách nếu đồng hạng).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MASACH, TENSACH, TACGIA, SO_LUOT_MUON}((E_{DEM} - \pi_{MASACH, SO_LUOT_MUON}(E_{DEM} \bowtie_{SO_LUOT_MUON < SO_LUOT_MUON2} \rho_{MASACH2, SO_LUOT_MUON2}(E_{DEM}))) \bowtie SACH)
```
**Câu lệnh SQL tương đương:**
```sql
WITH ThongKe AS (SELECT ct.MASACH, COUNT(pm.MAPM) AS SO_LUOT_MUON FROM PHIEUMUON pm JOIN CHITIET_MUON ct ON pm.MAPM = ct.MAPM WHERE pm.NGAYMUON >= '2024-01-01' AND pm.NGAYMUON <= '2024-12-31' GROUP BY ct.MASACH) SELECT s.MASACH, s.TENSACH, s.TACGIA, tk.SO_LUOT_MUON FROM SACH s JOIN ThongKe tk ON s.MASACH = tk.MASACH WHERE tk.SO_LUOT_MUON = (SELECT MAX(SO_LUOT_MUON) FROM ThongKe);
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYMUON \ge '2024-01-01' \wedge NGAYMUON \le '2024-12-31'}(PHIEUMUON)
1. E_2 = E_1 \bowtie CHITIET_MUON
1. E_{DEM} = \gamma_{MASACH, \text{COUNT}(MAPM) \to SO_LUOT_MUON}(E_2)
1. E_{NHO_HON} = \pi_{MASACH, SO_LUOT_MUON}(E_{DEM} \bowtie_{SO_LUOT_MUON < SO_LUOT_MUON2} \rho_{MASACH2, SO_LUOT_MUON2}(E_{DEM}))
1. E_{MAX} = E_{DEM} - E_{NHO_HON}
1. KQ = \pi_{MASACH, TENSACH, TACGIA, SO_LUOT_MUON}(E_{MAX} \bowtie SACH)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 15 [M08-Q2C4] — ĐSQH Gom Nhóm Tính Tổng Tiền Đơn Hàng Đã Giao Tháng 11/2024
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONHANG(MADH, NGAYDAT, MAKH, HINHTHUCTT, TRANGTHAI), CHITIET_DH(MADH, MASP, SOLUONG, DONGIA_BAN)`

### 1. Đề Bài
Tính tổng giá trị tiền hàng (TONG_TIEN_HANG) của từng đơn hàng (MADH, NGAYDAT) đặt trong tháng 11/2024 có trạng thái Đã giao.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MADH, NGAYDAT, TONG_TIEN_HANG}(E_1 \bowtie \gamma_{MADH, \text{SUM}(THANHTIEN) \to TONG_TIEN_HANG}(E_2))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT dh.MADH, dh.NGAYDAT, SUM(ct.SOLUONG * ct.DONGIA_BAN) AS TONG_TIEN_HANG FROM DONHANG dh JOIN CHITIET_DH ct ON dh.MADH = ct.MADH WHERE dh.NGAYDAT >= '2024-11-01' AND dh.NGAYDAT <= '2024-11-30' AND dh.TRANGTHAI = N'Đã giao' GROUP BY dh.MADH, dh.NGAYDAT;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYDAT \ge '2024-11-01' \wedge NGAYDAT \le '2024-11-30' \wedge TRANGTHAI = 'Đã giao'}(DONHANG)
1. E_2 = \pi_{MADH, SOLUONG * DONGIA_BAN \to THANHTIEN}(CHITIET_DH)
1. E_3 = \gamma_{MADH, \text{SUM}(THANHTIEN) \to TONG_TIEN_HANG}(E_2)
1. E_4 = E_1 \bowtie E_3
1. KQ = \pi_{MADH, NGAYDAT, TONG_TIEN_HANG}(E_4)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 16 [M08-Q2C5] — ĐSQH Phép Chia Tìm Đơn Hàng Mua Tất Cả Sản Phẩm Gia Dụng Của Gian Hàng Gia Dụng Thông Minh
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONHANG(MADH, NGAYDAT, MAKH, HINHTHUCTT, TRANGTHAI), CHITIET_DH(MADH, MASP, SOLUONG, DONGIA_BAN), SANPHAM(MASP, TENSP, LOAISP, GIANIEMYET, MAGH), GIANHANG(MAGH, TENGH, NGUOIDAIDIEN, THANHPHO)`

### 1. Đề Bài
Tìm các đơn hàng (MADH, NGAYDAT, MAKH) đã đặt mua tất cả các sản phẩm thuộc phân loại Gia dụng do gian hàng Gia Dụng Thông Minh cung ứng.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MADH, NGAYDAT, MAKH}((\pi_{MADH, MASP}(CHITIET_DH) \div \pi_{MASP}(\sigma_{LOAISP = 'Gia dụng'}(SANPHAM) \bowtie \sigma_{TENGH = 'Gia Dụng Thông Minh'}(GIANHANG))) \bowtie DONHANG)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT dh.MADH, dh.NGAYDAT, dh.MAKH FROM DONHANG dh WHERE EXISTS (SELECT 1 FROM CHITIET_DH ct WHERE ct.MADH = dh.MADH) AND NOT EXISTS (SELECT 1 FROM SANPHAM sp JOIN GIANHANG gh ON sp.MAGH = gh.MAGH WHERE sp.LOAISP = N'Gia dụng' AND gh.TENGH = N'Gia Dụng Thông Minh' AND NOT EXISTS (SELECT 1 FROM CHITIET_DH ct2 WHERE ct2.MADH = dh.MADH AND ct2.MASP = sp.MASP));
```

**Các bước suy luận tư duy:**
1. R = \pi_{MADH, MASP}(CHITIET_DH)
1. S = \pi_{MASP}(\sigma_{LOAISP = 'Gia dụng'}(SANPHAM) \bowtie \sigma_{TENGH = 'Gia Dụng Thông Minh'}(GIANHANG))
1. E_{DIV} = R \div S
1. KQ = \pi_{MADH, NGAYDAT, MAKH}(E_{DIV} \bowtie DONHANG)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 17 [M08-Q2C6] — ĐSQH Cực Trị Tìm Khách Hàng Có Tổng Số Lượng Sản Phẩm Mua Nhiều Nhất Tháng 11/2024
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONHANG(MADH, NGAYDAT, MAKH, HINHTHUCTT, TRANGTHAI), CHITIET_DH(MADH, MASP, SOLUONG, DONGIA_BAN), KHACHHANG(MAKH, HOTEN, DIACHI, HANGTHANHVIEN)`

### 1. Đề Bài
Tìm khách hàng (MAKH, HOTEN, HANGTHANHVIEN) có tổng số lượng sản phẩm đã mua nhiều nhất trong tháng 11/2024 (bảo toàn tất cả các khách hàng nếu đồng hạng).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAKH, HOTEN, HANGTHANHVIEN, TONG_SOLUONG}((E_{DEM} - \pi_{MAKH, TONG_SOLUONG}(E_{DEM} \bowtie_{TONG_SOLUONG < TONG_SOLUONG2} \rho_{MAKH2, TONG_SOLUONG2}(E_{DEM}))) \bowtie KHACHHANG)
```
**Câu lệnh SQL tương đương:**
```sql
WITH ThongKe AS (SELECT dh.MAKH, SUM(ct.SOLUONG) AS TONG_SOLUONG FROM DONHANG dh JOIN CHITIET_DH ct ON dh.MADH = ct.MADH WHERE dh.NGAYDAT >= '2024-11-01' AND dh.NGAYDAT <= '2024-11-30' GROUP BY dh.MAKH) SELECT kh.MAKH, kh.HOTEN, kh.HANGTHANHVIEN, tk.TONG_SOLUONG FROM KHACHHANG kh JOIN ThongKe tk ON kh.MAKH = tk.MAKH WHERE tk.TONG_SOLUONG = (SELECT MAX(TONG_SOLUONG) FROM ThongKe);
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYDAT \ge '2024-11-01' \wedge NGAYDAT \le '2024-11-30'}(DONHANG) \bowtie CHITIET_DH
1. E_{DEM} = \gamma_{MAKH, \text{SUM}(SOLUONG) \to TONG_SOLUONG}(E_1)
1. E_{NHO_HON} = \pi_{MAKH, TONG_SOLUONG}(E_{DEM} \bowtie_{TONG_SOLUONG < TONG_SOLUONG2} \rho_{MAKH2, TONG_SOLUONG2}(E_{DEM}))
1. E_{MAX} = E_{DEM} - E_{NHO_HON}
1. KQ = \pi_{MAKH, HOTEN, HANGTHANHVIEN, TONG_SOLUONG}(E_{MAX} \bowtie KHACHHANG)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 18 [M09-Q2C4] — ĐSQH Gom Nhóm Tính Tổng Tiền Thưởng Đội Thắng Tháng 11/2024
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TRANDAU(MATRAN, NGAYDAU, VONGDAU, DIADIEM), THAMGIA_TRAN(MATRAN, MADOI, SOVANTHANG, TIENTHUONG, KETQUA), DOITHI(MADOI, TENDOI, MATRUONG, NGUOIQUANLY)`

### 1. Đề Bài
Tính tổng tiền thưởng (TONG_TIEN_THUONG) của từng đội thi (MADOI, TENDOI) đạt được từ các trận đấu có kết quả Thắng trong tháng 11/2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MADOI, TENDOI, TONG_TIEN_THUONG}((\gamma_{MADOI, \text{SUM}(TIENTHUONG) \to TONG_TIEN_THUONG}(E_1 \bowtie \sigma_{KETQUA = 'Thắng'}(THAMGIA_TRAN))) \bowtie DOITHI)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT dt.MADOI, dt.TENDOI, SUM(tgt.TIENTHUONG) AS TONG_TIEN_THUONG FROM TRANDAU td JOIN THAMGIA_TRAN tgt ON td.MATRAN = tgt.MATRAN JOIN DOITHI dt ON tgt.MADOI = dt.MADOI WHERE td.NGAYDAU >= '2024-11-01' AND td.NGAYDAU <= '2024-11-30' AND tgt.KETQUA = N'Thắng' GROUP BY dt.MADOI, dt.TENDOI;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYDAU \ge '2024-11-01' \wedge NGAYDAU \le '2024-11-30'}(TRANDAU)
1. E_2 = \sigma_{KETQUA = 'Thắng'}(THAMGIA_TRAN)
1. E_3 = E_1 \bowtie E_2
1. E_4 = \gamma_{MADOI, \text{SUM}(TIENTHUONG) \to TONG_TIEN_THUONG}(E_3)
1. E_5 = E_4 \bowtie DOITHI
1. KQ = \pi_{MADOI, TENDOI, TONG_TIEN_THUONG}(E_5)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 19 [M09-Q2C5] — ĐSQH Phép Chia Tìm Đội Thi Đấu Tại Tất Cả Địa Điểm Vòng Bảng
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TRANDAU(MATRAN, NGAYDAU, VONGDAU, DIADIEM), THAMGIA_TRAN(MATRAN, MADOI, SOVANTHANG, TIENTHUONG, KETQUA), DOITHI(MADOI, TENDOI, MATRUONG, NGUOIQUANLY)`

### 1. Đề Bài
Tìm các đội thi (MADOI, TENDOI, MATRUONG) đã từng tham gia thi đấu tại tất cả các địa điểm thuộc vòng đấu Vòng bảng.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MADOI, TENDOI, MATRUONG}((\pi_{MADOI, DIADIEM}(THAMGIA_TRAN \bowtie TRANDAU) \div \pi_{DIADIEM}(\sigma_{VONGDAU = 'Vòng bảng'}(TRANDAU))) \bowtie DOITHI)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT dt.MADOI, dt.TENDOI, dt.MATRUONG FROM DOITHI dt WHERE EXISTS (SELECT 1 FROM THAMGIA_TRAN tgt WHERE tgt.MADOI = dt.MADOI) AND NOT EXISTS (SELECT 1 FROM TRANDAU td WHERE td.VONGDAU = N'Vòng bảng' AND NOT EXISTS (SELECT 1 FROM THAMGIA_TRAN tgt2 JOIN TRANDAU td2 ON tgt2.MATRAN = td2.MATRAN WHERE tgt2.MADOI = dt.MADOI AND td2.DIADIEM = td.DIADIEM));
```

**Các bước suy luận tư duy:**
1. R = \pi_{MADOI, DIADIEM}(THAMGIA_TRAN \bowtie TRANDAU)
1. S = \pi_{DIADIEM}(\sigma_{VONGDAU = 'Vòng bảng'}(TRANDAU))
1. E_{DIV} = R \div S
1. KQ = \pi_{MADOI, TENDOI, MATRUONG}(E_{DIV} \bowtie DOITHI)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 20 [M09-Q2C6] — ĐSQH Cực Trị Tìm Đội Thi Có Tổng Số Ván Thắng Nhiều Nhất Năm 2024
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `TRANDAU(MATRAN, NGAYDAU, VONGDAU, DIADIEM), THAMGIA_TRAN(MATRAN, MADOI, SOVANTHANG, TIENTHUONG, KETQUA), DOITHI(MADOI, TENDOI, MATRUONG, NGUOIQUANLY), TRUONG(MATRUONG, TENTRUONG, THANHPHO)`

### 1. Đề Bài
Tìm đội thi (MADOI, TENDOI, TENTRUONG) có tổng số ván thắng nhiều nhất trong toàn bộ giải đấu năm 2024 (bảo toàn tất cả các đội thi nếu đồng hạng).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MADOI, TENDOI, TENTRUONG, TONG_SO_VAN_THANG}(((E_{DEM} - \pi_{MADOI, TONG_SO_VAN_THANG}(E_{DEM} \bowtie_{TONG_SO_VAN_THANG < TONG_SO_VAN_THANG2} \rho_{MADOI2, TONG_SO_VAN_THANG2}(E_{DEM}))) \bowtie DOITHI) \bowtie TRUONG)
```
**Câu lệnh SQL tương đương:**
```sql
WITH ThongKe AS (SELECT tgt.MADOI, SUM(tgt.SOVANTHANG) AS TONG_SO_VAN_THANG FROM TRANDAU td JOIN THAMGIA_TRAN tgt ON td.MATRAN = tgt.MATRAN WHERE td.NGAYDAU >= '2024-01-01' AND td.NGAYDAU <= '2024-12-31' GROUP BY tgt.MADOI) SELECT dt.MADOI, dt.TENDOI, tr.TENTRUONG, tk.TONG_SO_VAN_THANG FROM DOITHI dt JOIN TRUONG tr ON dt.MATRUONG = tr.MATRUONG JOIN ThongKe tk ON dt.MADOI = tk.MADOI WHERE tk.TONG_SO_VAN_THANG = (SELECT MAX(TONG_SO_VAN_THANG) FROM ThongKe);
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYDAU \ge '2024-01-01' \wedge NGAYDAU \le '2024-12-31'}(TRANDAU) \bowtie THAMGIA_TRAN
1. E_{DEM} = \gamma_{MADOI, \text{SUM}(SOVANTHANG) \to TONG_SO_VAN_THANG}(E_1)
1. E_{NHO_HON} = \pi_{MADOI, TONG_SO_VAN_THANG}(E_{DEM} \bowtie_{TONG_SO_VAN_THANG < TONG_SO_VAN_THANG2} \rho_{MADOI2, TONG_SO_VAN_THANG2}(E_{DEM}))
1. E_{MAX} = E_{DEM} - E_{NHO_HON}
1. KQ = \pi_{MADOI, TENDOI, TENTRUONG, TONG_SO_VAN_THANG}(E_{MAX} \bowtie DOITHI \bowtie TRUONG)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.60đ
- `intermediate_steps`: 0.60đ

---

## Bài 21 [M10-Q2C4] — ĐSQH Gom Nhóm Tính Tổng Tiền Phụ Tùng Phiếu Hoàn Thành Tháng 11/2024
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEU_BD(MAPHIEU, NGAYLAP, BIENSO, MATHO, TONGTIEN, TRANGTHAI), CHITIET_BD(MAPHIEU, MAPT, SOLUONG, TIENCONG), PHUTUNG(MAPT, TENPT, LOAIPT, DONGIA, SOLUONGTON)`

### 1. Đề Bài
Tính tổng chi phí phụ tùng thay thế (TONG_TIEN_PHU_TUNG) của từng phiếu bảo dưỡng (MAPHIEU, NGAYLAP) lập trong tháng 11/2024 có trạng thái Đã hoàn thành.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAPHIEU, NGAYLAP, TONG_TIEN_PHU_TUNG}(E_1 \bowtie \gamma_{MAPHIEU, \text{SUM}(THANHTIEN) \to TONG_TIEN_PHU_TUNG}(\pi_{MAPHIEU, SOLUONG * DONGIA \to THANHTIEN}(CHITIET_BD \bowtie PHUTUNG)))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT pbd.MAPHIEU, pbd.NGAYLAP, SUM(ct.SOLUONG * pt.DONGIA) AS TONG_TIEN_PHU_TUNG FROM PHIEU_BD pbd JOIN CHITIET_BD ct ON pbd.MAPHIEU = ct.MAPHIEU JOIN PHUTUNG pt ON ct.MAPT = pt.MAPT WHERE pbd.NGAYLAP >= '2024-11-01' AND pbd.NGAYLAP <= '2024-11-30' AND pbd.TRANGTHAI = N'Đã hoàn thành' GROUP BY pbd.MAPHIEU, pbd.NGAYLAP;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYLAP \ge '2024-11-01' \wedge NGAYLAP \le '2024-11-30' \wedge TRANGTHAI = 'Đã hoàn thành'}(PHIEU_BD)
1. E_2 = CHITIET_BD \bowtie PHUTUNG
1. E_3 = \pi_{MAPHIEU, SOLUONG * DONGIA \to THANHTIEN}(E_2)
1. E_4 = \gamma_{MAPHIEU, \text{SUM}(THANHTIEN) \to TONG_TIEN_PHU_TUNG}(E_3)
1. E_5 = E_1 \bowtie E_4
1. KQ = \pi_{MAPHIEU, NGAYLAP, TONG_TIEN_PHU_TUNG}(E_5)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 22 [M10-Q2C5] — ĐSQH Phép Chia Tìm Xe Thay Thế Tất Cả Phụ Tùng Loại Dầu Nhớt
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEU_BD(MAPHIEU, NGAYLAP, BIENSO, MATHO, TONGTIEN, TRANGTHAI), CHITIET_BD(MAPHIEU, MAPT, SOLUONG, TIENCONG), PHUTUNG(MAPT, TENPT, LOAIPT, DONGIA, SOLUONGTON), XE(BIENSO, HANGXE, MODEL, NAMSX, MAKH)`

### 1. Đề Bài
Tìm các xe ô tô (BIENSO, HANGXE, MAKH) đã từng sử dụng/thay thế tất cả các phụ tùng thuộc loại Dầu nhớt của gara.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{BIENSO, HANGXE, MAKH}((\pi_{BIENSO, MAPT}(PHIEU_BD \bowtie CHITIET_BD) \div \pi_{MAPT}(\sigma_{LOAIPT = 'Dầu nhớt'}(PHUTUNG))) \bowtie XE)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT x.BIENSO, x.HANGXE, x.MAKH FROM XE x WHERE EXISTS (SELECT 1 FROM PHIEU_BD pbd JOIN CHITIET_BD ct ON pbd.MAPHIEU = ct.MAPHIEU WHERE pbd.BIENSO = x.BIENSO) AND NOT EXISTS (SELECT 1 FROM PHUTUNG pt WHERE pt.LOAIPT = N'Dầu nhớt' AND NOT EXISTS (SELECT 1 FROM PHIEU_BD pbd2 JOIN CHITIET_BD ct2 ON pbd2.MAPHIEU = ct2.MAPHIEU WHERE pbd2.BIENSO = x.BIENSO AND ct2.MAPT = pt.MAPT));
```

**Các bước suy luận tư duy:**
1. R = \pi_{BIENSO, MAPT}(PHIEU_BD \bowtie CHITIET_BD)
1. S = \pi_{MAPT}(\sigma_{LOAIPT = 'Dầu nhớt'}(PHUTUNG))
1. E_{DIV} = R \div S
1. KQ = \pi_{BIENSO, HANGXE, MAKH}(E_{DIV} \bowtie XE)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 23 [M10-Q2C6] — ĐSQH Cực Trị Tìm Phụ Tùng Có Tổng Số Lượng Sử Dụng Nhiều Nhất Năm 2024
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEU_BD(MAPHIEU, NGAYLAP, BIENSO, MATHO, TONGTIEN, TRANGTHAI), CHITIET_BD(MAPHIEU, MAPT, SOLUONG, TIENCONG), PHUTUNG(MAPT, TENPT, LOAIPT, DONGIA, SOLUONGTON)`

### 1. Đề Bài
Tìm phụ tùng (MAPT, TENPT, LOAIPT) có tổng số lượng sử dụng thay thế nhiều nhất trong toàn bộ các phiếu bảo dưỡng năm 2024 (bảo toàn tất cả phụ tùng nếu đồng hạng).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAPT, TENPT, LOAIPT, TONG_SOLUONG}((E_{DEM} - \pi_{MAPT, TONG_SOLUONG}(E_{DEM} \bowtie_{TONG_SOLUONG < TONG_SOLUONG2} \rho_{MAPT2, TONG_SOLUONG2}(E_{DEM}))) \bowtie PHUTUNG)
```
**Câu lệnh SQL tương đương:**
```sql
WITH ThongKe AS (SELECT ct.MAPT, SUM(ct.SOLUONG) AS TONG_SOLUONG FROM PHIEU_BD pbd JOIN CHITIET_BD ct ON pbd.MAPHIEU = ct.MAPHIEU WHERE pbd.NGAYLAP >= '2024-01-01' AND pbd.NGAYLAP <= '2024-12-31' GROUP BY ct.MAPT) SELECT pt.MAPT, pt.TENPT, pt.LOAIPT, tk.TONG_SOLUONG FROM PHUTUNG pt JOIN ThongKe tk ON pt.MAPT = tk.MAPT WHERE tk.TONG_SOLUONG = (SELECT MAX(TONG_SOLUONG) FROM ThongKe);
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYLAP \ge '2024-01-01' \wedge NGAYLAP \le '2024-12-31'}(PHIEU_BD) \bowtie CHITIET_BD
1. E_{DEM} = \gamma_{MAPT, \text{SUM}(SOLUONG) \to TONG_SOLUONG}(E_1)
1. E_{NHO_HON} = \pi_{MAPT, TONG_SOLUONG}(E_{DEM} \bowtie_{TONG_SOLUONG < TONG_SOLUONG2} \rho_{MAPT2, TONG_SOLUONG2}(E_{DEM}))
1. E_{MAX} = E_{DEM} - E_{NHO_HON}
1. KQ = \pi_{MAPT, TENPT, LOAIPT, TONG_SOLUONG}(E_{MAX} \bowtie PHUTUNG)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 24 [RA-D02] — ĐSQH Phép Chia VĐV Tham Gia Tất Cả Kỳ Olympic Từ 2008
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

## Bài 25 [M11-Q2C4] — ĐSQH Gom Nhóm Tính Tổng Giá Trị Xuất Hàng Tháng 11/2024 Đã Giao
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEUXUAT(MAPX, NGAYXUAT, MACH, TONGTIEN, TRANGTHAI), CHITIET_PX(MAPX, MANL, SOLUONG, DONGIA_XUAT)`

### 1. Đề Bài
Tính tổng giá trị xuất hàng thực tế (TONG_GIA_TRI_XUAT = SUM(SOLUONG * DONGIA_XUAT)) của từng phiếu xuất kho (MAPX, NGAYXUAT) lập trong tháng 11 năm 2024 có trạng thái là 'Đã giao'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAPX, NGAYXUAT, TONG_GIA_TRI_XUAT}(E_1 \bowtie \gamma_{MAPX, \text{SUM}(THANHTIEN) \to TONG_GIA_TRI_XUAT}(\pi_{MAPX, SOLUONG * DONGIA_XUAT \to THANHTIEN}(CHITIET_PX)))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT px.MAPX, px.NGAYXUAT, SUM(ct.SOLUONG * ct.DONGIA_XUAT) AS TONG_GIA_TRI_XUAT FROM PHIEUXUAT px JOIN CHITIET_PX ct ON px.MAPX = ct.MAPX WHERE px.NGAYXUAT >= '2024-11-01' AND px.NGAYXUAT <= '2024-11-30' AND px.TRANGTHAI = N'Đã giao' GROUP BY px.MAPX, px.NGAYXUAT;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYXUAT \ge '2024-11-01' \wedge NGAYXUAT \le '2024-11-30' \wedge TRANGTHAI = 'Đã giao'}(PHIEUXUAT)
1. E_2 = \pi_{MAPX, SOLUONG * DONGIA_XUAT \to THANHTIEN}(CHITIET_PX)
1. E_3 = \gamma_{MAPX, \text{SUM}(THANHTIEN) \to TONG_GIA_TRI_XUAT}(E_2)
1. E_4 = E_1 \bowtie E_3
1. KQ = \pi_{MAPX, NGAYXUAT, TONG_GIA_TRI_XUAT}(E_4)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 26 [M12-Q2C4] — ĐSQH Gom Nhóm Doanh Thu Vé Đã Thanh Toán Tháng 11/2024
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SUATCHIEU(MASC, MAPHIM, MAPC, NGAYCHIEU, GIOCHIEU, GIAVE_CHUAN), VEXEM(MAVE, MASC, MAKH, SOGHE, GIAVE_THUC, TRANGTHAI)`

### 1. Đề Bài
Tính tổng doanh thu thực tế bán vé (TONG_DOANHTHU = SUM(GIAVE_THUC)) của từng suất chiếu (MASC, NGAYCHIEU) diễn ra trong tháng 11 năm 2024 có trạng thái vé là 'Đã thanh toán'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MASC, NGAYCHIEU, TONG_DOANHTHU}(E_1 \bowtie \gamma_{MASC, \text{SUM}(GIAVE_THUC) \to TONG_DOANHTHU}(E_2))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT sc.MASC, sc.NGAYCHIEU, SUM(vx.GIAVE_THUC) AS TONG_DOANHTHU FROM SUATCHIEU sc JOIN VEXEM vx ON sc.MASC = vx.MASC WHERE sc.NGAYCHIEU >= '2024-11-01' AND sc.NGAYCHIEU <= '2024-11-30' AND vx.TRANGTHAI = N'Đã thanh toán' GROUP BY sc.MASC, sc.NGAYCHIEU;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYCHIEU \ge '2024-11-01' \wedge NGAYCHIEU \le '2024-11-30'}(SUATCHIEU)
1. E_2 = \sigma_{TRANGTHAI = 'Đã thanh toán'}(VEXEM)
1. E_3 = \gamma_{MASC, \text{SUM}(GIAVE_THUC) \to TONG_DOANHTHU}(E_2)
1. E_4 = E_1 \bowtie E_3
1. KQ = \pi_{MASC, NGAYCHIEU, TONG_DOANHTHU}(E_4)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 27 [M13-Q2C4] — ĐSQH Gom Nhóm Số Khách Phục Vụ Của Phương Tiện Ngày 20/11/2024
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHUONGTIEN(MAPT, BIENSO, SOGHE, NAMSX, MATUYEN), CHUYEN_DI(MACHUYEN, MAPT, NGAYCHAY, GIOXUATPHAT, SOLUONG_KHACH, DOANHTHU)`

### 1. Đề Bài
Tính tổng số lượng hành khách phục vụ (TONG_KHACH = SUM(SOLUONG_KHACH)) của từng phương tiện (MAPT, BIENSO) thực hiện các chuyến đi trong ngày 20 tháng 11 năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAPT, BIENSO, TONG_KHACH}(PHUONGTIEN \bowtie \gamma_{MAPT, \text{SUM}(SOLUONG_KHACH) \to TONG_KHACH}(\sigma_{NGAYCHAY = '2024-11-20'}(CHUYEN_DI)))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT pt.MAPT, pt.BIENSO, SUM(cd.SOLUONG_KHACH) AS TONG_KHACH FROM PHUONGTIEN pt JOIN CHUYEN_DI cd ON pt.MAPT = cd.MAPT WHERE cd.NGAYCHAY = '2024-11-20' GROUP BY pt.MAPT, pt.BIENSO;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYCHAY = '2024-11-20'}(CHUYEN_DI)
1. E_2 = \gamma_{MAPT, \text{SUM}(SOLUONG_KHACH) \to TONG_KHACH}(E_1)
1. E_3 = E_2 \bowtie PHUONGTIEN
1. KQ = \pi_{MAPT, BIENSO, TONG_KHACH}(E_3)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 28 [M13-Q2C5] — ĐSQH Phép Chia Tìm Tuyến Xe Đi Qua Tất Cả Trạm Ở Thủ Đức
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TUYEN_XE(MATUYEN, TENTUYEN, LOAI_HINH, CULY_KM, GIAVE_LUOT), TRAM_DUNG(MATRAM, TENTRAM, DIACHI, QUAN_HUYEN), LOTRINH(MATUYEN, MATRAM, SOTHUTU, KHOANGCACH_KM)`

### 1. Đề Bài
Tìm các tuyến xe (MATUYEN, TENTUYEN, LOAI_HINH) đi qua tất cả các trạm dừng nằm trên địa bàn quận 'Thủ Đức'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MATUYEN, TENTUYEN, LOAI_HINH}((\pi_{MATUYEN, MATRAM}(LOTRINH) \div \pi_{MATRAM}(\sigma_{QUAN_HUYEN = 'Thủ Đức'}(TRAM_DUNG))) \bowtie TUYEN_XE)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT tx.MATUYEN, tx.TENTUYEN, tx.LOAI_HINH FROM TUYEN_XE tx WHERE EXISTS (SELECT 1 FROM LOTRINH lt WHERE lt.MATUYEN = tx.MATUYEN) AND NOT EXISTS (SELECT 1 FROM TRAM_DUNG td WHERE td.QUAN_HUYEN = N'Thủ Đức' AND NOT EXISTS (SELECT 1 FROM LOTRINH lt2 WHERE lt2.MATUYEN = tx.MATUYEN AND lt2.MATRAM = td.MATRAM));
```

**Các bước suy luận tư duy:**
1. R = \pi_{MATUYEN, MATRAM}(LOTRINH)
1. S = \pi_{MATRAM}(\sigma_{QUAN_HUYEN = 'Thủ Đức'}(TRAM_DUNG))
1. E_{DIV} = R \div S
1. KQ = \pi_{MATUYEN, TENTUYEN, LOAI_HINH}(E_{DIV} \bowtie TUYEN_XE)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 29 [M13-Q2C6] — ĐSQH Cực Trị Tìm Tuyến Xe Có Doanh Thu Cao Nhất Năm 2024
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `TUYEN_XE(MATUYEN, TENTUYEN, LOAI_HINH, CULY_KM, GIAVE_LUOT), PHUONGTIEN(MAPT, BIENSO, SOGHE, NAMSX, MATUYEN), CHUYEN_DI(MACHUYEN, MAPT, NGAYCHAY, GIOXUATPHAT, SOLUONG_KHACH, DOANHTHU)`

### 1. Đề Bài
Tìm tuyến xe (MATUYEN, TENTUYEN, LOAI_HINH) có tổng doanh thu các chuyến đi (TONG_DOANHTHU) trong toàn bộ năm 2024 đạt cao nhất (bảo toàn tất cả các tuyến nếu đồng hạng).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MATUYEN, TENTUYEN, LOAI_HINH, TONG_DOANHTHU}((E_{DEM} - \pi_{MATUYEN, TONG_DOANHTHU}(E_{DEM} \bowtie_{TONG_DOANHTHU < TONG_DOANHTHU2} \rho_{MATUYEN2, TONG_DOANHTHU2}(E_{DEM}))) \bowtie TUYEN_XE)
```
**Câu lệnh SQL tương đương:**
```sql
WITH ThongKe AS (SELECT pt.MATUYEN, SUM(cd.DOANHTHU) AS TONG_DOANHTHU FROM PHUONGTIEN pt JOIN CHUYEN_DI cd ON pt.MAPT = cd.MAPT WHERE cd.NGAYCHAY >= '2024-01-01' AND cd.NGAYCHAY <= '2024-12-31' GROUP BY pt.MATUYEN) SELECT tx.MATUYEN, tx.TENTUYEN, tx.LOAI_HINH, tk.TONG_DOANHTHU FROM TUYEN_XE tx JOIN ThongKe tk ON tx.MATUYEN = tk.MATUYEN WHERE tk.TONG_DOANHTHU = (SELECT MAX(TONG_DOANHTHU) FROM ThongKe);
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYCHAY \ge '2024-01-01' \wedge NGAYCHAY \le '2024-12-31'}(CHUYEN_DI) \bowtie PHUONGTIEN
1. E_{DEM} = \gamma_{MATUYEN, \text{SUM}(DOANHTHU) \to TONG_DOANHTHU}(E_1)
1. E_{NHO_HON} = \pi_{MATUYEN, TONG_DOANHTHU}(E_{DEM} \bowtie_{TONG_DOANHTHU < TONG_DOANHTHU2} \rho_{MATUYEN2, TONG_DOANHTHU2}(E_{DEM}))
1. E_{MAX} = E_{DEM} - E_{NHO_HON}
1. KQ = \pi_{MATUYEN, TENTUYEN, LOAI_HINH, TONG_DOANHTHU}(E_{MAX} \bowtie TUYEN_XE)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.60đ
- `intermediate_steps`: 0.60đ

---

## Bài 30 [M14-Q2C4] — ĐSQH Gom Nhóm Kinh Phí Giải Ngân Thực Tế Năm 2024 Theo Đề Tài
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DETAI(MADT, TENDT, CAP_QUANLY, KINHPHI, NGAYBD, NGAYKT, CHUNHIEM_DT), GIAINGAN(MAGN, MADT, NGAYGN, SOTIEN_GN, NOIDUNG)`

### 1. Đề Bài
Tính tổng kinh phí đã giải ngân thực tế (TONG_GIAINGAN = SUM(SOTIEN_GN)) của từng đề tài (MADT, TENDT) đã được giải ngân trong năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MADT, TENDT, TONG_GIAINGAN}(DETAI \bowtie \gamma_{MADT, \text{SUM}(SOTIEN_GN) \to TONG_GIAINGAN}(\sigma_{NGAYGN \ge '2024-01-01' \wedge NGAYGN \le '2024-12-31'}(GIAINGAN)))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT dt.MADT, dt.TENDT, SUM(gn.SOTIEN_GN) AS TONG_GIAINGAN FROM DETAI dt JOIN GIAINGAN gn ON dt.MADT = gn.MADT WHERE gn.NGAYGN >= '2024-01-01' AND gn.NGAYGN <= '2024-12-31' GROUP BY dt.MADT, dt.TENDT;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYGN \ge '2024-01-01' \wedge NGAYGN \le '2024-12-31'}(GIAINGAN)
1. E_2 = \gamma_{MADT, \text{SUM}(SOTIEN_GN) \to TONG_GIAINGAN}(E_1)
1. E_3 = DETAI \bowtie E_2
1. KQ = \pi_{MADT, TENDT, TONG_GIAINGAN}(E_3)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 31 [M14-Q2C5] — ĐSQH Phép Chia Tìm Giảng Viên Tham Gia Tất Cả Đề Tài Cấp Nhà Nước
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DETAI(MADT, TENDT, CAP_QUANLY, KINHPHI, NGAYBD, NGAYKT, CHUNHIEM_DT), THAMGIA_DT(MADT, MAGV, VAITRO, SOGIO_TG), GIANGVIEN(MAGV, HOTEN, HOCHAM, HOCVI, LUONG, MAKV)`

### 1. Đề Bài
Tìm các giảng viên (MAGV, HOTEN, HOCVI) đã từng tham gia thực hiện tất cả các đề tài NCKH thuộc cấp quản lý 'Cấp Nhà nước' của trường.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAGV, HOTEN, HOCVI}((\pi_{MAGV, MADT}(THAMGIA_DT) \div \pi_{MADT}(\sigma_{CAP_QUANLY = 'Cấp Nhà nước'}(DETAI))) \bowtie GIANGVIEN)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT gv.MAGV, gv.HOTEN, gv.HOCVI FROM GIANGVIEN gv WHERE EXISTS (SELECT 1 FROM THAMGIA_DT tg WHERE tg.MAGV = gv.MAGV) AND NOT EXISTS (SELECT 1 FROM DETAI dt WHERE dt.CAP_QUANLY = N'Cấp Nhà nước' AND NOT EXISTS (SELECT 1 FROM THAMGIA_DT tg2 WHERE tg2.MAGV = gv.MAGV AND tg2.MADT = dt.MADT));
```

**Các bước suy luận tư duy:**
1. R = \pi_{MAGV, MADT}(THAMGIA_DT)
1. S = \pi_{MADT}(\sigma_{CAP_QUANLY = 'Cấp Nhà nước'}(DETAI))
1. E_{DIV} = R \div S
1. KQ = \pi_{MAGV, HOTEN, HOCVI}(E_{DIV} \bowtie GIANGVIEN)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 32 [M15-Q2C4] — ĐSQH Gom Nhóm Chi Phí Chăm Sóc Động Vật Tháng 10/2024
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONGVAT(MADV, MALOAI, GIOITINH, CANNANG_KG, TINHTRANG_SK, MAKHU), CHITIET_CS(MACS, MADV, MANV, NGAYCS, CHIPHI_CS, GHI_CHU)`

### 1. Đề Bài
Tính tổng chi phí chăm sóc y tế (TONG_CHIPHI = SUM(CHIPHI_CS)) của từng cá thể động vật (MADV, TINHTRANG_SK) phát sinh trong tháng 10 năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MADV, TINHTRANG_SK, TONG_CHIPHI}(DONGVAT \bowtie \gamma_{MADV, \text{SUM}(CHIPHI_CS) \to TONG_CHIPHI}(\sigma_{NGAYCS \ge '2024-10-01' \wedge NGAYCS \le '2024-10-31'}(CHITIET_CS)))
```
**Câu lệnh SQL tương đương:**
```sql
SELECT dv.MADV, dv.TINHTRANG_SK, SUM(cs.CHIPHI_CS) AS TONG_CHIPHI FROM DONGVAT dv JOIN CHITIET_CS cs ON dv.MADV = cs.MADV WHERE cs.NGAYCS >= '2024-10-01' AND cs.NGAYCS <= '2024-10-31' GROUP BY dv.MADV, dv.TINHTRANG_SK;
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYCS \ge '2024-10-01' \wedge NGAYCS \le '2024-10-31'}(CHITIET_CS)
1. E_2 = \gamma_{MADV, \text{SUM}(CHIPHI_CS) \to TONG_CHIPHI}(E_1)
1. E_3 = E_2 \bowtie DONGVAT
1. KQ = \pi_{MADV, TINHTRANG_SK, TONG_CHIPHI}(E_3)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 33 [M15-Q2C5] — ĐSQH Phép Chia Tìm Nhân Viên Chăm Sóc Tất Cả Tê Tê Java
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DONGVAT(MADV, MALOAI, GIOITINH, CANNANG_KG, TINHTRANG_SK, MAKHU), LOAI_DONGVAT(MALOAI, TENLOAI, TEN_KHOAHOC, MUC_NGUYCAP), CHITIET_CS(MACS, MADV, MANV, NGAYCS, CHIPHI_CS, GHI_CHU), NHANVIEN(MANV, HOTEN, CHUYENMON, LUONG, MAKHU)`

### 1. Đề Bài
Tìm các nhân viên (MANV, HOTEN, CHUYENMON) đã từng trực tiếp chăm sóc tất cả các cá thể động vật thuộc loài mang tên 'Tê tê Java'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MANV, HOTEN, CHUYENMON}((\pi_{MANV, MADV}(CHITIET_CS) \div \pi_{MADV}(DONGVAT \bowtie \sigma_{TENLOAI = 'Tê tê Java'}(LOAI_DONGVAT))) \bowtie NHANVIEN)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT nv.MANV, nv.HOTEN, nv.CHUYENMON FROM NHANVIEN nv WHERE EXISTS (SELECT 1 FROM CHITIET_CS cs WHERE cs.MANV = nv.MANV) AND NOT EXISTS (SELECT 1 FROM DONGVAT dv JOIN LOAI_DONGVAT ldv ON dv.MALOAI = ldv.MALOAI WHERE ldv.TENLOAI = N'Tê tê Java' AND NOT EXISTS (SELECT 1 FROM CHITIET_CS cs2 WHERE cs2.MANV = nv.MANV AND cs2.MADV = dv.MADV));
```

**Các bước suy luận tư duy:**
1. R = \pi_{MANV, MADV}(CHITIET_CS)
1. S = \pi_{MADV}(DONGVAT \bowtie \sigma_{TENLOAI = 'Tê tê Java'}(LOAI_DONGVAT))
1. E_{DIV} = R \div S
1. KQ = \pi_{MANV, HOTEN, CHUYENMON}(E_{DIV} \bowtie NHANVIEN)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 34 [M15-Q2C6] — ĐSQH Cực Trị Tìm Phân Khu Tiếp Nhận Nhiều Động Vật Nhất
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `KHU_BAOTON(MAKHU, TENKHU, DIENTICH_HA, NGUOI_PHUTRACH), DONGVAT(MADV, MALOAI, GIOITINH, CANNANG_KG, TINHTRANG_SK, MAKHU)`

### 1. Đề Bài
Tìm phân khu bảo tồn (MAKHU, TENKHU, DIENTICH_HA) có tổng số lượng cá thể động vật (TONG_DONGVAT) đang tiếp nhận nuôi dưỡng nhiều nhất (bảo toàn tất cả các phân khu nếu đồng hạng).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAKHU, TENKHU, DIENTICH_HA, TONG_DONGVAT}((E_{DEM} - \pi_{MAKHU, TONG_DONGVAT}(E_{DEM} \bowtie_{TONG_DONGVAT < TONG_DONGVAT2} \rho_{MAKHU2, TONG_DONGVAT2}(E_{DEM}))) \bowtie KHU_BAOTON)
```
**Câu lệnh SQL tương đương:**
```sql
WITH ThongKe AS (SELECT dv.MAKHU, COUNT(dv.MADV) AS TONG_DONGVAT FROM DONGVAT dv GROUP BY dv.MAKHU) SELECT kb.MAKHU, kb.TENKHU, kb.DIENTICH_HA, tk.TONG_DONGVAT FROM KHU_BAOTON kb JOIN ThongKe tk ON kb.MAKHU = tk.MAKHU WHERE tk.TONG_DONGVAT = (SELECT MAX(TONG_DONGVAT) FROM ThongKe);
```

**Các bước suy luận tư duy:**
1. E_{DEM} = \gamma_{MAKHU, \text{COUNT}(MADV) \to TONG_DONGVAT}(DONGVAT)
1. E_{NHO_HON} = \pi_{MAKHU, TONG_DONGVAT}(E_{DEM} \bowtie_{TONG_DONGVAT < TONG_DONGVAT2} \rho_{MAKHU2, TONG_DONGVAT2}(E_{DEM}))
1. E_{MAX} = E_{DEM} - E_{NHO_HON}
1. KQ = \pi_{MAKHU, TENKHU, DIENTICH_HA, TONG_DONGVAT}(E_{MAX} \bowtie KHU_BAOTON)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.60đ
- `intermediate_steps`: 0.60đ

---

## Bài 35 [RA-D46] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Điểm Tiêm & Vắc-Xin (Bài 46)
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

## Bài 36 [RA-D47] — ĐSQH Phép Chia (Tất Cả): Đơn Hàng & Mặt Hàng (Bài 47)
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

## Bài 37 [RA-D48] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Bác Sĩ & Bệnh Nhân (Bài 48)
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

## Bài 38 [RA-D49] — ĐSQH Phép Chia (Tất Cả): Học Viên & Khóa Học (Bài 49)
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

## Bài 39 [M14-Q2C6] — ĐSQH Cực Trị Tìm Đề Tài Có Nhiều Bài Báo Xếp Hạng Q1 Nhất
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DETAI(MADT, TENDT, CAP_QUANLY, KINHPHI, NGAYBD, NGAYKT, CHUNHIEM_DT), SANPHAM_KH(MASP, TENSP, LOAISP, XEP_HANG, MADT)`

### 1. Đề Bài
Tìm đề tài NCKH (MADT, TENDT, CAP_QUANLY) có tổng số lượng sản phẩm khoa học đạt xếp hạng 'Q1' công bố nhiều nhất (bảo toàn tất cả các đề tài nếu đồng hạng).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MADT, TENDT, CAP_QUANLY, TONG_SP}((E_{DEM} - \pi_{MADT, TONG_SP}(E_{DEM} \bowtie_{TONG_SP < TONG_SP2} \rho_{MADT2, TONG_SP2}(E_{DEM}))) \bowtie DETAI)
```
**Câu lệnh SQL tương đương:**
```sql
WITH ThongKe AS (SELECT sp.MADT, COUNT(sp.MASP) AS TONG_SP FROM SANPHAM_KH sp WHERE sp.XEP_HANG = 'Q1' GROUP BY sp.MADT) SELECT dt.MADT, dt.TENDT, dt.CAP_QUANLY, tk.TONG_SP FROM DETAI dt JOIN ThongKe tk ON dt.MADT = tk.MADT WHERE tk.TONG_SP = (SELECT MAX(TONG_SP) FROM ThongKe);
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{XEP_HANG = 'Q1'}(SANPHAM_KH)
1. E_{DEM} = \gamma_{MADT, \text{COUNT}(MASP) \to TONG_SP}(E_1)
1. E_{NHO_HON} = \pi_{MADT, TONG_SP}(E_{DEM} \bowtie_{TONG_SP < TONG_SP2} \rho_{MADT2, TONG_SP2}(E_{DEM}))
1. E_{MAX} = E_{DEM} - E_{NHO_HON}
1. KQ = \pi_{MADT, TENDT, CAP_QUANLY, TONG_SP}(E_{MAX} \bowtie DETAI)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 40 [M11-Q2C5] — ĐSQH Phép Chia Tìm Cửa Hàng Nhập Tất Cả Syrup Pha Chế
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEUXUAT(MAPX, NGAYXUAT, MACH, TONGTIEN, TRANGTHAI), CHITIET_PX(MAPX, MANL, SOLUONG, DONGIA_XUAT), NGUYENLIEU(MANL, TENNL, LOAINL, DONGIA_CHUAN, DVT), CUAHANG(MACH, TENCH, DIACHI, MAKV, NAM_KYHD)`

### 1. Đề Bài
Tìm các cửa hàng (MACH, TENCH, MAKV) đã từng nhập tất cả các loại nguyên liệu thuộc phân loại 'Syrup pha chế' của chuỗi.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MACH, TENCH, MAKV}((\pi_{MACH, MANL}(PHIEUXUAT \bowtie CHITIET_PX) \div \pi_{MANL}(\sigma_{LOAINL = 'Syrup pha chế'}(NGUYENLIEU))) \bowtie CUAHANG)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT ch.MACH, ch.TENCH, ch.MAKV FROM CUAHANG ch WHERE EXISTS (SELECT 1 FROM PHIEUXUAT px JOIN CHITIET_PX ct ON px.MAPX = ct.MAPX WHERE px.MACH = ch.MACH) AND NOT EXISTS (SELECT 1 FROM NGUYENLIEU nl WHERE nl.LOAINL = N'Syrup pha chế' AND NOT EXISTS (SELECT 1 FROM PHIEUXUAT px2 JOIN CHITIET_PX ct2 ON px2.MAPX = ct2.MAPX WHERE px2.MACH = ch.MACH AND ct2.MANL = nl.MANL));
```

**Các bước suy luận tư duy:**
1. R = \pi_{MACH, MANL}(PHIEUXUAT \bowtie CHITIET_PX)
1. S = \pi_{MANL}(\sigma_{LOAINL = 'Syrup pha chế'}(NGUYENLIEU))
1. E_{DIV} = R \div S
1. KQ = \pi_{MACH, TENCH, MAKV}(E_{DIV} \bowtie CUAHANG)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 41 [M11-Q2C6] — ĐSQH Cực Trị Tìm Cửa Hàng Nhập Tổng Số Lượng Nhiều Nhất Năm 2024
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `PHIEUXUAT(MAPX, NGAYXUAT, MACH, TONGTIEN, TRANGTHAI), CHITIET_PX(MAPX, MANL, SOLUONG, DONGIA_XUAT), CUAHANG(MACH, TENCH, DIACHI, MAKV, NAM_KYHD), KHUVUC(MAKV, TENKV, TRUONGVUNG)`

### 1. Đề Bài
Tìm cửa hàng (MACH, TENCH, TENKV) có tổng số lượng nguyên liệu nhập về nhiều nhất trong toàn bộ năm 2024 (bảo toàn tất cả cửa hàng nếu đồng hạng).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MACH, TENCH, TENKV, TONG_SOLUONG_NHAP}((E_{DEM} - \pi_{MACH, TONG_SOLUONG_NHAP}(E_{DEM} \bowtie_{TONG_SOLUONG_NHAP < TONG_SOLUONG_NHAP2} \rho_{MACH2, TONG_SOLUONG_NHAP2}(E_{DEM}))) \bowtie CUAHANG \bowtie KHUVUC)
```
**Câu lệnh SQL tương đương:**
```sql
WITH ThongKe AS (SELECT px.MACH, SUM(ct.SOLUONG) AS TONG_SOLUONG_NHAP FROM PHIEUXUAT px JOIN CHITIET_PX ct ON px.MAPX = ct.MAPX WHERE px.NGAYXUAT >= '2024-01-01' AND px.NGAYXUAT <= '2024-12-31' GROUP BY px.MACH) SELECT ch.MACH, ch.TENCH, kv.TENKV, tk.TONG_SOLUONG_NHAP FROM CUAHANG ch JOIN KHUVUC kv ON ch.MAKV = kv.MAKV JOIN ThongKe tk ON ch.MACH = tk.MACH WHERE tk.TONG_SOLUONG_NHAP = (SELECT MAX(TONG_SOLUONG_NHAP) FROM ThongKe);
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYXUAT \ge '2024-01-01' \wedge NGAYXUAT \le '2024-12-31'}(PHIEUXUAT) \bowtie CHITIET_PX
1. E_{DEM} = \gamma_{MACH, \text{SUM}(SOLUONG) \to TONG_SOLUONG_NHAP}(E_1)
1. E_{NHO_HON} = \pi_{MACH, TONG_SOLUONG_NHAP}(E_{DEM} \bowtie_{TONG_SOLUONG_NHAP < TONG_SOLUONG_NHAP2} \rho_{MACH2, TONG_SOLUONG_NHAP2}(E_{DEM}))
1. E_{MAX} = E_{DEM} - E_{NHO_HON}
1. E_{KQS} = E_{MAX} \bowtie CUAHANG \bowtie KHUVUC
1. KQ = \pi_{MACH, TENCH, TENKV, TONG_SOLUONG_NHAP}(E_{KQS})

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.60đ
- `intermediate_steps`: 0.60đ

---

## Bài 42 [M12-Q2C5] — ĐSQH Phép Chia Tìm Khách Hàng Mua Vé Xem Tất Cả Phim Kinh Dị
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SUATCHIEU(MASC, MAPHIM, MAPC, NGAYCHIEU, GIOCHIEU, GIAVE_CHUAN), VEXEM(MAVE, MASC, MAKH, SOGHE, GIAVE_THUC, TRANGTHAI), PHIM(MAPHIM, TENPHIM, THELOAI, THOILUONG, DAODIEN, NAMSX), KHACHHANG(MAKH, HOTEN, SDT, EMAIL, LOAITHANHVIEN)`

### 1. Đề Bài
Tìm các khách hàng (MAKH, HOTEN, SDT) đã từng mua vé xem ('Đã thanh toán') tất cả các bộ phim thuộc thể loại 'Kinh dị' của cụm rạp.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAKH, HOTEN, SDT}((\pi_{MAKH, MAPHIM}(SUATCHIEU \bowtie \sigma_{TRANGTHAI = 'Đã thanh toán'}(VEXEM)) \div \pi_{MAPHIM}(\sigma_{THELOAI = 'Kinh dị'}(PHIM))) \bowtie KHACHHANG)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT kh.MAKH, kh.HOTEN, kh.SDT FROM KHACHHANG kh WHERE EXISTS (SELECT 1 FROM VEXEM vx WHERE vx.MAKH = kh.MAKH AND vx.TRANGTHAI = N'Đã thanh toán') AND NOT EXISTS (SELECT 1 FROM PHIM p WHERE p.THELOAI = N'Kinh dị' AND NOT EXISTS (SELECT 1 FROM VEXEM vx2 JOIN SUATCHIEU sc2 ON vx2.MASC = sc2.MASC WHERE vx2.MAKH = kh.MAKH AND sc2.MAPHIM = p.MAPHIM AND vx2.TRANGTHAI = N'Đã thanh toán'));
```

**Các bước suy luận tư duy:**
1. R = \pi_{MAKH, MAPHIM}(SUATCHIEU \bowtie \sigma_{TRANGTHAI = 'Đã thanh toán'}(VEXEM))
1. S = \pi_{MAPHIM}(\sigma_{THELOAI = 'Kinh dị'}(PHIM))
1. E_{DIV} = R \div S
1. KQ = \pi_{MAKH, HOTEN, SDT}(E_{DIV} \bowtie KHACHHANG)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 43 [M12-Q2C6] — ĐSQH Cực Trị Tìm Phim Bán Được Nhiều Vé Nhất Năm 2024
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SUATCHIEU(MASC, MAPHIM, MAPC, NGAYCHIEU, GIOCHIEU, GIAVE_CHUAN), VEXEM(MAVE, MASC, MAKH, SOGHE, GIAVE_THUC, TRANGTHAI), PHIM(MAPHIM, TENPHIM, THELOAI, THOILUONG, DAODIEN, NAMSX)`

### 1. Đề Bài
Tìm bộ phim (MAPHIM, TENPHIM, THELOAI) có tổng số lượng vé đã bán thành công ('Đã thanh toán') nhiều nhất trong toàn bộ năm 2024 (bảo toàn tất cả các bộ phim nếu đồng hạng).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
KQ = \pi_{MAPHIM, TENPHIM, THELOAI, TONG_VE}((E_{DEM} - \pi_{MAPHIM, TONG_VE}(E_{DEM} \bowtie_{TONG_VE < TONG_VE2} \rho_{MAPHIM2, TONG_VE2}(E_{DEM}))) \bowtie PHIM)
```
**Câu lệnh SQL tương đương:**
```sql
WITH ThongKe AS (SELECT sc.MAPHIM, COUNT(vx.MAVE) AS TONG_VE FROM SUATCHIEU sc JOIN VEXEM vx ON sc.MASC = vx.MASC WHERE sc.NGAYCHIEU >= '2024-01-01' AND sc.NGAYCHIEU <= '2024-12-31' AND vx.TRANGTHAI = N'Đã thanh toán' GROUP BY sc.MAPHIM) SELECT p.MAPHIM, p.TENPHIM, p.THELOAI, tk.TONG_VE FROM PHIM p JOIN ThongKe tk ON p.MAPHIM = tk.MAPHIM WHERE tk.TONG_VE = (SELECT MAX(TONG_VE) FROM ThongKe);
```

**Các bước suy luận tư duy:**
1. E_1 = \sigma_{NGAYCHIEU \ge '2024-01-01' \wedge NGAYCHIEU \le '2024-12-31'}(SUATCHIEU) \bowtie \sigma_{TRANGTHAI = 'Đã thanh toán'}(VEXEM)
1. E_{DEM} = \gamma_{MAPHIM, \text{COUNT}(MAVE) \to TONG_VE}(E_1)
1. E_{NHO_HON} = \pi_{MAPHIM, TONG_VE}(E_{DEM} \bowtie_{TONG_VE < TONG_VE2} \rho_{MAPHIM2, TONG_VE2}(E_{DEM}))
1. E_{MAX} = E_{DEM} - E_{NHO_HON}
1. KQ = \pi_{MAPHIM, TENPHIM, THELOAI, TONG_VE}(E_{MAX} \bowtie PHIM)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `intermediate_steps`: 0.30đ

---

## Bài 44 [M03-Q2C4] — ĐSQH Gom Nhóm Tính Tổng Tiền Ủng Hộ Theo Nhà Hảo Tâm Năm 2024
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHA_HAOTAM, DONG_GOP`

### 1. Đề Bài
Tính tổng số tiền ủng hộ (TONG_TIEN) của từng nhà hảo tâm đã đóng góp trong năm 2024. Thông tin hiển thị gồm: MANHT, TENNHT, TONG_TIEN.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E1 ← σ_{NGAYDG ≥ '2024-01-01' ∧ NGAYDG ≤ '2024-12-31'}(DONG_GOP)
E2 ← NHA_HAOTAM ⋈ E1
KQ ← _{MANHT, TENNHT}γ_{SUM(SOTIEN) → TONG_TIEN}(E2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT NHT.MANHT, NHT.TENNHT, SUM(DG.SOTIEN) AS TONG_TIEN FROM NHA_HAOTAM NHT INNER JOIN DONG_GOP DG ON NHT.MANHT = DG.MANHT WHERE DG.NGAYDG >= '2024-01-01' AND DG.NGAYDG <= '2024-12-31' GROUP BY NHT.MANHT, NHT.TENNHT;
```

**Các bước suy luận tư duy:**
1. Lọc đóng góp trong năm 2024
1. Kết nối với bảng NHA_HAOTAM
1. Gom nhóm theo MANHT, TENNHT và tính SUM(SOTIEN)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `projection`: 0.30đ

---

## Bài 45 [M03-Q2C5] — ĐSQH Phép Chia Tìm Đợt Cứu Trợ Được Đóng Góp Bởi Tất Cả Doanh Nghiệp
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DOT_CUUTRO, DONG_GOP, NHA_HAOTAM`

### 1. Đề Bài
Tìm các đợt cứu trợ (MADOT, TENDOT, NGAYBD) đã tiếp nhận tiền đóng góp từ tất cả các nhà hảo tâm thuộc loại hình 'Doanh nghiệp'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R ← π_{MADOT, MANHT}(DONG_GOP)
S ← π_{MANHT}(σ_{LOAIHINH='Doanh nghiệp'}(NHA_HAOTAM))
R_KQ ← R ÷ S
KQ ← π_{MADOT, TENDOT, NGAYBD}(R_KQ ⋈ DOT_CUUTRO)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT DCT.MADOT, DCT.TENDOT, DCT.NGAYBD FROM DOT_CUUTRO DCT WHERE NOT EXISTS (SELECT * FROM NHA_HAOTAM NHT WHERE NHT.LOAIHINH = N'Doanh nghiệp' AND NOT EXISTS (SELECT * FROM DONG_GOP DG WHERE DG.MADOT = DCT.MADOT AND DG.MANHT = NHT.MANHT)) AND EXISTS (SELECT * FROM DONG_GOP WHERE MADOT = DCT.MADOT);
```

**Các bước suy luận tư duy:**
1. Xác định tập bị chia R(MADOT, MANHT)
1. Xác định tập chia S(MANHT) gồm các nhà hảo tâm Doanh nghiệp
1. Thực hiện phép chia R ÷ S để tìm đợt cứu trợ nhận đủ tất cả doanh nghiệp
1. Kết nối với DOT_CUUTRO để lấy thông tin đợt

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `projection`: 0.30đ

---

## Bài 46 [M03-Q2C6] — ĐSQH Tìm Xã Có Tổng Tiền Cứu Trợ Đã Phân Bổ Nhiều Nhất
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `XA, HO_DAN, PHIEU_NHAN`

### 1. Đề Bài
Tìm thông tin xã (MAXA, TENXA, HUYEN) có tổng số tiền cứu trợ đã phân bổ cho các hộ dân (TONG_CUUTRO) nhiều nhất (bảo toàn tất cả các xã nếu có nhiều xã cùng đạt số tiền cứu trợ lớn nhất).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_TongTien ← _{MAXA}γ_{SUM(SOTIEN) → TONG_CUUTRO}(HO_DAN ⋈ PHIEU_NHAN)
R_NhoHon ← π_{R1.TONG_CUUTRO}(σ_{R1.TONG_CUUTRO < R2.TONG_CUUTRO}(ρ_{R1}(R_TongTien) × ρ_{R2}(R_TongTien)))
R_Max ← π_{TONG_CUUTRO}(R_TongTien) - R_NhoHon
KQ ← π_{MAXA, TENXA, HUYEN}(XA ⋈ R_TongTien ⋈ R_Max)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT TOP 1 WITH TIES X.MAXA, X.TENXA, X.HUYEN, SUM(PN.SOTIEN) AS TONG_CUUTRO FROM XA X INNER JOIN HO_DAN HD ON X.MAXA = HD.MAXA INNER JOIN PHIEU_NHAN PN ON HD.MAHO = PN.MAHO GROUP BY X.MAXA, X.TENXA, X.HUYEN ORDER BY SUM(PN.SOTIEN) DESC;
```

**Các bước suy luận tư duy:**
1. Tính tổng tiền cứu trợ phân bổ cho từng xã
1. Dùng tích Descartes tìm các giá trị nhỏ hơn
1. Trừ tập hợp để tìm giá trị cực đại lớn nhất
1. Kết nối XA và bảo toàn đồng hạng

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.60đ
- `projection`: 0.50đ

---

## Bài 47 [M04-Q2C4] — ĐSQH Gom Nhóm Tính Tổng Số Lít Nhiên Liệu Đã Bán Tháng 10/2024
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CUAHANG, HOADON, CTHD`

### 1. Đề Bài
Tính tổng số lít nhiên liệu đã bán (TONG_LIT_BAN) của từng cửa hàng xăng dầu trong tháng 10 năm 2024. Thông tin hiển thị gồm: MACH, TENCH, TONG_LIT_BAN.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E1 ← σ_{NGAYHD ≥ '2024-10-01' ∧ NGAYHD ≤ '2024-10-31'}(HOADON)
E2 ← CUAHANG ⋈ E1 ⋈ CTHD
KQ ← _{MACH, TENCH}γ_{SUM(SOLUONG) → TONG_LIT_BAN}(E2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT CH.MACH, CH.TENCH, SUM(CT.SOLUONG) AS TONG_LIT_BAN FROM CUAHANG CH INNER JOIN HOADON HD ON CH.MACH = HD.MACH INNER JOIN CTHD CT ON HD.MAHD = CT.MAHD WHERE HD.NGAYHD >= '2024-10-01' AND HD.NGAYHD <= '2024-10-31 23:59:59' GROUP BY CH.MACH, CH.TENCH;
```

**Các bước suy luận tư duy:**
1. Lọc hóa đơn trong tháng 10/2024
1. Kết nối CUAHANG, HOADON, CTHD
1. Gom nhóm theo MACH, TENCH và tính SUM(SOLUONG)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `projection`: 0.30đ

---

## Bài 48 [M04-Q2C5] — ĐSQH Phép Chia Tìm Hóa Đơn Đã Bán Tất Cả Các Loại Xăng Khoáng
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOADON, CTHD, NHIENLIEU`

### 1. Đề Bài
Tìm các hóa đơn (MAHD, NGAYHD, MACH) đã bán tất cả các loại nhiên liệu thuộc phân loại 'Xăng khoáng'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R ← π_{MAHD, MANL}(CTHD)
S ← π_{MANL}(σ_{LOAINL='Xăng khoáng'}(NHIENLIEU))
R_KQ ← R ÷ S
KQ ← π_{MAHD, NGAYHD, MACH}(R_KQ ⋈ HOADON)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT HD.MAHD, HD.NGAYHD, HD.MACH FROM HOADON HD WHERE NOT EXISTS (SELECT * FROM NHIENLIEU NL WHERE NL.LOAINL = N'Xăng khoáng' AND NOT EXISTS (SELECT * FROM CTHD CT WHERE CT.MAHD = HD.MAHD AND CT.MANL = NL.MANL)) AND EXISTS (SELECT 1 FROM CTHD WHERE MAHD = HD.MAHD);
```

**Các bước suy luận tư duy:**
1. Xác định quan hệ bị chia R(MAHD, MANL)
1. Xác định tập chia S(MANL) gồm các mặt hàng Xăng khoáng
1. Thực hiện phép chia R ÷ S để tìm hóa đơn bán đủ các mặt hàng
1. Kết nối HOADON và chiếu kết quả

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `projection`: 0.30đ

---

## Bài 49 [M04-Q2C6] — ĐSQH Tìm Cửa Hàng Có Tổng Dung Tích Bể Chứa Lớn Nhất
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CUAHANG, BE_CHUA`

### 1. Đề Bài
Tìm cửa hàng xăng dầu (MACH, TENCH, QUAN) có tổng dung tích các bể chứa (TONG_DUNGTICH) lớn nhất trong hệ thống (bảo toàn tất cả các cửa hàng nếu có nhiều cửa hàng cùng đạt tổng dung tích lớn nhất).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R_TongDT ← _{MACH}γ_{SUM(DUNGTICH) → TONG_DUNGTICH}(BE_CHUA)
R_NhoHon ← π_{R1.TONG_DUNGTICH}(σ_{R1.TONG_DUNGTICH < R2.TONG_DUNGTICH}(ρ_{R1}(R_TongDT) × ρ_{R2}(R_TongDT)))
R_Max ← π_{TONG_DUNGTICH}(R_TongDT) - R_NhoHon
KQ ← π_{MACH, TENCH, QUAN}(CUAHANG ⋈ R_TongDT ⋈ R_Max)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT TOP 1 WITH TIES CH.MACH, CH.TENCH, CH.QUAN, SUM(BC.DUNGTICH) AS TONG_DUNGTICH FROM CUAHANG CH INNER JOIN BE_CHUA BC ON CH.MACH = BC.MACH GROUP BY CH.MACH, CH.TENCH, CH.QUAN ORDER BY SUM(BC.DUNGTICH) DESC;
```

**Các bước suy luận tư duy:**
1. Gom nhóm tính tổng dung tích các bể theo MACH
1. Dùng tích Descartes tìm các tổng dung tích nhỏ hơn
1. Trừ tập hợp để tìm giá trị cực đại lớn nhất
1. Kết nối CUAHANG và bảo toàn đồng hạng

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `projection`: 0.30đ

---

## Bài 50 [M05-Q2C4] — ĐSQH Gom Nhóm Tính Tổng Tiền Thu Năm 2024 Theo Hợp Đồng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 10 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOPDONG, PHIEUTHU`

### 1. Đề Bài
Tính tổng số tiền thu được (TONG_TIEN_THU) theo từng hợp đồng trong năm 2024. Thông tin hiển thị gồm: MAHD, NGAYKY, TONG_TIEN_THU.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E1 ← σ_{NAM=2024}(PHIEUTHU)
E2 ← HOPDONG ⋈ E1
KQ ← _{MAHD, NGAYKY}γ_{SUM(SOTIEN) → TONG_TIEN_THU}(E2)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT HD.MAHD, HD.NGAYKY, SUM(PT.SOTIEN) AS TONG_TIEN_THU FROM HOPDONG HD INNER JOIN PHIEUTHU PT ON HD.MAHD = PT.MAHD WHERE PT.NAM = 2024 GROUP BY HD.MAHD, HD.NGAYKY;
```

**Các bước suy luận tư duy:**
1. Lọc phiếu thu trong năm 2024
1. Kết nối HOPDONG với PHIEUTHU trên MAHD
1. Gom nhóm theo MAHD, NGAYKY và tính SUM(SOTIEN)

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `projection`: 0.30đ

---

## Bài 51 [M05-Q2C5] — ĐSQH Phép Chia Tìm Khách Hàng Thuê Căn Hộ Ở Tất Cả Tòa Nhà Quận 7
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG, HOPDONG, CANHO, TOANHA`

### 1. Đề Bài
Tìm các khách hàng (MAKH, HOTEN, SDT) đã từng ký hợp đồng thuê căn hộ tại tất cả các tòa nhà tọa lạc tại địa bàn 'Quận 7'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
R ← π_{MAKH, MATN}(HOPDONG ⋈ CANHO)
S ← π_{MATN}(σ_{DIACHI='Quận 7'}(TOANHA))
R_KQ ← R ÷ S
KQ ← π_{MAKH, HOTEN, SDT}(R_KQ ⋈ KHACHHANG)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT KH.MAKH, KH.HOTEN, KH.SDT FROM KHACHHANG KH WHERE NOT EXISTS (SELECT * FROM TOANHA TN WHERE TN.DIACHI = N'Quận 7' AND NOT EXISTS (SELECT * FROM HOPDONG HD INNER JOIN CANHO CH ON HD.MACH = CH.MACH WHERE HD.MAKH = KH.MAKH AND CH.MATN = TN.MATN)) AND EXISTS (SELECT 1 FROM HOPDONG WHERE MAKH = KH.MAKH);
```

**Các bước suy luận tư duy:**
1. Xác định quan hệ bị chia R(MAKH, MATN) giữa khách hàng và tòa nhà đã thuê
1. Xác định tập chia S(MATN) gồm các tòa nhà tại Quận 7
1. Thực hiện phép chia R ÷ S để tìm khách hàng thuê đủ tất cả tòa nhà Quận 7
1. Kết nối KHACHHANG và chiếu kết quả

**Barem chấm điểm đề xuất:**
- `syntax`: 0.30đ
- `logic`: 0.40đ
- `projection`: 0.30đ

---

## Bài 52 [M05-Q2C6] — ĐSQH Tìm Tòa Nhà Có Số Căn Hộ Đang Thuê Nhiều Nhất
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `TOANHA, CANHO`

### 1. Đề Bài
Tìm thông tin tòa nhà (MATN, TENTN, DIACHI) có số lượng căn hộ đang ở trạng thái 'Đang thuê' nhiều nhất trong hệ thống (bảo toàn tất cả các tòa nhà nếu có nhiều tòa nhà cùng đạt số lượng căn hộ đang thuê lớn nhất).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ:**
```text
E1 ← σ_{TRANGTHAI='Đang thuê'}(CANHO)
R_SoLuong ← _{MATN}γ_{COUNT(MACH) → SO_CAN_THUE}(E1)
R_NhoHon ← π_{R1.SO_CAN_THUE}(σ_{R1.SO_CAN_THUE < R2.SO_CAN_THUE}(ρ_{R1}(R_SoLuong) × ρ_{R2}(R_SoLuong)))
R_Max ← π_{SO_CAN_THUE}(R_SoLuong) - R_NhoHon
KQ ← π_{MATN, TENTN, DIACHI}(TOANHA ⋈ R_SoLuong ⋈ R_Max)
```
**Câu lệnh SQL tương đương:**
```sql
SELECT TOP 1 WITH TIES TN.MATN, TN.TENTN, TN.DIACHI, COUNT(CH.MACH) AS SO_CAN_THUE FROM TOANHA TN INNER JOIN CANHO CH ON TN.MATN = CH.MATN WHERE CH.TRANGTHAI = N'Đang thuê' GROUP BY TN.MATN, TN.TENTN, TN.DIACHI ORDER BY COUNT(CH.MACH) DESC;
```

**Các bước suy luận tư duy:**
1. Lọc căn hộ có trạng thái Đang thuê và gom nhóm đếm theo MATN
1. Dùng tích Descartes tìm các số lượng nhỏ hơn
1. Trừ tập hợp để tìm giá trị cực đại lớn nhất
1. Kết nối TOANHA và bảo toàn đồng hạng

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.60đ
- `projection`: 0.50đ

---
