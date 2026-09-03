---
title: Division — Phép chia hình thức cho truy vấn "Tất cả"
description: Định nghĩa toán học của phép chia quan hệ, ngữ nghĩa tập rỗng R ÷ ∅ = π_X(R), quy tắc 3 tập hợp, công thức Codd, kỹ thuật đếm nhóm và phân biệt với quan hệ ứng viên độc lập trong SQL.
type: theory
topics: [division, universal-query, relational-algebra]
related: [theory/relational-algebra, theory/double-not-exists, practice/lab-03, errors/wrong-universal-candidate, exercises/division-exercise]
provenance: verified-artifact
courseEvidence: [UIT-O02, LOC-LEC-LONG-CH03]
---
# Division (Phép chia hình thức cho truy vấn "Tất cả")

Phép chia quan hệ (Relational Division $R \div S$) là phép toán đại số quan hệ phái sinh giải quyết nhóm bài toán mang lượng từ phổ quát ($\forall$ - "Tất cả"). Đây là một trong những nội dung học thuật trọng tâm trong học phần IT004.

## 1. Định nghĩa toán học chuẩn tắc

Cho quan hệ $R$ có tập thuộc tính $U_R = X \cup Y$ và quan hệ $S$ có tập thuộc tính $U_S = Y$ (với $Y \subset U_R$ và $X \cap Y = \emptyset$).
Lưu ý: trong đại số quan hệ cổ điển, **$X$ là tập thuộc tính của chính quan hệ $R$**, không phải là một quan hệ bảng ứng viên độc lập.

**Phép chia $R \div S$** trả về một quan hệ trên tập thuộc tính $X$, gồm các bộ giá trị $t[X]$ sao cho với **mọi** bộ $u \in S$, bộ kết hợp $t[X] \circ u[Y]$ đều có mặt trong quan hệ $R$:

$$R \div S = \{t[X] \mid \exists r \in R \text{ sao cho } r[X] = t[X] \land \forall u \in S, (\exists r' \in R: r'[X] = t[X] \land r'[Y] = u[Y])\}$$

### Ngữ nghĩa toán học khi tập yêu cầu rỗng ($S = \emptyset$):
Khi quan hệ số chia $S$ rỗng ($S = \emptyset$), điều kiện phổ quát $\forall u \in \emptyset, \dots$ trở thành **chân lý rỗng (vacuously true)** với mọi bộ giá trị hiện diện trong $R$.
Do đó, phép chia đại số quan hệ cổ điển cho tập rỗng được xác định chính xác là:

$$R \div \emptyset = \pi_X(R)$$

Kết quả trả về chính xác là phép chiếu các giá trị thuộc tính $X$ đã từng xuất hiện trong quan hệ bằng chứng $R$.

## 2. Quy tắc 3 tập hợp phân tích bài toán chia

Mọi câu hỏi mang ý nghĩa "tất cả" đều có thể quy về 3 tập hợp rõ ràng:
1. **Tập thuộc tính/thực thể ứng viên ($X$):** Đối tượng cần tìm trong kết quả đầu ra (ví dụ: Mã sinh viên, Mã khách hàng).
2. **Tập mục tiêu / yêu cầu ($Y$):** Danh sách toàn bộ các giá trị mẫu cần phải thỏa mãn (ví dụ: Tất cả môn học của Khoa HTTT, Tất cả sản phẩm xuất xứ từ Việt Nam).
3. **Tập bằng chứng ($R$):** Quan hệ dữ liệu lưu vết lịch sử liên kết thực tế giữa $X$ và $Y$ (ví dụ: Bảng kết quả học tập, Chi tiết hóa đơn bán hàng).

*Cảnh báo bẫy thi:* Việc trích xuất sai bảng ứng viên ngay từ đầu sẽ làm sai lệch tập lượng từ, xem chi tiết cảnh báo tại [[errors/wrong-universal-candidate|Sai miền ứng viên trong câu hỏi Tất cả]].

## 3. Công thức phái sinh Codd từ các phép toán cơ bản

Vì các hệ quản trị CSDL không hỗ trợ toán tử $\div$ trực tiếp, E.F. Codd đã chứng minh phép chia có thể biểu diễn qua [[theory/relational-algebra|Đại số quan hệ]] cơ bản (chọn, chiếu, tích Descartes và phép trừ):

$$R \div S = \pi_X(R) - \pi_X\Big( \big(\pi_X(R) \times S\big) - R \Big)$$

### Ý nghĩa trực quan từng bước:
- $\pi_X(R)$: Tập tất cả các giá trị $X$ đã từng tham gia vào quan hệ bằng chứng.
- $\pi_X(R) \times S$: Tập hợp tất cả các cặp (ứng viên, yêu cầu) lý thuyết mà mỗi ứng viên bắt buộc phải có nếu hoàn thành 100% mục tiêu.
- $(\pi_X(R) \times S) - R$: Tập các yêu cầu mà từng ứng viên còn **thiếu** (chưa xuất hiện trong bằng chứng).
- $\pi_X(\text{thiếu})$: Danh sách các ứng viên còn thiếu ít nhất 1 yêu cầu.
- Lấy toàn bộ trừ đi danh sách ứng viên còn thiếu sẽ thu được chính xác các ứng viên đã hoàn thành **tất cả**. Khi $S = \emptyset$, $\pi_X(R) \times \emptyset = \emptyset$, do đó biểu thức cho ra $\pi_X(R) - \emptyset = \pi_X(R)$, hoàn toàn nhất quán.

## 4. Hiện thực hóa trên SQL Server: Đại số quan hệ vs Truy vấn ứng viên độc lập

Trong môi trường T-SQL thực tế, lập trình viên cần phân biệt rõ ràng giữa hai bài toán:

### Trường hợp A: Truy vấn phổ quát với Bảng ứng viên độc lập (Independent Candidate Table)
Trong thực tế phát triển phần mềm, miền ứng viên thường được lưu trong một bảng quan hệ độc lập $C$ (ví dụ: `dbo.tr_students`), còn bằng chứng nằm ở bảng liên kết $R$ (`dbo.tr_results`).
Khi đó cấu trúc chuẩn mực hai tầng [[theory/double-not-exists|Double NOT EXISTS]] được viết như sau:

```sql
SELECT c.StudentId, c.FullName
FROM dbo.tr_students AS c -- Bảng miền ứng viên độc lập C
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.RequiredCourses AS s -- Tập yêu cầu S
    WHERE NOT EXISTS (
        SELECT 1
        FROM dbo.tr_results AS r -- Bảng bằng chứng R
        WHERE r.StudentId = c.StudentId
          AND r.CourseId = s.CourseId
    )
);
```

**Hành vi khi $S = \emptyset$:** Mệnh đề `NOT EXISTS (SELECT 1 FROM dbo.RequiredCourses ...)` đánh giá thành `TRUE` cho **toàn bộ mọi dòng trong bảng ứng viên $c \in C$**.
Do đó, câu truy vấn SQL trả về toàn bộ mọi ứng viên từ bảng miền ứng viên độc lập $\pi_{\text{StudentId, FullName}}(C)$ (bao gồm cả những sinh viên mới nhập học chưa từng có dòng nào trong bảng bằng chứng `tr_results`).
*Điểm cần lưu ý:* Không đánh đồng tập thuộc tính $X$ trong đại số quan hệ (vốn chỉ là thuộc tính của $R$) với một bảng quan hệ ứng viên độc lập $C$ trong SQL.

### Trường hợp B: Kỹ thuật Gom nhóm và Đếm (Aggregation Alternative)
Sử dụng `GROUP BY` kết hợp mệnh đề `HAVING`:

```sql
-- Trường phái đếm nhóm:
-- BẮT BUỘC phải giới hạn bằng chứng vào tập yêu cầu S trước khi đếm
SELECT r.StudentId
FROM dbo.tr_results AS r
JOIN dbo.RequiredCourses AS s ON r.CourseId = s.CourseId -- Giới hạn bằng chứng vào đúng tập S
GROUP BY r.StudentId
HAVING COUNT(DISTINCT r.CourseId) = (SELECT COUNT(*) FROM dbo.RequiredCourses);
```

#### Ba giới hạn ngữ nghĩa bắt buộc phải nắm vững khi dùng kỹ thuật Đếm nhóm:
1. **Bắt buộc giới hạn bằng chứng vào tập $S$:** Nếu không thực hiện `JOIN dbo.RequiredCourses AS s ON r.CourseId = s.CourseId` (hoặc `WHERE r.CourseId IN (SELECT CourseId FROM dbo.RequiredCourses)`), hàm `COUNT(DISTINCT r.CourseId)` sẽ đếm cả những môn ngoài yêu cầu. Một sinh viên học đủ số lượng môn nhưng sai ngành/khoa sẽ bị nhận diện nhầm thành đạt yêu cầu.
2. **Hành vi khi tập yêu cầu rỗng ($S = \emptyset$):** Phép `JOIN dbo.RequiredCourses` khi bảng yêu cầu rỗng sẽ triệt tiêu 100% các dòng dữ liệu, khiến câu truy vấn đếm luôn trả về tập rỗng ($\emptyset$). Khi miền ứng viên hoặc quan hệ bằng chứng không rỗng, kết quả này làm sai lệch cả ngữ nghĩa đại số quan hệ cổ điển ($R \div \emptyset = \pi_X(R) \neq \emptyset$) lẫn ngữ nghĩa truy vấn ứng viên độc lập ($\pi_{\text{StudentId, FullName}}(C) \neq \emptyset$). Sự sai lệch này chỉ không xảy ra trong trường hợp tầm thường khi chính miền ứng viên hoặc quan hệ bằng chứng cũng rỗng ngay từ đầu.
3. **Bỏ sót ứng viên chưa có bằng chứng:** Câu lệnh `FROM dbo.tr_results AS r` chỉ duyệt qua các sinh viên đã có điểm thi trong hệ thống. Nếu muốn xét toàn bộ sinh viên trong trường, bắt buộc phải xuất phát từ `dbo.tr_students` và sử dụng `LEFT JOIN`.

Xem minh họa kịch bản thực hành tại [[practice/lab-03|Lab 03 — Truy vấn nâng cao]], bài tập có lời giải tại [[exercises/division-exercise|Bài tập phép chia]], và kỹ thuật tổng hợp truy vấn phổ quát tại [[cheat-sheets/universal-query|Bảng tra Universal Query]].
