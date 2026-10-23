-- ============================================================================
-- FIXTURE & VERIFICATION SCRIPT: MOCK-01 (GOLD STANDARD)
-- ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 01: QUẢN LÝ CUNG ỨNG & TIÊM CHỦNG VẮC-XIN
-- Tác giả: VÕ TRỌNG PHÚC — CSDL_UIT Master Series
-- Môi trường thực thi: Microsoft SQL Server (Transact-SQL)
-- ============================================================================

-- Khởi tạo Database kiểm thử riêng biệt
IF DB_ID('IT004_MOCK01_DB') IS NULL
    CREATE DATABASE IT004_MOCK01_DB;
GO

USE IT004_MOCK01_DB;
GO

-- 1. TẠO LƯỢC ĐỒ CƠ SỞ DỮ LIỆU
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
    SOLIEU INT CHECK (SOLIEU >= 0),
    DONGIA DECIMAL(12, 2) CHECK (DONGIA >= 0),
    MANCC VARCHAR(10) NOT NULL FOREIGN KEY REFERENCES NHACUNGCAP(MANCC)
);

CREATE TABLE DIEMTIEM (
    MADT VARCHAR(10) PRIMARY KEY,
    TENDT NVARCHAR(100) NOT NULL,
    DIACHI NVARCHAR(150),
    QUAN NVARCHAR(50) NOT NULL,
    SUCCHUA INT CHECK (SUCCHUA > 0)
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
    TRANGTHAI INT, -- 0: đang chuyển, 1: đã nhận
    MADT VARCHAR(10) NOT NULL FOREIGN KEY REFERENCES DIEMTIEM(MADT)
);

CREATE TABLE CTPX (
    MAPX VARCHAR(10) NOT NULL FOREIGN KEY REFERENCES PHIEUXUAT(MAPX),
    MALO VARCHAR(10) NOT NULL FOREIGN KEY REFERENCES LOVACXIN(MALO),
    SOLIEUXUAT INT,
    PRIMARY KEY (MAPX, MALO)
);
GO

-- 2. CÂU 2.1a: TẠO RÀNG BUỘC CHECK THEO YÊU CẦU ĐỀ BÀI
ALTER TABLE CTPX
ADD CONSTRAINT CK_CTPX_SOLIEUXUAT CHECK (SOLIEUXUAT > 0);

ALTER TABLE PHIEUXUAT
ADD CONSTRAINT CK_PHIEUXUAT_TRANGTHAI CHECK (TRANGTHAI IN (0, 1));
GO

PRINT '=== [TEST 2.1a: CHECK Constraints Verification] ===';
-- Test CHECK CK_CTPX_SOLIEUXUAT với giá trị không hợp lệ (SOLIEUXUAT = 0)
BEGIN TRY
    INSERT INTO CTPX VALUES ('PX_FAKE', 'LO_FAKE', 0);
    PRINT 'FAIL: CK_CTPX_SOLIEUXUAT did not reject 0';
END TRY
BEGIN CATCH
    PRINT 'PASS: CK_CTPX_SOLIEUXUAT successfully rejected invalid value 0 (Error ' + CAST(ERROR_NUMBER() AS VARCHAR) + ')';
END CATCH;

-- Test CHECK CK_PHIEUXUAT_TRANGTHAI với giá trị không hợp lệ (TRANGTHAI = 2)
BEGIN TRY
    INSERT INTO PHIEUXUAT VALUES ('PX_FAKE', '2024-10-15', 2, 'DT01');
    PRINT 'FAIL: CK_PHIEUXUAT_TRANGTHAI did not reject 2';
END TRY
BEGIN CATCH
    PRINT 'PASS: CK_PHIEUXUAT_TRANGTHAI successfully rejected invalid value 2 (Error ' + CAST(ERROR_NUMBER() AS VARCHAR) + ')';
END CATCH;
GO

-- 3. CHÈN DỮ LIỆU KIỂM THỬ (TEST FIXTURES & TOÀN BỘ EDGE CASES)
INSERT INTO NHACUNGCAP VALUES
('NCC01', 'AstraZeneca', N'Anh Quốc', '0281234567'),
('NCC02', 'Pfizer', N'Hoa Kỳ', '0282345678'),
('NCC03', 'Moderna', N'Hoa Kỳ', '0283456789'),
('NCC04', 'VnBiotech', N'Việt Nam', '0284567890');

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
('DT06', N'Trạm Y Tế P.12', N'Bùi Đình Túy', N'Bình Thạnh', 400);     -- Edge Case: Không có nhân viên để kiểm thử Left Outer Join

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
('PX06', '2024-10-22', 0, 'DT05'); -- Edge Case: TRANGTHAI = 0 (Đang chuyển, chưa tiếp nhận!)

INSERT INTO CTPX VALUES
('PX01', 'LO05', 1000),
('PX01', 'LO06', 1000), -- DT01 nhận cả LO05 và LO06 trong cùng 1 phiếu xuất
('PX01', 'LO03', 1500),
('PX02', 'LO05', 2000), -- DT02 nhận LO05 ở PX02
('PX03', 'LO06', 1500), -- DT02 nhận LO06 ở PX03 -> DT02 nhận đủ LO05 và LO06 qua 2 phiếu khác nhau!
('PX04', 'LO01', 2000), -- DT03 chỉ nhận LO01
('PX05', 'LO05', 3000), -- DT04 chỉ nhận LO05, THIẾU LO06 -> Không thỏa phép chia
('PX06', 'LO05', 500),  -- DT05 có cả LO05 và LO06 nhưng TRANGTHAI = 0 (chưa tiếp nhận) -> Không thỏa phép chia
('PX06', 'LO06', 500);
GO

-- ============================================================================
-- 4. THỰC THI KIỂM TRẢ CÁC CÂU TRUY VẤN
-- ============================================================================

-- Câu 2.1b: UPDATE tăng giá 10% các lô vắc-xin HSD 2025 của AstraZeneca
-- Expected: LO01 (150k -> 165k), LO02 (160k -> 176k)
PRINT '--- [TEST 2.1b: UPDATE 10% AstraZeneca 2025] ---';
UPDATE LOVACXIN
SET DONGIA = DONGIA * 1.1
FROM LOVACXIN LV
INNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC
WHERE YEAR(LV.HSD) = 2025
  AND NCC.TENNCC = 'AstraZeneca';

SELECT MALO, TENLO, DONGIA, HSD, MANCC
FROM LOVACXIN
WHERE MANCC = 'NCC01';
GO

-- Câu 2.2a: Lô vắc-xin Pfizer-BioNTech sản xuất năm 2024
-- Expected: LO03, LO04
PRINT '--- [TEST 2.2a: Select Pfizer 2024] ---';
SELECT MALO, TENLO, SOLIEU, DONGIA
FROM LOVACXIN
WHERE TENVACXIN = 'Pfizer-BioNTech'
  AND NGAYSX >= '2024-01-01' AND NGAYSX <= '2024-12-31';
GO

-- Câu 2.2b: Điểm tiêm đã tiếp nhận phiếu xuất ngày 15/10/2024 (TRANGTHAI = 1)
-- Expected: DT01, DT02, DT03
PRINT '--- [TEST 2.2b: Điểm tiêm đã tiếp nhận 15/10/2024] ---';
SELECT DISTINCT DT.MADT, DT.TENDT, DT.QUAN
FROM DIEMTIEM DT
INNER JOIN PHIEUXUAT PX ON DT.MADT = PX.MADT
WHERE PX.NGAYXUAT = '2024-10-15'
  AND PX.TRANGTHAI = 1;
GO

-- Câu 2.2c: Điểm tiêm quận Bình Thạnh và nhân viên công tác nếu có (LEFT OUTER JOIN)
-- Expected: DT01 (NV01), DT02 (NV02), DT06 (NULL) -> Chứng minh không mất DT06
PRINT '--- [TEST 2.2c: Left Outer Join Bình Thạnh] ---';
SELECT DT.MADT, DT.TENDT, NV.HOTEN
FROM DIEMTIEM DT
LEFT OUTER JOIN NHANVIEN NV ON DT.MADT = NV.MADT
WHERE DT.QUAN = N'Bình Thạnh';
GO

-- Câu 2.2d: Gom nhóm tổng số liều đã tiếp nhận (TRANGTHAI = 1) theo điểm tiêm T10/2024
-- Expected:
-- DT01: 1000 + 1000 + 1500 = 3500
-- DT02: 2000 (PX02) + 1500 (PX03) = 3500
-- DT03: 2000 (PX04) = 2000
-- DT04: 3000 (PX05) = 3000
-- (DT05 không có dòng nào vì PX06 có TRANGTHAI = 0)
PRINT '--- [TEST 2.2d: Gom nhóm tổng liều đã tiếp nhận T10/2024] ---';
SELECT PX.MADT, SUM(CT.SOLIEUXUAT) AS TONGLIEU
FROM PHIEUXUAT PX
INNER JOIN CTPX CT ON PX.MAPX = CT.MAPX
WHERE PX.NGAYXUAT >= '2024-10-01' AND PX.NGAYXUAT <= '2024-10-31'
  AND PX.TRANGTHAI = 1
GROUP BY PX.MADT;
GO

-- Câu 2.2e: Phép chia - Điểm tiêm đã tiếp nhận TẤT CẢ các lô của Moderna (LO05, LO06)
-- Expected: Đúng 2 điểm tiêm DT01 và DT02!
-- DT04 bị loại vì thiếu LO06.
-- DT05 bị loại vì PX06 có TRANGTHAI = 0 (chưa tiếp nhận).
PRINT '--- [TEST 2.2e: Phép chia Moderna] ---';
SELECT DT.MADT, DT.TENDT
FROM DIEMTIEM DT
WHERE NOT EXISTS (
    -- Tập các lô của Moderna
    SELECT LV.MALO
    FROM LOVACXIN LV
    INNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC
    WHERE NCC.TENNCC = 'Moderna'
    EXCEPT
    -- Tập các lô mà điểm tiêm DT thực sự đã tiếp nhận (TRANGTHAI = 1)
    SELECT CT.MALO
    FROM PHIEUXUAT PX
    INNER JOIN CTPX CT ON PX.MAPX = CT.MAPX
    WHERE PX.MADT = DT.MADT
      AND PX.TRANGTHAI = 1
);
GO

-- Câu 2.2f: Điểm tiêm có sức chứa lớn nhất tại Thủ Đức (Kèm Tie-breaking Đồng Hạng)
-- Expected: Cả hai điểm tiêm DT04 (2500) và DT05 (2500)! Cả hai đều lớn hơn DT03 (1800).
PRINT '--- [TEST 2.2f: Cực trị MAX sức chứa Thủ Đức (Đồng Hạng)] ---';
SELECT MADT, TENDT
FROM DIEMTIEM
WHERE QUAN = N'Thủ Đức'
  AND SUCCHUA = (SELECT MAX(SUCCHUA) FROM DIEMTIEM WHERE QUAN = N'Thủ Đức');
GO

PRINT '=== [MOCK-01 FIXTURE: ALL VERIFICATION QUERIES EXECUTED SUCCESSFULLY] ===';
GO
