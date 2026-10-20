# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 14 (MOCK-14)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu  
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series  

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)
Đọc ngữ cảnh bài toán 'Quản lý Đề Tài Nghiên Cứu Khoa Học Sinh Viên', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

**Yêu cầu:**
1. Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía. Vẽ mô hình ERD. (1.50 điểm)
2. Ánh xạ mô hình ERD sang Lược đồ cơ sở dữ liệu quan hệ, chỉ rõ Khóa chính (PK) và Khóa ngoại (FK). (1.00 điểm)

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)
Cho Lược đồ cơ sở dữ liệu 'Quản Lý Đề Tài Nghiên Cứu Khoa Học Trọng Điểm' gồm các quan hệ chuẩn hóa.

### 1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết câu truy vấn T-SQL bằng kỹ thuật tương quan hai lần lặp Double NOT EXISTS để tìm các khách hàng (MAKH, HOTEN) đã mở tất cả các loại tài khoản.  
b. (0.75 điểm) Viết lệnh T-SQL CREATE TABLE tạo bảng CTPX với PK kép và CHECK số lượng > 0.  

### 2. Viết các biểu thức Đại số quan hệ (6.0 điểm)
a. (1.0 điểm) Cho lược đồ CHUYENBAY(MACB, SOHIEU, GIOBAY, NOIDI, NOIDEN), PHICONG(MAPC, HOTEN, MACB). Viết biểu thức ĐSQH liệt kê danh sách chuyến bay xuất phát từ 'SGN' đến 'HAN'.  
b. (1.0 điểm) Cho lược đồ BACSI(MABS, HOTEN, CHUYENKHOA), PHONGKHAM(MAPK, TENPK, MABS_TRUONG). Viết biểu thức ĐSQH kết nối các quan hệ để tìm thông tin bác sĩ chuyên khoa 'Tai-Mũi-Họng'.  
c. (1.0 điểm) Cho lược đồ TAIKHOAN(SOTK, MAKH, SODU), GIAODICH(MAGD, SOTK, SOTIEN, NGAYGD). Liệt kê danh sách các đối tượng và thông tin liên quan nếu có.  
d. (1.0 điểm) Cho CSDL BACSI, PHUTRACH, BENHNHAN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.  
e. (1.0 điểm) Cho CSDL HOCVIEN, DANGKY, KHOAHOC. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: học viên hoàn thành tất cả khóa học nâng cao.  
f. (1.0 điểm) Cho CSDL TAU, CAPCANG, CANGBIEN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.  

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 14**  
*Cán bộ coi thi không giải thích gì thêm.*