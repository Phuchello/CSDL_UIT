---
title: "Tài liệu kỹ thuật & Chuẩn T-SQL (Technical Sources)"
description: Microsoft Learn và tài liệu chuẩn dùng cho các ghi chú kỹ thuật T-SQL.
type: source
topics: [sources, microsoft, provenance]
related: [practice/setup, practice/multi-row-trigger, cheat-sheets/sql-server]
provenance: verified-artifact
technicalSources: [TECH-A01, TECH-A02, TECH-A03, TECH-A04, TECH-A05, TECH-A06, TECH-A07, TECH-A08, TECH-A09, TECH-A10, TECH-A11]
---
# Tài liệu kỹ thuật & Chuẩn T-SQL (Technical Sources)

Các tài liệu kỹ thuật chuẩn mực từ Microsoft Learn (Authority Tier A) được dùng để định chuẩn cú pháp, ngữ nghĩa thực thi và cơ chế hoạt động của SQL Server trong toàn bộ cẩm nang và vườn tri thức:

- **TECH-A01** — [CREATE TABLE (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql): Cú pháp DDL, khóa chính, khóa ngoại, kiểu dữ liệu, NULL và DEFAULT.
- **TECH-A02** — [SELECT - GROUP BY](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-group-by-transact-sql): Gom nhóm, hàm kết hợp `COUNT`, `SUM`, `AVG`, mệnh đề `HAVING`.
- **TECH-A03** — [CREATE CHECK Constraints](https://learn.microsoft.com/en-us/sql/relational-databases/tables/create-check-constraints): Ràng buộc toàn vẹn khai báo trên một quan hệ.
- **TECH-A04** — [CREATE TRIGGER (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-trigger-transact-sql): Khai báo DML Trigger, các sự kiện AFTER INSERT/UPDATE/DELETE.
- **TECH-A05** — [Use inserted and deleted tables](https://learn.microsoft.com/en-us/sql/relational-databases/triggers/use-the-inserted-and-deleted-tables): Cơ chế hai bảng ảo tạm thời trong bộ nhớ.
- **TECH-A06** — [Handle multiple rows in DML triggers](https://learn.microsoft.com/en-us/sql/relational-databases/triggers/create-dml-triggers-to-handle-multiple-rows-of-data): Thiết kế trigger dạng tập hợp an toàn đa dòng qua `JOIN`.
- **TECH-A07** — [EXISTS (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/exists-transact-sql): Vị từ tồn tại, correlated subquery và kỹ thuật Double NOT EXISTS.
- **TECH-A08** — [SET Operators - UNION](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/set-operators-union-transact-sql): Các toán tử tập hợp `UNION`, `EXCEPT`, `INTERSECT`.
- **TECH-A09** — [CREATE PROCEDURE (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-procedure-transact-sql): Thủ tục lưu trữ và tham số.
- **TECH-A10** — [CREATE VIEW (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-view-transact-sql): Khung nhìn và truy vấn ảo.
- **TECH-A11** — [CREATE FUNCTION (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-function-transact-sql): Hàm người dùng định nghĩa (UDF).

Xem thêm sổ nguồn môn học tại [[sources/course|Tài liệu học phần (Course Sources)]] và hướng dẫn cài đặt [[practice/setup|Cài đặt môi trường thực hành (Setup)]].
