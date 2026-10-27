# ĐỀ THI GIỮA KỲ MÔ PHỎNG SỐ 03 (MOCK-03)
### MÔN HỌC: IT004 — CƠ SỞ DỮ LIỆU
**Thời gian làm bài:** 75 phút | **Hình thức:** Tự luận | **Tài liệu:** KHÔNG sử dụng tài liệu
**Biên soạn & Thiết kế:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.0 ĐIỂM)

Ban Chỉ huy Phòng chống thiên tai & Tìm kiếm cứu nạn một tỉnh miền Trung cần xây dựng cơ sở dữ liệu để quản lý công tác tiếp nhận và phân bổ tiền cứu trợ cho các hộ dân bị thiệt hại do bão lũ. Quy trình nghiệp vụ được mô tả cụ thể như sau:

1. Mỗi xã (**`XA`**) được định danh bởi một mã xã duy nhất (**`MAXA`**), cùng tên xã (**`TENXA`**) và huyện trực thuộc (**`HUYEN`**). Mỗi xã quản lý một hoặc nhiều hộ dân sinh sống trên địa bàn.
2. Mỗi hộ dân (**`HO_DAN`**) có một mã hộ dân duy nhất (**`MAHO`**), họ tên chủ hộ (**`CHUHO`**), số nhân khẩu (**`SONKHAU`**, số nguyên $\ge 1$), và mức độ thiệt hại (**`MUCDO_THIETHAI`** - nhận một trong các giá trị: 'Nhẹ', 'Trung bình', 'Nặng'). Mỗi hộ dân chỉ thuộc về đúng một xã xác định.
3. Các nhà hảo tâm (**`NHA_HAOTAM`**) đóng góp tài chính cho công tác cứu trợ. Mỗi nhà hảo tâm có mã duy nhất (**`MANHT`**), tên nhà hảo tâm (**`TENNHT`**), số điện thoại (**`SDT`**), và phân loại loại hình (**`LOAIHINH`** - ví dụ: 'Cá nhân', 'Doanh nghiệp', 'Tổ chức thiện nguyện').
4. Ban Chỉ huy tổ chức các đợt cứu trợ (**`DOT_CUUTRO`**). Mỗi đợt cứu trợ có một mã đợt duy nhất (**`MADOT`**), tên đợt cứu trợ (**`TENDOT`**), ngày bắt đầu (**`NGAYBD`**), và ngày kết thúc (**`NGAYKT`**).
5. Các nhà hảo tâm thực hiện đóng góp tiền ủng hộ (**`DONG_GOP`**) cho các đợt cứu trợ. Mỗi lần đóng góp có một mã đóng góp duy nhất (**`MADG`**), ghi nhận nhà hảo tâm đóng góp, đợt cứu trợ nhận đóng góp, ngày đóng góp (**`NGAYDG`**), và số tiền đóng góp (**`SOTIEN`**, tính theo VNĐ, $> 0$). Một nhà hảo tâm có thể đóng góp nhiều lần cho cùng một đợt hoặc cho nhiều đợt khác nhau.
6. Ban Chỉ huy lập các phiếu nhận cứu trợ (**`PHIEU_NHAN`**) để phân bổ tiền trực tiếp cho các hộ dân. Mỗi phiếu nhận có mã phiếu duy nhất (**`MAPHIEU`**), ghi nhận hộ dân được nhận tiền, thuộc đợt cứu trợ nào, ngày nhận tiền (**`NGAYNHAN`**), và số tiền cứu trợ thực tế (**`SOTIEN`**, tính theo VNĐ, $> 0$). Trong mỗi đợt cứu trợ, một hộ dân có thể nhận một phiếu hỗ trợ.

**Yêu cầu:**
1. *(1.20 điểm)* Xác định các tập thực thể, thuộc tính khóa, các mối kết hợp và bản số $(min, max)$ hai phía. Vẽ mô hình Thực thể – Mối kết hợp (ERD).
2. *(0.80 điểm)* Ánh xạ mô hình ERD sang Lược đồ cơ sở dữ liệu quan hệ, chỉ rõ Khóa chính (PK) bằng cách gạch chân và Khóa ngoại (FK) kèm bảng tham chiếu.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (8.0 ĐIỂM)

Cho Lược đồ cơ sở dữ liệu quan hệ **Quản Lý Tiếp Nhận & Phân Bổ Tiền Cứu Trợ Bão Lũ** gồm 6 quan hệ chuẩn hóa sau (các thuộc tính khóa chính được in đậm và gạch chân):

- `XA` (**`MAXA`**, `TENXA`, `HUYEN`)
- `HO_DAN` (**`MAHO`**, `CHUHO`, `SONKHAU`, `MUCDO_THIETHAI`, `MAXA`)
- `NHA_HAOTAM` (**`MANHT`**, `TENNHT`, `SDT`, `LOAIHINH`)
- `DOT_CUUTRO` (**`MADOT`**, `TENDOT`, `NGAYBD`, `NGAYKT`)
- `DONG_GOP` (**`MADG`**, `MANHT`, `MADOT`, `NGAYDG`, `SOTIEN`)
- `PHIEU_NHAN` (**`MAPHIEU`**, `MAHO`, `MADOT`, `NGAYNHAN`, `SOTIEN`)

### 1. Viết các câu lệnh SQL (1.5 điểm)

a. *(0.75 điểm)* Tạo ràng buộc toàn vẹn miền giá trị (CHECK constraint) kiểm tra thuộc tính `SOTIEN` trong quan hệ `PHIEU_NHAN` phải lớn hơn 0 ($> 0$), và thuộc tính `NGAYKT` trong quan hệ `DOT_CUUTRO` phải lớn hơn hoặc bằng ngày bắt đầu (`NGAYKT >= NGAYBD`). Cả hai thuộc tính đều không được mang giá trị `NULL`.

b. *(0.75 điểm)* Viết câu lệnh SQL cập nhật nâng mức độ thiệt hại (`MUCDO_THIETHAI`) thành 'Nặng' cho tất cả các hộ dân có số nhân khẩu từ 5 người trở lên (`SONKHAU >= 5`) thuộc xã có tên 'Hiệp Phước' (`TENXA = N'Hiệp Phước'`).

### 2. Viết các biểu thức Đại số quan hệ (6.5 điểm)

a. *(1.0 điểm)* Liệt kê danh sách các nhà hảo tâm (`MANHT`, `TENNHT`, `SDT`) thuộc loại hình 'Cá nhân' (`LOAIHINH = N'Cá nhân'`).

b. *(1.0 điểm)* Cho biết danh sách các hộ dân (`MAHO`, `CHUHO`, `SONKHAU`) thuộc huyện 'Cần Giờ' (`HUYEN = N'Cần Giờ'`) có mức độ thiệt hại là 'Nặng' (`MUCDO_THIETHAI = N'Nặng'`).

c. *(1.0 điểm)* Liệt kê thông tin tất cả các xã thuộc huyện 'Cần Giờ' (`MAXA`, `TENXA`) và danh sách các mã hộ dân (`MAHO`), tên chủ hộ (`CHUHO`) trực thuộc xã đó **nếu có** (những xã chưa có hộ dân nào đăng ký thiệt hại vẫn phải hiển thị thông tin xã, các cột hộ dân mang giá trị `NULL`).

d. *(1.0 điểm)* Tính tổng số tiền ủng hộ (`TONG_TIEN`) của từng nhà hảo tâm đã đóng góp trong năm 2024. Thông tin hiển thị gồm: `MANHT`, `TENNHT`, `TONG_TIEN`.

e. *(1.0 điểm)* Tìm các đợt cứu trợ (`MADOT`, `TENDOT`, `NGAYBD`) đã tiếp nhận tiền đóng góp từ **tất cả** các nhà hảo tâm thuộc loại hình 'Doanh nghiệp' (`LOAIHINH = N'Doanh nghiệp'`).

f. *(1.5 điểm)* Tìm thông tin xã (`MAXA`, `TENXA`, `HUYEN`) có tổng số tiền cứu trợ đã phân bổ cho các hộ dân (`TONG_CUUTRO`) nhiều nhất (bảo toàn tất cả các xã nếu có nhiều xã cùng đạt số tiền cứu trợ lớn nhất).

---

**HẾT ĐỀ THI MÔ PHỎNG SỐ 03**
*Cán bộ coi thi không giải thích gì thêm.*
