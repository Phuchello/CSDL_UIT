# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 06 (MOCK-06)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)

Đọc kỹ bài toán quản lý đặt khám & hồ sơ bệnh án điện tử tại một phòng khám đa khoa:

Phòng khám đa khoa cần xây dựng cơ sở dữ liệu quản lý các chuyên khoa, bác sĩ, bệnh nhân và các lượt khám chữa bệnh ngoại trú. Phòng khám có nhiều chuyên khoa (khoa khám); mỗi chuyên khoa có mã chuyên khoa duy nhất, tên chuyên khoa và tên bác sĩ trưởng khoa. Mỗi chuyên khoa có nhiều bác sĩ công tác; mỗi bác sĩ có mã bác sĩ, họ tên, học vị (như Thạc sĩ, Tiến sĩ, Bác sĩ CKI, Bác sĩ CKII), mức lương cơ bản và bắt buộc trực thuộc duy nhất một chuyên khoa.

Hệ thống quản lý thông tin bệnh nhân đến đăng ký khám bệnh. Mỗi bệnh nhân có mã bệnh nhân, họ tên, ngày sinh, giới tính và địa chỉ thường trú (tỉnh/thành phố). Danh mục dịch vụ y tế của phòng khám gồm nhiều dịch vụ khám và kỹ thuật cận lâm sàng; mỗi dịch vụ có mã dịch vụ, tên dịch vụ, phân loại dịch vụ (như Khám lâm sàng, Chẩn đoán hình ảnh, Xét nghiệm) và đơn giá niêm yết hiện hành.

Mỗi lần bệnh nhân đến phòng khám, nhân viên tiếp nhận tạo một phiếu khám bệnh. Phiếu khám có mã phiếu khám duy nhất, ngày giờ khám bệnh, kết luận chẩn đoán ban đầu của bác sĩ; mỗi phiếu khám do đúng một bác sĩ phụ trách khám cho đúng một bệnh nhân. Trong quá trình thăm khám, bác sĩ có thể chỉ định bệnh nhân thực hiện một hoặc nhiều dịch vụ cận lâm sàng. Mỗi chi tiết chỉ định dịch vụ ghi nhận mã phiếu khám, mã dịch vụ, số lượng chỉ định, đơn giá thực thu tại thời điểm chỉ định và kết quả thực hiện dịch vụ.

**Yêu cầu:**
1. (1.50 điểm) Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía giữa các tập thực thể. Vẽ mô hình Thực thể – Mối kết hợp (ERD).
2. (1.00 điểm) Ánh xạ mô hình ERD đã thiết kế sang Lược đồ cơ sở dữ liệu quan hệ hoàn chỉnh. Chỉ rõ Khóa chính (PK) gạch dưới và Khóa ngoại (FK) chỉ rõ bảng tham chiếu.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu quan hệ 'Quản Lý Phòng Khám Đa Khoa & Hồ Sơ Bệnh Án' được chuyển giao từ Câu 1:
- `CHUYENKHOA` (**<u>MAKC</u>**, TENKHOA, TRUONGKHOA)
- `BACSI` (**<u>MABS</u>**, HOTEN, HOCVI, MAKC, LUONG)
- `BENHNHAN` (**<u>MABN</u>**, HOTEN, NGAYSINH, GIOITINH, DIACHI)
- `DICHVU_KHAM` (**<u>MADV</u>**, TENDV, LOAIDV, DONGIA)
- `PHIEUKHAM` (**<u>MAPK</u>**, NGAYKHAM, MABN, MABS, CHANDOAN)
- `CHITIET_DV` (**<u>MAPK</u>**, **<u>MADV</u>**, SOLUONG, DONGIA_THU, KETQUA)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết câu lệnh SQL tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra số lượng dịch vụ chỉ định (`SOLUONG`) trong bảng `CHITIET_DV` phải lớn hơn 0 (> 0), và đơn giá niêm yết (`DONGIA`) trong bảng `DICHVU_KHAM` phải lớn hơn 0 (> 0). Cả hai thuộc tính đều không được mang giá trị `NULL`.

b. (0.75 điểm) Viết câu lệnh SQL cập nhật tăng mức lương cơ bản (`LUONG`) thêm 10% cho các bác sĩ có học vị (`HOCVI`) là 'Tiến sĩ' hoặc 'Bác sĩ CKII' trực thuộc chuyên khoa có tên (`TENKHOA`) là 'Nội tổng quát'.

### 2.2. Viết các biểu thức Đại số quan hệ (6.0 điểm)
Sinh viên sử dụng các ký hiệu phép toán chuẩn của Đại số quan hệ: $\sigma$ (chọn), $\pi$ (chiếu), $\bowtie$ (kết tự nhiên), $\bowtie_{\theta}$ (kết có điều kiện), $\leftouterjoin$ (kết ngoài trái), $\rho$ (đổi tên), $\gamma$ (gom nhóm & hàm gộp), $\div$ (chia). Mỗi câu cần nêu rõ các bước trung gian $E_1, E_2, \dots$ và biểu thức kết quả $\text{KQ}$.

a. (1.0 điểm) Liệt kê danh sách các bệnh nhân (**MABN**, **HOTEN**, **NGAYSINH**, **DIACHI**) có giới tính là 'Nữ' và có địa chỉ thường trú tại 'TP.HCM'.

b. (1.0 điểm) Cho biết danh sách các phiếu khám bệnh (**MAPK**, **NGAYKHAM**, **CHANDOAN**, **HOTEN**) do các bác sĩ thuộc chuyên khoa 'Nhi khoa' trực tiếp thăm khám.

c. (1.0 điểm) Liệt kê thông tin tất cả các chuyên khoa (**MAKC**, **TENKHOA**) và danh sách mã bác sĩ (**MABS**), họ tên bác sĩ (**HOTEN**) công tác tại chuyên khoa đó (nếu chuyên khoa mới thành lập chưa có bác sĩ nào thì thông tin bác sĩ mang giá trị `NULL`).

d. (1.0 điểm) Tính tổng số tiền dịch vụ cận lâm sàng đã chỉ định (**TONG_TIEN_DV**) của từng phiếu khám được lập trong tháng 10 năm 2024. Thông tin hiển thị gồm: **MAPK**, **NGAYKHAM**, **TONG_TIEN_DV**.

e. (1.0 điểm) Tìm các phiếu khám (**MAPK**, **NGAYKHAM**, **MABN**) đã được chỉ định **tất cả** các dịch vụ y tế thuộc phân loại 'Chẩn đoán hình ảnh'.

f. (1.0 điểm) Tìm bác sĩ (**MABS**, **HOTEN**, **HOCVI**) đã thực hiện số lượng phiếu khám bệnh (**SO_LUOT_KHAM**) nhiều nhất trong tháng 10 năm 2024 (bảo toàn tất cả các bác sĩ nếu có nhiều bác sĩ cùng đạt số lượt khám nhiều nhất).

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 06**
*Cán bộ coi thi không giải thích gì thêm.*
