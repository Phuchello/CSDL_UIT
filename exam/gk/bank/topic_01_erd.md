# CHUYÊN ĐỀ 1: MÔ HÌNH THỰC THỂ MỐI KẾT HỢP (ERD) & ÁNH XẠ QUAN HỆ
**Môn học:** IT004 — Cơ sở dữ liệu | **Hệ thống:** UIT Exam Mastery
**Biên soạn:** VÕ TRỌNG PHÚC | **Số lượng bài tập:** 29 bài

---

## Bài 01 [M01-Q1] — Thiết Kế ERD & Ánh Xạ CSDL Quản Lý Tiêm Chủng Vắc-Xin
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `ERD: NHACUNGCAP, LOVACXIN, DIEMTIEM, NHANVIEN, PHIEUXUAT`

### 1. Đề Bài
Thiết kế mô hình Thực thể – Mối kết hợp (ERD) và chuyển sang Lược đồ quan hệ cho Hệ thống Quản lý Tiếp nhận, Phân phối vắc-xin và Điều động nhân sự tiêm chủng.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- {'name': 'NHACUNGCAP', 'pk': 'MANCC', 'attributes': ['MANCC', 'TENNCC', 'QUOCGIA', 'SDT'], 'description': 'Nhà cung ứng nguồn vắc-xin.'}
- {'name': 'LOVACXIN', 'pk': 'MALO', 'attributes': ['MALO', 'TENLO', 'TENVACXIN', 'NGAYSX', 'HSD', 'SOLIEU', 'DONGIA'], 'description': 'Lô vắc-xin nhập kho.'}
- {'name': 'DIEMTIEM', 'pk': 'MADT', 'attributes': ['MADT', 'TENDT', 'DIACHI', 'QUAN', 'SUCCHUA'], 'description': 'Điểm tiêm chủng lưu động hoặc cố định.'}
- {'name': 'NHANVIEN', 'pk': 'MANV', 'attributes': ['MANV', 'HOTEN', 'CHUYENMON', 'SDT'], 'description': 'Nhân viên y tế (bác sĩ, điều dưỡng) phục vụ tiêm chủng.'}
- {'name': 'PHIEUXUAT', 'pk': 'MAPX', 'attributes': ['MAPX', 'NGAYXUAT', 'TRANGTHAI'], 'description': 'Phiếu xuất điều phối vắc-xin đến các điểm tiêm.'}
**Lược đồ quan hệ chuyển đổi:**
- NHACUNGCAP (MANCC, TENNCC, QUOCGIA, SDT) - PK: MANCC
- LOVACXIN (MALO, TENLO, TENVACXIN, NGAYSX, HSD, SOLIEU, DONGIA, MANCC) - PK: MALO, FK: MANCC -> NHACUNGCAP(MANCC)
- DIEMTIEM (MADT, TENDT, DIACHI, QUAN, SUCCHUA) - PK: MADT
- NHANVIEN (MANV, HOTEN, CHUYENMON, SDT, MADT) - PK: MANV, FK: MADT -> DIEMTIEM(MADT)
- PHIEUXUAT (MAPX, NGAYXUAT, TRANGTHAI, MADT) - PK: MAPX, FK: MADT -> DIEMTIEM(MADT)
- CTPX (MAPX, MALO, SOLIEUXUAT) - PK: (MAPX, MALO), FK: MAPX -> PHIEUXUAT(MAPX), MALO -> LOVACXIN(MALO)

**Các bước suy luận tư duy:**
1. Bước 1: Xác định 5 tập thực thể, thuộc tính và khóa chính.
1. Bước 2: Phân tích 4 mối kết hợp và bản số min-max hai phía (3 quan hệ 1:N và 1 quan hệ M:N).
1. Bước 3: Ánh xạ quan hệ 1:N bằng cách đưa khóa ngoại vào bảng phía N.
1. Bước 4: Ánh xạ quan hệ M:N CHI_TIET_XUAT thành bảng quan hệ trung gian CTPX gồm 2 khóa ngoại làm khóa chính phức hợp và thuộc tính SOLIEUXUAT.

**Barem chấm điểm đề xuất:**
- `entities_and_keys`: 0.50đ
- `relationships_and_cardinality`: 1.00đ (mỗi mối kết hợp 0.25đ)
- `relational_mapping_pk_fk`: 1.00đ

---

## Bài 02 [M02-Q1] — Thiết Kế ERD & Ánh Xạ CSDL Quản Lý PCCC Chung Cư
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `ERD: TOANHA, TANG, CANHO, THIETBI_PCCC, DOT_KIEMTRA, CT_KIEMTRA`

### 1. Đề Bài
Thiết kế mô hình Thực thể – Mối kết hợp (ERD) và chuyển sang Lược đồ quan hệ cho Hệ thống Quản lý An toàn Phòng cháy Chữa cháy (PCCC) Chung Cư Cao Tầng gồm TOANHA, TANG, CANHO, THIETBI_PCCC, DOT_KIEMTRA và CT_KIEMTRA.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- {'name': 'TOANHA', 'pk': 'MATN', 'attributes': ['MATN', 'TENTN', 'SOTANG', 'DIACHI'], 'description': 'Tòa nhà trong khu chung cư.'}
- {'name': 'TANG', 'pk': 'MATANG', 'attributes': ['MATANG', 'MATN', 'STTTANG', 'DIENTICH'], 'description': 'Tầng thuộc tòa nhà.'}
- {'name': 'CANHO', 'pk': 'MACANHO', 'attributes': ['MACANHO', 'MATANG', 'SOCANHO', 'DIENTICH', 'SOPHONGNGU', 'TRANGTHAI'], 'description': 'Căn hộ trên tầng.'}
- {'name': 'THIETBI_PCCC', 'pk': 'MATB', 'attributes': ['MATB', 'MATANG', 'TENTB', 'LOAITB', 'VITRI_LAPDAT', 'NGAYLAP', 'HANSUDUNG'], 'description': 'Thiết bị PCCC được lắp đặt trên tầng.'}
- {'name': 'DOT_KIEMTRA', 'pk': 'MADOT', 'attributes': ['MADOT', 'NGAYKT', 'NGUOIKT', 'KETLUAN_CHUNG'], 'description': 'Đợt kiểm tra an toàn PCCC.'}
**Lược đồ quan hệ chuyển đổi:**
- {'table': 'TOANHA', 'pk': ['MATN'], 'fk': []}
- {'table': 'TANG', 'pk': ['MATANG'], 'fk': [{'column': 'MATN', 'ref_table': 'TOANHA', 'ref_column': 'MATN'}]}
- {'table': 'CANHO', 'pk': ['MACANHO'], 'fk': [{'column': 'MATANG', 'ref_table': 'TANG', 'ref_column': 'MATANG'}]}
- {'table': 'THIETBI_PCCC', 'pk': ['MATB'], 'fk': [{'column': 'MATANG', 'ref_table': 'TANG', 'ref_column': 'MATANG'}]}
- {'table': 'DOT_KIEMTRA', 'pk': ['MADOT'], 'fk': []}
- {'table': 'CT_KIEMTRA', 'pk': ['MADOT', 'MATB'], 'fk': [{'column': 'MADOT', 'ref_table': 'DOT_KIEMTRA', 'ref_column': 'MADOT'}, {'column': 'MATB', 'ref_table': 'THIETBI_PCCC', 'ref_column': 'MATB'}]}

**Barem chấm điểm đề xuất:**
- `syntax`: 0.50đ
- `logic`: 1.00đ
- `intermediate_steps`: 1.00đ

---

## Bài 03 [ERD-001] — Thiết kế ERD & Ánh xạ Schema: Quản lý Cung ứng & Tiêm chủng Vắc-xin
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `TTYT, LOVACXIN, NHACC, DIEMTIEM, NHANVIEN, PHANPHOI`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Cung ứng & Tiêm chủng Vắc-xin', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Cung ứng & Tiêm chủng Vắc-xin
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.50đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 1.00đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 04 [ERD-004] — Thiết kế ERD & Ánh xạ Schema: Quản lý Trạm Xăng Dầu & Bán Lẻ Nhiên Liệu
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `DOANH_NGHIEP, LOAI_XANG, CUA_HANG, PHIEU_NHAP`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Trạm Xăng Dầu & Bán Lẻ Nhiên Liệu', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Trạm Xăng Dầu & Bán Lẻ Nhiên Liệu
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.50đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 1.00đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 05 [ERD-005] — Thiết kế ERD & Ánh xạ Schema: Quản lý Căn Hộ Chung Cư Cho Thuê
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `TOA_NHA, CAN_HO, KHACH_THUE, HOP_DONG, DICH_VU`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Căn Hộ Chung Cư Cho Thuê', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Căn Hộ Chung Cư Cho Thuê
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.20đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 0.80đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 06 [ERD-006] — Thiết kế ERD & Ánh xạ Schema: Quản lý Bệnh Viện & Phòng Khám Đa Khoa
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `KHOA, BAC_SI, BENH_NHAN, PHIEU_KHAM, DON_THUOC`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Bệnh Viện & Phòng Khám Đa Khoa', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Bệnh Viện & Phòng Khám Đa Khoa
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.50đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 1.00đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 07 [ERD-007] — Thiết kế ERD & Ánh xạ Schema: Quản lý Thư Viện Số UIT & Mượn Trả Sách
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `DAU_SACH, CUON_SACH, DOC_GIA, PHIEU_MUON, VI_PHAM`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Thư Viện Số UIT & Mượn Trả Sách', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Thư Viện Số UIT & Mượn Trả Sách
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.20đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 0.80đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 08 [ERD-008] — Thiết kế ERD & Ánh xạ Schema: Quản lý Sàn Thương Mại Điện Tử & Đơn Hàng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `NGUOI_BAN, SAN_PHAM, NGUOI_MUA, DON_HANG, VAN_CHUYEN`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Sàn Thương Mại Điện Tử & Đơn Hàng', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Sàn Thương Mại Điện Tử & Đơn Hàng
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.50đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 1.00đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 09 [ERD-009] — Thiết kế ERD & Ánh xạ Schema: Quản lý Giải Đấu Thể Thao Điện Tử (Esports)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `DOI_THI, TUYEN_THU, GIAI_DAU, TRAN_DAU, KET_QUA`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Giải Đấu Thể Thao Điện Tử (Esports)', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Giải Đấu Thể Thao Điện Tử (Esports)
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.20đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 0.80đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 10 [ERD-010] — Thiết kế ERD & Ánh xạ Schema: Quản lý Gara Sửa Chữa & Bảo Dưỡng Ô Tô
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `XE, KHACH_HANG, THO_SUA, PHIEU_SUACHUA, PHU_TUNG`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Gara Sửa Chữa & Bảo Dưỡng Ô Tô', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Gara Sửa Chữa & Bảo Dưỡng Ô Tô
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.50đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 1.00đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 11 [ERD-011] — Thiết kế ERD & Ánh xạ Schema: Quản lý Chuỗi Cà Phê Nhượng Quyền
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `CUA_HANG, NHAN_VIEN, THUC_UONG, NGUYEN_LIEU, HOA_DON`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Chuỗi Cà Phê Nhượng Quyền', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Chuỗi Cà Phê Nhượng Quyền
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.20đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 0.80đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 12 [ERD-012] — Thiết kế ERD & Ánh xạ Schema: Quản lý Rạp Chiếu Phim & Đặt Vé Trực Tuyến
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `PHIM, RAP, PHONG_CHIEU, SUAT_CHIEU, VE_XEM`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Rạp Chiếu Phim & Đặt Vé Trực Tuyến', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Rạp Chiếu Phim & Đặt Vé Trực Tuyến
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.50đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 1.00đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 13 [ERD-013] — Thiết kế ERD & Ánh xạ Schema: Quản lý Tuyến Xe Buýt & Metro Đô Thị
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `TUYEN_XE, TRAM_DUNG, XE_BUYT, TAI_XE, VE_XE`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Tuyến Xe Buýt & Metro Đô Thị', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Tuyến Xe Buýt & Metro Đô Thị
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.20đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 0.80đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 14 [ERD-014] — Thiết kế ERD & Ánh xạ Schema: Quản lý Đề Tài Nghiên Cứu Khoa Học Sinh Viên
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `GIANG_VIEN, SINH_VIEN, DE_TAI, HOI_DONG, BAI_BAO`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Đề Tài Nghiên Cứu Khoa Học Sinh Viên', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Đề Tài Nghiên Cứu Khoa Học Sinh Viên
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.50đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 1.00đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 15 [ERD-015] — Thiết kế ERD & Ánh xạ Schema: Quản lý Trại Cứu Hộ Động Vật Hoang Dã
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `KHU_VUC, LOAI_DONGVAT, DONG_VAT, NHANVIEN_CS, LICH_KHAM`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Trại Cứu Hộ Động Vật Hoang Dã', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Trại Cứu Hộ Động Vật Hoang Dã
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.20đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 0.80đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 16 [ERD-016] — Thiết kế ERD & Ánh xạ Schema: Quản lý Dự Án Xây Dựng & Nhà Thầu
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `DU_AN, HANG_MUC, NHA_THAU, CONG_NHAN, TIEN_DO`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Dự Án Xây Dựng & Nhà Thầu', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Dự Án Xây Dựng & Nhà Thầu
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.50đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 1.00đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 17 [ERD-017] — Thiết kế ERD & Ánh xạ Schema: Quản lý Khách Sạn & Đặt Phòng Nghỉ Dưỡng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `LOAI_PHONG, PHONG, KHACH_HANG, PHIEU_DAT, DICH_VU`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Khách Sạn & Đặt Phòng Nghỉ Dưỡng', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Khách Sạn & Đặt Phòng Nghỉ Dưỡng
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.20đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 0.80đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 18 [ERD-018] — Thiết kế ERD & Ánh xạ Schema: Quản lý Cảng Biển & Xuất Nhập Khẩu Container
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `TAU_HANG, CAU_CANG, CONTAINER, DOANH_NGHIEP, PHIEU_XUATNHAP`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Cảng Biển & Xuất Nhập Khẩu Container', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Cảng Biển & Xuất Nhập Khẩu Container
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.50đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 1.00đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 19 [ERD-019] — Thiết kế ERD & Ánh xạ Schema: Quản lý Vườn Ươm & Phân Phối Cây Cảnh
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `LOAI_CAY, CAY_CANH, VUON_UOM, NHA_VUON, DON_DAT`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Vườn Ươm & Phân Phối Cây Cảnh', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Vườn Ươm & Phân Phối Cây Cảnh
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.20đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 0.80đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 20 [ERD-020] — Thiết kế ERD & Ánh xạ Schema: Quản lý Thẻ Phòng Tập Gym & Huấn Luyện Viên
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `GOI_TAP, HOI_VIEN, HLV, BUOI_TAP, DIEM_DANH`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Thẻ Phòng Tập Gym & Huấn Luyện Viên', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Thẻ Phòng Tập Gym & Huấn Luyện Viên
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.50đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 1.00đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 21 [ERD-021] — Thiết kế ERD & Ánh xạ Schema: Quản lý Nhà Hàng Tiệc Cưới & Thực Đơn
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `SANH_TIEC, LOAI_TIEC, KHACH_DAT, THUC_DON, MON_AN`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Nhà Hàng Tiệc Cưới & Thực Đơn', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Nhà Hàng Tiệc Cưới & Thực Đơn
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.20đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 0.80đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 22 [ERD-022] — Thiết kế ERD & Ánh xạ Schema: Quản lý Học Bổng Khuyến Khích Học Tập UIT
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `LOAI_HOCBONG, SINH_VIEN, HOC_KY, HO_SO_XET, KET_QUA`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Học Bổng Khuyến Khích Học Tập UIT', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Học Bổng Khuyến Khích Học Tập UIT
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.50đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 1.00đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 23 [ERD-023] — Thiết kế ERD & Ánh xạ Schema: Quản lý Trạm Sạc Xe Điện Thông Minh
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `TRAM_SAC, TRU_SAC, XE_DIEN, PHIEN_SAC, HOA_DON`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Trạm Sạc Xe Điện Thông Minh', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Trạm Sạc Xe Điện Thông Minh
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.20đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 0.80đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 24 [ERD-024] — Thiết kế ERD & Ánh xạ Schema: Quản lý Trung Tâm Ngoại Ngữ & Thi Chứng Chỉ
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `KHOA_HOC, LOP_HOC, HOC_VIEN, GIANG_VIEN, CHUNG_CHI`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Trung Tâm Ngoại Ngữ & Thi Chứng Chỉ', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Trung Tâm Ngoại Ngữ & Thi Chứng Chỉ
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.50đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 1.00đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 25 [ERD-025] — Thiết kế ERD & Ánh xạ Schema: Quản lý Kho Vận & Robot Tự Hành AGV
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `KHO_HANG, KE_HANG, ROBOT, PALLET, DON_XUATKHO`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Kho Vận & Robot Tự Hành AGV', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Kho Vận & Robot Tự Hành AGV
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.20đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 0.80đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 26 [ERD-026] — Thiết kế ERD & Ánh xạ Schema: Quản lý Hệ Thống Bán Vé Tàu Hỏa Bắc - Nam
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `GA_TAU, CHUYEN_TAU, TOA_TAU, GHE_NGOI, VE_TAU`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Hệ Thống Bán Vé Tàu Hỏa Bắc - Nam', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Hệ Thống Bán Vé Tàu Hỏa Bắc - Nam
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.50đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 1.00đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 27 [ERD-027] — Thiết kế ERD & Ánh xạ Schema: Quản lý Ngân Hàng Máu & Hiến Máu Nhân Đạo
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `DIEM_HIENMAU, NGUOI_HIEN, TUI_MAU, BENH_VIEN, PHIEU_LINH`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Ngân Hàng Máu & Hiến Máu Nhân Đạo', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Ngân Hàng Máu & Hiến Máu Nhân Đạo
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.20đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 0.80đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 28 [ERD-028] — Thiết kế ERD & Ánh xạ Schema: Quản lý Sân Bay & Chuyến Bay Nội Địa
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `MAY_BAY, TUYEN_BAY, CHUYEN_BAY, PHI_CONG, HANH_KHACH`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Sân Bay & Chuyến Bay Nội Địa', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Sân Bay & Chuyến Bay Nội Địa
**Lược đồ quan hệ chuyển đổi:**
- Lược đồ quan hệ chuẩn hóa 3NF/BCNF với PK gạch chân và FK tường minh

**Các bước suy luận tư duy:**
1. Bước 1: Phân tích danh từ chỉ đối tượng để xác định Thực thể và Thuộc tính.
1. Bước 2: Phân tích động từ và mối liên kết để xác định Mối kết hợp.
1. Bước 3: Xác định ràng buộc số lượng để gán bản số min-max.
1. Bước 4: Ánh xạ: Thực thể -> Bảng; Quan hệ 1:N -> Đưa PK phía 1 sang phía N làm FK; Quan hệ M:N -> Tạo bảng trung gian có khóa chính kết hợp.

**Barem chấm điểm đề xuất:**
- `erd_design`: 1.50đ (Vẽ đúng thực thể, thuộc tính và bản số)
- `schema_mapping`: 1.00đ (Ánh xạ đúng PK, FK không sót)

---

## Bài 29 [M03-Q1] — Thiết Kế ERD & Ánh Xạ CSDL Quản Lý Cứu Trợ Bão Lũ
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `ERD: XA, HO_DAN, NHA_HAOTAM, DOT_CUUTRO, DONG_GOP, PHIEU_NHAN`

### 1. Đề Bài
Thiết kế mô hình Thực thể – Mối kết hợp (ERD) và chuyển sang Lược đồ quan hệ cho Hệ thống Quản lý Tiếp nhận & Phân bổ Tiền cứu trợ Bão lũ gồm các tập thực thể: XA, HO_DAN, NHA_HAOTAM, DOT_CUUTRO cùng các mối kết hợp tương ứng.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- {'name': 'XA', 'pk': 'MAXA', 'attributes': ['MAXA', 'TENXA', 'HUYEN'], 'description': 'Địa bàn hành chính cấp xã/phường.'}
- {'name': 'HO_DAN', 'pk': 'MAHO', 'attributes': ['MAHO', 'CHUHO', 'SONKHAU', 'MUCDO_THIETHAI', 'MAXA'], 'description': 'Hộ gia đình bị ảnh hưởng bão lũ.'}
- {'name': 'NHA_HAOTAM', 'pk': 'MANHT', 'attributes': ['MANHT', 'TENNHT', 'SDT', 'LOAIHINH'], 'description': 'Nhà hảo tâm đóng góp ủng hộ.'}
- {'name': 'DOT_CUUTRO', 'pk': 'MADOT', 'attributes': ['MADOT', 'TENDOT', 'NGAYBD', 'NGAYKT'], 'description': 'Đợt phát động cứu trợ.'}
**Lược đồ quan hệ chuyển đổi:**
- {'table': 'XA', 'pk': ['MAXA'], 'fk': []}
- {'table': 'HO_DAN', 'pk': ['MAHO'], 'fk': [{'column': 'MAXA', 'ref_table': 'XA', 'ref_column': 'MAXA'}]}
- {'table': 'NHA_HAOTAM', 'pk': ['MANHT'], 'fk': []}
- {'table': 'DOT_CUUTRO', 'pk': ['MADOT'], 'fk': []}
- {'table': 'DONG_GOP', 'pk': ['MADG'], 'fk': [{'column': 'MANHT', 'ref_table': 'NHA_HAOTAM', 'ref_column': 'MANHT'}, {'column': 'MADOT', 'ref_table': 'DOT_CUUTRO', 'ref_column': 'MADOT'}]}
- {'table': 'PHIEU_NHAN', 'pk': ['MAPHIEU'], 'fk': [{'column': 'MAHO', 'ref_table': 'HO_DAN', 'ref_column': 'MAHO'}, {'column': 'MADOT', 'ref_table': 'DOT_CUUTRO', 'ref_column': 'MADOT'}]}

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.80đ
- `intermediate_steps`: 0.80đ

---
