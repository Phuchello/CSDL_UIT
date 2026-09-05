---
title: Lab 03 — Truy vấn nâng cao (Advanced Queries)
description: Double NOT EXISTS, tập hợp, ngày tháng và NULL trên fixture training-v1.
type: practice
topics: [advanced-query, division, exists, null, set-operators]
related: [theory/division, theory/double-not-exists, errors/wrong-universal-candidate, errors/not-in-null, errors/unsafe-date-equality]
provenance: verified-artifact
fixture: training-v1
technicalSources: [TECH-A07, TECH-A08]
---
# Lab 03 — Truy vấn nâng cao (Advanced Queries)

Trong phòng thực hành, các bài toán phức tạp đòi hỏi kết hợp nhiều kỹ thuật suy luận ngữ nghĩa SQL:

Fixture chuẩn tắc dùng đúng các bảng `tr_students`, `tr_courses`, `tr_results` trong cơ sở dữ liệu huấn luyện; mã sinh viên mẫu là `S001`. Đây là mô tả tĩnh của script, chưa phải kết quả đã chạy.

```sql
SELECT s.StudentId
FROM dbo.tr_students AS s
WHERE NOT EXISTS (
  SELECT 1 FROM dbo.tr_courses AS c
  WHERE NOT EXISTS (
    SELECT 1 FROM dbo.tr_results AS r
    WHERE r.StudentId = s.StudentId AND r.CourseId = c.CourseId
  )
);
```

Nguyên lý hoạt động:
- Cấu trúc hai tầng tương quan hiện thực hóa bài toán [[theory/division|Phép chia]] hình thức: *Tìm sinh viên mà KHÔNG tồn tại khóa học nào mà sinh viên đó CHƯA có kết quả*. Chi tiết xem tại [[theory/double-not-exists|Kỹ thuật Double NOT EXISTS]].
- Kiểm tra cẩn thận miền ứng viên để tránh [[errors/wrong-universal-candidate|Sai miền ứng viên]].
- Tránh lỗi toán tử tập hợp khi có giá trị rỗng với [[errors/not-in-null|Bẫy NOT IN với NULL]].
- Thao tác so sánh ngày tháng chuẩn xác, tránh [[errors/unsafe-date-equality|So sánh ngày không an toàn]]. Căn cứ tài liệu kỹ thuật Microsoft [[sources/technical|TECH-A07, TECH-A08]].
