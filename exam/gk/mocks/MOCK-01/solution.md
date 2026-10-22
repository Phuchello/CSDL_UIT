# HƯỚNG DẪN CHẤM & LỜI GIẢI CHI TIẾT ĐỀ THI MÔ PHỎNG SỐ 01 (MOCK-01)
**Môn học:** IT004 — Cơ sở dữ liệu | **Thời gian thi:** 75 phút | **Thang điểm:** 10.0
**Tác giả biên soạn:** VÕ TRỌNG PHÚC — CSDL_UIT Master Series
**Tiêu chuẩn học thuật:** Hợp đồng giải thích chi tiết, tư duy tự nhiên $\to$ biểu thức logic $\to$ ĐSQH $\to$ T-SQL, barem điểm từng ý và bẫy lỗi.

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)

### 1.1. Phân tích ngữ cảnh & Sơ đồ ERD (1.5 điểm)

#### A. Bảng định danh tập thực thể và thuộc tính
| Tên Thực thể | Khóa chính (PK) | Các thuộc tính mô tả | Ý nghĩa nghiệp vụ |
| :--- | :--- | :--- | :--- |
| `TRUNGTAM_YTE` | `MaTT` | `TenTT`, `DiaChiQuan` | Cơ quan y tế quận/huyện quản lý điểm tiêm và nhân sự. |
| `NHA_CUNGCAP` | `MaNCC` | `TenNCC`, `QuocGia`, `SDT` | Đơn vị sản xuất và cung ứng các lô vắc-xin. |
| `LO_VACXIN` | `MaLo` | `TenLo`, `TenVacxin`, `NgaySX`, `HSD`, `SoLieuNhap`, `DonGia` | Lô vắc-xin cụ thể nhập về kho trung tâm. |
| `DIEM_TIEM` | `MaDT` | `TenDT`, `DiaDiem`, `SucChua` | Điểm tiêm chủng lưu động hoặc cố định trên địa bàn. |
| `NHAN_VIEN` | `MaNV` | `HoTen`, `ChuyenMon`, `SDT` | Bác sĩ, điều dưỡng tham gia công tác tiêm chủng. |

#### B. Phân tích mối kết hợp và bản số Min–Max hai phía
1. **Mối kết hợp `CUNG_CAP` (NHA_CUNGCAP — LO_VACXIN):**
   - Một nhà cung cấp có thể cung cấp nhiều lô vắc-xin: $(1, N)$.
   - Một lô vắc-xin do duy nhất 1 nhà cung cấp cung ứng: $(1, 1)$.
   - $\implies$ **Loại quan hệ: 1:N**. Bản số: `NHA_CUNGCAP (1, N)` — `(1, 1) LO_VACXIN`.
2. **Mối kết hợp `QUAN_LY_DIEMTIEM` (TRUNGTAM_YTE — DIEM_TIEM):**
   - Một trung tâm y tế quản lý một hoặc nhiều điểm tiêm: $(1, N)$.
   - Một điểm tiêm chỉ trực thuộc duy nhất một trung tâm y tế: $(1, 1)$.
   - $\implies$ **Loại quan hệ: 1:N**. Bản số: `TRUNGTAM_YTE (1, N)` — `(1, 1) DIEM_TIEM`.
3. **Mối kết hợp `BIEN_CHE` (TRUNGTAM_YTE — NHAN_VIEN):**
   - Một trung tâm y tế có nhiều nhân viên y tế: $(1, N)$.
   - Mỗi nhân viên chỉ thuộc biên chế chính thức của một trung tâm: $(1, 1)$.
   - $\implies$ **Loại quan hệ: 1:N**. Bản số: `TRUNGTAM_YTE (1, N)` — `(1, 1) NHAN_VIEN`.
4. **Mối kết hợp `PHAN_PHOI` (LO_VACXIN — DIEM_TIEM):**
   - Một lô vắc-xin có thể phân phối cho nhiều điểm tiêm (hoặc chưa phân phối): $(0, N)$.
   - Một điểm tiêm có thể tiếp nhận vắc-xin từ nhiều lô khác nhau: $(1, N)$.
   - **Thuộc tính của mối kết hợp:** `NgayPP` (ngày phân phối), `SoLieuPP` (số liều), `TrangThai` (đã nhận / đang chuyển).
   - $\implies$ **Loại quan hệ: M:N**. Bản số: `LO_VACXIN (0, N)` — `(1, N) DIEM_TIEM`.
5. **Mối kết hợp `TRUC_CA` (NHAN_VIEN — DIEM_TIEM):**
   - Một nhân viên y tế có thể được điều động trực nhiều ca tại các điểm tiêm: $(0, N)$.
   - Một điểm tiêm tiếp nhận nhiều nhân viên đến trực ca: $(1, N)$.
   - **Thuộc tính của mối kết hợp:** `NgayTruc`, `VaiTroTruc` (Bác sĩ khám sàng lọc, tiêm, theo dõi).
   - $\implies$ **Loại quan hệ: M:N**. Bản số: `NHAN_VIEN (0, N)` — `(1, N) DIEM_TIEM`.

#### C. Sơ đồ Thực thể – Mối kết hợp (ERD Text / Structure)
```
[NHA_CUNGCAP] 1 ──── (1,N) ──── <CUNG_CAP> ──── (1,1) ──── N [LO_VACXIN]
                                                                  │
[TRUNGTAM_YTE] 1 ── (1,N) ── <QUAN_LY> ── (1,1) ── N [DIEM_TIEM]   │ (0,N)
      │                                                │          │
      │ (1,N)                                          │ (1,N)    │
   <BIEN_CHE>                                      <PHAN_PHOI> ───┘
      │                                                │ [NgayPP, SoLieuPP, TrangThai]
      │ (1,1)                                          │
      N                                                │
[NHAN_VIEN] N ──── (0,N) ──── <TRUC_CA> ──── (1,N) ────┘
                              [NgayTruc, VaiTroTruc]
```

---

### 1.2. Ánh xạ sang Lược đồ quan hệ (1.0 điểm)

Áp dụng quy tắc chuyển đổi mô hình dữ liệu quan hệ chuẩn UIT:
1. `TRUNGTAM_YTE` ($\underline{\text{MaTT}}$, TenTT, DiaChiQuan)
2. `NHA_CUNGCAP` ($\underline{\text{MaNCC}}$, TenNCC, QuocGia, SDT)
3. `LO_VACXIN` ($\underline{\text{MaLo}}$, TenLo, TenVacxin, NgaySX, HSD, SoLieuNhap, DonGia, MaNCC)
   *Khóa ngoại:* `MaNCC` tham chiếu `NHA_CUNGCAP(MaNCC)`.
4. `DIEM_TIEM` ($\underline{\text{MaDT}}$, TenDT, DiaDiem, SucChua, MaTT)
   *Khóa ngoại:* `MaTT` tham chiếu `TRUNGTAM_YTE(MaTT)`.
5. `NHAN_VIEN` ($\underline{\text{MaNV}}$, HoTen, ChuyenMon, SDT, MaTT)
   *Khóa ngoại:* `MaTT` tham chiếu `TRUNGTAM_YTE(MaTT)`.
6. `PHAN_PHOI` ($\underline{\text{MaLo}}$, $\underline{\text{MaDT}}$, $\underline{\text{NgayPP}}$, SoLieuPP, TrangThai)
   *Khóa chính:* Tổ hợp $(\text{MaLo}, \text{MaDT}, \text{NgayPP})$.
   *Khóa ngoại:* `MaLo` $\to$ `LO_VACXIN(MaLo)`, `MaDT` $\to$ `DIEM_TIEM(MaDT)`.
7. `TRUC_CA` ($\underline{\text{MaNV}}$, $\underline{\text{MaDT}}$, $\underline{\text{NgayTruc}}$, VaiTroTruc)
   *Khóa chính:* Tổ hợp $(\text{MaNV}, \text{MaDT}, \text{NgayTruc})$.
   *Khóa ngoại:* `MaNV` $\to$ `NHAN_VIEN(MaNV)`, `MaDT` $\to$ `DIEM_TIEM(MaDT)`.

**Barem chấm Câu 1:**
- Xác định đủ 5 tập thực thể, thuộc tính và gạch chân PK: **0.50đ**
- Vẽ đúng 5 mối kết hợp và bản số min-max hai phía: **1.00đ** (mỗi quan hệ 0.20đ)
- Ánh xạ sang 7 quan hệ, xác định đúng PK và đầy đủ toàn bộ FK: **1.00đ**

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)

#### a. Ràng buộc CHECK miền giá trị trên CTPX và PHIEUXUAT (0.75 điểm)
- **Mục tiêu:** Đảm bảo toàn vẹn dữ liệu: `SOLIEUXUAT > 0` và `TRANGTHAI` chỉ nhận `0` hoặc `1`.
- **Cú pháp T-SQL chuẩn:**
```sql
-- Ràng buộc 1: Số liều xuất phải là số nguyên dương
ALTER TABLE CTPX
ADD CONSTRAINT CK_CTPX_SOLIEUXUAT CHECK (SOLIEUXUAT > 0);

-- Ràng buộc 2: Trạng thái phiếu xuất chỉ nhận giá trị 0 hoặc 1
ALTER TABLE PHIEUXUAT
ADD CONSTRAINT CK_PHIEUXUAT_TRANGTHAI CHECK (TRANGTHAI IN (0, 1));
```
- *Phân tích bẫy lỗi:*
  - Nhầm cú pháp `CREATE CONSTRAINT` thay vì `ADD CONSTRAINT`.
  - Quên đặt tên ràng buộc (`CK_...`) khiến khó quản lý schema.
  - Viết nhầm điều kiện `SOLIEUXUAT >= 0` (đề bài yêu cầu số nguyên dương, tức $> 0$).
- *Barem điểm:* Mỗi ràng buộc đúng đạt **0.375đ**.

#### b. Cập nhật UPDATE tăng giá theo HSD và Nhà cung cấp (0.75 điểm)
- **Mục tiêu:** Tăng giá đơn vị `DONGIA` thêm 10% (tức nhân hệ số $1.1$) cho các lô có `HSD` năm 2025 của NCC 'AstraZeneca'.
- **Cú pháp T-SQL chuẩn (JOIN UPDATE):**
```sql
UPDATE LOVACXIN
SET DONGIA = DONGIA * 1.1
FROM LOVACXIN LV
INNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC
WHERE YEAR(LV.HSD) = 2025
  AND NCC.TENNCC = 'AstraZeneca';
```
- **Cú pháp T-SQL tương đương (Subquery):**
```sql
UPDATE LOVACXIN
SET DONGIA = DONGIA * 1.1
WHERE YEAR(HSD) = 2025
  AND MANCC IN (SELECT MANCC FROM NHACUNGCAP WHERE TENNCC = 'AstraZeneca');
```
- *Barem điểm:*
  - Mệnh đề `UPDATE ... SET DONGIA = DONGIA * 1.1`: **0.25đ**
  - Mệnh đề `JOIN` hoặc `IN` liên kết đúng `NHACUNGCAP`: **0.25đ**
  - Điều kiện lọc `YEAR(HSD) = 2025` và `TENNCC = 'AstraZeneca'`: **0.25đ**

---

### 2.2. Viết các biểu thức Đại số quan hệ (6.0 điểm - mỗi câu 1.0 điểm)

#### a. Lọc lô vắc-xin theo tên và năm sản xuất (1.0 điểm)
- **Mục tiêu:** Lấy `MALO, TENLO, SOLIEU, DONGIA` của vắc-xin 'Pfizer-BioNTech' sản xuất năm 2024.
- **Tư duy:**
  1. Phép chọn $\sigma$ trên quan hệ `LOVACXIN`: điều kiện chuỗi `TENKVACXIN = 'Pfizer-BioNTech'` kết hợp khoảng thời gian `NGAYSX`.
  2. Phép chiếu $\pi$ lấy đúng 4 thuộc tính yêu cầu.
- **Biểu thức ĐSQH:**
  $$R_1 \leftarrow \sigma_{\text{TENKVACXIN} = '\text{Pfizer-BioNTech}' \wedge \text{NGAYSX} \ge '\text{01/01/2024}' \wedge \text{NGAYSX} \le '\text{31/12/2024}'}(\text{LOVACXIN})$$
  $$KQ \leftarrow \pi_{\text{MALO}, \text{TENLO}, \text{SOLIEU}, \text{DONGIA}}(R_1)$$
- *Barem điểm:* Phép chọn $\sigma$ đúng điều kiện: **0.50đ**; Phép chiếu $\pi$ đúng 4 thuộc tính: **0.50đ**.

#### b. Điểm tiêm nhận phiếu xuất ngày 15/10/2024 (1.0 điểm)
- **Mục tiêu:** Tìm `MADT, TENDT, QUAN` có phiếu xuất vắc-xin ngày 15/10/2024.
- **Tư duy:**
  1. Lọc trước trên `PHIEUXUAT` để tối ưu kích thước: $R_1 \leftarrow \sigma_{\text{NGAYXUAT} = '\text{15/10/2024}'}(\text{PHIEUXUAT})$.
  2. Kết nối tự nhiên giữa `DIEMTIEM` và $R_1$ qua thuộc tính chung `MADT`.
  3. Chiếu các thuộc tính đầu ra: `MADT, TENDT, QUAN`.
- **Biểu thức ĐSQH:**
  $$R_1 \leftarrow \sigma_{\text{NGAYXUAT} = '\text{15/10/2024}'}(\text{PHIEUXUAT})$$
  $$R_2 \leftarrow \text{DIEMTIEM} \bowtie R_1$$
  $$KQ \leftarrow \pi_{\text{MADT}, \text{TENDT}, \text{QUAN}}(R_2)$$
- *Barem điểm:* Phép chọn $\sigma$: **0.25đ**; Phép kết $\bowtie$: **0.50đ**; Phép chiếu $\pi$: **0.25đ**.

#### c. Điểm tiêm quận Bình Thạnh và bác sĩ trực "nếu có" (1.0 điểm)
- **Mục tiêu:** Lấy `MADT, TENDT` ở Bình Thạnh và `HOTEN` bác sĩ trực tại đó **nếu có**.
- **Tư duy Phân Loại B (Phép Kết Ngoài Trái $\mathbin{⟕}$):**
  - Từ khóa *"nếu có"* là yêu cầu bắt buộc của **Left Outer Join ($\mathbin{⟕}$)**.
  - Nếu dùng kết tự nhiên $\bowtie$, các điểm tiêm ở quận Bình Thạnh chưa được phân công bác sĩ trực (ví dụ `DT06`) sẽ bị loại bỏ hoàn toàn khỏi kết quả.
- **Biểu thức ĐSQH:**
  $$R_1 \leftarrow \sigma_{\text{QUAN} = '\text{Bình Thạnh}'}(\text{DIEMTIEM})$$
  $$R_2 \leftarrow R_1 \mathbin{⟕}_{R_1.\text{MADT} = \text{BACSI}.\text{MADT}} \text{BACSI}$$
  $$KQ \leftarrow \pi_{\text{MADT}, \text{TENDT}, \text{HOTEN}}(R_2)$$
- *Bẫy lỗi:* Dùng phép kết thường $\bowtie$ thay vì kết ngoài $\mathbin{⟕}$ bị trừ **0.50đ**.
- *Barem điểm:* Phép chọn Bình Thạnh: **0.25đ**; Phép kết ngoài $\mathbin{⟕}$: **0.50đ**; Phép chiếu $\pi$: **0.25đ**.

#### d. Gom nhóm tính tổng số liều xuất theo điểm tiêm tháng 10/2024 (1.0 điểm)
- **Mục tiêu:** Tính tổng số liều vắc-xin xuất theo từng điểm tiêm trong tháng 10/2024.
- **Tư duy:**
  1. Lọc các phiếu xuất phát sinh trong tháng 10/2024: $R_1$.
  2. Kết nối $R_1$ với `CTPX` qua `MAPX` để lấy `SOLIEUXUAT`: $R_2$.
  3. Gom nhóm $\gamma$ theo `MADT`, tính hàm tổng `SUM(SOLIEUXUAT)` và đổi tên thành thuộc tính mới `TONGLIEU`.
- **Biểu thức ĐSQH:**
  $$R_1 \leftarrow \sigma_{\text{NGAYXUAT} \ge '\text{01/10/2024}' \wedge \text{NGAYXUAT} \le '\text{31/10/2024}'}(\text{PHIEUXUAT})$$
  $$R_2 \leftarrow R_1 \bowtie \text{CTPX}$$
  $$KQ \leftarrow _{\text{MADT}} \gamma _{\text{SUM}(\text{SOLIEUXUAT}) \to \text{TONGLIEU}}(R_2)$$
- *Barem điểm:* Lọc thời gian và kết nối bảng: **0.50đ**; Phép gom nhóm $\gamma$ đúng thuộc tính nhóm và hàm tổng: **0.50đ**.

#### e. Phép chia: Điểm tiêm nhận tất cả các lô của Moderna (1.0 điểm)
- **Mục tiêu:** Tìm các điểm tiêm (`MADT, TENDT`) đã tiếp nhận **tất cả** các lô vắc-xin của nhà cung cấp 'Moderna'.
- **Tư duy Phân Loại C (Bài toán "Tất cả" - Phép chia $\div$):**
  1. **Tập chia (R_Moderna):** Tập hợp tất cả các mã lô vắc-xin của NCC 'Moderna':
     $$R_{\text{Moderna}} \leftarrow \pi_{\text{MALO}}(\sigma_{\text{TENNCC} = '\text{Moderna}'}(\text{NHACUNGCAP} \bowtie \text{LOVACXIN}))$$
  2. **Tập bị chia (R_DT_Lo):** Tập hợp các cặp $(\text{MADT}, \text{MALO})$ thực tế đã xuất vắc-xin:
     $$R_{\text{DT\_Lo}} \leftarrow \pi_{\text{MADT}, \text{MALO}}(\text{PHIEUXUAT} \bowtie \text{CTPX})$$
  3. **Phép chia hình thức:**
     $$R_{\text{Chia}} \leftarrow R_{\text{DT\_Lo}} \div R_{\text{Moderna}}$$
  4. **Kết nối lấy tên điểm tiêm:**
     $$KQ \leftarrow \pi_{\text{MADT}, \text{TENDT}}(R_{\text{Chia}} \bowtie \text{DIEMTIEM})$$
- *Barem điểm:*
  - Xác định đúng tập chia $R_{\text{Moderna}}$: **0.25đ**
  - Chiếu đúng quan hệ bị chia $R_{\text{DT\_Lo}}$: **0.25đ**
  - Phép chia $\div$ và kết lấy tên điểm tiêm: **0.50đ**

#### f. Điểm tiêm có sức chứa lớn nhất tại quận Thủ Đức (1.0 điểm)
- **Mục tiêu:** Tìm điểm tiêm (`MADT, TENDT`) có `SUCCHUA` lớn nhất trong quận 'Thủ Đức'.
- **Tư duy Phân Loại C (Bài toán Cực Trị trong ĐSQH thuần túy):**
  Trong ĐSQH chuẩn không có hàm `MAX()` trực tiếp trong mệnh đề chọn, ta áp dụng phương pháp **tự kết so sánh bé hơn và phép trừ**:
  1. Lọc các điểm tiêm tại Thủ Đức: $R_1 \leftarrow \sigma_{\text{QUAN} = '\text{Thủ Đức}'}(\text{DIEMTIEM})$.
  2. Tạo 2 bản sao đổi tên: $R_2 \leftarrow \rho_{D_1}(R_1)$ và $R_3 \leftarrow \rho_{D_2}(R_1)$.
  3. Tìm tập các điểm tiêm **không phải lớn nhất** (vì tồn tại điểm tiêm $D_2$ có sức chứa lớn hơn nó):
     $$R_{\text{KoMax}} \leftarrow \pi_{D_1.\text{MADT}}(R_2 \bowtie_{D_1.\text{SUCCHUA} < D_2.\text{SUCCHUA}} R_3)$$
  4. Lấy toàn bộ điểm tiêm ở Thủ Đức trừ đi tập không lớn nhất:
     $$R_{\text{Max}} \leftarrow \pi_{\text{MADT}}(R_1) - R_{\text{KoMax}}$$
  5. Chiếu thông tin đầu ra:
     $$KQ \leftarrow \pi_{\text{MADT}, \text{TENDT}}(R_{\text{Max}} \bowtie R_1)$$
- *Barem điểm:*
  - Tự kết so sánh bé hơn để tìm tập phần bù: **0.50đ**
  - Phép trừ tìm cực trị và chiếu kết quả: **0.50đ**

---
**TỔNG KẾT BÀI THI MOCK-01:**
- Thời gian làm bài: **75 phút** | Tổng điểm: **10.0 điểm** (chuẩn không sai lệch).
- Phân bổ: ERD & Ánh xạ: **2.5 điểm**; SQL DDL/DML: **1.5 điểm**; ĐSQH 6 câu: **6.0 điểm**.
- Đã kiểm chứng thực thi hoàn toàn trên Transact-SQL SQL Server (`fixture_mock01.sql`).
