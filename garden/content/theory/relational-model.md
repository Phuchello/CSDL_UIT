---
title: Mô hình quan hệ (Relational Model)
description: Relation, tuple, attribute, schema, instance và các ràng buộc toàn vẹn cơ bản trong mô hình quan hệ.
type: theory
topics: [relational-model, schema, instance]
related: [theory/relational-algebra, theory/candidate-keys, theory/rbtv-impact]
provenance: verified-artifact
courseEvidence: [UIT-O01, UIT-O02]
---
# Mô hình quan hệ (Relational Model)

Mô hình dữ liệu quan hệ (Relational Data Model) được E.F. Codd đề xuất năm 1970, tổ chức dữ liệu dưới dạng các bảng hai chiều (quan hệ - Relation):

## 1. Khái niệm cốt lõi
- **Thuộc tính (Attribute):** Cột có tên biểu diễn đặc trưng của thực thể.
- **Miền giá trị (Domain):** Tập các giá trị nguyên tố (atomic) hợp lệ cho thuộc tính.
- **Bộ (Tuple):** Một dòng trong quan hệ đại diện cho một đối tượng thực tế.
- **Lược đồ quan hệ (Relation Schema):** Tên quan hệ cùng danh sách thuộc tính $R(A_1, A_2, \dots, A_n)$.
- **Thể hiện quan hệ (Relation Instance):** Tập hữu hạn các bộ dữ liệu tại một thời điểm cụ thể.

Vì quan hệ là một tập hợp toán học, các bộ không có thứ tự và không chứa các dòng trùng lặp hoàn toàn.

## 2. Ràng buộc toàn vẹn cấu trúc
- **Khóa chính (Primary Key - PK):** Tập thuộc tính tối thiểu định danh duy nhất mỗi bộ, không chấp nhận giá trị NULL (Entity Integrity, xem [[theory/candidate-keys|Khóa ứng viên]]).
- **Khóa ngoại (Foreign Key - FK):** Tập thuộc tính tham chiếu đến khóa chính của quan hệ khác, đảm bảo tính toàn vẹn tham chiếu (Referential Integrity).

Các phép toán thao tác dữ liệu được định nghĩa hình thức qua [[theory/relational-algebra|Đại số quan hệ]], và các quy tắc kiểm tra tính hợp lệ dữ liệu được mô hình hóa thành [[theory/rbtv-impact|Bảng tầm ảnh hưởng RBTV]]. Cài đặt vật lý tương ứng trên SQL Server xem tại [[practice/setup|Setup môi trường thực hành]].
