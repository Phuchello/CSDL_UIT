#!/usr/bin/env python3
"""
scripts/seed_pilot.py
Seeds Gate P1 Gold Standard Pilot dataset:
- problems.json (16 representative problems across 4 topics)
- mocks.json (Mock-01 specification)
- mocks/mock_01/exam.md (Student exam paper - zero leaks)
- mocks/mock_01/solution.md (Comprehensive pedagogical solutions, rubrics, edge cases)
"""

import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
GK_DIR = REPO_ROOT / "exam" / "gk"
DATA_DIR = GK_DIR / "data"
MOCKS_DIR = GK_DIR / "mocks" / "mock_01"

MOCKS_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# 1. Pilot Problem Catalog
# -------------------------------------------------------------
problems = [
    # MOCK-01 QUESTIONS (8 sub-problems)
    {
        "id": "M01-Q1",
        "topic": "ERD_MAPPING",
        "difficulty": "B",
        "title": "Thiết kế ERD & Ánh xạ CSDL Quản lý Tiêm Chủng Vắc-Xin",
        "prompt": "Thiết kế mô hình Thực thể – Mối kết hợp (ERD) và chuyển sang Lược đồ quan hệ cho Hệ thống Quản lý Tiêm Chủng Vắc-Xin tại các Trung tâm Y tế. Bối cảnh gồm TTYT, LO_VACXIN, NHACUNGCAP, DIEMTIEM, NHANVIEN, và Đợt phân phối PHANPHOI.",
        "schema": "ERD: TTYT, LOVACXIN, NHACC, DIEMTIEM, NHANVIEN, PHANPHOI",
        "recommended_time_mins": 25,
        "points": 2.5,
        "solution": {
            "erd_entities": [
                {"name": "TRUNGTAM_YTE", "pk": "MaTT", "attributes": ["MaTT", "TenTT", "DiaChiQuan"]},
                {"name": "NHA_CUNGCAP", "pk": "MaNCC", "attributes": ["MaNCC", "TenNCC", "QuocGia", "SDT"]},
                {"name": "LO_VACXIN", "pk": "MaLo", "attributes": ["MaLo", "TenLo", "TenVacxin", "NgaySX", "HSD", "SoLieuNhap", "DonGia"]},
                {"name": "DIEM_TIEM", "pk": "MaDT", "attributes": ["MaDT", "TenDT", "DiaDiem", "SucChua"]},
                {"name": "NHAN_VIEN", "pk": "MaNV", "attributes": ["MaNV", "HoTen", "ChuyenMon", "SDT"]}
            ],
            "relationships": [
                {"name": "CUNG_CAP", "entities": ["NHA_CUNGCAP", "LO_VACXIN"], "cardinality": "1:N", "min_max": "NHA_CUNGCAP (1, N) - (1, 1) LO_VACXIN"},
                {"name": "QUAN_LY_DIEMTIEM", "entities": ["TRUNGTAM_YTE", "DIEM_TIEM"], "cardinality": "1:N", "min_max": "TRUNGTAM_YTE (1, N) - (1, 1) DIEM_TIEM"},
                {"name": "CONG_TAC", "entities": ["TRUNGTAM_YTE", "NHAN_VIEN"], "cardinality": "1:N", "min_max": "TRUNGTAM_YTE (1, N) - (1, 1) NHAN_VIEN"},
                {"name": "PHAN_PHOI", "entities": ["LO_VACXIN", "DIEM_TIEM"], "cardinality": "M:N", "attributes": ["NgayPP", "SoLieuPP", "TrangThai"], "min_max": "LO_VACXIN (0, N) - (1, N) DIEM_TIEM"},
                {"name": "TRUC_CA", "entities": ["NHAN_VIEN", "DIEM_TIEM"], "cardinality": "M:N", "attributes": ["NgayTruc", "VaiTroTruc"], "min_max": "NHAN_VIEN (0, N) - (1, N) DIEM_TIEM"}
            ],
            "relational_schema": [
                "TRUNGTAM_YTE (MaTT, TenTT, DiaChiQuan) - PK: MaTT",
                "NHA_CUNGCAP (MaNCC, TenNCC, QuocGia, SDT) - PK: MaNCC",
                "LO_VACXIN (MaLo, TenLo, TenVacxin, NgaySX, HSD, SoLieuNhap, DonGia, MaNCC) - PK: MaLo, FK: MaNCC -> NHA_CUNGCAP(MaNCC)",
                "DIEM_TIEM (MaDT, TenDT, DiaDiem, SucChua, MaTT) - PK: MaDT, FK: MaTT -> TRUNGTAM_YTE(MaTT)",
                "NHAN_VIEN (MaNV, HoTen, ChuyenMon, SDT, MaTT) - PK: MaNV, FK: MaTT -> TRUNGTAM_YTE(MaTT)",
                "PHAN_PHOI (MaLo, MaDT, NgayPP, SoLieuPP, TrangThai) - PK: (MaLo, MaDT, NgayPP), FK: MaLo -> LO_VACXIN(MaLo), MaDT -> DIEM_TIEM(MaDT)",
                "TRUC_CA (MaNV, MaDT, NgayTruc, VaiTroTruc) - PK: (MaNV, MaDT, NgayTruc), FK: MaNV -> NHAN_VIEN(MaNV), MaDT -> DIEM_TIEM(MaDT)"
            ],
            "intermediate_steps": [
                "Bước 1: Liệt kê thực thể và thuộc tính nhận diện từ văn bản.",
                "Bước 2: Xác định bản số min-max dựa trên từ khóa: 'mỗi lô do duy nhất 1 NCC' -> (1,1); 'một NCC cung cấp nhiều lô' -> (1,N).",
                "Bước 3: Chuyển đổi mối kết hợp 1:N bằng cách mang PK phía 1 sang làm FK phía N.",
                "Bước 4: Chuyển đổi mối kết hợp M:N (PHAN_PHOI, TRUC_CA) thành bảng riêng với khóa chính là tổ hợp PK hai phía kèm thuộc tính phân biệt thời gian."
            ]
        },
        "rubric": {
            "erd_entities": "0.75đ (Xác định đúng 5 thực thể và khóa chính)",
            "erd_relationships_cardinality": "0.75đ (Vẽ đúng mối kết hợp và bản số min-max hai phía)",
            "mapping_pk_fk": "1.00đ (Chuyển đổi đúng quan hệ, gạch chân PK và xác định rõ FK)"
        }
    },
    {
        "id": "M01-Q2A",
        "topic": "SQL_DDL_DML",
        "difficulty": "A",
        "title": "Tạo Ràng Buộc CHECK Miền Giá Trị Trên CTPX và PHIEUXUAT",
        "prompt": "Tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra thuộc tính SOLIEUXUAT trong CTPX phải là số nguyên dương (> 0), và thuộc tính TRANGTHAI trong PHIEUXUAT chỉ nhận một trong hai giá trị là 0 hoặc 1.",
        "schema": "CTPX(MAPX, MALO, SOLIEUXUAT), PHIEUXUAT(MAPX, NGAYXUAT, MADT, TRANGTHAI)",
        "recommended_time_mins": 5,
        "points": 0.75,
        "solution": {
            "sql": "ALTER TABLE CTPX ADD CONSTRAINT CK_CTPX_SOLIEUXUAT CHECK (SOLIEUXUAT > 0);\n\nALTER TABLE PHIEUXUAT ADD CONSTRAINT CK_PHIEUXUAT_TRANGTHAI CHECK (TRANGTHAI IN (0, 1));",
            "intermediate_steps": [
                "Xác định bảng cần áp dụng: CTPX và PHIEUXUAT.",
                "Dùng cú pháp ALTER TABLE ... ADD CONSTRAINT ... CHECK (...).",
                "Điều kiện miền giá trị: SOLIEUXUAT > 0 và TRANGTHAI IN (0, 1)."
            ]
        },
        "rubric": {
            "syntax_alter_table": "0.25đ",
            "check_solieuxuat": "0.25đ",
            "check_trangthai": "0.25đ"
        }
    },
    {
        "id": "M01-Q2B",
        "topic": "SQL_DDL_DML",
        "difficulty": "B",
        "title": "Cập Nhật Tăng Đơn Giá Vắc-Xin Theo HSD Và Nhà Cung Cấp",
        "prompt": "Viết câu lệnh SQL cập nhật (UPDATE) tăng giá đơn vị (DONGIA) thêm 10% đối với các lô vắc-xin có hạn sử dụng (HSD) trong năm 2025 do nhà cung cấp có tên là 'AstraZeneca' cung cấp.",
        "schema": "LOVACXIN(MALO, TENLO, TENKVACXIN, MANCC, NGAYSX, HSD, SOLIEU, DONGIA), NHACUNGCAP(MANCC, TENNCC, QUOCGIA, SDT)",
        "recommended_time_mins": 6,
        "points": 0.75,
        "solution": {
            "sql": "UPDATE LOVACXIN\nSET DONGIA = DONGIA * 1.1\nFROM LOVACXIN LV\nINNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC\nWHERE YEAR(LV.HSD) = 2025 AND NCC.TENNCC = 'AstraZeneca';",
            "intermediate_steps": [
                "Phép tính: Tăng 10% tức DONGIA = DONGIA * 1.1 (hoặc DONGIA + DONGIA * 0.1).",
                "Điều kiện lọc: YEAR(HSD) = 2025 và TENNCC = 'AstraZeneca'.",
                "Dùng cú pháp T-SQL UPDATE ... FROM ... INNER JOIN để liên kết bảng an toàn."
            ]
        },
        "rubric": {
            "update_set_calculation": "0.25đ",
            "join_condition": "0.25đ",
            "where_filtering": "0.25đ"
        }
    },
    {
        "id": "M01-Q2C1",
        "topic": "RA_BASIC_JOIN",
        "difficulty": "A",
        "title": "ĐSQH Lọc Lô Vắc-Xin Theo Tên Và Năm Sản Xuất",
        "prompt": "Liệt kê thông tin các lô vắc-xin (MALO, TENLO, SOLIEU, DONGIA) có tên vắc-xin là 'Pfizer-BioNTech' và được sản xuất trong năm 2024.",
        "schema": "LOVACXIN(MALO, TENLO, TENKVACXIN, MANCC, NGAYSX, HSD, SOLIEU, DONGIA)",
        "recommended_time_mins": 5,
        "points": 1.0,
        "solution": {
            "relational_algebra": "R1 ← σ_{TENKVACXIN = 'Pfizer-BioNTech' ∧ NGAYSX ≥ '01/01/2024' ∧ NGAYSX ≤ '31/12/2024'}(LOVACXIN)\nKQ ← π_{MALO, TENLO, SOLIEU, DONGIA}(R1)",
            "intermediate_steps": [
                "Bước 1: Phép chọn σ trên quan hệ LOVACXIN với điều kiện kép TENKVACXIN = 'Pfizer-BioNTech' và năm sản xuất 2024.",
                "Bước 2: Phép chiếu π lấy đúng 4 thuộc tính yêu cầu: MALO, TENLO, SOLIEU, DONGIA."
            ],
            "sql": "SELECT MALO, TENLO, SOLIEU, DONGIA\nFROM LOVACXIN\nWHERE TENKVACXIN = 'Pfizer-BioNTech' AND YEAR(NGAYSX) = 2024;"
        },
        "rubric": {
            "selection_condition": "0.50đ (Đúng điều kiện chuỗi và ngày tháng)",
            "projection_attributes": "0.50đ (Đúng tập thuộc tính đầu ra)"
        }
    },
    {
        "id": "M01-Q2C2",
        "topic": "RA_BASIC_JOIN",
        "difficulty": "B",
        "title": "ĐSQH Kết Nối Điểm Tiêm Nhận Phiếu Xuất Ngày 15/10/2024",
        "prompt": "Cho biết danh sách các điểm tiêm (MADT, TENDT, QUAN) đã tiếp nhận các phiếu xuất vắc-xin vào ngày '15/10/2024'.",
        "schema": "DIEMTIEM(MADT, TENDT, QUAN, SUCCHUA, MATRP), PHIEUXUAT(MAPX, NGAYXUAT, MADT, TRANGTHAI)",
        "recommended_time_mins": 6,
        "points": 1.0,
        "solution": {
            "relational_algebra": "R1 ← σ_{NGAYXUAT = '15/10/2024'}(PHIEUXUAT)\nR2 ← DIEMTIEM ⋈_{DIEMTIEM.MADT = R1.MADT} R1\nKQ ← π_{MADT, TENDT, QUAN}(R2)",
            "intermediate_steps": [
                "Bước 1: Lọc các phiếu xuất có NGAYXUAT = '15/10/2024' thành R1.",
                "Bước 2: Kết tự nhiên hoặc kết bằng giữa DIEMTIEM và R1 qua khóa ngoại MADT.",
                "Bước 3: Chiếu lấy các thuộc tính định danh điểm tiêm: MADT, TENDT, QUAN."
            ],
            "sql": "SELECT DISTINCT DT.MADT, DT.TENDT, DT.QUAN\nFROM DIEMTIEM DT\nINNER JOIN PHIEUXUAT PX ON DT.MADT = PX.MADT\nWHERE PX.NGAYXUAT = '2024-10-15';"
        },
        "rubric": {
            "selection_filter": "0.25đ",
            "join_operation": "0.50đ",
            "projection": "0.25đ"
        }
    },
    {
        "id": "M01-Q2C3",
        "topic": "RA_BASIC_JOIN",
        "difficulty": "B",
        "title": "ĐSQH Kết Ngoài Phụ Trách Điểm Tiêm Quận Bình Thạnh (Nếu Có)",
        "prompt": "Liệt kê thông tin các điểm tiêm ở quận 'Bình Thạnh' (MADT, TENDT) và họ tên bác sĩ (HOTEN) đang phụ trách tại điểm tiêm đó nếu có.",
        "schema": "DIEMTIEM(MADT, TENDT, QUAN, SUCCHUA, MATRP), BACSI(MABS, HOTEN, CHUYENKHOA, SDT, MADT)",
        "recommended_time_mins": 7,
        "points": 1.0,
        "solution": {
            "relational_algebra": "R1 ← σ_{QUAN = 'Bình Thạnh'}(DIEMTIEM)\nR2 ← R1 ⟕_{R1.MADT = BACSI.MADT} BACSI\nKQ ← π_{MADT, TENDT, HOTEN}(R2)",
            "intermediate_steps": [
                "Bước 1: Lọc điểm tiêm ở quận Bình Thạnh thành R1.",
                "Bước 2: Nhận diện từ khóa 'NẾU CÓ' -> Phải dùng Phép Kết Ngoài Trái (Left Outer Join ⟕) từ R1 sang BACSI để không làm mất các điểm tiêm chưa có bác sĩ trực.",
                "Bước 3: Chiếu lấy MADT, TENDT, HOTEN."
            ],
            "sql": "SELECT DT.MADT, DT.TENDT, BS.HOTEN\nFROM DIEMTIEM DT\nLEFT OUTER JOIN BACSI BS ON DT.MADT = BS.MADT\nWHERE DT.QUAN = N'Bình Thạnh';"
        },
        "rubric": {
            "outer_join_recognition": "0.50đ (Bắt buộc dùng ⟕ hoặc phân tích trường hợp NULL)",
            "selection_and_projection": "0.50đ"
        }
    },
    {
        "id": "M01-Q2C4",
        "topic": "RA_DIVISION_GROUPING",
        "difficulty": "B",
        "title": "ĐSQH Gom Nhóm Tính Tổng Liều Vắc-Xin Xuất Theo Điểm Tiêm",
        "prompt": "Tính tổng số liều vắc-xin xuất (SOLIEUXUAT) theo từng điểm tiêm (MADT) trong tháng 10 năm 2024. Thông tin hiển thị gồm: MADT, TONGLIEU.",
        "schema": "PHIEUXUAT(MAPX, NGAYXUAT, MADT, TRANGTHAI), CTPX(MAPX, MALO, SOLIEUXUAT)",
        "recommended_time_mins": 7,
        "points": 1.0,
        "solution": {
            "relational_algebra": "R1 ← σ_{NGAYXUAT ≥ '01/10/2024' ∧ NGAYXUAT ≤ '31/10/2024'}(PHIEUXUAT)\nR2 ← R1 ⋈_{R1.MAPX = CTPX.MAPX} CTPX\nKQ ← _{MADT} γ _{SUM(SOLIEUXUAT) → TONGLIEU}(R2)",
            "intermediate_steps": [
                "Bước 1: Lọc phiếu xuất phát sinh trong tháng 10/2024 thành R1.",
                "Bước 2: Kết nối R1 với CTPX qua MAPX để lấy số liều xuất.",
                "Bước 3: Thực hiện phép gom nhóm γ theo thuộc tính MADT, tính hàm tổng SUM(SOLIEUXUAT) và đổi tên thành TONGLIEU."
            ],
            "sql": "SELECT PX.MADT, SUM(CT.SOLIEUXUAT) AS TONGLIEU\nFROM PHIEUXUAT PX\nINNER JOIN CTPX CT ON PX.MAPX = CT.MAPX\nWHERE MONTH(PX.NGAYXUAT) = 10 AND YEAR(PX.NGAYXUAT) = 2024\nGROUP BY PX.MADT;"
        },
        "rubric": {
            "time_filter_and_join": "0.50đ",
            "grouping_gamma_aggregate": "0.50đ (Đúng thuộc tính gom nhóm và hàm SUM)"
        }
    },
    {
        "id": "M01-Q2C5",
        "topic": "RA_DIVISION_GROUPING",
        "difficulty": "C",
        "title": "ĐSQH Phép Chia Tìm Điểm Tiêm Nhận Tất Cả Lô Vắc-Xin Của Moderna",
        "prompt": "Tìm các điểm tiêm (MADT, TENDT) đã tiếp nhận tất cả các lô vắc-xin của nhà cung cấp có tên là 'Moderna' (TENNCC = 'Moderna').",
        "schema": "NHACUNGCAP(MANCC, TENNCC, QUOCGIA, SDT), LOVACXIN(MALO, TENLO, TENKVACXIN, MANCC, NGAYSX, HSD, SOLIEU, DONGIA), DIEMTIEM(MADT, TENDT, QUAN, SUCCHUA, MATRP), PHIEUXUAT(MAPX, NGAYXUAT, MADT, TRANGTHAI), CTPX(MAPX, MALO, SOLIEUXUAT)",
        "recommended_time_mins": 9,
        "points": 1.0,
        "solution": {
            "relational_algebra": "R_Moderna ← π_{MALO}(σ_{TENNCC = 'Moderna'}(NHACUNGCAP ⋈ LOVACXIN))\nR_DiemTiem_Lo ← π_{MADT, MALO}(DIEMTIEM ⋈ PHIEUXUAT ⋈ CTPX)\nR_Chia ← R_DiemTiem_Lo ÷ R_Moderna\nKQ ← π_{MADT, TENDT}(R_Chia ⋈ DIEMTIEM)",
            "intermediate_steps": [
                "Bước 1: Xác định tập mục tiêu (tập bị chia) R_Moderna: Chiếu lấy danh sách MALO thuộc nhà cung cấp 'Moderna'.",
                "Bước 2: Xác định quan hệ tham gia R_DiemTiem_Lo: Chiếu lấy các cặp (MADT, MALO) thực tế đã xuất vắc-xin đến điểm tiêm.",
                "Bước 3: Thực hiện phép chia hình thức R_Chia = R_DiemTiem_Lo ÷ R_Moderna. Kết quả trả về các MADT nhận đủ mọi MALO của Moderna.",
                "Bước 4: Kết nối ngược với DIEMTIEM để lấy TENDT."
            ],
            "sql": "SELECT DT.MADT, DT.TENDT\nFROM DIEMTIEM DT\nWHERE NOT EXISTS (\n    SELECT LV.MALO\n    FROM LOVACXIN LV\n    INNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC\n    WHERE NCC.TENNCC = 'Moderna'\n    EXCEPT\n    SELECT CT.MALO\n    FROM PHIEUXUAT PX\n    INNER JOIN CTPX CT ON PX.MAPX = CT.MAPX\n    WHERE PX.MADT = DT.MADT\n);"
        },
        "rubric": {
            "target_set_construction": "0.25đ",
            "candidate_relation_projection": "0.25đ",
            "division_operation": "0.50đ (Đúng bản chất toán học của phép chia)"
        }
    },
    {
        "id": "M01-Q2C6",
        "topic": "RA_DIVISION_GROUPING",
        "difficulty": "C",
        "title": "ĐSQH Tìm Điểm Tiêm Có Sức Chứa Lớn Nhất Tại Quận Thủ Đức",
        "prompt": "Cho biết điểm tiêm nào (MADT, TENDT) có sức chứa (SUCCHUA) lớn nhất trong số các điểm tiêm thuộc quận 'Thủ Đức'.",
        "schema": "DIEMTIEM(MADT, TENDT, QUAN, SUCCHUA, MATRP)",
        "recommended_time_mins": 8,
        "points": 1.0,
        "solution": {
            "relational_algebra": "R1 ← σ_{QUAN = 'Thủ Đức'}(DIEMTIEM)\nR2 ← ρ_{DT1}(R1)\nR3 ← ρ_{DT2}(R1)\nR_KhongLonNhat ← π_{DT1.MADT}(R2 ⋈_{DT1.SUCCHUA < DT2.SUCCHUA} R3)\nR_LonNhat ← π_{MADT}(R1) - R_KhongLonNhat\nKQ ← π_{MADT, TENDT}(R_LonNhat ⋈ R1)",
            "intermediate_steps": [
                "Bước 1: Lọc các điểm tiêm thuộc quận 'Thủ Đức' thành R1.",
                "Bước 2: Phép tìm cực trị MAX trong ĐSQH bằng phương pháp loại trừ: Tự kết R1 với chính nó qua điều kiện SUCCHUA1 < SUCCHUA2.",
                "Bước 3: Chiếu lấy DT1.MADT; đây là tập các điểm tiêm KHÔNG phải lớn nhất vì tồn tại điểm tiêm khác có sức chứa lớn hơn nó.",
                "Bước 4: Lấy toàn bộ MADT của Thủ Đức trừ đi tập R_KhongLonNhat, thu được điểm tiêm có sức chứa lớn nhất (có thể có đồng hạng)."
            ],
            "sql": "SELECT MADT, TENDT\nFROM DIEMTIEM\nWHERE QUAN = N'Thủ Đức'\n  AND SUCCHUA = (SELECT MAX(SUCCHUA) FROM DIEMTIEM WHERE QUAN = N'Thủ Đức');"
        },
        "rubric": {
            "subquery_or_self_join": "0.50đ",
            "subtraction_or_max_logic": "0.50đ"
        }
    },

    # 7 ADDITIONAL REPRESENTATIVE BANK PROBLEMS (TOTAL = 16 PILOT PROBLEMS)
    {
        "id": "ERD-002",
        "topic": "ERD_MAPPING",
        "difficulty": "B",
        "title": "Thiết Kế ERD Hệ Thống Phòng Cháy Chữa Cháy Chung Cư (Authentic 2023–2024)",
        "prompt": "Vẽ mô hình ERD và ánh xạ Lược đồ quan hệ quản lý PCCC: Khu chung cư có nhiều tòa nhà; mỗi tòa nhà có nhiều tầng. Mỗi tầng có mã số duy nhất, tên tầng, số căn hộ. Thiết bị PCCC có tên loại, mô tả. Đợt kiểm tra ghi nhận tình trạng hoạt động.",
        "schema": "ERD: TOANHA, TANG, LOAI_DUNG_CU, DOT_KIEM_TRA, CAN_HO",
        "recommended_time_mins": 25,
        "points": 2.5,
        "solution": {
            "erd_entities": [
                {"name": "TOA_NHA", "pk": "MaToa", "attributes": ["MaToa", "TenToa", "SoTang"]},
                {"name": "TANG", "pk": "MaTang", "attributes": ["MaTang", "TenTang", "SoCanHo"]},
                {"name": "LOAI_THIETBI", "pk": "MaLoai", "attributes": ["MaLoai", "TenLoai", "MoTa"]},
                {"name": "THIET_BI", "pk": "MaTB", "attributes": ["MaTB", "ViTriLapDat", "NgayTrangBi"]}
            ],
            "relationships": [
                {"name": "THUOC_TOA", "entities": ["TOA_NHA", "TANG"], "cardinality": "1:N", "min_max": "TOA_NHA (1, N) - (1, 1) TANG"},
                {"name": "PHAN_LOAI", "entities": ["LOAI_THIETBI", "THIET_BI"], "cardinality": "1:N", "min_max": "LOAI_THIETBI (1, N) - (1, 1) THIET_BI"},
                {"name": "LAP_DAT", "entities": ["TANG", "THIET_BI"], "cardinality": "1:N", "min_max": "TANG (0, N) - (1, 1) THIET_BI"}
            ],
            "relational_schema": [
                "TOA_NHA (MaToa, TenToa, SoTang) - PK: MaToa",
                "TANG (MaTang, TenTang, SoCanHo, MaToa) - PK: MaTang, FK: MaToa -> TOA_NHA(MaToa)",
                "LOAI_THIETBI (MaLoai, TenLoai, MoTa) - PK: MaLoai",
                "THIET_BI (MaTB, ViTriLapDat, NgayTrangBi, MaLoai, MaTang) - PK: MaTB, FK: MaLoai -> LOAI_THIETBI, MaTang -> TANG"
            ],
            "intermediate_steps": ["Xác định thực thể yếu/mạnh", "Bản số min-max", "Chuyển đổi quan hệ 1:N bằng FK."]
        },
        "rubric": {"erd": "1.50đ", "mapping": "1.00đ"}
    },
    {
        "id": "ERD-003",
        "topic": "ERD_MAPPING",
        "difficulty": "B",
        "title": "Thiết Kế ERD Quản Lý Cứu Trợ Thiên Tai & Bão Lũ (Authentic 2024–2025)",
        "prompt": "Thiết kế mô hình ERD quản lý cứu trợ bão lũ: Ghi nhận thông tin hộ dân thiệt hại theo địa bàn thôn/xã, các đợt cứu trợ và các khoản đóng góp ủng hộ của nhà hảo tâm.",
        "schema": "ERD: XA, HO_DAN, DOT_CUUTRO, NHA_HAOTAM, PHIEU_NHAN",
        "recommended_time_mins": 25,
        "points": 2.0,
        "solution": {
            "erd_entities": [
                {"name": "XA", "pk": "MaXa", "attributes": ["MaXa", "TenXa", "Huyen"]},
                {"name": "HO_DAN", "pk": "MaHo", "attributes": ["MaHo", "ChuHo", "SoNhanKhau", "MucDoThietHai"]},
                {"name": "NHA_HAOTAM", "pk": "MaNHT", "attributes": ["MaNHT", "TenNHT", "SDT", "LoaiHinh"]},
                {"name": "DOT_CUUTRO", "pk": "MaDot", "attributes": ["MaDot", "TenDot", "NgayBatDau"]}
            ],
            "relationships": [
                {"name": "TRUC_THUOC", "entities": ["XA", "HO_DAN"], "cardinality": "1:N", "min_max": "XA (1, N) - (1, 1) HO_DAN"},
                {"name": "DONG_GOP", "entities": ["NHA_HAOTAM", "DOT_CUUTRO"], "cardinality": "M:N", "attributes": ["SoTien", "NgayDongGop"], "min_max": "NHA_HAOTAM (1, N) - (1, N) DOT_CUUTRO"}
            ],
            "relational_schema": [
                "XA (MaXa, TenXa, Huyen) - PK: MaXa",
                "HO_DAN (MaHo, ChuHo, SoNhanKhau, MucDoThietHai, MaXa) - PK: MaHo, FK: MaXa -> XA(MaXa)",
                "NHA_HAOTAM (MaNHT, TenNHT, SDT, LoaiHinh) - PK: MaNHT",
                "DOT_CUUTRO (MaDot, TenDot, NgayBatDau) - PK: MaDot",
                "DONG_GOP (MaNHT, MaDot, NgayDongGop, SoTien) - PK: (MaNHT, MaDot, NgayDongGop), FK: MaNHT -> NHA_HAOTAM, MaDot -> DOT_CUUTRO"
            ],
            "intermediate_steps": ["Xác định thuộc tính", "Bản số min-max", "Ánh xạ bảng trung gian M:N."]
        },
        "rubric": {"erd": "1.25đ", "mapping": "0.75đ"}
    },
    {
        "id": "RA-B03",
        "topic": "RA_BASIC_JOIN",
        "difficulty": "B",
        "title": "ĐSQH Tự Kết Nối Phân Cấp Nhân Viên Và Người Quản Lý",
        "prompt": "Cho lược đồ NHANVIEN(MANV, HOTEN, PHAI, NGSINH, MA_NQL). Liệt kê mã số và họ tên của nhân viên cùng họ tên của người quản lý trực tiếp của nhân viên đó.",
        "schema": "NHANVIEN(MANV, HOTEN, PHAI, NGSINH, MA_NQL)",
        "recommended_time_mins": 6,
        "points": 1.0,
        "solution": {
            "relational_algebra": "NV1 ← ρ_{NV}(NHANVIEN)\nNV2 ← ρ_{QL}(NHANVIEN)\nR ← NV1 ⋈_{NV.MA_NQL = QL.MANV} NV2\nKQ ← π_{NV.MANV, NV.HOTEN, QL.HOTEN → TEN_QUANLY}(R)",
            "intermediate_steps": [
                "Bước 1: Đổi tên hai bản sao của quan hệ NHANVIEN thành NV và QL để tránh xung đột thuộc tính.",
                "Bước 2: Tự kết (Self-Join) qua điều kiện NV.MA_NQL = QL.MANV.",
                "Bước 3: Chiếu lấy MANV, HOTEN của nhân viên và HOTEN của người quản lý."
            ],
            "sql": "SELECT NV.MANV, NV.HOTEN, QL.HOTEN AS TEN_QUANLY\nFROM NHANVIEN NV\nINNER JOIN NHANVIEN QL ON NV.MA_NQL = QL.MANV;"
        },
        "rubric": {"rename_operation": "0.50đ", "self_join_and_projection": "0.50đ"}
    },
    {
        "id": "RA-B04",
        "topic": "RA_BASIC_JOIN",
        "difficulty": "B",
        "title": "ĐSQH Phép Giao Khách Hàng Mở Cả Hai Loại Tài Khoản",
        "prompt": "Cho CSDL Ngân hàng: Liệt kê khách hàng (MAKH, HOTEN) đã mở cả hai loại tài khoản: 'Tiết kiệm' và 'Thanh toán'.",
        "schema": "KHACHHANG(MAKH, HOTEN), TAIKHOAN(SOTK, MAKH, MALTK), LOAITK(MALTK, TENLTK)",
        "recommended_time_mins": 7,
        "points": 1.0,
        "solution": {
            "relational_algebra": "R_TK ← π_{MAKH, HOTEN}(KHACHHANG ⋈ TAIKHOAN ⋈ σ_{TENLTK = 'Tiết kiệm'}(LOAITK))\nR_TT ← π_{MAKH, HOTEN}(KHACHHANG ⋈ TAIKHOAN ⋈ σ_{TENLTK = 'Thanh toán'}(LOAITK))\nKQ ← R_TK ∩ R_TT",
            "intermediate_steps": [
                "Bước 1: Tìm danh sách khách hàng mở tài khoản Tiết kiệm.",
                "Bước 2: Tìm danh sách khách hàng mở tài khoản Thanh toán.",
                "Bước 3: Dùng phép giao ∩ giữa hai tập có cùng lược đồ thuộc tính (MAKH, HOTEN)."
            ],
            "sql": "SELECT KH.MAKH, KH.HOTEN\nFROM KHACHHANG KH\nINNER JOIN TAIKHOAN TK ON KH.MAKH = TK.MAKH\nINNER JOIN LOAITK LTK ON TK.MALTK = LTK.MALTK\nWHERE LTK.TENLTK = N'Tiết kiệm'\nINTERSECT\nSELECT KH.MAKH, KH.HOTEN\nFROM KHACHHANG KH\nINNER JOIN TAIKHOAN TK ON KH.MAKH = TK.MAKH\nINNER JOIN LOAITK LTK ON TK.MALTK = LTK.MALTK\nWHERE LTK.TENLTK = N'Thanh toán';"
        },
        "rubric": {"intersect_operands": "0.50đ", "set_intersection": "0.50đ"}
    },
    {
        "id": "RA-D01",
        "topic": "RA_DIVISION_GROUPING",
        "difficulty": "C",
        "title": "ĐSQH Phép Chia Đơn Đặt Hàng Đặt Tất Cả Mặt Hàng Của 'Vinamilk'",
        "prompt": "Tìm các đơn đặt hàng (MADH) đã đặt tất cả các mặt hàng do nhà cung cấp có tên là 'Vinamilk' cung cấp.",
        "schema": "DONDH(MADH, NGAYDH, MACC), CHITIET(MADH, MAMH, SOLUONG), CUNGCAP(MACC, MAMH), NHACC(MACC, TENCC)",
        "recommended_time_mins": 9,
        "points": 1.0,
        "solution": {
            "relational_algebra": "R_Vinamilk ← π_{MAMH}(σ_{TENCC = 'Vinamilk'}(NHACC ⋈ CUNGCAP))\nR_DH_MH ← π_{MADH, MAMH}(CHITIET)\nKQ ← R_DH_MH ÷ R_Vinamilk",
            "intermediate_steps": [
                "Bước 1: Tập chia R_Vinamilk là danh sách MAMH của NCC 'Vinamilk'.",
                "Bước 2: Tập bị chia R_DH_MH là các cặp (MADH, MAMH) trong CHITIET.",
                "Bước 3: Phép chia R_DH_MH ÷ R_Vinamilk cho ra MADH thỏa mãn."
            ],
            "sql": "SELECT DH.MADH\nFROM DONDH DH\nWHERE NOT EXISTS (\n    SELECT CC.MAMH\n    FROM CUNGCAP CC\n    INNER JOIN NHACC NC ON CC.MACC = NC.MACC\n    WHERE NC.TENCC = 'Vinamilk'\n    EXCEPT\n    SELECT CT.MAMH\n    FROM CHITIET CT\n    WHERE CT.MADH = DH.MADH\n);"
        },
        "rubric": {"division_algebra": "0.50đ", "equivalence_proof": "0.50đ"}
    },
    {
        "id": "RA-D03",
        "topic": "RA_DIVISION_GROUPING",
        "difficulty": "B",
        "title": "ĐSQH Gom Nhóm Doanh Thu Từng Sảnh Nhà Hàng White Palace",
        "prompt": "Cho CSDL Nhà hàng: Tính tổng doanh thu theo từng sảnh tiệc. Thông tin hiển thị gồm: MASANH, TENSANH, DOANHTHU.",
        "schema": "SANH(MASANH, TENSANH, LOAIBAN, SUCCHUA), TIEC(MATIEC, MASANH, CHUTIEC, SOBAN, DONGIA)",
        "recommended_time_mins": 7,
        "points": 1.0,
        "solution": {
            "relational_algebra": "R1 ← SANH ⋈ TIEC\nKQ ← _{MASANH, TENSANH} γ _{SUM(SOBAN * DONGIA) → DOANHTHU}(R1)",
            "intermediate_steps": [
                "Bước 1: Kết nối sảnh với các tiệc được tổ chức tại sảnh.",
                "Bước 2: Gom nhóm theo MASANH, TENSANH và tính SUM(SOBAN * DONGIA)."
            ],
            "sql": "SELECT S.MASANH, S.TENSANH, SUM(T.SOBAN * T.DONGIA) AS DOANHTHU\nFROM SANH S\nINNER JOIN TIEC T ON S.MASANH = T.MASANH\nGROUP BY S.MASANH, S.TENSANH;"
        },
        "rubric": {"join_and_grouping": "0.50đ", "expression_calculation": "0.50đ"}
    },
    {
        "id": "SQL-D03",
        "topic": "SQL_DDL_DML",
        "difficulty": "C",
        "title": "Chuyển Đổi Phép Chia ĐSQH Sang Double NOT EXISTS Trong T-SQL",
        "prompt": "Viết câu truy vấn T-SQL bằng kỹ thuật tương quan hai lần lặp Double NOT EXISTS để tìm các khách hàng (MAKH, HOTEN) đã mở tất cả các loại tài khoản.",
        "schema": "KHACHHANG(MAKH, HOTEN), TAIKHOAN(SOTK, MAKH, MALTK), LOAITK(MALTK, TENLTK)",
        "recommended_time_mins": 8,
        "points": 1.0,
        "solution": {
            "sql": "SELECT KH.MAKH, KH.HOTEN\nFROM KHACHHANG KH\nWHERE NOT EXISTS (\n    SELECT *\n    FROM LOAITK LTK\n    WHERE NOT EXISTS (\n        SELECT *\n        FROM TAIKHOAN TK\n        WHERE TK.MAKH = KH.MAKH AND TK.MALTK = LTK.MALTK\n    )\n);",
            "intermediate_steps": [
                "Nguyên lý: 'Không tồn tại loại tài khoản nào mà khách hàng KH đó KHÔNG mở'.",
                "Vòng lặp ngoài duyệt qua từng KHACHHANG.",
                "Vòng lặp giữa duyệt qua từng LOAITK.",
                "Vòng lặp trong kiểm tra sự tồn tại trong TAIKHOAN."
            ]
        },
        "rubric": {"double_not_exists_structure": "0.50đ", "correlation_matching": "0.50đ"}
    }
]

# -------------------------------------------------------------
# 2. Pilot Mock 01 Definition
# -------------------------------------------------------------
mocks = [
    {
        "id": "MOCK-01",
        "title": "Đề Thi Giữa Kỳ Mô Phỏng Số 01 — Quản Lý Cung Ứng & Tiêm Chủng Vắc-Xin",
        "duration_mins": 75,
        "total_points": 10.0,
        "profile": "HISTORICAL_2023_2024",
        "target_skills": ["ERD_DESIGN", "SCHEMA_MAPPING", "SQL_CHECK", "SQL_UPDATE", "RA_SELECT", "RA_JOIN", "RA_OUTER_JOIN", "RA_GROUPING", "RA_DIVISION", "RA_EXTREME"],
        "questions": [
            {"num": "1", "sub": "", "points": 2.5, "problem_id": "M01-Q1"},
            {"num": "2", "sub": "1a", "points": 0.75, "problem_id": "M01-Q2A"},
            {"num": "2", "sub": "1b", "points": 0.75, "problem_id": "M01-Q2B"},
            {"num": "2", "sub": "2a", "points": 1.0, "problem_id": "M01-Q2C1"},
            {"num": "2", "sub": "2b", "points": 1.0, "problem_id": "M01-Q2C2"},
            {"num": "2", "sub": "2c", "points": 1.0, "problem_id": "M01-Q2C3"},
            {"num": "2", "sub": "2d", "points": 1.0, "problem_id": "M01-Q2C4"},
            {"num": "2", "sub": "2e", "points": 1.0, "problem_id": "M01-Q2C5"},
            {"num": "2", "sub": "2f", "points": 1.0, "problem_id": "M01-Q2C6"}
        ]
    }
]

# Write JSON files
with open(DATA_DIR / "problems.json", "w", encoding="utf-8") as f:
    json.dump({"problems": problems}, f, ensure_ascii=False, indent=2)

with open(DATA_DIR / "mocks.json", "w", encoding="utf-8") as f:
    json.dump({"mocks": mocks}, f, ensure_ascii=False, indent=2)

# -------------------------------------------------------------
# 3. Write Mock 01 Student Exam Paper (ZERO SOLUTION LEAK)
# -------------------------------------------------------------
exam_md = """# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 01 (MOCK-01)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)

Để phục vụ công tác tiêm chủng phòng dịch trên địa bàn thành phố, Sở Y tế cần xây dựng cơ sở dữ liệu quản lý việc tiếp nhận và phân phối vắc-xin tại các điểm tiêm chủng, cụ thể như sau:

- Mỗi **Trung tâm Y tế** (`TRUNGTAM_YTE`) có mã trung tâm (`MaTT`) để phân biệt giữa các trung tâm, có tên trung tâm (`TenTT`), và địa chỉ quận/huyện (`DiaChiQuan`).
- Các **Nhà cung cấp** (`NHA_CUNGCAP`) cung ứng vắc-xin cần lưu trữ: mã nhà cung cấp (`MaNCC`), tên nhà cung cấp (`TenNCC`), quốc gia (`QuocGia`), và số điện thoại liên hệ (`SDT`).
- Mỗi **Lô vắc-xin** (`LO_VACXIN`) nhập kho được ghi nhận: mã lô (`MaLo`) duy nhất, tên lô (`TenLo`), tên loại vắc-xin (`TenVacxin`), ngày sản xuất (`NgaySX`), hạn sử dụng (`HSD`), số liều nhập (`SoLieuNhap`), và đơn giá mỗi liều (`DonGia`). Mỗi lô vắc-xin do duy nhất một nhà cung cấp cung ứng; một nhà cung cấp có thể cung cấp nhiều lô vắc-xin khác nhau.
- Các **Điểm tiêm chủng** (`DIEM_TIEM`) trực thuộc một Trung tâm Y tế quản lý gồm các thông tin: mã điểm tiêm (`MaDT`), tên điểm tiêm (`TenDT`), địa điểm cụ thể (`DiaDiem`), và sức chứa tối đa người tiêm trong ngày (`SucChua`). Mỗi điểm tiêm chỉ trực thuộc duy nhất một trung tâm y tế; một trung tâm y tế quản lý nhiều điểm tiêm khác nhau.
- Công tác phân phối vắc-xin từ các lô đến điểm tiêm được thực hiện qua các đợt **Phân phối** (`PHAN_PHOI`). Thông tin lưu trữ gồm: ngày phân phối (`NgayPP`), số liều phân phối (`SoLieuPP`), và trạng thái tiếp nhận (`TrangThai` nhận giá trị 1 nếu đã nhận, 0 nếu đang chuyển). Một lô vắc-xin có thể phân phối cho nhiều điểm tiêm; một điểm tiêm có thể tiếp nhận vắc-xin từ nhiều lô khác nhau vào các ngày khác nhau.
- Mỗi **Nhân viên y tế** (`NHAN_VIEN`) có mã nhân viên (`MaNV`), họ tên (`HoTen`), chuyên môn y tế (`ChuyenMon`), và số điện thoại (`SDT`). Mỗi nhân viên chỉ thuộc biên chế chính thức của một trung tâm y tế. Nhân viên được điều động tham gia trực tại các điểm tiêm trong các ca trực (`TRUC_CA`) cụ thể, ghi nhận ngày trực (`NgayTruc`) và vai trò trực (`VaiTroTruc`).

**Yêu cầu:**
1. Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số $(min, max)$ hai phía. Vẽ mô hình Thực thể – Mối kết hợp (ERD). *(1.5 điểm)*
2. Ánh xạ mô hình ERD trên sang Lược đồ cơ sở dữ liệu quan hệ, chỉ rõ các Khóa chính (gạch chân) và Khóa ngoại (ký hiệu mũi tên hoặc chú thích rõ). *(1.0 điểm)*

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu "Quản lý Cung ứng & Phân phối Vắc-xin" gồm các quan hệ sau (thuộc tính gạch chân là khóa chính):

- `NHACUNGCAP` (**`MANCC`**, `TENNCC`, `QUOCGIA`, `SDT`)
  *Tân từ:* Thông tin nhà cung cấp vắc-xin.
- `LOVACXIN` (**`MALO`**, `TENLO`, `TENKVACXIN`, `MANCC`, `NGAYSX`, `HSD`, `SOLIEU`, `DONGIA`)
  *Tân từ:* Thông tin lô vắc-xin nhập kho. `MANCC` là khóa ngoại trỏ về `NHACUNGCAP`.
- `DIEMTIEM` (**`MADT`**, `TENDT`, `QUAN`, `SUCCHUA`, `MATRP`)
  *Tân từ:* Điểm tiêm chủng lưu động. `MATRP` là mã bác sĩ trưởng điểm tiêm phụ trách.
- `BACSI` (**`MABS`**, `HOTEN`, `CHUYENKHOA`, `SDT`, `MADT`)
  *Tân từ:* Danh sách bác sĩ tham gia tiêm chủng. `MADT` là điểm tiêm bác sĩ đang trực.
- `PHIEUXUAT` (**`MAPX`**, `NGAYXUAT`, `MADT`, `TRANGTHAI`)
  *Tân từ:* Phiếu xuất vắc-xin đến điểm tiêm. `MADT` là khóa ngoại trỏ về `DIEMTIEM`.
- `CTPX` (**`MAPX`**, **`MALO`**, `SOLIEUXUAT`)
  *Tân từ:* Chi tiết số liều xuất theo từng lô vắc-xin trong mỗi phiếu xuất.

### 1. Viết các câu lệnh SQL (1.5 điểm)
a. *(0.75 điểm)* Tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra thuộc tính `SOLIEUXUAT` trong quan hệ `CTPX` phải là số nguyên dương ($> 0$), và thuộc tính `TRANGTHAI` trong quan hệ `PHIEUXUAT` chỉ nhận một trong hai giá trị là `0` hoặc `1`.
b. *(0.75 điểm)* Viết câu lệnh SQL cập nhật (`UPDATE`) tăng giá đơn vị (`DONGIA`) thêm 10% đối với các lô vắc-xin có hạn sử dụng (`HSD`) trong năm 2025 do nhà cung cấp có tên là 'AstraZeneca' cung cấp.

### 2. Viết các biểu thức Đại số quan hệ (6.0 điểm - mỗi câu 1.0 điểm)
a. *(1.0 điểm)* Liệt kê thông tin các lô vắc-xin (`MALO`, `TENLO`, `SOLIEU`, `DONGIA`) có tên vắc-xin là 'Pfizer-BioNTech' và được sản xuất trong năm 2024.
b. *(1.0 điểm)* Cho biết danh sách các điểm tiêm (`MADT`, `TENDT`, `QUAN`) đã tiếp nhận các phiếu xuất vắc-xin vào ngày '15/10/2024'.
c. *(1.0 điểm)* Liệt kê thông tin các điểm tiêm ở quận 'Bình Thạnh' (`MADT`, `TENDT`) và họ tên bác sĩ (`HOTEN`) đang phụ trách tại điểm tiêm đó **nếu có**.
d. *(1.0 điểm)* Tính tổng số liều vắc-xin xuất (`SOLIEUXUAT`) theo từng điểm tiêm (`MADT`) trong tháng 10 năm 2024. Thông tin hiển thị gồm: `MADT`, `TONGLIEU`.
e. *(1.0 điểm)* Tìm các điểm tiêm (`MADT`, `TENDT`) đã tiếp nhận **tất cả** các lô vắc-xin của nhà cung cấp có tên là 'Moderna' (`TENNCC = 'Moderna'`).
f. *(1.0 điểm)* Cho biết điểm tiêm nào (`MADT`, `TENDT`) có sức chứa (`SUCCHUA`) lớn nhất trong số các điểm tiêm thuộc quận 'Thủ Đức'.

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 01**
*Cán bộ coi thi không giải thích gì thêm.*
"""

with open(MOCKS_DIR / "exam.md", "w", encoding="utf-8") as f:
    f.write(exam_md.strip())

# -------------------------------------------------------------
# 4. Write Mock 01 Answer Key & Rubrics
# -------------------------------------------------------------
solution_md = """# HƯỚNG DẪN CHẤM & LỜI GIẢI CHI TIẾT ĐỀ THI MÔ PHỎNG SỐ 01 (MOCK-01)
**Môn học:** IT004 — Cơ sở dữ liệu | **Thời gian thi:** 75 phút | **Thang điểm:** 10.0
**Tác giả biên soạn:** VÕ TRỌNG PHÚC
**Tiêu chuẩn học thuật:** Hợp đồng lời giải chi tiết, phân tích tư duy tự nhiên $\\to$ biểu thức toán $\\to$ T-SQL, barem điểm và bẫy lỗi.

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)

### 1.1. Phân tích ngữ cảnh & Sơ đồ ERD (1.5 điểm)

#### A. Bảng tổng hợp thực thể và thuộc tính
1. `TRUNGTAM_YTE` (Mã TT $\\underline{MaTT}$, TenTT, DiaChiQuan) — Khóa chính: `MaTT`.
2. `NHA_CUNGCAP` (Mã NCC $\\underline{MaNCC}$, TenNCC, QuocGia, SDT) — Khóa chính: `MaNCC`.
3. `LO_VACXIN` (Mã lô $\\underline{MaLo}$, TenLo, TenVacxin, NgaySX, HSD, SoLieuNhap, DonGia) — Khóa chính: `MaLo`.
4. `DIEM_TIEM` (Mã ĐT $\\underline{MaDT}$, TenDT, DiaDiem, SucChua) — Khóa chính: `MaDT`.
5. `NHAN_VIEN` (Mã NV $\\underline{MaNV}$, HoTen, ChuyenMon, SDT) — Khóa chính: `MaNV`.

#### B. Phân tích mối kết hợp và bản số Min–Max
- **Mối kết hợp `CUNG_CAP` (NHA_CUNGCAP — LO_VACXIN):**
  - Một nhà cung cấp có thể cung cấp nhiều lô vắc-xin: $(1, N)$.
  - Một lô vắc-xin do duy nhất 1 nhà cung cấp cung ứng: $(1, 1)$.
  - $\\implies$ Bản số: `NHA_CUNGCAP (1, N)` — `(1, 1) LO_VACXIN` (Loại quan hệ: $1:N$).
- **Mối kết hợp `QUAN_LY_DIEMTIEM` (TRUNGTAM_YTE — DIEM_TIEM):**
  - Một trung tâm y tế quản lý nhiều điểm tiêm: $(1, N)$.
  - Một điểm tiêm trực thuộc duy nhất 1 trung tâm y tế: $(1, 1)$.
  - $\\implies$ Bản số: `TRUNGTAM_YTE (1, N)` — `(1, 1) DIEM_TIEM` (Loại quan hệ: $1:N$).
- **Mối kết hợp `BIEN_CHE` (TRUNGTAM_YTE — NHAN_VIEN):**
  - Một trung tâm y tế có nhiều nhân viên: $(1, N)$.
  - Mỗi nhân viên chỉ thuộc biên chế 1 trung tâm: $(1, 1)$.
  - $\\implies$ Bản số: `TRUNGTAM_YTE (1, N)` — `(1, 1) NHAN_VIEN` (Loại quan hệ: $1:N$).
- **Mối kết hợp `PHAN_PHOI` (LO_VACXIN — DIEM_TIEM):**
  - Một lô vắc-xin có thể phân phối cho nhiều điểm tiêm: $(0, N)$.
  - Một điểm tiêm có thể nhận vắc-xin từ nhiều lô khác nhau: $(1, N)$.
  - Thuộc tính của mối kết hợp: `NgayPP`, `SoLieuPP`, `TrangThai`.
  - $\\implies$ Loại quan hệ: $M:N$.
- **Mối kết hợp `TRUC_CA` (NHAN_VIEN — DIEM_TIEM):**
  - Một nhân viên có thể trực tại nhiều điểm tiêm vào các ngày khác nhau: $(0, N)$.
  - Một điểm tiêm có nhiều nhân viên đến trực: $(1, N)$.
  - Thuộc tính của mối kết hợp: `NgayTruc`, `VaiTroTruc`.
  - $\\implies$ Loại quan hệ: $M:N$.

```
[NHA_CUNGCAP] 1 ──── (1,N) ──── <CUNG_CAP> ──── (1,1) ──── N [LO_VACXIN]
                                                                  │
[TRUNGTAM_YTE] 1 ── (1,N) ── <QUAN_LY> ── (1,1) ── N [DIEM_TIEM]   │ (0,N)
      │                                                │          │
      │ (1,N)                                          │ (1,N)    │
   <BIEN_CHE>                                      <PHAN_PHOI> ───┘
      │                                                │ [NgayPP, SoLieuPP, TrangThai]
      │ (1,1)                                          │
      N                                                │
[NHAN_VIEN] N ──── (0,N) ──── <TRUC_CA> ──── (1,N) ────┘
                              [NgayTruc, VaiTroTruc]
```

### 1.2. Ánh xạ sang Lược đồ quan hệ (1.0 điểm)
Áp dụng các quy tắc ánh xạ chuẩn UIT:
1. `TRUNGTAM_YTE` ($\\underline{\\text{MaTT}}$, TenTT, DiaChiQuan)
2. `NHA_CUNGCAP` ($\\underline{\\text{MaNCC}}$, TenNCC, QuocGia, SDT)
3. `LO_VACXIN` ($\\underline{\\text{MaLo}}$, TenLo, TenVacxin, NgaySX, HSD, SoLieuNhap, DonGia, MaNCC)
   *Khóa ngoại:* `MaNCC` $\\to$ `NHA_CUNGCAP(MaNCC)`.
4. `DIEM_TIEM` ($\\underline{\\text{MaDT}}$, TenDT, DiaDiem, SucChua, MaTT)
   *Khóa ngoại:* `MaTT` $\\to$ `TRUNGTAM_YTE(MaTT)`.
5. `NHAN_VIEN` ($\\underline{\\text{MaNV}}$, HoTen, ChuyenMon, SDT, MaTT)
   *Khóa ngoại:* `MaTT` $\\to$ `TRUNGTAM_YTE(MaTT)`.
6. `PHAN_PHOI` ($\\underline{\\text{MaLo}}$, $\\underline{\\text{MaDT}}$, $\\underline{\\text{NgayPP}}$, SoLieuPP, TrangThai)
   *Khóa ngoại:* `MaLo` $\\to$ `LO_VACXIN(MaLo)`, `MaDT` $\\to$ `DIEM_TIEM(MaDT)`.
7. `TRUC_CA` ($\\underline{\\text{MaNV}}$, $\\underline{\\text{MaDT}}$, $\\underline{\\text{NgayTruc}}$, VaiTroTruc)
   *Khóa ngoại:* `MaNV` $\\to$ `NHAN_VIEN(MaNV)`, `MaDT` $\\to$ `DIEM_TIEM(MaDT)`.

**Barem chấm Câu 1:**
- Đủ 5 thực thể, thuộc tính và gạch chân PK: **0.50đ**
- Đúng mối kết hợp và bản số min-max hai phía: **1.00đ**
- Ánh xạ sang 7 quan hệ, xác định đúng PK và toàn bộ FK: **1.00đ**

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)

#### a. Ràng buộc CHECK miền giá trị (0.75 điểm)
```sql
-- Ràng buộc SOLIEUXUAT > 0 trong CTPX
ALTER TABLE CTPX
ADD CONSTRAINT CK_CTPX_SOLIEUXUAT CHECK (SOLIEUXUAT > 0);

-- Ràng buộc TRANGTHAI nhận 0 hoặc 1 trong PHIEUXUAT
ALTER TABLE PHIEUXUAT
ADD CONSTRAINT CK_PHIEUXUAT_TRANGTHAI CHECK (TRANGTHAI IN (0, 1));
```
- *Lỗi dễ mắc:* Dùng sai tên bảng, viết nhầm cú pháp `CREATE CONSTRAINT`, quên đặt tên ràng buộc.
- *Barem:* Mỗi ràng buộc đúng đạt **0.375đ**.

#### b. Cập nhật UPDATE tăng giá theo HSD và Nhà cung cấp (0.75 điểm)
- **Tư duy:** Tăng 10% tức `DONGIA = DONGIA * 1.1`. Cần liên kết `LOVACXIN` với `NHACUNGCAP` để kiểm tra `TENNCC = 'AstraZeneca'`. Điều kiện năm HSD dùng hàm `YEAR(HSD) = 2025`.

```sql
UPDATE LOVACXIN
SET DONGIA = DONGIA * 1.1
FROM LOVACXIN LV
INNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC
WHERE YEAR(LV.HSD) = 2025
  AND NCC.TENNCC = 'AstraZeneca';
```
*(Cách 2 dùng Subquery cũng được trọn điểm):*
```sql
UPDATE LOVACXIN
SET DONGIA = DONGIA * 1.1
WHERE YEAR(HSD) = 2025
  AND MANCC IN (SELECT MANCC FROM NHACUNGCAP WHERE TENNCC = 'AstraZeneca');
```
- *Barem:* Mệnh đề UPDATE & SET: **0.25đ**; Mệnh đề WHERE lọc năm và NCC: **0.50đ**.

---

### 2.2. Viết các biểu thức Đại số quan hệ (6.0 điểm)

#### a. Lọc lô vắc-xin theo tên và năm sản xuất (1.0 điểm)
- **Tư duy:**
  1. Phép chọn $\\sigma$ lọc thuộc tính chuỗi và khoảng thời gian năm 2024.
  2. Phép chiếu $\\pi$ lấy 4 thuộc tính theo đúng yêu cầu đề bài.
- **Biểu thức ĐSQH:**
  $$R_1 \\leftarrow \\sigma_{\\text{TENKVACXIN} = '\\text{Pfizer-BioNTech}' \\wedge \\text{NGAYSX} \\ge '\\text{01/01/2024}' \\wedge \\text{NGAYSX} \\le '\\text{31/12/2024}'}(\\text{LOVACXIN})$$
  $$KQ \\leftarrow \\pi_{\\text{MALO}, \\text{TENLO}, \\text{SOLIEU}, \\text{DONGIA}}(R_1)$$
- *Barem:* Phép chọn $\\sigma$: **0.50đ**; Phép chiếu $\\pi$: **0.50đ**.

#### b. Điểm tiêm nhận phiếu xuất ngày 15/10/2024 (1.0 điểm)
- **Tư duy:** Lọc phiếu xuất ngày 15/10/2024 trước để giảm kích thước bảng, sau đó kết tự nhiên với `DIEMTIEM` qua khóa ngoại `MADT`.
- **Biểu thức ĐSQH:**
  $$R_1 \\leftarrow \\sigma_{\\text{NGAYXUAT} = '\\text{15/10/2024}'}(\\text{PHIEUXUAT})$$
  $$R_2 \\leftarrow \\text{DIEMTIEM} \\bowtie R_1$$
  $$KQ \\leftarrow \\pi_{\\text{MADT}, \\text{TENDT}, \\text{QUAN}}(R_2)$$
- *Barem:* Phép chọn $\\sigma$: **0.25đ**; Phép kết $\\bowtie$: **0.50đ**; Phép chiếu $\\pi$: **0.25đ**.

#### c. Điểm tiêm quận Bình Thạnh và bác sĩ phụ trách "nếu có" (1.0 điểm)
- **Tư duy Phân Loại B:**
  - Từ khóa *"nếu có"* là tín hiệu bắt buộc của **Phép Kết Ngoài Trái (Left Outer Join $\\mathbin{⟕}$)**. Nếu dùng kết tự nhiên $\\bowtie$, các điểm tiêm ở Bình Thạnh chưa có bác sĩ trực sẽ bị loại bỏ, dẫn đến mất dữ liệu.
- **Biểu thức ĐSQH:**
  $$R_1 \\leftarrow \\sigma_{\\text{QUAN} = '\\text{Bình Thạnh}'}(\\text{DIEMTIEM})$$
  $$R_2 \\leftarrow R_1 \\mathbin{⟕}_{R_1.\\text{MADT} = \\text{BACSI}.\\text{MADT}} \\text{BACSI}$$
  $$KQ \\leftarrow \\pi_{\\text{MADT}, \\text{TENDT}, \\text{HOTEN}}(R_2)$$
- *Bẫy lỗi:* Dùng phép kết thường $\\bowtie$ thay vì kết ngoài $\\mathbin{⟕}$ bị trừ 0.50đ.
- *Barem:* Phép chọn Bình Thạnh: **0.25đ**; Phép kết ngoài $\\mathbin{⟕}$: **0.50đ**; Phép chiếu $\\pi$: **0.25đ**.

#### d. Gom nhóm tính tổng số liều xuất theo điểm tiêm tháng 10/2024 (1.0 điểm)
- **Tư duy:**
  1. Lọc các phiếu xuất có `NGAYXUAT` trong tháng 10/2024: $R_1$.
  2. Kết nối $R_1$ với `CTPX` qua `MAPX` để lấy số liều xuất: $R_2$.
  3. Gom nhóm $\\gamma$ theo `MADT`, tính hàm tổng `SUM(SOLIEUXUAT)` và đặt tên thuộc tính mới là `TONGLIEU`.
- **Biểu thức ĐSQH:**
  $$R_1 \\leftarrow \\sigma_{\\text{NGAYXUAT} \\ge '\\text{01/10/2024}' \\wedge \\text{NGAYXUAT} \\le '\\text{31/10/2024}'}(\\text{PHIEUXUAT})$$
  $$R_2 \\leftarrow R_1 \\bowtie \\text{CTPX}$$
  $$KQ \\leftarrow _{\\text{MADT}} \\gamma _{\\text{SUM}(\\text{SOLIEUXUAT}) \\to \\text{TONGLIEU}}(R_2)$$
- *Barem:* Lọc và kết nối bảng: **0.50đ**; Phép gom nhóm $\\gamma$ đúng cú pháp và hàm tổng: **0.50đ**.

#### e. Phép chia: Điểm tiêm nhận tất cả các lô của Moderna (1.0 điểm)
- **Tư duy Phân Loại C (Bài toán "Tất cả" - Phép chia $\\div$):**
  1. Xác định tập chia (tập các lô của Moderna):
     $$R_{\\text{Moderna}} \\leftarrow \\pi_{\\text{MALO}}(\\sigma_{\\text{TENNCC} = '\\text{Moderna}'}(\\text{NHACUNGCAP} \\bowtie \\text{LOVACXIN}))$$
  2. Xác định quan hệ các cặp (Điểm tiêm, Lô vắc-xin) đã thực sự tiếp nhận:
     $$R_{\\text{DT\\_Lo}} \\leftarrow \\pi_{\\text{MADT}, \\text{MALO}}(\\text{PHIEUXUAT} \\bowtie \\text{CTPX})$$
  3. Thực hiện phép chia hình thức:
     $$R_{\\text{Chia}} \\leftarrow R_{\\text{DT\\_Lo}} \\div R_{\\text{Moderna}}$$
  4. Lấy thông tin chi tiết tên điểm tiêm:
     $$KQ \\leftarrow \\pi_{\\text{MADT}, \\text{TENDT}}(R_{\\text{Chia}} \\bowtie \\text{DIEMTIEM})$$
- *Giải thích logic toán học:* Phép chia $R_{\\text{DT\\_Lo}} \\div R_{\\text{Moderna}}$ trả về tập các `MADT` sao cho $\\forall y \\in R_{\\text{Moderna}}, (\\text{MADT}, y) \\in R_{\\text{DT\\_Lo}}$.
- *Barem:* Xác định đúng tập chia $R_{\\text{Moderna}}$: **0.25đ**; Chiếu đúng quan hệ bị chia: **0.25đ**; Phép chia $\\div$ và kết lấy tên điểm tiêm: **0.50đ**.

#### f. Điểm tiêm có sức chứa lớn nhất tại Thủ Đức (1.0 điểm)
- **Tư duy Phân Loại C (Bài toán Cực Trị trong ĐSQH):**
  Trong ĐSQH thuần túy không có hàm `MAX()` trực tiếp cho bài toán lọc, ta dùng phương pháp **tự kết so sánh bé hơn và phép trừ**:
  1. Lọc danh sách điểm tiêm ở Thủ Đức: $R_1 \\leftarrow \\sigma_{\\text{QUAN} = '\\text{Thủ Đức}'}(\\text{DIEMTIEM})$.
  2. Tạo 2 bản sao đổi tên: $R_2 \\leftarrow \\rho_{D_1}(R_1)$ và $R_3 \\leftarrow \\rho_{D_2}(R_1)$.
  3. Tìm tập các điểm tiêm **chắc chắn không phải lớn nhất** (vì tồn tại điểm tiêm $D_2$ có sức chứa lớn hơn nó):
     $$R_{\\text{KoMax}} \\leftarrow \\pi_{D_1.\\text{MADT}}(R_2 \\bowtie_{D_1.\\text{SUCCHUA} < D_2.\\text{SUCCHUA}} R_3)$$
  4. Lấy toàn bộ các điểm tiêm ở Thủ Đức trừ đi tập không lớn nhất:
     $$R_{\\text{Max}} \\leftarrow \\pi_{\\text{MADT}}(R_1) - R_{\\text{KoMax}}$$
  5. Chiếu thông tin đầu ra:
     $$KQ \\leftarrow \\pi_{\\text{MADT}, \\text{TENDT}}(R_{\\text{Max}} \\bowtie R_1)$$
- *Barem:* Ý tưởng tự kết so sánh bé hơn: **0.50đ**; Phép trừ tìm cực trị và chiếu kết quả: **0.50đ**.

---
**TỔNG KẾT ĐÁNH GIÁ PILOT MOCK-01:**
- Đảm bảo 100% thời lượng 75 phút, thang điểm 10.0 không sai lệch.
- Phân bố phổ điểm đúng theo chuẩn kiểm định thực chứng: ERD 2.5đ + SQL 1.5đ + ĐSQH 6.0đ.
- Không để lộ đáp án trên đề bài học viên.
"""

with open(MOCKS_DIR / "solution.md", "w", encoding="utf-8") as f:
    f.write(solution_md.strip())

print(f"Seeded {len(problems)} problems and {len(mocks)} mock exam into {DATA_DIR} and {MOCKS_DIR}.")
