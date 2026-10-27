-- =============================================================================
-- IT004 Midterm Exam - MOCK-02 Automated Verification Fixture
-- Domain: Quản Lý Hệ Thống Phòng Cháy Chữa Cháy (PCCC) Chung Cư Cao Tầng
-- Engine: Microsoft SQL Server 2025 / Azure SQL Database
-- Author: VÕ TRỌNG PHÚC - CSDL_UIT Master Series
-- =============================================================================

USE tempdb;
GO

SET NOCOUNT ON;
SET ANSI_WARNINGS OFF;
GO

-- 1. CLEANUP PREVIOUS OBJECTS
IF OBJECT_ID('dbo.CT_KIEMTRA', 'U') IS NOT NULL DROP TABLE dbo.CT_KIEMTRA;
IF OBJECT_ID('dbo.DOT_KIEMTRA', 'U') IS NOT NULL DROP TABLE dbo.DOT_KIEMTRA;
IF OBJECT_ID('dbo.THIETBI_PCCC', 'U') IS NOT NULL DROP TABLE dbo.THIETBI_PCCC;
IF OBJECT_ID('dbo.CANHO', 'U') IS NOT NULL DROP TABLE dbo.CANHO;
IF OBJECT_ID('dbo.TANG', 'U') IS NOT NULL DROP TABLE dbo.TANG;
IF OBJECT_ID('dbo.TOANHA', 'U') IS NOT NULL DROP TABLE dbo.TOANHA;
GO

-- 2. DDL: CREATE RELATIONAL TABLES
CREATE TABLE dbo.TOANHA (
    MATN VARCHAR(10) NOT NULL,
    TENTN NVARCHAR(100) NOT NULL,
    SOTANG INT NOT NULL,
    DIACHI NVARCHAR(200) NOT NULL,
    CONSTRAINT PK_TOANHA PRIMARY KEY (MATN)
);

CREATE TABLE dbo.TANG (
    MATANG VARCHAR(10) NOT NULL,
    MATN VARCHAR(10) NOT NULL,
    STTTANG INT NOT NULL,
    DIENTICH FLOAT NOT NULL,
    CONSTRAINT PK_TANG PRIMARY KEY (MATANG),
    CONSTRAINT FK_TANG_TOANHA FOREIGN KEY (MATN) REFERENCES dbo.TOANHA(MATN) ON DELETE CASCADE
);

CREATE TABLE dbo.CANHO (
    MACANHO VARCHAR(10) NOT NULL,
    MATANG VARCHAR(10) NOT NULL,
    SOCANHO VARCHAR(20) NOT NULL,
    DIENTICH FLOAT NULL, -- Will test NOT NULL & CHECK via ALTER TABLE
    SOPHONGNGU INT NOT NULL,
    TRANGTHAI NVARCHAR(50) NOT NULL,
    CONSTRAINT PK_CANHO PRIMARY KEY (MACANHO),
    CONSTRAINT FK_CANHO_TANG FOREIGN KEY (MATANG) REFERENCES dbo.TANG(MATANG) ON DELETE CASCADE
);

CREATE TABLE dbo.THIETBI_PCCC (
    MATB VARCHAR(10) NOT NULL,
    MATANG VARCHAR(10) NOT NULL,
    TENTB NVARCHAR(100) NOT NULL,
    LOAITB NVARCHAR(50) NOT NULL,
    VITRI_LAPDAT NVARCHAR(100) NOT NULL,
    NGAYLAP DATE NOT NULL,
    HANSUDUNG DATE NULL, -- Will test NOT NULL & CHECK via ALTER TABLE
    CONSTRAINT PK_THIETBI_PCCC PRIMARY KEY (MATB),
    CONSTRAINT FK_THIETBI_TANG FOREIGN KEY (MATANG) REFERENCES dbo.TANG(MATANG) ON DELETE CASCADE
);

CREATE TABLE dbo.DOT_KIEMTRA (
    MADOT VARCHAR(10) NOT NULL,
    NGAYKT DATE NOT NULL,
    NGUOIKT NVARCHAR(100) NOT NULL,
    KETLUAN_CHUNG NVARCHAR(200) NOT NULL,
    CONSTRAINT PK_DOT_KIEMTRA PRIMARY KEY (MADOT)
);

CREATE TABLE dbo.CT_KIEMTRA (
    MADOT VARCHAR(10) NOT NULL,
    MATB VARCHAR(10) NOT NULL,
    TINHTRANG NVARCHAR(50) NOT NULL,
    GHICHU NVARCHAR(200) NULL,
    CONSTRAINT PK_CT_KIEMTRA PRIMARY KEY (MADOT, MATB),
    CONSTRAINT FK_CT_DOT FOREIGN KEY (MADOT) REFERENCES dbo.DOT_KIEMTRA(MADOT) ON DELETE CASCADE,
    CONSTRAINT FK_CT_TB FOREIGN KEY (MATB) REFERENCES dbo.THIETBI_PCCC(MATB) ON DELETE CASCADE
);
GO

-- 3. APPLY QUESTION 2.1A CHECK CONSTRAINTS & NOT NULL POLICIES
ALTER TABLE dbo.CANHO ALTER COLUMN DIENTICH FLOAT NOT NULL;
ALTER TABLE dbo.CANHO ADD CONSTRAINT CK_CANHO_DIENTICH CHECK (DIENTICH > 0);

ALTER TABLE dbo.THIETBI_PCCC ALTER COLUMN HANSUDUNG DATE NOT NULL;
ALTER TABLE dbo.THIETBI_PCCC ADD CONSTRAINT CK_TB_HANSUDUNG CHECK (HANSUDUNG >= NGAYLAP);
GO

-- 4. INSERT REALISTIC SEED DATA
-- 3 Toà nhà ban đầu
INSERT INTO dbo.TOANHA (MATN, TENTN, SOTANG, DIACHI) VALUES
('TN01', N'Ruby Tower', 25, N'123 Mai Chí Thọ, P. An Phú, TP. Thủ Đức'),
('TN02', N'Sapphire Tower', 30, N'456 Võ Nguyên Giáp, P. Thảo Điền, TP. Thủ Đức'),
('TN03', N'Emerald Tower', 18, N'789 Nguyễn Hữu Thọ, P. Tân Hưng, Q. 7');

-- Tầng
INSERT INTO dbo.TANG (MATANG, MATN, STTTANG, DIENTICH) VALUES
('TANG01', 'TN01', 1, 850.0),
('TANG02', 'TN01', 10, 800.0),
('TANG03', 'TN01', 15, 800.0),
('TANG04', 'TN01', 20, 600.0), -- Tầng không có thiết bị PCCC (dùng test LEFT JOIN)
('TANG05', 'TN02', 1, 900.0),
('TANG06', 'TN02', 12, 850.0),
('TANG07', 'TN03', 1, 700.0);   -- Tầng không có thiết bị PCCC (TN03 không có thiết bị nào)

-- Căn hộ:
-- TN01 có 4 căn hộ (CH01, CH02, CH03, CH04)
-- TN02 có 4 căn hộ (CH05, CH06, CH07, CH08) -> Đồng hạng cực đại (4 căn)
-- TN03 có 2 căn hộ (CH09, CH10)
INSERT INTO dbo.CANHO (MACANHO, MATANG, SOCANHO, DIENTICH, SOPHONGNGU, TRANGTHAI) VALUES
('CH01', 'TANG01', 'A101', 65.5, 2, N'Đang ở'),
('CH02', 'TANG02', 'A1001', 85.0, 3, N'Đang ở'),
('CH03', 'TANG02', 'A1002', 72.0, 2, N'Trống'),
('CH04', 'TANG03', 'A1501', 110.0, 3, N'Đang ở'),
('CH05', 'TANG05', 'B101', 55.0, 1, N'Đang ở'),
('CH06', 'TANG05', 'B102', 60.0, 2, N'Đang ở'),
('CH07', 'TANG06', 'B1201', 95.0, 3, N'Trống'),
('CH08', 'TANG06', 'B1202', 90.0, 3, N'Đang ở'),
('CH09', 'TANG07', 'C101', 50.0, 1, N'Đang ở'),
('CH10', 'TANG07', 'C102', 52.0, 1, N'Trống');

-- Thiết bị PCCC
INSERT INTO dbo.THIETBI_PCCC (MATB, MATANG, TENTB, LOAITB, VITRI_LAPDAT, NGAYLAP, HANSUDUNG) VALUES
('TB01', 'TANG01', N'Đầu báo khói quang điện T1', N'Đầu báo khói', N'Hành lang T1', '2023-01-10', '2027-01-10'),
('TB02', 'TANG02', N'Đầu báo khói nhiệt T10', N'Đầu báo khói', N'Cửa thang máy T10', '2023-01-10', '2027-01-10'),
('TB03', 'TANG03', N'Đầu báo khói thông minh T15', N'Đầu báo khói', N'Phòng rác T15', '2023-05-15', '2027-05-15'),
('TB04', 'TANG01', N'Bình bột MFZ4 - 01', N'Bình chữa cháy bột', N'Hộp PCCC vách tường T1', '2022-03-01', '2025-05-15'),
('TB05', 'TANG02', N'Bình bột MFZ4 - 02', N'Bình chữa cháy bột', N'Hộp PCCC vách tường T10', '2022-04-10', '2025-11-20'),
('TB06', 'TANG05', N'Bình bột MFZ8 - 01', N'Bình chữa cháy bột', N'Hành lang sảnh B', '2023-01-01', '2026-01-01'),
('TB07', 'TANG06', N'Họng nước D65', N'Họng nước cứu hỏa', N'Hộp kỹ thuật tầng 12', '2023-02-15', '2028-02-15');

-- Đợt kiểm tra
INSERT INTO dbo.DOT_KIEMTRA (MADOT, NGAYKT, NGUOIKT, KETLUAN_CHUNG) VALUES
('DKT01', '2024-10-15', N'Đoàn kiểm tra PCCC Q.Thủ Đức', N'Đạt yêu cầu'),
('DKT02', '2024-11-20', N'Trung tâm Kiểm định PCCC TP.HCM', N'Đạt chuẩn'),
('DKT03', '2024-12-05', N'Kỹ sư an toàn tòa nhà', N'Cần bảo dưỡng'),
('DKT04', '2025-01-10', N'Ban Quản trị chung cư', N'Bình thường');

-- Chi tiết kiểm tra
-- DKT01 kiểm tra: TB01, TB02, TB03 (đủ 3 Đầu báo khói) + TB04 (Bình bột HSD 2025-05-15)
-- DKT02 kiểm tra: TB01, TB02, TB03 (đủ 3 Đầu báo khói) + TB05, TB06
-- DKT03 kiểm tra: TB01, TB02 (thiếu TB03)
-- DKT04 kiểm tra: TB04, TB05 (không có đầu báo khói nào)
INSERT INTO dbo.CT_KIEMTRA (MADOT, MATB, TINHTRANG, GHICHU) VALUES
('DKT01', 'TB01', N'Bình thường', N'Độ nhạy tốt'),
('DKT01', 'TB02', N'Bình thường', N'Đã test còi'),
('DKT01', 'TB03', N'Bình thường', N'Tín hiệu kết nối ổn định'),
('DKT01', 'TB04', N'Bình thường', N'Kiểm tra định kỳ'),
('DKT02', 'TB01', N'Bình thường', N'Đạt chuẩn định kỳ'),
('DKT02', 'TB02', N'Bình thường', N'Đạt chuẩn định kỳ'),
('DKT02', 'TB03', N'Bình thường', N'Đạt chuẩn định kỳ'),
('DKT02', 'TB05', N'Bình thường', N'Đồng hồ áp đạt'),
('DKT02', 'TB06', N'Bình thường', N'Niêm phong nguyên vẹn'),
('DKT03', 'TB01', N'Bình thường', N'Kiểm tra đột xuất'),
('DKT03', 'TB02', N'Bình thường', N'Kiểm tra đột xuất'),
('DKT04', 'TB04', N'Bình thường', N'Kiểm tra đầu năm'),
('DKT04', 'TB05', N'Bình thường', N'Kiểm tra đầu năm');
GO

-- =============================================================================
-- 5. ADVERSARIAL CHECK CONSTRAINT VERIFICATION TESTS
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY ===';
PRINT '------------------------------------------------------------';

-- Test 1A: CANHO.DIENTICH <= 0 (Using valid foreign key TANG01)
BEGIN TRY
    INSERT INTO dbo.CANHO (MACANHO, MATANG, SOCANHO, DIENTICH, SOPHONGNGU, TRANGTHAI)
    VALUES ('CH_FAIL', 'TANG01', 'X000', -10.0, 1, N'Trống');
    PRINT '  [FAIL] Test 1A: Negative DIENTICH was accepted unexpectedly!';
    THROW 50001, 'Test 1A Failed: Negative DIENTICH accepted', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_CANHO_DIENTICH%'
        PRINT '  [PASS] Test 1A: CK_CANHO_DIENTICH correctly blocked DIENTICH = -10.0';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1A unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;

-- Test 1B: CANHO.DIENTICH = 0
BEGIN TRY
    INSERT INTO dbo.CANHO (MACANHO, MATANG, SOCANHO, DIENTICH, SOPHONGNGU, TRANGTHAI)
    VALUES ('CH_ZERO', 'TANG01', 'X000', 0.0, 1, N'Trống');
    PRINT '  [FAIL] Test 1B: Zero DIENTICH was accepted unexpectedly!';
    THROW 50002, 'Test 1B Failed: Zero DIENTICH accepted', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_CANHO_DIENTICH%'
        PRINT '  [PASS] Test 1B: CK_CANHO_DIENTICH correctly blocked DIENTICH = 0';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1B unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;

-- Test 1C: THIETBI_PCCC.HANSUDUNG < NGAYLAP (Using valid foreign key TANG01)
BEGIN TRY
    INSERT INTO dbo.THIETBI_PCCC (MATB, MATANG, TENTB, LOAITB, VITRI_LAPDAT, NGAYLAP, HANSUDUNG)
    VALUES ('TB_FAIL', 'TANG01', N'Thiết bị lỗi', N'Bình chữa cháy bột', N'Hành lang', '2024-05-01', '2024-01-01');
    PRINT '  [FAIL] Test 1C: Expired on installation was accepted unexpectedly!';
    THROW 50003, 'Test 1C Failed: HANSUDUNG < NGAYLAP accepted', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_TB_HANSUDUNG%'
        PRINT '  [PASS] Test 1C: CK_TB_HANSUDUNG correctly blocked HANSUDUNG < NGAYLAP';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1C unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;

-- Test 1D: NOT NULL Integrity Enforcement (Error 515)
BEGIN TRY
    INSERT INTO dbo.CANHO (MACANHO, MATANG, SOCANHO, DIENTICH, SOPHONGNGU, TRANGTHAI)
    VALUES ('CH_NULL', 'TANG01', 'X000', NULL, 1, N'Trống');
    PRINT '  [FAIL] Test 1D: NULL DIENTICH was accepted unexpectedly!';
    THROW 50004, 'Test 1D Failed: NULL DIENTICH accepted', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] Test 1D: NOT NULL policy correctly rejected NULL DIENTICH (Error 515)';
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

-- Perform UPDATE: Update TINHTRANG in CT_KIEMTRA to 'Hết hạn' for DKT01 where HANSUDUNG < '2025-06-01'
-- In seed data: TB04 has HANSUDUNG = '2025-05-15' (< '2025-06-01') and is tested in DKT01
-- Expected affected rows: exactly 1 row (DKT01, TB04)
UPDATE CT
SET CT.TINHTRANG = N'Hết hạn'
FROM dbo.CT_KIEMTRA CT
INNER JOIN dbo.THIETBI_PCCC TB ON CT.MATB = TB.MATB
WHERE CT.MADOT = 'DKT01'
  AND TB.HANSUDUNG < '2025-06-01';

DECLARE @updated_count INT = @@ROWCOUNT;
IF @updated_count = 1
    PRINT '  [PASS] Test 2: UPDATE correctly affected 1 row as expected.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 2: UPDATE affected ' + CAST(@updated_count AS VARCHAR) + ' rows, expected 1!';
    THROW 50005, 'Test 2 Failed', 1;
END

-- Verify updated status in database with strict assertion
DECLARE @status_val NVARCHAR(50);
SELECT @status_val = CT.TINHTRANG
FROM dbo.CT_KIEMTRA CT
WHERE CT.MADOT = 'DKT01' AND CT.MATB = 'TB04';

IF @status_val = N'Hết hạn'
    PRINT '  [PASS] Test 2b: Verified TINHTRANG in database is updated to ''Het han''.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 2b: Unexpected TINHTRANG: ' + ISNULL(@status_val, 'NULL');
    THROW 50006, 'Test 2b Failed', 1;
END
GO

-- =============================================================================
-- 7. VERIFY QUESTION 2.2 RELATIONAL ALGEBRA / SQL QUERIES WITH STRICT ASSERTIONS
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 3: QUESTION 2.2A SELECTION & PROJECTION ===';
PRINT '------------------------------------------------------------';
-- Liệt kê thiết bị PCCC loại 'Bình chữa cháy bột' có HANSUDUNG trong năm 2025
-- Expected: TB04 (2025-05-15) and TB05 (2025-11-20). TB06 (2026-01-01) excluded.
DECLARE @t3_cnt INT, @t3_valid INT;
SELECT @t3_cnt = COUNT(*),
       @t3_valid = SUM(CASE WHEN MATB IN ('TB04', 'TB05') THEN 1 ELSE 0 END)
FROM dbo.THIETBI_PCCC
WHERE LOAITB = N'Bình chữa cháy bột'
  AND HANSUDUNG >= '2025-01-01' AND HANSUDUNG <= '2025-12-31';

IF @t3_cnt = 2 AND @t3_valid = 2
    PRINT '  [PASS] Test 3: Selection returned exactly 2 devices (TB04, TB05) with HSD in 2025.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 3: Expected exactly TB04 and TB05, got count=' + CAST(@t3_cnt AS VARCHAR);
    THROW 50007, 'Test 3 Failed', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 4: QUESTION 2.2B JOIN QUERY ===';
PRINT '------------------------------------------------------------';
-- Căn hộ thuộc 'Ruby Tower' ở tầng >= 10
-- Expected: CH02 (A1001), CH03 (A1002), CH04 (A1501). CH01 (tầng 1) excluded.
DECLARE @t4_cnt INT, @t4_valid INT;
SELECT @t4_cnt = COUNT(*),
       @t4_valid = SUM(CASE WHEN CH.MACANHO IN ('CH02', 'CH03', 'CH04') THEN 1 ELSE 0 END)
FROM dbo.CANHO CH
INNER JOIN dbo.TANG T ON CH.MATANG = T.MATANG
INNER JOIN dbo.TOANHA TN ON T.MATN = TN.MATN
WHERE TN.TENTN = N'Ruby Tower'
  AND T.STTTANG >= 10;

IF @t4_cnt = 3 AND @t4_valid = 3
    PRINT '  [PASS] Test 4: Join returned exactly 3 apartments (CH02, CH03, CH04) at floors >= 10.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 4: Expected 3 rows, got count=' + CAST(@t4_cnt AS VARCHAR);
    THROW 50008, 'Test 4 Failed', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 5: QUESTION 2.2C OUTER JOIN QUERY ===';
PRINT '------------------------------------------------------------';
-- Tất cả các tầng thuộc TN01 và thiết bị nếu có
-- Expected: TANG01, TANG02, TANG03 have devices; TANG04 has NULL for MATB and TENTB
DECLARE @t5_cnt INT, @t5_null_cnt INT;
SELECT @t5_cnt = COUNT(*),
       @t5_null_cnt = SUM(CASE WHEN T.MATANG = 'TANG04' AND TB.MATB IS NULL THEN 1 ELSE 0 END)
FROM dbo.TANG T
LEFT OUTER JOIN dbo.THIETBI_PCCC TB ON T.MATANG = TB.MATANG
WHERE T.MATN = 'TN01';

IF @t5_cnt = 6 AND @t5_null_cnt = 1
    PRINT '  [PASS] Test 5: Outer join correctly preserved TANG04 with NULL device info (total 6 rows).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 5: Outer join assertion failed! Total=' + CAST(@t5_cnt AS VARCHAR) + ', NullCnt=' + CAST(@t5_null_cnt AS VARCHAR);
    THROW 50009, 'Test 5 Failed', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE ===';
PRINT '------------------------------------------------------------';
-- Tổng số lượng thiết bị PCCC theo từng tòa nhà
-- Expected INNER JOIN: TN01: 5 devices (TB01-TB05), TN02: 2 devices (TB06-TB07). TN03 has 0 devices so excluded.
-- Expected LEFT JOIN: TN01: 5, TN02: 2, TN03: 0.
DECLARE @t6_tn01 INT, @t6_tn02 INT, @t6_tn03_inner INT, @t6_tn03_left INT;

SELECT @t6_tn01 = CNT
FROM (
    SELECT TN.MATN, COUNT(TB.MATB) AS CNT
    FROM dbo.TOANHA TN
    INNER JOIN dbo.TANG T ON TN.MATN = T.MATN
    INNER JOIN dbo.THIETBI_PCCC TB ON T.MATANG = TB.MATANG
    GROUP BY TN.MATN
) G WHERE G.MATN = 'TN01';

SELECT @t6_tn02 = CNT
FROM (
    SELECT TN.MATN, COUNT(TB.MATB) AS CNT
    FROM dbo.TOANHA TN
    INNER JOIN dbo.TANG T ON TN.MATN = T.MATN
    INNER JOIN dbo.THIETBI_PCCC TB ON T.MATANG = TB.MATANG
    GROUP BY TN.MATN
) G WHERE G.MATN = 'TN02';

SELECT @t6_tn03_inner = COUNT(*)
FROM (
    SELECT TN.MATN
    FROM dbo.TOANHA TN
    INNER JOIN dbo.TANG T ON TN.MATN = T.MATN
    INNER JOIN dbo.THIETBI_PCCC TB ON T.MATANG = TB.MATANG
    GROUP BY TN.MATN
) G WHERE G.MATN = 'TN03';

SELECT @t6_tn03_left = COUNT(TB.MATB)
FROM dbo.TOANHA TN
LEFT JOIN dbo.TANG T ON TN.MATN = T.MATN
LEFT JOIN dbo.THIETBI_PCCC TB ON T.MATANG = TB.MATANG
WHERE TN.MATN = 'TN03'
GROUP BY TN.MATN;

IF @t6_tn01 = 5 AND @t6_tn02 = 2 AND ISNULL(@t6_tn03_inner, 0) = 0 AND @t6_tn03_left = 0
    PRINT '  [PASS] Test 6: Grouping verified: TN01=5, TN02=2; TN03 excluded in INNER JOIN, counted as 0 in LEFT JOIN.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 6: Grouping counts mismatch! TN01=' + CAST(@t6_tn01 AS VARCHAR) + ', TN02=' + CAST(@t6_tn02 AS VARCHAR);
    THROW 50010, 'Test 6 Failed', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION ===';
PRINT '------------------------------------------------------------';
-- Tìm đợt kiểm tra đã kiểm tra TẤT CẢ các thiết bị 'Đầu báo khói' (TB01, TB02, TB03)
-- Expected: DKT01 and DKT02 pass; DKT03 (missing TB03) and DKT04 (no smoke detectors) fail.
DECLARE @t7_dne_cnt INT, @t7_dne_valid INT;
SELECT @t7_dne_cnt = COUNT(*),
       @t7_dne_valid = SUM(CASE WHEN DK.MADOT IN ('DKT01', 'DKT02') THEN 1 ELSE 0 END)
FROM dbo.DOT_KIEMTRA DK
WHERE NOT EXISTS (
    SELECT *
    FROM dbo.THIETBI_PCCC TB
    WHERE TB.LOAITB = N'Đầu báo khói'
      AND NOT EXISTS (
          SELECT *
          FROM dbo.CT_KIEMTRA CT
          WHERE CT.MADOT = DK.MADOT
            AND CT.MATB = TB.MATB
      )
)
AND EXISTS (SELECT * FROM dbo.CT_KIEMTRA WHERE MADOT = DK.MADOT);

DECLARE @t7_grp_cnt INT, @t7_grp_valid INT;
SELECT @t7_grp_cnt = COUNT(*),
       @t7_grp_valid = SUM(CASE WHEN Res.MADOT IN ('DKT01', 'DKT02') THEN 1 ELSE 0 END)
FROM (
    SELECT DK.MADOT
    FROM dbo.DOT_KIEMTRA DK
    INNER JOIN dbo.CT_KIEMTRA CT ON DK.MADOT = CT.MADOT
    INNER JOIN dbo.THIETBI_PCCC TB ON CT.MATB = TB.MATB
    WHERE TB.LOAITB = N'Đầu báo khói'
    GROUP BY DK.MADOT
    HAVING COUNT(DISTINCT TB.MATB) = (
        SELECT COUNT(*)
        FROM dbo.THIETBI_PCCC
        WHERE LOAITB = N'Đầu báo khói'
    )
) AS Res;

IF @t7_dne_cnt = 2 AND @t7_dne_valid = 2 AND @t7_grp_cnt = 2 AND @t7_grp_valid = 2
    PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (DKT01, DKT02).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 7: Division results mismatch! DNE_cnt=' + CAST(@t7_dne_cnt AS VARCHAR) + ', Grp_cnt=' + CAST(@t7_grp_cnt AS VARCHAR);
    THROW 50011, 'Test 7 Failed', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE ===';
PRINT '------------------------------------------------------------';
-- Edge Case: Target equipment type with 0 devices (e.g. 'Hệ thống FM200')
-- In pure Relational Algebra R / 0 = pi_MADOT(R).
-- Insert DKT05 into DOT_KIEMTRA to verify the candidate universe boundary:
INSERT INTO dbo.DOT_KIEMTRA (MADOT, NGAYKT, NGUOIKT, KETLUAN_CHUNG)
VALUES ('DKT05', '2025-02-01', N'Cán bộ dự bị', N'Chưa thực hiện');

-- Bounded candidate universe: pi_MADOT(CT_KIEMTRA) returns exactly the 4 active batches (DKT01..DKT04)
DECLARE @t8_bounded_cnt INT;
SELECT @t8_bounded_cnt = COUNT(DISTINCT CT.MADOT)
FROM dbo.CT_KIEMTRA CT
WHERE NOT EXISTS (
    SELECT *
    FROM dbo.THIETBI_PCCC TB
    WHERE TB.LOAITB = N'Hệ thống FM200'
      AND NOT EXISTS (
          SELECT *
          FROM dbo.CT_KIEMTRA CT2
          WHERE CT2.MADOT = CT.MADOT
            AND CT2.MATB = TB.MATB
      )
);

-- Unbounded entity universe: DOT_KIEMTRA returns all 5 batches (including DKT05 with 0 records in CT_KIEMTRA)
DECLARE @t8_unbounded_cnt INT;
SELECT @t8_unbounded_cnt = COUNT(*)
FROM dbo.DOT_KIEMTRA DK
WHERE NOT EXISTS (
    SELECT *
    FROM dbo.THIETBI_PCCC TB
    WHERE TB.LOAITB = N'Hệ thống FM200'
      AND NOT EXISTS (
          SELECT *
          FROM dbo.CT_KIEMTRA CT2
          WHERE CT2.MADOT = DK.MADOT
            AND CT2.MATB = TB.MATB
      )
);

IF @t8_bounded_cnt = 4 AND @t8_unbounded_cnt = 5
    PRINT '  [PASS] Test 8: Empty target S=∅ semantic verified: bounded candidate universe returns 4 batches, unbounded returns 5.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 8: Empty target count mismatch! Bounded=' + CAST(@t8_bounded_cnt AS VARCHAR) + ', Unbounded=' + CAST(@t8_unbounded_cnt AS VARCHAR);
    THROW 50012, 'Test 8 Failed', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING ===';
PRINT '------------------------------------------------------------';
-- Thêm tòa nhà TN04 có 0 căn hộ để kiểm thử triệt để trường hợp biên
INSERT INTO dbo.TOANHA (MATN, TENTN, SOTANG, DIACHI)
VALUES ('TN04', N'Commercial Plaza', 10, N'99 Song Hành, TP. Thủ Đức');

DECLARE @t9_cnt INT, @t9_tn01 INT, @t9_tn02 INT;
SELECT @t9_cnt = COUNT(*),
       @t9_tn01 = SUM(CASE WHEN Res.MATN = 'TN01' AND Res.SOCAN = 4 THEN 1 ELSE 0 END),
       @t9_tn02 = SUM(CASE WHEN Res.MATN = 'TN02' AND Res.SOCAN = 4 THEN 1 ELSE 0 END)
FROM (
    SELECT TOP 1 WITH TIES TN.MATN, TN.TENTN, TN.SOTANG, COUNT(CH.MACANHO) AS SOCAN
    FROM dbo.TOANHA TN
    INNER JOIN dbo.TANG T ON TN.MATN = T.MATN
    INNER JOIN dbo.CANHO CH ON T.MATANG = CH.MATANG
    GROUP BY TN.MATN, TN.TENTN, TN.SOTANG
    ORDER BY COUNT(CH.MACANHO) DESC
) AS Res;

IF @t9_cnt = 2 AND @t9_tn01 = 1 AND @t9_tn02 = 1
    PRINT '  [PASS] Test 9: Extreme tie-breaking verified: TN01 (4) and TN02 (4) preserved; TN03 (2) and TN04 (0) excluded.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 9: Extreme tie-breaking mismatch! Count=' + CAST(@t9_cnt AS VARCHAR);
    THROW 50013, 'Test 9 Failed', 1;
END

PRINT '------------------------------------------------------------';
PRINT '=== ALL 9 MOCK-02 VERIFICATION SUITES PASSED WITH ASSERTIONS ===';
PRINT '------------------------------------------------------------';
GO
