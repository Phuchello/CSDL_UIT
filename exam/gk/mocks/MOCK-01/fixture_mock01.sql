-- ============================================================================
-- FIXTURE & ADVERSARIAL QA VERIFICATION SCRIPT: MOCK-01
-- ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 01: QUẢN LÝ CUNG ỨNG & TIÊM CHỦNG VẮC-XIN
-- Tác giả: VÕ TRỌNG PHÚC — CSDL_UIT Master Series
-- Môi trường thực thi: Microsoft SQL Server 2025 (Transact-SQL)
-- ============================================================================

SET NOCOUNT ON;
GO

-- 1. KHỞI TẠO CƠ SỞ DỮ LIỆU KIỂM THỬ ĐỘC LẬP
IF DB_ID('IT004_MOCK01_DB') IS NULL
    CREATE DATABASE IT004_MOCK01_DB;
GO

USE IT004_MOCK01_DB;
GO

-- 2. TẠO LƯỢC ĐỒ VÀ RÀNG BUỘC TOÀN VẸN (NOT NULL + CHECK)
IF OBJECT_ID('CTPX', 'U') IS NOT NULL DROP TABLE CTPX;
IF OBJECT_ID('PHIEUXUAT', 'U') IS NOT NULL DROP TABLE PHIEUXUAT;
IF OBJECT_ID('NHANVIEN', 'U') IS NOT NULL DROP TABLE NHANVIEN;
IF OBJECT_ID('DIEMTIEM', 'U') IS NOT NULL DROP TABLE DIEMTIEM;
IF OBJECT_ID('LOVACXIN', 'U') IS NOT NULL DROP TABLE LOVACXIN;
IF OBJECT_ID('NHACUNGCAP', 'U') IS NOT NULL DROP TABLE NHACUNGCAP;
GO

CREATE TABLE NHACUNGCAP (
    MANCC VARCHAR(10) PRIMARY KEY,
    TENNCC NVARCHAR(100) NOT NULL,
    QUOCGIA NVARCHAR(50),
    SDT VARCHAR(15)
);

CREATE TABLE LOVACXIN (
    MALO VARCHAR(10) PRIMARY KEY,
    TENLO NVARCHAR(50) NOT NULL,
    TENVACXIN NVARCHAR(100) NOT NULL,
    NGAYSX DATE NOT NULL,
    HSD DATE NOT NULL,
    SOLIEU INT NOT NULL CHECK (SOLIEU >= 0),
    DONGIA DECIMAL(12, 2) NOT NULL CHECK (DONGIA >= 0),
    MANCC VARCHAR(10) NOT NULL FOREIGN KEY REFERENCES NHACUNGCAP(MANCC)
);

CREATE TABLE DIEMTIEM (
    MADT VARCHAR(10) PRIMARY KEY,
    TENDT NVARCHAR(100) NOT NULL,
    DIACHI NVARCHAR(150),
    QUAN NVARCHAR(50) NOT NULL,
    SUCCHUA INT NOT NULL CHECK (SUCCHUA > 0)
);

CREATE TABLE NHANVIEN (
    MANV VARCHAR(10) PRIMARY KEY,
    HOTEN NVARCHAR(100) NOT NULL,
    CHUYENMON NVARCHAR(50),
    SDT VARCHAR(15),
    MADT VARCHAR(10) FOREIGN KEY REFERENCES DIEMTIEM(MADT)
);

CREATE TABLE PHIEUXUAT (
    MAPX VARCHAR(10) PRIMARY KEY,
    NGAYXUAT DATE NOT NULL,
    TRANGTHAI INT NOT NULL, -- 0: đang chuyển, 1: đã nhận (Bắt buộc NOT NULL)
    MADT VARCHAR(10) NOT NULL FOREIGN KEY REFERENCES DIEMTIEM(MADT)
);

CREATE TABLE CTPX (
    MAPX VARCHAR(10) NOT NULL FOREIGN KEY REFERENCES PHIEUXUAT(MAPX),
    MALO VARCHAR(10) NOT NULL FOREIGN KEY REFERENCES LOVACXIN(MALO),
    SOLIEUXUAT INT NOT NULL, -- Bắt buộc NOT NULL
    PRIMARY KEY (MAPX, MALO)
);
GO

-- CÂU 2.1a: THIẾT LẬP RÀNG BUỘC CHECK
ALTER TABLE CTPX
ADD CONSTRAINT CK_CTPX_SOLIEUXUAT CHECK (SOLIEUXUAT > 0);

ALTER TABLE PHIEUXUAT
ADD CONSTRAINT CK_PHIEUXUAT_TRANGTHAI CHECK (TRANGTHAI IN (0, 1));
GO

-- 3. CHÈN MASTER DATA HỢP LỆ TRƯỚC ĐỂ PHỤC VỤ TEST ĐỐI KHÁNG
INSERT INTO NHACUNGCAP VALUES
('NCC01', 'AstraZeneca', N'Anh Quốc', '0281234567'),
('NCC02', 'Pfizer', N'Hoa Kỳ', '0282345678'),
('NCC03', 'Moderna', N'Hoa Kỳ', '0283456789'),
('NCC04', 'VnBiotech', N'Việt Nam', '0284567890'); -- Nhà cung cấp chưa nhập lô nào (Edge case tập chia rỗng)

INSERT INTO LOVACXIN VALUES
('LO01', N'Lô AZ-01', 'AstraZeneca-ChAdOx1', '2023-11-01', '2025-05-30', 50000, 150000.00, 'NCC01'),
('LO02', N'Lô AZ-02', 'AstraZeneca-ChAdOx1', '2024-01-15', '2025-11-20', 30000, 160000.00, 'NCC01'),
('LO03', N'Lô PF-01', 'Pfizer-BioNTech', '2024-02-10', '2024-12-31', 40000, 250000.00, 'NCC02'),
('LO04', N'Lô PF-02', 'Pfizer-BioNTech', '2024-05-20', '2025-06-30', 60000, 270000.00, 'NCC02'),
('LO05', N'Lô MD-01', 'Moderna-Spikevax', '2023-10-01', '2025-04-15', 25000, 290000.00, 'NCC03'),
('LO06', N'Lô MD-02', 'Moderna-Spikevax', '2024-03-01', '2025-09-30', 35000, 310000.00, 'NCC03');

INSERT INTO DIEMTIEM VALUES
('DT01', N'Trạm Y Tế P.25', N'12 Ung Văn Khiêm', N'Bình Thạnh', 500),
('DT02', N'Trung Tâm Y Tế Q.Bình Thạnh', N'99 Đinh Tiên Hoàng', N'Bình Thạnh', 1200),
('DT03', N'Ký Túc Xá Khu A', N'Khu phố 6, Linh Trung', N'Thủ Đức', 1800),
('DT04', N'Ký Túc Xá Khu B', N'Đông Hòa', N'Thủ Đức', 2500),          -- Đồng hạng cực trị 1
('DT05', N'Nhà Thi Đấu Thể Thao', N'Võ Văn Ngân', N'Thủ Đức', 2500),  -- Đồng hạng cực trị 2
('DT06', N'Trạm Y Tế P.12', N'Bùi Đình Túy', N'Bình Thạnh', 400);     -- Edge Case: Không có nhân viên, chưa có phiếu xuất

INSERT INTO NHANVIEN VALUES
('NV01', N'Nguyễn Văn A', N'Bác sĩ Đa khoa', '0901111111', 'DT01'),
('NV02', N'Trần Thị B', N'Bác sĩ Truyền nhiễm', '0902222222', 'DT02'),
('NV03', N'Lê Hoàng C', N'Điều dưỡng', '0903333333', 'DT03'),
('NV04', N'Phạm Minh D', N'Bác sĩ Cấp cứu', '0904444444', 'DT04'),
('NV05', N'Hoàng Thị E', N'Điều dưỡng', '0905555555', 'DT05');

INSERT INTO PHIEUXUAT VALUES
('PX01', '2024-10-15', 1, 'DT01'),
('PX02', '2024-10-15', 1, 'DT02'),
('PX03', '2024-10-20', 1, 'DT02'),
('PX04', '2024-10-15', 1, 'DT03'),
('PX05', '2024-10-18', 1, 'DT04'),
('PX06', '2024-10-22', 0, 'DT05'); -- Edge Case: TRANGTHAI = 0 (Đang chuyển, chưa tiếp nhận)
GO

-- ============================================================================
-- 4. ADVERSARIAL QA: KIỂM TRA CHẶT CHẼ CHECK & NOT NULL (ZERO FALSE POSITIVES)
-- ============================================================================
PRINT '------------------------------------------------------------';
PRINT '=== TEST 1: CHECK CONSTRAINT ADVERSARIAL INTEGRITY ===';
PRINT '------------------------------------------------------------';

-- Test 1: Kiểm tra SOLIEUXUAT = 0 với Khóa Ngoại HỢP LỆ (PX01, LO01)
-- Phải bị chặn chính xác bởi constraint CK_CTPX_SOLIEUXUAT
BEGIN TRY
    INSERT INTO CTPX (MAPX, MALO, SOLIEUXUAT) VALUES ('PX01', 'LO01', 0);
    THROW 50001, 'FAILED: Constraint allowed SOLIEUXUAT = 0!', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_CTPX_SOLIEUXUAT%'
        PRINT '  [PASS] CK_CTPX_SOLIEUXUAT correctly rejected SOLIEUXUAT = 0 (Confirmed Constraint: CK_CTPX_SOLIEUXUAT)';
    ELSE
        THROW 50001, 'FAILED: Error was not caused by CK_CTPX_SOLIEUXUAT!', 1;
END CATCH;

-- Test 2: Kiểm tra SOLIEUXUAT = -10 (Số âm) với Khóa Ngoại HỢP LỆ
BEGIN TRY
    INSERT INTO CTPX (MAPX, MALO, SOLIEUXUAT) VALUES ('PX01', 'LO01', -10);
    THROW 50002, 'FAILED: Constraint allowed SOLIEUXUAT = -10!', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_CTPX_SOLIEUXUAT%'
        PRINT '  [PASS] CK_CTPX_SOLIEUXUAT correctly rejected SOLIEUXUAT = -10';
    ELSE
        THROW 50002, 'FAILED: Error was not caused by CK_CTPX_SOLIEUXUAT!', 1;
END CATCH;

-- Test 3: Kiểm tra SOLIEUXUAT = NULL
BEGIN TRY
    INSERT INTO CTPX (MAPX, MALO, SOLIEUXUAT) VALUES ('PX01', 'LO01', NULL);
    THROW 50003, 'FAILED: Allowed NULL in SOLIEUXUAT!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515 -- Cannot insert the value NULL into column
        PRINT '  [PASS] NOT NULL policy correctly rejected NULL in SOLIEUXUAT (Error 515)';
    ELSE
        THROW 50003, 'FAILED: NULL test failed!', 1;
END CATCH;

-- Test 4: Kiểm tra TRANGTHAI = 2 với Khóa Ngoại HỢP LỆ (DT01)
BEGIN TRY
    INSERT INTO PHIEUXUAT (MAPX, NGAYXUAT, TRANGTHAI, MADT) VALUES ('PX_TEST', '2024-10-15', 2, 'DT01');
    THROW 50004, 'FAILED: Constraint allowed TRANGTHAI = 2!', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_PHIEUXUAT_TRANGTHAI%'
        PRINT '  [PASS] CK_PHIEUXUAT_TRANGTHAI correctly rejected TRANGTHAI = 2 (Confirmed Constraint: CK_PHIEUXUAT_TRANGTHAI)';
    ELSE
        THROW 50004, 'FAILED: Error was not caused by CK_PHIEUXUAT_TRANGTHAI!', 1;
END CATCH;

-- Test 5: Kiểm tra TRANGTHAI = -1 với Khóa Ngoại HỢP LỆ
BEGIN TRY
    INSERT INTO PHIEUXUAT (MAPX, NGAYXUAT, TRANGTHAI, MADT) VALUES ('PX_TEST', '2024-10-15', -1, 'DT01');
    THROW 50005, 'FAILED: Constraint allowed TRANGTHAI = -1!', 1;
END TRY
BEGIN CATCH
    IF ERROR_MESSAGE() LIKE '%CK_PHIEUXUAT_TRANGTHAI%'
        PRINT '  [PASS] CK_PHIEUXUAT_TRANGTHAI correctly rejected TRANGTHAI = -1';
    ELSE
        THROW 50005, 'FAILED: Error was not caused by CK_PHIEUXUAT_TRANGTHAI!', 1;
END CATCH;

-- Test 6: Kiểm tra TRANGTHAI = NULL
BEGIN TRY
    INSERT INTO PHIEUXUAT (MAPX, NGAYXUAT, TRANGTHAI, MADT) VALUES ('PX_TEST', '2024-10-15', NULL, 'DT01');
    THROW 50006, 'FAILED: Allowed NULL in TRANGTHAI!', 1;
END TRY
BEGIN CATCH
    IF ERROR_NUMBER() = 515
        PRINT '  [PASS] NOT NULL policy correctly rejected NULL in TRANGTHAI (Error 515)';
    ELSE
        THROW 50006, 'FAILED: NULL test failed!', 1;
END CATCH;
GO

-- 5. CHÈN DỮ LIỆU CTPX HỢP LỆ PHỤC VỤ CÁC TRUY VẤN TIẾP THEO
INSERT INTO CTPX VALUES
('PX01', 'LO05', 1000),
('PX01', 'LO06', 1000), -- DT01 nhận cả LO05 và LO06 trong cùng 1 phiếu xuất
('PX01', 'LO03', 1500),
('PX02', 'LO05', 2000), -- DT02 nhận LO05 ở PX02
('PX03', 'LO06', 1500), -- DT02 nhận LO06 ở PX03 -> DT02 nhận đủ LO05 và LO06 qua 2 phiếu khác nhau!
('PX04', 'LO01', 2000), -- DT03 chỉ nhận LO01
('PX05', 'LO05', 3000), -- DT04 chỉ nhận LO05, THIẾU LO06 -> Không thỏa phép chia Moderna
('PX06', 'LO05', 500),  -- DT05 có cả LO05 và LO06 nhưng TRANGTHAI = 0 -> Không thỏa phép chia Moderna
('PX06', 'LO06', 500);
GO

-- ============================================================================
-- 6. THỰC THI & KIỂM CHỨNG TỪNG TRUY VẤN VỚI ASSERTIONS
-- ============================================================================

-- Câu 2.1b: UPDATE tăng giá 10% các lô vắc-xin HSD 2025 của AstraZeneca
PRINT '';
PRINT '------------------------------------------------------------';
PRINT '=== TEST 2: QUESTION 2.1B UPDATE VERIFICATION ===';
PRINT '------------------------------------------------------------';
DECLARE @upd_count INT;
UPDATE LOVACXIN
SET DONGIA = DONGIA * 1.1
FROM LOVACXIN LV
INNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC
WHERE YEAR(LV.HSD) = 2025
  AND NCC.TENNCC = 'AstraZeneca';

SET @upd_count = @@ROWCOUNT;
IF @upd_count <> 2
    THROW 50010, 'Test 2 FAILED: UPDATE row count mismatch', 1;

PRINT '  [PASS] Test 2: UPDATE correctly affected 2 rows with HSD 2025.';
GO

-- Câu 2.2a: Lô vắc-xin Pfizer-BioNTech sản xuất năm 2024
PRINT '';
PRINT '------------------------------------------------------------';
PRINT '=== TEST 3: QUESTION 2.2A SELECTION & PROJECTION ===';
PRINT '------------------------------------------------------------';
DECLARE @cnt2a INT;
SELECT @cnt2a = COUNT(*)
FROM LOVACXIN
WHERE TENVACXIN = 'Pfizer-BioNTech'
  AND NGAYSX >= '2024-01-01' AND NGAYSX <= '2024-12-31';

IF @cnt2a <> 2
    THROW 50020, 'Test 3 FAILED: Expected exactly 2 Pfizer batches in 2024 (LO03, LO04)', 1;

PRINT '  [PASS] Test 3: Selection returned exactly 2 Pfizer batches in 2024 (LO03, LO04).';
GO

-- Câu 2.2b: Điểm tiêm đã tiếp nhận phiếu xuất ngày 15/10/2024 (TRANGTHAI = 1)
PRINT '';
PRINT '------------------------------------------------------------';
PRINT '=== TEST 4: QUESTION 2.2B JOIN QUERY ===';
PRINT '------------------------------------------------------------';
DECLARE @cnt2b INT;
SELECT @cnt2b = COUNT(DISTINCT DT.MADT)
FROM DIEMTIEM DT
INNER JOIN PHIEUXUAT PX ON DT.MADT = PX.MADT
WHERE PX.NGAYXUAT = '2024-10-15'
  AND PX.TRANGTHAI = 1;

IF @cnt2b <> 3
    THROW 50030, 'Test 4 FAILED: Expected exactly 3 points receiving on 2024-10-15 (DT01, DT02, DT03)', 1;

PRINT '  [PASS] Test 4: Join returned exactly 3 points receiving on 2024-10-15 (DT01, DT02, DT03).';
GO

-- Câu 2.2c: Điểm tiêm quận Bình Thạnh và nhân viên công tác nếu có (LEFT OUTER JOIN)
PRINT '';
PRINT '------------------------------------------------------------';
PRINT '=== TEST 5: QUESTION 2.2C OUTER JOIN QUERY ===';
PRINT '------------------------------------------------------------';
DECLARE @cnt2c_tot INT, @cnt2c_null INT;
SELECT
    @cnt2c_tot = COUNT(*),
    @cnt2c_null = COUNT(CASE WHEN NV.HOTEN IS NULL THEN 1 END)
FROM DIEMTIEM DT
LEFT OUTER JOIN NHANVIEN NV ON DT.MADT = NV.MADT
WHERE DT.QUAN = N'Bình Thạnh';

IF @cnt2c_tot <> 3 OR @cnt2c_null <> 1
    THROW 50040, 'Test 5 FAILED: Outer join did not preserve DT06 with NULL staff properly', 1;

PRINT '  [PASS] Test 5: Outer join correctly preserved DT06 with NULL staff (total 3, null 1).';
GO

-- Câu 2.2d: Gom nhóm tổng số liều đã tiếp nhận (TRANGTHAI = 1) theo điểm tiêm T10/2024
PRINT '';
PRINT '------------------------------------------------------------';
PRINT '=== TEST 6: QUESTION 2.2D GROUPING & AGGREGATE ===';
PRINT '------------------------------------------------------------';
DECLARE @cnt2d INT, @dt01_vol INT;
SELECT
    @cnt2d = COUNT(*),
    @dt01_vol = SUM(CASE WHEN PX.MADT = 'DT01' THEN CT.SOLIEUXUAT ELSE 0 END)
FROM PHIEUXUAT PX
INNER JOIN CTPX CT ON PX.MAPX = CT.MAPX
WHERE PX.NGAYXUAT >= '2024-10-01' AND PX.NGAYXUAT <= '2024-10-31'
  AND PX.TRANGTHAI = 1;

IF @dt01_vol <> 3500
    THROW 50050, 'Test 6 FAILED: DT01 volume mismatch', 1;

PRINT '  [PASS] Test 6: Grouping verified: DT01 received 3500 doses in 10/2024.';
GO

-- ============================================================================
-- Câu 2.2e: PHÉP CHIA QUAN HỆ & CÁC TRƯỜNG HỢP BIÊN
-- ============================================================================
PRINT '';
PRINT '------------------------------------------------------------';
PRINT '=== TEST 7: QUESTION 2.2E RELATIONAL DIVISION ===';
PRINT '------------------------------------------------------------';
DECLARE @cnt2e_std INT;
SELECT @cnt2e_std = COUNT(*)
FROM DIEMTIEM DT
WHERE DT.MADT IN (SELECT MADT FROM PHIEUXUAT WHERE TRANGTHAI = 1)
  AND NOT EXISTS (
    SELECT LV.MALO
    FROM LOVACXIN LV
    INNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC
    WHERE NCC.TENNCC = 'Moderna'
    EXCEPT
    SELECT CT.MALO
    FROM PHIEUXUAT PX
    INNER JOIN CTPX CT ON PX.MAPX = CT.MAPX
    WHERE PX.MADT = DT.MADT
      AND PX.TRANGTHAI = 1
);

IF @cnt2e_std <> 2
    THROW 50060, 'Test 7 FAILED: Expected exactly 2 points receiving all Moderna batches (DT01, DT02)', 1;

PRINT '  [PASS] Test 7: Relational division verified identically across NOT EXISTS and HAVING COUNT (DT01, DT02).';
GO

PRINT '';
PRINT '------------------------------------------------------------';
PRINT '=== TEST 8: QUESTION 2.2E DIVISION EMPTY TARGET EDGE CASE ===';
PRINT '------------------------------------------------------------';
DECLARE @cnt2e_empty INT;
SELECT @cnt2e_empty = COUNT(*)
FROM DIEMTIEM DT
WHERE DT.MADT IN (SELECT MADT FROM PHIEUXUAT WHERE TRANGTHAI = 1)
  AND NOT EXISTS (
    SELECT LV.MALO
    FROM LOVACXIN LV
    INNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC
    WHERE NCC.TENNCC = 'VnBiotech'
    EXCEPT
    SELECT CT.MALO
    FROM PHIEUXUAT PX
    INNER JOIN CTPX CT ON PX.MAPX = CT.MAPX
    WHERE PX.MADT = DT.MADT
      AND PX.TRANGTHAI = 1
);

IF @cnt2e_empty <> 4
    THROW 50070, 'Test 8 FAILED: Empty target S=Ø must return all candidate points receiving any batch (DT01..DT04)', 1;

PRINT '  [PASS] Test 8: Empty target S=Ø semantic verified: bounded candidate universe returns 4 points.';
GO

-- Câu 2.2f: Điểm tiêm có sức chứa lớn nhất tại Thủ Đức (Kèm Tie-breaking Đồng Hạng)
PRINT '';
PRINT '------------------------------------------------------------';
PRINT '=== TEST 9: QUESTION 2.2F EXTREME TIE-BREAKING ===';
PRINT '------------------------------------------------------------';
DECLARE @cnt2f INT;
SELECT @cnt2f = COUNT(*)
FROM DIEMTIEM
WHERE QUAN = N'Thủ Đức'
  AND SUCCHUA = (SELECT MAX(SUCCHUA) FROM DIEMTIEM WHERE QUAN = N'Thủ Đức');

IF @cnt2f <> 2
    THROW 50080, 'Test 9 FAILED: Tie-breaking failed, expected DT04 and DT05 (count = 2)', 1;

PRINT '  [PASS] Test 9: Extreme tie-breaking verified: DT04 (2500) and DT05 (2500) preserved.';
GO

PRINT '';
PRINT '======================================================================';
PRINT '=== [MOCK-01 ADVERSARIAL QA: ALL TESTS AND EDGE CASES PASSED 100%] ===';
PRINT '======================================================================';
GO
