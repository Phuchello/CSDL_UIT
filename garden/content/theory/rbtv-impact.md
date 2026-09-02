---
title: RBTV và impact table
description: Ràng buộc toàn vẹn, bảng tác động và cách suy luận ảnh hưởng.
type: theory
topics: [integrity, constraints, impact-table]
related: [multi-row-trigger, lab-04, debugging]
provenance: verified-artifact
courseEvidence: [UIT-O06]
---
# RBTV và impact table

Với mỗi thao tác `INSERT`, `UPDATE`, `DELETE`, impact table ghi quan hệ bị tác động, cột thay đổi, và ràng buộc cần kiểm. PK/UNIQUE, FK, CHECK, NOT NULL là các lớp kiểm khác nhau; đừng dùng trigger để thay thế ràng buộc khai báo khi SQL Server đã hỗ trợ.

Trigger đọc tập [[multi-row-trigger]] bằng `inserted`/`deleted`, không giả định một dòng.
