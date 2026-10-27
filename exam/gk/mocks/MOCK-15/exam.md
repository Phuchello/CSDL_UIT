# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 15 (MOCK-15)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.0 ĐIỂM)

Đọc kỹ bài toán quản lý trung tâm cứu hộ, bảo tồn và tái thả động vật hoang dã:

Trung tâm Cứu hộ Động vật Hoang dã Vườn quốc gia cần xây dựng cơ sở dữ liệu quan hệ để theo dõi quá trình cứu hộ y tế, chăm sóc bán hoang dã và tái thả các cá thể động vật quý hiếm về môi trường rừng tự nhiên. Trung tâm phân chia khuôn viên thành nhiều phân khu bảo tồn chức năng; mỗi phân khu có mã khu duy nhất, tên phân khu (như 'Khu Cứu Hộ Thú Lớn', 'Khu Bán Tự Nhiên Cát Tiên', 'Khu Cứu Hộ Linh Trưởng'), diện tích (hecta) và họ tên cán bộ phụ trách khu.

Trung tâm lưu trữ danh mục các loài động vật hoang dã nằm trong sách đỏ; mỗi loài có mã loài duy nhất, tên loài thông thường, tên khoa học quốc tế và mức độ nguy cấp ('Cực kỳ nguy cấp', 'Nguy cấp', 'Sắp nguy cấp'). Mỗi cá thể động vật được cứu hộ về trung tâm được gắn mã cá thể duy nhất, thuộc về đúng một loài động vật, giới tính ('Đực', 'Cái'), cân nặng (kg), tình trạng sức khỏe tiếp nhận ('Khỏe mạnh', 'Đang điều trị', 'Chờ tái thả') và được nuôi dưỡng tại đúng một phân khu bảo tồn.

Đội ngũ nhân sự chuyên trách chăm sóc động vật; mỗi nhân viên có mã nhân viên duy nhất, họ tên, chuyên môn chính ('Bác sĩ thú y', 'Chuyên viên cứu hộ', 'Kiểm lâm viên'), mức lương cơ bản hàng tháng và làm việc cố định tại đúng một phân khu bảo tồn. Quá trình chăm sóc điều trị được ghi chép chi tiết; mỗi lượt chăm sóc có mã chăm sóc duy nhất, ghi rõ cá thể động vật được chăm sóc, nhân viên trực tiếp thực hiện, ngày chăm sóc, chi phí phát sinh (tiền thuốc, dinh dưỡng) và ghi chú y khoa. Khi động vật phục hồi thể trạng hoàn toàn, trung tâm tổ chức các đợt tái thả về tự nhiên; mỗi đợt tái thả có mã đợt duy nhất, cá thể động vật được thả, ngày tái thả, địa điểm thả rừng và trạng thái giám sát sau thả ('Thành công', 'Đang giám sát GPS', 'Thất bại').

**Yêu cầu:**
1. (1.20 điểm) Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía giữa các tập thực thể. Vẽ mô hình Thực thể – Mối kết hợp (ERD).
2. (0.80 điểm) Ánh xạ mô hình ERD đã thiết kế sang Lược đồ cơ sở dữ liệu quan hệ hoàn chỉnh. Chỉ rõ Khóa chính (PK) gạch dưới và Khóa ngoại (FK) chỉ rõ bảng tham chiếu.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (8.0 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu quan hệ 'Quản Lý Trại Cứu Hộ Động Vật Hoang Dã' được chuyển giao từ Câu 1:
- `KHU_BAOTON` (**<u>MAKHU</u>**, TENKHU, DIENTICH_HA, NGUOI_PHUTRACH)
- `LOAI_DONGVAT` (**<u>MALOAI</u>**, TENLOAI, TEN_KHOAHOC, MUC_NGUYCAP)
- `DONGVAT` (**<u>MADV</u>**, MALOAI, GIOITINH, CANNANG_KG, TINHTRANG_SK, MAKHU)
- `NHANVIEN` (**<u>MANV</u>**, HOTEN, CHUYENMON, LUONG, MAKHU)
- `CHITIET_CS` (**<u>MACS</u>**, MADV, MANV, NGAYCS, CHIPHI_CS, GHI_CHU)
- `DOT_TAITHA` (**<u>MADOT</u>**, MADV, NGAYTHA, DIADIEM_THA, TRANGTHAI)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết câu lệnh SQL tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra chi phí chăm sóc (`CHIPHI_CS >= 0`) trong bảng `CHITIET_CS` và cân nặng cá thể động vật (`CANNANG_KG > 0`) trong bảng `DONGVAT`. Cả hai thuộc tính đều không được mang giá trị `NULL`.

b. (0.75 điểm) Viết câu lệnh SQL cập nhật tăng 10% mức lương (`LUONG = LUONG * 1.10`) cho các nhân viên có chuyên môn (`CHUYENMON`) là 'Bác sĩ thú y' công tác tại phân khu có tên (`TENKHU`) là 'Khu Cứu Hộ Thú Lớn'.

### 2.2. Viết các biểu thức Đại số quan hệ (6.5 điểm)
Sinh viên sử dụng các ký hiệu phép toán chuẩn của Đại số quan hệ: $\sigma$ (chọn), $\pi$ (chiếu), $\bowtie$ (kết tự nhiên), $\bowtie_{\theta}$ (kết có điều kiện), $\leftouterjoin$ (kết ngoài trái), $\rho$ (đổi tên), $\gamma$ (gom nhóm & hàm gộp), $\div$ (chia). Mỗi câu cần nêu rõ các bước trung gian $E_1, E_2, \dots$ và biểu thức kết quả $\text{KQ}$.

a. (1.0 điểm) Liệt kê danh sách các loài động vật (**MALOAI**, **TENLOAI**, **TEN_KHOAHOC**) có mức độ nguy cấp là 'Cực kỳ nguy cấp'.

b. (1.0 điểm) Cho biết danh sách các cá thể động vật (**MADV**, **GIOITINH**, **CANNANG_KG**, **TINHTRANG_SK**) thuộc phân khu bảo tồn có tên là `TENKHU = 'Khu Bán Tự Nhiên Cát Tiên'`.

c. (1.0 điểm) Liệt kê thông tin tất cả các phân khu bảo tồn (**MAKHU**, **TENKHU**) cùng mã nhân viên (**MANV**), họ tên nhân viên (**HOTEN**) công tác tại phân khu đó (nếu phân khu mới thành lập chưa bố trí nhân viên thì thông tin nhân viên mang giá trị `NULL`).

d. (1.0 điểm) Tính tổng chi phí chăm sóc y tế (**TONG_CHIPHI** = SUM(CHIPHI_CS)) của từng cá thể động vật (**MADV**, **TINHTRANG_SK**) phát sinh trong tháng 10 năm 2024.

e. (1.0 điểm) Tìm các nhân viên (**MANV**, **HOTEN**, **CHUYENMON**) đã từng trực tiếp chăm sóc **tất cả** các cá thể động vật thuộc loài mang tên `TENLOAI = 'Tê tê Java'`.

f. (1.5 điểm) Tìm phân khu bảo tồn (**MAKHU**, **TENKHU**, **DIENTICH_HA**) có tổng số lượng cá thể động vật (**TONG_DONGVAT**) đang tiếp nhận nuôi dưỡng nhiều nhất (bảo toàn tất cả các phân khu nếu có nhiều phân khu cùng đạt số lượng cao nhất).

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 15**
*Cán bộ coi thi không giải thích gì thêm.*
