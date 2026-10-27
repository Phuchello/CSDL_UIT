-- =============================================================================
-- FIXTURE & ADVERSARIAL VERIFICATION SCRIPT: MOCK-15
-- Domain: Quản Lý Trại Cứu Hộ Động Vật Hoang Dã
-- Profile: RECENT_VERIFIED (10.0 pts, 75 mins)
-- Engine: Microsoft SQL Server 2025 / Azure SQL
-- Author: VÕ TRỌNG PHÚC — CSDL_UIT Master Series
-- =============================================================================

SET NOCOUNT ON;
USE master;
GO

IF DB_ID('Mock15_Wildlife_DB') IS NOT NULL
BEGIN
    ALTER DATABASE Mock15_Wildlife_DB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE Mock15_Wildlife_DB;
END
GO

CREATE DATABASE Mock15_Wildlife_DB COLLATE Vietnamese_CI_AS;
GO

USE Mock15_Wildlife_DB;
GO

PRINT '============================================================';
PRINT '=== MOCK-15: CREATING TABLES WITH INTEGRITY CONSTRAINTS   ===';
PRINT '============================================================';

-- 1. KHU_BAOTON
CREATE TABLE KHU_BAOTON (
    MAKHU VARCHAR(10) NOT NULL PRIMARY KEY,
    TENKHU NVARCHAR(100) NOT NULL,
    DIENTICH_HA DECIMAL(8, 2) NOT NULL CHECK (DIENTICH_HA > 0),
    NGUOI_PHUTRACH NVARCHAR(50) NOT NULL
);

-- 2. LOAI_DONGVAT
CREATE TABLE LOAI_DONGVAT (
    MALOAI VARCHAR(10) NOT NULL PRIMARY KEY,
    TENLOAI NVARCHAR(100) NOT NULL,
    TEN_KHOAHOC NVARCHAR(100) NOT NULL,
    MUC_NGUYCAP NVARCHAR(50) NOT NULL
);

-- 3. DONGVAT
CREATE TABLE DONGVAT (
    MADV VARCHAR(10) NOT NULL PRIMARY KEY,
    MALOAI VARCHAR(10) NOT NULL REFERENCES LOAI_DONGVAT(MALOAI),
    GIOITINH NVARCHAR(10) NOT NULL,
    CANNANG_KG DECIMAL(6, 2) NOT NULL,
    TINHTRANG_SK NVARCHAR(50) NOT NULL,
    MAKHU VARCHAR(10) NOT NULL REFERENCES KHU_BAOTON(MAKHU)
);

-- 4. NHANVIEN
CREATE TABLE NHANVIEN (
    MANV VARCHAR(10) NOT NULL PRIMARY KEY,
    HOTEN NVARCHAR(50) NOT NULL,
    CHUYENMON NVARCHAR(50) NOT NULL,
    LUONG DECIMAL(18, 2) NOT NULL CHECK (LUONG > 0),
    MAKHU VARCHAR(10) NOT NULL REFERENCES KHU_BAOTON(MAKHU)
);

-- 5. CHITIET_CS
CREATE TABLE CHITIET_CS (
    MACS VARCHAR(10) NOT NULL PRIMARY KEY,
    MADV VARCHAR(10) NOT NULL REFERENCES DONGVAT(MADV),
    MANV VARCHAR(10) NOT NULL REFERENCES NHANVIEN(MANV),
    NGAYCS DATE NOT NULL,
    CHIPHI_CS DECIMAL(18, 2) NOT NULL,
    GHI_CHU NVARCHAR(200) NOT NULL
);

-- 6. DOT_TAITHA
CREATE TABLE DOT_TAITHA (
    MADOT VARCHAR(10) NOT NULL PRIMARY KEY,
    MADV VARCHAR(10) NOT NULL REFERENCES DONGVAT(MADV),
    NGAYTHA DATE NOT NULL,
    DIADIEM_THA NVARCHAR(200) NOT NULL,
    TRANGTHAI NVARCHAR(50) NOT NULL
);
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: QUESTION 2.1A CHECK & NOT NULL INTEGRITY     ===';
PRINT '------------------------------------------------------------';

-- Add Question 2.1a constraints
ALTER TABLE CHITIET_CS
ADD CONSTRAINT CK_CHITIETCS_CHIPHI CHECK (CHIPHI_CS >= 0);

ALTER TABLE DONGVAT
ADD CONSTRAINT CK_DONGVAT_CANNANG CHECK (CANNANG_KG > 0);
GO

-- Seed minimal parent data for constraint adversarial tests
INSERT INTO KHU_BAOTON (MAKHU, TENKHU, DIENTICH_HA, NGUOI_PHUTRACH) VALUES
('KB01', N'Khu Cứu Hộ Thú Lớn', 50.0, N'Trần Văn Nam');

INSERT INTO LOAI_DONGVAT (MALOAI, TENLOAI, TEN_KHOAHOC, MUC_NGUYCAP) VALUES
('L01', N'Tê tê Java', N'Manis javanica', N'Cực kỳ nguy cấp');

INSERT INTO DONGVAT (MADV, MALOAI, GIOITINH, CANNANG_KG, TINHTRANG_SK, MAKHU) VALUES
('DV01', 'L01', N'Đực', 4.5, N'Đang điều trị', 'KB01');

INSERT INTO NHANVIEN (MANV, HOTEN, CHUYENMON, LUONG, MAKHU) VALUES
('NV01', N'Lê Minh Tuấn', N'Bác sĩ thú y', 18000000, 'KB01');
GO

-- Adversarial Test 1A: Negative care cost
BEGIN TRY
    INSERT INTO CHITIET_CS (MACS, MADV, MANV, NGAYCS, CHIPHI_CS, GHI_CHU)
    VALUES ('CS_TEST1', 'DV01', 'NV01', '2024-10-15', -100000, N'Khám bệnh');
    THROW 50001, 'Test 1A FAILED: Negative care cost was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_CHITIETCS_CHIPHI%'
        PRINT '  [PASS] Test 1A: CK_CHITIETCS_CHIPHI correctly blocked negative care cost.';
    ELSE
    BEGIN
        DECLARE @err1 NVARCHAR(400) = ERROR_MESSAGE();
        PRINT '  [FAIL] Test 1A unexpected error: ' + @err1;
        THROW 50002, @err1, 1;
    END
END CATCH;

-- Adversarial Test 1B: Zero or negative animal weight
BEGIN TRY
    INSERT INTO DONGVAT (MADV, MALOAI, GIOITINH, CANNANG_KG, TINHTRANG_SK, MAKHU)
    VALUES ('DV_TEST2', 'L01', N'Cái', 0, N'Khỏe mạnh', 'KB01');
    THROW 50003, 'Test 1B FAILED: Zero animal weight was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_DONGVAT_CANNANG%'
        PRINT '  [PASS] Test 1B: CK_DONGVAT_CANNANG correctly blocked zero/negative weight.';
    ELSE
    BEGIN
        DECLARE @err2 NVARCHAR(400) = ERROR_MESSAGE();
        PRINT '  [FAIL] Test 1B unexpected error: ' + @err2;
        THROW 50004, @err2, 1;
    END
END CATCH;

-- Adversarial Test 1C: NULL policy
BEGIN TRY
    INSERT INTO DONGVAT (MADV, MALOAI, GIOITINH, CANNANG_KG, TINHTRANG_SK, MAKHU)
    VALUES ('DV_TEST3', 'L01', N'Cái', NULL, N'Khỏe mạnh', 'KB01');
    THROW 50005, 'Test 1C FAILED: NULL weight was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] Test 1C: NOT NULL policy correctly rejected NULL CANNANG_KG (Error 515).';
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

DELETE FROM DOT_TAITHA;
DELETE FROM CHITIET_CS;
DELETE FROM NHANVIEN;
DELETE FROM DONGVAT;
DELETE FROM LOAI_DONGVAT;
DELETE FROM KHU_BAOTON;

-- 1. KHU_BAOTON (4 phân khu: KB01, KB02, KB03 có nhân viên/động vật; KB04 mới mở chưa có nhân viên)
INSERT INTO KHU_BAOTON (MAKHU, TENKHU, DIENTICH_HA, NGUOI_PHUTRACH) VALUES
('KB01', N'Khu Cứu Hộ Thú Lớn', 50.0, N'Trần Văn Nam'),
('KB02', N'Khu Bán Tự Nhiên Cát Tiên', 120.0, N'Nguyễn Thị Lan'),
('KB03', N'Khu Cứu Hộ Linh Trưởng', 30.0, N'Lê Minh Hoàng'),
('KB04', N'Khu Cách Ly Kiểm Dịch Mới', 15.0, N'Phạm Quang Đức');

-- 2. LOAI_DONGVAT (5 loài)
-- L01, L02: Cực kỳ nguy cấp
-- L03, L04: Nguy cấp
-- L05: Sắp nguy cấp
INSERT INTO LOAI_DONGVAT (MALOAI, TENLOAI, TEN_KHOAHOC, MUC_NGUYCAP) VALUES
('L01', N'Voọc chà vá chân nâu', N'Pygathrix nemaeus', N'Cực kỳ nguy cấp'),
('L02', N'Tê tê Java', N'Manis javanica', N'Cực kỳ nguy cấp'),
('L03', N'Gấu ngựa', N'Ursus thibetanus', N'Nguy cấp'),
('L04', N'Vượn đen má vàng', N'Nomascus gabriellae', N'Nguy cấp'),
('L05', N'Khỉ đuôi lợn', N'Macaca leonina', N'Sắp nguy cấp');

-- 3. DONGVAT (8 cá thể)
-- Tê tê Java: DV01, DV02 (2 cá thể)
-- Cá thể thuộc KB02 (Khu Bán Tự Nhiên Cát Tiên): DV01, DV02, DV03
-- KB01 có: DV04, DV05, DV08 -> 3 cá thể
-- KB02 có: DV01, DV02, DV03 -> 3 cá thể -> Tied at 3 animals!
-- KB03 có: DV06, DV07 -> 2 cá thể
INSERT INTO DONGVAT (MADV, MALOAI, GIOITINH, CANNANG_KG, TINHTRANG_SK, MAKHU) VALUES
('DV01', 'L02', N'Đực', 4.5, N'Đang điều trị', 'KB02'), -- Tê tê Java 1 (KB02)
('DV02', 'L02', N'Cái', 3.8, N'Khỏe mạnh', 'KB02'),     -- Tê tê Java 2 (KB02)
('DV03', 'L01', N'Đực', 8.2, N'Chờ tái thả', 'KB02'),   -- Voọc (KB02)
('DV04', 'L03', N'Cái', 110.0, N'Đang điều trị', 'KB01'),-- Gấu ngựa (KB01)
('DV05', 'L03', N'Đực', 135.0, N'Khỏe mạnh', 'KB01'),   -- Gấu ngựa (KB01)
('DV08', 'L03', N'Đực', 95.0, N'Đang điều trị', 'KB01'), -- Gấu ngựa (KB01)
('DV06', 'L04', N'Cái', 6.5, N'Khỏe mạnh', 'KB03'),     -- Vượn (KB03)
('DV07', 'L05', N'Đực', 7.8, N'Khỏe mạnh', 'KB03');     -- Khỉ (KB03)

-- 4. NHANVIEN (5 nhân viên)
-- NV01, NV02: Bác sĩ thú y tại KB01 -> Test 2 UPDATE target (+10%)
-- NV03: Chuyên viên cứu hộ tại KB01 -> Không đổi
-- NV04: Bác sĩ thú y tại KB02 -> Không đổi (khác khu)
-- NV05: Kiểm lâm viên tại KB03 -> Không đổi
INSERT INTO NHANVIEN (MANV, HOTEN, CHUYENMON, LUONG, MAKHU) VALUES
('NV01', N'Lê Minh Tuấn', N'Bác sĩ thú y', 18000000, 'KB01'),
('NV02', N'Nguyễn Thị Thu', N'Bác sĩ thú y', 16000000, 'KB01'),
('NV03', N'Vũ Đình Khang', N'Chuyên viên cứu hộ', 12000000, 'KB01'),
('NV04', N'Hoàng Trọng Nghĩa', N'Bác sĩ thú y', 17000000, 'KB02'),
('NV05', N'Đỗ Quốc Bảo', N'Kiểm lâm viên', 14000000, 'KB03');

-- 5. CHITIET_CS (Lượt chăm sóc y tế)
-- Chăm sóc Tê tê Java (DV01, DV02):
-- NV01: CS01 (DV01), CS02 (DV02) -> Chăm sóc đủ cả 2 cá thể!
-- NV04: CS03 (DV01), CS04 (DV02) -> Chăm sóc đủ cả 2 cá thể!
-- NV02: CS05 (DV01) -> Thiếu DV02, loại!
-- NV03: CS07 (DV04) -> Loại
-- NV05: CS08 (DV07) -> Loại

-- Chi phí chăm sóc tháng 10/2024:
-- DV01: CS01 (2.5tr, 10/10) + CS06 (1.5tr, 25/10) = 4.0m
-- DV02: CS02 (3.0tr, 12/10) = 3.0m
-- DV04: CS07 (5.0tr, 18/10) = 5.0m
-- CS09 (DV01, tháng 11/2024, 2.0tr) -> Loại khỏi tháng 10/2024
INSERT INTO CHITIET_CS (MACS, MADV, MANV, NGAYCS, CHIPHI_CS, GHI_CHU) VALUES
('CS01', 'DV01', 'NV01', '2024-10-10', 2500000, N'Điều trị vết thương da vảy'),
('CS02', 'DV02', 'NV01', '2024-10-12', 3000000, N'Truyền kháng sinh và men tiêu hóa'),
('CS03', 'DV01', 'NV04', '2024-09-05', 1800000, N'Kiểm tra định kỳ tháng 9'),
('CS04', 'DV02', 'NV04', '2024-09-08', 2200000, N'Tẩy ký sinh trùng đường ruột'),
('CS05', 'DV01', 'NV02', '2024-08-20', 1200000, N'Bổ sung vi chất dinh dưỡng'),
('CS06', 'DV01', 'NV04', '2024-10-25', 1500000, N'Tái khám vết thương vảy'),
('CS07', 'DV04', 'NV01', '2024-10-18', 5000000, N'Phẫu thuật móng gấu bị nhiễm trùng'),
('CS08', 'DV07', 'NV05', '2024-10-22', 800000, N'Khám tổng quát khỉ đuôi lợn'),
('CS09', 'DV01', 'NV01', '2024-11-05', 2000000, N'Khám sức khỏe trước tái thả');

-- 6. DOT_TAITHA
INSERT INTO DOT_TAITHA (MADOT, MADV, NGAYTHA, DIADIEM_THA, TRANGTHAI) VALUES
('DT01', 'DV03', '2024-11-15', N'Tiểu khu 32, Vườn quốc gia Cát Tiên', N'Thành công');
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 2: QUESTION 2.1B UPDATE QUERY                   ===';
PRINT '------------------------------------------------------------';

-- Update 10% salary for Vets at 'Khu Cứu Hộ Thú Lớn'
UPDATE NHANVIEN
SET LUONG = LUONG * 1.10
FROM NHANVIEN nv
JOIN KHU_BAOTON kb ON nv.MAKHU = kb.MAKHU
WHERE kb.TENKHU = N'Khu Cứu Hộ Thú Lớn'
  AND nv.CHUYENMON = N'Bác sĩ thú y';

-- Assertions: NV01 (18m -> 19.8m), NV02 (16m -> 17.6m), NV03 (12m unchanged), NV04 (17m unchanged)
DECLARE @nv01_sal DECIMAL(18,2), @nv02_sal DECIMAL(18,2), @nv03_sal DECIMAL(18,2), @nv04_sal DECIMAL(18,2);
SELECT @nv01_sal = LUONG FROM NHANVIEN WHERE MANV = 'NV01';
SELECT @nv02_sal = LUONG FROM NHANVIEN WHERE MANV = 'NV02';
SELECT @nv03_sal = LUONG FROM NHANVIEN WHERE MANV = 'NV03';
SELECT @nv04_sal = LUONG FROM NHANVIEN WHERE MANV = 'NV04';

IF @nv01_sal = 19800000 AND @nv02_sal = 17600000 AND @nv03_sal = 12000000 AND @nv04_sal = 17000000
    PRINT '  [PASS] Test 2: Salaries verified: NV01=19.8m (+10%), NV02=17.6m (+10%), others unchanged.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 2 mismatch: NV01=' + CAST(@nv01_sal AS VARCHAR) + ', NV02=' + CAST(@nv02_sal AS VARCHAR);
    THROW 50010, 'Test 2 FAILED', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 3: QUESTION 2.2A SELECTION QUERY                ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2a: Critically Endangered species (L01, L02)
DECLARE @cnt3 INT;
SELECT @cnt3 = COUNT(*)
FROM LOAI_DONGVAT
WHERE MUC_NGUYCAP = N'Cực kỳ nguy cấp';

IF @cnt3 = 2
    PRINT '  [PASS] Test 3: Selection returned exactly 2 Critically Endangered species (L01, L02).';
ELSE
    THROW 50020, 'Test 3 FAILED: Incorrect count for CR species selection', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 4: QUESTION 2.2B JOIN QUERY                     ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2b: Animals at 'Khu Bán Tự Nhiên Cát Tiên' (DV01, DV02, DV03)
DECLARE @cnt4 INT;
SELECT @cnt4 = COUNT(*)
FROM DONGVAT dv
JOIN KHU_BAOTON kb ON dv.MAKHU = kb.MAKHU
WHERE kb.TENKHU = N'Khu Bán Tự Nhiên Cát Tiên';

IF @cnt4 = 3
    PRINT '  [PASS] Test 4: Join returned exactly 3 animals at Khu Bán Tự Nhiên Cát Tiên (DV01, DV02, DV03).';
ELSE
    THROW 50030, 'Test 4 FAILED: Incorrect join animal count', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 5: QUESTION 2.2C OUTER JOIN QUERY               ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2c: Left Outer Join KHU_BAOTON with NHANVIEN
DECLARE @cnt5_total INT, @cnt5_null INT;
SELECT @cnt5_total = COUNT(*), @cnt5_null = SUM(CASE WHEN nv.MANV IS NULL THEN 1 ELSE 0 END)
FROM KHU_BAOTON kb
LEFT JOIN NHANVIEN nv ON kb.MAKHU = nv.MAKHU;

IF @cnt5_total = 6 AND @cnt5_null = 1
    PRINT '  [PASS] Test 5: Outer join preserved KB04 with NULL employee info (total 6 rows, 1 NULL).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 5 count: Total=' + CAST(@cnt5_total AS VARCHAR) + ', Null=' + CAST(@cnt5_null AS VARCHAR);
    THROW 50040, 'Test 5 FAILED: Outer join did not preserve empty sanctuary properly', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE           ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2d: Total care costs in Oct 2024 by animal
-- DV01: CS01 (2.5m) + CS06 (1.5m) = 4.0m
-- DV02: CS02 (3.0m) = 3.0m
-- DV04: CS07 (5.0m) = 5.0m
DECLARE @cost_dv01 DECIMAL(18,2), @cost_dv02 DECIMAL(18,2);
SELECT @cost_dv01 = SUM(cs.CHIPHI_CS) FROM DONGVAT dv JOIN CHITIET_CS cs ON dv.MADV = cs.MADV WHERE dv.MADV = 'DV01' AND cs.NGAYCS >= '2024-10-01' AND cs.NGAYCS <= '2024-10-31';
SELECT @cost_dv02 = SUM(cs.CHIPHI_CS) FROM DONGVAT dv JOIN CHITIET_CS cs ON dv.MADV = cs.MADV WHERE dv.MADV = 'DV02' AND cs.NGAYCS >= '2024-10-01' AND cs.NGAYCS <= '2024-10-31';

IF @cost_dv01 = 4000000 AND @cost_dv02 = 3000000
    PRINT '  [PASS] Test 6: Grouping SUM verified: DV01=4.0m, DV02=3.0m care costs in Oct 2024.';
ELSE
    THROW 50050, 'Test 6 FAILED: Grouping care cost calculation mismatch', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION            ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2e: Employees caring for ALL Sunda pangolins (DV01, DV02)
DECLARE @div_not_exists TABLE (MANV VARCHAR(10), HOTEN NVARCHAR(50), CHUYENMON NVARCHAR(50));
INSERT INTO @div_not_exists
SELECT nv.MANV, nv.HOTEN, nv.CHUYENMON
FROM NHANVIEN nv
WHERE EXISTS (
    SELECT 1 FROM CHITIET_CS cs
    WHERE cs.MANV = nv.MANV
)
AND NOT EXISTS (
    SELECT 1 FROM DONGVAT dv
    JOIN LOAI_DONGVAT ldv ON dv.MALOAI = ldv.MALOAI
    WHERE ldv.TENLOAI = N'Tê tê Java'
      AND NOT EXISTS (
          SELECT 1 FROM CHITIET_CS cs2
          WHERE cs2.MANV = nv.MANV
            AND cs2.MADV = dv.MADV
      )
);

DECLARE @div_having TABLE (MANV VARCHAR(10), HOTEN NVARCHAR(50), CHUYENMON NVARCHAR(50));
WITH R AS (
    SELECT DISTINCT MANV, MADV FROM CHITIET_CS
),
S AS (
    SELECT dv.MADV
    FROM DONGVAT dv
    JOIN LOAI_DONGVAT ldv ON dv.MALOAI = ldv.MALOAI
    WHERE ldv.TENLOAI = N'Tê tê Java'
)
INSERT INTO @div_having
SELECT nv.MANV, nv.HOTEN, nv.CHUYENMON
FROM NHANVIEN nv
JOIN (
    SELECT R.MANV
    FROM R
    LEFT JOIN S ON R.MADV = S.MADV
    GROUP BY R.MANV
    HAVING COUNT(DISTINCT S.MADV) = (SELECT COUNT(*) FROM S)
) div ON nv.MANV = div.MANV;

-- Verify identical results: NV01 and NV04
DECLARE @diff1 INT, @diff2 INT;
SELECT @diff1 = COUNT(*) FROM (SELECT MANV FROM @div_not_exists EXCEPT SELECT MANV FROM @div_having) t;
SELECT @diff2 = COUNT(*) FROM (SELECT MANV FROM @div_having EXCEPT SELECT MANV FROM @div_not_exists) t;

IF @diff1 = 0 AND @diff2 = 0 AND (SELECT COUNT(*) FROM @div_not_exists) = 2
    PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (NV01, NV04).';
ELSE
    THROW 50060, 'Test 7 FAILED: Relational division discrepancy between formulations', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE ===';
PRINT '------------------------------------------------------------';

-- Adversarial Test 8: Empty target S = Ø (No animal for 'Sao la')
DECLARE @empty_not_exists TABLE (MANV VARCHAR(10));
INSERT INTO @empty_not_exists
SELECT nv.MANV
FROM NHANVIEN nv
WHERE EXISTS (
    SELECT 1 FROM CHITIET_CS cs
    WHERE cs.MANV = nv.MANV
)
AND NOT EXISTS (
    SELECT 1 FROM DONGVAT dv
    JOIN LOAI_DONGVAT ldv ON dv.MALOAI = ldv.MALOAI
    WHERE ldv.TENLOAI = N'Sao la'
      AND NOT EXISTS (
          SELECT 1 FROM CHITIET_CS cs2
          WHERE cs2.MANV = nv.MANV
            AND cs2.MADV = dv.MADV
      )
);

DECLARE @empty_having TABLE (MANV VARCHAR(10));
WITH R AS (
    SELECT DISTINCT MANV, MADV FROM CHITIET_CS
),
S AS (
    SELECT dv.MADV
    FROM DONGVAT dv
    JOIN LOAI_DONGVAT ldv ON dv.MALOAI = ldv.MALOAI
    WHERE ldv.TENLOAI = N'Sao la'
)
INSERT INTO @empty_having
SELECT nv.MANV
FROM NHANVIEN nv
JOIN (
    SELECT R.MANV
    FROM R
    LEFT JOIN S ON R.MADV = S.MADV
    GROUP BY R.MANV
    HAVING COUNT(DISTINCT S.MADV) = (SELECT COUNT(*) FROM S)
) div ON nv.MANV = div.MANV;

-- All employees who have performed care (NV01, NV02, NV04, NV05 = 4 employees; NV03 did not care for anyone)
DECLARE @ediff1 INT, @ediff2 INT;
SELECT @ediff1 = COUNT(*) FROM (SELECT MANV FROM @empty_not_exists EXCEPT SELECT MANV FROM @empty_having) t;
SELECT @ediff2 = COUNT(*) FROM (SELECT MANV FROM @empty_having EXCEPT SELECT MANV FROM @empty_not_exists) t;

IF @ediff1 = 0 AND @ediff2 = 0 AND (SELECT COUNT(*) FROM @empty_not_exists) = 4
    PRINT '  [PASS] Test 8: Empty target S=Ø verified with EXCEPT set comparison: RA, NOT EXISTS and HAVING COUNT identical (4 employees).';
ELSE
    THROW 50070, 'Test 8 FAILED: Empty target division discrepancy', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING           ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2f: Sanctuaries tied with MAX animal count
-- Both KB01 and KB02 have exactly 3 animals
DECLARE @max_sanctuaries TABLE (MAKHU VARCHAR(10), TENKHU NVARCHAR(100), DIENTICH_HA DECIMAL(8,2), TONG_DONGVAT INT);
WITH ThongKe AS (
    SELECT dv.MAKHU, COUNT(dv.MADV) AS TONG_DONGVAT
    FROM DONGVAT dv
    GROUP BY dv.MAKHU
)
INSERT INTO @max_sanctuaries
SELECT kb.MAKHU, kb.TENKHU, kb.DIENTICH_HA, tk.TONG_DONGVAT
FROM KHU_BAOTON kb
JOIN ThongKe tk ON kb.MAKHU = tk.MAKHU
WHERE tk.TONG_DONGVAT = (SELECT MAX(TONG_DONGVAT) FROM ThongKe);

DECLARE @max_cnt INT, @min_cnt INT;
SELECT @max_cnt = COUNT(*), @min_cnt = MIN(TONG_DONGVAT) FROM @max_sanctuaries;

IF @max_cnt = 2 AND @min_cnt = 3
    PRINT '  [PASS] Test 9: Extreme tie-breaking verified: KB01 (3 animals) and KB02 (3 animals) preserved; others excluded.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 9: Count=' + CAST(@max_cnt AS VARCHAR) + ', Min=' + CAST(@min_cnt AS VARCHAR);
    THROW 50080, 'Test 9 FAILED: Extreme tie-breaking did not preserve tied records', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== ALL 9 MOCK-15 VERIFICATION SUITES PASSED WITH ASSERTIONS ===';
PRINT '------------------------------------------------------------';
