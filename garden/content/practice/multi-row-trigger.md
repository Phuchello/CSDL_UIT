---
title: Multi-row trigger
description: Mẫu trigger an toàn đa dòng với cơ chế phân biệt sự kiện DELETE và UPDATE.
type: practice
topics: [trigger, multi-row, sql-server]
related: [theory/rbtv-impact, practice/lab-04, errors/scalar-trigger, errors/multi-row-trigger-failure, practice/debugging]
provenance: original-practice
fixture: training-v1
technicalSources: [TECH-A04, TECH-A05, TECH-A06]
---
# Multi-row trigger

Trong SQL Server, câu lệnh DML tác động trên tập hợp dòng. Mọi DML Trigger phải được thiết kế dạng tập hợp (set-based), xử lý đồng thời nhiều dòng trong các bảng ảo `inserted` và `deleted` mà không dùng biến vô hướng (scalar variable, xem [[errors/scalar-trigger|scalar-trigger]]).

## Hợp đồng phân biệt sự kiện DELETE và UPDATE

Khi sự kiện `UPDATE` xảy ra, SQL Server tự động đưa giá trị cũ vào `deleted` và giá trị mới vào `inserted`. Vì vậy, một trigger khai báo `AFTER DELETE, UPDATE` nếu kiểm tra `deleted` một cách đơn giản mà không đối chiếu với `inserted` sẽ bắt nhầm mọi thao tác `UPDATE` (ngay cả khi chỉ sửa thông tin không liên quan như lương hay họ tên).

Trong lược đồ chuẩn tắc [[practice/setup|fixture training-v1]] (`tr_departments`, `tr_employees`), ràng buộc toàn vẹn quy định: *Trưởng bộ phận (`HeadEmployeeId`) phải là nhân viên thuộc chính phòng ban đó (`DeptId`), và không thể xóa nhân viên đang giữ chức vụ trưởng bộ phận*.

```sql
-- Cài đặt chuẩn tắc trong practice/sql/05_triggers.sql
-- Lưu ý thứ tự thẩm định trong SQL Server: Khóa ngoại được kiểm tra TRƯỚC AFTER trigger.
-- Khóa ngoại FK_tr_departments_head ngăn chặn xóa trưởng bộ phận ở mức khai báo (Msg 547).
-- Do đó, trigger chỉ cần quản lý sự kiện AFTER UPDATE cho các nghiệp vụ mà DDL không thể diễn đạt.
CREATE TRIGGER dbo.trg_tr_employees_head_guard
ON dbo.tr_employees
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    -- Nhánh UPDATE DeptId:
    -- Chỉ kiểm tra khi cột DeptId bị tác động và nhân viên là trưởng bộ phận.
    -- Lưu ý: i.DeptId IS NULL là logic phòng vệ sâu (defensive programming);
    -- trong fixture training-v1, cột DeptId đã có ràng buộc NOT NULL ở cấp schema.
    IF UPDATE(DeptId) AND EXISTS (
        SELECT 1
        FROM inserted AS i
        JOIN dbo.tr_departments AS dep ON dep.HeadEmployeeId = i.EmployeeId
        WHERE i.DeptId IS NULL OR i.DeptId <> dep.DeptId
    )
    BEGIN
        THROW 51003, 'A department head must remain in the same department.', 1;
    END;
END;
GO
```

## Ma trận thẩm định tĩnh các kịch bản kiểm thử

Theo hợp đồng kiểm thử đã được chuẩn hóa trong [[theory/rbtv-impact|Bảng tầm ảnh hưởng]]:

| Kịch bản | Thao tác | Hành vi mong đợi | Cơ chế bắt lỗi |
| :--- | :--- | :---: | :--- |
| **A. Sửa thông tin ngoài** | `UPDATE tr_employees SET Salary = Salary * 1.1 WHERE EmployeeId = ...` | **PASS** | `UPDATE(DeptId)` trả về FALSE $\rightarrow$ bỏ qua kiểm tra, cập nhật an toàn. |
| **B. Đổi DeptId về cùng phòng** | `UPDATE tr_employees SET DeptId = DeptId WHERE EmployeeId = ...` | **PASS** | Không thỏa mãn điều kiện `i.DeptId <> dep.DeptId`. |
| **C. Đổi DeptId sang phòng khác** | `UPDATE tr_employees SET DeptId = 'D02' WHERE EmployeeId = 'E01'` | **REJECT** | Bị chặn bởi nhánh `UPDATE(DeptId)` của trigger $\rightarrow$ `THROW 51003`. |
| **D. Đổi DeptId thành NULL** | `UPDATE tr_employees SET DeptId = NULL WHERE EmployeeId = 'E01'` | **REJECT** | **Cấp Schema:** Cột `DeptId` khai báo `NOT NULL` trong `01_schema.sql` chặn trực tiếp tại DDL engine (Msg 515); điều kiện `i.DeptId IS NULL` trong trigger là lớp phòng vệ sâu (defensive logic). |
| **E. Xóa trưởng bộ phận** | `DELETE FROM tr_employees WHERE EmployeeId = 'E01'` | **REJECT** | **Cấp Khai báo (Declarative):** Khóa ngoại `FK_tr_departments_head` được SQL Server kiểm tra trước `AFTER` trigger $\rightarrow$ chặn trực tiếp ở tầng DDL với `Msg 547`. Nhánh `AFTER DELETE` không bao giờ được kích hoạt. |
| **F. Thao tác đa dòng có 1 lỗi** | `UPDATE tr_employees SET DeptId = 'D02'` | **REJECT TOÀN BỘ** | `IF EXISTS` phát hiện ít nhất 1 dòng vi phạm $\rightarrow$ hủy toàn bộ batch (tính nguyên tố ACID). |

Tham khảo quy trình chẩn đoán lỗi trong [[practice/debugging|debugging]] và kịch bản sập logic trong [[errors/multi-row-trigger-failure|multi-row-trigger-failure]]. Căn cứ tài liệu kỹ thuật Microsoft [[sources/technical|TECH-A04, TECH-A05, TECH-A06]].
