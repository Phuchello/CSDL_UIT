# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 11 (MOCK-11)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.0 ĐIỂM)

Đọc kỹ bài toán quản lý chuỗi cửa hàng cà phê nhượng quyền và chuỗi cung ứng nguyên liệu pha chế:

Hệ thống chuỗi cà phê nhượng quyền cần xây dựng cơ sở dữ liệu để quản lý các khu vực kinh doanh, mạng lưới cửa hàng chi nhánh, đội ngũ nhân viên, danh mục nguyên liệu pha chế và các phiếu phân phối xuất kho từ trung tâm. Chuỗi phân chia mạng lưới theo nhiều khu vực địa lý; mỗi khu vực có mã khu vực duy nhất, tên khu vực và họ tên trưởng vùng phụ trách. Mỗi khu vực quản lý nhiều cửa hàng chi nhánh; mỗi cửa hàng có mã cửa hàng duy nhất, tên cửa hàng, địa chỉ kinh doanh, năm ký hợp đồng nhượng quyền và bắt buộc trực thuộc duy nhất một khu vực.

Tại mỗi cửa hàng có nhiều nhân viên làm việc; mỗi nhân viên có mã nhân viên duy nhất, họ tên, chức vụ ('Cửa hàng trưởng', 'Pha chế chính', 'Thu ngân', 'Phục vụ'), mức lương cơ bản hàng tháng và làm việc cố định tại đúng một cửa hàng. Tổng kho nguyên liệu của chuỗi lưu trữ nhiều loại nguyên liệu pha chế chuẩn hóa; mỗi nguyên liệu có mã nguyên liệu duy nhất, tên nguyên liệu, phân loại nguyên liệu (như 'Hạt cà phê', 'Syrup pha chế', 'Sữa đặc & tươi', 'Trà nguyên lá'), đơn giá niêm yết chuẩn và đơn vị tính (kg, lít, hộp, chai).

Khi cửa hàng có nhu cầu nhập hàng, tổng kho xuất một phiếu xuất kho nguyên liệu. Phiếu xuất có mã phiếu duy nhất, ngày xuất kho, xuất cho đúng một cửa hàng chi nhánh, tổng giá trị thanh toán dự kiến và trạng thái đơn xuất hàng ('Đang chuẩn bị', 'Đang chuyển hàng', 'Đã giao'). Trong một lần xuất kho, tổng kho có thể phân phối một hoặc nhiều loại nguyên liệu khác nhau. Mỗi chi tiết xuất kho lưu trữ mã phiếu xuất, mã nguyên liệu, số lượng xuất và đơn giá xuất thực tế tại thời điểm giao dịch.

**Yêu cầu:**
1. (1.20 điểm) Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía giữa các tập thực thể. Vẽ mô hình Thực thể – Mối kết hợp (ERD).
2. (0.80 điểm) Ánh xạ mô hình ERD đã thiết kế sang Lược đồ cơ sở dữ liệu quan hệ hoàn chỉnh. Chỉ rõ Khóa chính (PK) gạch dưới và Khóa ngoại (FK) chỉ rõ bảng tham chiếu.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (8.0 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu quan hệ 'Quản Lý Chuỗi Cà Phê Nhượng Quyền & Nguyên Liệu Pha Chế' được chuyển giao từ Câu 1:
- `KHUVUC` (**<u>MAKV</u>**, TENKV, TRUONGVUNG)
- `CUAHANG` (**<u>MACH</u>**, TENCH, DIACHI, MAKV, NAM_KYHD)
- `NHANVIEN` (**<u>MANV</u>**, HOTEN, CHUCVU, LUONG, MACH)
- `NGUYENLIEU` (**<u>MANL</u>**, TENNL, LOAINL, DONGIA_CHUAN, DVT)
- `PHIEUXUAT` (**<u>MAPX</u>**, NGAYXUAT, MACH, TONGTIEN, TRANGTHAI)
- `CHITIET_PX` (**<u>MAPX</u>**, **<u>MANL</u>**, SOLUONG, DONGIA_XUAT)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết câu lệnh SQL tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra số lượng xuất (`SOLUONG`) và đơn giá xuất (`DONGIA_XUAT`) trong bảng `CHITIET_PX` phải lớn hơn 0 (> 0). Cả hai thuộc tính đều không được mang giá trị `NULL`.

b. (0.75 điểm) Viết câu lệnh SQL cập nhật tăng 10% mức lương (`LUONG = LUONG * 1.10`) cho các nhân viên có chức vụ (`CHUCVU`) là 'Cửa hàng trưởng' làm việc tại các cửa hàng thuộc khu vực có tên (`TENKV`) là 'Khu vực Trung tâm'.

### 2.2. Viết các biểu thức Đại số quan hệ (6.5 điểm)
Sinh viên sử dụng các ký hiệu phép toán chuẩn của Đại số quan hệ: $\sigma$ (chọn), $\pi$ (chiếu), $\bowtie$ (kết tự nhiên), $\bowtie_{\theta}$ (kết có điều kiện), $\leftouterjoin$ (kết ngoài trái), $\rho$ (đổi tên), $\gamma$ (gom nhóm & hàm gộp), $\div$ (chia). Mỗi câu cần nêu rõ các bước trung gian $E_1, E_2, \dots$ và biểu thức kết quả $\text{KQ}$.

a. (1.0 điểm) Liệt kê danh sách các nguyên liệu (**MANL**, **TENNL**, **DONGIA_CHUAN**, **DVT**) thuộc phân loại 'Hạt cà phê' có đơn giá chuẩn từ 200.000 VNĐ trở lên ($\ge 200.000$).

b. (1.0 điểm) Cho biết danh sách các phiếu xuất kho (**MAPX**, **NGAYXUAT**, **TONGTIEN**, **TENCH**) xuất cho cửa hàng mang tên `TENCH = 'The Coffee House Landmark 81'`.

c. (1.0 điểm) Liệt kê thông tin tất cả các khu vực (**MAKV**, **TENKV**) cùng danh sách mã cửa hàng (**MACH**), tên cửa hàng (**TENCH**) trực thuộc khu vực đó (nếu khu vực mới mở chưa thành lập cửa hàng nào thì thông tin cửa hàng mang giá trị `NULL`).

d. (1.0 điểm) Tính tổng giá trị xuất hàng thực tế (**TONG_GIA_TRI_XUAT** = SUM(SOLUONG * DONGIA_XUAT)) của từng phiếu xuất kho (**MAPX**, **NGAYXUAT**) lập trong tháng 11 năm 2024 có trạng thái là 'Đã giao'.

e. (1.0 điểm) Tìm các cửa hàng (**MACH**, **TENCH**, **MAKV**) đã từng nhập **tất cả** các loại nguyên liệu thuộc phân loại 'Syrup pha chế' của chuỗi.

f. (1.5 điểm) Tìm cửa hàng (**MACH**, **TENCH**, **TENKV**) có tổng số lượng nguyên liệu nhập về (**TONG_SOLUONG_NHAP**) nhiều nhất trong toàn bộ năm 2024 (bảo toàn tất cả các cửa hàng nếu có nhiều cửa hàng cùng đạt số lượng nhập cao nhất).

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 11**
*Cán bộ coi thi không giải thích gì thêm.*
