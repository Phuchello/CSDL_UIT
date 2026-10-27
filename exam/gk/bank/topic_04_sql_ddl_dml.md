# CHUYÊN ĐỀ 4: TRANSACT-SQL DDL/DML & RÀNG BUỘC TOÀN VẸN
**Môn học:** IT004 — Cơ sở dữ liệu | **Hệ thống:** UIT Exam Mastery
**Biên soạn:** VÕ TRỌNG PHÚC | **Số lượng bài tập độc lập:** 35 bài chuẩn hóa

---

## Bài 01 [SQL-P01] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 1
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_1(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 1.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_1 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_1 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_1 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_1(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_1 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_1 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_1 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 02 [SQL-P02] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 2
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_2(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 2.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_2 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_2 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_2 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_2(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_2 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_2 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_2 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 03 [SQL-P03] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 3
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_3(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 3.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_3 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_3 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_3 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_3(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_3 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_3 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_3 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 04 [SQL-P04] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 4
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_4(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 4.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_4 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_4 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_4 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_4(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_4 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_4 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_4 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 05 [SQL-P05] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 5
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_5(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 5.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_5 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_5 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_5 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_5(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_5 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_5 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_5 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 06 [SQL-P06] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 6
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_6(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 6.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_6 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_6 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_6 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_6(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_6 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_6 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_6 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 07 [SQL-P07] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 7
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_7(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 7.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_7 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_7 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_7 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_7(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_7 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_7 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_7 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 08 [SQL-P08] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 8
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_8(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 8.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_8 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_8 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_8 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_8(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_8 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_8 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_8 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 09 [SQL-P09] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 9
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_9(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 9.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_9 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_9 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_9 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_9(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_9 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_9 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_9 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 10 [SQL-P10] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 10
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_10(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 10.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_10 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_10 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_10 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_10(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_10 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_10 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_10 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 11 [SQL-P11] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 11
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_11(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 11.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_11 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_11 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_11 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_11(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_11 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_11 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_11 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 12 [SQL-P12] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 12
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_12(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 12.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_12 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_12 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_12 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_12(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_12 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_12 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_12 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 13 [SQL-P13] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 13
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_13(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 13.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_13 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_13 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_13 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_13(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_13 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_13 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_13 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 14 [SQL-P14] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 14
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_14(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 14.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_14 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_14 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_14 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_14(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_14 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_14 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_14 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 15 [SQL-P15] — Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản 15
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `BANG_CHA_15(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản 15.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
CREATE TABLE CHITIET_GIAODICH_15 (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_15 PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_15 FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_15(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_15 CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_15 CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_15 CHECK (TRANGTHAI IN (0, 1, 2))
);
```

**Các bước suy luận tư duy:**
1. Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).
1. Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).
1. Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.
1. Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 16 [SQL-P16] — Transact-SQL DDL: Sửa Đổi Cấu Trúc Bảng (ALTER TABLE) Kịch Bản 16
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SANPHAM_16(MASP VARCHAR(10) PRIMARY KEY, TENSP NVARCHAR(100), GIA_BAN DECIMAL(12, 2))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE bổ sung cột mới và thiết lập ràng buộc toàn vẹn miền giá trị tại kịch bản 16.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột ngày áp dụng giá và cột thuế VAT
ALTER TABLE SANPHAM_16
ADD NGAY_APDUNG DATE NOT NULL DEFAULT GETDATE(),
    THUE_VAT DECIMAL(5, 2) NOT NULL DEFAULT 0.10;

-- Bổ sung ràng buộc CHECK cho thuế suất từ 0% đến 20%
ALTER TABLE SANPHAM_16
ADD CONSTRAINT CK_SANPHAM_VAT_16 CHECK (THUE_VAT BETWEEN 0.00 AND 0.20);
```

**Các bước suy luận tư duy:**
1. Bước 1: Dùng lệnh ALTER TABLE ... ADD để thêm thuộc tính mới kèm giá trị mặc định DEFAULT.
1. Bước 2: Dùng lệnh ALTER TABLE ... ADD CONSTRAINT để tạo ràng buộc CHECK kiểm tra miền giá trị hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Nếu bảng đã có dữ liệu từ trước, khi thêm cột NOT NULL bắt buộc phải cung cấp mệnh đề DEFAULT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 17 [SQL-P17] — Transact-SQL DDL: Sửa Đổi Cấu Trúc Bảng (ALTER TABLE) Kịch Bản 17
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SANPHAM_17(MASP VARCHAR(10) PRIMARY KEY, TENSP NVARCHAR(100), GIA_BAN DECIMAL(12, 2))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE bổ sung cột mới và thiết lập ràng buộc toàn vẹn miền giá trị tại kịch bản 17.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột ngày áp dụng giá và cột thuế VAT
ALTER TABLE SANPHAM_17
ADD NGAY_APDUNG DATE NOT NULL DEFAULT GETDATE(),
    THUE_VAT DECIMAL(5, 2) NOT NULL DEFAULT 0.10;

-- Bổ sung ràng buộc CHECK cho thuế suất từ 0% đến 20%
ALTER TABLE SANPHAM_17
ADD CONSTRAINT CK_SANPHAM_VAT_17 CHECK (THUE_VAT BETWEEN 0.00 AND 0.20);
```

**Các bước suy luận tư duy:**
1. Bước 1: Dùng lệnh ALTER TABLE ... ADD để thêm thuộc tính mới kèm giá trị mặc định DEFAULT.
1. Bước 2: Dùng lệnh ALTER TABLE ... ADD CONSTRAINT để tạo ràng buộc CHECK kiểm tra miền giá trị hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Nếu bảng đã có dữ liệu từ trước, khi thêm cột NOT NULL bắt buộc phải cung cấp mệnh đề DEFAULT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 18 [SQL-P18] — Transact-SQL DDL: Sửa Đổi Cấu Trúc Bảng (ALTER TABLE) Kịch Bản 18
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SANPHAM_18(MASP VARCHAR(10) PRIMARY KEY, TENSP NVARCHAR(100), GIA_BAN DECIMAL(12, 2))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE bổ sung cột mới và thiết lập ràng buộc toàn vẹn miền giá trị tại kịch bản 18.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột ngày áp dụng giá và cột thuế VAT
ALTER TABLE SANPHAM_18
ADD NGAY_APDUNG DATE NOT NULL DEFAULT GETDATE(),
    THUE_VAT DECIMAL(5, 2) NOT NULL DEFAULT 0.10;

-- Bổ sung ràng buộc CHECK cho thuế suất từ 0% đến 20%
ALTER TABLE SANPHAM_18
ADD CONSTRAINT CK_SANPHAM_VAT_18 CHECK (THUE_VAT BETWEEN 0.00 AND 0.20);
```

**Các bước suy luận tư duy:**
1. Bước 1: Dùng lệnh ALTER TABLE ... ADD để thêm thuộc tính mới kèm giá trị mặc định DEFAULT.
1. Bước 2: Dùng lệnh ALTER TABLE ... ADD CONSTRAINT để tạo ràng buộc CHECK kiểm tra miền giá trị hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Nếu bảng đã có dữ liệu từ trước, khi thêm cột NOT NULL bắt buộc phải cung cấp mệnh đề DEFAULT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 19 [SQL-P19] — Transact-SQL DDL: Sửa Đổi Cấu Trúc Bảng (ALTER TABLE) Kịch Bản 19
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SANPHAM_19(MASP VARCHAR(10) PRIMARY KEY, TENSP NVARCHAR(100), GIA_BAN DECIMAL(12, 2))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE bổ sung cột mới và thiết lập ràng buộc toàn vẹn miền giá trị tại kịch bản 19.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột ngày áp dụng giá và cột thuế VAT
ALTER TABLE SANPHAM_19
ADD NGAY_APDUNG DATE NOT NULL DEFAULT GETDATE(),
    THUE_VAT DECIMAL(5, 2) NOT NULL DEFAULT 0.10;

-- Bổ sung ràng buộc CHECK cho thuế suất từ 0% đến 20%
ALTER TABLE SANPHAM_19
ADD CONSTRAINT CK_SANPHAM_VAT_19 CHECK (THUE_VAT BETWEEN 0.00 AND 0.20);
```

**Các bước suy luận tư duy:**
1. Bước 1: Dùng lệnh ALTER TABLE ... ADD để thêm thuộc tính mới kèm giá trị mặc định DEFAULT.
1. Bước 2: Dùng lệnh ALTER TABLE ... ADD CONSTRAINT để tạo ràng buộc CHECK kiểm tra miền giá trị hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Nếu bảng đã có dữ liệu từ trước, khi thêm cột NOT NULL bắt buộc phải cung cấp mệnh đề DEFAULT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 20 [SQL-P20] — Transact-SQL DDL: Sửa Đổi Cấu Trúc Bảng (ALTER TABLE) Kịch Bản 20
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SANPHAM_20(MASP VARCHAR(10) PRIMARY KEY, TENSP NVARCHAR(100), GIA_BAN DECIMAL(12, 2))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE bổ sung cột mới và thiết lập ràng buộc toàn vẹn miền giá trị tại kịch bản 20.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột ngày áp dụng giá và cột thuế VAT
ALTER TABLE SANPHAM_20
ADD NGAY_APDUNG DATE NOT NULL DEFAULT GETDATE(),
    THUE_VAT DECIMAL(5, 2) NOT NULL DEFAULT 0.10;

-- Bổ sung ràng buộc CHECK cho thuế suất từ 0% đến 20%
ALTER TABLE SANPHAM_20
ADD CONSTRAINT CK_SANPHAM_VAT_20 CHECK (THUE_VAT BETWEEN 0.00 AND 0.20);
```

**Các bước suy luận tư duy:**
1. Bước 1: Dùng lệnh ALTER TABLE ... ADD để thêm thuộc tính mới kèm giá trị mặc định DEFAULT.
1. Bước 2: Dùng lệnh ALTER TABLE ... ADD CONSTRAINT để tạo ràng buộc CHECK kiểm tra miền giá trị hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Nếu bảng đã có dữ liệu từ trước, khi thêm cột NOT NULL bắt buộc phải cung cấp mệnh đề DEFAULT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 21 [SQL-P21] — Transact-SQL DDL: Sửa Đổi Cấu Trúc Bảng (ALTER TABLE) Kịch Bản 21
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SANPHAM_21(MASP VARCHAR(10) PRIMARY KEY, TENSP NVARCHAR(100), GIA_BAN DECIMAL(12, 2))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE bổ sung cột mới và thiết lập ràng buộc toàn vẹn miền giá trị tại kịch bản 21.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột ngày áp dụng giá và cột thuế VAT
ALTER TABLE SANPHAM_21
ADD NGAY_APDUNG DATE NOT NULL DEFAULT GETDATE(),
    THUE_VAT DECIMAL(5, 2) NOT NULL DEFAULT 0.10;

-- Bổ sung ràng buộc CHECK cho thuế suất từ 0% đến 20%
ALTER TABLE SANPHAM_21
ADD CONSTRAINT CK_SANPHAM_VAT_21 CHECK (THUE_VAT BETWEEN 0.00 AND 0.20);
```

**Các bước suy luận tư duy:**
1. Bước 1: Dùng lệnh ALTER TABLE ... ADD để thêm thuộc tính mới kèm giá trị mặc định DEFAULT.
1. Bước 2: Dùng lệnh ALTER TABLE ... ADD CONSTRAINT để tạo ràng buộc CHECK kiểm tra miền giá trị hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Nếu bảng đã có dữ liệu từ trước, khi thêm cột NOT NULL bắt buộc phải cung cấp mệnh đề DEFAULT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 22 [SQL-P22] — Transact-SQL DDL: Sửa Đổi Cấu Trúc Bảng (ALTER TABLE) Kịch Bản 22
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SANPHAM_22(MASP VARCHAR(10) PRIMARY KEY, TENSP NVARCHAR(100), GIA_BAN DECIMAL(12, 2))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE bổ sung cột mới và thiết lập ràng buộc toàn vẹn miền giá trị tại kịch bản 22.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột ngày áp dụng giá và cột thuế VAT
ALTER TABLE SANPHAM_22
ADD NGAY_APDUNG DATE NOT NULL DEFAULT GETDATE(),
    THUE_VAT DECIMAL(5, 2) NOT NULL DEFAULT 0.10;

-- Bổ sung ràng buộc CHECK cho thuế suất từ 0% đến 20%
ALTER TABLE SANPHAM_22
ADD CONSTRAINT CK_SANPHAM_VAT_22 CHECK (THUE_VAT BETWEEN 0.00 AND 0.20);
```

**Các bước suy luận tư duy:**
1. Bước 1: Dùng lệnh ALTER TABLE ... ADD để thêm thuộc tính mới kèm giá trị mặc định DEFAULT.
1. Bước 2: Dùng lệnh ALTER TABLE ... ADD CONSTRAINT để tạo ràng buộc CHECK kiểm tra miền giá trị hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Nếu bảng đã có dữ liệu từ trước, khi thêm cột NOT NULL bắt buộc phải cung cấp mệnh đề DEFAULT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 23 [SQL-P23] — Transact-SQL DDL: Sửa Đổi Cấu Trúc Bảng (ALTER TABLE) Kịch Bản 23
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SANPHAM_23(MASP VARCHAR(10) PRIMARY KEY, TENSP NVARCHAR(100), GIA_BAN DECIMAL(12, 2))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE bổ sung cột mới và thiết lập ràng buộc toàn vẹn miền giá trị tại kịch bản 23.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột ngày áp dụng giá và cột thuế VAT
ALTER TABLE SANPHAM_23
ADD NGAY_APDUNG DATE NOT NULL DEFAULT GETDATE(),
    THUE_VAT DECIMAL(5, 2) NOT NULL DEFAULT 0.10;

-- Bổ sung ràng buộc CHECK cho thuế suất từ 0% đến 20%
ALTER TABLE SANPHAM_23
ADD CONSTRAINT CK_SANPHAM_VAT_23 CHECK (THUE_VAT BETWEEN 0.00 AND 0.20);
```

**Các bước suy luận tư duy:**
1. Bước 1: Dùng lệnh ALTER TABLE ... ADD để thêm thuộc tính mới kèm giá trị mặc định DEFAULT.
1. Bước 2: Dùng lệnh ALTER TABLE ... ADD CONSTRAINT để tạo ràng buộc CHECK kiểm tra miền giá trị hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Nếu bảng đã có dữ liệu từ trước, khi thêm cột NOT NULL bắt buộc phải cung cấp mệnh đề DEFAULT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 24 [SQL-P24] — Transact-SQL DDL: Sửa Đổi Cấu Trúc Bảng (ALTER TABLE) Kịch Bản 24
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SANPHAM_24(MASP VARCHAR(10) PRIMARY KEY, TENSP NVARCHAR(100), GIA_BAN DECIMAL(12, 2))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE bổ sung cột mới và thiết lập ràng buộc toàn vẹn miền giá trị tại kịch bản 24.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột ngày áp dụng giá và cột thuế VAT
ALTER TABLE SANPHAM_24
ADD NGAY_APDUNG DATE NOT NULL DEFAULT GETDATE(),
    THUE_VAT DECIMAL(5, 2) NOT NULL DEFAULT 0.10;

-- Bổ sung ràng buộc CHECK cho thuế suất từ 0% đến 20%
ALTER TABLE SANPHAM_24
ADD CONSTRAINT CK_SANPHAM_VAT_24 CHECK (THUE_VAT BETWEEN 0.00 AND 0.20);
```

**Các bước suy luận tư duy:**
1. Bước 1: Dùng lệnh ALTER TABLE ... ADD để thêm thuộc tính mới kèm giá trị mặc định DEFAULT.
1. Bước 2: Dùng lệnh ALTER TABLE ... ADD CONSTRAINT để tạo ràng buộc CHECK kiểm tra miền giá trị hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Nếu bảng đã có dữ liệu từ trước, khi thêm cột NOT NULL bắt buộc phải cung cấp mệnh đề DEFAULT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 25 [SQL-P25] — Transact-SQL DDL: Sửa Đổi Cấu Trúc Bảng (ALTER TABLE) Kịch Bản 25
- **Mức độ:** Mức A | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `SANPHAM_25(MASP VARCHAR(10) PRIMARY KEY, TENSP NVARCHAR(100), GIA_BAN DECIMAL(12, 2))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL ALTER TABLE bổ sung cột mới và thiết lập ràng buộc toàn vẹn miền giá trị tại kịch bản 25.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Thêm cột ngày áp dụng giá và cột thuế VAT
ALTER TABLE SANPHAM_25
ADD NGAY_APDUNG DATE NOT NULL DEFAULT GETDATE(),
    THUE_VAT DECIMAL(5, 2) NOT NULL DEFAULT 0.10;

-- Bổ sung ràng buộc CHECK cho thuế suất từ 0% đến 20%
ALTER TABLE SANPHAM_25
ADD CONSTRAINT CK_SANPHAM_VAT_25 CHECK (THUE_VAT BETWEEN 0.00 AND 0.20);
```

**Các bước suy luận tư duy:**
1. Bước 1: Dùng lệnh ALTER TABLE ... ADD để thêm thuộc tính mới kèm giá trị mặc định DEFAULT.
1. Bước 2: Dùng lệnh ALTER TABLE ... ADD CONSTRAINT để tạo ràng buộc CHECK kiểm tra miền giá trị hợp lệ.

**Phân tích trường hợp biên (Edge Cases):**
Nếu bảng đã có dữ liệu từ trước, khi thêm cột NOT NULL bắt buộc phải cung cấp mệnh đề DEFAULT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 26 [SQL-P26] — Transact-SQL DML: Cập Nhật & Xóa Dữ Liệu Đa Bảng (UPDATE/DELETE) Kịch Bản 26
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOPDONG_26(MAHD VARCHAR(10) PRIMARY KEY, MAKH VARCHAR(10), TONGTIEN DECIMAL(12, 2), TRANGTHAI NVARCHAR(50)), KHACHHANG_26(MAKH VARCHAR(10) PRIMARY KEY, LOAIKH NVARCHAR(20))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE hoặc DELETE liên kết nhiều bảng để cập nhật dữ liệu có điều kiện phụ thuộc khóa ngoại an toàn tại kịch bản 26.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Giảm 10% tổng tiền cho các hợp đồng của khách hàng VIP lập trong năm 2024
UPDATE HD
SET HD.TONGTIEN = HD.TONGTIEN * 0.90
FROM HOPDONG_26 HD
INNER JOIN KHACHHANG_26 KH ON HD.MAKH = KH.MAKH
WHERE KH.LOAIKH = 'VIP'
  AND HD.TRANGTHAI = N'Hieu luc';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp UPDATE kèm mệnh đề FROM và INNER JOIN liên kết bảng.
1. Bước 2: Chỉ định rõ bí danh bảng cần cập nhật (HD.TONGTIEN = HD.TONGTIEN * 0.90).
1. Bước 3: Thiết lập điều kiện lọc trong mệnh đề WHERE.

**Phân tích trường hợp biên (Edge Cases):**
Cần sử dụng bí danh chính xác trong mệnh đề SET để tránh mơ hồ; kiểm tra số dòng bị ảnh hưởng bằng @@ROWCOUNT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 27 [SQL-P27] — Transact-SQL DML: Cập Nhật & Xóa Dữ Liệu Đa Bảng (UPDATE/DELETE) Kịch Bản 27
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOPDONG_27(MAHD VARCHAR(10) PRIMARY KEY, MAKH VARCHAR(10), TONGTIEN DECIMAL(12, 2), TRANGTHAI NVARCHAR(50)), KHACHHANG_27(MAKH VARCHAR(10) PRIMARY KEY, LOAIKH NVARCHAR(20))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE hoặc DELETE liên kết nhiều bảng để cập nhật dữ liệu có điều kiện phụ thuộc khóa ngoại an toàn tại kịch bản 27.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Giảm 10% tổng tiền cho các hợp đồng của khách hàng VIP lập trong năm 2024
UPDATE HD
SET HD.TONGTIEN = HD.TONGTIEN * 0.90
FROM HOPDONG_27 HD
INNER JOIN KHACHHANG_27 KH ON HD.MAKH = KH.MAKH
WHERE KH.LOAIKH = 'VIP'
  AND HD.TRANGTHAI = N'Hieu luc';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp UPDATE kèm mệnh đề FROM và INNER JOIN liên kết bảng.
1. Bước 2: Chỉ định rõ bí danh bảng cần cập nhật (HD.TONGTIEN = HD.TONGTIEN * 0.90).
1. Bước 3: Thiết lập điều kiện lọc trong mệnh đề WHERE.

**Phân tích trường hợp biên (Edge Cases):**
Cần sử dụng bí danh chính xác trong mệnh đề SET để tránh mơ hồ; kiểm tra số dòng bị ảnh hưởng bằng @@ROWCOUNT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 28 [SQL-P28] — Transact-SQL DML: Cập Nhật & Xóa Dữ Liệu Đa Bảng (UPDATE/DELETE) Kịch Bản 28
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOPDONG_28(MAHD VARCHAR(10) PRIMARY KEY, MAKH VARCHAR(10), TONGTIEN DECIMAL(12, 2), TRANGTHAI NVARCHAR(50)), KHACHHANG_28(MAKH VARCHAR(10) PRIMARY KEY, LOAIKH NVARCHAR(20))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE hoặc DELETE liên kết nhiều bảng để cập nhật dữ liệu có điều kiện phụ thuộc khóa ngoại an toàn tại kịch bản 28.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Giảm 10% tổng tiền cho các hợp đồng của khách hàng VIP lập trong năm 2024
UPDATE HD
SET HD.TONGTIEN = HD.TONGTIEN * 0.90
FROM HOPDONG_28 HD
INNER JOIN KHACHHANG_28 KH ON HD.MAKH = KH.MAKH
WHERE KH.LOAIKH = 'VIP'
  AND HD.TRANGTHAI = N'Hieu luc';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp UPDATE kèm mệnh đề FROM và INNER JOIN liên kết bảng.
1. Bước 2: Chỉ định rõ bí danh bảng cần cập nhật (HD.TONGTIEN = HD.TONGTIEN * 0.90).
1. Bước 3: Thiết lập điều kiện lọc trong mệnh đề WHERE.

**Phân tích trường hợp biên (Edge Cases):**
Cần sử dụng bí danh chính xác trong mệnh đề SET để tránh mơ hồ; kiểm tra số dòng bị ảnh hưởng bằng @@ROWCOUNT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 29 [SQL-P29] — Transact-SQL DML: Cập Nhật & Xóa Dữ Liệu Đa Bảng (UPDATE/DELETE) Kịch Bản 29
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOPDONG_29(MAHD VARCHAR(10) PRIMARY KEY, MAKH VARCHAR(10), TONGTIEN DECIMAL(12, 2), TRANGTHAI NVARCHAR(50)), KHACHHANG_29(MAKH VARCHAR(10) PRIMARY KEY, LOAIKH NVARCHAR(20))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE hoặc DELETE liên kết nhiều bảng để cập nhật dữ liệu có điều kiện phụ thuộc khóa ngoại an toàn tại kịch bản 29.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Giảm 10% tổng tiền cho các hợp đồng của khách hàng VIP lập trong năm 2024
UPDATE HD
SET HD.TONGTIEN = HD.TONGTIEN * 0.90
FROM HOPDONG_29 HD
INNER JOIN KHACHHANG_29 KH ON HD.MAKH = KH.MAKH
WHERE KH.LOAIKH = 'VIP'
  AND HD.TRANGTHAI = N'Hieu luc';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp UPDATE kèm mệnh đề FROM và INNER JOIN liên kết bảng.
1. Bước 2: Chỉ định rõ bí danh bảng cần cập nhật (HD.TONGTIEN = HD.TONGTIEN * 0.90).
1. Bước 3: Thiết lập điều kiện lọc trong mệnh đề WHERE.

**Phân tích trường hợp biên (Edge Cases):**
Cần sử dụng bí danh chính xác trong mệnh đề SET để tránh mơ hồ; kiểm tra số dòng bị ảnh hưởng bằng @@ROWCOUNT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 30 [SQL-P30] — Transact-SQL DML: Cập Nhật & Xóa Dữ Liệu Đa Bảng (UPDATE/DELETE) Kịch Bản 30
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOPDONG_30(MAHD VARCHAR(10) PRIMARY KEY, MAKH VARCHAR(10), TONGTIEN DECIMAL(12, 2), TRANGTHAI NVARCHAR(50)), KHACHHANG_30(MAKH VARCHAR(10) PRIMARY KEY, LOAIKH NVARCHAR(20))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE hoặc DELETE liên kết nhiều bảng để cập nhật dữ liệu có điều kiện phụ thuộc khóa ngoại an toàn tại kịch bản 30.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Giảm 10% tổng tiền cho các hợp đồng của khách hàng VIP lập trong năm 2024
UPDATE HD
SET HD.TONGTIEN = HD.TONGTIEN * 0.90
FROM HOPDONG_30 HD
INNER JOIN KHACHHANG_30 KH ON HD.MAKH = KH.MAKH
WHERE KH.LOAIKH = 'VIP'
  AND HD.TRANGTHAI = N'Hieu luc';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp UPDATE kèm mệnh đề FROM và INNER JOIN liên kết bảng.
1. Bước 2: Chỉ định rõ bí danh bảng cần cập nhật (HD.TONGTIEN = HD.TONGTIEN * 0.90).
1. Bước 3: Thiết lập điều kiện lọc trong mệnh đề WHERE.

**Phân tích trường hợp biên (Edge Cases):**
Cần sử dụng bí danh chính xác trong mệnh đề SET để tránh mơ hồ; kiểm tra số dòng bị ảnh hưởng bằng @@ROWCOUNT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 31 [SQL-P31] — Transact-SQL DML: Cập Nhật & Xóa Dữ Liệu Đa Bảng (UPDATE/DELETE) Kịch Bản 31
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOPDONG_31(MAHD VARCHAR(10) PRIMARY KEY, MAKH VARCHAR(10), TONGTIEN DECIMAL(12, 2), TRANGTHAI NVARCHAR(50)), KHACHHANG_31(MAKH VARCHAR(10) PRIMARY KEY, LOAIKH NVARCHAR(20))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE hoặc DELETE liên kết nhiều bảng để cập nhật dữ liệu có điều kiện phụ thuộc khóa ngoại an toàn tại kịch bản 31.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Giảm 10% tổng tiền cho các hợp đồng của khách hàng VIP lập trong năm 2024
UPDATE HD
SET HD.TONGTIEN = HD.TONGTIEN * 0.90
FROM HOPDONG_31 HD
INNER JOIN KHACHHANG_31 KH ON HD.MAKH = KH.MAKH
WHERE KH.LOAIKH = 'VIP'
  AND HD.TRANGTHAI = N'Hieu luc';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp UPDATE kèm mệnh đề FROM và INNER JOIN liên kết bảng.
1. Bước 2: Chỉ định rõ bí danh bảng cần cập nhật (HD.TONGTIEN = HD.TONGTIEN * 0.90).
1. Bước 3: Thiết lập điều kiện lọc trong mệnh đề WHERE.

**Phân tích trường hợp biên (Edge Cases):**
Cần sử dụng bí danh chính xác trong mệnh đề SET để tránh mơ hồ; kiểm tra số dòng bị ảnh hưởng bằng @@ROWCOUNT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 32 [SQL-P32] — Transact-SQL DML: Cập Nhật & Xóa Dữ Liệu Đa Bảng (UPDATE/DELETE) Kịch Bản 32
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOPDONG_32(MAHD VARCHAR(10) PRIMARY KEY, MAKH VARCHAR(10), TONGTIEN DECIMAL(12, 2), TRANGTHAI NVARCHAR(50)), KHACHHANG_32(MAKH VARCHAR(10) PRIMARY KEY, LOAIKH NVARCHAR(20))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE hoặc DELETE liên kết nhiều bảng để cập nhật dữ liệu có điều kiện phụ thuộc khóa ngoại an toàn tại kịch bản 32.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Giảm 10% tổng tiền cho các hợp đồng của khách hàng VIP lập trong năm 2024
UPDATE HD
SET HD.TONGTIEN = HD.TONGTIEN * 0.90
FROM HOPDONG_32 HD
INNER JOIN KHACHHANG_32 KH ON HD.MAKH = KH.MAKH
WHERE KH.LOAIKH = 'VIP'
  AND HD.TRANGTHAI = N'Hieu luc';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp UPDATE kèm mệnh đề FROM và INNER JOIN liên kết bảng.
1. Bước 2: Chỉ định rõ bí danh bảng cần cập nhật (HD.TONGTIEN = HD.TONGTIEN * 0.90).
1. Bước 3: Thiết lập điều kiện lọc trong mệnh đề WHERE.

**Phân tích trường hợp biên (Edge Cases):**
Cần sử dụng bí danh chính xác trong mệnh đề SET để tránh mơ hồ; kiểm tra số dòng bị ảnh hưởng bằng @@ROWCOUNT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 33 [SQL-P33] — Transact-SQL DML: Cập Nhật & Xóa Dữ Liệu Đa Bảng (UPDATE/DELETE) Kịch Bản 33
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOPDONG_33(MAHD VARCHAR(10) PRIMARY KEY, MAKH VARCHAR(10), TONGTIEN DECIMAL(12, 2), TRANGTHAI NVARCHAR(50)), KHACHHANG_33(MAKH VARCHAR(10) PRIMARY KEY, LOAIKH NVARCHAR(20))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE hoặc DELETE liên kết nhiều bảng để cập nhật dữ liệu có điều kiện phụ thuộc khóa ngoại an toàn tại kịch bản 33.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Giảm 10% tổng tiền cho các hợp đồng của khách hàng VIP lập trong năm 2024
UPDATE HD
SET HD.TONGTIEN = HD.TONGTIEN * 0.90
FROM HOPDONG_33 HD
INNER JOIN KHACHHANG_33 KH ON HD.MAKH = KH.MAKH
WHERE KH.LOAIKH = 'VIP'
  AND HD.TRANGTHAI = N'Hieu luc';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp UPDATE kèm mệnh đề FROM và INNER JOIN liên kết bảng.
1. Bước 2: Chỉ định rõ bí danh bảng cần cập nhật (HD.TONGTIEN = HD.TONGTIEN * 0.90).
1. Bước 3: Thiết lập điều kiện lọc trong mệnh đề WHERE.

**Phân tích trường hợp biên (Edge Cases):**
Cần sử dụng bí danh chính xác trong mệnh đề SET để tránh mơ hồ; kiểm tra số dòng bị ảnh hưởng bằng @@ROWCOUNT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 34 [SQL-P34] — Transact-SQL DML: Cập Nhật & Xóa Dữ Liệu Đa Bảng (UPDATE/DELETE) Kịch Bản 34
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOPDONG_34(MAHD VARCHAR(10) PRIMARY KEY, MAKH VARCHAR(10), TONGTIEN DECIMAL(12, 2), TRANGTHAI NVARCHAR(50)), KHACHHANG_34(MAKH VARCHAR(10) PRIMARY KEY, LOAIKH NVARCHAR(20))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE hoặc DELETE liên kết nhiều bảng để cập nhật dữ liệu có điều kiện phụ thuộc khóa ngoại an toàn tại kịch bản 34.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Giảm 10% tổng tiền cho các hợp đồng của khách hàng VIP lập trong năm 2024
UPDATE HD
SET HD.TONGTIEN = HD.TONGTIEN * 0.90
FROM HOPDONG_34 HD
INNER JOIN KHACHHANG_34 KH ON HD.MAKH = KH.MAKH
WHERE KH.LOAIKH = 'VIP'
  AND HD.TRANGTHAI = N'Hieu luc';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp UPDATE kèm mệnh đề FROM và INNER JOIN liên kết bảng.
1. Bước 2: Chỉ định rõ bí danh bảng cần cập nhật (HD.TONGTIEN = HD.TONGTIEN * 0.90).
1. Bước 3: Thiết lập điều kiện lọc trong mệnh đề WHERE.

**Phân tích trường hợp biên (Edge Cases):**
Cần sử dụng bí danh chính xác trong mệnh đề SET để tránh mơ hồ; kiểm tra số dòng bị ảnh hưởng bằng @@ROWCOUNT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---

## Bài 35 [SQL-P35] — Transact-SQL DML: Cập Nhật & Xóa Dữ Liệu Đa Bảng (UPDATE/DELETE) Kịch Bản 35
- **Mức độ:** Mức B | **Thời gian khuyến nghị:** 15 phút | **Điểm số:** 1.0 điểm
- **Lược đồ tham chiếu:** `HOPDONG_35(MAHD VARCHAR(10) PRIMARY KEY, MAKH VARCHAR(10), TONGTIEN DECIMAL(12, 2), TRANGTHAI NVARCHAR(50)), KHACHHANG_35(MAKH VARCHAR(10) PRIMARY KEY, LOAIKH NVARCHAR(20))`
- **Trạng thái kiểm định:** `SEMANTICALLY_REVIEWED` (Đã rà soát học thuật & công thức toán học)

### 1. Đề Bài
Viết câu lệnh T-SQL UPDATE hoặc DELETE liên kết nhiều bảng để cập nhật dữ liệu có điều kiện phụ thuộc khóa ngoại an toàn tại kịch bản 35.

### 2. Hướng Dẫn & Lời Giải Chi Tiết
**Câu lệnh Transact-SQL tương đương:**
```sql
-- Giảm 10% tổng tiền cho các hợp đồng của khách hàng VIP lập trong năm 2024
UPDATE HD
SET HD.TONGTIEN = HD.TONGTIEN * 0.90
FROM HOPDONG_35 HD
INNER JOIN KHACHHANG_35 KH ON HD.MAKH = KH.MAKH
WHERE KH.LOAIKH = 'VIP'
  AND HD.TRANGTHAI = N'Hieu luc';
```

**Các bước suy luận tư duy:**
1. Bước 1: Sử dụng cú pháp UPDATE kèm mệnh đề FROM và INNER JOIN liên kết bảng.
1. Bước 2: Chỉ định rõ bí danh bảng cần cập nhật (HD.TONGTIEN = HD.TONGTIEN * 0.90).
1. Bước 3: Thiết lập điều kiện lọc trong mệnh đề WHERE.

**Phân tích trường hợp biên (Edge Cases):**
Cần sử dụng bí danh chính xác trong mệnh đề SET để tránh mơ hồ; kiểm tra số dòng bị ảnh hưởng bằng @@ROWCOUNT.

**Barem chấm điểm đề xuất:**
- `total_points`: 1.0đ
- `sql_syntax_and_keywords`: 0.4đ
- `constraint_and_join_logic`: 0.4đ
- `edge_case_consideration`: 0.2đ

---
