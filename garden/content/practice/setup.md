---
title: SQL Server setup
description: Database context, SSMS workflow và cách ghi lại script có thể chạy lại.
type: practice
topics: [sql-server, ssms, setup]
related: [lab-01, debugging, sql-server]
provenance: verified-artifact
technicalSources: [TECH-MS01]
---
# SQL Server setup

Mở SSMS, chọn đúng instance, tạo/chọn database, rồi chạy schema theo thứ tự. Mỗi script nên có `USE`, kiểm tra tồn tại đối tượng khi cần, và một đoạn SELECT xác nhận. Nếu gặp `Invalid object name`, xem [[wrong-database]] và [[invalid-object-column]].
