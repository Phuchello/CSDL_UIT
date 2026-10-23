# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 13 (MOCK-13)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.0 ĐIỂM)
Đọc ngữ cảnh bài toán 'Quản lý Tuyến Xe Buýt & Metro Đô Thị', xây dựng mô hình Thực thể – Mối kết hợp (ERD) hoàn chỉnh với đầy đủ thực thể, thuộc tính khóa, mối kết hợp và bản số min-max (0,1), (1,1), (0,N), (1,N). Sau đó ánh xạ sang Lược đồ cơ sở dữ liệu quan hệ chỉ rõ Khóa chính (PK) và Khóa ngoại (FK).

**Yêu cầu:**
1. Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía. Vẽ mô hình ERD. (1.20 điểm)
2. Ánh xạ mô hình ERD sang Lược đồ cơ sở dữ liệu quan hệ, chỉ rõ Khóa chính (PK) và Khóa ngoại (FK). (0.80 điểm)

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (8.0 ĐIỂM)
Cho Lược đồ cơ sở dữ liệu 'Quản Lý Hệ Thống Tuyến Xe Buýt & Metro TP.HCM' gồm các quan hệ chuẩn hóa.

### 1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra thuộc tính SOLIEUXUAT trong CTPX phải là số nguyên dương (> 0), và thuộc tính TRANGTHAI trong PHIEUXUAT chỉ nhận một trong hai giá trị là 0 hoặc 1.
b. (0.75 điểm) Viết câu lệnh SQL cập nhật (UPDATE) tăng giá đơn vị (DONGIA) thêm 10% đối với các lô vắc-xin có hạn sử dụng (HSD) trong năm 2025 do nhà cung cấp có tên là 'AstraZeneca' cung cấp.

### 2. Viết các biểu thức Đại số quan hệ (6.5 điểm)
a. (1.0 điểm) Cho lược đồ SINHVIEN(MASV, HOTEN, PHAI, MAKHOA), KHOA(MAKHOA, TENKHOA). Liệt kê danh sách các đối tượng và thông tin liên quan nếu có.
b. (1.0 điểm) Cho lược đồ KHACHHANG(MAKH, HOTEN, DIACHI), DONHANG(MADH, MAKH, NGAYDH, TRIGIA). Viết biểu thức ĐSQH tự kết (Self-Join) tìm đối tượng cùng nhóm.
c. (1.0 điểm) Cho lược đồ SACH(MASACH, TENSACH, MATG, NXB), TACGIA(MATG, TENTG, QUOCTICH). Tìm các đối tượng thỏa mãn điều kiện A nhưng không thỏa điều kiện B.
d. (1.0 điểm) Cho CSDL DOCGIA, MUONSACH, SACH, THELOAI. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: độc giả đã mượn sách thuộc tất cả các thể loại khoa học.
e. (1.0 điểm) Cho CSDL DIEMTIEM, PHIEUXUAT, CTPX, VACXIN. Viết biểu thức ĐSQH gom nhóm tính tổng hoặc tìm đối tượng đạt giá trị cao nhất.
f. (1.5 điểm) Cho CSDL DONHANG, CHITIET, MATHANG. Viết biểu thức ĐSQH tìm danh sách đối tượng thỏa mãn điều kiện: đơn hàng mua tất cả mặt hàng loại 'Điện tử'.

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 13**
*Cán bộ coi thi không giải thích gì thêm.*
