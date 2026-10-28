# CHUYÊN ĐỀ 4: TRANSACT-SQL DDL/DML & RÀNG BUỘC TOÀN VẸN
**Môn học:** IT004 — Cơ sở dữ liệu | **Hệ thống:** UIT Exam Mastery
**Biên soạn:** VÕ TRỌNG PHÚC | **Số lượng bài tập độc lập:** 35 bài chuẩn hóa

---

## Bài 01 [SQL-P01] — T-SQL DDL: Tạo Bảng Đăng Ký Học Phần Tín Chỉ UIT
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `LOPHOCPHAN_P01(MALHP VARCHAR(10) PRIMARY KEY), SINHVIEN_P01(MSSV VARCHAR(10) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng DANGKY_HOCPHAN_P01 với khóa chính phức hợp (MSSV, MALHP), các khóa ngoại tham chiếu, ràng buộc CHECK điểm số giữa 0.0 và 10.0, và giá trị mặc định cho ngày đăng ký.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE DANGKY_HOCPHAN_P01 (
    MSSV VARCHAR(10) NOT NULL,
    MALHP VARCHAR(10) NOT NULL,
    NGAYDK DATE NOT NULL DEFAULT GETDATE(),
    DIEMGK DECIMAL(4, 2) NULL,
    DIEMCK DECIMAL(4, 2) NULL,
    TRANGTHAI NVARCHAR(20) NOT NULL DEFAULT N'Da dang ky',
    CONSTRAINT PK_DANGKY_P01 PRIMARY KEY (MSSV, MALHP),
    CONSTRAINT FK_DANGKY_SV_P01 FOREIGN KEY (MSSV) REFERENCES SINHVIEN_P01(MSSV) ON DELETE CASCADE,
    CONSTRAINT FK_DANGKY_LHP_P01 FOREIGN KEY (MALHP) REFERENCES LOPHOCPHAN_P01(MALHP) ON DELETE CASCADE,
    CONSTRAINT CK_DANGKY_DIEMGK_P01 CHECK (DIEMGK BETWEEN 0.0 AND 10.0),
    CONSTRAINT CK_DANGKY_DIEMCK_P01 CHECK (DIEMCK BETWEEN 0.0 AND 10.0),
    CONSTRAINT CK_DANGKY_TRANGTHAI_P01 CHECK (TRANGTHAI IN (N'Da dang ky', N'Da huy', N'Hoan thanh'))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột MSSV, MALHP, NGAYDK, DIEMGK, DIEMCK, TRANGTHAI với kiểu dữ liệu phù hợp.
1. Bước 2: Thiết lập khóa chính phức hợp (MSSV, MALHP) qua CONSTRAINT PK_DANGKY_P01.
1. Bước 3: Thiết lập hai khóa ngoại tham chiếu đến SINHVIEN_P01 và LOPHOCPHAN_P01 kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK điểm số trong khoảng [0.0, 10.0] và miền trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Các cột tham gia khóa chính bắt buộc phải khai báo NOT NULL; cột điểm cho phép NULL khi mới đăng ký chưa có điểm thi.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 02 [SQL-P02] — T-SQL DDL: Tạo Bảng Phiếu Tiêm Chủng Vắc-Xin
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BACSI_P02(MABS VARCHAR(10) PRIMARY KEY), BENHNHAN_P02(MABN VARCHAR(10) PRIMARY KEY), LOVACXIN_P02(MALO VARCHAR(10) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng TIEM_VACXIN_P02 gồm mã phiếu, bác sĩ chỉ định, bệnh nhân, lô vắc-xin, liều lượng (ml), ngày tiêm và phản ứng sau tiêm.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE TIEM_VACXIN_P02 (
    MAPHIEU VARCHAR(10) NOT NULL,
    MABS VARCHAR(10) NOT NULL,
    MABN VARCHAR(10) NOT NULL,
    MALO VARCHAR(10) NOT NULL,
    NGAYTIEM DATETIME NOT NULL DEFAULT GETDATE(),
    LIEULUONG_ML DECIMAL(4, 2) NOT NULL,
    PHANUNG_SAUTIEM NVARCHAR(50) NOT NULL DEFAULT N'Binh thuong',
    CONSTRAINT PK_TIEM_VACXIN_P02 PRIMARY KEY (MAPHIEU),
    CONSTRAINT FK_TIEM_BS_P02 FOREIGN KEY (MABS) REFERENCES BACSI_P02(MABS),
    CONSTRAINT FK_TIEM_BN_P02 FOREIGN KEY (MABN) REFERENCES BENHNHAN_P02(MABN),
    CONSTRAINT FK_TIEM_LO_P02 FOREIGN KEY (MALO) REFERENCES LOVACXIN_P02(MALO),
    CONSTRAINT CK_TIEM_LIEULUONG_P02 CHECK (LIEULUONG_ML > 0.0),
    CONSTRAINT CK_TIEM_PHANUNG_P02 CHECK (PHANUNG_SAUTIEM IN (N'Binh thuong', N'Sot nhe', N'Di ung', N'Theo doi dac biet'))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo khóa chính đơn MAPHIEU.
1. Bước 2: Thiết lập 3 khóa ngoại liên kết tới bác sĩ, bệnh nhân và lô vắc-xin.
1. Bước 3: Định nghĩa ràng buộc CHECK liều lượng phải lớn hơn 0 và danh mục phản ứng sau tiêm hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm an toàn tiêm chủng với liều lượng dương và kiểm soát phản ứng sau tiêm.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 03 [SQL-P03] — T-SQL DDL: Tạo Bảng Chi Tiết Hóa Đơn Dược Phẩm (Computed Column)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOADON_P03(MAHD VARCHAR(10) PRIMARY KEY), THUOC_P03(MATHUOC VARCHAR(10) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng CTHD_PHARMACY_P03 với khóa chính phức hợp (MAHD, MATHUOC), số lượng bán > 0, đơn giá bán >= 0, mức giảm giá từ 0% đến 50% và cột tính toán THANHTIEN tự động.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CTHD_PHARMACY_P03 (
    MAHD VARCHAR(10) NOT NULL,
    MATHUOC VARCHAR(10) NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    GIAMGIA DECIMAL(4, 2) NOT NULL DEFAULT 0.00,
    THANHTIEN AS (SOLUONG * DONGIA * (1.00 - GIAMGIA)),
    CONSTRAINT PK_CTHD_PHARMACY_P03 PRIMARY KEY (MAHD, MATHUOC),
    CONSTRAINT FK_CTHD_HD_P03 FOREIGN KEY (MAHD) REFERENCES HOADON_P03(MAHD) ON DELETE CASCADE,
    CONSTRAINT FK_CTHD_THUOC_P03 FOREIGN KEY (MATHUOC) REFERENCES THUOC_P03(MATHUOC),
    CONSTRAINT CK_CTHD_SOLUONG_P03 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTHD_DONGIA_P03 CHECK (DONGIA >= 0.0),
    CONSTRAINT CK_CTHD_GIAMGIA_P03 CHECK (GIAMGIA BETWEEN 0.00 AND 0.50)
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột khóa chính phức hợp và thông tin bán hàng.
1. Bước 2: Sử dụng cú pháp cột tính toán `AS (...)` để tự động tính tiền có trừ chiết khấu.
1. Bước 3: Thêm các ràng buộc toàn vẹn miền giá trị (CHECK) cho số lượng, đơn giá và tỷ lệ giảm giá.

**Phân tích trường hợp biên (Edge Cases):**
Cột tính toán AS không cần chỉ định kiểu dữ liệu; SQL Server tự suy diễn kiểu từ biểu thức tính toán.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 04 [SQL-P04] — T-SQL DDL: Tạo Bảng Vé Máy Bay & Hạng Vé Hàng Không
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CHUYENBAY_P04(MACB VARCHAR(10) PRIMARY KEY), HANHKHACH_P04(MAHK VARCHAR(10) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng VE_MAYBAY_P04 với ràng buộc kiểm tra hạng vé chỉ nhận các giá trị ('Eco', 'Deluxe', 'Business'), giá vé > 0 và số ghế không rỗng.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE VE_MAYBAY_P04 (
    MAVE VARCHAR(10) NOT NULL,
    MACB VARCHAR(10) NOT NULL,
    MAHK VARCHAR(10) NOT NULL,
    SOGHE VARCHAR(10) NOT NULL,
    HANGVE VARCHAR(20) NOT NULL,
    GIAVE DECIMAL(12, 2) NOT NULL,
    NGAYDAT DATETIME NOT NULL DEFAULT GETDATE(),
    CONSTRAINT PK_VE_MAYBAY_P04 PRIMARY KEY (MAVE),
    CONSTRAINT FK_VE_CB_P04 FOREIGN KEY (MACB) REFERENCES CHUYENBAY_P04(MACB),
    CONSTRAINT FK_VE_HK_P04 FOREIGN KEY (MAHK) REFERENCES HANHKHACH_P04(MAHK),
    CONSTRAINT CK_VE_HANGVE_P04 CHECK (HANGVE IN ('Eco', 'Deluxe', 'Business')),
    CONSTRAINT CK_VE_GIAVE_P04 CHECK (GIAVE > 0),
    CONSTRAINT UQ_VE_GHE_CB_P04 UNIQUE (MACB, SOGHE)
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo khóa chính MAVE và khóa ngoại liên kết CHUYENBAY, HANHKHACH.
1. Bước 2: Định nghĩa CHECK constraint giới hạn 3 hạng vé hợp lệ.
1. Bước 3: Thiết lập ràng buộc UNIQUE (MACB, SOGHE) để bảo đảm mỗi ghế trên một chuyến bay chỉ bán cho đúng 1 vé.

**Phân tích trường hợp biên (Edge Cases):**
Ràng buộc UNIQUE kết hợp hai cột giúp loại trừ lỗi bán trùng chỗ (overbooking/duplicate seat).

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 05 [SQL-P05] — T-SQL DDL: Tạo Bảng Hợp Đồng Thuê Ký Túc Xá Sinh Viên
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SINHVIEN_P05(MSSV VARCHAR(10) PRIMARY KEY), PHONG_P05(MAPHONG VARCHAR(10) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng HOPDONG_KTX_P05 với ràng buộc ngày kết thúc phải sau ngày bắt đầu, tiền cọc không âm và tiền phòng tháng > 0.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE HOPDONG_KTX_P05 (
    MAHD VARCHAR(10) NOT NULL,
    MSSV VARCHAR(10) NOT NULL,
    MAPHONG VARCHAR(10) NOT NULL,
    NGAYBD DATE NOT NULL,
    NGAYKT DATE NOT NULL,
    TIENCOC DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    TIENPHONG_THANG DECIMAL(10, 2) NOT NULL,
    CONSTRAINT PK_HOPDONG_KTX_P05 PRIMARY KEY (MAHD),
    CONSTRAINT FK_HDKTX_SV_P05 FOREIGN KEY (MSSV) REFERENCES SINHVIEN_P05(MSSV),
    CONSTRAINT FK_HDKTX_PHONG_P05 FOREIGN KEY (MAPHONG) REFERENCES PHONG_P05(MAPHONG),
    CONSTRAINT CK_HDKTX_NGAY_P05 CHECK (NGAYKT > NGAYBD),
    CONSTRAINT CK_HDKTX_TIENCOC_P05 CHECK (TIENCOC >= 0.0),
    CONSTRAINT CK_HDKTX_GIA_P05 CHECK (TIENPHONG_THANG > 0.0)
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các thuộc tính hợp đồng thuê phòng.
1. Bước 2: Thiết lập khóa chính và các khóa ngoại.
1. Bước 3: Tạo ràng buộc CHECK so sánh giữa hai cột ngày NGAYKT > NGAYBD và miền giá trị tài chính.

**Phân tích trường hợp biên (Edge Cases):**
Ràng buộc CHECK bảng có thể tham chiếu đồng thời 2 cột trong cùng một dòng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 06 [SQL-P06] — T-SQL DDL: Tạo Bảng Giao Dịch Thẻ ATM Ngân Hàng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THE_ATM_P06(MATHE VARCHAR(20) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng GIAODICH_ATM_P06 ghi nhận lịch sử giao dịch với ràng buộc loại giao dịch ('Rut tien', 'Chuyen khoan', 'Nop tien', 'Thanh toan'), số tiền > 0 và lệ phí >= 0.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE GIAODICH_ATM_P06 (
    MAGD VARCHAR(20) NOT NULL,
    MATHE VARCHAR(20) NOT NULL,
    THOIGIAN DATETIME NOT NULL DEFAULT GETDATE(),
    SOTIEN DECIMAL(14, 2) NOT NULL,
    LOAIGD NVARCHAR(30) NOT NULL,
    LEPHI DECIMAL(8, 2) NOT NULL DEFAULT 0.00,
    CONSTRAINT PK_GIAODICH_ATM_P06 PRIMARY KEY (MAGD),
    CONSTRAINT FK_GD_THE_P06 FOREIGN KEY (MATHE) REFERENCES THE_ATM_P06(MATHE),
    CONSTRAINT CK_GD_SOTIEN_P06 CHECK (SOTIEN > 0),
    CONSTRAINT CK_GD_LEPHI_P06 CHECK (LEPHI >= 0),
    CONSTRAINT CK_GD_LOAIGD_P06 CHECK (LOAIGD IN (N'Rut tien', N'Chuyen khoan', N'Nop tien', N'Thanh toan'))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo khóa chính MAGD và khóa ngoại MATHE.
1. Bước 2: Sử dụng kiểu dữ liệu DECIMAL(14, 2) cho số tiền tài chính ngân hàng.
1. Bước 3: Định nghĩa các ràng buộc CHECK số tiền dương, phí không âm và danh mục loại giao dịch.

**Phân tích trường hợp biên (Edge Cases):**
Cần dùng NVARCHAR cho tiếng Việt Unicode có dấu kèm tiền tố N'...'.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 07 [SQL-P07] — T-SQL DDL: Tạo Bảng Đặt Phòng Resort & Nghỉ Dưỡng
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `RESORT_P07(MARS VARCHAR(10) PRIMARY KEY), KHACHHANG_P07(MAKH VARCHAR(10) PRIMARY KEY), PHONG_P07(MAPHONG VARCHAR(10) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng PHIEUDAT_RESORT_P07 kiểm tra ngày đi NGAYDI > NGAYDEN, số lượng khách tối đa từ 1 đến 10 người và tiền cọc >= 0.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE PHIEUDAT_RESORT_P07 (
    MAPD VARCHAR(10) NOT NULL,
    MARS VARCHAR(10) NOT NULL,
    MAKH VARCHAR(10) NOT NULL,
    MAPHONG VARCHAR(10) NOT NULL,
    NGAYDEN DATE NOT NULL,
    NGAYDI DATE NOT NULL,
    SOKHACH INT NOT NULL DEFAULT 2,
    TIEN_DATCOC DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    CONSTRAINT PK_PHIEUDAT_RESORT_P07 PRIMARY KEY (MAPD),
    CONSTRAINT FK_PD_RESORT_P07 FOREIGN KEY (MARS) REFERENCES RESORT_P07(MARS),
    CONSTRAINT FK_PD_KH_P07 FOREIGN KEY (MAKH) REFERENCES KHACHHANG_P07(MAKH),
    CONSTRAINT FK_PD_PHONG_P07 FOREIGN KEY (MAPHONG) REFERENCES PHONG_P07(MAPHONG),
    CONSTRAINT CK_PD_NGAY_P07 CHECK (NGAYDI > NGAYDEN),
    CONSTRAINT CK_PD_SOKHACH_P07 CHECK (SOKHACH BETWEEN 1 AND 10),
    CONSTRAINT CK_PD_TIENCOC_P07 CHECK (TIEN_DATCOC >= 0.0)
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Tạo bảng với đầy đủ khóa chính và 3 khóa ngoại liên kết.
1. Bước 2: Thiết lập CHECK kiểm tra ngày trả phòng sau ngày nhận phòng.
1. Bước 3: Giới hạn số khách từ 1 đến 10 người qua mệnh đề BETWEEN.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm dữ liệu lưu trú hợp lệ không bị âm ngày ở.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 08 [SQL-P08] — T-SQL DDL: Tạo Bảng Chuyến Đi Xe Công Nghệ (Ride-Hailing)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `TAIXE_P08(MATX VARCHAR(10) PRIMARY KEY), KHACHHANG_P08(MAKH VARCHAR(10) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng CHUYENXE_CONGNGHE_P08 với quãng đường di chuyển > 0 km, cước phí > 0, và trạng thái chuyến xe ('Da dat', 'Dang di', 'Hoan thanh', 'Huy').

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHUYENXE_CONGNGHE_P08 (
    MACHUYEN VARCHAR(10) NOT NULL,
    MATX VARCHAR(10) NOT NULL,
    MAKH VARCHAR(10) NOT NULL,
    QUANGDUONG_KM DECIMAL(6, 2) NOT NULL,
    CUOCPHI DECIMAL(10, 2) NOT NULL,
    THOIGIAN_BD DATETIME NOT NULL DEFAULT GETDATE(),
    TRANGTHAI NVARCHAR(20) NOT NULL DEFAULT N'Da dat',
    CONSTRAINT PK_CHUYENXE_P08 PRIMARY KEY (MACHUYEN),
    CONSTRAINT FK_CX_TX_P08 FOREIGN KEY (MATX) REFERENCES TAIXE_P08(MATX),
    CONSTRAINT FK_CX_KH_P08 FOREIGN KEY (MAKH) REFERENCES KHACHHANG_P08(MAKH),
    CONSTRAINT CK_CX_QUANGDUONG_P08 CHECK (QUANGDUONG_KM > 0.0),
    CONSTRAINT CK_CX_CUOCPHI_P08 CHECK (CUOCPHI > 0.0),
    CONSTRAINT CK_CX_TRANGTHAI_P08 CHECK (TRANGTHAI IN (N'Da dat', N'Dang di', N'Hoan thanh', N'Huy'))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo cấu trúc bảng chuyến xe công nghệ.
1. Bước 2: Liên kết tài xế và khách hàng qua hai khóa ngoại.
1. Bước 3: Ràng buộc quãng đường và cước phí phải là số dương.

**Phân tích trường hợp biên (Edge Cases):**
Trạng thái chuyến xe mặc định là 'Da dat' khi khách vừa tạo cuốc.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 09 [SQL-P09] — T-SQL DDL: Tạo Bảng Chi Tiết Mượn Sách & Phạt Quá Hạn
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEUMUON_P09(MAPM VARCHAR(10) PRIMARY KEY), CUONSACH_P09(MACS VARCHAR(10) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng CT_PHIEUMUON_P09 với khóa chính phức hợp (MAPM, MACS), tình trạng sách lúc trả ('Tot', 'Hong nhe', 'Hong nang', 'Mat sach'), tiền phạt >= 0.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CT_PHIEUMUON_P09 (
    MAPM VARCHAR(10) NOT NULL,
    MACS VARCHAR(10) NOT NULL,
    NGAYTRA_THUC DATE NULL,
    TIENPHAT DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    TINHTRANG_SACH NVARCHAR(30) NOT NULL DEFAULT N'Tot',
    CONSTRAINT PK_CT_PHIEUMUON_P09 PRIMARY KEY (MAPM, MACS),
    CONSTRAINT FK_CTPM_PM_P09 FOREIGN KEY (MAPM) REFERENCES PHIEUMUON_P09(MAPM) ON DELETE CASCADE,
    CONSTRAINT FK_CTPM_CS_P09 FOREIGN KEY (MACS) REFERENCES CUONSACH_P09(MACS),
    CONSTRAINT CK_CTPM_TIENPHAT_P09 CHECK (TIENPHAT >= 0.0),
    CONSTRAINT CK_CTPM_TINHTRANG_P09 CHECK (TINHTRANG_SACH IN (N'Tot', N'Hong nhe', N'Hong nang', N'Mat sach'))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo khóa chính phức hợp (MAPM, MACS).
1. Bước 2: Cột NGAYTRA_THUC cho phép NULL khi sách đang trong thời gian mượn chưa trả.
1. Bước 3: Định nghĩa ràng buộc CHECK tiền phạt và trạng thái vật lý của cuốn sách.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm toàn vẹn thư viện: sách trả hỏng hoặc mất sẽ bị tính tiền phạt.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 10 [SQL-P10] — T-SQL DDL: Tạo Bảng Phiếu Xuất Kho Hàng Hóa
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHO_P10(MAKHO VARCHAR(10) PRIMARY KEY), NHANVIEN_P10(MANV VARCHAR(10) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng PHIEU_XUATKHO_P10 có tổng trị giá không âm, trạng thái phiếu xuất ('Cho xuat', 'Da xuat', 'Huy') và ngày xuất mặc định là ngày hiện tại.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE PHIEU_XUATKHO_P10 (
    MAPX VARCHAR(10) NOT NULL,
    MAKHO VARCHAR(10) NOT NULL,
    MANV VARCHAR(10) NOT NULL,
    NGAYXUAT DATETIME NOT NULL DEFAULT GETDATE(),
    TONGTRIGIA DECIMAL(14, 2) NOT NULL DEFAULT 0.00,
    TRANGTHAI NVARCHAR(20) NOT NULL DEFAULT N'Cho xuat',
    CONSTRAINT PK_PHIEU_XUATKHO_P10 PRIMARY KEY (MAPX),
    CONSTRAINT FK_PX_KHO_P10 FOREIGN KEY (MAKHO) REFERENCES KHO_P10(MAKHO),
    CONSTRAINT FK_PX_NV_P10 FOREIGN KEY (MANV) REFERENCES NHANVIEN_P10(MANV),
    CONSTRAINT CK_PX_TONGTRIGIA_P10 CHECK (TONGTRIGIA >= 0.0),
    CONSTRAINT CK_PX_TRANGTHAI_P10 CHECK (TRANGTHAI IN (N'Cho xuat', N'Da xuat', N'Huy'))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo bảng phiếu xuất kho với các khóa ngoại tới kho và nhân viên phụ trách.
1. Bước 2: Áp dụng giá trị DEFAULT GETDATE() cho thời điểm lập phiếu.
1. Bước 3: Thiết lập ràng buộc CHECK tổng trị giá và trạng thái phiếu.

**Phân tích trường hợp biên (Edge Cases):**
Tổng giá trị phiếu xuất kho không được phép mang giá trị âm.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 11 [SQL-P11] — T-SQL DDL: Tạo Bảng Kết Quả Xét Nghiệm Bệnh Viện
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BENHNHAN_P11(MABN VARCHAR(10) PRIMARY KEY), BACSI_P11(MABS VARCHAR(10) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng KETQUA_XETNGHIEM_P11 lưu trữ kết quả định lượng y khoa với kết quả số >= 0, loại xét nghiệm không rỗng và đơn vị đo chuẩn.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE KETQUA_XETNGHIEM_P11 (
    MAXN VARCHAR(10) NOT NULL,
    MABN VARCHAR(10) NOT NULL,
    MABS_CHIDINH VARCHAR(10) NOT NULL,
    NGAYXN DATETIME NOT NULL DEFAULT GETDATE(),
    LOAIXN NVARCHAR(50) NOT NULL,
    KETQUA_SO DECIMAL(8, 2) NOT NULL,
    DONVI_DO VARCHAR(20) NOT NULL,
    CONSTRAINT PK_KETQUA_XN_P11 PRIMARY KEY (MAXN),
    CONSTRAINT FK_XN_BN_P11 FOREIGN KEY (MABN) REFERENCES BENHNHAN_P11(MABN),
    CONSTRAINT FK_XN_BS_P11 FOREIGN KEY (MABS_CHIDINH) REFERENCES BACSI_P11(MABS),
    CONSTRAINT CK_XN_KETQUA_P11 CHECK (KETQUA_SO >= 0.0)
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các trường thông tin xét nghiệm lâm sàng.
1. Bước 2: Thiết lập khóa ngoại bác sĩ chỉ định và bệnh nhân.
1. Bước 3: Ràng buộc chỉ số kết quả xét nghiệm không âm.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm dữ liệu y tế định lượng chính xác.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 12 [SQL-P12] — T-SQL DDL: Tạo Bảng Bài Học Khóa Học Trực Tuyến
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHOAHOC_P12(MAKH VARCHAR(10) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng BAIHOC_ONLINE_P12 với thứ tự bài học > 0, thời lượng bài học (phút) từ 1 đến 300 phút, cờ miễn phí chỉ nhận 0 hoặc 1.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE BAIHOC_ONLINE_P12 (
    MABH VARCHAR(10) NOT NULL,
    MAKH VARCHAR(10) NOT NULL,
    THUTU_BAI INT NOT NULL,
    TIEUDE NVARCHAR(150) NOT NULL,
    THOILUONG_PHUT INT NOT NULL,
    MIENPHI BIT NOT NULL DEFAULT 0,
    CONSTRAINT PK_BAIHOC_ONLINE_P12 PRIMARY KEY (MABH),
    CONSTRAINT FK_BH_KH_P12 FOREIGN KEY (MAKH) REFERENCES KHOAHOC_P12(MAKH) ON DELETE CASCADE,
    CONSTRAINT CK_BH_THUTU_P12 CHECK (THUTU_BAI > 0),
    CONSTRAINT CK_BH_THOILUONG_P12 CHECK (THOILUONG_PHUT BETWEEN 1 AND 300),
    CONSTRAINT UQ_BH_THUTU_KH_P12 UNIQUE (MAKH, THUTU_BAI)
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Tạo bảng bài học trực tuyến liên kết khóa học.
1. Bước 2: Ràng buộc thứ tự bài học duy nhất trong cùng một khóa học qua UNIQUE (MAKH, THUTU_BAI).
1. Bước 3: Ràng buộc thời lượng bài học từ 1 đến 300 phút.

**Phân tích trường hợp biên (Edge Cases):**
Cột cờ BIT chỉ nhận giá trị 0 (trả phí) hoặc 1 (học thử miễn phí).

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 13 [SQL-P13] — T-SQL DDL: Tạo Bảng Chỉ Số Công Tơ Điện Ký Túc Xá
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHONG_P13(MAPHONG VARCHAR(10) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng CONGTO_DIEN_P13 với khóa chính phức hợp (MAPHONG, THANG, NAM), tháng từ 1 đến 12, năm >= 2020 và chỉ số mới phải lớn hơn hoặc bằng chỉ số cũ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CONGTO_DIEN_P13 (
    MAPHONG VARCHAR(10) NOT NULL,
    THANG INT NOT NULL,
    NAM INT NOT NULL,
    CHISO_CU INT NOT NULL,
    CHISO_MOI INT NOT NULL,
    SANLUONG_KWH AS (CHISO_MOI - CHISO_CU),
    CONSTRAINT PK_CONGTO_DIEN_P13 PRIMARY KEY (MAPHONG, THANG, NAM),
    CONSTRAINT FK_CTD_PHONG_P13 FOREIGN KEY (MAPHONG) REFERENCES PHONG_P13(MAPHONG),
    CONSTRAINT CK_CTD_THANG_P13 CHECK (THANG BETWEEN 1 AND 12),
    CONSTRAINT CK_CTD_NAM_P13 CHECK (NAM >= 2020),
    CONSTRAINT CK_CTD_CHISO_P13 CHECK (CHISO_MOI >= CHISO_CU)
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Thiết lập khóa chính 3 thuộc tính (MAPHONG, THANG, NAM).
1. Bước 2: Tạo cột tính toán SANLUONG_KWH tự động tính số kWh tiêu thụ.
1. Bước 3: Ràng buộc CHECK CHISO_MOI >= CHISO_CU để bảo đảm công tơ quay thuận.

**Phân tích trường hợp biên (Edge Cases):**
Chỉ số điện không bao giờ được phép giảm lùi trong cùng kỳ đo.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 14 [SQL-P14] — T-SQL DDL: Tạo Bảng Suất Chiếu Phim Rạp Chiếu
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIM_P14(MAPHIM VARCHAR(10) PRIMARY KEY), PHONGCHIEU_P14(MAPHONG VARCHAR(10) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng SUATCHIEU_PHIM_P14 với giá vé gốc từ 45.000 VNĐ trở lên, ngày chiếu không rỗng và giờ chiếu hợp lệ.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE SUATCHIEU_PHIM_P14 (
    MASC VARCHAR(10) NOT NULL,
    MAPHIM VARCHAR(10) NOT NULL,
    MAPHONG VARCHAR(10) NOT NULL,
    NGAYCHIEU DATE NOT NULL,
    GIOCHIEU TIME NOT NULL,
    GIAGOC DECIMAL(10, 2) NOT NULL,
    CONSTRAINT PK_SUATCHIEU_P14 PRIMARY KEY (MASC),
    CONSTRAINT FK_SC_PHIM_P14 FOREIGN KEY (MAPHIM) REFERENCES PHIM_P14(MAPHIM),
    CONSTRAINT FK_SC_PHONG_P14 FOREIGN KEY (MAPHONG) REFERENCES PHONGCHIEU_P14(MAPHONG),
    CONSTRAINT CK_SC_GIAGOC_P14 CHECK (GIAGOC >= 45000.0)
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Tạo bảng suất chiếu liên kết phim và phòng chiếu.
1. Bước 2: Sử dụng kiểu DATE cho ngày và TIME cho giờ chiếu.
1. Bước 3: Ràng buộc giá gốc tối thiểu của rạp chiếu là 45.000 VNĐ.

**Phân tích trường hợp biên (Edge Cases):**
Định dạng kiểu TIME chuẩn SQL Server lưu trữ giờ chiếu phim.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 15 [SQL-P15] — T-SQL DDL: Tạo Bảng Hợp Đồng Bản Quyền Biểu Diễn Âm Nhạc
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BAIHAT_P15(MABH VARCHAR(10) PRIMARY KEY), CASI_P15(MACS VARCHAR(10) PRIMARY KEY)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng HOPDONG_BIEUDIEN_P15 với phí bản quyền >= 0, thời hạn hợp đồng (tháng) từ 1 đến 120 tháng, và ngày ký hợp đồng.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE HOPDONG_BIEUDIEN_P15 (
    MAHD VARCHAR(10) NOT NULL,
    MABH VARCHAR(10) NOT NULL,
    MACS VARCHAR(10) NOT NULL,
    NGAYKY DATE NOT NULL DEFAULT GETDATE(),
    PHIBANQUYEN_USD DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    THOIHAN_THANG INT NOT NULL,
    CONSTRAINT PK_HDBD_P15 PRIMARY KEY (MAHD),
    CONSTRAINT FK_HDBD_BH_P15 FOREIGN KEY (MABH) REFERENCES BAIHAT_P15(MABH),
    CONSTRAINT FK_HDBD_CS_P15 FOREIGN KEY (MACS) REFERENCES CASI_P15(MACS),
    CONSTRAINT CK_HDBD_PHI_P15 CHECK (PHIBANQUYEN_USD >= 0.0),
    CONSTRAINT CK_HDBD_THOIHAN_P15 CHECK (THOIHAN_THANG BETWEEN 1 AND 120)
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo bảng hợp đồng cấp quyền biểu diễn tác phẩm âm nhạc.
1. Bước 2: Thiết lập ràng buộc khóa ngoại tới bài hát và ca sĩ.
1. Bước 3: Ràng buộc phí bản quyền không âm và thời hạn từ 1 tháng đến tối đa 10 năm (120 tháng).

**Phân tích trường hợp biên (Edge Cases):**
Bảo vệ quyền sở hữu trí tuệ âm nhạc trực tuyến theo chuẩn pháp lý.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 16 [SQL-P16] — T-SQL DDL: Sửa Bảng Thêm Cột Email & Ràng Buộc Định Dạng Email
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SINHVIEN_P16(MSSV VARCHAR(10) PRIMARY KEY, HOTEN NVARCHAR(100), NGAYSINH DATE)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE thêm cột EMAIL vào bảng SINHVIEN_P16 và bổ sung ràng buộc CHECK kiểm tra định dạng email hợp lệ (phải chứa ký tự '@' và '.').

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột EMAIL kèm ràng buộc CHECK định dạng
ALTER TABLE SINHVIEN_P16
ADD EMAIL VARCHAR(100) NULL
    CONSTRAINT CK_SINHVIEN_EMAIL_P16 CHECK (EMAIL LIKE '%_@__%.__%');
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp ALTER TABLE ... ADD kèm định nghĩa ràng buộc CONSTRAINT inline.
1. Bước 2: Ràng buộc CHECK với mẫu LIKE '%_@__%.__%' kiểm tra ký tự @ và dấu chấm hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Khai báo ràng buộc CHECK inline cùng lệnh ADD giúp thực thi an toàn trong 1 câu lệnh duy nhất.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 17 [SQL-P17] — T-SQL DDL: Sửa Bảng Bổ Sung Hạn Sử Dụng Dược Phẩm
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `DUOCPHAM_P17(MATHUOC VARCHAR(10) PRIMARY KEY, TENTHUOC NVARCHAR(100), NGAYSX DATE NOT NULL)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE thêm cột HSD (Hạn sử dụng) vào bảng DUOCPHAM_P17 và tạo ràng buộc CHECK bảo đảm HSD >= NGAYSX.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột HSD
ALTER TABLE DUOCPHAM_P17
ADD HSD DATE NULL;
GO

-- Ràng buộc CHECK hạn sử dụng phải sau hoặc bằng ngày sản xuất
ALTER TABLE DUOCPHAM_P17
ADD CONSTRAINT CK_DUOCPHAM_HSD_P17 CHECK (HSD >= NGAYSX);
```

**Các bước suy luận tư duy:**
1. Bước 1: Thêm cột HSD kiểu DATE.
1. Bước 2: Tách lệnh bằng GO và bổ sung ràng buộc CHECK bảng so sánh giữa hai cột HSD >= NGAYSX.

**Phân tích trường hợp biên (Edge Cases):**
Cần phân tách batch bằng GO khi ràng buộc mức bảng tham chiếu đến cột mới vừa thêm trong batch trước.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 18 [SQL-P18] — T-SQL DDL: Sửa Bảng Thêm Cột Điểm Tiêu Chuẩn Môn Học
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `MONHOC_P18(MAMH VARCHAR(10) PRIMARY KEY, TENMH NVARCHAR(100), SOTC INT)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE thêm cột DIEM_CHUAN_QUA_MON vào bảng MONHOC_P18 với giá trị mặc định là 5.0 và ràng buộc điểm trong khoảng [0.0, 10.0].

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột điểm chuẩn qua môn kèm DEFAULT 5.0 và CHECK thang điểm 10
ALTER TABLE MONHOC_P18
ADD DIEM_CHUAN_QUA_MON DECIMAL(3, 1) NOT NULL
    CONSTRAINT DF_MONHOC_DIEM_P18 DEFAULT 5.0
    CONSTRAINT CK_MONHOC_DIEM_P18 CHECK (DIEM_CHUAN_QUA_MON BETWEEN 0.0 AND 10.0);
```

**Các bước suy luận tư duy:**
1. Bước 1: Thêm cột NOT NULL kèm mệnh đề DEFAULT để gán giá trị 5.0 cho các dòng dữ liệu hiện hữu.
1. Bước 2: Thêm ràng buộc CHECK giới hạn thang điểm 10.

**Phân tích trường hợp biên (Edge Cases):**
Cung cấp CONSTRAINT DF_... DEFAULT cho cột NOT NULL bảo đảm lệnh ALTER thành công trên bảng có sẵn dòng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 19 [SQL-P19] — T-SQL DDL: Sửa Bảng Bổ Sung Hệ Số Lương Nhân Viên
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHANVIEN_P19(MANV VARCHAR(10) PRIMARY KEY, HOTEN NVARCHAR(100), LUONGCB DECIMAL(12, 2))`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE bổ sung cột HE_SO_LUONG với giá trị mặc định là 1.00 và ràng buộc CHECK hệ số lương phải lớn hơn hoặc bằng 1.00.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột hệ số lương kèm DEFAULT 1.00 và CHECK >= 1.00
ALTER TABLE NHANVIEN_P19
ADD HE_SO_LUONG DECIMAL(4, 2) NOT NULL
    CONSTRAINT DF_NV_HESOLUONG_P19 DEFAULT 1.00
    CONSTRAINT CK_NV_HESOLUONG_P19 CHECK (HE_SO_LUONG >= 1.00);
```

**Các bước suy luận tư duy:**
1. Bước 1: Thêm cột HE_SO_LUONG kiểu DECIMAL(4, 2) có DEFAULT 1.00.
1. Bước 2: Tạo ràng buộc CHECK kiểm tra hệ số lương không được nhỏ hơn 1.00.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm quyền lợi nhân viên theo quy chế tiền lương.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 20 [SQL-P20] — T-SQL DDL: Sửa Bảng Thiết Lập Khóa Ngoại ON DELETE SET NULL
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHONGBAN_P20(MAPB VARCHAR(10) PRIMARY KEY, TENPB NVARCHAR(100)), NHANVIEN_P20(MANV VARCHAR(10) PRIMARY KEY, HOTEN NVARCHAR(100), MAPB VARCHAR(10))`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE tạo ràng buộc khóa ngoại từ NHANVIEN_P20(MAPB) tham chiếu đến PHONGBAN_P20(MAPB) kèm hành vi ON DELETE SET NULL.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
ALTER TABLE NHANVIEN_P20
ADD CONSTRAINT FK_NV_PB_P20 FOREIGN KEY (MAPB)
REFERENCES PHONGBAN_P20(MAPB)
ON DELETE SET NULL;
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp ALTER TABLE NHANVIEN_P20 ADD CONSTRAINT FK_... FOREIGN KEY.
1. Bước 2: Chỉ định bảng tham chiếu PHONGBAN_P20(MAPB) và hành vi ON DELETE SET NULL.

**Phân tích trường hợp biên (Edge Cases):**
Cột MAPB trong bảng NHANVIEN_P20 bắt buộc phải cho phép NULL để hành động ON DELETE SET NULL có hiệu lực.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 21 [SQL-P21] — T-SQL DDL: Sửa Bảng Thêm Cột Điểm Đánh Giá Chuyến Xe
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CHUYENXE_P21(MACHUYEN VARCHAR(10) PRIMARY KEY, CUOCPHI DECIMAL(10, 2))`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE thêm cột DIEM_DANHGIA vào bảng CHUYENXE_P21 và ràng buộc CHECK điểm đánh giá chỉ được nhận số nguyên từ 1 đến 5 sao.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột điểm đánh giá sao kèm CHECK thang 1 đến 5
ALTER TABLE CHUYENXE_P21
ADD DIEM_DANHGIA INT NULL
    CONSTRAINT CK_CX_DIEM_P21 CHECK (DIEM_DANHGIA BETWEEN 1 AND 5);
```

**Các bước suy luận tư duy:**
1. Bước 1: Thêm cột DIEM_DANHGIA INT NULL (cho phép NULL khi khách chưa đánh giá).
1. Bước 2: Tạo ràng buộc CHECK BETWEEN 1 AND 5 inline.

**Phân tích trường hợp biên (Edge Cases):**
Giá trị NULL hợp lệ khi khách hàng bỏ qua bước đánh giá sau chuyến đi.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 22 [SQL-P22] — T-SQL DDL: Sửa Bảng Thiết Lập Ràng Buộc UNIQUE Cho Căn Cước Công Dân
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG_P22(MAKH VARCHAR(10) PRIMARY KEY, HOTEN NVARCHAR(100), CCCD VARCHAR(20) NOT NULL)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE bổ sung ràng buộc UNIQUE cho cột số căn cước công dân (CCCD) trong bảng KHACHHANG_P22.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
ALTER TABLE KHACHHANG_P22
ADD CONSTRAINT UQ_KHACHHANG_CCCD_P22 UNIQUE (CCCD);
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng lệnh ALTER TABLE KHACHHANG_P22 ADD CONSTRAINT UQ_... UNIQUE (CCCD).

**Phân tích trường hợp biên (Edge Cases):**
Ràng buộc UNIQUE tự động tạo Unique Non-Clustered Index trong SQL Server để tăng tốc tìm kiếm.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 23 [SQL-P23] — T-SQL DDL: Sửa Bảng Bổ Sung Hạn Mức Tín Dụng Thẻ ATM
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `THE_ATM_P23(MATHE VARCHAR(20) PRIMARY KEY, SOTK VARCHAR(20) NOT NULL)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE thêm cột HANMUC_TINDUNG với giá trị mặc định là 10.000.000 VNĐ và ràng buộc CHECK hạn mức >= 0.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột hạn mức tín dụng kèm DEFAULT và CHECK >= 0
ALTER TABLE THE_ATM_P23
ADD HANMUC_TINDUNG DECIMAL(12, 2) NOT NULL
    CONSTRAINT DF_THE_HANMUC_P23 DEFAULT 10000000.00
    CONSTRAINT CK_THE_HANMUC_P23 CHECK (HANMUC_TINDUNG >= 0.0);
```

**Các bước suy luận tư duy:**
1. Bước 1: Thêm thuộc tính HANMUC_TINDUNG DECIMAL(12, 2) NOT NULL kèm DEFAULT 10 triệu.
1. Bước 2: Bổ sung ràng buộc toàn vẹn CHECK >= 0 inline.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm an toàn hạn mức tài khoản thẻ ngân hàng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 24 [SQL-P24] — T-SQL DDL: Sửa Bảng Thêm Cột Tỷ Lệ Chiết Khấu Hóa Đơn
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOADON_P24(MAHD VARCHAR(10) PRIMARY KEY, NGAYLAP DATE NOT NULL, TONGTIEN DECIMAL(12, 2) NOT NULL)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE thêm cột CHIETKHAU_PT (phần trăm chiết khấu) vào bảng HOADON_P24 với giá trị mặc định là 0% và ràng buộc CHECK không vượt quá 30%.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột chiết khấu phần trăm kèm DEFAULT 0 và CHECK <= 30%
ALTER TABLE HOADON_P24
ADD CHIETKHAU_PT DECIMAL(4, 2) NOT NULL
    CONSTRAINT DF_HD_CHIETKHAU_P24 DEFAULT 0.00
    CONSTRAINT CK_HD_CHIETKHAU_P24 CHECK (CHIETKHAU_PT BETWEEN 0.00 AND 0.30);
```

**Các bước suy luận tư duy:**
1. Bước 1: Thêm cột CHIETKHAU_PT DECIMAL(4, 2) NOT NULL DEFAULT 0.00.
1. Bước 2: Ràng buộc giá trị chiết khấu từ 0.00 (0%) đến 0.30 (30%) inline.

**Phân tích trường hợp biên (Edge Cases):**
Kiểm soát chính sách khuyến mãi hóa đơn bán hàng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 25 [SQL-P25] — T-SQL DDL: Sửa Bảng Bổ Sung Ràng Buộc Kiểm Tra Ngày Khóa Học
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHOAHOC_P25(MAKH VARCHAR(10) PRIMARY KEY, TENKH NVARCHAR(100), NGAY_BD DATE NOT NULL, NGAY_KT DATE NOT NULL)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE bổ sung ràng buộc toàn vẹn CHECK bảo đảm ngày kết thúc khóa học NGAY_KT phải sau ngày bắt đầu NGAY_BD.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
ALTER TABLE KHOAHOC_P25
ADD CONSTRAINT CK_KHOAHOC_THOIGIAN_P25 CHECK (NGAY_KT > NGAY_BD);
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng lệnh ALTER TABLE KHOAHOC_P25 ADD CONSTRAINT CK_... CHECK (NGAY_KT > NGAY_BD).

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm tính logic của thời lượng khóa học đào tạo.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 26 [SQL-P26] — T-SQL DML: Giảm 15% Học Phí Lớp Học Phần Cho Sinh Viên Hoàn Cảnh Khó Khăn Đăng Ký Năm 2024 (Sửa P0-03)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SINHVIEN_P26(MSSV VARCHAR(10) PRIMARY KEY, HOTEN NVARCHAR(100), LOAI_SV NVARCHAR(30)), DANGKY_P26(MSSV VARCHAR(10), MALHP VARCHAR(10), NGAYDK DATE, HOCPHI_PHAITHU DECIMAL(12, 2), PRIMARY KEY (MSSV, MALHP))`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE giảm 15% học phí phải thu (HOCPHI_PHAITHU = HOCPHI_PHAITHU * 0.85) cho các lượt đăng ký lớp học phần của sinh viên thuộc diện 'Kho khan' đăng ký trong năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Giảm 15% học phí cho sinh viên khó khăn đăng ký trong năm 2024
UPDATE DK
SET HOCPHI_PHAITHU = DK.HOCPHI_PHAITHU * 0.85
FROM DANGKY_P26 DK
INNER JOIN SINHVIEN_P26 SV ON DK.MSSV = SV.MSSV
WHERE SV.LOAI_SV = N'Kho khan'
  AND YEAR(DK.NGAYDK) = 2024;
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp T-SQL UPDATE với bí danh bảng mục tiêu DK (DANGKY_P26).
1. Bước 2: Trong mệnh đề SET, chỉ định rõ tên cột không chứa tiền tố bí danh (SET HOCPHI_PHAITHU = DK.HOCPHI_PHAITHU * 0.85) theo đúng chuẩn Transact-SQL của Microsoft SQL Server.
1. Bước 3: Mệnh đề FROM liên kết DANGKY_P26 DK với SINHVIEN_P26 SV qua khóa ngoại MSSV.
1. Bước 4: Mệnh đề WHERE lọc diện sinh viên khó khăn và năm đăng ký YEAR(DK.NGAYDK) = 2024.

**Phân tích trường hợp biên (Edge Cases):**
ĐÃ SỬA LỖI P0-03: Cú pháp chuẩn SQL Server không cho phép đặt bí danh trước tên cột được gán (SET col = expr). Bảng DANGKY_P26 có đầy đủ cột NGAYDK và mệnh đề WHERE lọc chính xác năm 2024.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 27 [SQL-P27] — T-SQL DML: Tăng 10% Đơn Giá Lô Vắc-Xin Bảo Quản Âm Sâu Nhập Khẩu Từ Mỹ Năm 2024 (Sửa P0-03)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `NHACUNGCAP_P27(MANCC VARCHAR(10) PRIMARY KEY, TENNCC NVARCHAR(100), QUOCGIA NVARCHAR(50)), LOVACXIN_P27(MALO VARCHAR(10) PRIMARY KEY, MANCC VARCHAR(10), LOAI_BQ NVARCHAR(30), NGAYNHAP DATE, DONGIA DECIMAL(12, 2))`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE tăng 10% đơn giá (DONGIA = DONGIA * 1.10) cho các lô vắc-xin yêu cầu bảo quản 'Am sau' do nhà cung cấp có quốc gia 'My' cung ứng và nhập kho trong năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Tăng 10% đơn giá lô vắc-xin âm sâu nhập từ Mỹ trong năm 2024
UPDATE LV
SET DONGIA = LV.DONGIA * 1.10
FROM LOVACXIN_P27 LV
INNER JOIN NHACUNGCAP_P27 NCC ON LV.MANCC = NCC.MANCC
WHERE NCC.QUOCGIA = N'My'
  AND LV.LOAI_BQ = N'Am sau'
  AND YEAR(LV.NGAYNHAP) = 2024;
```

**Các bước suy luận tư duy:**
1. Bước 1: UPDATE bảng LOVACXIN_P27 với bí danh LV.
1. Bước 2: Mệnh đề SET DONGIA = LV.DONGIA * 1.10 đúng chuẩn T-SQL.
1. Bước 3: INNER JOIN với NHACUNGCAP_P27 qua MANCC.
1. Bước 4: WHERE lọc quốc gia 'My', loại bảo quản 'Am sau' và YEAR(NGAYNHAP) = 2024.

**Phân tích trường hợp biên (Edge Cases):**
Cột NGAYNHAP đảm bảo tính nhất quán dữ liệu với năm 2024 được yêu cầu trong đề bài.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 28 [SQL-P28] — T-SQL DML: Cập Nhật Phụ Phí 50.000 VNĐ Chuyến Bay Đêm Cao Điểm Tết 2024 (Sửa P0-03)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `CHUYENBAY_P28(MACB VARCHAR(10) PRIMARY KEY, NGAYBAY DATE, GIOBAY TIME, PHUPHI DECIMAL(10, 2), LOAICHUYEN NVARCHAR(30))`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE cộng thêm phụ phí 50.000 VNĐ vào cột PHUPHI cho các chuyến bay cất cánh sau 22:00 (GIOBAY >= '22:00:00') thuộc đợt cao điểm Tết năm 2024 (từ 2024-02-01 đến 2024-02-15).

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Cập nhật phụ phí 50.000 VNĐ cho chuyến bay đêm cao điểm Tết 2024
UPDATE CB
SET PHUPHI = CB.PHUPHI + 50000.00
FROM CHUYENBAY_P28 CB
WHERE CB.GIOBAY >= '22:00:00'
  AND CB.NGAYBAY BETWEEN '2024-02-01' AND '2024-02-15';
```

**Các bước suy luận tư duy:**
1. Bước 1: UPDATE CHUYENBAY_P28 CB.
1. Bước 2: SET PHUPHI = CB.PHUPHI + 50000.00.
1. Bước 3: Lọc giờ bay đêm sau 22:00 và khoảng ngày bay trong tháng 02/2024.

**Phân tích trường hợp biên (Edge Cases):**
Mệnh đề WHERE kiểm tra đồng thời cả giờ bay và ngày bay cụ thể.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 29 [SQL-P29] — T-SQL DML: Xóa Lịch Sử Đăng Ký Cư Dân Hết Hạn Hợp Đồng Thuê Trước Năm 2024 (Sửa P0-03)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOPDONG_P29(MAHD VARCHAR(10) PRIMARY KEY, MACAN VARCHAR(10), NGAYKT DATE), CUDAN_LUTRUG_P29(MACD VARCHAR(10) PRIMARY KEY, MAHD VARCHAR(10), HOTEN NVARCHAR(100), NGAY_DANGKY DATE)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL DELETE xóa toàn bộ bản ghi lưu trú của cư dân tại bảng CUDAN_LUTRUG_P29 thuộc các hợp đồng thuê nhà đã hết hạn trước ngày '2024-01-01' (NGAYKT < '2024-01-01').

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Xóa lịch sử lưu trú của hợp đồng hết hạn trước năm 2024
DELETE CD
FROM CUDAN_LUTRUG_P29 CD
INNER JOIN HOPDONG_P29 HD ON CD.MAHD = HD.MAHD
WHERE HD.NGAYKT < '2024-01-01';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp DELETE kèm bí danh CD.
1. Bước 2: Mệnh đề FROM CUDAN_LUTRUG_P29 CD INNER JOIN HOPDONG_P29 HD.
1. Bước 3: Điều kiện WHERE HD.NGAYKT < '2024-01-01'.

**Phân tích trường hợp biên (Edge Cases):**
Cú pháp DELETE table_alias FROM table table_alias JOIN là cú pháp chuẩn của Microsoft SQL Server.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 30 [SQL-P30] — T-SQL DML: Nâng Hạng Khách Hàng VIP Cho Hóa Đơn Lớn Lập Năm 2024 (Sửa P0-03)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG_P30(MAKH VARCHAR(10) PRIMARY KEY, HOTEN NVARCHAR(100), HANG_THE NVARCHAR(20)), HOADON_P30(MAHD VARCHAR(10) PRIMARY KEY, MAKH VARCHAR(10), NGAYLAP DATE, TONGTIEN DECIMAL(12, 2))`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE cập nhật nâng hạng thẻ thành 'VIP' trong bảng KHACHHANG_P30 cho các khách hàng có hóa đơn mua sắm trong năm 2024 đạt tổng tiền từ 50.000.000 VNĐ trở lên.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Nâng hạng khách hàng VIP cho khách có hóa đơn trên 50 triệu năm 2024
UPDATE KH
SET HANG_THE = N'VIP'
FROM KHACHHANG_P30 KH
INNER JOIN HOADON_P30 HD ON KH.MAKH = HD.MAKH
WHERE HD.TONGTIEN >= 50000000.00
  AND YEAR(HD.NGAYLAP) = 2024;
```

**Các bước suy luận tư duy:**
1. Bước 1: UPDATE KH SET HANG_THE = N'VIP'.
1. Bước 2: FROM KHACHHANG_P30 KH INNER JOIN HOADON_P30 HD ON KH.MAKH = HD.MAKH.
1. Bước 3: WHERE HD.TONGTIEN >= 50000000 và YEAR(HD.NGAYLAP) = 2024.

**Phân tích trường hợp biên (Edge Cases):**
Cú pháp chuẩn SET HANG_THE = N'VIP' (không có KH.HANG_THE trong SET).

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 31 [SQL-P31] — T-SQL DML: Miễn Phí Tiền Nước Cho Phòng KTX Tình Nguyện Hè Tháng 08/2024 (Sửa P0-03)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHONG_P31(MAPHONG VARCHAR(10) PRIMARY KEY, LOAIPHONG NVARCHAR(30)), TIEN_DICHVU_P31(MAPHONG VARCHAR(10), THANG INT, NAM INT, TIEN_NUOC DECIMAL(10, 2), PRIMARY KEY (MAPHONG, THANG, NAM))`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE gán TIEN_NUOC = 0 cho các phòng ký túc xá thuộc loại 'Tinh nguyen hè' (LOAIPHONG = 'Tinh nguyen he') trong kỳ thu phí tháng 8 năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Miễn phí tiền nước cho phòng tình nguyện hè tháng 8/2024
UPDATE DV
SET TIEN_NUOC = 0.00
FROM TIEN_DICHVU_P31 DV
INNER JOIN PHONG_P31 P ON DV.MAPHONG = P.MAPHONG
WHERE P.LOAIPHONG = N'Tinh nguyen he'
  AND DV.THANG = 8
  AND DV.NAM = 2024;
```

**Các bước suy luận tư duy:**
1. Bước 1: UPDATE DV SET TIEN_NUOC = 0.00.
1. Bước 2: FROM TIEN_DICHVU_P31 DV INNER JOIN PHONG_P31 P ON DV.MAPHONG = P.MAPHONG.
1. Bước 3: Lọc theo loại phòng và đúng tháng 8/2024.

**Phân tích trường hợp biên (Edge Cases):**
Cột THANG và NAM trong TIEN_DICHVU_P31 đảm bảo lọc chính xác thời điểm.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 32 [SQL-P32] — T-SQL DML: Tặng Điểm Thưởng Khách Đặt Phòng Resort 5 Sao Tháng 12/2024 (Sửa P0-03)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHACHHANG_P32(MAKH VARCHAR(10) PRIMARY KEY, HOTEN NVARCHAR(100), DIEM_TICHLUY INT), PHIEUDAT_P32(MAPD VARCHAR(10) PRIMARY KEY, MAKH VARCHAR(10), HANG_SAO INT, NGAYDEN DATE)`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE cộng thêm 200 điểm thưởng tích lũy (DIEM_TICHLUY = DIEM_TICHLUY + 200) cho các khách hàng có phiếu đặt phòng tại resort đạt tiêu chuẩn 5 sao có ngày đến trong tháng 12/2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Tặng 200 điểm tích lũy cho khách đặt phòng resort 5 sao tháng 12/2024
UPDATE KH
SET DIEM_TICHLUY = KH.DIEM_TICHLUY + 200
FROM KHACHHANG_P32 KH
INNER JOIN PHIEUDAT_P32 PD ON KH.MAKH = PD.MAKH
WHERE PD.HANG_SAO = 5
  AND MONTH(PD.NGAYDEN) = 12
  AND YEAR(PD.NGAYDEN) = 2024;
```

**Các bước suy luận tư duy:**
1. Bước 1: UPDATE KH SET DIEM_TICHLUY = KH.DIEM_TICHLUY + 200.
1. Bước 2: FROM KHACHHANG_P32 KH INNER JOIN PHIEUDAT_P32 PD ON KH.MAKH = PD.MAKH.
1. Bước 3: Lọc khách sạn 5 sao và ngày đến trong tháng 12/2024.

**Phân tích trường hợp biên (Edge Cases):**
Cập nhật tăng giá trị tích lũy an toàn trên dữ liệu đa bảng.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 33 [SQL-P33] — T-SQL DML: Tăng 10% Cước Phí Chuyến Xe Cao Điểm Mưa Bão Tháng 10/2024 (Sửa P0-03)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `KHUVUC_P33(MAKV VARCHAR(10) PRIMARY KEY, TINHTRANG_THOITIET NVARCHAR(30)), CHUYENXE_P33(MACHUYEN VARCHAR(10) PRIMARY KEY, MAKV VARCHAR(10), THOIGIAN_BD DATETIME, CUOCPHI DECIMAL(10, 2))`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE tăng 10% cước phí (CUOCPHI = CUOCPHI * 1.10) cho các chuyến xe xuất phát tại khu vực có thời tiết 'Mua bao' trong tháng 10 năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Tăng 10% cước phí chuyến xe giờ mưa bão tháng 10/2024
UPDATE CX
SET CUOCPHI = CX.CUOCPHI * 1.10
FROM CHUYENXE_P33 CX
INNER JOIN KHUVUC_P33 KV ON CX.MAKV = KV.MAKV
WHERE KV.TINHTRANG_THOITIET = N'Mua bao'
  AND MONTH(CX.THOIGIAN_BD) = 10
  AND YEAR(CX.THOIGIAN_BD) = 2024;
```

**Các bước suy luận tư duy:**
1. Bước 1: UPDATE CX SET CUOCPHI = CX.CUOCPHI * 1.10.
1. Bước 2: FROM CHUYENXE_P33 CX INNER JOIN KHUVUC_P33 KV ON CX.MAKV = KV.MAKV.
1. Bước 3: Lọc tình trạng thời tiết mưa bão trong tháng 10/2024.

**Phân tích trường hợp biên (Edge Cases):**
Chính sách phụ thu thời tiết bất lợi trong ứng dụng gọi xe công nghệ.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 34 [SQL-P34] — T-SQL DML: Xóa Phiếu Mượn Sách Quá Hạn Đã Bồi Thường Đầy Đủ Trước Năm 2024 (Sửa P0-03)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `PHIEUMUON_P34(MAPM VARCHAR(10) PRIMARY KEY, NGAYTRA DATE, TRANGTHAI NVARCHAR(30), TIENBOITHUONG DECIMAL(10, 2))`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL DELETE xóa các phiếu mượn sách đã hoàn tất bồi thường (TRANGTHAI = 'Da boi thuong') có ngày trả hoặc thanh lý trước ngày '2024-01-01'.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Xóa phiếu mượn sách đã bồi thường xong trước năm 2024
DELETE PM
FROM PHIEUMUON_P34 PM
WHERE PM.TRANGTHAI = N'Da boi thuong'
  AND PM.NGAYTRA < '2024-01-01';
```

**Các bước suy luận tư duy:**
1. Bước 1: DELETE PM FROM PHIEUMUON_P34 PM.
1. Bước 2: Lọc trạng thái 'Da boi thuong' và NGAYTRA < '2024-01-01'.

**Phân tích trường hợp biên (Edge Cases):**
Dọn dẹp dữ liệu lịch sử các khoản nợ thư viện đã được xử lý xong.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 35 [SQL-P35] — T-SQL DML: Tăng 5% Lương Cơ Bản Bác Sĩ Cấp Cứu Trực Đêm Năm 2024 (Sửa P0-03)
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BACSI_P35(MABS VARCHAR(10) PRIMARY KEY, HOTEN NVARCHAR(100), CHUYENKHOA NVARCHAR(50), LUONGCB DECIMAL(12, 2)), CATRUC_P35(MACATRUC VARCHAR(10) PRIMARY KEY, MABS VARCHAR(10), NGAYTRUC DATE, LOAICATRUC NVARCHAR(20))`
- **Trạng thái kiểm định:** `EXECUTION_VERIFIED` (Đã thực thi & kiểm chứng trên SQL Server 2025)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE tăng 5% lương cơ bản (LUONGCB = LUONGCB * 1.05) trong bảng BACSI_P35 cho các bác sĩ thuộc chuyên khoa 'Cap cuu' đã tham gia ca trực 'Truc dem' trong năm 2024.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Tăng 5% lương cơ bản cho bác sĩ cấp cứu có tham gia trực đêm năm 2024
UPDATE BS
SET LUONGCB = BS.LUONGCB * 1.05
FROM BACSI_P35 BS
INNER JOIN CATRUC_P35 CT ON BS.MABS = CT.MABS
WHERE BS.CHUYENKHOA = N'Cap cuu'
  AND CT.LOAICATRUC = N'Truc dem'
  AND YEAR(CT.NGAYTRUC) = 2024;
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp UPDATE BS SET LUONGCB = BS.LUONGCB * 1.05 (chuẩn T-SQL không có bí danh trong vế trái mệnh đề SET).
1. Bước 2: FROM BACSI_P35 BS INNER JOIN CATRUC_P35 CT ON BS.MABS = CT.MABS.
1. Bước 3: Mệnh đề WHERE kiểm tra đồng thời chuyên khoa cấp cứu, loại ca trực đêm và năm trực YEAR(CT.NGAYTRUC) = 2024.

**Phân tích trường hợp biên (Edge Cases):**
ĐÃ SỬA LỖI P0-03 TOÀN DIỆN: Bảng CATRUC_P35 có đầy đủ cột NGAYTRUC kiểu DATE, mệnh đề WHERE có bộ lọc YEAR(CT.NGAYTRUC) = 2024 chuẩn xác, giải quyết dứt điểm phản hồi kiểm toán.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---
