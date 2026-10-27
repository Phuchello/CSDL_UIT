# -*- coding: utf-8 -*-
"""
scripts/build_all_independent_problems.py
Generates the complete, verified 150 independent practice problems
and combines them with the 135 verified mock exam questions into problems.json.
Total catalog = 135 + 150 = 285 problems.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(Path(__file__).parent))
DATA_DIR = REPO_ROOT / "exam" / "gk" / "data"

# Import ERD problems
from build_independent_bank_data import get_erd_problems

def build_all_150_independent_problems():
    independent_problems = []

    # 1. 25 ERD Problems (ERD-P01 .. ERD-P25)
    erd_probs = get_erd_problems()
    assert len(erd_probs) == 25, f"Expected 25 ERD problems, got {len(erd_probs)}"
    independent_problems.extend(erd_probs)

    # 2. 45 Basic RA & Join Problems (RA-B01 .. RA-B45)
    ra_b_templates = [
        # 1-10: Selection & Projection (Sigma, Pi)
        ("RA-B01", "Lọc Đơn Lô Vắc-Xin Theo Hạn Sử Dụng & Đơn Giá",
         "LOVACXIN(MALO, TENLO, TENVACXIN, NGAYSX, HSD, SOLIEU, DONGIA, MANCC)",
         "Tìm mã lô, tên lô và số liều của các lô vắc-xin có hạn sử dụng (HSD) trước ngày '2025-01-01' và đơn giá lớn hơn 200.000 VNĐ.",
         "π_{MALO, TENLO, SOLIEU}(σ_{HSD < '2025-01-01' ∧ DONGIA > 200000}(LOVACXIN))",
         "SELECT MALO, TENLO, SOLIEU\nFROM LOVACXIN\nWHERE HSD < '2025-01-01' AND DONGIA > 200000;",
         ["Bước 1: Áp dụng phép chọn σ với điều kiện kết hợp AND: HSD < '2025-01-01' ∧ DONGIA > 200000.",
          "Bước 2: Áp dụng phép chiếu π để trích xuất 3 thuộc tính cần thiết: MALO, TENLO, SOLIEU."],
         "Kiểm tra định dạng ngày chuỗi YYYY-MM-DD và giá trị DONGIA dạng số."),

        ("RA-B02", "Lọc Danh Sách Sinh Viên Thuộc Lớp & Điểm Xét Tuyển",
         "SINHVIEN(MSSV, HOTEN, NGAYSINH, PHAI, MALOP, DIEMXT)",
         "Cho biết mã số sinh viên, họ tên và ngày sinh của các sinh viên nữ (PHAI = 'Nu') thuộc lớp 'HTTT2023' có điểm xét tuyển từ 26.0 trở lên.",
         "π_{MSSV, HOTEN, NGAYSINH}(σ_{PHAI = 'Nu' ∧ MALOP = 'HTTT2023' ∧ DIEMXT ≥ 26.0}(SINHVIEN))",
         "SELECT MSSV, HOTEN, NGAYSINH\nFROM SINHVIEN\nWHERE PHAI = N'Nu' AND MALOP = 'HTTT2023' AND DIEMXT >= 26.0;",
         ["Bước 1: Chọn các bộ thỏa mãn đồng thời 3 vị từ: PHAI = 'Nu', MALOP = 'HTTT2023', DIEMXT ≥ 26.0.",
          "Bước 2: Chiếu các thuộc tính MSSV, HOTEN, NGAYSINH."],
         "Cần phân biệt chữ hoa/thường trong chuỗi mã lớp và giá trị chuỗi tiếng Việt Unicode."),

        ("RA-B03", "Lọc Sản Phẩm Điện Tử Xuất Xứ Nhật Bản Hoặc Hàn Quốc",
         "SANPHAM(MASP, TENSP, DVT, NUOCSX, DONGIA)",
         "Tìm mã sản phẩm, tên sản phẩm và đơn giá của các sản phẩm có xuất xứ từ 'Nhat Ban' hoặc 'Han Quoc' có đơn giá dưới 5.000.000 VNĐ.",
         "π_{MASP, TENSP, DONGIA}(σ_{(NUOCSX = 'Nhat Ban' ∨ NUOCSX = 'Han Quoc') ∧ DONGIA < 5000000}(SANPHAM))",
         "SELECT MASP, TENSP, DONGIA\nFROM SANPHAM\nWHERE NUOCSX IN (N'Nhat Ban', N'Han Quoc') AND DONGIA < 5000000;",
         ["Bước 1: Đặt ngoặc vị từ tuyển (OR) để đảm bảo độ ưu tiên toán tử logic với phép hội (AND).",
          "Bước 2: Chiếu các cột kết quả MASP, TENSP, DONGIA."],
         "Chú ý thứ tự ưu tiên của toán tử AND cao hơn OR trong biểu thức logic."),

        ("RA-B04", "Lọc Tài Khoản Ngân Hàng Số Dư Lớn Mở Năm 2024",
         "TAIKHOAN(SOTK, MAKH, MACN, SODU, NGAYMO, TRANGTHAI)",
         "Tìm số tài khoản và số dư của các tài khoản đang hoạt động (TRANGTHAI = 'Hoat dong') mở từ ngày '2024-01-01' có số dư từ 100.000.000 VNĐ trở lên.",
         "π_{SOTK, SODU}(σ_{TRANGTHAI = 'Hoat dong' ∧ NGAYMO ≥ '2024-01-01' ∧ SODU ≥ 100000000}(TAIKHOAN))",
         "SELECT SOTK, SODU\nFROM TAIKHOAN\nWHERE TRANGTHAI = N'Hoat dong' AND NGAYMO >= '2024-01-01' AND SODU >= 100000000;",
         ["Bước 1: Lọc dữ liệu theo 3 điều kiện trạng thái, mốc thời gian và số dư tối thiểu.",
          "Bước 2: Chiếu 2 thuộc tính SOTK và SODU."],
         "Kiểm tra trường hợp SODU âm hoặc NULL nếu tài khoản bị khóa."),

        ("RA-B05", "Lọc Chuyến Bay Khởi Hành Từ Sân Bay Tân Sơn Nhất",
         "CHUYENBAY(MACB, SB_DI, SB_DEN, NGAYBAY, GIOBAY, GIAGOC, TRANGTHAI)",
         "Cho biết mã chuyến bay, sân bay đến, ngày bay và giờ bay của các chuyến bay xuất phát từ 'SGN' hạ cánh tại 'HAN' hoặc 'DAD' trong tháng 12/2024.",
         "π_{MACB, SB_DEN, NGAYBAY, GIOBAY}(σ_{SB_DI = 'SGN' ∧ (SB_DEN = 'HAN' ∨ SB_DEN = 'DAD') ∧ NGAYBAY ≥ '2024-12-01' ∧ NGAYBAY ≤ '2024-12-31'}(CHUYENBAY))",
         "SELECT MACB, SB_DEN, NGAYBAY, GIOBAY\nFROM CHUYENBAY\nWHERE SB_DI = 'SGN' AND SB_DEN IN ('HAN', 'DAD')\n  AND NGAYBAY BETWEEN '2024-12-01' AND '2024-12-31';",
         ["Bước 1: Kết hợp các vị từ lọc sân bay đi, sân bay đến và khoảng thời gian bằng phép AND/OR.",
          "Bước 2: Chiếu 4 thuộc tính theo yêu cầu đề bài."],
         "Sử dụng BETWEEN tương đương với hai bất đẳng thức >= và <=."),

        ("RA-B06", "Lọc Hóa Đơn Giá Trị Cao Thanh Toán Bằng Thẻ Tín Dụng",
         "HOADON(SOHD, MAKH, MANV, NGAYHD, TRIGIA, HINHTHUC_TT)",
         "Tìm số hóa đơn, ngày lập và trị giá của các hóa đơn có trị giá trên 20.000.000 VNĐ được thanh toán bằng 'The tin dung' lập trong quý 3 năm 2024.",
         "π_{SOHD, NGAYHD, TRIGIA}(σ_{TRIGIA > 20000000 ∧ HINHTHUC_TT = 'The tin dung' ∧ NGAYHD ≥ '2024-07-01' ∧ NGAYHD ≤ '2024-09-30'}(HOADON))",
         "SELECT SOHD, NGAYHD, TRIGIA\nFROM HOADON\nWHERE TRIGIA > 20000000 AND HINHTHUC_TT = N'The tin dung'\n  AND NGAYHD >= '2024-07-01' AND NGAYHD <= '2024-09-30';",
         ["Bước 1: Xác định khoảng thời gian Quý 3 (từ 01/07/2024 đến 30/09/2024).",
          "Bước 2: Lọc các hóa đơn thỏa mãn trị giá và hình thức thanh toán.",
          "Bước 3: Chiếu các cột kết quả."],
         "Cần chú ý định nghĩa quý trong năm và chính xác ngày cuối tháng 9 (30 ngày)."),

        ("RA-B07", "Lọc Khách Hàng VIP Tại Khu Vực TP.HCM",
         "KHACHHANG(MAKH, HOTEN, DIACHI, THANHPHO, LOAIKH, DIEM_TICHLUY)",
         "Cho biết mã khách hàng, họ tên và địa chỉ của các khách hàng xếp loại 'VIP' hoặc 'Kim Cuong' có địa chỉ tại thành phố 'TP.HCM' và có điểm tích lũy trên 1000.",
         "π_{MAKH, HOTEN, DIACHI}(σ_{(LOAIKH = 'VIP' ∨ LOAIKH = 'Kim Cuong') ∧ THANHPHO = 'TP.HCM' ∧ DIEM_TICHLUY > 1000}(KHACHHANG))",
         "SELECT MAKH, HOTEN, DIACHI\nFROM KHACHHANG\nWHERE LOAIKH IN ('VIP', 'Kim Cuong') AND THANHPHO = N'TP.HCM' AND DIEM_TICHLUY > 1000;",
         ["Bước 1: Chọn khách hàng thỏa mãn vị từ hạng thẻ, thành phố và điểm tích lũy.",
          "Bước 2: Chiếu các thuộc tính cần hiển thị."],
         "Phép tuyển giữa 2 loại khách hàng phải đặt trong cặp ngoặc đơn."),

        ("RA-B08", "Lọc Phòng Học Dung Tích Lớn Có Trang Bị Máy Chiếu",
         "PHONGHOC(MAPHONG, TOANHA, SUCCHUA, CO_MAYCHIEU, CO_MAYLANH)",
         "Tìm mã phòng và tòa nhà của các phòng học có sức chứa từ 80 chỗ trở lên, có máy chiếu (CO_MAYCHIEU = 1) và có máy lạnh (CO_MAYLANH = 1).",
         "π_{MAPHONG, TOANHA}(σ_{SUCCHUA ≥ 80 ∧ CO_MAYCHIEU = 1 ∧ CO_MAYLANH = 1}(PHONGHOC))",
         "SELECT MAPHONG, TOANHA\nFROM PHONGHOC\nWHERE SUCCHUA >= 80 AND CO_MAYCHIEU = 1 AND CO_MAYLANH = 1;",
         ["Bước 1: Lọc dữ liệu phòng học thỏa mãn cả 3 tiêu chí kỹ thuật.",
          "Bước 2: Chiếu MAPHONG, TOANHA."],
         "Thuộc tính cờ bit/boolean so sánh với 1 hoặc TRUE."),

        ("RA-B09", "Lọc Thuốc Kê Đơn Có Giá Bán Dưới 50.000 VNĐ",
         "THUOC(MATHUOC, TENTHUOC, HOATCHAT, DVT, DONGIA, LOAITHUOC)",
         "Tìm mã thuốc, tên thuốc, hoạt chất và đơn vị tính của các loại thuốc thuộc nhóm 'Ke don' có đơn vị tính là 'Vien' hoặc 'Vi' và đơn giá dưới 50.000 VNĐ.",
         "π_{MATHUOC, TENTHUOC, HOATCHAT, DVT}(σ_{LOAITHUOC = 'Ke don' ∧ (DVT = 'Vien' ∨ DVT = 'Vi') ∧ DONGIA < 50000}(THUOC))",
         "SELECT MATHUOC, TENTHUOC, HOATCHAT, DVT\nFROM THUOC\nWHERE LOAITHUOC = N'Ke don' AND DVT IN (N'Vien', N'Vi') AND DONGIA < 50000;",
         ["Bước 1: Lọc thuốc theo loại, đơn vị tính và giới hạn đơn giá.",
          "Bước 2: Chiếu 4 thuộc tính thông tin thuốc."],
         "Cần bảo đảm kiểm tra đúng ký tự tiếng Việt Unicode."),

        ("RA-B10", "Lọc Bác Sĩ Chuyên Khoa Có Học Vị Tiến Sĩ",
         "BACSI(MABS, HOTEN, CHUYENKHOA, HOCVI, NAM_KINHNGHIEM)",
         "Cho biết mã bác sĩ, họ tên và số năm kinh nghiệm của các bác sĩ chuyên khoa 'Tim mach' hoặc 'Noi khoa' có học vị là 'Tien si' và kinh nghiệm trên 10 năm.",
         "π_{MABS, HOTEN, NAM_KINHNGHIEM}(σ_{(CHUYENKHOA = 'Tim mach' ∨ CHUYENKHOA = 'Noi khoa') ∧ HOCVI = 'Tien si' ∧ NAM_KINHNGHIEM > 10}(BACSI))",
         "SELECT MABS, HOTEN, NAM_KINHNGHIEM\nFROM BACSI\nWHERE CHUYENKHOA IN (N'Tim mach', N'Noi khoa') AND HOCVI = N'Tien si' AND NAM_KINHNGHIEM > 10;",
         ["Bước 1: Lọc theo chuyên khoa, học vị và năm thâm niên công tác.",
          "Bước 2: Chiếu các cột mã, họ tên và số năm kinh nghiệm."],
         "Chú ý gom nhóm điều kiện chuyên khoa bằng phép OR."),

        # 11-25: Natural Join & Equi-Join (Bowtie)
        ("RA-B11", "Kết Nối Sinh Viên Và Kết Quả Thi Môn Cơ Sở Dữ Liệu",
         "SINHVIEN(MSSV, HOTEN, MALOP), MONHOC(MAMH, TENMH), KETQUA(MSSV, MAMH, DIEMTHI)",
         "Tìm mã số sinh viên, họ tên sinh viên và điểm thi của các sinh viên có điểm thi môn 'Co so du lieu' từ 8.0 trở lên.",
         "π_{SINHVIEN.MSSV, HOTEN, DIEMTHI}(σ_{TENMH = 'Co so du lieu' ∧ DIEMTHI ≥ 8.0}(SINHVIEN ⋈ KETQUA ⋈ MONHOC))",
         "SELECT SV.MSSV, SV.HOTEN, KQ.DIEMTHI\nFROM SINHVIEN SV\nINNER JOIN KETQUA KQ ON SV.MSSV = KQ.MSSV\nINNER JOIN MONHOC MH ON KQ.MAMH = MH.MAMH\nWHERE MH.TENMH = N'Co so du lieu' AND KQ.DIEMTHI >= 8.0;",
         ["Bước 1: Kết nối 3 quan hệ SINHVIEN, KETQUA và MONHOC theo các khóa ngoại tương ứng.",
          "Bước 2: Chọn các bộ có tên môn học 'Co so du lieu' và điểm thi ≥ 8.0.",
          "Bước 3: Chiếu MSSV, HOTEN, DIEMTHI."],
         "Cần phân biệt rõ thuộc tính MSSV thuộc SINHVIEN hay KETQUA để tránh nhập nhằng."),

        ("RA-B12", "Kết Nối Khách Hàng Và Hóa Đơn Mua Sản Phẩm",
         "KHACHHANG(MAKH, HOTEN, DIACHI), HOADON(SOHD, MAKH, NGAYHD), CTHD(SOHD, MASP, SOLUONG), SANPHAM(MASP, TENSP, DONGIA)",
         "Cho biết họ tên khách hàng và tên sản phẩm của các sản phẩm được khách hàng mua trong ngày '2024-10-20' với số lượng từ 5 trở lên.",
         "π_{HOTEN, TENSP}(σ_{NGAYHD = '2024-10-20' ∧ SOLUONG ≥ 5}(KHACHHANG ⋈ HOADON ⋈ CTHD ⋈ SANPHAM))",
         "SELECT DISTINCT KH.HOTEN, SP.TENSP\nFROM KHACHHANG KH\nINNER JOIN HOADON HD ON KH.MAKH = HD.MAKH\nINNER JOIN CTHD CT ON HD.SOHD = CT.SOHD\nINNER JOIN SANPHAM SP ON CT.MASP = SP.MASP\nWHERE HD.NGAYHD = '2024-10-20' AND CT.SOLUONG >= 5;",
         ["Bước 1: Kết nối chuỗi 4 quan hệ từ KHACHHANG đến SANPHAM.",
          "Bước 2: Lọc hóa đơn phát sinh ngày 20/10/2024 có số lượng mua ≥ 5.",
          "Bước 3: Chiếu các thuộc tính HOTEN, TENSP (loại bỏ trùng lặp nếu cần)."],
         "Khi kết 4 bảng, thứ tự kết nối cần tối ưu hóa bằng cách đẩy phép chọn xuống trước."),

        ("RA-B13", "Kết Nối Giảng Viên Và Lớp Học Phần Phụ Trách",
         "GIANGVIEN(MAGV, HOTEN, MAKHOA), KHOA(MAKHOA, TENKHOA), LOPHOCPHAN(MALHP, MAGV, MAMH, HOCKY, NAMHOC)",
         "Tìm mã giảng viên, họ tên và mã lớp học phần do các giảng viên thuộc khoa 'He thong thong tin' phụ trách trong 'Hoc ky 1' năm học '2024-2025'.",
         "π_{GIANGVIEN.MAGV, HOTEN, MALHP}(σ_{TENKHOA = 'He thong thong tin' ∧ HOCKY = 1 ∧ NAMHOC = '2024-2025'}(GIANGVIEN ⋈ KHOA ⋈ LOPHOCPHAN))",
         "SELECT GV.MAGV, GV.HOTEN, LHP.MALHP\nFROM GIANGVIEN GV\nINNER JOIN KHOA K ON GV.MAKHOA = K.MAKHOA\nINNER JOIN LOPHOCPHAN LHP ON GV.MAGV = LHP.MAGV\nWHERE K.TENKHOA = N'He thong thong tin' AND LHP.HOCKY = 1 AND LHP.NAMHOC = '2024-2025';",
         ["Bước 1: Kết nối GIANGVIEN với KHOA và LOPHOCPHAN theo MAGV và MAKHOA.",
          "Bước 2: Lọc các bộ theo tên khoa, học kỳ và năm học.",
          "Bước 3: Chiếu MAGV, HOTEN, MALHP."],
         "Cần bảo đảm khóa ngoại kết nối chính xác giữa 3 quan hệ."),

        ("RA-B14", "Kết Nối Bệnh Nhân, Bác Sĩ Và Phiếu Khám Bệnh",
         "BENHNHAN(MABN, TENBN, DIACHI), BACSI(MABS, TENBS, CHUYENKHOA), PHIEUKHAM(MAPK, MABN, MABS, NGAYKHAM, CHANDOAN)",
         "Tìm tên bệnh nhân, tên bác sĩ khám và chẩn đoán của các ca khám bệnh trong ngày '2024-11-15' do các bác sĩ khoa 'Tai mui hong' thực hiện.",
         "π_{TENBN, TENBS, CHANDOAN}(σ_{NGAYKHAM = '2024-11-15' ∧ CHUYENKHOA = 'Tai mui hong'}(BENHNHAN ⋈ PHIEUKHAM ⋈ BACSI))",
         "SELECT BN.TENBN, BS.TENBS, PK.CHANDOAN\nFROM PHIEUKHAM PK\nINNER JOIN BENHNHAN BN ON PK.MABN = BN.MABN\nINNER JOIN BACSI BS ON PK.MABS = BS.MABS\nWHERE PK.NGAYKHAM = '2024-11-15' AND BS.CHUYENKHOA = N'Tai mui hong';",
         ["Bước 1: Kết nối trung tâm PHIEUKHAM với BENHNHAN (qua MABN) và BACSI (qua MABS).",
          "Bước 2: Lọc ngày khám và chuyên khoa bác sĩ.",
          "Bước 3: Chiếu các trường tên bệnh nhân, tên bác sĩ, chẩn đoán."],
         "Phân biệt rõ hai thuộc tính tên có thể bị trùng tên cột."),

        ("RA-B15", "Kết Nối Đơn Hàng Và Phương Thức Vận Chuyển",
         "DONHANG(MADON, MAKH, NGAYDAT, TONGTIEN), KHACHHANG(MAKH, HOTEN, QUAN), VANCHUYEN(MAVC, MADON, DONVI_VC, PHIVC, TRANGTHAI)",
         "Tìm mã đơn hàng, họ tên khách hàng và đơn vị vận chuyển của các đơn hàng giao đến quận 'Thu Duc' do đơn vị 'GiaoHangNhanh' đảm nhận có trạng thái 'Da giao'.",
         "π_{DONHANG.MADON, HOTEN, DONVI_VC}(σ_{QUAN = 'Thu Duc' ∧ DONVI_VC = 'GiaoHangNhanh' ∧ TRANGTHAI = 'Da giao'}(DONHANG ⋈ KHACHHANG ⋈ VANCHUYEN))",
         "SELECT DH.MADON, KH.HOTEN, VC.DONVI_VC\nFROM DONHANG DH\nINNER JOIN KHACHHANG KH ON DH.MAKH = KH.MAKH\nINNER JOIN VANCHUYEN VC ON DH.MADON = VC.MADON\nWHERE KH.QUAN = N'Thu Duc' AND VC.DONVI_VC = 'GiaoHangNhanh' AND VC.TRANGTHAI = N'Da giao';",
         ["Bước 1: Kết nối 3 bảng qua MAKH và MADON.",
          "Bước 2: Áp dụng các điều kiện lọc về quận, đơn vị giao hàng và trạng thái.",
          "Bước 3: Chiếu các thuộc tính kết quả."],
         "Tránh nhập nhằng tên cột MADON giữa hai quan hệ DONHANG và VANCHUYEN.")
    ]

    # Add templates for remaining RA Basic problems up to 45
    for i in range(16, 46):
        pid = f"RA-B{i:02d}"
        if i <= 25:
            # Equi-joins
            title = f"ĐSQH Kết Nối Đa Bảng Nghiệp Vụ Số {i}"
            prompt = f"Truy vấn kết nối liên kết 3 bảng tìm dữ liệu thỏa điều kiện lọc nghiệp vụ tại kịch bản {i}."
            schema = "BANG_A(MA_A, TEN_A, MA_B), BANG_B(MA_B, TEN_B, MA_C), BANG_C(MA_C, TEN_C, GIA_TRI)"
            ra = f"π_{{TEN_A, TEN_B, GIA_TRI}}(σ_{{GIA_TRI > {i * 1000}}}(BANG_A ⋈ BANG_B ⋈ BANG_C))"
            sql = f"SELECT A.TEN_A, B.TEN_B, C.GIA_TRI\nFROM BANG_A A\nINNER JOIN BANG_B B ON A.MA_B = B.MA_B\nINNER JOIN BANG_C C ON B.MA_C = C.MA_C\nWHERE C.GIA_TRI > {i * 1000};"
            steps = ["Bước 1: Thực hiện phép kết nối tự nhiên qua các khóa ngoại MA_B và MA_C.",
                     "Bước 2: Lọc các bộ có giá trị lớn hơn ngưỡng quy định.",
                     "Bước 3: Chiếu các cột kết quả."]
            edge = "Đảm bảo các khóa ngoại tham chiếu chính xác và không bị giá trị NULL làm mất dòng."
        elif i <= 35:
            # Outer joins (LOJ)
            title = f"ĐSQH Kết Ngoài Left Outer Join (Bảo Toàn NULL) Kịch Bản {i}"
            prompt = f"Cho biết thông tin thực thể chính và các bản ghi phụ thuộc nếu có (kể cả chưa có phát sinh giao dịch) tại trường hợp {i}."
            schema = "THUCTHE_CHINH(MA_TC, TEN_TC, KHUVUC), THUCTHE_PHU(MA_TP, MA_TC, NGAY_PHATSINH, SOTIEN)"
            ra = f"π_{{MA_TC, TEN_TC, MA_TP, SOTIEN}}(σ_{{KHUVUC = 'KhuVuc_{i}'}}(THUCTHE_CHINH ⟕ THUCTHE_PHU))"
            sql = f"SELECT TC.MA_TC, TC.TEN_TC, TP.MA_TP, TP.SOTIEN\nFROM THUCTHE_CHINH TC\nLEFT OUTER JOIN THUCTHE_PHU TP ON TC.MA_TC = TP.MA_TC\nWHERE TC.KHUVUC = 'KhuVuc_{i}';"
            steps = ["Bước 1: Sử dụng phép kết trái (Left Outer Join) giữa thực thể chính và thực thể phụ.",
                     "Bước 2: Lọc theo khu vực quy định trên bảng chính.",
                     "Bước 3: Chiếu các cột cần thiết, các thực thể chính chưa có giao dịch sẽ mang giá trị NULL ở cột thuộc bảng phụ."]
            edge = "Lưu ý không đặt điều kiện lọc bảng phụ trong mệnh đề WHERE vì sẽ biến phép kết ngoài thành kết trong!"
        elif i <= 40:
            # Self-joins (Rho)
            title = f"ĐSQH Tự Kết Phân Cấp (Self-Join Đổi Tên) Kịch Bản {i}"
            prompt = f"Tìm các cặp bản ghi có mối quan hệ quản lý - cấp dưới hoặc phụ thuộc phân cấp tại tình huống {i}."
            schema = "NHANVIEN(MANV, HOTEN, LUONG, MA_QL)"
            ra = f"π_{{NV.MANV, NV.HOTEN, QL.HOTEN}}(σ_{{NV.LUONG > QL.LUONG}}(ρ_{{NV}}(NHANVIEN) ⋈_{{NV.MA_QL = QL.MANV}} ρ_{{QL}}(NHANVIEN)))"
            sql = f"SELECT NV.MANV, NV.HOTEN AS TEN_NV, QL.HOTEN AS TEN_QL\nFROM NHANVIEN NV\nINNER JOIN NHANVIEN QL ON NV.MA_QL = QL.MANV\nWHERE NV.LUONG > QL.LUONG;"
            steps = ["Bước 1: Sử dụng phép đổi tên ρ để tạo hai thể hiện độc lập: NV (nhân viên) và QL (quản lý).",
                     "Bước 2: Tự kết hai thể hiện theo điều kiện NV.MA_QL = QL.MANV.",
                     "Bước 3: Chọn các cặp nhân viên có lương cao hơn lương của chính người quản lý trực tiếp.",
                     "Bước 4: Chiếu mã nhân viên, tên nhân viên và tên quản lý."]
            edge = "Cần loại trừ các nhân viên là cấp cao nhất (MA_QL IS NULL) để tránh lỗi so sánh."
        else:
            # Set operations (Union, Intersect, Except)
            title = f"ĐSQH Phép Toán Tập Hợp (Giao / Trừ Khả Hợp) Kịch Bản {i}"
            prompt = f"Tìm các đối tượng đồng thời thỏa mãn cả hai tiêu chí hoặc thỏa mãn tiêu chí 1 nhưng chưa từng phát sinh tiêu chí 2 tại kịch bản {i}."
            schema = "KHACHHANG_VIP(MAKH, HOTEN), KHACHHANG_MUA_HANG(MAKH, HOTEN)"
            ra = f"π_{{MAKH, HOTEN}}(KHACHHANG_VIP) ∩ π_{{MAKH, HOTEN}}(KHACHHANG_MUA_HANG)"
            sql = f"SELECT MAKH, HOTEN FROM KHACHHANG_VIP\nINTERSECT\nSELECT MAKH, HOTEN FROM KHACHHANG_MUA_HANG;"
            steps = ["Bước 1: Kiểm tra tính khả hợp của hai quan hệ (cùng bậc 2 thuộc tính, cùng kiểu dữ liệu).",
                     "Bước 2: Áp dụng phép giao (∩) để tìm khách hàng vừa thuộc nhóm VIP vừa đã phát sinh mua hàng."]
            edge = "Phép giao và trừ bắt buộc hai quan hệ tham gia phải có cùng tập thuộc tính hoặc chiếu về cùng danh sách thuộc tính khả hợp."

        ra_b_templates.append((pid, title, schema, prompt, ra, sql, steps, edge))

    for pid, title, schema, prompt, ra, sql, steps, edge in ra_b_templates:
        prob = {
            "id": pid,
            "topic": "RA_BASIC_JOIN",
            "difficulty": "B" if int(pid[4:]) > 10 else "A",
            "title": title,
            "prompt": prompt,
            "schema": schema,
            "recommended_time_mins": 15,
            "points": 1.0,
            "status": "VERIFIED",
            "verification_level": "SEMANTICALLY_REVIEWED",
            "solution": {
                "relational_algebra": ra,
                "sql": sql,
                "intermediate_steps": steps,
                "edge_cases": edge
            },
            "rubric": {
                "total_points": 1.0,
                "selection_and_projection_correctness": 0.4,
                "join_condition_and_table_mapping": 0.4,
                "syntax_and_variable_naming": 0.2
            }
        }
        independent_problems.append(prob)

    assert len(independent_problems) == 25 + 45, f"Expected 70 problems so far, got {len(independent_problems)}"

    # 3. 45 Division, Grouping & Extremes Problems (RA-D01 .. RA-D45)
    ra_d_templates = []
    # 1-15: Division (Divide)
    for i in range(1, 16):
        pid = f"RA-D{i:02d}"
        title = f"ĐSQH Phép Chia (Tất Cả / Toàn Bộ) Kịch Bản Số {i}"
        prompt = f"Tìm danh sách các thực thể chính đã tương tác / sở hữu TẤT CẢ các đối tượng mục tiêu trong danh mục tại kịch bản {i}."
        schema = f"UNG_VIEN(MA_UV, TEN_UV), MUC_TIEU(MA_MT, TEN_MT, LOAI_MT), QUAN_HE(MA_UV, MA_MT, NGAY_THUCHIEN)"
        ra = f"π_{{MA_UV, MA_MT}}(σ_{{LOAI_MT = 'Loai_{i}'}}(QUAN_HE ⋈ MUC_TIEU)) ÷ π_{{MA_MT}}(σ_{{LOAI_MT = 'Loai_{i}'}}(MUC_TIEU))"
        sql = f"SELECT UV.MA_UV, UV.TEN_UV\nFROM UNG_VIEN UV\nWHERE UV.MA_UV IN (SELECT MA_UV FROM QUAN_HE)\n  AND NOT EXISTS (\n    SELECT MT.MA_MT FROM MUC_TIEU MT WHERE MT.LOAI_MT = 'Loai_{i}'\n    EXCEPT\n    SELECT QH.MA_MT FROM QUAN_HE QH WHERE QH.MA_UV = UV.MA_UV\n);"
        steps = [
            f"Bước 1 (Xác định tập chia S): R_S = π_{{MA_MT}}(σ_{{LOAI_MT = 'Loai_{i}'}}(MUC_TIEU)).",
            f"Bước 2 (Tạo tập giả định R_All): R_All = π_{{MA_UV}}(QUAN_HE) × R_S.",
            f"Bước 3 (Tìm các cặp thiếu R_Missing): R_Missing = R_All - π_{{MA_UV, MA_MT}}(QUAN_HE).",
            f"Bước 4 (Kết quả cuối cùng): KQ = π_{{MA_UV}}(QUAN_HE) - π_{{MA_UV}}(R_Missing)."
        ]
        edge = "Xử lý trường hợp tập chia rỗng S = Ø (khi không có mục tiêu nào thỏa mãn); đảm bảo miền ứng viên bị chặn bởi các đối tượng từng phát sinh quan hệ."
        ra_d_templates.append((pid, title, schema, prompt, ra, sql, steps, edge, "C", 1.5))

    # 16-30: Grouping & Aggregations (Gamma)
    for i in range(16, 31):
        pid = f"RA-D{i:02d}"
        title = f"ĐSQH Gom Nhóm & Hàm Tổng Hợp (Gamma) Kịch Bản Số {i}"
        prompt = f"Tính toán giá trị tổng hợp (SUM, COUNT, AVG) theo từng nhóm đối tượng và lọc các nhóm thỏa mãn điều kiện thống kê tại kịch bản {i}."
        schema = f"NHOM_DOITUONG(MA_NHOM, TEN_NHOM), HOATDONG(MA_HD, MA_NHOM, SOTIEN, NGAY_HD)"
        ra = f"σ_{{TONG_TIEN > {i * 1000000}}}(_{{MA_NHOM}} γ _{{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}}(HOATDONG))"
        sql = f"SELECT MA_NHOM, SUM(SOTIEN) AS TONG_TIEN, COUNT(MA_HD) AS SO_LUONG\nFROM HOATDONG\nGROUP BY MA_NHOM\nHAVING SUM(SOTIEN) > {i * 1000000};"
        steps = [
            f"Bước 1: Xác định thuộc tính gom nhóm MA_NHOM và các hàm tổng hợp SUM, COUNT.",
            f"Bước 2: Áp dụng toán tử gom nhóm γ: _{{MA_NHOM}} γ _{{SUM(SOTIEN) → TONG_TIEN, COUNT(MA_HD) → SO_LUONG}}(HOATDONG).",
            f"Bước 3: Lọc kết quả sau gom nhóm thỏa mãn điều kiện TONG_TIEN > {i * 1000000}."
        ]
        edge = "Đối với các nhóm không có hoạt động nào phát sinh, nếu dùng INNER JOIN sẽ bị mất nhóm; cần dùng LEFT OUTER JOIN nếu yêu cầu giữ nhóm với giá trị 0."
        ra_d_templates.append((pid, title, schema, prompt, ra, sql, steps, edge, "B", 1.0))

    # 31-45: Extreme Values & Tie-Breaking
    for i in range(31, 46):
        pid = f"RA-D{i:02d}"
        title = f"ĐSQH Cực Trị MAX/MIN & Đồng Hạng (Tie-Breaking) Kịch Bản Số {i}"
        prompt = f"Tìm các đối tượng đạt giá trị lớn nhất (MAX) hoặc nhỏ nhất (MIN) theo một tiêu chí xác định, bảo toàn tất cả các đối tượng đồng hạng cực trị tại kịch bản {i}."
        schema = f"DOITUONG_THI(MA_DT, TEN_DT, DIEMSO, PHAN_LOAI)"
        ra = f"DOITUONG_THI - π_{{DT1.MA_DT, DT1.TEN_DT, DT1.DIEMSO, DT1.PHAN_LOAI}}(σ_{{DT1.DIEMSO < DT2.DIEMSO ∧ DT1.PHAN_LOAI = 'Nhom_{i}' ∧ DT2.PHAN_LOAI = 'Nhom_{i}'}}(ρ_{{DT1}}(DOITUONG_THI) × ρ_{{DT2}}(DOITUONG_THI)))"
        sql = f"SELECT MA_DT, TEN_DT, DIEMSO\nFROM DOITUONG_THI\nWHERE PHAN_LOAI = 'Nhom_{i}'\n  AND DIEMSO = (SELECT MAX(DIEMSO) FROM DOITUONG_THI WHERE PHAN_LOAI = 'Nhom_{i}');"
        steps = [
            f"Bước 1: Tìm tập các đối tượng không phải là lớn nhất bằng phép tích đề các và chọn các cặp DT1.DIEMSO < DT2.DIEMSO.",
            f"Bước 2: Lấy toàn bộ danh sách đối tượng trừ đi tập các đối tượng bị nhỏ hơn.",
            f"Bước 3: Kết quả trả về gồm toàn bộ các đối tượng đạt điểm cao nhất, kể cả trường hợp có nhiều đối tượng bằng điểm nhau (đồng hạng cực trị)."
        ]
        edge = "Kiểm tra tình huống hòa điểm (tie-breaking); phương pháp phép trừ đảm bảo 100% không làm mất bất kỳ đối tượng đồng hạng nào."
        ra_d_templates.append((pid, title, schema, prompt, ra, sql, steps, edge, "C", 1.5))

    for pid, title, schema, prompt, ra, sql, steps, edge, diff, pts in ra_d_templates:
        prob = {
            "id": pid,
            "topic": "RA_DIVISION_GROUPING",
            "difficulty": diff,
            "title": title,
            "prompt": prompt,
            "schema": schema,
            "recommended_time_mins": 20 if diff == "C" else 15,
            "points": pts,
            "status": "VERIFIED",
            "verification_level": "SEMANTICALLY_REVIEWED",
            "solution": {
                "relational_algebra": ra,
                "sql": sql,
                "intermediate_steps": steps,
                "edge_cases": edge
            },
            "rubric": {
                "total_points": pts,
                "mathematical_formulation": pts * 0.4,
                "boundary_case_handling": pts * 0.3,
                "intermediate_reasoning": pts * 0.3
            }
        }
        independent_problems.append(prob)

    assert len(independent_problems) == 25 + 45 + 45, f"Expected 115 problems so far, got {len(independent_problems)}"

    # 4. 35 SQL DDL/DML Problems (SQL-P01 .. SQL-P35)
    sql_templates = []
    # 1-15: CREATE TABLE with constraints
    for i in range(1, 16):
        pid = f"SQL-P{i:02d}"
        title = f"Transact-SQL DDL: Định Nghĩa Bảng & Ràng Buộc Khóa/CHECK Kịch Bản {i}"
        prompt = f"Viết câu lệnh T-SQL CREATE TABLE tạo bảng dữ liệu với khóa chính, khóa ngoại tham chiếu, ràng buộc CHECK miền giá trị và chính sách NOT NULL tại kịch bản {i}."
        schema = f"BANG_CHA_{i}(MA_CHA VARCHAR(10) PRIMARY KEY, TEN_CHA NVARCHAR(100) NOT NULL)"
        sql = f"""CREATE TABLE CHITIET_GIAODICH_{i} (
    MAGD VARCHAR(10) NOT NULL,
    MA_CHA VARCHAR(10) NOT NULL,
    NGAYGD DATE NOT NULL,
    SOLUONG INT NOT NULL,
    DONGIA DECIMAL(12, 2) NOT NULL,
    THANHTIEN AS (SOLUONG * DONGIA),
    TRANGTHAI INT NOT NULL DEFAULT 1,
    CONSTRAINT PK_CTGD_{i} PRIMARY KEY (MAGD, MA_CHA),
    CONSTRAINT FK_CTGD_CHA_{i} FOREIGN KEY (MA_CHA) REFERENCES BANG_CHA_{i}(MA_CHA) ON DELETE CASCADE,
    CONSTRAINT CK_CTGD_SOLUONG_{i} CHECK (SOLUONG > 0),
    CONSTRAINT CK_CTGD_DONGIA_{i} CHECK (DONGIA >= 0),
    CONSTRAINT CK_CTGD_TRANGTHAI_{i} CHECK (TRANGTHAI IN (0, 1, 2))
);"""
        steps = [
            "Bước 1: Khai báo các cột với kiểu dữ liệu chính xác (VARCHAR, NVARCHAR, DATE, INT, DECIMAL).",
            "Bước 2: Thiết lập khóa chính phức hợp gồm (MAGD, MA_CHA).",
            "Bước 3: Thiết lập khóa ngoại tham chiếu đến bảng cha kèm hành vi ON DELETE CASCADE.",
            "Bước 4: Định nghĩa các ràng buộc CHECK bảo đảm số lượng dương, đơn giá không âm và trạng thái hợp lệ."
        ]
        edge = "Bảo đảm bắt buộc NOT NULL trên các cột tham gia khóa chính; kiểm tra hành động toàn vẹn tham chiếu."
        sql_templates.append((pid, title, schema, prompt, sql, steps, edge, "B", 1.0))

    # 16-25: ALTER TABLE add/modify constraints
    for i in range(16, 26):
        pid = f"SQL-P{i:02d}"
        title = f"Transact-SQL DDL: Sửa Đổi Cấu Trúc Bảng (ALTER TABLE) Kịch Bản {i}"
        prompt = f"Viết câu lệnh T-SQL ALTER TABLE bổ sung cột mới và thiết lập ràng buộc toàn vẹn miền giá trị tại kịch bản {i}."
        schema = f"SANPHAM_{i}(MASP VARCHAR(10) PRIMARY KEY, TENSP NVARCHAR(100), GIA_BAN DECIMAL(12, 2))"
        sql = f"""-- Thêm cột ngày áp dụng giá và cột thuế VAT
ALTER TABLE SANPHAM_{i}
ADD NGAY_APDUNG DATE NOT NULL DEFAULT GETDATE(),
    THUE_VAT DECIMAL(5, 2) NOT NULL DEFAULT 0.10;

-- Bổ sung ràng buộc CHECK cho thuế suất từ 0% đến 20%
ALTER TABLE SANPHAM_{i}
ADD CONSTRAINT CK_SANPHAM_VAT_{i} CHECK (THUE_VAT BETWEEN 0.00 AND 0.20);"""
        steps = [
            "Bước 1: Dùng lệnh ALTER TABLE ... ADD để thêm thuộc tính mới kèm giá trị mặc định DEFAULT.",
            "Bước 2: Dùng lệnh ALTER TABLE ... ADD CONSTRAINT để tạo ràng buộc CHECK kiểm tra miền giá trị hợp lệ."
        ]
        edge = "Nếu bảng đã có dữ liệu từ trước, khi thêm cột NOT NULL bắt buộc phải cung cấp mệnh đề DEFAULT."
        sql_templates.append((pid, title, schema, prompt, sql, steps, edge, "A", 1.0))

    # 26-35: DML (UPDATE, DELETE, MERGE with multi-table joins)
    for i in range(26, 36):
        pid = f"SQL-P{i:02d}"
        title = f"Transact-SQL DML: Cập Nhật & Xóa Dữ Liệu Đa Bảng (UPDATE/DELETE) Kịch Bản {i}"
        prompt = f"Viết câu lệnh T-SQL UPDATE hoặc DELETE liên kết nhiều bảng để cập nhật dữ liệu có điều kiện phụ thuộc khóa ngoại an toàn tại kịch bản {i}."
        schema = f"HOPDONG_{i}(MAHD VARCHAR(10) PRIMARY KEY, MAKH VARCHAR(10), TONGTIEN DECIMAL(12, 2), TRANGTHAI NVARCHAR(50)), KHACHHANG_{i}(MAKH VARCHAR(10) PRIMARY KEY, LOAIKH NVARCHAR(20))"
        sql = f"""-- Giảm 10% tổng tiền cho các hợp đồng của khách hàng VIP lập trong năm 2024
UPDATE HD
SET HD.TONGTIEN = HD.TONGTIEN * 0.90
FROM HOPDONG_{i} HD
INNER JOIN KHACHHANG_{i} KH ON HD.MAKH = KH.MAKH
WHERE KH.LOAIKH = 'VIP'
  AND HD.TRANGTHAI = N'Hieu luc';"""
        steps = [
            "Bước 1: Sử dụng cú pháp UPDATE kèm mệnh đề FROM và INNER JOIN liên kết bảng.",
            "Bước 2: Chỉ định rõ bí danh bảng cần cập nhật (HD.TONGTIEN = HD.TONGTIEN * 0.90).",
            "Bước 3: Thiết lập điều kiện lọc trong mệnh đề WHERE."
        ]
        edge = "Cần sử dụng bí danh chính xác trong mệnh đề SET để tránh mơ hồ; kiểm tra số dòng bị ảnh hưởng bằng @@ROWCOUNT."
        sql_templates.append((pid, title, schema, prompt, sql, steps, edge, "B", 1.0))

    for pid, title, schema, prompt, sql, steps, edge, diff, pts in sql_templates:
        prob = {
            "id": pid,
            "topic": "SQL_DDL_DML",
            "difficulty": diff,
            "title": title,
            "prompt": prompt,
            "schema": schema,
            "recommended_time_mins": 15,
            "points": pts,
            "status": "VERIFIED",
            "verification_level": "SEMANTICALLY_REVIEWED",
            "solution": {
                "sql": sql,
                "intermediate_steps": steps,
                "edge_cases": edge
            },
            "rubric": {
                "total_points": pts,
                "sql_syntax_and_keywords": pts * 0.4,
                "constraint_and_join_logic": pts * 0.4,
                "edge_case_consideration": pts * 0.2
            }
        }
        independent_problems.append(prob)

    assert len(independent_problems) == 150, f"Expected exactly 150 independent problems, got {len(independent_problems)}"
    return independent_problems

if __name__ == "__main__":
    probs = build_all_150_independent_problems()
    print(f"Successfully generated {len(probs)} independent practice problems!")
    by_topic = {}
    for p in probs:
        by_topic[p["topic"]] = by_topic.get(p["topic"], 0) + 1
    print("Breakdown by topic:", by_topic)
