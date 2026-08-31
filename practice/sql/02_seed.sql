USE IT004_Training;
GO

DELETE FROM dbo.tr_results;
DELETE FROM dbo.tr_order_items;
DELETE FROM dbo.tr_orders;
UPDATE dbo.tr_departments SET HeadEmployeeId = NULL;
DELETE FROM dbo.tr_employees;
DELETE FROM dbo.tr_departments;
DELETE FROM dbo.tr_students;
DELETE FROM dbo.tr_courses;
DELETE FROM dbo.tr_products;
DELETE FROM dbo.tr_customers;
GO

INSERT INTO dbo.tr_customers (CustomerId, FullName, City, RegisteredOn, CreditLimit, Segment)
VALUES
    ('C001', N'An Phạm',   N'Thủ Đức',  '20240115', 5000.00, 'A'),
    ('C002', N'Bình Lê',   N'Gò Vấp',   '20240201', 2500.00, 'B'),
    ('C003', N'Chi Trần',  N'Quận 3',   '20240310', 3000.00, 'B'),
    ('C004', N'Dũng Võ',   N'Bình Thạnh','20240320', 1800.00, 'C'),
    ('C005', N'Eva Đỗ',    N'Tân Bình', '20240401', 1200.00, 'C');

INSERT INTO dbo.tr_products (ProductId, ProductName, Category, Country, Price, Stock, IsActive)
VALUES
    ('P001', N'Laptop học tập', N'Thiết bị', N'Việt Nam', 1200.00, 8, 1),
    ('P002', N'Chuột không dây', N'Phụ kiện', N'Singapore', 25.00, 30, 1),
    ('P003', N'Bàn phím cơ', N'Phụ kiện', N'Singapore', 45.00, 20, 1),
    ('P004', N'Ghế công thái học', N'Nội thất', N'Việt Nam', 150.00, 6, 1),
    ('P005', N'Đèn bàn', N'Nội thất', N'Malaysia', 35.00, 12, 1),
    ('P006', N'Màn hình 24 inch', N'Thiết bị', N'Việt Nam', 300.00, 10, 1),
    ('P007', N'Webcam học trực tuyến', N'Thiết bị', N'Việt Nam', 80.00, 5, 1);

INSERT INTO dbo.tr_orders (OrderId, CustomerId, OrderDate, Status)
VALUES
    (1001, 'C001', '2024-10-15T09:10:00', 'PAID'),
    (1002, 'C001', '2024-10-16T15:30:00', 'PAID'),
    (1003, 'C002', '2024-10-16T10:00:00', 'PAID'),
    (1004, 'C003', '2024-10-17T11:20:00', 'PENDING'),
    (1005, 'C004', '2024-11-02T08:45:00', 'PAID');

INSERT INTO dbo.tr_order_items (OrderId, ProductId, Qty, UnitPrice)
VALUES
    (1001, 'P001', 1, 1200.00), (1001, 'P002', 2, 25.00),
    (1002, 'P003', 1, 45.00),  (1002, 'P004', 2, 150.00),
    (1003, 'P002', 1, 25.00),   (1003, 'P005', 3, 35.00),
    (1004, 'P004', 1, 150.00),  (1004, 'P006', 1, 300.00),
    (1005, 'P001', 1, 1200.00), (1005, 'P003', 2, 45.00), (1005, 'P006', 1, 300.00);

INSERT INTO dbo.tr_departments (DeptId, DeptName, HeadEmployeeId)
VALUES ('D001', N'Dữ liệu', NULL), ('D002', N'Kiểm thử', NULL);

INSERT INTO dbo.tr_employees (EmployeeId, FullName, DeptId, ManagerId, Salary)
VALUES
    ('E001', N'Lan Nguyễn', 'D001', NULL, 2100.00),
    ('E002', N'Minh Trần',  'D001', 'E001', 1500.00),
    ('E003', N'An Lê',     'D001', 'E001', 1450.00),
    ('E004', N'Bình Phạm', 'D002', NULL, 1900.00);

UPDATE dbo.tr_departments SET HeadEmployeeId = 'E001' WHERE DeptId = 'D001';
UPDATE dbo.tr_departments SET HeadEmployeeId = 'E004' WHERE DeptId = 'D002';

INSERT INTO dbo.tr_students (StudentId, FullName, Cohort)
VALUES ('S001', N'Hà Nguyễn', 'K20'), ('S002', N'Khoa Trần', 'K20'),
       ('S003', N'Linh Phạm', 'K21'), ('S004', N'Mai Võ', 'K21');

INSERT INTO dbo.tr_courses (CourseId, CourseName, Credits)
VALUES ('C101', N'Cơ sở dữ liệu', 3), ('C102', N'SQL Server', 3), ('C103', N'Mô hình ER', 2);

/* S001 has a retake for C101; COUNT(DISTINCT CourseId) must count that course once. */
INSERT INTO dbo.tr_results (StudentId, CourseId, AttemptNo, Score)
VALUES
    ('S001', 'C101', 1, 7.00), ('S001', 'C101', 2, 9.00),
    ('S001', 'C102', 1, 8.00), ('S001', 'C103', 1, 9.00),
    ('S002', 'C101', 1, 8.00), ('S002', 'C102', 1, 7.50),
    ('S003', 'C101', 1, 6.50), ('S003', 'C103', 1, 8.50),
    ('S004', 'C101', 1, 9.00);
GO
