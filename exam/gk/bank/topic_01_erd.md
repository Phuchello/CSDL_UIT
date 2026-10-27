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

## Bài 04 [M06-Q1] — Thiết Kế ERD & Ánh Xạ CSDL Phòng Khám Đa Khoa & Hồ Sơ Khám Bệnh
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `ERD: CHUYENKHOA, BACSI, BENHNHAN, DICHVU_KHAM, PHIEUKHAM, CHITIET_DV`

### 1. Đề Bài
Thiết kế mô hình Thực thể – Mối kết hợp (ERD) và chuyển sang Lược đồ quan hệ cho Hệ thống Quản lý Đặt khám & Hồ sơ Bệnh án Phòng khám Đa khoa gồm các thực thể: CHUYENKHOA, BACSI, BENHNHAN, DICHVU_KHAM, PHIEUKHAM và mối kết hợp CHITIET_DV.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- {'name': 'CHUYENKHOA', 'pk': 'MAKC', 'attributes': ['MAKC', 'TENKHOA', 'TRUONGKHOA'], 'description': 'Khoa chuyên môn điều trị.'}
- {'name': 'BACSI', 'pk': 'MABS', 'attributes': ['MABS', 'HOTEN', 'HOCVI', 'LUONG'], 'description': 'Bác sĩ thuộc phòng khám.'}
- {'name': 'BENHNHAN', 'pk': 'MABN', 'attributes': ['MABN', 'HOTEN', 'NGAYSINH', 'GIOITINH', 'DIACHI'], 'description': 'Bệnh nhân đăng ký khám.'}
- {'name': 'DICHVU_KHAM', 'pk': 'MADV', 'attributes': ['MADV', 'TENDV', 'LOAIDV', 'DONGIA'], 'description': 'Dịch vụ y tế kỹ thuật niêm yết.'}
- {'name': 'PHIEUKHAM', 'pk': 'MAPK', 'attributes': ['MAPK', 'NGAYKHAM', 'CHANDOAN'], 'description': 'Phiếu khám bệnh của bệnh nhân.'}
**Lược đồ quan hệ chuyển đổi:**
- {'table': 'CHUYENKHOA', 'pk': ['MAKC'], 'fk': []}
- {'table': 'BACSI', 'pk': ['MABS'], 'fk': [{'column': 'MAKC', 'ref_table': 'CHUYENKHOA', 'ref_column': 'MAKC'}]}
- {'table': 'BENHNHAN', 'pk': ['MABN'], 'fk': []}
- {'table': 'DICHVU_KHAM', 'pk': ['MADV'], 'fk': []}
- {'table': 'PHIEUKHAM', 'pk': ['MAPK'], 'fk': [{'column': 'MABN', 'ref_table': 'BENHNHAN', 'ref_column': 'MABN'}, {'column': 'MABS', 'ref_table': 'BACSI', 'ref_column': 'MABS'}]}
- {'table': 'CHITIET_DV', 'pk': ['MAPK', 'MADV'], 'fk': [{'column': 'MAPK', 'ref_table': 'PHIEUKHAM', 'ref_column': 'MAPK'}, {'column': 'MADV', 'ref_table': 'DICHVU_KHAM', 'ref_column': 'MADV'}]}

**Barem chấm điểm đề xuất:**
- `syntax`: 0.50đ
- `logic`: 1.00đ
- `intermediate_steps`: 1.00đ

---

## Bài 05 [M07-Q1] — Thiết Kế ERD & Ánh Xạ CSDL Quản Lý Thư Viện Đại Học & Mượn Trả Sách
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `ERD: KHOAVIEN, DOCGIA, SACH, THUTHU, PHIEUMUON, CHITIET_MUON`

### 1. Đề Bài
Thiết kế mô hình Thực thể – Mối kết hợp (ERD) và chuyển sang Lược đồ quan hệ cho Hệ thống Quản lý Thư viện Đại học gồm các thực thể: KHOAVIEN, DOCGIA, SACH, THUTHU, PHIEUMUON và mối kết hợp CHITIET_MUON.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- {'name': 'KHOAVIEN', 'pk': 'MAKV', 'attributes': ['MAKV', 'TENKV', 'NAMTL'], 'description': 'Khoa/Viện đào tạo trong trường đại học.'}
- {'name': 'DOCGIA', 'pk': 'MADG', 'attributes': ['MADG', 'HOTEN', 'NGAYSINH', 'LOAIDG'], 'description': 'Độc giả sinh viên/giảng viên.'}
- {'name': 'SACH', 'pk': 'MASACH', 'attributes': ['MASACH', 'TENSACH', 'TACGIA', 'NXB', 'NAMXB', 'SOLUONGTON'], 'description': 'Đầu sách in lưu hành.'}
- {'name': 'THUTHU', 'pk': 'MATT', 'attributes': ['MATT', 'HOTEN', 'SODT'], 'description': 'Cán bộ thủ thư quản lý mượn trả.'}
- {'name': 'PHIEUMUON', 'pk': 'MAPM', 'attributes': ['MAPM', 'NGAYMUON', 'HANTRA', 'TRANGTHAI'], 'description': 'Phiếu mượn tài liệu sách in.'}
**Lược đồ quan hệ chuyển đổi:**
- {'table': 'KHOAVIEN', 'pk': ['MAKV'], 'fk': []}
- {'table': 'DOCGIA', 'pk': ['MADG'], 'fk': [{'column': 'MAKV', 'ref_table': 'KHOAVIEN', 'ref_column': 'MAKV'}]}
- {'table': 'SACH', 'pk': ['MASACH'], 'fk': []}
- {'table': 'THUTHU', 'pk': ['MATT'], 'fk': []}
- {'table': 'PHIEUMUON', 'pk': ['MAPM'], 'fk': [{'column': 'MADG', 'ref_table': 'DOCGIA', 'ref_column': 'MADG'}, {'column': 'MATT', 'ref_table': 'THUTHU', 'ref_column': 'MATT'}]}
- {'table': 'CHITIET_MUON', 'pk': ['MAPM', 'MASACH'], 'fk': [{'column': 'MAPM', 'ref_table': 'PHIEUMUON', 'ref_column': 'MAPM'}, {'column': 'MASACH', 'ref_table': 'SACH', 'ref_column': 'MASACH'}]}

**Barem chấm điểm đề xuất:**
- `syntax`: 0.50đ
- `logic`: 1.00đ
- `intermediate_steps`: 1.00đ

---

## Bài 06 [M08-Q1] — Thiết Kế ERD & Ánh Xạ CSDL Quản Lý Sàn Thương Mại Điện Tử & Đơn Hàng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `ERD: GIANHANG, SANPHAM, KHACHHANG, DONHANG, VANCHUYEN, CHITIET_DH`

### 1. Đề Bài
Thiết kế mô hình Thực thể – Mối kết hợp (ERD) và chuyển sang Lược đồ quan hệ cho Hệ thống Quản lý Sàn Thương mại Điện tử gồm các thực thể: GIANHANG, SANPHAM, KHACHHANG, DONHANG, VANCHUYEN và mối kết hợp CHITIET_DH.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- {'name': 'GIANHANG', 'pk': 'MAGH', 'attributes': ['MAGH', 'TENGH', 'NGUOIDAIDIEN', 'THANHPHO'], 'description': 'Gian hàng người bán.'}
- {'name': 'SANPHAM', 'pk': 'MASP', 'attributes': ['MASP', 'TENSP', 'LOAISP', 'GIANIEMYET'], 'description': 'Hàng hóa niêm yết bán.'}
- {'name': 'KHACHHANG', 'pk': 'MAKH', 'attributes': ['MAKH', 'HOTEN', 'DIACHI', 'HANGTHANHVIEN'], 'description': 'Khách hàng mua sắm.'}
- {'name': 'DONHANG', 'pk': 'MADH', 'attributes': ['MADH', 'NGAYDAT', 'HINHTHUCTT', 'TRANGTHAI'], 'description': 'Đơn đặt hàng trực tuyến.'}
- {'name': 'VANCHUYEN', 'pk': 'MAVD', 'attributes': ['MAVD', 'DONVIVC', 'CUOCPHI', 'NGAYGIAO'], 'description': 'Vận đơn giao hàng.'}
**Lược đồ quan hệ chuyển đổi:**
- {'table': 'GIANHANG', 'pk': ['MAGH'], 'fk': []}
- {'table': 'SANPHAM', 'pk': ['MASP'], 'fk': [{'column': 'MAGH', 'ref_table': 'GIANHANG', 'ref_column': 'MAGH'}]}
- {'table': 'KHACHHANG', 'pk': ['MAKH'], 'fk': []}
- {'table': 'DONHANG', 'pk': ['MADH'], 'fk': [{'column': 'MAKH', 'ref_table': 'KHACHHANG', 'ref_column': 'MAKH'}]}
- {'table': 'CHITIET_DH', 'pk': ['MADH', 'MASP'], 'fk': [{'column': 'MADH', 'ref_table': 'DONHANG', 'ref_column': 'MADH'}, {'column': 'MASP', 'ref_table': 'SANPHAM', 'ref_column': 'MASP'}]}
- {'table': 'VANCHUYEN', 'pk': ['MAVD'], 'fk': [{'column': 'MADH', 'ref_table': 'DONHANG', 'ref_column': 'MADH'}]}

**Barem chấm điểm đề xuất:**
- `syntax`: 0.50đ
- `logic`: 1.00đ
- `intermediate_steps`: 1.00đ

---

## Bài 07 [M09-Q1] — Thiết Kế ERD & Ánh Xạ CSDL Quản Lý Giải Đấu Thể Thao Điện Tử Sinh Viên
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `ERD: TRUONG, DOITHI, TUYENTHU, TRANDAU, NHATAITRO, THAMGIA_TRAN`

### 1. Đề Bài
Thiết kế mô hình Thực thể – Mối kết hợp (ERD) và chuyển sang Lược đồ quan hệ cho Hệ thống Quản lý Giải đấu Thể thao Điện tử gồm các thực thể: TRUONG, DOITHI, TUYENTHU, TRANDAU, NHATAITRO và mối kết hợp THAMGIA_TRAN.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- {'name': 'TRUONG', 'pk': 'MATRUONG', 'attributes': ['MATRUONG', 'TENTRUONG', 'THANHPHO'], 'description': 'Trường đại học tham dự.'}
- {'name': 'DOITHI', 'pk': 'MADOI', 'attributes': ['MADOI', 'TENDOI', 'NGUOIQUANLY'], 'description': 'Đội tuyển thi đấu.'}
- {'name': 'TUYENTHU', 'pk': 'MATT', 'attributes': ['MATT', 'HOTEN', 'VITRI', 'TIENLUONG'], 'description': 'Tuyển thủ thi đấu.'}
- {'name': 'TRANDAU', 'pk': 'MATRAN', 'attributes': ['MATRAN', 'NGAYDAU', 'VONGDAU', 'DIADIEM'], 'description': 'Trận đấu theo lịch trình.'}
- {'name': 'NHATAITRO', 'pk': 'MANTT', 'attributes': ['MANTT', 'TENNTT', 'SOTIEN_TT'], 'description': 'Nhà tài trợ thương mại.'}
**Lược đồ quan hệ chuyển đổi:**
- {'table': 'TRUONG', 'pk': ['MATRUONG'], 'fk': []}
- {'table': 'DOITHI', 'pk': ['MADOI'], 'fk': [{'column': 'MATRUONG', 'ref_table': 'TRUONG', 'ref_column': 'MATRUONG'}]}
- {'table': 'TUYENTHU', 'pk': ['MATT'], 'fk': [{'column': 'MADOI', 'ref_table': 'DOITHI', 'ref_column': 'MADOI'}]}
- {'table': 'TRANDAU', 'pk': ['MATRAN'], 'fk': []}
- {'table': 'THAMGIA_TRAN', 'pk': ['MATRAN', 'MADOI'], 'fk': [{'column': 'MATRAN', 'ref_table': 'TRANDAU', 'ref_column': 'MATRAN'}, {'column': 'MADOI', 'ref_table': 'DOITHI', 'ref_column': 'MADOI'}]}
- {'table': 'NHATAITRO', 'pk': ['MANTT'], 'fk': [{'column': 'MATRAN', 'ref_table': 'TRANDAU', 'ref_column': 'MATRAN'}]}

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.80đ
- `intermediate_steps`: 0.80đ

---

## Bài 08 [M10-Q1] — Thiết Kế ERD & Ánh Xạ CSDL Quản Lý Gara Ô Tô & Lịch Trình Bảo Dưỡng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `ERD: KHACHHANG, XE, THO, PHUTUNG, PHIEU_BD, CHITIET_BD`

### 1. Đề Bài
Thiết kế mô hình Thực thể – Mối kết hợp (ERD) và chuyển sang Lược đồ quan hệ cho Hệ thống Quản lý Gara Ô tô gồm các thực thể: KHACHHANG, XE, THO, PHUTUNG, PHIEU_BD và mối kết hợp CHITIET_BD.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- {'name': 'KHACHHANG', 'pk': 'MAKH', 'attributes': ['MAKH', 'HOTEN', 'DIENTHOAI', 'DIACHI'], 'description': 'Khách hàng chủ xe.'}
- {'name': 'XE', 'pk': 'BIENSO', 'attributes': ['BIENSO', 'HANGXE', 'MODEL', 'NAMSX'], 'description': 'Phương tiện ô tô.'}
- {'name': 'THO', 'pk': 'MATHO', 'attributes': ['MATHO', 'HOTEN', 'CHUYENMON', 'LUONG_CB'], 'description': 'Thợ kỹ thuật gara.'}
- {'name': 'PHUTUNG', 'pk': 'MAPT', 'attributes': ['MAPT', 'TENPT', 'LOAIPT', 'DONGIA', 'SOLUONGTON'], 'description': 'Phụ tùng thay thế.'}
- {'name': 'PHIEU_BD', 'pk': 'MAPHIEU', 'attributes': ['MAPHIEU', 'NGAYLAP', 'TONGTIEN', 'TRANGTHAI'], 'description': 'Phiếu bảo dưỡng ô tô.'}
**Lược đồ quan hệ chuyển đổi:**
- {'table': 'KHACHHANG', 'pk': ['MAKH'], 'fk': []}
- {'table': 'XE', 'pk': ['BIENSO'], 'fk': [{'column': 'MAKH', 'ref_table': 'KHACHHANG', 'ref_column': 'MAKH'}]}
- {'table': 'THO', 'pk': ['MATHO'], 'fk': []}
- {'table': 'PHUTUNG', 'pk': ['MAPT'], 'fk': []}
- {'table': 'PHIEU_BD', 'pk': ['MAPHIEU'], 'fk': [{'column': 'BIENSO', 'ref_table': 'XE', 'ref_column': 'BIENSO'}, {'column': 'MATHO', 'ref_table': 'THO', 'ref_column': 'MATHO'}]}
- {'table': 'CHITIET_BD', 'pk': ['MAPHIEU', 'MAPT'], 'fk': [{'column': 'MAPHIEU', 'ref_table': 'PHIEU_BD', 'ref_column': 'MAPHIEU'}, {'column': 'MAPT', 'ref_table': 'PHUTUNG', 'ref_column': 'MAPT'}]}

**Barem chấm điểm đề xuất:**
- `syntax`: 0.50đ
- `logic`: 1.00đ
- `intermediate_steps`: 1.00đ

---

## Bài 09 [M11-Q1] — Thiết Kế ERD & Ánh Xạ CSDL Quản Lý Chuỗi Cà Phê Nhượng Quyền
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 20 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `ERD: KHUVUC, CUAHANG, NHANVIEN, NGUYENLIEU, PHIEUXUAT, CHITIET_PX`

### 1. Đề Bài
Thiết kế mô hình Thực thể – Mối kết hợp (ERD) và chuyển sang Lược đồ quan hệ cho Hệ thống Quản lý Chuỗi Cà phê Nhượng quyền gồm các thực thể: KHUVUC, CUAHANG, NHANVIEN, NGUYENLIEU, PHIEUXUAT và mối kết hợp CHITIET_PX.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- {'name': 'KHUVUC', 'pk': 'MAKV', 'attributes': ['MAKV', 'TENKV', 'TRUONGVUNG'], 'description': 'Khu vực quản lý kinh doanh.'}
- {'name': 'CUAHANG', 'pk': 'MACH', 'attributes': ['MACH', 'TENCH', 'DIACHI', 'MAKV', 'NAM_KYHD'], 'description': 'Cửa hàng chi nhánh nhượng quyền.'}
- {'name': 'NHANVIEN', 'pk': 'MANV', 'attributes': ['MANV', 'HOTEN', 'CHUCVU', 'LUONG', 'MACH'], 'description': 'Nhân sự cửa hàng.'}
- {'name': 'NGUYENLIEU', 'pk': 'MANL', 'attributes': ['MANL', 'TENNL', 'LOAINL', 'DONGIA_CHUAN', 'DVT'], 'description': 'Nguyên liệu pha chế.'}
- {'name': 'PHIEUXUAT', 'pk': 'MAPX', 'attributes': ['MAPX', 'NGAYXUAT', 'MACH', 'TONGTIEN', 'TRANGTHAI'], 'description': 'Phiếu xuất kho phân phối.'}
**Lược đồ quan hệ chuyển đổi:**
- {'table': 'KHUVUC', 'pk': ['MAKV'], 'fk': []}
- {'table': 'CUAHANG', 'pk': ['MACH'], 'fk': [{'column': 'MAKV', 'ref_table': 'KHUVUC', 'ref_column': 'MAKV'}]}
- {'table': 'NHANVIEN', 'pk': ['MANV'], 'fk': [{'column': 'MACH', 'ref_table': 'CUAHANG', 'ref_column': 'MACH'}]}
- {'table': 'NGUYENLIEU', 'pk': ['MANL'], 'fk': []}
- {'table': 'PHIEUXUAT', 'pk': ['MAPX'], 'fk': [{'column': 'MACH', 'ref_table': 'CUAHANG', 'ref_column': 'MACH'}]}
- {'table': 'CHITIET_PX', 'pk': ['MAPX', 'MANL'], 'fk': [{'column': 'MAPX', 'ref_table': 'PHIEUXUAT', 'ref_column': 'MAPX'}, {'column': 'MANL', 'ref_table': 'NGUYENLIEU', 'ref_column': 'MANL'}]}

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.80đ
- `intermediate_steps`: 0.80đ

---

## Bài 10 [ERD-012] — Thiết kế ERD & Ánh xạ Schema: Quản lý Rạp Chiếu Phim & Đặt Vé Trực Tuyến
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

## Bài 11 [ERD-013] — Thiết kế ERD & Ánh xạ Schema: Quản lý Tuyến Xe Buýt & Metro Đô Thị
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

## Bài 12 [ERD-014] — Thiết kế ERD & Ánh xạ Schema: Quản lý Đề Tài Nghiên Cứu Khoa Học Sinh Viên
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

## Bài 13 [ERD-015] — Thiết kế ERD & Ánh xạ Schema: Quản lý Trại Cứu Hộ Động Vật Hoang Dã
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

## Bài 14 [ERD-016] — Thiết kế ERD & Ánh xạ Schema: Quản lý Dự Án Xây Dựng & Nhà Thầu
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

## Bài 15 [ERD-017] — Thiết kế ERD & Ánh xạ Schema: Quản lý Khách Sạn & Đặt Phòng Nghỉ Dưỡng
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

## Bài 16 [ERD-018] — Thiết kế ERD & Ánh xạ Schema: Quản lý Cảng Biển & Xuất Nhập Khẩu Container
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

## Bài 17 [ERD-019] — Thiết kế ERD & Ánh xạ Schema: Quản lý Vườn Ươm & Phân Phối Cây Cảnh
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

## Bài 18 [ERD-020] — Thiết kế ERD & Ánh xạ Schema: Quản lý Thẻ Phòng Tập Gym & Huấn Luyện Viên
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

## Bài 19 [ERD-021] — Thiết kế ERD & Ánh xạ Schema: Quản lý Nhà Hàng Tiệc Cưới & Thực Đơn
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

## Bài 20 [ERD-022] — Thiết kế ERD & Ánh xạ Schema: Quản lý Học Bổng Khuyến Khích Học Tập UIT
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

## Bài 21 [ERD-023] — Thiết kế ERD & Ánh xạ Schema: Quản lý Trạm Sạc Xe Điện Thông Minh
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

## Bài 22 [ERD-024] — Thiết kế ERD & Ánh xạ Schema: Quản lý Trung Tâm Ngoại Ngữ & Thi Chứng Chỉ
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

## Bài 23 [ERD-025] — Thiết kế ERD & Ánh xạ Schema: Quản lý Kho Vận & Robot Tự Hành AGV
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

## Bài 24 [ERD-026] — Thiết kế ERD & Ánh xạ Schema: Quản lý Hệ Thống Bán Vé Tàu Hỏa Bắc - Nam
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

## Bài 25 [ERD-027] — Thiết kế ERD & Ánh xạ Schema: Quản lý Ngân Hàng Máu & Hiến Máu Nhân Đạo
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

## Bài 26 [ERD-028] — Thiết kế ERD & Ánh xạ Schema: Quản lý Sân Bay & Chuyến Bay Nội Địa
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

## Bài 27 [M03-Q1] — Thiết Kế ERD & Ánh Xạ CSDL Quản Lý Cứu Trợ Bão Lũ
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

## Bài 28 [M04-Q1] — Thiết Kế ERD & Ánh Xạ CSDL Chuỗi Cửa Hàng Xăng Dầu
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.5 điểm
- **Lược đồ tham chiếu:** `ERD: CUAHANG, NHANVIEN, NHIENLIEU, BE_CHUA, HOADON, CTHD`

### 1. Đề Bài
Thiết kế mô hình Thực thể – Mối kết hợp (ERD) và chuyển sang Lược đồ quan hệ cho Hệ thống Quản lý Chuỗi Cửa hàng Bán lẻ Xăng dầu gồm các thực thể: CUAHANG, NHANVIEN, NHIENLIEU, BE_CHUA, HOADON cùng các mối kết hợp tương ứng.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- {'name': 'CUAHANG', 'pk': 'MACH', 'attributes': ['MACH', 'TENCH', 'DIACHI', 'QUAN', 'SO_TRU_BOM'], 'description': 'Cửa hàng xăng dầu trực thuộc chuỗi.'}
- {'name': 'NHANVIEN', 'pk': 'MANV', 'attributes': ['MANV', 'HOTEN', 'NGAYSINH', 'CHUCVU', 'LUONG'], 'description': 'Nhân viên công tác tại cửa hàng.'}
- {'name': 'NHIENLIEU', 'pk': 'MANL', 'attributes': ['MANL', 'TENNL', 'LOAINL', 'DONVITINH', 'DONGIA'], 'description': 'Mặt hàng xăng dầu phân phối.'}
- {'name': 'BE_CHUA', 'pk': 'MABE', 'attributes': ['MABE', 'DUNGTICH', 'LUONG_TON'], 'description': 'Bể ngầm chứa nhiên liệu tại cửa hàng.'}
- {'name': 'HOADON', 'pk': 'MAHD', 'attributes': ['MAHD', 'NGAYHD', 'HINHTHUC_TT'], 'description': 'Hóa đơn xuất bán lẻ xăng dầu.'}
**Lược đồ quan hệ chuyển đổi:**
- {'table': 'CUAHANG', 'pk': ['MACH'], 'fk': []}
- {'table': 'NHANVIEN', 'pk': ['MANV'], 'fk': [{'column': 'MACH', 'ref_table': 'CUAHANG', 'ref_column': 'MACH'}]}
- {'table': 'NHIENLIEU', 'pk': ['MANL'], 'fk': []}
- {'table': 'BE_CHUA', 'pk': ['MABE'], 'fk': [{'column': 'MACH', 'ref_table': 'CUAHANG', 'ref_column': 'MACH'}, {'column': 'MANL', 'ref_table': 'NHIENLIEU', 'ref_column': 'MANL'}]}
- {'table': 'HOADON', 'pk': ['MAHD'], 'fk': [{'column': 'MACH', 'ref_table': 'CUAHANG', 'ref_column': 'MACH'}, {'column': 'MANV', 'ref_table': 'NHANVIEN', 'ref_column': 'MANV'}]}
- {'table': 'CTHD', 'pk': ['MAHD', 'MANL'], 'fk': [{'column': 'MAHD', 'ref_table': 'HOADON', 'ref_column': 'MAHD'}, {'column': 'MANL', 'ref_table': 'NHIENLIEU', 'ref_column': 'MANL'}]}

**Barem chấm điểm đề xuất:**
- `syntax`: 0.50đ
- `logic`: 1.00đ
- `intermediate_steps`: 1.00đ

---

## Bài 29 [M05-Q1] — Thiết Kế ERD & Ánh Xạ CSDL Căn Hộ Chung Cư & Hợp Đồng Thuê Nhà
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 25 phút | **Điểm số:** 2.0 điểm
- **Lược đồ tham chiếu:** `ERD: TOANHA, CANHO, KHACHHANG, NHANVIEN, HOPDONG, PHIEUTHU`

### 1. Đề Bài
Thiết kế mô hình Thực thể – Mối kết hợp (ERD) và chuyển sang Lược đồ quan hệ cho Hệ thống Quản lý Căn hộ Chung cư & Hợp đồng Thuê nhà gồm các thực thể: TOANHA, CANHO, KHACHHANG, NHANVIEN, HOPDONG, PHIEUTHU cùng các mối kết hợp tương ứng.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Các thực thể và thuộc tính:**
- {'name': 'TOANHA', 'pk': 'MATN', 'attributes': ['MATN', 'TENTN', 'DIACHI', 'SOTANG'], 'description': 'Tòa nhà / Block chung cư.'}
- {'name': 'CANHO', 'pk': 'MACH', 'attributes': ['MACH', 'SOPHONG', 'DIENTICH', 'GIATHUE_CHUAN', 'TRANGTHAI'], 'description': 'Căn hộ trong tòa nhà.'}
- {'name': 'KHACHHANG', 'pk': 'MAKH', 'attributes': ['MAKH', 'HOTEN', 'CCCD', 'SDT', 'LOAIKH'], 'description': 'Khách hàng thuê căn hộ.'}
- {'name': 'NHANVIEN', 'pk': 'MANV', 'attributes': ['MANV', 'HOTEN', 'PHONGBAN', 'SDT'], 'description': 'Nhân viên môi giới / quản lý.'}
- {'name': 'HOPDONG', 'pk': 'MAHD', 'attributes': ['MAHD', 'NGAYKY', 'NGAYBD', 'NGAYKT', 'GIATHUE_THUCTE', 'TIENCOC'], 'description': 'Hợp đồng cho thuê căn hộ.'}
- {'name': 'PHIEUTHU', 'pk': 'SOPHIEU', 'attributes': ['SOPHIEU', 'THANG', 'NAM', 'NGAYTHU', 'SOTIEN'], 'description': 'Phiếu thu tiền thuê hàng tháng.'}
**Lược đồ quan hệ chuyển đổi:**
- {'table': 'TOANHA', 'pk': ['MATN'], 'fk': []}
- {'table': 'CANHO', 'pk': ['MACH'], 'fk': [{'column': 'MATN', 'ref_table': 'TOANHA', 'ref_column': 'MATN'}]}
- {'table': 'KHACHHANG', 'pk': ['MAKH'], 'fk': []}
- {'table': 'NHANVIEN', 'pk': ['MANV'], 'fk': []}
- {'table': 'HOPDONG', 'pk': ['MAHD'], 'fk': [{'column': 'MACH', 'ref_table': 'CANHO', 'ref_column': 'MACH'}, {'column': 'MAKH', 'ref_table': 'KHACHHANG', 'ref_column': 'MAKH'}, {'column': 'MANV', 'ref_table': 'NHANVIEN', 'ref_column': 'MANV'}]}
- {'table': 'PHIEUTHU', 'pk': ['SOPHIEU'], 'fk': [{'column': 'MAHD', 'ref_table': 'HOPDONG', 'ref_column': 'MAHD'}]}

**Barem chấm điểm đề xuất:**
- `syntax`: 0.40đ
- `logic`: 0.80đ
- `intermediate_steps`: 0.80đ

---
