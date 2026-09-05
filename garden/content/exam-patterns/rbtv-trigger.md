---
title: Dạng đề quan sát — RBTV và Trigger
description: Mẫu bài tập Ràng buộc toàn vẹn, Bảng tầm ảnh hưởng và cài đặt Trigger trong đề thi UIT.
type: exam-pattern
topics: [exam, integrity, trigger]
related: [theory/rbtv-impact, practice/multi-row-trigger, errors/multi-row-trigger-failure]
provenance: reconstructed-exam-pattern
courseEvidence: [EXAM-2024-2025-HK1-FINAL-01, PRAC-2023-2024-HK1-FINAL-01, LOC-LEC-LONG-CH05]
---
# Dạng đề quan sát — Ràng buộc toàn vẹn & Trigger (RBTV & Trigger)

Trong các đề khảo sát tự luận và thực hành máy UIT (minh chứng qua bản sao cộng đồng `EXAM-2024-2025-HK1-FINAL-01`, `PRAC-2023-2024-HK1-FINAL-01` và slide bài giảng chính thức `LOC-LEC-LONG-CH05`), dạng bài Ràng buộc toàn vẹn (RBTV) và Trigger thường được quan sát với cấu trúc gồm các bước:

1. **Phát biểu tân từ và Bối cảnh**: Nêu rõ các quan hệ liên quan và điều kiện logic cần bảo toàn tính toàn vẹn dữ liệu.
2. **Lập Bảng tầm ảnh hưởng (Impact Matrix)**: Xác định dấu tác động `+` (thao tác có thể gây vi phạm nên cần kiểm tra), `-` (thao tác không thể làm phát sinh vi phạm), và `+(Thuộc tính)` cho trường hợp `UPDATE` chỉ có khả năng gây vi phạm khi sửa các thuộc tính được chỉ định. Khi tài liệu dùng ký hiệu `-(*)`, dấu này biểu thị thao tác tương ứng không thực hiện được nên không thể gây vi phạm. Xem hướng dẫn chi tiết tại [[theory/rbtv-impact|Bảng tầm ảnh hưởng]].
3. **Lựa chọn cơ chế thực thi**: Phân định rạch ròi giữa ràng buộc khai báo nội tại (`CHECK`, `PRIMARY KEY`, `FOREIGN KEY`) và các ràng buộc phức tạp liên quan hệ đòi hỏi cài đặt bằng `TRIGGER`.
4. **Cài đặt DML Trigger tập hợp**: Viết trigger an toàn đa dòng trên SQL Server, phân biệt rạch ròi sự kiện `DELETE` và `UPDATE` dựa trên bảng ảo `inserted` và `deleted` (xem chuẩn mẫu tại [[practice/multi-row-trigger|Trigger xử lý tập hợp đa dòng]]). Tránh tuyệt đối lỗi sập logic khi dữ liệu đến theo batch (xem [[errors/multi-row-trigger-failure|Sập trigger khi chạy batch nhiều dòng]]).

Tham khảo các quy chuẩn kỹ thuật Microsoft Learn tại [[sources/technical|Tài liệu kỹ thuật (Technical Sources)]].
