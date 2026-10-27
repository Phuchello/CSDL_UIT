-- ============================================================================
-- FIXTURE & ADVERSARIAL QA SUITE: MOCK-11
-- Business Domain: Quản Lý Chuỗi Cà Phê Nhượng Quyền & Nguyên Liệu
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
    OBJECT_ID(N'dbo.CHITIET_PX'), OBJECT_ID(N'dbo.PHIEUXUAT'),
    OBJECT_ID(N'dbo.NGUYENLIEU'), OBJECT_ID(N'dbo.NHANVIEN'),
    OBJECT_ID(N'dbo.CUAHANG'), OBJECT_ID(N'dbo.KHUVUC')
);
IF @dropFkSql <> N'' EXEC sp_executesql @dropFkSql;

IF OBJECT_ID(N'dbo.CHITIET_PX', N'U') IS NOT NULL DROP TABLE dbo.CHITIET_PX;
IF OBJECT_ID(N'dbo.PHIEUXUAT', N'U') IS NOT NULL DROP TABLE dbo.PHIEUXUAT;
IF OBJECT_ID(N'dbo.NGUYENLIEU', N'U') IS NOT NULL DROP TABLE dbo.NGUYENLIEU;
IF OBJECT_ID(N'dbo.NHANVIEN', N'U') IS NOT NULL DROP TABLE dbo.NHANVIEN;
IF OBJECT_ID(N'dbo.CUAHANG', N'U') IS NOT NULL DROP TABLE dbo.CUAHANG;
IF OBJECT_ID(N'dbo.KHUVUC', N'U') IS NOT NULL DROP TABLE dbo.KHUVUC;
GO

-- 1. DDL: RELATIONAL SCHEMA
CREATE TABLE dbo.KHUVUC (
    MAKV NVARCHAR(10) NOT NULL CONSTRAINT PK_KHUVUC PRIMARY KEY,
    TENKV NVARCHAR(100) NOT NULL,
    TRUONGVUNG NVARCHAR(100) NOT NULL
);

CREATE TABLE dbo.CUAHANG (
    MACH NVARCHAR(10) NOT NULL CONSTRAINT PK_CUAHANG PRIMARY KEY,
    TENCH NVARCHAR(100) NOT NULL,
    DIACHI NVARCHAR(200) NOT NULL,
    MAKV NVARCHAR(10) NOT NULL CONSTRAINT FK_CUAHANG_KHUVUC REFERENCES dbo.KHUVUC(MAKV),
    NAM_KYHD INT NOT NULL
);

CREATE TABLE dbo.NHANVIEN (
    MANV NVARCHAR(10) NOT NULL CONSTRAINT PK_NHANVIEN PRIMARY KEY,
    HOTEN NVARCHAR(100) NOT NULL,
    CHUCVU NVARCHAR(50) NOT NULL,
    LUONG DECIMAL(18, 2) NOT NULL,
    MACH NVARCHAR(10) NOT NULL CONSTRAINT FK_NHANVIEN_CUAHANG REFERENCES dbo.CUAHANG(MACH)
);

CREATE TABLE dbo.NGUYENLIEU (
    MANL NVARCHAR(10) NOT NULL CONSTRAINT PK_NGUYENLIEU PRIMARY KEY,
    TENNL NVARCHAR(100) NOT NULL,
    LOAINL NVARCHAR(50) NOT NULL,
    DONGIA_CHUAN DECIMAL(18, 2) NOT NULL,
    DVT NVARCHAR(20) NOT NULL
);

CREATE TABLE dbo.PHIEUXUAT (
    MAPX NVARCHAR(10) NOT NULL CONSTRAINT PK_PHIEUXUAT PRIMARY KEY,
    NGAYXUAT DATE NOT NULL,
    MACH NVARCHAR(10) NOT NULL CONSTRAINT FK_PHIEUXUAT_CUAHANG REFERENCES dbo.CUAHANG(MACH),
    TONGTIEN DECIMAL(18, 2) NOT NULL,
    TRANGTHAI NVARCHAR(50) NOT NULL
);

CREATE TABLE dbo.CHITIET_PX (
    MAPX NVARCHAR(10) NOT NULL CONSTRAINT FK_CTPX_PHIEUXUAT REFERENCES dbo.PHIEUXUAT(MAPX),
    MANL NVARCHAR(10) NOT NULL CONSTRAINT FK_CTPX_NGUYENLIEU REFERENCES dbo.NGUYENLIEU(MANL),
    SOLUONG INT NOT NULL,
    DONGIA_XUAT DECIMAL(18, 2) NOT NULL,
    CONSTRAINT PK_CHITIET_PX PRIMARY KEY (MAPX, MANL)
);
GO

-- 2. DML FIXTURE: SEED DATA
INSERT INTO dbo.KHUVUC (MAKV, TENKV, TRUONGVUNG) VALUES
(N'KV01', N'Khu vực Trung tâm', N'Nguyễn Thế Hùng'),
(N'KV02', N'Khu vực Đông Sài Gòn', N'Lê Thị Thu Thủy'),
(N'KV03', N'Khu vực Tây Nam', N'Phạm Quốc Bảo'),
(N'KV04', N'Khu vực Bắc Sài Gòn', N'Trần Đình Trọng'); -- 0 stores for Left Outer Join

INSERT INTO dbo.CUAHANG (MACH, TENCH, DIACHI, MAKV, NAM_KYHD) VALUES
(N'CH01', N'The Coffee House Landmark 81', N'720A Điện Biên Phủ, Bình Thạnh', N'KV01', 2019),
(N'CH02', N'The Coffee House Nhà Thờ', N'01 Công Xã Paris, Q.1', N'KV01', 2018),
(N'CH03', N'The Coffee House Thảo Điền', N'55 Xuân Thủy, TP.Thủ Đức', N'KV02', 2021),
(N'CH04', N'The Coffee House Phú Mỹ Hưng', N'100 Nguyễn Lương Bằng, Q.7', N'KV03', 2020);

INSERT INTO dbo.NHANVIEN (MANV, HOTEN, CHUCVU, LUONG, MACH) VALUES
(N'NV01', N'Lê Hoàng Nam', N'Cửa hàng trưởng', 18000000.00, N'CH01'), -- KV01 Manager -> update
(N'NV02', N'Trần Bảo Anh', N'Pha chế chính', 12000000.00, N'CH01'),   -- not Manager
(N'NV03', N'Phạm Quỳnh Nga', N'Cửa hàng trưởng', 17000000.00, N'CH02'), -- KV01 Manager -> update
(N'NV04', N'Nguyễn Văn Minh', N'Cửa hàng trưởng', 16000000.00, N'CH03'); -- KV02 Manager

INSERT INTO dbo.NGUYENLIEU (MANL, TENNL, LOAINL, DONGIA_CHUAN, DVT) VALUES
(N'NL01', N'Cà phê hạt Robusta Buôn Ma Thuột', N'Hạt cà phê', 220000.00, N'kg'),
(N'NL02', N'Cà phê hạt Arabica Cầu Đất', N'Hạt cà phê', 320000.00, N'kg'),
(N'NL03', N'Cà phê hạt Blend Special', N'Hạt cà phê', 180000.00, N'kg'),
(N'NL04', N'Syrup Caramel Torani', N'Syrup pha chế', 250000.00, N'chai'),
(N'NL05', N'Syrup Hazelnut Monin', N'Syrup pha chế', 280000.00, N'chai'),
(N'NL06', N'Sữa tươi thanh trùng Đà Lạt', N'Sữa đặc & tươi', 45000.00, N'hộp');

INSERT INTO dbo.PHIEUXUAT (MAPX, NGAYXUAT, MACH, TONGTIEN, TRANGTHAI) VALUES
(N'PX01', '2024-11-05', N'CH01', 5000000.00, N'Đã giao'),
(N'PX02', '2024-11-12', N'CH01', 8000000.00, N'Đã giao'),
(N'PX03', '2024-11-15', N'CH02', 4500000.00, N'Đã giao'),
(N'PX04', '2024-11-20', N'CH03', 6000000.00, N'Đã giao'),
(N'PX05', '2024-11-25', N'CH04', 3000000.00, N'Đang chuyển hàng'),
(N'PX06', '2024-10-10', N'CH01', 4000000.00, N'Đã giao');

INSERT INTO dbo.CHITIET_PX (MAPX, MANL, SOLUONG, DONGIA_XUAT) VALUES
-- PX01: NL04 (10), NL01 (15) -> total = 10*250k + 15*220k = 5.8m
(N'PX01', N'NL04', 10, 250000.00),
(N'PX01', N'NL01', 15, 220000.00),
-- PX02: NL05 (10), NL02 (15) -> total = 10*280k + 15*320k = 7.6m
(N'PX02', N'NL05', 10, 280000.00),
(N'PX02', N'NL02', 15, 320000.00),
-- PX03: NL04 (10), NL05 (10), NL06 (40) -> total = 10*250k + 10*280k + 40*45k = 7.1m
(N'PX03', N'NL04', 10, 250000.00),
(N'PX03', N'NL05', 10, 280000.00),
(N'PX03', N'NL06', 40, 45000.00),
-- PX04: NL01 (20), NL06 (30) -> total = 20*220k + 30*45k = 5.75m
(N'PX04', N'NL01', 20, 220000.00),
(N'PX04', N'NL06', 30, 45000.00),
-- PX05: NL04 (5)
(N'PX05', N'NL04', 5, 250000.00),
-- PX06: NL06 (10)
(N'PX06', N'NL06', 10, 45000.00);
GO

-- ============================================================================
-- TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY ===';
PRINT '------------------------------------------------------------';

ALTER TABLE dbo.CHITIET_PX ADD CONSTRAINT CK_CTPX_SOLUONG CHECK (SOLUONG > 0);
ALTER TABLE dbo.CHITIET_PX ADD CONSTRAINT CK_CTPX_DONGIA CHECK (DONGIA_XUAT > 0);

-- Test 1A: Check non-positive SOLUONG
BEGIN TRY
    INSERT INTO dbo.CHITIET_PX (MAPX, MANL, SOLUONG, DONGIA_XUAT)
    VALUES (N'PX01', N'NL03', 0, 180000.00);
    THROW 50001, 'Test 1A FAILED: Zero SOLUONG was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_CTPX_SOLUONG%'
        PRINT '  [PASS] Test 1A: CK_CTPX_SOLUONG correctly blocked zero SOLUONG.';
    ELSE
        THROW;
END CATCH;

-- Test 1B: Check non-positive DONGIA_XUAT
BEGIN TRY
    INSERT INTO dbo.CHITIET_PX (MAPX, MANL, SOLUONG, DONGIA_XUAT)
    VALUES (N'PX01', N'NL03', 5, -5000.00);
    THROW 50002, 'Test 1B FAILED: Negative DONGIA_XUAT was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_CTPX_DONGIA%'
        PRINT '  [PASS] Test 1B: CK_CTPX_DONGIA correctly blocked negative DONGIA_XUAT.';
    ELSE
        THROW;
END CATCH;

-- Test 1C: Check NOT NULL policy
BEGIN TRY
    INSERT INTO dbo.CHITIET_PX (MAPX, MANL, SOLUONG, DONGIA_XUAT)
    VALUES (N'PX01', N'NL03', NULL, 180000.00);
    THROW 50003, 'Test 1C FAILED: NULL SOLUONG was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] Test 1C: NOT NULL policy correctly rejected NULL SOLUONG (Error 515).';
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

UPDATE dbo.NHANVIEN
SET LUONG = LUONG * 1.10
FROM dbo.NHANVIEN nv
JOIN dbo.CUAHANG ch ON nv.MACH = ch.MACH
JOIN dbo.KHUVUC kv ON ch.MAKV = kv.MAKV
WHERE kv.TENKV = N'Khu vực Trung tâm'
  AND nv.CHUCVU = N'Cửa hàng trưởng';

DECLARE @rowsAffected INT = @@ROWCOUNT;
IF @rowsAffected <> 2
    THROW 50010, 'Test 2 FAILED: Expected 2 managers updated in Central region (NV01, NV03)!', 1;
PRINT '  [PASS] Test 2: UPDATE correctly affected 2 store managers (NV01, NV03).';

-- Verify exact salary
DECLARE @s1 DECIMAL(18, 2) = (SELECT LUONG FROM dbo.NHANVIEN WHERE MANV = N'NV01');
DECLARE @s2 DECIMAL(18, 2) = (SELECT LUONG FROM dbo.NHANVIEN WHERE MANV = N'NV03');
DECLARE @s3 DECIMAL(18, 2) = (SELECT LUONG FROM dbo.NHANVIEN WHERE MANV = N'NV02');
DECLARE @s4 DECIMAL(18, 2) = (SELECT LUONG FROM dbo.NHANVIEN WHERE MANV = N'NV04');

IF @s1 <> 19800000.00 OR @s2 <> 18700000.00 OR @s3 <> 12000000.00 OR @s4 <> 16000000.00
    THROW 50011, 'Test 2b FAILED: Updated salaries are incorrect!', 1;
PRINT '  [PASS] Test 2b: Salaries verified: NV01=19.8m (+10%), NV03=18.7m (+10%), NV02=12m (unchanged), NV04=16m (unchanged).';
GO

-- ============================================================================
-- TEST 3: QUESTION 2.2A SELECTION & PROJECTION
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 3: QUESTION 2.2A SELECTION & PROJECTION ===';
PRINT '------------------------------------------------------------';

DECLARE @res3 TABLE (MANL NVARCHAR(10), TENNL NVARCHAR(100), DONGIA_CHUAN DECIMAL(18, 2), DVT NVARCHAR(20));
INSERT INTO @res3
SELECT MANL, TENNL, DONGIA_CHUAN, DVT
FROM dbo.NGUYENLIEU
WHERE LOAINL = N'Hạt cà phê'
  AND DONGIA_CHUAN >= 200000;

DECLARE @count3 INT = (SELECT COUNT(*) FROM @res3);
IF @count3 <> 2
    THROW 50020, 'Test 3 FAILED: Expected 2 coffee bean items >= 200k (NL01, NL02)!', 1;
IF NOT EXISTS (SELECT 1 FROM @res3 WHERE MANL = N'NL01') OR NOT EXISTS (SELECT 1 FROM @res3 WHERE MANL = N'NL02')
    THROW 50021, 'Test 3 FAILED: Incorrect ingredients returned!', 1;
PRINT '  [PASS] Test 3: Selection returned exactly 2 coffee bean items >= 200k (NL01, NL02).';
GO

-- ============================================================================
-- TEST 4: QUESTION 2.2B JOIN QUERY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 4: QUESTION 2.2B JOIN QUERY ===';
PRINT '------------------------------------------------------------';

DECLARE @res4 TABLE (MAPX NVARCHAR(10), NGAYXUAT DATE, TONGTIEN DECIMAL(18, 2), TENCH NVARCHAR(100));
INSERT INTO @res4
SELECT px.MAPX, px.NGAYXUAT, px.TONGTIEN, ch.TENCH
FROM dbo.PHIEUXUAT px
JOIN dbo.CUAHANG ch ON px.MACH = ch.MACH
WHERE ch.TENCH = N'The Coffee House Landmark 81';

DECLARE @count4 INT = (SELECT COUNT(*) FROM @res4);
IF @count4 <> 3
    THROW 50030, 'Test 4 FAILED: Expected 3 slips for Landmark 81 (PX01, PX02, PX06)!', 1;
PRINT '  [PASS] Test 4: Join returned exactly 3 slips (PX01, PX02, PX06).';
GO

-- ============================================================================
-- TEST 5: QUESTION 2.2C OUTER JOIN QUERY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 5: QUESTION 2.2C OUTER JOIN QUERY ===';
PRINT '------------------------------------------------------------';

DECLARE @res5 TABLE (MAKV NVARCHAR(10), TENKV NVARCHAR(100), MACH NVARCHAR(10), TENCH NVARCHAR(100));
INSERT INTO @res5
SELECT kv.MAKV, kv.TENKV, ch.MACH, ch.TENCH
FROM dbo.KHUVUC kv
LEFT JOIN dbo.CUAHANG ch ON kv.MAKV = ch.MAKV;

DECLARE @totalRows5 INT = (SELECT COUNT(*) FROM @res5);
DECLARE @nullCount5 INT = (SELECT COUNT(*) FROM @res5 WHERE MACH IS NULL);

IF @totalRows5 <> 5 OR @nullCount5 <> 1
    THROW 50040, 'Test 5 FAILED: Expected 5 rows preserving KV04 with NULL store info!', 1;
PRINT '  [PASS] Test 5: Outer join preserved KV04 with NULL store info (total 5 rows).';
GO

-- ============================================================================
-- TEST 6: QUESTION 2.2D GROUPING & AGGREGATE
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE ===';
PRINT '------------------------------------------------------------';

DECLARE @res6 TABLE (MAPX NVARCHAR(10), NGAYXUAT DATE, TONG_GIA_TRI_XUAT DECIMAL(18, 2));
INSERT INTO @res6
SELECT px.MAPX, px.NGAYXUAT, SUM(ct.SOLUONG * ct.DONGIA_XUAT) AS TONG_GIA_TRI_XUAT
FROM dbo.PHIEUXUAT px
JOIN dbo.CHITIET_PX ct ON px.MAPX = ct.MAPX
WHERE px.NGAYXUAT >= '2024-11-01'
  AND px.NGAYXUAT <= '2024-11-30'
  AND px.TRANGTHAI = N'Đã giao'
GROUP BY px.MAPX, px.NGAYXUAT;

DECLARE @count6 INT = (SELECT COUNT(*) FROM @res6);
DECLARE @v1 DECIMAL(18, 2) = (SELECT TONG_GIA_TRI_XUAT FROM @res6 WHERE MAPX = N'PX01');
DECLARE @v2 DECIMAL(18, 2) = (SELECT TONG_GIA_TRI_XUAT FROM @res6 WHERE MAPX = N'PX02');
DECLARE @v3 DECIMAL(18, 2) = (SELECT TONG_GIA_TRI_XUAT FROM @res6 WHERE MAPX = N'PX03');
DECLARE @v4 DECIMAL(18, 2) = (SELECT TONG_GIA_TRI_XUAT FROM @res6 WHERE MAPX = N'PX04');

IF @count6 <> 4 OR @v1 <> 5800000.00 OR @v2 <> 7600000.00 OR @v3 <> 7100000.00 OR @v4 <> 5750000.00
    THROW 50050, 'Test 6 FAILED: Grouping sums incorrect for Nov 2024 delivered slips!', 1;
PRINT '  [PASS] Test 6: Grouping SUM verified: PX01=5.80m, PX02=7.60m, PX03=7.10m, PX04=5.75m.';
GO

-- ============================================================================
-- TEST 7: QUESTION 2.2E RELATIONAL DIVISION
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION ===';
PRINT '------------------------------------------------------------';

-- Method 1: Double NOT EXISTS bounded to candidate stores
DECLARE @divNotExists TABLE (MACH NVARCHAR(10));
INSERT INTO @divNotExists
SELECT ch.MACH
FROM dbo.CUAHANG ch
WHERE EXISTS (
    SELECT 1 FROM dbo.PHIEUXUAT px
    JOIN dbo.CHITIET_PX ct ON px.MAPX = ct.MAPX
    WHERE px.MACH = ch.MACH
)
AND NOT EXISTS (
    SELECT 1 FROM dbo.NGUYENLIEU nl
    WHERE nl.LOAINL = N'Syrup pha chế'
      AND NOT EXISTS (
          SELECT 1 FROM dbo.PHIEUXUAT px2
          JOIN dbo.CHITIET_PX ct2 ON px2.MAPX = ct2.MAPX
          WHERE px2.MACH = ch.MACH
            AND ct2.MANL = nl.MANL
      )
);

-- Method 2: Bounded LEFT JOIN HAVING COUNT
DECLARE @divHaving TABLE (MACH NVARCHAR(10));
WITH R AS (
    SELECT DISTINCT px.MACH, ct.MANL
    FROM dbo.PHIEUXUAT px
    JOIN dbo.CHITIET_PX ct ON px.MAPX = ct.MAPX
),
S AS (
    SELECT MANL FROM dbo.NGUYENLIEU WHERE LOAINL = N'Syrup pha chế'
)
INSERT INTO @divHaving
SELECT R.MACH
FROM R
LEFT JOIN S ON R.MANL = S.MANL
GROUP BY R.MACH
HAVING COUNT(DISTINCT S.MANL) = (SELECT COUNT(*) FROM S);

-- Compare sets
DECLARE @diff1 INT = (SELECT COUNT(*) FROM (SELECT MACH FROM @divNotExists EXCEPT SELECT MACH FROM @divHaving) d);
DECLARE @diff2 INT = (SELECT COUNT(*) FROM (SELECT MACH FROM @divHaving EXCEPT SELECT MACH FROM @divNotExists) d);

IF @diff1 <> 0 OR @diff2 <> 0 OR (SELECT COUNT(*) FROM @divNotExists) <> 2
    THROW 50060, 'Test 7 FAILED: Discrepancy between NOT EXISTS and HAVING COUNT in Relational Division!', 1;

IF NOT EXISTS (SELECT 1 FROM @divNotExists WHERE MACH = N'CH01')
   OR NOT EXISTS (SELECT 1 FROM @divNotExists WHERE MACH = N'CH02')
    THROW 50061, 'Test 7 FAILED: Stores importing all syrups must be CH01 and CH02!', 1;
PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (CH01, CH02).';
GO

-- ============================================================================
-- TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE (S = Ø)
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE ===';
PRINT '------------------------------------------------------------';

-- Category 'Bánh ngọt' has 0 ingredients in NGUYENLIEU
DECLARE @emptyDivNotExists TABLE (MACH NVARCHAR(10));
INSERT INTO @emptyDivNotExists
SELECT ch.MACH
FROM dbo.CUAHANG ch
WHERE EXISTS (
    SELECT 1 FROM dbo.PHIEUXUAT px
    JOIN dbo.CHITIET_PX ct ON px.MAPX = ct.MAPX
    WHERE px.MACH = ch.MACH
)
AND NOT EXISTS (
    SELECT 1 FROM dbo.NGUYENLIEU nl
    WHERE nl.LOAINL = N'Bánh ngọt'
      AND NOT EXISTS (
          SELECT 1 FROM dbo.PHIEUXUAT px2
          JOIN dbo.CHITIET_PX ct2 ON px2.MAPX = ct2.MAPX
          WHERE px2.MACH = ch.MACH
            AND ct2.MANL = nl.MANL
      )
);

DECLARE @emptyDivHaving TABLE (MACH NVARCHAR(10));
WITH R AS (
    SELECT DISTINCT px.MACH, ct.MANL
    FROM dbo.PHIEUXUAT px
    JOIN dbo.CHITIET_PX ct ON px.MAPX = ct.MAPX
),
S AS (
    SELECT MANL FROM dbo.NGUYENLIEU WHERE LOAINL = N'Bánh ngọt'
)
INSERT INTO @emptyDivHaving
SELECT R.MACH
FROM R
LEFT JOIN S ON R.MANL = S.MANL
GROUP BY R.MACH
HAVING COUNT(DISTINCT S.MANL) = (SELECT COUNT(*) FROM S);

-- Candidate universe: all stores in CHITIET_PX (4 stores)
DECLARE @candidateCount INT = (
    SELECT COUNT(DISTINCT px.MACH)
    FROM dbo.PHIEUXUAT px
    JOIN dbo.CHITIET_PX ct ON px.MAPX = ct.MAPX
);

DECLARE @diffEmpty1 INT = (SELECT COUNT(*) FROM (SELECT MACH FROM @emptyDivNotExists EXCEPT SELECT MACH FROM @emptyDivHaving) d);
DECLARE @diffEmpty2 INT = (SELECT COUNT(*) FROM (SELECT MACH FROM @emptyDivHaving EXCEPT SELECT MACH FROM @emptyDivNotExists) d);

IF @diffEmpty1 <> 0 OR @diffEmpty2 <> 0 OR (SELECT COUNT(*) FROM @emptyDivNotExists) <> @candidateCount
    THROW 50070, 'Test 8 FAILED: Empty divisor S=Ø did not return all candidate stores consistently!', 1;
PRINT '  [PASS] Test 8: Empty target S=Ø verified with EXCEPT set comparison: RA, NOT EXISTS and HAVING COUNT identical (4 stores).';
GO

-- ============================================================================
-- TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING ===';
PRINT '------------------------------------------------------------';

DECLARE @res9 TABLE (MACH NVARCHAR(10), TENCH NVARCHAR(100), TENKV NVARCHAR(100), TONG_SOLUONG_NHAP INT);
WITH ThongKe AS (
    SELECT px.MACH, SUM(ct.SOLUONG) AS TONG_SOLUONG_NHAP
    FROM dbo.PHIEUXUAT px
    JOIN dbo.CHITIET_PX ct ON px.MAPX = ct.MAPX
    WHERE px.NGAYXUAT >= '2024-01-01'
      AND px.NGAYXUAT <= '2024-12-31'
    GROUP BY px.MACH
)
INSERT INTO @res9
SELECT ch.MACH, ch.TENCH, kv.TENKV, tk.TONG_SOLUONG_NHAP
FROM dbo.CUAHANG ch
JOIN dbo.KHUVUC kv ON ch.MAKV = kv.MAKV
JOIN ThongKe tk ON ch.MACH = tk.MACH
WHERE tk.TONG_SOLUONG_NHAP = (SELECT MAX(TONG_SOLUONG_NHAP) FROM ThongKe);

DECLARE @count9 INT = (SELECT COUNT(*) FROM @res9);
IF @count9 <> 2
    THROW 50080, 'Test 9 FAILED: Expected exactly 2 stores tied with MAX imported ingredients (CH01, CH02)!', 1;

IF NOT EXISTS (SELECT 1 FROM @res9 WHERE MACH = N'CH01' AND TONG_SOLUONG_NHAP = 60)
   OR NOT EXISTS (SELECT 1 FROM @res9 WHERE MACH = N'CH02' AND TONG_SOLUONG_NHAP = 60)
    THROW 50081, 'Test 9 FAILED: Tie-breaking failed to preserve CH01 and CH02 with quantity 60!', 1;

IF EXISTS (SELECT 1 FROM @res9 WHERE MACH IN (N'CH03', N'CH04'))
    THROW 50082, 'Test 9 FAILED: Non-maximal stores were incorrectly included!', 1;
PRINT '  [PASS] Test 9: Extreme tie-breaking verified: CH01 (60 units) and CH02 (60 units) preserved; others excluded.';
GO

PRINT '------------------------------------------------------------';
PRINT '=== ALL 9 MOCK-11 VERIFICATION SUITES PASSED WITH ASSERTIONS ===';
PRINT '------------------------------------------------------------';
GO
