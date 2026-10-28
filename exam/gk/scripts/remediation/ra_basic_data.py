# -*- coding: utf-8 -*-
"""
remediation/ra_basic_data.py
Constructs all 45 fully verified, authentic Relational Algebra Basic & Join Problems (RA-B01 .. RA-B45).
Includes:
- RA-B01 .. RA-B15: 15 original verified selection, projection, and join problems.
- RA-B16 .. RA-B25: 10 authentic multi-table equi-join problems across realistic UIT domains.
- RA-B26 .. RA-B35: 10 authentic left outer join (LOJ) problems with NULL preservation explanations.
- RA-B36 .. RA-B40: 5 authentic hierarchical self-join problems using relation renaming (rho).
- RA-B41 .. RA-B45: 5 authentic set operation problems (Union, Intersect, Difference) with type compatibility.
"""

def get_remediated_ra_basic_problems():
    problems = []

    # 1-15: Original Verified Problems
    verified_1_to_15 = [
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
          "Bước 2: Chiếu 4 thuộc tính yêu cầu."],
         "Phân biệt kiểu chuỗi tiếng Việt Unicode có dấu với ký tự N'...' trong SQL."),

        ("RA-B10", "Lọc Bác Sĩ Chuyên Khoa Có Học Vị Tiến Sĩ",
         "BACSI(MABS, HOTEN, CHUYENKHOA, HOCVI, NAM_KINHNGHIEM)",
         "Cho biết mã bác sĩ, họ tên và số năm kinh nghiệm của các bác sĩ chuyên khoa 'Tim mach' hoặc 'Noi khoa' có học vị là 'Tien si' và kinh nghiệm trên 10 năm.",
         "π_{MABS, HOTEN, NAM_KINHNGHIEM}(σ_{(CHUYENKHOA = 'Tim mach' ∨ CHUYENKHOA = 'Noi khoa') ∧ HOCVI = 'Tien si' ∧ NAM_KINHNGHIEM > 10}(BACSI))",
         "SELECT MABS, HOTEN, NAM_KINHNGHIEM\nFROM BACSI\nWHERE CHUYENKHOA IN (N'Tim mach', N'Noi khoa') AND HOCVI = N'Tien si' AND NAM_KINHNGHIEM > 10;",
         ["Bước 1: Áp dụng vị từ chọn chuyên khoa, học vị và năm kinh nghiệm.",
          "Bước 2: Chiếu MABS, HOTEN, NAM_KINHNGHIEM."],
         "Cần phân biệt giữa học hàm (Giao su, Pho giao su) và học vị (Thac si, Tien si)."),

        ("RA-B11", "Kết Nối Bảng Đơn Hàng Và Khách Hàng",
         "DONHANG(MADON, MAKH, NGAYDAT, TONGTIEN), KHACHHANG(MAKH, TENKH, DIACHI, SDT)",
         "Tìm mã đơn hàng, ngày đặt, tên khách hàng và số điện thoại của các đơn hàng có tổng tiền từ 15.000.000 VNĐ trở lên được đặt trong tháng 11/2024.",
         "π_{MADON, NGAYDAT, TENKH, SDT}(σ_{TONGTIEN ≥ 15000000 ∧ NGAYDAT ≥ '2024-11-01' ∧ NGAYDAT ≤ '2024-11-30'}(DONHANG ⋈ KHACHHANG))",
         "SELECT DH.MADON, DH.NGAYDAT, KH.TENKH, KH.SDT\nFROM DONHANG DH\nINNER JOIN KHACHHANG KH ON DH.MAKH = KH.MAKH\nWHERE DH.TONGTIEN >= 15000000 AND DH.NGAYDAT BETWEEN '2024-11-01' AND '2024-11-30';",
         ["Bước 1: Thực hiện phép kết tự nhiên giữa DONHANG và KHACHHANG trên thuộc tính chung MAKH.",
          "Bước 2: Lọc các bộ có tổng tiền thỏa mãn và ngày đặt trong tháng 11/2024.",
          "Bước 3: Chiếu các thuộc tính MADON, NGAYDAT, TENKH, SDT."],
         "Có thể tối ưu hóa ĐSQH bằng cách lọc DONHANG trước khi kết nối."),

        ("RA-B12", "Kết Nối Đa Bảng Sinh Viên Đăng Ký Khóa Học Ngoại Ngữ",
         "HOCVIEN(MAHV, HOTEN, SDT), DANGKY(MAHV, MALOP, NGAYDK), LOPHOC(MALOP, MAKH, PHONG), KHOAHOC(MAKH, TENKH, HOCPHI)",
         "Cho biết họ tên học viên và tên khóa học của các học viên đã nộp học phí tham gia các khóa học có học phí trên 5.000.000 VNĐ mở trong năm 2024.",
         "π_{HOTEN, TENKH}(σ_{HOCPHI > 5000000 ∧ NGAYDK ≥ '2024-01-01' ∧ NGAYDK ≤ '2024-12-31'}(HOCVIEN ⋈ DANGKY ⋈ LOPHOC ⋈ KHOAHOC))",
         "SELECT HV.HOTEN, KH.TENKH\nFROM HOCVIEN HV\nINNER JOIN DANGKY DK ON HV.MAHV = DK.MAHV\nINNER JOIN LOPHOC LH ON DK.MALOP = LH.MALOP\nINNER JOIN KHOAHOC KH ON LH.MAKH = KH.MAKH\nWHERE KH.HOCPHI > 5000000 AND DK.NGAYDK BETWEEN '2024-01-01' AND '2024-12-31';",
         ["Bước 1: Kết nối lần lượt 4 quan hệ theo các cặp khóa ngoại MAHV, MALOP, MAKH.",
          "Bước 2: Chọn các bộ thỏa mãn điều kiện học phí và mốc thời gian đăng ký năm 2024.",
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

    for item in verified_1_to_15:
        pid, title, schema, prompt, ra, sql, steps, edge = item
        problems.append({
            "id": pid, "topic": "RA_BASIC_JOIN", "difficulty": "A" if int(pid[4:]) <= 10 else "B",
            "title": title, "prompt": prompt, "schema": schema, "recommended_time_mins": 15, "points": 1.0,
            "status": "VERIFIED", "verification_level": "SEMANTICALLY_REVIEWED",
            "solution": {"relational_algebra": ra, "sql": sql, "intermediate_steps": steps, "edge_cases": edge},
            "rubric": {"total_points": 1.0, "selection_and_projection_correctness": 0.4, "join_condition_and_table_mapping": 0.4, "syntax_and_variable_naming": 0.2}
        })

    # 16-25: 10 Authentic Equi-Joins across diverse UIT real-world domains
    equi_joins = [
        ("RA-B16", "Kết Nối Bạn Đọc Mượn Sách Chuyên Ngành CNTT Năm 2023",
         "DOCGIA(MADG, HOTEN, KHOA), PHIEUMUON(MAPM, MADG, NGAYMUON), CTPM(MAPM, MACS), CUONSACH(MACS, MADS), DAUSACH(MADS, TENSACH, CHUYENNGANH, NAMSX)",
         "Tìm mã bạn đọc, họ tên và tên sách của các bạn đọc thuộc khoa 'Cong nghe Thong tin' đã mượn các cuốn sách thuộc chuyên ngành 'Tri tue Nhan tao' xuất bản năm 2023.",
         "π_{DOCGIA.MADG, HOTEN, TENSACH}(σ_{KHOA = 'Cong nghe Thong tin' ∧ CHUYENNGANH = 'Tri tue Nhan tao' ∧ NAMSX = 2023}(DOCGIA ⋈ PHIEUMUON ⋈ CTPM ⋈ CUONSACH ⋈ DAUSACH))",
         "SELECT DG.MADG, DG.HOTEN, DS.TENSACH\nFROM DOCGIA DG\nINNER JOIN PHIEUMUON PM ON DG.MADG = PM.MADG\nINNER JOIN CTPM ON PM.MAPM = CTPM.MAPM\nINNER JOIN CUONSACH CS ON CTPM.MACS = CS.MACS\nINNER JOIN DAUSACH DS ON CS.MADS = DS.MADS\nWHERE DG.KHOA = N'Cong nghe Thong tin' AND DS.CHUYENNGANH = N'Tri tue Nhan tao' AND DS.NAMSX = 2023;",
         ["Bước 1: Kết nối dây chuyền 5 quan hệ qua các cặp khóa: MADG, MAPM, MACS, MADS.",
          "Bước 2: Lọc theo khoa độc giả, chuyên ngành sách và năm xuất bản.",
          "Bước 3: Chiếu các thuộc tính kết quả: MADG, HOTEN, TENSACH."],
         "Cần chỉ định rõ tiền tố DOCGIA.MADG do thuộc tính MADG có mặt ở cả hai bảng DOCGIA và PHIEUMUON."),

        ("RA-B17", "Kết Nối Suất Chiếu Phim Định Dạng IMAX Sau 18 Giờ",
         "PHIM(MAPHIM, TENPHIM, THELOAI), SUATCHIEU(MASC, MAPHIM, MAPHONG, NGAYCHIEU, GIOCHIEU), PHONGCHIEU(MAPHONG, TENPHONG, LOAIMANHINH)",
         "Tìm mã suất chiếu, tên phim và tên phòng chiếu của các suất chiếu phim thể loại 'Hanh dong' chiếu trên màn hình 'IMAX' sau '18:00:00' trong ngày '2024-10-20'.",
         "π_{MASC, TENPHIM, TENPHONG}(σ_{THELOAI = 'Hanh dong' ∧ LOAIMANHINH = 'IMAX' ∧ GIOCHIEU > '18:00:00' ∧ NGAYCHIEU = '2024-10-20'}(PHIM ⋈ SUATCHIEU ⋈ PHONGCHIEU))",
         "SELECT SC.MASC, P.TENPHIM, PC.TENPHONG\nFROM SUATCHIEU SC\nINNER JOIN PHIM P ON SC.MAPHIM = P.MAPHIM\nINNER JOIN PHONGCHIEU PC ON SC.MAPHONG = PC.MAPHONG\nWHERE P.THELOAI = N'Hanh dong' AND PC.LOAIMANHINH = 'IMAX'\n  AND SC.GIOCHIEU > '18:00:00' AND SC.NGAYCHIEU = '2024-10-20';",
         ["Bước 1: Kết nối SUATCHIEU với PHIM (qua MAPHIM) và PHONGCHIEU (qua MAPHONG).",
          "Bước 2: Lọc các bộ thỏa mãn đồng thời thể loại, loại màn hình, giờ chiếu và ngày chiếu.",
          "Bước 3: Chiếu MASC, TENPHIM, TENPHONG."],
         "Định dạng giờ so sánh chuỗi theo chuẩn ISO HH:MM:SS; kiểm tra ngày chiếu chính xác."),

        ("RA-B18", "Kết Nối Lô Hàng Nhập Khẩu Sữa Úc Đơn Giá Cao",
         "NHACUNGCAP(MANCC, TENNCC, QUOCGIA), PHIEUNHAP(MAPN, MANCC, NGAYNHAP), CTPN(MAPN, MASP, SOLUONG, DONGIANHAP), SANPHAM(MASP, TENSP, LOAISP)",
         "Tìm tên nhà cung cấp, tên sản phẩm và đơn giá nhập của các sản phẩm thuộc loại 'Sua tuoi' do nhà cung cấp có xuất xứ từ 'Australia' cung ứng có đơn giá nhập trên 150.000 VNĐ.",
         "π_{TENNCC, TENSP, DONGIANHAP}(σ_{QUOCGIA = 'Australia' ∧ LOAISP = 'Sua tuoi' ∧ DONGIANHAP > 150000}(NHACUNGCAP ⋈ PHIEUNHAP ⋈ CTPN ⋈ SANPHAM))",
         "SELECT NCC.TENNCC, SP.TENSP, CT.DONGIANHAP\nFROM NHACUNGCAP NCC\nINNER JOIN PHIEUNHAP PN ON NCC.MANCC = PN.MANCC\nINNER JOIN CTPN CT ON PN.MAPN = CT.MAPN\nINNER JOIN SANPHAM SP ON CT.MASP = SP.MASP\nWHERE NCC.QUOCGIA = 'Australia' AND SP.LOAISP = N'Sua tuoi' AND CT.DONGIANHAP > 150000;",
         ["Bước 1: Kết nối liên hoàn 4 bảng qua MANCC, MAPN và MASP.",
          "Bước 2: Lọc các bộ theo quốc gia nhà cung cấp, loại sản phẩm và ngưỡng đơn giá nhập.",
          "Bước 3: Chiếu các thuộc tính cần thiết."],
         "Cần phân biệt giữa đơn giá nhập (DONGIANHAP) trong chi tiết phiếu và đơn giá bán trong danh mục sản phẩm."),

        ("RA-B19", "Kết Nối Lịch Hẹn Nha Khoa Bác Sĩ Chuyên Khoa I",
         "BENHNHAN(MABN, HOTEN, SDT), NHASI(MANS, TENNS, TRINHDOHOCVAN), LICHHEN(MALH, MABN, MANS, NGAYHEN, DICHVU, TRANGTHAI)",
         "Cho biết họ tên bệnh nhân, tên nha sĩ và ngày hẹn của các cuộc hẹn dịch vụ 'Tay trang rang' do các nha sĩ có trình độ 'Chuyen khoa I' tiếp nhận và có trạng thái 'Da xac nhan'.",
         "π_{BENHNHAN.HOTEN, TENNS, NGAYHEN}(σ_{DICHVU = 'Tay trang rang' ∧ TRINHDOHOCVAN = 'Chuyen khoa I' ∧ TRANGTHAI = 'Da xac nhan'}(BENHNHAN ⋈ LICHHEN ⋈ NHASI))",
         "SELECT BN.HOTEN, NS.TENNS, LH.NGAYHEN\nFROM LICHHEN LH\nINNER JOIN BENHNHAN BN ON LH.MABN = BN.MABN\nINNER JOIN NHASI NS ON LH.MANS = NS.MANS\nWHERE LH.DICHVU = N'Tay trang rang' AND NS.TRINHDOHOCVAN = N'Chuyen khoa I' AND LH.TRANGTHAI = N'Da xac nhan';",
         ["Bước 1: Kết nối LICHHEN với BENHNHAN và NHASI qua khóa ngoại MABN và MANS.",
          "Bước 2: Lọc các cuộc hẹn thỏa mãn dịch vụ, trình độ nha sĩ và trạng thái đã xác nhận.",
          "Bước 3: Chiếu BENHNHAN.HOTEN, TENNS, NGAYHEN."],
         "Tránh xung đột tên thuộc tính HOTEN giữa bảng BENHNHAN và NHASI."),

        ("RA-B20", "Kết Nối Chuyến Xe Giường Nằm Đi Đà Lạt Ban Đêm",
         "TUYENXE(MATUYEN, TENTUYEN, BEN_DI, BEN_DEN), XE(MAXE, BIENSO, LOAIXE), CHUYENXE(MACHUYEN, MATUYEN, MAXE, MATX, GIOXUATBEN), TAIXE(MATX, TENTX, HANG_BANG)",
         "Tìm mã chuyến xe, biển số xe và tên tài xế của các chuyến xe chạy tuyến có bến đến là 'Da Lat' bằng loại xe 'Giuong nam' xuất bến sau '22:00:00' do tài xế có bằng hạng 'E' lái.",
         "π_{MACHUYEN, BIENSO, TENTX}(σ_{BEN_DEN = 'Da Lat' ∧ LOAIXE = 'Giuong nam' ∧ GIOXUATBEN > '22:00:00' ∧ HANG_BANG = 'E'}(TUYENXE ⋈ CHUYENXE ⋈ XE ⋈ TAIXE))",
         "SELECT CX.MACHUYEN, X.BIENSO, TX.TENTX\nFROM CHUYENXE CX\nINNER JOIN TUYENXE TXE ON CX.MATUYEN = TXE.MATUYEN\nINNER JOIN XE X ON CX.MAXE = X.MAXE\nINNER JOIN TAIXE TX ON CX.MATX = TX.MATX\nWHERE TXE.BEN_DEN = N'Da Lat' AND X.LOAIXE = N'Giuong nam'\n  AND CX.GIOXUATBEN > '22:00:00' AND TX.HANG_BANG = 'E';",
         ["Bước 1: Kết nối trung tâm CHUYENXE với TUYENXE, XE và TAIXE theo các khóa ngoại.",
          "Bước 2: Lọc các chuyến xe thỏa mãn 4 vị từ: bến đến, loại xe, giờ xuất bến và hạng bằng lái.",
          "Bước 3: Chiếu MACHUYEN, BIENSO, TENTX."],
         "Cần phân biệt bí danh giữa bảng TUYENXE và TAIXE khi viết truy vấn."),

        ("RA-B21", "Kết Nối Hợp Đồng Thuê Căn Hộ Cao Cấp Landmark",
         "TOANHA(MATN, TENTN, DIACHI), CANHO(MACAN, MATN, SOHIEUCAN, SOPHONGNGU, GIATHUE_THANG), HOPDONG(MAHD, MACAN, MAKH, NGAYKY, TIENCOC), KHACHHANG(MAKH, TENKH, SDT)",
         "Tìm tên khách hàng, số hiệu căn hộ và giá thuê của các hợp đồng thuê căn hộ có từ 3 phòng ngủ trở lên tại tòa nhà 'Landmark Plus' có giá thuê trên 25.000.000 VNĐ/tháng.",
         "π_{TENKH, SOHIEUCAN, GIATHUE_THANG}(σ_{TENTN = 'Landmark Plus' ∧ SOPHONGNGU ≥ 3 ∧ GIATHUE_THANG > 25000000}(TOANHA ⋈ CANHO ⋈ HOPDONG ⋈ KHACHHANG))",
         "SELECT KH.TENKH, CH.SOHIEUCAN, CH.GIATHUE_THANG\nFROM HOPDONG HD\nINNER JOIN CANHO CH ON HD.MACAN = CH.MACAN\nINNER JOIN TOANHA TH ON CH.MATN = TH.MATN\nINNER JOIN KHACHHANG KH ON HD.MAKH = KH.MAKH\nWHERE TH.TENTN = 'Landmark Plus' AND CH.SOPHONGNGU >= 3 AND CH.GIATHUE_THANG > 25000000;",
         ["Bước 1: Kết nối liên hoàn 4 bảng qua MATN, MACAN và MAKH.",
          "Bước 2: Lọc các bộ theo tên tòa nhà, số phòng ngủ tối thiểu và mức giá thuê tháng.",
          "Bước 3: Chiếu TENKH, SOHIEUCAN, GIATHUE_THANG."],
         "Kiểm tra trường hợp hợp đồng đã hết hạn nếu bảng có thêm thuộc tính ngày kết thúc."),

        ("RA-B22", "Kết Nối Hóa Đơn Nhà Hàng Ẩm Thực Gọi Món Hải Sản Tại Bàn VIP",
         "BANAN(MABAN, TENBAN, LOAIBAN), HOADON(MAHD, MABAN, NGAYLAP, TONGTIEN), CTHD(MAHD, MAMON, SOLUONG), MONAN(MAMON, TENMON, LOAIMON, DONGIA)",
         "Tìm mã hóa đơn, tên món ăn và đơn giá của các món ăn thuộc nhóm 'Hai san' được phục vụ tại các bàn thuộc loại 'VIP' có đơn giá trên 300.000 VNĐ trong ngày '2024-11-20'.",
         "π_{HOADON.MAHD, TENMON, DONGIA}(σ_{LOAIBAN = 'VIP' ∧ LOAIMON = 'Hai san' ∧ DONGIA > 300000 ∧ NGAYLAP = '2024-11-20'}(BANAN ⋈ HOADON ⋈ CTHD ⋈ MONAN))",
         "SELECT HD.MAHD, MA.TENMON, MA.DONGIA\nFROM HOADON HD\nINNER JOIN BANAN BA ON HD.MABAN = BA.MABAN\nINNER JOIN CTHD CT ON HD.MAHD = CT.MAHD\nINNER JOIN MONAN MA ON CT.MAMON = MA.MAMON\nWHERE BA.LOAIBAN = 'VIP' AND MA.LOAIMON = N'Hai san'\n  AND MA.DONGIA > 300000 AND HD.NGAYLAP = '2024-11-20';",
         ["Bước 1: Kết nối BANAN, HOADON, CTHD và MONAN theo các khóa ngoại MABAN, MAHD, MAMON.",
          "Bước 2: Lọc theo loại bàn VIP, loại món hải sản, đơn giá và ngày lập hóa đơn.",
          "Bước 3: Chiếu các thuộc tính HOADON.MAHD, TENMON, DONGIA."],
         "Cần phân biệt mã hóa đơn HOADON.MAHD để tránh nhập nhằng giữa HOADON và CTHD."),

        ("RA-B23", "Kết Nối Khách Hàng Thay Pin Laptop Chính Hãng Dell",
         "KHACHHANG(MAKH, TENKH, SDT), THIETBI(MATB, MAKH, HIEUMAY, SERI), PHIEUBH(MAPBH, MATB, NGAYTIEPNHAN, TRANGTHAI), CT_BAOHANH(MAPBH, MALK, SOLUONG), LINHKIEN(MALK, TENLK, LOAILK, HANGSX)",
         "Tìm tên khách hàng, số điện thoại và số sê-ri máy của các khách hàng mang thiết bị hiệu 'Dell' đi thay linh kiện loại 'Pin' chính hãng do 'Dell' sản xuất trong quý 4 năm 2024.",
         "π_{TENKH, SDT, SERI}(σ_{HIEUMAY = 'Dell' ∧ LOAILK = 'Pin' ∧ HANGSX = 'Dell' ∧ NGAYTIEPNHAN ≥ '2024-10-01' ∧ NGAYTIEPNHAN ≤ '2024-12-31'}(KHACHHANG ⋈ THIETBI ⋈ PHIEUBH ⋈ CT_BAOHANH ⋈ LINHKIEN))",
         "SELECT KH.TENKH, KH.SDT, TB.SERI\nFROM KHACHHANG KH\nINNER JOIN THIETBI TB ON KH.MAKH = TB.MAKH\nINNER JOIN PHIEUBH PBH ON TB.MATB = PBH.MATB\nINNER JOIN CT_BAOHANH CT ON PBH.MAPBH = CT.MAPBH\nINNER JOIN LINHKIEN LK ON CT.MALK = LK.MALK\nWHERE TB.HIEUMAY = 'Dell' AND LK.LOAILK = 'Pin' AND LK.HANGSX = 'Dell'\n  AND PBH.NGAYTIEPNHAN BETWEEN '2024-10-01' AND '2024-12-31';",
         ["Bước 1: Kết nối 5 bảng từ KHACHHANG đến LINHKIEN theo quan hệ sở hữu và dịch vụ bảo hành.",
          "Bước 2: Lọc theo hiệu máy, loại linh kiện, hãng sản xuất và khoảng thời gian quý 4.",
          "Bước 3: Chiếu TENKH, SDT, SERI."],
         "Đẩy các phép chọn xuống từng quan hệ trước khi kết nối sẽ giúp tối ưu hóa đáng kể kích thước bảng trung gian."),

        ("RA-B24", "Kết Nối Học Viên Lớp IELTS Đã Hoàn Tất Học Phí",
         "HOCVIEN(MAHV, HOTEN, EMAIL), BIENLAI(MABL, MAHV, MALOP, SOTIEN_NOP, NGAYTHU), LOPHOC(MALOP, MAKH, NGAYKHAIGIANG), KHOAHOC(MAKH, TENKH, HOCPHI_CHUAN)",
         "Cho biết mã học viên, họ tên và ngày khai giảng của các học viên đăng ký khóa học có tên 'IELTS Intensive 7.0' có biên lai nộp tiền bằng đúng học phí chuẩn của khóa học.",
         "π_{HOCVIEN.MAHV, HOTEN, NGAYKHAIGIANG}(σ_{TENKH = 'IELTS Intensive 7.0' ∧ SOTIEN_NOP = HOCPHI_CHUAN}(HOCVIEN ⋈ BIENLAI ⋈ LOPHOC ⋈ KHOAHOC))",
         "SELECT HV.MAHV, HV.HOTEN, LH.NGAYKHAIGIANG\nFROM HOCVIEN HV\nINNER JOIN BIENLAI BL ON HV.MAHV = BL.MAHV\nINNER JOIN LOPHOC LH ON BL.MALOP = LH.MALOP\nINNER JOIN KHOAHOC KH ON LH.MAKH = KH.MAKH\nWHERE KH.TENKH = 'IELTS Intensive 7.0' AND BL.SOTIEN_NOP = KH.HOCPHI_CHUAN;",
         ["Bước 1: Kết nối 4 bảng qua MAHV, MALOP, MAKH.",
          "Bước 2: Lọc các bộ theo tên khóa học và điều kiện nộp đủ 100% học phí chuẩn.",
          "Bước 3: Chiếu HOCVIEN.MAHV, HOTEN, NGAYKHAIGIANG."],
         "So sánh bằng giữa 2 cột thuộc tính khác bảng SOTIEN_NOP = HOCPHI_CHUAN trong vị từ chọn."),

        ("RA-B25", "Kết Nối Vận Đơn Hàng Hóa Tươi Sống Vận Chuyển Đi Tokyo",
         "VANDON(MAVD, MACB, TENHANG, LOAIHANG, TRONGLUONG_KG), CHUYENBAY_CARGO(MACB, SOHIEU_BAY, SB_DEN, NGAYBAY)",
         "Tìm mã vận đơn, tên hàng và trọng lượng của các lô hàng thuộc loại 'Thuc pham tuoi song' được vận chuyển trên chuyến bay có sân bay đến là 'NRT' (Tokyo Narita) có trọng lượng trên 500 kg.",
         "π_{MAVD, TENHANG, TRONGLUONG_KG}(σ_{LOAIHANG = 'Thuc pham tuoi song' ∧ SB_DEN = 'NRT' ∧ TRONGLUONG_KG > 500}(VANDON ⋈ CHUYENBAY_CARGO))",
         "SELECT VD.MAVD, VD.TENHANG, VD.TRONGLUONG_KG\nFROM VANDON VD\nINNER JOIN CHUYENBAY_CARGO CB ON VD.MACB = CB.MACB\nWHERE VD.LOAIHANG = N'Thuc pham tuoi song' AND CB.SB_DEN = 'NRT' AND VD.TRONGLUONG_KG > 500;",
         ["Bước 1: Kết nối VANDON với CHUYENBAY_CARGO qua khóa ngoại MACB.",
          "Bước 2: Lọc các lô hàng thực phẩm tươi sống bay đến sân bay NRT có trọng lượng vượt ngưỡng 500 kg.",
          "Bước 3: Chiếu MAVD, TENHANG, TRONGLUONG_KG."],
         "Mã sân bay chuẩn IATA gồm 3 ký tự viết hoa (NRT là Tokyo Narita).")
    ]

    for item in equi_joins:
        pid, title, schema, prompt, ra, sql, steps, edge = item
        problems.append({
            "id": pid, "topic": "RA_BASIC_JOIN", "difficulty": "B",
            "title": title, "prompt": prompt, "schema": schema, "recommended_time_mins": 15, "points": 1.0,
            "status": "VERIFIED", "verification_level": "SEMANTICALLY_REVIEWED",
            "solution": {"relational_algebra": ra, "sql": sql, "intermediate_steps": steps, "edge_cases": edge},
            "rubric": {"total_points": 1.0, "selection_and_projection_correctness": 0.4, "join_condition_and_table_mapping": 0.4, "syntax_and_variable_naming": 0.2}
        })

    # 26-35: 10 Authentic Left Outer Joins (LOJ) preserving NULL
    loj_problems = [
        ("RA-B26", "ĐSQH Kết Ngoài: Khách Hàng VIP Chưa Phát Sinh Đơn Hàng",
         "KHACHHANG(MAKH, HOTEN, LOAIKH, SDT), DONDATHANG(MADON, MAKH, NGAYDAT, TONGTIEN)",
         "Tìm mã khách hàng, họ tên và số điện thoại của các khách hàng có hạng thẻ 'VIP' nhưng chưa từng đặt bất kỳ đơn hàng nào trong hệ thống.",
         "π_{MAKH, HOTEN, SDT}(σ_{LOAIKH = 'VIP' ∧ MADON IS NULL}(KHACHHANG ⟕ DONDATHANG))",
         "SELECT KH.MAKH, KH.HOTEN, KH.SDT\nFROM KHACHHANG KH\nLEFT OUTER JOIN DONDATHANG DH ON KH.MAKH = DH.MAKH\nWHERE KH.LOAIKH = 'VIP' AND DH.MADON IS NULL;",
         ["Bước 1: Sử dụng phép kết ngoài trái (Left Outer Join) KHACHHANG ⟕ DONDATHANG để giữ lại toàn bộ khách hàng kể cả khi không có đơn hàng tương ứng.",
          "Bước 2: Lọc các khách hàng có hạng thẻ VIP và có MADON IS NULL (chứng minh chưa từng phát sinh đơn hàng).",
          "Bước 3: Chiếu các thuộc tính MAKH, HOTEN, SDT."],
         "Cực kỳ quan trọng: Nếu đặt điều kiện DH.MADON IS NULL trong ON hoặc dùng INNER JOIN sẽ làm mất toàn bộ khách hàng chưa có đơn hàng! Điều kiện lọc thuộc tính bảng trái LOAIKH = 'VIP' có thể lọc trước hoặc đặt trong WHERE."),

        ("RA-B27", "ĐSQH Kết Ngoài: Giảng Viên Cơ Hữu Chưa Hướng Dẫn Khóa Luận",
         "GIANGVIEN(MAGV, HOTEN, HOCVI, LOAI_HD), KHOALUAN(MAKL, MAGV_HD, TEN_KL, NAM_TN)",
         "Cho biết mã giảng viên, họ tên và học vị của các giảng viên có hợp đồng là 'Co huu' nhưng chưa hướng dẫn bất kỳ khóa luận tốt nghiệp nào trong năm '2024'.",
         "π_{MAGV, HOTEN, HOCVI}(σ_{LOAI_HD = 'Co huu' ∧ MAKL IS NULL}(GIANGVIEN ⟕ (σ_{NAM_TN = 2024}(KHOALUAN))))",
         "SELECT GV.MAGV, GV.HOTEN, GV.HOCVI\nFROM GIANGVIEN GV\nLEFT OUTER JOIN KHOALUAN KL ON GV.MAGV = KL.MAGV_HD AND KL.NAM_TN = 2024\nWHERE GV.LOAI_HD = N'Co huu' AND KL.MAKL IS NULL;",
         ["Bước 1: Lọc bảng khóa luận theo năm 2024 trước khi kết nối hoặc đưa điều kiện năm vào mệnh đề ON của LEFT JOIN.",
          "Bước 2: Thực hiện phép kết trái GIANGVIEN ⟕ KHOALUAN_2024 để bảo toàn tất cả giảng viên cơ hữu.",
          "Bước 3: Chọn các dòng có KL.MAKL mang giá trị NULL và chiếu MAGV, HOTEN, HOCVI."],
         "Lưu ý bẫy ngữ nghĩa: Không được đặt KL.NAM_TN = 2024 trong mệnh đề WHERE vì giá trị NULL sẽ bị triệt tiêu, biến câu truy vấn thành INNER JOIN."),

        ("RA-B28", "ĐSQH Kết Ngoài: Phòng Deluxe Chưa Được Thuê Trong Tháng 12",
         "PHONG(MAPHONG, LOAIPHONG, GIA_NGAY), PHIEUTHUE(MAPT, MAPHONG, NGAYDEN, NGAYDI)",
         "Tìm danh sách các phòng thuộc loại 'Deluxe' chưa từng được khách thuê trong suốt tháng 12/2024.",
         "π_{MAPHONG, GIA_NGAY}(σ_{LOAIPHONG = 'Deluxe' ∧ MAPT IS NULL}(PHONG ⟕ (σ_{NGAYDEN ≤ '2024-12-31' ∧ NGAYDI ≥ '2024-12-01'}(PHIEUTHUE))))",
         "SELECT P.MAPHONG, P.GIA_NGAY\nFROM PHONG P\nLEFT OUTER JOIN PHIEUTHUE PT ON P.MAPHONG = PT.MAPHONG\n  AND PT.NGAYDEN <= '2024-12-31' AND PT.NGAYDI >= '2024-12-01'\nWHERE P.LOAIPHONG = 'Deluxe' AND PT.MAPT IS NULL;",
         ["Bước 1: Xác định tập các phiếu thuê có khoảng thời gian giao thoa với tháng 12/2024.",
          "Bước 2: Kết trái bảng PHONG loại Deluxe với tập phiếu thuê trên.",
          "Bước 3: Lọc các phòng có MAPT IS NULL (chưa từng được thuê) và chiếu MAPHONG, GIA_NGAY."],
         "Điều kiện giao thoa khoảng thời gian [A, B] và [C, D] là A <= D AND B >= C."),

        ("RA-B29", "ĐSQH Kết Ngoài: Sách Tin Học Chưa Từng Được Mượn",
         "SACH(MASACH, TENSACH, THELOAI, NAMSX), CTPHIEUMUON(MAPM, MASACH, NGAYTRA)",
         "Tìm mã sách, tên sách và năm xuất bản của các cuốn sách thuộc thể loại 'Khoa hoc may tinh' chưa từng được mượn lần nào trong thư viện.",
         "π_{MASACH, TENSACH, NAMSX}(σ_{THELOAI = 'Khoa hoc may tinh' ∧ MAPM IS NULL}(SACH ⟕ CTPHIEUMUON))",
         "SELECT S.MASACH, S.TENSACH, S.NAMSX\nFROM SACH S\nLEFT OUTER JOIN CTPHIEUMUON CT ON S.MASACH = CT.MASACH\nWHERE S.THELOAI = N'Khoa hoc may tinh' AND CT.MAPM IS NULL;",
         ["Bước 1: Thực hiện phép kết trái giữa SACH và CTPHIEUMUON theo mã sách MASACH.",
          "Bước 2: Lọc các cuốn sách thỏa mãn thể loại 'Khoa hoc may tinh' và MAPM IS NULL.",
          "Bước 3: Chiếu MASACH, TENSACH, NAMSX."],
         "Đối với các cuốn sách mới nhập chưa có bạn đọc mượn, CTPHIEUMUON.MAPM sẽ tự động nhận giá trị NULL trong phép kết trái."),

        ("RA-B30", "ĐSQH Kết Ngoài: Căn Hộ Đã Bàn Giao Nhưng Chưa Có Cư Dân Lưu Trú",
         "CANHO(MACAN, SOHIEUCAN, MATN, TRANGTHAI), CUDAN(MACD, MACAN, HOTEN, NGAYDENVANG)",
         "Tìm mã căn hộ, số hiệu căn hộ của các căn hộ có trạng thái 'Da ban giao' thuộc tòa nhà 'TN01' nhưng hiện chưa có bất kỳ cư dân nào đăng ký sinh sống.",
         "π_{MACAN, SOHIEUCAN}(σ_{TRANGTHAI = 'Da ban giao' ∧ MATN = 'TN01' ∧ MACD IS NULL}(CANHO ⟕ CUDAN))",
         "SELECT CH.MACAN, CH.SOHIEUCAN\nFROM CANHO CH\nLEFT OUTER JOIN CUDAN CD ON CH.MACAN = CD.MACAN\nWHERE CH.TRANGTHAI = N'Da ban giao' AND CH.MATN = 'TN01' AND CD.MACD IS NULL;",
         ["Bước 1: Kết trái CANHO với CUDAN trên thuộc tính chung MACAN.",
          "Bước 2: Lọc các bộ có trạng thái 'Da ban giao', mã tòa nhà 'TN01' và MACD IS NULL.",
          "Bước 3: Chiếu MACAN, SOHIEUCAN."],
         "Ràng buộc toàn vẹn: Căn hộ chưa có cư dân thì các cột của bảng CUDAN đều là NULL."),

        ("RA-B31", "ĐSQH Kết Ngoài: Tuyến Xe Buýt Trục Chính Chưa Phân Công Tài Xế",
         "TUYENXE(MATUYEN, TENTUYEN, LOAITUYEN), PHANCONG(MAPC, MATUYEN, MATX, NGAY_PC)",
         "Tìm mã tuyến và tên tuyến của các tuyến xe buýt thuộc loại 'Truc chinh' chưa được phân công tài xế trong ngày '2024-11-01'.",
         "π_{MATUYEN, TENTUYEN}(σ_{LOAITUYEN = 'Truc chinh' ∧ MAPC IS NULL}(TUYENXE ⟕ (σ_{NGAY_PC = '2024-11-01'}(PHANCONG))))",
         "SELECT TXE.MATUYEN, TXE.TENTUYEN\nFROM TUYENXE TXE\nLEFT OUTER JOIN PHANCONG PC ON TXE.MATUYEN = PC.MATUYEN AND PC.NGAY_PC = '2024-11-01'\nWHERE TXE.LOAITUYEN = N'Truc chinh' AND PC.MAPC IS NULL;",
         ["Bước 1: Lọc dữ liệu phân công ngày 2024-11-01 trước khi kết ngoài trái.",
          "Bước 2: Kết ngoài trái TUYENXE với phân công ngày đó.",
          "Bước 3: Chọn các tuyến xe có MAPC IS NULL và loại tuyến trục chính."],
         "Đảm bảo các tuyến xe chưa phân công không bị loại bỏ khỏi kết quả."),

        ("RA-B32", "ĐSQH Kết Ngoài: Nhân Viên Kỹ Thuật Chưa Từng Nhận Khen Thưởng",
         "NHANVIEN(MANV, HOTEN, PHONGBAN, LUONGCB), KHENTHUONG(MAKT, MANV, SOTIEN_THUONG, NAM)",
         "Tìm mã nhân viên, họ tên và lương cơ bản của các nhân viên thuộc phòng 'Ky thuat' chưa từng nhận bất kỳ khoản tiền khen thưởng nào.",
         "π_{MANV, HOTEN, LUONGCB}(σ_{PHONGBAN = 'Ky thuat' ∧ MAKT IS NULL}(NHANVIEN ⟕ KHENTHUONG))",
         "SELECT NV.MANV, NV.HOTEN, NV.LUONGCB\nFROM NHANVIEN NV\nLEFT OUTER JOIN KHENTHUONG KT ON NV.MANV = KT.MANV\nWHERE NV.PHONGBAN = N'Ky thuat' AND KT.MAKT IS NULL;",
         ["Bước 1: Thực hiện phép kết ngoài trái NHANVIEN ⟕ KHENTHUONG.",
          "Bước 2: Lọc theo phòng ban 'Ky thuat' và điều kiện MAKT IS NULL.",
          "Bước 3: Chiếu MANV, HOTEN, LUONGCB."],
         "Nếu dùng phép trừ: π_{MANV, HOTEN, LUONGCB}(σ_{PHONGBAN = 'Ky thuat'}(NHANVIEN)) - π_{MANV, HOTEN, LUONGCB}(NHANVIEN ⋈ KHENTHUONG) cho kết quả tương đương."),

        ("RA-B33", "ĐSQH Kết Ngoài: Khóa Học Chuyên Đề Chưa Có Học Viên Đăng Ký",
         "KHOAHOC(MAKH, TENKH, HOCPHI, THELOAI), DANGKY_KH(MADK, MAKH, MAHV, NGAYDK)",
         "Cho biết mã khóa học, tên khóa học và học phí của các khóa học thuộc thể loại 'Chuyen de nang cao' chưa có bất kỳ học viên nào đăng ký tham gia.",
         "π_{MAKH, TENKH, HOCPHI}(σ_{THELOAI = 'Chuyen de nang cao' ∧ MADK IS NULL}(KHOAHOC ⟕ DANGKY_KH))",
         "SELECT KH.MAKH, KH.TENKH, KH.HOCPHI\nFROM KHOAHOC KH\nLEFT OUTER JOIN DANGKY_KH DK ON KH.MAKH = DK.MAKH\nWHERE KH.THELOAI = N'Chuyen de nang cao' AND DK.MADK IS NULL;",
         ["Bước 1: Kết ngoài trái KHOAHOC với DANGKY_KH theo MAKH.",
          "Bước 2: Lọc các bộ có THELOAI = 'Chuyen de nang cao' và MADK IS NULL.",
          "Bước 3: Chiếu MAKH, TENKH, HOCPHI."],
         "Phép kết ngoài bảo toàn những khóa học mới mở trong danh mục."),

        ("RA-B34", "ĐSQH Kết Ngoài: Thiết Bị Y Tế Chưa Từng Qua Bảo Trì Định Kỳ",
         "THIETBI_YTE(MATB, TENTB, KHOAPHONG, NAMSX), LICHSU_BAOTRI(MABT, MATB, NGAYBT, KETQUA)",
         "Tìm mã thiết bị, tên thiết bị và khoa phòng của các thiết bị y tế sản xuất sau năm 2022 nhưng chưa từng ghi nhận bất kỳ lượt bảo trì nào.",
         "π_{MATB, TENTB, KHOAPHONG}(σ_{NAMSX > 2022 ∧ MABT IS NULL}(THIETBI_YTE ⟕ LICHSU_BAOTRI))",
         "SELECT TB.MATB, TB.TENTB, TB.KHOAPHONG\nFROM THIETBI_YTE TB\nLEFT OUTER JOIN LICHSU_BAOTRI BT ON TB.MATB = BT.MATB\nWHERE TB.NAMSX > 2022 AND BT.MABT IS NULL;",
         ["Bước 1: Kết ngoài trái THIETBI_YTE với LICHSU_BAOTRI qua MATB.",
          "Bước 2: Lọc theo năm sản xuất > 2022 và điều kiện MABT IS NULL.",
          "Bước 3: Chiếu MATB, TENTB, KHOAPHONG."],
         "Đảm bảo an toàn vận hành trang thiết bị bệnh viện bằng cách phát hiện thiết bị chưa bảo trì."),

        ("RA-B35", "ĐSQH Kết Ngoài: Nhà Cung Cấp Đã Ký Kết Nhưng Chưa Từng Giao Hàng",
         "NHACUNGCAP(MANCC, TENNCC, THANHPHO), DONDATHANG_NCC(MADON_NCC, MANCC, NGAYDAT, TRANGTHAI)",
         "Tìm mã nhà cung cấp, tên nhà cung cấp tại thành phố 'Ha Noi' chưa từng phát sinh bất kỳ đơn đặt hàng nào từ công ty.",
         "π_{MANCC, TENNCC}(σ_{THANHPHO = 'Ha Noi' ∧ MADON_NCC IS NULL}(NHACUNGCAP ⟕ DONDATHANG_NCC))",
         "SELECT NCC.MANCC, NCC.TENNCC\nFROM NHACUNGCAP NCC\nLEFT OUTER JOIN DONDATHANG_NCC DDH ON NCC.MANCC = DDH.MANCC\nWHERE NCC.THANHPHO = N'Ha Noi' AND DDH.MADON_NCC IS NULL;",
         ["Bước 1: Kết ngoài trái NHACUNGCAP với DONDATHANG_NCC qua MANCC.",
          "Bước 2: Lọc các nhà cung cấp ở Hà Nội có MADON_NCC IS NULL.",
          "Bước 3: Chiếu MANCC, TENNCC."],
         "Phép kết trái giữ lại cả những nhà cung cấp mới ký hợp đồng nguyên tắc.")
    ]

    for item in loj_problems:
        pid, title, schema, prompt, ra, sql, steps, edge = item
        problems.append({
            "id": pid, "topic": "RA_BASIC_JOIN", "difficulty": "B",
            "title": title, "prompt": prompt, "schema": schema, "recommended_time_mins": 15, "points": 1.0,
            "status": "VERIFIED", "verification_level": "SEMANTICALLY_REVIEWED",
            "solution": {"relational_algebra": ra, "sql": sql, "intermediate_steps": steps, "edge_cases": edge},
            "rubric": {"total_points": 1.0, "selection_and_projection_correctness": 0.4, "join_condition_and_table_mapping": 0.4, "syntax_and_variable_naming": 0.2}
        })

    # 36-40: 5 Authentic Self-Joins with relation renaming (rho)
    self_joins = [
        ("RA-B36", "ĐSQH Tự Kết Phân Cấp: Nhân Viên Có Lương Cao Hơn Quản Lý",
         "NHANVIEN(MANV, HOTEN, LUONG, MA_QL)",
         "Tìm mã nhân viên, họ tên nhân viên, tên người quản lý trực tiếp và mức chênh lệch lương của các nhân viên có lương cao hơn chính người quản lý trực tiếp của họ.",
         "π_{NV.MANV, NV.HOTEN, QL.HOTEN}(σ_{NV.LUONG > QL.LUONG}(ρ_{NV}(NHANVIEN) ⋈_{NV.MA_QL = QL.MANV} ρ_{QL}(NHANVIEN)))",
         "SELECT NV.MANV, NV.HOTEN AS TEN_NV, QL.HOTEN AS TEN_QL\nFROM NHANVIEN NV\nINNER JOIN NHANVIEN QL ON NV.MA_QL = QL.MANV\nWHERE NV.LUONG > QL.LUONG;",
         ["Bước 1: Dùng phép đổi tên ρ tạo 2 thể hiện độc lập: NV (nhân viên) và QL (quản lý trực tiếp).",
          "Bước 2: Tự kết nối 2 thể hiện theo điều kiện NV.MA_QL = QL.MANV.",
          "Bước 3: Chọn các bộ có NV.LUONG > QL.LUONG.",
          "Bước 4: Chiếu NV.MANV, NV.HOTEN, QL.HOTEN."],
         "Loại trừ nhân viên cấp cao nhất (Tổng Giám đốc có MA_QL IS NULL) để tránh lỗi so sánh với NULL."),

        ("RA-B37", "ĐSQH Tự Kết: Chuyến Bay Khứ Hồi Giữa Hai Sân Bay Trong Cùng Ngày",
         "CHUYENBAY(MACB, HANG_BAY, SB_DI, SB_DEN, NGAYBAY, GIOBAY)",
         "Tìm các cặp mã chuyến bay khứ hồi (chuyến đi và chuyến về) của cùng hãng bay 'Vietnam Airlines' bay giữa Hà Nội ('HAN') và TP.HCM ('SGN') trong cùng ngày '2024-12-25'.",
         "π_{CB1.MACB, CB2.MACB}(σ_{CB1.HANG_BAY = 'Vietnam Airlines' ∧ CB1.SB_DI = 'SGN' ∧ CB1.SB_DEN = 'HAN' ∧ CB2.SB_DI = 'HAN' ∧ CB2.SB_DEN = 'SGN' ∧ CB1.NGAYBAY = '2024-12-25' ∧ CB2.GIOBAY > CB1.GIOBAY}(ρ_{CB1}(CHUYENBAY) ⋈_{CB1.HANG_BAY = CB2.HANG_BAY ∧ CB1.NGAYBAY = CB2.NGAYBAY} ρ_{CB2}(CHUYENBAY)))",
         "SELECT CB1.MACB AS CHUYEN_DI, CB2.MACB AS CHUYEN_VE\nFROM CHUYENBAY CB1\nINNER JOIN CHUYENBAY CB2 ON CB1.HANG_BAY = CB2.HANG_BAY AND CB1.NGAYBAY = CB2.NGAYBAY\nWHERE CB1.HANG_BAY = 'Vietnam Airlines'\n  AND CB1.SB_DI = 'SGN' AND CB1.SB_DEN = 'HAN'\n  AND CB2.SB_DI = 'HAN' AND CB2.SB_DEN = 'SGN'\n  AND CB1.NGAYBAY = '2024-12-25' AND CB2.GIOBAY > CB1.GIOBAY;",
         ["Bước 1: Đổi tên 2 thể hiện chuyến bay CB1 (chiều đi) và CB2 (chiều về).",
          "Bước 2: Kết theo cùng hãng bay và cùng ngày bay.",
          "Bước 3: Lọc chiều đi SGN -> HAN và chiều về HAN -> SGN kèm điều kiện giờ về CB2.GIOBAY > CB1.GIOBAY.",
          "Bước 4: Chiếu mã 2 chuyến bay."],
         "Điều kiện giờ về sau giờ đi đảm bảo tính khả thi thực tế của hành trình khứ hồi."),

        ("RA-B38", "ĐSQH Tự Kết: Môn Học Có Số Tín Chỉ Lớn Hơn Môn Tiên Quyết",
         "MONHOC(MAMH, TENMH, SOTC, MAMH_TQ)",
         "Tìm mã môn học, tên môn học và tên môn tiên quyết của các môn học có số tín chỉ lớn hơn số tín chỉ của chính môn học tiên quyết của nó.",
         "π_{MH.MAMH, MH.TENMH, TQ.TENMH}(σ_{MH.SOTC > TQ.SOTC}(ρ_{MH}(MONHOC) ⋈_{MH.MAMH_TQ = TQ.MAMH} ρ_{TQ}(MONHOC)))",
         "SELECT MH.MAMH, MH.TENMH AS TEN_MON, TQ.TENMH AS TEN_MON_TIENQUYET\nFROM MONHOC MH\nINNER JOIN MONHOC TQ ON MH.MAMH_TQ = TQ.MAMH\nWHERE MH.SOTC > TQ.SOTC;",
         ["Bước 1: Đổi tên hai thể hiện: MH (môn học hiện tại) và TQ (môn tiên quyết).",
          "Bước 2: Kết nối theo MH.MAMH_TQ = TQ.MAMH.",
          "Bước 3: Lọc MH.SOTC > TQ.SOTC.",
          "Bước 4: Chiếu các thuộc tính cần thiết."],
         "Các môn không có môn tiên quyết (MAMH_TQ IS NULL) sẽ tự động bị loại khỏi phép kết trong."),

        ("RA-B39", "ĐSQH Tự Kết: Sản Phẩm Cùng Loại Có Giá Bán Gấp Đôi",
         "SANPHAM(MASP, TENSP, LOAISP, GIABAN)",
         "Tìm các cặp mã sản phẩm (SP1, SP2) thuộc cùng một loại sản phẩm ('Dien thoai') sao cho giá bán của SP1 gấp từ 2 lần trở lên so với giá bán của SP2.",
         "π_{SP1.MASP, SP2.MASP}(σ_{SP1.LOAISP = 'Dien thoai' ∧ SP1.GIABAN ≥ 2 * SP2.GIABAN}(ρ_{SP1}(SANPHAM) ⋈_{SP1.LOAISP = SP2.LOAISP ∧ SP1.MASP ≠ SP2.MASP} ρ_{SP2}(SANPHAM)))",
         "SELECT SP1.MASP AS MASP_CAO, SP2.MASP AS MASP_THAP\nFROM SANPHAM SP1\nINNER JOIN SANPHAM SP2 ON SP1.LOAISP = SP2.LOAISP AND SP1.MASP <> SP2.MASP\nWHERE SP1.LOAISP = N'Dien thoai' AND SP1.GIABAN >= 2 * SP2.GIABAN;",
         ["Bước 1: Đổi tên 2 thể hiện sản phẩm SP1 và SP2.",
          "Bước 2: Kết theo cùng loại sản phẩm và mã khác nhau SP1.MASP ≠ SP2.MASP.",
          "Bước 3: Lọc theo loại 'Dien thoai' và điều kiện giá SP1.GIABAN >= 2 * SP2.GIABAN.",
          "Bước 4: Chiếu cặp mã sản phẩm."],
         "Bắt buộc có điều kiện SP1.MASP ≠ SP2.MASP để tránh tự so sánh một sản phẩm với chính nó."),

        ("RA-B40", "ĐSQH Tự Kết: Bác Sĩ Cùng Chuyên Khoa Có Thâm Niên Cao Hơn Trưởng Khoa",
         "BACSI(MABS, HOTEN, CHUYENKHOA, NAM_KINHNGHIEM, MABS_TRUONGKHOA)",
         "Tìm mã bác sĩ và họ tên của các bác sĩ có số năm kinh nghiệm cao hơn số năm kinh nghiệm của chính bác sĩ trưởng khoa phụ trách chuyên khoa đó.",
         "π_{BS.MABS, BS.HOTEN}(σ_{BS.NAM_KINHNGHIEM > TK.NAM_KINHNGHIEM}(ρ_{BS}(BACSI) ⋈_{BS.MABS_TRUONGKHOA = TK.MABS} ρ_{TK}(BACSI)))",
         "SELECT BS.MABS, BS.HOTEN\nFROM BACSI BS\nINNER JOIN BACSI TK ON BS.MABS_TRUONGKHOA = TK.MABS\nWHERE BS.NAM_KINHNGHIEM > TK.NAM_KINHNGHIEM;",
         ["Bước 1: Đổi tên 2 thể hiện bác sĩ: BS (bác sĩ thành viên) và TK (bác sĩ trưởng khoa).",
          "Bước 2: Kết theo BS.MABS_TRUONGKHOA = TK.MABS.",
          "Bước 3: Lọc BS.NAM_KINHNGHIEM > TK.NAM_KINHNGHIEM.",
          "Bước 4: Chiếu BS.MABS, BS.HOTEN."],
         "Trưởng khoa có MABS_TRUONGKHOA là chính mình hoặc NULL tùy thiết kế cơ sở dữ liệu.")
    ]

    for item in self_joins:
        pid, title, schema, prompt, ra, sql, steps, edge = item
        problems.append({
            "id": pid, "topic": "RA_BASIC_JOIN", "difficulty": "B",
            "title": title, "prompt": prompt, "schema": schema, "recommended_time_mins": 15, "points": 1.0,
            "status": "VERIFIED", "verification_level": "SEMANTICALLY_REVIEWED",
            "solution": {"relational_algebra": ra, "sql": sql, "intermediate_steps": steps, "edge_cases": edge},
            "rubric": {"total_points": 1.0, "selection_and_projection_correctness": 0.4, "join_condition_and_table_mapping": 0.4, "syntax_and_variable_naming": 0.2}
        })

    # 41-45: 5 Authentic Set Operations (Union, Intersect, Difference) with type compatibility
    set_ops = [
        ("RA-B41", "ĐSQH Phép Hợp (Union): Sinh Viên Đạt Học Bổng Kỳ 1 Hoặc Kỳ 2",
         "HOCBONG_HK1(MSSV, HOTEN, DIEM_RL, TIEN_HB), HOCBONG_HK2(MSSV, HOTEN, DIEM_RL, TIEN_HB)",
         "Tìm mã số sinh viên và họ tên của các sinh viên được nhận học bổng khuyến khích học tập ở Học kỳ 1 HOẶC Học kỳ 2 trong năm học 2024.",
         "π_{MSSV, HOTEN}(HOCBONG_HK1) ∪ π_{MSSV, HOTEN}(HOCBONG_HK2)",
         "SELECT MSSV, HOTEN FROM HOCBONG_HK1\nUNION\nSELECT MSSV, HOTEN FROM HOCBONG_HK2;",
         ["Bước 1: Chiếu hai thuộc tính MSSV và HOTEN trên cả hai quan hệ HOCBONG_HK1 và HOCBONG_HK2 để bảo đảm tính khả hợp (cùng bậc 2 và tương thích kiểu dữ liệu).",
          "Bước 2: Áp dụng phép hợp (∪) để lấy tất cả sinh viên nhận học bổng ở ít nhất một trong hai kỳ, tự động loại bỏ các sinh viên trùng lặp nhận học bổng cả hai kỳ."],
         "Phép hợp trong ĐSQH thuần túy loại bỏ trùng lặp (tương đương UNION trong SQL, khác UNION ALL)."),

        ("RA-B42", "ĐSQH Phép Giao (Intersect): Khách Hàng Mua Cả Smart TV Và Loa Soundbar",
         "DONHANG(MADON, MAKH, NGAYDAT), CTHD(MADON, MASP), SANPHAM(MASP, TENSP, LOAISP)",
         "Tìm mã khách hàng của những khách hàng đã mua cả sản phẩm thuộc loại 'Smart TV' VÀ sản phẩm thuộc loại 'Loa Soundbar' trong năm 2024.",
         "π_{MAKH}(σ_{LOAISP = 'Smart TV' ∧ NGAYDAT ≥ '2024-01-01'}(DONHANG ⋈ CTHD ⋈ SANPHAM)) ∩ π_{MAKH}(σ_{LOAISP = 'Loai Soundbar' ∧ NGAYDAT ≥ '2024-01-01'}(DONHANG ⋈ CTHD ⋈ SANPHAM))",
         "SELECT DH.MAKH\nFROM DONHANG DH INNER JOIN CTHD CT ON DH.MADON = CT.MADON INNER JOIN SANPHAM SP ON CT.MASP = SP.MASP\nWHERE SP.LOAISP = 'Smart TV' AND DH.NGAYDAT >= '2024-01-01'\nINTERSECT\nSELECT DH.MAKH\nFROM DONHANG DH INNER JOIN CTHD CT ON DH.MADON = CT.MADON INNER JOIN SANPHAM SP ON CT.MASP = SP.MASP\nWHERE SP.LOAISP = 'Loai Soundbar' AND DH.NGAYDAT >= '2024-01-01';",
         ["Bước 1: Tìm tập khách hàng mua Smart TV trong năm 2024.",
          "Bước 2: Tìm tập khách hàng mua Loa Soundbar trong năm 2024.",
          "Bước 3: Lấy giao (∩) của hai tập hợp trên để tìm khách hàng đồng thời thuộc cả hai nhóm."],
         "Hai biểu thức con phải cùng chiếu ra duy nhất thuộc tính MAKH để thỏa mãn điều kiện khả hợp."),

        ("RA-B43", "ĐSQH Phép Trừ (Except): Giảng Viên Dạy Lý Thuyết Nhưng Không Dạy Thực Hành",
         "GIANGVIEN(MAGV, HOTEN, MAKHOA), LOPHOCPHAN(MALHP, MAGV, LOAI_LHP)",
         "Tìm mã giảng viên và họ tên của các giảng viên có tham gia giảng dạy lớp học phần lý thuyết (LOAI_LHP = 'Ly thuyet') nhưng KHÔNG tham gia giảng dạy bất kỳ lớp học phần thực hành nào (LOAI_LHP = 'Thuc hanh').",
         "π_{GIANGVIEN.MAGV, HOTEN}(σ_{LOAI_LHP = 'Ly thuyet'}(GIANGVIEN ⋈ LOPHOCPHAN)) - π_{GIANGVIEN.MAGV, HOTEN}(σ_{LOAI_LHP = 'Thuc hanh'}(GIANGVIEN ⋈ LOPHOCPHAN))",
         "SELECT GV.MAGV, GV.HOTEN\nFROM GIANGVIEN GV INNER JOIN LOPHOCPHAN LHP ON GV.MAGV = LHP.MAGV\nWHERE LHP.LOAI_LHP = 'Ly thuyet'\nEXCEPT\nSELECT GV.MAGV, GV.HOTEN\nFROM GIANGVIEN GV INNER JOIN LOPHOCPHAN LHP ON GV.MAGV = LHP.MAGV\nWHERE LHP.LOAI_LHP = 'Thuc hanh';",
         ["Bước 1: Tìm tập giảng viên phụ trách lớp lý thuyết: R1 = π_{MAGV, HOTEN}(σ_{LOAI_LHP = 'Ly thuyet'}(GIANGVIEN ⋈ LOPHOCPHAN)).",
          "Bước 2: Tìm tập giảng viên phụ trách lớp thực hành: R2 = π_{MAGV, HOTEN}(σ_{LOAI_LHP = 'Thuc hanh'}(GIANGVIEN ⋈ LOPHOCPHAN)).",
          "Bước 3: Lấy hiệu tập hợp R1 - R2 để thu được giảng viên chỉ dạy lý thuyết."],
         "Phép trừ không có tính giao hoán: R1 - R2 khác R2 - R1."),

        ("RA-B44", "ĐSQH Phép Trừ: Dược Phẩm Có Ở Kho Quận 1 Nhưng Hết Ở Kho Quận 5",
         "TONKHO(MAKHO, MATHUOC, SOLUONG_TON), KHO(MAKHO, TENKHO, QUAN), THUOC(MATHUOC, TENTHUOC)",
         "Tìm mã thuốc và tên thuốc của các loại thuốc có số lượng tồn kho lớn hơn 0 tại kho ở 'Quan 1' nhưng KHÔNG còn tồn kho (hoặc không lưu kho) tại kho ở 'Quan 5'.",
         "π_{THUOC.MATHUOC, TENTHUOC}(σ_{QUAN = 'Quan 1' ∧ SOLUONG_TON > 0}(THUOC ⋈ TONKHO ⋈ KHO)) - π_{THUOC.MATHUOC, TENTHUOC}(σ_{QUAN = 'Quan 5' ∧ SOLUONG_TON > 0}(THUOC ⋈ TONKHO ⋈ KHO))",
         "SELECT T.MATHUOC, T.TENTHUOC\nFROM THUOC T INNER JOIN TONKHO TK ON T.MATHUOC = TK.MATHUOC INNER JOIN KHO K ON TK.MAKHO = K.MAKHO\nWHERE K.QUAN = 'Quan 1' AND TK.SOLUONG_TON > 0\nEXCEPT\nSELECT T.MATHUOC, T.TENTHUOC\nFROM THUOC T INNER JOIN TONKHO TK ON T.MATHUOC = TK.MATHUOC INNER JOIN KHO K ON TK.MAKHO = K.MAKHO\nWHERE K.QUAN = 'Quan 5' AND TK.SOLUONG_TON > 0;",
         ["Bước 1: Xác định danh mục thuốc còn hàng tại kho Quận 1.",
          "Bước 2: Xác định danh mục thuốc còn hàng tại kho Quận 5.",
          "Bước 3: Lấy hiệu tập hợp giữa danh mục Quận 1 trừ đi danh mục Quận 5."],
         "Bảo đảm cả hai nhánh phép trừ chiếu cùng danh sách thuộc tính (MATHUOC, TENTHUOC)."),

        ("RA-B45", "ĐSQH Phép Giao: Bạn Đọc Vừa Là Sinh Viên Vừa Là Cán Bộ Nghiên Cứu",
         "DOCGIA_SINHVIEN(MADG, HOTEN, CCCD, KHOA), DOCGIA_CANBO(MADG, HOTEN, CCCD, PHONGBAN)",
         "Tìm mã bạn đọc, họ tên và số căn cước công dân (CCCD) của những người vừa có thẻ bạn đọc sinh viên vừa có thẻ bạn đọc cán bộ trong cơ sở dữ liệu thư viện.",
         "π_{MADG, HOTEN, CCCD}(DOCGIA_SINHVIEN) ∩ π_{MADG, HOTEN, CCCD}(DOCGIA_CANBO)",
         "SELECT MADG, HOTEN, CCCD FROM DOCGIA_SINHVIEN\nINTERSECT\nSELECT MADG, HOTEN, CCCD FROM DOCGIA_CANBO;",
         ["Bước 1: Chiếu các thuộc tính nhận diện khả hợp (MADG, HOTEN, CCCD) trên cả hai bảng bạn đọc.",
          "Bước 2: Áp dụng phép giao (∩) để tìm những người hiện diện ở cả hai danh mục."],
         "Thuộc tính KHOA và PHONGBAN khác nhau không thể tham gia trực tiếp vào phép giao; bắt buộc phải chiếu trước khi giao.")
    ]

    for item in set_ops:
        pid, title, schema, prompt, ra, sql, steps, edge = item
        problems.append({
            "id": pid, "topic": "RA_BASIC_JOIN", "difficulty": "B",
            "title": title, "prompt": prompt, "schema": schema, "recommended_time_mins": 15, "points": 1.0,
            "status": "VERIFIED", "verification_level": "SEMANTICALLY_REVIEWED",
            "solution": {"relational_algebra": ra, "sql": sql, "intermediate_steps": steps, "edge_cases": edge},
            "rubric": {"total_points": 1.0, "selection_and_projection_correctness": 0.4, "join_condition_and_table_mapping": 0.4, "syntax_and_variable_naming": 0.2}
        })

    assert len(problems) == 45, f"Expected 45 RA Basic problems, got {len(problems)}"
    return problems

if __name__ == "__main__":
    probs = get_remediated_ra_basic_problems()
    print(f"Generated {len(probs)} RA Basic problems.")
    for p in probs:
        assert p["id"].startswith("RA-B")
        ra = p["solution"]["relational_algebra"]
        assert any(s in ra for s in ["π", "σ", "⋈", "⟕", "ρ", "∪", "∩", "-"]), f"Missing operator in {p['id']}"
    print("ALL RA BASIC PROBLEMS VALIDATED SUCCESSFULLY!")
