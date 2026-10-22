-- ============================================================================
-- FIXTURE & VERIFICATION SCRIPT: MOCK-01
-- ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 01: QUẢN LÝ CUNG ỨNG & TIÊM CHỦNG VẮC-XIN
-- Tác giả: VÕ TRỌNG PHÚC
-- Môi trường: Microsoft SQL Server (Transact-SQL)
-- ============================================================================

-- 1. TẠO LƯỢC ĐỒ CƠ SỞ DỮ LIỆU
IF OBJECT_ID('CTPX', 'U') IS NOT NULL DROP TABLE CTPX;
IF OBJECT_ID('PHIEUXUAT', 'U') IS NOT NULL DROP TABLE PHIEUXUAT;
IF OBJECT_ID('BACSI', 'U') IS NOT NULL DROP TABLE BACSI;
IF OBJECT_ID('DIEMTIEM', 'U') IS NOT NULL DROP TABLE DIEMTIEM;
IF OBJECT_ID('LOVACXIN', 'U') IS NOT NULL DROP TABLE LOVACXIN;
IF OBJECT_ID('NHACUNGCAP', 'U') IS NOT NULL DROP TABLE NHACUNGCAP;

CREATE TABLE NHACUNGCAP (
    MANCC VARCHAR(10) PRIMARY KEY,
    TENNCC NVARCHAR(100) NOT NULL,
    QUOCGIA NVARCHAR(50),
    SDT VARCHAR(15)
);

CREATE TABLE LOVACXIN (
    MALO VARCHAR(10) PRIMARY KEY,
    TENLO NVARCHAR(50) NOT NULL,
    TENKVACXIN NVARCHAR(100) NOT NULL,
    MANCC VARCHAR(10) NOT NULL FOREIGN KEY REFERENCES NHACUNGCAP(MANCC),
    NGAYSX DATE NOT NULL,
    HSD DATE NOT NULL,
    SOLIEU INT CHECK (SOLIEU >= 0),
    DONGIA DECIMAL(12, 2) CHECK (DONGIA >= 0)
);

CREATE TABLE DIEMTIEM (
    MADT VARCHAR(10) PRIMARY KEY,
    TENDT NVARCHAR(100) NOT NULL,
    QUAN NVARCHAR(50) NOT NULL,
    SUCCHUA INT CHECK (SUCCHUA > 0),
    MATRP VARCHAR(10) -- Mã trưởng điểm tiêm
);

CREATE TABLE BACSI (
    MABS VARCHAR(10) PRIMARY KEY,
    HOTEN NVARCHAR(100) NOT NULL,
    CHUYENKHOA NVARCHAR(50),
    SDT VARCHAR(15),
    MADT VARCHAR(10) FOREIGN KEY REFERENCES DIEMTIEM(MADT)
);

CREATE TABLE PHIEUXUAT (
    MAPX VARCHAR(10) PRIMARY KEY,
    NGAYXUAT DATE NOT NULL,
    MADT VARCHAR(10) NOT NULL FOREIGN KEY REFERENCES DIEMTIEM(MADT),
    TRANGTHAI INT CHECK (TRANGTHAI IN (0, 1))
);

CREATE TABLE CTPX (
    MAPX VARCHAR(10) NOT NULL FOREIGN KEY REFERENCES PHIEUXUAT(MAPX),
    MALO VARCHAR(10) NOT NULL FOREIGN KEY REFERENCES LOVACXIN(MALO),
    SOLIEUXUAT INT CHECK (SOLIEUXUAT > 0),
    PRIMARY KEY (MAPX, MALO)
);

-- 2. CHÈN DỮ LIỆU KIỂM THỬ (TEST FIXTURES & EDGE CASES)
INSERT INTO NHACUNGCAP VALUES
('NCC01', 'AstraZeneca', N'Anh Quốc', '0281234567'),
('NCC02', 'Pfizer', N'Hoa Kỳ', '0282345678'),
('NCC03', 'Moderna', N'Hoa Kỳ', '0283456789'),
('NCC04', 'VnBiotech', N'Việt Nam', '0284567890');

INSERT INTO LOVACXIN VALUES
('LO01', N'Lô AZ-01', 'AstraZeneca-ChAdOx1', 'NCC01', '2023-11-01', '2025-05-30', 50000, 150000.00),
('LO02', N'Lô AZ-02', 'AstraZeneca-ChAdOx1', 'NCC01', '2024-01-15', '2025-11-20', 30000, 160000.00),
('LO03', N'Lô PF-01', 'Pfizer-BioNTech', 'NCC02', '2024-02-10', '2024-12-31', 40000, 250000.00),
('LO04', N'Lô PF-02', 'Pfizer-BioNTech', 'NCC02', '2024-05-20', '2025-06-30', 60000, 270000.00),
('LO05', N'Lô MD-01', 'Moderna-Spikevax', 'NCC03', '2023-10-01', '2025-04-15', 25000, 290000.00),
('LO06', N'Lô MD-02', 'Moderna-Spikevax', 'NCC03', '2024-03-01', '2025-09-30', 35000, 310000.00);

INSERT INTO DIEMTIEM VALUES
('DT01', N'Điểm Tiêm Trạm Y Tế P.25', N'Bình Thạnh', 500, 'BS01'),
('DT02', N'Điểm Tiêm Trung Tâm Y Tế Q.Bình Thạnh', N'Bình Thạnh', 1200, 'BS02'),
('DT03', N'Điểm Tiêm Lưu Động Linh Trung', N'Thủ Đức', 800, 'BS03'),
('DT04', N'Điểm Tiêm Ký Túc Xá Khu B', N'Thủ Đức', 2500, 'BS04'),
('DT05', N'Điểm Tiêm Nhà Văn Hóa Lao Động', N'Thủ Đức', 1800, 'BS05'),
('DT06', N'Điểm Tiêm Trạm Y Tế P.12', N'Bình Thạnh', 400, NULL); -- Edge Case: Không có bác sĩ trực để test Outer Join

INSERT INTO BACSI VALUES
('BS01', N'Nguyễn Văn A', N'Đa khoa', '0901111111', 'DT01'),
('BS02', N'Trần Thị B', N'Truyền nhiễm', '0902222222', 'DT02'),
('BS03', N'Lê Hoàng C', N'Nội nhi', '0903333333', 'DT03'),
('BS04', N'Phạm Minh D', N'Cấp cứu', '0904444444', 'DT04'),
('BS05', N'Hoàng Thị E', N'Đa khoa', '0905555555', 'DT05');

INSERT INTO PHIEUXUAT VALUES
('PX01', '2024-10-15', 'DT01', 1),
('PX02', '2024-10-15', 'DT03', 1),
('PX03', '2024-10-20', 'DT04', 1),
('PX04', '2024-10-25', 'DT01', 1),
('PX05', '2024-09-10', 'DT02', 1),
('PX06', '2024-10-18', 'DT04', 1);

INSERT INTO CTPX VALUES
('PX01', 'LO03', 1500),
('PX01', 'LO05', 1000),
('PX01', 'LO06', 1000), -- DT01 nhận cả LO05 và LO06 (đủ mọi lô của Moderna)
('PX02', 'LO01', 2000),
('PX03', 'LO05', 3000), -- DT04 chỉ nhận LO05, thiếu LO06 (không thỏa phép chia Moderna)
('PX04', 'LO04', 1200),
('PX05', 'LO01', 5000),
('PX06', 'LO06', 2500);

-- ============================================================================
-- 3. CHẠY KIỂM THỬ CÁC CÂU HỎI TRONG ĐỀ THI MOCK-01
-- ============================================================================

-- Câu 2.1b: Cập nhật tăng giá 10% lô HSD 2025 của AstraZeneca
-- Expected: LO01 và LO02 được tăng 10%
PRINT '--- Test 2.1b: UPDATE ---';
UPDATE LOVACXIN
SET DONGIA = DONGIA * 1.1
FROM LOVACXIN LV
INNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC
WHERE YEAR(LV.HSD) = 2025
  AND NCC.TENNCC = 'AstraZeneca';

-- Câu 2.2a: Lọc lô Pfizer-BioNTech sản xuất 2024
-- Expected: LO03, LO04
PRINT '--- Test 2.2a: Select Pfizer 2024 ---';
SELECT MALO, TENLO, SOLIEU, DONGIA
FROM LOVACXIN
WHERE TENKVACXIN = 'Pfizer-BioNTech'
  AND NGAYSX >= '2024-01-01' AND NGAYSX <= '2024-12-31';

-- Câu 2.2b: Điểm tiêm nhận phiếu xuất ngày 15/10/2024
-- Expected: DT01, DT03
PRINT '--- Test 2.2b: Điểm tiêm xuất 15/10/2024 ---';
SELECT DISTINCT DT.MADT, DT.TENDT, DT.QUAN
FROM DIEMTIEM DT
INNER JOIN PHIEUXUAT PX ON DT.MADT = PX.MADT
WHERE PX.NGAYXUAT = '2024-10-15';

-- Câu 2.2c: Điểm tiêm Bình Thạnh và bác sĩ trực nếu có (LEFT OUTER JOIN)
-- Expected: DT01 (BS A), DT02 (BS B), DT06 (NULL) -> Chứng minh không mất DT06
PRINT '--- Test 2.2c: Left Outer Join Bình Thạnh ---';
SELECT DT.MADT, DT.TENDT, BS.HOTEN
FROM DIEMTIEM DT
LEFT OUTER JOIN BACSI BS ON DT.MADT = BS.MADT
WHERE DT.QUAN = N'Bình Thạnh';

-- Câu 2.2d: Gom nhóm tổng liều xuất theo điểm tiêm tháng 10/2024
-- Expected: DT01 (1500+1000+1000+1200 = 4700), DT03 (2000), DT04 (3000+2500 = 5500)
PRINT '--- Test 2.2d: Gom nhóm tổng liều xuất T10/2024 ---';
SELECT PX.MADT, SUM(CT.SOLIEUXUAT) AS TONGLIEU
FROM PHIEUXUAT PX
INNER JOIN CTPX CT ON PX.MAPX = CT.MAPX
WHERE PX.NGAYXUAT >= '2024-10-01' AND PX.NGAYXUAT <= '2024-10-31'
GROUP BY PX.MADT;

-- Câu 2.2e: Phép chia - Điểm tiêm nhận TẤT CẢ các lô của Moderna (LO05, LO06)
-- Expected: Duy nhất DT01 (nhận cả LO05 và LO06). DT04 nhận LO05, LO06 qua 2 phiếu khác nhau nên cũng nhận đủ!
PRINT '--- Test 2.2e: Phép chia Moderna ---';
SELECT DT.MADT, DT.TENDT
FROM DIEMTIEM DT
WHERE NOT EXISTS (
    SELECT LV.MALO
    FROM LOVACXIN LV
    INNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC
    WHERE NCC.TENNCC = 'Moderna'
    EXCEPT
    SELECT CT.MALO
    FROM PHIEUXUAT PX
    INNER JOIN CTPX CT ON PX.MAPX = CT.MAPX
    WHERE PX.MADT = DT.MADT
);

-- Câu 2.2f: Điểm tiêm có sức chứa lớn nhất tại Thủ Đức
-- Expected: DT04 (Sức chứa 2500 > DT05: 1800 > DT03: 800)
PRINT '--- Test 2.2f: Cực trị MAX sức chứa Thủ Đức ---';
SELECT MADT, TENDT
FROM DIEMTIEM
WHERE QUAN = N'Thủ Đức'
  AND SUCCHUA = (SELECT MAX(SUCCHUA) FROM DIEMTIEM WHERE QUAN = N'Thủ Đức');
