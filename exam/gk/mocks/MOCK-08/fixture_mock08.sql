-- ============================================================================
-- FIXTURE & ADVERSARIAL QA SUITE: MOCK-08
-- Business Domain: Sàn Thương Mại Điện Tử & Vận Chuyển Hàng
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
    OBJECT_ID(N'dbo.VANCHUYEN'), OBJECT_ID(N'dbo.CHITIET_DH'),
    OBJECT_ID(N'dbo.DONHANG'), OBJECT_ID(N'dbo.SANPHAM'),
    OBJECT_ID(N'dbo.KHACHHANG'), OBJECT_ID(N'dbo.GIANHANG')
);
IF @dropFkSql <> N'' EXEC sp_executesql @dropFkSql;

IF OBJECT_ID(N'dbo.VANCHUYEN', N'U') IS NOT NULL DROP TABLE dbo.VANCHUYEN;
IF OBJECT_ID(N'dbo.CHITIET_DH', N'U') IS NOT NULL DROP TABLE dbo.CHITIET_DH;
IF OBJECT_ID(N'dbo.DONHANG', N'U') IS NOT NULL DROP TABLE dbo.DONHANG;
IF OBJECT_ID(N'dbo.SANPHAM', N'U') IS NOT NULL DROP TABLE dbo.SANPHAM;
IF OBJECT_ID(N'dbo.KHACHHANG', N'U') IS NOT NULL DROP TABLE dbo.KHACHHANG;
IF OBJECT_ID(N'dbo.GIANHANG', N'U') IS NOT NULL DROP TABLE dbo.GIANHANG;
GO

-- 1. DDL: RELATIONAL SCHEMA
CREATE TABLE dbo.GIANHANG (
    MAGH NVARCHAR(10) NOT NULL CONSTRAINT PK_GIANHANG PRIMARY KEY,
    TENGH NVARCHAR(100) NOT NULL,
    NGUOIDAIDIEN NVARCHAR(100) NOT NULL,
    THANHPHO NVARCHAR(50) NOT NULL
);

CREATE TABLE dbo.SANPHAM (
    MASP NVARCHAR(10) NOT NULL CONSTRAINT PK_SANPHAM PRIMARY KEY,
    TENSP NVARCHAR(200) NOT NULL,
    LOAISP NVARCHAR(50) NOT NULL,
    GIANIEMYET DECIMAL(18, 2) NOT NULL,
    MAGH NVARCHAR(10) NOT NULL CONSTRAINT FK_SANPHAM_GIANHANG REFERENCES dbo.GIANHANG(MAGH)
);

CREATE TABLE dbo.KHACHHANG (
    MAKH NVARCHAR(10) NOT NULL CONSTRAINT PK_KHACHHANG PRIMARY KEY,
    HOTEN NVARCHAR(100) NOT NULL,
    DIACHI NVARCHAR(100) NOT NULL,
    HANGTHANHVIEN NVARCHAR(20) NOT NULL
);

CREATE TABLE dbo.DONHANG (
    MADH NVARCHAR(10) NOT NULL CONSTRAINT PK_DONHANG PRIMARY KEY,
    NGAYDAT DATE NOT NULL,
    MAKH NVARCHAR(10) NOT NULL CONSTRAINT FK_DONHANG_KHACHHANG REFERENCES dbo.KHACHHANG(MAKH),
    HINHTHUCTT NVARCHAR(50) NOT NULL,
    TRANGTHAI NVARCHAR(20) NOT NULL
);

CREATE TABLE dbo.CHITIET_DH (
    MADH NVARCHAR(10) NOT NULL CONSTRAINT FK_CTDH_DONHANG REFERENCES dbo.DONHANG(MADH),
    MASP NVARCHAR(10) NOT NULL CONSTRAINT FK_CTDH_SANPHAM REFERENCES dbo.SANPHAM(MASP),
    SOLUONG INT NOT NULL,
    DONGIA_BAN DECIMAL(18, 2) NOT NULL,
    CONSTRAINT PK_CHITIET_DH PRIMARY KEY (MADH, MASP)
);

CREATE TABLE dbo.VANCHUYEN (
    MAVD NVARCHAR(10) NOT NULL CONSTRAINT PK_VANCHUYEN PRIMARY KEY,
    MADH NVARCHAR(10) NOT NULL CONSTRAINT FK_VANCHUYEN_DONHANG REFERENCES dbo.DONHANG(MADH),
    DONVIVC NVARCHAR(50) NOT NULL,
    CUOCPHI DECIMAL(18, 2) NOT NULL,
    NGAYGIAO DATE NULL
);
GO

-- 2. DML FIXTURE: SEED DATA
INSERT INTO dbo.GIANHANG (MAGH, TENGH, NGUOIDAIDIEN, THANHPHO) VALUES
(N'GH01', N'Gia Dụng Thông Minh', N'Lê Hoàng Nam', N'Hà Nội'),
(N'GH02', N'Thế Giới Công Nghệ', N'Trần Bảo Anh', N'TP.HCM'),
(N'GH03', N'Thời Trang Xu Hướng', N'Phạm Quỳnh Nga', N'Đà Nẵng'), -- 0 products for Outer Join
(N'GH04', N'Mỹ Phẩm Xanh', N'Nguyễn Thị Hoa', N'Hà Nội');          -- 0 products for Outer Join

INSERT INTO dbo.SANPHAM (MASP, TENSP, LOAISP, GIANIEMYET, MAGH) VALUES
(N'SP01', N'Nồi chiên không dầu Lock&Lock', N'Gia dụng', 2500000.00, N'GH01'),
(N'SP02', N'Máy hút bụi cầm tay Philips', N'Gia dụng', 1800000.00, N'GH01'),
(N'SP03', N'Ấm siêu tốc Bluestone', N'Gia dụng', 600000.00, N'GH01'),
(N'SP04', N'Điện thoại iPhone 15 Pro', N'Điện tử', 28000000.00, N'GH02'),
(N'SP05', N'Tai nghe Bluetooth AirPods Pro', N'Điện tử', 5500000.00, N'GH02'),
(N'SP06', N'Laptop Asus Zenbook', N'Điện tử', 22000000.00, N'GH02');

INSERT INTO dbo.KHACHHANG (MAKH, HOTEN, DIACHI, HANGTHANHVIEN) VALUES
(N'KH01', N'Nguyễn Văn Minh', N'Hà Nội', N'Gold'),
(N'KH02', N'Lê Thùy Dương', N'Hà Nội', N'Silver'),
(N'KH03', N'Trần Đình Trọng', N'TP.HCM', N'Diamond'),
(N'KH04', N'Vũ Hải Đăng', N'Đà Nẵng', N'Standard');

INSERT INTO dbo.DONHANG (MADH, NGAYDAT, MAKH, HINHTHUCTT, TRANGTHAI) VALUES
(N'DH01', '2024-11-05', N'KH01', N'Ví điện tử', N'Đã giao'),
(N'DH02', '2024-11-12', N'KH01', N'COD', N'Đã giao'),
(N'DH03', '2024-11-15', N'KH02', N'Ví điện tử', N'Đã giao'),
(N'DH04', '2024-11-20', N'KH03', N'Thẻ tín dụng', N'Đã giao'),
(N'DH05', '2024-11-25', N'KH04', N'Ví điện tử', N'Đã hủy'),
(N'DH06', '2024-10-10', N'KH01', N'Ví điện tử', N'Đã giao'); -- Oct 2024

INSERT INTO dbo.CHITIET_DH (MADH, MASP, SOLUONG, DONGIA_BAN) VALUES
-- DH01: KH01, items=4, value=5.5m (has SP01, SP02, SP03)
(N'DH01', N'SP01', 1, 2500000.00),
(N'DH01', N'SP02', 1, 1800000.00),
(N'DH01', N'SP03', 2, 600000.00),
-- DH02: KH01, items=2, value=33.5m -> KH01 total items in Nov = 6!
(N'DH02', N'SP04', 1, 28000000.00),
(N'DH02', N'SP05', 1, 5500000.00),
-- DH03: KH02, items=6, value=9.8m (has SP01, SP02, SP03) -> KH02 total items in Nov = 6! (TIE)
(N'DH03', N'SP01', 2, 2500000.00),
(N'DH03', N'SP02', 2, 1800000.00),
(N'DH03', N'SP03', 2, 600000.00),
-- DH04: KH03, items=3, value=46.5m
(N'DH04', N'SP06', 2, 22000000.00),
(N'DH04', N'SP01', 1, 2500000.00),
-- DH05: KH04, cancelled
(N'DH05', N'SP05', 1, 5500000.00),
-- DH06: KH01, Oct
(N'DH06', N'SP03', 1, 600000.00);

INSERT INTO dbo.VANCHUYEN (MAVD, MADH, DONVIVC, CUOCPHI, NGAYGIAO) VALUES
(N'VD01', N'DH01', N'Giao Hàng Nhanh', 30000.00, '2024-11-08'),
(N'VD02', N'DH02', N'Viettel Post', 50000.00, '2024-11-15'),
(N'VD03', N'DH03', N'Shopee Xpress', 25000.00, '2024-11-18'),
(N'VD04', N'DH04', N'Giao Hàng Nhanh', 45000.00, '2024-11-23');
GO

-- ============================================================================
-- TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY ===';
PRINT '------------------------------------------------------------';

ALTER TABLE dbo.CHITIET_DH ADD CONSTRAINT CK_CTDH_SOLUONG CHECK (SOLUONG > 0);
ALTER TABLE dbo.SANPHAM ADD CONSTRAINT CK_SANPHAM_GIANIEMYET CHECK (GIANIEMYET > 0);

-- Test 1A: Check SOLUONG <= 0
BEGIN TRY
    INSERT INTO dbo.CHITIET_DH (MADH, MASP, SOLUONG, DONGIA_BAN)
    VALUES (N'DH01', N'SP06', 0, 22000000.00);
    THROW 50001, 'Test 1A FAILED: Zero SOLUONG was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_CTDH_SOLUONG%'
        PRINT '  [PASS] Test 1A: CK_CTDH_SOLUONG correctly blocked SOLUONG = 0.';
    ELSE
        THROW;
END CATCH;

-- Test 1B: Check negative GIANIEMYET
BEGIN TRY
    INSERT INTO dbo.SANPHAM (MASP, TENSP, LOAISP, GIANIEMYET, MAGH)
    VALUES (N'SP_BAD', N'Sản Phẩm Lỗi Giá', N'Gia dụng', -50000.00, N'GH01');
    THROW 50002, 'Test 1B FAILED: Negative GIANIEMYET was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_SANPHAM_GIANIEMYET%'
        PRINT '  [PASS] Test 1B: CK_SANPHAM_GIANIEMYET correctly blocked negative GIANIEMYET.';
    ELSE
        THROW;
END CATCH;

-- Test 1C: Check NOT NULL policy
BEGIN TRY
    INSERT INTO dbo.SANPHAM (MASP, TENSP, LOAISP, GIANIEMYET, MAGH)
    VALUES (N'SP_NULL', N'Sản Phẩm NULL Giá', N'Gia dụng', NULL, N'GH01');
    THROW 50003, 'Test 1C FAILED: NULL GIANIEMYET was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] Test 1C: NOT NULL policy correctly rejected NULL GIANIEMYET (Error 515).';
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

UPDATE dbo.SANPHAM
SET GIANIEMYET = GIANIEMYET * 0.90
FROM dbo.SANPHAM sp
JOIN dbo.GIANHANG gh ON sp.MAGH = gh.MAGH
WHERE gh.NGUOIDAIDIEN = N'Lê Hoàng Nam'
  AND sp.LOAISP = N'Gia dụng';

DECLARE @rowsAffected INT = @@ROWCOUNT;
IF @rowsAffected <> 3
    THROW 50010, 'Test 2 FAILED: Expected 3 home appliances updated for Lê Hoàng Nam!', 1;
PRINT '  [PASS] Test 2: UPDATE correctly affected 3 products (SP01, SP02, SP03).';

-- Verify exact prices
DECLARE @p1 DECIMAL(18, 2) = (SELECT GIANIEMYET FROM dbo.SANPHAM WHERE MASP = N'SP01');
DECLARE @p2 DECIMAL(18, 2) = (SELECT GIANIEMYET FROM dbo.SANPHAM WHERE MASP = N'SP02');
DECLARE @p3 DECIMAL(18, 2) = (SELECT GIANIEMYET FROM dbo.SANPHAM WHERE MASP = N'SP03');
DECLARE @p4 DECIMAL(18, 2) = (SELECT GIANIEMYET FROM dbo.SANPHAM WHERE MASP = N'SP04');

IF @p1 <> 2250000.00 OR @p2 <> 1620000.00 OR @p3 <> 540000.00 OR @p4 <> 28000000.00
    THROW 50011, 'Test 2b FAILED: Discounted prices are incorrect!', 1;
PRINT '  [PASS] Test 2b: Prices verified: SP01=2.25m (-10%), SP02=1.62m (-10%), SP03=540k (-10%), SP04=28m (unchanged).';
GO

-- ============================================================================
-- TEST 3: QUESTION 2.2A SELECTION & PROJECTION
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 3: QUESTION 2.2A SELECTION & PROJECTION ===';
PRINT '------------------------------------------------------------';

DECLARE @res3 TABLE (MASP NVARCHAR(10), TENSP NVARCHAR(200), GIANIEMYET DECIMAL(18, 2));
INSERT INTO @res3
SELECT MASP, TENSP, GIANIEMYET
FROM dbo.SANPHAM
WHERE LOAISP = N'Điện tử'
  AND GIANIEMYET >= 10000000;

DECLARE @count3 INT = (SELECT COUNT(*) FROM @res3);
IF @count3 <> 2
    THROW 50020, 'Test 3 FAILED: Expected 2 electronic products >= 10m (SP04, SP06)!', 1;
IF NOT EXISTS (SELECT 1 FROM @res3 WHERE MASP = N'SP04') OR NOT EXISTS (SELECT 1 FROM @res3 WHERE MASP = N'SP06')
    THROW 50021, 'Test 3 FAILED: Incorrect products returned!', 1;
PRINT '  [PASS] Test 3: Selection returned exactly 2 electronics >= 10m (SP04, SP06).';
GO

-- ============================================================================
-- TEST 4: QUESTION 2.2B JOIN QUERY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 4: QUESTION 2.2B JOIN QUERY ===';
PRINT '------------------------------------------------------------';

DECLARE @res4 TABLE (MADH NVARCHAR(10), NGAYDAT DATE, HINHTHUCTT NVARCHAR(50), HOTEN NVARCHAR(100));
INSERT INTO @res4
SELECT dh.MADH, dh.NGAYDAT, dh.HINHTHUCTT, kh.HOTEN
FROM dbo.DONHANG dh
JOIN dbo.KHACHHANG kh ON dh.MAKH = kh.MAKH
WHERE kh.DIACHI = N'Hà Nội'
  AND dh.HINHTHUCTT = N'Ví điện tử';

DECLARE @count4 INT = (SELECT COUNT(*) FROM @res4);
IF @count4 <> 3
    THROW 50030, 'Test 4 FAILED: Expected 3 orders from Hanoi paid by E-Wallet (DH01, DH03, DH06)!', 1;
PRINT '  [PASS] Test 4: Join returned exactly 3 orders (DH01, DH03, DH06).';
GO

-- ============================================================================
-- TEST 5: QUESTION 2.2C OUTER JOIN QUERY
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 5: QUESTION 2.2C OUTER JOIN QUERY ===';
PRINT '------------------------------------------------------------';

DECLARE @res5 TABLE (MAGH NVARCHAR(10), TENGH NVARCHAR(100), MASP NVARCHAR(10), TENSP NVARCHAR(200));
INSERT INTO @res5
SELECT gh.MAGH, gh.TENGH, sp.MASP, sp.TENSP
FROM dbo.GIANHANG gh
LEFT JOIN dbo.SANPHAM sp ON gh.MAGH = sp.MAGH;

DECLARE @totalRows5 INT = (SELECT COUNT(*) FROM @res5);
DECLARE @nullCount5 INT = (SELECT COUNT(*) FROM @res5 WHERE MASP IS NULL);

IF @totalRows5 <> 8 OR @nullCount5 <> 2
    THROW 50040, 'Test 5 FAILED: Expected 8 rows preserving GH03 and GH04 with NULL product info!', 1;
PRINT '  [PASS] Test 5: Outer join preserved GH03 & GH04 with NULL products (total 8 rows).';
GO

-- ============================================================================
-- TEST 6: QUESTION 2.2D GROUPING & AGGREGATE
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE ===';
PRINT '------------------------------------------------------------';

DECLARE @res6 TABLE (MADH NVARCHAR(10), NGAYDAT DATE, TONG_TIEN_HANG DECIMAL(18, 2));
INSERT INTO @res6
SELECT dh.MADH, dh.NGAYDAT, SUM(ct.SOLUONG * ct.DONGIA_BAN) AS TONG_TIEN_HANG
FROM dbo.DONHANG dh
JOIN dbo.CHITIET_DH ct ON dh.MADH = ct.MADH
WHERE dh.NGAYDAT >= '2024-11-01'
  AND dh.NGAYDAT <= '2024-11-30'
  AND dh.TRANGTHAI = N'Đã giao'
GROUP BY dh.MADH, dh.NGAYDAT;

DECLARE @count6 INT = (SELECT COUNT(*) FROM @res6);
DECLARE @v1 DECIMAL(18, 2) = (SELECT TONG_TIEN_HANG FROM @res6 WHERE MADH = N'DH01');
DECLARE @v2 DECIMAL(18, 2) = (SELECT TONG_TIEN_HANG FROM @res6 WHERE MADH = N'DH02');
DECLARE @v3 DECIMAL(18, 2) = (SELECT TONG_TIEN_HANG FROM @res6 WHERE MADH = N'DH03');
DECLARE @v4 DECIMAL(18, 2) = (SELECT TONG_TIEN_HANG FROM @res6 WHERE MADH = N'DH04');

IF @count6 <> 4 OR @v1 <> 5500000.00 OR @v2 <> 33500000.00 OR @v3 <> 9800000.00 OR @v4 <> 46500000.00
    THROW 50050, 'Test 6 FAILED: Grouping sums incorrect for Nov 2024 delivered orders!', 1;
PRINT '  [PASS] Test 6: Grouping SUM verified: DH01=5.5m, DH02=33.5m, DH03=9.8m, DH04=46.5m.';
GO

-- ============================================================================
-- TEST 7: QUESTION 2.2E RELATIONAL DIVISION
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION ===';
PRINT '------------------------------------------------------------';

-- Method 1: Double NOT EXISTS bounded to candidate orders
DECLARE @divNotExists TABLE (MADH NVARCHAR(10));
INSERT INTO @divNotExists
SELECT dh.MADH
FROM dbo.DONHANG dh
WHERE EXISTS (
    SELECT 1 FROM dbo.CHITIET_DH ct
    WHERE ct.MADH = dh.MADH
)
AND NOT EXISTS (
    SELECT 1 FROM dbo.SANPHAM sp
    JOIN dbo.GIANHANG gh ON sp.MAGH = gh.MAGH
    WHERE sp.LOAISP = N'Gia dụng'
      AND gh.TENGH = N'Gia Dụng Thông Minh'
      AND NOT EXISTS (
          SELECT 1 FROM dbo.CHITIET_DH ct2
          WHERE ct2.MADH = dh.MADH
            AND ct2.MASP = sp.MASP
      )
);

-- Method 2: Bounded LEFT JOIN HAVING COUNT
DECLARE @divHaving TABLE (MADH NVARCHAR(10));
WITH R AS (
    SELECT DISTINCT MADH, MASP
    FROM dbo.CHITIET_DH
),
S AS (
    SELECT sp.MASP
    FROM dbo.SANPHAM sp
    JOIN dbo.GIANHANG gh ON sp.MAGH = gh.MAGH
    WHERE sp.LOAISP = N'Gia dụng'
      AND gh.TENGH = N'Gia Dụng Thông Minh'
)
INSERT INTO @divHaving
SELECT R.MADH
FROM R
LEFT JOIN S ON R.MASP = S.MASP
GROUP BY R.MADH
HAVING COUNT(DISTINCT S.MASP) = (SELECT COUNT(*) FROM S);

-- Compare sets
DECLARE @diff1 INT = (SELECT COUNT(*) FROM (SELECT MADH FROM @divNotExists EXCEPT SELECT MADH FROM @divHaving) d);
DECLARE @diff2 INT = (SELECT COUNT(*) FROM (SELECT MADH FROM @divHaving EXCEPT SELECT MADH FROM @divNotExists) d);

IF @diff1 <> 0 OR @diff2 <> 0 OR (SELECT COUNT(*) FROM @divNotExists) <> 2
    THROW 50060, 'Test 7 FAILED: Discrepancy between NOT EXISTS and HAVING COUNT in Relational Division!', 1;

IF NOT EXISTS (SELECT 1 FROM @divNotExists WHERE MADH = N'DH01')
   OR NOT EXISTS (SELECT 1 FROM @divNotExists WHERE MADH = N'DH03')
    THROW 50061, 'Test 7 FAILED: Orders containing all appliances of Gia Dụng Thông Minh must be DH01 and DH03!', 1;
PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (DH01, DH03).';
GO

-- ============================================================================
-- TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE (S = Ø)
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE ===';
PRINT '------------------------------------------------------------';

-- Category 'Thời trang' has 0 products in GH01
DECLARE @emptyDivNotExists TABLE (MADH NVARCHAR(10));
INSERT INTO @emptyDivNotExists
SELECT dh.MADH
FROM dbo.DONHANG dh
WHERE EXISTS (
    SELECT 1 FROM dbo.CHITIET_DH ct
    WHERE ct.MADH = dh.MADH
)
AND NOT EXISTS (
    SELECT 1 FROM dbo.SANPHAM sp
    JOIN dbo.GIANHANG gh ON sp.MAGH = gh.MAGH
    WHERE sp.LOAISP = N'Thời trang'
      AND gh.TENGH = N'Gia Dụng Thông Minh'
      AND NOT EXISTS (
          SELECT 1 FROM dbo.CHITIET_DH ct2
          WHERE ct2.MADH = dh.MADH
            AND ct2.MASP = sp.MASP
      )
);

DECLARE @emptyDivHaving TABLE (MADH NVARCHAR(10));
WITH R AS (
    SELECT DISTINCT MADH, MASP
    FROM dbo.CHITIET_DH
),
S AS (
    SELECT sp.MASP
    FROM dbo.SANPHAM sp
    JOIN dbo.GIANHANG gh ON sp.MAGH = gh.MAGH
    WHERE sp.LOAISP = N'Thời trang'
      AND gh.TENGH = N'Gia Dụng Thông Minh'
)
INSERT INTO @emptyDivHaving
SELECT R.MADH
FROM R
LEFT JOIN S ON R.MASP = S.MASP
GROUP BY R.MADH
HAVING COUNT(DISTINCT S.MASP) = (SELECT COUNT(*) FROM S);

-- Candidate universe: all orders in CHITIET_DH (6 orders: DH01..DH06)
DECLARE @candidateCount INT = (SELECT COUNT(DISTINCT MADH) FROM dbo.CHITIET_DH);

DECLARE @diffEmpty1 INT = (SELECT COUNT(*) FROM (SELECT MADH FROM @emptyDivNotExists EXCEPT SELECT MADH FROM @emptyDivHaving) d);
DECLARE @diffEmpty2 INT = (SELECT COUNT(*) FROM (SELECT MADH FROM @emptyDivHaving EXCEPT SELECT MADH FROM @emptyDivNotExists) d);

IF @diffEmpty1 <> 0 OR @diffEmpty2 <> 0 OR (SELECT COUNT(*) FROM @emptyDivNotExists) <> @candidateCount
    THROW 50070, 'Test 8 FAILED: Empty divisor S=Ø did not return all candidate orders consistently!', 1;
PRINT '  [PASS] Test 8: Empty target S=Ø verified with EXCEPT set comparison: RA, NOT EXISTS and HAVING COUNT identical (6 orders).';
GO

-- ============================================================================
-- TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING ===';
PRINT '------------------------------------------------------------';

DECLARE @res9 TABLE (MAKH NVARCHAR(10), HOTEN NVARCHAR(100), HANGTHANHVIEN NVARCHAR(20), TONG_SOLUONG INT);
WITH ThongKe AS (
    SELECT dh.MAKH, SUM(ct.SOLUONG) AS TONG_SOLUONG
    FROM dbo.DONHANG dh
    JOIN dbo.CHITIET_DH ct ON dh.MADH = ct.MADH
    WHERE dh.NGAYDAT >= '2024-11-01'
      AND dh.NGAYDAT <= '2024-11-30'
    GROUP BY dh.MAKH
)
INSERT INTO @res9
SELECT kh.MAKH, kh.HOTEN, kh.HANGTHANHVIEN, tk.TONG_SOLUONG
FROM dbo.KHACHHANG kh
JOIN ThongKe tk ON kh.MAKH = tk.MAKH
WHERE tk.TONG_SOLUONG = (SELECT MAX(TONG_SOLUONG) FROM ThongKe);

DECLARE @count9 INT = (SELECT COUNT(*) FROM @res9);
IF @count9 <> 2
    THROW 50080, 'Test 9 FAILED: Expected exactly 2 customers tied with MAX purchased items (KH01, KH02)!', 1;

IF NOT EXISTS (SELECT 1 FROM @res9 WHERE MAKH = N'KH01' AND TONG_SOLUONG = 6)
   OR NOT EXISTS (SELECT 1 FROM @res9 WHERE MAKH = N'KH02' AND TONG_SOLUONG = 6)
    THROW 50081, 'Test 9 FAILED: Tie-breaking failed to preserve KH01 and KH02 with item count 6!', 1;

IF EXISTS (SELECT 1 FROM @res9 WHERE MAKH IN (N'KH03', N'KH04'))
    THROW 50082, 'Test 9 FAILED: Non-maximal customers were incorrectly included!', 1;
PRINT '  [PASS] Test 9: Extreme tie-breaking verified: KH01 (6 items) and KH02 (6 items) preserved; others excluded.';
GO

PRINT '------------------------------------------------------------';
PRINT '=== ALL 9 MOCK-08 VERIFICATION SUITES PASSED WITH ASSERTIONS ===';
PRINT '------------------------------------------------------------';
GO
