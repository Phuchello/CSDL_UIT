-- =============================================================================
-- FIXTURE & ADVERSARIAL VERIFICATION SCRIPT: MOCK-14
-- Domain: Quản Lý Đề Tài Nghiên Cứu Khoa Học Trọng Điểm
-- Profile: RECENT_VERIFIED (10.0 pts, 75 mins)
-- Engine: Microsoft SQL Server 2025 / Azure SQL
-- Author: VÕ TRỌNG PHÚC — CSDL_UIT Master Series
-- =============================================================================

SET NOCOUNT ON;
USE master;
GO

IF DB_ID('Mock14_Research_DB') IS NOT NULL
BEGIN
    ALTER DATABASE Mock14_Research_DB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE Mock14_Research_DB;
END
GO

CREATE DATABASE Mock14_Research_DB COLLATE Vietnamese_CI_AS;
GO

USE Mock14_Research_DB;
GO

PRINT '============================================================';
PRINT '=== MOCK-14: CREATING TABLES WITH INTEGRITY CONSTRAINTS   ===';
PRINT '============================================================';

-- 1. KHOA_VIEN
CREATE TABLE KHOA_VIEN (
    MAKV VARCHAR(10) NOT NULL PRIMARY KEY,
    TENKV NVARCHAR(100) NOT NULL,
    DIENTHOAI VARCHAR(15) NOT NULL,
    TRUONGKHOA NVARCHAR(50) NOT NULL
);

-- 2. GIANGVIEN
CREATE TABLE GIANGVIEN (
    MAGV VARCHAR(10) NOT NULL PRIMARY KEY,
    HOTEN NVARCHAR(50) NOT NULL,
    HOCHAM NVARCHAR(20) NOT NULL,
    HOCVI NVARCHAR(20) NOT NULL,
    LUONG DECIMAL(18, 2) NOT NULL CHECK (LUONG > 0),
    MAKV VARCHAR(10) NOT NULL REFERENCES KHOA_VIEN(MAKV)
);

-- 3. DETAI
CREATE TABLE DETAI (
    MADT VARCHAR(10) NOT NULL PRIMARY KEY,
    TENDT NVARCHAR(200) NOT NULL,
    CAP_QUANLY NVARCHAR(50) NOT NULL,
    KINHPHI DECIMAL(18, 2) NOT NULL CHECK (KINHPHI > 0),
    NGAYBD DATE NOT NULL,
    NGAYKT DATE NOT NULL,
    CHUNHIEM_DT VARCHAR(10) NOT NULL REFERENCES GIANGVIEN(MAGV)
);

-- 4. THAMGIA_DT
CREATE TABLE THAMGIA_DT (
    MADT VARCHAR(10) NOT NULL REFERENCES DETAI(MADT),
    MAGV VARCHAR(10) NOT NULL REFERENCES GIANGVIEN(MAGV),
    VAITRO NVARCHAR(50) NOT NULL,
    SOGIO_TG INT NOT NULL CHECK (SOGIO_TG > 0),
    PRIMARY KEY (MADT, MAGV)
);

-- 5. SANPHAM_KH
CREATE TABLE SANPHAM_KH (
    MASP VARCHAR(10) NOT NULL PRIMARY KEY,
    TENSP NVARCHAR(200) NOT NULL,
    LOAISP NVARCHAR(50) NOT NULL,
    XEP_HANG VARCHAR(20) NOT NULL,
    MADT VARCHAR(10) NOT NULL REFERENCES DETAI(MADT)
);

-- 6. GIAINGAN
CREATE TABLE GIAINGAN (
    MAGN VARCHAR(10) NOT NULL PRIMARY KEY,
    MADT VARCHAR(10) NOT NULL REFERENCES DETAI(MADT),
    NGAYGN DATE NOT NULL,
    SOTIEN_GN DECIMAL(18, 2) NOT NULL,
    NOIDUNG NVARCHAR(200) NOT NULL
);
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: QUESTION 2.1A CHECK & NOT NULL INTEGRITY     ===';
PRINT '------------------------------------------------------------';

-- Add Question 2.1a constraints
ALTER TABLE GIAINGAN
ADD CONSTRAINT CK_GIAINGAN_SOTIEN CHECK (SOTIEN_GN > 0);

ALTER TABLE DETAI
ADD CONSTRAINT CK_DETAI_NGAY CHECK (NGAYKT > NGAYBD);
GO

-- Seed minimal parent data for constraint adversarial tests
INSERT INTO KHOA_VIEN (MAKV, TENKV, DIENTHOAI, TRUONGKHOA) VALUES
('KV01', N'Viện Công Nghệ Thông Tin', '02837252001', N'GS.TS. Trần Đình An');

INSERT INTO GIANGVIEN (MAGV, HOTEN, HOCHAM, HOCVI, LUONG, MAKV) VALUES
('GV01', N'Trần Đình An', N'Giáo sư', N'Tiến sĩ', 25000000, 'KV01');

INSERT INTO DETAI (MADT, TENDT, CAP_QUANLY, KINHPHI, NGAYBD, NGAYKT, CHUNHIEM_DT) VALUES
('DT01', N'Mô hình LLM tiếng Việt', N'Cấp Nhà nước', 2500000000, '2024-01-01', '2025-12-31', 'GV01');
GO

-- Adversarial Test 1A: Non-positive disbursement amount
BEGIN TRY
    INSERT INTO GIAINGAN (MAGN, MADT, NGAYGN, SOTIEN_GN, NOIDUNG)
    VALUES ('GN_TEST1', 'DT01', '2024-06-01', 0, N'Tạm ứng');
    THROW 50001, 'Test 1A FAILED: Zero disbursement amount was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_GIAINGAN_SOTIEN%'
        PRINT '  [PASS] Test 1A: CK_GIAINGAN_SOTIEN correctly blocked zero SOTIEN_GN.';
    ELSE
    BEGIN
        DECLARE @err1 NVARCHAR(400) = ERROR_MESSAGE();
        PRINT '  [FAIL] Test 1A unexpected error: ' + @err1;
        THROW 50002, @err1, 1;
    END
END CATCH;

-- Adversarial Test 1B: Invalid date range (NGAYKT <= NGAYBD)
BEGIN TRY
    INSERT INTO DETAI (MADT, TENDT, CAP_QUANLY, KINHPHI, NGAYBD, NGAYKT, CHUNHIEM_DT)
    VALUES ('DT_TEST2', N'Đề tài sai ngày', N'Cấp Bộ', 500000000, '2024-12-01', '2024-05-01', 'GV01');
    THROW 50003, 'Test 1B FAILED: Invalid date range was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_DETAI_NGAY%'
        PRINT '  [PASS] Test 1B: CK_DETAI_NGAY correctly blocked NGAYKT <= NGAYBD.';
    ELSE
    BEGIN
        DECLARE @err2 NVARCHAR(400) = ERROR_MESSAGE();
        PRINT '  [FAIL] Test 1B unexpected error: ' + @err2;
        THROW 50004, @err2, 1;
    END
END CATCH;

-- Adversarial Test 1C: NULL policy
BEGIN TRY
    INSERT INTO GIAINGAN (MAGN, MADT, NGAYGN, SOTIEN_GN, NOIDUNG)
    VALUES ('GN_TEST3', 'DT01', '2024-06-01', NULL, N'Tạm ứng');
    THROW 50005, 'Test 1C FAILED: NULL SOTIEN_GN was accepted!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] Test 1C: NOT NULL policy correctly rejected NULL SOTIEN_GN (Error 515).';
    ELSE
    BEGIN
        DECLARE @err3 NVARCHAR(400) = ERROR_MESSAGE();
        PRINT '  [FAIL] Test 1C unexpected error: ' + @err3;
        THROW 50006, @err3, 1;
    END
END CATCH;
GO

PRINT '------------------------------------------------------------';
PRINT '=== SEEDING COMPREHENSIVE BENCHMARK DATASET               ===';
PRINT '------------------------------------------------------------';

DELETE FROM GIAINGAN;
DELETE FROM SANPHAM_KH;
DELETE FROM THAMGIA_DT;
DELETE FROM DETAI;
DELETE FROM GIANGVIEN;
DELETE FROM KHOA_VIEN;

-- 1. KHOA_VIEN (4 đơn vị: KV01, KV02, KV03 có GV/đề tài; KV04 mới mở chưa có đề tài)
INSERT INTO KHOA_VIEN (MAKV, TENKV, DIENTHOAI, TRUONGKHOA) VALUES
('KV01', N'Viện Công Nghệ Thông Tin', '02837252001', N'GS.TS. Trần Đình An'),
('KV02', N'Khoa Khoa Học Máy Tính', '02837252002', N'PGS.TS. Lê Hoàng Mai'),
('KV03', N'Khoa Mạng Máy Tính & Truyền Thông', '02837252003', N'TS. Vũ Minh Trí'),
('KV04', N'Viện Nghiên Cứu Nano & Năng Lượng Mới', '02837252004', N'TS. Đặng Thanh Phong');

-- 2. GIANGVIEN (5 giảng viên)
-- GV01, GV02: Viện CNTT Tiến sĩ -> Test 2 UPDATE target
-- GV03: Viện CNTT Thạc sĩ -> Không đổi
-- GV04: Khoa KHMT Tiến sĩ -> Không đổi
-- GV05: Khoa MMT Tiến sĩ -> Không đổi
INSERT INTO GIANGVIEN (MAGV, HOTEN, HOCHAM, HOCVI, LUONG, MAKV) VALUES
('GV01', N'Trần Đình An', N'Giáo sư', N'Tiến sĩ', 25000000, 'KV01'),
('GV02', N'Lê Hoàng Mai', N'Phó Giáo sư', N'Tiến sĩ', 22000000, 'KV01'),
('GV03', N'Nguyễn Văn Bình', N'Không', N'Thạc sĩ', 15000000, 'KV01'),
('GV04', N'Vũ Minh Trí', N'Không', N'Tiến sĩ', 20000000, 'KV02'),
('GV05', N'Phạm Ngọc Lan', N'Không', N'Tiến sĩ', 18000000, 'KV03');

-- 3. DETAI (5 đề tài)
-- Đề tài Cấp Nhà nước: DT01 (2.5 tỷ, >= 1 tỷ), DT02 (1.2 tỷ, >= 1 tỷ), DT05 (900tr, < 1 tỷ)
-- DT03: Cấp Bộ (800tr)
-- DT04: Cấp ĐHQG (300tr)
-- Chủ nhiệm GV01: DT01, DT02
-- Chủ nhiệm GV04: DT03, DT05
-- Chủ nhiệm GV05: DT04
INSERT INTO DETAI (MADT, TENDT, CAP_QUANLY, KINHPHI, NGAYBD, NGAYKT, CHUNHIEM_DT) VALUES
('DT01', N'Nghiên Cứu Mô Hình LLM Đa Ngữ Tiếng Việt', N'Cấp Nhà nước', 2500000000, '2023-01-01', '2025-12-31', 'GV01'),
('DT02', N'Nền Tảng AI Tự Động Hóa Chẩn Đoán Y Tế', N'Cấp Nhà nước', 1200000000, '2024-01-01', '2026-06-30', 'GV01'),
('DT03', N'Hệ Thống IoT Giám Sát Cảnh Báo Ngập', N'Cấp Bộ', 800000000, '2023-06-01', '2024-12-31', 'GV04'),
('DT04', N'Xử Lý Ảnh Y Khoa Phổi Với Deep Learning', N'Cấp ĐHQG', 300000000, '2024-03-01', '2025-03-01', 'GV05'),
('DT05', N'Robot Phục Hồi Chức Năng Bệnh Nhân Đột Quỵ', N'Cấp Nhà nước', 900000000, '2024-05-01', '2026-05-01', 'GV04');

-- 4. THAMGIA_DT
-- Đề tài Cấp Nhà nước gồm: DT01, DT02, DT05 (3 đề tài).
-- GV01: tham gia DT01, DT02, DT05 -> Đạt phép chia!
-- GV02: tham gia DT01, DT02, DT05 -> Đạt phép chia!
-- GV04: tham gia DT01, DT05 (thiếu DT02) -> Loại
-- GV03: tham gia DT03 -> Loại
-- GV05: tham gia DT04 -> Loại
INSERT INTO THAMGIA_DT (MADT, MAGV, VAITRO, SOGIO_TG) VALUES
('DT01', 'GV01', N'Chủ nhiệm đề tài', 500),
('DT01', 'GV02', N'Nghiên cứu viên chính', 400),
('DT01', 'GV04', N'Cộng tác viên', 150),
('DT02', 'GV01', N'Chủ nhiệm đề tài', 450),
('DT02', 'GV02', N'Nghiên cứu viên chính', 350),
('DT05', 'GV01', N'Cộng tác viên', 120),
('DT05', 'GV02', N'Nghiên cứu viên chính', 300),
('DT05', 'GV04', N'Chủ nhiệm đề tài', 400),
('DT03', 'GV03', N'Thư ký khoa học', 200),
('DT04', 'GV05', N'Chủ nhiệm đề tài', 250);

-- 5. SANPHAM_KH (Sản phẩm công bố)
-- DT01 (do GV01 CN): SP01 (Q1), SP02 (Q1), SP03 (Q1) -> 3 bài Q1
-- DT02 (do GV01 CN): SP04 (Q1), SP05 (Q1), SP06 (Q1) -> 3 bài Q1 -> Tied at 3 Q1 papers!
-- DT03: SP07 (Q1), SP08 (Q2) -> 1 bài Q1
-- DT04: SP09 (Scopus)
-- DT05: SP10 (Q2)
-- Sản phẩm của GV01 làm chủ nhiệm: SP01..SP06 (6 sản phẩm)
INSERT INTO SANPHAM_KH (MASP, TENSP, LOAISP, XEP_HANG, MADT) VALUES
('SP01', N'Vietnamese LLM Architecture (IEEE TPAMI)', N'Bài báo quốc tế', 'Q1', 'DT01'),
('SP02', N'Instruction Fine-tuning (NeurIPS)', N'Bài báo quốc tế', 'Q1', 'DT01'),
('SP03', N'Low-resource NLP Toolkit (ACL)', N'Bài báo quốc tế', 'Q1', 'DT01'),
('SP04', N'Medical AI Vision Foundation (Nature Medicine)', N'Bài báo quốc tế', 'Q1', 'DT02'),
('SP05', N'Automated Clinical NLP (Lancet Digital)', N'Bài báo quốc tế', 'Q1', 'DT02'),
('SP06', N'Federated Healthcare System (IEEE JBHI)', N'Bài báo quốc tế', 'Q1', 'DT02'),
('SP07', N'IoT Flood Sensor Network (IEEE Sensors)', N'Bài báo quốc tế', 'Q1', 'DT03'),
('SP08', N'Edge Computing for Urban Drainage', N'Bài báo quốc tế', 'Q2', 'DT03'),
('SP09', N'Pneumonia CT Screening (Springer)', N'Bài báo quốc tế', 'Scopus', 'DT04'),
('SP10', N'Rehabilitation Exoskeleton Control', N'Bài báo quốc tế', 'Q2', 'DT05');

-- 6. GIAINGAN (Giải ngân 2024)
-- DT01: GN01 (500tr) + GN02 (400tr) = 900 triệu
-- DT02: GN03 (600tr) = 600 triệu
-- DT03: GN04 (300tr) = 300 triệu
-- DT05: GN06 (200tr) = 200 triệu
-- GN05: Năm 2023 của DT01 (200tr) -> không tính vào năm 2024
INSERT INTO GIAINGAN (MAGN, MADT, NGAYGN, SOTIEN_GN, NOIDUNG) VALUES
('GN01', 'DT01', '2024-03-15', 500000000, N'Tạm ứng đợt 1 năm 2024'),
('GN02', 'DT01', '2024-09-20', 400000000, N'Giải ngân đợt 2 mua server AI'),
('GN03', 'DT02', '2024-05-10', 600000000, N'Kinh phí thu thập dữ liệu y tế'),
('GN04', 'DT03', '2024-06-15', 300000000, N'Thi công trạm cảm biến'),
('GN05', 'DT01', '2023-11-20', 200000000, N'Kinh phí khởi động năm 2023'),
('GN06', 'DT05', '2024-08-01', 200000000, N'Vật tư cơ khí chế tạo robot');
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 2: QUESTION 2.1B UPDATE QUERY                   ===';
PRINT '------------------------------------------------------------';

-- Update 15% salary for PhD lecturers at Viện CNTT
UPDATE GIANGVIEN
SET LUONG = LUONG * 1.15
FROM GIANGVIEN gv
JOIN KHOA_VIEN kv ON gv.MAKV = kv.MAKV
WHERE kv.TENKV = N'Viện Công Nghệ Thông Tin'
  AND gv.HOCVI = N'Tiến sĩ';

-- Assertions: GV01 (25m -> 28.75m), GV02 (22m -> 25.3m), GV03 (15m unchanged), GV04 (20m unchanged)
DECLARE @gv01_sal DECIMAL(18,2), @gv02_sal DECIMAL(18,2), @gv03_sal DECIMAL(18,2), @gv04_sal DECIMAL(18,2);
SELECT @gv01_sal = LUONG FROM GIANGVIEN WHERE MAGV = 'GV01';
SELECT @gv02_sal = LUONG FROM GIANGVIEN WHERE MAGV = 'GV02';
SELECT @gv03_sal = LUONG FROM GIANGVIEN WHERE MAGV = 'GV03';
SELECT @gv04_sal = LUONG FROM GIANGVIEN WHERE MAGV = 'GV04';

IF @gv01_sal = 28750000 AND @gv02_sal = 25300000 AND @gv03_sal = 15000000 AND @gv04_sal = 20000000
    PRINT '  [PASS] Test 2: Salaries verified: GV01=28.75m (+15%), GV02=25.3m (+15%), others unchanged.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 2 mismatch: GV01=' + CAST(@gv01_sal AS VARCHAR) + ', GV02=' + CAST(@gv02_sal AS VARCHAR);
    THROW 50010, 'Test 2 FAILED', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 3: QUESTION 2.2A SELECTION QUERY                ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2a: State-level projects >= 1 billion VND
DECLARE @cnt3 INT;
SELECT @cnt3 = COUNT(*)
FROM DETAI
WHERE CAP_QUANLY = N'Cấp Nhà nước'
  AND KINHPHI >= 1000000000;

IF @cnt3 = 2
    PRINT '  [PASS] Test 3: Selection returned exactly 2 State-level projects >= 1 billion (DT01, DT02).';
ELSE
    THROW 50020, 'Test 3 FAILED: Incorrect count for state-level project selection', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 4: QUESTION 2.2B JOIN QUERY                     ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2b: Products published from projects where GV01 is project lead
DECLARE @cnt4 INT;
SELECT @cnt4 = COUNT(*)
FROM SANPHAM_KH sp
JOIN DETAI dt ON sp.MADT = dt.MADT
WHERE dt.CHUNHIEM_DT = 'GV01';

IF @cnt4 = 6
    PRINT '  [PASS] Test 4: Join returned exactly 6 publications from GV01 projects (SP01..SP06).';
ELSE
    THROW 50030, 'Test 4 FAILED: Incorrect join publication count', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 5: QUESTION 2.2C OUTER JOIN QUERY               ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2c: Left Outer Join KHOA_VIEN with GIANGVIEN and DETAI
DECLARE @cnt5_total INT, @cnt5_null INT;
SELECT @cnt5_total = COUNT(*), @cnt5_null = SUM(CASE WHEN dt.MADT IS NULL THEN 1 ELSE 0 END)
FROM KHOA_VIEN kv
LEFT JOIN GIANGVIEN gv ON kv.MAKV = gv.MAKV
LEFT JOIN DETAI dt ON gv.MAGV = dt.CHUNHIEM_DT;

IF @cnt5_total = 8 AND @cnt5_null = 3
    PRINT '  [PASS] Test 5: Outer join preserved KV04 and GV02/GV03 with NULL project info (total 8 rows, 3 NULLs).';
ELSE
BEGIN
    PRINT '  [FAIL] Test 5 count: Total=' + CAST(@cnt5_total AS VARCHAR) + ', Null=' + CAST(@cnt5_null AS VARCHAR);
    THROW 50040, 'Test 5 FAILED: Outer join did not preserve empty institute properly', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE           ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2d: Total disbursements in 2024 by project
-- DT01: 500m + 400m = 900m
-- DT02: 600m
-- DT03: 300m
-- DT05: 200m
DECLARE @disb_dt01 DECIMAL(18,2), @disb_dt02 DECIMAL(18,2);
SELECT @disb_dt01 = SUM(gn.SOTIEN_GN) FROM DETAI dt JOIN GIAINGAN gn ON dt.MADT = gn.MADT WHERE dt.MADT = 'DT01' AND gn.NGAYGN >= '2024-01-01' AND gn.NGAYGN <= '2024-12-31';
SELECT @disb_dt02 = SUM(gn.SOTIEN_GN) FROM DETAI dt JOIN GIAINGAN gn ON dt.MADT = gn.MADT WHERE dt.MADT = 'DT02' AND gn.NGAYGN >= '2024-01-01' AND gn.NGAYGN <= '2024-12-31';

IF @disb_dt01 = 900000000 AND @disb_dt02 = 600000000
    PRINT '  [PASS] Test 6: Grouping SUM verified: DT01=900m, DT02=600m disbursed in 2024.';
ELSE
    THROW 50050, 'Test 6 FAILED: Grouping disbursement calculation mismatch', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION            ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2e: Researchers participating in ALL State-level projects (DT01, DT02, DT05)
DECLARE @div_not_exists TABLE (MAGV VARCHAR(10), HOTEN NVARCHAR(50), HOCVI NVARCHAR(20));
INSERT INTO @div_not_exists
SELECT gv.MAGV, gv.HOTEN, gv.HOCVI
FROM GIANGVIEN gv
WHERE EXISTS (
    SELECT 1 FROM THAMGIA_DT tg
    WHERE tg.MAGV = gv.MAGV
)
AND NOT EXISTS (
    SELECT 1 FROM DETAI dt
    WHERE dt.CAP_QUANLY = N'Cấp Nhà nước'
      AND NOT EXISTS (
          SELECT 1 FROM THAMGIA_DT tg2
          WHERE tg2.MAGV = gv.MAGV
            AND tg2.MADT = dt.MADT
      )
);

DECLARE @div_having TABLE (MAGV VARCHAR(10), HOTEN NVARCHAR(50), HOCVI NVARCHAR(20));
WITH R AS (
    SELECT DISTINCT MAGV, MADT FROM THAMGIA_DT
),
S AS (
    SELECT MADT FROM DETAI WHERE CAP_QUANLY = N'Cấp Nhà nước'
)
INSERT INTO @div_having
SELECT gv.MAGV, gv.HOTEN, gv.HOCVI
FROM GIANGVIEN gv
JOIN (
    SELECT R.MAGV
    FROM R
    LEFT JOIN S ON R.MADT = S.MADT
    GROUP BY R.MAGV
    HAVING COUNT(DISTINCT S.MADT) = (SELECT COUNT(*) FROM S)
) div ON gv.MAGV = div.MAGV;

-- Verify identical results: GV01 and GV02
DECLARE @diff1 INT, @diff2 INT;
SELECT @diff1 = COUNT(*) FROM (SELECT MAGV FROM @div_not_exists EXCEPT SELECT MAGV FROM @div_having) t;
SELECT @diff2 = COUNT(*) FROM (SELECT MAGV FROM @div_having EXCEPT SELECT MAGV FROM @div_not_exists) t;

IF @diff1 = 0 AND @diff2 = 0 AND (SELECT COUNT(*) FROM @div_not_exists) = 2
    PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (GV01, GV02).';
ELSE
    THROW 50060, 'Test 7 FAILED: Relational division discrepancy between formulations', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE ===';
PRINT '------------------------------------------------------------';

-- Adversarial Test 8: Empty target S = Ø (No project with CAP_QUANLY = 'Cấp Quốc Tế')
DECLARE @empty_not_exists TABLE (MAGV VARCHAR(10));
INSERT INTO @empty_not_exists
SELECT gv.MAGV
FROM GIANGVIEN gv
WHERE EXISTS (
    SELECT 1 FROM THAMGIA_DT tg
    WHERE tg.MAGV = gv.MAGV
)
AND NOT EXISTS (
    SELECT 1 FROM DETAI dt
    WHERE dt.CAP_QUANLY = N'Cấp Quốc Tế'
      AND NOT EXISTS (
          SELECT 1 FROM THAMGIA_DT tg2
          WHERE tg2.MAGV = gv.MAGV
            AND tg2.MADT = dt.MADT
      )
);

DECLARE @empty_having TABLE (MAGV VARCHAR(10));
WITH R AS (
    SELECT DISTINCT MAGV, MADT FROM THAMGIA_DT
),
S AS (
    SELECT MADT FROM DETAI WHERE CAP_QUANLY = N'Cấp Quốc Tế'
)
INSERT INTO @empty_having
SELECT gv.MAGV
FROM GIANGVIEN gv
JOIN (
    SELECT R.MAGV
    FROM R
    LEFT JOIN S ON R.MADT = S.MADT
    GROUP BY R.MAGV
    HAVING COUNT(DISTINCT S.MADT) = (SELECT COUNT(*) FROM S)
) div ON gv.MAGV = div.MAGV;

-- All researchers participating in at least 1 project (GV01, GV02, GV03, GV04, GV05 = 5 researchers)
DECLARE @ediff1 INT, @ediff2 INT;
SELECT @ediff1 = COUNT(*) FROM (SELECT MAGV FROM @empty_not_exists EXCEPT SELECT MAGV FROM @empty_having) t;
SELECT @ediff2 = COUNT(*) FROM (SELECT MAGV FROM @empty_having EXCEPT SELECT MAGV FROM @empty_not_exists) t;

IF @ediff1 = 0 AND @ediff2 = 0 AND (SELECT COUNT(*) FROM @empty_not_exists) = 5
    PRINT '  [PASS] Test 8: Empty target S=Ø verified with EXCEPT set comparison: RA, NOT EXISTS and HAVING COUNT identical (5 researchers).';
ELSE
    THROW 50070, 'Test 8 FAILED: Empty target division discrepancy', 1;
GO

PRINT '------------------------------------------------------------';
PRINT '=== TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING           ===';
PRINT '------------------------------------------------------------';

-- RA Question 2.2f: Projects tied with MAX Q1 publications
-- Both DT01 and DT02 have exactly 3 Q1 publications
DECLARE @max_projects TABLE (MADT VARCHAR(10), TENDT NVARCHAR(200), CAP_QUANLY NVARCHAR(50), TONG_SP INT);
WITH ThongKe AS (
    SELECT sp.MADT, COUNT(sp.MASP) AS TONG_SP
    FROM SANPHAM_KH sp
    WHERE sp.XEP_HANG = 'Q1'
    GROUP BY sp.MADT
)
INSERT INTO @max_projects
SELECT dt.MADT, dt.TENDT, dt.CAP_QUANLY, tk.TONG_SP
FROM DETAI dt
JOIN ThongKe tk ON dt.MADT = tk.MADT
WHERE tk.TONG_SP = (SELECT MAX(TONG_SP) FROM ThongKe);

DECLARE @max_cnt INT, @min_cnt INT;
SELECT @max_cnt = COUNT(*), @min_cnt = MIN(TONG_SP) FROM @max_projects;

IF @max_cnt = 2 AND @min_cnt = 3
    PRINT '  [PASS] Test 9: Extreme tie-breaking verified: DT01 (3 Q1) and DT02 (3 Q1) preserved; others excluded.';
ELSE
BEGIN
    PRINT '  [FAIL] Test 9: Count=' + CAST(@max_cnt AS VARCHAR) + ', Min=' + CAST(@min_cnt AS VARCHAR);
    THROW 50080, 'Test 9 FAILED: Extreme tie-breaking did not preserve tied records', 1;
END
GO

PRINT '------------------------------------------------------------';
PRINT '=== ALL 9 MOCK-14 VERIFICATION SUITES PASSED WITH ASSERTIONS ===';
PRINT '------------------------------------------------------------';
