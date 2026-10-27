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

## Bài 18 [RA-D02] — ĐSQH Phép Chia VĐV Tham Gia Tất Cả Kỳ Olympic Từ 2008
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

## Bài 19 [RA-D25] — ĐSQH Phép Chia (Tất Cả): Học Viên & Khóa Học (Bài 25)
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

## Bài 20 [RA-D26] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Tàu & Cảng Biển (Bài 26)
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

## Bài 21 [RA-D27] — ĐSQH Phép Chia (Tất Cả): Nhà Đầu Tư & Dự Án (Bài 27)
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

## Bài 22 [RA-D28] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Khách Hàng & Sảnh Tiệc (Bài 28)
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

## Bài 23 [RA-D29] — ĐSQH Phép Chia (Tất Cả): Độc Giả & Thể Loại Sách (Bài 29)
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

## Bài 24 [RA-D30] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Điểm Tiêm & Vắc-Xin (Bài 30)
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

## Bài 25 [RA-D31] — ĐSQH Phép Chia (Tất Cả): Đơn Hàng & Mặt Hàng (Bài 31)
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

## Bài 26 [RA-D32] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Bác Sĩ & Bệnh Nhân (Bài 32)
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

## Bài 27 [RA-D33] — ĐSQH Phép Chia (Tất Cả): Học Viên & Khóa Học (Bài 33)
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

## Bài 28 [RA-D34] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Tàu & Cảng Biển (Bài 34)
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

## Bài 29 [RA-D35] — ĐSQH Phép Chia (Tất Cả): Nhà Đầu Tư & Dự Án (Bài 35)
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

## Bài 30 [RA-D36] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Khách Hàng & Sảnh Tiệc (Bài 36)
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

## Bài 31 [RA-D37] — ĐSQH Phép Chia (Tất Cả): Độc Giả & Thể Loại Sách (Bài 37)
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

## Bài 32 [RA-D38] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Điểm Tiêm & Vắc-Xin (Bài 38)
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

## Bài 33 [RA-D39] — ĐSQH Phép Chia (Tất Cả): Đơn Hàng & Mặt Hàng (Bài 39)
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

## Bài 34 [RA-D40] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Bác Sĩ & Bệnh Nhân (Bài 40)
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

## Bài 35 [RA-D41] — ĐSQH Phép Chia (Tất Cả): Học Viên & Khóa Học (Bài 41)
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

## Bài 36 [RA-D42] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Tàu & Cảng Biển (Bài 42)
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

## Bài 37 [RA-D43] — ĐSQH Phép Chia (Tất Cả): Nhà Đầu Tư & Dự Án (Bài 43)
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

## Bài 38 [RA-D44] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Khách Hàng & Sảnh Tiệc (Bài 44)
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

## Bài 39 [RA-D45] — ĐSQH Phép Chia (Tất Cả): Độc Giả & Thể Loại Sách (Bài 45)
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

## Bài 40 [RA-D46] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Điểm Tiêm & Vắc-Xin (Bài 46)
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

## Bài 41 [RA-D47] — ĐSQH Phép Chia (Tất Cả): Đơn Hàng & Mặt Hàng (Bài 47)
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

## Bài 42 [RA-D48] — ĐSQH Gom Nhóm & Cực Trị MAX/MIN: Bác Sĩ & Bệnh Nhân (Bài 48)
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

## Bài 43 [RA-D49] — ĐSQH Phép Chia (Tất Cả): Học Viên & Khóa Học (Bài 49)
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
