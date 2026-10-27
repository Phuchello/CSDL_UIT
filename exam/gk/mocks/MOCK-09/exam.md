# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 09 (MOCK-09)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.0 ĐIỂM)

Đọc kỹ bài toán quản lý giải đấu thể thao điện tử (Esports) sinh viên liên trường:

Ban tổ chức giải đấu thể thao điện tử sinh viên cần xây dựng cơ sở dữ liệu để quản lý các trường đại học, đội tuyển thi đấu, tuyển thủ, các trận đấu và nhà tài trợ. Giải đấu quy tụ sinh viên từ nhiều trường đại học; mỗi trường đại học có một mã trường duy nhất, tên trường và thành phố đặt trụ sở chính. Mỗi trường có thể cử nhiều đội tuyển tham gia tranh tài ở các bộ môn khác nhau; mỗi đội thi có mã đội duy nhất, tên đội tuyển, họ tên người quản lý đội và bắt buộc đại diện cho duy nhất một trường đại học.

Mỗi đội thi bao gồm nhiều tuyển thủ chính thức và dự bị; mỗi tuyển thủ có mã tuyển thủ duy nhất, họ tên, vị trí thi đấu ('Đường trên', 'Đi rừng', 'Đường giữa', 'Xạ thủ', 'Hỗ trợ'), mức thù lao theo mùa giải và chỉ thi đấu cho đúng một đội tuyển trong suốt mùa giải.

Khuôn khổ giải đấu gồm nhiều trận đấu đối kháng diễn ra theo lịch trình. Mỗi trận đấu có mã trận đấu duy nhất, ngày thi đấu, vòng đấu ('Vòng bảng', 'Tứ kết', 'Bán kết', 'Chung kết') và địa điểm thi đấu (tên nhà thi đấu hoặc phòng máy). Mỗi trận đấu có đúng 2 đội tuyển tham gia tranh tài; mỗi chi tiết tham gia trận đấu ghi nhận mã trận đấu, mã đội thi, số ván thắng trong trận đấu, số tiền thưởng đạt được và kết quả thi đấu ('Thắng' hoặc 'Thua'). Ngoài ra, mỗi trận đấu có thể được tài trợ bởi các nhà tài trợ thương mại. Mỗi khoản tài trợ ghi nhận mã nhà tài trợ, tên nhà tài trợ, trận đấu được tài trợ và số tiền tài trợ.

**Yêu cầu:**
1. (1.20 điểm) Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía giữa các tập thực thể. Vẽ mô hình Thực thể – Mối kết hợp (ERD).
2. (0.80 điểm) Ánh xạ mô hình ERD đã thiết kế sang Lược đồ cơ sở dữ liệu quan hệ hoàn chỉnh. Chỉ rõ Khóa chính (PK) gạch dưới và Khóa ngoại (FK) chỉ rõ bảng tham chiếu.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (8.0 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu quan hệ 'Quản Lý Giải Đấu Thể Thao Điện Tử Sinh Viên' được chuyển giao từ Câu 1:
- `TRUONG` (**<u>MATRUONG</u>**, TENTRUONG, THANHPHO)
- `DOITHI` (**<u>MADOI</u>**, TENDOI, MATRUONG, NGUOIQUANLY)
- `TUYENTHU` (**<u>MATT</u>**, HOTEN, VITRI, MADOI, TIENLUONG)
- `TRANDAU` (**<u>MATRAN</u>**, NGAYDAU, VONGDAU, DIADIEM)
- `THAMGIA_TRAN` (**<u>MATRAN</u>**, **<u>MADOI</u>**, SOVANTHANG, TIENTHUONG, KETQUA)
- `NHATAITRO` (**<u>MANTT</u>**, TENNTT, MATRAN, SOTIEN_TT)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết câu lệnh SQL tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra số ván thắng (`SOVANTHANG`) trong bảng `THAMGIA_TRAN` phải lớn hơn hoặc bằng 0 ($\ge 0$), và mức thù lao (`TIENLUONG`) trong bảng `TUYENTHU` phải lớn hơn 0 (> 0). Cả hai thuộc tính đều không được mang giá trị `NULL`.

b. (0.75 điểm) Viết câu lệnh SQL cập nhật tăng 15% mức thù lao (`TIENLUONG = TIENLUONG * 1.15`) cho các tuyển thủ có vị trí thi đấu (`VITRI`) là 'Đường giữa' thuộc các đội thi đấu đại diện cho trường có tên (`TENTRUONG`) là 'Đại học CNTT'.

### 2.2. Viết các biểu thức Đại số quan hệ (6.5 điểm)
Sinh viên sử dụng các ký hiệu phép toán chuẩn của Đại số quan hệ: $\sigma$ (chọn), $\pi$ (chiếu), $\bowtie$ (kết tự nhiên), $\bowtie_{\theta}$ (kết có điều kiện), $\leftouterjoin$ (kết ngoài trái), $\rho$ (đổi tên), $\gamma$ (gom nhóm & hàm gộp), $\div$ (chia). Mỗi câu cần nêu rõ các bước trung gian $E_1, E_2, \dots$ và biểu thức kết quả $\text{KQ}$.

a. (1.0 điểm) Liệt kê danh sách các tuyển thủ (**MATT**, **HOTEN**, **TIENLUONG**) thi đấu ở vị trí 'Xạ thủ' có mức thù lao từ 15.000.000 VNĐ trở lên ($\ge 15.000.000$).

b. (1.0 điểm) Cho biết danh sách các trận đấu (**MATRAN**, **NGAYDAU**, **VONGDAU**, **TENDOI**) có sự tham gia thi đấu của đội tuyển mang tên `TENDOI = 'UIT Hunters'`.

c. (1.0 điểm) Liệt kê thông tin tất cả các trường đại học (**MATRUONG**, **TENTRUONG**) cùng danh sách mã đội thi (**MADOI**), tên đội (**TENDOI**) trực thuộc trường đó (nếu trường mới đăng ký chưa thành lập đội tuyển nào thì thông tin đội thi mang giá trị `NULL`).

d. (1.0 điểm) Tính tổng số tiền thưởng (**TONG_TIEN_THUONG** = SUM(TIENTHUONG)) của từng đội thi (**MADOI**, **TENDOI**) đạt được từ các trận đấu có kết quả `KETQUA = 'Thắng'` diễn ra trong tháng 11 năm 2024.

e. (1.0 điểm) Tìm các đội thi (**MADOI**, **TENDOI**, **MATRUONG**) đã từng tham gia thi đấu tại **tất cả** các địa điểm (`DIADIEM`) thuộc vòng đấu 'Vòng bảng'.

f. (1.5 điểm) Tìm đội thi (**MADOI**, **TENDOI**, **TENTRUONG**) có tổng số ván thắng (**TONG_SO_VAN_THANG**) nhiều nhất trong toàn bộ giải đấu năm 2024 (bảo toàn tất cả các đội thi nếu có nhiều đội cùng đạt số ván thắng cao nhất).

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 09**
*Cán bộ coi thi không giải thích gì thêm.*
