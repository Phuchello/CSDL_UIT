# CHUYÊN ĐỀ 1: MÔ HÌNH THỰC THỂ MỐI KẾT HỢP (ERD) & ÁNH XẠ QUAN HỆ
**Môn học:** IT004 — Cơ sở dữ liệu | **Hệ thống:** UIT Exam Mastery
**Biên soạn:** VÕ TRỌNG PHÚC | **Số lượng bài tập:** 33 bài

---

## Bài 01 [M01-Q1] — Thiết kế ERD & Ánh xạ CSDL Quản lý Tiêm Chủng Vắc-Xin
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `ERD: TTYT, LOVACXIN, NHACC, DIEMTIEM, NHANVIEN, PHANPHOI`

### 1. Đề Bài
Thiết kế mô hình Thực thể – Mối kết hợp (ERD) và chuyển sang Lược đồ quan hệ cho Hệ thống Quản lý Tiêm Chủng Vắc-Xin tại các Trung tâm Y tế. Bối cảnh gồm TTYT, LO_VACXIN, NHACUNGCAP, DIEMTIEM, NHANVIEN, và Đợt phân phối PHANPHOI.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- {'name': 'TRUNGTAM_YTE', 'pk': 'MaTT', 'attributes': ['MaTT', 'TenTT', 'DiaChiQuan']}
- {'name': 'NHA_CUNGCAP', 'pk': 'MaNCC', 'attributes': ['MaNCC', 'TenNCC', 'QuocGia', 'SDT']}
- {'name': 'LO_VACXIN', 'pk': 'MaLo', 'attributes': ['MaLo', 'TenLo', 'TenVacxin', 'NgaySX', 'HSD', 'SoLieuNhap', 'DonGia']}
- {'name': 'DIEM_TIEM', 'pk': 'MaDT', 'attributes': ['MaDT', 'TenDT', 'DiaDiem', 'SucChua']}
- {'name': 'NHAN_VIEN', 'pk': 'MaNV', 'attributes': ['MaNV', 'HoTen', 'ChuyenMon', 'SDT']}
**Lược đồ quan hệ chuyển đổi:**
- TRUNGTAM_YTE (MaTT, TenTT, DiaChiQuan) - PK: MaTT
- NHA_CUNGCAP (MaNCC, TenNCC, QuocGia, SDT) - PK: MaNCC
- LO_VACXIN (MaLo, TenLo, TenVacxin, NgaySX, HSD, SoLieuNhap, DonGia, MaNCC) - PK: MaLo, FK: MaNCC -> NHA_CUNGCAP(MaNCC)
- DIEM_TIEM (MaDT, TenDT, DiaDiem, SucChua, MaTT) - PK: MaDT, FK: MaTT -> TRUNGTAM_YTE(MaTT)
- NHAN_VIEN (MaNV, HoTen, ChuyenMon, SDT, MaTT) - PK: MaNV, FK: MaTT -> TRUNGTAM_YTE(MaTT)
- PHAN_PHOI (MaLo, MaDT, NgayPP, SoLieuPP, TrangThai) - PK: (MaLo, MaDT, NgayPP), FK: MaLo -> LO_VACXIN(MaLo), MaDT -> DIEM_TIEM(MaDT)
- TRUC_CA (MaNV, MaDT, NgayTruc, VaiTroTruc) - PK: (MaNV, MaDT, NgayTruc), FK: MaNV -> NHAN_VIEN(MaNV), MaDT -> DIEM_TIEM(MaDT)

**Các bước suy luận tư duy:**
1. Bước 1: Liệt kê thực thể và thuộc tính nhận diện từ văn bản.
1. Bước 2: Xác định bản số min-max dựa trên từ khóa: 'mỗi lô do duy nhất 1 NCC' -> (1,1); 'một NCC cung cấp nhiều lô' -> (1,N).
1. Bước 3: Chuyển đổi mối kết hợp 1:N bằng cách mang PK phía 1 sang làm FK phía N.
1. Bước 4: Chuyển đổi mối kết hợp M:N (PHAN_PHOI, TRUC_CA) thành bảng riêng với khóa chính là tổ hợp PK hai phía kèm thuộc tính phân biệt thời gian.

**Barem chấm điểm đề xuất:**
- `erd_entities`: 0.75đ (Xác định đúng 5 thực thể và khóa chính)
- `erd_relationships_cardinality`: 0.75đ (Vẽ đúng mối kết hợp và bản số min-max hai phía)
- `mapping_pk_fk`: 1.00đ (Chuyển đổi đúng quan hệ, gạch chân PK và xác định rõ FK)

---

## Bài 02 [ERD-002] — Thiết Kế ERD Hệ Thống Phòng Cháy Chữa Cháy Chung Cư (Authentic 2023–2024)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `ERD: TOANHA, TANG, LOAI_DUNG_CU, DOT_KIEM_TRA, CAN_HO`

### 1. Đề Bài
Vẽ mô hình ERD và ánh xạ Lược đồ quan hệ quản lý PCCC: Khu chung cư có nhiều tòa nhà; mỗi tòa nhà có nhiều tầng. Mỗi tầng có mã số duy nhất, tên tầng, số căn hộ. Thiết bị PCCC có tên loại, mô tả. Đợt kiểm tra ghi nhận tình trạng hoạt động.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- {'name': 'TOA_NHA', 'pk': 'MaToa', 'attributes': ['MaToa', 'TenToa', 'SoTang']}
- {'name': 'TANG', 'pk': 'MaTang', 'attributes': ['MaTang', 'TenTang', 'SoCanHo']}
- {'name': 'LOAI_THIETBI', 'pk': 'MaLoai', 'attributes': ['MaLoai', 'TenLoai', 'MoTa']}
- {'name': 'THIET_BI', 'pk': 'MaTB', 'attributes': ['MaTB', 'ViTriLapDat', 'NgayTrangBi']}
**Lược đồ quan hệ chuyển đổi:**
- TOA_NHA (MaToa, TenToa, SoTang) - PK: MaToa
- TANG (MaTang, TenTang, SoCanHo, MaToa) - PK: MaTang, FK: MaToa -> TOA_NHA(MaToa)
- LOAI_THIETBI (MaLoai, TenLoai, MoTa) - PK: MaLoai
- THIET_BI (MaTB, ViTriLapDat, NgayTrangBi, MaLoai, MaTang) - PK: MaTB, FK: MaLoai -> LOAI_THIETBI, MaTang -> TANG

**Các bước suy luận tư duy:**
1. Xác định thực thể yếu/mạnh
1. Bản số min-max
1. Chuyển đổi quan hệ 1:N bằng FK.

**Barem chấm điểm đề xuất:**
- `erd`: 1.50đ
- `mapping`: 1.00đ

---

## Bài 03 [ERD-003] — Thiết Kế ERD Quản Lý Cứu Trợ Thiên Tai & Bão Lũ (Authentic 2024–2025)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `ERD: XA, HO_DAN, DOT_CUUTRO, NHA_HAOTAM, PHIEU_NHAN`

### 1. Đề Bài
Thiết kế mô hình ERD quản lý cứu trợ bão lũ: Ghi nhận thông tin hộ dân thiệt hại theo địa bàn thôn/xã, các đợt cứu trợ và các khoản đóng góp ủng hộ của nhà hảo tâm.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- {'name': 'XA', 'pk': 'MaXa', 'attributes': ['MaXa', 'TenXa', 'Huyen']}
- {'name': 'HO_DAN', 'pk': 'MaHo', 'attributes': ['MaHo', 'ChuHo', 'SoNhanKhau', 'MucDoThietHai']}
- {'name': 'NHA_HAOTAM', 'pk': 'MaNHT', 'attributes': ['MaNHT', 'TenNHT', 'SDT', 'LoaiHinh']}
- {'name': 'DOT_CUUTRO', 'pk': 'MaDot', 'attributes': ['MaDot', 'TenDot', 'NgayBatDau']}
**Lược đồ quan hệ chuyển đổi:**
- XA (MaXa, TenXa, Huyen) - PK: MaXa
- HO_DAN (MaHo, ChuHo, SoNhanKhau, MucDoThietHai, MaXa) - PK: MaHo, FK: MaXa -> XA(MaXa)
- NHA_HAOTAM (MaNHT, TenNHT, SDT, LoaiHinh) - PK: MaNHT
- DOT_CUUTRO (MaDot, TenDot, NgayBatDau) - PK: MaDot
- DONG_GOP (MaNHT, MaDot, NgayDongGop, SoTien) - PK: (MaNHT, MaDot, NgayDongGop), FK: MaNHT -> NHA_HAOTAM, MaDot -> DOT_CUUTRO

**Các bước suy luận tư duy:**
1. Xác định thuộc tính
1. Bản số min-max
1. Ánh xạ bảng trung gian M:N.

**Barem chấm điểm đề xuất:**
- `erd`: 1.25đ
- `mapping`: 0.75đ

---

## Bài 04 [ERD-001] — Thiết kế ERD & Ánh xạ Schema: Quản lý Cung ứng & Tiêm chủng Vắc-xin
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

## Bài 05 [ERD-004] — Thiết kế ERD & Ánh xạ Schema: Quản lý Trạm Xăng Dầu & Bán Lẻ Nhiên Liệu
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

## Bài 06 [ERD-005] — Thiết kế ERD & Ánh xạ Schema: Quản lý Căn Hộ Chung Cư Cho Thuê
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

## Bài 07 [ERD-006] — Thiết kế ERD & Ánh xạ Schema: Quản lý Bệnh Viện & Phòng Khám Đa Khoa
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

## Bài 08 [ERD-007] — Thiết kế ERD & Ánh xạ Schema: Quản lý Thư Viện Số UIT & Mượn Trả Sách
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

## Bài 09 [ERD-008] — Thiết kế ERD & Ánh xạ Schema: Quản lý Sàn Thương Mại Điện Tử & Đơn Hàng
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

## Bài 10 [ERD-009] — Thiết kế ERD & Ánh xạ Schema: Quản lý Giải Đấu Thể Thao Điện Tử (Esports)
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

## Bài 11 [ERD-010] — Thiết kế ERD & Ánh xạ Schema: Quản lý Gara Sửa Chữa & Bảo Dưỡng Ô Tô
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

## Bài 12 [ERD-011] — Thiết kế ERD & Ánh xạ Schema: Quản lý Chuỗi Cà Phê Nhượng Quyền
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

## Bài 13 [ERD-012] — Thiết kế ERD & Ánh xạ Schema: Quản lý Rạp Chiếu Phim & Đặt Vé Trực Tuyến
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

## Bài 14 [ERD-013] — Thiết kế ERD & Ánh xạ Schema: Quản lý Tuyến Xe Buýt & Metro Đô Thị
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

## Bài 15 [ERD-014] — Thiết kế ERD & Ánh xạ Schema: Quản lý Đề Tài Nghiên Cứu Khoa Học Sinh Viên
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

## Bài 16 [ERD-015] — Thiết kế ERD & Ánh xạ Schema: Quản lý Trại Cứu Hộ Động Vật Hoang Dã
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

## Bài 17 [ERD-016] — Thiết kế ERD & Ánh xạ Schema: Quản lý Dự Án Xây Dựng & Nhà Thầu
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

## Bài 18 [ERD-017] — Thiết kế ERD & Ánh xạ Schema: Quản lý Khách Sạn & Đặt Phòng Nghỉ Dưỡng
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

## Bài 19 [ERD-018] — Thiết kế ERD & Ánh xạ Schema: Quản lý Cảng Biển & Xuất Nhập Khẩu Container
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

## Bài 20 [ERD-019] — Thiết kế ERD & Ánh xạ Schema: Quản lý Vườn Ươm & Phân Phối Cây Cảnh
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

## Bài 21 [ERD-020] — Thiết kế ERD & Ánh xạ Schema: Quản lý Thẻ Phòng Tập Gym & Huấn Luyện Viên
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

## Bài 22 [ERD-021] — Thiết kế ERD & Ánh xạ Schema: Quản lý Nhà Hàng Tiệc Cưới & Thực Đơn
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

## Bài 23 [ERD-022] — Thiết kế ERD & Ánh xạ Schema: Quản lý Học Bổng Khuyến Khích Học Tập UIT
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

## Bài 24 [ERD-023] — Thiết kế ERD & Ánh xạ Schema: Quản lý Trạm Sạc Xe Điện Thông Minh
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

## Bài 25 [ERD-024] — Thiết kế ERD & Ánh xạ Schema: Quản lý Trung Tâm Ngoại Ngữ & Thi Chứng Chỉ
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

## Bài 26 [ERD-025] — Thiết kế ERD & Ánh xạ Schema: Quản lý Kho Vận & Robot Tự Hành AGV
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

## Bài 27 [ERD-026] — Thiết kế ERD & Ánh xạ Schema: Quản lý Hệ Thống Bán Vé Tàu Hỏa Bắc - Nam
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

## Bài 28 [ERD-027] — Thiết kế ERD & Ánh xạ Schema: Quản lý Ngân Hàng Máu & Hiến Máu Nhân Đạo
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

## Bài 29 [ERD-028] — Thiết kế ERD & Ánh xạ Schema: Quản lý Sân Bay & Chuyến Bay Nội Địa
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

## Bài 30 [ERD-029] — Thiết kế ERD & Ánh xạ Schema: Quản lý Dịch Vụ Cứu Hộ Giao Thông 24/7
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `XE_CUUHO, TAI_XE, CUOC_GOI, SU_CO, BIEN_BAN`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Dịch Vụ Cứu Hộ Giao Thông 24/7', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Dịch Vụ Cứu Hộ Giao Thông 24/7
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

## Bài 31 [ERD-030] — Thiết kế ERD & Ánh xạ Schema: Quản lý Nông Sản Sạch & Truy Xuất Nguồn Gốc
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `NONG_TRAI, NONG_SAN, LO_HANG, CHUNG_NHAN, DIEM_BAN`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Nông Sản Sạch & Truy Xuất Nguồn Gốc', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Nông Sản Sạch & Truy Xuất Nguồn Gốc
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

## Bài 32 [ERD-031] — Thiết kế ERD & Ánh xạ Schema: Quản lý Đăng Ký Học Phần & Thời Khóa Biểu
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `MON_HOC, LOP_HOCPHAN, GIANG_VIEN, SINH_VIEN, PHONG_HOC`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Đăng Ký Học Phần & Thời Khóa Biểu', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Đăng Ký Học Phần & Thời Khóa Biểu
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

## Bài 33 [ERD-032] — Thiết kế ERD & Ánh xạ Schema: Quản lý Siêu Thị Điện Máy & Bảo Hành
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `NHOM_HANG, SAN_PHAM, KHACH_HANG, HOA_DON, PHIEU_BAOHANH`

### 1. Đề Bài
Đọc ngữ cảnh bài toán 'Quản lý Siêu Thị Điện Máy & Bảo Hành', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- Thực thể chuẩn hóa cho Quản lý Siêu Thị Điện Máy & Bảo Hành
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
