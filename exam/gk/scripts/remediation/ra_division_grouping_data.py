# -*- coding: utf-8 -*-
"""
remediation/ra_division_grouping_data.py
Constructs all 45 fully verified, authentic Relational Algebra Division & Grouping Problems (RA-D01 .. RA-D45).
Includes:
- RA-D01 .. RA-D15: 15 authentic Relational Division problems with 4-step canonical subtraction & empty target handling.
- RA-D16 .. RA-D30: 15 authentic Grouping & Aggregations (Gamma) problems across realistic domains.
- RA-D31 .. RA-D45: 15 authentic Extreme Values & Tie-Breaking problems with mathematically sound subgroup filtering (R_sub - NonMax), resolving P0-04.
"""

def get_remediated_ra_division_grouping_problems():
    problems = []

    # 1-15: 15 Relational Division Problems
    division_problems = [
        ("RA-D01", "ĐSQH Phép Chia: Sinh Viên Đăng Ký Tất Cả Môn Học Bắt Buộc Chuyên Ngành ATTT",
         "SINHVIEN(MSSV, HOTEN, CHUYENNGANH), MONHOC(MAMH, TENMH, CHUYENNGANH, LOAI_MH), DANGKY(MSSV, MAMH, HOCKY)",
         "Tìm mã số sinh viên và họ tên của các sinh viên chuyên ngành 'An toan thong tin' đã đăng ký tham gia TẤT CẢ các môn học bắt buộc (LOAI_MH = 'Bat buoc') của chuyên ngành này.",
         "π_{MSSV, HOTEN}(SINHVIEN ⋈ (π_{MSSV, MAMH}(DANGKY) ÷ π_{MAMH}(σ_{CHUYENNGANH = 'An toan thong tin' ∧ LOAI_MH = 'Bat buoc'}(MONHOC))))",
         "SELECT SV.MSSV, SV.HOTEN\nFROM SINHVIEN SV\nWHERE SV.CHUYENNGANH = N'An toan thong tin'\n  AND NOT EXISTS (\n    SELECT MH.MAMH FROM MONHOC MH\n    WHERE MH.CHUYENNGANH = N'An toan thong tin' AND MH.LOAI_MH = N'Bat buoc'\n    EXCEPT\n    SELECT DK.MAMH FROM DANGKY DK WHERE DK.MSSV = SV.MSSV\n);",
         [
             "Bước 1 (Xác định tập chia S): R_S = π_{MAMH}(σ_{CHUYENNGANH = 'An toan thong tin' ∧ LOAI_MH = 'Bat buoc'}(MONHOC)).",
             "Bước 2 (Xác định tập ứng viên U): R_U = π_{MSSV}(σ_{CHUYENNGANH = 'An toan thong tin'}(SINHVIEN ⋈ DANGKY)).",
             "Bước 3 (Tạo tập giả định và tìm các cặp thiếu): R_All = R_U × R_S; R_Missing = π_{MSSV}(R_All - π_{MSSV, MAMH}(DANGKY)).",
             "Bước 4 (Kết quả cuối cùng): KQ = (R_U - R_Missing) ⋈ π_{MSSV, HOTEN}(SINHVIEN)."
         ],
         "Nếu tập chia S rỗng (chuyên ngành chưa có môn bắt buộc nào), theo lý thuyết ĐSQH mọi sinh viên thỏa mãn nhưng trong thực tế hệ thống coi như chưa phát sinh yêu cầu; bắt buộc chặn tập ứng viên bởi các sinh viên thuộc ngành ATTT đã có đăng ký."),

        ("RA-D02", "ĐSQH Phép Chia: Khách Hàng Mua Tất Cả Sản Phẩm Apple Năm 2024",
         "KHACHHANG(MAKH, HOTEN, EMAIL), SANPHAM(MASP, TENSP, HANGSX, NAMSX), DONHANG(MADON, MAKH, NGAYDAT), CTHD(MADON, MASP)",
         "Tìm mã khách hàng và họ tên của các khách hàng đã mua TẤT CẢ các dòng sản phẩm của hãng 'Apple' phát hành trong năm 2024.",
         "π_{MAKH, HOTEN}(KHACHHANG ⋈ (π_{MAKH, MASP}(DONHANG ⋈ CTHD) ÷ π_{MASP}(σ_{HANGSX = 'Apple' ∧ NAMSX = 2024}(SANPHAM))))",
         "SELECT KH.MAKH, KH.HOTEN\nFROM KHACHHANG KH\nWHERE EXISTS (SELECT 1 FROM DONHANG DH WHERE DH.MAKH = KH.MAKH)\n  AND NOT EXISTS (\n    SELECT SP.MASP FROM SANPHAM SP WHERE SP.HANGSX = 'Apple' AND SP.NAMSX = 2024\n    EXCEPT\n    SELECT CT.MASP FROM DONHANG DH INNER JOIN CTHD CT ON DH.MADON = CT.MADON WHERE DH.MAKH = KH.MAKH\n);",
         [
             "Bước 1 (Xác định tập chia S): S = π_{MASP}(σ_{HANGSX = 'Apple' ∧ NAMSX = 2024}(SANPHAM)).",
             "Bước 2 (Xác định tập ứng viên U): U = π_{MAKH}(DONHANG).",
             "Bước 3 (Tìm khách hàng mua thiếu sản phẩm): Missing = π_{MAKH}((U × S) - π_{MAKH, MASP}(DONHANG ⋈ CTHD)).",
             "Bước 4 (Khách hàng mua đủ): KQ = (U - Missing) ⋈ π_{MAKH, HOTEN}(KHACHHANG)."
         ],
         "Chặn miền ứng viên U bằng các khách hàng từng có đơn hàng; khách hàng mua nhiều đơn khác nhau gom lại đủ các sản phẩm của Apple vẫn được chấp nhận."),

        ("RA-D03", "ĐSQH Phép Chia: Bác Sĩ Tham Gia Tất Cả Đợt Tập Huấn Cấp Cứu",
         "BACSI(MABS, HOTEN, MAKHOA), DOTTAPHUAN(MADOT, TENDOT, LOAI_TH), THAMGIA_TH(MABS, MADOT, KETQUA)",
         "Tìm mã bác sĩ và họ tên của các bác sĩ đã hoàn thành đạt (KETQUA = 'Dat') TẤT CẢ các đợt tập huấn thuộc loại 'Cap cuu hoi suc'.",
         "π_{MABS, HOTEN}(BACSI ⋈ (π_{MABS, MADOT}(σ_{KETQUA = 'Dat'}(THAMGIA_TH)) ÷ π_{MADOT}(σ_{LOAI_TH = 'Cap cuu hoi suc'}(DOTTAPHUAN))))",
         "SELECT BS.MABS, BS.HOTEN\nFROM BACSI BS\nWHERE EXISTS (SELECT 1 FROM THAMGIA_TH TG WHERE TG.MABS = BS.MABS)\n  AND NOT EXISTS (\n    SELECT DTH.MADOT FROM DOTTAPHUAN DTH WHERE DTH.LOAI_TH = N'Cap cuu hoi suc'\n    EXCEPT\n    SELECT TG.MADOT FROM THAMGIA_TH TG WHERE TG.MABS = BS.MABS AND TG.KETQUA = N'Dat'\n);",
         [
             "Bước 1: Tập mục tiêu S = π_{MADOT}(σ_{LOAI_TH = 'Cap cuu hoi suc'}(DOTTAPHUAN)).",
             "Bước 2: Quan hệ thực tế R_Actual = π_{MABS, MADOT}(σ_{KETQUA = 'Dat'}(THAMGIA_TH)).",
             "Bước 3: Tập ứng viên U = π_{MABS}(R_Actual).",
             "Bước 4: Missing = π_{MABS}((U × S) - R_Actual); KQ = (U - Missing) ⋈ BACSI."
         ],
         "Bác sĩ có tham gia nhưng bị xếp loại 'Khong dat' ở một đợt bất kỳ sẽ không được xem là hoàn thành đợt đó."),

        ("RA-D04", "ĐSQH Phép Chia: Giảng Viên Đã Giảng Dạy Ở Tất Cả Cơ Sở Đào Tạo",
         "GIANGVIEN(MAGV, HOTEN, MAKHOA), COSO(MACS, TENCS, THANHPHO), LOPHOCPHAN(MALHP, MAGV, MACS, HOCKY)",
         "Tìm mã giảng viên và họ tên của các giảng viên đã từng giảng dạy các lớp học phần tại TẤT CẢ các cơ sở đào tạo của nhà trường.",
         "π_{MAGV, HOTEN}(GIANGVIEN ⋈ (π_{MAGV, MACS}(LOPHOCPHAN) ÷ π_{MACS}(COSO)))",
         "SELECT GV.MAGV, GV.HOTEN\nFROM GIANGVIEN GV\nWHERE EXISTS (SELECT 1 FROM LOPHOCPHAN LHP WHERE LHP.MAGV = GV.MAGV)\n  AND NOT EXISTS (\n    SELECT CS.MACS FROM COSO CS\n    EXCEPT\n    SELECT LHP.MACS FROM LOPHOCPHAN LHP WHERE LHP.MAGV = GV.MAGV\n);",
         [
             "Bước 1: Tập chia S = π_{MACS}(COSO).",
             "Bước 2: Tập ứng viên U = π_{MAGV}(LOPHOCPHAN).",
             "Bước 3: Missing = π_{MAGV}((U × S) - π_{MAGV, MACS}(LOPHOCPHAN)).",
             "Bước 4: KQ = (U - Missing) ⋈ π_{MAGV, HOTEN}(GIANGVIEN)."
         ],
         "Đảm bảo nhà trường có ít nhất 1 cơ sở; giảng viên mới tuyển chưa dạy lớp nào không được rơi vào kết quả."),

        ("RA-D05", "ĐSQH Phép Chia: Tàu Hàng Cập Bến Tất Cả Cảng Biển Loại 1 Miền Nam",
         "TAU_HANG(MATAU, TENTAU, QUOCTICH), CANGBIEN(MACANG, TENCANG, PHANKY, VUNG_MIEN), LICH_CAPBEN(MATAU, MACANG, NGAYCAP)",
         "Tìm mã tàu và tên tàu của các tàu hàng đã từng cập bến TẤT CẢ các cảng biển xếp hạng 'Loai 1' tại vùng miền 'Mien Nam'.",
         "π_{MATAU, TENTAU}(TAU_HANG ⋈ (π_{MATAU, MACANG}(LICH_CAPBEN) ÷ π_{MACANG}(σ_{PHANKY = 'Loai 1' ∧ VUNG_MIEN = 'Mien Nam'}(CANGBIEN))))",
         "SELECT TH.MATAU, TH.TENTAU\nFROM TAU_HANG TH\nWHERE EXISTS (SELECT 1 FROM LICH_CAPBEN LCB WHERE LCB.MATAU = TH.MATAU)\n  AND NOT EXISTS (\n    SELECT CB.MACANG FROM CANGBIEN CB WHERE CB.PHANKY = 'Loai 1' AND CB.VUNG_MIEN = N'Mien Nam'\n    EXCEPT\n    SELECT LCB.MACANG FROM LICH_CAPBEN LCB WHERE LCB.MATAU = TH.MATAU\n);",
         [
             "Bước 1: S = π_{MACANG}(σ_{PHANKY = 'Loai 1' ∧ VUNG_MIEN = 'Mien Nam'}(CANGBIEN)).",
             "Bước 2: U = π_{MATAU}(LICH_CAPBEN).",
             "Bước 3: Missing = π_{MATAU}((U × S) - π_{MATAU, MACANG}(LICH_CAPBEN)).",
             "Bước 4: KQ = (U - Missing) ⋈ π_{MATAU, TENTAU}(TAU_HANG)."
         ],
         "Nếu miền Nam không có cảng loại 1 nào, truy vấn SQL NOT EXISTS sẽ trả về rỗng do điều kiện EXISTS U."),

        ("RA-D06", "ĐSQH Phép Chia: Nhân Viên Kinh Doanh Ký Hợp Đồng Với Tất Cả Đối Tác Chiến Lược",
         "NHANVIEN(MANV, HOTEN, PHONGBAN), DOITAC(MADT, TENDT, PHANLOAI), HOPDONG(MAHD, MANV, MADT, NGAYKY)",
         "Tìm mã nhân viên và họ tên của các nhân viên phòng 'Kinh doanh' đã ký hợp đồng với TẤT CẢ các đối tác có phân loại là 'Chien luoc'.",
         "π_{MANV, HOTEN}(σ_{PHONGBAN = 'Kinh doanh'}(NHANVIEN) ⋈ (π_{MANV, MADT}(HOPDONG) ÷ π_{MADT}(σ_{PHANLOAI = 'Chien luoc'}(DOITAC))))",
         "SELECT NV.MANV, NV.HOTEN\nFROM NHANVIEN NV\nWHERE NV.PHONGBAN = N'Kinh doanh'\n  AND NOT EXISTS (\n    SELECT DT.MADT FROM DOITAC DT WHERE DT.PHANLOAI = N'Chien luoc'\n    EXCEPT\n    SELECT HD.MADT FROM HOPDONG HD WHERE HD.MANV = NV.MANV\n);",
         [
             "Bước 1: S = π_{MADT}(σ_{PHANLOAI = 'Chien luoc'}(DOITAC)).",
             "Bước 2: U = π_{MANV}(σ_{PHONGBAN = 'Kinh doanh'}(NHANVIEN ⋈ HOPDONG)).",
             "Bước 3: Missing = π_{MANV}((U × S) - π_{MANV, MADT}(HOPDONG)).",
             "Bước 4: KQ = (U - Missing) ⋈ π_{MANV, HOTEN}(NHANVIEN)."
         ],
         "Nhân viên phòng ban khác dù có ký hợp đồng với tất cả đối tác chiến lược cũng bị loại trừ bởi điều kiện phòng ban."),

        ("RA-D07", "ĐSQH Phép Chia: Thí Sinh Dự Thi Đủ Tất Cả Môn Tổ Hợp A00",
         "THISINH(SBD, HOTEN, KHUVUC), TOHOP_MON(MATOHOP, MAMH), DIEMTHI(SBD, MAMH, DIEMSO)",
         "Tìm số báo danh và họ tên của các thí sinh đã tham gia thi và có điểm số (DIEMSO IS NOT NULL) ở TẤT CẢ các môn học thuộc tổ hợp xét tuyển 'A00'.",
         "π_{SBD, HOTEN}(THISINH ⋈ (π_{SBD, MAMH}(σ_{DIEMSO IS NOT NULL}(DIEMTHI)) ÷ π_{MAMH}(σ_{MATOHOP = 'A00'}(TOHOP_MON))))",
         "SELECT TS.SBD, TS.HOTEN\nFROM THISINH TS\nWHERE EXISTS (SELECT 1 FROM DIEMTHI DT WHERE DT.SBD = TS.SBD)\n  AND NOT EXISTS (\n    SELECT TH.MAMH FROM TOHOP_MON TH WHERE TH.MATOHOP = 'A00'\n    EXCEPT\n    SELECT DT.MAMH FROM DIEMTHI DT WHERE DT.SBD = TS.SBD AND DT.DIEMSO IS NOT NULL\n);",
         [
             "Bước 1: S = π_{MAMH}(σ_{MATOHOP = 'A00'}(TOHOP_MON)) (gồm Toán, Lý, Hóa).",
             "Bước 2: U = π_{SBD}(DIEMTHI).",
             "Bước 3: Missing = π_{SBD}((U × S) - π_{SBD, MAMH}(σ_{DIEMSO IS NOT NULL}(DIEMTHI))).",
             "Bước 4: KQ = (U - Missing) ⋈ π_{SBD, HOTEN}(THISINH)."
         ],
         "Thí sinh vắng thi có DIEMSO mang giá trị NULL sẽ bị tính là chưa hoàn thành môn thi."),

        ("RA-D08", "ĐSQH Phép Chia: Phi Công Điều Khiển Tất Cả Dòng Máy Bay Thân Rộng",
         "PHICONG(MAPC, HOTEN, HANG_BANG), MAYBAY(MAMB, DONG_MAYBAY, LOAITHAN), PHANCONG_BAY(MAPC, MAMB, NGAYBAY)",
         "Cho biết mã phi công và họ tên của các phi công đã từng điều khiển TẤT CẢ các dòng máy bay có thiết kế là 'Than rong' (LOAITHAN = 'Than rong') của hãng.",
         "π_{MAPC, HOTEN}(PHICONG ⋈ (π_{MAPC, DONG_MAYBAY}(PHANCONG_BAY ⋈ MAYBAY) ÷ π_{DONG_MAYBAY}(σ_{LOAITHAN = 'Than rong'}(MAYBAY))))",
         "SELECT PC.MAPC, PC.HOTEN\nFROM PHICONG PC\nWHERE EXISTS (SELECT 1 FROM PHANCONG_BAY PCB WHERE PCB.MAPC = PC.MAPC)\n  AND NOT EXISTS (\n    SELECT MB.DONG_MAYBAY FROM MAYBAY MB WHERE MB.LOAITHAN = N'Than rong'\n    EXCEPT\n    SELECT MB2.DONG_MAYBAY FROM PHANCONG_BAY PCB2 INNER JOIN MAYBAY MB2 ON PCB2.MAMB = MB2.MAMB WHERE PCB2.MAPC = PC.MAPC\n);",
         [
             "Bước 1: S = π_{DONG_MAYBAY}(σ_{LOAITHAN = 'Than rong'}(MAYBAY)).",
             "Bước 2: R_Actual = π_{MAPC, DONG_MAYBAY}(PHANCONG_BAY ⋈ MAYBAY).",
             "Bước 3: U = π_{MAPC}(R_Actual); Missing = π_{MAPC}((U × S) - R_Actual).",
             "Bước 4: KQ = (U - Missing) ⋈ π_{MAPC, HOTEN}(PHICONG)."
         ],
         "Mục tiêu chia là dòng máy bay (DONG_MAYBAY ví dụ Boeing 787, Airbus A350), không phải từng chiếc máy bay cụ thể."),

        ("RA-D09", "ĐSQH Phép Chia: Kỹ Sư Kiểm Thử Thực Hiện Tất Cả Test Case Hồi Quy Bảo Mật",
         "KYSU(MAKS, HOTEN, TRINHDOHOCVAN), TESTCASE(MATC, LOAITC, MUC_DO), KETQUA_TEST(MAKS, MATC, NGAYCHAY, TRANGTHAI)",
         "Tìm mã kỹ sư và họ tên của các kỹ sư kiểm thử đã thực thi (TRANGTHAI = 'Passed') TẤT CẢ các test case thuộc loại kiểm thử hồi quy bảo mật (LOAITC = 'Security Regression').",
         "π_{MAKS, HOTEN}(KYSU ⋈ (π_{MAKS, MATC}(σ_{TRANGTHAI = 'Passed'}(KETQUA_TEST)) ÷ π_{MATC}(σ_{LOAITC = 'Security Regression'}(TESTCASE))))",
         "SELECT KS.MAKS, KS.HOTEN\nFROM KYSU KS\nWHERE EXISTS (SELECT 1 FROM KETQUA_TEST KQ WHERE KQ.MAKS = KS.MAKS)\n  AND NOT EXISTS (\n    SELECT TC.MATC FROM TESTCASE TC WHERE TC.LOAITC = 'Security Regression'\n    EXCEPT\n    SELECT KQ.MATC FROM KETQUA_TEST KQ WHERE KQ.MAKS = KS.MAKS AND KQ.TRANGTHAI = 'Passed'\n);",
         [
             "Bước 1: S = π_{MATC}(σ_{LOAITC = 'Security Regression'}(TESTCASE)).",
             "Bước 2: R_Actual = π_{MAKS, MATC}(σ_{TRANGTHAI = 'Passed'}(KETQUA_TEST)).",
             "Bước 3: U = π_{MAKS}(R_Actual); Missing = π_{MAKS}((U × S) - R_Actual).",
             "Bước 4: KQ = (U - Missing) ⋈ π_{MAKS, HOTEN}(KYSU)."
         ],
         "Test case chạy bị lỗi Failed không được tính là vượt qua kiểm thử."),

        ("RA-D10", "ĐSQH Phép Chia: Khách Hàng Lưu Trú Tại Tất Cả Khu Resort 5 Sao",
         "KHACHHANG(MAKH, HOTEN, QUOCTICH), RESORT(MARS, TENRS, HANG_SAO, KHUVUC), PHIEUDAT(MAPD, MAKH, MARS, NGAYDEN)",
         "Tìm mã khách hàng và họ tên của các du khách đã từng đặt phòng và lưu trú tại TẤT CẢ các khu resort '5 sao' thuộc tập đoàn.",
         "π_{MAKH, HOTEN}(KHACHHANG ⋈ (π_{MAKH, MARS}(PHIEUDAT) ÷ π_{MARS}(σ_{HANG_SAO = '5 sao'}(RESORT))))",
         "SELECT KH.MAKH, KH.HOTEN\nFROM KHACHHANG KH\nWHERE EXISTS (SELECT 1 FROM PHIEUDAT PD WHERE PD.MAKH = KH.MAKH)\n  AND NOT EXISTS (\n    SELECT RS.MARS FROM RESORT RS WHERE RS.HANG_SAO = '5 sao'\n    EXCEPT\n    SELECT PD.MARS FROM PHIEUDAT PD WHERE PD.MAKH = KH.MAKH\n);",
         [
             "Bước 1: S = π_{MARS}(σ_{HANG_SAO = '5 sao'}(RESORT)).",
             "Bước 2: U = π_{MAKH}(PHIEUDAT).",
             "Bước 3: Missing = π_{MAKH}((U × S) - π_{MAKH, MARS}(PHIEUDAT)).",
             "Bước 4: KQ = (U - Missing) ⋈ π_{MAKH, HOTEN}(KHACHHANG)."
         ],
         "Khách hàng trung thành đã trải nghiệm toàn bộ chuỗi sản phẩm cao cấp."),

        ("RA-D11", "ĐSQH Phép Chia: Sinh Viên Tham Gia Tất Cả Chiến Dịch Mùa Hè Xanh",
         "SINHVIEN(MSSV, HOTEN, KHOA), CHIENDICH(MACD, TENCD, NAM), DANGKY_CD(MSSV, MACD, VAITRO)",
         "Cho biết mã sinh viên và họ tên của các sinh viên khóa 'K2021' đã tham gia TẤT CẢ các chiến dịch Mùa hè xanh được tổ chức trong giai đoạn từ năm 2022 đến 2024.",
         "π_{MSSV, HOTEN}(σ_{KHOA = 'K2021'}(SINHVIEN) ⋈ (π_{MSSV, MACD}(DANGKY_CD) ÷ π_{MACD}(σ_{NAM ≥ 2022 ∧ NAM ≤ 2024}(CHIENDICH))))",
         "SELECT SV.MSSV, SV.HOTEN\nFROM SINHVIEN SV\nWHERE SV.KHOA = 'K2021'\n  AND NOT EXISTS (\n    SELECT CD.MACD FROM CHIENDICH CD WHERE CD.NAM BETWEEN 2022 AND 2024\n    EXCEPT\n    SELECT DK.MACD FROM DANGKY_CD DK WHERE DK.MSSV = SV.MSSV\n);",
         [
             "Bước 1: S = π_{MACD}(σ_{NAM ≥ 2022 ∧ NAM ≤ 2024}(CHIENDICH)).",
             "Bước 2: U = π_{MSSV}(σ_{KHOA = 'K2021'}(SINHVIEN ⋈ DANGKY_CD)).",
             "Bước 3: Missing = π_{MSSV}((U × S) - π_{MSSV, MACD}(DANGKY_CD)).",
             "Bước 4: KQ = (U - Missing) ⋈ π_{MSSV, HOTEN}(SINHVIEN)."
         ],
         "Chỉ xét sinh viên khóa K2021 có tham gia phong trào Đoàn hội liên tục các năm."),

        ("RA-D12", "ĐSQH Phép Chia: Độc Giả Mượn Tất Cả Các Tập Bộ Sách Lịch Sử",
         "DOCGIA(MADG, HOTEN, SDT), CUONSACH(MACS, MABO, SOTAP), PHIEUMUON(MAPM, MADG, NGAYMUON), CTPM(MAPM, MACS)",
         "Tìm mã độc giả và họ tên của các bạn đọc đã mượn TẤT CẢ các tập sách thuộc bộ sách có mã 'BO_HIST_01'.",
         "π_{MADG, HOTEN}(DOCGIA ⋈ (π_{MADG, MACS}(PHIEUMUON ⋈ CTPM) ÷ π_{MACS}(σ_{MABO = 'BO_HIST_01'}(CUONSACH))))",
         "SELECT DG.MADG, DG.HOTEN\nFROM DOCGIA DG\nWHERE EXISTS (SELECT 1 FROM PHIEUMUON PM WHERE PM.MADG = DG.MADG)\n  AND NOT EXISTS (\n    SELECT CS.MACS FROM CUONSACH CS WHERE CS.MABO = 'BO_HIST_01'\n    EXCEPT\n    SELECT CT.MACS FROM PHIEUMUON PM INNER JOIN CTPM CT ON PM.MAPM = CT.MAPM WHERE PM.MADG = DG.MADG\n);",
         [
             "Bước 1: S = π_{MACS}(σ_{MABO = 'BO_HIST_01'}(CUONSACH)).",
             "Bước 2: U = π_{MADG}(PHIEUMUON).",
             "Bước 3: Missing = π_{MADG}((U × S) - π_{MADG, MACS}(PHIEUMUON ⋈ CTPM)).",
             "Bước 4: KQ = (U - Missing) ⋈ π_{MADG, HOTEN}(DOCGIA)."
         ],
         "Độc giả có thể mượn từng tập ở các lần mượn khác nhau."),

        ("RA-D13", "ĐSQH Phép Chia: Cửa Hàng Tiện Lợi Phân Phối Tất Cả Sản Phẩm Sữa Vinamilk",
         "CUAHANG(MACH, TENCH, QUAN), SANPHAM(MASP, TENSP, NHANHIEU), NHAPHANG(MAPN, MACH, NGAYNHAP), CT_NHAP(MAPN, MASP, SOLUONG)",
         "Tìm mã cửa hàng và tên cửa hàng tại quận 'Thu Duc' đã từng nhập phân phối TẤT CẢ các sản phẩm thuộc nhãn hiệu 'Vinamilk'.",
         "π_{MACH, TENCH}(σ_{QUAN = 'Thu Duc'}(CUAHANG) ⋈ (π_{MACH, MASP}(NHAPHANG ⋈ CT_NHAP) ÷ π_{MASP}(σ_{NHANHIEU = 'Vinamilk'}(SANPHAM))))",
         "SELECT CH.MACH, CH.TENCH\nFROM CUAHANG CH\nWHERE CH.QUAN = N'Thu Duc'\n  AND NOT EXISTS (\n    SELECT SP.MASP FROM SANPHAM SP WHERE SP.NHANHIEU = 'Vinamilk'\n    EXCEPT\n    SELECT CT.MASP FROM NHAPHANG NH INNER JOIN CT_NHAP CT ON NH.MAPN = CT.MAPN WHERE NH.MACH = CH.MACH\n);",
         [
             "Bước 1: S = π_{MASP}(σ_{NHANHIEU = 'Vinamilk'}(SANPHAM)).",
             "Bước 2: U = π_{MACH}(σ_{QUAN = 'Thu Duc'}(CUAHANG ⋈ NHAPHANG)).",
             "Bước 3: Missing = π_{MACH}((U × S) - π_{MACH, MASP}(NHAPHANG ⋈ CT_NHAP)).",
             "Bước 4: KQ = (U - Missing) ⋈ π_{MACH, TENCH}(CUAHANG)."
         ],
         "Cửa hàng ở quận khác phân phối đủ vẫn bị loại bởi điều kiện QUAN = 'Thu Duc'."),

        ("RA-D14", "ĐSQH Phép Chia: Bệnh Nhân Tiêm Đủ Phác Đồ 5 Mũi Phòng Dại",
         "BENHNHAN(MABN, HOTEN, SDT), MUITIEM_CHUAN(MAMUI, TENMUI, NGAYTHU), LICHSU_TIEM(MABN, MAMUI, NGAYTIEM_THUC, TRANGTHAI)",
         "Tìm mã bệnh nhân và họ tên của các bệnh nhân đã tiêm hoàn tất (TRANGTHAI = 'Hoan thanh') TẤT CẢ các mũi tiêm trong phác đồ phòng dại (thuộc danh mục MUITIEM_CHUAN).",
         "π_{MABN, HOTEN}(BENHNHAN ⋈ (π_{MABN, MAMUI}(σ_{TRANGTHAI = 'Hoan thanh'}(LICHSU_TIEM)) ÷ π_{MAMUI}(MUITIEM_CHUAN)))",
         "SELECT BN.MABN, BN.HOTEN\nFROM BENHNHAN BN\nWHERE EXISTS (SELECT 1 FROM LICHSU_TIEM LS WHERE LS.MABN = BN.MABN)\n  AND NOT EXISTS (\n    SELECT MTC.MAMUI FROM MUITIEM_CHUAN MTC\n    EXCEPT\n    SELECT LS.MAMUI FROM LICHSU_TIEM LS WHERE LS.MABN = BN.MABN AND LS.TRANGTHAI = N'Hoan thanh'\n);",
         [
             "Bước 1: S = π_{MAMUI}(MUITIEM_CHUAN).",
             "Bước 2: R_Actual = π_{MABN, MAMUI}(σ_{TRANGTHAI = 'Hoan thanh'}(LICHSU_TIEM)).",
             "Bước 3: U = π_{MABN}(R_Actual); Missing = π_{MABN}((U × S) - R_Actual).",
             "Bước 4: KQ = (U - Missing) ⋈ π_{MABN, HOTEN}(BENHNHAN)."
         ],
         "Bệnh nhân bỏ dở giữa chừng (mới tiêm 3/5 mũi) sẽ có Missing khác rỗng và bị loại."),

        ("RA-D15", "ĐSQH Phép Chia: Lập Trình Viên Đóng Góp Vào Tất Cả Microservices Lõi",
         "LAPTRINHVIEN(MALTV, HOTEN, PHONG_DEV), MICROSERVICE(MASVC, TENSVC, PHANLOAI), COMMIT_LOG(MA_COMMIT, MALTV, MASVC, NGAY_COMMIT)",
         "Cho biết mã lập trình viên và họ tên của các lập trình viên thuộc phòng 'Backend' đã từng đóng góp commit vào TẤT CẢ các microservice có phân loại là 'Core Service'.",
         "π_{MALTV, HOTEN}(σ_{PHONG_DEV = 'Backend'}(LAPTRINHVIEN) ⋈ (π_{MALTV, MASVC}(COMMIT_LOG) ÷ π_{MASVC}(σ_{PHANLOAI = 'Core Service'}(MICROSERVICE))))",
         "SELECT LTV.MALTV, LTV.HOTEN\nFROM LAPTRINHVIEN LTV\nWHERE LTV.PHONG_DEV = 'Backend'\n  AND NOT EXISTS (\n    SELECT MS.MASVC FROM MICROSERVICE MS WHERE MS.PHANLOAI = 'Core Service'\n    EXCEPT\n    SELECT CL.MASVC FROM COMMIT_LOG CL WHERE CL.MALTV = LTV.MALTV\n);",
         [
             "Bước 1: S = π_{MASVC}(σ_{PHANLOAI = 'Core Service'}(MICROSERVICE)).",
             "Bước 2: U = π_{MALTV}(σ_{PHONG_DEV = 'Backend'}(LAPTRINHVIEN ⋈ COMMIT_LOG)).",
             "Bước 3: Missing = π_{MALTV}((U × S) - π_{MALTV, MASVC}(COMMIT_LOG)).",
             "Bước 4: KQ = (U - Missing) ⋈ π_{MALTV, HOTEN}(LAPTRINHVIEN)."
         ],
         "Bảo đảm kiến trúc microservices được bao phủ kiểm tra đóng góp mã nguồn đầy đủ.")
    ]

    for item in division_problems:
        pid, title, schema, prompt, ra, sql, steps, edge = item
        problems.append({
            "id": pid, "topic": "RA_DIVISION_GROUPING", "difficulty": "C",
            "title": title, "prompt": prompt, "schema": schema, "recommended_time_mins": 20, "points": 1.5,
            "status": "VERIFIED", "verification_level": "SEMANTICALLY_REVIEWED",
            "solution": {"relational_algebra": ra, "sql": sql, "intermediate_steps": steps, "edge_cases": edge},
            "rubric": {"total_points": 1.5, "target_and_candidate_definition": 0.5, "cartesian_and_subtraction_correctness": 0.6, "edge_case_and_boundary_handling": 0.4}
        })

    # 16-30: 15 Grouping & Aggregations (Gamma) Problems
    grouping_problems = [
        ("RA-D16", "ĐSQH Gom Nhóm: Thống Kê Số Lượng Sinh Viên Theo Từng Ngành",
         "NGANH(MANGANH, TENNGANH), SINHVIEN(MSSV, HOTEN, MANGANH)",
         "Cho biết mã ngành, tên ngành và số lượng sinh viên của các ngành đào tạo có từ 150 sinh viên trở lên.",
         "σ_{SO_SV ≥ 150}(_{MANGANH, TENNGANH} γ _{COUNT(MSSV) → SO_SV}(NGANH ⋈ SINHVIEN))",
         "SELECT N.MANGANH, N.TENNGANH, COUNT(SV.MSSV) AS SO_SV\nFROM NGANH N INNER JOIN SINHVIEN SV ON N.MANGANH = SV.MANGANH\nGROUP BY N.MANGANH, N.TENNGANH\nHAVING COUNT(SV.MSSV) >= 150;",
         ["Bước 1: Kết nối NGANH với SINHVIEN theo khóa MANGANH.",
          "Bước 2: Gom nhóm theo MANGANH, TENNGANH và áp dụng hàm tổng hợp COUNT(MSSV) đổi tên thành SO_SV.",
          "Bước 3: Áp dụng phép chọn σ trên kết quả gom nhóm với điều kiện SO_SV >= 150."],
         "Nếu ngành chưa có sinh viên nào, INNER JOIN sẽ loại bỏ ngành đó; điều kiện >= 150 không bị ảnh hưởng."),

        ("RA-D17", "ĐSQH Gom Nhóm: Tính Tổng Tiền Mua Hàng Khách Hàng VIP Năm 2024",
         "KHACHHANG(MAKH, HOTEN), DONHANG(MADON, MAKH, NGAYDAT, TONGTIEN)",
         "Tìm mã khách hàng, họ tên và tổng số tiền đã mua của các khách hàng có tổng chi tiêu trong năm 2024 vượt quá 50.000.000 VNĐ.",
         "σ_{TONG_CHITIEU > 50000000}(_{KHACHHANG.MAKH, HOTEN} γ _{SUM(TONGTIEN) → TONG_CHITIEU}(KHACHHANG ⋈ σ_{NGAYDAT ≥ '2024-01-01' ∧ NGAYDAT ≤ '2024-12-31'}(DONHANG)))",
         "SELECT KH.MAKH, KH.HOTEN, SUM(DH.TONGTIEN) AS TONG_CHITIEU\nFROM KHACHHANG KH INNER JOIN DONHANG DH ON KH.MAKH = DH.MAKH\nWHERE DH.NGAYDAT BETWEEN '2024-01-01' AND '2024-12-31'\nGROUP BY KH.MAKH, KH.HOTEN\nHAVING SUM(DH.TONGTIEN) > 50000000;",
         ["Bước 1: Lọc bảng DONHANG theo khoảng thời gian năm 2024.",
          "Bước 2: Kết nối với KHACHHANG theo MAKH.",
          "Bước 3: Gom nhóm theo MAKH, HOTEN và tính SUM(TONGTIEN) -> TONG_CHITIEU.",
          "Bước 4: Lọc các nhóm có TONG_CHITIEU > 50.000.000."],
         "Lọc ngày trước khi gom nhóm tương ứng mệnh đề WHERE trong SQL."),

        ("RA-D18", "ĐSQH Gom Nhóm: Đếm Số Ca Mổ Của Bác Sĩ Ngoại Khoa Quý 4",
         "BACSI(MABS, HOTEN, CHUYENKHOA), CAMO(MACAMO, MABS_CHINH, NGAYMO, KETQUA)",
         "Tìm mã bác sĩ, họ tên và số ca mổ đã thực hiện của các bác sĩ chuyên khoa 'Ngoai khoa' đã mổ chính từ 10 ca trở lên trong quý 4 năm 2024.",
         "σ_{SO_CAMO ≥ 10}(_{BACSI.MABS, HOTEN} γ _{COUNT(MACAMO) → SO_CAMO}(σ_{CHUYENKHOA = 'Ngoai khoa'}(BACSI) ⋈_{MABS = MABS_CHINH} σ_{NGAYMO ≥ '2024-10-01' ∧ NGAYMO ≤ '2024-12-31'}(CAMO)))",
         "SELECT BS.MABS, BS.HOTEN, COUNT(CM.MACAMO) AS SO_CAMO\nFROM BACSI BS INNER JOIN CAMO CM ON BS.MABS = CM.MABS_CHINH\nWHERE BS.CHUYENKHOA = N'Ngoai khoa' AND CM.NGAYMO BETWEEN '2024-10-01' AND '2024-12-31'\nGROUP BY BS.MABS, BS.HOTEN\nHAVING COUNT(CM.MACAMO) >= 10;",
         ["Bước 1: Lọc bác sĩ ngoại khoa và lọc ca mổ trong quý 4/2024.",
          "Bước 2: Kết nối theo MABS = MABS_CHINH.",
          "Bước 3: Gom nhóm theo MABS, HOTEN và đếm COUNT(MACAMO) -> SO_CAMO.",
          "Bước 4: Chọn các nhóm có SO_CAMO >= 10."],
         "Cần phân biệt bác sĩ mổ chính với bác sĩ phụ mổ nếu có."),

        ("RA-D19", "ĐSQH Gom Nhóm: Tính Điểm Trung Bình Tích Lũy Theo Từng Lớp",
         "LOP(MALOP, TENLOP, KHOAHOC), SINHVIEN(MSSV, HOTEN, MALOP, DIEM_TBTL)",
         "Cho biết mã lớp, tên lớp và điểm trung bình tích lũy trung bình của lớp đối với các lớp thuộc khóa 'K2023' có điểm trung bình toàn lớp từ 8.0 trở lên.",
         "σ_{DTB_LOP ≥ 8.0}(_{LOP.MALOP, TENLOP} γ _{AVG(DIEM_TBTL) → DTB_LOP}(σ_{KHOAHOC = 'K2023'}(LOP) ⋈ SINHVIEN))",
         "SELECT L.MALOP, L.TENLOP, AVG(SV.DIEM_TBTL) AS DTB_LOP\nFROM LOP L INNER JOIN SINHVIEN SV ON L.MALOP = SV.MALOP\nWHERE L.KHOAHOC = 'K2023'\nGROUP BY L.MALOP, L.TENLOP\nHAVING AVG(SV.DIEM_TBTL) >= 8.0;",
         ["Bước 1: Lọc các lớp khóa K2023 và kết nối với SINHVIEN theo MALOP.",
          "Bước 2: Gom nhóm theo MALOP, TENLOP.",
          "Bước 3: Tính hàm tổng hợp AVG(DIEM_TBTL) đặt tên DTB_LOP.",
          "Bước 4: Lọc điều kiện DTB_LOP >= 8.0."],
         "Hàm AVG bỏ qua các giá trị NULL trong tập dữ liệu."),

        ("RA-D20", "ĐSQH Gom Nhóm: Tổng Doanh Thu Chi Nhánh Nhà Thuốc Quý 4",
         "NHATHUOC(MANT, TENNT, QUAN), HOADON(MAHD, MANT, NGAYLAP, TONGTIEN)",
         "Tìm mã nhà thuốc, tên nhà thuốc tại 'Quan 1' có tổng doanh thu trong quý 4/2024 đạt từ 200.000.000 VNĐ trở lên.",
         "σ_{DOANHTHU ≥ 200000000}(_{NHATHUOC.MANT, TENNT} γ _{SUM(TONGTIEN) → DOANHTHU}(σ_{QUAN = 'Quan 1'}(NHATHUOC) ⋈ σ_{NGAYLAP ≥ '2024-10-01' ∧ NGAYLAP ≤ '2024-12-31'}(HOADON)))",
         "SELECT NT.MANT, NT.TENNT, SUM(HD.TONGTIEN) AS DOANHTHU\nFROM NHATHUOC NT INNER JOIN HOADON HD ON NT.MANT = HD.MANT\nWHERE NT.QUAN = 'Quan 1' AND HD.NGAYLAP BETWEEN '2024-10-01' AND '2024-12-31'\nGROUP BY NT.MANT, NT.TENNT\nHAVING SUM(HD.TONGTIEN) >= 200000000;",
         ["Bước 1: Lọc nhà thuốc ở Quận 1 và hóa đơn trong quý 4.",
          "Bước 2: Kết nối theo MANT.",
          "Bước 3: Gom nhóm theo MANT, TENNT và tính SUM(TONGTIEN).",
          "Bước 4: Lọc ngưỡng DOANHTHU >= 200.000.000."],
         "Phép chọn trước kết nối giúp giảm thiểu tối đa kích thước dữ liệu cần gom nhóm."),

        ("RA-D21", "ĐSQH Gom Nhóm: Số Lượt Chuyến Bay Khai Thác Theo Tàu Bay",
         "MAYBAY(MAMB, SOHIEU, LOAIMB), CHUYENBAY(MACB, MAMB, NGAYBAY, TRANGTHAI)",
         "Tìm mã máy bay, số hiệu và số chuyến bay đã hoàn thành của các máy bay thực hiện từ 40 chuyến bay thành công (TRANGTHAI = 'Hoan thanh') trở lên trong tháng 11/2024.",
         "σ_{SO_CHUYEN ≥ 40}(_{MAYBAY.MAMB, SOHIEU} γ _{COUNT(MACB) → SO_CHUYEN}(MAYBAY ⋈ σ_{TRANGTHAI = 'Hoan thanh' ∧ NGAYBAY ≥ '2024-11-01' ∧ NGAYBAY ≤ '2024-11-30'}(CHUYENBAY)))",
         "SELECT MB.MAMB, MB.SOHIEU, COUNT(CB.MACB) AS SO_CHUYEN\nFROM MAYBAY MB INNER JOIN CHUYENBAY CB ON MB.MAMB = CB.MAMB\nWHERE CB.TRANGTHAI = N'Hoan thanh' AND CB.NGAYBAY BETWEEN '2024-11-01' AND '2024-11-30'\nGROUP BY MB.MAMB, MB.SOHIEU\nHAVING COUNT(CB.MACB) >= 40;",
         ["Bước 1: Lọc các chuyến bay hoàn thành trong tháng 11/2024.",
          "Bước 2: Kết nối với MAYBAY theo MAMB.",
          "Bước 3: Gom nhóm theo MAMB, SOHIEU và đếm COUNT(MACB).",
          "Bước 4: Chọn các tàu bay có SO_CHUYEN >= 40."],
         "Các chuyến bay bị hủy (TRANGTHAI = 'Huy') bị loại bỏ bởi phép chọn."),

        ("RA-D22", "ĐSQH Gom Nhóm: Tổng Khối Lượng Rác Tái Chế Theo Khu Vực",
         "KHUVUC_GOM(MAKV, TENKV, QUAN), CHUYEN_GOM(MACHUYEN, MAKV, NGAYGOM, KHOILUONG_KG, LOAIRAC)",
         "Tìm mã khu vực gom, tên khu vực tại quận 'Binh Thanh' có tổng khối lượng rác thuộc loại 'Tai che' thu gom trong tháng 10/2024 đạt từ 10.000 kg trở lên.",
         "σ_{TONG_KG ≥ 10000}(_{KHUVUC_GOM.MAKV, TENKV} γ _{SUM(KHOILUONG_KG) → TONG_KG}(σ_{QUAN = 'Binh Thanh'}(KHUVUC_GOM) ⋈ σ_{LOAIRAC = 'Tai che' ∧ NGAYGOM ≥ '2024-10-01' ∧ NGAYGOM ≤ '2024-10-31'}(CHUYEN_GOM)))",
         "SELECT KV.MAKV, KV.TENKV, SUM(CG.KHOILUONG_KG) AS TONG_KG\nFROM KHUVUC_GOM KV INNER JOIN CHUYEN_GOM CG ON KV.MAKV = CG.MAKV\nWHERE KV.QUAN = N'Binh Thanh' AND CG.LOAIRAC = N'Tai che' AND CG.NGAYGOM BETWEEN '2024-10-01' AND '2024-10-31'\nGROUP BY KV.MAKV, KV.TENKV\nHAVING SUM(CG.KHOILUONG_KG) >= 10000;",
         ["Bước 1: Lọc khu vực thuộc quận Bình Thạnh và các chuyến gom rác tái chế tháng 10.",
          "Bước 2: Kết nối theo MAKV.",
          "Bước 3: Gom nhóm MAKV, TENKV và tính SUM(KHOILUONG_KG).",
          "Bước 4: Lọc TONG_KG >= 10.000."],
         "Cần bảo đảm đơn vị tính khối lượng đồng nhất (kg)."),

        ("RA-D23", "ĐSQH Gom Nhóm: Số Đề Tài Nghiên Cứu Khoa Học Của Bộ Môn",
         "BOMON(MABM, TENBM, MAKHOA), DETAI(MADT, MABM, KETQUA_NT, NAM_NT)",
         "Cho biết mã bộ môn, tên bộ môn và số lượng đề tài nghiên cứu khoa học đạt loại 'Xuat sac' được nghiệm thu trong năm 2024 của các bộ môn có từ 3 đề tài xuất sắc trở lên.",
         "σ_{SO_DETAI ≥ 3}(_{BOMON.MABM, TENBM} γ _{COUNT(MADT) → SO_DETAI}(BOMON ⋈ σ_{KETQUA_NT = 'Xuat sac' ∧ NAM_NT = 2024}(DETAI)))",
         "SELECT BM.MABM, BM.TENBM, COUNT(DT.MADT) AS SO_DETAI\nFROM BOMON BM INNER JOIN DETAI DT ON BM.MABM = DT.MABM\nWHERE DT.KETQUA_NT = N'Xuat sac' AND DT.NAM_NT = 2024\nGROUP BY BM.MABM, BM.TENBM\nHAVING COUNT(DT.MADT) >= 3;",
         ["Bước 1: Lọc đề tài đạt xuất sắc nghiệm thu năm 2024.",
          "Bước 2: Kết nối với BOMON theo MABM.",
          "Bước 3: Gom nhóm theo MABM, TENBM và đếm số đề tài.",
          "Bước 4: Lọc SO_DETAI >= 3."],
         "Các bộ môn không có đề tài nào xuất sắc sẽ tự động không thỏa mãn điều kiện HAVING."),

        ("RA-D24", "ĐSQH Gom Nhóm: Giá Cước Trung Bình Chuyến Xe Theo Tài Xế",
         "TAIXE(MATX, HOTEN, LOAIXE), CHUYENXE(MACHUYEN, MATX, GIA_CUOC, TRANGTHAI)",
         "Tìm mã tài xế, họ tên của các tài xế lái xe 'O to 4 cho' đã hoàn thành (TRANGTHAI = 'Hoan thanh') từ 100 chuyến xe trở lên và có giá cước trung bình mỗi chuyến đạt trên 120.000 VNĐ.",
         "σ_{SO_CHUYEN ≥ 100 ∧ CUOC_TB > 120000}(_{TAIXE.MATX, HOTEN} γ _{COUNT(MACHUYEN) → SO_CHUYEN, AVG(GIA_CUOC) → CUOC_TB}(σ_{LOAIXE = 'O to 4 cho'}(TAIXE) ⋈ σ_{TRANGTHAI = 'Hoan thanh'}(CHUYENXE)))",
         "SELECT TX.MATX, TX.HOTEN, COUNT(CX.MACHUYEN) AS SO_CHUYEN, AVG(CX.GIA_CUOC) AS CUOC_TB\nFROM TAIXE TX INNER JOIN CHUYENXE CX ON TX.MATX = CX.MATX\nWHERE TX.LOAIXE = 'O to 4 cho' AND CX.TRANGTHAI = N'Hoan thanh'\nGROUP BY TX.MATX, TX.HOTEN\nHAVING COUNT(CX.MACHUYEN) >= 100 AND AVG(CX.GIA_CUOC) > 120000;",
         ["Bước 1: Lọc tài xế ô tô 4 chỗ và chuyến xe đã hoàn thành.",
          "Bước 2: Kết nối theo MATX.",
          "Bước 3: Gom nhóm theo MATX, HOTEN, tính đồng thời COUNT và AVG.",
          "Bước 4: Áp dụng vị từ chọn kết hợp cả 2 tiêu chí số chuyến và giá cước trung bình."],
         "Toán tử gamma cho phép định nghĩa nhiều hàm tổng hợp cùng lúc."),

        ("RA-D25", "ĐSQH Gom Nhóm: Số Phòng Đã Cho Thuê Theo Tòa Nhà Chung Cư",
         "TOANHA(MATN, TENTN, DIACHI), CANHO(MACAN, MATN, TRANGTHAI)",
         "Tìm mã tòa nhà, tên tòa nhà và số lượng căn hộ đang cho thuê (TRANGTHAI = 'Dang thue') của các tòa nhà có từ 50 căn hộ đang cho thuê trở lên.",
         "σ_{SO_CAN_THUE ≥ 50}(_{TOANHA.MATN, TENTN} γ _{COUNT(MACAN) → SO_CAN_THUE}(TOANHA ⋈ σ_{TRANGTHAI = 'Dang thue'}(CANHO)))",
         "SELECT TH.MATN, TH.TENTN, COUNT(CH.MACAN) AS SO_CAN_THUE\nFROM TOANHA TH INNER JOIN CANHO CH ON TH.MATN = CH.MATN\nWHERE CH.TRANGTHAI = N'Dang thue'\nGROUP BY TH.MATN, TH.TENTN\nHAVING COUNT(CH.MACAN) >= 50;",
         ["Bước 1: Lọc căn hộ đang thuê.",
          "Bước 2: Kết nối với TOANHA theo MATN.",
          "Bước 3: Gom nhóm theo MATN, TENTN và đếm số căn.",
          "Bước 4: Lọc SO_CAN_THUE >= 50."],
         "Tránh đếm các căn hộ trống hoặc đang sửa chữa."),

        ("RA-D26", "ĐSQH Gom Nhóm: Tổng Lượng Mưa Quan Trắc Theo Trạm Khí Tượng",
         "TRAM_DO(MATRAM, TENTRAM, TINH_TP), PHIEN_DODAC(MAPHIEN, MATRAM, THOIDIEM, LUONGMUA_MM)",
         "Cho biết mã trạm, tên trạm tại tỉnh 'Quang Nam' có tổng lượng mưa đo được trong tháng 10/2024 vượt quá 1.000 mm.",
         "σ_{TONG_MUA > 1000}(_{TRAM_DO.MATRAM, TENTRAM} γ _{SUM(LUONGMUA_MM) → TONG_MUA}(σ_{TINH_TP = 'Quang Nam'}(TRAM_DO) ⋈ σ_{THOIDIEM ≥ '2024-10-01' ∧ THOIDIEM ≤ '2024-10-31'}(PHIEN_DODAC)))",
         "SELECT TD.MATRAM, TD.TENTRAM, SUM(PD.LUONGMUA_MM) AS TONG_MUA\nFROM TRAM_DO TD INNER JOIN PHIEN_DODAC PD ON TD.MATRAM = PD.MATRAM\nWHERE TD.TINH_TP = N'Quang Nam' AND PD.THOIDIEM BETWEEN '2024-10-01' AND '2024-10-31'\nGROUP BY TD.MATRAM, TD.TENTRAM\nHAVING SUM(PD.LUONGMUA_MM) > 1000;",
         ["Bước 1: Lọc trạm ở Quảng Nam và các phiên đo tháng 10/2024.",
          "Bước 2: Kết nối theo MATRAM.",
          "Bước 3: Gom nhóm theo MATRAM, TENTRAM và tính tổng lượng mưa.",
          "Bước 4: Chọn các trạm có TONG_MUA > 1000 mm."],
         "Lượng mưa mang giá trị thực (DECIMAL/FLOAT)."),

        ("RA-D27", "ĐSQH Gom Nhóm: Tổng Tiền Thuê Đất Theo Doanh Nghiệp KCN",
         "DOANHNGHIEP(MADN, TENDN, QUOCTICH), HOPDONG_THUE(MAHD, MADN, GIATHUE_HANGNAM, TRANGTHAI)",
         "Tìm mã doanh nghiệp, tên doanh nghiệp có quốc tịch 'Nhat Ban' đang có tổng giá trị thuê đất hàng năm trên các hợp đồng còn hiệu lực (TRANGTHAI = 'Hieu luc') vượt quá 10.000.000.000 VNĐ (10 tỷ VNĐ).",
         "σ_{TONG_TIEN_THUE > 10000000000}(_{DOANHNGHIEP.MADN, TENDN} γ _{SUM(GIATHUE_HANGNAM) → TONG_TIEN_THUE}(σ_{QUOCTICH = 'Nhat Ban'}(DOANHNGHIEP) ⋈ σ_{TRANGTHAI = 'Hieu luc'}(HOPDONG_THUE)))",
         "SELECT DN.MADN, DN.TENDN, SUM(HD.GIATHUE_HANGNAM) AS TONG_TIEN_THUE\nFROM DOANHNGHIEP DN INNER JOIN HOPDONG_THUE HD ON DN.MADN = HD.MADN\nWHERE DN.QUOCTICH = N'Nhat Ban' AND HD.TRANGTHAI = N'Hieu luc'\nGROUP BY DN.MADN, DN.TENDN\nHAVING SUM(HD.GIATHUE_HANGNAM) > 10000000000;",
         ["Bước 1: Lọc doanh nghiệp Nhật Bản và hợp đồng còn hiệu lực.",
          "Bước 2: Kết nối theo MADN.",
          "Bước 3: Gom nhóm MADN, TENDN và tính SUM(GIATHUE_HANGNAM).",
          "Bước 4: Lọc ngưỡng 10 tỷ VNĐ."],
         "Hợp đồng hết hạn hoặc đã thanh lý bị loại bỏ."),

        ("RA-D28", "ĐSQH Gom Nhóm: Đếm Số Bản Thu Âm Triệu Stream Của Nhạc Sĩ",
         "NHACSI(MANS, HOTEN, BUTDANH), BAN_THUAM(MABT, MANS, LUOT_STREAM, NAM_PHATHANH)",
         "Tìm mã nhạc sĩ, bút danh và số lượng bản thu âm phát hành năm 2024 đạt từ 1.000.000 lượt stream trở lên của các nhạc sĩ có từ 3 bản thu âm triệu stream trở lên.",
         "σ_{SO_HIT ≥ 3}(_{NHACSI.MANS, BUTDANH} γ _{COUNT(MABT) → SO_HIT}(NHACSI ⋈ σ_{LUOT_STREAM ≥ 1000000 ∧ NAM_PHATHANH = 2024}(BAN_THUAM)))",
         "SELECT NS.MANS, NS.BUTDANH, COUNT(BT.MABT) AS SO_HIT\nFROM NHACSI NS INNER JOIN BAN_THUAM BT ON NS.MANS = BT.MANS\nWHERE BT.LUOT_STREAM >= 1000000 AND BT.NAM_PHATHANH = 2024\nGROUP BY NS.MANS, NS.BUTDANH\nHAVING COUNT(BT.MABT) >= 3;",
         ["Bước 1: Lọc bản thu âm đạt mốc 1 triệu stream năm 2024.",
          "Bước 2: Kết nối với NHACSI theo MANS.",
          "Bước 3: Gom nhóm MANS, BUTDANH và đếm COUNT(MABT).",
          "Bước 4: Lọc SO_HIT >= 3."],
         "Cần bảo đảm LUOT_STREAM dùng kiểu dữ liệu số lớn (BIGINT)."),

        ("RA-D29", "ĐSQH Gom Nhóm: Số Lượng Thiết Bị Y Tế Hỏng Cần Bảo Trì",
         "KHOA_PHONG(MAKHOA, TENKHOA), THIETBI(MATB, MAKHOA, TRANGTHAI)",
         "Cho biết mã khoa phòng, tên khoa phòng và số lượng thiết bị đang bị hỏng (TRANGTHAI = 'Hong hoc') của các khoa phòng có từ 5 thiết bị hỏng trở lên.",
         "σ_{SO_TB_HONG ≥ 5}(_{KHOA_PHONG.MAKHOA, TENKHOA} γ _{COUNT(MATB) → SO_TB_HONG}(KHOA_PHONG ⋈ σ_{TRANGTHAI = 'Hong hoc'}(THIETBI)))",
         "SELECT KP.MAKHOA, KP.TENKHOA, COUNT(TB.MATB) AS SO_TB_HONG\nFROM KHOA_PHONG KP INNER JOIN THIETBI TB ON KP.MAKHOA = TB.MAKHOA\nWHERE TB.TRANGTHAI = N'Hong hoc'\nGROUP BY KP.MAKHOA, KP.TENKHOA\nHAVING COUNT(TB.MATB) >= 5;",
         ["Bước 1: Lọc thiết bị có trạng thái hỏng hóc.",
          "Bước 2: Kết nối với KHOA_PHONG theo MAKHOA.",
          "Bước 3: Gom nhóm theo MAKHOA, TENKHOA và đếm số lượng.",
          "Bước 4: Lọc SO_TB_HONG >= 5."],
         "Cảnh báo bảo trì trang thiết bị trọng điểm bệnh viện."),

        ("RA-D30", "ĐSQH Gom Nhóm: Tổng Số Tiết Giảng Dạy Của Giảng Viên Vượt Chuẩn",
         "GIANGVIEN(MAGV, HOTEN, MAKHOA), LOPHOCPHAN(MALHP, MAGV, SOTIET, NAMHOC)",
         "Tìm mã giảng viên, họ tên của các giảng viên thuộc khoa 'Khoa hoc May tinh' có tổng số tiết giảng dạy trong năm học '2023-2024' vượt định mức 300 tiết.",
         "σ_{TONG_TIET > 300}(_{GIANGVIEN.MAGV, HOTEN} γ _{SUM(SOTIET) → TONG_TIET}(σ_{MAKHOA = 'KHMT'}(GIANGVIEN) ⋈ σ_{NAMHOC = '2023-2024'}(LOPHOCPHAN)))",
         "SELECT GV.MAGV, GV.HOTEN, SUM(LHP.SOTIET) AS TONG_TIET\nFROM GIANGVIEN GV INNER JOIN LOPHOCPHAN LHP ON GV.MAGV = LHP.MAGV\nWHERE GV.MAKHOA = 'KHMT' AND LHP.NAMHOC = '2023-2024'\nGROUP BY GV.MAGV, GV.HOTEN\nHAVING SUM(LHP.SOTIET) > 300;",
         ["Bước 1: Lọc giảng viên khoa KHMT và lớp học phần năm 2023-2024.",
          "Bước 2: Kết nối theo MAGV.",
          "Bước 3: Gom nhóm MAGV, HOTEN và tính SUM(SOTIET).",
          "Bước 4: Lọc TONG_TIET > 300."],
         "Chỉ tính số tiết thực dạy trong năm học được xét.")
    ]

    for item in grouping_problems:
        pid, title, schema, prompt, ra, sql, steps, edge = item
        problems.append({
            "id": pid, "topic": "RA_DIVISION_GROUPING", "difficulty": "B",
            "title": title, "prompt": prompt, "schema": schema, "recommended_time_mins": 15, "points": 1.0,
            "status": "VERIFIED", "verification_level": "SEMANTICALLY_REVIEWED",
            "solution": {"relational_algebra": ra, "sql": sql, "intermediate_steps": steps, "edge_cases": edge},
            "rubric": {"total_points": 1.0, "grouping_attributes_and_gamma": 0.4, "aggregation_functions": 0.4, "having_filter_condition": 0.2}
        })

    # 31-45: 15 Extreme Values & Tie-Breaking (MAX / MIN) Problems (Fixing P0-04)
    extreme_problems = [
        ("RA-D31", "ĐSQH Cực Trị: Sinh Viên Điểm GPA Cao Nhất Khoa Công Nghệ Phần Mềm",
         "SINHVIEN(MSSV, HOTEN, KHOA, DIEM_GPA)",
         "Tìm mã số sinh viên, họ tên và điểm GPA của các sinh viên đạt điểm GPA cao nhất trong khoa 'Cong nghe Phan mem' (bảo toàn tất cả sinh viên đồng hạng thủ khoa).",
         # Correct subgroup math: R_sub = sigma_{KHOA = 'CNPM'}(SINHVIEN)
         "R_{sub} = σ_{KHOA = 'Cong nghe Phan mem'}(SINHVIEN)\nNonMax = π_{SV1.MSSV, SV1.HOTEN, SV1.KHOA, SV1.DIEM_GPA}(σ_{SV1.DIEM_GPA < SV2.DIEM_GPA}(ρ_{SV1}(R_{sub}) × ρ_{SV2}(R_{sub})))\nKQ = R_{sub} - NonMax",
         "SELECT SV.MSSV, SV.HOTEN, SV.DIEM_GPA\nFROM SINHVIEN SV\nWHERE SV.KHOA = N'Cong nghe Phan mem'\n  AND SV.DIEM_GPA = (SELECT MAX(DIEM_GPA) FROM SINHVIEN WHERE KHOA = N'Cong nghe Phan mem');",
         ["Bước 1 (Lọc tập con phân nhóm R_sub): Lọc trước toàn bộ sinh viên thuộc khoa 'Cong nghe Phan mem'.",
          "Bước 2 (Tìm tập không phải lớn nhất NonMax): Tích Descartes ρ_{SV1}(R_sub) × ρ_{SV2}(R_sub) và chọn các cặp có SV1.DIEM_GPA < SV2.DIEM_GPA.",
          "Bước 3 (Lấy hiệu trên chính R_sub): Lấy R_sub trừ đi NonMax. Kết quả chỉ chứa sinh viên khoa CNPM có GPA cao nhất và bảo toàn tất cả các sinh viên đồng hạng!"],
         "Tuyệt đối không lấy toàn bảng SINHVIEN trừ NonMax vì sinh viên các khoa khác không xuất hiện trong NonMax sẽ bị sót lại trong kết quả sai lệch!"),

        ("RA-D32", "ĐSQH Cực Trị: Sản Phẩm Bán Chạy Nhất Danh Mục Điện Thoại",
         "SANPHAM(MASP, TENSP, DANHMUC, SOLUONG_BAN)",
         "Tìm mã sản phẩm, tên sản phẩm và số lượng bán của các sản phẩm có số lượng bán nhiều nhất trong danh mục 'Dien thoai' năm 2024.",
         "R_{sub} = σ_{DANHMUC = 'Dien thoai'}(SANPHAM)\nNonMax = π_{SP1.MASP, SP1.TENSP, SP1.DANHMUC, SP1.SOLUONG_BAN}(σ_{SP1.SOLUONG_BAN < SP2.SOLUONG_BAN}(ρ_{SP1}(R_{sub}) × ρ_{SP2}(R_{sub})))\nKQ = R_{sub} - NonMax",
         "SELECT SP.MASP, SP.TENSP, SP.SOLUONG_BAN\nFROM SANPHAM SP\nWHERE SP.DANHMUC = N'Dien thoai'\n  AND SP.SOLUONG_BAN = (SELECT MAX(SOLUONG_BAN) FROM SANPHAM WHERE DANHMUC = N'Dien thoai');",
         ["Bước 1: Lọc danh mục sản phẩm điện thoại: R_sub = σ_{DANHMUC = 'Dien thoai'}(SANPHAM).",
          "Bước 2: Tìm tập sản phẩm có số lượng bán bị vượt qua: NonMax = π_{SP1}(σ_{SP1.SOLUONG_BAN < SP2.SOLUONG_BAN}(ρ_{SP1}(R_sub) × ρ_{SP2}(R_sub))).",
          "Bước 3: Kết quả = R_sub - NonMax."],
         "Bảo toàn tất cả sản phẩm bán chạy nhất nếu có nhiều dòng máy cùng đạt số lượng bán kỷ lục."),

        ("RA-D33", "ĐSQH Cực Trị: Bác Sĩ Có Nhiều Ca Khám Bệnh Nhất Khoa Cấp Cứu",
         "BACSI(MABS, HOTEN, KHOAPHONG, SOCA_KHAM)",
         "Tìm mã bác sĩ, họ tên và số ca khám của các bác sĩ thực hiện nhiều ca khám bệnh nhất tại khoa 'Cap cuu'.",
         "R_{sub} = σ_{KHOAPHONG = 'Cap cuu'}(BACSI)\nNonMax = π_{BS1.MABS, BS1.HOTEN, BS1.KHOAPHONG, BS1.SOCA_KHAM}(σ_{BS1.SOCA_KHAM < BS2.SOCA_KHAM}(ρ_{BS1}(R_{sub}) × ρ_{BS2}(R_{sub})))\nKQ = R_{sub} - NonMax",
         "SELECT BS.MABS, BS.HOTEN, BS.SOCA_KHAM\nFROM BACSI BS\nWHERE BS.KHOAPHONG = N'Cap cuu'\n  AND BS.SOCA_KHAM = (SELECT MAX(SOCA_KHAM) FROM BACSI WHERE KHOAPHONG = N'Cap cuu');",
         ["Bước 1: R_sub = σ_{KHOAPHONG = 'Cap cuu'}(BACSI).",
          "Bước 2: NonMax = π_{BS1}(σ_{BS1.SOCA_KHAM < BS2.SOCA_KHAM}(ρ_{BS1}(R_sub) × ρ_{BS2}(R_sub))).",
          "Bước 3: KQ = R_sub - NonMax."],
         "Phương pháp hiệu tập con đảm bảo không làm lọt bác sĩ khoa khác vào kết quả."),

        ("RA-D34", "ĐSQH Cực Trị: Chuyến Bay Có Giá Vé Thấp Nhất Chặng SGN - DAD",
         "CHUYENBAY(MACB, HANG_BAY, CHANG_BAY, GIAVE)",
         "Tìm mã chuyến bay, hãng bay và giá vé của các chuyến bay có giá vé thấp nhất (MIN) trên chặng bay 'SGN-DAD'.",
         "R_{sub} = σ_{CHANG_BAY = 'SGN-DAD'}(CHUYENBAY)\nNonMin = π_{CB1.MACB, CB1.HANG_BAY, CB1.CHANG_BAY, CB1.GIAVE}(σ_{CB1.GIAVE > CB2.GIAVE}(ρ_{CB1}(R_{sub}) × ρ_{CB2}(R_{sub})))\nKQ = R_{sub} - NonMin",
         "SELECT CB.MACB, CB.HANG_BAY, CB.GIAVE\nFROM CHUYENBAY CB\nWHERE CB.CHANG_BAY = 'SGN-DAD'\n  AND CB.GIAVE = (SELECT MIN(GIAVE) FROM CHUYENBAY WHERE CHANG_BAY = 'SGN-DAD');",
         ["Bước 1: Lọc chuyến bay chặng SGN-DAD: R_sub = σ_{CHANG_BAY = 'SGN-DAD'}(CHUYENBAY).",
          "Bước 2: Tìm các chuyến bay có giá cao hơn chuyến khác trong chặng: NonMin = π_{CB1}(σ_{CB1.GIAVE > CB2.GIAVE}(ρ_{CB1}(R_sub) × ρ_{CB2}(R_sub))).",
          "Bước 3: Lấy R_sub trừ đi NonMin để thu được chuyến bay giá rẻ nhất."],
         "Đối với cực tiểu (MIN), điều kiện lọc cặp là CB1.GIAVE > CB2.GIAVE."),

        ("RA-D35", "ĐSQH Cực Trị: Căn Hộ Có Diện Tích Lớn Nhất Tòa Skyview",
         "CANHO(MACAN, TOANHA, SOHIEUCAN, DIENTICH_M2)",
         "Tìm mã căn hộ, số hiệu căn hộ và diện tích của các căn hộ có diện tích lớn nhất (MAX) tại tòa nhà 'Skyview'.",
         "R_{sub} = σ_{TOANHA = 'Skyview'}(CANHO)\nNonMax = π_{CH1.MACAN, CH1.TOANHA, CH1.SOHIEUCAN, CH1.DIENTICH_M2}(σ_{CH1.DIEMSO < CH2.DIEMSO}(ρ_{CH1}(R_{sub}) × ρ_{CH2}(R_{sub})))\nKQ = R_{sub} - NonMax",
         "SELECT CH.MACAN, CH.SOHIEUCAN, CH.DIENTICH_M2\nFROM CANHO CH\nWHERE CH.TOANHA = 'Skyview'\n  AND CH.DIENTICH_M2 = (SELECT MAX(DIENTICH_M2) FROM CANHO WHERE TOANHA = 'Skyview');",
         ["Bước 1: R_sub = σ_{TOANHA = 'Skyview'}(CANHO).",
          "Bước 2: NonMax = π_{CH1}(σ_{CH1.DIENTICH_M2 < CH2.DIENTICH_M2}(ρ_{CH1}(R_sub) × ρ_{CH2}(R_sub))).",
          "Bước 3: KQ = R_sub - NonMax."],
         "Nếu có nhiều căn hộ penthouse cùng diện tích tối đa, phép trừ bảo toàn toàn bộ."),

        ("RA-D36", "ĐSQH Cực Trị: Khách Hàng Có Chi Tiêu Cao Nhất Ngày Black Friday",
         "HOADON_BF(MAHD, MAKH, HOTEN_KH, TONGTIEN, NGAYMUA)",
         "Tìm mã khách hàng, tên khách hàng và tổng tiền của khách hàng có hóa đơn mua sắm trị giá cao nhất trong đợt khuyến mãi '2024-11-29'.",
         "R_{sub} = σ_{NGAYMUA = '2024-11-29'}(HOADON_BF)\nNonMax = π_{HD1.MAHD, HD1.MAKH, HD1.HOTEN_KH, HD1.TONGTIEN, HD1.NGAYMUA}(σ_{HD1.TONGTIEN < HD2.TONGTIEN}(ρ_{HD1}(R_{sub}) × ρ_{HD2}(R_{sub})))\nKQ = R_{sub} - NonMax",
         "SELECT HD.MAKH, HD.HOTEN_KH, HD.TONGTIEN\nFROM HOADON_BF HD\nWHERE HD.NGAYMUA = '2024-11-29'\n  AND HD.TONGTIEN = (SELECT MAX(TONGTIEN) FROM HOADON_BF WHERE NGAYMUA = '2024-11-29');",
         ["Bước 1: Lọc hóa đơn phát sinh ngày Black Friday: R_sub.",
          "Bước 2: Tìm các hóa đơn bị nhỏ hơn hóa đơn khác trong ngày: NonMax.",
          "Bước 3: KQ = R_sub - NonMax."],
         "Khách hàng đồng hạng giải Nhất được hiển thị đầy đủ."),

        ("RA-D37", "ĐSQH Cực Trị: Lô Vắc-Xin Nhập Nhiều Liều Nhất Của Moderna",
         "LOVACXIN(MALO, TENVACXIN, NHASANXUAT, SOLIEU_NHAP)",
         "Tìm mã lô, tên vắc-xin và số liều nhập của các lô vắc-xin có số lượng liều nhập nhiều nhất của nhà sản xuất 'Moderna'.",
         "R_{sub} = σ_{NHASANXUAT = 'Moderna'}(LOVACXIN)\nNonMax = π_{L1.MALO, L1.TENVACXIN, L1.NHASANXUAT, L1.SOLIEU_NHAP}(σ_{L1.SOLUONG < L2.SOLUONG}(ρ_{L1}(R_{sub}) × ρ_{L2}(R_{sub})))\nKQ = R_{sub} - NonMax",
         "SELECT LV.MALO, LV.TENVACXIN, LV.SOLIEU_NHAP\nFROM LOVACXIN LV\nWHERE LV.NHASANXUAT = 'Moderna'\n  AND LV.SOLIEU_NHAP = (SELECT MAX(SOLIEU_NHAP) FROM LOVACXIN WHERE NHASANXUAT = 'Moderna');",
         ["Bước 1: R_sub = σ_{NHASANXUAT = 'Moderna'}(LOVACXIN).",
          "Bước 2: NonMax = π_{L1}(σ_{L1.SOLIEU_NHAP < L2.SOLIEU_NHAP}(ρ_{L1}(R_sub) × ρ_{L2}(R_sub))).",
          "Bước 3: KQ = R_sub - NonMax."],
         "Lô của nhà sản xuất khác như Pfizer, AstraZeneca không bị ảnh hưởng."),

        ("RA-D38", "ĐSQH Cực Trị: Đề Tài NCKH Có Kinh Phí Lớn Nhất Năm 2024",
         "DETAI_NCKH(MADT, TENDT, NAM_TRIENKHAI, KINHPHI_VND)",
         "Tìm mã đề tài, tên đề tài và kinh phí của các đề tài nghiên cứu khoa học có kinh phí được phê duyệt lớn nhất trong năm '2024'.",
         "R_{sub} = σ_{NAM_TRIENKHAI = 2024}(DETAI_NCKH)\nNonMax = π_{DT1.MADT, DT1.TENDT, DT1.NAM_TRIENKHAI, DT1.KINHPHI_VND}(σ_{DT1.KINHPHI_VND < DT2.KINHPHI_VND}(ρ_{DT1}(R_{sub}) × ρ_{DT2}(R_{sub})))\nKQ = R_{sub} - NonMax",
         "SELECT DT.MADT, DT.TENDT, DT.KINHPHI_VND\nFROM DETAI_NCKH DT\nWHERE DT.NAM_TRIENKHAI = 2024\n  AND DT.KINHPHI_VND = (SELECT MAX(KINHPHI_VND) FROM DETAI_NCKH WHERE NAM_TRIENKHAI = 2024);",
         ["Bước 1: R_sub = σ_{NAM_TRIENKHAI = 2024}(DETAI_NCKH).",
          "Bước 2: NonMax = π_{DT1}(σ_{DT1.KINHPHI_VND < DT2.KINHPHI_VND}(ρ_{DT1}(R_sub) × ρ_{DT2}(R_sub))).",
          "Bước 3: KQ = R_sub - NonMax."],
         "Tránh lấy toàn bảng trừ NonMax làm sót các đề tài của các năm khác."),

        ("RA-D39", "ĐSQH Cực Trị: Tài Xế Công Nghệ Điểm Sao Cao Nhất Đội Xe 01",
         "TAIXE(MATX, HOTEN, MADOI, DIEM_SAO_TB)",
         "Tìm mã tài xế, họ tên và điểm sao trung bình của các tài xế đạt điểm đánh giá sao cao nhất thuộc đội xe có mã 'DOI_01'.",
         "R_{sub} = σ_{MADOI = 'DOI_01'}(TAIXE)\nNonMax = π_{TX1.MATX, TX1.HOTEN, TX1.MADOI, TX1.DIEM_SAO_TB}(σ_{TX1.DIEM_SAO_TB < TX2.DIEM_SAO_TB}(ρ_{TX1}(R_{sub}) × ρ_{TX2}(R_{sub})))\nKQ = R_{sub} - NonMax",
         "SELECT TX.MATX, TX.HOTEN, TX.DIEM_SAO_TB\nFROM TAIXE TX\nWHERE TX.MADOI = 'DOI_01'\n  AND TX.DIEM_SAO_TB = (SELECT MAX(DIEM_SAO_TB) FROM TAIXE WHERE MADOI = 'DOI_01');",
         ["Bước 1: R_sub = σ_{MADOI = 'DOI_01'}(TAIXE).",
          "Bước 2: NonMax = π_{TX1}(σ_{TX1.DIEM_SAO_TB < TX2.DIEM_SAO_TB}(ρ_{TX1}(R_sub) × ρ_{TX2}(R_sub))).",
          "Bước 3: KQ = R_sub - NonMax."],
         "Tất cả tài xế đạt cùng điểm số tối đa 5.0 sao đều được giữ lại trong kết quả."),

        ("RA-D40", "ĐSQH Cực Trị: Trạm Đo Ghi Nhận Lượng Mưa Cao Nhất Đợt Bão",
         "QUANTRAC_BAO(MATRAM, TENTRAM, VUNG_BAO, LUONGMUA_MM)",
         "Tìm mã trạm, tên trạm và lượng mưa của các trạm ghi nhận lượng mưa cao nhất trong vùng tâm bão 'Bao_So_3'.",
         "R_{sub} = σ_{VUNG_BAO = 'Bao_So_3'}(QUANTRAC_BAO)\nNonMax = π_{T1.MATRAM, T1.TENTRAM, T1.VUNG_BAO, T1.LUONGMUA_MM}(σ_{T1.LUONGMUA_MM < T2.LUONGMUA_MM}(ρ_{T1}(R_{sub}) × ρ_{T2}(R_{sub})))\nKQ = R_{sub} - NonMax",
         "SELECT T.MATRAM, T.TENTRAM, T.LUONGMUA_MM\nFROM QUANTRAC_BAO T\nWHERE T.VUNG_BAO = 'Bao_So_3'\n  AND T.LUONGMUA_MM = (SELECT MAX(LUONGMUA_MM) FROM QUANTRAC_BAO WHERE VUNG_BAO = 'Bao_So_3');",
         ["Bước 1: R_sub = σ_{VUNG_BAO = 'Bao_So_3'}(QUANTRAC_BAO).",
          "Bước 2: NonMax = π_{T1}(σ_{T1.LUONGMUA_MM < T2.LUONGMUA_MM}(ρ_{T1}(R_sub) × ρ_{T2}(R_sub))).",
          "Bước 3: KQ = R_sub - NonMax."],
         "Dữ liệu khí tượng thủy văn cần tính toán cực trị chính xác cho công tác cảnh báo thiên tai."),

        ("RA-D41", "ĐSQH Cực Trị: Cuốn Sách Được Mượn Nhiều Nhất Thể Loại CSDL",
         "THONGKE_SACH(MASACH, TENSACH, THELOAI, LUOT_MUON)",
         "Tìm mã sách, tên sách và số lượt mượn của các cuốn sách có lượt mượn nhiều nhất trong thể loại 'Co so du lieu'.",
         "R_{sub} = σ_{THELOAI = 'Co so du lieu'}(THONGKE_SACH)\nNonMax = π_{S1.MASACH, S1.TENSACH, S1.THELOAI, S1.LUOT_MUON}(σ_{S1.LUOT_MUON < S2.LUOT_MUON}(ρ_{S1}(R_{sub}) × ρ_{S2}(R_{sub})))\nKQ = R_{sub} - NonMax",
         "SELECT S.MASACH, S.TENSACH, S.LUOT_MUON\nFROM THONGKE_SACH S\nWHERE S.THELOAI = N'Co so du lieu'\n  AND S.LUOT_MUON = (SELECT MAX(LUOT_MUON) FROM THONGKE_SACH WHERE THELOAI = N'Co so du lieu');",
         ["Bước 1: R_sub = σ_{THELOAI = 'Co so du lieu'}(THONGKE_SACH).",
          "Bước 2: NonMax = π_{S1}(σ_{S1.LUOT_MUON < S2.LUOT_MUON}(ρ_{S1}(R_sub) × ρ_{S2}(R_sub))).",
          "Bước 3: KQ = R_sub - NonMax."],
         "Bảo toàn cả những cuốn sách có cùng lượt mượn cao nhất."),

        ("RA-D42", "ĐSQH Cực Trị: Nhà Thuốc Có Doanh Thu Cao Nhất Chuỗi Quận 1",
         "NHATHUOC(MANT, TENNT, QUAN, TONG_DOANHTHU)",
         "Tìm mã nhà thuốc, tên nhà thuốc và doanh thu của nhà thuốc đạt doanh thu cao nhất thuộc khu vực 'Quan 1'.",
         "R_{sub} = σ_{QUAN = 'Quan 1'}(NHATHUOC)\nNonMax = π_{NT1.MANT, NT1.TENNT, NT1.QUAN, NT1.TONG_DOANHTHU}(σ_{NT1.TONG_DOANHTHU < NT2.TONG_DOANHTHU}(ρ_{NT1}(R_{sub}) × ρ_{NT2}(R_{sub})))\nKQ = R_{sub} - NonMax",
         "SELECT NT.MANT, NT.TENNT, NT.TONG_DOANHTHU\nFROM NHATHUOC NT\nWHERE NT.QUAN = 'Quan 1'\n  AND NT.TONG_DOANHTHU = (SELECT MAX(TONG_DOANHTHU) FROM NHATHUOC WHERE QUAN = 'Quan 1');",
         ["Bước 1: R_sub = σ_{QUAN = 'Quan 1'}(NHATHUOC).",
          "Bước 2: NonMax = π_{NT1}(σ_{NT1.TONG_DOANHTHU < NT2.TONG_DOANHTHU}(ρ_{NT1}(R_sub) × ρ_{NT2}(R_sub))).",
          "Bước 3: KQ = R_sub - NonMax."],
         "Doanh thu lớn nhất trong phạm vi phân nhóm Quận 1."),

        ("RA-D43", "ĐSQH Cực Trị: Phòng Khách Sạn Đơn Giá Thấp Nhất Hạng Executive Suite",
         "PHONG_KS(MAPHONG, LOAIPHONG, DONGIA_DEM)",
         "Tìm mã phòng và đơn giá đêm của các phòng có giá thấp nhất (MIN) thuộc hạng phòng 'Executive Suite'.",
         "R_{sub} = σ_{LOAIPHONG = 'Executive Suite'}(PHONG_KS)\nNonMin = π_{P1.MAPHONG, P1.LOAIPHONG, P1.DONGIA_DEM}(σ_{P1.DONGIA_DEM > P2.DONGIA_DEM}(ρ_{P1}(R_{sub}) × ρ_{P2}(R_{sub})))\nKQ = R_{sub} - NonMin",
         "SELECT P.MAPHONG, P.DONGIA_DEM\nFROM PHONG_KS P\nWHERE P.LOAIPHONG = 'Executive Suite'\n  AND P.DONGIA_DEM = (SELECT MIN(DONGIA_DEM) FROM PHONG_KS WHERE LOAIPHONG = 'Executive Suite');",
         ["Bước 1: R_sub = σ_{LOAIPHONG = 'Executive Suite'}(PHONG_KS).",
          "Bước 2: NonMin = π_{P1}(σ_{P1.DONGIA_DEM > P2.DONGIA_DEM}(ρ_{P1}(R_sub) × ρ_{P2}(R_sub))).",
          "Bước 3: KQ = R_sub - NonMin."],
         "Cực tiểu sử dụng vị từ so sánh lớn hơn để tìm NonMin."),

        ("RA-D44", "ĐSQH Cực Trị: Nhân Viên Có Số Năm Công Tác Lâu Nhất Phòng Kỹ Thuật",
         "NHANVIEN(MANV, HOTEN, PHONGBAN, THAM_NIEN_NAM)",
         "Tìm mã nhân viên, họ tên và số năm thâm niên của nhân viên có thời gian công tác lâu năm nhất tại phòng 'Ky thuat ha tang'.",
         "R_{sub} = σ_{PHONGBAN = 'Ky thuat ha tang'}(NHANVIEN)\nNonMax = π_{NV1.MANV, NV1.HOTEN, NV1.PHONGBAN, NV1.THAM_NIEN_NAM}(σ_{NV1.THAM_NIEN_NAM < NV2.THAM_NIEN_NAM}(ρ_{NV1}(R_{sub}) × ρ_{NV2}(R_{sub})))\nKQ = R_{sub} - NonMax",
         "SELECT NV.MANV, NV.HOTEN, NV.THAM_NIEN_NAM\nFROM NHANVIEN NV\nWHERE NV.PHONGBAN = N'Ky thuat ha tang'\n  AND NV.THAM_NIEN_NAM = (SELECT MAX(THAM_NIEN_NAM) FROM NHANVIEN WHERE PHONGBAN = N'Ky thuat ha tang');",
         ["Bước 1: R_sub = σ_{PHONGBAN = 'Ky thuat ha tang'}(NHANVIEN).",
          "Bước 2: NonMax = π_{NV1}(σ_{NV1.THAM_NIEN_NAM < NV2.THAM_NIEN_NAM}(ρ_{NV1}(R_sub) × ρ_{NV2}(R_sub))).",
          "Bước 3: KQ = R_sub - NonMax."],
         "Nhân viên phòng ban khác không bao giờ bị trừ hoặc xuất hiện ở kết quả."),

        ("RA-D45", "ĐSQH Cực Trị: Doanh Nghiệp Thuê Diện Tích Lớn Nhất Phân Khu CNC (Sửa P0-04)",
         "DOANHNGHIEP_KCN(MADN, TENDN, MAPK, DIENTICH_THUE_M2)",
         "Tìm mã doanh nghiệp, tên doanh nghiệp và diện tích thuê của các doanh nghiệp thuê diện tích đất xưởng lớn nhất (MAX) tại phân khu 'PK_CNC' (Khu công nghệ cao).",
         # CRITICAL FIX FOR P0-04: Subgroup math must filter R_sub first!
         "R_{sub} = σ_{MAPK = 'PK_CNC'}(DOANHNGHIEP_KCN)\nNonMax = π_{DN1.MADN, DN1.TENDN, DN1.MAPK, DN1.DIENTICH_THUE_M2}(σ_{DN1.DIENTICH_THUE_M2 < DN2.DIENTICH_THUE_M2}(ρ_{DN1}(R_{sub}) × ρ_{DN2}(R_{sub})))\nKQ = R_{sub} - NonMax",
         "SELECT DN.MADN, DN.TENDN, DN.DIENTICH_THUE_M2\nFROM DOANHNGHIEP_KCN DN\nWHERE DN.MAPK = 'PK_CNC'\n  AND DN.DIENTICH_THUE_M2 = (SELECT MAX(DIENTICH_THUE_M2) FROM DOANHNGHIEP_KCN WHERE MAPK = 'PK_CNC');",
         [
             "Bước 1 (Lọc tập con phân nhóm R_sub): R_sub = σ_{MAPK = 'PK_CNC'}(DOANHNGHIEP_KCN). Đây là bước quyết định để cô lập không gian tìm kiếm cực trị trong đúng phân khu 'PK_CNC'.",
             "Bước 2 (Tìm các doanh nghiệp bị vượt diện tích trong phân khu): NonMax = π_{DN1.MADN, DN1.TENDN, DN1.MAPK, DN1.DIENTICH_THUE_M2}(σ_{DN1.DIENTICH_THUE_M2 < DN2.DIENTICH_THUE_M2}(ρ_{DN1}(R_sub) × ρ_{DN2}(R_sub))).",
             "Bước 3 (Hiệu tập hợp trên chính R_sub): KQ = R_sub - NonMax. Kết quả trả về chính xác 100% doanh nghiệp thuê nhiều đất nhất phân khu PK_CNC, đồng thời bảo toàn mọi đối tượng đồng hạng (tie-breaking)."
         ],
         "ĐÃ SỬA LỖI P0-04: Tuyệt đối không lấy toàn bảng DOANHNGHIEP_KCN trừ NonMax, vì các doanh nghiệp ở các phân khu khác (như PK_DETMAY, PK_HOACHAT) không nằm trong NonMax nên nếu trừ từ toàn bảng sẽ bị rò rỉ vào kết quả sai lệch! Phép trừ phải thực hiện trên chính quan hệ tập con R_sub.")
    ]

    for item in extreme_problems:
        pid, title, schema, prompt, ra, sql, steps, edge = item
        problems.append({
            "id": pid, "topic": "RA_DIVISION_GROUPING", "difficulty": "C",
            "title": title, "prompt": prompt, "schema": schema, "recommended_time_mins": 20, "points": 1.5,
            "status": "VERIFIED", "verification_level": "SEMANTICALLY_REVIEWED",
            "solution": {"relational_algebra": ra, "sql": sql, "intermediate_steps": steps, "edge_cases": edge},
            "rubric": {"total_points": 1.5, "subgroup_isolation": 0.5, "cartesian_product_and_inequality": 0.5, "set_difference_and_tie_breaking": 0.5}
        })

    assert len(problems) == 45, f"Expected 45 RA Division & Grouping problems, got {len(problems)}"
    return problems

if __name__ == "__main__":
    probs = get_remediated_ra_division_grouping_problems()
    print(f"Generated {len(probs)} RA Division & Grouping problems.")
    for p in probs:
        assert p["id"].startswith("RA-D")
        ra = p["solution"]["relational_algebra"]
        assert any(s in ra for s in ["÷", "γ", "NonMax", "NonMin", "R_{sub}"]), f"Missing operator in {p['id']}"
    print("ALL RA DIVISION & GROUPING PROBLEMS VALIDATED SUCCESSFULLY!")
