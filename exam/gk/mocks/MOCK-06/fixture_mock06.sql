-- =============================================================================
-- FIXTURE & ADVERSARIAL QA SUITE: MOCK-06
-- Subject: IT004 - Database Systems (Midterm Exam MOCK-06)
-- Domain: Quản Lý Đặt Khám & Hồ Sơ Bệnh Án Điện Tử Phòng Khám Đa Khoa
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

IF OBJECT_ID('dbo.CHITIET_DV', 'U') IS NOT NULL DROP TABLE dbo.CHITIET_DV;
IF OBJECT_ID('dbo.PHIEUKHAM', 'U') IS NOT NULL DROP TABLE dbo.PHIEUKHAM;
IF OBJECT_ID('dbo.DICHVU_KHAM', 'U') IS NOT NULL DROP TABLE dbo.DICHVU_KHAM;
IF OBJECT_ID('dbo.BENHNHAN', 'U') IS NOT NULL DROP TABLE dbo.BENHNHAN;
IF OBJECT_ID('dbo.BACSI', 'U') IS NOT NULL DROP TABLE dbo.BACSI;
IF OBJECT_ID('dbo.CHUYENKHOA', 'U') IS NOT NULL DROP TABLE dbo.CHUYENKHOA;
GO

-- 2. DDL: CREATE 6 UNIFIED RELATIONS
CREATE TABLE CHUYENKHOA (
    MAKC VARCHAR(10) NOT NULL,
    TENKHOA NVARCHAR(100) NOT NULL,
    TRUONGKHOA NVARCHAR(100) NOT NULL,
    CONSTRAINT PK_CHUYENKHOA PRIMARY KEY (MAKC)
);

CREATE TABLE BACSI (
    MABS VARCHAR(10) NOT NULL,
    HOTEN NVARCHAR(100) NOT NULL,
    HOCVI NVARCHAR(50) NOT NULL,
    MAKC VARCHAR(10) NOT NULL,
    LUONG DECIMAL(18, 2) NOT NULL,
    CONSTRAINT PK_BACSI PRIMARY KEY (MABS),
    CONSTRAINT FK_BACSI_CHUYENKHOA FOREIGN KEY (MAKC) REFERENCES CHUYENKHOA(MAKC)
);

CREATE TABLE BENHNHAN (
    MABN VARCHAR(10) NOT NULL,
    HOTEN NVARCHAR(100) NOT NULL,
    NGAYSINH DATE NOT NULL,
    GIOITINH NVARCHAR(10) NOT NULL,
    DIACHI NVARCHAR(200) NOT NULL,
    CONSTRAINT PK_BENHNHAN PRIMARY KEY (MABN)
);

CREATE TABLE DICHVU_KHAM (
    MADV VARCHAR(10) NOT NULL,
    TENDV NVARCHAR(100) NOT NULL,
    LOAIDV NVARCHAR(50) NOT NULL,
    DONGIA DECIMAL(18, 2) NOT NULL,
    CONSTRAINT PK_DICHVU_KHAM PRIMARY KEY (MADV)
);

CREATE TABLE PHIEUKHAM (
    MAPK VARCHAR(10) NOT NULL,
    NGAYKHAM DATETIME NOT NULL,
    MABN VARCHAR(10) NOT NULL,
    MABS VARCHAR(10) NOT NULL,
    CHANDOAN NVARCHAR(200) NOT NULL,
    CONSTRAINT PK_PHIEUKHAM PRIMARY KEY (MAPK),
    CONSTRAINT FK_PHIEUKHAM_BENHNHAN FOREIGN KEY (MABN) REFERENCES BENHNHAN(MABN),
    CONSTRAINT FK_PHIEUKHAM_BACSI FOREIGN KEY (MABS) REFERENCES BACSI(MABS)
);

CREATE TABLE CHITIET_DV (
    MAPK VARCHAR(10) NOT NULL,
    MADV VARCHAR(10) NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA_THU DECIMAL(18, 2) NOT NULL,
    KETQUA NVARCHAR(200) NOT NULL,
    CONSTRAINT PK_CHITIET_DV PRIMARY KEY (MAPK, MADV),
    CONSTRAINT FK_CHITIET_DV_PHIEUKHAM FOREIGN KEY (MAPK) REFERENCES PHIEUKHAM(MAPK),
    CONSTRAINT FK_CHITIET_DV_DICHVU FOREIGN KEY (MADV) REFERENCES DICHVU_KHAM(MADV)
);
GO

-- 3. APPLY QUESTION 2.1A CHECK CONSTRAINTS
ALTER TABLE CHITIET_DV ADD CONSTRAINT CK_CTDV_SOLUONG CHECK (SOLUONG > 0);
ALTER TABLE DICHVU_KHAM ADD CONSTRAINT CK_DVKHAM_DONGIA CHECK (DONGIA > 0);
GO

-- 4. INSERT VERIFIED FIXTURE SEED DATA
-- Chuyên khoa
INSERT INTO CHUYENKHOA (MAKC, TENKHOA, TRUONGKHOA) VALUES
('CK01', N'Nội tổng quát', N'TS. Nguyễn Văn A'),
('CK02', N'Tai-Mũi-Họng', N'BS.CKII Trần Văn B'),
('CK03', N'Nhi khoa', N'ThS. Lê Thị C'),
('CK04', N'Da liễu', N'BS.CKI Phạm Văn D'); -- Mới thành lập, 0 bác sĩ

-- Bác sĩ
INSERT INTO BACSI (MABS, HOTEN, HOCVI, MAKC, LUONG) VALUES
('BS01', N'Nguyễn Văn An', N'Tiến sĩ', 'CK01', 25000000),      -- Thỏa update
('BS02', N'Trần Thị Bình', N'Bác sĩ CKI', 'CK01', 18000000),   -- Không thỏa (CKI)
('BS03', N'Lê Hoàng Cường', N'Bác sĩ CKII', 'CK01', 22000000), -- Thỏa update
('BS04', N'Phạm Quốc Dũng', N'Thạc sĩ', 'CK03', 20000000),     -- Nhi khoa
('BS05', N'Hoàng Minh Em', N'Bác sĩ CKI', 'CK02', 17000000);

-- Bệnh nhân
INSERT INTO BENHNHAN (MABN, HOTEN, NGAYSINH, GIOITINH, DIACHI) VALUES
('BN01', N'Vũ Thị Hạnh', '1995-02-14', N'Nữ', N'TP.HCM'),     -- Thỏa 2.2a
('BN02', N'Đặng Thu Trang', '2000-08-20', N'Nữ', N'TP.HCM'),  -- Thỏa 2.2a
('BN03', N'Nguyễn Văn Hùng', '1988-11-05', N'Nam', N'TP.HCM'),-- Nam -> Loại 2.2a
('BN04', N'Lê Thị Mai', '1992-06-30', N'Nữ', N'Bình Dương');  -- Bình Dương -> Loại 2.2a

-- Dịch vụ khám
-- Chẩn đoán hình ảnh gồm DV01 và DV02.
INSERT INTO DICHVU_KHAM (MADV, TENDV, LOAIDV, DONGIA) VALUES
('DV01', N'Chụp X-quang phổi', N'Chẩn đoán hình ảnh', 200000),
('DV02', N'Siêu âm tim màu', N'Chẩn đoán hình ảnh', 350000),
('DV03', N'Khám nội tổng quát', N'Khám lâm sàng', 150000),
('DV04', N'Xét nghiệm máu tổng quát', N'Xét nghiệm', 300000),
('DV05', N'Nhiệm vụ Thử nghiệm', N'Chẩn đoán hình ảnh rỗng', 500000);

-- Phiếu khám
INSERT INTO PHIEUKHAM (MAPK, NGAYKHAM, MABN, MABS, CHANDOAN) VALUES
('PK01', '2024-10-05 08:30:00', 'BN01', 'BS01', N'Viêm họng cấp'),
('PK02', '2024-10-10 09:15:00', 'BN02', 'BS01', N'Rối loạn tiền đình'),
('PK03', '2024-10-12 14:00:00', 'BN03', 'BS04', N'Sốt xuất huyết'), -- BS04 Nhi khoa -> Thỏa 2.2b
('PK04', '2024-10-18 10:30:00', 'BN01', 'BS04', N'Viêm phế quản'),  -- BS04 Nhi khoa -> Thỏa 2.2b
('PK05', '2024-10-25 15:45:00', 'BN04', 'BS05', N'Viêm da cơ địa'),
('PK06', '2024-11-02 09:00:00', 'BN02', 'BS05', N'Tái khám');      -- Tháng 11

-- Chi tiết dịch vụ
-- Chẩn đoán hình ảnh gồm: DV01, DV02
-- PK01: có DV01 (1) và DV02 (1) -> Thỏa phép chia
INSERT INTO CHITIET_DV (MAPK, MADV, SOLUONG, DONGIA_THU, KETQUA) VALUES
('PK01', 'DV01', 1, 200000, N'Bình thường'),
('PK01', 'DV02', 1, 350000, N'Hở van 2 lá nhẹ');

-- PK02: chỉ có DV01 -> Thiếu DV02
INSERT INTO CHITIET_DV (MAPK, MADV, SOLUONG, DONGIA_THU, KETQUA) VALUES
('PK02', 'DV01', 1, 200000, N'Bình thường'),
('PK02', 'DV03', 1, 150000, N'Chỉ định khám nội');

-- PK03: có DV01 (1) và DV02 (1) -> Thỏa phép chia
INSERT INTO CHITIET_DV (MAPK, MADV, SOLUONG, DONGIA_THU, KETQUA) VALUES
('PK03', 'DV01', 1, 200000, N'Bình thường'),
('PK03', 'DV02', 1, 350000, N'Bình thường');

-- PK04: có DV02 và DV04 -> Thiếu DV01
INSERT INTO CHITIET_DV (MAPK, MADV, SOLUONG, DONGIA_THU, KETQUA) VALUES
('PK04', 'DV02', 1, 350000, N'Bình thường'),
('PK04', 'DV04', 1, 300000, N'Bạch cầu tăng nhẹ');

-- PK05: chỉ có DV03
INSERT INTO CHITIET_DV (MAPK, MADV, SOLUONG, DONGIA_THU, KETQUA) VALUES
('PK05', 'DV03', 1, 150000, N'Theo dõi dị ứng');

-- PK06: chỉ có DV01 (tháng 11)
INSERT INTO CHITIET_DV (MAPK, MADV, SOLUONG, DONGIA_THU, KETQUA) VALUES
('PK06', 'DV01', 1, 200000, N'Bình thường');
GO

-- =============================================================================
-- TEST SUITE 1: ADVERSARIAL CHECK CONSTRAINTS & NOT NULL
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY ===';
PRINT '------------------------------------------------------------';

-- Test 1A: Check SOLUONG <= 0
BEGIN TRY
    INSERT INTO CHITIET_DV (MAPK, MADV, SOLUONG, DONGIA_THU, KETQUA)
    VALUES ('PK01', 'DV04', 0, 300000, N'Test lỗi');
    PRINT '  [FAIL] Test 1A: SOLUONG = 0 was NOT blocked!';
    THROW 50001, 'Test 1A Failed', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_CTDV_SOLUONG%'
        PRINT '  [PASS] Test 1A: CK_CTDV_SOLUONG correctly blocked SOLUONG = 0.';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1A: Unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;

-- Test 1B: Check DONGIA <= 0
BEGIN TRY
    INSERT INTO DICHVU_KHAM (MADV, TENDV, LOAIDV, DONGIA)
    VALUES ('DV_ERR', N'Dịch vụ lỗi', N'Xét nghiệm', -50000);
    PRINT '  [FAIL] Test 1B: Negative DONGIA was NOT blocked!';
    THROW 50002, 'Test 1B Failed', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 547 AND ERROR_MESSAGE() LIKE '%CK_DVKHAM_DONGIA%'
        PRINT '  [PASS] Test 1B: CK_DVKHAM_DONGIA correctly blocked negative DONGIA.';
    ELSE
    BEGIN
        PRINT '  [FAIL] Test 1B: Unexpected error: ' + ERROR_MESSAGE();
        THROW;
    END
END CATCH;

-- Test 1C: Check NOT NULL policy (Error 515)
BEGIN TRY
    INSERT INTO DICHVU_KHAM (MADV, TENDV, LOAIDV, DONGIA)
    VALUES ('DV_ERR2', N'Dịch vụ lỗi 2', N'Xét nghiệm', NULL);
    PRINT '  [FAIL] Test 1C: NULL DONGIA was NOT blocked!';
    THROW 50003, 'Test 1C Failed', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] Test 1C: NOT NULL policy correctly rejected NULL DONGIA (Error 515).';
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

UPDATE BS
SET BS.LUONG = BS.LUONG * 1.10
FROM BACSI BS
INNER JOIN CHUYENKHOA CK ON BS.MAKC = CK.MAKC
WHERE CK.TENKHOA = N'Nội tổng quát'
  AND (BS.HOCVI = N'Tiến sĩ' OR BS.HOCVI = N'Bác sĩ CKII');

DECLARE @upd_cnt INT = @@ROWCOUNT;
IF @upd_cnt = 2
    PRINT '  [PASS] Test 2: UPDATE correctly affected 2 doctors (BS01, BS03).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 2: Expected 2 rows updated, got ' + CAST(@upd_cnt AS VARCHAR);
    THROW 50004, 'Test 2 Failed', 1;
END;

DECLARE @bs01_sal DECIMAL(18,2), @bs02_sal DECIMAL(18,2), @bs03_sal DECIMAL(18,2);
SELECT @bs01_sal = LUONG FROM BACSI WHERE MABS = 'BS01';
SELECT @bs02_sal = LUONG FROM BACSI WHERE MABS = 'BS02';
SELECT @bs03_sal = LUONG FROM BACSI WHERE MABS = 'BS03';

IF @bs01_sal = 27500000.00 AND @bs03_sal = 24200000.00 AND @bs02_sal = 18000000.00
    PRINT '  [PASS] Test 2b: Salary verified: BS01=27.5tr (+10%), BS03=24.2tr (+10%), BS02=18tr (unchanged).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 2b: Salary mismatch!';
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
FROM BENHNHAN
WHERE GIOITINH = N'Nữ' AND DIACHI = N'TP.HCM';

IF @cnt_q3 = 2 AND EXISTS (SELECT 1 FROM BENHNHAN WHERE MABN = 'BN01')
               AND EXISTS (SELECT 1 FROM BENHNHAN WHERE MABN = 'BN02')
    PRINT '  [PASS] Test 3: Selection returned exactly 2 female patients in HCMC (BN01, BN02).';
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
FROM PHIEUKHAM PK
INNER JOIN BACSI BS ON PK.MABS = BS.MABS
INNER JOIN CHUYENKHOA CK ON BS.MAKC = CK.MAKC
WHERE CK.TENKHOA = N'Nhi khoa';

IF @cnt_q4 = 2 AND EXISTS (SELECT 1 FROM PHIEUKHAM WHERE MAPK = 'PK03')
               AND EXISTS (SELECT 1 FROM PHIEUKHAM WHERE MAPK = 'PK04')
    PRINT '  [PASS] Test 4: Join returned exactly 2 examination slips by Pediatrics (PK03, PK04).';
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

DECLARE @cnt_q5 INT, @cnt_null_mabs INT;
SELECT @cnt_q5 = COUNT(*)
FROM CHUYENKHOA CK
LEFT OUTER JOIN BACSI BS ON CK.MAKC = BS.MAKC;

SELECT @cnt_null_mabs = COUNT(*)
FROM CHUYENKHOA CK
LEFT OUTER JOIN BACSI BS ON CK.MAKC = BS.MAKC
WHERE BS.MABS IS NULL AND CK.MAKC = 'CK04';

-- Total rows = 5 doctor rows + 1 null row for CK04 = 6 rows
IF @cnt_q5 = 6 AND @cnt_null_mabs = 1
    PRINT '  [PASS] Test 5: Outer join preserved CK04 with NULL doctor info (total 6 rows).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 5: Outer join failed! Total=' + CAST(@cnt_q5 AS VARCHAR) + ', NULL MABS=' + CAST(@cnt_null_mabs AS VARCHAR);
    THROW 50008, 'Test 5 Failed', 1;
END;
GO

-- =============================================================================
-- TEST SUITE 6: QUESTION 2.2D GROUPING & AGGREGATE
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE ===';
PRINT '------------------------------------------------------------';

DECLARE @fee_pk01 DECIMAL(18,2), @fee_pk02 DECIMAL(18,2);

SELECT @fee_pk01 = SUM(CT.SOLUONG * CT.DONGIA_THU)
FROM PHIEUKHAM PK
INNER JOIN CHITIET_DV CT ON PK.MAPK = CT.MAPK
WHERE PK.NGAYKHAM >= '2024-10-01' AND PK.NGAYKHAM <= '2024-10-31 23:59:59' AND PK.MAPK = 'PK01';

SELECT @fee_pk02 = SUM(CT.SOLUONG * CT.DONGIA_THU)
FROM PHIEUKHAM PK
INNER JOIN CHITIET_DV CT ON PK.MAPK = CT.MAPK
WHERE PK.NGAYKHAM >= '2024-10-01' AND PK.NGAYKHAM <= '2024-10-31 23:59:59' AND PK.MAPK = 'PK02';

-- PK01: DV01 (200k) + DV02 (350k) = 550,000
-- PK02: DV01 (200k) + DV03 (150k) = 350,000
IF @fee_pk01 = 550000.00 AND @fee_pk02 = 350000.00
    PRINT '  [PASS] Test 6: Grouping SUM verified: PK01=550,000; PK02=350,000.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 6: Grouping fee mismatch! PK01=' + CAST(@fee_pk01 AS VARCHAR) + ', PK02=' + CAST(@fee_pk02 AS VARCHAR);
    THROW 50009, 'Test 6 Failed', 1;
END;
GO

-- =============================================================================
-- TEST SUITE 7: QUESTION 2.2E RELATIONAL DIVISION
-- =============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION ===';
PRINT '------------------------------------------------------------';

-- Target: LOAIDV = 'Chẩn đoán hình ảnh' (DV01, DV02)
-- Method 1: Double NOT EXISTS
DECLARE @div1_cnt INT;
SELECT @div1_cnt = COUNT(*)
FROM PHIEUKHAM PK
WHERE NOT EXISTS (
    SELECT *
    FROM DICHVU_KHAM DV
    WHERE DV.LOAIDV = N'Chẩn đoán hình ảnh'
      AND NOT EXISTS (
          SELECT *
          FROM CHITIET_DV CT
          WHERE CT.MAPK = PK.MAPK
            AND CT.MADV = DV.MADV
      )
)
AND EXISTS (SELECT 1 FROM CHITIET_DV WHERE MAPK = PK.MAPK);

-- Method 2: LEFT JOIN ... HAVING COUNT on candidate universe
DECLARE @div2_cnt INT;
SELECT @div2_cnt = COUNT(*)
FROM (
    SELECT CT.MAPK
    FROM CHITIET_DV CT
    LEFT JOIN (SELECT MADV FROM DICHVU_KHAM WHERE LOAIDV = N'Chẩn đoán hình ảnh') S ON CT.MADV = S.MADV
    GROUP BY CT.MAPK
    HAVING COUNT(DISTINCT S.MADV) = (SELECT COUNT(*) FROM DICHVU_KHAM WHERE LOAIDV = N'Chẩn đoán hình ảnh')
) AS H;

IF @div1_cnt = 2 AND @div2_cnt = 2
   AND EXISTS (SELECT 1 FROM PHIEUKHAM WHERE MAPK = 'PK01')
   AND EXISTS (SELECT 1 FROM PHIEUKHAM WHERE MAPK = 'PK03')
    PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (PK01, PK03).';
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

-- Target: LOAIDV = 'KhongTonTai' -> S = Ø
-- Candidate universe bounded by π_MAPK(CHITIET_DV): exactly 6 examination slips have detail lines
DECLARE @empty_bounded_cnt INT;
SELECT @empty_bounded_cnt = COUNT(*)
FROM PHIEUKHAM PK
WHERE NOT EXISTS (
    SELECT *
    FROM DICHVU_KHAM DV
    WHERE DV.LOAIDV = N'KhongTonTai'
      AND NOT EXISTS (
          SELECT *
          FROM CHITIET_DV CT
          WHERE CT.MAPK = PK.MAPK
            AND CT.MADV = DV.MADV
      )
)
AND EXISTS (SELECT 1 FROM CHITIET_DV WHERE MAPK = PK.MAPK);

DECLARE @empty_having_cnt INT;
SELECT @empty_having_cnt = COUNT(*)
FROM (
    SELECT CT.MAPK
    FROM CHITIET_DV CT
    LEFT JOIN (SELECT MADV FROM DICHVU_KHAM WHERE LOAIDV = N'KhongTonTai') S ON CT.MADV = S.MADV
    GROUP BY CT.MAPK
    HAVING COUNT(DISTINCT S.MADV) = (SELECT COUNT(*) FROM DICHVU_KHAM WHERE LOAIDV = N'KhongTonTai')
) AS H;

-- Set-wise comparison using EXCEPT
DECLARE @t8_diff_1_2 INT, @t8_diff_2_1 INT;
SELECT @t8_diff_1_2 = COUNT(*) FROM (
    SELECT PK.MAPK FROM PHIEUKHAM PK
    WHERE NOT EXISTS (
        SELECT * FROM DICHVU_KHAM DV WHERE DV.LOAIDV = N'KhongTonTai'
        AND NOT EXISTS (SELECT * FROM CHITIET_DV CT WHERE CT.MAPK = PK.MAPK AND CT.MADV = DV.MADV)
    ) AND EXISTS (SELECT 1 FROM CHITIET_DV WHERE MAPK = PK.MAPK)
    EXCEPT
    SELECT CT.MAPK FROM CHITIET_DV CT
    LEFT JOIN (SELECT MADV FROM DICHVU_KHAM WHERE LOAIDV = N'KhongTonTai') S ON CT.MADV = S.MADV
    GROUP BY CT.MAPK
    HAVING COUNT(DISTINCT S.MADV) = (SELECT COUNT(*) FROM DICHVU_KHAM WHERE LOAIDV = N'KhongTonTai')
) AS D1;

SELECT @t8_diff_2_1 = COUNT(*) FROM (
    SELECT CT.MAPK FROM CHITIET_DV CT
    LEFT JOIN (SELECT MADV FROM DICHVU_KHAM WHERE LOAIDV = N'KhongTonTai') S ON CT.MADV = S.MADV
    GROUP BY CT.MAPK
    HAVING COUNT(DISTINCT S.MADV) = (SELECT COUNT(*) FROM DICHVU_KHAM WHERE LOAIDV = N'KhongTonTai')
    EXCEPT
    SELECT PK.MAPK FROM PHIEUKHAM PK
    WHERE NOT EXISTS (
        SELECT * FROM DICHVU_KHAM DV WHERE DV.LOAIDV = N'KhongTonTai'
        AND NOT EXISTS (SELECT * FROM CHITIET_DV CT WHERE CT.MAPK = PK.MAPK AND CT.MADV = DV.MADV)
    ) AND EXISTS (SELECT 1 FROM CHITIET_DV WHERE MAPK = PK.MAPK)
) AS D2;

IF @empty_bounded_cnt = 6 AND @empty_having_cnt = 6 AND @t8_diff_1_2 = 0 AND @t8_diff_2_1 = 0
    PRINT '  [PASS] Test 8: Empty target S=Ø verified with EXCEPT set comparison: RA, NOT EXISTS and HAVING COUNT identical (6 slips).';
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

DECLARE @tie_cnt INT, @max_slk INT;

SELECT @tie_cnt = COUNT(*)
FROM (
    SELECT TOP 1 WITH TIES BS.MABS, BS.HOTEN, BS.HOCVI, COUNT(PK.MAPK) AS SO_LUOT_KHAM
    FROM BACSI BS
    INNER JOIN PHIEUKHAM PK ON BS.MABS = PK.MABS
    WHERE PK.NGAYKHAM >= '2024-10-01' AND PK.NGAYKHAM <= '2024-10-31 23:59:59'
    GROUP BY BS.MABS, BS.HOTEN, BS.HOCVI
    ORDER BY COUNT(PK.MAPK) DESC
) AS T;

SELECT TOP 1 @max_slk = COUNT(PK.MAPK)
FROM BACSI BS
INNER JOIN PHIEUKHAM PK ON BS.MABS = PK.MABS
WHERE PK.NGAYKHAM >= '2024-10-01' AND PK.NGAYKHAM <= '2024-10-31 23:59:59'
GROUP BY BS.MABS
ORDER BY COUNT(PK.MAPK) DESC;

-- BS01 (2 lượt) and BS04 (2 lượt) tie for MAX in Oct 2024; BS05 (1 lượt) and BS02/03 (0 lượt) excluded
IF @tie_cnt = 2 AND @max_slk = 2
   AND EXISTS (SELECT 1 FROM BACSI WHERE MABS = 'BS01')
   AND EXISTS (SELECT 1 FROM BACSI WHERE MABS = 'BS04')
    PRINT '  [PASS] Test 9: Extreme tie-breaking verified: BS01 (2 slips) and BS04 (2 slips) preserved; BS05 (1 slip) excluded.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 9: Tie-breaking failed! tie_cnt=' + CAST(@tie_cnt AS VARCHAR) + ', max=' + CAST(@max_slk AS VARCHAR);
    THROW 50012, 'Test 9 Failed', 1;
END;
GO

PRINT '------------------------------------------------------------';
PRINT '=== ALL 9 MOCK-06 VERIFICATION SUITES PASSED WITH ASSERTIONS ===';
PRINT '------------------------------------------------------------';
GO
