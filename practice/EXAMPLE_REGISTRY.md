# IT004 Practical Example Registry

Canonical contract between printed anchors and runnable SQL. All rows use practice/sql/02_seed.sql unless stated otherwise. STATIC means the key set is derived from the deterministic seed and checked by the static validator; ILLUSTRATIVE is intentionally not a claimed execution result.

| Example ID | Printed chapter/page anchor | Runnable SQL file | Dataset | Purpose | Expected row count | Expected key values | Validation mode |
|---|---|---|---|---|---:|---|---|
| B01 | Lab 02 — Projection | 03_queries_basic.sql | tr_customers | Segment A/B projection | 3 | C001, C002, C003 | STATIC |
| B02 | Lab 02 — Projection | 03_queries_basic.sql | tr_orders | Half-open date range [2024-10-15, 2024-10-18) | 4 | 1001, 1002, 1003, 1004; dates [2024-10-15, 2024-10-18) | STATIC |
| B03 | Lab 02 — Join | 03_queries_basic.sql | orders/items/products/customers | Explicit four-table join | 11 | OrderId/item pairs from seed | STATIC |
| B04 | Lab 02 — Join | 03_queries_basic.sql | tr_customers left join tr_orders | Preserve customer with no order | 5 | C005 has OrderCount 0 | STATIC |
| B05 | Lab 02 — Self join | 03_queries_basic.sql | tr_employees | Employee → manager lookup | 4 | E001, E002, E003, E004 | STATIC |
| A01 | Lab 03 — Scalar | 04_queries_advanced.sql | tr_products | Maximum price | 1 | P001, Price 1200 | STATIC |
| A02 | Lab 03 — Correlated | 04_queries_advanced.sql | tr_products | Maximum price per country | 3 | P001, P003, P005 | STATIC |
| A03 | Lab 03 — NOT EXISTS | 04_queries_advanced.sql | tr_products/items | Unsold product | 1 | P007 | STATIC |
| A04 | Lab 03 — Double NOT EXISTS | 04_queries_advanced.sql | students/courses/results | Student with every course | 1 | S001 | STATIC |
| A05 | Lab 03 — COUNT DISTINCT | 04_queries_advanced.sql | students/courses/results | Retake-safe universal alternative | 1 | S001 | STATIC |
| A06 | Lab 03 — Set operators | 04_queries_advanced.sql | customers/students/products/items | INTERSECT and EXCEPT | 0 + 1 | EXCEPT key P007; INTERSECT empty | STATIC |
| A07 | Lab 03 — CASE | 04_queries_advanced.sql | tr_products | Stock-band projection | 7 | P001/P004/P007 = LOW | STATIC |
| TOP-TIE | Lab 04 — TOP WITH TIES | Lab 04 exercise | temporary tie row | Explain boundary tie behavior | n or more | Illustrative tie at ORDER BY boundary | ILLUSTRATIVE |
| TRG-A | Debugging — trigger tests | 06_test_cases.sql | tr_employees | UPDATE FullName on head | pass | E001 remains head | STATIC |
| TRG-B | Debugging — trigger tests | 06_test_cases.sql | tr_employees | UPDATE Salary on head | pass | E001 remains head | STATIC |
| TRG-C | Debugging — trigger tests | 06_test_cases.sql | tr_employees | Same DeptId | pass | D001 unchanged | STATIC |
| TRG-D | Debugging — trigger tests | 06_test_cases.sql | tr_employees | Different DeptId | reject | E001 → D002 blocked | STATIC |
| TRG-E | Debugging — trigger tests | 06_test_cases.sql | tr_employees | NULL DeptId | schema reject | NOT NULL blocks before trigger | STATIC |
| TRG-F | Debugging — trigger tests | 06_test_cases.sql | tr_employees | Delete department head | declarative reject | FK_tr_departments_head blocks before trigger (Msg 547) | STATIC |
| TRG-G | Debugging — trigger tests | 06_test_cases.sql | tr_employees | Multi-row unrelated update | pass | D001 salaries update together | STATIC |
| TRG-H | Debugging — trigger tests | 06_test_cases.sql | tr_employees | Multi-row violating update | reject whole statement | D001 → D002 blocked | STATIC |

The registry is the single ID contract. If a query or seed changes, update the registry and QA report in the same commit. Runtime remains a separate status and is never inferred from this table.
