# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 04 (MOCK-04)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)

Đọc kỹ bài toán quản lý chuỗi cửa hàng bán lẻ xăng dầu trực thuộc một công ty phân phối nhiên liệu:

Hệ thống cần quản lý mạng lưới các cửa hàng xăng dầu trên địa bàn. Mỗi cửa hàng có một mã cửa hàng duy nhất để phân biệt, tên cửa hàng, địa chỉ, quận/huyện và số trụ bơm đang hoạt động. Mỗi cửa hàng có nhiều nhân viên công tác, mỗi nhân viên có mã nhân viên, họ tên, ngày sinh, chức vụ (như Cửa hàng trưởng, Nhân viên bán hàng, Kế toán) và mức lương cơ bản; mỗi nhân viên bắt buộc chỉ thuộc quyền quản lý của đúng một cửa hàng.

Công ty cung cấp nhiều mặt hàng xăng dầu (nhiên liệu). Mỗi loại nhiên liệu có mã nhiên liệu, tên loại nhiên liệu, phân loại nhiên liệu (như Xăng khoáng, Xăng sinh học, Dầu DO), đơn vị tính và đơn giá niêm yết hiện hành. Tại mỗi cửa hàng có lắp đặt các bể chứa nhiên liệu ngầm. Mỗi bể chứa có mã bể chứa, thuộc về đúng một cửa hàng, dùng để chứa duy nhất một loại nhiên liệu nhất định, có dung tích tối đa (tính theo lít) và lượng nhiên liệu tồn hiện tại. Một cửa hàng có thể có nhiều bể chứa, và một loại nhiên liệu có thể được chứa ở nhiều bể chứa thuộc các cửa hàng khác nhau.

Mỗi khi khách hàng mua nhiên liệu, nhân viên ca trực lập một hóa đơn bán hàng. Hóa đơn có mã hóa đơn, ngày giờ lập hóa đơn, hình thức thanh toán (Tiền mặt, Chuyển khoản, Thẻ POS), do đúng một nhân viên lập tại cửa hàng mà nhân viên đó đang làm việc. Một hóa đơn có thể mua nhiều loại nhiên liệu khác nhau. Mỗi chi tiết mua ghi nhận số lượng lít bơm bán, đơn giá thực tế tại thời điểm giao dịch và thành tiền.

**Yêu cầu:**
1. (1.50 điểm) Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía giữa các tập thực thể. Vẽ mô hình Thực thể – Mối kết hợp (ERD).
2. (1.00 điểm) Ánh xạ mô hình ERD đã thiết kế sang Lược đồ cơ sở dữ liệu quan hệ hoàn chỉnh. Chỉ rõ Khóa chính (PK) gạch dưới và Khóa ngoại (FK) chỉ rõ bảng tham chiếu.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu quan hệ 'Quản Lý Chuỗi Cửa Hàng Bán Lẻ Xăng Dầu' được chuyển giao từ Câu 1:
- `CUAHANG` (**<u>MACH</u>**, TENCH, DIACHI, QUAN, SO_TRU_BOM)
- `NHANVIEN` (**<u>MANV</u>**, HOTEN, NGAYSINH, CHUCVU, LUONG, MACH)
- `NHIENLIEU` (**<u>MANL</u>**, TENNL, LOAINL, DONVITINH, DONGIA)
- `BE_CHUA` (**<u>MABE</u>**, MACH, MANL, DUNGTICH, LUONG_TON)
- `HOADON` (**<u>MAHD</u>**, NGAYHD, MACH, MANV, HINHTHUC_TT)
- `CTHD` (**<u>MAHD</u>**, **<u>MANL</u>**, SOLUONG, DONGIA_BAN, THANHTIEN)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết câu lệnh SQL tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra thuộc tính dung tích bể (`DUNGTICH`) trong bảng `BE_CHUA` phải lớn hơn 0 (> 0), và lượng nhiên liệu tồn (`LUONG_TON`) phải lớn hơn hoặc bằng 0 đồng thời không vượt quá dung tích của bể ($0 \le \text{LUONG\_TON} \le \text{DUNGTICH}$). Cả hai thuộc tính đều không được mang giá trị `NULL`.

b. (0.75 điểm) Viết câu lệnh SQL cập nhật tăng đơn giá niêm yết (`DONGIA`) thêm 5% cho tất cả các mặt hàng nhiên liệu thuộc phân loại (`LOAINL`) là 'Xăng khoáng' có đơn vị tính (`DONVITINH`) là 'Lít'.

### 2.2. Viết các biểu thức Đại số quan hệ (6.0 điểm)
Sinh viên sử dụng các ký hiệu phép toán chuẩn của Đại số quan hệ: $\sigma$ (chọn), $\pi$ (chiếu), $\bowtie$ (kết tự nhiên), $\bowtie_{\theta}$ (kết có điều kiện), $\leftouterjoin$ (kết ngoài trái), $\rho$ (đổi tên), $\gamma$ (gom nhóm & hàm gộp), $\div$ (chia). Mỗi câu cần nêu rõ các bước trung gian $E_1, E_2, \dots$ và biểu thức kết quả $\text{KQ}$.

a. (1.0 điểm) Liệt kê danh sách các nhân viên (**MANV**, **HOTEN**, **NGAYSINH**, **LUONG**) có chức vụ là 'Nhân viên bán hàng' và có mức lương cơ bản từ 8,000,000 đồng trở lên.

b. (1.0 điểm) Cho biết danh sách các hóa đơn (**MAHD**, **NGAYHD**, **HINHTHUC_TT**, **TENCH**) được phát hành tại các cửa hàng xăng dầu thuộc quận 'Bình Thạnh' với hình thức thanh toán là 'Chuyển khoản'.

c. (1.0 điểm) Liệt kê danh sách thông tin tất cả các cửa hàng xăng dầu (**MACH**, **TENCH**, **QUAN**) và mã các bể chứa (**MABE**), dung tích bể (**DUNGTICH**) trực thuộc cửa hàng đó (nếu cửa hàng chưa lắp đặt bể chứa nào thì thông tin bể chứa mang giá trị `NULL`).

d. (1.0 điểm) Tính tổng số lít nhiên liệu đã bán (**TONG_LIT_BAN**) của từng cửa hàng xăng dầu trong tháng 10 năm 2024. Thông tin hiển thị gồm: **MACH**, **TENCH**, **TONG_LIT_BAN**.

e. (1.0 điểm) Tìm các hóa đơn (**MAHD**, **NGAYHD**, **MACH**) đã bán **tất cả** các loại nhiên liệu thuộc phân loại 'Xăng khoáng'.

f. (1.0 điểm) Tìm cửa hàng xăng dầu (**MACH**, **TENCH**, **QUAN**) có tổng dung tích các bể chứa (**TONG_DUNGTICH**) lớn nhất trong hệ thống (bảo toàn tất cả các cửa hàng nếu có nhiều cửa hàng cùng đạt tổng dung tích lớn nhất).

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 04**
*Cán bộ coi thi không giải thích gì thêm.*
