---
title: Relational algebra
description: Hệ thống 8 phép toán hình thức của đại số quan hệ, tính khả hợp, các phép toán phái sinh và mối liên hệ với SQL.
type: theory
topics: [relational-algebra, selection, projection, join, division]
related: [theory/relational-model, theory/division, theory/double-not-exists, practice/lab-02, exam-patterns/relational-algebra]
provenance: verified-artifact
courseEvidence: [UIT-O02, LOC-LEC-LONG-CH03]
---
# Relational algebra (Đại số quan hệ)

Đại số quan hệ (Relational Algebra - RA) do E.F. Codd đề xuất là ngôn ngữ truy vấn hình thức mang tính thủ tục (procedural), đóng vai trò nền tảng toán học cho mô hình dữ liệu quan hệ và cơ chế tối ưu hóa câu truy vấn của các RDBMS hiện đại.

## 1. Bản chất và tính đóng (Closure Property)

- **Tính đóng:** Mọi phép toán trong đại số quan hệ đều nhận một hoặc hai quan hệ làm đầu vào và luôn trả về một quan hệ mới làm kết quả.
- **Tính lồng ghép:** Nhờ tính đóng, các phép toán có thể được lồng ghép không giới hạn để tạo thành các biểu thức đại số quan hệ phức tạp nhằm giải quyết các yêu cầu truy vấn nghiệp vụ.
- **Ngữ nghĩa tập hợp (Set Semantics):** Kết quả của mọi phép toán đại số quan hệ là một tập hợp toán học, do đó tự động loại bỏ các bộ trùng lặp (khác với cơ chế bag semantics đa tập của SQL thô, xem [[errors/unexpected-duplicates|Trùng lặp dòng ngoài ý muốn]]).

## 2. Nhóm phép toán tập hợp và điều kiện khả hợp

Để thực hiện các phép toán tập hợp giữa hai quan hệ $R$ và $S$, hai quan hệ bắt buộc phải **khả hợp (Union-compatible)**:
- Cùng bậc: Số lượng thuộc tính của $R$ và $S$ phải bằng nhau.
- Tương thích miền giá trị: Miền giá trị của thuộc tính thứ $i$ trong $R$ phải tương thích với thuộc tính thứ $i$ trong $S$.

### Ba phép toán tập hợp cơ bản:
1. **Phép hợp ($\cup$):** $R \cup S = \{t \mid t \in R \lor t \in S\}$.
2. **Phép giao ($\cap$):** $R \cap S = \{t \mid t \in R \land t \in S\} = R - (R - S)$.
3. **Phép trừ ($-$):** $R - S = \{t \mid t \in R \land t \notin S\}$. Lưu ý: Phép trừ không có tính giao hoán ($R - S \neq S - R$).

## 3. Nhóm phép toán quan hệ cơ bản

- **Phép chọn ($\sigma_C$):** Trích xuất các bộ trong quan hệ thỏa mãn điều kiện logic $C$:
  $$\sigma_C(R) = \{t \in R \mid C(t) = \text{true}\}$$
- **Phép chiếu ($\pi_L$):** Trích xuất danh sách các thuộc tính chỉ định $L = \{A_1, \dots, A_k\}$ và loại bỏ các cột còn lại:
  $$\pi_L(R) = \{t[L] \mid t \in R\}$$
- **Phép tích Descartes ($\times$):** Kết hợp mọi bộ của $R$ với mọi bộ của $S$:
  $$R(A_1, \dots, A_n) \times S(B_1, \dots, B_m) \implies \text{bậc } n+m, \text{ số bộ } |R| \times |S|$$

## 4. Nhóm phép toán phái sinh nâng cao

1. **Phép kết có điều kiện (Theta Join $\bowtie_\theta$):** Kết hợp tích Descartes với phép chọn theo điều kiện $\theta$:
   $$R \bowtie_\theta S = \sigma_\theta(R \times S)$$
2. **Phép kết tự nhiên (Natural Join $\bowtie$):** Ghép hai quan hệ dựa trên sự bằng nhau của tất cả các thuộc tính có cùng tên, tự động chiếu loại bỏ các cột trùng lặp.
3. **Phép chia ($\div$):** Dùng để giải quyết câu hỏi phổ quát "cho tất cả" (universal query). Chi tiết định nghĩa hình thức và thuật toán biến đổi xem tại [[theory/division|Phép chia hình thức]].

## 5. Ánh xạ biểu thức đại số quan hệ sang SQL Server

| Đại số quan hệ | Mệnh đề T-SQL tương đương | Lưu ý ngữ nghĩa |
| :---: | :---: | :--- |
| $\sigma_C(R)$ | `SELECT * FROM R WHERE C` | SQL dùng logic 3 trị với NULL |
| $\pi_L(R)$ | `SELECT DISTINCT L FROM R` | Phải có `DISTINCT` để đảm bảo set semantics |
| $R \bowtie S$ | `SELECT * FROM R INNER JOIN S ON ...` | Nối theo khóa chính / khóa ngoại |
| $R - S$ | `SELECT * FROM R EXCEPT SELECT * FROM S` | T-SQL tự động khử trùng lặp |
| $R \div S$ | Dùng kỹ thuật [[theory/double-not-exists|Double NOT EXISTS]] | Hoặc kiểm tra đếm với `COUNT(DISTINCT)` |

Luyện tập kết nối bảng trong thực hành tại [[practice/lab-02|Lab 02 — DML và JOIN]], truy vấn nâng cao tại [[practice/lab-03|Lab 03 — Truy vấn nâng cao]], và khảo sát cấu trúc đề thi tại [[exam-patterns/relational-algebra|Observed pattern — relational algebra]]. Căn cứ mô hình dữ liệu nền tảng tại [[theory/relational-model|Relational model]].
