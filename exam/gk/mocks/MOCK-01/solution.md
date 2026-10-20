# HƯỚNG DẪN CHẤM & LỜI GIẢI CHI TIẾT ĐỀ THI MÔ PHỎNG SỐ 01 (MOCK-01)
**Môn học:** IT004 — Cơ sở dữ liệu | **Thời gian thi:** 75 phút | **Thang điểm:** 10.0  
**Tác giả biên soạn:** VÕ TRỌNG PHÚC  
**Tiêu chuẩn học thuật:** Hợp đồng lời giải chi tiết, phân tích tư duy tự nhiên $\to$ biểu thức toán $\to$ T-SQL, barem điểm và bẫy lỗi.

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)

### 1.1. Phân tích ngữ cảnh & Sơ đồ ERD (1.5 điểm)

#### A. Bảng tổng hợp thực thể và thuộc tính
1. `TRUNGTAM_YTE` (Mã TT $\underline{MaTT}$, TenTT, DiaChiQuan) — Khóa chính: `MaTT`.
2. `NHA_CUNGCAP` (Mã NCC $\underline{MaNCC}$, TenNCC, QuocGia, SDT) — Khóa chính: `MaNCC`.
3. `LO_VACXIN` (Mã lô $\underline{MaLo}$, TenLo, TenVacxin, NgaySX, HSD, SoLieuNhap, DonGia) — Khóa chính: `MaLo`.
4. `DIEM_TIEM` (Mã ĐT $\underline{MaDT}$, TenDT, DiaDiem, SucChua) — Khóa chính: `MaDT`.
5. `NHAN_VIEN` (Mã NV $\underline{MaNV}$, HoTen, ChuyenMon, SDT) — Khóa chính: `MaNV`.

#### B. Phân tích mối kết hợp và bản số Min–Max
- **Mối kết hợp `CUNG_CAP` (NHA_CUNGCAP — LO_VACXIN):**
  - Một nhà cung cấp có thể cung cấp nhiều lô vắc-xin: $(1, N)$.
  - Một lô vắc-xin do duy nhất 1 nhà cung cấp cung ứng: $(1, 1)$.
  - $\implies$ Bản số: `NHA_CUNGCAP (1, N)` — `(1, 1) LO_VACXIN` (Loại quan hệ: $1:N$).
- **Mối kết hợp `QUAN_LY_DIEMTIEM` (TRUNGTAM_YTE — DIEM_TIEM):**
  - Một trung tâm y tế quản lý nhiều điểm tiêm: $(1, N)$.
  - Một điểm tiêm trực thuộc duy nhất 1 trung tâm y tế: $(1, 1)$.
  - $\implies$ Bản số: `TRUNGTAM_YTE (1, N)` — `(1, 1) DIEM_TIEM` (Loại quan hệ: $1:N$).
- **Mối kết hợp `BIEN_CHE` (TRUNGTAM_YTE — NHAN_VIEN):**
  - Một trung tâm y tế có nhiều nhân viên: $(1, N)$.
  - Mỗi nhân viên chỉ thuộc biên chế 1 trung tâm: $(1, 1)$.
  - $\implies$ Bản số: `TRUNGTAM_YTE (1, N)` — `(1, 1) NHAN_VIEN` (Loại quan hệ: $1:N$).
- **Mối kết hợp `PHAN_PHOI` (LO_VACXIN — DIEM_TIEM):**
  - Một lô vắc-xin có thể phân phối cho nhiều điểm tiêm: $(0, N)$.
  - Một điểm tiêm có thể nhận vắc-xin từ nhiều lô khác nhau: $(1, N)$.
  - Thuộc tính của mối kết hợp: `NgayPP`, `SoLieuPP`, `TrangThai`.
  - $\implies$ Loại quan hệ: $M:N$.
- **Mối kết hợp `TRUC_CA` (NHAN_VIEN — DIEM_TIEM):**
  - Một nhân viên có thể trực tại nhiều điểm tiêm vào các ngày khác nhau: $(0, N)$.
  - Một điểm tiêm có nhiều nhân viên đến trực: $(1, N)$.
  - Thuộc tính của mối kết hợp: `NgayTruc`, `VaiTroTruc`.
  - $\implies$ Loại quan hệ: $M:N$.

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

### 1.2. Ánh xạ sang Lược đồ quan hệ (1.0 điểm)
Áp dụng các quy tắc ánh xạ chuẩn UIT:
1. `TRUNGTAM_YTE` ($\underline{\text{MaTT}}$, TenTT, DiaChiQuan)
2. `NHA_CUNGCAP` ($\underline{\text{MaNCC}}$, TenNCC, QuocGia, SDT)
3. `LO_VACXIN` ($\underline{\text{MaLo}}$, TenLo, TenVacxin, NgaySX, HSD, SoLieuNhap, DonGia, MaNCC)  
   *Khóa ngoại:* `MaNCC` $\to$ `NHA_CUNGCAP(MaNCC)`.
4. `DIEM_TIEM` ($\underline{\text{MaDT}}$, TenDT, DiaDiem, SucChua, MaTT)  
   *Khóa ngoại:* `MaTT` $\to$ `TRUNGTAM_YTE(MaTT)`.
5. `NHAN_VIEN` ($\underline{\text{MaNV}}$, HoTen, ChuyenMon, SDT, MaTT)  
   *Khóa ngoại:* `MaTT` $\to$ `TRUNGTAM_YTE(MaTT)`.
6. `PHAN_PHOI` ($\underline{\text{MaLo}}$, $\underline{\text{MaDT}}$, $\underline{\text{NgayPP}}$, SoLieuPP, TrangThai)  
   *Khóa ngoại:* `MaLo` $\to$ `LO_VACXIN(MaLo)`, `MaDT` $\to$ `DIEM_TIEM(MaDT)`.
7. `TRUC_CA` ($\underline{\text{MaNV}}$, $\underline{\text{MaDT}}$, $\underline{\text{NgayTruc}}$, VaiTroTruc)  
   *Khóa ngoại:* `MaNV` $\to$ `NHAN_VIEN(MaNV)`, `MaDT` $\to$ `DIEM_TIEM(MaDT)`.

**Barem chấm Câu 1:**
- Đủ 5 thực thể, thuộc tính và gạch chân PK: **0.50đ**
- Đúng mối kết hợp và bản số min-max hai phía: **1.00đ**
- Ánh xạ sang 7 quan hệ, xác định đúng PK và toàn bộ FK: **1.00đ**

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)

#### a. Ràng buộc CHECK miền giá trị (0.75 điểm)
```sql
-- Ràng buộc SOLIEUXUAT > 0 trong CTPX
ALTER TABLE CTPX 
ADD CONSTRAINT CK_CTPX_SOLIEUXUAT CHECK (SOLIEUXUAT > 0);

-- Ràng buộc TRANGTHAI nhận 0 hoặc 1 trong PHIEUXUAT
ALTER TABLE PHIEUXUAT 
ADD CONSTRAINT CK_PHIEUXUAT_TRANGTHAI CHECK (TRANGTHAI IN (0, 1));
```
- *Lỗi dễ mắc:* Dùng sai tên bảng, viết nhầm cú pháp `CREATE CONSTRAINT`, quên đặt tên ràng buộc.
- *Barem:* Mỗi ràng buộc đúng đạt **0.375đ**.

#### b. Cập nhật UPDATE tăng giá theo HSD và Nhà cung cấp (0.75 điểm)
- **Tư duy:** Tăng 10% tức `DONGIA = DONGIA * 1.1`. Cần liên kết `LOVACXIN` với `NHACUNGCAP` để kiểm tra `TENNCC = 'AstraZeneca'`. Điều kiện năm HSD dùng hàm `YEAR(HSD) = 2025`.

```sql
UPDATE LOVACXIN
SET DONGIA = DONGIA * 1.1
FROM LOVACXIN LV
INNER JOIN NHACUNGCAP NCC ON LV.MANCC = NCC.MANCC
WHERE YEAR(LV.HSD) = 2025 
  AND NCC.TENNCC = 'AstraZeneca';
```
*(Cách 2 dùng Subquery cũng được trọn điểm):*
```sql
UPDATE LOVACXIN
SET DONGIA = DONGIA * 1.1
WHERE YEAR(HSD) = 2025 
  AND MANCC IN (SELECT MANCC FROM NHACUNGCAP WHERE TENNCC = 'AstraZeneca');
```
- *Barem:* Mệnh đề UPDATE & SET: **0.25đ**; Mệnh đề WHERE lọc năm và NCC: **0.50đ**.

---

### 2.2. Viết các biểu thức Đại số quan hệ (6.0 điểm)

#### a. Lọc lô vắc-xin theo tên và năm sản xuất (1.0 điểm)
- **Tư duy:**
  1. Phép chọn $\sigma$ lọc thuộc tính chuỗi và khoảng thời gian năm 2024.
  2. Phép chiếu $\pi$ lấy 4 thuộc tính theo đúng yêu cầu đề bài.
- **Biểu thức ĐSQH:**
  $$R_1 \leftarrow \sigma_{\text{TENKVACXIN} = '\text{Pfizer-BioNTech}' \wedge \text{NGAYSX} \ge '\text{01/01/2024}' \wedge \text{NGAYSX} \le '\text{31/12/2024}'}(\text{LOVACXIN})$$
  $$KQ \leftarrow \pi_{\text{MALO}, \text{TENLO}, \text{SOLIEU}, \text{DONGIA}}(R_1)$$
- *Barem:* Phép chọn $\sigma$: **0.50đ**; Phép chiếu $\pi$: **0.50đ**.

#### b. Điểm tiêm nhận phiếu xuất ngày 15/10/2024 (1.0 điểm)
- **Tư duy:** Lọc phiếu xuất ngày 15/10/2024 trước để giảm kích thước bảng, sau đó kết tự nhiên với `DIEMTIEM` qua khóa ngoại `MADT`.
- **Biểu thức ĐSQH:**
  $$R_1 \leftarrow \sigma_{\text{NGAYXUAT} = '\text{15/10/2024}'}(\text{PHIEUXUAT})$$
  $$R_2 \leftarrow \text{DIEMTIEM} \bowtie R_1$$
  $$KQ \leftarrow \pi_{\text{MADT}, \text{TENDT}, \text{QUAN}}(R_2)$$
- *Barem:* Phép chọn $\sigma$: **0.25đ**; Phép kết $\bowtie$: **0.50đ**; Phép chiếu $\pi$: **0.25đ**.

#### c. Điểm tiêm quận Bình Thạnh và bác sĩ phụ trách "nếu có" (1.0 điểm)
- **Tư duy Phân Loại B:**
  - Từ khóa *"nếu có"* là tín hiệu bắt buộc của **Phép Kết Ngoài Trái (Left Outer Join $\mathbin{⟕}$)**. Nếu dùng kết tự nhiên $\bowtie$, các điểm tiêm ở Bình Thạnh chưa có bác sĩ trực sẽ bị loại bỏ, dẫn đến mất dữ liệu.
- **Biểu thức ĐSQH:**
  $$R_1 \leftarrow \sigma_{\text{QUAN} = '\text{Bình Thạnh}'}(\text{DIEMTIEM})$$
  $$R_2 \leftarrow R_1 \mathbin{⟕}_{R_1.\text{MADT} = \text{BACSI}.\text{MADT}} \text{BACSI}$$
  $$KQ \leftarrow \pi_{\text{MADT}, \text{TENDT}, \text{HOTEN}}(R_2)$$
- *Bẫy lỗi:* Dùng phép kết thường $\bowtie$ thay vì kết ngoài $\mathbin{⟕}$ bị trừ 0.50đ.
- *Barem:* Phép chọn Bình Thạnh: **0.25đ**; Phép kết ngoài $\mathbin{⟕}$: **0.50đ**; Phép chiếu $\pi$: **0.25đ**.

#### d. Gom nhóm tính tổng số liều xuất theo điểm tiêm tháng 10/2024 (1.0 điểm)
- **Tư duy:**
  1. Lọc các phiếu xuất có `NGAYXUAT` trong tháng 10/2024: $R_1$.
  2. Kết nối $R_1$ với `CTPX` qua `MAPX` để lấy số liều xuất: $R_2$.
  3. Gom nhóm $\gamma$ theo `MADT`, tính hàm tổng `SUM(SOLIEUXUAT)` và đặt tên thuộc tính mới là `TONGLIEU`.
- **Biểu thức ĐSQH:**
  $$R_1 \leftarrow \sigma_{\text{NGAYXUAT} \ge '\text{01/10/2024}' \wedge \text{NGAYXUAT} \le '\text{31/10/2024}'}(\text{PHIEUXUAT})$$
  $$R_2 \leftarrow R_1 \bowtie \text{CTPX}$$
  $$KQ \leftarrow _{\text{MADT}} \gamma _{\text{SUM}(\text{SOLIEUXUAT}) \to \text{TONGLIEU}}(R_2)$$
- *Barem:* Lọc và kết nối bảng: **0.50đ**; Phép gom nhóm $\gamma$ đúng cú pháp và hàm tổng: **0.50đ**.

#### e. Phép chia: Điểm tiêm nhận tất cả các lô của Moderna (1.0 điểm)
- **Tư duy Phân Loại C (Bài toán "Tất cả" - Phép chia $\div$):**
  1. Xác định tập chia (tập các lô của Moderna):
     $$R_{\text{Moderna}} \leftarrow \pi_{\text{MALO}}(\sigma_{\text{TENNCC} = '\text{Moderna}'}(\text{NHACUNGCAP} \bowtie \text{LOVACXIN}))$$
  2. Xác định quan hệ các cặp (Điểm tiêm, Lô vắc-xin) đã thực sự tiếp nhận:
     $$R_{\text{DT\_Lo}} \leftarrow \pi_{\text{MADT}, \text{MALO}}(\text{PHIEUXUAT} \bowtie \text{CTPX})$$
  3. Thực hiện phép chia hình thức:
     $$R_{\text{Chia}} \leftarrow R_{\text{DT\_Lo}} \div R_{\text{Moderna}}$$
  4. Lấy thông tin chi tiết tên điểm tiêm:
     $$KQ \leftarrow \pi_{\text{MADT}, \text{TENDT}}(R_{\text{Chia}} \bowtie \text{DIEMTIEM})$$
- *Giải thích logic toán học:* Phép chia $R_{\text{DT\_Lo}} \div R_{\text{Moderna}}$ trả về tập các `MADT` sao cho $\forall y \in R_{\text{Moderna}}, (\text{MADT}, y) \in R_{\text{DT\_Lo}}$.
- *Barem:* Xác định đúng tập chia $R_{\text{Moderna}}$: **0.25đ**; Chiếu đúng quan hệ bị chia: **0.25đ**; Phép chia $\div$ và kết lấy tên điểm tiêm: **0.50đ**.

#### f. Điểm tiêm có sức chứa lớn nhất tại Thủ Đức (1.0 điểm)
- **Tư duy Phân Loại C (Bài toán Cực Trị trong ĐSQH):**
  Trong ĐSQH thuần túy không có hàm `MAX()` trực tiếp cho bài toán lọc, ta dùng phương pháp **tự kết so sánh bé hơn và phép trừ**:
  1. Lọc danh sách điểm tiêm ở Thủ Đức: $R_1 \leftarrow \sigma_{\text{QUAN} = '\text{Thủ Đức}'}(\text{DIEMTIEM})$.
  2. Tạo 2 bản sao đổi tên: $R_2 \leftarrow \rho_{D_1}(R_1)$ và $R_3 \leftarrow \rho_{D_2}(R_1)$.
  3. Tìm tập các điểm tiêm **chắc chắn không phải lớn nhất** (vì tồn tại điểm tiêm $D_2$ có sức chứa lớn hơn nó):
     $$R_{\text{KoMax}} \leftarrow \pi_{D_1.\text{MADT}}(R_2 \bowtie_{D_1.\text{SUCCHUA} < D_2.\text{SUCCHUA}} R_3)$$
  4. Lấy toàn bộ các điểm tiêm ở Thủ Đức trừ đi tập không lớn nhất:
     $$R_{\text{Max}} \leftarrow \pi_{\text{MADT}}(R_1) - R_{\text{KoMax}}$$
  5. Chiếu thông tin đầu ra:
     $$KQ \leftarrow \pi_{\text{MADT}, \text{TENDT}}(R_{\text{Max}} \bowtie R_1)$$
- *Barem:* Ý tưởng tự kết so sánh bé hơn: **0.50đ**; Phép trừ tìm cực trị và chiếu kết quả: **0.50đ**.

---
**TỔNG KẾT ĐÁNH GIÁ PILOT MOCK-01:**
- Đảm bảo 100% thời lượng 75 phút, thang điểm 10.0 không sai lệch.
- Phân bố phổ điểm đúng theo chuẩn kiểm định thực chứng: ERD 2.5đ + SQL 1.5đ + ĐSQH 6.0đ.
- Không để lộ đáp án trên đề bài học viên.