# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 05 (MOCK-05)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.0 ĐIỂM)

Đọc kỹ bài toán quản lý căn hộ chung cư và hợp đồng cho thuê nhà:

Một ban quản lý bất động sản cần xây dựng cơ sở dữ liệu quản lý các tòa nhà chung cư cao tầng và hoạt động cho thuê căn hộ. Hệ thống quản lý các tòa nhà (Block chung cư), mỗi tòa nhà có mã tòa nhà duy nhất, tên tòa nhà, địa chỉ và số tầng. Trong mỗi tòa nhà có nhiều căn hộ; mỗi căn hộ có mã căn hộ, thuộc về đúng một tòa nhà, có số phòng ngủ, diện tích (m2), đơn giá thuê chuẩn hàng tháng và trạng thái hiện tại (Trống, Đang thuê, Bảo trì).

Khách hàng thuê căn hộ có thể là cá nhân hoặc tổ chức. Mỗi khách hàng có mã khách hàng, họ tên khách thuê, số CCCD/mã số thuế, số điện thoại và phân loại khách hàng (Cá nhân, Doanh nghiệp, Gia đình). Mỗi nhân viên môi giới có mã nhân viên, họ tên, phòng ban phụ trách và số điện thoại liên hệ.

Mỗi khi khách hàng thỏa thuận thuê một căn hộ, nhân viên phụ trách sẽ lập một hợp đồng thuê nhà. Hợp đồng có mã hợp đồng, ghi nhận ngày ký kết, ngày bắt đầu hiệu lực thuê, ngày kết thúc hiệu lực thuê, giá thuê thực tế thỏa thuận và số tiền đặt cọc. Mỗi hợp đồng do đúng một khách hàng ký, thuê đúng một căn hộ nhất định và do đúng một nhân viên môi giới lập. Hàng tháng, ban quản lý phát hành các phiếu thu tiền thuê nhà theo từng hợp đồng; mỗi phiếu thu có số phiếu thu duy nhất, thuộc về đúng một hợp đồng, ghi nhận tháng, năm thu, ngày thu tiền thực tế và số tiền thu.

**Yêu cầu:**
1. (1.20 điểm) Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía giữa các tập thực thể. Vẽ mô hình Thực thể – Mối kết hợp (ERD).
2. (0.80 điểm) Ánh xạ mô hình ERD đã thiết kế sang Lược đồ cơ sở dữ liệu quan hệ hoàn chỉnh. Chỉ rõ Khóa chính (PK) gạch dưới và Khóa ngoại (FK) chỉ rõ bảng tham chiếu.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (8.0 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu quan hệ 'Quản Lý Căn Hộ Chung Cư & Hợp Đồng Thuê Nhà' gồm các quan hệ:
- `TOANHA` (**<u>MATN</u>**, TENTN, DIACHI, SOTANG)
- `CANHO` (**<u>MACH</u>**, MATN, SOPHONG, DIENTICH, GIATHUE_CHUAN, TRANGTHAI)
- `KHACHHANG` (**<u>MAKH</u>**, HOTEN, CCCD, SDT, LOAIKH)
- `NHANVIEN` (**<u>MANV</u>**, HOTEN, PHONGBAN, SDT)
- `HOPDONG` (**<u>MAHD</u>**, MACH, MAKH, MANV, NGAYKY, NGAYBD, NGAYKT, GIATHUE_THUCTE, TIENCOC)
- `PHIEUTHU` (**<u>SOPHIEU</u>**, MAHD, THANG, NAM, NGAYTHU, SOTIEN)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết câu lệnh SQL tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra tiền đặt cọc (`TIENCOC`) trong quan hệ `HOPDONG` phải lớn hơn hoặc bằng 0 ($\ge 0$), và ngày kết thúc hợp đồng thuê (`NGAYKT`) phải sau ngày bắt đầu hiệu lực thuê (`NGAYKT > NGAYBD`). Cả hai thuộc tính đều không được mang giá trị `NULL`.

b. (0.75 điểm) Viết câu lệnh SQL cập nhật trạng thái (`TRANGTHAI`) thành 'Đang thuê' cho tất cả các căn hộ có trong các hợp đồng thuê (`HOPDONG`) được ký trong năm 2024 mà ngày kết thúc hợp đồng (`NGAYKT`) từ ngày '2024-12-31' trở về sau.

### 2.2. Viết các biểu thức Đại số quan hệ (6.5 điểm)
Sinh viên sử dụng các ký hiệu phép toán chuẩn của Đại số quan hệ: $\sigma$ (chọn), $\pi$ (chiếu), $\bowtie$ (kết tự nhiên), $\bowtie_{\theta}$ (kết có điều kiện), $\leftouterjoin$ (kết ngoài trái), $\rho$ (đổi tên), $\gamma$ (gom nhóm & hàm gộp), $\div$ (chia). Mỗi câu cần nêu rõ các bước trung gian $E_1, E_2, \dots$ và biểu thức kết quả $\text{KQ}$.

a. (1.0 điểm) Liệt kê danh sách các khách hàng (**MAKH**, **HOTEN**, **SDT**) thuộc phân loại khách hàng là 'Doanh nghiệp'.

b. (1.0 điểm) Cho biết danh sách các căn hộ (**MACH**, **SOPHONG**, **DIENTICH**, **TENTN**) thuộc tòa nhà 'Sky Garden' có giá thuê chuẩn (**GIATHUE_CHUAN**) từ 15,000,000 đồng/tháng trở lên.

c. (1.0 điểm) Liệt kê danh sách thông tin tất cả các tòa nhà chung cư (**MATN**, **TENTN**, **DIACHI**) và mã các căn hộ (**MACH**), số phòng ngủ (**SOPHONG**) thuộc tòa nhà đó (nếu tòa nhà chưa có căn hộ nào thì thông tin căn hộ mang giá trị `NULL`).

d. (1.0 điểm) Tính tổng số tiền thu được (**TONG_TIEN_THU**) theo từng hợp đồng trong năm 2024. Thông tin hiển thị gồm: **MAHD**, **NGAYKY**, **TONG_TIEN_THU**.

e. (1.0 điểm) Tìm các khách hàng (**MAKH**, **HOTEN**, **SDT**) đã từng ký hợp đồng thuê căn hộ tại **tất cả** các tòa nhà tọa lạc tại địa bàn 'Quận 7'.

f. (1.5 điểm) Tìm thông tin tòa nhà (**MATN**, **TENTN**, **DIACHI**) có số lượng căn hộ đang ở trạng thái 'Đang thuê' nhiều nhất trong hệ thống (bảo toàn tất cả các tòa nhà nếu có nhiều tòa nhà cùng đạt số lượng căn hộ đang thuê lớn nhất).

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 05**
*Cán bộ coi thi không giải thích gì thêm.*
