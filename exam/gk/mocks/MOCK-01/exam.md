# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 01 (MOCK-01)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu  
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series  

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)

Để phục vụ công tác tiêm chủng phòng dịch trên địa bàn thành phố, Sở Y tế cần xây dựng cơ sở dữ liệu quản lý việc tiếp nhận và phân phối vắc-xin tại các điểm tiêm chủng, cụ thể như sau:

- Mỗi **Trung tâm Y tế** (`TRUNGTAM_YTE`) có mã trung tâm (`MaTT`) để phân biệt giữa các trung tâm, có tên trung tâm (`TenTT`), và địa chỉ quận/huyện (`DiaChiQuan`).
- Các **Nhà cung cấp** (`NHA_CUNGCAP`) cung ứng vắc-xin cần lưu trữ: mã nhà cung cấp (`MaNCC`), tên nhà cung cấp (`TenNCC`), quốc gia (`QuocGia`), và số điện thoại liên hệ (`SDT`).
- Mỗi **Lô vắc-xin** (`LO_VACXIN`) nhập kho được ghi nhận: mã lô (`MaLo`) duy nhất, tên lô (`TenLo`), tên loại vắc-xin (`TenVacxin`), ngày sản xuất (`NgaySX`), hạn sử dụng (`HSD`), số liều nhập (`SoLieuNhap`), và đơn giá mỗi liều (`DonGia`). Mỗi lô vắc-xin do duy nhất một nhà cung cấp cung ứng; một nhà cung cấp có thể cung cấp nhiều lô vắc-xin khác nhau.
- Các **Điểm tiêm chủng** (`DIEM_TIEM`) trực thuộc một Trung tâm Y tế quản lý gồm các thông tin: mã điểm tiêm (`MaDT`), tên điểm tiêm (`TenDT`), địa điểm cụ thể (`DiaDiem`), và sức chứa tối đa người tiêm trong ngày (`SucChua`). Mỗi điểm tiêm chỉ trực thuộc duy nhất một trung tâm y tế; một trung tâm y tế quản lý nhiều điểm tiêm khác nhau.
- Công tác phân phối vắc-xin từ các lô đến điểm tiêm được thực hiện qua các đợt **Phân phối** (`PHAN_PHOI`). Thông tin lưu trữ gồm: ngày phân phối (`NgayPP`), số liều phân phối (`SoLieuPP`), và trạng thái tiếp nhận (`TrangThai` nhận giá trị 1 nếu đã nhận, 0 nếu đang chuyển). Một lô vắc-xin có thể phân phối cho nhiều điểm tiêm; một điểm tiêm có thể tiếp nhận vắc-xin từ nhiều lô khác nhau vào các ngày khác nhau.
- Mỗi **Nhân viên y tế** (`NHAN_VIEN`) có mã nhân viên (`MaNV`), họ tên (`HoTen`), chuyên môn y tế (`ChuyenMon`), và số điện thoại (`SDT`). Mỗi nhân viên chỉ thuộc biên chế chính thức của một trung tâm y tế. Nhân viên được điều động tham gia trực tại các điểm tiêm trong các ca trực (`TRUC_CA`) cụ thể, ghi nhận ngày trực (`NgayTruc`) và vai trò trực (`VaiTroTruc`).

**Yêu cầu:**
1. Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số $(min, max)$ hai phía. Vẽ mô hình Thực thể – Mối kết hợp (ERD). *(1.5 điểm)*
2. Ánh xạ mô hình ERD trên sang Lược đồ cơ sở dữ liệu quan hệ, chỉ rõ các Khóa chính (gạch chân) và Khóa ngoại (ký hiệu mũi tên hoặc chú thích rõ). *(1.0 điểm)*

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu "Quản lý Cung ứng & Phân phối Vắc-xin" gồm các quan hệ sau (thuộc tính gạch chân là khóa chính):

- `NHACUNGCAP` (**`MANCC`**, `TENNCC`, `QUOCGIA`, `SDT`)  
  *Tân từ:* Thông tin nhà cung cấp vắc-xin.
- `LOVACXIN` (**`MALO`**, `TENLO`, `TENKVACXIN`, `MANCC`, `NGAYSX`, `HSD`, `SOLIEU`, `DONGIA`)  
  *Tân từ:* Thông tin lô vắc-xin nhập kho. `MANCC` là khóa ngoại trỏ về `NHACUNGCAP`.
- `DIEMTIEM` (**`MADT`**, `TENDT`, `QUAN`, `SUCCHUA`, `MATRP`)  
  *Tân từ:* Điểm tiêm chủng lưu động. `MATRP` là mã bác sĩ trưởng điểm tiêm phụ trách.
- `BACSI` (**`MABS`**, `HOTEN`, `CHUYENKHOA`, `SDT`, `MADT`)  
  *Tân từ:* Danh sách bác sĩ tham gia tiêm chủng. `MADT` là điểm tiêm bác sĩ đang trực.
- `PHIEUXUAT` (**`MAPX`**, `NGAYXUAT`, `MADT`, `TRANGTHAI`)  
  *Tân từ:* Phiếu xuất vắc-xin đến điểm tiêm. `MADT` là khóa ngoại trỏ về `DIEMTIEM`.
- `CTPX` (**`MAPX`**, **`MALO`**, `SOLIEUXUAT`)  
  *Tân từ:* Chi tiết số liều xuất theo từng lô vắc-xin trong mỗi phiếu xuất.

### 1. Viết các câu lệnh SQL (1.5 điểm)
a. *(0.75 điểm)* Tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra thuộc tính `SOLIEUXUAT` trong quan hệ `CTPX` phải là số nguyên dương ($> 0$), và thuộc tính `TRANGTHAI` trong quan hệ `PHIEUXUAT` chỉ nhận một trong hai giá trị là `0` hoặc `1`.  
b. *(0.75 điểm)* Viết câu lệnh SQL cập nhật (`UPDATE`) tăng giá đơn vị (`DONGIA`) thêm 10% đối với các lô vắc-xin có hạn sử dụng (`HSD`) trong năm 2025 do nhà cung cấp có tên là 'AstraZeneca' cung cấp.

### 2. Viết các biểu thức Đại số quan hệ (6.0 điểm - mỗi câu 1.0 điểm)
a. *(1.0 điểm)* Liệt kê thông tin các lô vắc-xin (`MALO`, `TENLO`, `SOLIEU`, `DONGIA`) có tên vắc-xin là 'Pfizer-BioNTech' và được sản xuất trong năm 2024.  
b. *(1.0 điểm)* Cho biết danh sách các điểm tiêm (`MADT`, `TENDT`, `QUAN`) đã tiếp nhận các phiếu xuất vắc-xin vào ngày '15/10/2024'.  
c. *(1.0 điểm)* Liệt kê thông tin các điểm tiêm ở quận 'Bình Thạnh' (`MADT`, `TENDT`) và họ tên bác sĩ (`HOTEN`) đang phụ trách tại điểm tiêm đó **nếu có**.  
d. *(1.0 điểm)* Tính tổng số liều vắc-xin xuất (`SOLIEUXUAT`) theo từng điểm tiêm (`MADT`) trong tháng 10 năm 2024. Thông tin hiển thị gồm: `MADT`, `TONGLIEU`.  
e. *(1.0 điểm)* Tìm các điểm tiêm (`MADT`, `TENDT`) đã tiếp nhận **tất cả** các lô vắc-xin của nhà cung cấp có tên là 'Moderna' (`TENNCC = 'Moderna'`).  
f. *(1.0 điểm)* Cho biết điểm tiêm nào (`MADT`, `TENDT`) có sức chứa (`SUCCHUA`) lớn nhất trong số các điểm tiêm thuộc quận 'Thủ Đức'.

---
**HẾT ĐỀ THI MÔ PHỎNG SỐ 01**  
*Cán bộ coi thi không giải thích gì thêm.*