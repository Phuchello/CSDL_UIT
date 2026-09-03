---
title: "Cài đặt & Thiết lập SQL Server (Setup)"
description: Database context, SSMS workflow và cách ghi lại script có thể chạy lại.
type: practice
topics: [sql-server, ssms, setup]
related: [practice/lab-01, practice/debugging, cheat-sheets/sql-server]
provenance: verified-artifact
technicalSources: [TECH-A01]
---
# Cài đặt & Thiết lập môi trường SQL Server (Setup)

Mở SSMS, kết nối đúng instance máy chủ cục bộ hoặc phòng máy, khởi tạo ngữ cảnh database trước khi chạy script:

- Luôn chỉ định `USE IT004_Training; GO` ở đầu tệp SQL để tránh thực thi nhầm vào cơ sở dữ liệu hệ thống `master`.
- Tạo bảng và cấu trúc schema theo thứ tự quan hệ cha trước, quan hệ con sau để thỏa mãn ràng buộc khóa ngoại (xem [[practice/lab-01|Lab 01]]).
- Nếu gặp lỗi `Invalid object name`, tham khảo cách khắc phục tại [[errors/wrong-database|Lỗi sai Database]] và [[errors/invalid-object-column|Lỗi sai tên đối tượng/cột]].
- Quy trình kiểm thử và xử lý lỗi xem tại [[practice/debugging|Debugging]] và tài liệu kỹ thuật Microsoft [[sources/technical|TECH-A01]].
