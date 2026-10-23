# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 01 (MOCK-01)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thẩm định:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)

Để phục vụ công tác tiêm chủng phòng dịch trên địa bàn thành phố, Sở Y tế cần xây dựng cơ sở dữ liệu quản lý việc tiếp nhận, phân phối vắc-xin và điều động nhân sự tại các điểm tiêm chủng, cụ thể như sau:

- Các **Nhà cung cấp** (`NHACUNGCAP`) cung ứng vắc-xin cần lưu trữ: mã nhà cung cấp (`MANCC`) định danh duy nhất, tên nhà cung cấp (`TENNCC`), quốc gia xuất xứ (`QUOCGIA`), và số điện thoại liên hệ (`SDT`).
- Mỗi **Lô vắc-xin** (`LOVACXIN`) nhập kho được ghi nhận: mã lô (`MALO`) định danh duy nhất, tên lô (`TENLO`), tên loại vắc-xin (`TENVACXIN`), ngày sản xuất (`NGAYSX`), hạn sử dụng (`HSD`), số lượng liều nhập (`SOLIEU`), và đơn giá mỗi liều (`DONGIA`). Mỗi lô vắc-xin do duy nhất một nhà cung cấp cung ứng; một nhà cung cấp có thể cung ứng nhiều lô vắc-xin khác nhau (hoặc là nhà cung cấp mới ký hợp đồng, chưa nhập lô nào).
- Các **Điểm tiêm chủng** (`DIEMTIEM`) gồm các thông tin: mã điểm tiêm (`MADT`) định danh duy nhất, tên điểm tiêm (`TENDT`), địa chỉ cụ thể (`DIACHI`), quận phụ trách (`QUAN`), và sức chứa tối đa người tiêm trong ngày (`SUCCHUA`).
- Mỗi **Nhân viên y tế** (`NHANVIEN`) tham gia công tác tiêm chủng (gồm bác sĩ, điều dưỡng) có: mã nhân viên (`MANV`) định danh duy nhất, họ tên (`HOTEN`), chuyên môn y tế (`CHUYENMON`), và số điện thoại (`SDT`). Mỗi nhân viên được điều động công tác tại tối đa một điểm tiêm (hoặc là nhân viên dự bị chưa phân công); một điểm tiêm có thể có nhiều nhân viên y tế công tác (hoặc chưa được bố trí nhân viên).
- Công tác phân phối vắc-xin đến các điểm tiêm được quản lý thông qua các **Phiếu xuất** (`PHIEUXUAT`). Mỗi phiếu xuất có mã phiếu (`MAPX`) định danh duy nhất, ngày xuất (`NGAYXUAT`), và trạng thái tiếp nhận (`TRANGTHAI`: nhận giá trị 1 nếu điểm tiêm đã tiếp nhận thực tế, nhận giá trị 0 nếu đang trên đường vận chuyển). Mỗi phiếu xuất được điều phối đến duy nhất một điểm tiêm; một điểm tiêm có thể tiếp nhận nhiều phiếu xuất khác nhau (hoặc chưa tiếp nhận phiếu xuất nào).
- Mỗi phiếu xuất có thể gồm nhiều lô vắc-xin khác nhau (tối thiểu một lô); mỗi lô vắc-xin có thể được xuất trong nhiều phiếu xuất khác nhau (hoặc lưu kho chưa xuất đợt nào). Trong mỗi phiếu xuất, với mỗi lô vắc-xin cụ thể, cần lưu trữ số liều thực tế được xuất (`SOLIEUXUAT`).

**Yêu cầu:**
1. Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số $(min, max)$ hai phía. Vẽ mô hình Thực thể – Mối kết hợp (ERD). *(1.5 điểm)*
2. Ánh xạ mô hình ERD trên sang Lược đồ cơ sở dữ liệu quan hệ, chỉ rõ các Khóa chính (gạch chân) và Khóa ngoại (ký hiệu mũi tên hoặc chú thích rõ). *(1.0 điểm)*

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu "Quản lý Cung ứng & Phân phối Vắc-xin" gồm các quan hệ chuẩn hóa sau (thuộc tính gạch chân là khóa chính):

- `NHACUNGCAP` (**`MANCC`**, `TENNCC`, `QUOCGIA`, `SDT`)
  *Tân từ:* Danh sách nhà cung cấp vắc-xin.
- `LOVACXIN` (**`MALO`**, `TENLO`, `TENVACXIN`, `NGAYSX`, `HSD`, `SOLIEU`, `DONGIA`, `MANCC`)
  *Tân từ:* Lô vắc-xin nhập kho. `MANCC` là khóa ngoại tham chiếu đến `NHACUNGCAP(MANCC)`.
- `DIEMTIEM` (**`MADT`**, `TENDT`, `DIACHI`, `QUAN`, `SUCCHUA`)
  *Tân từ:* Điểm tiêm chủng lưu động hoặc cố định.
- `NHANVIEN` (**`MANV`**, `HOTEN`, `CHUYENMON`, `SDT`, `MADT`)
  *Tân từ:* Nhân viên y tế phục vụ tiêm chủng. `MADT` là khóa ngoại tham chiếu đến `DIEMTIEM(MADT)`.
- `PHIEUXUAT` (**`MAPX`**, `NGAYXUAT`, `TRANGTHAI`, `MADT`)
  *Tân từ:* Phiếu xuất điều phối vắc-xin. `MADT` là khóa ngoại tham chiếu đến `DIEMTIEM(MADT)`. `TRANGTHAI` mang giá trị 1 (đã nhận) hoặc 0 (đang chuyển).
- `CTPX` (**`MAPX`**, **`MALO`**, `SOLIEUXUAT`)
  *Tân từ:* Chi tiết số liều xuất theo từng lô vắc-xin. `MAPX` tham chiếu `PHIEUXUAT(MAPX)`, `MALO` tham chiếu `LOVACXIN(MALO)`.

### 1. Viết các câu lệnh SQL (1.5 điểm)
a. *(0.75 điểm)* Tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra thuộc tính `SOLIEUXUAT` trong quan hệ `CTPX` phải là số nguyên dương ($> 0$), và thuộc tính `TRANGTHAI` trong quan hệ `PHIEUXUAT` chỉ nhận một trong hai giá trị là `0` hoặc `1`. Cả hai thuộc tính đều không được mang giá trị `NULL`.
b. *(0.75 điểm)* Viết câu lệnh SQL cập nhật (`UPDATE`) tăng giá đơn vị (`DONGIA`) thêm 10% đối với các lô vắc-xin có hạn sử dụng (`HSD`) trong năm 2025 do nhà cung cấp có tên là 'AstraZeneca' cung cấp.

### 2. Viết các biểu thức Đại số quan hệ (6.0 điểm - mỗi câu 1.0 điểm)
a. *(1.0 điểm)* Liệt kê thông tin các lô vắc-xin (`MALO`, `TENLO`, `SOLIEU`, `DONGIA`) có tên loại vắc-xin là 'Pfizer-BioNTech' và được sản xuất trong năm 2024.
b. *(1.0 điểm)* Cho biết danh sách các điểm tiêm (`MADT`, `TENDT`, `QUAN`) đã tiếp nhận (`TRANGTHAI = 1`) các phiếu xuất vắc-xin vào ngày '15/10/2024'.
c. *(1.0 điểm)* Liệt kê thông tin các điểm tiêm ở quận 'Bình Thạnh' (`MADT`, `TENDT`) và họ tên nhân viên y tế (`HOTEN`) đang công tác tại điểm tiêm đó **nếu có**.
d. *(1.0 điểm)* Tính tổng số liều vắc-xin đã tiếp nhận (`SOLIEUXUAT`, với `TRANGTHAI = 1`) theo từng điểm tiêm (`MADT`) trong tháng 10 năm 2024. Thông tin hiển thị gồm: `MADT`, `TONGLIEU`.
e. *(1.0 điểm)* Tìm các điểm tiêm (`MADT`, `TENDT`) đã tiếp nhận thực tế (`TRANGTHAI = 1`) **tất cả** các lô vắc-xin của nhà cung cấp có tên là 'Moderna' (`TENNCC = 'Moderna'`).
f. *(1.0 điểm)* Cho biết điểm tiêm nào (`MADT`, `TENDT`) có sức chứa (`SUCCHUA`) lớn nhất trong số các điểm tiêm thuộc quận 'Thủ Đức' (xét cả trường hợp có nhiều điểm tiêm đồng hạng lớn nhất).

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 01**
*Cán bộ coi thi không giải thích gì thêm.*
