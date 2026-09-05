---
title: Dạng đề quan sát — Tư duy logic SQL (SQL Reasoning)
description: Mẫu câu hỏi suy luận và bẫy ngữ nghĩa SQL trong đề thi và thực hành máy.
type: exam-pattern
topics: [exam, sql, null, join, exists]
related: [errors/null-comparison, errors/not-in-null, errors/group-by-8120, theory/double-not-exists]
provenance: reconstructed-exam-pattern
courseEvidence: [EXAM-2023-2024-HK1-FINAL-01, PRAC-2024-2025-HK1-01]
---
# Dạng đề quan sát — Tư duy logic SQL (SQL Reasoning)

Trong các kỳ thi cuối kỳ và thực hành máy IT004 (như `EXAM-2023-2024-HK1-FINAL-01` và `PRAC-2024-2025-HK1-01`), câu hỏi SQL không chỉ dừng lại ở việc viết câu truy vấn thông thường mà thường cài cắm các bẫy ngữ nghĩa và yêu cầu suy luận kết quả:

1. **Bẫy logic 3 giá trị (3VL) và NULL**: Đề bài yêu cầu giải thích vì sao phép so sánh trực tiếp `= NULL` không trả về dòng nào (xem [[errors/null-comparison|So sánh với NULL]]) hoặc vì sao `NOT IN` trả về tập rỗng khi tập con chứa giá trị NULL (xem [[errors/not-in-null|Bẫy NOT IN với NULL]]).
2. **Gom nhóm và điều kiện lọc**: Phân biệt bản chất giữa `WHERE` (lọc dòng thô trước khi gom nhóm) và `HAVING` (lọc trên kết quả hàm kết hợp sau gom nhóm). Bẫy lỗi Msg 8120 kinh điển được phân tích chi tiết tại [[errors/group-by-8120|Lỗi Group By 8120]].
3. **Bài toán "Tất cả" (Phép chia trong SQL)**: Hiện thực bằng kỹ thuật tương quan hai tầng [[theory/double-not-exists|Double NOT EXISTS]], tránh sai lầm dùng `COUNT(DISTINCT)` khi tập mẫu rỗng.

Thí sinh cần xác định rõ mức độ chi tiết (grain) của kết quả truy vấn và chứng minh tính đúng đắn trên cả tập dữ liệu biên.
