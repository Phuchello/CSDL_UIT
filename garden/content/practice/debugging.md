---
title: SQL debugging workflow
description: Quy trình tái hiện, khoanh vùng, kiểm tra và sửa lỗi SQL Server.
type: practice
topics: [debugging, sql-server, reproducibility]
related: [setup, invalid-object-column, group-by-8120, multi-row-trigger-failure, errors]
provenance: original-practice
technicalSources: [TECH-MS06]
---
# SQL debugging workflow

1. Ghi database context và câu lệnh tối thiểu tái hiện.
2. Đọc message, kiểm tra object/column/kiểu dữ liệu và số dòng.
3. Chạy SELECT kiểm chứng trước khi sửa.
4. Sửa nhỏ, chạy lại cả case một dòng và nhiều dòng.

Tra symptom cụ thể trong [[errors]]; không suy luận từ một kết quả “trông có vẻ đúng”.
