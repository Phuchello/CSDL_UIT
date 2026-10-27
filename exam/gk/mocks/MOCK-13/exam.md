# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 13 (MOCK-13)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.0 ĐIỂM)

Đọc kỹ bài toán quản lý mạng lưới vận tải hành khách công cộng xe buýt và tuyến đường sắt đô thị (Metro) TP.HCM:

Trung tâm Quản lý Giao thông Công cộng TP.HCM cần xây dựng cơ sở dữ liệu để vận hành hệ thống xe buýt đa phương thức và các tuyến đường sắt đô thị Metro. Hệ thống quản lý mạng lưới các tuyến vận chuyển hành khách; mỗi tuyến xe có mã tuyến duy nhất, tên tuyến (như 'Bến Thành - Suối Tiên', 'Bến Thành - Bến xe Miền Đông mới'), loại hình phương tiện ('Xe buýt phổ thông', 'Xe buýt điện VinBus', 'Tuyến Metro'), cự ly tuyến đường (tính theo km) và mức giá vé một lượt chuẩn.

Trên các tuyến đường có bố trí hệ thống trạm dừng đón trả khách; mỗi trạm dừng có mã trạm duy nhất, tên trạm dừng, địa chỉ cụ thể và quận huyện trực thuộc. Một tuyến xe đi qua nhiều trạm dừng khác nhau theo một lộ trình xác định, và một trạm dừng có thể phục vụ nhiều tuyến xe cùng ghé qua. Mỗi chi tiết lộ trình ghi nhận mã tuyến, mã trạm dừng, số thứ tự ghé trạm của trạm dừng trên tuyến đó và khoảng cách (km) tính từ trạm xuất phát đầu tuyến.

Để vận hành các tuyến, trung tâm quản lý đội xe phương tiện giao thông; mỗi phương tiện có mã phương tiện duy nhất, biển số kiểm soát, số ghế ngồi, năm sản xuất và hoạt động cố định trên đúng một tuyến xe. Đội ngũ tài xế chuyên nghiệp điều khiển phương tiện; mỗi tài xế có mã tài xế duy nhất, họ tên, hạng giấy phép lái xe ('Hạng D', 'Hạng E'), mức lương cơ bản hàng tháng và được phân công phụ trách cố định đúng một phương tiện. Hàng ngày, mỗi phương tiện thực hiện nhiều chuyến đi; mỗi chuyến đi có mã chuyến duy nhất, thuộc về đúng một phương tiện, ngày chạy, giờ xuất phát, tổng số lượng hành khách phục vụ và tổng doanh thu bán vé thực tế thu được trong chuyến đi.

**Yêu cầu:**
1. (1.20 điểm) Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía giữa các tập thực thể. Vẽ mô hình Thực thể – Mối kết hợp (ERD).
2. (0.80 điểm) Ánh xạ mô hình ERD đã thiết kế sang Lược đồ cơ sở dữ liệu quan hệ hoàn chỉnh. Chỉ rõ Khóa chính (PK) gạch dưới và Khóa ngoại (FK) chỉ rõ bảng tham chiếu.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (8.0 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu quan hệ 'Quản Lý Tuyến Xe Buýt & Metro TP.HCM' được chuyển giao từ Câu 1:
- `TUYEN_XE` (**<u>MATUYEN</u>**, TENTUYEN, LOAI_HINH, CULY_KM, GIAVE_LUOT)
- `TRAM_DUNG` (**<u>MATRAM</u>**, TENTRAM, DIACHI, QUAN_HUYEN)
- `LOTRINH` (**<u>MATUYEN</u>**, **<u>MATRAM</u>**, SOTHUTU, KHOANGCACH_KM)
- `PHUONGTIEN` (**<u>MAPT</u>**, BIENSO, SOGHE, NAMSX, MATUYEN)
- `TAIXE` (**<u>MATX</u>**, HOTEN, HANG_GPLX, LUONG_CB, MAPT)
- `CHUYEN_DI` (**<u>MACHUYEN</u>**, MAPT, NGAYCHAY, GIOXUATPHAT, SOLUONG_KHACH, DOANHTHU)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết câu lệnh SQL tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra số lượng hành khách (`SOLUONG_KHACH`) và doanh thu (`DOANHTHU`) trong bảng `CHUYEN_DI` phải không âm ($\ge 0$). Cả hai thuộc tính đều không được mang giá trị `NULL`.

b. (0.75 điểm) Viết câu lệnh SQL cập nhật tăng 10% mức lương cơ bản (`LUONG_CB = LUONG_CB * 1.10`) cho các tài xế điều khiển phương tiện đang phục vụ trên tuyến xe có loại hình (`LOAI_HINH`) là 'Xe buýt điện VinBus'.

### 2.2. Viết các biểu thức Đại số quan hệ (6.5 điểm)
Sinh viên sử dụng các ký hiệu phép toán chuẩn của Đại số quan hệ: $\sigma$ (chọn), $\pi$ (chiếu), $\bowtie$ (kết tự nhiên), $\bowtie_{\theta}$ (kết có điều kiện), $\leftouterjoin$ (kết ngoài trái), $\rho$ (đổi tên), $\gamma$ (gom nhóm & hàm gộp), $\div$ (chia). Mỗi câu cần nêu rõ các bước trung gian $E_1, E_2, \dots$ và biểu thức kết quả $\text{KQ}$.

a. (1.0 điểm) Liệt kê danh sách các tuyến xe (**MATUYEN**, **TENTUYEN**, **CULY_KM**, **GIAVE_LUOT**) thuộc loại hình 'Tuyến Metro' có cự ly từ 15 km trở lên ($\ge 15$).

b. (1.0 điểm) Cho biết danh sách các phương tiện (**MAPT**, **BIENSO**, **SOGHE**) đang phục vụ cho tuyến xe mang tên `TENTUYEN = 'Bến Thành - Bến xe Miền Đông mới'`.

c. (1.0 điểm) Liệt kê thông tin tất cả các trạm dừng (**MATRAM**, **TENTRAM**, **QUAN_HUYEN**) cùng mã tuyến xe (**MATUYEN**), số thứ tự ghé trạm (**SOTHUTU**) đi qua trạm đó (nếu trạm dừng mới xây dựng chưa có tuyến nào đi qua thì thông tin tuyến xe mang giá trị `NULL`).

d. (1.0 điểm) Tính tổng số lượng hành khách phục vụ (**TONG_KHACH** = SUM(SOLUONG_KHACH)) của từng phương tiện (**MAPT**, **BIENSO**) thực hiện các chuyến đi trong ngày 20 tháng 11 năm 2024.

e. (1.0 điểm) Tìm các tuyến xe (**MATUYEN**, **TENTUYEN**, **LOAI_HINH**) đi qua **tất cả** các trạm dừng nằm trên địa bàn quận `QUAN_HUYEN = 'Thủ Đức'`.

f. (1.5 điểm) Tìm tuyến xe (**MATUYEN**, **TENTUYEN**, **LOAI_HINH**) có tổng doanh thu các chuyến đi (**TONG_DOANHTHU**) trong toàn bộ năm 2024 đạt cao nhất (bảo toàn tất cả các tuyến nếu có nhiều tuyến cùng đạt doanh thu cao nhất).

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 13**
*Cán bộ coi thi không giải thích gì thêm.*
