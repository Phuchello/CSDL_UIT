-- =============================================================================
-- FIXTURE & ADVERSARIAL VERIFICATION SCRIPT: MOCK-12
-- Domain: Quản Lý Cụm Rạp Chiếu Phim & Đặt Vé Trực Tuyến
-- Profile: RECENT_VERIFIED (10.0 pts, 75 mins)
-- Engine: Microsoft SQL Server 2025 / Azure SQL
-- Author: VÕ TRỌNG PHÚC — CSDL_UIT Master Series
-- =============================================================================

SET NOCOUNT ON;
USE master;
GO

IF DB_ID('Mock12_Cinema_DB') IS NOT NULL
BEGIN
    ALTER DATABASE Mock12_Cinema_DB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE Mock12_Cinema_DB;
END
GO

CREATE DATABASE Mock12_Cinema_DB COLLATE Vietnamese_CI_AS;
GO

USE Mock12_Cinema_DB;
GO

PRINT '============================================================';
PRINT '=== MOCK-12: CREATING TABLES WITH INTEGRITY CONSTRAINTS   ===';
PRINT '============================================================';

-- 1. CUMRAP
CREATE TABLE CUMRAP (
    MACR VARCHAR(10) NOT NULL PRIMARY KEY,
    TENCR NVARCHAR(100) NOT NULL,
    DIACHI NVARCHAR(200) NOT NULL,
    THANHPHO NVARCHAR(50) NOT NULL
);

-- 2. PHONGCHIEU
CREATE TABLE PHONGCHIEU (
    MAPC VARCHAR(10) NOT NULL PRIMARY KEY,
    TENPHONG NVARCHAR(50) NOT NULL,
    SOGHETOI_DA INT NOT NULL CHECK (SOGHETOI_DA > 0),
    LOAIPHONG NVARCHAR(30) NOT NULL,
    MACR VARCHAR(10) NOT NULL REFERENCES CUMRAP(MACR)
);

-- 3. PHIM
CREATE TABLE PHIM (
    MAPHIM VARCHAR(10) NOT NULL PRIMARY KEY,
    TENPHIM NVARCHAR(100) NOT NULL,
    THELOAI NVARCHAR(50) NOT NULL,
    THOILUONG INT NOT NULL CHECK (THOILUONG > 0),
    DAODIEN NVARCHAR(50) NOT NULL,
    NAMSX INT NOT NULL CHECK (NAMSX >= 1900)
);

-- 4. SUATCHIEU
CREATE TABLE SUATCHIEU (
    MASC VARCHAR(10) NOT NULL PRIMARY KEY,
    MAPHIM VARCHAR(10) NOT NULL REFERENCES PHIM(MAPHIM),
    MAPC VARCHAR(10) NOT NULL REFERENCES PHONGCHIEU(MAPC),
    NGAYCHIEU DATE NOT NULL,
    GIOCHIEU TIME NOT NULL,
    GIAVE_CHUAN DECIMAL(18, 2) NOT NULL CHECK (GIAVE_CHUAN > 0)
);

-- 5. KHACHHANG
CREATE TABLE KHACHHANG (
    MAKH VARCHAR(10) NOT NULL PRIMARY KEY,
    HOTEN NVARCHAR(50) NOT NULL,
    SDT VARCHAR(15) NOT NULL,
    EMAIL VARCHAR(50) NOT NULL,
    LOAITHANHVIEN NVARCHAR(20) NOT NULL
);

-- 6. VEXEM
CREATE TABLE VEXEM (
    MAVE VARCHAR(10) NOT NULL PRIMARY KEY,
    MASC VARCHAR(10) NOT NULL REFERENCES SUATCHIEU(MASC),
    MAKH VARCHAR(10) NOT NULL REFERENCES KHACHHANG(MAKH),
    SOGHE VARCHAR(10) NOT NULL,
    GIAVE_THUC DECIMAL(18, 2) NOT NULL,
    TRANGTHAI NVARCHAR(30) NOT NULL
);
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: QUESTION 2.1A CHECK & NOT NULL INTEGRITY     ===';
PRINT '------------------------------------------------------------';

-- Add Question 2.1a constraints
ALTER TABLE VEXEM
ADD CONSTRAINT CK_VEXEM_GIAVE CHECK (GIAVE_THUC > 0);

ALTER TABLE VEXEM
ADD CONSTRAINT CK_VEXEM_TRANGTHAI CHECK (TRANGTHAI IN (N'Đã thanh toán', N'Đã hủy', N'Đang giữ chỗ'));
GO

-- Seed minimal parent data for constraint adversarial tests
INSERT INTO CUMRAP (MACR, TENCR, DIACHI, THANHPHO) VALUES
('CR01', N'CGV Landmark 81', N'Vinhomes Central Park, Bình Thạnh', N'TP.HCM');

INSERT INTO PHONGCHIEU (MAPC, TENPHONG, SOGHETOI_DA, LOAIPHONG, MACR) VALUES
('PC01', N'Phòng 01 - IMAX Laser', 250, N'3D IMAX', 'CR01');

INSERT INTO PHIM (MAPHIM, TENPHIM, THELOAI, THOILUONG, DAODIEN, NAMSX) VALUES
('P01', N'Dune: Phần Hai', N'Khoa học viễn tưởng', 166, N'Denis Villeneuve', 2024);

INSERT INTO SUATCHIEU (MASC, MAPHIM, MAPC, NGAYCHIEU, GIOCHIEU, GIAVE_CHUAN) VALUES
('SC01', 'P01', 'PC01', '2024-11-15', '19:30:00', 150000);

INSERT INTO KHACHHANG (MAKH, HOTEN, SDT, EMAIL, LOAITHANHVIEN) VALUES
('KH01', N'Nguyễn Hoàng Long', '0901112233', 'long@gmail.com', N'VIP');
GO

-- Adversarial Test 1A: Non-positive price
BEGIN TRY
    INSERT INTO VEXEM (MAVE, MASC, MAKH, SOGHE, GIAVE_THUC, TRANGTHAI)
    VALUES ('VX_TEST1', 'SC01', 'KH01', 'A01', 0, N'Đã thanh toán');
    THROW 50001, 'Test 1A FAILED: Zero ticket price was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_VEXEM_GIAVE%'
        PRINT '  [PASS] Test 1A: CK_VEXEM_GIAVE correctly blocked zero GIAVE_THUC.';
    ELSE
    BEGIN
        DECLARE @err1 NVARCHAR(400) = ERROR_MESSAGE();
        PRINT '  [FAIL] Test 1A unexpected error: ' + @err1;
        THROW 50002, @err1, 1;
    END
END CATCH;

-- Adversarial Test 1B: Invalid status
BEGIN TRY
    INSERT INTO VEXEM (MAVE, MASC, MAKH, SOGHE, GIAVE_THUC, TRANGTHAI)
    VALUES ('VX_TEST2', 'SC01', 'KH01', 'A02', 120000, N'Đã chuyển tiền');
    THROW 50003, 'Test 1B FAILED: Invalid status was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_VEXEM_TRANGTHAI%'
        PRINT '  [PASS] Test 1B: CK_VEXEM_TRANGTHAI correctly blocked invalid status.';
    ELSE
    BEGIN
        DECLARE @err2 NVARCHAR(400) = ERROR_MESSAGE();
        PRINT '  [FAIL] Test 1B unexpected error: ' + @err2;
        THROW 50004, @err2, 1;
    END
END CATCH;

-- Adversarial Test 1C: NULL policy
BEGIN TRY
    INSERT INTO VEXEM (MAVE, MASC, MAKH, SOGHE, GIAVE_THUC, TRANGTHAI)
    VALUES ('VX_TEST3', 'SC01', 'KH01', 'A03', NULL, N'Đã thanh toán');
    THROW 50005, 'Test 1C FAILED: NULL GIAVE_THUC was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] Test 1C: NOT NULL policy correctly rejected NULL GIAVE_THUC (Error 515).';
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

-- Clear minimal seed
DELETE FROM VEXEM;
DELETE FROM SUATCHIEU;
DELETE FROM PHIM;
DELETE FROM PHONGCHIEU;
DELETE FROM CUMRAP;
DELETE FROM KHACHHANG;

-- 1. CUMRAP (4 cụm rạp: CR01, CR02, CR03 có phòng chiếu; CR04 mới mở chưa có phòng chiếu)
INSERT INTO CUMRAP (MACR, TENCR, DIACHI, THANHPHO) VALUES
('CR01', N'CGV Landmark 81', N'Tầng B1, TTTM Landmark 81, Bình Thạnh', N'TP.HCM'),
('CR02', N'CGV Vincom Đồng Khởi', N'Tầng 3, 72 Lê Thánh Tôn, Quận 1', N'TP.HCM'),
('CR03', N'CGV Aeon Mall Bình Tân', N'Tầng 3, Số 1 Đường 17A, Bình Tân', N'TP.HCM'),
('CR04', N'CGV Vincom Cần Thơ', N'Số 2 Hùng Vương, Ninh Kiều', N'Cần Thơ');

-- 2. PHONGCHIEU (5 phòng chiếu)
INSERT INTO PHONGCHIEU (MAPC, TENPHONG, SOGHETOI_DA, LOAIPHONG, MACR) VALUES
('PC01', N'Phòng 01 - IMAX Laser', 250, N'3D IMAX', 'CR01'),
('PC02', N'Phòng 02 - Gold Class', 60, N'4DX Gold', 'CR01'),
('PC03', N'Phòng Cinema 01', 180, N'2D Standard', 'CR02'),
('PC04', N'Phòng Cinema 02', 150, N'2D Standard', 'CR02'),
('PC05', N'Phòng Starium 01', 300, N'3D IMAX', 'CR03');

-- 3. PHIM (6 phim)
-- P01: Khoa học viễn tưởng, 166p (>= 120)
-- P02: Khoa học viễn tưởng, 169p (>= 120)
-- P03: Kinh dị, 112p
-- P04: Kinh dị, 90p
-- P05: Hoạt hình, 95p
-- P06: Hành động, 148p
INSERT INTO PHIM (MAPHIM, TENPHIM, THELOAI, THOILUONG, DAODIEN, NAMSX) VALUES
('P01', N'Dune: Phần Hai', N'Khoa học viễn tưởng', 166, N'Denis Villeneuve', 2024),
('P02', N'Interstellar Tái Khởi Chiếu', N'Khoa học viễn tưởng', 169, N'Christopher Nolan', 2024),
('P03', N'Ám Ảnh Kinh Hoàng', N'Kinh dị', 112, N'James Wan', 2023),
('P04', N'Vùng Đất Câm Lặng: Ngày Một', N'Kinh dị', 90, N'Michael Sarnoski', 2024),
('P05', N'Kẻ Trộm Mặt Trăng 4', N'Hoạt hình', 95, N'Chris Renaud', 2024),
('P06', N'Deadpool & Wolverine', N'Hành động', 148, N'Shawn Levy', 2024);

-- 4. SUATCHIEU (8 suất chiếu)
-- SC01, SC02: Hoạt hình chiếu tháng 12/2024 -> Test 2 UPDATE target
-- SC03: Hoạt hình nhưng chiếu tháng 11/2024 -> Không đổi
-- SC04, SC05: Chiếu tại CR01 trong tháng 11/2024
-- SC06, SC07: Phim Kinh dị (P03, P04)
-- SC08: Chiếu tại CR03
INSERT INTO SUATCHIEU (MASC, MAPHIM, MAPC, NGAYCHIEU, GIOCHIEU, GIAVE_CHUAN) VALUES
('SC01', 'P05', 'PC01', '2024-12-05', '10:00:00', 120000), -- Hoạt hình, 12/2024 -> 108.000
('SC02', 'P05', 'PC03', '2024-12-10', '14:30:00', 100000), -- Hoạt hình, 12/2024 -> 90.000
('SC03', 'P05', 'PC04', '2024-11-20', '18:00:00', 110000), -- Hoạt hình, 11/2024 -> giữ 110.000
('SC04', 'P01', 'PC01', '2024-11-15', '19:30:00', 180000), -- CGV Landmark 81
('SC05', 'P02', 'PC02', '2024-11-18', '21:00:00', 250000), -- CGV Landmark 81
('SC06', 'P03', 'PC03', '2024-10-25', '22:30:00', 95000),  -- Kinh dị P03
('SC07', 'P04', 'PC04', '2024-10-28', '23:00:00', 95000),  -- Kinh dị P04
('SC08', 'P06', 'PC05', '2024-11-22', '20:15:00', 160000);
GO

-- 5. KHACHHANG (5 khách hàng)
INSERT INTO KHACHHANG (MAKH, HOTEN, SDT, EMAIL, LOAITHANHVIEN) VALUES
('KH01', N'Nguyễn Hoàng Long', '0901112233', 'long.nh@gmail.com', N'VIP'),
('KH02', N'Trần Thị Bích Ngọc', '0902223344', 'ngoc.tb@gmail.com', N'Diamond'),
('KH03', N'Lê Minh Tuấn', '0903334455', 'tuan.lm@gmail.com', N'Standard'),
('KH04', N'Phạm Thu Trang', '0904445566', 'trang.pt@gmail.com', N'Standard'),
('KH05', N'Vũ Đình Khang', '0905556677', 'khang.vd@gmail.com', N'VIP');

-- 6. VEXEM (Vé bán)
-- KH01: Mua P03 (SC06, Đã TT) và P04 (SC07, Đã TT) -> Thỏa phép chia Kinh dị
-- KH02: Mua P03 (SC06, Đã TT) và P04 (SC07, Đã TT) -> Thỏa phép chia Kinh dị
-- KH03: Chỉ mua P03 (SC06, Đã TT), thiếu P04 -> Loại khỏi phép chia
-- KH04: Mua P03 (SC06, Đã TT) và P04 (SC07, ĐÃ HỦY) -> Loại khỏi phép chia vì bị hủy
-- KH05: Mua P01 và P06, không xem phim kinh dị -> Loại

-- Doanh thu tháng 11/2024:
-- SC04 (15/11): VX01 (180k, Đã TT) + VX02 (180k, Đã TT) = 360k
-- SC05 (18/11): VX03 (250k, Đã TT) + VX04 (250k, Đã hủy) = 250k
-- SC03 (20/11): VX05 (110k, Đã TT) + VX06 (110k, Đã TT) = 220k
-- SC08 (22/11): VX07 (160k, Đã TT) = 160k

-- Tie-breaking vé bán 2024:
-- P01: 6 vé Đã TT (VX01, VX02, VX13, VX14, VX15, VX16)
-- P02: 6 vé Đã TT (VX03, VX17, VX18, VX19, VX20, VX21) -> Tied at 6!
-- P03: 3 vé Đã TT (VX08, VX09, VX10)
-- P04: 2 vé Đã TT (VX11, VX22)
-- P05: 2 vé Đã TT (VX05, VX06)
-- P06: 1 vé Đã TT (VX07)
INSERT INTO VEXEM (MAVE, MASC, MAKH, SOGHE, GIAVE_THUC, TRANGTHAI) VALUES
-- Suất SC04 (P01) tại CR01 (CGV Landmark 81)
('VX01', 'SC04', 'KH01', 'F01', 180000, N'Đã thanh toán'),
('VX02', 'SC04', 'KH02', 'F02', 180000, N'Đã thanh toán'),
-- Suất SC05 (P02) tại CR01 (CGV Landmark 81)
('VX03', 'SC05', 'KH01', 'A01', 250000, N'Đã thanh toán'),
('VX04', 'SC05', 'KH03', 'A02', 250000, N'Đã hủy'),
-- Suất SC03 (P05) tại CR02
('VX05', 'SC03', 'KH04', 'B05', 110000, N'Đã thanh toán'),
('VX06', 'SC03', 'KH05', 'B06', 110000, N'Đã thanh toán'),
-- Suất SC08 (P06) tại CR03
('VX07', 'SC08', 'KH05', 'H10', 160000, N'Đã thanh toán'),
-- Suất SC06 (P03 - Kinh dị 1)
('VX08', 'SC06', 'KH01', 'E01', 95000, N'Đã thanh toán'),
('VX09', 'SC06', 'KH02', 'E02', 95000, N'Đã thanh toán'),
('VX10', 'SC06', 'KH03', 'E03', 95000, N'Đã thanh toán'),
-- Suất SC07 (P04 - Kinh dị 2)
('VX11', 'SC07', 'KH01', 'E04', 95000, N'Đã thanh toán'),
('VX12', 'SC07', 'KH04', 'E05', 95000, N'Đã hủy'),
('VX22', 'SC07', 'KH02', 'E06', 95000, N'Đã thanh toán'),
-- Bổ sung thêm vé cho P01 để đạt 6 vé
('VX13', 'SC04', 'KH03', 'F03', 180000, N'Đã thanh toán'),
('VX14', 'SC04', 'KH04', 'F04', 180000, N'Đã thanh toán'),
('VX15', 'SC04', 'KH05', 'F05', 180000, N'Đã thanh toán'),
('VX16', 'SC04', 'KH01', 'F06', 180000, N'Đã thanh toán'),
-- Bổ sung thêm vé cho P02 để đạt 6 vé (đồng hạng MAX)
('VX17', 'SC05', 'KH02', 'A03', 250000, N'Đã thanh toán'),
('VX18', 'SC05', 'KH03', 'A04', 250000, N'Đã thanh toán'),
('VX19', 'SC05', 'KH04', 'A05', 250000, N'Đã thanh toán'),
('VX20', 'SC05', 'KH05', 'A06', 250000, N'Đã thanh toán'),
('VX21', 'SC05', 'KH01', 'A07', 250000, N'Đã thanh toán');
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 2: QUESTION 2.1B UPDATE QUERY                   ===';
PRINT '------------------------------------------------------------';

-- Update 10% discount for Animated films in Dec 2024
UPDATE SUATCHIEU
SET GIAVE_CHUAN = GIAVE_CHUAN * 0.90
FROM SUATCHIEU sc
JOIN PHIM p ON sc.MAPHIM = p.MAPHIM
WHERE p.THELOAI = N'Hoạt hình'
  AND sc.NGAYCHIEU >= '2024-12-01'
  AND sc.NGAYCHIEU <= '2024-12-31';

-- Assertions: SC01 (120k -> 108k), SC02 (100k -> 90k), SC03 (110k unchanged)
DECLARE @sc01_price DECIMAL(18,2), @sc02_price DECIMAL(18,2), @sc03_price DECIMAL(18,2);
SELECT @sc01_price = GIAVE_CHUAN FROM SUATCHIEU WHERE MASC = 'SC01';
SELECT @sc02_price = GIAVE_CHUAN FROM SUATCHIEU WHERE MASC = 'SC02';
SELECT @sc03_price = GIAVE_CHUAN FROM SUATCHIEU WHERE MASC = 'SC03';

IF @sc01_price = 108000 AND @sc02_price = 90000 AND @sc03_price = 110000
    PRINT '  [PASS] Test 2: Standard prices verified: SC01=108k (-10%), SC02=90k (-10%), SC03=110k (unchanged).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 2 mismatch: SC01=' + CAST(@sc01_price AS VARCHAR) + ', SC02=' + CAST(@sc02_price AS VARCHAR);
    THROW 50010, 'Test 2 FAILED', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 3: QUESTION 2.2A SELECTION QUERY                ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2a: Sci-Fi films >= 120 mins
DECLARE @cnt3 INT;
SELECT @cnt3 = COUNT(*)
FROM PHIM
WHERE THELOAI = N'Khoa học viễn tưởng'
  AND THOILUONG >= 120;

IF @cnt3 = 2
    PRINT '  [PASS] Test 3: Selection returned exactly 2 Sci-Fi films >= 120 mins (P01, P02).';
ELSE
    THROW 50020, 'Test 3 FAILED: Incorrect count for Sci-Fi selection', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 4: QUESTION 2.2B JOIN QUERY                     ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2b: Tickets at CGV Landmark 81
-- SC04 has 6 tickets (VX01, VX02, VX13, VX14, VX15, VX16)
-- SC05 has 6 tickets (VX03, VX04, VX17, VX18, VX19, VX20, VX21) -> total 13 tickets
DECLARE @cnt4 INT;
SELECT @cnt4 = COUNT(*)
FROM VEXEM vx
JOIN SUATCHIEU sc ON vx.MASC = sc.MASC
JOIN PHONGCHIEU pc ON sc.MAPC = pc.MAPC
JOIN CUMRAP cr ON pc.MACR = cr.MACR
WHERE cr.TENCR = N'CGV Landmark 81';

IF @cnt4 = 13
    PRINT '  [PASS] Test 4: Join returned exactly 13 tickets at CGV Landmark 81.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 4 count: ' + CAST(@cnt4 AS VARCHAR);
    THROW 50030, 'Test 4 FAILED: Incorrect join ticket count', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 5: QUESTION 2.2C OUTER JOIN QUERY               ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2c: Left Outer Join CUMRAP with PHONGCHIEU
DECLARE @cnt5_total INT, @cnt5_null INT;
SELECT @cnt5_total = COUNT(*), @cnt5_null = SUM(CASE WHEN pc.MAPC IS NULL THEN 1 ELSE 0 END)
FROM CUMRAP cr
LEFT JOIN PHONGCHIEU pc ON cr.MACR = pc.MACR;

IF @cnt5_total = 6 AND @cnt5_null = 1
    PRINT '  [PASS] Test 5: Outer join preserved CR04 with NULL room info (total 6 rows, 1 NULL).';
ELSE
    THROW 50040, 'Test 5 FAILED: Outer join did not preserve empty complex properly', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE           ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2d: Grouping SUM for Nov 2024 shows with 'Đã thanh toán'
-- SC04: 6 tickets * 180k = 1,080,000
-- SC05: 6 paid tickets * 250k = 1,500,000 (VX04 is cancelled, excluded)
-- SC03: 2 tickets * 110k = 220,000
-- SC08: 1 ticket * 160k = 160,000
DECLARE @rev_sc04 DECIMAL(18,2), @rev_sc05 DECIMAL(18,2);
SELECT @rev_sc04 = SUM(vx.GIAVE_THUC) FROM SUATCHIEU sc JOIN VEXEM vx ON sc.MASC = vx.MASC WHERE sc.MASC = 'SC04' AND vx.TRANGTHAI = N'Đã thanh toán';
SELECT @rev_sc05 = SUM(vx.GIAVE_THUC) FROM SUATCHIEU sc JOIN VEXEM vx ON sc.MASC = vx.MASC WHERE sc.MASC = 'SC05' AND vx.TRANGTHAI = N'Đã thanh toán';

IF @rev_sc04 = 1080000 AND @rev_sc05 = 1500000
    PRINT '  [PASS] Test 6: Grouping SUM verified: SC04=1.08m, SC05=1.50m (excluded cancelled VX04).';
ELSE
    THROW 50050, 'Test 6 FAILED: Grouping revenue calculation mismatch', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION            ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2e: Relational division (Customers bought all Horror movies)
-- Double NOT EXISTS bounded to candidate customers
DECLARE @div_not_exists TABLE (MAKH VARCHAR(10), HOTEN NVARCHAR(50), SDT VARCHAR(15));
INSERT INTO @div_not_exists
SELECT kh.MAKH, kh.HOTEN, kh.SDT
FROM KHACHHANG kh
WHERE EXISTS (
    SELECT 1 FROM VEXEM vx
    WHERE vx.MAKH = kh.MAKH AND vx.TRANGTHAI = N'Đã thanh toán'
)
AND NOT EXISTS (
    SELECT 1 FROM PHIM p
    WHERE p.THELOAI = N'Kinh dị'
      AND NOT EXISTS (
          SELECT 1 FROM VEXEM vx2
          JOIN SUATCHIEU sc2 ON vx2.MASC = sc2.MASC
          WHERE vx2.MAKH = kh.MAKH
            AND sc2.MAPHIM = p.MAPHIM
            AND vx2.TRANGTHAI = N'Đã thanh toán'
      )
);

-- Alternative HAVING COUNT formulation
DECLARE @div_having TABLE (MAKH VARCHAR(10), HOTEN NVARCHAR(50), SDT VARCHAR(15));
WITH R AS (
    SELECT DISTINCT vx.MAKH, sc.MAPHIM
    FROM VEXEM vx
    JOIN SUATCHIEU sc ON vx.MASC = sc.MASC
    WHERE vx.TRANGTHAI = N'Đã thanh toán'
),
S AS (
    SELECT MAPHIM FROM PHIM WHERE THELOAI = N'Kinh dị'
)
INSERT INTO @div_having
SELECT kh.MAKH, kh.HOTEN, kh.SDT
FROM KHACHHANG kh
JOIN (
    SELECT R.MAKH
    FROM R
    LEFT JOIN S ON R.MAPHIM = S.MAPHIM
    GROUP BY R.MAKH
    HAVING COUNT(DISTINCT S.MAPHIM) = (SELECT COUNT(*) FROM S)
) d ON kh.MAKH = d.MAKH;

-- Verify identical results: KH01 and KH02
DECLARE @diff1 INT, @diff2 INT;
SELECT @diff1 = COUNT(*) FROM (SELECT MAKH FROM @div_not_exists EXCEPT SELECT MAKH FROM @div_having) t;
SELECT @diff2 = COUNT(*) FROM (SELECT MAKH FROM @div_having EXCEPT SELECT MAKH FROM @div_not_exists) t;

IF @diff1 = 0 AND @diff2 = 0 AND (SELECT COUNT(*) FROM @div_not_exists) = 2
    PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (KH01, KH02).';
ELSE
    THROW 50060, 'Test 7 FAILED: Relational division discrepancy between formulations', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE ===';
PRINT '------------------------------------------------------------';

-- Adversarial Test 8: Empty target S = Ø (No film with genre 'Phim tài liệu')
DECLARE @empty_not_exists TABLE (MAKH VARCHAR(10));
INSERT INTO @empty_not_exists
SELECT kh.MAKH
FROM KHACHHANG kh
WHERE EXISTS (
    SELECT 1 FROM VEXEM vx
    WHERE vx.MAKH = kh.MAKH AND vx.TRANGTHAI = N'Đã thanh toán'
)
AND NOT EXISTS (
    SELECT 1 FROM PHIM p
    WHERE p.THELOAI = N'Phim tài liệu'
      AND NOT EXISTS (
          SELECT 1 FROM VEXEM vx2
          JOIN SUATCHIEU sc2 ON vx2.MASC = sc2.MASC
          WHERE vx2.MAKH = kh.MAKH
            AND sc2.MAPHIM = p.MAPHIM
            AND vx2.TRANGTHAI = N'Đã thanh toán'
      )
);

DECLARE @empty_having TABLE (MAKH VARCHAR(10));
WITH R AS (
    SELECT DISTINCT vx.MAKH, sc.MAPHIM
    FROM VEXEM vx
    JOIN SUATCHIEU sc ON vx.MASC = sc.MASC
    WHERE vx.TRANGTHAI = N'Đã thanh toán'
),
S AS (
    SELECT MAPHIM FROM PHIM WHERE THELOAI = N'Phim tài liệu'
)
INSERT INTO @empty_having
SELECT kh.MAKH
FROM KHACHHANG kh
JOIN (
    SELECT R.MAKH
    FROM R
    LEFT JOIN S ON R.MAPHIM = S.MAPHIM
    GROUP BY R.MAKH
    HAVING COUNT(DISTINCT S.MAPHIM) = (SELECT COUNT(*) FROM S)
) d ON kh.MAKH = d.MAKH;

-- All customers who have ever bought a paid ticket (KH01, KH02, KH03, KH04, KH05 = 5 customers)
DECLARE @ediff1 INT, @ediff2 INT;
SELECT @ediff1 = COUNT(*) FROM (SELECT MAKH FROM @empty_not_exists EXCEPT SELECT MAKH FROM @empty_having) t;
SELECT @ediff2 = COUNT(*) FROM (SELECT MAKH FROM @empty_having EXCEPT SELECT MAKH FROM @empty_not_exists) t;

IF @ediff1 = 0 AND @ediff2 = 0 AND (SELECT COUNT(*) FROM @empty_not_exists) = 5
    PRINT '  [PASS] Test 8: Empty target S=Ø verified with EXCEPT set comparison: RA, NOT EXISTS and HAVING COUNT identical (5 customers).';
ELSE
    THROW 50070, 'Test 8 FAILED: Empty target division discrepancy', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING           ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2f: Movies tied with MAX paid tickets in 2024
-- Both P01 and P02 have exactly 6 paid tickets in 2024
DECLARE @max_movies TABLE (MAPHIM VARCHAR(10), TENPHIM NVARCHAR(100), THELOAI NVARCHAR(50), TONG_VE INT);
WITH ThongKe AS (
    SELECT sc.MAPHIM, COUNT(vx.MAVE) AS TONG_VE
    FROM SUATCHIEU sc
    JOIN VEXEM vx ON sc.MASC = vx.MASC
    WHERE sc.NGAYCHIEU >= '2024-01-01'
      AND sc.NGAYCHIEU <= '2024-12-31'
      AND vx.TRANGTHAI = N'Đã thanh toán'
    GROUP BY sc.MAPHIM
)
INSERT INTO @max_movies
SELECT p.MAPHIM, p.TENPHIM, p.THELOAI, tk.TONG_VE
FROM PHIM p
JOIN ThongKe tk ON p.MAPHIM = tk.MAPHIM
WHERE tk.TONG_VE = (SELECT MAX(TONG_VE) FROM ThongKe);

DECLARE @max_cnt INT, @min_cnt INT;
SELECT @max_cnt = COUNT(*), @min_cnt = MIN(TONG_VE) FROM @max_movies;

IF @max_cnt = 2 AND @min_cnt = 6
    PRINT '  [PASS] Test 9: Extreme tie-breaking verified: P01 (6 tickets) and P02 (6 tickets) preserved; others excluded.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 9: Count=' + CAST(@max_cnt AS VARCHAR) + ', Min=' + CAST(@min_cnt AS VARCHAR);
    THROW 50080, 'Test 9 FAILED: Extreme tie-breaking did not preserve tied records', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== ALL 9 MOCK-12 VERIFICATION SUITES PASSED WITH ASSERTIONS ===';
PRINT '------------------------------------------------------------';
