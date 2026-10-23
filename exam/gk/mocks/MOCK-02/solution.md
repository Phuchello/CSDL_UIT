# HƯỚNG DẪN CHẤM & LỜI GIẢI CHI TIẾT (MOCK-02)
**Đề thi:** Đề Thi Giữa Kỳ Mô Phỏng Số 02 — Quản Lý Hệ Thống Phòng Cháy Chữa Cháy Chung Cư
**Thời gian thi:** 75 phút | **Thang điểm:** 10.0 | **Tác giả:** VÕ TRỌNG PHÚC

---

## CÂU 1: THIẾT KẾ MÔ HÌNH DỮ LIỆU (2.5 ĐIỂM)
### 1.1. Phân tích thực thể, mối kết hợp & Sơ đồ ERD
- Thực thể chính: ERD: TOANHA, TANG, LOAI_DUNG_CU, DOT_KIEM_TRA, CAN_HO
- Bản số min-max phân định rõ 1:N và M:N.
- Khóa chính được gạch chân xác định duy nhất.

### 1.2. Ánh xạ sang Lược đồ quan hệ
- Chuyển đổi đúng theo quy tắc chuẩn: Thực thể -> Quan hệ; Mối kết hợp 1:N -> Đưa PK sang làm FK; Mối kết hợp M:N -> Bảng trung gian.
- **Barem điểm:** ERD đạt 1.50đ; Ánh xạ quan hệ đạt 1.00đ.

---

## CÂU 2: SQL & ĐẠI SỐ QUAN HỆ (7.5 ĐIỂM)

### 2.1. Viết các câu lệnh SQL (1.5 điểm)
- **Câu a (0.75đ):**
```sql
UPDATE LOVACXIN SET DONGIA = DONGIA * 0.85 WHERE HSD >= '2025-01-01' AND HSD <= '2025-03-31';
```
- **Câu b (0.75đ):**
```sql
ALTER TABLE BANG_4 ADD CONSTRAINT CK_BANG_4 CHECK (SOLUONG > 0 AND TRANGTHAI IN ('A', 'B'));
```

### 2.2. Viết các biểu thức Đại số quan hệ (6.0 điểm)
- **Câu 2a (1.0đ):**
  - Biểu thức ĐSQH: `π_{TENNCC, TENKVACXIN}(NHACUNGCAP ⋈ LOVACXIN ⋈ CTPX ⋈ σ_{MADT='DT01'}(PHIEUXUAT))`
  - T-SQL tương đương: `SELECT DISTINCT NCC.TENNCC, LV.TENKVACXIN FROM NHACUNGCAP NCC JOIN LOVACXIN LV ON NCC.MANCC=LV.MANCC JOIN CTPX CT ON LV.MALO=CT.MALO JOIN PHIEUXUAT PX ON CT.MAPX=PX.MAPX WHERE PX.MADT='DT01';`
- **Câu 2b (1.0đ):**
  - Biểu thức ĐSQH: `π_{MANCC, TENCC}(NHACC ⋈ CUNGCAP ⋈ σ_{NUOCSX='VN'}(MATHANG)) - π_{MANCC, TENCC}(NHACC ⋈ CUNGCAP ⋈ σ_{NUOCSX='TQ'}(MATHANG))`
  - T-SQL tương đương: `SELECT NC.MANCC, NC.TENCC FROM NHACC NC JOIN CUNGCAP CC ON NC.MANCC=CC.MACC JOIN MATHANG MH ON CC.MAMH=MH.MAMH WHERE MH.NUOCSX='VN' EXCEPT SELECT NC.MANCC, NC.TENCC FROM NHACC NC JOIN CUNGCAP CC ON NC.MANCC=CC.MACC JOIN MATHANG MH ON CC.MAMH=MH.MAMH WHERE MH.NUOCSX='TQ';`
- **Câu 2c (1.0đ):**
  - Biểu thức ĐSQH: `π_{MASANH, TENSANH, MATIEC, CHUTIEC}(SANH ⟕ TIEC)`
  - T-SQL tương đương: `SELECT S.MASANH, S.TENSANH, T.MATIEC, T.CHUTIEC FROM SANH S LEFT OUTER JOIN TIEC T ON S.MASANH = T.MASANH;`
- **Câu 2d (1.0đ):**
  - Biểu thức ĐSQH: `R_Div ← R1 ÷ R2
KQ ← R_Div ⋈ INFO`
  - T-SQL tương đương: `SELECT ID FROM R1 WHERE NOT EXISTS (SELECT * FROM R2 WHERE NOT EXISTS (...));`
- **Câu 2e (1.0đ):**
  - Biểu thức ĐSQH: `R_Div ← R1 ÷ R2
KQ ← R_Div ⋈ INFO`
  - T-SQL tương đương: `SELECT ID FROM R1 WHERE NOT EXISTS (SELECT * FROM R2 WHERE NOT EXISTS (...));`
- **Câu 2f (1.0đ):**
  - Biểu thức ĐSQH: `R_Div ← R1 ÷ R2
KQ ← R_Div ⋈ INFO`
  - T-SQL tương đương: `SELECT ID FROM R1 WHERE NOT EXISTS (SELECT * FROM R2 WHERE NOT EXISTS (...));`

---
**TỔNG ĐIỂM TOÀN BÀI: 10.0 ĐIỂM**
