-- =============================================================================
-- FIXTURE & ADVERSARIAL QA SUITE: MOCK-05
-- Subject: IT004 - Database Systems (Midterm Exam MOCK-05)
-- Domain: Quản Lý Căn Hộ Chung Cư & Hợp Đồng Thuê Nhà
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

IF OBJECT_ID('dbo.PHIEUTHU', 'U') IS NOT NULL DROP TABLE dbo.PHIEUTHU;
IF OBJECT_ID('dbo.HOPDONG', 'U') IS NOT NULL DROP TABLE dbo.HOPDONG;
IF OBJECT_ID('dbo.NHANVIEN', 'U') IS NOT NULL DROP TABLE dbo.NHANVIEN;
IF OBJECT_ID('dbo.KHACHHANG', 'U') IS NOT NULL DROP TABLE dbo.KHACHHANG;
IF OBJECT_ID('dbo.CANHO', 'U') IS NOT NULL DROP TABLE dbo.CANHO;
IF OBJECT_ID('dbo.TOANHA', 'U') IS NOT NULL DROP TABLE dbo.TOANHA;
GO

-- 2. DDL: CREATE 6 UNIFIED RELATIONS
CREATE TABLE TOANHA (
    MATN VARCHAR(10) NOT NULL,
    TENTN NVARCHAR(100) NOT NULL,
    DIACHI NVARCHAR(200) NOT NULL,
    SOTANG INT NOT NULL,
    CONSTRAINT PK_TOANHA PRIMARY KEY (MATN)
);

CREATE TABLE CANHO (
    MACH VARCHAR(10) NOT NULL,
    MATN VARCHAR(10) NOT NULL,
    SOPHONG INT NOT NULL,
    DIENTICH FLOAT NOT NULL,
    GIATHUE_CHUAN DECIMAL(18, 2) NOT NULL,
    TRANGTHAI NVARCHAR(50) NOT NULL,
    CONSTRAINT PK_CANHO PRIMARY KEY (MACH),
    CONSTRAINT FK_CANHO_TOANHA FOREIGN KEY (MATN) REFERENCES TOANHA(MATN)
);

CREATE TABLE KHACHHANG (
    MAKH VARCHAR(10) NOT NULL,
    HOTEN NVARCHAR(100) NOT NULL,
    CCCD VARCHAR(20) NOT NULL,
    SDT VARCHAR(15) NOT NULL,
    LOAIKH NVARCHAR(50) NOT NULL,
    CONSTRAINT PK_KHACHHANG PRIMARY KEY (MAKH)
);

CREATE TABLE NHANVIEN (
    MANV VARCHAR(10) NOT NULL,
    HOTEN NVARCHAR(100) NOT NULL,
    PHONGBAN NVARCHAR(50) NOT NULL,
    SDT VARCHAR(15) NOT NULL,
    CONSTRAINT PK_NHANVIEN PRIMARY KEY (MANV)
);

CREATE TABLE HOPDONG (
    MAHD VARCHAR(10) NOT NULL,
    MACH VARCHAR(10) NOT NULL,
    MAKH VARCHAR(10) NOT NULL,
    MANV VARCHAR(10) NOT NULL,
    NGAYKY DATE NOT NULL,
    NGAYBD DATE NOT NULL,
    NGAYKT DATE NOT NULL,
    GIATHUE_THUCTE DECIMAL(18, 2) NOT NULL,
    TIENCOC DECIMAL(18, 2) NOT NULL,
    CONSTRAINT PK_HOPDONG PRIMARY KEY (MAHD),
    CONSTRAINT FK_HOPDONG_CANHO FOREIGN KEY (MACH) REFERENCES CANHO(MACH),
    CONSTRAINT FK_HOPDONG_KHACHHANG FOREIGN KEY (MAKH) REFERENCES KHACHHANG(MAKH),
    CONSTRAINT FK_HOPDONG_NHANVIEN FOREIGN KEY (MANV) REFERENCES NHANVIEN(MANV)
);

CREATE TABLE PHIEUTHU (
    SOPHIEU VARCHAR(10) NOT NULL,
    MAHD VARCHAR(10) NOT NULL,
    THANG INT NOT NULL,
    NAM INT NOT NULL,
    NGAYTHU DATE NOT NULL,
    SOTIEN DECIMAL(18, 2) NOT NULL,
    CONSTRAINT PK_PHIEUTHU PRIMARY KEY (SOPHIEU),
    CONSTRAINT FK_PHIEUTHU_HOPDONG FOREIGN KEY (MAHD) REFERENCES HOPDONG(MAHD)
);
GO

-- 3. APPLY QUESTION 2.1A CHECK CONSTRAINTS
ALTER TABLE HOPDONG ADD CONSTRAINT CK_HOPDONG_TIENCOC CHECK (TIENCOC >= 0);
ALTER TABLE HOPDONG ADD CONSTRAINT CK_HOPDONG_NGAY CHECK (NGAYKT > NGAYBD);
GO

-- 4. INSERT VERIFIED FIXTURE SEED DATA
-- Tòa nhà
INSERT INTO TOANHA (MATN, TENTN, DIACHI, SOTANG) VALUES
('TN01', N'Sky Garden', N'Quận 7', 20),
('TN02', N'Sunrise City', N'Quận 7', 25),
('TN03', N'The Manor', N'Bình Thạnh', 30),
('TN04', N'Grand Riverside', N'Quận 4', 22); -- Mới xây, 0 căn hộ

-- Căn hộ
INSERT INTO CANHO (MACH, MATN, SOPHONG, DIENTICH, GIATHUE_CHUAN, TRANGTHAI) VALUES
('CH01', 'TN01', 2, 75.0, 16000000, N'Trống'), -- Sẽ được UPDATE sang Đang thuê
('CH02', 'TN01', 3, 100.0, 22000000, N'Trống'), -- Sẽ được UPDATE sang Đang thuê
('CH03', 'TN01', 1, 45.0, 10000000, N'Trống'),
('CH04', 'TN02', 2, 80.0, 18000000, N'Trống'), -- Sẽ được UPDATE sang Đang thuê
('CH05', 'TN02', 3, 110.0, 25000000, N'Trống'), -- Sẽ được UPDATE sang Đang thuê
('CH06', 'TN03', 2, 85.0, 20000000, N'Trống');  -- Sẽ được UPDATE sang Đang thuê

-- Khách hàng
INSERT INTO KHACHHANG (MAKH, HOTEN, CCCD, SDT, LOAIKH) VALUES
('KH01', N'Công ty TNHH Đầu tư Nam Long', '079011111111', '0901111111', N'Doanh nghiệp'),
('KH02', N'Tập đoàn Phát triển Vina', '079022222222', '0902222222', N'Doanh nghiệp'),
('KH03', N'Nguyễn Văn An', '079033333333', '0903333333', N'Cá nhân'),
('KH04', N'Trần Thị Bình', '079044444444', '0904444444', N'Cá nhân');

-- Nhân viên
INSERT INTO NHANVIEN (MANV, HOTEN, PHONGBAN, SDT) VALUES
('NV01', N'Lê Hoàng Mai', N'Kinh doanh', '0911223344'),
('NV02', N'Phạm Quốc Huy', N'Kinh doanh', '0911556677');

-- Hợp đồng
-- KH01 thuê CH01 (TN01, Quận 7) và CH04 (TN02, Quận 7) -> Thỏa phép chia
INSERT INTO HOPDONG (MAHD, MACH, MAKH, MANV, NGAYKY, NGAYBD, NGAYKT, GIATHUE_THUCTE, TIENCOC) VALUES
('HD01', 'CH01', 'KH01', 'NV01', '2024-01-10', '2024-01-15', '2025-01-15', 16000000, 32000000),
('HD02', 'CH04', 'KH01', 'NV01', '2024-02-01', '2024-02-05', '2025-02-05', 18000000, 36000000);

-- KH02 thuê CH02 (TN01, Quận 7) và CH05 (TN02, Quận 7) -> Thỏa phép chia
INSERT INTO HOPDONG (MAHD, MACH, MAKH, MANV, NGAYKY, NGAYBD, NGAYKT, GIATHUE_THUCTE, TIENCOC) VALUES
('HD03', 'CH02', 'KH02', 'NV02', '2024-03-01', '2024-03-10', '2025-03-10', 22000000, 44000000),
('HD04', 'CH05', 'KH02', 'NV02', '2024-04-15', '2024-04-20', '2025-04-20', 25000000, 50000000);

-- KH03 chỉ thuê CH03 (TN01) -> Thiếu TN02 -> Loại khỏi phép chia
INSERT INTO HOPDONG (MAHD, MACH, MAKH, MANV, NGAYKY, NGAYBD, NGAYKT, GIATHUE_THUCTE, TIENCOC) VALUES
('HD05', 'CH03', 'KH03', 'NV01', '2024-05-01', '2024-05-05', '2024-11-05', 10000000, 20000000); -- Hết hạn tháng 11/2024

-- KH04 thuê CH06 (TN03, Bình Thạnh) -> Không ở Quận 7 -> Loại khỏi phép chia
INSERT INTO HOPDONG (MAHD, MACH, MAKH, MANV, NGAYKY, NGAYBD, NGAYKT, GIATHUE_THUCTE, TIENCOC) VALUES
('HD06', 'CH06', 'KH04', 'NV02', '2024-06-01', '2024-06-05', '2025-06-05', 20000000, 40000000);

-- Phiếu thu tiền
INSERT INTO PHIEUTHU (SOPHIEU, MAHD, THANG, NAM, NGAYTHU, SOTIEN) VALUES
('PT01', 'HD01', 10, 2024, '2024-10-05', 16000000),
('PT02', 'HD01', 11, 2024, '2024-11-05', 16000000), -- HD01 tổng năm 2024 = 32tr
('PT03', 'HD02', 10, 2024, '2024-10-06', 18000000), -- HD02 tổng năm 2024 = 18tr
('PT04', 'HD03', 10, 2024, '2024-10-07', 22000000), -- HD03 tổng năm 2024 = 22tr
('PT05', 'HD04', 10, 2024, '2024-10-08', 25000000); -- HD04 tổng năm 2024 = 25tr
GO

-- =============================================================================
-- TEST SUITE 1: ADVERSARIAL CHECK CONSTRAINTS & NOT NULL
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY ===';
PRINT '------------------------------------------------------------';

-- Test 1A: Check TIENCOC < 0
BEGIN TRY
    INSERT INTO HOPDONG (MAHD, MACH, MAKH, MANV, NGAYKY, NGAYBD, NGAYKT, GIATHUE_THUCTE, TIENCOC)
    VALUES ('HD_ERR1', 'CH01', 'KH01', 'NV01', '2024-01-01', '2024-01-05', '2025-01-05', 15000000, -1000000);
    PRINT '  [FAIL] Test 1A: Negative TIENCOC was NOT blocked!';
    THROW 50001, 'Test 1A Failed', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_HOPDONG_TIENCOC%'
        PRINT '  [PASS] Test 1A: CK_HOPDONG_TIENCOC correctly blocked negative TIENCOC.';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1A: Unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;

-- Test 1B: Check NGAYKT <= NGAYBD
BEGIN TRY
    INSERT INTO HOPDONG (MAHD, MACH, MAKH, MANV, NGAYKY, NGAYBD, NGAYKT, GIATHUE_THUCTE, TIENCOC)
    VALUES ('HD_ERR2', 'CH01', 'KH01', 'NV01', '2024-01-01', '2024-01-10', '2024-01-05', 15000000, 30000000);
    PRINT '  [FAIL] Test 1B: NGAYKT <= NGAYBD was NOT blocked!';
    THROW 50002, 'Test 1B Failed', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_HOPDONG_NGAY%'
        PRINT '  [PASS] Test 1B: CK_HOPDONG_NGAY correctly blocked NGAYKT <= NGAYBD.';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1B: Unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;

-- Test 1C: Check NOT NULL policy (Error 515)
BEGIN TRY
    INSERT INTO HOPDONG (MAHD, MACH, MAKH, MANV, NGAYKY, NGAYBD, NGAYKT, GIATHUE_THUCTE, TIENCOC)
    VALUES ('HD_ERR3', 'CH01', 'KH01', 'NV01', '2024-01-01', '2024-01-05', '2025-01-05', 15000000, NULL);
    PRINT '  [FAIL] Test 1C: NULL TIENCOC was NOT blocked!';
    THROW 50003, 'Test 1C Failed', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] Test 1C: NOT NULL policy correctly rejected NULL TIENCOC (Error 515).';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1C: Unexpected error: ' + ERROR_MESSAGE();
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

UPDATE CH
SET CH.TRANGTHAI = N'Đang thuê'
FROM CANHO CH
INNER JOIN HOPDONG HD ON CH.MACH = HD.MACH
WHERE HD.NGAYKY >= '2024-01-01' AND HD.NGAYKY <= '2024-12-31'
  AND HD.NGAYKT >= '2024-12-31';

DECLARE @upd_cnt INT = @@ROWCOUNT;
-- HD01 (CH01), HD02 (CH04), HD03 (CH02), HD04 (CH05), HD06 (CH06) satisfy criteria (HD05 ended in Nov 2024)
IF @upd_cnt = 5
    PRINT '  [PASS] Test 2: UPDATE correctly affected 5 apartments (CH01, CH02, CH04, CH05, CH06).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 2: Expected 5 rows updated, got ' + CAST(@upd_cnt AS VARCHAR);
    THROW 50004, 'Test 2 Failed', 1;
END;

DECLARE @ch03_stat NVARCHAR(50);
SELECT @ch03_stat = TRANGTHAI FROM CANHO WHERE MACH = 'CH03';
IF @ch03_stat = N'Trống'
    PRINT '  [PASS] Test 2b: Verified CH03 remains Trong as HD05 expired before 2024-12-31.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 2b: CH03 status mismatch! Got: ' + @ch03_stat;
    THROW 50005, 'Test 2b Failed', 1;
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
FROM KHACHHANG
WHERE LOAIKH = N'Doanh nghiệp';

IF @cnt_q3 = 2 AND EXISTS (SELECT 1 FROM KHACHHANG WHERE MAKH = 'KH01')
               AND EXISTS (SELECT 1 FROM KHACHHANG WHERE MAKH = 'KH02')
    PRINT '  [PASS] Test 3: Selection returned exactly 2 corporate clients (KH01, KH02).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 3: Selection failed! Count=' + CAST(@cnt_q3 AS VARCHAR);
    THROW 50006, 'Test 3 Failed', 1;
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
FROM CANHO CH
INNER JOIN TOANHA TN ON CH.MATN = TN.MATN
WHERE TN.TENTN = N'Sky Garden'
  AND CH.GIATHUE_CHUAN >= 15000000;

IF @cnt_q4 = 2 AND EXISTS (SELECT 1 FROM CANHO WHERE MACH = 'CH01')
               AND EXISTS (SELECT 1 FROM CANHO WHERE MACH = 'CH02')
    PRINT '  [PASS] Test 4: Join returned exactly 2 apartments in Sky Garden >= 15tr (CH01, CH02).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 4: Join failed! Count=' + CAST(@cnt_q4 AS VARCHAR);
    THROW 50007, 'Test 4 Failed', 1;
END;
GO

-- =============================================================================
-- TEST SUITE 5: QUESTION 2.2C OUTER JOIN QUERY
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 5: QUESTION 2.2C OUTER JOIN QUERY ===';
PRINT '------------------------------------------------------------';

DECLARE @cnt_q5 INT, @cnt_null_mach INT;
SELECT @cnt_q5 = COUNT(*)
FROM TOANHA TN
LEFT OUTER JOIN CANHO CH ON TN.MATN = CH.MATN;

SELECT @cnt_null_mach = COUNT(*)
FROM TOANHA TN
LEFT OUTER JOIN CANHO CH ON TN.MATN = CH.MATN
WHERE CH.MACH IS NULL AND TN.MATN = 'TN04';

-- Total rows = 6 apartment rows + 1 null row for TN04 = 7 rows
IF @cnt_q5 = 7 AND @cnt_null_mach = 1
    PRINT '  [PASS] Test 5: Outer join preserved TN04 with NULL apartment info (total 7 rows).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 5: Outer join failed! Total=' + CAST(@cnt_q5 AS VARCHAR) + ', NULL MACH=' + CAST(@cnt_null_mach AS VARCHAR);
    THROW 50008, 'Test 5 Failed', 1;
END;
GO

-- =============================================================================
-- TEST SUITE 6: QUESTION 2.2D GROUPING & AGGREGATE
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE ===';
PRINT '------------------------------------------------------------';

DECLARE @thu_hd01 DECIMAL(18,2), @thu_hd02 DECIMAL(18,2);

SELECT @thu_hd01 = SUM(PT.SOTIEN)
FROM HOPDONG HD
INNER JOIN PHIEUTHU PT ON HD.MAHD = PT.MAHD
WHERE PT.NAM = 2024 AND HD.MAHD = 'HD01';

SELECT @thu_hd02 = SUM(PT.SOTIEN)
FROM HOPDONG HD
INNER JOIN PHIEUTHU PT ON HD.MAHD = PT.MAHD
WHERE PT.NAM = 2024 AND HD.MAHD = 'HD02';

-- HD01: PT01 (16tr) + PT02 (16tr) = 32tr
-- HD02: PT03 (18tr) = 18tr
IF @thu_hd01 = 32000000.00 AND @thu_hd02 = 18000000.00
    PRINT '  [PASS] Test 6: Grouping SUM verified: HD01=32,000,000; HD02=18,000,000.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 6: Grouping mismatch! HD01=' + CAST(@thu_hd01 AS VARCHAR) + ', HD02=' + CAST(@thu_hd02 AS VARCHAR);
    THROW 50009, 'Test 6 Failed', 1;
END;
GO

-- =============================================================================
-- TEST SUITE 7: QUESTION 2.2E RELATIONAL DIVISION
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION ===';
PRINT '------------------------------------------------------------';

-- Target: All buildings in Quan 7 (TN01, TN02)
-- Method 1: Double NOT EXISTS
DECLARE @div1_cnt INT;
SELECT @div1_cnt = COUNT(*)
FROM KHACHHANG KH
WHERE NOT EXISTS (
    SELECT *
    FROM TOANHA TN
    WHERE TN.DIACHI = N'Quận 7'
      AND NOT EXISTS (
          SELECT *
          FROM HOPDONG HD
          INNER JOIN CANHO CH ON HD.MACH = CH.MACH
          WHERE HD.MAKH = KH.MAKH
            AND CH.MATN = TN.MATN
      )
)
AND EXISTS (SELECT 1 FROM HOPDONG WHERE MAKH = KH.MAKH);

-- Method 2: HAVING COUNT
DECLARE @div2_cnt INT;
SELECT @div2_cnt = COUNT(*)
FROM (
    SELECT KH.MAKH
    FROM KHACHHANG KH
    INNER JOIN HOPDONG HD ON KH.MAKH = HD.MAKH
    INNER JOIN CANHO CH ON HD.MACH = CH.MACH
    INNER JOIN TOANHA TN ON CH.MATN = TN.MATN
    WHERE TN.DIACHI = N'Quận 7'
    GROUP BY KH.MAKH
    HAVING COUNT(DISTINCT TN.MATN) = (
        SELECT COUNT(*)
        FROM TOANHA
        WHERE DIACHI = N'Quận 7'
    )
) AS T;

IF @div1_cnt = 2 AND @div2_cnt = 2
   AND EXISTS (SELECT 1 FROM KHACHHANG WHERE MAKH = 'KH01')
   AND EXISTS (SELECT 1 FROM KHACHHANG WHERE MAKH = 'KH02')
    PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (KH01, KH02).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 7: Division mismatch! div1=' + CAST(@div1_cnt AS VARCHAR) + ', div2=' + CAST(@div2_cnt AS VARCHAR);
    THROW 50010, 'Test 7 Failed', 1;
END;
GO

-- =============================================================================
-- TEST SUITE 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE (S = Ø)
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE ===';
PRINT '------------------------------------------------------------';

-- Target: DIACHI = 'QuanKhongTonTai' -> S = Ø
-- Candidate universe bounded by π_MAKH(HOPDONG): exactly 4 clients have signed contracts

-- Method 1: Double NOT EXISTS bounded by candidate universe
DECLARE @empty_bounded_cnt INT;
SELECT @empty_bounded_cnt = COUNT(*)
FROM KHACHHANG KH
WHERE NOT EXISTS (
    SELECT *
    FROM TOANHA TN
    WHERE TN.DIACHI = N'QuanKhongTonTai'
      AND NOT EXISTS (
          SELECT *
          FROM HOPDONG HD
          INNER JOIN CANHO CH ON HD.MACH = CH.MACH
          WHERE HD.MAKH = KH.MAKH
            AND CH.MATN = TN.MATN
      )
)
AND EXISTS (SELECT 1 FROM HOPDONG WHERE MAKH = KH.MAKH);

-- Method 2: LEFT JOIN ... HAVING COUNT on candidate universe
DECLARE @empty_having_cnt INT;
SELECT @empty_having_cnt = COUNT(*)
FROM (
    SELECT HD.MAKH
    FROM HOPDONG HD
    INNER JOIN CANHO CH ON HD.MACH = CH.MACH
    LEFT JOIN (SELECT MATN FROM TOANHA WHERE DIACHI = N'QuanKhongTonTai') S ON CH.MATN = S.MATN
    GROUP BY HD.MAKH
    HAVING COUNT(DISTINCT S.MATN) = (SELECT COUNT(*) FROM TOANHA WHERE DIACHI = N'QuanKhongTonTai')
) AS H;

-- Set-wise comparison between Method 1 and Method 2 using EXCEPT
DECLARE @t8_diff_1_2 INT, @t8_diff_2_1 INT;
SELECT @t8_diff_1_2 = COUNT(*) FROM (
    SELECT KH.MAKH FROM KHACHHANG KH
    WHERE NOT EXISTS (
        SELECT * FROM TOANHA TN WHERE TN.DIACHI = N'QuanKhongTonTai'
        AND NOT EXISTS (
            SELECT * FROM HOPDONG HD INNER JOIN CANHO CH ON HD.MACH = CH.MACH
            WHERE HD.MAKH = KH.MAKH AND CH.MATN = TN.MATN
        )
    ) AND EXISTS (SELECT 1 FROM HOPDONG WHERE MAKH = KH.MAKH)
    EXCEPT
    SELECT HD.MAKH FROM HOPDONG HD
    INNER JOIN CANHO CH ON HD.MACH = CH.MACH
    LEFT JOIN (SELECT MATN FROM TOANHA WHERE DIACHI = N'QuanKhongTonTai') S ON CH.MATN = S.MATN
    GROUP BY HD.MAKH
    HAVING COUNT(DISTINCT S.MATN) = (SELECT COUNT(*) FROM TOANHA WHERE DIACHI = N'QuanKhongTonTai')
) AS D1;

SELECT @t8_diff_2_1 = COUNT(*) FROM (
    SELECT HD.MAKH FROM HOPDONG HD
    INNER JOIN CANHO CH ON HD.MACH = CH.MACH
    LEFT JOIN (SELECT MATN FROM TOANHA WHERE DIACHI = N'QuanKhongTonTai') S ON CH.MATN = S.MATN
    GROUP BY HD.MAKH
    HAVING COUNT(DISTINCT S.MATN) = (SELECT COUNT(*) FROM TOANHA WHERE DIACHI = N'QuanKhongTonTai')
    EXCEPT
    SELECT KH.MAKH FROM KHACHHANG KH
    WHERE NOT EXISTS (
        SELECT * FROM TOANHA TN WHERE TN.DIACHI = N'QuanKhongTonTai'
        AND NOT EXISTS (
            SELECT * FROM HOPDONG HD INNER JOIN CANHO CH ON HD.MACH = CH.MACH
            WHERE HD.MAKH = KH.MAKH AND CH.MATN = TN.MATN
        )
    ) AND EXISTS (SELECT 1 FROM HOPDONG WHERE MAKH = KH.MAKH)
) AS D2;

IF @empty_bounded_cnt = 4 AND @empty_having_cnt = 4 AND @t8_diff_1_2 = 0 AND @t8_diff_2_1 = 0
    PRINT '  [PASS] Test 8: Empty target S=Ø verified with EXCEPT set comparison: RA, NOT EXISTS and HAVING COUNT identical (4 clients).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 8: Empty target comparison failed!';
    THROW 50011, 'Test 8 Failed', 1;
END;
GO

-- =============================================================================
-- TEST SUITE 9: QUESTION 2.2F EXTREME TIE-BREAKING
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING ===';
PRINT '------------------------------------------------------------';

DECLARE @tie_cnt INT, @max_rented INT;

SELECT @tie_cnt = COUNT(*)
FROM (
    SELECT TOP 1 WITH TIES TN.MATN, TN.TENTN, TN.DIACHI, COUNT(CH.MACH) AS SO_CAN_THUE
    FROM TOANHA TN
    INNER JOIN CANHO CH ON TN.MATN = CH.MATN
    WHERE CH.TRANGTHAI = N'Đang thuê'
    GROUP BY TN.MATN, TN.TENTN, TN.DIACHI
    ORDER BY COUNT(CH.MACH) DESC
) AS T;

SELECT TOP 1 @max_rented = COUNT(CH.MACH)
FROM TOANHA TN
INNER JOIN CANHO CH ON TN.MATN = CH.MATN
WHERE CH.TRANGTHAI = N'Đang thuê'
GROUP BY TN.MATN
ORDER BY COUNT(CH.MACH) DESC;

-- TN01 (2 căn) and TN02 (2 căn) are in a 2-way tie; TN03 (1 căn) and TN04 (0 căn) are excluded
IF @tie_cnt = 2 AND @max_rented = 2
   AND EXISTS (SELECT 1 FROM TOANHA WHERE MATN = 'TN01')
   AND EXISTS (SELECT 1 FROM TOANHA WHERE MATN = 'TN02')
    PRINT '  [PASS] Test 9: Extreme tie-breaking verified: TN01 (2 units) and TN02 (2 units) preserved; TN03 (1 unit) excluded.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 9: Tie-breaking failed! tie_cnt=' + CAST(@tie_cnt AS VARCHAR) + ', max=' + CAST(@max_rented AS VARCHAR);
    THROW 50012, 'Test 9 Failed', 1;
END;
GO

PRINT '------------------------------------------------------------';
PRINT '=== ALL 9 MOCK-05 VERIFICATION SUITES PASSED WITH ASSERTIONS ===';
PRINT '------------------------------------------------------------';
GO
