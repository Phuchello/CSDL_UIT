# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 14 (MOCK-14)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)

Đọc kỹ bài toán quản lý đề tài nghiên cứu khoa học trọng điểm và công bố quốc tế tại Đại học Quốc gia:

Phòng Quản lý Khoa học và Công nghệ của Đại học Quốc gia cần xây dựng một cơ sở dữ liệu quan hệ để theo dõi tiến độ thực hiện các đề tài nghiên cứu, phân bổ ngân sách giải ngân và ghi nhận các sản phẩm khoa học công bố quốc tế. Trường có nhiều khoa và viện nghiên cứu chuyên ngành; mỗi khoa viện có mã khoa viện duy nhất, tên khoa viện, số điện thoại văn phòng và họ tên trưởng khoa/viện trưởng. Tại mỗi khoa viện có đội ngũ giảng viên và chuyên viên nghiên cứu công tác; mỗi giảng viên có mã giảng viên duy nhất, họ tên, học hàm ('Giáo sư', 'Phó Giáo sư', 'Không'), học vị cao nhất ('Tiến sĩ', 'Thạc sĩ', 'Cử nhân'), mức lương và trực thuộc duy nhất một khoa viện.

Nhà trường phê duyệt và cấp mã quản lý cho các đề tài nghiên cứu khoa học; mỗi đề tài có mã đề tài duy nhất, tên đề tài, cấp quản lý ('Cấp Nhà nước', 'Cấp Bộ', 'Cấp ĐHQG'), tổng kinh phí phê duyệt, ngày bắt đầu, ngày kết thúc dự kiến và do đúng một giảng viên giữ vai trò chủ nhiệm đề tài chịu trách nhiệm chính. Một đề tài có sự tham gia phối hợp của nhiều nhà khoa học; mỗi phân công tham gia lưu mã đề tài, mã giảng viên, vai trò trong đề tài ('Thư ký khoa học', 'Nghiên cứu viên chính', 'Cộng tác viên') và số giờ đăng ký tham gia đóng góp.

Trong quá trình thực hiện, nhà trường tiến hành các đợt giải ngân kinh phí nghiên cứu theo tiến độ; mỗi đợt giải ngân có mã giải ngân duy nhất, thuộc về đúng một đề tài, ngày giải ngân, số tiền giải ngân thực tế và nội dung chi. Đồng thời, đề tài nghiệm thu các sản phẩm khoa học công bố; mỗi sản phẩm khoa học có mã sản phẩm duy nhất, tên sản phẩm (tên bài báo khoa học, sáng chế), phân loại sản phẩm, xếp hạng quốc tế ('Q1', 'Q2', 'Scopus', 'Trong nước') và được công bố từ đúng một đề tài nghiên cứu.

**Yêu cầu:**
1. (1.50 điểm) Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía giữa các tập thực thể. Vẽ mô hình Thực thể – Mối kết hợp (ERD).
2. (1.00 điểm) Ánh xạ mô hình ERD đã thiết kế sang Lược đồ cơ sở dữ liệu quan hệ hoàn chỉnh. Chỉ rõ Khóa chính (PK) gạch dưới và Khóa ngoại (FK) chỉ rõ bảng tham chiếu.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu quan hệ 'Quản Lý Đề Tài Nghiên Cứu Khoa Học Trọng Điểm' được chuyển giao từ Câu 1:
- `KHOA_VIEN` (**<u>MAKV</u>**, TENKV, DIENTHOAI, TRUONGKHOA)
- `GIANGVIEN` (**<u>MAGV</u>**, HOTEN, HOCHAM, HOCVI, LUONG, MAKV)
- `DETAI` (**<u>MADT</u>**, TENDT, CAP_QUANLY, KINHPHI, NGAYBD, NGAYKT, CHUNHIEM_DT)
- `THAMGIA_DT` (**<u>MADT</u>**, **<u>MAGV</u>**, VAITRO, SOGIO_TG)
- `SANPHAM_KH` (**<u>MASP</u>**, TENSP, LOAISP, XEP_HANG, MADT)
- `GIAINGAN` (**<u>MAGN</u>**, MADT, NGAYGN, SOTIEN_GN, NOIDUNG)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết câu lệnh SQL tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra số tiền giải ngân (`SOTIEN_GN > 0`) trong bảng `GIAINGAN` và ngày kết thúc đề tài phải sau ngày bắt đầu (`NGAYKT > NGAYBD`) trong bảng `DETAI`. Cả hai thuộc tính đều không được mang giá trị `NULL`.

b. (0.75 điểm) Viết câu lệnh SQL cập nhật tăng 15% mức lương (`LUONG = LUONG * 1.15`) cho các giảng viên có học vị (`HOCVI`) là 'Tiến sĩ' công tác tại khoa viện có tên (`TENKV`) là 'Viện Công Nghệ Thông Tin'.

### 2.2. Viết các biểu thức Đại số quan hệ (6.0 điểm)
Sinh viên sử dụng các ký hiệu phép toán chuẩn của Đại số quan hệ: $\sigma$ (chọn), $\pi$ (chiếu), $\bowtie$ (kết tự nhiên), $\bowtie_{\theta}$ (kết có điều kiện), $\leftouterjoin$ (kết ngoài trái), $\rho$ (đổi tên), $\gamma$ (gom nhóm & hàm gộp), $\div$ (chia). Mỗi câu cần nêu rõ các bước trung gian $E_1, E_2, \dots$ và biểu thức kết quả $\text{KQ}$.

a. (1.0 điểm) Liệt kê danh sách các đề tài NCKH (**MADT**, **TENDT**, **KINHPHI**, **NGAYBD**) thuộc cấp quản lý 'Cấp Nhà nước' có tổng kinh phí từ 1.000.000.000 VNĐ (1 tỷ đồng) trở lên ($\ge 1000000000$).

b. (1.0 điểm) Cho biết danh sách các sản phẩm khoa học (**MASP**, **TENSP**, **LOAISP**, **XEP_HANG**) được công bố từ các đề tài do giảng viên mang mã `MAGV = 'GV01'` làm chủ nhiệm đề tài.

c. (1.0 điểm) Liệt kê thông tin tất cả các khoa viện (**MAKV**, **TENKV**) cùng mã đề tài (**MADT**), tên đề tài (**TENDT**) do giảng viên trực thuộc khoa viện đó làm chủ nhiệm (nếu khoa viện mới mở chưa có giảng viên chủ nhiệm đề tài nào thì thông tin đề tài mang giá trị `NULL`).

d. (1.0 điểm) Tính tổng kinh phí đã giải ngân thực tế (**TONG_GIAINGAN** = SUM(SOTIEN_GN)) của từng đề tài (**MADT**, **TENDT**) đã được giải ngân trong năm 2024.

e. (1.0 điểm) Tìm các giảng viên (**MAGV**, **HOTEN**, **HOCVI**) đã từng tham gia thực hiện **tất cả** các đề tài NCKH thuộc cấp quản lý 'Cấp Nhà nước' của trường.

f. (1.0 điểm) Tìm đề tài NCKH (**MADT**, **TENDT**, **CAP_QUANLY**) có tổng số lượng sản phẩm khoa học đạt xếp hạng 'Q1' công bố nhiều nhất (bảo toàn tất cả các đề tài nếu có nhiều đề tài cùng đạt số lượng sản phẩm cao nhất).

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 14**
*Cán bộ coi thi không giải thích gì thêm.*
