---
title: "Quy trình chẩn đoán & Gỡ lỗi SQL (Debugging Workflow)"
description: Quy trình tái hiện, khoanh vùng, kiểm tra và sửa lỗi SQL Server.
type: practice
topics: [debugging, sql-server, reproducibility]
related: [practice/setup, errors/invalid-object-column, errors/group-by-8120, errors/multi-row-trigger-failure, errors/index]
provenance: original-practice
technicalSources: [TECH-A01, TECH-A03, TECH-A04, TECH-A05]
---
# Quy trình chẩn đoán & Gỡ lỗi SQL (Debugging Workflow)

Quy trình 4 bước chuẩn tắc để cô lập và xử lý triệt để các lỗi T-SQL trong môi trường thực hành:

1. **Ghi nhận ngữ cảnh cơ sở dữ liệu và tái hiện tối thiểu:** Kiểm tra ngữ cảnh database hiện tại với [[practice/setup|Setup]] và cô lập câu truy vấn tối thiểu gây ra lỗi.
2. **Phân tích thông báo lỗi hệ thống:** Đọc kỹ mã lỗi (Error Number) và dòng thông báo (Error Message), phân định rõ giữa lỗi sai đối tượng/cột ([[errors/invalid-object-column|Invalid object/column name]]), lỗi gom nhóm ([[errors/group-by-8120|Msg 8120]]), hay lỗi logic batch ([[errors/multi-row-trigger-failure|Multi-row trigger failure]]).
3. **Chạy câu lệnh kiểm chứng dữ liệu:** Chạy truy vấn `SELECT` kiểm tra dữ liệu trước khi thay đổi để xác định miền giá trị vi phạm.
4. **Sửa đổi và kiểm thử hồi quy:** Sửa từng đoạn mã nhỏ, kiểm thử lại trên cả trường hợp đơn dòng và trường hợp batch nhiều dòng.

Xem toàn bộ danh mục triệu chứng lỗi và cách khắc phục tại [[errors/index|Danh mục lỗi thường gặp]]. Căn cứ tài liệu Microsoft Learn [[sources/technical|TECH-A01, TECH-A03, TECH-A04, TECH-A05]].
