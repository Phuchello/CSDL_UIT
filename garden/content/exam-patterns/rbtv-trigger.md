---
title: Observed pattern — RBTV and trigger
description: Mẫu bài tập Ràng buộc toàn vẹn, Bảng tầm ảnh hưởng và cài đặt Trigger trong đề thi UIT.
type: exam-pattern
topics: [exam, integrity, trigger]
related: [theory/rbtv-impact, practice/multi-row-trigger, errors/multi-row-trigger-failure]
provenance: reconstructed-exam-pattern
courseEvidence: [EXAM-2024-2025-HK1-FINAL-01, PRAC-2023-2024-HK1-FINAL-01, LOC-LEC-LONG-CH05]
---
# Observed pattern — RBTV and trigger

Trong các đề khảo sát tự luận và thực hành máy UIT (minh chứng qua bản sao cộng đồng `EXAM-2024-2025-HK1-FINAL-01`, `PRAC-2023-2024-HK1-FINAL-01` và slide bài giảng chính thức `LOC-LEC-LONG-CH05`), dạng bài Ràng buộc toàn vẹn (RBTV) và Trigger thường được quan sát với cấu trúc gồm các bước:

1. **Phát biểu tân từ và Bối cảnh**: Nêu rõ các quan hệ liên quan và điều kiện logic cần bảo toàn tính toàn vẹn dữ liệu.
2. **Lập Bảng tầm ảnh hưởng (Impact Matrix)**: Xác định dấu tác động `+` (cần kiểm tra), `-` (không vi phạm), và `*` (chỉ kiểm tra khi sửa đổi các thuộc tính liên quan) cho từng thao tác `INSERT`, `DELETE`, `UPDATE` trên từng quan hệ (xem hướng dẫn chi tiết tại [[theory/rbtv-impact|Bảng tầm ảnh hưởng]]).
3. **Lựa chọn cơ chế thực thi**: Phân định rạch ròi giữa ràng buộc khai báo nội tại (`CHECK`, `PRIMARY KEY`, `FOREIGN KEY`) và các ràng buộc phức tạp liên quan hệ đòi hỏi cài đặt bằng `TRIGGER`.
4. **Cài đặt DML Trigger tập hợp**: Viết trigger an toàn đa dòng trên SQL Server, phân biệt rạch ròi sự kiện `DELETE` và `UPDATE` dựa trên bảng ảo `inserted` và `deleted` (xem chuẩn mẫu tại [[practice/multi-row-trigger|Multi-row trigger]]). Tránh tuyệt đối lỗi sập logic khi dữ liệu đến theo batch (xem [[errors/multi-row-trigger-failure|Multi-row trigger failure]]).

Tham khảo các quy chuẩn kỹ thuật Microsoft Learn tại [[sources/technical|Technical sources]].
