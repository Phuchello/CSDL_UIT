-- ============================================================================
-- FIXTURE & ADVERSARIAL QA SUITE: MOCK-07
-- Business Domain: Quản Lý Thư Viện Đại Học & Mượn Trả Sách
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
    OBJECT_ID(N'dbo.CHITIET_MUON'), OBJECT_ID(N'dbo.PHIEUMUON'),
    OBJECT_ID(N'dbo.THUTHU'), OBJECT_ID(N'dbo.SACH'),
    OBJECT_ID(N'dbo.DOCGIA'), OBJECT_ID(N'dbo.KHOAVIEN')
);
IF @dropFkSql <> N'' EXEC sp_executesql @dropFkSql;

IF OBJECT_ID(N'dbo.CHITIET_MUON', N'U') IS NOT NULL DROP TABLE dbo.CHITIET_MUON;
IF OBJECT_ID(N'dbo.PHIEUMUON', N'U') IS NOT NULL DROP TABLE dbo.PHIEUMUON;
IF OBJECT_ID(N'dbo.THUTHU', N'U') IS NOT NULL DROP TABLE dbo.THUTHU;
IF OBJECT_ID(N'dbo.SACH', N'U') IS NOT NULL DROP TABLE dbo.SACH;
IF OBJECT_ID(N'dbo.DOCGIA', N'U') IS NOT NULL DROP TABLE dbo.DOCGIA;
IF OBJECT_ID(N'dbo.KHOAVIEN', N'U') IS NOT NULL DROP TABLE dbo.KHOAVIEN;
GO

-- 1. DDL: RELATIONAL SCHEMA
CREATE TABLE dbo.KHOAVIEN (
    MAKV NVARCHAR(10) NOT NULL CONSTRAINT PK_KHOAVIEN PRIMARY KEY,
    TENKV NVARCHAR(100) NOT NULL,
    NAMTL INT NOT NULL
);

CREATE TABLE dbo.DOCGIA (
    MADG NVARCHAR(10) NOT NULL CONSTRAINT PK_DOCGIA PRIMARY KEY,
    HOTEN NVARCHAR(100) NOT NULL,
    NGAYSINH DATE NOT NULL,
    LOAIDG NVARCHAR(20) NOT NULL,
    MAKV NVARCHAR(10) NOT NULL CONSTRAINT FK_DOCGIA_KHOAVIEN REFERENCES dbo.KHOAVIEN(MAKV)
);

CREATE TABLE dbo.SACH (
    MASACH NVARCHAR(10) NOT NULL CONSTRAINT PK_SACH PRIMARY KEY,
    TENSACH NVARCHAR(200) NOT NULL,
    TACGIA NVARCHAR(100) NOT NULL,
    NXB NVARCHAR(100) NOT NULL,
    NAMXB INT NOT NULL,
    SOLUONGTON INT NOT NULL
);

CREATE TABLE dbo.THUTHU (
    MATT NVARCHAR(10) NOT NULL CONSTRAINT PK_THUTHU PRIMARY KEY,
    HOTEN NVARCHAR(100) NOT NULL,
    SODT NVARCHAR(15) NOT NULL
);

CREATE TABLE dbo.PHIEUMUON (
    MAPM NVARCHAR(10) NOT NULL CONSTRAINT PK_PHIEUMUON PRIMARY KEY,
    NGAYMUON DATE NOT NULL,
    HANTRA DATE NOT NULL,
    MADG NVARCHAR(10) NOT NULL CONSTRAINT FK_PHIEUMUON_DOCGIA REFERENCES dbo.DOCGIA(MADG),
    MATT NVARCHAR(10) NOT NULL CONSTRAINT FK_PHIEUMUON_THUTHU REFERENCES dbo.THUTHU(MATT),
    TRANGTHAI NVARCHAR(20) NOT NULL
);

CREATE TABLE dbo.CHITIET_MUON (
    MAPM NVARCHAR(10) NOT NULL CONSTRAINT FK_CTMUON_PM REFERENCES dbo.PHIEUMUON(MAPM),
    MASACH NVARCHAR(10) NOT NULL CONSTRAINT FK_CTMUON_SACH REFERENCES dbo.SACH(MASACH),
    NGAYTRA DATE NULL,
    TIENPHAT DECIMAL(18, 2) NOT NULL,
    CONSTRAINT PK_CHITIET_MUON PRIMARY KEY (MAPM, MASACH)
);
GO

-- 2. DML FIXTURE: SEED DATA
INSERT INTO dbo.KHOAVIEN (MAKV, TENKV, NAMTL) VALUES
(N'KV01', N'Khoa học Máy tính', 2006),
(N'KV02', N'Kỹ thuật Phần mềm', 2008),
(N'KV03', N'Hệ thống Thông tin', 2006),
(N'KV04', N'Mạng máy tính & Truyền thông', 2007); -- Faculty with 0 readers for Left Outer Join

INSERT INTO dbo.DOCGIA (MADG, HOTEN, NGAYSINH, LOAIDG, MAKV) VALUES
(N'DG01', N'Nguyễn Văn An', '2004-03-15', N'Sinh viên', N'KV01'),
(N'DG02', N'Trần Thị Bích', '2003-08-22', N'Sinh viên', N'KV01'),
(N'DG03', N'Lê Hoàng Nam', '1985-11-10', N'Giảng viên', N'KV02'),
(N'DG04', N'Phạm Quỳnh Nga', '1990-05-18', N'Giảng viên', N'KV03'),
(N'DG05', N'Đỗ Minh Khang', '2004-12-01', N'Sinh viên', N'KV02'),
(N'DG06', N'Hoàng Văn Sơn', '2002-09-09', N'Sinh viên', N'KV03');

INSERT INTO dbo.THUTHU (MATT, HOTEN, SODT) VALUES
(N'TT01', N'Bùi Thu Trang', N'0901234567'),
(N'TT02', N'Vũ Minh Tuấn', N'0912345678');

INSERT INTO dbo.SACH (MASACH, TENSACH, TACGIA, NXB, NAMXB, SOLUONGTON) VALUES
(N'S01', N'Mắt Biếc', N'Nguyễn Nhật Ánh', N'NXB Trẻ', 2018, 15),
(N'S02', N'Tôi Thấy Hoa Vàng Trên Cỏ Xanh', N'Nguyễn Nhật Ánh', N'NXB Trẻ', 2019, 20),
(N'S03', N'Cho Tôi Xin Một Vé Đi Tuổi Thơ', N'Nguyễn Nhật Ánh', N'NXB Trẻ', 2015, 12),
(N'S04', N'Nhập Môn Cơ Sở Dữ Liệu', N'Đỗ Phúc', N'NXB Giáo Dục', 2021, 50),
(N'S05', N'Giải Thuật Lập Trình', N'Lê Minh Hoàng', N'NXB Giáo Dục', 2020, 30),
(N'S06', N'Trí Tuệ Nhân Tạo Hiện Đại', N'Stuart Russell', N'NXB Khoa Học Kỹ Thuật', 2022, 10);

INSERT INTO dbo.PHIEUMUON (MAPM, NGAYMUON, HANTRA, MADG, MATT, TRANGTHAI) VALUES
(N'PM01', '2024-10-05', '2024-10-20', N'DG03', N'TT01', N'Đang mượn'), -- Giảng viên, Oct 2024
(N'PM02', '2024-10-12', '2024-10-27', N'DG04', N'TT02', N'Đang mượn'), -- Giảng viên, Oct 2024
(N'PM03', '2024-10-15', '2024-10-30', N'DG01', N'TT01', N'Đã đóng'),   -- Sinh viên, Oct 2024
(N'PM04', '2024-04-10', '2024-04-25', N'DG01', N'TT02', N'Đã đóng'),   -- Sinh viên, Apr 2024
(N'PM05', '2024-05-18', '2024-06-02', N'DG02', N'TT01', N'Đã đóng'),   -- Sinh viên, May 2024
(N'PM06', '2024-09-01', '2024-09-15', N'DG05', N'TT02', N'Đang mượn'); -- Sinh viên, Sep 2024

INSERT INTO dbo.CHITIET_MUON (MAPM, MASACH, NGAYTRA, TIENPHAT) VALUES
(N'PM01', N'S04', NULL, 0.00),
(N'PM02', N'S05', NULL, 0.00),
(N'PM03', N'S01', '2024-10-28', 0.00),
(N'PM03', N'S04', '2024-10-28', 0.00),  -- DG01 borrows S04 (NXB Giáo Dục)
(N'PM04', N'S02', '2024-04-26', 10000.00), -- DG01 has fine
(N'PM04', N'S03', '2024-04-28', 20000.00), -- DG01 has fine
(N'PM05', N'S01', '2024-06-05', 15000.00), -- DG02 has fine
(N'PM05', N'S02', '2024-06-05', 0.00),
(N'PM05', N'S03', '2024-06-05', 0.00),
(N'PM06', N'S01', NULL, 0.00),
(N'PM06', N'S04', NULL, 0.00);
GO

-- ============================================================================
-- TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY ===';
PRINT '------------------------------------------------------------';

ALTER TABLE dbo.SACH ADD CONSTRAINT CK_SACH_SOLUONGTON CHECK (SOLUONGTON >= 0);
ALTER TABLE dbo.CHITIET_MUON ADD CONSTRAINT CK_CTMUON_TIENPHAT CHECK (TIENPHAT >= 0);

-- Test 1A: Check negative SOLUONGTON
BEGIN TRY
    INSERT INTO dbo.SACH (MASACH, TENSACH, TACGIA, NXB, NAMXB, SOLUONGTON)
    VALUES (N'S_BAD', N'Sách Lỗi Tồn Kho', N'Tác Giả X', N'NXB X', 2024, -5);
    THROW 50001, 'Test 1A FAILED: Negative SOLUONGTON was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_SACH_SOLUONGTON%'
        PRINT '  [PASS] Test 1A: CK_SACH_SOLUONGTON correctly blocked negative SOLUONGTON.';
    ELSE
        THROW;
END CATCH;

-- Test 1B: Check negative TIENPHAT
BEGIN TRY
    INSERT INTO dbo.CHITIET_MUON (MAPM, MASACH, NGAYTRA, TIENPHAT)
    VALUES (N'PM01', N'S01', NULL, -10000.00);
    THROW 50002, 'Test 1B FAILED: Negative TIENPHAT was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_CTMUON_TIENPHAT%'
        PRINT '  [PASS] Test 1B: CK_CTMUON_TIENPHAT correctly blocked negative TIENPHAT.';
    ELSE
        THROW;
END CATCH;

-- Test 1C: Check NOT NULL policy
BEGIN TRY
    INSERT INTO dbo.SACH (MASACH, TENSACH, TACGIA, NXB, NAMXB, SOLUONGTON)
    VALUES (N'S_NULL', N'Sách NULL Tồn', N'Tác Giả Y', N'NXB Y', 2024, NULL);
    THROW 50003, 'Test 1C FAILED: NULL SOLUONGTON was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] Test 1C: NOT NULL policy correctly rejected NULL SOLUONGTON (Error 515).';
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

DECLARE @initialHantras TABLE (MAPM NVARCHAR(10), HANTRA DATE);
INSERT INTO @initialHantras SELECT MAPM, HANTRA FROM dbo.PHIEUMUON;

UPDATE dbo.PHIEUMUON
SET HANTRA = DATEADD(DAY, 15, HANTRA)
FROM dbo.PHIEUMUON pm
JOIN dbo.DOCGIA dg ON pm.MADG = dg.MADG
WHERE dg.LOAIDG = N'Giảng viên'
  AND pm.NGAYMUON >= '2024-10-01'
  AND pm.NGAYMUON <= '2024-10-31';

DECLARE @rowsAffected INT = @@ROWCOUNT;
IF @rowsAffected <> 2
    THROW 50010, 'Test 2 FAILED: Expected 2 rows updated for Lecturer loans in Oct 2024!', 1;
PRINT '  [PASS] Test 2: UPDATE correctly affected 2 loan slips (PM01, PM02).';

-- Verify exact dates: PM01 2024-10-20 -> 2024-11-04; PM02 2024-10-27 -> 2024-11-11; PM03 unchanged
DECLARE @h1 DATE = (SELECT HANTRA FROM dbo.PHIEUMUON WHERE MAPM = N'PM01');
DECLARE @h2 DATE = (SELECT HANTRA FROM dbo.PHIEUMUON WHERE MAPM = N'PM02');
DECLARE @h3 DATE = (SELECT HANTRA FROM dbo.PHIEUMUON WHERE MAPM = N'PM03');

IF @h1 <> '2024-11-04' OR @h2 <> '2024-11-11' OR @h3 <> '2024-10-30'
    THROW 50011, 'Test 2b FAILED: Extended due dates are incorrect!', 1;
PRINT '  [PASS] Test 2b: Due dates verified: PM01=2024-11-04 (+15d), PM02=2024-11-11 (+15d), PM03=2024-10-30 (unchanged).';
GO

-- ============================================================================
-- TEST 3: QUESTION 2.2A SELECTION & PROJECTION
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 3: QUESTION 2.2A SELECTION & PROJECTION ===';
PRINT '------------------------------------------------------------';

DECLARE @res3 TABLE (MADG NVARCHAR(10), HOTEN NVARCHAR(100), NGAYSINH DATE);
INSERT INTO @res3
SELECT dg.MADG, dg.HOTEN, dg.NGAYSINH
FROM dbo.DOCGIA dg
JOIN dbo.KHOAVIEN kv ON dg.MAKV = kv.MAKV
WHERE dg.LOAIDG = N'Sinh viên'
  AND kv.TENKV = N'Khoa học Máy tính';

DECLARE @count3 INT = (SELECT COUNT(*) FROM @res3);
IF @count3 <> 2
    THROW 50020, 'Test 3 FAILED: Expected 2 CS students (DG01, DG02)!', 1;
IF NOT EXISTS (SELECT 1 FROM @res3 WHERE MADG = N'DG01') OR NOT EXISTS (SELECT 1 FROM @res3 WHERE MADG = N'DG02')
    THROW 50021, 'Test 3 FAILED: Incorrect CS student IDs!', 1;
PRINT '  [PASS] Test 3: Selection returned exactly 2 Computer Science students (DG01, DG02).';
GO

-- ============================================================================
-- TEST 4: QUESTION 2.2B JOIN QUERY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 4: QUESTION 2.2B JOIN QUERY ===';
PRINT '------------------------------------------------------------';

DECLARE @res4 TABLE (MASACH NVARCHAR(10), TENSACH NVARCHAR(200), NXB NVARCHAR(100));
INSERT INTO @res4
SELECT s.MASACH, s.TENSACH, s.NXB
FROM dbo.PHIEUMUON pm
JOIN dbo.CHITIET_MUON ct ON pm.MAPM = ct.MAPM
JOIN dbo.SACH s ON ct.MASACH = s.MASACH
WHERE pm.MADG = N'DG01'
  AND s.NXB = N'NXB Giáo Dục';

DECLARE @count4 INT = (SELECT COUNT(*) FROM @res4);
IF @count4 <> 1 OR NOT EXISTS (SELECT 1 FROM @res4 WHERE MASACH = N'S04')
    THROW 50030, 'Test 4 FAILED: Expected exactly 1 book S04 for DG01 from NXB Giáo Dục!', 1;
PRINT '  [PASS] Test 4: Join returned exactly 1 book (S04: Nhập Môn Cơ Sở Dữ Liệu).';
GO

-- ============================================================================
-- TEST 5: QUESTION 2.2C OUTER JOIN QUERY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 5: QUESTION 2.2C OUTER JOIN QUERY ===';
PRINT '------------------------------------------------------------';

DECLARE @res5 TABLE (MAKV NVARCHAR(10), TENKV NVARCHAR(100), MADG NVARCHAR(10), HOTEN NVARCHAR(100));
INSERT INTO @res5
SELECT kv.MAKV, kv.TENKV, dg.MADG, dg.HOTEN
FROM dbo.KHOAVIEN kv
LEFT JOIN dbo.DOCGIA dg ON kv.MAKV = dg.MAKV;

DECLARE @totalRows5 INT = (SELECT COUNT(*) FROM @res5);
DECLARE @nullCount5 INT = (SELECT COUNT(*) FROM @res5 WHERE MADG IS NULL AND MAKV = N'KV04');

IF @totalRows5 <> 7 OR @nullCount5 <> 1
    THROW 50040, 'Test 5 FAILED: Expected 7 rows preserving KV04 with NULL reader info!', 1;
PRINT '  [PASS] Test 5: Outer join preserved KV04 with NULL reader info (total 7 rows).';
GO

-- ============================================================================
-- TEST 6: QUESTION 2.2D GROUPING & AGGREGATE
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE ===';
PRINT '------------------------------------------------------------';

DECLARE @res6 TABLE (MADG NVARCHAR(10), HOTEN NVARCHAR(100), TONG_TIEN_PHAT DECIMAL(18, 2));
INSERT INTO @res6
SELECT dg.MADG, dg.HOTEN, SUM(ct.TIENPHAT) AS TONG_TIEN_PHAT
FROM dbo.PHIEUMUON pm
JOIN dbo.CHITIET_MUON ct ON pm.MAPM = ct.MAPM
JOIN dbo.DOCGIA dg ON pm.MADG = dg.MADG
WHERE pm.NGAYMUON >= '2024-01-01'
  AND pm.NGAYMUON <= '2024-12-31'
  AND ct.TIENPHAT > 0
GROUP BY dg.MADG, dg.HOTEN;

DECLARE @count6 INT = (SELECT COUNT(*) FROM @res6);
DECLARE @fine1 DECIMAL(18, 2) = (SELECT TONG_TIEN_PHAT FROM @res6 WHERE MADG = N'DG01');
DECLARE @fine2 DECIMAL(18, 2) = (SELECT TONG_TIEN_PHAT FROM @res6 WHERE MADG = N'DG02');

IF @count6 <> 2 OR @fine1 <> 30000.00 OR @fine2 <> 15000.00
    THROW 50050, 'Test 6 FAILED: Expected DG01=30,000 and DG02=15,000!', 1;
PRINT '  [PASS] Test 6: Grouping SUM verified: DG01=30,000; DG02=15,000.';
GO

-- ============================================================================
-- TEST 7: QUESTION 2.2E RELATIONAL DIVISION
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION ===';
PRINT '------------------------------------------------------------';

-- Method 1: Double NOT EXISTS bounded to candidate readers
DECLARE @divNotExists TABLE (MADG NVARCHAR(10));
INSERT INTO @divNotExists
SELECT dg.MADG
FROM dbo.DOCGIA dg
WHERE EXISTS (
    SELECT 1 FROM dbo.PHIEUMUON pm
    JOIN dbo.CHITIET_MUON ct ON pm.MAPM = ct.MAPM
    WHERE pm.MADG = dg.MADG
)
AND NOT EXISTS (
    SELECT 1 FROM dbo.SACH s
    WHERE s.TACGIA = N'Nguyễn Nhật Ánh'
      AND NOT EXISTS (
          SELECT 1 FROM dbo.PHIEUMUON pm2
          JOIN dbo.CHITIET_MUON ct2 ON pm2.MAPM = ct2.MAPM
          WHERE pm2.MADG = dg.MADG
            AND ct2.MASACH = s.MASACH
      )
);

-- Method 2: Bounded LEFT JOIN HAVING COUNT
DECLARE @divHaving TABLE (MADG NVARCHAR(10));
WITH R AS (
    SELECT DISTINCT pm.MADG, ct.MASACH
    FROM dbo.PHIEUMUON pm
    JOIN dbo.CHITIET_MUON ct ON pm.MAPM = ct.MAPM
),
S AS (
    SELECT MASACH FROM dbo.SACH WHERE TACGIA = N'Nguyễn Nhật Ánh'
)
INSERT INTO @divHaving
SELECT R.MADG
FROM R
LEFT JOIN S ON R.MASACH = S.MASACH
GROUP BY R.MADG
HAVING COUNT(DISTINCT S.MASACH) = (SELECT COUNT(*) FROM S);

-- Compare sets
DECLARE @diff1 INT = (SELECT COUNT(*) FROM (SELECT MADG FROM @divNotExists EXCEPT SELECT MADG FROM @divHaving) d);
DECLARE @diff2 INT = (SELECT COUNT(*) FROM (SELECT MADG FROM @divHaving EXCEPT SELECT MADG FROM @divNotExists) d);

IF @diff1 <> 0 OR @diff2 <> 0 OR (SELECT COUNT(*) FROM @divNotExists) <> 2
    THROW 50060, 'Test 7 FAILED: Discrepancy between NOT EXISTS and HAVING COUNT in Relational Division!', 1;

IF NOT EXISTS (SELECT 1 FROM @divNotExists WHERE MADG = N'DG01')
   OR NOT EXISTS (SELECT 1 FROM @divNotExists WHERE MADG = N'DG02')
    THROW 50061, 'Test 7 FAILED: Readers who borrowed all books of Nguyễn Nhật Ánh should be DG01 and DG02!', 1;
PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (DG01, DG02).';
GO

-- ============================================================================
-- TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE (S = Ø)
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE ===';
PRINT '------------------------------------------------------------';

-- Author 'Haruki Murakami' has 0 books in SACH
DECLARE @emptyDivNotExists TABLE (MADG NVARCHAR(10));
INSERT INTO @emptyDivNotExists
SELECT dg.MADG
FROM dbo.DOCGIA dg
WHERE EXISTS (
    SELECT 1 FROM dbo.PHIEUMUON pm
    JOIN dbo.CHITIET_MUON ct ON pm.MAPM = ct.MAPM
    WHERE pm.MADG = dg.MADG
)
AND NOT EXISTS (
    SELECT 1 FROM dbo.SACH s
    WHERE s.TACGIA = N'Haruki Murakami'
      AND NOT EXISTS (
          SELECT 1 FROM dbo.PHIEUMUON pm2
          JOIN dbo.CHITIET_MUON ct2 ON pm2.MAPM = ct2.MAPM
          WHERE pm2.MADG = dg.MADG
            AND ct2.MASACH = s.MASACH
      )
);

DECLARE @emptyDivHaving TABLE (MADG NVARCHAR(10));
WITH R AS (
    SELECT DISTINCT pm.MADG, ct.MASACH
    FROM dbo.PHIEUMUON pm
    JOIN dbo.CHITIET_MUON ct ON pm.MAPM = ct.MAPM
),
S AS (
    SELECT MASACH FROM dbo.SACH WHERE TACGIA = N'Haruki Murakami'
)
INSERT INTO @emptyDivHaving
SELECT R.MADG
FROM R
LEFT JOIN S ON R.MASACH = S.MASACH
GROUP BY R.MADG
HAVING COUNT(DISTINCT S.MASACH) = (SELECT COUNT(*) FROM S);

-- Candidate universe: all readers who have ever borrowed a book (5 readers: DG01, DG02, DG03, DG04, DG05)
DECLARE @candidateCount INT = (
    SELECT COUNT(DISTINCT pm.MADG)
    FROM dbo.PHIEUMUON pm
    JOIN dbo.CHITIET_MUON ct ON pm.MAPM = ct.MAPM
);

DECLARE @diffEmpty1 INT = (SELECT COUNT(*) FROM (SELECT MADG FROM @emptyDivNotExists EXCEPT SELECT MADG FROM @emptyDivHaving) d);
DECLARE @diffEmpty2 INT = (SELECT COUNT(*) FROM (SELECT MADG FROM @emptyDivHaving EXCEPT SELECT MADG FROM @emptyDivNotExists) d);

IF @diffEmpty1 <> 0 OR @diffEmpty2 <> 0 OR (SELECT COUNT(*) FROM @emptyDivNotExists) <> @candidateCount
    THROW 50070, 'Test 8 FAILED: Empty divisor S=Ø did not return all candidate readers consistently!', 1;
PRINT '  [PASS] Test 8: Empty target S=Ø verified with EXCEPT set comparison: RA, NOT EXISTS and HAVING COUNT identical (5 readers).';
GO

-- ============================================================================
-- TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING ===';
PRINT '------------------------------------------------------------';

DECLARE @res9 TABLE (MASACH NVARCHAR(10), TENSACH NVARCHAR(200), TACGIA NVARCHAR(100), SO_LUOT_MUON INT);
WITH ThongKe AS (
    SELECT ct.MASACH, COUNT(pm.MAPM) AS SO_LUOT_MUON
    FROM dbo.PHIEUMUON pm
    JOIN dbo.CHITIET_MUON ct ON pm.MAPM = ct.MAPM
    WHERE pm.NGAYMUON >= '2024-01-01'
      AND pm.NGAYMUON <= '2024-12-31'
    GROUP BY ct.MASACH
)
INSERT INTO @res9
SELECT s.MASACH, s.TENSACH, s.TACGIA, tk.SO_LUOT_MUON
FROM dbo.SACH s
JOIN ThongKe tk ON s.MASACH = tk.MASACH
WHERE tk.SO_LUOT_MUON = (SELECT MAX(SO_LUOT_MUON) FROM ThongKe);

DECLARE @count9 INT = (SELECT COUNT(*) FROM @res9);
IF @count9 <> 2
    THROW 50080, 'Test 9 FAILED: Expected exactly 2 books tied with MAX loans (S01, S04)!', 1;

IF NOT EXISTS (SELECT 1 FROM @res9 WHERE MASACH = N'S01' AND SO_LUOT_MUON = 3)
   OR NOT EXISTS (SELECT 1 FROM @res9 WHERE MASACH = N'S04' AND SO_LUOT_MUON = 3)
    THROW 50081, 'Test 9 FAILED: Tie-breaking failed to preserve S01 and S04 with count 3!', 1;

IF EXISTS (SELECT 1 FROM @res9 WHERE MASACH IN (N'S02', N'S03', N'S05', N'S06'))
    THROW 50082, 'Test 9 FAILED: Non-maximal books were incorrectly included!', 1;
PRINT '  [PASS] Test 9: Extreme tie-breaking verified: S01 (3 loans) and S04 (3 loans) preserved; others excluded.';
GO

PRINT '------------------------------------------------------------';
PRINT '=== ALL 9 MOCK-07 VERIFICATION SUITES PASSED WITH ASSERTIONS ===';
PRINT '------------------------------------------------------------';
GO
