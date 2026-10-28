# CHUYÊN ĐỀ 3: PHÉP CHIA (TẤT CẢ), GOM NHÓM & TRUY VẤN PHỨC HỢP
**Môn học:** IT004 — Cơ sở dữ liệu | **Hệ thống:** UIT Exam Mastery
**Biên soạn:** VÕ TRỌNG PHÚC | **Số lượng bài tập độc lập:** 45 bài chuẩn hóa

---

## Bài 01 [RA-D01] — ĐSQH Phép Chia: Sinh Viên Đăng Ký Tất Cả Môn Học Bắt Buộc Chuyên Ngành ATTT
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `SINHVIEN(MSSV, HOTEN, CHUYENNGANH), MONHOC(MAMH, TENMH, CHUYENNGANH, LOAI_MH), DANGKY(MSSV, MAMH, HOCKY)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã số sinh viên và họ tên của các sinh viên chuyên ngành 'An toan thong tin' đã đăng ký tham gia TẤT CẢ các môn học bắt buộc (LOAI_MH = 'Bat buoc') của chuyên ngành này.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MSSV, HOTEN}((π_{MSSV, MAMH}(σ_{CHUYENNGANH = 'An toan thong tin'}(SINHVIEN) ⋈ DANGKY) ÷ π_{MAMH}(σ_{CHUYENNGANH = 'An toan thong tin' ∧ LOAI_MH = 'Bat buoc'}(MONHOC))) ⋈ SINHVIEN)
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT SV.MSSV, SV.HOTEN
FROM SINHVIEN SV
WHERE SV.CHUYENNGANH = N'An toan thong tin'
  AND EXISTS (SELECT 1 FROM DANGKY DK WHERE DK.MSSV = SV.MSSV)
  AND NOT EXISTS (
    SELECT MH.MAMH FROM MONHOC MH
    WHERE MH.CHUYENNGANH = N'An toan thong tin' AND MH.LOAI_MH = N'Bat buoc'
    EXCEPT
    SELECT DK.MAMH FROM DANGKY DK WHERE DK.MSSV = SV.MSSV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MAMH}(σ_{CHUYENNGANH = 'An toan thong tin' ∧ LOAI_MH = 'Bat buoc'}(MONHOC)).
1. Bước 2 (Xác định tập ứng viên U): R_U = π_{MSSV}(σ_{CHUYENNGANH = 'An toan thong tin'}(SINHVIEN) ⋈ DANGKY).
1. Bước 3 (Tạo tập giả định và tìm các cặp thiếu): R_All = R_U × R_S; R_Missing = π_{MSSV}(R_All - π_{MSSV, MAMH}(DANGKY)).
1. Bước 4 (Kết quả cuối cùng): KQ = (R_U - R_Missing) ⋈ π_{MSSV, HOTEN}(SINHVIEN).

**Phân tích trường hợp biên (Edge Cases):**
Nếu tập chia S rỗng (chuyên ngành chưa có môn bắt buộc nào), theo lý thuyết ĐSQH chuẩn tắc R_U - ∅ = R_U trả về sinh viên ATTT đã đăng ký môn; mệnh đề SQL có điều kiện EXISTS tương ứng chặn sinh viên chưa đăng ký môn nào. Sinh viên ngành khác dù học đủ môn ATTT cũng bị loại bỏ bởi điều kiện lọc ứng viên.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 02 [RA-D02] — ĐSQH Phép Chia: Khách Hàng Mua Tất Cả Sản Phẩm Apple Năm 2024
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `KHACHHANG(MAKH, HOTEN, EMAIL), SANPHAM(MASP, TENSP, HANGSX, NAMSX), DONHANG(MADON, MAKH, NGAYDAT), CTHD(MADON, MASP)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã khách hàng và họ tên của các khách hàng đã mua TẤT CẢ các dòng sản phẩm của hãng 'Apple' phát hành trong năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAKH, HOTEN}(KHACHHANG ⋈ (π_{MAKH, MASP}(DONHANG ⋈ CTHD) ÷ π_{MASP}(σ_{HANGSX = 'Apple' ∧ NAMSX = 2024}(SANPHAM))))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT KH.MAKH, KH.HOTEN
FROM KHACHHANG KH
WHERE EXISTS (SELECT 1 FROM DONHANG DH WHERE DH.MAKH = KH.MAKH)
  AND NOT EXISTS (
    SELECT SP.MASP FROM SANPHAM SP WHERE SP.HANGSX = 'Apple' AND SP.NAMSX = 2024
    EXCEPT
    SELECT CT.MASP FROM DONHANG DH INNER JOIN CTHD CT ON DH.MADON = CT.MADON WHERE DH.MAKH = KH.MAKH
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): S = π_{MASP}(σ_{HANGSX = 'Apple' ∧ NAMSX = 2024}(SANPHAM)).
1. Bước 2 (Xác định tập ứng viên U): U = π_{MAKH}(DONHANG).
1. Bước 3 (Tìm khách hàng mua thiếu sản phẩm): Missing = π_{MAKH}((U × S) - π_{MAKH, MASP}(DONHANG ⋈ CTHD)).
1. Bước 4 (Khách hàng mua đủ): KQ = (U - Missing) ⋈ π_{MAKH, HOTEN}(KHACHHANG).

**Phân tích trường hợp biên (Edge Cases):**
Chặn miền ứng viên U bằng các khách hàng từng có đơn hàng; khách hàng mua nhiều đơn khác nhau gom lại đủ các sản phẩm của Apple vẫn được chấp nhận.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 03 [RA-D03] — ĐSQH Phép Chia: Bác Sĩ Tham Gia Tất Cả Đợt Tập Huấn Cấp Cứu
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `BACSI(MABS, HOTEN, MAKHOA), DOTTAPHUAN(MADOT, TENDOT, LOAI_TH), THAMGIA_TH(MABS, MADOT, KETQUA)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã bác sĩ và họ tên của các bác sĩ đã hoàn thành đạt (KETQUA = 'Dat') TẤT CẢ các đợt tập huấn thuộc loại 'Cap cuu hoi suc'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MABS, HOTEN}(BACSI ⋈ (π_{MABS, MADOT}(σ_{KETQUA = 'Dat'}(THAMGIA_TH)) ÷ π_{MADOT}(σ_{LOAI_TH = 'Cap cuu hoi suc'}(DOTTAPHUAN))))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT BS.MABS, BS.HOTEN
FROM BACSI BS
WHERE EXISTS (SELECT 1 FROM THAMGIA_TH TG WHERE TG.MABS = BS.MABS AND TG.KETQUA = N'Dat')
  AND NOT EXISTS (
    SELECT DTH.MADOT FROM DOTTAPHUAN DTH WHERE DTH.LOAI_TH = N'Cap cuu hoi suc'
    EXCEPT
    SELECT TG.MADOT FROM THAMGIA_TH TG WHERE TG.MABS = BS.MABS AND TG.KETQUA = N'Dat'
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Tập mục tiêu S = π_{MADOT}(σ_{LOAI_TH = 'Cap cuu hoi suc'}(DOTTAPHUAN)).
1. Bước 2: Quan hệ thực tế R_Actual = π_{MABS, MADOT}(σ_{KETQUA = 'Dat'}(THAMGIA_TH)).
1. Bước 3: Tập ứng viên U = π_{MABS}(R_Actual).
1. Bước 4: Missing = π_{MABS}((U × S) - R_Actual); KQ = (U - Missing) ⋈ BACSI.

**Phân tích trường hợp biên (Edge Cases):**
Bác sĩ có tham gia nhưng bị xếp loại 'Khong dat' ở một đợt bất kỳ sẽ không được xem là hoàn thành đợt đó.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 04 [RA-D04] — ĐSQH Phép Chia: Giảng Viên Đã Giảng Dạy Ở Tất Cả Cơ Sở Đào Tạo
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `GIANGVIEN(MAGV, HOTEN, MAKHOA), COSO(MACS, TENCS, THANHPHO), LOPHOCPHAN(MALHP, MAGV, MACS, HOCKY)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã giảng viên và họ tên của các giảng viên đã từng giảng dạy các lớp học phần tại TẤT CẢ các cơ sở đào tạo của nhà trường.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAGV, HOTEN}(GIANGVIEN ⋈ (π_{MAGV, MACS}(LOPHOCPHAN) ÷ π_{MACS}(COSO)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT GV.MAGV, GV.HOTEN
FROM GIANGVIEN GV
WHERE EXISTS (SELECT 1 FROM LOPHOCPHAN LHP WHERE LHP.MAGV = GV.MAGV)
  AND NOT EXISTS (
    SELECT CS.MACS FROM COSO CS
    EXCEPT
    SELECT LHP.MACS FROM LOPHOCPHAN LHP WHERE LHP.MAGV = GV.MAGV
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Tập chia S = π_{MACS}(COSO).
1. Bước 2: Tập ứng viên U = π_{MAGV}(LOPHOCPHAN).
1. Bước 3: Missing = π_{MAGV}((U × S) - π_{MAGV, MACS}(LOPHOCPHAN)).
1. Bước 4: KQ = (U - Missing) ⋈ π_{MAGV, HOTEN}(GIANGVIEN).

**Phân tích trường hợp biên (Edge Cases):**
Đảm bảo nhà trường có ít nhất 1 cơ sở; giảng viên mới tuyển chưa dạy lớp nào không được rơi vào kết quả.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 05 [RA-D05] — ĐSQH Phép Chia: Tàu Hàng Cập Bến Tất Cả Cảng Biển Loại 1 Miền Nam
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `TAU_HANG(MATAU, TENTAU, QUOCTICH), CANGBIEN(MACANG, TENCANG, PHANKY, VUNG_MIEN), LICH_CAPBEN(MATAU, MACANG, NGAYCAP)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã tàu và tên tàu của các tàu hàng đã từng cập bến TẤT CẢ các cảng biển xếp hạng 'Loai 1' tại vùng miền 'Mien Nam'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MATAU, TENTAU}(TAU_HANG ⋈ (π_{MATAU, MACANG}(LICH_CAPBEN) ÷ π_{MACANG}(σ_{PHANKY = 'Loai 1' ∧ VUNG_MIEN = 'Mien Nam'}(CANGBIEN))))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TH.MATAU, TH.TENTAU
FROM TAU_HANG TH
WHERE EXISTS (SELECT 1 FROM LICH_CAPBEN LCB WHERE LCB.MATAU = TH.MATAU)
  AND NOT EXISTS (
    SELECT CB.MACANG FROM CANGBIEN CB WHERE CB.PHANKY = 'Loai 1' AND CB.VUNG_MIEN = N'Mien Nam'
    EXCEPT
    SELECT LCB.MACANG FROM LICH_CAPBEN LCB WHERE LCB.MATAU = TH.MATAU
);
```

**Các bước suy luận tư duy:**
1. Bước 1: S = π_{MACANG}(σ_{PHANKY = 'Loai 1' ∧ VUNG_MIEN = 'Mien Nam'}(CANGBIEN)).
1. Bước 2: U = π_{MATAU}(LICH_CAPBEN).
1. Bước 3: Missing = π_{MATAU}((U × S) - π_{MATAU, MACANG}(LICH_CAPBEN)).
1. Bước 4: KQ = (U - Missing) ⋈ π_{MATAU, TENTAU}(TAU_HANG).

**Phân tích trường hợp biên (Edge Cases):**
Nếu miền Nam không có cảng loại 1 nào, truy vấn SQL NOT EXISTS sẽ trả về rỗng do điều kiện EXISTS U.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 06 [RA-D06] — ĐSQH Phép Chia: Nhân Viên Kinh Doanh Ký Hợp Đồng Với Tất Cả Đối Tác Chiến Lược
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `NHANVIEN(MANV, HOTEN, PHONGBAN), DOITAC(MADT, TENDT, PHANLOAI), HOPDONG(MAHD, MANV, MADT, NGAYKY)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã nhân viên và họ tên của các nhân viên phòng 'Kinh doanh' đã ký hợp đồng với TẤT CẢ các đối tác có phân loại là 'Chien luoc'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MANV, HOTEN}((π_{MANV, MADT}(σ_{PHONGBAN = 'Kinh doanh'}(NHANVIEN) ⋈ HOPDONG) ÷ π_{MADT}(σ_{PHANLOAI = 'Chien luoc'}(DOITAC))) ⋈ NHANVIEN)
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT NV.MANV, NV.HOTEN
FROM NHANVIEN NV
WHERE NV.PHONGBAN = N'Kinh doanh'
  AND EXISTS (SELECT 1 FROM HOPDONG HD WHERE HD.MANV = NV.MANV)
  AND NOT EXISTS (
    SELECT DT.MADT FROM DOITAC DT WHERE DT.PHANLOAI = N'Chien luoc'
    EXCEPT
    SELECT HD.MADT FROM HOPDONG HD WHERE HD.MANV = NV.MANV
);
```

**Các bước suy luận tư duy:**
1. Bước 1: S = π_{MADT}(σ_{PHANLOAI = 'Chien luoc'}(DOITAC)).
1. Bước 2: U = π_{MANV}(σ_{PHONGBAN = 'Kinh doanh'}(NHANVIEN) ⋈ HOPDONG).
1. Bước 3: Missing = π_{MANV}((U × S) - π_{MANV, MADT}(HOPDONG)).
1. Bước 4: KQ = (U - Missing) ⋈ π_{MANV, HOTEN}(NHANVIEN).

**Phân tích trường hợp biên (Edge Cases):**
Nhân viên phòng ban khác dù có ký hợp đồng với tất cả đối tác chiến lược cũng bị loại trừ bởi điều kiện phòng ban. Điều kiện EXISTS đảm bảo khi S rỗng chỉ trả về nhân viên kinh doanh đã ký hợp đồng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 07 [RA-D07] — ĐSQH Phép Chia: Thí Sinh Dự Thi Đủ Tất Cả Môn Tổ Hợp A00
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `THISINH(SBD, HOTEN, KHUVUC), TOHOP_MON(MATOHOP, MAMH), DIEMTHI(SBD, MAMH, DIEMSO)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm số báo danh và họ tên của các thí sinh đã tham gia thi và có điểm số (DIEMSO IS NOT NULL) ở TẤT CẢ các môn học thuộc tổ hợp xét tuyển 'A00'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{SBD, HOTEN}(THISINH ⋈ (π_{SBD, MAMH}(σ_{DIEMSO IS NOT NULL}(DIEMTHI)) ÷ π_{MAMH}(σ_{MATOHOP = 'A00'}(TOHOP_MON))))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TS.SBD, TS.HOTEN
FROM THISINH TS
WHERE EXISTS (SELECT 1 FROM DIEMTHI DT WHERE DT.SBD = TS.SBD AND DT.DIEMSO IS NOT NULL)
  AND NOT EXISTS (
    SELECT TH.MAMH FROM TOHOP_MON TH WHERE TH.MATOHOP = 'A00'
    EXCEPT
    SELECT DT.MAMH FROM DIEMTHI DT WHERE DT.SBD = TS.SBD AND DT.DIEMSO IS NOT NULL
);
```

**Các bước suy luận tư duy:**
1. Bước 1: S = π_{MAMH}(σ_{MATOHOP = 'A00'}(TOHOP_MON)) (gồm Toán, Lý, Hóa).
1. Bước 2: U = π_{SBD}(σ_{DIEMSO IS NOT NULL}(DIEMTHI)).
1. Bước 3: Missing = π_{SBD}((U × S) - π_{SBD, MAMH}(σ_{DIEMSO IS NOT NULL}(DIEMTHI))).
1. Bước 4: KQ = (U - Missing) ⋈ π_{SBD, HOTEN}(THISINH).

**Phân tích trường hợp biên (Edge Cases):**
Thí sinh vắng thi có DIEMSO mang giá trị NULL sẽ bị tính là chưa hoàn thành môn thi.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 08 [RA-D08] — ĐSQH Phép Chia: Phi Công Điều Khiển Tất Cả Dòng Máy Bay Thân Rộng
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `PHICONG(MAPC, HOTEN, HANG_BANG), MAYBAY(MAMB, DONG_MAYBAY, LOAITHAN), PHANCONG_BAY(MAPC, MAMB, NGAYBAY)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã phi công và họ tên của các phi công đã từng điều khiển TẤT CẢ các dòng máy bay có thiết kế là 'Than rong' (LOAITHAN = 'Than rong') của hãng.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAPC, HOTEN}(PHICONG ⋈ (π_{MAPC, DONG_MAYBAY}(PHANCONG_BAY ⋈ MAYBAY) ÷ π_{DONG_MAYBAY}(σ_{LOAITHAN = 'Than rong'}(MAYBAY))))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT PC.MAPC, PC.HOTEN
FROM PHICONG PC
WHERE EXISTS (SELECT 1 FROM PHANCONG_BAY PCB WHERE PCB.MAPC = PC.MAPC)
  AND NOT EXISTS (
    SELECT MB.DONG_MAYBAY FROM MAYBAY MB WHERE MB.LOAITHAN = N'Than rong'
    EXCEPT
    SELECT MB2.DONG_MAYBAY FROM PHANCONG_BAY PCB2 INNER JOIN MAYBAY MB2 ON PCB2.MAMB = MB2.MAMB WHERE PCB2.MAPC = PC.MAPC
);
```

**Các bước suy luận tư duy:**
1. Bước 1: S = π_{DONG_MAYBAY}(σ_{LOAITHAN = 'Than rong'}(MAYBAY)).
1. Bước 2: R_Actual = π_{MAPC, DONG_MAYBAY}(PHANCONG_BAY ⋈ MAYBAY).
1. Bước 3: U = π_{MAPC}(R_Actual); Missing = π_{MAPC}((U × S) - R_Actual).
1. Bước 4: KQ = (U - Missing) ⋈ π_{MAPC, HOTEN}(PHICONG).

**Phân tích trường hợp biên (Edge Cases):**
Mục tiêu chia là dòng máy bay (DONG_MAYBAY ví dụ Boeing 787, Airbus A350), không phải từng chiếc máy bay cụ thể.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 09 [RA-D09] — ĐSQH Phép Chia: Kỹ Sư Kiểm Thử Thực Hiện Tất Cả Test Case Hồi Quy Bảo Mật
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `KYSU(MAKS, HOTEN, TRINHDOHOCVAN), TESTCASE(MATC, LOAITC, MUC_DO), KETQUA_TEST(MAKS, MATC, NGAYCHAY, TRANGTHAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã kỹ sư và họ tên của các kỹ sư kiểm thử đã thực thi (TRANGTHAI = 'Passed') TẤT CẢ các test case thuộc loại kiểm thử hồi quy bảo mật (LOAITC = 'Security Regression').

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAKS, HOTEN}(KYSU ⋈ (π_{MAKS, MATC}(σ_{TRANGTHAI = 'Passed'}(KETQUA_TEST)) ÷ π_{MATC}(σ_{LOAITC = 'Security Regression'}(TESTCASE))))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT KS.MAKS, KS.HOTEN
FROM KYSU KS
WHERE EXISTS (SELECT 1 FROM KETQUA_TEST KQ WHERE KQ.MAKS = KS.MAKS AND KQ.TRANGTHAI = 'Passed')
  AND NOT EXISTS (
    SELECT TC.MATC FROM TESTCASE TC WHERE TC.LOAITC = 'Security Regression'
    EXCEPT
    SELECT KQ.MATC FROM KETQUA_TEST KQ WHERE KQ.MAKS = KS.MAKS AND KQ.TRANGTHAI = 'Passed'
);
```

**Các bước suy luận tư duy:**
1. Bước 1: S = π_{MATC}(σ_{LOAITC = 'Security Regression'}(TESTCASE)).
1. Bước 2: R_Actual = π_{MAKS, MATC}(σ_{TRANGTHAI = 'Passed'}(KETQUA_TEST)).
1. Bước 3: U = π_{MAKS}(R_Actual); Missing = π_{MAKS}((U × S) - R_Actual).
1. Bước 4: KQ = (U - Missing) ⋈ π_{MAKS, HOTEN}(KYSU).

**Phân tích trường hợp biên (Edge Cases):**
Test case chạy bị lỗi Failed không được tính là vượt qua kiểm thử.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 10 [RA-D10] — ĐSQH Phép Chia: Khách Hàng Lưu Trú Tại Tất Cả Khu Resort 5 Sao
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `KHACHHANG(MAKH, HOTEN, QUOCTICH), RESORT(MARS, TENRS, HANG_SAO, KHUVUC), PHIEUDAT(MAPD, MAKH, MARS, NGAYDEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã khách hàng và họ tên của các du khách đã từng đặt phòng và lưu trú tại TẤT CẢ các khu resort '5 sao' thuộc tập đoàn.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MAKH, HOTEN}(KHACHHANG ⋈ (π_{MAKH, MARS}(PHIEUDAT) ÷ π_{MARS}(σ_{HANG_SAO = '5 sao'}(RESORT))))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT KH.MAKH, KH.HOTEN
FROM KHACHHANG KH
WHERE EXISTS (SELECT 1 FROM PHIEUDAT PD WHERE PD.MAKH = KH.MAKH)
  AND NOT EXISTS (
    SELECT RS.MARS FROM RESORT RS WHERE RS.HANG_SAO = '5 sao'
    EXCEPT
    SELECT PD.MARS FROM PHIEUDAT PD WHERE PD.MAKH = KH.MAKH
);
```

**Các bước suy luận tư duy:**
1. Bước 1: S = π_{MARS}(σ_{HANG_SAO = '5 sao'}(RESORT)).
1. Bước 2: U = π_{MAKH}(PHIEUDAT).
1. Bước 3: Missing = π_{MAKH}((U × S) - π_{MAKH, MARS}(PHIEUDAT)).
1. Bước 4: KQ = (U - Missing) ⋈ π_{MAKH, HOTEN}(KHACHHANG).

**Phân tích trường hợp biên (Edge Cases):**
Khách hàng trung thành đã trải nghiệm toàn bộ chuỗi sản phẩm cao cấp.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 11 [RA-D11] — ĐSQH Phép Chia: Sinh Viên Tham Gia Tất Cả Chiến Dịch Mùa Hè Xanh
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `SINHVIEN(MSSV, HOTEN, KHOA), CHIENDICH(MACD, TENCD, NAM), DANGKY_CD(MSSV, MACD, VAITRO)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã sinh viên và họ tên của các sinh viên khóa 'K2021' đã tham gia TẤT CẢ các chiến dịch Mùa hè xanh được tổ chức trong giai đoạn từ năm 2022 đến 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MSSV, HOTEN}((π_{MSSV, MACD}(σ_{KHOA = 'K2021'}(SINHVIEN) ⋈ DANGKY_CD) ÷ π_{MACD}(σ_{NAM ≥ 2022 ∧ NAM ≤ 2024}(CHIENDICH))) ⋈ SINHVIEN)
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT SV.MSSV, SV.HOTEN
FROM SINHVIEN SV
WHERE SV.KHOA = 'K2021'
  AND EXISTS (SELECT 1 FROM DANGKY_CD DK WHERE DK.MSSV = SV.MSSV)
  AND NOT EXISTS (
    SELECT CD.MACD FROM CHIENDICH CD WHERE CD.NAM BETWEEN 2022 AND 2024
    EXCEPT
    SELECT DK.MACD FROM DANGKY_CD DK WHERE DK.MSSV = SV.MSSV
);
```

**Các bước suy luận tư duy:**
1. Bước 1: S = π_{MACD}(σ_{NAM ≥ 2022 ∧ NAM ≤ 2024}(CHIENDICH)).
1. Bước 2: U = π_{MSSV}(σ_{KHOA = 'K2021'}(SINHVIEN) ⋈ DANGKY_CD).
1. Bước 3: Missing = π_{MSSV}((U × S) - π_{MSSV, MACD}(DANGKY_CD)).
1. Bước 4: KQ = (U - Missing) ⋈ π_{MSSV, HOTEN}(SINHVIEN).

**Phân tích trường hợp biên (Edge Cases):**
Chỉ xét sinh viên khóa K2021 có tham gia phong trào Đoàn hội liên tục các năm. Điều kiện EXISTS đảm bảo khi S rỗng chỉ trả về sinh viên K2021 có đăng ký tham gia chiến dịch.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 12 [RA-D12] — ĐSQH Phép Chia: Độc Giả Mượn Tất Cả Các Tập Bộ Sách Lịch Sử
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOCGIA(MADG, HOTEN, SDT), CUONSACH(MACS, MABO, SOTAP), PHIEUMUON(MAPM, MADG, NGAYMUON), CTPM(MAPM, MACS)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã độc giả và họ tên của các bạn đọc đã mượn TẤT CẢ các tập sách thuộc bộ sách có mã 'BO_HIST_01'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MADG, HOTEN}(DOCGIA ⋈ (π_{MADG, MACS}(PHIEUMUON ⋈ CTPM) ÷ π_{MACS}(σ_{MABO = 'BO_HIST_01'}(CUONSACH))))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT DG.MADG, DG.HOTEN
FROM DOCGIA DG
WHERE EXISTS (SELECT 1 FROM PHIEUMUON PM WHERE PM.MADG = DG.MADG)
  AND NOT EXISTS (
    SELECT CS.MACS FROM CUONSACH CS WHERE CS.MABO = 'BO_HIST_01'
    EXCEPT
    SELECT CT.MACS FROM PHIEUMUON PM INNER JOIN CTPM CT ON PM.MAPM = CT.MAPM WHERE PM.MADG = DG.MADG
);
```

**Các bước suy luận tư duy:**
1. Bước 1: S = π_{MACS}(σ_{MABO = 'BO_HIST_01'}(CUONSACH)).
1. Bước 2: U = π_{MADG}(PHIEUMUON).
1. Bước 3: Missing = π_{MADG}((U × S) - π_{MADG, MACS}(PHIEUMUON ⋈ CTPM)).
1. Bước 4: KQ = (U - Missing) ⋈ π_{MADG, HOTEN}(DOCGIA).

**Phân tích trường hợp biên (Edge Cases):**
Độc giả có thể mượn từng tập ở các lần mượn khác nhau.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 13 [RA-D13] — ĐSQH Phép Chia: Cửa Hàng Tiện Lợi Phân Phối Tất CẢ Sản Phẩm Sữa Vinamilk
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `CUAHANG(MACH, TENCH, QUAN), SANPHAM(MASP, TENSP, NHANHIEU), NHAPHANG(MAPN, MACH, NGAYNHAP), CT_NHAP(MAPN, MASP, SOLUONG)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã cửa hàng và tên cửa hàng tại quận 'Thu Duc' đã từng nhập phân phối TẤT CẢ các sản phẩm thuộc nhãn hiệu 'Vinamilk'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MACH, TENCH}((π_{MACH, MASP}(σ_{QUAN = 'Thu Duc'}(CUAHANG) ⋈ NHAPHANG ⋈ CT_NHAP) ÷ π_{MASP}(σ_{NHANHIEU = 'Vinamilk'}(SANPHAM))) ⋈ CUAHANG)
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT CH.MACH, CH.TENCH
FROM CUAHANG CH
WHERE CH.QUAN = N'Thu Duc'
  AND EXISTS (SELECT 1 FROM NHAPHANG NH WHERE NH.MACH = CH.MACH)
  AND NOT EXISTS (
    SELECT SP.MASP FROM SANPHAM SP WHERE SP.NHANHIEU = 'Vinamilk'
    EXCEPT
    SELECT CT.MASP FROM NHAPHANG NH INNER JOIN CT_NHAP CT ON NH.MAPN = CT.MAPN WHERE NH.MACH = CH.MACH
);
```

**Các bước suy luận tư duy:**
1. Bước 1: S = π_{MASP}(σ_{NHANHIEU = 'Vinamilk'}(SANPHAM)).
1. Bước 2: U = π_{MACH}(σ_{QUAN = 'Thu Duc'}(CUAHANG) ⋈ NHAPHANG).
1. Bước 3: Missing = π_{MACH}((U × S) - π_{MACH, MASP}(NHAPHANG ⋈ CT_NHAP)).
1. Bước 4: KQ = (U - Missing) ⋈ π_{MACH, TENCH}(CUAHANG).

**Phân tích trường hợp biên (Edge Cases):**
Cửa hàng ở quận khác phân phối đủ vẫn bị loại bởi điều kiện QUAN = 'Thu Duc'. EXISTS bảo đảm khi S rỗng chỉ các cửa hàng tại Thủ Đức có phát sinh nhập hàng mới được trả về.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 14 [RA-D14] — ĐSQH Phép Chia: Bệnh Nhân Tiêm Đủ Phác Đồ 5 Mũi Phòng Dại
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `BENHNHAN(MABN, HOTEN, SDT), MUITIEM_CHUAN(MAMUI, TENMUI, NGAYTHU), LICHSU_TIEM(MABN, MAMUI, NGAYTIEM_THUC, TRANGTHAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã bệnh nhân và họ tên của các bệnh nhân đã tiêm hoàn tất (TRANGTHAI = 'Hoan thanh') TẤT CẢ các mũi tiêm trong phác đồ phòng dại (thuộc danh mục MUITIEM_CHUAN).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MABN, HOTEN}(BENHNHAN ⋈ (π_{MABN, MAMUI}(σ_{TRANGTHAI = 'Hoan thanh'}(LICHSU_TIEM)) ÷ π_{MAMUI}(MUITIEM_CHUAN)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT BN.MABN, BN.HOTEN
FROM BENHNHAN BN
WHERE EXISTS (SELECT 1 FROM LICHSU_TIEM LS WHERE LS.MABN = BN.MABN AND LS.TRANGTHAI = N'Hoan thanh')
  AND NOT EXISTS (
    SELECT MTC.MAMUI FROM MUITIEM_CHUAN MTC
    EXCEPT
    SELECT LS.MAMUI FROM LICHSU_TIEM LS WHERE LS.MABN = BN.MABN AND LS.TRANGTHAI = N'Hoan thanh'
);
```

**Các bước suy luận tư duy:**
1. Bước 1: S = π_{MAMUI}(MUITIEM_CHUAN).
1. Bước 2: R_Actual = π_{MABN, MAMUI}(σ_{TRANGTHAI = 'Hoan thanh'}(LICHSU_TIEM)).
1. Bước 3: U = π_{MABN}(R_Actual); Missing = π_{MABN}((U × S) - R_Actual).
1. Bước 4: KQ = (U - Missing) ⋈ π_{MABN, HOTEN}(BENHNHAN).

**Phân tích trường hợp biên (Edge Cases):**
Bệnh nhân bỏ dở giữa chừng (mới tiêm 3/5 mũi) sẽ có Missing khác rỗng và bị loại.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 15 [RA-D15] — ĐSQH Phép Chia: Lập Trình Viên Đóng Góp Vào Tất Cả Microservices Lõi
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `LAPTRINHVIEN(MALTV, HOTEN, PHONG_DEV), MICROSERVICE(MASVC, TENSVC, PHANLOAI), COMMIT_LOG(MA_COMMIT, MALTV, MASVC, NGAY_COMMIT)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã lập trình viên và họ tên của các lập trình viên thuộc phòng 'Backend' đã từng đóng góp commit vào TẤT CẢ các microservice có phân loại là 'Core Service'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MALTV, HOTEN}((π_{MALTV, MASVC}(σ_{PHONG_DEV = 'Backend'}(LAPTRINHVIEN) ⋈ COMMIT_LOG) ÷ π_{MASVC}(σ_{PHANLOAI = 'Core Service'}(MICROSERVICE))) ⋈ LAPTRINHVIEN)
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT LTV.MALTV, LTV.HOTEN
FROM LAPTRINHVIEN LTV
WHERE LTV.PHONG_DEV = 'Backend'
  AND EXISTS (SELECT 1 FROM COMMIT_LOG CL WHERE CL.MALTV = LTV.MALTV)
  AND NOT EXISTS (
    SELECT MS.MASVC FROM MICROSERVICE MS WHERE MS.PHANLOAI = 'Core Service'
    EXCEPT
    SELECT CL.MASVC FROM COMMIT_LOG CL WHERE CL.MALTV = LTV.MALTV
);
```

**Các bước suy luận tư duy:**
1. Bước 1: S = π_{MASVC}(σ_{PHANLOAI = 'Core Service'}(MICROSERVICE)).
1. Bước 2: U = π_{MALTV}(σ_{PHONG_DEV = 'Backend'}(LAPTRINHVIEN) ⋈ COMMIT_LOG).
1. Bước 3: Missing = π_{MALTV}((U × S) - π_{MALTV, MASVC}(COMMIT_LOG)).
1. Bước 4: KQ = (U - Missing) ⋈ π_{MALTV, HOTEN}(LAPTRINHVIEN).

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm kiến trúc microservices được bao phủ kiểm tra đóng góp mã nguồn đầy đủ. EXISTS bảo đảm khi S rỗng chỉ xét lập trình viên Backend có commit.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `target_and_candidate_definition`: 0.5đ
- `cartesian_and_subtraction_correctness`: 0.6đ
- `edge_case_and_boundary_handling`: 0.4đ

---

## Bài 16 [RA-D16] — ĐSQH Gom Nhóm: Thống Kê Số Lượng Sinh Viên Theo Từng Ngành
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NGANH(MANGANH, TENNGANH), SINHVIEN(MSSV, HOTEN, MANGANH)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã ngành, tên ngành và số lượng sinh viên của các ngành đào tạo có từ 150 sinh viên trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{SO_SV ≥ 150}(_{MANGANH, TENNGANH} γ _{COUNT(MSSV) → SO_SV}(NGANH ⋈ SINHVIEN))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT N.MANGANH, N.TENNGANH, COUNT(SV.MSSV) AS SO_SV
FROM NGANH N INNER JOIN SINHVIEN SV ON N.MANGANH = SV.MANGANH
GROUP BY N.MANGANH, N.TENNGANH
HAVING COUNT(SV.MSSV) >= 150;
```

**Các bước suy luận tư duy:**
1. Bước 1: Kết nối NGANH với SINHVIEN theo khóa MANGANH.
1. Bước 2: Gom nhóm theo MANGANH, TENNGANH và áp dụng hàm tổng hợp COUNT(MSSV) đổi tên thành SO_SV.
1. Bước 3: Áp dụng phép chọn σ trên kết quả gom nhóm với điều kiện SO_SV >= 150.

**Phân tích trường hợp biên (Edge Cases):**
Nếu ngành chưa có sinh viên nào, INNER JOIN sẽ loại bỏ ngành đó; điều kiện >= 150 không bị ảnh hưởng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 17 [RA-D17] — ĐSQH Gom Nhóm: Tính Tổng Tiền Mua Hàng Khách Hàng VIP Năm 2024
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG(MAKH, HOTEN), DONHANG(MADON, MAKH, NGAYDAT, TONGTIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã khách hàng, họ tên và tổng số tiền đã mua của các khách hàng có tổng chi tiêu trong năm 2024 vượt quá 50.000.000 VNĐ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_CHITIEU > 50000000}(_{KHACHHANG.MAKH, HOTEN} γ _{SUM(TONGTIEN) → TONG_CHITIEU}(KHACHHANG ⋈ σ_{NGAYDAT ≥ '2024-01-01' ∧ NGAYDAT ≤ '2024-12-31'}(DONHANG)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT KH.MAKH, KH.HOTEN, SUM(DH.TONGTIEN) AS TONG_CHITIEU
FROM KHACHHANG KH INNER JOIN DONHANG DH ON KH.MAKH = DH.MAKH
WHERE DH.NGAYDAT BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY KH.MAKH, KH.HOTEN
HAVING SUM(DH.TONGTIEN) > 50000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc bảng DONHANG theo khoảng thời gian năm 2024.
1. Bước 2: Kết nối với KHACHHANG theo MAKH.
1. Bước 3: Gom nhóm theo MAKH, HOTEN và tính SUM(TONGTIEN) -> TONG_CHITIEU.
1. Bước 4: Lọc các nhóm có TONG_CHITIEU > 50.000.000.

**Phân tích trường hợp biên (Edge Cases):**
Lọc ngày trước khi gom nhóm tương ứng mệnh đề WHERE trong SQL.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 18 [RA-D18] — ĐSQH Gom Nhóm: Đếm Số Ca Mổ Của Bác Sĩ Ngoại Khoa Quý 4
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BACSI(MABS, HOTEN, CHUYENKHOA), CAMO(MACAMO, MABS_CHINH, NGAYMO, KETQUA)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã bác sĩ, họ tên và số ca mổ đã thực hiện của các bác sĩ chuyên khoa 'Ngoai khoa' đã mổ chính từ 10 ca trở lên trong quý 4 năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{SO_CAMO ≥ 10}(_{BACSI.MABS, HOTEN} γ _{COUNT(MACAMO) → SO_CAMO}(σ_{CHUYENKHOA = 'Ngoai khoa'}(BACSI) ⋈_{MABS = MABS_CHINH} σ_{NGAYMO ≥ '2024-10-01' ∧ NGAYMO ≤ '2024-12-31'}(CAMO)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT BS.MABS, BS.HOTEN, COUNT(CM.MACAMO) AS SO_CAMO
FROM BACSI BS INNER JOIN CAMO CM ON BS.MABS = CM.MABS_CHINH
WHERE BS.CHUYENKHOA = N'Ngoai khoa' AND CM.NGAYMO BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY BS.MABS, BS.HOTEN
HAVING COUNT(CM.MACAMO) >= 10;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc bác sĩ ngoại khoa và lọc ca mổ trong quý 4/2024.
1. Bước 2: Kết nối theo MABS = MABS_CHINH.
1. Bước 3: Gom nhóm theo MABS, HOTEN và đếm COUNT(MACAMO) -> SO_CAMO.
1. Bước 4: Chọn các nhóm có SO_CAMO >= 10.

**Phân tích trường hợp biên (Edge Cases):**
Cần phân biệt bác sĩ mổ chính với bác sĩ phụ mổ nếu có.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 19 [RA-D19] — ĐSQH Gom Nhóm: Tính Điểm Trung Bình Tích Lũy Theo Từng Lớp
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `LOP(MALOP, TENLOP, KHOAHOC), SINHVIEN(MSSV, HOTEN, MALOP, DIEM_TBTL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã lớp, tên lớp và điểm trung bình tích lũy trung bình của lớp đối với các lớp thuộc khóa 'K2023' có điểm trung bình toàn lớp từ 8.0 trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{DTB_LOP ≥ 8.0}(_{LOP.MALOP, TENLOP} γ _{AVG(DIEM_TBTL) → DTB_LOP}(σ_{KHOAHOC = 'K2023'}(LOP) ⋈ SINHVIEN))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT L.MALOP, L.TENLOP, AVG(SV.DIEM_TBTL) AS DTB_LOP
FROM LOP L INNER JOIN SINHVIEN SV ON L.MALOP = SV.MALOP
WHERE L.KHOAHOC = 'K2023'
GROUP BY L.MALOP, L.TENLOP
HAVING AVG(SV.DIEM_TBTL) >= 8.0;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc các lớp khóa K2023 và kết nối với SINHVIEN theo MALOP.
1. Bước 2: Gom nhóm theo MALOP, TENLOP.
1. Bước 3: Tính hàm tổng hợp AVG(DIEM_TBTL) đặt tên DTB_LOP.
1. Bước 4: Lọc điều kiện DTB_LOP >= 8.0.

**Phân tích trường hợp biên (Edge Cases):**
Hàm AVG bỏ qua các giá trị NULL trong tập dữ liệu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 20 [RA-D20] — ĐSQH Gom Nhóm: Tổng Doanh Thu Chi Nhánh Nhà Thuốc Quý 4
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHATHUOC(MANT, TENNT, QUAN), HOADON(MAHD, MANT, NGAYLAP, TONGTIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã nhà thuốc, tên nhà thuốc tại 'Quan 1' có tổng doanh thu trong quý 4/2024 đạt từ 200.000.000 VNĐ trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{DOANHTHU ≥ 200000000}(_{NHATHUOC.MANT, TENNT} γ _{SUM(TONGTIEN) → DOANHTHU}(σ_{QUAN = 'Quan 1'}(NHATHUOC) ⋈ σ_{NGAYLAP ≥ '2024-10-01' ∧ NGAYLAP ≤ '2024-12-31'}(HOADON)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT NT.MANT, NT.TENNT, SUM(HD.TONGTIEN) AS DOANHTHU
FROM NHATHUOC NT INNER JOIN HOADON HD ON NT.MANT = HD.MANT
WHERE NT.QUAN = 'Quan 1' AND HD.NGAYLAP BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY NT.MANT, NT.TENNT
HAVING SUM(HD.TONGTIEN) >= 200000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc nhà thuốc ở Quận 1 và hóa đơn trong quý 4.
1. Bước 2: Kết nối theo MANT.
1. Bước 3: Gom nhóm theo MANT, TENNT và tính SUM(TONGTIEN).
1. Bước 4: Lọc ngưỡng DOANHTHU >= 200.000.000.

**Phân tích trường hợp biên (Edge Cases):**
Phép chọn trước kết nối giúp giảm thiểu tối đa kích thước dữ liệu cần gom nhóm.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 21 [RA-D21] — ĐSQH Gom Nhóm: Số Lượt Chuyến Bay Khai Thác Theo Tàu Bay
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `MAYBAY(MAMB, SOHIEU, LOAIMB), CHUYENBAY(MACB, MAMB, NGAYBAY, TRANGTHAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã máy bay, số hiệu và số chuyến bay đã hoàn thành của các máy bay thực hiện từ 40 chuyến bay thành công (TRANGTHAI = 'Hoan thanh') trở lên trong tháng 11/2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{SO_CHUYEN ≥ 40}(_{MAYBAY.MAMB, SOHIEU} γ _{COUNT(MACB) → SO_CHUYEN}(MAYBAY ⋈ σ_{TRANGTHAI = 'Hoan thanh' ∧ NGAYBAY ≥ '2024-11-01' ∧ NGAYBAY ≤ '2024-11-30'}(CHUYENBAY)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MB.MAMB, MB.SOHIEU, COUNT(CB.MACB) AS SO_CHUYEN
FROM MAYBAY MB INNER JOIN CHUYENBAY CB ON MB.MAMB = CB.MAMB
WHERE CB.TRANGTHAI = N'Hoan thanh' AND CB.NGAYBAY BETWEEN '2024-11-01' AND '2024-11-30'
GROUP BY MB.MAMB, MB.SOHIEU
HAVING COUNT(CB.MACB) >= 40;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc các chuyến bay hoàn thành trong tháng 11/2024.
1. Bước 2: Kết nối với MAYBAY theo MAMB.
1. Bước 3: Gom nhóm theo MAMB, SOHIEU và đếm COUNT(MACB).
1. Bước 4: Chọn các tàu bay có SO_CHUYEN >= 40.

**Phân tích trường hợp biên (Edge Cases):**
Các chuyến bay bị hủy (TRANGTHAI = 'Huy') bị loại bỏ bởi phép chọn.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 22 [RA-D22] — ĐSQH Gom Nhóm: Tổng Khối Lượng Rác Tái Chế Theo Khu Vực
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHUVUC_GOM(MAKV, TENKV, QUAN), CHUYEN_GOM(MACHUYEN, MAKV, NGAYGOM, KHOILUONG_KG, LOAIRAC)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã khu vực gom, tên khu vực tại quận 'Binh Thanh' có tổng khối lượng rác thuộc loại 'Tai che' thu gom trong tháng 10/2024 đạt từ 10.000 kg trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_KG ≥ 10000}(_{KHUVUC_GOM.MAKV, TENKV} γ _{SUM(KHOILUONG_KG) → TONG_KG}(σ_{QUAN = 'Binh Thanh'}(KHUVUC_GOM) ⋈ σ_{LOAIRAC = 'Tai che' ∧ NGAYGOM ≥ '2024-10-01' ∧ NGAYGOM ≤ '2024-10-31'}(CHUYEN_GOM)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT KV.MAKV, KV.TENKV, SUM(CG.KHOILUONG_KG) AS TONG_KG
FROM KHUVUC_GOM KV INNER JOIN CHUYEN_GOM CG ON KV.MAKV = CG.MAKV
WHERE KV.QUAN = N'Binh Thanh' AND CG.LOAIRAC = N'Tai che' AND CG.NGAYGOM BETWEEN '2024-10-01' AND '2024-10-31'
GROUP BY KV.MAKV, KV.TENKV
HAVING SUM(CG.KHOILUONG_KG) >= 10000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc khu vực thuộc quận Bình Thạnh và các chuyến gom rác tái chế tháng 10.
1. Bước 2: Kết nối theo MAKV.
1. Bước 3: Gom nhóm MAKV, TENKV và tính SUM(KHOILUONG_KG).
1. Bước 4: Lọc TONG_KG >= 10.000.

**Phân tích trường hợp biên (Edge Cases):**
Cần bảo đảm đơn vị tính khối lượng đồng nhất (kg).

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 23 [RA-D23] — ĐSQH Gom Nhóm: Số Đề Tài Nghiên Cứu Khoa Học Của Bộ Môn
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BOMON(MABM, TENBM, MAKHOA), DETAI(MADT, MABM, KETQUA_NT, NAM_NT)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã bộ môn, tên bộ môn và số lượng đề tài nghiên cứu khoa học đạt loại 'Xuat sac' được nghiệm thu trong năm 2024 của các bộ môn có từ 3 đề tài xuất sắc trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{SO_DETAI ≥ 3}(_{BOMON.MABM, TENBM} γ _{COUNT(MADT) → SO_DETAI}(BOMON ⋈ σ_{KETQUA_NT = 'Xuat sac' ∧ NAM_NT = 2024}(DETAI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT BM.MABM, BM.TENBM, COUNT(DT.MADT) AS SO_DETAI
FROM BOMON BM INNER JOIN DETAI DT ON BM.MABM = DT.MABM
WHERE DT.KETQUA_NT = N'Xuat sac' AND DT.NAM_NT = 2024
GROUP BY BM.MABM, BM.TENBM
HAVING COUNT(DT.MADT) >= 3;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc đề tài đạt xuất sắc nghiệm thu năm 2024.
1. Bước 2: Kết nối với BOMON theo MABM.
1. Bước 3: Gom nhóm theo MABM, TENBM và đếm số đề tài.
1. Bước 4: Lọc SO_DETAI >= 3.

**Phân tích trường hợp biên (Edge Cases):**
Các bộ môn không có đề tài nào xuất sắc sẽ tự động không thỏa mãn điều kiện HAVING.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 24 [RA-D24] — ĐSQH Gom Nhóm: Giá Cước Trung Bình Chuyến Xe Theo Tài Xế
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TAIXE(MATX, HOTEN, LOAIXE), CHUYENXE(MACHUYEN, MATX, GIA_CUOC, TRANGTHAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã tài xế, họ tên của các tài xế lái xe 'O to 4 cho' đã hoàn thành (TRANGTHAI = 'Hoan thanh') từ 100 chuyến xe trở lên và có giá cước trung bình mỗi chuyến đạt trên 120.000 VNĐ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{SO_CHUYEN ≥ 100 ∧ CUOC_TB > 120000}(_{TAIXE.MATX, HOTEN} γ _{COUNT(MACHUYEN) → SO_CHUYEN, AVG(GIA_CUOC) → CUOC_TB}(σ_{LOAIXE = 'O to 4 cho'}(TAIXE) ⋈ σ_{TRANGTHAI = 'Hoan thanh'}(CHUYENXE)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TX.MATX, TX.HOTEN, COUNT(CX.MACHUYEN) AS SO_CHUYEN, AVG(CX.GIA_CUOC) AS CUOC_TB
FROM TAIXE TX INNER JOIN CHUYENXE CX ON TX.MATX = CX.MATX
WHERE TX.LOAIXE = 'O to 4 cho' AND CX.TRANGTHAI = N'Hoan thanh'
GROUP BY TX.MATX, TX.HOTEN
HAVING COUNT(CX.MACHUYEN) >= 100 AND AVG(CX.GIA_CUOC) > 120000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc tài xế ô tô 4 chỗ và chuyến xe đã hoàn thành.
1. Bước 2: Kết nối theo MATX.
1. Bước 3: Gom nhóm theo MATX, HOTEN, tính đồng thời COUNT và AVG.
1. Bước 4: Áp dụng vị từ chọn kết hợp cả 2 tiêu chí số chuyến và giá cước trung bình.

**Phân tích trường hợp biên (Edge Cases):**
Toán tử gamma cho phép định nghĩa nhiều hàm tổng hợp cùng lúc.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 25 [RA-D25] — ĐSQH Gom Nhóm: Số Phòng Đã Cho Thuê Theo Tòa Nhà Chung Cư
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TOANHA(MATN, TENTN, DIACHI), CANHO(MACAN, MATN, TRANGTHAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã tòa nhà, tên tòa nhà và số lượng căn hộ đang cho thuê (TRANGTHAI = 'Dang thue') của các tòa nhà có từ 50 căn hộ đang cho thuê trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{SO_CAN_THUE ≥ 50}(_{TOANHA.MATN, TENTN} γ _{COUNT(MACAN) → SO_CAN_THUE}(TOANHA ⋈ σ_{TRANGTHAI = 'Dang thue'}(CANHO)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TH.MATN, TH.TENTN, COUNT(CH.MACAN) AS SO_CAN_THUE
FROM TOANHA TH INNER JOIN CANHO CH ON TH.MATN = CH.MATN
WHERE CH.TRANGTHAI = N'Dang thue'
GROUP BY TH.MATN, TH.TENTN
HAVING COUNT(CH.MACAN) >= 50;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc căn hộ đang thuê.
1. Bước 2: Kết nối với TOANHA theo MATN.
1. Bước 3: Gom nhóm theo MATN, TENTN và đếm số căn.
1. Bước 4: Lọc SO_CAN_THUE >= 50.

**Phân tích trường hợp biên (Edge Cases):**
Tránh đếm các căn hộ trống hoặc đang sửa chữa.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 26 [RA-D26] — ĐSQH Gom Nhóm: Tổng Lượng Mưa Quan Trắc Theo Trạm Khí Tượng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TRAM_DO(MATRAM, TENTRAM, TINH_TP), PHIEN_DODAC(MAPHIEN, MATRAM, THOIDIEM, LUONGMUA_MM)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã trạm, tên trạm tại tỉnh 'Quang Nam' có tổng lượng mưa đo được trong tháng 10/2024 vượt quá 1.000 mm.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_MUA > 1000}(_{TRAM_DO.MATRAM, TENTRAM} γ _{SUM(LUONGMUA_MM) → TONG_MUA}(σ_{TINH_TP = 'Quang Nam'}(TRAM_DO) ⋈ σ_{THOIDIEM ≥ '2024-10-01' ∧ THOIDIEM ≤ '2024-10-31'}(PHIEN_DODAC)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TD.MATRAM, TD.TENTRAM, SUM(PD.LUONGMUA_MM) AS TONG_MUA
FROM TRAM_DO TD INNER JOIN PHIEN_DODAC PD ON TD.MATRAM = PD.MATRAM
WHERE TD.TINH_TP = N'Quang Nam' AND PD.THOIDIEM BETWEEN '2024-10-01' AND '2024-10-31'
GROUP BY TD.MATRAM, TD.TENTRAM
HAVING SUM(PD.LUONGMUA_MM) > 1000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc trạm ở Quảng Nam và các phiên đo tháng 10/2024.
1. Bước 2: Kết nối theo MATRAM.
1. Bước 3: Gom nhóm theo MATRAM, TENTRAM và tính tổng lượng mưa.
1. Bước 4: Chọn các trạm có TONG_MUA > 1000 mm.

**Phân tích trường hợp biên (Edge Cases):**
Lượng mưa mang giá trị thực (DECIMAL/FLOAT).

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 27 [RA-D27] — ĐSQH Gom Nhóm: Tổng Tiền Thuê Đất Theo Doanh Nghiệp KCN
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DOANHNGHIEP(MADN, TENDN, QUOCTICH), HOPDONG_THUE(MAHD, MADN, GIATHUE_HANGNAM, TRANGTHAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã doanh nghiệp, tên doanh nghiệp có quốc tịch 'Nhat Ban' đang có tổng giá trị thuê đất hàng năm trên các hợp đồng còn hiệu lực (TRANGTHAI = 'Hieu luc') vượt quá 10.000.000.000 VNĐ (10 tỷ VNĐ).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN_THUE > 10000000000}(_{DOANHNGHIEP.MADN, TENDN} γ _{SUM(GIATHUE_HANGNAM) → TONG_TIEN_THUE}(σ_{QUOCTICH = 'Nhat Ban'}(DOANHNGHIEP) ⋈ σ_{TRANGTHAI = 'Hieu luc'}(HOPDONG_THUE)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT DN.MADN, DN.TENDN, SUM(HD.GIATHUE_HANGNAM) AS TONG_TIEN_THUE
FROM DOANHNGHIEP DN INNER JOIN HOPDONG_THUE HD ON DN.MADN = HD.MADN
WHERE DN.QUOCTICH = N'Nhat Ban' AND HD.TRANGTHAI = N'Hieu luc'
GROUP BY DN.MADN, DN.TENDN
HAVING SUM(HD.GIATHUE_HANGNAM) > 10000000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc doanh nghiệp Nhật Bản và hợp đồng còn hiệu lực.
1. Bước 2: Kết nối theo MADN.
1. Bước 3: Gom nhóm MADN, TENDN và tính SUM(GIATHUE_HANGNAM).
1. Bước 4: Lọc ngưỡng 10 tỷ VNĐ.

**Phân tích trường hợp biên (Edge Cases):**
Hợp đồng hết hạn hoặc đã thanh lý bị loại bỏ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 28 [RA-D28] — ĐSQH Gom Nhóm: Đếm Số Bản Thu Âm Triệu Stream Của Nhạc Sĩ
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHACSI(MANS, HOTEN, BUTDANH), BAN_THUAM(MABT, MANS, LUOT_STREAM, NAM_PHATHANH)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã nhạc sĩ, bút danh và số lượng bản thu âm phát hành năm 2024 đạt từ 1.000.000 lượt stream trở lên của các nhạc sĩ có từ 3 bản thu âm triệu stream trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{SO_HIT ≥ 3}(_{NHACSI.MANS, BUTDANH} γ _{COUNT(MABT) → SO_HIT}(NHACSI ⋈ σ_{LUOT_STREAM ≥ 1000000 ∧ NAM_PHATHANH = 2024}(BAN_THUAM)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT NS.MANS, NS.BUTDANH, COUNT(BT.MABT) AS SO_HIT
FROM NHACSI NS INNER JOIN BAN_THUAM BT ON NS.MANS = BT.MANS
WHERE BT.LUOT_STREAM >= 1000000 AND BT.NAM_PHATHANH = 2024
GROUP BY NS.MANS, NS.BUTDANH
HAVING COUNT(BT.MABT) >= 3;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc bản thu âm đạt mốc 1 triệu stream năm 2024.
1. Bước 2: Kết nối với NHACSI theo MANS.
1. Bước 3: Gom nhóm MANS, BUTDANH và đếm COUNT(MABT).
1. Bước 4: Lọc SO_HIT >= 3.

**Phân tích trường hợp biên (Edge Cases):**
Cần bảo đảm LUOT_STREAM dùng kiểu dữ liệu số lớn (BIGINT).

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 29 [RA-D29] — ĐSQH Gom Nhóm: Số Lượng Thiết Bị Y Tế Hỏng Cần Bảo Trì
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHOA_PHONG(MAKHOA, TENKHOA), THIETBI(MATB, MAKHOA, TRANGTHAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Cho biết mã khoa phòng, tên khoa phòng và số lượng thiết bị đang bị hỏng (TRANGTHAI = 'Hong hoc') của các khoa phòng có từ 5 thiết bị hỏng trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{SO_TB_HONG ≥ 5}(_{KHOA_PHONG.MAKHOA, TENKHOA} γ _{COUNT(MATB) → SO_TB_HONG}(KHOA_PHONG ⋈ σ_{TRANGTHAI = 'Hong hoc'}(THIETBI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT KP.MAKHOA, KP.TENKHOA, COUNT(TB.MATB) AS SO_TB_HONG
FROM KHOA_PHONG KP INNER JOIN THIETBI TB ON KP.MAKHOA = TB.MAKHOA
WHERE TB.TRANGTHAI = N'Hong hoc'
GROUP BY KP.MAKHOA, KP.TENKHOA
HAVING COUNT(TB.MATB) >= 5;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc thiết bị có trạng thái hỏng hóc.
1. Bước 2: Kết nối với KHOA_PHONG theo MAKHOA.
1. Bước 3: Gom nhóm theo MAKHOA, TENKHOA và đếm số lượng.
1. Bước 4: Lọc SO_TB_HONG >= 5.

**Phân tích trường hợp biên (Edge Cases):**
Cảnh báo bảo trì trang thiết bị trọng điểm bệnh viện.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 30 [RA-D30] — ĐSQH Gom Nhóm: Tổng Số Tiết Giảng Dạy Của Giảng Viên Vượt Chuẩn
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `GIANGVIEN(MAGV, HOTEN, MAKHOA), LOPHOCPHAN(MALHP, MAGV, SOTIET, NAMHOC)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã giảng viên, họ tên của các giảng viên thuộc khoa 'Khoa hoc May tinh' có tổng số tiết giảng dạy trong năm học '2023-2024' vượt định mức 300 tiết.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIET > 300}(_{GIANGVIEN.MAGV, HOTEN} γ _{SUM(SOTIET) → TONG_TIET}(σ_{MAKHOA = 'KHMT'}(GIANGVIEN) ⋈ σ_{NAMHOC = '2023-2024'}(LOPHOCPHAN)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT GV.MAGV, GV.HOTEN, SUM(LHP.SOTIET) AS TONG_TIET
FROM GIANGVIEN GV INNER JOIN LOPHOCPHAN LHP ON GV.MAGV = LHP.MAGV
WHERE GV.MAKHOA = 'KHMT' AND LHP.NAMHOC = '2023-2024'
GROUP BY GV.MAGV, GV.HOTEN
HAVING SUM(LHP.SOTIET) > 300;
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc giảng viên khoa KHMT và lớp học phần năm 2023-2024.
1. Bước 2: Kết nối theo MAGV.
1. Bước 3: Gom nhóm MAGV, HOTEN và tính SUM(SOTIET).
1. Bước 4: Lọc TONG_TIET > 300.

**Phân tích trường hợp biên (Edge Cases):**
Chỉ tính số tiết thực dạy trong năm học được xét.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `grouping_attributes_and_gamma`: 0.4đ
- `aggregation_functions`: 0.4đ
- `having_filter_condition`: 0.2đ

---

## Bài 31 [RA-D31] — ĐSQH Cực Trị: Sinh Viên Điểm GPA Cao Nhất Khoa Công Nghệ Phần Mềm
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `SINHVIEN(MSSV, HOTEN, KHOA, DIEM_GPA)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã số sinh viên, họ tên và điểm GPA của các sinh viên đạt điểm GPA cao nhất trong khoa 'Cong nghe Phan mem' (bảo toàn tất cả sinh viên đồng hạng thủ khoa).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{KHOA = 'Cong nghe Phan mem'}(SINHVIEN)
NonMax = π_{SV1.MSSV, SV1.HOTEN, SV1.KHOA, SV1.DIEM_GPA}(σ_{SV1.DIEM_GPA < SV2.DIEM_GPA}(ρ_{SV1}(R_{sub}) × ρ_{SV2}(R_{sub})))
KQ = R_{sub} - NonMax
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT SV.MSSV, SV.HOTEN, SV.DIEM_GPA
FROM SINHVIEN SV
WHERE SV.KHOA = N'Cong nghe Phan mem'
  AND SV.DIEM_GPA = (SELECT MAX(DIEM_GPA) FROM SINHVIEN WHERE KHOA = N'Cong nghe Phan mem');
```

**Các bước suy luận tư duy:**
1. Bước 1 (Lọc tập con phân nhóm R_sub): Lọc trước toàn bộ sinh viên thuộc khoa 'Cong nghe Phan mem'.
1. Bước 2 (Tìm tập không phải lớn nhất NonMax): Tích Descartes ρ_{SV1}(R_sub) × ρ_{SV2}(R_sub) và chọn các cặp có SV1.DIEM_GPA < SV2.DIEM_GPA.
1. Bước 3 (Lấy hiệu trên chính R_sub): Lấy R_sub trừ đi NonMax. Kết quả chỉ chứa sinh viên khoa CNPM có GPA cao nhất và bảo toàn tất cả các sinh viên đồng hạng!

**Phân tích trường hợp biên (Edge Cases):**
Tuyệt đối không lấy toàn bảng SINHVIEN trừ NonMax vì sinh viên các khoa khác không xuất hiện trong NonMax sẽ bị sót lại trong kết quả sai lệch!

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---

## Bài 32 [RA-D32] — ĐSQH Cực Trị: Sản Phẩm Bán Chạy Nhất Danh Mục Điện Thoại
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `SANPHAM(MASP, TENSP, DANHMUC, SOLUONG_BAN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã sản phẩm, tên sản phẩm và số lượng bán của các sản phẩm có số lượng bán nhiều nhất trong danh mục 'Dien thoai' năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{DANHMUC = 'Dien thoai'}(SANPHAM)
NonMax = π_{SP1.MASP, SP1.TENSP, SP1.DANHMUC, SP1.SOLUONG_BAN}(σ_{SP1.SOLUONG_BAN < SP2.SOLUONG_BAN}(ρ_{SP1}(R_{sub}) × ρ_{SP2}(R_{sub})))
KQ = R_{sub} - NonMax
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT SP.MASP, SP.TENSP, SP.SOLUONG_BAN
FROM SANPHAM SP
WHERE SP.DANHMUC = N'Dien thoai'
  AND SP.SOLUONG_BAN = (SELECT MAX(SOLUONG_BAN) FROM SANPHAM WHERE DANHMUC = N'Dien thoai');
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc danh mục sản phẩm điện thoại: R_sub = σ_{DANHMUC = 'Dien thoai'}(SANPHAM).
1. Bước 2: Tìm tập sản phẩm có số lượng bán bị vượt qua: NonMax = π_{SP1}(σ_{SP1.SOLUONG_BAN < SP2.SOLUONG_BAN}(ρ_{SP1}(R_sub) × ρ_{SP2}(R_sub))).
1. Bước 3: Kết quả = R_sub - NonMax.

**Phân tích trường hợp biên (Edge Cases):**
Bảo toàn tất cả sản phẩm bán chạy nhất nếu có nhiều dòng máy cùng đạt số lượng bán kỷ lục.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---

## Bài 33 [RA-D33] — ĐSQH Cực Trị: Bác Sĩ Có Nhiều Ca Khám Bệnh Nhất Khoa Cấp Cứu
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `BACSI(MABS, HOTEN, KHOAPHONG, SOCA_KHAM)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã bác sĩ, họ tên và số ca khám của các bác sĩ thực hiện nhiều ca khám bệnh nhất tại khoa 'Cap cuu'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{KHOAPHONG = 'Cap cuu'}(BACSI)
NonMax = π_{BS1.MABS, BS1.HOTEN, BS1.KHOAPHONG, BS1.SOCA_KHAM}(σ_{BS1.SOCA_KHAM < BS2.SOCA_KHAM}(ρ_{BS1}(R_{sub}) × ρ_{BS2}(R_{sub})))
KQ = R_{sub} - NonMax
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT BS.MABS, BS.HOTEN, BS.SOCA_KHAM
FROM BACSI BS
WHERE BS.KHOAPHONG = N'Cap cuu'
  AND BS.SOCA_KHAM = (SELECT MAX(SOCA_KHAM) FROM BACSI WHERE KHOAPHONG = N'Cap cuu');
```

**Các bước suy luận tư duy:**
1. Bước 1: R_sub = σ_{KHOAPHONG = 'Cap cuu'}(BACSI).
1. Bước 2: NonMax = π_{BS1}(σ_{BS1.SOCA_KHAM < BS2.SOCA_KHAM}(ρ_{BS1}(R_sub) × ρ_{BS2}(R_sub))).
1. Bước 3: KQ = R_sub - NonMax.

**Phân tích trường hợp biên (Edge Cases):**
Phương pháp hiệu tập con đảm bảo không làm lọt bác sĩ khoa khác vào kết quả.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---

## Bài 34 [RA-D34] — ĐSQH Cực Trị: Chuyến Bay Có Giá Vé Thấp Nhất Chặng SGN - DAD
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `CHUYENBAY(MACB, HANG_BAY, CHANG_BAY, GIAVE)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã chuyến bay, hãng bay và giá vé của các chuyến bay có giá vé thấp nhất (MIN) trên chặng bay 'SGN-DAD'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{CHANG_BAY = 'SGN-DAD'}(CHUYENBAY)
NonMin = π_{CB1.MACB, CB1.HANG_BAY, CB1.CHANG_BAY, CB1.GIAVE}(σ_{CB1.GIAVE > CB2.GIAVE}(ρ_{CB1}(R_{sub}) × ρ_{CB2}(R_{sub})))
KQ = R_{sub} - NonMin
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT CB.MACB, CB.HANG_BAY, CB.GIAVE
FROM CHUYENBAY CB
WHERE CB.CHANG_BAY = 'SGN-DAD'
  AND CB.GIAVE = (SELECT MIN(GIAVE) FROM CHUYENBAY WHERE CHANG_BAY = 'SGN-DAD');
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc chuyến bay chặng SGN-DAD: R_sub = σ_{CHANG_BAY = 'SGN-DAD'}(CHUYENBAY).
1. Bước 2: Tìm các chuyến bay có giá cao hơn chuyến khác trong chặng: NonMin = π_{CB1}(σ_{CB1.GIAVE > CB2.GIAVE}(ρ_{CB1}(R_sub) × ρ_{CB2}(R_sub))).
1. Bước 3: Lấy R_sub trừ đi NonMin để thu được chuyến bay giá rẻ nhất.

**Phân tích trường hợp biên (Edge Cases):**
Đối với cực tiểu (MIN), điều kiện lọc cặp là CB1.GIAVE > CB2.GIAVE.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---

## Bài 35 [RA-D35] — ĐSQH Cực Trị: Căn Hộ Có Diện Tích Lớn Nhất Tòa Skyview
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `CANHO(MACAN, TOANHA, SOHIEUCAN, DIENTICH_M2)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã căn hộ, số hiệu căn hộ và diện tích của các căn hộ có diện tích lớn nhất (MAX) tại tòa nhà 'Skyview'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{TOANHA = 'Skyview'}(CANHO)
NonMax = π_{CH1.MACAN, CH1.TOANHA, CH1.SOHIEUCAN, CH1.DIENTICH_M2}(σ_{CH1.DIEMSO < CH2.DIEMSO}(ρ_{CH1}(R_{sub}) × ρ_{CH2}(R_{sub})))
KQ = R_{sub} - NonMax
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT CH.MACAN, CH.SOHIEUCAN, CH.DIENTICH_M2
FROM CANHO CH
WHERE CH.TOANHA = 'Skyview'
  AND CH.DIENTICH_M2 = (SELECT MAX(DIENTICH_M2) FROM CANHO WHERE TOANHA = 'Skyview');
```

**Các bước suy luận tư duy:**
1. Bước 1: R_sub = σ_{TOANHA = 'Skyview'}(CANHO).
1. Bước 2: NonMax = π_{CH1}(σ_{CH1.DIENTICH_M2 < CH2.DIENTICH_M2}(ρ_{CH1}(R_sub) × ρ_{CH2}(R_sub))).
1. Bước 3: KQ = R_sub - NonMax.

**Phân tích trường hợp biên (Edge Cases):**
Nếu có nhiều căn hộ penthouse cùng diện tích tối đa, phép trừ bảo toàn toàn bộ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---

## Bài 36 [RA-D36] — ĐSQH Cực Trị: Khách Hàng Có Chi Tiêu Cao Nhất Ngày Black Friday
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `HOADON_BF(MAHD, MAKH, HOTEN_KH, TONGTIEN, NGAYMUA)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã khách hàng, tên khách hàng và tổng tiền của khách hàng có hóa đơn mua sắm trị giá cao nhất trong đợt khuyến mãi '2024-11-29'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{NGAYMUA = '2024-11-29'}(HOADON_BF)
NonMax = π_{HD1.MAHD, HD1.MAKH, HD1.HOTEN_KH, HD1.TONGTIEN, HD1.NGAYMUA}(σ_{HD1.TONGTIEN < HD2.TONGTIEN}(ρ_{HD1}(R_{sub}) × ρ_{HD2}(R_{sub})))
KQ = R_{sub} - NonMax
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT HD.MAKH, HD.HOTEN_KH, HD.TONGTIEN
FROM HOADON_BF HD
WHERE HD.NGAYMUA = '2024-11-29'
  AND HD.TONGTIEN = (SELECT MAX(TONGTIEN) FROM HOADON_BF WHERE NGAYMUA = '2024-11-29');
```

**Các bước suy luận tư duy:**
1. Bước 1: Lọc hóa đơn phát sinh ngày Black Friday: R_sub.
1. Bước 2: Tìm các hóa đơn bị nhỏ hơn hóa đơn khác trong ngày: NonMax.
1. Bước 3: KQ = R_sub - NonMax.

**Phân tích trường hợp biên (Edge Cases):**
Khách hàng đồng hạng giải Nhất được hiển thị đầy đủ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---

## Bài 37 [RA-D37] — ĐSQH Cực Trị: Lô Vắc-Xin Nhập Nhiều Liều Nhất Của Moderna
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `LOVACXIN(MALO, TENVACXIN, NHASANXUAT, SOLIEU_NHAP)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã lô, tên vắc-xin và số liều nhập của các lô vắc-xin có số lượng liều nhập nhiều nhất của nhà sản xuất 'Moderna'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{NHASANXUAT = 'Moderna'}(LOVACXIN)
NonMax = π_{L1.MALO, L1.TENVACXIN, L1.NHASANXUAT, L1.SOLIEU_NHAP}(σ_{L1.SOLUONG < L2.SOLUONG}(ρ_{L1}(R_{sub}) × ρ_{L2}(R_{sub})))
KQ = R_{sub} - NonMax
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT LV.MALO, LV.TENVACXIN, LV.SOLIEU_NHAP
FROM LOVACXIN LV
WHERE LV.NHASANXUAT = 'Moderna'
  AND LV.SOLIEU_NHAP = (SELECT MAX(SOLIEU_NHAP) FROM LOVACXIN WHERE NHASANXUAT = 'Moderna');
```

**Các bước suy luận tư duy:**
1. Bước 1: R_sub = σ_{NHASANXUAT = 'Moderna'}(LOVACXIN).
1. Bước 2: NonMax = π_{L1}(σ_{L1.SOLIEU_NHAP < L2.SOLIEU_NHAP}(ρ_{L1}(R_sub) × ρ_{L2}(R_sub))).
1. Bước 3: KQ = R_sub - NonMax.

**Phân tích trường hợp biên (Edge Cases):**
Lô của nhà sản xuất khác như Pfizer, AstraZeneca không bị ảnh hưởng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---

## Bài 38 [RA-D38] — ĐSQH Cực Trị: Đề Tài NCKH Có Kinh Phí Lớn Nhất Năm 2024
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DETAI_NCKH(MADT, TENDT, NAM_TRIENKHAI, KINHPHI_VND)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã đề tài, tên đề tài và kinh phí của các đề tài nghiên cứu khoa học có kinh phí được phê duyệt lớn nhất trong năm '2024'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{NAM_TRIENKHAI = 2024}(DETAI_NCKH)
NonMax = π_{DT1.MADT, DT1.TENDT, DT1.NAM_TRIENKHAI, DT1.KINHPHI_VND}(σ_{DT1.KINHPHI_VND < DT2.KINHPHI_VND}(ρ_{DT1}(R_{sub}) × ρ_{DT2}(R_{sub})))
KQ = R_{sub} - NonMax
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT DT.MADT, DT.TENDT, DT.KINHPHI_VND
FROM DETAI_NCKH DT
WHERE DT.NAM_TRIENKHAI = 2024
  AND DT.KINHPHI_VND = (SELECT MAX(KINHPHI_VND) FROM DETAI_NCKH WHERE NAM_TRIENKHAI = 2024);
```

**Các bước suy luận tư duy:**
1. Bước 1: R_sub = σ_{NAM_TRIENKHAI = 2024}(DETAI_NCKH).
1. Bước 2: NonMax = π_{DT1}(σ_{DT1.KINHPHI_VND < DT2.KINHPHI_VND}(ρ_{DT1}(R_sub) × ρ_{DT2}(R_sub))).
1. Bước 3: KQ = R_sub - NonMax.

**Phân tích trường hợp biên (Edge Cases):**
Tránh lấy toàn bảng trừ NonMax làm sót các đề tài của các năm khác.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---

## Bài 39 [RA-D39] — ĐSQH Cực Trị: Tài Xế Công Nghệ Điểm Sao Cao Nhất Đội Xe 01
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `TAIXE(MATX, HOTEN, MADOI, DIEM_SAO_TB)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã tài xế, họ tên và điểm sao trung bình của các tài xế đạt điểm đánh giá sao cao nhất thuộc đội xe có mã 'DOI_01'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{MADOI = 'DOI_01'}(TAIXE)
NonMax = π_{TX1.MATX, TX1.HOTEN, TX1.MADOI, TX1.DIEM_SAO_TB}(σ_{TX1.DIEM_SAO_TB < TX2.DIEM_SAO_TB}(ρ_{TX1}(R_{sub}) × ρ_{TX2}(R_{sub})))
KQ = R_{sub} - NonMax
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT TX.MATX, TX.HOTEN, TX.DIEM_SAO_TB
FROM TAIXE TX
WHERE TX.MADOI = 'DOI_01'
  AND TX.DIEM_SAO_TB = (SELECT MAX(DIEM_SAO_TB) FROM TAIXE WHERE MADOI = 'DOI_01');
```

**Các bước suy luận tư duy:**
1. Bước 1: R_sub = σ_{MADOI = 'DOI_01'}(TAIXE).
1. Bước 2: NonMax = π_{TX1}(σ_{TX1.DIEM_SAO_TB < TX2.DIEM_SAO_TB}(ρ_{TX1}(R_sub) × ρ_{TX2}(R_sub))).
1. Bước 3: KQ = R_sub - NonMax.

**Phân tích trường hợp biên (Edge Cases):**
Tất cả tài xế đạt cùng điểm số tối đa 5.0 sao đều được giữ lại trong kết quả.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---

## Bài 40 [RA-D40] — ĐSQH Cực Trị: Trạm Đo Ghi Nhận Lượng Mưa Cao Nhất Đợt Bão
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `QUANTRAC_BAO(MATRAM, TENTRAM, VUNG_BAO, LUONGMUA_MM)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã trạm, tên trạm và lượng mưa của các trạm ghi nhận lượng mưa cao nhất trong vùng tâm bão 'Bao_So_3'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{VUNG_BAO = 'Bao_So_3'}(QUANTRAC_BAO)
NonMax = π_{T1.MATRAM, T1.TENTRAM, T1.VUNG_BAO, T1.LUONGMUA_MM}(σ_{T1.LUONGMUA_MM < T2.LUONGMUA_MM}(ρ_{T1}(R_{sub}) × ρ_{T2}(R_{sub})))
KQ = R_{sub} - NonMax
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT T.MATRAM, T.TENTRAM, T.LUONGMUA_MM
FROM QUANTRAC_BAO T
WHERE T.VUNG_BAO = 'Bao_So_3'
  AND T.LUONGMUA_MM = (SELECT MAX(LUONGMUA_MM) FROM QUANTRAC_BAO WHERE VUNG_BAO = 'Bao_So_3');
```

**Các bước suy luận tư duy:**
1. Bước 1: R_sub = σ_{VUNG_BAO = 'Bao_So_3'}(QUANTRAC_BAO).
1. Bước 2: NonMax = π_{T1}(σ_{T1.LUONGMUA_MM < T2.LUONGMUA_MM}(ρ_{T1}(R_sub) × ρ_{T2}(R_sub))).
1. Bước 3: KQ = R_sub - NonMax.

**Phân tích trường hợp biên (Edge Cases):**
Dữ liệu khí tượng thủy văn cần tính toán cực trị chính xác cho công tác cảnh báo thiên tai.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---

## Bài 41 [RA-D41] — ĐSQH Cực Trị: Cuốn Sách Được Mượn Nhiều Nhất Thể Loại CSDL
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `THONGKE_SACH(MASACH, TENSACH, THELOAI, LUOT_MUON)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã sách, tên sách và số lượt mượn của các cuốn sách có lượt mượn nhiều nhất trong thể loại 'Co so du lieu'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{THELOAI = 'Co so du lieu'}(THONGKE_SACH)
NonMax = π_{S1.MASACH, S1.TENSACH, S1.THELOAI, S1.LUOT_MUON}(σ_{S1.LUOT_MUON < S2.LUOT_MUON}(ρ_{S1}(R_{sub}) × ρ_{S2}(R_{sub})))
KQ = R_{sub} - NonMax
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT S.MASACH, S.TENSACH, S.LUOT_MUON
FROM THONGKE_SACH S
WHERE S.THELOAI = N'Co so du lieu'
  AND S.LUOT_MUON = (SELECT MAX(LUOT_MUON) FROM THONGKE_SACH WHERE THELOAI = N'Co so du lieu');
```

**Các bước suy luận tư duy:**
1. Bước 1: R_sub = σ_{THELOAI = 'Co so du lieu'}(THONGKE_SACH).
1. Bước 2: NonMax = π_{S1}(σ_{S1.LUOT_MUON < S2.LUOT_MUON}(ρ_{S1}(R_sub) × ρ_{S2}(R_sub))).
1. Bước 3: KQ = R_sub - NonMax.

**Phân tích trường hợp biên (Edge Cases):**
Bảo toàn cả những cuốn sách có cùng lượt mượn cao nhất.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---

## Bài 42 [RA-D42] — ĐSQH Cực Trị: Nhà Thuốc Có Doanh Thu Cao Nhất Chuỗi Quận 1
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `NHATHUOC(MANT, TENNT, QUAN, TONG_DOANHTHU)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã nhà thuốc, tên nhà thuốc và doanh thu của nhà thuốc đạt doanh thu cao nhất thuộc khu vực 'Quan 1'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{QUAN = 'Quan 1'}(NHATHUOC)
NonMax = π_{NT1.MANT, NT1.TENNT, NT1.QUAN, NT1.TONG_DOANHTHU}(σ_{NT1.TONG_DOANHTHU < NT2.TONG_DOANHTHU}(ρ_{NT1}(R_{sub}) × ρ_{NT2}(R_{sub})))
KQ = R_{sub} - NonMax
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT NT.MANT, NT.TENNT, NT.TONG_DOANHTHU
FROM NHATHUOC NT
WHERE NT.QUAN = 'Quan 1'
  AND NT.TONG_DOANHTHU = (SELECT MAX(TONG_DOANHTHU) FROM NHATHUOC WHERE QUAN = 'Quan 1');
```

**Các bước suy luận tư duy:**
1. Bước 1: R_sub = σ_{QUAN = 'Quan 1'}(NHATHUOC).
1. Bước 2: NonMax = π_{NT1}(σ_{NT1.TONG_DOANHTHU < NT2.TONG_DOANHTHU}(ρ_{NT1}(R_sub) × ρ_{NT2}(R_sub))).
1. Bước 3: KQ = R_sub - NonMax.

**Phân tích trường hợp biên (Edge Cases):**
Doanh thu lớn nhất trong phạm vi phân nhóm Quận 1.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---

## Bài 43 [RA-D43] — ĐSQH Cực Trị: Phòng Khách Sạn Đơn Giá Thấp Nhất Hạng Executive Suite
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `PHONG_KS(MAPHONG, LOAIPHONG, DONGIA_DEM)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã phòng và đơn giá đêm của các phòng có giá thấp nhất (MIN) thuộc hạng phòng 'Executive Suite'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{LOAIPHONG = 'Executive Suite'}(PHONG_KS)
NonMin = π_{P1.MAPHONG, P1.LOAIPHONG, P1.DONGIA_DEM}(σ_{P1.DONGIA_DEM > P2.DONGIA_DEM}(ρ_{P1}(R_{sub}) × ρ_{P2}(R_{sub})))
KQ = R_{sub} - NonMin
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT P.MAPHONG, P.DONGIA_DEM
FROM PHONG_KS P
WHERE P.LOAIPHONG = 'Executive Suite'
  AND P.DONGIA_DEM = (SELECT MIN(DONGIA_DEM) FROM PHONG_KS WHERE LOAIPHONG = 'Executive Suite');
```

**Các bước suy luận tư duy:**
1. Bước 1: R_sub = σ_{LOAIPHONG = 'Executive Suite'}(PHONG_KS).
1. Bước 2: NonMin = π_{P1}(σ_{P1.DONGIA_DEM > P2.DONGIA_DEM}(ρ_{P1}(R_sub) × ρ_{P2}(R_sub))).
1. Bước 3: KQ = R_sub - NonMin.

**Phân tích trường hợp biên (Edge Cases):**
Cực tiểu sử dụng vị từ so sánh lớn hơn để tìm NonMin.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---

## Bài 44 [RA-D44] — ĐSQH Cực Trị: Nhân Viên Có Số Năm Công Tác Lâu Nhất Phòng Kỹ Thuật
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `NHANVIEN(MANV, HOTEN, PHONGBAN, THAM_NIEN_NAM)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã nhân viên, họ tên và số năm thâm niên của nhân viên có thời gian công tác lâu năm nhất tại phòng 'Ky thuat ha tang'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{PHONGBAN = 'Ky thuat ha tang'}(NHANVIEN)
NonMax = π_{NV1.MANV, NV1.HOTEN, NV1.PHONGBAN, NV1.THAM_NIEN_NAM}(σ_{NV1.THAM_NIEN_NAM < NV2.THAM_NIEN_NAM}(ρ_{NV1}(R_{sub}) × ρ_{NV2}(R_{sub})))
KQ = R_{sub} - NonMax
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT NV.MANV, NV.HOTEN, NV.THAM_NIEN_NAM
FROM NHANVIEN NV
WHERE NV.PHONGBAN = N'Ky thuat ha tang'
  AND NV.THAM_NIEN_NAM = (SELECT MAX(THAM_NIEN_NAM) FROM NHANVIEN WHERE PHONGBAN = N'Ky thuat ha tang');
```

**Các bước suy luận tư duy:**
1. Bước 1: R_sub = σ_{PHONGBAN = 'Ky thuat ha tang'}(NHANVIEN).
1. Bước 2: NonMax = π_{NV1}(σ_{NV1.THAM_NIEN_NAM < NV2.THAM_NIEN_NAM}(ρ_{NV1}(R_sub) × ρ_{NV2}(R_sub))).
1. Bước 3: KQ = R_sub - NonMax.

**Phân tích trường hợp biên (Edge Cases):**
Nhân viên phòng ban khác không bao giờ bị trừ hoặc xuất hiện ở kết quả.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---

## Bài 45 [RA-D45] — ĐSQH Cực Trị: Doanh Nghiệp Thuê Diện Tích Lớn Nhất Phân Khu CNC (Sửa P0-04)
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOANHNGHIEP_KCN(MADN, TENDN, MAPK, DIENTICH_THUE_M2)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm mã doanh nghiệp, tên doanh nghiệp và diện tích thuê của các doanh nghiệp thuê diện tích đất xưởng lớn nhất (MAX) tại phân khu 'PK_CNC' (Khu công nghệ cao).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
R_{sub} = σ_{MAPK = 'PK_CNC'}(DOANHNGHIEP_KCN)
NonMax = π_{DN1.MADN, DN1.TENDN, DN1.MAPK, DN1.DIENTICH_THUE_M2}(σ_{DN1.DIENTICH_THUE_M2 < DN2.DIENTICH_THUE_M2}(ρ_{DN1}(R_{sub}) × ρ_{DN2}(R_{sub})))
KQ = R_{sub} - NonMax
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT DN.MADN, DN.TENDN, DN.DIENTICH_THUE_M2
FROM DOANHNGHIEP_KCN DN
WHERE DN.MAPK = 'PK_CNC'
  AND DN.DIENTICH_THUE_M2 = (SELECT MAX(DIENTICH_THUE_M2) FROM DOANHNGHIEP_KCN WHERE MAPK = 'PK_CNC');
```

**Các bước suy luận tư duy:**
1. Bước 1 (Lọc tập con phân nhóm R_sub): R_sub = σ_{MAPK = 'PK_CNC'}(DOANHNGHIEP_KCN). Đây là bước quyết định để cô lập không gian tìm kiếm cực trị trong đúng phân khu 'PK_CNC'.
1. Bước 2 (Tìm các doanh nghiệp bị vượt diện tích trong phân khu): NonMax = π_{DN1.MADN, DN1.TENDN, DN1.MAPK, DN1.DIENTICH_THUE_M2}(σ_{DN1.DIENTICH_THUE_M2 < DN2.DIENTICH_THUE_M2}(ρ_{DN1}(R_sub) × ρ_{DN2}(R_sub))).
1. Bước 3 (Hiệu tập hợp trên chính R_sub): KQ = R_sub - NonMax. Kết quả trả về chính xác 100% doanh nghiệp thuê nhiều đất nhất phân khu PK_CNC, đồng thời bảo toàn mọi đối tượng đồng hạng (tie-breaking).

**Phân tích trường hợp biên (Edge Cases):**
ĐÃ SỬA LỖI P0-04: Tuyệt đối không lấy toàn bảng DOANHNGHIEP_KCN trừ NonMax, vì các doanh nghiệp ở các phân khu khác (như PK_DETMAY, PK_HOACHAT) không nằm trong NonMax nên nếu trừ từ toàn bảng sẽ bị rò rỉ vào kết quả sai lệch! Phép trừ phải thực hiện trên chính quan hệ tập con R_sub.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `subgroup_isolation`: 0.5đ
- `cartesian_product_and_inequality`: 0.5đ
- `set_difference_and_tie_breaking`: 0.5đ

---
