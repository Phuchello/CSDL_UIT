# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 08 (MOCK-08)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)

Đọc kỹ bài toán quản lý hoạt động kinh doanh trực tuyến và phân phối hàng hóa trên sàn thương mại điện tử:

Sàn thương mại điện tử cần xây dựng cơ sở dữ liệu quản lý các gian hàng bán lẻ, danh mục sản phẩm, khách hàng, đơn đặt hàng và giao vận. Sàn có nhiều gian hàng đăng ký hoạt động; mỗi gian hàng có một mã gian hàng duy nhất, tên gian hàng, họ tên người đại diện và thành phố đặt kho hàng chính. Mỗi gian hàng kinh doanh nhiều sản phẩm; mỗi sản phẩm có mã sản phẩm duy nhất, tên sản phẩm, phân loại sản phẩm (như 'Gia dụng', 'Điện tử', 'Thời trang', 'Mỹ phẩm'), giá niêm yết hiện tại và bắt buộc trực thuộc một gian hàng cung ứng duy nhất.

Hệ thống lưu trữ hồ sơ người tiêu dùng tham gia mua sắm. Mỗi khách hàng có mã khách hàng duy nhất, họ tên, địa chỉ nhận hàng (tỉnh/thành phố) và hạng thành viên ('Standard', 'Silver', 'Gold', 'Diamond').

Khi khách hàng mua sắm trên sàn, hệ thống tạo một đơn đặt hàng. Mỗi đơn hàng có mã đơn hàng duy nhất, ngày giờ đặt hàng, do đúng một khách hàng khởi tạo, có hình thức thanh toán ('COD', 'Ví điện tử', 'Thẻ tín dụng') và trạng thái xử lý ('Chờ giao', 'Đã giao', 'Đã hủy'). Trong một đơn hàng, khách hàng có thể đặt mua một hoặc nhiều sản phẩm khác nhau. Mỗi chi tiết đơn hàng lưu trữ mã đơn hàng, mã sản phẩm, số lượng đặt mua và đơn giá bán thực tế tại thời điểm giao dịch thành công. Mỗi đơn hàng sau khi hoàn tất đóng gói sẽ được điều phối cho một đơn vị vận chuyển phụ trách. Mỗi thông tin vận chuyển có mã vận đơn duy nhất, đơn vị vận chuyển ('Giao Hàng Nhanh', 'Viettel Post', 'Shopee Xpress'), cước phí vận chuyển và ngày giao hàng thực tế.

**Yêu cầu:**
1. (1.50 điểm) Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía giữa các tập thực thể. Vẽ mô hình Thực thể – Mối kết hợp (ERD).
2. (1.00 điểm) Ánh xạ mô hình ERD đã thiết kế sang Lược đồ cơ sở dữ liệu quan hệ hoàn chỉnh. Chỉ rõ Khóa chính (PK) gạch dưới và Khóa ngoại (FK) chỉ rõ bảng tham chiếu.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu quan hệ 'Quản Lý Sàn Thương Mại Điện Tử & Vận Chuyển Hàng' được chuyển giao từ Câu 1:
- `GIANHANG` (**<u>MAGH</u>**, TENGH, NGUOIDAIDIEN, THANHPHO)
- `SANPHAM` (**<u>MASP</u>**, TENSP, LOAISP, GIANIEMYET, MAGH)
- `KHACHHANG` (**<u>MAKH</u>**, HOTEN, DIACHI, HANGTHANHVIEN)
- `DONHANG` (**<u>MADH</u>**, NGAYDAT, MAKH, HINHTHUCTT, TRANGTHAI)
- `CHITIET_DH` (**<u>MADH</u>**, **<u>MASP</u>**, SOLUONG, DONGIA_BAN)
- `VANCHUYEN` (**<u>MAVD</u>**, MADH, DONVIVC, CUOCPHI, NGAYGIAO)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết câu lệnh SQL tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra số lượng mua (`SOLUONG`) trong bảng `CHITIET_DH` phải lớn hơn 0 (> 0), và giá niêm yết (`GIANIEMYET`) trong bảng `SANPHAM` phải lớn hơn 0 (> 0). Cả hai thuộc tính đều không được mang giá trị `NULL`.

b. (0.75 điểm) Viết câu lệnh SQL cập nhật giảm 10% giá niêm yết (`GIANIEMYET = GIANIEMYET * 0.90`) cho các sản phẩm thuộc phân loại (`LOAISP`) là 'Gia dụng' do gian hàng có người đại diện (`NGUOIDAIDIEN`) tên là 'Lê Hoàng Nam' cung cấp.

### 2.2. Viết các biểu thức Đại số quan hệ (6.0 điểm)
Sinh viên sử dụng các ký hiệu phép toán chuẩn của Đại số quan hệ: $\sigma$ (chọn), $\pi$ (chiếu), $\bowtie$ (kết tự nhiên), $\bowtie_{\theta}$ (kết có điều kiện), $\leftouterjoin$ (kết ngoài trái), $\rho$ (đổi tên), $\gamma$ (gom nhóm & hàm gộp), $\div$ (chia). Mỗi câu cần nêu rõ các bước trung gian $E_1, E_2, \dots$ và biểu thức kết quả $\text{KQ}$.

a. (1.0 điểm) Liệt kê danh sách các sản phẩm (**MASP**, **TENSP**, **GIANIEMYET**) thuộc phân loại sản phẩm 'Điện tử' có giá niêm yết từ 10.000.000 VNĐ trở lên ($\ge 10.000.000$).

b. (1.0 điểm) Cho biết danh sách các đơn hàng (**MADH**, **NGAYDAT**, **HINHTHUCTT**, **HOTEN**) của các khách hàng có địa chỉ thường trú tại 'Hà Nội' và lựa chọn phương thức thanh toán là 'Ví điện tử'.

c. (1.0 điểm) Liệt kê thông tin tất cả các gian hàng (**MAGH**, **TENGH**) cùng danh mục mã sản phẩm (**MASP**), tên sản phẩm (**TENSP**) do gian hàng đó cung cấp (nếu gian hàng mới mở chưa đăng bán sản phẩm nào thì thông tin sản phẩm mang giá trị `NULL`).

d. (1.0 điểm) Tính tổng giá trị tiền hàng (**TONG_TIEN_HANG** = SUM(SOLUONG * DONGIA_BAN)) của từng đơn hàng (**MADH**, **NGAYDAT**) được đặt trong tháng 11 năm 2024 có trạng thái đơn hàng là 'Đã giao'.

e. (1.0 điểm) Tìm các đơn hàng (**MADH**, **NGAYDAT**, **MAKH**) đã đặt mua **tất cả** các sản phẩm thuộc phân loại 'Gia dụng' do gian hàng có tên là 'Gia Dụng Thông Minh' cung ứng.

f. (1.0 điểm) Tìm khách hàng (**MAKH**, **HOTEN**, **HANGTHANHVIEN**) có tổng số lượng sản phẩm đã mua (**TONG_SOLUONG**) nhiều nhất trong tháng 11 năm 2024 (bảo toàn tất cả các khách hàng nếu có nhiều khách hàng cùng đạt số lượng mua cao nhất).

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 08**
*Cán bộ coi thi không giải thích gì thêm.*
