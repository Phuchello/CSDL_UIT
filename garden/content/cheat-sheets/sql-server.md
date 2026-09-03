---
title: Bảng tra cú pháp SQL Server
description: Context, kiểu ngày, NULL và kiểm thử batch.
type: cheatsheet
topics: [sql-server, ssms]
related: [practice/setup, errors/date-conversion, errors/null-comparison, practice/multi-row-trigger, practice/debugging]
provenance: original-practice
technicalSources: [TECH-A01, TECH-A02]
---
# Bảng tra cú pháp SQL Server (SQL Server Cheat Sheet)

Bảng kiểm tra nhanh quy tắc môi trường T-SQL:

- **Ngữ cảnh cơ sở dữ liệu:** Luôn kiểm tra `SELECT DB_NAME()` hoặc dùng lệnh `USE IT004_Training; GO` trước khi thực thi script (xem [[practice/setup|Setup]]).
- **Định dạng ngày tháng:** Sử dụng chuẩn ISO `YYYY-MM-DD` hoặc `YYYYMMDD` để tránh lỗi chuyển đổi định dạng (xem [[errors/date-conversion|Date conversion]]).
- **Xử lý NULL:** Luôn dùng `IS NULL` / `IS NOT NULL`, không dùng so sánh trực tiếp `= NULL` (xem [[errors/null-comparison|Bẫy so sánh với NULL (NULL Comparison)]]).
- **Thiết kế Trigger:** Luôn xử lý theo tập hợp dữ liệu (`inserted` và `deleted`), không dùng biến vô hướng (xem [[practice/multi-row-trigger|Multi-row trigger]]).
- **Quy trình chẩn đoán lỗi:** Phân tích mã lỗi hệ thống và kiểm thử đơn vị xem tại [[practice/debugging|Debugging]]. Căn cứ kỹ thuật Microsoft Learn [[sources/technical|TECH-A01, TECH-A02]].
