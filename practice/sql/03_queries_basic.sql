USE IT004_Training;
GO

/* B01 — projection + WHERE: expected keys C001, C002, C003 (3 rows). */
SELECT CustomerId, FullName, City
FROM dbo.tr_customers
WHERE Segment IN ('A', 'B')
ORDER BY CustomerId;

/* B02 — half-open DATETIME2 range: expected OrderId 1001, 1002, 1003, 1004. */
SELECT OrderId, CustomerId, OrderDate
FROM dbo.tr_orders
WHERE OrderDate >= '20241015'
  AND OrderDate <  '20241018'
ORDER BY OrderDate, OrderId;

/* B03 — explicit JOIN and line total: expected 11 item rows after the join. */
SELECT o.OrderId, c.FullName, p.ProductName, i.Qty,
       i.Qty * i.UnitPrice AS LineTotal
FROM dbo.tr_orders AS o
JOIN dbo.tr_customers AS c ON c.CustomerId = o.CustomerId
JOIN dbo.tr_order_items AS i ON i.OrderId = o.OrderId
JOIN dbo.tr_products AS p ON p.ProductId = i.ProductId
ORDER BY o.OrderId, p.ProductId;

/* B04 — LEFT JOIN preserves C005, which has no order. */
SELECT c.CustomerId, c.FullName, COUNT(o.OrderId) AS OrderCount
FROM dbo.tr_customers AS c
LEFT JOIN dbo.tr_orders AS o ON o.CustomerId = c.CustomerId
GROUP BY c.CustomerId, c.FullName
ORDER BY c.CustomerId;

/* B05 — self-join uses the independent employee mini-schema. */
SELECT e.EmployeeId, e.FullName, m.FullName AS ManagerName
FROM dbo.tr_employees AS e
LEFT JOIN dbo.tr_employees AS m ON m.EmployeeId = e.ManagerId
ORDER BY e.EmployeeId;
GO
