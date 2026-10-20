# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 03 (MOCK-03)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu  
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series  

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.0 ĐIỂM)
Thiết kế mô hình ERD quản lý cứu trợ bão lũ: Ghi nhận thông tin hộ dân thiệt hại theo địa bàn thôn/xã, các đợt cứu trợ và các khoản đóng góp ủng hộ của nhà hảo tâm.

**Yêu cầu:**
1. Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía. Vẽ mô hình ERD. (1.20 điểm)
2. Ánh xạ mô hình ERD sang Lược đồ cơ sở dữ liệu quan hệ, chỉ rõ Khóa chính (PK) và Khóa ngoại (FK). (0.80 điểm)

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (8.0 ĐIỂM)
Cho Lược đồ cơ sở dữ liệu 'Quản Lý Tiếp Nhận & Phân Bổ Tiền Cứu Trợ Bão Lũ' gồm các quan hệ chuẩn hóa.

### 1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết lệnh UPDATE tăng/giảm giá trị của một quan hệ dựa trên thông tin kết nối từ quan hệ khác.  
b. (0.75 điểm) Viết lệnh ALTER TABLE thêm ràng buộc CHECK kiểm tra giá trị cột số liệu phải dương và trạng thái hợp lệ.  

### 2. Viết các biểu thức Đại số quan hệ (6.5 điểm)
a. (1.0 điểm) Cho lược đồ SINHVIEN(MASV, HOTEN, PHAI, MAKHOA), KHOA(MAKHOA, TENKHOA). Liệt kê danh sách các đối tượng và thông tin liên quan nếu có.  
b. (1.0 điểm) Cho lược đồ KHACHHANG(MAKH, HOTEN, DIACHI), DONHANG(MADH, MAKH, NGAYDH, TRIGIA). Viết biểu thức ĐSQH tự kết (Self-Join) tìm đối tượng cùng nhóm.  
c. (1.0 điểm) Cho lược đồ SACH(MASACH, TENSACH, MATG, NXB), TACGIA(MATG, TENTG, QUOCTICH). Tìm các đối tượng thỏa mãn điều kiện A nhưng không thỏa điều kiện B.  
d. (1.0 điểm) Cho CSDL DONHANG, CHITIET, MATHANG. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: đơn hàng mua tất cả mặt hàng loại 'Điện tử'.  
e. (1.0 điểm) Cho CSDL BACSI, PHUTRACH, BENHNHAN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.  
f. (1.5 điểm) Cho CSDL HOCVIEN, DANGKY, KHOAHOC. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: học viên hoàn thành tất cả khóa học nâng cao.  

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 03**  
*Cán bộ coi thi không giải thích gì thêm.*