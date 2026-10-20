# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 08 (MOCK-08)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu  
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series  

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)
Đọc ngữ cảnh bài toán 'Quản lý Sàn Thương Mại Điện Tử & Đơn Hàng', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

**Yêu cầu:**
1. Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía. Vẽ mô hình ERD. (1.50 điểm)
2. Ánh xạ mô hình ERD sang Lược đồ cơ sở dữ liệu quan hệ, chỉ rõ Khóa chính (PK) và Khóa ngoại (FK). (1.00 điểm)

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)
Cho Lược đồ cơ sở dữ liệu 'Quản Lý Sàn Thương Mại Điện Tử & Vận Chuyển Hàng' gồm các quan hệ chuẩn hóa.

### 1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết lệnh UPDATE tăng/giảm giá trị của một quan hệ dựa trên thông tin kết nối từ quan hệ khác.  
b. (0.75 điểm) Viết lệnh ALTER TABLE thêm ràng buộc CHECK kiểm tra giá trị cột số liệu phải dương và trạng thái hợp lệ.  

### 2. Viết các biểu thức Đại số quan hệ (6.0 điểm)
a. (1.0 điểm) Cho lược đồ TAIKHOAN(SOTK, MAKH, SODU), GIAODICH(MAGD, SOTK, SOTIEN, NGAYGD). Liệt kê danh sách các đối tượng và thông tin liên quan nếu có.  
b. (1.0 điểm) Cho lược đồ MONHOC(MAMH, TENMH, SOTC), LOPHOC(MALOP, MAMH, HOCKY, NAM). Viết biểu thức ĐSQH tự kết (Self-Join) tìm đối tượng cùng nhóm.  
c. (1.0 điểm) Cho lược đồ XEMAY(MAXE, BIENSO, DONGXE), BAODUONG(MABD, MAXE, NGAYBD, CHIPHI). Tìm các đối tượng thỏa mãn điều kiện A nhưng không thỏa điều kiện B.  
d. (1.0 điểm) Cho CSDL DIEMTIEM, PHIEUXUAT, CTPX, VACXIN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.  
e. (1.0 điểm) Cho CSDL DONHANG, CHITIET, MATHANG. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: đơn hàng mua tất cả mặt hàng loại 'Điện tử'.  
f. (1.0 điểm) Cho CSDL BACSI, PHUTRACH, BENHNHAN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.  

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 08**  
*Cán bộ coi thi không giải thích gì thêm.*