USE IT004_Training;
GO

/* Child objects first make this script repeatable without dropping the database. */
IF OBJECT_ID(N'dbo.tr_results', N'U') IS NOT NULL DROP TABLE dbo.tr_results;
IF OBJECT_ID(N'dbo.tr_enrollments', N'U') IS NOT NULL DROP TABLE dbo.tr_enrollments;
IF OBJECT_ID(N'dbo.tr_courses', N'U') IS NOT NULL DROP TABLE dbo.tr_courses;
IF OBJECT_ID(N'dbo.tr_students', N'U') IS NOT NULL DROP TABLE dbo.tr_students;
IF OBJECT_ID(N'dbo.tr_order_items', N'U') IS NOT NULL DROP TABLE dbo.tr_order_items;
IF OBJECT_ID(N'dbo.tr_orders', N'U') IS NOT NULL DROP TABLE dbo.tr_orders;
IF OBJECT_ID(N'dbo.tr_products', N'U') IS NOT NULL DROP TABLE dbo.tr_products;
IF OBJECT_ID(N'dbo.tr_employees', N'U') IS NOT NULL DROP TABLE dbo.tr_employees;
IF OBJECT_ID(N'dbo.tr_departments', N'U') IS NOT NULL DROP TABLE dbo.tr_departments;
IF OBJECT_ID(N'dbo.tr_customers', N'U') IS NOT NULL DROP TABLE dbo.tr_customers;
GO

CREATE TABLE dbo.tr_customers (
    CustomerId   CHAR(4)        NOT NULL CONSTRAINT PK_tr_customers PRIMARY KEY,
    FullName     NVARCHAR(60)   NOT NULL,
    City         NVARCHAR(40)   NOT NULL,
    RegisteredOn DATE           NOT NULL,
    CreditLimit  DECIMAL(10, 2) NOT NULL CONSTRAINT CK_tr_customers_credit CHECK (CreditLimit >= 0),
    Segment      CHAR(1)        NOT NULL CONSTRAINT CK_tr_customers_segment CHECK (Segment IN ('A', 'B', 'C'))
);
GO

CREATE TABLE dbo.tr_products (
    ProductId    CHAR(4)        NOT NULL CONSTRAINT PK_tr_products PRIMARY KEY,
    ProductName  NVARCHAR(80)   NOT NULL,
    Category     NVARCHAR(30)   NOT NULL,
    Country      NVARCHAR(30)   NOT NULL,
    Price        DECIMAL(10, 2) NOT NULL CONSTRAINT CK_tr_products_price CHECK (Price > 0),
    Stock        INT            NOT NULL CONSTRAINT CK_tr_products_stock CHECK (Stock >= 0),
    IsActive     BIT            NOT NULL CONSTRAINT DF_tr_products_active DEFAULT (1)
);
GO

CREATE TABLE dbo.tr_orders (
    OrderId      INT            NOT NULL CONSTRAINT PK_tr_orders PRIMARY KEY,
    CustomerId   CHAR(4)        NOT NULL,
    OrderDate    DATETIME2(0)   NOT NULL,
    Status       VARCHAR(12)    NOT NULL CONSTRAINT CK_tr_orders_status CHECK (Status IN ('PAID', 'PENDING', 'CANCELLED')),
    CONSTRAINT FK_tr_orders_customer FOREIGN KEY (CustomerId) REFERENCES dbo.tr_customers(CustomerId)
);
GO

CREATE TABLE dbo.tr_order_items (
    OrderId      INT            NOT NULL,
    ProductId    CHAR(4)        NOT NULL,
    Qty          INT            NOT NULL CONSTRAINT CK_tr_items_qty CHECK (Qty > 0),
    UnitPrice    DECIMAL(10, 2) NOT NULL CONSTRAINT CK_tr_items_price CHECK (UnitPrice > 0),
    CONSTRAINT PK_tr_order_items PRIMARY KEY (OrderId, ProductId),
    CONSTRAINT FK_tr_items_order FOREIGN KEY (OrderId) REFERENCES dbo.tr_orders(OrderId),
    CONSTRAINT FK_tr_items_product FOREIGN KEY (ProductId) REFERENCES dbo.tr_products(ProductId)
);
GO

/* Departments and employees deliberately demonstrate a circular FK dependency. */
CREATE TABLE dbo.tr_departments (
    DeptId          CHAR(4)      NOT NULL CONSTRAINT PK_tr_departments PRIMARY KEY,
    DeptName        NVARCHAR(50) NOT NULL,
    HeadEmployeeId  CHAR(4)      NULL
);
GO

CREATE TABLE dbo.tr_employees (
    EmployeeId  CHAR(4)        NOT NULL CONSTRAINT PK_tr_employees PRIMARY KEY,
    FullName    NVARCHAR(60)   NOT NULL,
    DeptId      CHAR(4)        NOT NULL,
    ManagerId   CHAR(4)        NULL,
    Salary      DECIMAL(10, 2) NOT NULL CONSTRAINT CK_tr_employees_salary CHECK (Salary > 0),
    CONSTRAINT FK_tr_employees_department FOREIGN KEY (DeptId) REFERENCES dbo.tr_departments(DeptId),
    CONSTRAINT FK_tr_employees_manager FOREIGN KEY (ManagerId) REFERENCES dbo.tr_employees(EmployeeId)
);
GO

ALTER TABLE dbo.tr_departments
    ADD CONSTRAINT FK_tr_departments_head
    FOREIGN KEY (HeadEmployeeId) REFERENCES dbo.tr_employees(EmployeeId);
GO

CREATE TABLE dbo.tr_students (
    StudentId  CHAR(4)      NOT NULL CONSTRAINT PK_tr_students PRIMARY KEY,
    FullName   NVARCHAR(60) NOT NULL,
    Cohort     CHAR(4)      NOT NULL
);
GO

CREATE TABLE dbo.tr_courses (
    CourseId    CHAR(4)      NOT NULL CONSTRAINT PK_tr_courses PRIMARY KEY,
    CourseName  NVARCHAR(60) NOT NULL,
    Credits     TINYINT      NOT NULL CONSTRAINT CK_tr_courses_credits CHECK (Credits BETWEEN 1 AND 6)
);
GO

CREATE TABLE dbo.tr_results (
    StudentId  CHAR(4)       NOT NULL,
    CourseId   CHAR(4)       NOT NULL,
    AttemptNo  TINYINT       NOT NULL CONSTRAINT CK_tr_results_attempt CHECK (AttemptNo >= 1),
    Score      DECIMAL(4, 2)  NOT NULL CONSTRAINT CK_tr_results_score CHECK (Score BETWEEN 0 AND 10),
    CONSTRAINT PK_tr_results PRIMARY KEY (StudentId, CourseId, AttemptNo),
    CONSTRAINT FK_tr_results_student FOREIGN KEY (StudentId) REFERENCES dbo.tr_students(StudentId),
    CONSTRAINT FK_tr_results_course FOREIGN KEY (CourseId) REFERENCES dbo.tr_courses(CourseId)
);
GO
