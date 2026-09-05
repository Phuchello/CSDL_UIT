---
title: 'Sai miền ứng viên trong truy vấn phổ dụng "Tất cả"'
description: Sai lầm xác định miền ứng viên trong câu truy vấn phổ quát mang lượng từ "Tất cả".
type: error
topics: [division, universal-query, exists]
related: [theory/division, theory/double-not-exists, practice/lab-03]
provenance: original-practice
---
# Sai miền ứng viên trong truy vấn phổ dụng "Tất cả" (Wrong Candidate Domain)

Trong các bài toán hiện thực hóa [[theory/division|Phép chia hình thức]] hoặc viết câu truy vấn [[theory/double-not-exists|Double NOT EXISTS]], sai lầm phổ biến nhất của sinh viên là **đặt sai bảng ở tầng truy vấn ngoài cùng (Outer Query)**.

## 1. Triệu chứng (Symptom)
- Câu truy vấn trả về tập kết quả bị rỗng bất thường, hoặc trả về danh sách các thực thể không phải là đối tượng cần tìm (ví dụ: đề bài yêu cầu tìm *sinh viên* nhưng kết quả lại in ra danh sách *môn học*).
- Số lượng dòng trả về nhiều hơn hoặc ít hơn đáng kể so với kết quả kỳ vọng.

## 2. Nguyên nhân (Root Cause)
Người viết nhầm lẫn giữa **Tập ứng viên ($X$)** và **Tập yêu cầu ($Y$)**:
- Giả sử yêu cầu nghiệp vụ: *"Tìm các sinh viên đã học tất cả các môn học có 4 tín chỉ"*.
  - $X$ (Ứng viên): Danh sách sinh viên (`dbo.tr_students`).
  - $Y$ (Yêu cầu): Danh sách môn học 4 tín chỉ (`dbo.tr_courses` với `Credits = 4`).
- Lỗi sai: Viết tầng ngoài cùng là `FROM dbo.tr_courses AS c` và tầng giữa là `FROM dbo.tr_students AS s`. Điều này đảo ngược ngữ nghĩa thành: *"Tìm các môn học 4 tín chỉ được học bởi tất cả sinh viên"*.

## 3. Cách thẩm tra và chẩn đoán (Verify)
Trước khi đặt bút viết code SQL, luôn phân rã bài toán thành 3 tập hợp rõ ràng theo quy tắc tại [[theory/division|Phép chia]]:
1. **$X$ (Candidate):** Ta đang cần tìm cái gì? $\implies$ Đưa bảng đó vào mệnh đề `FROM` của tầng ngoài cùng.
2. **$Y$ (Target Requirement):** Điều kiện "tất cả" áp đặt lên đối tượng nào? $\implies$ Đưa bảng đó vào tầng `FROM` của subquery thứ nhất.
3. **$R$ (Evidence):** Sự kiện liên kết nằm ở đâu? $\implies$ Đưa bảng đó vào tầng `FROM` của subquery thứ hai, kết nối với cả $X$ và $Y$.

## 4. Cách khắc phục chuẩn xác (Fix)
Đảm bảo cấu trúc câu truy vấn tuân thủ đúng vị trí phân tầng và dùng đúng các cột chuẩn tắc trong schema:

```sql
-- Cấu trúc chuẩn tắc: Outer FROM là Ứng viên (X)
SELECT s.StudentId, s.FullName
FROM dbo.tr_students AS s -- Tập ứng viên X
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.tr_courses AS c -- Tập yêu cầu Y
    WHERE c.Credits = 4
      AND NOT EXISTS (
          SELECT 1
          FROM dbo.tr_results AS r -- Bảng bằng chứng R nối X và Y
          WHERE r.StudentId = s.StudentId
            AND r.CourseId = c.CourseId
      )
);
```

Xem bài tập thực hành hoàn chỉnh tại [[practice/lab-03|Lab 03 — Truy vấn nâng cao]], lý thuyết lượng từ tại [[theory/double-not-exists|Double NOT EXISTS]], và bản đồ phép toán tại [[theory/division|Phép chia hình thức]].
