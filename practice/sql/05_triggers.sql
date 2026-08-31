USE IT004_Training;
GO

IF OBJECT_ID(N'dbo.trg_tr_departments_head_guard', N'TR') IS NOT NULL
    DROP TRIGGER dbo.trg_tr_departments_head_guard;
IF OBJECT_ID(N'dbo.trg_tr_employees_head_guard', N'TR') IS NOT NULL
    DROP TRIGGER dbo.trg_tr_employees_head_guard;
GO

/* Department INSERT/UPDATE: a head must exist and belong to that department. */
CREATE TRIGGER dbo.trg_tr_departments_head_guard
ON dbo.tr_departments
AFTER INSERT, UPDATE
AS
BEGIN
    SET NOCOUNT ON;
    IF EXISTS (
        SELECT 1
        FROM inserted AS d
        LEFT JOIN dbo.tr_employees AS e
          ON e.EmployeeId = d.HeadEmployeeId
         AND e.DeptId = d.DeptId
        WHERE d.HeadEmployeeId IS NOT NULL
          AND e.EmployeeId IS NULL
    )
    BEGIN
        THROW 51001, 'Department head must be an employee of the same department.', 1;
    END;
END;
GO

/*
  Combined DELETE/UPDATE trigger with event discrimination.
  UPDATE HOTEN or SALARY leaves inserted rows present and does not enter
  the DELETE branch. Every test below is statement-level and set-based.
*/
CREATE TRIGGER dbo.trg_tr_employees_head_guard
ON dbo.tr_employees
AFTER DELETE, UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    /* DELETE: deleted row has no matching inserted row. */
    IF EXISTS (
        SELECT 1
        FROM deleted AS d
        JOIN dbo.tr_departments AS dep ON dep.HeadEmployeeId = d.EmployeeId
        LEFT JOIN inserted AS i ON i.EmployeeId = d.EmployeeId
        WHERE i.EmployeeId IS NULL
    )
    BEGIN
        THROW 51002, 'A department head cannot be deleted.', 1;
    END;

    /* UPDATE DeptId: check only surviving heads whose department changed. */
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
