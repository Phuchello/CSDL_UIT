USE IT004_Training;
GO

/* These checks are deliberately wrapped in transactions. The failing cases
   are commented so a student can enable one at a time and observe the error. */

-- A. UPDATE HOTEN of head: PASS
BEGIN TRANSACTION;
UPDATE dbo.tr_employees SET FullName = N'Lan Nguyễn (đã kiểm tra)' WHERE EmployeeId = 'E001';
SELECT EmployeeId, FullName FROM dbo.tr_employees WHERE EmployeeId = 'E001';
ROLLBACK TRANSACTION;

-- B. UPDATE Salary/HESO analogue: PASS
BEGIN TRANSACTION;
UPDATE dbo.tr_employees SET Salary = Salary * 1.05 WHERE EmployeeId = 'E001';
ROLLBACK TRANSACTION;

-- C. UPDATE DeptId to the same department: PASS
BEGIN TRANSACTION;
UPDATE dbo.tr_employees SET DeptId = 'D001' WHERE EmployeeId = 'E001';
ROLLBACK TRANSACTION;

-- D. UPDATE DeptId to another department: REJECT 51003
-- UPDATE dbo.tr_employees SET DeptId = 'D002' WHERE EmployeeId = 'E001';

-- E. UPDATE DeptId to NULL: blocked by NOT NULL before the trigger.
-- UPDATE dbo.tr_employees SET DeptId = NULL WHERE EmployeeId = 'E001';

-- F. DELETE department head: REJECT 51002
-- DELETE FROM dbo.tr_employees WHERE EmployeeId = 'E001';

-- G. Multi-row unrelated UPDATE: PASS; no scalar assumption.
BEGIN TRANSACTION;
UPDATE dbo.tr_employees SET Salary = Salary + 10 WHERE DeptId = 'D001';
ROLLBACK TRANSACTION;

-- H. Multi-row violating DeptId UPDATE: REJECT whole statement, then rollback.
-- UPDATE dbo.tr_employees SET DeptId = 'D002' WHERE DeptId = 'D001';
GO
