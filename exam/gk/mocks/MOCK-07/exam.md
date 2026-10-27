# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 07 (MOCK-07)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)

Đọc kỹ bài toán quản lý thư viện trung tâm và lưu hành tài liệu học thuật tại một trường đại học:

Thư viện trung tâm trường đại học cần xây dựng cơ sở dữ liệu quản lý các khoa viện đào tạo, độc giả, tài liệu sách in và các lượt mượn trả sách. Trường có nhiều khoa viện; mỗi khoa viện có một mã khoa viện duy nhất, tên khoa viện và năm thành lập. Độc giả của thư viện gồm sinh viên và giảng viên thuộc các khoa viện. Mỗi độc giả có mã độc giả duy nhất, họ tên, ngày sinh, loại độc giả ('Sinh viên' hoặc 'Giảng viên') và trực thuộc duy nhất một khoa viện.

Kho tài liệu của thư viện gồm nhiều đầu sách in phục vụ nghiên cứu và giảng dạy. Mỗi cuốn sách có mã sách duy nhất, tên sách, tác giả, nhà xuất bản, năm xuất bản và số lượng hiện còn tồn trong kho. Hoạt động cho mượn sách được phụ trách bởi các cán bộ thủ thư. Mỗi thủ thư có mã thủ thư duy nhất, họ tên và số điện thoại liên lạc.

Mỗi khi độc giả mượn sách, thủ thư tiếp nhận và lập một phiếu mượn. Phiếu mượn có mã phiếu mượn duy nhất, ngày mượn, ngày hẹn trả, do đúng một thủ thư phụ trách lập cho đúng một độc giả, và có trạng thái phiếu mượn ('Đang mượn' hoặc 'Đã đóng'). Trong một lần mượn, độc giả có thể mượn một hoặc nhiều cuốn sách khác nhau. Mỗi chi tiết mượn sách ghi nhận mã phiếu mượn, mã sách, ngày trả thực tế (nếu độc giả chưa trả thì mang giá trị rỗng/NULL) và số tiền phạt phát sinh nếu làm hư hỏng hoặc trễ hạn (mặc định là 0 nếu không có phạt).

**Yêu cầu:**
1. (1.50 điểm) Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số (min, max) hai phía giữa các tập thực thể. Vẽ mô hình Thực thể – Mối kết hợp (ERD).
2. (1.00 điểm) Ánh xạ mô hình ERD đã thiết kế sang Lược đồ cơ sở dữ liệu quan hệ hoàn chỉnh. Chỉ rõ Khóa chính (PK) gạch dưới và Khóa ngoại (FK) chỉ rõ bảng tham chiếu.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu quan hệ 'Quản Lý Thư Viện Đại Học & Mượn Trả Sách' được chuyển giao từ Câu 1:
- `KHOAVIEN` (**<u>MAKV</u>**, TENKV, NAMTL)
- `DOCGIA` (**<u>MADG</u>**, HOTEN, NGAYSINH, LOAIDG, MAKV)
- `SACH` (**<u>MASACH</u>**, TENSACH, TACGIA, NXB, NAMXB, SOLUONGTON)
- `THUTHU` (**<u>MATT</u>**, HOTEN, SODT)
- `PHIEUMUON` (**<u>MAPM</u>**, NGAYMUON, HANTRA, MADG, MATT, TRANGTHAI)
- `CHITIET_MUON` (**<u>MAPM</u>**, **<u>MASACH</u>**, NGAYTRA, TIENPHAT)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)
a. (0.75 điểm) Viết câu lệnh SQL tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra số lượng tồn (`SOLUONGTON`) trong bảng `SACH` phải lớn hơn hoặc bằng 0 ($\ge 0$), và số tiền phạt (`TIENPHAT`) trong bảng `CHITIET_MUON` phải lớn hơn hoặc bằng 0 ($\ge 0$). Cả hai thuộc tính đều không được mang giá trị `NULL`.

b. (0.75 điểm) Viết câu lệnh SQL cập nhật gia hạn ngày hẹn trả (`HANTRA`) thêm 15 ngày cho tất cả các phiếu mượn (`PHIEUMUON`) của những độc giả có loại độc giả (`LOAIDG`) là 'Giảng viên' và có ngày mượn sách trong tháng 10 năm 2024.

### 2.2. Viết các biểu thức Đại số quan hệ (6.0 điểm)
Sinh viên sử dụng các ký hiệu phép toán chuẩn của Đại số quan hệ: $\sigma$ (chọn), $\pi$ (chiếu), $\bowtie$ (kết tự nhiên), $\bowtie_{\theta}$ (kết có điều kiện), $\leftouterjoin$ (kết ngoài trái), $\rho$ (đổi tên), $\gamma$ (gom nhóm & hàm gộp), $\div$ (chia). Mỗi câu cần nêu rõ các bước trung gian $E_1, E_2, \dots$ và biểu thức kết quả $\text{KQ}$.

a. (1.0 điểm) Liệt kê danh sách các độc giả (**MADG**, **HOTEN**, **NGAYSINH**) có loại độc giả là 'Sinh viên' và trực thuộc khoa viện có tên (`TENKV`) là 'Khoa học Máy tính'.

b. (1.0 điểm) Cho biết danh sách các cuốn sách (**MASACH**, **TENSACH**, **NXB**) do nhà xuất bản 'NXB Giáo Dục' ấn hành đã được mượn bởi độc giả có mã độc giả `MADG = 'DG01'`.

c. (1.0 điểm) Liệt kê thông tin tất cả các khoa viện (**MAKV**, **TENKV**) và danh sách mã độc giả (**MADG**), họ tên độc giả (**HOTEN**) thuộc khoa viện đó (nếu khoa viện mới thành lập chưa có độc giả nào đăng ký thì thông tin độc giả mang giá trị `NULL`).

d. (1.0 điểm) Tính tổng số tiền phạt phát sinh (**TONG_TIEN_PHAT**) theo từng độc giả (**MADG**, **HOTEN**) đối với các lượt mượn trong năm 2024 có phát sinh tiền phạt (`TIENPHAT > 0`).

e. (1.0 điểm) Tìm các độc giả (**MADG**, **HOTEN**, **LOAIDG**) đã từng mượn **tất cả** các cuốn sách của tác giả 'Nguyễn Nhật Ánh'.

f. (1.0 điểm) Tìm cuốn sách (**MASACH**, **TENSACH**, **TACGIA**) có số lượt mượn (**SO_LUOT_MUON**) nhiều nhất trong năm 2024 (bảo toàn tất cả các cuốn sách nếu có nhiều cuốn cùng đạt số lượt mượn cao nhất).

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 07**
*Cán bộ coi thi không giải thích gì thêm.*
