USE IT004_Training;
GO

/* A01 — scalar subquery; P001 is the unique maximum-price product. */
SELECT ProductId, ProductName, Price
FROM dbo.tr_products
WHERE Price = (SELECT MAX(Price) FROM dbo.tr_products)
ORDER BY ProductId;

/* A02 — correlated subquery: maximum price per country. */
SELECT p.ProductId, p.ProductName, p.Country, p.Price
FROM dbo.tr_products AS p
WHERE p.Price = (
    SELECT MAX(p2.Price)
    FROM dbo.tr_products AS p2
    WHERE p2.Country = p.Country
)
ORDER BY p.Country, p.ProductId;

/* A03 — NOT EXISTS finds the only unsold product, P007. */
SELECT p.ProductId, p.ProductName
FROM dbo.tr_products AS p
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.tr_order_items AS i
    WHERE i.ProductId = p.ProductId
)
ORDER BY p.ProductId;

/* A04 — universal query: S001 is the only student with every course. */
SELECT s.StudentId, s.FullName
FROM dbo.tr_students AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.tr_courses AS c
    WHERE NOT EXISTS (
        SELECT 1
        FROM dbo.tr_results AS r
        WHERE r.StudentId = s.StudentId
          AND r.CourseId = c.CourseId
    )
)
ORDER BY s.StudentId;

/* A05 — COUNT DISTINCT alternative; the retake of C101 is not double-counted. */
SELECT r.StudentId
FROM dbo.tr_results AS r
GROUP BY r.StudentId
HAVING COUNT(DISTINCT r.CourseId) = (SELECT COUNT(*) FROM dbo.tr_courses);

/* A06 — SQL Server set operators: INTERSECT and EXCEPT remove duplicate rows. */
SELECT CustomerId AS Id FROM dbo.tr_customers
INTERSECT
SELECT StudentId FROM dbo.tr_students;

SELECT ProductId FROM dbo.tr_products
EXCEPT
SELECT ProductId FROM dbo.tr_order_items;

/* A07 — CASE is a projection; it does not change stored rows. */
SELECT ProductId, ProductName,
       CASE WHEN Stock = 0 THEN 'OUT'
            WHEN Stock < 10 THEN 'LOW'
            ELSE 'OK' END AS StockBand
FROM dbo.tr_products
ORDER BY ProductId;
GO
