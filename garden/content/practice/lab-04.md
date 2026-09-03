---
title: Lab 04 — trigger và toàn vẹn
description: Trigger, inserted/deleted và kiểm thử thao tác nhiều dòng.
type: practice
topics: [trigger, integrity, inserted, deleted]
related: [theory/rbtv-impact, practice/multi-row-trigger, practice/debugging, errors/multi-row-trigger-failure]
provenance: verified-artifact
fixture: training-v1
technicalSources: [TECH-A04, TECH-A05, TECH-A06]
---
# Lab 04 — trigger và toàn vẹn

Lab 04 tập trung vào việc hiện thực hóa các quy tắc toàn vẹn nghiệp vụ phức tạp bằng DML Trigger trên SQL Server:

- **Phân tích trước khi viết code:** Bắt đầu bằng việc lập [[theory/rbtv-impact|Bảng tầm ảnh hưởng]] để khoanh vùng chính xác các thao tác `INSERT`, `DELETE`, `UPDATE` cần kiểm soát.
- **Xử lý đa dòng tập hợp:** Luôn viết trigger dựa trên phép nối (`JOIN`) giữa bảng ảo `inserted` / `deleted` với bảng cơ sở dữ liệu thực, xem chi tiết mẫu tại [[practice/multi-row-trigger|Multi-row trigger]].
- **Phòng ngừa sập logic batch:** Tránh hoàn toàn việc đọc dữ liệu ra biến vô hướng (scalar variable), nguyên nhân dẫn tới [[errors/multi-row-trigger-failure|Lỗi sập Trigger khi xử lý nhiều dòng]].
- **Quy trình gỡ lỗi:** Tham khảo phương pháp cô lập lỗi tại [[practice/debugging|Debugging]]. Căn cứ tài liệu kỹ thuật Microsoft [[sources/technical|TECH-A04, TECH-A05, TECH-A06]].
