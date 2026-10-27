-- =============================================================================
-- FIXTURE & ADVERSARIAL VERIFICATION SCRIPT: MOCK-13
-- Domain: Quản Lý Tuyến Xe Buýt & Metro TP.HCM
-- Profile: RECENT_VERIFIED (10.0 pts, 75 mins)
-- Engine: Microsoft SQL Server 2025 / Azure SQL
-- Author: VÕ TRỌNG PHÚC — CSDL_UIT Master Series
-- =============================================================================

SET NOCOUNT ON;
USE master;
GO

IF DB_ID('Mock13_Transit_DB') IS NOT NULL
BEGIN
    ALTER DATABASE Mock13_Transit_DB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE Mock13_Transit_DB;
END
GO

CREATE DATABASE Mock13_Transit_DB COLLATE Vietnamese_CI_AS;
GO

USE Mock13_Transit_DB;
GO

PRINT '============================================================';
PRINT '=== MOCK-13: CREATING TABLES WITH INTEGRITY CONSTRAINTS   ===';
PRINT '============================================================';

-- 1. TUYEN_XE
CREATE TABLE TUYEN_XE (
    MATUYEN VARCHAR(10) NOT NULL PRIMARY KEY,
    TENTUYEN NVARCHAR(100) NOT NULL,
    LOAI_HINH NVARCHAR(50) NOT NULL,
    CULY_KM DECIMAL(6, 2) NOT NULL CHECK (CULY_KM > 0),
    GIAVE_LUOT DECIMAL(18, 2) NOT NULL CHECK (GIAVE_LUOT > 0)
);

-- 2. TRAM_DUNG
CREATE TABLE TRAM_DUNG (
    MATRAM VARCHAR(10) NOT NULL PRIMARY KEY,
    TENTRAM NVARCHAR(100) NOT NULL,
    DIACHI NVARCHAR(200) NOT NULL,
    QUAN_HUYEN NVARCHAR(50) NOT NULL
);

-- 3. LOTRINH
CREATE TABLE LOTRINH (
    MATUYEN VARCHAR(10) NOT NULL REFERENCES TUYEN_XE(MATUYEN),
    MATRAM VARCHAR(10) NOT NULL REFERENCES TRAM_DUNG(MATRAM),
    SOTHUTU INT NOT NULL CHECK (SOTHUTU > 0),
    KHOANGCACH_KM DECIMAL(6, 2) NOT NULL CHECK (KHOANGCACH_KM >= 0),
    PRIMARY KEY (MATUYEN, MATRAM)
);

-- 4. PHUONGTIEN
CREATE TABLE PHUONGTIEN (
    MAPT VARCHAR(10) NOT NULL PRIMARY KEY,
    BIENSO VARCHAR(20) NOT NULL UNIQUE,
    SOGHE INT NOT NULL CHECK (SOGHE > 0),
    NAMSX INT NOT NULL CHECK (NAMSX >= 1990),
    MATUYEN VARCHAR(10) NOT NULL REFERENCES TUYEN_XE(MATUYEN)
);

-- 5. TAIXE
CREATE TABLE TAIXE (
    MATX VARCHAR(10) NOT NULL PRIMARY KEY,
    HOTEN NVARCHAR(50) NOT NULL,
    HANG_GPLX VARCHAR(10) NOT NULL,
    LUONG_CB DECIMAL(18, 2) NOT NULL CHECK (LUONG_CB > 0),
    MAPT VARCHAR(10) NOT NULL REFERENCES PHUONGTIEN(MAPT)
);

-- 6. CHUYEN_DI
CREATE TABLE CHUYEN_DI (
    MACHUYEN VARCHAR(10) NOT NULL PRIMARY KEY,
    MAPT VARCHAR(10) NOT NULL REFERENCES PHUONGTIEN(MAPT),
    NGAYCHAY DATE NOT NULL,
    GIOXUATPHAT TIME NOT NULL,
    SOLUONG_KHACH INT NOT NULL,
    DOANHTHU DECIMAL(18, 2) NOT NULL
);
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: QUESTION 2.1A CHECK & NOT NULL INTEGRITY     ===';
PRINT '------------------------------------------------------------';

-- Add Question 2.1a constraints
ALTER TABLE CHUYEN_DI
ADD CONSTRAINT CK_CHUYENDI_KHACH CHECK (SOLUONG_KHACH >= 0);

ALTER TABLE CHUYEN_DI
ADD CONSTRAINT CK_CHUYENDI_DOANHTHU CHECK (DOANHTHU >= 0);
GO

-- Seed minimal parent data for constraint adversarial tests
INSERT INTO TUYEN_XE (MATUYEN, TENTUYEN, LOAI_HINH, CULY_KM, GIAVE_LUOT) VALUES
('TX01', N'Bến Thành - Suối Tiên', N'Tuyến Metro', 19.7, 15000);

INSERT INTO PHUONGTIEN (MAPT, BIENSO, SOGHE, NAMSX, MATUYEN) VALUES
('PT01', '50LD-12345', 120, 2023, 'TX01');
GO

-- Adversarial Test 1A: Negative passengers
BEGIN TRY
    INSERT INTO CHUYEN_DI (MACHUYEN, MAPT, NGAYCHAY, GIOXUATPHAT, SOLUONG_KHACH, DOANHTHU)
    VALUES ('CD_TEST1', 'PT01', '2024-11-20', '06:00:00', -5, 100000);
    THROW 50001, 'Test 1A FAILED: Negative passengers count was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_CHUYENDI_KHACH%'
        PRINT '  [PASS] Test 1A: CK_CHUYENDI_KHACH correctly blocked negative passengers.';
    ELSE
    BEGIN
        DECLARE @err1 NVARCHAR(400) = ERROR_MESSAGE();
        PRINT '  [FAIL] Test 1A unexpected error: ' + @err1;
        THROW 50002, @err1, 1;
    END
END CATCH;

-- Adversarial Test 1B: Negative revenue
BEGIN TRY
    INSERT INTO CHUYEN_DI (MACHUYEN, MAPT, NGAYCHAY, GIOXUATPHAT, SOLUONG_KHACH, DOANHTHU)
    VALUES ('CD_TEST2', 'PT01', '2024-11-20', '07:00:00', 50, -50000);
    THROW 50003, 'Test 1B FAILED: Negative revenue was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_CHUYENDI_DOANHTHU%'
        PRINT '  [PASS] Test 1B: CK_CHUYENDI_DOANHTHU correctly blocked negative revenue.';
    ELSE
    BEGIN
        DECLARE @err2 NVARCHAR(400) = ERROR_MESSAGE();
        PRINT '  [FAIL] Test 1B unexpected error: ' + @err2;
        THROW 50004, @err2, 1;
    END
END CATCH;

-- Adversarial Test 1C: NULL policy
BEGIN TRY
    INSERT INTO CHUYEN_DI (MACHUYEN, MAPT, NGAYCHAY, GIOXUATPHAT, SOLUONG_KHACH, DOANHTHU)
    VALUES ('CD_TEST3', 'PT01', '2024-11-20', '08:00:00', NULL, 100000);
    THROW 50005, 'Test 1C FAILED: NULL passenger count was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] Test 1C: NOT NULL policy correctly rejected NULL SOLUONG_KHACH (Error 515).';
    ELSE
    BEGIN
        DECLARE @err3 NVARCHAR(400) = ERROR_MESSAGE();
        PRINT '  [FAIL] Test 1C unexpected error: ' + @err3;
        THROW 50006, @err3, 1;
    END
END CATCH;
GO

PRINT '------------------------------------------------------------';
PRINT '=== SEEDING COMPREHENSIVE BENCHMARK DATASET               ===';
PRINT '------------------------------------------------------------';

DELETE FROM CHUYEN_DI;
DELETE FROM TAIXE;
DELETE FROM PHUONGTIEN;
DELETE FROM LOTRINH;
DELETE FROM TRAM_DUNG;
DELETE FROM TUYEN_XE;

-- 1. TUYEN_XE (5 tuyến)
-- TX01: Tuyến Metro, 19.7km (>= 15km)
-- TX02: Tuyến Metro, 11.3km (< 15km)
-- TX03: Xe buýt phổ thông, 'Bến Thành - Bến xe Miền Đông mới'
-- TX04: Xe buýt điện VinBus
-- TX05: Xe buýt điện VinBus
INSERT INTO TUYEN_XE (MATUYEN, TENTUYEN, LOAI_HINH, CULY_KM, GIAVE_LUOT) VALUES
('TX01', N'Bến Thành - Suối Tiên (Metro Số 1)', N'Tuyến Metro', 19.7, 15000),
('TX02', N'Bến Thành - Tham Lương (Metro Số 2)', N'Tuyến Metro', 11.3, 12000),
('TX03', N'Bến Thành - Bến xe Miền Đông mới', N'Xe buýt phổ thông', 24.5, 7000),
('TX04', N'Vinhomes Grand Park - Bến Thành', N'Xe buýt điện VinBus', 26.0, 8000),
('TX05', N'Đại học Quốc gia - Chợ Bến Thành', N'Xe buýt điện VinBus', 22.0, 7000);

-- 2. TRAM_DUNG (6 trạm)
-- Trạm tại Thủ Đức: TR01, TR02, TR05 (3 trạm)
-- Trạm Quận 1: TR03
-- Trạm Bình Thạnh: TR04
-- Trạm TR06 (Dĩ An): Mới quy hoạch, chưa có tuyến nào đi qua
INSERT INTO TRAM_DUNG (MATRAM, TENTRAM, DIACHI, QUAN_HUYEN) VALUES
('TR01', N'Trạm Ga Đại Học Quốc Gia', N'Khu phố 6, Linh Trung', N'Thủ Đức'),
('TR02', N'Trạm Ký túc xá Khu B', N'Đường Tạ Quang Bửu, Linh Trung', N'Thủ Đức'),
('TR03', N'Trạm Ga Ngầm Bến Thành', N'Công trường Quách Thị Trang', N'Quận 1'),
('TR04', N'Trạm Tân Cảng - Landmark 81', N'Điện Biên Phủ, Phường 22', N'Bình Thạnh'),
('TR05', N'Trạm Bến xe Miền Đông mới', N'Xa lộ Hà Nội, Long Bình', N'Thủ Đức'),
('TR06', N'Trạm Trung tâm Logistics Dĩ An', N'Quốc lộ 1K, Bình An', N'Dĩ An');

-- 3. LOTRINH
-- TX01: qua TR03 (Q1), TR04 (Bình Thạnh), TR01 (Thủ Đức), TR02 (Thủ Đức), TR05 (Thủ Đức) -> Đủ cả 3 trạm Thủ Đức!
-- TX04: qua TR03, TR01, TR02, TR05 -> Đủ cả 3 trạm Thủ Đức!
-- TX03: qua TR03, TR04, TR01, TR02 (thiếu TR05) -> Loại khỏi phép chia
-- TX02: qua TR03 (chỉ 1 trạm) -> Loại
-- TX05: qua TR02, TR03 -> Loại
INSERT INTO LOTRINH (MATUYEN, MATRAM, SOTHUTU, KHOANGCACH_KM) VALUES
-- TX01
('TX01', 'TR03', 1, 0.0),
('TX01', 'TR04', 2, 4.5),
('TX01', 'TR01', 3, 15.2),
('TX01', 'TR02', 4, 17.5),
('TX01', 'TR05', 5, 19.7),
-- TX04
('TX04', 'TR03', 1, 0.0),
('TX04', 'TR01', 2, 16.0),
('TX04', 'TR02', 3, 18.5),
('TX04', 'TR05', 4, 26.0),
-- TX03
('TX03', 'TR03', 1, 0.0),
('TX03', 'TR04', 2, 5.0),
('TX03', 'TR01', 3, 16.5),
('TX03', 'TR02', 4, 19.0),
-- TX02
('TX02', 'TR03', 1, 0.0),
-- TX05
('TX05', 'TR02', 1, 0.0),
('TX05', 'TR03', 2, 22.0);

-- 4. PHUONGTIEN (5 xe/đoàn tàu)
INSERT INTO PHUONGTIEN (MAPT, BIENSO, SOGHE, NAMSX, MATUYEN) VALUES
('PT01', '51B-11111', 40, 2022, 'TX03'), -- Phục vụ TX03 (Bến Thành - Bến xe Miền Đông mới)
('PT02', '51B-22222', 45, 2023, 'TX03'), -- Phục vụ TX03 (Bến Thành - Bến xe Miền Đông mới)
('PT03', '50E-33333', 35, 2024, 'TX04'), -- Phục vụ TX04 (VinBus)
('PT04', '50E-44444', 35, 2024, 'TX05'), -- Phục vụ TX05 (VinBus)
('PT05', 'METRO-01', 150, 2023, 'TX01'); -- Phục vụ TX01 (Metro)

-- 5. TAIXE (4 tài xế)
INSERT INTO TAIXE (MATX, HOTEN, HANG_GPLX, LUONG_CB, MAPT) VALUES
('TXE01', N'Nguyễn Văn Thành', 'Hạng E', 12000000, 'PT03'), -- Lái VinBus -> Tăng 10% = 13.200.000
('TXE02', N'Trần Đình Trọng', 'Hạng E', 14000000, 'PT04'), -- Lái VinBus -> Tăng 10% = 15.400.000
('TXE03', N'Lê Hoàng Phúc', 'Hạng D', 11000000, 'PT01'),   -- Lái Buýt thường -> Giữ nguyên
('TXE04', N'Đỗ Minh Quân', 'Hạng E', 16000000, 'PT05');   -- Lái Metro -> Giữ nguyên

-- 6. CHUYEN_DI (Chuyến đi 2024)
-- Ngày 20/11/2024:
-- PT01: CD01 (85 khách, 595k) + CD02 (95 khách, 665k) = 180 khách
-- PT02: CD03 (110 khách, 770k) = 110 khách
-- PT03: CD04 (90 khách, ngày 21/11, không tính vào 20/11)

-- Doanh thu 2024:
-- TX01 (PT05): CD07 (10.0m) + CD08 (15.0m) = 25.0m
-- TX04 (PT03): CD04 (12.0m) + CD09 (13.0m) = 25.0m -> Tied at 25.0m!
-- TX03 (PT01, PT02): CD01+CD02+CD03 = 2.03m
-- TX05 (PT04): CD05 (8.0m)
INSERT INTO CHUYEN_DI (MACHUYEN, MAPT, NGAYCHAY, GIOXUATPHAT, SOLUONG_KHACH, DOANHTHU) VALUES
-- 20/11/2024
('CD01', 'PT01', '2024-11-20', '06:30:00', 85, 595000),
('CD02', 'PT01', '2024-11-20', '11:30:00', 95, 665000),
('CD03', 'PT02', '2024-11-20', '08:00:00', 110, 770000),
-- Các ngày khác 2024
('CD04', 'PT03', '2024-11-21', '07:00:00', 90, 12000000),
('CD09', 'PT03', '2024-12-05', '16:00:00', 100, 13000000),
('CD05', 'PT04', '2024-10-15', '14:00:00', 70, 8000000),
('CD07', 'PT05', '2024-10-01', '06:00:00', 200, 10000000),
('CD08', 'PT05', '2024-11-01', '17:30:00', 250, 15000000);
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 2: QUESTION 2.1B UPDATE QUERY                   ===';
PRINT '------------------------------------------------------------';

-- Update 10% salary for VinBus drivers
UPDATE TAIXE
SET LUONG_CB = LUONG_CB * 1.10
FROM TAIXE tx
JOIN PHUONGTIEN pt ON tx.MAPT = pt.MAPT
JOIN TUYEN_XE tx_route ON pt.MATUYEN = tx_route.MATUYEN
WHERE tx_route.LOAI_HINH = N'Xe buýt điện VinBus';

-- Assertions: TXE01 (12m -> 13.2m), TXE02 (14m -> 15.4m), TXE03 (11m unchanged)
DECLARE @tx01_sal DECIMAL(18,2), @tx02_sal DECIMAL(18,2), @tx03_sal DECIMAL(18,2);
SELECT @tx01_sal = LUONG_CB FROM TAIXE WHERE MATX = 'TXE01';
SELECT @tx02_sal = LUONG_CB FROM TAIXE WHERE MATX = 'TXE02';
SELECT @tx03_sal = LUONG_CB FROM TAIXE WHERE MATX = 'TXE03';

IF @tx01_sal = 13200000 AND @tx02_sal = 15400000 AND @tx03_sal = 11000000
    PRINT '  [PASS] Test 2: Salaries verified: TXE01=13.2m (+10%), TXE02=15.4m (+10%), TXE03=11m (unchanged).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 2 mismatch: TXE01=' + CAST(@tx01_sal AS VARCHAR) + ', TXE02=' + CAST(@tx02_sal AS VARCHAR);
    THROW 50010, 'Test 2 FAILED', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 3: QUESTION 2.2A SELECTION QUERY                ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2a: Metro routes >= 15 km
DECLARE @cnt3 INT;
SELECT @cnt3 = COUNT(*)
FROM TUYEN_XE
WHERE LOAI_HINH = N'Tuyến Metro'
  AND CULY_KM >= 15;

IF @cnt3 = 1
    PRINT '  [PASS] Test 3: Selection returned exactly 1 Metro route >= 15km (TX01).';
ELSE
    THROW 50020, 'Test 3 FAILED: Incorrect count for Metro route selection', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 4: QUESTION 2.2B JOIN QUERY                     ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2b: Vehicles serving 'Bến Thành - Bến xe Miền Đông mới'
DECLARE @cnt4 INT;
SELECT @cnt4 = COUNT(*)
FROM PHUONGTIEN pt
JOIN TUYEN_XE tx ON pt.MATUYEN = tx.MATUYEN
WHERE tx.TENTUYEN = N'Bến Thành - Bến xe Miền Đông mới';

IF @cnt4 = 2
    PRINT '  [PASS] Test 4: Join returned exactly 2 vehicles for Bến xe Miền Đông mới route (PT01, PT02).';
ELSE
    THROW 50030, 'Test 4 FAILED: Incorrect join vehicle count', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 5: QUESTION 2.2C OUTER JOIN QUERY               ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2c: Left Outer Join TRAM_DUNG with LOTRINH
DECLARE @cnt5_total INT, @cnt5_null INT;
SELECT @cnt5_total = COUNT(*), @cnt5_null = SUM(CASE WHEN lt.MATUYEN IS NULL THEN 1 ELSE 0 END)
FROM TRAM_DUNG td
LEFT JOIN LOTRINH lt ON td.MATRAM = lt.MATRAM;

IF @cnt5_total = 17 AND @cnt5_null = 1
    PRINT '  [PASS] Test 5: Outer join preserved TR06 with NULL route info (total 17 rows, 1 NULL).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 5 count: Total=' + CAST(@cnt5_total AS VARCHAR) + ', Null=' + CAST(@cnt5_null AS VARCHAR);
    THROW 50040, 'Test 5 FAILED: Outer join did not preserve empty stop properly', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE           ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2d: Total passengers on 20/11/2024 by vehicle
-- PT01: 85 + 95 = 180
-- PT02: 110
DECLARE @pax_pt01 INT, @pax_pt02 INT;
SELECT @pax_pt01 = SUM(cd.SOLUONG_KHACH) FROM PHUONGTIEN pt JOIN CHUYEN_DI cd ON pt.MAPT = cd.MAPT WHERE pt.MAPT = 'PT01' AND cd.NGAYCHAY = '2024-11-20';
SELECT @pax_pt02 = SUM(cd.SOLUONG_KHACH) FROM PHUONGTIEN pt JOIN CHUYEN_DI cd ON pt.MAPT = cd.MAPT WHERE pt.MAPT = 'PT02' AND cd.NGAYCHAY = '2024-11-20';

IF @pax_pt01 = 180 AND @pax_pt02 = 110
    PRINT '  [PASS] Test 6: Grouping SUM verified: PT01=180 pax, PT02=110 pax on 20/11/2024.';
ELSE
    THROW 50050, 'Test 6 FAILED: Grouping passenger count calculation mismatch', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION            ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2e: Routes passing all stops in Thủ Đức (TR01, TR02, TR05)
DECLARE @div_not_exists TABLE (MATUYEN VARCHAR(10), TENTUYEN NVARCHAR(100), LOAI_HINH NVARCHAR(50));
INSERT INTO @div_not_exists
SELECT tx.MATUYEN, tx.TENTUYEN, tx.LOAI_HINH
FROM TUYEN_XE tx
WHERE EXISTS (
    SELECT 1 FROM LOTRINH lt
    WHERE lt.MATUYEN = tx.MATUYEN
)
AND NOT EXISTS (
    SELECT 1 FROM TRAM_DUNG td
    WHERE td.QUAN_HUYEN = N'Thủ Đức'
      AND NOT EXISTS (
          SELECT 1 FROM LOTRINH lt2
          WHERE lt2.MATUYEN = tx.MATUYEN
            AND lt2.MATRAM = td.MATRAM
      )
);

DECLARE @div_having TABLE (MATUYEN VARCHAR(10), TENTUYEN NVARCHAR(100), LOAI_HINH NVARCHAR(50));
WITH R AS (
    SELECT DISTINCT MATUYEN, MATRAM FROM LOTRINH
),
S AS (
    SELECT MATRAM FROM TRAM_DUNG WHERE QUAN_HUYEN = N'Thủ Đức'
)
INSERT INTO @div_having
SELECT tx.MATUYEN, tx.TENTUYEN, tx.LOAI_HINH
FROM TUYEN_XE tx
JOIN (
    SELECT R.MATUYEN
    FROM R
    LEFT JOIN S ON R.MATRAM = S.MATRAM
    GROUP BY R.MATUYEN
    HAVING COUNT(DISTINCT S.MATRAM) = (SELECT COUNT(*) FROM S)
) div ON tx.MATUYEN = div.MATUYEN;

-- Verify identical results: TX01 and TX04
DECLARE @diff1 INT, @diff2 INT;
SELECT @diff1 = COUNT(*) FROM (SELECT MATUYEN FROM @div_not_exists EXCEPT SELECT MATUYEN FROM @div_having) t;
SELECT @diff2 = COUNT(*) FROM (SELECT MATUYEN FROM @div_having EXCEPT SELECT MATUYEN FROM @div_not_exists) t;

IF @diff1 = 0 AND @diff2 = 0 AND (SELECT COUNT(*) FROM @div_not_exists) = 2
    PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (TX01, TX04).';
ELSE
    THROW 50060, 'Test 7 FAILED: Relational division discrepancy between formulations', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE ===';
PRINT '------------------------------------------------------------';

-- Adversarial Test 8: Empty target S = Ø (No stop in 'Cần Giờ')
DECLARE @empty_not_exists TABLE (MATUYEN VARCHAR(10));
INSERT INTO @empty_not_exists
SELECT tx.MATUYEN
FROM TUYEN_XE tx
WHERE EXISTS (
    SELECT 1 FROM LOTRINH lt
    WHERE lt.MATUYEN = tx.MATUYEN
)
AND NOT EXISTS (
    SELECT 1 FROM TRAM_DUNG td
    WHERE td.QUAN_HUYEN = N'Cần Giờ'
      AND NOT EXISTS (
          SELECT 1 FROM LOTRINH lt2
          WHERE lt2.MATUYEN = tx.MATUYEN
            AND lt2.MATRAM = td.MATRAM
      )
);

DECLARE @empty_having TABLE (MATUYEN VARCHAR(10));
WITH R AS (
    SELECT DISTINCT MATUYEN, MATRAM FROM LOTRINH
),
S AS (
    SELECT MATRAM FROM TRAM_DUNG WHERE QUAN_HUYEN = N'Cần Giờ'
)
INSERT INTO @empty_having
SELECT tx.MATUYEN
FROM TUYEN_XE tx
JOIN (
    SELECT R.MATUYEN
    FROM R
    LEFT JOIN S ON R.MATRAM = S.MATRAM
    GROUP BY R.MATUYEN
    HAVING COUNT(DISTINCT S.MATRAM) = (SELECT COUNT(*) FROM S)
) div ON tx.MATUYEN = div.MATUYEN;

-- All routes with at least 1 stop in LOTRINH (TX01, TX02, TX03, TX04, TX05 = 5 routes)
DECLARE @ediff1 INT, @ediff2 INT;
SELECT @ediff1 = COUNT(*) FROM (SELECT MATUYEN FROM @empty_not_exists EXCEPT SELECT MATUYEN FROM @empty_having) t;
SELECT @ediff2 = COUNT(*) FROM (SELECT MATUYEN FROM @empty_having EXCEPT SELECT MATUYEN FROM @empty_not_exists) t;

IF @ediff1 = 0 AND @ediff2 = 0 AND (SELECT COUNT(*) FROM @empty_not_exists) = 5
    PRINT '  [PASS] Test 8: Empty target S=Ø verified with EXCEPT set comparison: RA, NOT EXISTS and HAVING COUNT identical (5 routes).';
ELSE
    THROW 50070, 'Test 8 FAILED: Empty target division discrepancy', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING           ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2f: Routes tied with MAX trip revenue in 2024
-- Both TX01 and TX04 have exactly 25,000,000 VND
DECLARE @max_routes TABLE (MATUYEN VARCHAR(10), TENTUYEN NVARCHAR(100), LOAI_HINH NVARCHAR(50), TONG_DOANHTHU DECIMAL(18,2));
WITH ThongKe AS (
    SELECT pt.MATUYEN, SUM(cd.DOANHTHU) AS TONG_DOANHTHU
    FROM PHUONGTIEN pt
    JOIN CHUYEN_DI cd ON pt.MAPT = cd.MAPT
    WHERE cd.NGAYCHAY >= '2024-01-01'
      AND cd.NGAYCHAY <= '2024-12-31'
    GROUP BY pt.MATUYEN
)
INSERT INTO @max_routes
SELECT tx.MATUYEN, tx.TENTUYEN, tx.LOAI_HINH, tk.TONG_DOANHTHU
FROM TUYEN_XE tx
JOIN ThongKe tk ON tx.MATUYEN = tk.MATUYEN
WHERE tk.TONG_DOANHTHU = (SELECT MAX(TONG_DOANHTHU) FROM ThongKe);

DECLARE @max_cnt INT;
DECLARE @min_rev DECIMAL(18,2);
SELECT @max_cnt = COUNT(*), @min_rev = MIN(TONG_DOANHTHU) FROM @max_routes;

IF @max_cnt = 2 AND @min_rev = 25000000
    PRINT '  [PASS] Test 9: Extreme tie-breaking verified: TX01 (25m) and TX04 (25m) preserved; others excluded.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 9: Count=' + CAST(@max_cnt AS VARCHAR) + ', Min=' + CAST(@min_rev AS VARCHAR);
    THROW 50080, 'Test 9 FAILED: Extreme tie-breaking did not preserve tied records', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== ALL 9 MOCK-13 VERIFICATION SUITES PASSED WITH ASSERTIONS ===';
PRINT '------------------------------------------------------------';
