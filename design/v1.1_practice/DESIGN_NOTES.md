# Ghi Chú Thiết Kế Cẩm Nang Thực Hành (Practical Design Notes) — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31  
**Tác giả biên soạn:** Võ Trọng Phúc  
**Tài liệu đích:** `dist/proofs/IT004_CSDL_UIT_v1.1_Practice_DesignProof.pdf` (21 trang A4)

---

## 1. Triết Lý & Quan Hệ Gia Đình với Sổ Tay Lý Thuyết

Cẩm nang Thực hành IT004 được thiết kế như ấn phẩm đồng hành cùng Sổ tay Lý thuyết đã được phê duyệt và đóng băng ở Phase B2 (`v1.1-theory-redesign`).

- **Tính nhất quán hình thức (Visual Family):**
  - **Hệ màu kiềm chế B1:** Sử dụng đồng nhất màu Mực Navy (`#203047`), Xanh cổ vịt Teal (`#1e7881`), Đất son Ochre (`#b57b36`), Đỏ gỉ Rust (`#a94a32`), Nền giấy ấm Paper (`#fbfaf7`), và các dải màu mềm phụ trợ (`#e7f1f1`, `#f6efe5`, `#fbeee9`).
  - **Kiểu chữ:** Thân bài Serif học thuật (`Georgia`, `Cambria`), Tiêu đề Sans-serif hình học (`Segoe UI`, `Arial`), Mã nguồn Monospace (`Consolas`, `Cascadia Mono`).
  - **Bìa Cover A Thực hành:** Kế thừa bố cục tối giản của Cover A Lý thuyết (chỉ gồm `IT004`, `THỰC HÀNH CƠ SỞ DỮ LIỆU`, `BIÊN SOẠN: VÕ TRỌNG PHÚC`) cùng sơ đồ vector chuyển hóa dữ liệu: *Bảng nguồn (R1, R2) $\rightarrow$ SQL Server Engine $\rightarrow$ Quan hệ kết quả (R3)*.

- **Tính chất khác biệt (Differentiated Identity):**
  - Khác với sách lý thuyết tập trung vào chứng minh toán học và đại số quan hệ, sách thực hành có mật độ mã nguồn cao hơn, tập trung vào cơ chế thực thi bên trong hệ quản trị CSDL, bảng kết quả mẫu và hệ thống chẩn đoán lỗi.

---

## 2. Kỷ Luật Phạm Vi & Căn Cứ Thực Chứng (Scope Discipline)

Nội dung cẩm nang tuân thủ nghiêm ngặt phân loại kỹ năng từ **Phase A** (`research/v1.1_phase_a/practical_coverage_map.md`):

| Nhóm kỹ năng | Phân loại | Căn cứ thẩm quyền | Trọng tâm trong Cẩm nang |
| :--- | :---: | :--- | :--- |
| **DDL, DML, SELECT, JOIN, GROUP BY, Subquery** | **CORE** | `LOC-SQL-LAB01`–`LAB04`, `TECH-A01`–`TECH-A03`, `TECH-A07` | Toàn bộ Phần 1 đến Phần 5: giải thích cơ chế sâu sắc, có dòng thực thi và kiểm chứng. |
| **DML Trigger (An toàn đa dòng)** | **CORE THEORY & EXAM / ADVANCED PRACTICAL** | `TECH-A04`–`TECH-A06`, `LOC-LEC-LONG-CH05`, 10 Practical Exam Artifacts | Phần 6: Phân tích chi tiết bảng ảo `inserted`/`deleted`, loại bỏ tư duy biến vô hướng, chuẩn hóa dạng tập hợp. |
| **Stored Procedure, View** | **OPTIONAL / ADVANCED** | `TECH-A09`, `TECH-A10` | Đặt tại Phụ lục mở rộng, không làm loãng luồng học chính. |
| **Transactions & Locking** | **UNSUPPORTED** | Ngoài chuẩn đầu ra môn học | Loại bỏ hoàn toàn khỏi phạm vi cẩm nang. |

---

## 3. Khung Trình Bày Mã Nguồn & Dòng Thực Thi (Execution Trace)

1. **Khối mã nguồn (Pale Editorial Code Blocks):** Không dùng giao diện dòng lệnh tối màu hay terminal giả lập. Mã nguồn được trình bày trên nền xám nhạt (`#eef2f2`), viền trái màu Teal (`#1e7881`), làm nổi bật từ khóa T-SQL, chuỗi ký tự và chú thích.
2. **Dòng thực thi truy vấn (Execution Trace):** Mỗi truy vấn phức tạp (như phép kết, gom nhóm hay phép chia) đều được phân rã thành các bước xử lý logic tuần tự:
   $$\text{FROM / JOIN} \longrightarrow \text{WHERE} \longrightarrow \text{GROUP BY} \longrightarrow \text{HAVING} \longrightarrow \text{SELECT} \longrightarrow \text{ORDER BY}$$
3. **Bảng kết quả (Result Tables):** Trình bày gọn gàng, làm nổi bật các ô dữ liệu quan trọng, hiển thị rõ ràng giá trị `NULL` và ghi chú đối chiếu.

---

## 4. Chuẩn Mực Trigger Dạng Tập Hợp (Multi-Row Safety)

Cẩm nang kiên quyết bác bỏ mẫu Trigger dùng biến vô hướng `SELECT @val = cot FROM inserted`. Tài liệu phân tích rõ:
- Khi một câu lệnh `INSERT` hàng loạt 100 dòng được thực thi, việc gán vào biến vô hướng chỉ lấy giá trị của 1 dòng bất kỳ, khiến 99 dòng vi phạm khác lọt qua lưới bảo vệ.
- Mẫu chuẩn tắc bắt buộc: Sử dụng `IF EXISTS (SELECT 1 FROM inserted i JOIN ... WHERE <vi phạm>) BEGIN RAISERROR(...); ROLLBACK TRAN; END` để đảm bảo an toàn giao dịch 100%.

---

## 5. Hệ Thống Chẩn Đoán Lỗi (Debugging System)

Áp dụng phương pháp luận 5 bước cho 6 nhóm lỗi T-SQL phổ biến nhất:
$$\text{TRIỆU CHỨNG} \longrightarrow \text{NGUYÊN NHÂN} \longrightarrow \text{CÁCH KIỂM TRA} \longrightarrow \text{CÁCH SỬA} \longrightarrow \text{CÁCH PHÒNG TRÁNH}$$
Giúp sinh viên tự tin xử lý sự cố trong phòng máy mà không cần hỗ trợ của giảng viên.
