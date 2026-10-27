# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 10 (MOCK-10)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)

Đọc kỹ bài toán quản lý quy trình tiếp nhận và bảo dưỡng sửa chữa ô tô tại gara:

Gara sửa chữa và bảo dưỡng ô tô cần xây dựng cơ sở dữ liệu để quản lý thông tin khách hàng, phương tiện ô tô, đội ngũ thợ kỹ thuật, kho phụ tùng thay thế và các phiếu bảo dưỡng. Mỗi khách hàng đến gara có một mã khách hàng duy nhất, họ tên, số điện thoại liên lạc và địa chỉ thường trú. Khách hàng có thể sở hữu một hoặc nhiều xe ô tô; mỗi xe ô tô được định danh bằng biển số xe duy nhất, hãng xe (như 'Toyota', 'Honda', 'Ford', 'Hyundai'), model dòng xe, năm sản xuất và bắt buộc thuộc quyền sở hữu của đúng một khách hàng.

Đội ngũ kỹ thuật viên của gara gồm nhiều thợ chuyên trách; mỗi thợ kỹ thuật có mã thợ duy nhất, họ tên, chuyên môn chính ('Máy gầm', 'Điện lạnh', 'Sơn gò', 'Bảo dưỡng nhanh') và mức lương cơ bản hàng tháng. Kho phụ tùng của gara lưu trữ nhiều linh kiện, vật tư kỹ thuật; mỗi phụ tùng có mã phụ tùng duy nhất, tên phụ tùng, phân loại phụ tùng (như 'Dầu nhớt', 'Hệ thống phanh', 'Lọc gió', 'Lốp xe'), đơn giá niêm yết và số lượng hiện còn tồn kho.

Mỗi khi xe được đưa vào gara làm dịch vụ, nhân viên lập một phiếu bảo dưỡng. Phiếu bảo dưỡng có mã phiếu duy nhất, ngày lập phiếu, do đúng một thợ kỹ thuật phụ trách chính cho đúng một xe ô tô, tổng chi phí dự toán ban đầu và trạng thái phiếu bảo dưỡng ('Đang xử lý', 'Đã hoàn thành', 'Đã hủy'). Trong một lần bảo dưỡng, xe có thể cần thay thế hoặc sử dụng một hoặc nhiều loại phụ tùng khác nhau. Mỗi chi tiết bảo dưỡng ghi nhận mã phiếu bảo dưỡng, mã phụ tùng, số lượng phụ tùng thay thế và tiền công kỹ thuật tương ứng.

**Yêu cầu:**
1. (1.50 điểm) Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía giữa các tập thực thể. Vẽ mô hình Thực thể – Mối kết hợp (ERD).
2. (1.00 điểm) Ánh xạ mô hình ERD đã thiết kế sang Lược đồ cơ sở dữ liệu quan hệ hoàn chỉnh. Chỉ rõ Khóa chính (PK) gạch dưới và Khóa ngoại (FK) chỉ rõ bảng tham chiếu.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu quan hệ 'Quản Lý Gara Ô Tô & Lịch Trình Bảo Dưỡng Phụ Tùng' được chuyển giao từ Câu 1:
- `KHACHHANG` (**<u>MAKH</u>**, HOTEN, DIENTHOAI, DIACHI)
- `XE` (**<u>BIENSO</u>**, HANGXE, MODEL, NAMSX, MAKH)
- `THO` (**<u>MATHO</u>**, HOTEN, CHUYENMON, LUONG_CB)
- `PHUTUNG` (**<u>MAPT</u>**, TENPT, LOAIPT, DONGIA, SOLUONGTON)
- `PHIEU_BD` (**<u>MAPHIEU</u>**, NGAYLAP, BIENSO, MATHO, TONGTIEN, TRANGTHAI)
- `CHITIET_BD` (**<u>MAPHIEU</u>**, **<u>MAPT</u>**, SOLUONG, TIENCONG)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết câu lệnh SQL tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra số lượng tồn kho (`SOLUONGTON`) trong bảng `PHUTUNG` phải lớn hơn hoặc bằng 0 ($\ge 0$), và đơn giá niêm yết (`DONGIA`) trong bảng `PHUTUNG` phải lớn hơn 0 (> 0). Cả hai thuộc tính đều không được mang giá trị `NULL`.

b. (0.75 điểm) Viết câu lệnh SQL cập nhật tăng 10% mức lương cơ bản (`LUONG_CB = LUONG_CB * 1.10`) cho các thợ kỹ thuật có chuyên môn (`CHUYENMON`) là 'Máy gầm' đã từng phụ trách ít nhất một phiếu bảo dưỡng (`PHIEU_BD`) lập trong tháng 11 năm 2024.

### 2.2. Viết các biểu thức Đại số quan hệ (6.0 điểm)
Sinh viên sử dụng các ký hiệu phép toán chuẩn của Đại số quan hệ: $\sigma$ (chọn), $\pi$ (chiếu), $\bowtie$ (kết tự nhiên), $\bowtie_{\theta}$ (kết có điều kiện), $\leftouterjoin$ (kết ngoài trái), $\rho$ (đổi tên), $\gamma$ (gom nhóm & hàm gộp), $\div$ (chia). Mỗi câu cần nêu rõ các bước trung gian $E_1, E_2, \dots$ và biểu thức kết quả $\text{KQ}$.

a. (1.0 điểm) Liệt kê danh sách các xe ô tô (**BIENSO**, **HANGXE**, **MODEL**, **NAMSX**) thuộc hãng xe 'Toyota' có năm sản xuất từ năm 2022 trở lại đây ($\ge 2022$).

b. (1.0 điểm) Cho biết danh sách các phiếu bảo dưỡng (**MAPHIEU**, **NGAYLAP**, **BIENSO**, **HOTEN**) do thợ kỹ thuật có họ tên `HOTEN = 'Trần Văn Mạnh'` trực tiếp phụ trách.

c. (1.0 điểm) Liệt kê thông tin tất cả các khách hàng (**MAKH**, **HOTEN**) cùng danh sách biển số xe (**BIENSO**), hãng xe (**HANGXE**) thuộc quyền sở hữu của khách hàng đó (nếu khách hàng mới đăng ký chưa khai báo xe ô tô nào thì thông tin xe mang giá trị `NULL`).

d. (1.0 điểm) Tính tổng chi phí phụ tùng thay thế (**TONG_TIEN_PHU_TUNG** = SUM(SOLUONG * DONGIA)) của từng phiếu bảo dưỡng (**MAPHIEU**, **NGAYLAP**) lập trong tháng 11 năm 2024 có trạng thái là 'Đã hoàn thành'.

e. (1.0 điểm) Tìm các xe ô tô (**BIENSO**, **HANGXE**, **MAKH**) đã từng sử dụng/thay thế **tất cả** các loại phụ tùng thuộc phân loại `LOAIPT = 'Dầu nhớt'` của gara.

f. (1.0 điểm) Tìm phụ tùng (**MAPT**, **TENPT**, **LOAIPT**) có tổng số lượng sử dụng thay thế (**TONG_SOLUONG**) nhiều nhất trong toàn bộ các phiếu bảo dưỡng năm 2024 (bảo toàn tất cả phụ tùng nếu có nhiều phụ tùng cùng đạt số lượng cao nhất).

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 10**
*Cán bộ coi thi không giải thích gì thêm.*
