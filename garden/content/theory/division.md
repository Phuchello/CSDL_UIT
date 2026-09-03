---
title: Division — Phép chia hình thức cho truy vấn "Tất cả"
description: Định nghĩa toán học của phép chia quan hệ, thuật toán phân tích 3 tập hợp, công thức phái sinh Codd, kỹ thuật đếm nhóm và ánh xạ SQL.
type: theory
topics: [division, universal-query, relational-algebra]
related: [theory/relational-algebra, theory/double-not-exists, practice/lab-03, errors/wrong-universal-candidate, exercises/division-exercise]
provenance: verified-artifact
courseEvidence: [UIT-O02, LOC-LEC-LONG-CH03]
---
# Division (Phép chia hình thức cho truy vấn "Tất cả")

Phép chia quan hệ (Relational Division $R \div S$) là phép toán đại số quan hệ phái sinh giải quyết nhóm bài toán mang lượng từ phổ quát ($\forall$ - "Tất cả"). Đây là một trong những nội dung học thuật trọng tâm trong học phần IT004.

## 1. Định nghĩa toán học

Cho quan hệ $R$ có tập thuộc tính $U_R = X \cup Y$ và quan hệ $S$ có tập thuộc tính $U_S = Y$ (với $Y \subset U_R$ và $X \cap Y = \emptyset$).
**Phép chia $R \div S$** trả về một quan hệ trên tập thuộc tính $X$, gồm các bộ giá trị $t[X]$ sao cho với **mọi** bộ $u \in S$, bộ kết hợp $t[X] \circ u[Y]$ đều có mặt trong quan hệ $R$:

$$R \div S = \{t[X] \mid \forall u \in S, \exists r \in R \text{ sao cho } r[X] = t[X] \land r[Y] = u[Y]\}$$

## 2. Quy tắc 3 tập hợp phân tích bài toán chia

Mọi câu hỏi mang ý nghĩa "tất cả" đều có thể quy về 3 tập hợp rõ ràng:
1. **Tập ứng viên ($X$):** Thực thể cần tìm trong kết quả đầu ra (ví dụ: Danh sách sinh viên, Mã khách hàng, Mã nhân viên).
2. **Tập mục tiêu / yêu cầu ($Y$):** Danh sách toàn bộ các giá trị mẫu cần phải thỏa mãn (ví dụ: Tất cả môn học của Khoa HTTT, Tất cả sản phẩm xuất xứ từ Việt Nam).
3. **Tập bằng chứng ($R$):** Bảng dữ liệu lưu vết lịch sử liên kết thực tế giữa $X$ và $Y$ (ví dụ: Bảng kết quả học tập, Chi tiết hóa đơn bán hàng).

*Cảnh báo bẫy thi:* Việc trích xuất sai bảng ứng viên ngay từ đầu sẽ làm sai lệch tập lượng từ, xem chi tiết cảnh báo tại [[errors/wrong-universal-candidate|Sai miền ứng viên trong câu hỏi Tất cả]].

## 3. Công thức phái sinh Codd từ các phép toán cơ bản

Vì các hệ quản trị CSDL không hỗ trợ toán tử $\div$ trực tiếp, E.F. Codd đã chứng minh phép chia có thể biểu diễn qua [[theory/relational-algebra|Đại số quan hệ]] cơ bản (chọn, chiếu, tích Descartes và phép trừ):

$$R \div S = \pi_X(R) - \pi_X\Big( \big(\pi_X(R) \times S\big) - R \Big)$$

### Ý nghĩa trực quan từng bước:
- $\pi_X(R)$: Tập tất cả các ứng viên đã từng tham gia vào tập bằng chứng.
- $\pi_X(R) \times S$: Tập hợp tất cả các cặp (ứng viên, yêu cầu) lý thuyết mà mỗi ứng viên bắt buộc phải có nếu hoàn thành 100% mục tiêu.
- $(\pi_X(R) \times S) - R$: Tập các yêu cầu mà từng ứng viên còn **thiếu** (chưa xuất hiện trong bằng chứng).
- $\pi_X(\text{thiếu})$: Danh sách các ứng viên còn thiếu ít nhất 1 yêu cầu.
- Lấy toàn bộ trừ đi danh sách ứng viên còn thiếu sẽ thu được chính xác các ứng viên đã hoàn thành **tất cả**.

## 4. Hiện thực hóa trên SQL Server

Trong môi trường T-SQL, phép chia đại số quan hệ được hiện thực hóa qua hai trường phái chính:

### Trường phái 1: Phủ định tương quan (Double NOT EXISTS)
Sử dụng cấu trúc hai tầng phủ định tương quan [[theory/double-not-exists|Double NOT EXISTS]]:
- Phát biểu: *"Tìm ứng viên mà KHÔNG TỒN TẠI yêu cầu nào trong $S$ mà KHÔNG CÓ bằng chứng trong $R$"*.
- Ưu điểm: Chuẩn mực toán học, miễn nhiễm với bẫy NULL và xử lý chính xác ngay cả khi tập $S$ rỗng hoặc miền ứng viên mở rộng.

### Trường phái 2: Gom nhóm và Đếm (Aggregation Alternative)
Sử dụng `GROUP BY` kết hợp mệnh đề `HAVING`:

```sql
-- Trường phái đếm nhóm chuẩn xác:
-- BẮT BUỘC phải giới hạn bằng chứng vào tập yêu cầu S
SELECT r.CandidateId
FROM dbo.Evidence AS r
JOIN dbo.RequiredSet AS s ON r.ItemId = s.ItemId -- Giới hạn bằng chứng vào đúng tập S
GROUP BY r.CandidateId
HAVING COUNT(DISTINCT r.ItemId) = (SELECT COUNT(*) FROM dbo.RequiredSet);
```

#### Ba điều kiện biên bắt buộc phải lưu ý khi dùng kỹ thuật Đếm nhóm:
1. **Giới hạn bằng chứng vào tập $S$:** Nếu không thực hiện `JOIN dbo.RequiredSet AS s ON r.ItemId = s.ItemId` (hoặc `WHERE r.ItemId IN (SELECT ItemId FROM dbo.RequiredSet)`), `COUNT(DISTINCT r.ItemId)` sẽ đếm cả những mục nằm ngoài yêu cầu. Một ứng viên có đủ số lượng nhưng sai mục tiêu sẽ bị nhận diện nhầm thành thỏa mãn.
2. **Điều kiện tập yêu cầu rỗng ($S = \emptyset$):** Về mặt toán học hình thức, khi $S = \emptyset$, mệnh đề $\forall u \in \emptyset, \dots$ là chân lý rỗng (vacuously true), nên $R \div \emptyset$ phải trả về toàn bộ ứng viên trong $X$. Tuy nhiên, với truy vấn đếm, phép `JOIN` với bảng rỗng sẽ triệt tiêu toàn bộ dòng và trả về tập rỗng, sai lệch ngữ nghĩa toán học.
3. **Điều kiện miền ứng viên (Candidate Domain Condition):** Mệnh đề `FROM dbo.Evidence AS r` chỉ duyệt qua các ứng viên đã có ít nhất một dòng trong bằng chứng. Những ứng viên hợp lệ trong $X$ nhưng chưa phát sinh sự kiện sẽ bị bỏ sót hoàn toàn.

Xem minh họa kịch bản thực hành tại [[practice/lab-03|Lab 03 — Truy vấn nâng cao]], bài tập có lời giải tại [[exercises/division-exercise|Bài tập phép chia]], và kỹ thuật tổng hợp truy vấn phổ quát tại [[cheat-sheets/universal-query|Bảng tra Universal Query]].
