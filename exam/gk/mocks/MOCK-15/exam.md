# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 15 (MOCK-15)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.0 ĐIỂM)
Đọc ngữ cảnh bài toán 'Quản lý Trại Cứu Hộ Động Vật Hoang Dã', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

**Yêu cầu:**
1. Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía. Vẽ mô hình ERD. (1.20 điểm)
2. Ánh xạ mô hình ERD sang Lược đồ cơ sở dữ liệu quan hệ, chỉ rõ Khóa chính (PK) và Khóa ngoại (FK). (0.80 điểm)

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (8.0 ĐIỂM)
Cho Lược đồ cơ sở dữ liệu 'Quản Lý Trại Cứu Hộ Động Vật Hoang Dã' gồm các quan hệ chuẩn hóa.

### 1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết lệnh T-SQL UPDATE giảm 15% đơn giá cho các lô vắc-xin hết hạn trong quý 1 năm 2025.
b. (0.75 điểm) Viết lệnh ALTER TABLE thêm ràng buộc CHECK kiểm tra giá trị cột số liệu phải dương và trạng thái hợp lệ.

### 2. Viết các biểu thức Đại số quan hệ (6.5 điểm)
a. (1.0 điểm) Cho lược đồ MONHOC(MAMH, TENMH, SOTC), LOPHOC(MALOP, MAMH, HOCKY, NAM). Viết biểu thức ĐSQH tự kết (Self-Join) tìm đối tượng cùng nhóm.
b. (1.0 điểm) Cho lược đồ XEMAY(MAXE, BIENSO, DONGXE), BAODUONG(MABD, MAXE, NGAYBD, CHIPHI). Tìm các đối tượng thỏa mãn điều kiện A nhưng không thỏa điều kiện B.
c. (1.0 điểm) Cho lược đồ NHANVIEN(MANV, HOTEN, CHUCVU), HOADON(MAHD, MANV, NGAYLAP). Viết biểu thức ĐSQH liệt kê danh sách hóa đơn do nhân viên chức vụ 'Thu ngân' lập.
d. (1.0 điểm) Cho CSDL NHA_DAUTU, GOPT_VON, DUAN. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: nhà đầu tư góp vốn vào tất cả dự án năng lượng xanh.
e. (1.0 điểm) Cho CSDL KHACH, DATTIEC, SANHTIEC. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.
f. (1.5 điểm) Cho CSDL DOCGIA, MUONSACH, SACH, THELOAI. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: độc giả đã mượn sách thuộc tất cả các thể loại khoa học.

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 15**
*Cán bộ coi thi không giải thích gì thêm.*
