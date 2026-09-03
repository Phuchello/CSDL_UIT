---
title: Candidate keys
description: Định nghĩa siêu khóa, khóa ứng viên tối thiểu, và thuật toán phân loại L/R/N/LR để tìm toàn bộ khóa quan hệ.
type: theory
topics: [candidate-keys, keys, closure]
related: [theory/functional-dependencies, theory/closure, theory/minimal-cover, theory/3nf, theory/bcnf]
provenance: verified-artifact
courseEvidence: [UIT-O05, LOC-LEC-LONG-CH06]
---
# Candidate keys (Khóa ứng viên)

Khóa ứng viên là khái niệm trung tâm trong lý thuyết thiết kế cơ sở dữ liệu quan hệ, làm cơ sở để xác định khóa chính (`PRIMARY KEY`), thuộc tính khóa và phân định các dạng chuẩn [[theory/3nf|3NF]] và [[theory/bcnf|BCNF]].

## 1. Định nghĩa hình thức

Cho lược đồ quan hệ $R$ với tập thuộc tính $U$ và tập phụ thuộc hàm $F$:
- **Siêu khóa (Superkey):** Tập thuộc tính $K \subseteq U$ là siêu khóa nếu $K^+ = U$ (tức bao đóng của $K$ theo $F$ bao quát toàn bộ thuộc tính của quan hệ).
- **Khóa ứng viên (Candidate Key):** Tập thuộc tính $K \subseteq U$ là khóa ứng viên nếu $K$ là siêu khóa tối thiểu — nghĩa là không tồn tại bất kỳ tập con thực sự $K' \subset K$ nào thỏa mãn $K'^+ = U$.
- **Thuộc tính khóa (Prime Attribute):** Mọi thuộc tính xuất hiện trong ít nhất một khóa ứng viên.
- **Thuộc tính không khóa (Non-prime Attribute):** Thuộc tính không thuộc bất kỳ khóa ứng viên nào.

## 2. Thuật toán tìm toàn bộ khóa ứng viên qua phân loại L / R / N / LR

Xét quan hệ $R(U)$ và tập phụ thuộc hàm $F$. Phân chia tập thuộc tính $U$ thành 4 nhóm độc lập dựa trên vị trí xuất hiện trong các phụ thuộc hàm $X \rightarrow Y \in F$:

| Nhóm | Vị trí xuất hiện | Vai trò trong khóa ứng viên |
| :---: | :--- | :--- |
| **$L$** | Chỉ xuất hiện ở vế trái (Left only) | **Bắt buộc** có mặt trong mọi khóa ứng viên. |
| **$N$** | Không xuất hiện ở cả hai vế (Neither) | **Bắt buộc** có mặt trong mọi khóa ứng viên. |
| **$R$** | Chỉ xuất hiện ở vế phải (Right only) | **Không bao giờ** xuất hiện trong bất kỳ khóa tối thiểu nào. |
| **$LR$** | Xuất hiện ở cả hai vế (Both) | **Có thể** thuộc về một số khóa; dùng để rẽ nhánh tổ hợp. |

### Quy trình 3 bước thực hiện:
1. **Khởi tạo tập nguồn bắt buộc:** Đặt $S = L \cup N$.
2. **Kiểm tra điều kiện dừng sớm:** Tính [[theory/closure|bao đóng]] $S^+$.
   - Nếu $S^+ = U$: Dừng lại ngay lập tức. $S$ chính là **khóa ứng viên duy nhất** của $R$.
3. **Rẽ nhánh tổ hợp (Branching):** Nếu $S^+ \subset U$, lần lượt kết hợp $S$ với từng tổ hợp 1, 2, 3... thuộc tính thuộc nhóm $LR$:
   - Tính bao đóng của từng tổ hợp $(S \cup \{A_i\})^+$.
   - Nếu bằng $U$: ghi nhận là một khóa ứng viên mới.
   - **Quy tắc cắt tỉa:** Không xét các tổ hợp bậc cao hơn đã chứa một khóa đã tìm được (để đảm bảo tính tối thiểu).

Xem thuật toán tính bao đóng tại [[theory/closure|Closure]] và mẫu bài thi điển hình tại [[exam-patterns/normalization|Observed pattern — normalization]].
