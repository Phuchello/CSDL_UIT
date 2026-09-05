---
title: Hai tầng phủ định tương quan (Double NOT EXISTS)
description: Kỹ thuật hai tầng phủ định tương quan trong T-SQL, chuyển đổi lượng từ phổ quát và phòng ngừa bẫy NULL.
type: theory
topics: [sql, exists, not-exists, universal-query, division]
related: [theory/division, practice/lab-03, errors/wrong-universal-candidate, errors/null-comparison, errors/not-in-null, cheat-sheets/universal-query]
provenance: original-practice
technicalSources: [TECH-A07]
---
# Hai tầng phủ định tương quan (Double NOT EXISTS)

Kỹ thuật hai tầng phủ định tương quan (`Double NOT EXISTS`) là phương pháp kinh điển và chuẩn tắc nhất để hiện thực hóa [[theory/division|Phép chia hình thức]] trong SQL Server, cho phép trả lời các câu hỏi mang lượng từ "Tất cả" mà không bị ảnh hưởng bởi bẫy logic giá trị rỗng NULL.

## 1. Cơ sở toán học: Chuyển đổi lượng từ

Trong logic vị từ hình thức, một phát biểu mang lượng từ phổ quát ($\forall$) có thể chuyển đổi tương đương sang phủ định của lượng từ tồn tại ($\exists$):
$$\forall y \in S, P(x, y) \iff \neg \exists y \in S, \neg P(x, y)$$

Áp dụng vào cơ sở dữ liệu:
> "Tìm sinh viên $x$ đã thi đạt **tất cả** các môn học $y$ trong danh mục $S$."
>
> $\iff$ "Tìm sinh viên $x$ sao cho **KHÔNG TỒN TẠI** một môn học $y$ nào trong $S$ mà **KHÔNG TỒN TẠI** kết quả thi đạt của sinh viên $x$ cho môn $y$ đó."

## 2. Cấu trúc 3 tầng chuẩn tắc

Một câu truy vấn `Double NOT EXISTS` luôn gồm 3 tầng lồng nhau:
1. **Tầng ngoài cùng (Outer Query):** Lấy danh sách từ tập ứng viên $X$ (ví dụ: `dbo.tr_students`). Bắt buộc phải là tập thực thể cần hiển thị, tránh [[errors/wrong-universal-candidate|lỗi chọn sai miền ứng viên]].
2. **Tầng giữa (Middle Subquery):** Lấy danh sách từ tập mục tiêu $Y$ (ví dụ: `dbo.tr_courses`). Đây là danh mục điều kiện chuẩn mà ứng viên phải thỏa mãn toàn bộ.
3. **Tầng trong cùng (Innermost Subquery):** Bảng bằng chứng liên kết $R$ (ví dụ: `dbo.tr_results`). Tại đây bắt buộc phải có hai điều kiện tương quan kết nối với cả tầng ngoài và tầng giữa: `r.StudentId = s.StudentId AND r.CourseId = c.CourseId`.

```sql
-- Cài đặt chuẩn tắc từ practice/lab-03.md trên fixture training-v1
SELECT s.StudentId
FROM dbo.tr_students AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.tr_courses AS c
    WHERE NOT EXISTS (
        SELECT 1
        FROM dbo.tr_results AS r
        WHERE r.StudentId = s.StudentId
          AND r.CourseId = c.CourseId
    )
);
```

## 3. Vì sao Double NOT EXISTS vượt trội hơn NOT IN và COUNT?

- **Miễn nhiễm hoàn toàn với bẫy NULL:** Phép toán `NOT IN` sẽ trả về tập rỗng ngay lập tức nếu truy vấn con chứa bất kỳ giá trị `NULL` nào do cơ chế logic 3 trị (3VL, xem [[errors/not-in-null|Bẫy NOT IN với NULL]]). Ngược lại, `NOT EXISTS` chỉ kiểm tra sự tồn tại của dòng (tồn tại ít nhất một dòng hay không) nên hoàn toàn không bị ảnh hưởng bởi giá trị của các cột trong danh sách chọn (xem [[errors/null-comparison|So sánh với NULL]]).
- **Bảo toàn ngữ nghĩa tập hợp:** So với phương pháp gom nhóm đếm `HAVING COUNT(DISTINCT CourseId) = ...`, `Double NOT EXISTS` phản ánh đúng ngữ nghĩa của phép chia đại số quan hệ và hoạt động chuẩn xác ngay cả khi danh mục yêu cầu có các cấu trúc ràng buộc phức tạp.

Xem hướng dẫn thực thi trên cơ sở dữ liệu mẫu tại [[practice/lab-03|Lab 03 — Truy vấn nâng cao]], lý thuyết phép toán tại [[theory/division|Phép chia hình thức]], và bảng tra cứu đối chiếu tại [[cheat-sheets/universal-query|Bảng tra truy vấn phổ dụng "Tất cả"]]. Căn cứ kỹ thuật Microsoft Learn [[sources/technical|TECH-A07]].
