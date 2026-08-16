# Source Conflicts – IT004 CSDL UIT

> Ghi nhận các khác biệt giữa các nguồn tài liệu.

## Ký hiệu và Thuật ngữ

| Vấn đề | Nguồn 1 | Nguồn 2 | Quyết định | Lý do |
|---|---|---|---|---|
| Ký hiệu Natural Join | Slide UIT: ⋈ | Textbook: ⋈ (giống) | ⋈ | Thống nhất |
| Ký hiệu Division | Slide UIT: ÷ | Một số textbook: / | ÷ | Theo UIT |
| Tên gọi "Tân từ" vs "Predicate" | Slide UIT: Tân từ | Textbook: Predicate | Tân từ (Predicate) | Theo UIT, ghi Anh trong ngoặc |

## Bảng tầm ảnh hưởng

| Vấn đề | Nguồn 1 | Nguồn 2 | Quyết định |
|---|---|---|---|
| Ký hiệu "+(A)" | Slide UIT bộ 1 | Slide UIT bộ 2 (2024) | Theo bộ 2024 (mới hơn) |
| Ký hiệu + / - | Cả 2 bộ slide đều dùng | — | Thống nhất |

## SQL Dialect

| Vấn đề | SQL Server | Textbook/Generic SQL | Quyết định |
|---|---|---|---|
| TOP vs LIMIT | TOP (T-SQL) | LIMIT (MySQL/PostgreSQL) | TOP — theo SQL Server |
| YEAR() function | YEAR(date) | EXTRACT(YEAR FROM date) | YEAR() — theo SQL Server |
| String concat | + operator | \|\| operator | + — theo SQL Server |
| Identity column | IDENTITY(1,1) | AUTO_INCREMENT | IDENTITY — theo SQL Server |

## Phụ thuộc hàm

| Vấn đề | Textbook A | Textbook B | Quyết định |
|---|---|---|---|
| Pseudotransitivity | Có dạy | Một số sách bỏ qua | Dạy (theo UIT slide) |
| Tìm ALL candidate keys | Dạy branching | Dạy brute force | Dạy phương pháp phân tích LHS/RHS/cả hai + branching |

## Không phát hiện mâu thuẫn nghiêm trọng

Các nguồn UIT chính thức (2 bộ slide) nhìn chung thống nhất về nội dung. Sự khác biệt chủ yếu ở mức trình bày và chi tiết.
