---
title: Lab 01 — DDL và ràng buộc toàn vẹn
description: Tạo bảng, khoá và ràng buộc trên SQL Server.
type: practice
topics: [ddl, constraints, sql-server]
related: [practice/setup, errors/fk-conflict, errors/check-conflict, errors/duplicate-key]
provenance: verified-artifact
fixture: training-v1
technicalSources: [TECH-A01, TECH-A03]
---
# Lab 01 — DDL và ràng buộc toàn vẹn

Thực hành tạo lập bảng và ràng buộc toàn vẹn khai báo trên SQL Server trong môi trường [[practice/setup|Setup]]:

- **Thứ tự tạo bảng:** Tạo các bảng cha (không chứa khóa ngoại) trước, sau đó mới tạo các bảng con có khóa ngoại tham chiếu.
- **Ràng buộc khóa chính và duy nhất:** Khai báo `PRIMARY KEY` (không chấp nhận NULL) và `UNIQUE` để định danh bộ dữ liệu, phòng ngừa [[errors/duplicate-key|Lỗi trùng lặp khóa chính]].
- **Ràng buộc khóa ngoại và miền giá trị:** Khai báo `FOREIGN KEY` tham chiếu để tránh [[errors/fk-conflict|Lỗi xung đột khóa ngoại]], và thiết lập `CHECK` constraints để tránh [[errors/check-conflict|Lỗi vi phạm miền giá trị]]. Căn cứ kỹ thuật Microsoft Learn [[sources/technical|TECH-A01, TECH-A03]].
