-- ============================================================================
-- FIXTURE & ADVERSARIAL QA SUITE: MOCK-10
-- Business Domain: Quản Lý Gara Ô Tô & Phụ Tùng Bảo Dưỡng
-- Profile: HISTORICAL_2023_2024 (10.0đ, 75 mins)
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
    OBJECT_ID(N'dbo.CHITIET_BD'), OBJECT_ID(N'dbo.PHIEU_BD'),
    OBJECT_ID(N'dbo.PHUTUNG'), OBJECT_ID(N'dbo.THO'),
    OBJECT_ID(N'dbo.XE'), OBJECT_ID(N'dbo.KHACHHANG')
);
IF @dropFkSql <> N'' EXEC sp_executesql @dropFkSql;

IF OBJECT_ID(N'dbo.CHITIET_BD', N'U') IS NOT NULL DROP TABLE dbo.CHITIET_BD;
IF OBJECT_ID(N'dbo.PHIEU_BD', N'U') IS NOT NULL DROP TABLE dbo.PHIEU_BD;
IF OBJECT_ID(N'dbo.PHUTUNG', N'U') IS NOT NULL DROP TABLE dbo.PHUTUNG;
IF OBJECT_ID(N'dbo.THO', N'U') IS NOT NULL DROP TABLE dbo.THO;
IF OBJECT_ID(N'dbo.XE', N'U') IS NOT NULL DROP TABLE dbo.XE;
IF OBJECT_ID(N'dbo.KHACHHANG', N'U') IS NOT NULL DROP TABLE dbo.KHACHHANG;
GO

-- 1. DDL: RELATIONAL SCHEMA
CREATE TABLE dbo.KHACHHANG (
    MAKH NVARCHAR(10) NOT NULL CONSTRAINT PK_KHACHHANG PRIMARY KEY,
    HOTEN NVARCHAR(100) NOT NULL,
    DIENTHOAI NVARCHAR(20) NOT NULL,
    DIACHI NVARCHAR(100) NOT NULL
);

CREATE TABLE dbo.XE (
    BIENSO NVARCHAR(20) NOT NULL CONSTRAINT PK_XE PRIMARY KEY,
    HANGXE NVARCHAR(50) NOT NULL,
    MODEL NVARCHAR(50) NOT NULL,
    NAMSX INT NOT NULL,
    MAKH NVARCHAR(10) NOT NULL CONSTRAINT FK_XE_KHACHHANG REFERENCES dbo.KHACHHANG(MAKH)
);

CREATE TABLE dbo.THO (
    MATHO NVARCHAR(10) NOT NULL CONSTRAINT PK_THO PRIMARY KEY,
    HOTEN NVARCHAR(100) NOT NULL,
    CHUYENMON NVARCHAR(50) NOT NULL,
    LUONG_CB DECIMAL(18, 2) NOT NULL
);

CREATE TABLE dbo.PHUTUNG (
    MAPT NVARCHAR(10) NOT NULL CONSTRAINT PK_PHUTUNG PRIMARY KEY,
    TENPT NVARCHAR(100) NOT NULL,
    LOAIPT NVARCHAR(50) NOT NULL,
    DONGIA DECIMAL(18, 2) NOT NULL,
    SOLUONGTON INT NOT NULL
);

CREATE TABLE dbo.PHIEU_BD (
    MAPHIEU NVARCHAR(10) NOT NULL CONSTRAINT PK_PHIEU_BD PRIMARY KEY,
    NGAYLAP DATE NOT NULL,
    BIENSO NVARCHAR(20) NOT NULL CONSTRAINT FK_PHIEUBD_XE REFERENCES dbo.XE(BIENSO),
    MATHO NVARCHAR(10) NOT NULL CONSTRAINT FK_PHIEUBD_THO REFERENCES dbo.THO(MATHO),
    TONGTIEN DECIMAL(18, 2) NOT NULL,
    TRANGTHAI NVARCHAR(50) NOT NULL
);

CREATE TABLE dbo.CHITIET_BD (
    MAPHIEU NVARCHAR(10) NOT NULL CONSTRAINT FK_CTBD_PHIEU REFERENCES dbo.PHIEU_BD(MAPHIEU),
    MAPT NVARCHAR(10) NOT NULL CONSTRAINT FK_CTBD_PHUTUNG REFERENCES dbo.PHUTUNG(MAPT),
    SOLUONG INT NOT NULL,
    TIENCONG DECIMAL(18, 2) NOT NULL,
    CONSTRAINT PK_CHITIET_BD PRIMARY KEY (MAPHIEU, MAPT)
);
GO

-- 2. DML FIXTURE: SEED DATA
INSERT INTO dbo.KHACHHANG (MAKH, HOTEN, DIENTHOAI, DIACHI) VALUES
(N'KH01', N'Nguyễn Văn Hùng', N'0903111222', N'TP.HCM'),
(N'KH02', N'Lê Thị Thu', N'0918222333', N'Bình Dương'),
(N'KH03', N'Trần Đình Trọng', N'0988333444', N'Đồng Nai'),
(N'KH04', N'Phạm Minh Tuấn', N'0977444555', N'TP.HCM'); -- 0 cars for Left Outer Join

INSERT INTO dbo.XE (BIENSO, HANGXE, MODEL, NAMSX, MAKH) VALUES
(N'51A-12345', N'Toyota', N'Camry', 2023, N'KH01'),
(N'51K-67890', N'Toyota', N'Corolla Cross', 2022, N'KH01'),
(N'60B-55566', N'Toyota', N'Vios', 2020, N'KH02'),
(N'61C-99988', N'Honda', N'CR-V', 2023, N'KH03'),
(N'51H-33322', N'Ford', N'Ranger', 2021, N'KH03');

INSERT INTO dbo.THO (MATHO, HOTEN, CHUYENMON, LUONG_CB) VALUES
(N'TH01', N'Trần Văn Mạnh', N'Máy gầm', 15000000.00),
(N'TH02', N'Nguyễn Tuấn Kiệt', N'Máy gầm', 14000000.00),
(N'TH03', N'Lê Hoàng Nam', N'Máy gầm', 13000000.00), -- no Nov slips
(N'TH04', N'Vũ Minh Tuấn', N'Điện lạnh', 16000000.00);

INSERT INTO dbo.PHUTUNG (MAPT, TENPT, LOAIPT, DONGIA, SOLUONGTON) VALUES
(N'PT01', N'Dầu động cơ Castrol Edge', N'Dầu nhớt', 850000.00, 50),
(N'PT02', N'Dầu hộp số tự động Mobil', N'Dầu nhớt', 650000.00, 30),
(N'PT03', N'Dầu phanh DOT 4 Bosch', N'Dầu nhớt', 250000.00, 40),
(N'PT04', N'Má phanh trước Brembo', N'Hệ thống phanh', 1500000.00, 20),
(N'PT05', N'Lọc gió động cơ Toyota Genuine', N'Lọc gió', 350000.00, 60),
(N'PT06', N'Bugi Iridium NGK', N'Đánh lửa', 200000.00, 100);

INSERT INTO dbo.PHIEU_BD (MAPHIEU, NGAYLAP, BIENSO, MATHO, TONGTIEN, TRANGTHAI) VALUES
(N'P01', '2024-11-05', N'51A-12345', N'TH01', 2500000.00, N'Đã hoàn thành'),
(N'P02', '2024-11-12', N'51A-12345', N'TH02', 1500000.00, N'Đã hoàn thành'),
(N'P03', '2024-11-15', N'51K-67890', N'TH01', 3000000.00, N'Đã hoàn thành'),
(N'P04', '2024-11-20', N'60B-55566', N'TH02', 1800000.00, N'Đã hoàn thành'),
(N'P05', '2024-11-25', N'61C-99988', N'TH04', 4000000.00, N'Đang xử lý'),
(N'P06', '2024-10-10', N'51A-12345', N'TH01', 2000000.00, N'Đã hoàn thành');

INSERT INTO dbo.CHITIET_BD (MAPHIEU, MAPT, SOLUONG, TIENCONG) VALUES
-- P01: PT01 (2), PT02 (1) -> total PT cost = 2*850k + 1*650k = 2.35m
(N'P01', N'PT01', 2, 200000.00),
(N'P01', N'PT02', 1, 150000.00),
-- P02: PT03 (2), PT05 (2) -> total PT cost = 2*250k + 2*350k = 1.2m
(N'P02', N'PT03', 2, 100000.00),
(N'P02', N'PT05', 2, 100000.00),
-- P03: PT01 (2), PT02 (1), PT03 (1) -> total PT cost = 2*850k + 1*650k + 1*250k = 2.6m
(N'P03', N'PT01', 2, 200000.00),
(N'P03', N'PT02', 1, 150000.00),
(N'P03', N'PT03', 1, 100000.00),
-- P04: PT01 (1), PT05 (2) -> total PT cost = 1*850k + 2*350k = 1.55m
(N'P04', N'PT01', 1, 200000.00),
(N'P04', N'PT05', 2, 100000.00),
-- P05: PT04 (2)
(N'P05', N'PT04', 2, 300000.00),
-- P06: PT05 (1)
(N'P06', N'PT05', 1, 100000.00);
GO

-- ============================================================================
-- TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY ===';
PRINT '------------------------------------------------------------';

ALTER TABLE dbo.PHUTUNG ADD CONSTRAINT CK_PHUTUNG_SOLUONGTON CHECK (SOLUONGTON >= 0);
ALTER TABLE dbo.PHUTUNG ADD CONSTRAINT CK_PHUTUNG_DONGIA CHECK (DONGIA > 0);

-- Test 1A: Check negative SOLUONGTON
BEGIN TRY
    INSERT INTO dbo.PHUTUNG (MAPT, TENPT, LOAIPT, DONGIA, SOLUONGTON)
    VALUES (N'PT_BAD1', N'Phụ tùng lỗi tồn', N'Lọc gió', 100000.00, -5);
    THROW 50001, 'Test 1A FAILED: Negative SOLUONGTON was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_PHUTUNG_SOLUONGTON%'
        PRINT '  [PASS] Test 1A: CK_PHUTUNG_SOLUONGTON correctly blocked negative SOLUONGTON.';
    ELSE
        THROW;
END CATCH;

-- Test 1B: Check non-positive DONGIA
BEGIN TRY
    INSERT INTO dbo.PHUTUNG (MAPT, TENPT, LOAIPT, DONGIA, SOLUONGTON)
    VALUES (N'PT_BAD2', N'Phụ tùng lỗi giá', N'Lọc gió', 0.00, 10);
    THROW 50002, 'Test 1B FAILED: Zero DONGIA was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_PHUTUNG_DONGIA%'
        PRINT '  [PASS] Test 1B: CK_PHUTUNG_DONGIA correctly blocked zero DONGIA.';
    ELSE
        THROW;
END CATCH;

-- Test 1C: Check NOT NULL policy
BEGIN TRY
    INSERT INTO dbo.PHUTUNG (MAPT, TENPT, LOAIPT, DONGIA, SOLUONGTON)
    VALUES (N'PT_NULL', N'Phụ tùng NULL giá', N'Lọc gió', NULL, 10);
    THROW 50003, 'Test 1C FAILED: NULL DONGIA was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] Test 1C: NOT NULL policy correctly rejected NULL DONGIA (Error 515).';
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

UPDATE dbo.THO
SET LUONG_CB = LUONG_CB * 1.10
FROM dbo.THO t
WHERE t.CHUYENMON = N'Máy gầm'
  AND EXISTS (
      SELECT 1 FROM dbo.PHIEU_BD pbd
      WHERE pbd.MATHO = t.MATHO
        AND pbd.NGAYLAP >= '2024-11-01'
        AND pbd.NGAYLAP <= '2024-11-30'
  );

DECLARE @rowsAffected INT = @@ROWCOUNT;
IF @rowsAffected <> 2
    THROW 50010, 'Test 2 FAILED: Expected 2 mechanics updated (TH01, TH02)!', 1;
PRINT '  [PASS] Test 2: UPDATE correctly affected 2 mechanics (TH01, TH02).';

-- Verify exact salary
DECLARE @s1 DECIMAL(18, 2) = (SELECT LUONG_CB FROM dbo.THO WHERE MATHO = N'TH01');
DECLARE @s2 DECIMAL(18, 2) = (SELECT LUONG_CB FROM dbo.THO WHERE MATHO = N'TH02');
DECLARE @s3 DECIMAL(18, 2) = (SELECT LUONG_CB FROM dbo.THO WHERE MATHO = N'TH03');
DECLARE @s4 DECIMAL(18, 2) = (SELECT LUONG_CB FROM dbo.THO WHERE MATHO = N'TH04');

IF @s1 <> 16500000.00 OR @s2 <> 15400000.00 OR @s3 <> 13000000.00 OR @s4 <> 16000000.00
    THROW 50011, 'Test 2b FAILED: Updated salaries are incorrect!', 1;
PRINT '  [PASS] Test 2b: Salaries verified: TH01=16.5m (+10%), TH02=15.4m (+10%), TH03=13m (unchanged), TH04=16m (unchanged).';
GO

-- ============================================================================
-- TEST 3: QUESTION 2.2A SELECTION & PROJECTION
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 3: QUESTION 2.2A SELECTION & PROJECTION ===';
PRINT '------------------------------------------------------------';

DECLARE @res3 TABLE (BIENSO NVARCHAR(20), HANGXE NVARCHAR(50), MODEL NVARCHAR(50), NAMSX INT);
INSERT INTO @res3
SELECT BIENSO, HANGXE, MODEL, NAMSX
FROM dbo.XE
WHERE HANGXE = N'Toyota'
  AND NAMSX >= 2022;

DECLARE @count3 INT = (SELECT COUNT(*) FROM @res3);
IF @count3 <> 2
    THROW 50020, 'Test 3 FAILED: Expected 2 Toyota cars >= 2022 (51A-12345, 51K-67890)!', 1;
IF NOT EXISTS (SELECT 1 FROM @res3 WHERE BIENSO = N'51A-12345') OR NOT EXISTS (SELECT 1 FROM @res3 WHERE BIENSO = N'51K-67890')
    THROW 50021, 'Test 3 FAILED: Incorrect cars returned!', 1;
PRINT '  [PASS] Test 3: Selection returned exactly 2 Toyota cars >= 2022 (51A-12345, 51K-67890).';
GO

-- ============================================================================
-- TEST 4: QUESTION 2.2B JOIN QUERY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 4: QUESTION 2.2B JOIN QUERY ===';
PRINT '------------------------------------------------------------';

DECLARE @res4 TABLE (MAPHIEU NVARCHAR(10), NGAYLAP DATE, BIENSO NVARCHAR(20), HOTEN NVARCHAR(100));
INSERT INTO @res4
SELECT pbd.MAPHIEU, pbd.NGAYLAP, pbd.BIENSO, t.HOTEN
FROM dbo.PHIEU_BD pbd
JOIN dbo.THO t ON pbd.MATHO = t.MATHO
WHERE t.HOTEN = N'Trần Văn Mạnh';

DECLARE @count4 INT = (SELECT COUNT(*) FROM @res4);
IF @count4 <> 3
    THROW 50030, 'Test 4 FAILED: Expected 3 slips managed by Trần Văn Mạnh (P01, P03, P06)!', 1;
PRINT '  [PASS] Test 4: Join returned exactly 3 slips (P01, P03, P06).';
GO

-- ============================================================================
-- TEST 5: QUESTION 2.2C OUTER JOIN QUERY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 5: QUESTION 2.2C OUTER JOIN QUERY ===';
PRINT '------------------------------------------------------------';

DECLARE @res5 TABLE (MAKH NVARCHAR(10), HOTEN NVARCHAR(100), BIENSO NVARCHAR(20), HANGXE NVARCHAR(50));
INSERT INTO @res5
SELECT kh.MAKH, kh.HOTEN, x.BIENSO, x.HANGXE
FROM dbo.KHACHHANG kh
LEFT JOIN dbo.XE x ON kh.MAKH = x.MAKH;

DECLARE @totalRows5 INT = (SELECT COUNT(*) FROM @res5);
DECLARE @nullCount5 INT = (SELECT COUNT(*) FROM @res5 WHERE BIENSO IS NULL);

IF @totalRows5 <> 6 OR @nullCount5 <> 1
    THROW 50040, 'Test 5 FAILED: Expected 6 rows preserving KH04 with NULL car info!', 1;
PRINT '  [PASS] Test 5: Outer join preserved KH04 with NULL car info (total 6 rows).';
GO

-- ============================================================================
-- TEST 6: QUESTION 2.2D GROUPING & AGGREGATE
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE ===';
PRINT '------------------------------------------------------------';

DECLARE @res6 TABLE (MAPHIEU NVARCHAR(10), NGAYLAP DATE, TONG_TIEN_PHU_TUNG DECIMAL(18, 2));
INSERT INTO @res6
SELECT pbd.MAPHIEU, pbd.NGAYLAP, SUM(ct.SOLUONG * pt.DONGIA) AS TONG_TIEN_PHU_TUNG
FROM dbo.PHIEU_BD pbd
JOIN dbo.CHITIET_BD ct ON pbd.MAPHIEU = ct.MAPHIEU
JOIN dbo.PHUTUNG pt ON ct.MAPT = pt.MAPT
WHERE pbd.NGAYLAP >= '2024-11-01'
  AND pbd.NGAYLAP <= '2024-11-30'
  AND pbd.TRANGTHAI = N'Đã hoàn thành'
GROUP BY pbd.MAPHIEU, pbd.NGAYLAP;

DECLARE @count6 INT = (SELECT COUNT(*) FROM @res6);
DECLARE @v1 DECIMAL(18, 2) = (SELECT TONG_TIEN_PHU_TUNG FROM @res6 WHERE MAPHIEU = N'P01');
DECLARE @v2 DECIMAL(18, 2) = (SELECT TONG_TIEN_PHU_TUNG FROM @res6 WHERE MAPHIEU = N'P02');
DECLARE @v3 DECIMAL(18, 2) = (SELECT TONG_TIEN_PHU_TUNG FROM @res6 WHERE MAPHIEU = N'P03');
DECLARE @v4 DECIMAL(18, 2) = (SELECT TONG_TIEN_PHU_TUNG FROM @res6 WHERE MAPHIEU = N'P04');

IF @count6 <> 4 OR @v1 <> 2350000.00 OR @v2 <> 1200000.00 OR @v3 <> 2600000.00 OR @v4 <> 1550000.00
    THROW 50050, 'Test 6 FAILED: Grouping sums incorrect for Nov 2024 completed slips!', 1;
PRINT '  [PASS] Test 6: Grouping SUM verified: P01=2.35m, P02=1.20m, P03=2.60m, P04=1.55m.';
GO

-- ============================================================================
-- TEST 7: QUESTION 2.2E RELATIONAL DIVISION
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION ===';
PRINT '------------------------------------------------------------';

-- Method 1: Double NOT EXISTS bounded to candidate vehicles
DECLARE @divNotExists TABLE (BIENSO NVARCHAR(20));
INSERT INTO @divNotExists
SELECT x.BIENSO
FROM dbo.XE x
WHERE EXISTS (
    SELECT 1 FROM dbo.PHIEU_BD pbd
    JOIN dbo.CHITIET_BD ct ON pbd.MAPHIEU = ct.MAPHIEU
    WHERE pbd.BIENSO = x.BIENSO
)
AND NOT EXISTS (
    SELECT 1 FROM dbo.PHUTUNG pt
    WHERE pt.LOAIPT = N'Dầu nhớt'
      AND NOT EXISTS (
          SELECT 1 FROM dbo.PHIEU_BD pbd2
          JOIN dbo.CHITIET_BD ct2 ON pbd2.MAPHIEU = ct2.MAPHIEU
          WHERE pbd2.BIENSO = x.BIENSO
            AND ct2.MAPT = pt.MAPT
      )
);

-- Method 2: Bounded LEFT JOIN HAVING COUNT
DECLARE @divHaving TABLE (BIENSO NVARCHAR(20));
WITH R AS (
    SELECT DISTINCT pbd.BIENSO, ct.MAPT
    FROM dbo.PHIEU_BD pbd
    JOIN dbo.CHITIET_BD ct ON pbd.MAPHIEU = ct.MAPHIEU
),
S AS (
    SELECT MAPT FROM dbo.PHUTUNG WHERE LOAIPT = N'Dầu nhớt'
)
INSERT INTO @divHaving
SELECT R.BIENSO
FROM R
LEFT JOIN S ON R.MAPT = S.MAPT
GROUP BY R.BIENSO
HAVING COUNT(DISTINCT S.MAPT) = (SELECT COUNT(*) FROM S);

-- Compare sets
DECLARE @diff1 INT = (SELECT COUNT(*) FROM (SELECT BIENSO FROM @divNotExists EXCEPT SELECT BIENSO FROM @divHaving) d);
DECLARE @diff2 INT = (SELECT COUNT(*) FROM (SELECT BIENSO FROM @divHaving EXCEPT SELECT BIENSO FROM @divNotExists) d);

IF @diff1 <> 0 OR @diff2 <> 0 OR (SELECT COUNT(*) FROM @divNotExists) <> 2
    THROW 50060, 'Test 7 FAILED: Discrepancy between NOT EXISTS and HAVING COUNT in Relational Division!', 1;

IF NOT EXISTS (SELECT 1 FROM @divNotExists WHERE BIENSO = N'51A-12345')
   OR NOT EXISTS (SELECT 1 FROM @divNotExists WHERE BIENSO = N'51K-67890')
    THROW 50061, 'Test 7 FAILED: Cars replacing all oils must be 51A-12345 and 51K-67890!', 1;
PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (51A-12345, 51K-67890).';
GO

-- ============================================================================
-- TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE (S = Ø)
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE ===';
PRINT '------------------------------------------------------------';

-- Category 'Ắc quy' has 0 parts in PHUTUNG
DECLARE @emptyDivNotExists TABLE (BIENSO NVARCHAR(20));
INSERT INTO @emptyDivNotExists
SELECT x.BIENSO
FROM dbo.XE x
WHERE EXISTS (
    SELECT 1 FROM dbo.PHIEU_BD pbd
    JOIN dbo.CHITIET_BD ct ON pbd.MAPHIEU = ct.MAPHIEU
    WHERE pbd.BIENSO = x.BIENSO
)
AND NOT EXISTS (
    SELECT 1 FROM dbo.PHUTUNG pt
    WHERE pt.LOAIPT = N'Ắc quy'
      AND NOT EXISTS (
          SELECT 1 FROM dbo.PHIEU_BD pbd2
          JOIN dbo.CHITIET_BD ct2 ON pbd2.MAPHIEU = ct2.MAPHIEU
          WHERE pbd2.BIENSO = x.BIENSO
            AND ct2.MAPT = pt.MAPT
      )
);

DECLARE @emptyDivHaving TABLE (BIENSO NVARCHAR(20));
WITH R AS (
    SELECT DISTINCT pbd.BIENSO, ct.MAPT
    FROM dbo.PHIEU_BD pbd
    JOIN dbo.CHITIET_BD ct ON pbd.MAPHIEU = ct.MAPHIEU
),
S AS (
    SELECT MAPT FROM dbo.PHUTUNG WHERE LOAIPT = N'Ắc quy'
)
INSERT INTO @emptyDivHaving
SELECT R.BIENSO
FROM R
LEFT JOIN S ON R.MAPT = S.MAPT
GROUP BY R.BIENSO
HAVING COUNT(DISTINCT S.MAPT) = (SELECT COUNT(*) FROM S);

-- Candidate universe: all vehicles in CHITIET_BD (4 vehicles)
DECLARE @candidateCount INT = (
    SELECT COUNT(DISTINCT pbd.BIENSO)
    FROM dbo.PHIEU_BD pbd
    JOIN dbo.CHITIET_BD ct ON pbd.MAPHIEU = ct.MAPHIEU
);

DECLARE @diffEmpty1 INT = (SELECT COUNT(*) FROM (SELECT BIENSO FROM @emptyDivNotExists EXCEPT SELECT BIENSO FROM @emptyDivHaving) d);
DECLARE @diffEmpty2 INT = (SELECT COUNT(*) FROM (SELECT BIENSO FROM @emptyDivHaving EXCEPT SELECT BIENSO FROM @emptyDivNotExists) d);

IF @diffEmpty1 <> 0 OR @diffEmpty2 <> 0 OR (SELECT COUNT(*) FROM @emptyDivNotExists) <> @candidateCount
    THROW 50070, 'Test 8 FAILED: Empty divisor S=Ø did not return all candidate cars consistently!', 1;
PRINT '  [PASS] Test 8: Empty target S=Ø verified with EXCEPT set comparison: RA, NOT EXISTS and HAVING COUNT identical (4 vehicles).';
GO

-- ============================================================================
-- TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING ===';
PRINT '------------------------------------------------------------';

DECLARE @res9 TABLE (MAPT NVARCHAR(10), TENPT NVARCHAR(100), LOAIPT NVARCHAR(50), TONG_SOLUONG INT);
WITH ThongKe AS (
    SELECT ct.MAPT, SUM(ct.SOLUONG) AS TONG_SOLUONG
    FROM dbo.PHIEU_BD pbd
    JOIN dbo.CHITIET_BD ct ON pbd.MAPHIEU = ct.MAPHIEU
    WHERE pbd.NGAYLAP >= '2024-01-01'
      AND pbd.NGAYLAP <= '2024-12-31'
    GROUP BY ct.MAPT
)
INSERT INTO @res9
SELECT pt.MAPT, pt.TENPT, pt.LOAIPT, tk.TONG_SOLUONG
FROM dbo.PHUTUNG pt
JOIN ThongKe tk ON pt.MAPT = tk.MAPT
WHERE tk.TONG_SOLUONG = (SELECT MAX(TONG_SOLUONG) FROM ThongKe);

DECLARE @count9 INT = (SELECT COUNT(*) FROM @res9);
IF @count9 <> 2
    THROW 50080, 'Test 9 FAILED: Expected exactly 2 parts tied with MAX replacement quantity (PT01, PT05)!', 1;

IF NOT EXISTS (SELECT 1 FROM @res9 WHERE MAPT = N'PT01' AND TONG_SOLUONG = 5)
   OR NOT EXISTS (SELECT 1 FROM @res9 WHERE MAPT = N'PT05' AND TONG_SOLUONG = 5)
    THROW 50081, 'Test 9 FAILED: Tie-breaking failed to preserve PT01 and PT05 with count 5!', 1;

IF EXISTS (SELECT 1 FROM @res9 WHERE MAPT IN (N'PT02', N'PT03', N'PT04', N'PT06'))
    THROW 50082, 'Test 9 FAILED: Non-maximal parts were incorrectly included!', 1;
PRINT '  [PASS] Test 9: Extreme tie-breaking verified: PT01 (5 units) and PT05 (5 units) preserved; others excluded.';
GO

PRINT '------------------------------------------------------------';
PRINT '=== ALL 9 MOCK-10 VERIFICATION SUITES PASSED WITH ASSERTIONS ===';
PRINT '------------------------------------------------------------';
GO
