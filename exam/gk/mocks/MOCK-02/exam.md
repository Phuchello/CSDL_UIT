# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 02 (MOCK-02)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)

Khu dân cư phức hợp cao tầng cần xây dựng cơ sở dữ liệu quản lý công tác bảo trì và kiểm định an toàn phòng cháy chữa cháy (PCCC) cho toàn bộ các tòa chung cư. Quy trình nghiệp vụ được mô tả chi tiết như sau:

1. Mỗi tòa nhà (**`TOANHA`**) trong khu chung cư có một mã tòa nhà duy nhất (**`MATN`**), tên gọi tòa nhà (**`TENTN`**), tổng số tầng (**`SOTANG`**), và địa chỉ cụ thể (**`DIACHI`**). Mỗi tòa nhà bắt buộc có ít nhất một hoặc nhiều tầng (**`TANG`**).
2. Mỗi tầng (**`TANG`**) thuộc về đúng một tòa nhà xác định, được định danh duy nhất bởi mã tầng (**`MATANG`**). Mỗi tầng ghi nhận số thứ tự tầng (**`STTTANG`**, là số nguyên $\ge 1$) và diện tích sàn (**`DIENTICH`**, tính theo $m^2$).
3. Trên mỗi tầng có thể bố trí các căn hộ (**`CANHO`**). Mỗi căn hộ được cấp một mã căn hộ duy nhất (**`MACANHO`**), số hiệu phòng (**`SOCANHO`**), diện tích phòng (**`DIENTICH`**), số lượng phòng ngủ (**`SOPHONGNGU`**) và trạng thái sử dụng hiện tại (**`TRANGTHAI`** - ví dụ: 'Đang ở', 'Trống', 'Đang sửa chữa'). Một tầng kỹ thuật hoặc tầng thương mại có thể không bố trí căn hộ nào. Mỗi căn hộ chỉ thuộc về đúng một tầng.
4. Để đảm bảo an toàn PCCC theo quy chuẩn, tại các tầng được lắp đặt nhiều loại trang thiết bị PCCC (**`THIETBI_PCCC`**). Mỗi thiết bị PCCC có mã thiết bị duy nhất (**`MATB`**), tên thiết bị (**`TENTB`**), phân loại thiết bị (**`LOAITB`** - ví dụ: 'Bình chữa cháy bột', 'Đầu báo khói', 'Họng nước cứu hỏa', 'Còi báo động'), vị trí lắp đặt cụ thể (**`VITRI_LAPDAT`**), ngày lắp đặt đưa vào sử dụng (**`NGAYLAP`**), và hạn sử dụng/kiểm định kế tiếp (**`HANSUDUNG`**). Mỗi thiết bị PCCC được bố trí cố định tại đúng một tầng xác định. Một tầng có thể bố trí nhiều thiết bị hoặc chưa lắp đặt thiết bị nào.
5. Ban Quản trị định kỳ tổ chức các đợt kiểm tra an toàn PCCC (**`DOT_KIEMTRA`**). Mỗi đợt kiểm tra có mã đợt duy nhất (**`MADOT`**), ngày tiến hành kiểm tra (**`NGAYKT`**), họ tên người chịu trách nhiệm kiểm tra (**`NGUOIKT`**), và kết luận chung của đợt kiểm tra (**`KETLUAN_CHUNG`** - ví dụ: 'Đạt chuẩn', 'Cần bảo dưỡng', 'Khắc phục ngay').
6. Trong mỗi đợt kiểm tra, cán bộ kỹ thuật kiểm tra thực tế nhiều thiết bị PCCC khác nhau, và một thiết bị PCCC có thể được kiểm tra qua nhiều đợt kiểm tra định kỳ theo thời gian. Mỗi khi kiểm tra một thiết bị trong một đợt nhất định, hệ thống cần lưu lại tình trạng hoạt động thực tế (**`TINHTRANG`** - ví dụ: 'Bình thường', 'Hết hạn', 'Hỏng áp suất', 'Mất niêm phong') và các ghi chú khắc phục (**`GHICHU`**).

**Yêu cầu:**
1. *(1.50 điểm)* Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số $(min, max)$ hai phía. Vẽ mô hình Thực thể – Mối kết hợp (ERD).
2. *(1.00 điểm)* Ánh xạ mô hình ERD sang Lược đồ cơ sở dữ liệu quan hệ, chỉ rõ Khóa chính (PK) bằng cách gạch chân và Khóa ngoại (FK) kèm bảng tham chiếu.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu quan hệ **Quản Lý Hệ Thống Phòng Cháy Chữa Cháy Chung Cư** gồm 6 quan hệ chuẩn hóa sau (các thuộc tính khóa chính được in đậm và gạch chân):

- `TOANHA` (**`MATN`**, `TENTN`, `SOTANG`, `DIACHI`)
- `TANG` (**`MATANG`**, `MATN`, `STTTANG`, `DIENTICH`)
- `CANHO` (**`MACANHO`**, `MATANG`, `SOCANHO`, `DIENTICH`, `SOPHONGNGU`, `TRANGTHAI`)
- `THIETBI_PCCC` (**`MATB`**, `MATANG`, `TENTB`, `LOAITB`, `VITRI_LAPDAT`, `NGAYLAP`, `HANSUDUNG`)
- `DOT_KIEMTRA` (**`MADOT`**, `NGAYKT`, `NGUOIKT`, `KETLUAN_CHUNG`)
- `CT_KIEMTRA` (**`MADOT`**, **`MATB`**, `TINHTRANG`, `GHICHU`)

### 1. Viết các câu lệnh SQL (1.5 điểm)

a. *(0.75 điểm)* Tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra thuộc tính `DIENTICH` trong quan hệ `CANHO` phải là số thực dương ($> 0$), và thuộc tính `HANSUDUNG` trong quan hệ `THIETBI_PCCC` phải lớn hơn hoặc bằng ngày lắp đặt (`HANSUDUNG >= NGAYLAP`). Cả hai thuộc tính đều không được mang giá trị `NULL`.

b. *(0.75 điểm)* Viết câu lệnh SQL cập nhật tình trạng (`TINHTRANG`) trong quan hệ `CT_KIEMTRA` thành 'Hết hạn' cho tất cả các thiết bị được kiểm tra trong đợt kiểm tra có mã `'DKT01'` mà thiết bị đó có hạn sử dụng (`HANSUDUNG`) trước ngày `'01/06/2025'`.

### 2. Viết các biểu thức Đại số quan hệ (6.0 điểm)

a. *(1.0 điểm)* Liệt kê danh sách các thiết bị PCCC (`MATB`, `TENTB`, `VITRI_LAPDAT`, `HANSUDUNG`) thuộc loại 'Bình chữa cháy bột' có hạn sử dụng (`HANSUDUNG`) trong năm 2025.

b. *(1.0 điểm)* Cho biết danh sách các căn hộ (`MACANHO`, `SOCANHO`, `DIENTICH`) thuộc tòa nhà có tên 'Ruby Tower' (`TENTN = 'Ruby Tower'`) và nằm ở các tầng có số thứ tự tầng (`STTTANG`) từ tầng 10 trở lên.

c. *(1.0 điểm)* Liệt kê thông tin tất cả các tầng thuộc tòa nhà `'TN01'` (`MATANG`, `STTTANG`) và danh sách các mã thiết bị PCCC (`MATB`), tên thiết bị (`TENTB`) được bố trí tại tầng đó **nếu có** (những tầng chưa lắp thiết bị PCCC vẫn phải hiển thị thông tin tầng, các cột thiết bị mang giá trị `NULL`).

d. *(1.0 điểm)* Tính tổng số lượng thiết bị PCCC (`TONG_THIETBI`) được bố trí tại mỗi tòa nhà. Thông tin hiển thị gồm: `MATN`, `TENTN`, `TONG_THIETBI`.

e. *(1.0 điểm)* Tìm các đợt kiểm tra (`MADOT`, `NGAYKT`, `NGUOIKT`) đã tiến hành kiểm tra **tất cả** các thiết bị PCCC thuộc loại 'Đầu báo khói' (`LOAITB = 'Đầu báo khói'`).

f. *(1.0 điểm)* Tìm thông tin tòa nhà (`MATN`, `TENTN`, `SOTANG`) có số lượng căn hộ nhiều nhất trong khu chung cư (bảo toàn tất cả các tòa nhà nếu có nhiều tòa cùng đạt số lượng căn hộ lớn nhất).

---

**HẾT ĐỀ THI MÔ PHỎNG SỐ 02**
*Cán bộ coi thi không giải thích gì thêm.*
