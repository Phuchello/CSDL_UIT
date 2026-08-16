# Coverage Matrix – IT004 CSDL UIT

## Ký hiệu
- 🔴 **UIT Core** — Kiến thức bắt buộc, chắc chắn thi
- 🟠 **Exam Important** — Hay xuất hiện trong đề thi
- 🟡 **Practice Important** — Quan trọng cho thực hành
- 🟢 **Supporting** — Hỗ trợ hiểu bài
- 🔵 **Advanced / Beyond UIT** — Nâng cao, gắn badge MỞ RỘNG

---

## Chương 1 — Tổng quan CSDL

| Kiến thức | Mức | Ghi chú |
|---|---|---|
| Data vs Information | 🟢 | Nền tảng |
| File System vs DBMS | 🔴 | Thường hỏi so sánh |
| Database, DBMS, DBS | 🔴 | Định nghĩa cơ bản |
| Data redundancy, inconsistency | 🔴 | Lý do cần CSDL |
| Data independence | 🔴 | Logical/Physical |
| Kiến trúc 3 mức (ANSI/SPARC) | 🔴 | External/Conceptual/Internal |
| Schema vs Instance | 🔴 | Hay nhầm |
| User roles (DBA, End user…) | 🟢 | Biết qua |
| Mô hình dữ liệu (ER, Relational…) | 🔴 | Phân biệt |
| Relational database | 🔴 | Nền tảng chương sau |

## Chương 2 — ER & Mô hình quan hệ

| Kiến thức | Mức | Ghi chú |
|---|---|---|
| Entity, Entity set | 🔴 | |
| Attribute types (key, composite, multivalued, derived) | 🔴 | |
| Relationship, Degree | 🔴 | |
| Cardinality (1:1, 1:N, M:N) | 🔴 | Trọng điểm thi GK |
| Participation (total, partial) | 🔴 | |
| Min-max notation: (0,1) (1,1) (0,n) (1,n) | 🔴 | Rất hay thi |
| ER Diagram drawing | 🟠 | Câu 1 GK |
| Relation, Tuple, Attribute, Domain | 🔴 | |
| Degree, Cardinality (relation) | 🔴 | |
| Superkey, Candidate key, Primary key | 🔴 | |
| Foreign key | 🔴 | |
| NULL semantics | 🔴 | |
| Predicate / Tân từ | 🟠 | UIT hay hỏi |
| ER → Relational Schema (Ánh xạ) | 🔴 | Trọng điểm thi GK |
| 1:1 mapping | 🔴 | |
| 1:N mapping | 🔴 | |
| M:N mapping (bảng trung gian) | 🔴 | Hay sai |
| Relationship có attribute | 🟠 | |

## Chương 3 — Đại số quan hệ

| Kiến thức | Mức | Ghi chú |
|---|---|---|
| Selection σ | 🔴 | |
| Projection π | 🔴 | |
| Rename ρ | 🟠 | |
| Cartesian product × | 🔴 | |
| Theta join ⋈_θ | 🔴 | |
| Equi-join | 🔴 | |
| Natural join ⋈ | 🔴 | |
| Union ∪ | 🔴 | |
| Intersection ∩ | 🔴 | |
| Difference − | 🔴 | |
| Division ÷ | 🔴 | Khó nhất, hay thi |
| Aggregation (COUNT, SUM, AVG, MAX, MIN) | 🔴 | |
| Grouping Ɣ | 🔴 | |
| Outer join | 🟡 | Ít thi lý thuyết |
| "Tất cả" → Division / NOT EXISTS | 🟠 | Bẫy kinh điển |
| "Không" → Difference | 🟠 | |
| "Mỗi" → Grouping | 🟠 | |

## Chương 4 — SQL Server / T-SQL

| Kiến thức | Mức | Ghi chú |
|---|---|---|
| CREATE DATABASE/TABLE | 🔴 | DDL |
| Data types (SQL Server) | 🟡 | |
| PRIMARY KEY, FOREIGN KEY | 🔴 | |
| UNIQUE, NOT NULL, DEFAULT, CHECK | 🔴 | |
| ALTER TABLE, DROP | 🟡 | |
| INSERT, UPDATE, DELETE | 🔴 | |
| SELECT, DISTINCT, WHERE | 🔴 | |
| Operators, LIKE, IN, BETWEEN | 🔴 | |
| NULL handling (IS NULL) | 🔴 | Bẫy |
| ORDER BY | 🟡 | |
| INNER JOIN, LEFT/RIGHT/FULL JOIN | 🔴 | |
| Self JOIN | 🟠 | |
| COUNT, SUM, AVG, MAX, MIN | 🔴 | |
| GROUP BY, HAVING | 🔴 | WHERE vs HAVING bẫy |
| UNION, INTERSECT, EXCEPT | 🔴 | |
| Subquery (scalar, IN, EXISTS) | 🔴 | |
| Correlated subquery | 🟠 | |
| NOT EXISTS | 🔴 | "Tất cả" pattern |
| Double NOT EXISTS | 🟠 | Division SQL |
| COUNT DISTINCT pattern | 🟠 | Cách 2 cho "tất cả" |
| ALL / >= ALL | 🟠 | Max pattern |
| TOP WITH TIES | 🟡 | |
| YEAR(), MONTH(), date functions | 🟡 | |
| View | 🟡 | Có thể thi TH |
| Stored Procedure | 🟡 | Thi TH cuối kỳ |
| Trigger | 🟡 | Thi TH cuối kỳ |

## Chương 5 — Ràng buộc toàn vẹn

| Kiến thức | Mức | Ghi chú |
|---|---|---|
| Khái niệm RBTV | 🔴 | |
| Nội dung, Bối cảnh RBTV | 🔴 | |
| Domain constraint | 🔴 | |
| Key constraint | 🔴 | |
| Entity integrity | 🔴 | |
| Referential integrity | 🔴 | |
| Bảng tầm ảnh hưởng | 🔴 | Trọng điểm CK |
| Thêm/Xóa/Sửa → +/−/+(A) | 🔴 | Ký hiệu UIT |
| Inter-attribute constraint | 🟠 | |
| Inter-tuple constraint | 🟠 | |
| Multi-relation constraints | 🟠 | |
| Aggregate constraints | 🟡 | Tùy syllabus |
| SQL implementation (CHECK, TRIGGER) | 🟡 | TH |

## Chương 6 — Phụ thuộc hàm, Khóa & Dạng chuẩn

| Kiến thức | Mức | Ghi chú |
|---|---|---|
| Functional dependency X → Y | 🔴 | |
| Trivial / Non-trivial FD | 🔴 | |
| Armstrong's axioms | 🔴 | Reflexivity, Augmentation, Transitivity |
| Derived rules (Union, Decomp, Pseudo) | 🔴 | |
| Chứng minh PTH | 🟠 | Thi CK |
| Attribute closure X⁺ | 🔴 | Trọng điểm CK |
| Kiểm tra superkey | 🔴 | |
| Tìm candidate key | 🔴 | Trọng điểm CK |
| Tìm TẤT CẢ candidate keys | 🟠 | Khó |
| Minimal cover (Phủ tối thiểu) | 🔴 | Trọng điểm CK |
| 1NF | 🔴 | |
| 2NF | 🔴 | |
| 3NF | 🔴 | |
| BCNF | 🔴 | |
| Xác định dạng chuẩn cao nhất | 🔴 | Trọng điểm CK |
| Lossless join decomposition | 🟠 | Tùy syllabus |
| Dependency preservation | 🟠 | Tùy syllabus |
| Decomposition to 3NF/BCNF | 🟡 | Có thể nâng cao |

## Nâng cao / Mở rộng (🔵)

| Kiến thức | Ghi chú |
|---|---|
| Indexing | Thường không thi IT004 |
| Transactions & ACID | Week 13–14 có thể đề cập |
| Query optimization | Mở rộng |
| Isolation levels | Mở rộng |
