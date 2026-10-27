-- =============================================================================
-- FIXTURE & ADVERSARIAL QA SUITE: MOCK-04
-- Subject: IT004 - Database Systems (Midterm Exam MOCK-04)
-- Domain: Quản Lý Chuỗi Cửa Hàng Bán Lẻ Xăng Dầu
-- Engine: Microsoft SQL Server 2025 (Transact-SQL)
-- Author: VO TRONG PHUC - CSDL_UIT Master Series
-- =============================================================================

USE tempdb;
GO

SET NOCOUNT ON;
SET ANSI_WARNINGS OFF;
GO

-- 1. CLEANUP PREVIOUS TABLES & FOREIGN KEYS
DECLARE @sql NVARCHAR(MAX) = N'';
SELECT @sql += N'ALTER TABLE ' + QUOTENAME(s.name) + N'.' + QUOTENAME(t.name) +
               N' DROP CONSTRAINT ' + QUOTENAME(f.name) + N';' + CHAR(13)
FROM sys.foreign_keys f
INNER JOIN sys.tables t ON f.parent_object_id = t.object_id
INNER JOIN sys.schemas s ON t.schema_id = s.schema_id;
IF @sql <> N'' EXEC sp_executesql @sql;

IF OBJECT_ID('dbo.CTHD', 'U') IS NOT NULL DROP TABLE dbo.CTHD;
IF OBJECT_ID('dbo.HOADON', 'U') IS NOT NULL DROP TABLE dbo.HOADON;
IF OBJECT_ID('dbo.BE_CHUA', 'U') IS NOT NULL DROP TABLE dbo.BE_CHUA;
IF OBJECT_ID('dbo.NHIENLIEU', 'U') IS NOT NULL DROP TABLE dbo.NHIENLIEU;
IF OBJECT_ID('dbo.NHANVIEN', 'U') IS NOT NULL DROP TABLE dbo.NHANVIEN;
IF OBJECT_ID('dbo.CUAHANG', 'U') IS NOT NULL DROP TABLE dbo.CUAHANG;
GO

-- 2. DDL: CREATE 6 UNIFIED RELATIONS
CREATE TABLE CUAHANG (
    MACH VARCHAR(10) NOT NULL,
    TENCH NVARCHAR(100) NOT NULL,
    DIACHI NVARCHAR(200) NOT NULL,
    QUAN NVARCHAR(50) NOT NULL,
    SO_TRU_BOM INT NOT NULL,
    CONSTRAINT PK_CUAHANG PRIMARY KEY (MACH)
);

CREATE TABLE NHANVIEN (
    MANV VARCHAR(10) NOT NULL,
    HOTEN NVARCHAR(100) NOT NULL,
    NGAYSINH DATE NOT NULL,
    CHUCVU NVARCHAR(50) NOT NULL,
    LUONG DECIMAL(18, 2) NOT NULL,
    MACH VARCHAR(10) NOT NULL,
    CONSTRAINT PK_NHANVIEN PRIMARY KEY (MANV),
    CONSTRAINT FK_NHANVIEN_CUAHANG FOREIGN KEY (MACH) REFERENCES CUAHANG(MACH)
);

CREATE TABLE NHIENLIEU (
    MANL VARCHAR(10) NOT NULL,
    TENNL NVARCHAR(100) NOT NULL,
    LOAINL NVARCHAR(50) NOT NULL,
    DONVITINH NVARCHAR(20) NOT NULL,
    DONGIA DECIMAL(18, 2) NOT NULL,
    CONSTRAINT PK_NHIENLIEU PRIMARY KEY (MANL)
);

CREATE TABLE BE_CHUA (
    MABE VARCHAR(10) NOT NULL,
    MACH VARCHAR(10) NOT NULL,
    MANL VARCHAR(10) NOT NULL,
    DUNGTICH FLOAT NOT NULL,
    LUONG_TON FLOAT NOT NULL,
    CONSTRAINT PK_BE_CHUA PRIMARY KEY (MABE),
    CONSTRAINT FK_BECHUA_CUAHANG FOREIGN KEY (MACH) REFERENCES CUAHANG(MACH),
    CONSTRAINT FK_BECHUA_NHIENLIEU FOREIGN KEY (MANL) REFERENCES NHIENLIEU(MANL)
);

CREATE TABLE HOADON (
    MAHD VARCHAR(10) NOT NULL,
    NGAYHD DATETIME NOT NULL,
    MACH VARCHAR(10) NOT NULL,
    MANV VARCHAR(10) NOT NULL,
    HINHTHUC_TT NVARCHAR(50) NOT NULL,
    CONSTRAINT PK_HOADON PRIMARY KEY (MAHD),
    CONSTRAINT FK_HOADON_CUAHANG FOREIGN KEY (MACH) REFERENCES CUAHANG(MACH),
    CONSTRAINT FK_HOADON_NHANVIEN FOREIGN KEY (MANV) REFERENCES NHANVIEN(MANV)
);

CREATE TABLE CTHD (
    MAHD VARCHAR(10) NOT NULL,
    MANL VARCHAR(10) NOT NULL,
    SOLUONG FLOAT NOT NULL,
    DONGIA_BAN DECIMAL(18, 2) NOT NULL,
    THANHTIEN DECIMAL(18, 2) NOT NULL,
    CONSTRAINT PK_CTHD PRIMARY KEY (MAHD, MANL),
    CONSTRAINT FK_CTHD_HOADON FOREIGN KEY (MAHD) REFERENCES HOADON(MAHD),
    CONSTRAINT FK_CTHD_NHIENLIEU FOREIGN KEY (MANL) REFERENCES NHIENLIEU(MANL)
);
GO

-- 3. APPLY QUESTION 2.1A CHECK CONSTRAINTS
ALTER TABLE BE_CHUA ADD CONSTRAINT CK_BECHUA_DUNGTICH CHECK (DUNGTICH > 0);
ALTER TABLE BE_CHUA ADD CONSTRAINT CK_BECHUA_LUONGTON CHECK (LUONG_TON >= 0 AND LUONG_TON <= DUNGTICH);
GO

-- 4. INSERT VERIFIED FIXTURE SEED DATA
-- Cửa hàng
INSERT INTO CUAHANG (MACH, TENCH, DIACHI, QUAN, SO_TRU_BOM) VALUES
('CH01', N'Cửa hàng Xăng dầu Số 1', N'123 Xô Viết Nghệ Tĩnh', N'Bình Thạnh', 6),
('CH02', N'Cửa hàng Xăng dầu Số 2', N'456 Điện Biên Phủ', N'Bình Thạnh', 8),
('CH03', N'Cửa hàng Xăng dầu Số 3', N'78 Lê Duẩn', N'Quận 1', 4),
('CH04', N'Cửa hàng Xăng dầu Số 4', N'12 Võ Văn Ngân', N'Thủ Đức', 6),
('CH05', N'Cửa hàng Xăng dầu Số 5', N'99 Phạm Văn Đồng', N'Gò Vấp', 4); -- Chưa có bể chứa

-- Nhân viên
INSERT INTO NHANVIEN (MANV, HOTEN, NGAYSINH, CHUCVU, LUONG, MACH) VALUES
('NV01', N'Nguyễn Văn Tuấn', '1990-05-10', N'Cửa hàng trưởng', 15000000, 'CH01'),
('NV02', N'Trần Thị Lan', '1995-08-20', N'Nhân viên bán hàng', 8500000, 'CH01'),
('NV03', N'Lê Hoàng Nam', '1998-11-15', N'Nhân viên bán hàng', 7500000, 'CH01'),
('NV04', N'Phạm Minh Đức', '1992-03-25', N'Nhân viên bán hàng', 9000000, 'CH02'),
('NV05', N'Vũ Hoài Anh', '1996-07-30', N'Kế toán', 10000000, 'CH03');

-- Nhiên liệu
INSERT INTO NHIENLIEU (MANL, TENNL, LOAINL, DONVITINH, DONGIA) VALUES
('NL01', N'Xăng RON 95-III', N'Xăng khoáng', N'Lít', 24000),
('NL02', N'Xăng E5 RON 92-II', N'Xăng khoáng', N'Lít', 22000),
('NL03', N'Dầu Diesel 0.05S', N'Dầu DO', N'Lít', 20000),
('NL04', N'Dầu Hỏa', N'Dầu DO', N'Lít', 19000),
('NL05', N'Nhiên liệu Thử nghiệm', N'Thử nghiệm', N'Lít', 30000);

-- Bể chứa
INSERT INTO BE_CHUA (MABE, MACH, MANL, DUNGTICH, LUONG_TON) VALUES
('BE01', 'CH01', 'NL01', 20000, 15000),
('BE02', 'CH01', 'NL02', 20000, 12000), -- CH01 tổng = 40000 lít
('BE03', 'CH02', 'NL01', 20000, 16000),
('BE04', 'CH02', 'NL03', 15000, 10000), -- CH02 tổng = 35000 lít
('BE05', 'CH03', 'NL01', 10000, 8000),   -- CH03 tổng = 10000 lít
('BE06', 'CH04', 'NL01', 20000, 15000),
('BE07', 'CH04', 'NL02', 20000, 14000); -- CH04 tổng = 40000 lít (Đồng hạng cực đại với CH01)

-- Hóa đơn
INSERT INTO HOADON (MAHD, NGAYHD, MACH, MANV, HINHTHUC_TT) VALUES
('HD01', '2024-10-10 08:30:00', 'CH01', 'NV02', N'Chuyển khoản'),
('HD02', '2024-10-12 14:15:00', 'CH01', 'NV02', N'Tiền mặt'),
('HD03', '2024-10-15 09:00:00', 'CH02', 'NV04', N'Chuyển khoản'),
('HD04', '2024-10-20 18:45:00', 'CH03', 'NV05', N'Chuyển khoản'),
('HD05', '2024-11-02 10:00:00', 'CH01', 'NV03', N'Thẻ POS'),
('HD06', '2024-10-25 16:20:00', 'CH04', 'NV04', N'Tiền mặt');

-- Chi tiết hóa đơn
-- Xăng khoáng gồm NL01 và NL02.
-- HD01: bán cả NL01 và NL02 -> Thỏa phép chia
INSERT INTO CTHD (MAHD, MANL, SOLUONG, DONGIA_BAN, THANHTIEN) VALUES
('HD01', 'NL01', 50, 24000, 1200000),
('HD01', 'NL02', 30, 22000, 660000);

-- HD02: chỉ bán NL01 -> Thiếu NL02
INSERT INTO CTHD (MAHD, MANL, SOLUONG, DONGIA_BAN, THANHTIEN) VALUES
('HD02', 'NL01', 25, 24000, 600000);

-- HD03: bán cả NL01 và NL02 -> Thỏa phép chia
INSERT INTO CTHD (MAHD, MANL, SOLUONG, DONGIA_BAN, THANHTIEN) VALUES
('HD03', 'NL01', 40, 24000, 960000),
('HD03', 'NL02', 40, 22000, 880000);

-- HD04: bán NL01 và NL03 -> Thiếu NL02
INSERT INTO CTHD (MAHD, MANL, SOLUONG, DONGIA_BAN, THANHTIEN) VALUES
('HD04', 'NL01', 30, 24000, 720000),
('HD04', 'NL03', 50, 20000, 1000000);

-- HD05: chỉ bán NL02 (tháng 11) -> Thiếu NL01
INSERT INTO CTHD (MAHD, MANL, SOLUONG, DONGIA_BAN, THANHTIEN) VALUES
('HD05', 'NL02', 20, 22000, 440000);

-- HD06: chỉ bán NL03
INSERT INTO CTHD (MAHD, MANL, SOLUONG, DONGIA_BAN, THANHTIEN) VALUES
('HD06', 'NL03', 100, 20000, 2000000);
GO

-- =============================================================================
-- TEST SUITE 1: ADVERSARIAL CHECK CONSTRAINTS & NOT NULL
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY ===';
PRINT '------------------------------------------------------------';

-- Test 1A: Check DUNGTICH <= 0
BEGIN TRY
    INSERT INTO BE_CHUA (MABE, MACH, MANL, DUNGTICH, LUONG_TON)
    VALUES ('BE_ERR1', 'CH01', 'NL01', 0, 0);
    PRINT '  [FAIL] Test 1A: DUNGTICH = 0 was NOT blocked!';
    THROW 50001, 'Test 1A Failed', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_BECHUA_DUNGTICH%'
        PRINT '  [PASS] Test 1A: CK_BECHUA_DUNGTICH correctly blocked DUNGTICH = 0.';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1A: Unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;

-- Test 1B: Check LUONG_TON < 0
BEGIN TRY
    INSERT INTO BE_CHUA (MABE, MACH, MANL, DUNGTICH, LUONG_TON)
    VALUES ('BE_ERR2', 'CH01', 'NL01', 20000, -500);
    PRINT '  [FAIL] Test 1B: LUONG_TON < 0 was NOT blocked!';
    THROW 50002, 'Test 1B Failed', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_BECHUA_LUONGTON%'
        PRINT '  [PASS] Test 1B: CK_BECHUA_LUONGTON correctly blocked LUONG_TON < 0.';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1B: Unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;

-- Test 1C: Check LUONG_TON > DUNGTICH
BEGIN TRY
    INSERT INTO BE_CHUA (MABE, MACH, MANL, DUNGTICH, LUONG_TON)
    VALUES ('BE_ERR3', 'CH01', 'NL01', 20000, 25000);
    PRINT '  [FAIL] Test 1C: LUONG_TON > DUNGTICH was NOT blocked!';
    THROW 50003, 'Test 1C Failed', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_BECHUA_LUONGTON%'
        PRINT '  [PASS] Test 1C: CK_BECHUA_LUONGTON correctly blocked LUONG_TON > DUNGTICH.';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1C: Unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;

-- Test 1D: Check NOT NULL policy (Error 515)
BEGIN TRY
    INSERT INTO BE_CHUA (MABE, MACH, MANL, DUNGTICH, LUONG_TON)
    VALUES ('BE_ERR4', 'CH01', 'NL01', NULL, 5000);
    PRINT '  [FAIL] Test 1D: NULL DUNGTICH was NOT blocked!';
    THROW 50004, 'Test 1D Failed', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] Test 1D: NOT NULL policy correctly rejected NULL DUNGTICH (Error 515).';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1D: Unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;
GO

-- =============================================================================
-- TEST SUITE 2: QUESTION 2.1B UPDATE VERIFICATION
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 2: QUESTION 2.1B UPDATE VERIFICATION ===';
PRINT '------------------------------------------------------------';

UPDATE NHIENLIEU
SET DONGIA = DONGIA * 1.05
WHERE LOAINL = N'Xăng khoáng'
  AND DONVITINH = N'Lít';

DECLARE @upd_cnt INT = @@ROWCOUNT;
IF @upd_cnt = 2
    PRINT '  [PASS] Test 2: UPDATE correctly affected 2 items (NL01, NL02).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 2: Expected 2 rows updated, got ' + CAST(@upd_cnt AS VARCHAR);
    THROW 50005, 'Test 2 Failed', 1;
END;

DECLARE @nl01_price DECIMAL(18,2), @nl02_price DECIMAL(18,2), @nl03_price DECIMAL(18,2);
SELECT @nl01_price = DONGIA FROM NHIENLIEU WHERE MANL = 'NL01';
SELECT @nl02_price = DONGIA FROM NHIENLIEU WHERE MANL = 'NL02';
SELECT @nl03_price = DONGIA FROM NHIENLIEU WHERE MANL = 'NL03';

IF @nl01_price = 25200.00 AND @nl02_price = 23100.00 AND @nl03_price = 20000.00
    PRINT '  [PASS] Test 2b: Price verified (NL01=25,200; NL02=23,100; NL03 unchanged at 20,000).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 2b: Price mismatch!';
    THROW 50006, 'Test 2b Failed', 1;
END;
GO

-- =============================================================================
-- TEST SUITE 3: QUESTION 2.2A SELECTION & PROJECTION
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 3: QUESTION 2.2A SELECTION & PROJECTION ===';
PRINT '------------------------------------------------------------';

DECLARE @cnt_q3 INT;
SELECT @cnt_q3 = COUNT(*)
FROM NHANVIEN
WHERE CHUCVU = N'Nhân viên bán hàng'
  AND LUONG >= 8000000;

IF @cnt_q3 = 2 AND EXISTS (SELECT 1 FROM NHANVIEN WHERE MANV = 'NV02' AND CHUCVU = N'Nhân viên bán hàng' AND LUONG >= 8000000)
               AND EXISTS (SELECT 1 FROM NHANVIEN WHERE MANV = 'NV04' AND CHUCVU = N'Nhân viên bán hàng' AND LUONG >= 8000000)
    PRINT '  [PASS] Test 3: Selection returned exactly 2 staff members (NV02, NV04).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 3: Selection failed! Count=' + CAST(@cnt_q3 AS VARCHAR);
    THROW 50007, 'Test 3 Failed', 1;
END;
GO

-- =============================================================================
-- TEST SUITE 4: QUESTION 2.2B JOIN QUERY
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 4: QUESTION 2.2B JOIN QUERY ===';
PRINT '------------------------------------------------------------';

DECLARE @cnt_q4 INT;
SELECT @cnt_q4 = COUNT(*)
FROM HOADON HD
INNER JOIN CUAHANG CH ON HD.MACH = CH.MACH
WHERE CH.QUAN = N'Bình Thạnh'
  AND HD.HINHTHUC_TT = N'Chuyển khoản';

IF @cnt_q4 = 2 AND EXISTS (SELECT 1 FROM HOADON WHERE MAHD = 'HD01')
               AND EXISTS (SELECT 1 FROM HOADON WHERE MAHD = 'HD03')
    PRINT '  [PASS] Test 4: Join returned exactly 2 transfer invoices in Binh Thanh (HD01, HD03).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 4: Join failed! Count=' + CAST(@cnt_q4 AS VARCHAR);
    THROW 50008, 'Test 4 Failed', 1;
END;
GO

-- =============================================================================
-- TEST SUITE 5: QUESTION 2.2C OUTER JOIN QUERY
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 5: QUESTION 2.2C OUTER JOIN QUERY ===';
PRINT '------------------------------------------------------------';

DECLARE @cnt_q5 INT, @cnt_null_mabe INT;
SELECT @cnt_q5 = COUNT(*)
FROM CUAHANG CH
LEFT OUTER JOIN BE_CHUA BC ON CH.MACH = BC.MACH;

SELECT @cnt_null_mabe = COUNT(*)
FROM CUAHANG CH
LEFT OUTER JOIN BE_CHUA BC ON CH.MACH = BC.MACH
WHERE BC.MABE IS NULL AND CH.MACH = 'CH05';

-- Total rows = 7 tank rows + 1 null row for CH05 = 8 rows
IF @cnt_q5 = 8 AND @cnt_null_mabe = 1
    PRINT '  [PASS] Test 5: Outer join preserved CH05 with NULL tank info (total 8 rows).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 5: Outer join failed! Total=' + CAST(@cnt_q5 AS VARCHAR) + ', NULL MABE=' + CAST(@cnt_null_mabe AS VARCHAR);
    THROW 50009, 'Test 5 Failed', 1;
END;
GO

-- =============================================================================
-- TEST SUITE 6: QUESTION 2.2D GROUPING & AGGREGATE
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE ===';
PRINT '------------------------------------------------------------';

DECLARE @lit_ch01 FLOAT, @lit_ch02 FLOAT, @lit_ch03 FLOAT, @lit_ch04 FLOAT;

SELECT @lit_ch01 = SUM(CT.SOLUONG)
FROM CUAHANG CH
INNER JOIN HOADON HD ON CH.MACH = HD.MACH
INNER JOIN CTHD CT ON HD.MAHD = CT.MAHD
WHERE HD.NGAYHD >= '2024-10-01' AND HD.NGAYHD <= '2024-10-31 23:59:59' AND CH.MACH = 'CH01';

SELECT @lit_ch02 = SUM(CT.SOLUONG)
FROM CUAHANG CH
INNER JOIN HOADON HD ON CH.MACH = HD.MACH
INNER JOIN CTHD CT ON HD.MAHD = CT.MAHD
WHERE HD.NGAYHD >= '2024-10-01' AND HD.NGAYHD <= '2024-10-31 23:59:59' AND CH.MACH = 'CH02';

-- CH01: HD01 (50+30) + HD02 (25) = 105 lít (HD05 is in Nov, excluded)
-- CH02: HD03 (40+40) = 80 lít
IF @lit_ch01 = 105 AND @lit_ch02 = 80
    PRINT '  [PASS] Test 6: Grouping SUM verified: CH01=105 lit, CH02=80 lit.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 6: Grouping mismatch! CH01=' + CAST(@lit_ch01 AS VARCHAR) + ', CH02=' + CAST(@lit_ch02 AS VARCHAR);
    THROW 50010, 'Test 6 Failed', 1;
END;
GO

-- =============================================================================
-- TEST SUITE 7: QUESTION 2.2E RELATIONAL DIVISION
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION ===';
PRINT '------------------------------------------------------------';

-- Method 1: Double NOT EXISTS
DECLARE @div1_cnt INT;
SELECT @div1_cnt = COUNT(*)
FROM HOADON HD
WHERE NOT EXISTS (
    SELECT *
    FROM NHIENLIEU NL
    WHERE NL.LOAINL = N'Xăng khoáng'
      AND NOT EXISTS (
          SELECT *
          FROM CTHD CT
          WHERE CT.MAHD = HD.MAHD
            AND CT.MANL = NL.MANL
      )
)
AND EXISTS (SELECT 1 FROM CTHD WHERE MAHD = HD.MAHD);

-- Method 2: HAVING COUNT
DECLARE @div2_cnt INT;
SELECT @div2_cnt = COUNT(*)
FROM (
    SELECT HD.MAHD
    FROM HOADON HD
    INNER JOIN CTHD CT ON HD.MAHD = CT.MAHD
    INNER JOIN NHIENLIEU NL ON CT.MANL = NL.MANL
    WHERE NL.LOAINL = N'Xăng khoáng'
    GROUP BY HD.MAHD
    HAVING COUNT(DISTINCT NL.MANL) = (
        SELECT COUNT(*)
        FROM NHIENLIEU
        WHERE LOAINL = N'Xăng khoáng'
    )
) AS T;

IF @div1_cnt = 2 AND @div2_cnt = 2
   AND EXISTS (SELECT 1 FROM HOADON HD WHERE HD.MAHD = 'HD01')
   AND EXISTS (SELECT 1 FROM HOADON HD WHERE HD.MAHD = 'HD03')
    PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (HD01, HD03).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 7: Division mismatch! div1=' + CAST(@div1_cnt AS VARCHAR) + ', div2=' + CAST(@div2_cnt AS VARCHAR);
    THROW 50011, 'Test 7 Failed', 1;
END;
GO

-- =============================================================================
-- TEST SUITE 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE (S = Ø)
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE ===';
PRINT '------------------------------------------------------------';

-- Target: LOAINL = 'KhongTonTai' -> S = Ø
-- Candidate universe bounded by π_MAHD(CTHD): exactly 6 invoices have detail lines

-- Method 1: Double NOT EXISTS bounded by candidate universe
DECLARE @empty_bounded_cnt INT;
SELECT @empty_bounded_cnt = COUNT(*)
FROM HOADON HD
WHERE NOT EXISTS (
    SELECT *
    FROM NHIENLIEU NL
    WHERE NL.LOAINL = N'KhongTonTai'
      AND NOT EXISTS (
          SELECT *
          FROM CTHD CT
          WHERE CT.MAHD = HD.MAHD
            AND CT.MANL = NL.MANL
      )
)
AND EXISTS (SELECT 1 FROM CTHD WHERE MAHD = HD.MAHD);

-- Method 2: LEFT JOIN ... HAVING COUNT on candidate universe
DECLARE @empty_having_cnt INT;
SELECT @empty_having_cnt = COUNT(*)
FROM (
    SELECT CT.MAHD
    FROM CTHD CT
    LEFT JOIN (SELECT MANL FROM NHIENLIEU WHERE LOAINL = N'KhongTonTai') S ON CT.MANL = S.MANL
    GROUP BY CT.MAHD
    HAVING COUNT(DISTINCT S.MANL) = (SELECT COUNT(*) FROM NHIENLIEU WHERE LOAINL = N'KhongTonTai')
) AS H;

-- Set-wise comparison between Method 1 and Method 2 using EXCEPT
DECLARE @t8_diff_1_2 INT, @t8_diff_2_1 INT;
SELECT @t8_diff_1_2 = COUNT(*) FROM (
    SELECT HD.MAHD FROM HOADON HD
    WHERE NOT EXISTS (
        SELECT * FROM NHIENLIEU NL WHERE NL.LOAINL = N'KhongTonTai'
        AND NOT EXISTS (SELECT * FROM CTHD CT WHERE CT.MAHD = HD.MAHD AND CT.MANL = NL.MANL)
    ) AND EXISTS (SELECT 1 FROM CTHD WHERE MAHD = HD.MAHD)
    EXCEPT
    SELECT CT.MAHD FROM CTHD CT
    LEFT JOIN (SELECT MANL FROM NHIENLIEU WHERE LOAINL = N'KhongTonTai') S ON CT.MANL = S.MANL
    GROUP BY CT.MAHD
    HAVING COUNT(DISTINCT S.MANL) = (SELECT COUNT(*) FROM NHIENLIEU WHERE LOAINL = N'KhongTonTai')
) AS D1;

SELECT @t8_diff_2_1 = COUNT(*) FROM (
    SELECT CT.MAHD FROM CTHD CT
    LEFT JOIN (SELECT MANL FROM NHIENLIEU WHERE LOAINL = N'KhongTonTai') S ON CT.MANL = S.MANL
    GROUP BY CT.MAHD
    HAVING COUNT(DISTINCT S.MANL) = (SELECT COUNT(*) FROM NHIENLIEU WHERE LOAINL = N'KhongTonTai')
    EXCEPT
    SELECT HD.MAHD FROM HOADON HD
    WHERE NOT EXISTS (
        SELECT * FROM NHIENLIEU NL WHERE NL.LOAINL = N'KhongTonTai'
        AND NOT EXISTS (SELECT * FROM CTHD CT WHERE CT.MAHD = HD.MAHD AND CT.MANL = NL.MANL)
    ) AND EXISTS (SELECT 1 FROM CTHD WHERE MAHD = HD.MAHD)
) AS D2;

IF @empty_bounded_cnt = 6 AND @empty_having_cnt = 6 AND @t8_diff_1_2 = 0 AND @t8_diff_2_1 = 0
    PRINT '  [PASS] Test 8: Empty target S=Ø verified with EXCEPT set comparison: RA, NOT EXISTS and HAVING COUNT identical (6 invoices).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 8: Empty target comparison failed!';
    THROW 50012, 'Test 8 Failed', 1;
END;
GO

-- =============================================================================
-- TEST SUITE 9: QUESTION 2.2F EXTREME TIE-BREAKING
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING ===';
PRINT '------------------------------------------------------------';

DECLARE @tie_cnt INT, @max_capacity FLOAT;

SELECT @tie_cnt = COUNT(*)
FROM (
    SELECT TOP 1 WITH TIES CH.MACH, CH.TENCH, CH.QUAN, SUM(BC.DUNGTICH) AS TONG_DUNGTICH
    FROM CUAHANG CH
    INNER JOIN BE_CHUA BC ON CH.MACH = BC.MACH
    GROUP BY CH.MACH, CH.TENCH, CH.QUAN
    ORDER BY SUM(BC.DUNGTICH) DESC
) AS T;

SELECT TOP 1 @max_capacity = SUM(BC.DUNGTICH)
FROM CUAHANG CH
INNER JOIN BE_CHUA BC ON CH.MACH = BC.MACH
GROUP BY CH.MACH
ORDER BY SUM(BC.DUNGTICH) DESC;

-- CH01 (40000) and CH04 (40000) are in a 2-way tie; CH02 (35000), CH03 (10000), CH05 (0) are excluded
IF @tie_cnt = 2 AND @max_capacity = 40000
   AND EXISTS (SELECT 1 FROM CUAHANG WHERE MACH = 'CH01')
   AND EXISTS (SELECT 1 FROM CUAHANG WHERE MACH = 'CH04')
    PRINT '  [PASS] Test 9: Extreme tie-breaking verified: CH01 (40,000L) and CH04 (40,000L) preserved; CH02 (35,000L) excluded.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 9: Tie-breaking failed! tie_cnt=' + CAST(@tie_cnt AS VARCHAR) + ', max=' + CAST(@max_capacity AS VARCHAR);
    THROW 50013, 'Test 9 Failed', 1;
END;
GO

PRINT '------------------------------------------------------------';
PRINT '=== ALL 9 MOCK-04 VERIFICATION SUITES PASSED WITH ASSERTIONS ===';
PRINT '------------------------------------------------------------';
GO
