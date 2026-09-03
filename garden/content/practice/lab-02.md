---
title: Lab 02 — DML và JOIN
description: Chèn, cập nhật, xoá và nối bảng mà không mất miền dữ liệu.
type: practice
topics: [dml, join, aggregation]
related: [practice/lab-01, errors/unexpected-duplicates, errors/group-by-8120]
provenance: verified-artifact
fixture: training-v1
technicalSources: [TECH-A01, TECH-A02]
---
# Lab 02 — DML và JOIN

Sau khi hoàn thành cấu trúc bảng ở [[practice/lab-01|Lab 01]], quy trình thao tác dữ liệu và kết nối bảng đòi hỏi kiểm soát chặt chẽ mức độ chi tiết (grain):

- **Chèn dữ liệu (INSERT):** Tuân thủ thứ tự khóa ngoại, tránh đưa vào các mã tham chiếu chưa tồn tại ở bảng cha.
- **Cập nhật và Xóa (UPDATE / DELETE):** Luôn đi kèm mệnh đề `WHERE` cụ thể và kiểm tra số dòng bị ảnh hưởng (`@@ROWCOUNT`).
- **Phép kết nối (JOIN):** Xác định rõ bản số quan hệ (1-1, 1-N, N-N). Nếu thiếu điều kiện kết nối, kết quả sẽ sinh ra tích Descartes gây [[errors/unexpected-duplicates|Trùng lặp dòng ngoài ý muốn]].
- **Gom nhóm (GROUP BY):** Mọi thuộc tính trong danh sách `SELECT` không nằm trong hàm kết hợp đều bắt buộc phải xuất hiện trong mệnh đề `GROUP BY` để tránh [[errors/group-by-8120|Lỗi Group By 8120]]. Căn cứ kỹ thuật Microsoft Learn [[sources/technical|TECH-A01, TECH-A02]].
