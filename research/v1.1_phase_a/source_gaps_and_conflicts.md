# Hồ Sơ Khoảng Trống, Xung Đột & Bản Quyền Nguồn (Source Gaps, Conflicts, and Rights) — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31
**Mục đích:** Ghi nhận minh bạch toàn bộ các điểm nghẽn tiếp cận, giải quyết các xung đột học thuật/ký hiệu và xác lập ranh giới bản quyền an toàn cho dự án.

---

## 1. Giải Quyết Toàn Diện Nhãn "ACCESS BLOCKED" Trước Đây

Trong đợt kiểm toán này, toàn bộ 6 tệp đính kèm cục bộ đã được tiếp cận và kiểm thử trực tiếp:
- `CSDL_UIT_LOCAL_LECTURES_PART1.pdf` (94 trang) $\rightarrow$ Phục hồi `LOC-LEC-AN-CH01`, `LOC-LEC-AN-CH02`, `LOC-LEC-LONG-CH01`, `LOC-LEC-LONG-CH02`, `LOC-LEC-LONG-CH03`.
- `CSDL_UIT_LOCAL_LECTURES_PART2.pdf` (94 trang) $\rightarrow$ Phục hồi `LOC-LEC-LONG-CH05`, `LOC-LEC-LONG-CH06`.
- `CSDL_UIT_LOCAL_EXAMS_REVIEW.pdf` (25 trang) $\rightarrow$ Phục hồi `LOC-EXAM-2023-2024-MID-D1`, `LOC-EXAM-2023-2024-MID-D2`, `LOC-EXAM-K18-2024-1-SOL`, `LOC-REV-2024-10-01`, `LOC-REV-DSQH-2024`, `LOC-HW-23520266-1`, `LOC-HW-23520266-2`.
- `CSDL_UIT_LOCAL_LABS_AND_SQL.txt` (114 KB) $\rightarrow$ Phục hồi `LOC-SQL-LAB01`, `LOC-SQL-LAB02`, `LOC-SQL-LAB03`, `LOC-SQL-LAB04`, `LOC-SQL-LAB04-ALL`, `LOC-NOTE-NHAP`.
- `QLBANHANG.xlsx` (5 sheets) $\rightarrow$ Phục hồi `LOC-XLSX-QLBH`.
- `23520266_Homework5_CSDL.docx` (533 đoạn) $\rightarrow$ Phục hồi `LOC-HW-23520266-5`.

**Toàn bộ các mục `ACCESS BLOCKED` trong sổ đăng ký nguồn đã được giải phóng thành công và chuyển hóa thành các nguồn tài liệu có bằng chứng kiểm chứng trực tiếp.**

---

## 2. Các Khoảng Trống Học Thuật Còn Lại (Remaining Gaps & Limitations)

1. **Kho đề thi chính thức công khai trực tuyến**:
   - Trường ĐH Công nghệ Thông tin không công khai toàn văn đề thi các năm trên cổng thông tin chung. Đề thi chỉ được lưu hành nội bộ trong phòng thi hoặc lưu truyền qua các bản sao chép/chụp ảnh của sinh viên (community mirrors).
   - Vì vậy, các hiện vật đề thi đều được xếp vào nhóm `strong-provenance-local` hoặc `community-mirror`, không dán nhãn `official-public` khi không có URL cổng trường chính thức.

2. **Tính thẩm quyền của bài làm sinh viên**:
   - Bài làm trong `23520266_Homework5_CSDL.docx`, `LOC-EXAM-K18-2024-1-SOL` và các kho GitHub của sinh viên chỉ là **bằng chứng về hoạt động học tập (evidence of course activity)**, không phải đáp án chuẩn tắc. Mọi lời giải phải được thẩm định lại qua Microsoft Learn và giáo trình quốc tế.

3. **Giới hạn tải xuống tài liệu từ Studocu/Scribd**:
   - Một số trang yêu cầu tài khoản sinh viên đăng bài hoặc trả phí để mở khóa toàn bộ tệp; dự án chỉ sử dụng bản xem trước (preview) và đối chiếu với bản gốc cục bộ.

---

## 3. Bảng Quyết Định Xử Lý Xung Đột Học Thuật (Conflict Resolution Ledger)

| Vấn đề học thuật | Các nguồn xung đột | Quyết định xử lý chuẩn mực cho v1.1 |
| :--- | :--- | :--- |
| **Ký hiệu Phép chiếu ĐSQH** | Slide ThS. Long dùng $R[X]$, giáo trình quốc tế dùng $\pi_X(R)$ | Trình bày $\pi_X(R)$ làm cú pháp chuẩn, đồng thời giải thích rõ ký hiệu $R[X]$ thường gặp trong các đề thi và bài giảng tại UIT. |
| **Ký hiệu Phép gom nhóm $\Im$** | Một số slide dùng $\gamma$, Slide ThS. Long dùng $_{G_1..G_n}\Im_{F_1..F_m}(E)$ | Chuẩn hóa theo ký hiệu $\Im$ của Khoa HTTT – UIT, nêu chú thích đối chiếu với ký hiệu $\gamma$ của Silberschatz. |
| **Thuật toán tìm khóa** | Sách v1.0 dùng $L/R/N/LR$, Slide ThS. Long dùng Tập nguồn $Ng$, trung gian $Tg$, treo $Tr$ | Tích hợp song song: $Ng = L$, $Tg = LR$, $Tr = N$. Hướng dẫn sinh viên cách lập bảng theo cả 2 phương pháp. |
| **Phương ngữ SQL (Dialect)** | PostgreSQL dùng `LIMIT/OFFSET`, MySQL dùng `AUTO_INCREMENT`, Oracle dùng `||` | **100% chuẩn hóa Transact-SQL (SQL Server)**: Dùng `TOP (n) [WITH TIES]`, `IDENTITY(1,1)`, phép nối chuỗi `+`, các hàm ngày `DATEDIFF`, `DATEADD`, `YEAR`, `MONTH`. |
| **An toàn Đa dòng trong Trigger** | Mã sinh viên thường gán biến vô hướng (`SELECT @var = col FROM inserted`), Microsoft khuyến cáo set-based | **Quy chuẩn 100% Trigger dạng tập hợp (Set-based)**: Luôn dùng `INNER JOIN inserted` hoặc `EXISTS (SELECT 1 FROM inserted ...)` để xử lý an toàn cho lệnh `INSERT` nhiều dòng. |
| **Phép chia SQL** | Cách 1: Double `NOT EXISTS`<br>Cách 2: `GROUP BY ... HAVING COUNT` | Giải thích cả 2 cách: Double `NOT EXISTS` là chuẩn tắc hình thức ĐSQH, `GROUP BY / HAVING COUNT` là cách viết nhanh trong thực hành phòng máy có ràng buộc dữ liệu. |

---

## 4. Chính Sách Bản Quyền & Tái Phân Phối An Toàn (Copyright & Safety Boundaries)

1. **Tuyệt đối không đẩy (commit/push) các tệp nguồn có bản quyền lên kho lưu trữ GitHub công khai**:
   - Không commit các slide bài giảng PDF của giảng viên.
   - Không commit ảnh chụp/scan đề thi của Trường.
   - Không commit tệp Word/Excel chứa bài nộp cá nhân của sinh viên (`23520266_...`, `QLBANHANG.xlsx`).
   - Không commit các tài liệu trích xuất từ Studocu/Scribd.

2. **Nội dung được phép lưu trữ trên GitHub**:
   - Bảng danh mục siêu dữ liệu nguồn (`source_inventory.md`).
   - Bảng đăng ký hiện vật chuẩn hóa (`artifact_registry.md`).
   - Các bài tập và câu hỏi được tác giả biên soạn độc lập (`reconstructed-exam-pattern`, `original-practice`).
   - Sơ đồ kiến trúc vector do chính tác giả thiết kế (`it004-knowledge-map.svg`).
   - Mã nguồn cẩm nang HTML/CSS và công cụ kiểm thử tự động độc lập.
