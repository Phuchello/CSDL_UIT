---
title: Lỗi thường gặp (Common Errors)
description: Sổ chẩn đoán theo symptom, cause, verify, fix và liên kết liên quan.
type: error
topics: [debugging, sql-server]
related: [practice/debugging, errors/null-comparison, errors/group-by-8120, errors/multi-row-trigger-failure]
---
# Sổ chẩn đoán lỗi thường gặp (Common Errors)

Sổ tra cứu chẩn đoán và khắc phục lỗi thực hành SQL Server:

- [[practice/debugging|Quy trình chẩn đoán & gỡ lỗi SQL (Debugging)]]: Quy trình tái hiện, cô lập và sửa lỗi 4 bước.
- [[errors/null-comparison|Bẫy so sánh với NULL (NULL Comparison)]]: Bẫy so sánh trực tiếp `= NULL` trong mệnh đề `WHERE`.
- [[errors/group-by-8120|Lỗi Msg 8120 khi gom nhóm]]: Lỗi cột không hợp lệ trong mệnh đề chọn khi gom nhóm `GROUP BY`.
- [[errors/multi-row-trigger-failure|Sập trigger khi chạy batch nhiều dòng]]: Lỗi sập trigger khi xử lý nhiều dòng dữ liệu đồng thời.
- [[errors/fk-conflict|Xung đột ràng buộc khóa ngoại]]: Lỗi vi phạm ràng buộc toàn vẹn khóa ngoại.
- [[errors/check-conflict|Xung đột ràng buộc CHECK]]: Lỗi vi phạm miền giá trị ràng buộc `CHECK`.
