# -*- coding: utf-8 -*-
"""
scripts/build_independent_bank_data.py
Constructs the complete 150 independent practice questions for IT004 GK:
- Topic 1: ERD & Relational Mapping (25 problems: ERD-P01 .. ERD-P25)
- Topic 2: Relational Algebra Basic & Joins (45 problems: RA-B01 .. RA-B45)
- Topic 3: Relational Algebra Division & Grouping (45 problems: RA-D01 .. RA-D45)
- Topic 4: SQL DDL, DML & Constraints (35 problems: SQL-P01 .. SQL-P35)
Total independent practice questions = 150 problems.
Combined with 135 mock questions = 285 problems.
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
DATA_DIR = REPO_ROOT / "exam" / "gk" / "data"

def get_erd_problems():
    domains = [
        ("ERD-P01", "Quản Lý Đăng Ký Học Phần & Thời Khóa Biểu UIT",
         "SINHVIEN(MSSV, HOTEN, NGAYSINH, PHAI, MALOP), GIANGVIEN(MAGV, HOTEN, HOCHAM, HOCVI), MONHOC(MAMH, TENMH, SOTC), LOPHOCPHAN(MALHP, MAMH, MAGV, HOCKY, NAMHOC, PHONG), DANGKY(MSSV, MALHP, DIEMGK, DIEMCK)",
         "Thiết kế mô hình ERD và chuyển sang Lược đồ quan hệ cho Hệ thống Quản lý Đăng ký học phần tín chỉ tại UIT. Hệ thống cần quản lý thông tin sinh viên, giảng viên, môn học, các lớp học phần mở trong từng học kỳ và kết quả đăng ký học phần của sinh viên.",
         ["SINHVIEN: MSSV, HOTEN, NGAYSINH, PHAI, MALOP", "GIANGVIEN: MAGV, HOTEN, HOCHAM, HOCVI", "MONHOC: MAMH, TENMH, SOTC", "LOPHOCPHAN: MALHP, HOCKY, NAMHOC, PHONG", "DANGKY: DIEMGK, DIEMCK"],
         ["SINHVIEN - DANGKY - LOPHOCPHAN: M:N (Một SV đăng ký nhiều LHP, một LHP có nhiều SV)", "GIANGVIEN - LOPHOCPHAN: 1:N (Một GV phụ trách nhiều LHP)", "MONHOC - LOPHOCPHAN: 1:N (Một MH mở nhiều LHP)"]),

        ("ERD-P02", "Quản Lý Ký Túc Xá Sinh Viên Đại Học",
         "TOANHA(MATN, TENTN, DIACHI, SOTANG), PHONG(MAPHONG, MATN, TENPHONG, SOGIUONG, GIALE), SINHVIEN(MSSV, HOTEN, GIOITINH, SDT, QUEQUAN), HOPDONG(MAHD, MSSV, MAPHONG, NGAYBD, NGAYKT, TIENCOC), DICHVU(MADV, TENDV, DONGIA), SUDUNG_DV(MAHD, MADV, THANG, NAM, CHISO_CU, CHISO_MOI)",
         "Thiết kế mô hình ERD và chuyển đổi quan hệ cho Hệ thống Ký túc xá Đại học gồm các tòa nhà, phòng ở, sinh viên lưu trú, hợp đồng thuê phòng và việc sử dụng các dịch vụ (điện, nước, internet).",
         ["TOANHA: MATN, TENTN, DIACHI, SOTANG", "PHONG: MAPHONG, TENPHONG, SOGIUONG, GIALE", "SINHVIEN: MSSV, HOTEN, GIOITINH, SDT, QUEQUAN", "HOPDONG: MAHD, NGAYBD, NGAYKT, TIENCOC", "DICHVU: MADV, TENDV, DONGIA"],
         ["TOANHA - PHONG: 1:N (Tòa nhà có nhiều phòng)", "PHONG - HOPDONG: 1:N (Phòng được thuê qua nhiều HĐ theo thời gian)", "SINHVIEN - HOPDONG: 1:N (SV có thể ký nhiều HĐ qua các năm)", "HOPDONG - DICHVU: M:N (Mối kết hợp SUDUNG_DV)"]),

        ("ERD-P03", "Quản Lý Chuỗi Nhà Thuốc & Bán Lẻ Dược Phẩm",
         "NHATHUOC(MANT, TENNT, DIACHI, DUOCSI_QL), DUOCSI(MADS, HOTEN, BANGTHOAN, SDT, MANT), THUOC(MATHUOC, TENTHUOC, HOATCHAT, DVT, DONGIA), HOADON(MAHD, MANT, MADS, NGAYLAP, HOTEN_KH), CHITIET_HD(MAHD, MATHUOC, SOLUONG, GIABAN)",
         "Thiết kế mô hình ERD và lược đồ quan hệ cho Chuỗi Nhà thuốc bán lẻ gồm thông tin nhà thuốc, dược sĩ, danh mục dược phẩm và các hóa đơn bán hàng theo đơn hoặc không kê đơn.",
         ["NHATHUOC: MANT, TENNT, DIACHI", "DUOCSI: MADS, HOTEN, BANGTHOAN, SDT", "THUOC: MATHUOC, TENTHUOC, HOATCHAT, DVT, DONGIA", "HOADON: MAHD, NGAYLAP, HOTEN_KH"],
         ["NHATHUOC - DUOCSI: 1:N (Dược sĩ công tác tại 1 nhà thuốc; 1 dược sĩ làm quản lý 1:1)", "DUOCSI - HOADON: 1:N (Dược sĩ lập hóa đơn)", "NHATHUOC - HOADON: 1:N (Hóa đơn phát sinh tại nhà thuốc)", "HOADON - THUOC: M:N qua CHITIET_HD"]),

        ("ERD-P04", "Quản Lý Hãng Hàng Không & Lịch Bay Nội Địa",
         "SANBAY(MASB, TENSB, THANHPHO, QUOCGIA), MAYBAY(MAMB, SOHIEU, LOAIMB, SOGHE, NAMSX), CHUYENBAY(MACB, MAMB, MASB_DI, MASB_DEN, NGAYBAY, GIOBAY, GIAGOC), HANHKHACH(MAHK, HOTEN, CCCD, SDT, EMAIL), VEBAY(MAVE, MACB, MAHK, SOGHE, HANGVE, GIATHOA)",
         "Thiết kế mô hình ERD quản lý lịch trình các chuyến bay, máy bay khai thác, sân bay đi - đến và hành khách mua vé của một hãng hàng không nội địa.",
         ["SANBAY: MASB, TENSB, THANHPHO, QUOCGIA", "MAYBAY: MAMB, SOHIEU, LOAIMB, SOGHE, NAMSX", "CHUYENBAY: MACB, NGAYBAY, GIOBAY, GIAGOC", "HANHKHACH: MAHK, HOTEN, CCCD, SDT", "VEBAY: MAVE, SOGHE, HANGVE, GIATHOA"],
         ["MAYBAY - CHUYENBAY: 1:N (Máy bay thực hiện nhiều chuyến bay)", "SANBAY - CHUYENBAY (Khởi hành): 1:N", "SANBAY - CHUYENBAY (Hạ cánh): 1:N", "CHUYENBAY - HANHKHACH: M:N qua thực thể yếu VEBAY"]),

        ("ERD-P05", "Quản Lý Hệ Thống Tuyển Sinh & Xét Tuyển Đại Học",
         "NGANH(MANGANH, TENNANH, CHITIEU, DIEMCHUAN), THISINH(SBD, HOTEN, NGAYSINH, KHUVUC, DIEMTOC), MONTHI(MAMT, TENMT), DIEMTHI(SBD, MAMT, DIEMSO), NGUYENVONG(SBD, THUTU_NV, MANGANH, TOHOP, TRANGTHAI)",
         "Thiết kế ERD cho Hệ thống Đăng ký Xét tuyển Đại học: Thí sinh đăng ký nhiều nguyện vọng theo thứ tự ưu tiên vào các ngành học, quản lý điểm thi các môn theo tổ hợp xét tuyển.",
         ["NGANH: MANGANH, TENNANH, CHITIEU, DIEMCHUAN", "THISINH: SBD, HOTEN, NGAYSINH, KHUVUC", "MONTHI: MAMT, TENMT", "NGUYENVONG: THUTU_NV, TOHOP, TRANGTHAI", "DIEMTHI: DIEMSO"],
         ["THISINH - MONTHI: M:N qua DIEMTHI (SBD, MAMT)", "THISINH - NGANH: M:N qua NGUYENVONG (SBD, THUTU_NV, MANGANH)"]),

        ("ERD-P06", "Quản Lý Hệ Thống Ngân Hàng & Giao Dịch Thẻ ATM",
         "CHINHANH(MACN, TENCN, DIACHI, SDT), KHACHHANG(MAKH, HOTEN, CCCD, DIACHI, SDT), TAIKHOAN(SOTK, MAKH, MACN, SODU, LOAITK, NGAYMO), THE_ATM(MATHE, SOTK, NGAYPHATHANH, NGAYHETHAN, LOAITHE), GIAODICH(MAGD, MATHE, NGAYGD, SOTIEN, LOAIGD, NOIDUNG)",
         "Thiết kế ERD cho Hệ thống Ngân hàng thương mại: Quản lý khách hàng, tài khoản thanh toán tại các chi nhánh, phát hành thẻ ATM và lịch sử các giao dịch gửi/rút/chuyển khoản.",
         ["CHINHANH: MACN, TENCN, DIACHI, SDT", "KHACHHANG: MAKH, HOTEN, CCCD, DIACHI", "TAIKHOAN: SOTK, SODU, LOAITK, NGAYMO", "THE_ATM: MATHE, NGAYPHATHANH, NGAYHETHAN", "GIAODICH: MAGD, NGAYGD, SOTIEN, LOAIGD"],
         ["CHINHANH - TAIKHOAN: 1:N", "KHACHHANG - TAIKHOAN: 1:N", "TAIKHOAN - THE_ATM: 1:N (1 TK có thể mở nhiều thẻ phụ)", "THE_ATM - GIAODICH: 1:N"]),

        ("ERD-P07", "Quản Lý Khách Sạn & Đặt Phòng Nghỉ Dưỡng",
         "KHACHSAN(MAKS, TENKS, DIACHI, TIEUCHUAN_SAO), LOAIPHONG(MALP, TENLP, SOGIUONG, DONGIA_NGAY), PHONG(MAPHONG, MAKS, MALP, SOPHONG, TRANGTHAI), KHACHHANG(MAKH, HOTEN, SDT, QUOCTICH), PHIEUDAT(MAPD, MAKH, MAPHONG, NGAYDEN, NGAYDI, TIENCOC)",
         "Thiết kế mô hình ERD quản lý chuỗi khách sạn nghỉ dưỡng: Quản lý chi nhánh khách sạn, các loại phòng, danh sách phòng thực tế và các phiếu đặt phòng của khách hàng.",
         ["KHACHSAN: MAKS, TENKS, DIACHI, TIEUCHUAN_SAO", "LOAIPHONG: MALP, TENLP, SOGIUONG, DONGIA_NGAY", "PHONG: MAPHONG, SOPHONG, TRANGTHAI", "KHACHHANG: MAKH, HOTEN, SDT, QUOCTICH", "PHIEUDAT: MAPD, NGAYDEN, NGAYDI, TIENCOC"],
         ["KHACHSAN - PHONG: 1:N", "LOAIPHONG - PHONG: 1:N", "KHACHHANG - PHIEUDAT: 1:N", "PHONG - PHIEUDAT: 1:N"]),

        ("ERD-P08", "Quản Lý Xuất Bản & Phát Hành Sách",
         "NXB(MANXB, TENNXB, DIACHI, EMAIL), TACGIA(MATG, HOTEN, BUTDANH, QUOCTICH), SACH(MASACH, TENSACH, MANXB, NAMXB, TIENTHOA), BIENSOAN(MATG, MASACH, VAITRO), DAILI(MADL, TENDL, DIACHI, SDT), PHIEUXUAT_SACH(MAPX, MADL, MASACH, NGAYXUAT, SOLUONG, DONGIAXUAT)",
         "Thiết kế mô hình ERD cho Nhà xuất bản: Quản lý tác giả biên soạn sách (một sách có thể do nhiều tác giả đồng biên soạn), bản quyền xuất bản và phân phối đến các đại lý.",
         ["NXB: MANXB, TENNXB, DIACHI", "TACGIA: MATG, HOTEN, BUTDANH, QUOCTICH", "SACH: MASACH, TENSACH, NAMXB, TIENTHOA", "DAILI: MADL, TENDL, DIACHI, SDT", "PHIEUXUAT: MAPX, NGAYXUAT, SOLUONG, DONGIAXUAT"],
         ["NXB - SACH: 1:N", "TACGIA - SACH: M:N qua BIENSOAN (MATG, MASACH, VAITRO)", "SACH - DAILI: M:N qua PHIEUXUAT_SACH"]),

        ("ERD-P09", "Quản Lý Giao Hàng Chuyển Phát Nhanh Express",
         "BUUCUC(MABC, TENBC, DIACHI, SDT), BUUTA(MABT, HOTEN, SDT, MABC), KHACHHANG(MAKH, HOTEN, DIACHI, SDT), DONHANG(MADON, MAKH_GUI, MAKH_NHAN, MABT, NGAYGUI, TRANGTHAI, PHIVC), KIENHANG(MAKIEN, MADON, MOTA, TRONGLUONG_KG, KICHTHUOC)",
         "Thiết kế ERD cho Hệ thống Giao hàng nhanh: Khách hàng gửi đơn hàng từ bưu cục, bưu tá nhận phụ trách vận chuyển, đơn hàng gồm nhiều kiện hàng có trọng lượng khác nhau.",
         ["BUUCUC: MABC, TENBC, DIACHI", "BUUTA: MABT, HOTEN, SDT", "KHACHHANG: MAKH, HOTEN, DIACHI, SDT", "DONHANG: MADON, NGAYGUI, TRANGTHAI, PHIVC", "KIENHANG: MAKIEN, MOTA, TRONGLUONG_KG"],
         ["BUUCUC - BUUTA: 1:N", "BUUTA - DONHANG: 1:N", "KHACHHANG (Gửi/Nhận) - DONHANG: 1:N", "DONHANG - KIENHANG: 1:N (Thực thể yếu Kiện hàng)"]),

        ("ERD-P10", "Quản Lý Chuỗi Siêu Thị Mini & Nhà Cung Cấp",
         "CUAHANG(MACH, TENCH, DIACHI, QUAN), NHANVIEN(MANV, HOTEN, CHUCVU, MACH), NHACUNGCAP(MANCC, TENNCC, DIACHI, SDT), MAT_HANG(MAMH, TENMH, DVT, DONGIA_BAN), DON_NHAP(MADN, MACH, MANCC, NGAYNHAP, TONGTIEN), CT_NHAP(MADN, MAMH, SOLUONG, DONGIANHAP)",
         "Thiết kế ERD cho chuỗi siêu thị tiện lợi: Quản lý các cửa hàng chi nhánh, nhân viên làm việc, nhà cung cấp giao các lô hàng và bán hàng cho người tiêu dùng.",
         ["CUAHANG: MACH, TENCH, DIACHI, QUAN", "NHANVIEN: MANV, HOTEN, CHUCVU", "NHACUNGCAP: MANCC, TENNCC, DIACHI", "MAT_HANG: MAMH, TENMH, DVT, DONGIA_BAN", "DON_NHAP: MADN, NGAYNHAP, TONGTIEN"],
         ["CUAHANG - NHANVIEN: 1:N", "CUAHANG - DON_NHAP: 1:N", "NHACUNGCAP - DON_NHAP: 1:N", "DON_NHAP - MAT_HANG: M:N qua CT_NHAP"]),

        ("ERD-P11", "Quản Lý Trung Tâm Ngoại Ngữ & Thi Chứng Chỉ",
         "TRUNGTAM(MATT, TENTT, DIACHI), KHOAHOC(MAKH, TENKH, THOILUONG, HOCPHI), LOPHOC(MALOP, MAKH, MATT, NGAYBD, PHONG), GIAOVIEN(MAGV, HOTEN, CHUNGCHI, SDT), PHANCONG_DAY(MALOP, MAGV, THULAODAY), HOCVIEN(MAHV, HOTEN, NGAYSINH, SDT), DANGKY_HOC(MALOP, MAHV, NGAYDK, DIEMTHI)",
         "Thiết kế ERD quản lý trung tâm đào tạo tiếng Anh: Các khóa học (IELTS, TOEIC), mở thành nhiều lớp tại các chi nhánh, giáo viên giảng dạy và học viên đăng ký theo học.",
         ["TRUNGTAM: MATT, TENTT, DIACHI", "KHOAHOC: MAKH, TENKH, THOILUONG, HOCPHI", "LOPHOC: MALOP, NGAYBD, PHONG", "GIAOVIEN: MAGV, HOTEN, CHUNGCHI", "HOCVIEN: MAHV, HOTEN, NGAYSINH"],
         ["TRUNGTAM - LOPHOC: 1:N", "KHOAHOC - LOPHOC: 1:N", "LOPHOC - GIAOVIEN: M:N qua PHANCONG_DAY", "LOPHOC - HOCVIEN: M:N qua DANGKY_HOC"]),

        ("ERD-P12", "Quản Lý Bảo Hiểm Y Tế & Khám Chữa Bệnh",
         "COQUAN_BH(MACQ, TENCQ, TINH_TP), BENHNHAN(MABN, HOTEN, NGAYSINH, CCCD, DIACHI), THE_BHYT(MATHE, MABN, MACQ, NGAYCAP, HANSUDUNG, MUC_HUONG), BENHVIEN(MABV, TENBV, TUYEN_BV, DIACHI), DOT_KHAM(MA_DK, MATHE, MABV, NGAYKHAM, CHANDOAN, CHIPHI_TONG, BHYT_CHITRA)",
         "Thiết kế ERD cho Hệ thống Bảo hiểm y tế toàn dân: Cơ quan BH cấp thẻ cho công dân, công dân sử dụng thẻ để khám chữa bệnh tại các bệnh viện theo tuyến quy định.",
         ["COQUAN_BH: MACQ, TENCQ, TINH_TP", "BENHNHAN: MABN, HOTEN, NGAYSINH, CCCD", "THE_BHYT: MATHE, NGAYCAP, HANSUDUNG, MUC_HUONG", "BENHVIEN: MABV, TENBV, TUYEN_BV", "DOT_KHAM: MA_DK, NGAYKHAM, CHANDOAN, CHIPHI_TONG"],
         ["BENHNHAN - THE_BHYT: 1:1 (hoặc 1:N theo từng đợt cấp)", "COQUAN_BH - THE_BHYT: 1:N", "THE_BHYT - DOT_KHAM: 1:N", "BENHVIEN - DOT_KHAM: 1:N"]),

        ("ERD-P13", "Quản Lý Bãi Đỗ Xe Tự Động Smart Parking",
         "BAIDO(MABD, TENBD, DIACHI, SUCCHUA), KHUVUC(MAKV, MABD, TENKV, LOAIXE_CHO_PHEP), VITRI_DO(MAVT, MAKV, SOVITRI, TRANGTHAI), KHACHHANG(MAKH, HOTEN, SDT), PHUONGTIEN(BIENSO, MAKH, LOAIXE, MAUXE), LUOT_GUI(MALUOT, BIENSO, MAVT, THOIGIAPVAO, THOIGIARA, GIATIEN)",
         "Thiết kế ERD cho Hệ thống Bãi đỗ xe thông minh: Quản lý bãi đỗ phân chia theo các khu vực đỗ, vị trí đỗ dành cho xe máy/ô tô và các lượt gửi xe có thời gian vào - ra.",
         ["BAIDO: MABD, TENBD, DIACHI, SUCCHUA", "KHUVUC: MAKV, TENKV, LOAIXE_CHO_PHEP", "VITRI_DO: MAVT, SOVITRI, TRANGTHAI", "KHACHHANG: MAKH, HOTEN, SDT", "PHUONGTIEN: BIENSO, LOAIXE", "LUOT_GUI: MALUOT, THOIGIAPVAO, THOIGIARA, GIATIEN"],
         ["BAIDO - KHUVUC: 1:N", "KHUVUC - VITRI_DO: 1:N", "KHACHHANG - PHUONGTIEN: 1:N", "PHUONGTIEN - LUOT_GUI: 1:N", "VITRI_DO - LUOT_GUI: 1:N"]),

        ("ERD-P14", "Quản Lý Nhà Hàng & Bàn Ăn Trực Tuyến",
         "KHUVUC_BAN(MAKV, TENKV, PHUTHU), BANAN(MABAN, MAKV, SOBAN, SOGHE, TRANGTHAI), MONAN(MAMON, TENMON, DVT, DONGIA, LOAIMON), NHANVIEN(MANV, HOTEN, CALAM, SDT), HOADON(MAHD, MABAN, MANV, NGAYLAP, GIOLAP, TONGTIEN), CT_GOIMON(MAHD, MAMON, SOLUONG, GHICHU)",
         "Thiết kế ERD quản lý nhà hàng ẩm thực: Bàn ăn phân bổ theo các khu vực (VIP, sân vườn, phòng lạnh), nhân viên phục vụ mở bàn và ghi nhận danh sách món ăn gọi cho khách.",
         ["KHUVUC_BAN: MAKV, TENKV, PHUTHU", "BANAN: MABAN, SOBAN, SOGHE, TRANGTHAI", "MONAN: MAMON, TENMON, DVT, DONGIA", "NHANVIEN: MANV, HOTEN, CALAM", "HOADON: MAHD, NGAYLAP, GIOLAP, TONGTIEN"],
         ["KHUVUC_BAN - BANAN: 1:N", "BANAN - HOADON: 1:N", "NHANVIEN - HOADON: 1:N", "HOADON - MONAN: M:N qua CT_GOIMON"]),

        ("ERD-P15", "Quản Lý Triển Lãm & Tác Phẩm Nghệ Thuật",
         "BAOTANG(MABT, TENBT, THANHPHO), HOASI(MAHS, HOTEN, NAMSINH, QUOCTICH, PHONGCACH), TACPHAM(MATP, TENTP, MAHS, NAMST, CHATLIEU, GIATRIdo_USD), TRIENLAM(MATL, TENTL, MABT, NGAYBD, NGAYKT), TRUNGBAY(MATL, MATP, VITRI_TREO, BAOHIEM_USD)",
         "Thiết kế ERD cho Bảo tàng mỹ thuật: Quản lý họa sĩ sáng tác tác phẩm, bảo tàng tổ chức các đợt triển lãm và danh sách tác phẩm được trưng bày trong từng đợt.",
         ["BAOTANG: MABT, TENBT, THANHPHO", "HOASI: MAHS, HOTEN, NAMSINH, QUOCTICH", "TACPHAM: MATP, TENTP, NAMST, CHATLIEU, GIATRI", "TRIENLAM: MATL, TENTL, NGAYBD, NGAYKT"],
         ["HOASI - TACPHAM: 1:N", "BAOTANG - TRIENLAM: 1:N", "TRIENLAM - TACPHAM: M:N qua TRUNGBAY"]),

        ("ERD-P16", "Quản Lý Trạm Sạc Xe Điện Toàn Quốc",
         "TRAMSAC(MATS, TENTS, DIACHI, TOADO_GPS), TRUSAC(MATRU, MATS, CONGSUAT_KW, CHUAN_CAM, TRANGTHAI), KHACHHANG(MAKH, HOTEN, SDT, SOTK_THANHTOAN), XEDIEN(BIENSO, MAKH, HANGXE, DUDUNGLUONG_PIN), PHIEN_SAC(MAPHIEN, MATRU, BIENSO, GIO_BD, GIO_KT, SODIEN_KWH, THANHTIEN)",
         "Thiết kế ERD cho Mạng lưới trạm sạc xe điện thông minh: Mỗi trạm có nhiều trụ sạc công suất khác nhau (sạc nhanh, sạc siêu nhanh), ghi nhận lịch sử phiên sạc của phương tiện.",
         ["TRAMSAC: MATS, TENTS, DIACHI, TOADO_GPS", "TRUSAC: MATRU, CONGSUAT_KW, CHUAN_CAM", "KHACHHANG: MAKH, HOTEN, SDT", "XEDIEN: BIENSO, HANGXE, DUDUNGLUONG_PIN", "PHIEN_SAC: MAPHIEN, GIO_BD, GIO_KT, SODIEN_KWH, THANHTIEN"],
         ["TRAMSAC - TRUSAC: 1:N", "KHACHHANG - XEDIEN: 1:N", "TRUSAC - PHIEN_SAC: 1:N", "XEDIEN - PHIEN_SAC: 1:N"]),

        ("ERD-P17", "Quản Lý Nhà Hát Kịch & Vé Buổi Diễn",
         "RAPHAT(MARAP, TENRAP, DIACHI, SOGHE), VOIKICH(MAVK, TENTACPHAM, DAODIEN, THOILUONG), NGHESI(MANS, HOTEN, DANHHIEU, CHUYENMON), BUOIDISEN(MABD, MARAP, MAVK, NGAYDIEN, GIODIEN, GIAVE_CHUAN), THAMGIA_VK(MAVK, MANS, VAIDIEN), VE_XEM(MAVE, MABD, SOGHE, TENKHACH, SDT, GIATHU)",
         "Thiết kế ERD quản lý sân khấu kịch nghệ: Các vở kịch do nhiều nghệ sĩ tham gia diễn xuất, tổ chức diễn tại các rạp hát và phát hành vé ngồi cho khán giả.",
         ["RAPHAT: MARAP, TENRAP, DIACHI, SOGHE", "VOIKICH: MAVK, TENTACPHAM, DAODIEN, THOILUONG", "NGHESI: MANS, HOTEN, DANHHIEU", "BUOIDISEN: MABD, NGAYDIEN, GIODIEN", "VE_XEM: MAVE, SOGHE, TENKHACH, GIATHU"],
         ["RAPHAT - BUOIDISEN: 1:N", "VOIKICH - BUOIDISEN: 1:N", "VOIKICH - NGHESI: M:N qua THAMGIA_VK", "BUOIDISEN - VE_XEM: 1:N"]),

        ("ERD-P18", "Quản Lý Đội Xe Cứu Thương Khẩn Cấp 115",
         "BENHVIEN(MABV, TENBV, DIACHI, SDT_CAPCUU), DOIXE(MADOI, MABV, TENDOI), XECUUTHUONG(MAXE, MADOI, BIENSO, TRANGTHIETBI, TRANGTHAI), NHANSU(MANS, HOTEN, CHUCDANH, MADOI), CUOCGOI_CC(MACUOC, NGAYGIO, DIACHINHAN, HOTEN_BENHNHAN, TINHTRANG), DIEUDONG(MACUOC, MAXE, MANS_TAIXE, MANS_YTA, GIO_XUATPHAT, GIO_DEN)",
         "Thiết kế ERD cho Đội xe cứu thương khẩn cấp: Bệnh viện quản lý đội xe và nhân sự (tài xế, y tá), tiếp nhận cuộc gọi cấp cứu và điều động phương tiện đến hiện trường.",
         ["BENHVIEN: MABV, TENBV, DIACHI", "DOIXE: MADOI, TENDOI", "XECUUTHUONG: MAXE, BIENSO, TRANGTHAI", "NHANSU: MANS, HOTEN, CHUCDANH", "CUOCGOI_CC: MACUOC, NGAYGIO, DIACHINHAN, TINHTRANG"],
         ["BENHVIEN - DOIXE: 1:N", "DOIXE - XECUUTHUONG: 1:N", "DOIXE - NHANSU: 1:N", "CUOCGOI_CC - DIEUDONG: 1:N", "XECUUTHUONG - DIEUDONG: 1:N"]),

        ("ERD-P19", "Quản Lý Phòng Gym & Huấn Luyện Viên Cá Nhân",
         "PHONGGYM(MAPG, TENPG, DIACHI, HOTLINE), HLV(MAHLV, HOTEN, CHUYENMON, CHUNGCHI, MAPG), HOIVIEN(MAHV, HOTEN, NGAYSINH, SDT, GIOITINH), GOITAP(MAGT, TENGT, THOIHAN_THANG, GIATIEN), THE_HOIVIEN(MATHE, MAHV, MAGT, MAPG, NGAYKICHHOAT, HANSUDUNG), LICHHEN_PT(MALICH, MATHE, MAHLV, NGAYTAP, GIOTAP, NOIDUNGTAP)",
         "Thiết kế ERD cho Hệ thống Fitness & Gym: Hội viên đăng ký các gói tập (thẻ hội viên), thuê huấn luyện viên cá nhân (PT) và đặt lịch tập luyện định kỳ.",
         ["PHONGGYM: MAPG, TENPG, DIACHI", "HLV: MAHLV, HOTEN, CHUYENMON, CHUNGCHI", "HOIVIEN: MAHV, HOTEN, NGAYSINH, SDT", "GOITAP: MAGT, TENGT, THOIHAN_THANG, GIATIEN", "THE_HOIVIEN: MATHE, NGAYKICHHOAT, HANSUDUNG", "LICHHEN_PT: MALICH, NGAYTAP, GIOTAP"],
         ["PHONGGYM - HLV: 1:N", "HOIVIEN - THE_HOIVIEN: 1:N", "GOITAP - THE_HOIVIEN: 1:N", "PHONGGYM - THE_HOIVIEN: 1:N", "THE_HOIVIEN - LICHHEN_PT: 1:N", "HLV - LICHHEN_PT: 1:N"]),

        ("ERD-P20", "Quản Lý Nông Nghiệp Công Nghệ Cao Smart Farm",
         "TRANGTRAI(MATT, TENTT, VITRI, DIENTICH_HA), KHUNHATRONG(MAKHU, MATT, TENKHU, LOAITRUONG, DIENTICH_M2), CAYTRONG(MACAY, TENCAY, GIONG, THOIVU_NGAY), DOT_TRONG(MADOT, MAKHU, MACAY, NGAYXUONGGIONG, NGAYTHUHOACH_DUKIEN, SANLUONG_KG), CAMBIEN(MACB, MAKHU, LOAICAMBIEN, NGAYLAPDAT), DULIEU_DO(MADO, MACB, THOIDIEM, NHIETDO, DOAM, PH_DAT)",
         "Thiết kế ERD cho Trang trại nông nghiệp thông minh: Quản lý khu nhà màng, cây trồng theo từng mùa vụ và hệ thống cảm biến IoT thu thập dữ liệu đất, nhiệt độ, độ ẩm.",
         ["TRANGTRAI: MATT, TENTT, VITRI, DIENTICH_HA", "KHUNHATRONG: MAKHU, TENKHU, LOAITRUONG", "CAYTRONG: MACAY, TENCAY, GIONG", "DOT_TRONG: MADOT, NGAYXUONGGIONG, SANLUONG_KG", "CAMBIEN: MACB, LOAICAMBIEN", "DULIEU_DO: MADO, THOIDIEM, NHIETDO, DOAM"],
         ["TRANGTRAI - KHUNHATRONG: 1:N", "KHUNHATRONG - DOT_TRONG: 1:N", "CAYTRONG - DOT_TRONG: 1:N", "KHUNHATRONG - CAMBIEN: 1:N", "CAMBIEN - DULIEU_DO: 1:N"]),

        ("ERD-P21", "Quản Lý Khu Công Nghiệp & Cho Thuê Đất Xưởng",
         "KHU_CN(MAKCN, TENKCN, TINH_TP, DIENTICH_HA), PHANKHU(MAPK, MAKCN, TENPK, QUYHOACH_NGANH), LODAT(MALO, MAPK, DIENTICH_M2, VITRI, GIATHUE_M2_NAM, TRANGTHAI), DOANHNGHIEP(MADN, TENDN, MASOTHUE, NGUOIDAIDIEN, QUOCTICH), HOPDONG_THUE(MAHD, MALO, MADN, NGAYKY, THOIHAN_NAM, TIENCOC, GIATHUE_HANGNAM)",
         "Thiết kế ERD cho Ban Quản lý Khu Công nghiệp: Quản lý phân lô đất xưởng theo ngành nghề, doanh nghiệp thuê đất dài hạn và các hợp đồng pháp lý.",
         ["KHU_CN: MAKCN, TENKCN, TINH_TP", "PHANKHU: MAPK, TENPK, QUYHOACH_NGANH", "LODAT: MALO, DIENTICH_M2, VITRI, GIATHUE_M2_NAM", "DOANHNGHIEP: MADN, TENDN, MASOTHUE, QUOCTICH", "HOPDONG_THUE: MAHD, NGAYKY, THOIHAN_NAM, TIENCOC"],
         ["KHU_CN - PHANKHU: 1:N", "PHANKHU - LODAT: 1:N", "LODAT - HOPDONG_THUE: 1:N", "DOANHNGHIEP - HOPDONG_THUE: 1:N"]),

        ("ERD-P22", "Quản Lý Hãng Xe Công Nghệ & Chuyến Xe",
         "DOI_XE(MADOI, TENDOI, THANHPHO), TAIXE(MATX, HOTEN, CCCD, SDT, BIENSO, LOAIXE, MADOI), KHACHHANG(MAKH, HOTEN, SDT, DIEM_TICHLUY), CHUYENXE(MACHUYEN, MATX, MAKH, DIEMDON, DIEMDEN, QUANGDUONG_KM, GIA_CUOC, THOIGIAN_BD, THOIGIAN_KT, TRANGTHAI), DANHGIA(MADG, MACHUYEN, DIEM_SAO, NHANXET)",
         "Thiết kế ERD cho Ứng dụng đặt xe công nghệ (Ride-hailing): Quản lý tài xế theo đội xe, khách hàng đặt các chuyến đi từ điểm đón đến điểm đến và đánh giá sao.",
         ["DOI_XE: MADOI, TENDOI, THANHPHO", "TAIXE: MATX, HOTEN, CCCD, SDT, BIENSO, LOAIXE", "KHACHHANG: MAKH, HOTEN, SDT, DIEM_TICHLUY", "CHUYENXE: MACHUYEN, DIEMDON, DIEMDEN, QUANGDUONG_KM, GIA_CUOC", "DANHGIA: MADG, DIEM_SAO, NHANXET"],
         ["DOI_XE - TAIXE: 1:N", "TAIXE - CHUYENXE: 1:N", "KHACHHANG - CHUYENXE: 1:N", "CHUYENXE - DANHGIA: 1:1"]),

        ("ERD-P23", "Quản Lý Nhà Máy Xử Lý & Tái Chế Rác Thải",
         "NHAMAY(MANM, TENNM, DIACHI, CONGSUAT_TAN_NGAY), KHUVUC_GOM(MAKV, TENKV, QUAN_HUYEN), XE_THUGOM(MAXE, BIENSO, TRONGLUONG_MAX, MANM), CONGNHAN(MACN, HOTEN, SDT, MANM), CHUYEN_GOM(MACHUYEN, MAXE, MAKV, MACN_LAIXE, NGAYGOM, KHOILUONG_KG), DOTHANH_XULY(MADOT, MANM, NGAYXULY, KHOILUONG_TAICHE_KG, KHOILUONG_CHONLAP_KG)",
         "Thiết kế ERD quản lý thu gom và tái chế rác thải đô thị: Xe chuyên dụng gom rác từ các khu vực chuyển về nhà máy xử lý phân loại tái chế hoặc chôn lấp.",
         ["NHAMAY: MANM, TENNM, DIACHI, CONGSUAT_TAN_NGAY", "KHUVUC_GOM: MAKV, TENKV, QUAN_HUYEN", "XE_THUGOM: MAXE, BIENSO, TRONGLUONG_MAX", "CONGNHAN: MACN, HOTEN, SDT", "CHUYEN_GOM: MACHUYEN, NGAYGOM, KHOILUONG_KG"],
         ["NHAMAY - XE_THUGOM: 1:N", "NHAMAY - CONGNHAN: 1:N", "XE_THUGOM - CHUYEN_GOM: 1:N", "KHUVUC_GOM - CHUYEN_GOM: 1:N", "CONGNHAN - CHUYEN_GOM: 1:N", "NHAMAY - DOTHANH_XULY: 1:N"]),

        ("ERD-P24", "Quản Lý Bản Quyền Âm Nhạc Trực Tuyến",
         "TRUNGTAM_BQ(MATT, TENTT, QUOCGIA), NHACSI(MANS, HOTEN, BUTDANH, QUOCTICH), CASI(MACS, NGHEDANH, SDT, EMAIL), BAIHAT(MABH, TENBH, MANS, THELOAI, NAMST, MATT), HOPDONG_BIEUDIEN(MAHD, MABH, MACS, NGAYKY, PHIBANQUYEN_USD, THOIHAN_NAM), BAN_THUAM(MABT, MABH, MACS, NGAYPHATHANH, NEN_TANG, LUOT_STREAM)",
         "Thiết kế ERD quản lý sở hữu trí tuệ âm nhạc: Nhạc sĩ đăng ký bản quyền bài hát, cấp phép cho ca sĩ biểu diễn hoặc phát hành bản thu âm trên các nền tảng số.",
         ["TRUNGTAM_BQ: MATT, TENTT, QUOCGIA", "NHACSI: MANS, HOTEN, BUTDANH", "CASI: MACS, NGHEDANH, SDT", "BAIHAT: MABH, TENBH, THELOAI, NAMST", "HOPDONG_BIEUDIEN: MAHD, PHIBANQUYEN_USD, THOIHAN_NAM", "BAN_THUAM: MABT, NEN_TANG, LUOT_STREAM"],
         ["TRUNGTAM_BQ - BAIHAT: 1:N", "NHACSI - BAIHAT: 1:N", "BAIHAT - CASI: M:N qua HOPDONG_BIEUDIEN và BAN_THUAM"]),

        ("ERD-P25", "Quản Lý Trạm Khí Tượng Thủy Văn & Dự Báo",
         "COQUAN_KT(MACQ, TENCQ, CAP_QUANLY), TRAM_DO(MATRAM, TENTRAM, TOADO_GPS, DIABAN, MACQ), THIETBI(MATB, MATRAM, LOAITB, NAMSX, TRANGTHAI), CHUYENGIA(MACG, HOTEN, CHUYENNGANH, MACQ), PHIEN_DODAC(MAPHIEN, MATRAM, THOIDIEM, NHIETDO_C, AP_SUAT_HPA, LUONGMUA_MM, TOCDOGIO_KMH), BAN_TIN_DB(MABANTIN, MACG, THOIDIEM_PHAT, PHAMVI_DUBAO, CAP_CANHBAO, NOIDUNG)",
         "Thiết kế ERD cho Mạng lưới trạm quan trắc khí tượng thủy văn: Thu thập dữ liệu nhiệt độ, áp suất, lượng mưa tự động và chuyên gia lập bản tin cảnh báo thiên tai.",
         ["COQUAN_KT: MACQ, TENCQ, CAP_QUANLY", "TRAM_DO: MATRAM, TENTRAM, TOADO_GPS, DIABAN", "THIETBI: MATB, LOAITB, NAMSX", "CHUYENGIA: MACG, HOTEN, CHUYENNGANH", "PHIEN_DODAC: MAPHIEN, THOIDIEM, NHIETDO_C, LUONGMUA_MM", "BAN_TIN_DB: MABANTIN, THOIDIEM_PHAT, CAP_CANHBAO"],
         ["COQUAN_KT - TRAM_DO: 1:N", "COQUAN_KT - CHUYENGIA: 1:N", "TRAM_DO - THIETBI: 1:N", "TRAM_DO - PHIEN_DODAC: 1:N", "CHUYENGIA - BAN_TIN_DB: 1:N"])
    ]

    problems = []
    for pid, title, schema, prompt, entities, rels in domains:
        prob = {
            "id": pid,
            "topic": "ERD_MAPPING",
            "difficulty": "B",
            "title": f"Thiết kế ERD & Ánh xạ Schema: {title}",
            "prompt": prompt,
            "schema": schema,
            "recommended_time_mins": 25,
            "points": 2.5,
            "status": "VERIFIED",
            "verification_level": "SEMANTICALLY_REVIEWED",
            "solution": {
                "erd_entities": entities,
                "relationships": rels,
                "relational_schema": [s.strip() for s in schema.split("), ")],
                "intermediate_steps": [
                    "Bước 1: Xác định đầy đủ các thực thể độc lập, thực thể yếu, thuộc tính đơn, thuộc tính khóa chính (PK).",
                    "Bước 2: Phân tích các mối kết hợp thực tế giữa các thực thể, xác định bản số min-max (0..1, 1..1, 0..n, 1..n).",
                    "Bước 3: Ánh xạ quan hệ 1:N bằng cách đưa khóa chính của phía 1 sang làm khóa ngoại (FK) của phía N.",
                    "Bước 4: Ánh xạ quan hệ M:N thành bảng liên kết trung gian, có khóa chính là khóa phức hợp gồm 2 khóa ngoại."
                ],
                "edge_cases": "Lưu ý không đặt trùng tên khóa ngoại; kiểm tra các thuộc tính đa trị nếu có phải tách thành bảng riêng; khóa chính bảng trung gian bắt buộc NOT NULL."
            },
            "rubric": {
                "total_points": 2.5,
                "entities_and_keys": 0.5,
                "relationships_and_cardinalities": 1.0,
                "relational_mapping_and_foreign_keys": 1.0
            }
        }
        problems.append(prob)
    return problems

print("ERD Generator ready. Count:", len(get_erd_problems()))
