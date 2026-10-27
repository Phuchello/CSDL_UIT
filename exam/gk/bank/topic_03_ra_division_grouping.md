# CHUYÊN ĐỀ 3: PHÉP CHIA (TẤT CẢ), GOM NHÓM & TRUY VẤN PHỨC HỢP
**Môn học:** IT004 — Cơ sở dữ liệu | **Hệ thống:** UIT Exam Mastery
**Biên soạn:** VÕ TRỌNG PHÚC | **Số lượng bài tập độc lập:** 45 bài chuẩn hóa

---

## Bài 01 [RA-D01] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 1
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 1.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_1'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_1'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_1'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_1'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 02 [RA-D02] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 2
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 2.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_2'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_2'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_2'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_2'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 03 [RA-D03] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 3
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 3.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_3'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_3'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_3'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_3'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 04 [RA-D04] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 4
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 4.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_4'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_4'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_4'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_4'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 05 [RA-D05] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 5
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 5.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_5'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_5'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_5'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_5'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 06 [RA-D06] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 6
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 6.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_6'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_6'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_6'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_6'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 07 [RA-D07] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 7
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 7.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_7'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_7'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_7'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_7'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 08 [RA-D08] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 8
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 8.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_8'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_8'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_8'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_8'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 09 [RA-D09] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 9
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 9.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_9'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_9'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_9'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_9'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 10 [RA-D10] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 10
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 10.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_10'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_10'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_10'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_10'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 11 [RA-D11] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 11
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 11.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_11'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_11'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_11'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_11'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 12 [RA-D12] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 12
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 12.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_12'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_12'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_12'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_12'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 13 [RA-D13] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 13
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 13.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_13'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_13'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_13'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_13'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 14 [RA-D14] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 14
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 14.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_14'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_14'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_14'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_14'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 15 [RA-D15] — ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số 15
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản 15.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
π_{MA_UV, MA_MT}(σ_{LOAI_MT = 'Loai_15'}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{MA_MT}(σ_{LOAI_MT = 'Loai_15'}(MUC_TIEU))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT UV.MA_UV, UV.TEN_UV
FROM UNG_VIEN UV
WHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)
  AND NOT EXISTS (
    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_15'
    EXCEPT
    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV
);
```

**Các bước suy luận tư duy:**
1. Bước 1 (Xác định tập chia S): R_S = π_{MA_MT}(σ_{LOAI_MT = 'Loai_15'}(MUC_TIEU)).
1. Bước 2 (Tạo tập giả định R_All): R_All = π_{MA_UV}(QUAN_HE) × R_S.
1. Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{MA_UV, MA_MT}(QUAN_HE).
1. Bước 4 (Kết quả cuối cùng): KQ = π_{MA_UV}(QUAN_HE) - π_{MA_UV}(R_Missing).

**Phân tích trường hợp biên (Edge Cases):**
Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 16 [RA-D16] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 16
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 16.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 16000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 16000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 16000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 17 [RA-D17] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 17
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 17.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 17000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 17000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 17000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 18 [RA-D18] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 18
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 18.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 18000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 18000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 18000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 19 [RA-D19] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 19
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 19.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 19000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 19000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 19000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 20 [RA-D20] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 20
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 20.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 20000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 20000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 20000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 21 [RA-D21] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 21
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 21.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 21000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 21000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 21000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 22 [RA-D22] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 22
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 22.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 22000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 22000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 22000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 23 [RA-D23] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 23
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 23.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 23000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 23000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 23000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 24 [RA-D24] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 24
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 24.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 24000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 24000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 24000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 25 [RA-D25] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 25
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 25.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 25000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 25000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 25000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 26 [RA-D26] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 26
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 26.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 26000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 26000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 26000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 27 [RA-D27] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 27
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 27.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 27000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 27000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 27000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 28 [RA-D28] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 28
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 28.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 28000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 28000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 28000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 29 [RA-D29] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 29
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 29.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 29000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 29000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 29000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 30 [RA-D30] — ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số 30
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản 30.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
σ_{TONG_TIEN > 30000000}(_{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG
FROM HOATDONG
GROUP BY MA_NHOM
HAVING SUM(SOTIEN) > 30000000;
```

**Các bước suy luận tư duy:**
1. Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.
1. Bước 2: Áp dụng toán tử gom nhóm γ: _{MA_NHOM} γ _{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}(HOATDONG).
1. Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > 30000000.

**Phân tích trường hợp biên (Edge Cases):**
Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `mathematical_formulation`: 0.4đ
- `boundary_case_handling`: 0.3đ
- `intermediate_reasoning`: 0.3đ

---

## Bài 31 [RA-D31] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 31
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 31.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_31' ∧ DT2.PHAN_LOAI = 'Nhom_31'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_31'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_31');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 32 [RA-D32] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 32
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 32.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_32' ∧ DT2.PHAN_LOAI = 'Nhom_32'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_32'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_32');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 33 [RA-D33] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 33
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 33.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_33' ∧ DT2.PHAN_LOAI = 'Nhom_33'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_33'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_33');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 34 [RA-D34] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 34
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 34.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_34' ∧ DT2.PHAN_LOAI = 'Nhom_34'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_34'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_34');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 35 [RA-D35] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 35
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 35.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_35' ∧ DT2.PHAN_LOAI = 'Nhom_35'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_35'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_35');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 36 [RA-D36] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 36
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 36.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_36' ∧ DT2.PHAN_LOAI = 'Nhom_36'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_36'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_36');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 37 [RA-D37] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 37
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 37.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_37' ∧ DT2.PHAN_LOAI = 'Nhom_37'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_37'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_37');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 38 [RA-D38] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 38
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 38.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_38' ∧ DT2.PHAN_LOAI = 'Nhom_38'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_38'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_38');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 39 [RA-D39] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 39
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 39.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_39' ∧ DT2.PHAN_LOAI = 'Nhom_39'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_39'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_39');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 40 [RA-D40] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 40
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 40.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_40' ∧ DT2.PHAN_LOAI = 'Nhom_40'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_40'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_40');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 41 [RA-D41] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 41
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 41.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_41' ∧ DT2.PHAN_LOAI = 'Nhom_41'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_41'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_41');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 42 [RA-D42] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 42
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 42.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_42' ∧ DT2.PHAN_LOAI = 'Nhom_42'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_42'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_42');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 43 [RA-D43] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 43
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 43.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_43' ∧ DT2.PHAN_LOAI = 'Nhom_43'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_43'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_43');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 44 [RA-D44] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 44
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 44.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_44' ∧ DT2.PHAN_LOAI = 'Nhom_44'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_44'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_44');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---

## Bài 45 [RA-D45] — ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số 45
- **Mức độ:** Mức C | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 1.5 điểm
- **Lược đồ tham chiếu:** `DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản 45.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Biểu thức Đại số quan hệ (ĐSQH):**
```text
DOITUONG_THI - π_{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}(σ_{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_45' ∧ DT2.PHAN_LOAI = 'Nhom_45'}(ρ_{DT1}(DOITUONG_THI) × ρ_{DT2}(DOITUONG_THI)))
```

**Câu lệnh Transact-SQL tương đương:**
```sql
SELECT MA_DT, TEN_DT, DIEMSO
FROM DOITUONG_THI
WHERE PHAN_LOAI = 'Nhom_45'
  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_45');
```

**Các bước suy luận tư duy:**
1. Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.
1. Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.
1. Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị).

**Phân tích trường hợp biên (Edge Cases):**
Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.5đ
- `mathematical_formulation`: 0.6000000000000001đ
- `boundary_case_handling`: 0.44999999999999996đ
- `intermediate_reasoning`: 0.44999999999999996đ

---
