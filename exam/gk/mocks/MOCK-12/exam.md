# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 12 (MOCK-12)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)

Đọc kỹ bài toán quản lý chuỗi cụm rạp chiếu phim và hệ thống bán vé xem phim trực tuyến:

Chuỗi rạp chiếu phim đa quốc gia cần xây dựng một cơ sở dữ liệu quan hệ tập trung để vận hành hệ thống bán vé và quản lý lịch chiếu. Chuỗi sở hữu nhiều cụm rạp đặt tại các trung tâm thương mại lớn; mỗi cụm rạp có mã cụm rạp duy nhất, tên cụm rạp, địa chỉ và thành phố trực thuộc. Tại mỗi cụm rạp có nhiều phòng chiếu phục vụ khán giả; mỗi phòng chiếu có mã phòng chiếu duy nhất, tên phòng chiếu, số lượng ghế ngồi tối đa, phân loại phòng chiếu ('2D Standard', '3D IMAX', '4DX Gold') và bắt buộc trực thuộc duy nhất một cụm rạp.

Hệ thống quản lý danh mục các bộ phim được cấp phép phát hành; mỗi bộ phim có mã phim duy nhất, tên phim, thể loại chính ('Hành động', 'Khoa học viễn tưởng', 'Hoạt hình', 'Kinh dị', 'Tâm lý'), thời lượng chiếu (tính theo phút), tên đạo diễn và năm sản xuất. Để phục vụ khán giả, rạp tổ chức các suất chiếu phim theo lịch trình cụ thể; mỗi suất chiếu có mã suất chiếu duy nhất, chiếu đúng một bộ phim, diễn ra tại đúng một phòng chiếu vào một ngày chiếu và giờ chiếu xác định, cùng mức giá vé niêm yết chuẩn của suất chiếu đó.

Khách hàng đăng ký tài khoản thành viên trực tuyến trên ứng dụng của rạp; mỗi khách hàng có mã khách hàng duy nhất, họ tên, số điện thoại liên lạc, địa chỉ email và phân hạng thành viên ('Standard', 'VIP', 'Diamond'). Khách hàng có thể đặt mua vé xem phim cho các suất chiếu mong muốn; mỗi vé xem phim có mã vé duy nhất, thuộc về đúng một suất chiếu, do đúng một khách hàng đặt mua, có số thứ tự ghế ngồi, giá vé thực tế thanh toán (sau khi áp dụng ưu đãi thành viên) và trạng thái vé ('Đã thanh toán', 'Đã hủy', 'Đang giữ chỗ'). Mỗi vé chỉ tương ứng với một chỗ ngồi tại một suất chiếu xác định.

**Yêu cầu:**
1. (1.50 điểm) Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía giữa các tập thực thể. Vẽ mô hình Thực thể – Mối kết hợp (ERD).
2. (1.00 điểm) Ánh xạ mô hình ERD đã thiết kế sang Lược đồ cơ sở dữ liệu quan hệ hoàn chỉnh. Chỉ rõ Khóa chính (PK) gạch dưới và Khóa ngoại (FK) chỉ rõ bảng tham chiếu.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu quan hệ 'Quản Lý Cụm Rạp Chiếu Phim & Đặt Vé Trực Tuyến' được chuyển giao từ Câu 1:
- `CUMRAP` (**<u>MACR</u>**, TENCR, DIACHI, THANHPHO)
- `PHONGCHIEU` (**<u>MAPC</u>**, TENPHONG, SOGHETOI_DA, LOAIPHONG, MACR)
- `PHIM` (**<u>MAPHIM</u>**, TENPHIM, THELOAI, THOILUONG, DAODIEN, NAMSX)
- `SUATCHIEU` (**<u>MASC</u>**, MAPHIM, MAPC, NGAYCHIEU, GIOCHIEU, GIAVE_CHUAN)
- `KHACHHANG` (**<u>MAKH</u>**, HOTEN, SDT, EMAIL, LOAITHANHVIEN)
- `VEXEM` (**<u>MAVE</u>**, MASC, MAKH, SOGHE, GIAVE_THUC, TRANGTHAI)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết câu lệnh SQL tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra giá vé thực tế thanh toán (`GIAVE_THUC`) trong bảng `VEXEM` phải lớn hơn 0 (> 0) và trạng thái vé (`TRANGTHAI`) chỉ được nhận một trong ba giá trị hợp lệ: 'Đã thanh toán', 'Đã hủy', 'Đang giữ chỗ'. Cả hai thuộc tính đều không được mang giá trị `NULL`.

b. (0.75 điểm) Viết câu lệnh SQL cập nhật giảm giá 10% giá vé chuẩn (`GIAVE_CHUAN = GIAVE_CHUAN * 0.90`) cho các suất chiếu của các bộ phim thuộc thể loại (`THELOAI`) là 'Hoạt hình' có ngày chiếu (`NGAYCHIEU`) trong tháng 12 năm 2024.

### 2.2. Viết các biểu thức Đại số quan hệ (6.0 điểm)
Sinh viên sử dụng các ký hiệu phép toán chuẩn của Đại số quan hệ: $\sigma$ (chọn), $\pi$ (chiếu), $\bowtie$ (kết tự nhiên), $\bowtie_{\theta}$ (kết có điều kiện), $\leftouterjoin$ (kết ngoài trái), $\rho$ (đổi tên), $\gamma$ (gom nhóm & hàm gộp), $\div$ (chia). Mỗi câu cần nêu rõ các bước trung gian $E_1, E_2, \dots$ và biểu thức kết quả $\text{KQ}$.

a. (1.0 điểm) Liệt kê danh sách các bộ phim (**MAPHIM**, **TENPHIM**, **THOILUONG**, **DAODIEN**) thuộc thể loại 'Khoa học viễn tưởng' có thời lượng chiếu từ 120 phút trở lên ($\ge 120$).

b. (1.0 điểm) Cho biết danh sách các vé xem phim (**MAVE**, **SOGHE**, **GIAVE_THUC**, **TENCR**) của các suất chiếu được tổ chức tại cụm rạp mang tên `TENCR = 'CGV Landmark 81'`.

c. (1.0 điểm) Liệt kê thông tin tất cả các cụm rạp (**MACR**, **TENCR**) cùng mã phòng chiếu (**MAPC**), tên phòng chiếu (**TENPHONG**) trực thuộc cụm rạp đó (nếu cụm rạp mới mở chưa có phòng chiếu nào thì thông tin phòng chiếu mang giá trị `NULL`).

d. (1.0 điểm) Tính tổng doanh thu thực tế bán vé (**TONG_DOANHTHU** = SUM(GIAVE_THUC)) của từng suất chiếu (**MASC**, **NGAYCHIEU**) diễn ra trong tháng 11 năm 2024 có trạng thái vé là 'Đã thanh toán'.

e. (1.0 điểm) Tìm các khách hàng (**MAKH**, **HOTEN**, **SDT**) đã từng mua vé xem ('Đã thanh toán') **tất cả** các bộ phim thuộc thể loại 'Kinh dị' của cụm rạp.

f. (1.0 điểm) Tìm bộ phim (**MAPHIM**, **TENPHIM**, **THELOAI**) có tổng số lượng vé đã bán thành công ('Đã thanh toán') nhiều nhất trong toàn bộ năm 2024 (bảo toàn tất cả các bộ phim nếu có nhiều phim cùng đạt số vé cao nhất).

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 12**
*Cán bộ coi thi không giải thích gì thêm.*
