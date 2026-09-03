---
title: Unexpected duplicate rows
description: JOIN hoặc bag semantics làm số dòng tăng bất thường do thiếu điều kiện kết nối hoặc sai mức chi tiết (grain).
type: error
topics: [join, duplicates, aggregation]
related: [practice/lab-02, errors/group-by-8120, theory/relational-algebra]
provenance: original-practice
---
# Unexpected duplicate rows

- **Triệu chứng (Symptom):** Một đối tượng thực thể xuất hiện lặp lại nhiều lần trong kết quả truy vấn.
- **Nguyên nhân (Cause):** Bội số quan hệ 1-N hoặc điều kiện `JOIN` bị thiếu/thiếu khóa ngoại, hoặc thực hiện phép tích Descartes trước khi lọc.
- **Thẩm tra (Verify):** Đếm số dòng (`COUNT(*)`) trước và sau khi `JOIN` dựa theo khóa chính (`PRIMARY KEY`).
- **Khắc phục (Fix):** Nối đúng khóa, xác định đúng mức chi tiết (grain) trước khi gom nhóm; chỉ sử dụng `DISTINCT` khi việc lặp dòng là đặc trưng nghiệp vụ hợp lệ, không lạm dụng `DISTINCT` để che giấu lỗi sai logic `JOIN`.

Liên kết chẩn đoán: [[errors/group-by-8120|Lỗi Group By 8120]], [[theory/relational-algebra|Đại số quan hệ]], và thực hành truy vấn tại [[practice/lab-02|Lab 02]].
