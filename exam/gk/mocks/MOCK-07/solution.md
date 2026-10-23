# HƯỚNG DẪN CHẤM & LỜI GIẢI CHI TIẾT (MOCK-07)
**Đề thi:** Đề Thi Giữa Kỳ Mô Phỏng Số 07 — Quản Lý Thư Viện Số UIT & Mượn Trả Tài Liệu
**Thời gian thi:** 75 phút | **Thang điểm:** 10.0 | **Tác giả:** VÕ TRỌNG PHÚC

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.0 ĐIỂM)
### 1.1. Phân tích thực thể, mối kết hợp & Sơ đồ ERD
- Thực thể chính: DAU_SACH, CUON_SACH, DOC_GIA, PHIEU_MUON, VI_PHAM
- Bản số min-max phân định rõ 1:N và M:N.
- Khóa chính được gạch chân xác định duy nhất.

### 1.2. Ánh xạ sang Lược đồ quan hệ
- Chuyển đổi đúng theo quy tắc chuẩn: Thực thể -> Quan hệ; Mối kết hợp 1:N -> Đưa PK sang làm FK; Mối kết hợp M:N -> Bảng trung gian.
- **Barem điểm:** ERD đạt 1.20đ; Ánh xạ quan hệ đạt 0.80đ.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (8.0 ĐIỂM)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)
- **Câu a (0.75đ):**
```sql
UPDATE B1 SET B1.GIA = B1.GIA * 1.05 FROM BANG_A B1 INNER JOIN BANG_B B2 ON B1.ID = B2.ID WHERE B2.LOAI = 'VIP';
```
- **Câu b (0.75đ):**
```sql
ALTER TABLE BANG_14 ADD CONSTRAINT CK_BANG_14 CHECK (SOLUONG > 0 AND TRANGTHAI IN ('A', 'B'));
```

### 2.2. Viết các biểu thức Đại số quan hệ (6.5 điểm)
- **Câu 2a (1.0đ):**
  - Biểu thức ĐSQH: `KQ ← π_{ID}(σ_{A}(R)) - π_{ID}(σ_{B}(R))`
  - T-SQL tương đương: `SELECT ID FROM R WHERE A EXCEPT SELECT ID FROM R WHERE B;`
- **Câu 2b (1.0đ):**
  - Biểu thức ĐSQH: `KQ ← π_{ID, TEN}(σ_{DIEUKIEN}(ChuyếnBay))`
  - T-SQL tương đương: `SELECT ID, TEN FROM ChuyếnBay WHERE DIEUKIEN;`
- **Câu 2c (1.0đ):**
  - Biểu thức ĐSQH: `KQ ← π_{THUOCTINH}(R1 ⋈ R2)`
  - T-SQL tương đương: `SELECT * FROM R1 JOIN R2 ON R1.KEY = R2.KEY WHERE DIEUKIEN;`
- **Câu 2d (1.0đ):**
  - Biểu thức ĐSQH: `R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO`
  - T-SQL tương đương: `SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));`
- **Câu 2e (1.0đ):**
  - Biểu thức ĐSQH: `R_Group ← _{KEY} γ _{SUM(VAL) → TONG, COUNT(*) → SL}(R)
KQ ← π_{KEY, TONG}(R_Group)`
  - T-SQL tương đương: `SELECT KEY, SUM(VAL) AS TONG, COUNT(*) AS SL FROM R GROUP BY KEY HAVING COUNT(*) >= 2;`
- **Câu 2f (1.5đ):**
  - Biểu thức ĐSQH: `R_Target ← π_{KEY2}(σ_{DK}(R2))
R_Cand ← π_{KEY1, KEY2}(R1)
KQ ← (R_Cand ÷ R_Target) ⋈ INFO`
  - T-SQL tương đương: `SELECT KEY1 FROM R1 WHERE NOT EXISTS (SELECT KEY2 FROM R2 WHERE NOT EXISTS (SELECT * FROM REL WHERE REL.KEY1=R1.KEY1 AND REL.KEY2=R2.KEY2));`

---
**TỔNG ĐIỂM TOÀN BÀI: 10.0 ĐIỂM**
