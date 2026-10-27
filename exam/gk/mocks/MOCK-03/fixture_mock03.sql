-- =============================================================================
-- IT004 Midterm Exam - MOCK-03 Automated Verification Fixture
-- Domain: Quản Lý Tiếp Nhận & Phân Bổ Tiền Cứu Trợ Bão Lũ
-- Engine: Microsoft SQL Server 2025 / Azure SQL Database
-- Author: VÕ TRỌNG PHÚC - CSDL_UIT Master Series
-- =============================================================================

USE tempdb;
GO

SET NOCOUNT ON;
SET ANSI_WARNINGS OFF;
GO

-- 1. CLEANUP PREVIOUS OBJECTS
IF OBJECT_ID('dbo.PHIEU_NHAN', 'U') IS NOT NULL DROP TABLE dbo.PHIEU_NHAN;
IF OBJECT_ID('dbo.DONG_GOP', 'U') IS NOT NULL DROP TABLE dbo.DONG_GOP;
IF OBJECT_ID('dbo.DOT_CUUTRO', 'U') IS NOT NULL DROP TABLE dbo.DOT_CUUTRO;
IF OBJECT_ID('dbo.NHA_HAOTAM', 'U') IS NOT NULL DROP TABLE dbo.NHA_HAOTAM;
IF OBJECT_ID('dbo.HO_DAN', 'U') IS NOT NULL DROP TABLE dbo.HO_DAN;
IF OBJECT_ID('dbo.XA', 'U') IS NOT NULL DROP TABLE dbo.XA;
GO

-- 2. DDL: CREATE RELATIONAL TABLES
CREATE TABLE dbo.XA (
    MAXA VARCHAR(10) NOT NULL,
    TENXA NVARCHAR(100) NOT NULL,
    HUYEN NVARCHAR(100) NOT NULL,
    CONSTRAINT PK_XA PRIMARY KEY (MAXA)
);

CREATE TABLE dbo.HO_DAN (
    MAHO VARCHAR(10) NOT NULL,
    CHUHO NVARCHAR(100) NOT NULL,
    SONKHAU INT NOT NULL,
    MUCDO_THIETHAI NVARCHAR(50) NOT NULL,
    MAXA VARCHAR(10) NOT NULL,
    CONSTRAINT PK_HODAN PRIMARY KEY (MAHO),
    CONSTRAINT FK_HODAN_XA FOREIGN KEY (MAXA) REFERENCES dbo.XA(MAXA) ON DELETE CASCADE
);

CREATE TABLE dbo.NHA_HAOTAM (
    MANHT VARCHAR(10) NOT NULL,
    TENNHT NVARCHAR(100) NOT NULL,
    SDT VARCHAR(20) NOT NULL,
    LOAIHINH NVARCHAR(50) NOT NULL,
    CONSTRAINT PK_NHAHAOTAM PRIMARY KEY (MANHT)
);

CREATE TABLE dbo.DOT_CUUTRO (
    MADOT VARCHAR(10) NOT NULL,
    TENDOT NVARCHAR(150) NOT NULL,
    NGAYBD DATE NOT NULL,
    NGAYKT DATE NULL, -- Will test NOT NULL & CHECK via ALTER TABLE
    CONSTRAINT PK_DOTCUUTRO PRIMARY KEY (MADOT)
);

CREATE TABLE dbo.DONG_GOP (
    MADG VARCHAR(10) NOT NULL,
    MANHT VARCHAR(10) NOT NULL,
    MADOT VARCHAR(10) NOT NULL,
    NGAYDG DATE NOT NULL,
    SOTIEN DECIMAL(18, 2) NOT NULL,
    CONSTRAINT PK_DONGGOP PRIMARY KEY (MADG),
    CONSTRAINT FK_DG_NHT FOREIGN KEY (MANHT) REFERENCES dbo.NHA_HAOTAM(MANHT) ON DELETE CASCADE,
    CONSTRAINT FK_DG_DOT FOREIGN KEY (MADOT) REFERENCES dbo.DOT_CUUTRO(MADOT) ON DELETE CASCADE
);

CREATE TABLE dbo.PHIEU_NHAN (
    MAPHIEU VARCHAR(10) NOT NULL,
    MAHO VARCHAR(10) NOT NULL,
    MADOT VARCHAR(10) NOT NULL,
    NGAYNHAN DATE NOT NULL,
    SOTIEN DECIMAL(18, 2) NULL, -- Will test NOT NULL & CHECK via ALTER TABLE
    CONSTRAINT PK_PHIEUNHAN PRIMARY KEY (MAPHIEU),
    CONSTRAINT FK_PN_HO FOREIGN KEY (MAHO) REFERENCES dbo.HO_DAN(MAHO) ON DELETE CASCADE,
    CONSTRAINT FK_PN_DOT FOREIGN KEY (MADOT) REFERENCES dbo.DOT_CUUTRO(MADOT) ON DELETE CASCADE
);
GO

-- 3. APPLY QUESTION 2.1A CHECK CONSTRAINTS & NOT NULL POLICIES
ALTER TABLE dbo.PHIEU_NHAN ALTER COLUMN SOTIEN DECIMAL(18, 2) NOT NULL;
ALTER TABLE dbo.PHIEU_NHAN ADD CONSTRAINT CK_PHIEUNHAN_SOTIEN CHECK (SOTIEN > 0);

ALTER TABLE dbo.DOT_CUUTRO ALTER COLUMN NGAYKT DATE NOT NULL;
ALTER TABLE dbo.DOT_CUUTRO ADD CONSTRAINT CK_DOTCUUTRO_NGAY CHECK (NGAYKT >= NGAYBD);
GO

-- 4. INSERT REALISTIC SEED DATA
-- Xã
INSERT INTO dbo.XA (MAXA, TENXA, HUYEN) VALUES
('XA01', N'Hiệp Phước', N'Cần Giờ'),
('XA02', N'Lý Nhơn', N'Cần Giờ'),
('XA03', N'An Thới Đông', N'Cần Giờ'), -- Xã chưa có hộ dân (dùng test LEFT JOIN)
('XA04', N'Bình Khánh', N'Cần Giờ');

-- Hộ dân
INSERT INTO dbo.HO_DAN (MAHO, CHUHO, SONKHAU, MUCDO_THIETHAI, MAXA) VALUES
('HD01', N'Nguyễn Văn Nam', 5, N'Trung bình', 'XA01'), -- Hiệp Phước, >= 5, sẽ được UPDATE thành 'Nặng'
('HD02', N'Trần Thị Mai', 6, N'Nhẹ', 'XA01'),        -- Hiệp Phước, >= 5, sẽ được UPDATE thành 'Nặng'
('HD03', N'Lê Văn Cường', 3, N'Trung bình', 'XA01'), -- Hiệp Phước, < 5
('HD04', N'Phạm Văn Dũng', 4, N'Nặng', 'XA02'),
('HD05', N'Hoàng Thị Lan', 5, N'Nặng', 'XA02'),
('HD06', N'Vũ Văn Hùng', 2, N'Trung bình', 'XA04');

-- Nhà hảo tâm
INSERT INTO dbo.NHA_HAOTAM (MANHT, TENNHT, SDT, LOAIHINH) VALUES
('NHT01', N'Tập đoàn Vingroup', '0901111111', N'Doanh nghiệp'),
('NHT02', N'Công ty FPT', '0902222222', N'Doanh nghiệp'),
('NHT03', N'Ông Nguyễn Văn A', '0903333333', N'Cá nhân'),
('NHT04', N'Bà Trần Thị B', '0904444444', N'Cá nhân');

-- Đợt cứu trợ
INSERT INTO dbo.DOT_CUUTRO (MADOT, TENDOT, NGAYBD, NGAYKT) VALUES
('DOT01', N'Cứu trợ bão số 3 Yagi', '2024-09-10', '2024-09-25'),
('DOT02', N'Hỗ trợ lũ lụt miền Trung', '2024-10-05', '2024-10-20'),
('DOT03', N'Đợt đông ấm 2024', '2024-11-01', '2024-11-15'),
('DOT04', N'Đợt khẩn cấp đầu năm 2025', '2025-01-05', '2025-01-15');

-- Đóng góp
-- DOT01: Nhận từ NHT01 và NHT02 (ĐỦ TẤT CẢ DOANH NGHIỆP)
-- DOT02: Nhận từ NHT01 và NHT02 (ĐỦ TẤT CẢ DOANH NGHIỆP)
-- DOT03: Chỉ nhận từ NHT01 (thiếu NHT02)
-- DOT04: Chỉ nhận từ NHT03 (Cá nhân)
INSERT INTO dbo.DONG_GOP (MADG, MANHT, MADOT, NGAYDG, SOTIEN) VALUES
('DG01', 'NHT01', 'DOT01', '2024-09-12', 500000000.00),
('DG02', 'NHT02', 'DOT01', '2024-09-13', 300000000.00),
('DG03', 'NHT01', 'DOT02', '2024-10-06', 400000000.00),
('DG04', 'NHT02', 'DOT02', '2024-10-08', 250000000.00),
('DG05', 'NHT01', 'DOT03', '2024-11-02', 100000000.00),
('DG06', 'NHT03', 'DOT04', '2025-01-06', 50000000.00),
('DG07', 'NHT03', 'DOT01', '2024-09-15', 20000000.00),
('DG08', 'NHT04', 'DOT02', '2024-10-10', 30000000.00);

-- Phiếu nhận
-- Xã XA01 (Hiệp Phước): HD01 nhận 10tr, HD02 nhận 10tr -> Tổng XA01 = 20,000,000
-- Xã XA02 (Lý Nhơn): HD04 nhận 12tr, HD05 nhận 8tr -> Tổng XA02 = 20,000,000 -> ĐỒNG HẠNG CỰC ĐẠI
-- Xã XA04 (Bình Khánh): HD06 nhận 5tr -> Tổng XA04 = 5,000,000
-- Xã XA03: 0đ
INSERT INTO dbo.PHIEU_NHAN (MAPHIEU, MAHO, MADOT, NGAYNHAN, SOTIEN) VALUES
('PN01', 'HD01', 'DOT01', '2024-09-20', 10000000.00),
('PN02', 'HD02', 'DOT01', '2024-09-21', 10000000.00),
('PN03', 'HD04', 'DOT01', '2024-09-22', 12000000.00),
('PN04', 'HD05', 'DOT02', '2024-10-15', 8000000.00),
('PN05', 'HD06', 'DOT02', '2024-10-16', 5000000.00);
GO

-- =============================================================================
-- 5. ADVERSARIAL CHECK CONSTRAINT VERIFICATION TESTS
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY ===';
PRINT '------------------------------------------------------------';

-- Test 1A: SOTIEN <= 0 (Using valid foreign key HD01, DOT01)
BEGIN TRY
    INSERT INTO dbo.PHIEU_NHAN (MAPHIEU, MAHO, MADOT, NGAYNHAN, SOTIEN)
    VALUES ('PN_FAIL', 'HD01', 'DOT01', '2024-09-25', -1000000.00);
    PRINT '  [FAIL] Test 1A: Negative SOTIEN was accepted unexpectedly!';
    THROW 50001, 'Test 1A Failed', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_PHIEUNHAN_SOTIEN%'
        PRINT '  [PASS] Test 1A: CK_PHIEUNHAN_SOTIEN correctly blocked negative SOTIEN.';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1A unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;

-- Test 1B: SOTIEN = 0
BEGIN TRY
    INSERT INTO dbo.PHIEU_NHAN (MAPHIEU, MAHO, MADOT, NGAYNHAN, SOTIEN)
    VALUES ('PN_ZERO', 'HD01', 'DOT01', '2024-09-25', 0.00);
    PRINT '  [FAIL] Test 1B: Zero SOTIEN was accepted unexpectedly!';
    THROW 50002, 'Test 1B Failed', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_PHIEUNHAN_SOTIEN%'
        PRINT '  [PASS] Test 1B: CK_PHIEUNHAN_SOTIEN correctly blocked SOTIEN = 0.';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1B unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;

-- Test 1C: NGAYKT < NGAYBD
BEGIN TRY
    INSERT INTO dbo.DOT_CUUTRO (MADOT, TENDOT, NGAYBD, NGAYKT)
    VALUES ('DOT_FAIL', N'Đợt lỗi ngày', '2024-10-20', '2024-10-10');
    PRINT '  [FAIL] Test 1C: NGAYKT < NGAYBD was accepted unexpectedly!';
    THROW 50003, 'Test 1C Failed', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_DOTCUUTRO_NGAY%'
        PRINT '  [PASS] Test 1C: CK_DOTCUUTRO_NGAY correctly blocked NGAYKT < NGAYBD.';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1C unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;

-- Test 1D: NOT NULL Integrity Enforcement (Error 515)
BEGIN TRY
    INSERT INTO dbo.PHIEU_NHAN (MAPHIEU, MAHO, MADOT, NGAYNHAN, SOTIEN)
    VALUES ('PN_NULL', 'HD01', 'DOT01', '2024-09-25', NULL);
    PRINT '  [FAIL] Test 1D: NULL SOTIEN was accepted unexpectedly!';
    THROW 50004, 'Test 1D Failed', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] Test 1D: NOT NULL policy correctly rejected NULL SOTIEN (Error 515).';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1D unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;
GO

-- =============================================================================
-- 6. VERIFY QUESTION 2.1B: T-SQL UPDATE STATEMENT
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 2: QUESTION 2.1B UPDATE VERIFICATION ===';
PRINT '------------------------------------------------------------';

-- Update MUCDO_THIETHAI = N'Nặng' cho các hộ có SONKHAU >= 5 thuộc xã 'Hiệp Phước'
-- In seed data: HD01 (SONKHAU=5, XA01) and HD02 (SONKHAU=6, XA01) match. Expected 2 rows affected.
UPDATE HD
SET HD.MUCDO_THIETHAI = N'Nặng'
FROM dbo.HO_DAN HD
INNER JOIN dbo.XA X ON HD.MAXA = X.MAXA
WHERE X.TENXA = N'Hiệp Phước'
  AND HD.SONKHAU >= 5;

DECLARE @updated_cnt INT = @@ROWCOUNT;
IF @updated_cnt = 2
    PRINT '  [PASS] Test 2: UPDATE correctly affected 2 households (HD01, HD02).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 2: UPDATE affected ' + CAST(@updated_cnt AS VARCHAR) + ' rows, expected 2!';
    THROW 50005, 'Test 2 Failed', 1;
END

-- Verify updated status in database
DECLARE @hd01_stat NVARCHAR(50), @hd02_stat NVARCHAR(50);
SELECT @hd01_stat = MUCDO_THIETHAI FROM dbo.HO_DAN WHERE MAHO = 'HD01';
SELECT @hd02_stat = MUCDO_THIETHAI FROM dbo.HO_DAN WHERE MAHO = 'HD02';

IF @hd01_stat = N'Nặng' AND @hd02_stat = N'Nặng'
    PRINT '  [PASS] Test 2b: Verified both HD01 and HD02 updated to Nang.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 2b: Status mismatch! HD01=' + @hd01_stat + ', HD02=' + @hd02_stat;
    THROW 50006, 'Test 2b Failed', 1;
END
GO

-- =============================================================================
-- 7. VERIFY QUESTION 2.2 RELATIONAL ALGEBRA / SQL QUERIES WITH STRICT ASSERTIONS
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 3: QUESTION 2.2A SELECTION & PROJECTION ===';
PRINT '------------------------------------------------------------';
-- Liệt kê nhà hảo tâm loại hình 'Cá nhân'
-- Expected: NHT03 and NHT04 (2 rows).
DECLARE @t3_cnt INT, @t3_valid INT;
SELECT @t3_cnt = COUNT(*),
       @t3_valid = SUM(CASE WHEN MANHT IN ('NHT03', 'NHT04') THEN 1 ELSE 0 END)
FROM dbo.NHA_HAOTAM
WHERE LOAIHINH = N'Cá nhân';

IF @t3_cnt = 2 AND @t3_valid = 2
    PRINT '  [PASS] Test 3: Selection returned exactly 2 individual donors (NHT03, NHT04).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 3: Selection count mismatch! Count=' + CAST(@t3_cnt AS VARCHAR);
    THROW 50007, 'Test 3 Failed', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 4: QUESTION 2.2B JOIN QUERY ===';
PRINT '------------------------------------------------------------';
-- Hộ dân thuộc huyện 'Cần Giờ' có mức độ thiệt hại 'Nặng'
-- After UPDATE: HD01, HD02 (XA01), HD04, HD05 (XA02) all have MUCDO_THIETHAI = 'Nặng'. Expected 4 rows.
DECLARE @t4_cnt INT, @t4_valid INT;
SELECT @t4_cnt = COUNT(*),
       @t4_valid = SUM(CASE WHEN HD.MAHO IN ('HD01', 'HD02', 'HD04', 'HD05') THEN 1 ELSE 0 END)
FROM dbo.HO_DAN HD
INNER JOIN dbo.XA X ON HD.MAXA = X.MAXA
WHERE X.HUYEN = N'Cần Giờ'
  AND HD.MUCDO_THIETHAI = N'Nặng';

IF @t4_cnt = 4 AND @t4_valid = 4
    PRINT '  [PASS] Test 4: Join returned exactly 4 severely damaged households in Can Gio.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 4: Join count mismatch! Count=' + CAST(@t4_cnt AS VARCHAR);
    THROW 50008, 'Test 4 Failed', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 5: QUESTION 2.2C OUTER JOIN QUERY ===';
PRINT '------------------------------------------------------------';
-- Tất cả các xã thuộc Cần Giờ và hộ dân nếu có
-- Expected: XA01 (3 hộ), XA02 (2 hộ), XA04 (1 hộ), XA03 (0 hộ -> NULL). Total 7 rows.
DECLARE @t5_cnt INT, @t5_null_cnt INT;
SELECT @t5_cnt = COUNT(*),
       @t5_null_cnt = SUM(CASE WHEN X.MAXA = 'XA03' AND HD.MAHO IS NULL THEN 1 ELSE 0 END)
FROM dbo.XA X
LEFT OUTER JOIN dbo.HO_DAN HD ON X.MAXA = HD.MAXA
WHERE X.HUYEN = N'Cần Giờ';

IF @t5_cnt = 7 AND @t5_null_cnt = 1
    PRINT '  [PASS] Test 5: Outer join preserved XA03 with NULL household info (total 7 rows).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 5: Outer join assertion failed! Total=' + CAST(@t5_cnt AS VARCHAR);
    THROW 50009, 'Test 5 Failed', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE ===';
PRINT '------------------------------------------------------------';
-- Tổng số tiền ủng hộ trong năm 2024 theo từng nhà hảo tâm
-- NHT01: DG01(500tr) + DG03(400tr) + DG05(100tr) = 1,000,000,000
-- NHT02: DG02(300tr) + DG04(250tr) = 550,000,000
-- NHT03: DG07(20tr) = 20,000,000
-- NHT04: DG08(30tr) = 30,000,000
DECLARE @t6_nht01 DECIMAL(18, 2), @t6_nht02 DECIMAL(18, 2);
SELECT @t6_nht01 = SUM(DG.SOTIEN) FROM dbo.DONG_GOP DG WHERE DG.MANHT = 'NHT01' AND YEAR(DG.NGAYDG) = 2024;
SELECT @t6_nht02 = SUM(DG.SOTIEN) FROM dbo.DONG_GOP DG WHERE DG.MANHT = 'NHT02' AND YEAR(DG.NGAYDG) = 2024;

IF @t6_nht01 = 1000000000.00 AND @t6_nht02 = 550000000.00
    PRINT '  [PASS] Test 6: Grouping SUM verified: NHT01=1,000,000,000; NHT02=550,000,000.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 6: Grouping sum mismatch!';
    THROW 50010, 'Test 6 Failed', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION ===';
PRINT '------------------------------------------------------------';
-- Tìm đợt cứu trợ đã nhận tiền đóng góp từ TẤT CẢ nhà hảo tâm là 'Doanh nghiệp' (NHT01, NHT02)
-- Expected: DOT01 and DOT02. DOT03 (only NHT01) and DOT04 (only NHT03) excluded.
DECLARE @t7_dne_cnt INT, @t7_dne_valid INT;
SELECT @t7_dne_cnt = COUNT(*),
       @t7_dne_valid = SUM(CASE WHEN DCT.MADOT IN ('DOT01', 'DOT02') THEN 1 ELSE 0 END)
FROM dbo.DOT_CUUTRO DCT
WHERE NOT EXISTS (
    SELECT *
    FROM dbo.NHA_HAOTAM NHT
    WHERE NHT.LOAIHINH = N'Doanh nghiệp'
      AND NOT EXISTS (
          SELECT *
          FROM dbo.DONG_GOP DG
          WHERE DG.MADOT = DCT.MADOT
            AND DG.MANHT = NHT.MANHT
      )
)
AND EXISTS (SELECT * FROM dbo.DONG_GOP WHERE MADOT = DCT.MADOT);

DECLARE @t7_grp_cnt INT, @t7_grp_valid INT;
SELECT @t7_grp_cnt = COUNT(*),
       @t7_grp_valid = SUM(CASE WHEN Res.MADOT IN ('DOT01', 'DOT02') THEN 1 ELSE 0 END)
FROM (
    SELECT DCT.MADOT
    FROM dbo.DOT_CUUTRO DCT
    INNER JOIN dbo.DONG_GOP DG ON DCT.MADOT = DG.MADOT
    INNER JOIN dbo.NHA_HAOTAM NHT ON DG.MANHT = NHT.MANHT
    WHERE NHT.LOAIHINH = N'Doanh nghiệp'
    GROUP BY DCT.MADOT
    HAVING COUNT(DISTINCT NHT.MANHT) = (
        SELECT COUNT(*)
        FROM dbo.NHA_HAOTAM
        WHERE LOAIHINH = N'Doanh nghiệp'
    )
) AS Res;

IF @t7_dne_cnt = 2 AND @t7_dne_valid = 2 AND @t7_grp_cnt = 2 AND @t7_grp_valid = 2
    PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (DOT01, DOT02).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 7: Division mismatch!';
    THROW 50011, 'Test 7 Failed', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE ===';
PRINT '------------------------------------------------------------';
-- Edge Case: Target donor type with 0 records (e.g. 'Tập đoàn Quốc tế')
-- Pure RA: R / 0 = pi_MADOT(R). Returns all 4 active relief batches in DONG_GOP.
DECLARE @t8_bounded_cnt INT;
SELECT @t8_bounded_cnt = COUNT(DISTINCT DG.MADOT)
FROM dbo.DONG_GOP DG
WHERE NOT EXISTS (
    SELECT *
    FROM dbo.NHA_HAOTAM NHT
    WHERE NHT.LOAIHINH = N'Tập đoàn Quốc tế'
      AND NOT EXISTS (
          SELECT *
          FROM dbo.DONG_GOP DG2
          WHERE DG2.MADOT = DG.MADOT
            AND DG2.MANHT = NHT.MANHT
      )
);

IF @t8_bounded_cnt = 4
    PRINT '  [PASS] Test 8: Empty target S=∅ semantic verified: candidate universe returns 4 active batches.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 8: Empty target count mismatch!';
    THROW 50012, 'Test 8 Failed', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING ===';
PRINT '------------------------------------------------------------';
-- Xã nhận nhiều tiền cứu trợ nhất (bảo toàn đồng hạng)
-- Expected: Both XA01 (20,000,000) and XA02 (20,000,000) tie for MAX. XA04 (5,000,000) and XA03 (0) excluded.
DECLARE @t9_cnt INT, @t9_xa01 INT, @t9_xa02 INT;
SELECT @t9_cnt = COUNT(*),
       @t9_xa01 = SUM(CASE WHEN Res.MAXA = 'XA01' AND Res.TONG_CUUTRO = 20000000.00 THEN 1 ELSE 0 END),
       @t9_xa02 = SUM(CASE WHEN Res.MAXA = 'XA02' AND Res.TONG_CUUTRO = 20000000.00 THEN 1 ELSE 0 END)
FROM (
    SELECT TOP 1 WITH TIES X.MAXA, X.TENXA, X.HUYEN, SUM(PN.SOTIEN) AS TONG_CUUTRO
    FROM dbo.XA X
    INNER JOIN dbo.HO_DAN HD ON X.MAXA = HD.MAXA
    INNER JOIN dbo.PHIEU_NHAN PN ON HD.MAHO = PN.MAHO
    GROUP BY X.MAXA, X.TENXA, X.HUYEN
    ORDER BY SUM(PN.SOTIEN) DESC
) AS Res;

IF @t9_cnt = 2 AND @t9_xa01 = 1 AND @t9_xa02 = 1
    PRINT '  [PASS] Test 9: Extreme tie-breaking verified: XA01 (20tr) and XA02 (20tr) preserved; XA04 (5tr) excluded.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 9: Extreme tie-breaking mismatch! Count=' + CAST(@t9_cnt AS VARCHAR);
    THROW 50013, 'Test 9 Failed', 1;
END

PRINT '------------------------------------------------------------';
PRINT '=== ALL 9 MOCK-03 VERIFICATION SUITES PASSED WITH ASSERTIONS ===';
PRINT '------------------------------------------------------------';
GO
