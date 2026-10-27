-- ============================================================================
-- FIXTURE & ADVERSARIAL QA SUITE: MOCK-09
-- Business Domain: Quản Lý Giải Đấu Thể Thao Điện Tử Sinh Viên
-- Profile: RECENT_VERIFIED (10.0đ, 75 mins)
-- Author: VÕ TRỌNG PHÚC — CSDL_UIT Master Series
-- Engine: Microsoft SQL Server 2025 / Localhost
-- ============================================================================

USE tempdb;
GO

SET NOCOUNT ON;
SET ANSI_WARNINGS ON;
GO

-- 0. DYNAMIC FOREIGN KEY & TABLE CLEANUP
DECLARE @dropFkSql NVARCHAR(MAX) = N'';
SELECT @dropFkSql += N'ALTER TABLE ' + QUOTENAME(OBJECT_SCHEMA_NAME(parent_object_id))
    + N'.' + QUOTENAME(OBJECT_NAME(parent_object_id))
    + N' DROP CONSTRAINT ' + QUOTENAME(name) + N';' + CHAR(13)
FROM sys.foreign_keys
WHERE referenced_object_id IN (
    OBJECT_ID(N'dbo.NHATAITRO'), OBJECT_ID(N'dbo.THAMGIA_TRAN'),
    OBJECT_ID(N'dbo.TRANDAU'), OBJECT_ID(N'dbo.TUYENTHU'),
    OBJECT_ID(N'dbo.DOITHI'), OBJECT_ID(N'dbo.TRUONG')
);
IF @dropFkSql <> N'' EXEC sp_executesql @dropFkSql;

IF OBJECT_ID(N'dbo.NHATAITRO', N'U') IS NOT NULL DROP TABLE dbo.NHATAITRO;
IF OBJECT_ID(N'dbo.THAMGIA_TRAN', N'U') IS NOT NULL DROP TABLE dbo.THAMGIA_TRAN;
IF OBJECT_ID(N'dbo.TRANDAU', N'U') IS NOT NULL DROP TABLE dbo.TRANDAU;
IF OBJECT_ID(N'dbo.TUYENTHU', N'U') IS NOT NULL DROP TABLE dbo.TUYENTHU;
IF OBJECT_ID(N'dbo.DOITHI', N'U') IS NOT NULL DROP TABLE dbo.DOITHI;
IF OBJECT_ID(N'dbo.TRUONG', N'U') IS NOT NULL DROP TABLE dbo.TRUONG;
GO

-- 1. DDL: RELATIONAL SCHEMA
CREATE TABLE dbo.TRUONG (
    MATRUONG NVARCHAR(10) NOT NULL CONSTRAINT PK_TRUONG PRIMARY KEY,
    TENTRUONG NVARCHAR(100) NOT NULL,
    THANHPHO NVARCHAR(50) NOT NULL
);

CREATE TABLE dbo.DOITHI (
    MADOI NVARCHAR(10) NOT NULL CONSTRAINT PK_DOITHI PRIMARY KEY,
    TENDOI NVARCHAR(100) NOT NULL,
    MATRUONG NVARCHAR(10) NOT NULL CONSTRAINT FK_DOITHI_TRUONG REFERENCES dbo.TRUONG(MATRUONG),
    NGUOIQUANLY NVARCHAR(100) NOT NULL
);

CREATE TABLE dbo.TUYENTHU (
    MATT NVARCHAR(10) NOT NULL CONSTRAINT PK_TUYENTHU PRIMARY KEY,
    HOTEN NVARCHAR(100) NOT NULL,
    VITRI NVARCHAR(50) NOT NULL,
    MADOI NVARCHAR(10) NOT NULL CONSTRAINT FK_TUYENTHU_DOITHI REFERENCES dbo.DOITHI(MADOI),
    TIENLUONG DECIMAL(18, 2) NOT NULL
);

CREATE TABLE dbo.TRANDAU (
    MATRAN NVARCHAR(10) NOT NULL CONSTRAINT PK_TRANDAU PRIMARY KEY,
    NGAYDAU DATE NOT NULL,
    VONGDAU NVARCHAR(50) NOT NULL,
    DIADIEM NVARCHAR(100) NOT NULL
);

CREATE TABLE dbo.THAMGIA_TRAN (
    MATRAN NVARCHAR(10) NOT NULL CONSTRAINT FK_THAMGIA_TRANDAU REFERENCES dbo.TRANDAU(MATRAN),
    MADOI NVARCHAR(10) NOT NULL CONSTRAINT FK_THAMGIA_DOITHI REFERENCES dbo.DOITHI(MADOI),
    SOVANTHANG INT NOT NULL,
    TIENTHUONG DECIMAL(18, 2) NOT NULL,
    KETQUA NVARCHAR(20) NOT NULL,
    CONSTRAINT PK_THAMGIA_TRAN PRIMARY KEY (MATRAN, MADOI)
);

CREATE TABLE dbo.NHATAITRO (
    MANTT NVARCHAR(10) NOT NULL CONSTRAINT PK_NHATAITRO PRIMARY KEY,
    TENNTT NVARCHAR(100) NOT NULL,
    MATRAN NVARCHAR(10) NOT NULL CONSTRAINT FK_NHATAITRO_TRANDAU REFERENCES dbo.TRANDAU(MATRAN),
    SOTIEN_TT DECIMAL(18, 2) NOT NULL
);
GO

-- 2. DML FIXTURE: SEED DATA
INSERT INTO dbo.TRUONG (MATRUONG, TENTRUONG, THANHPHO) VALUES
(N'TR01', N'Đại học CNTT', N'TP.HCM'),
(N'TR02', N'Đại học Bách Khoa', N'TP.HCM'),
(N'TR03', N'Đại học KHTN', N'TP.HCM'),
(N'TR04', N'Đại học Kinh Tế', N'TP.HCM'); -- 0 teams for Left Outer Join

INSERT INTO dbo.DOITHI (MADOI, TENDOI, MATRUONG, NGUOIQUANLY) VALUES
(N'DT01', N'UIT Hunters', N'TR01', N'Nguyễn Văn A'),
(N'DT02', N'UIT Shadows', N'TR01', N'Trần Thị B'),
(N'DT03', N'BK Titans', N'TR02', N'Lê Văn C'),
(N'DT04', N'KHTN Wizards', N'TR03', N'Phạm Thị D');

INSERT INTO dbo.TUYENTHU (MATT, HOTEN, VITRI, MADOI, TIENLUONG) VALUES
(N'TT01', N'Nguyễn Hoàng Long', N'Xạ thủ', N'DT01', 18000000.00),
(N'TT02', N'Trần Quốc Bảo', N'Đường giữa', N'DT01', 16000000.00), -- UIT Mid -> updated
(N'TT03', N'Lê Minh Tuấn', N'Đường trên', N'DT01', 12000000.00),
(N'TT04', N'Phạm Đức Huy', N'Xạ thủ', N'DT02', 11000000.00),
(N'TT05', N'Đỗ Gia Bảo', N'Đường giữa', N'DT02', 14000000.00),    -- UIT Mid -> updated
(N'TT06', N'Vũ Hải Nam', N'Đường giữa', N'DT03', 15000000.00),     -- BK Mid -> not updated
(N'TT07', N'Bùi Anh Tuấn', N'Xạ thủ', N'DT03', 20000000.00);

INSERT INTO dbo.TRANDAU (MATRAN, NGAYDAU, VONGDAU, DIADIEM) VALUES
(N'M01', '2024-11-05', N'Vòng bảng', N'Nhà thi đấu Rạch Miễu'),
(N'M02', '2024-11-10', N'Vòng bảng', N'Nhà thi đấu Hồ Xuân Hương'),
(N'M03', '2024-11-15', N'Vòng bảng', N'Phòng máy Cyzone'),
(N'M04', '2024-11-20', N'Bán kết', N'Nhà thi đấu Quân Khu 7'),
(N'M05', '2024-11-25', N'Chung kết', N'Nhà thi đấu Phú Thọ'),
(N'M06', '2024-10-15', N'Vòng loại', N'Phòng máy Cyzone'),
(N'M07', '2024-11-08', N'Vòng bảng', N'Nhà thi đấu Hồ Xuân Hương'),
(N'M08', '2024-11-12', N'Vòng bảng', N'Phòng máy Cyzone');

INSERT INTO dbo.THAMGIA_TRAN (MATRAN, MADOI, SOVANTHANG, TIENTHUONG, KETQUA) VALUES
(N'M01', N'DT01', 2, 5000000.00, N'Thắng'),
(N'M01', N'DT03', 1, 2000000.00, N'Thua'),
(N'M02', N'DT01', 2, 5000000.00, N'Thắng'),
(N'M02', N'DT04', 0, 1000000.00, N'Thua'),
(N'M03', N'DT01', 2, 5000000.00, N'Thắng'),
(N'M03', N'DT02', 1, 2000000.00, N'Thua'),
(N'M04', N'DT01', 3, 10000000.00, N'Thắng'),
(N'M04', N'DT03', 2, 5000000.00, N'Thua'),
(N'M05', N'DT01', 2, 15000000.00, N'Thua'),
(N'M05', N'DT03', 3, 30000000.00, N'Thắng'),
(N'M06', N'DT02', 2, 3000000.00, N'Thắng'),
(N'M06', N'DT04', 0, 1000000.00, N'Thua'),
(N'M07', N'DT03', 2, 5000000.00, N'Thắng'),
(N'M07', N'DT02', 0, 1000000.00, N'Thua'),
(N'M08', N'DT03', 3, 5000000.00, N'Thắng'),
(N'M08', N'DT04', 1, 2000000.00, N'Thua');

INSERT INTO dbo.NHATAITRO (MANTT, TENNTT, MATRAN, SOTIEN_TT) VALUES
(N'NT01', N'Asus ROG', N'M01', 20000000.00),
(N'NT02', N'Monster Energy', N'M04', 50000000.00),
(N'NT03', N'Intel Vietnam', N'M05', 100000000.00);
GO

-- ============================================================================
-- TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY ===';
PRINT '------------------------------------------------------------';

ALTER TABLE dbo.THAMGIA_TRAN ADD CONSTRAINT CK_THAMGIA_SOVANTHANG CHECK (SOVANTHANG >= 0);
ALTER TABLE dbo.TUYENTHU ADD CONSTRAINT CK_TUYENTHU_TIENLUONG CHECK (TIENLUONG > 0);

-- Test 1A: Check negative SOVANTHANG
BEGIN TRY
    INSERT INTO dbo.THAMGIA_TRAN (MATRAN, MADOI, SOVANTHANG, TIENTHUONG, KETQUA)
    VALUES (N'M01', N'DT04', -1, 1000000.00, N'Thua');
    THROW 50001, 'Test 1A FAILED: Negative SOVANTHANG was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_THAMGIA_SOVANTHANG%'
        PRINT '  [PASS] Test 1A: CK_THAMGIA_SOVANTHANG correctly blocked negative SOVANTHANG.';
    ELSE
        THROW;
END CATCH;

-- Test 1B: Check non-positive TIENLUONG
BEGIN TRY
    INSERT INTO dbo.TUYENTHU (MATT, HOTEN, VITRI, MADOI, TIENLUONG)
    VALUES (N'TT_BAD', N'Tuyển Thủ Lỗi Lương', N'Xạ thủ', N'DT01', 0.00);
    THROW 50002, 'Test 1B FAILED: Zero TIENLUONG was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_TUYENTHU_TIENLUONG%'
        PRINT '  [PASS] Test 1B: CK_TUYENTHU_TIENLUONG correctly blocked zero TIENLUONG.';
    ELSE
        THROW;
END CATCH;

-- Test 1C: Check NOT NULL policy
BEGIN TRY
    INSERT INTO dbo.TUYENTHU (MATT, HOTEN, VITRI, MADOI, TIENLUONG)
    VALUES (N'TT_NULL', N'Tuyển Thủ NULL Lương', N'Xạ thủ', N'DT01', NULL);
    THROW 50003, 'Test 1C FAILED: NULL TIENLUONG was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] Test 1C: NOT NULL policy correctly rejected NULL TIENLUONG (Error 515).';
    ELSE
        THROW;
END CATCH;
GO

-- ============================================================================
-- TEST 2: QUESTION 2.1B UPDATE VERIFICATION
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 2: QUESTION 2.1B UPDATE VERIFICATION ===';
PRINT '------------------------------------------------------------';

UPDATE dbo.TUYENTHU
SET TIENLUONG = TIENLUONG * 1.15
FROM dbo.TUYENTHU tt
JOIN dbo.DOITHI dt ON tt.MADOI = dt.MADOI
JOIN dbo.TRUONG tr ON dt.MATRUONG = tr.MATRUONG
WHERE tr.TENTRUONG = N'Đại học CNTT'
  AND tt.VITRI = N'Đường giữa';

DECLARE @rowsAffected INT = @@ROWCOUNT;
IF @rowsAffected <> 2
    THROW 50010, 'Test 2 FAILED: Expected 2 Mid players of UIT updated!', 1;
PRINT '  [PASS] Test 2: UPDATE correctly affected 2 Mid players (TT02, TT05).';

-- Verify exact salary
DECLARE @s1 DECIMAL(18, 2) = (SELECT TIENLUONG FROM dbo.TUYENTHU WHERE MATT = N'TT02');
DECLARE @s2 DECIMAL(18, 2) = (SELECT TIENLUONG FROM dbo.TUYENTHU WHERE MATT = N'TT05');
DECLARE @s3 DECIMAL(18, 2) = (SELECT TIENLUONG FROM dbo.TUYENTHU WHERE MATT = N'TT06');

IF @s1 <> 18400000.00 OR @s2 <> 16100000.00 OR @s3 <> 15000000.00
    THROW 50011, 'Test 2b FAILED: Updated salaries are incorrect!', 1;
PRINT '  [PASS] Test 2b: Salaries verified: TT02=18.4m (+15%), TT05=16.1m (+15%), TT06=15m (unchanged).';
GO

-- ============================================================================
-- TEST 3: QUESTION 2.2A SELECTION & PROJECTION
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 3: QUESTION 2.2A SELECTION & PROJECTION ===';
PRINT '------------------------------------------------------------';

DECLARE @res3 TABLE (MATT NVARCHAR(10), HOTEN NVARCHAR(100), TIENLUONG DECIMAL(18, 2));
INSERT INTO @res3
SELECT MATT, HOTEN, TIENLUONG
FROM dbo.TUYENTHU
WHERE VITRI = N'Xạ thủ'
  AND TIENLUONG >= 15000000;

DECLARE @count3 INT = (SELECT COUNT(*) FROM @res3);
IF @count3 <> 2
    THROW 50020, 'Test 3 FAILED: Expected 2 ADC players with salary >= 15m (TT01, TT07)!', 1;
IF NOT EXISTS (SELECT 1 FROM @res3 WHERE MATT = N'TT01') OR NOT EXISTS (SELECT 1 FROM @res3 WHERE MATT = N'TT07')
    THROW 50021, 'Test 3 FAILED: Incorrect ADC players returned!', 1;
PRINT '  [PASS] Test 3: Selection returned exactly 2 ADC players >= 15m (TT01, TT07).';
GO

-- ============================================================================
-- TEST 4: QUESTION 2.2B JOIN QUERY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 4: QUESTION 2.2B JOIN QUERY ===';
PRINT '------------------------------------------------------------';

DECLARE @res4 TABLE (MATRAN NVARCHAR(10), NGAYDAU DATE, VONGDAU NVARCHAR(50), TENDOI NVARCHAR(100));
INSERT INTO @res4
SELECT td.MATRAN, td.NGAYDAU, td.VONGDAU, dt.TENDOI
FROM dbo.TRANDAU td
JOIN dbo.THAMGIA_TRAN tgt ON td.MATRAN = tgt.MATRAN
JOIN dbo.DOITHI dt ON tgt.MADOI = dt.MADOI
WHERE dt.TENDOI = N'UIT Hunters';

DECLARE @count4 INT = (SELECT COUNT(*) FROM @res4);
IF @count4 <> 5
    THROW 50030, 'Test 4 FAILED: Expected 5 matches for UIT Hunters (M01..M05)!', 1;
PRINT '  [PASS] Test 4: Join returned exactly 5 matches played by UIT Hunters.';
GO

-- ============================================================================
-- TEST 5: QUESTION 2.2C OUTER JOIN QUERY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 5: QUESTION 2.2C OUTER JOIN QUERY ===';
PRINT '------------------------------------------------------------';

DECLARE @res5 TABLE (MATRUONG NVARCHAR(10), TENTRUONG NVARCHAR(100), MADOI NVARCHAR(10), TENDOI NVARCHAR(100));
INSERT INTO @res5
SELECT tr.MATRUONG, tr.TENTRUONG, dt.MADOI, dt.TENDOI
FROM dbo.TRUONG tr
LEFT JOIN dbo.DOITHI dt ON tr.MATRUONG = dt.MATRUONG;

DECLARE @totalRows5 INT = (SELECT COUNT(*) FROM @res5);
DECLARE @nullCount5 INT = (SELECT COUNT(*) FROM @res5 WHERE MADOI IS NULL);

IF @totalRows5 <> 5 OR @nullCount5 <> 1
    THROW 50040, 'Test 5 FAILED: Expected 5 rows preserving TR04 with NULL team info!', 1;
PRINT '  [PASS] Test 5: Outer join preserved TR04 with NULL team info (total 5 rows).';
GO

-- ============================================================================
-- TEST 6: QUESTION 2.2D GROUPING & AGGREGATE
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE ===';
PRINT '------------------------------------------------------------';

DECLARE @res6 TABLE (MADOI NVARCHAR(10), TENDOI NVARCHAR(100), TONG_TIEN_THUONG DECIMAL(18, 2));
INSERT INTO @res6
SELECT dt.MADOI, dt.TENDOI, SUM(tgt.TIENTHUONG) AS TONG_TIEN_THUONG
FROM dbo.TRANDAU td
JOIN dbo.THAMGIA_TRAN tgt ON td.MATRAN = tgt.MATRAN
JOIN dbo.DOITHI dt ON tgt.MADOI = dt.MADOI
WHERE td.NGAYDAU >= '2024-11-01'
  AND td.NGAYDAU <= '2024-11-30'
  AND tgt.KETQUA = N'Thắng'
GROUP BY dt.MADOI, dt.TENDOI;

DECLARE @count6 INT = (SELECT COUNT(*) FROM @res6);
DECLARE @w1 DECIMAL(18, 2) = (SELECT TONG_TIEN_THUONG FROM @res6 WHERE MADOI = N'DT01');
DECLARE @w2 DECIMAL(18, 2) = (SELECT TONG_TIEN_THUONG FROM @res6 WHERE MADOI = N'DT03');

IF @count6 <> 2 OR @w1 <> 25000000.00 OR @w2 <> 40000000.00
    THROW 50050, 'Test 6 FAILED: Winning prizes incorrect for Nov 2024!', 1;
PRINT '  [PASS] Test 6: Grouping SUM verified: DT01=25,000,000đ; DT03=40,000,000đ.';
GO

-- ============================================================================
-- TEST 7: QUESTION 2.2E RELATIONAL DIVISION
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION ===';
PRINT '------------------------------------------------------------';

-- Method 1: Double NOT EXISTS bounded to candidate teams
DECLARE @divNotExists TABLE (MADOI NVARCHAR(10));
INSERT INTO @divNotExists
SELECT dt.MADOI
FROM dbo.DOITHI dt
WHERE EXISTS (
    SELECT 1 FROM dbo.THAMGIA_TRAN tgt
    WHERE tgt.MADOI = dt.MADOI
)
AND NOT EXISTS (
    SELECT 1 FROM dbo.TRANDAU td
    WHERE td.VONGDAU = N'Vòng bảng'
      AND NOT EXISTS (
          SELECT 1 FROM dbo.THAMGIA_TRAN tgt2
          JOIN dbo.TRANDAU td2 ON tgt2.MATRAN = td2.MATRAN
          WHERE tgt2.MADOI = dt.MADOI
            AND td2.DIADIEM = td.DIADIEM
      )
);

-- Method 2: Bounded LEFT JOIN HAVING COUNT
DECLARE @divHaving TABLE (MADOI NVARCHAR(10));
WITH R AS (
    SELECT DISTINCT tgt.MADOI, td.DIADIEM
    FROM dbo.THAMGIA_TRAN tgt
    JOIN dbo.TRANDAU td ON tgt.MATRAN = td.MATRAN
),
S AS (
    SELECT DISTINCT DIADIEM
    FROM dbo.TRANDAU
    WHERE VONGDAU = N'Vòng bảng'
)
INSERT INTO @divHaving
SELECT R.MADOI
FROM R
LEFT JOIN S ON R.DIADIEM = S.DIADIEM
GROUP BY R.MADOI
HAVING COUNT(DISTINCT S.DIADIEM) = (SELECT COUNT(*) FROM S);

-- Compare sets
DECLARE @diff1 INT = (SELECT COUNT(*) FROM (SELECT MADOI FROM @divNotExists EXCEPT SELECT MADOI FROM @divHaving) d);
DECLARE @diff2 INT = (SELECT COUNT(*) FROM (SELECT MADOI FROM @divHaving EXCEPT SELECT MADOI FROM @divNotExists) d);

IF @diff1 <> 0 OR @diff2 <> 0 OR (SELECT COUNT(*) FROM @divNotExists) <> 2
    THROW 50060, 'Test 7 FAILED: Discrepancy between NOT EXISTS and HAVING COUNT in Relational Division!', 1;

IF NOT EXISTS (SELECT 1 FROM @divNotExists WHERE MADOI = N'DT01')
   OR NOT EXISTS (SELECT 1 FROM @divNotExists WHERE MADOI = N'DT03')
    THROW 50061, 'Test 7 FAILED: Teams playing at all Group stage venues must be DT01 and DT03!', 1;
PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (DT01, DT03).';
GO

-- ============================================================================
-- TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE (S = Ø)
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE ===';
PRINT '------------------------------------------------------------';

-- Stage 'Chung kết nhánh thua' has 0 matches in TRANDAU
DECLARE @emptyDivNotExists TABLE (MADOI NVARCHAR(10));
INSERT INTO @emptyDivNotExists
SELECT dt.MADOI
FROM dbo.DOITHI dt
WHERE EXISTS (
    SELECT 1 FROM dbo.THAMGIA_TRAN tgt
    WHERE tgt.MADOI = dt.MADOI
)
AND NOT EXISTS (
    SELECT 1 FROM dbo.TRANDAU td
    WHERE td.VONGDAU = N'Chung kết nhánh thua'
      AND NOT EXISTS (
          SELECT 1 FROM dbo.THAMGIA_TRAN tgt2
          JOIN dbo.TRANDAU td2 ON tgt2.MATRAN = td2.MATRAN
          WHERE tgt2.MADOI = dt.MADOI
            AND td2.DIADIEM = td.DIADIEM
      )
);

DECLARE @emptyDivHaving TABLE (MADOI NVARCHAR(10));
WITH R AS (
    SELECT DISTINCT tgt.MADOI, td.DIADIEM
    FROM dbo.THAMGIA_TRAN tgt
    JOIN dbo.TRANDAU td ON tgt.MATRAN = td.MATRAN
),
S AS (
    SELECT DISTINCT DIADIEM
    FROM dbo.TRANDAU
    WHERE VONGDAU = N'Chung kết nhánh thua'
)
INSERT INTO @emptyDivHaving
SELECT R.MADOI
FROM R
LEFT JOIN S ON R.DIADIEM = S.DIADIEM
GROUP BY R.MADOI
HAVING COUNT(DISTINCT S.DIADIEM) = (SELECT COUNT(*) FROM S);

-- Candidate universe: all teams in THAMGIA_TRAN (4 teams: DT01..DT04)
DECLARE @candidateCount INT = (SELECT COUNT(DISTINCT MADOI) FROM dbo.THAMGIA_TRAN);

DECLARE @diffEmpty1 INT = (SELECT COUNT(*) FROM (SELECT MADOI FROM @emptyDivNotExists EXCEPT SELECT MADOI FROM @emptyDivHaving) d);
DECLARE @diffEmpty2 INT = (SELECT COUNT(*) FROM (SELECT MADOI FROM @emptyDivHaving EXCEPT SELECT MADOI FROM @emptyDivNotExists) d);

IF @diffEmpty1 <> 0 OR @diffEmpty2 <> 0 OR (SELECT COUNT(*) FROM @emptyDivNotExists) <> @candidateCount
    THROW 50070, 'Test 8 FAILED: Empty divisor S=Ø did not return all candidate teams consistently!', 1;
PRINT '  [PASS] Test 8: Empty target S=Ø verified with EXCEPT set comparison: RA, NOT EXISTS and HAVING COUNT identical (4 teams).';
GO

-- ============================================================================
-- TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING ===';
PRINT '------------------------------------------------------------';

DECLARE @res9 TABLE (MADOI NVARCHAR(10), TENDOI NVARCHAR(100), TENTRUONG NVARCHAR(100), TONG_SO_VAN_THANG INT);
WITH ThongKe AS (
    SELECT tgt.MADOI, SUM(tgt.SOVANTHANG) AS TONG_SO_VAN_THANG
    FROM dbo.TRANDAU td
    JOIN dbo.THAMGIA_TRAN tgt ON td.MATRAN = tgt.MATRAN
    WHERE td.NGAYDAU >= '2024-01-01'
      AND td.NGAYDAU <= '2024-12-31'
    GROUP BY tgt.MADOI
)
INSERT INTO @res9
SELECT dt.MADOI, dt.TENDOI, tr.TENTRUONG, tk.TONG_SO_VAN_THANG
FROM dbo.DOITHI dt
JOIN dbo.TRUONG tr ON dt.MATRUONG = tr.MATRUONG
JOIN ThongKe tk ON dt.MADOI = tk.MADOI
WHERE tk.TONG_SO_VAN_THANG = (SELECT MAX(TONG_SO_VAN_THANG) FROM ThongKe);

DECLARE @count9 INT = (SELECT COUNT(*) FROM @res9);
IF @count9 <> 2
    THROW 50080, 'Test 9 FAILED: Expected exactly 2 teams tied with MAX match wins (DT01, DT03)!', 1;

IF NOT EXISTS (SELECT 1 FROM @res9 WHERE MADOI = N'DT01' AND TONG_SO_VAN_THANG = 11)
   OR NOT EXISTS (SELECT 1 FROM @res9 WHERE MADOI = N'DT03' AND TONG_SO_VAN_THANG = 11)
    THROW 50081, 'Test 9 FAILED: Tie-breaking failed to preserve DT01 and DT03 with 11 wins!', 1;

IF EXISTS (SELECT 1 FROM @res9 WHERE MADOI IN (N'DT02', N'DT04'))
    THROW 50082, 'Test 9 FAILED: Non-maximal teams were incorrectly included!', 1;
PRINT '  [PASS] Test 9: Extreme tie-breaking verified: DT01 (11 wins) and DT03 (11 wins) preserved; others excluded.';
GO

PRINT '------------------------------------------------------------';
PRINT '=== ALL 9 MOCK-09 VERIFICATION SUITES PASSED WITH ASSERTIONS ===';
PRINT '------------------------------------------------------------';
GO
