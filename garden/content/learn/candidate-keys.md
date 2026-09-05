---
title: Khóa ứng viên (Candidate Keys) · Học chủ động
description: Bài học chủ động về Khóa ứng viên — Hiểu bản chất, bao đóng, rẽ nhánh L/R/N/LR, kiểm tra tối thiểu và tránh bẫy đề thi.
type: learning-unit
chapter: ch06
skill_id: candidate-keys
priority: core
prerequisites: [closure]
related: [theory/candidate-keys, theory/closure, theory/functional-dependencies]
exam_weight: high
has_trace: true
has_recall: true
has_practice: true
has_diagnosis: true
provenance: verified-artifact
courseEvidence: [UIT-O05, LOC-LEC-LONG-CH06]
---

<div class="learning-shell">

<!-- Top Navigation & Reference Mode Link -->
<nav class="learning-nav-bar" aria-label="Điều hướng bài học">
<a href="./theory" class="learning-breadcrumb-link">← Chương 6 · Phụ thuộc hàm &amp; Chuẩn hóa</a>
<a href="./theory/candidate-keys" class="ref-mode-link" title="Xem bài viết tra cứu lý thuyết đầy đủ trong Vườn tri thức">
<span>📖 Tra cứu lý thuyết đầy đủ</span>
<span aria-hidden="true">↗</span>
</a>
</nav>

<!-- Learning Unit Hero Header -->
<header class="learning-header">
<div class="learning-badge-row">
<span class="learning-chapter-tag">Chương 6 · Trọng tâm thi</span>
<span class="learning-time-estimate">⏱ Thời lượng ước tính: ~30–45 phút</span>
</div>
<h1 class="learning-title">Khóa ứng viên (Candidate Keys)</h1>
<p class="learning-summary">
Bạn sẽ nắm vững cách tìm <strong>TẤT CẢ</strong> các khóa ứng viên của lược đồ quan hệ, hiểu sâu sắc sự khác biệt giữa <em>Siêu khóa</em> và <em>Khóa ứng viên tối thiểu</em>, và tránh các bẫy phổ biến trong đề thi UIT.
</p>
</header>

<!-- Mastery Progress Indicator -->
<div class="mastery-card" aria-live="polite">
<div class="mastery-info">
<span class="mastery-label-prefix">Cấp độ thông thạo hiện tại</span>
<span class="mastery-status-badge" data-mastery="UNSEEN">Chưa học (UNSEEN)</span>
</div>
<button type="button" class="btn-reset-mastery" title="Xóa dữ liệu luyện tập cục bộ để học lại từ đầu">
↺ Đặt lại tiến độ
</button>
</div>

<!-- Stage Progress Ladder -->
<div class="stage-progress-ladder" aria-label="Các giai đoạn học tập">
<span class="stage-step stage-active">1. Bản đồ</span>
<span class="stage-arrow">→</span>
<span class="stage-step">2. Bản chất</span>
<span class="stage-arrow">→</span>
<span class="stage-step">3. Vết thuật toán</span>
<span class="stage-arrow">→</span>
<span class="stage-step">4. Luyện có giàn giáo</span>
<span class="stage-arrow">→</span>
<span class="stage-step">5. Tự giải độc lập</span>
<span class="stage-arrow">→</span>
<span class="stage-step">6. Chẩn đoán</span>
<span class="stage-arrow">→</span>
<span class="stage-step">7. Hồi tưởng</span>
</div>

<!-- BLOCK 1: PURPOSE -->
<section class="learning-block" id="block-purpose">

## 1. Mục đích: Tại sao cần tìm Candidate Key?

Trong thiết kế cơ sở dữ liệu quan hệ, chúng ta cần đảm bảo mỗi bộ dữ liệu (tuple) được phân biệt duy nhất mà không lãng phí dung lượng lưu trữ. **Khóa ứng viên** là tập thuộc tính *nhỏ nhất* có thể định danh toàn bộ quan hệ. Nếu không tìm được tất cả các khóa, bạn không thể chọn Khóa chính (`PRIMARY KEY`) tối ưu, không xác định đúng thuộc tính khóa, và chắc chắn sẽ phân tích sai các dạng chuẩn 3NF và BCNF trong đề thi.

</section>

<!-- BLOCK 2: PREREQUISITE MAP -->
<section class="learning-block" id="block-prerequisites">

## 2. Bản đồ tiền đề (Prerequisite Map)

Để tìm được khóa ứng viên một cách chính xác, bạn cần dựa trên chuỗi kiến thức nền tảng sau:

<div class="concept-map-grid">
<div class="concept-card">

#### 1. Phụ thuộc hàm (FD)

Mối liên hệ $X \rightarrow Y$: biết giá trị của $X$ thì suy ra duy nhất giá trị của $Y$.

</div>
<div class="concept-card">

#### 2. Bao đóng thuộc tính ($X^+$)

Tập tất cả thuộc tính suy dẫn được từ $X$. Công cụ tính toán trực tiếp để kiểm tra khóa.

</div>
<div class="concept-card">

#### 3. Siêu khóa (Superkey)

Tập thuộc tính $K$ có bao đóng phủ kín toàn bộ quan hệ: $K^+ = U$.

</div>
<div class="concept-card card-candidate-key">

#### 4. Khóa ứng viên

Siêu khóa **tối thiểu**: không có tập con thực sự nào vẫn là siêu khóa.

</div>
</div>

<details class="closure-refresher">
<summary><strong>Nhắc nhanh thuật toán tính Bao đóng $X^+$ (Bấm để xem)</strong></summary>
<div style="margin-top: 0.75rem; padding: 0.75rem; background: var(--lightgray); border-radius: 6px;">

1. Khởi tạo: $X^{(0)} = X$.
2. Lặp: Với mỗi $V \rightarrow W \in F$, nếu $V \subseteq X^{(k)}$ thì $X^{(k+1)} = X^{(k)} \cup W$.
3. Dừng khi $X^{(k+1)} = X^{(k)}$ (điểm bất động) hoặc khi $X^{(k)} = U$. Đặt $X^+ = X^{(k)}$.

Xem chi tiết tại [Bao đóng thuộc tính (Attribute Closure)](./theory/closure).

</div>
</details>

</section>

<!-- BLOCK 3: CONCEPT MAP / 80-20 CORE -->
<section class="learning-block" id="block-concept-map">

## 3. Phân biệt cốt lõi: Siêu khóa vs Khóa ứng viên vs Khóa chính

Đây là điểm 80/20 quan trọng nhất. Rất nhiều sinh viên nhầm lẫn giữa điều kiện ĐỦ và điều kiện TỐI THIỂU:

<div class="concept-map-grid">
<div class="concept-card card-superkey">

#### Siêu khóa (Superkey)

**Điều kiện: ĐỦ ($K^+ = U$)**

Chỉ cần bao đóng bằng toàn bộ quan hệ $U$. Có thể chứa các thuộc tính thừa thãi, không cần tối thiểu.

</div>
<div class="concept-card card-candidate-key">

#### Khóa ứng viên (Candidate Key)

**Điều kiện: ĐỦ + TỐI THIỂU**

Là siêu khóa nhưng **không thể bỏ bớt** bất kỳ thuộc tính nào mà vẫn là siêu khóa. Nếu bỏ bớt một thuộc tính, bao đóng sẽ không còn là $U$.

</div>
<div class="concept-card card-primary-key">

#### Khóa chính (Primary Key)

**Điều kiện: Đúng 1 khóa được chọn**

Người thiết kế cơ sở dữ liệu chọn ra đúng một Khóa ứng viên thích hợp nhất để làm khóa chính cho bảng.

</div>
</div>

<div style="margin-top: 1rem; padding: 1rem; border: 1px solid var(--lightgray); border-radius: 6px;">

<h4 style="margin-top: 0;">Kiểm tra nhanh định hướng</h4>

<form id="form-orientation-check" class="interactive-form">
<p style="margin: 0;">Khẳng định nào sau đây là <strong>đúng nhất</strong>?</p>
<label style="display: flex; gap: 0.5rem; align-items: center; cursor: pointer;">
<input type="radio" name="orientation-q1" value="sufficient" required />
<span>Mọi tập thuộc tính có bao đóng bằng U đều là Khóa ứng viên.</span>
</label>
<label style="display: flex; gap: 0.5rem; align-items: center; cursor: pointer;">
<input type="radio" name="orientation-q1" value="minimal" />
<span>Khóa ứng viên bắt buộc phải là Siêu khóa tối thiểu (không chứa thuộc tính dư thừa).</span>
</label>
<label style="display: flex; gap: 0.5rem; align-items: center; cursor: pointer;">
<input type="radio" name="orientation-q1" value="primary" />
<span>Khóa chính và Khóa ứng viên là hai tập thuộc tính hoàn toàn độc lập với nhau.</span>
</label>
<button type="submit" class="interactive-btn-submit">Xác nhận câu trả lời</button>
</form>

<div id="feedback-orientation"></div>

</div>

</section>

<!-- BLOCK 4: MENTAL MODEL -->
<section class="learning-block" id="block-mental-model">

## 4. Mô hình tư duy tìm khóa (Mental Model)

Thay vì thử ngẫu nhiên tổ hợp, hãy dùng tư duy 3 nhịp có hệ thống:

- **Nhịp 1 — Bắt buộc phải có ($L \cup N$):** Thuộc tính không thể được suy ra từ ai khác bắt buộc phải có mặt trong mọi khóa. Đây là hạt nhân xuất phát.
- **Nhịp 2 — Thêm tối thiểu từ $LR$:** Nếu hạt nhân chưa đủ để bao đóng thành $U$, ta thử kết hợp thêm tối thiểu các thuộc tính nhóm $LR$ theo từng bậc tăng dần (bậc 1, bậc 2...).
- **Nhịp 3 — Cắt tỉa nhánh (Branch Pruning):** Ngay khi tìm thấy một khóa ứng viên $K$, mọi tập mở rộng chứa $K$ (như $K \cup \{X\}$) chắc chắn là siêu khóa dư thừa. Cắt bỏ ngay nhánh đó không cần tính tiếp!

</section>

<!-- BLOCK 5: MECHANISM -->
<section class="learning-block" id="block-mechanism">

## 5. Cơ chế phân loại L / R / N / LR

Thuật toán chính khóa tại UIT dựa trên việc phân loại tập thuộc tính $U$ thành 4 nhóm độc lập:

| Nhóm | Vị trí xuất hiện trong các FD | Vai trò trong Khóa ứng viên |
| :--- | :--- | :--- |
| **$L$ (Left only)** | Chỉ xuất hiện ở vế trái | **Bắt buộc** có mặt trong TẤT CẢ các khóa ứng viên. |
| **$N$ (Neither)** | Không xuất hiện ở cả hai vế | **Bắt buộc** có mặt trong TẤT CẢ các khóa ứng viên. |
| **$R$ (Right only)** | Chỉ xuất hiện ở vế phải | **Không bao giờ** xuất hiện trong bất kỳ khóa tối thiểu nào. |
| **$LR$ (Both)** | Xuất hiện ở cả hai vế | **Có thể** thuộc về một số khóa; dùng để rẽ nhánh tổ hợp. |

**Quy trình thực thi chuẩn:**

1. Đặt tập nguồn $S = L \cup N$.
2. Tính $S^+$. Nếu $S^+ = U$, suy ra $S$ là **khóa ứng viên DUY NHẤT**. Kết thúc!
3. Nếu $S^+ \subset U$, lần lượt kết hợp $S$ với các tổ hợp 1, 2, 3... thuộc tính trong nhóm $LR$. Kiểm tra tính tối thiểu và cắt tỉa nhánh.

</section>
<!-- BLOCK 6: EXECUTION TRACE (TraceStepper) -->
<section class="learning-block" id="block-trace">

## 6. Vết thực thi tương tác (Interactive TraceStepper)

Theo dõi từng bước thực thi của thuật toán tìm toàn bộ khóa ứng viên trên bài toán kinh điển:

$R(A, B, C, D, E)$ với tập phụ thuộc hàm $F = \{A \rightarrow BC, \; CD \rightarrow E, \; B \rightarrow D, \; E \rightarrow A\}$.

<div class="trace-stepper-container" tabindex="0" aria-label="Bộ trình diễn vết thuật toán">
<div class="stepper-header">
<span class="stepper-step-counter">Bước 0 / 10</span>
<span class="stepper-step-title" style="font-weight: 600;">Bước 0 — Phân loại thuộc tính</span>
</div>

<div class="stepper-body">
<div class="stepper-state-row">
<div class="state-chip">
<span class="chip-label">Tập đang xét</span>
<span class="stepper-current-set" style="font-family: monospace; font-weight: bold;">L: ∅, LR: {A,B,C,D,E}</span>
</div>
<div class="state-chip">
<span class="chip-label">Thao tác hiện tại</span>
<span class="stepper-action" style="font-weight: 500;">Lập bảng phân loại</span>
</div>
<div class="state-chip">
<span class="chip-label">Bao đóng thu được</span>
<span class="stepper-closure" style="font-family: monospace;">Chưa tính</span>
</div>
</div>

<div class="stepper-reasoning-box">
<p class="stepper-reasoning" style="margin: 0;"></p>
</div>

<p style="font-size: 0.9rem; color: var(--gray); margin: 0;">
<strong>Nhánh tiếp theo:</strong> <span class="stepper-continues"></span>
</p>
</div>

<div class="stepper-footer">
<button type="button" class="stepper-btn stepper-btn-prev" disabled>← Bước trước</button>
<span style="font-size: 0.8rem; color: var(--gray); align-self: center;">Mẹo: Bạn có thể dùng phím mũi tên Trái / Phải để duyệt</span>
<button type="button" class="stepper-btn stepper-btn-next">Bước tiếp →</button>
</div>
</div>

</section>

<!-- BLOCK 7: WORKED EXAMPLE -->
<section class="learning-block" id="block-worked">

## 7. Ví dụ giải mẫu chi tiết (Worked Example: `ck-worked-001`)

**Đề bài:** Cho lược đồ quan hệ $R(A, B, C, D, E)$ và tập phụ thuộc hàm:

$$F = \{AB \rightarrow C, \; C \rightarrow D, \; D \rightarrow E, \; E \rightarrow A\}$$

Hãy tìm tất cả các khóa ứng viên của $R$.

<div style="background: var(--lightgray); padding: 1.25rem; border-radius: 6px; line-height: 1.6;">

#### Lời giải từng bước với giải thích "Tại sao":

**Bước 1: Lập bảng phân loại vị trí xuất hiện**
- Tập vế trái: $LHS = \{A, B, C, D, E\}$.
- Tập vế phải: $RHS = \{C, D, E, A\}$.
- Do đó: Thuộc tính $B$ chỉ xuất hiện ở vế trái: $B \in L$.
- Do đó: Các thuộc tính $A, C, D, E$ xuất hiện ở cả hai vế: $LR = \{A, C, D, E\}$.
- Do đó: Không có thuộc tính nhóm $R$ hoặc $N$: $R = \emptyset$, $N = \emptyset$.

**Bước 2: Xác định tập nguồn bắt buộc**
Tập nguồn bắt buộc là $S = L \cup N = \{B\}$. Mọi khóa ứng viên đều *bắt buộc phải chứa $B$* vì không có bất kỳ FD nào suy ra được $B$.

**Bước 3: Tính bao đóng của tập nguồn**
Tính $\{B\}^+$: Không có FD nào có vế trái là $B$ đứng một mình, suy ra $\{B\}^+ = \{B\} \neq U$.
Do đó $B$ không thể đứng một mình làm khóa. Ta cần kết hợp $B$ với các thuộc tính trong $LR$.

**Bước 4: Rẽ nhánh tổ hợp bậc 2 (kết hợp B với từng phần tử LR)**
- *Nhánh {B, A}:* $\{AB\}^+ = ABCDE = U$ (do $AB \rightarrow C \rightarrow D \rightarrow E$).
  Kiểm tra tối thiểu: $\{B\}^+ \neq U$, $\{A\}^+ = \{A\} \neq U$, suy ra **$AB$ là Khóa ứng viên 1**.
- *Nhánh {B, C}:* $\{BC\}^+ = BCDEA = U$ (do $C \rightarrow D \rightarrow E \rightarrow A$, kết hợp $B$ suy ra $C$).
  Kiểm tra tối thiểu: $\{B\}^+ \neq U$, $\{C\}^+ = \{C, D, E\} \neq U$, suy ra **$BC$ là Khóa ứng viên 2**.
- *Nhánh {B, D}:* $\{BD\}^+ = BDEAC = U$ (do $D \rightarrow E \rightarrow A$, suy ra $AB \rightarrow C$).
  Kiểm tra tối thiểu: $\{B\}^+ \neq U$, $\{D\}^+ \neq U$, suy ra **$BD$ là Khóa ứng viên 3**.
- *Nhánh {B, E}:* $\{BE\}^+ = BEACD = U$ (do $E \rightarrow A$, suy ra $AB \rightarrow C \rightarrow D$).
  Kiểm tra tối thiểu: $\{B\}^+ \neq U$, $\{E\}^+ \neq U$, suy ra **$BE$ là Khóa ứng viên 4**.

**Bước 5: Áp dụng quy tắc cắt tỉa nhánh bậc 3+**
Mọi tổ hợp bậc 3 chứa $B$ đều có dạng $BXY$ với $X, Y \in \{A, C, D, E\}$. Vì bất kỳ tổ hợp nào cũng chứa một trong các khóa đã tìm thấy ($AB, BC, BD, BE$), chúng đều là siêu khóa không tối thiểu. Cắt tỉa toàn bộ!

**Kết luận:** Quan hệ $R$ có đúng 4 khóa ứng viên: **$AB, BC, BD, BE$**.

</div>

</section>

<!-- BLOCK 8: SELF-EXPLANATION PROMPTS -->
<section class="learning-block" id="block-self-explanation">

## 8. Câu hỏi tự giải thích (Self-Explanation Prompts)

Hãy tự trả lời hai câu hỏi sâu này trước khi xem đáp án để củng cố mô hình tư duy:

<div style="border-left: 3px solid var(--secondary); padding-left: 1rem; margin-bottom: 1.5rem;">

**Câu hỏi 1:** Tại sao thuộc tính $B$ bắt buộc phải xuất hiện trong *tất cả* các khóa ứng viên của $R$ ở ví dụ trên?

<button type="button" id="btn-check-self-1" class="stepper-btn">Xem giải thích</button>

<div id="answer-self-1" style="display: none; margin-top: 0.75rem; background: var(--lightgray); padding: 0.75rem; border-radius: 4px;">

*Bản chất:* Vì $B \in L$ (không nằm ở vế phải của bất kỳ FD nào trong $F$). Nếu một tập thuộc tính không chứa $B$, bao đóng của nó không bao giờ có thể sinh ra $B$, do đó không thể phủ kín quan hệ $U$.

</div>
</div>

<div style="border-left: 3px solid var(--secondary); padding-left: 1rem;">

**Câu hỏi 2:** Tại sao ta không cần tính bao đóng của tổ hợp bậc 3 như $\{A, B, C\}$?

<button type="button" id="btn-check-self-2" class="stepper-btn">Xem giải thích</button>

<div id="answer-self-2" style="display: none; margin-top: 0.75rem; background: var(--lightgray); padding: 0.75rem; border-radius: 4px;">

*Bản chất:* Vì $\{A, B\}$ đã được chứng minh là một khóa ứng viên, nên tập cha $\{A, B, C\}$ hiển nhiên có $\{A, B, C\}^+ = U$, nhưng nó chứa tập con thực sự $\{A, B\}$ cũng có bao đóng bằng $U$. Theo định nghĩa, $\{A, B, C\}$ là siêu khóa dư thừa (không tối thiểu). Việc tính tiếp sẽ lãng phí thời gian thi!

</div>
</div>

</section>

<!-- BLOCK 9: FADED EXAMPLE -->
<section class="learning-block" id="block-faded">

## 9. Luyện tập có giàn giáo (Faded Example: `ck-faded-001`)

Cho $R(A, B, C, D)$ với $F = \{A \rightarrow B, \; B \rightarrow C, \; C \rightarrow D, \; D \rightarrow B\}$.

Phân loại đã cho sẵn: $L = \{A\}$, $R = \emptyset$, $N = \emptyset$, $LR = \{B, C, D\}$.

Hãy hoàn thành các bước suy luận còn khuyết bên dưới:

<form id="form-faded-example" class="interactive-form">
<div>
<label for="faded-blank-1"><strong>1. Tập nguồn bắt buộc S = L ∪ N là:</strong></label>
<input type="text" id="faded-blank-1" class="interactive-input" placeholder="Ví dụ: A" required />
</div>

<div>
<label for="faded-blank-2"><strong>2. Tính bao đóng của tập nguồn {A}+:</strong></label>
<input type="text" id="faded-blank-2" class="interactive-input" placeholder="Ví dụ: ABCD" required />
</div>

<div>
<label><strong>3. Tập {A} có phải là Khóa ứng viên tối thiểu không?</strong></label>
<div style="display: flex; gap: 1rem; margin-top: 0.25rem;">
<label><input type="radio" name="faded-q3" value="yes" required /> Có, vì không có tập con thực sự nào phủ được U</label>
<label><input type="radio" name="faded-q3" value="no" /> Không, vì phải có ít nhất 2 thuộc tính</label>
</div>
</div>

<button type="submit" class="interactive-btn-submit">Kiểm tra kết quả giàn giáo</button>
</form>

<div id="feedback-faded"></div>

</section>

<!-- BLOCK 10: COLD PROBLEM -->
<section class="learning-block" id="block-cold">

## 10. Bài tập độc lập (Cold Problem: `ck-cold-001`)

**Thử thách độc lập:** Không có lời giải hiển thị trước. Hãy tự giải hoàn chỉnh bài toán sau:

Cho lược đồ quan hệ $R(A, B, C, D, E)$ và tập phụ thuộc hàm $F$:

$$F = \{A \rightarrow B, \; BC \rightarrow D, \; D \rightarrow E, \; E \rightarrow C\}$$

Hãy tìm **tất cả** các khóa ứng viên của quan hệ $R$.

<div class="hint-drawer-section">
<div style="display: flex; justify-content: space-between; align-items: center;">
<span style="font-weight: 600; font-size: 0.9rem;">Hệ thống trợ giúp phân tầng (Hint Drawer)</span>
<button type="button" id="btn-cold-hint" class="stepper-btn">Xem gợi ý kế tiếp</button>
</div>
<div id="cold-hint-container"></div>
<div id="cold-hint-notice" class="hint-notice-warning" style="display: none;">
⚠️ Chú ý: Bạn đã mở gợi ý sâu (tầng 3 trở lên). Lượt làm bài này sẽ được tính là có hướng dẫn (GUIDED).
</div>
</div>

<form id="form-cold-problem" class="interactive-form">
<div>
<label for="cold-answer-input"><strong>Nhập tất cả các khóa ứng viên tìm được:</strong></label>
<input
type="text"
id="cold-answer-input"
class="interactive-input"
placeholder="Ví dụ: {AC, AD, AE} hoặc AC, AD, AE"
required
/>
<div style="font-size: 0.8rem; color: var(--gray); margin-top: 0.25rem;">
Hệ thống tự động chuẩn hóa: chấp nhận không phân biệt hoa thường, thứ tự khóa và thứ tự thuộc tính.
</div>
</div>

<button type="submit" class="interactive-btn-submit">Nộp bài &amp; Kiểm tra độ thông thạo</button>
</form>

<div id="feedback-cold"></div>

</section>
<!-- BLOCK 11: VARIANT / TRANSFER PROBLEM -->
<section class="learning-block" id="block-transfer">

## 11. Bài toán biến thể chuyển giao (Transfer Problem: `ck-transfer-001`)

Bài toán có cấu trúc khác biệt để kiểm tra xem bạn đã thực sự làm chủ cơ chế hay chỉ học vẹt:

Cho lược đồ $R(A, B, C, D, X)$ với tập phụ thuộc hàm:

$$F = \{AB \rightarrow C, \; C \rightarrow D, \; D \rightarrow A\}$$

*Lưu ý đặc biệt:* Quan sát kỹ thuộc tính $X$ và tìm tất cả các khóa ứng viên.

<form id="form-transfer-problem" class="interactive-form">
<div>
<label for="transfer-answer-input"><strong>Nhập danh sách khóa ứng viên:</strong></label>
<input
type="text"
id="transfer-answer-input"
class="interactive-input"
placeholder="Ví dụ: {ABX, BCX, BDX}"
required
/>
</div>
<button type="submit" class="interactive-btn-submit">Kiểm tra bài chuyển giao</button>
</form>

<div id="feedback-transfer"></div>

</section>

<!-- BLOCK 12: EXAM TRAP ACTIVITY -->
<section class="learning-block" id="block-exam-trap">

## 12. Bẫy đề thi UIT điển hình (Exam Trap: `ck-trap-001`)

Quan sát bài làm thực tế sau của một sinh viên trong phòng thi:

<div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 1rem; border-radius: 6px;">

Đề bài: $R(A, B, C, D)$, $F = \{A \rightarrow B, \; B \rightarrow C, \; C \rightarrow D\}$.

Bài làm của sinh viên:
"Ta có: $\{A, B\}^+ = ABCD = R$. Vậy khóa ứng viên của quan hệ là $AB$."

</div>

<form id="form-trap-activity" class="interactive-form">
<p style="margin: 0;"><strong>Lỗi nghiêm trọng nhất của bài làm trên là gì?</strong></p>
<label style="display: flex; gap: 0.5rem; align-items: center; cursor: pointer;">
<input type="radio" name="trap-choice" value="calc" required />
<span>Tính sai bao đóng của {A, B}.</span>
</label>
<label style="display: flex; gap: 0.5rem; align-items: center; cursor: pointer;">
<input type="radio" name="trap-choice" value="minimality" />
<span>Không kiểm tra tính tối thiểu: {A} đứng một mình đã phủ U, nên AB là siêu khóa dư thừa, không phải khóa ứng viên!</span>
</label>
<label style="display: flex; gap: 0.5rem; align-items: center; cursor: pointer;">
<input type="radio" name="trap-choice" value="syntax" />
<span>Chưa viết chữ PRIMARY KEY hoa.</span>
</label>
<button type="submit" class="interactive-btn-submit">Xác nhận phân tích bẫy</button>
</form>

<div id="feedback-trap"></div>

</section>

<!-- BLOCK 13: ERROR DIAGNOSIS REGISTRY -->
<section class="learning-block" id="block-diagnosis-registry">

## 13. Sổ tay chẩn đoán 6 lỗi sai kinh điển

Hệ thống tự động phát hiện và hướng dẫn khắc phục 6 dạng sai lầm tư duy sau:

<div style="display: flex; flex-direction: column; gap: 0.75rem;">

<div class="diagnosis-card">
<div class="diagnosis-badge">1. <code>minimality-not-checked</code></div>

**Triệu chứng:** Tìm được siêu khóa $K^+ = U$ và vội vàng kết luận là khóa ứng viên mà không thử bỏ bớt thuộc tính.

<div class="diagnosis-repair">

**Cách sửa:** Luôn kiểm tra bao đóng của từng tập con $K \setminus \{A\}$.

</div>
</div>

<div class="diagnosis-card">
<div class="diagnosis-badge">2. <code>closure-stopped-too-early</code></div>

**Triệu chứng:** Dừng vòng lặp bao đóng trước khi đạt điểm cố định.

<div class="diagnosis-repair">

**Cách sửa:** Quét lại toàn bộ tập FD sau mỗi lần có thêm thuộc tính mới cho đến khi không còn thuộc tính nào bổ sung.

</div>
</div>

<div class="diagnosis-card">
<div class="diagnosis-badge">3. <code>missing-mandatory-attribute</code></div>

**Triệu chứng:** Khóa ứng viên thiếu thuộc tính nhóm $L$ hoặc nhóm $N$.

<div class="diagnosis-repair">

**Cách sửa:** Lập bảng $L, R, N, LR$ trước tiên; mọi khóa đều phải chứa $L \cup N$.

</div>
</div>

<div class="diagnosis-card">
<div class="diagnosis-badge">4. <code>only-one-key-found</code></div>

**Triệu chứng:** Dừng lại sau khi tìm được 1 khóa thay vì duyệt hết các nhánh rẽ.

<div class="diagnosis-repair">

**Cách sửa:** Duyệt hết các nhánh tổ hợp khả dĩ từ $LR$ để không bỏ sót khóa và thuộc tính khóa.

</div>
</div>

<div class="diagnosis-card">
<div class="diagnosis-badge">5. <code>redundant-branch-search</code></div>

**Triệu chứng:** Mở rộng tìm kiếm trên tập cha của một khóa đã tìm thấy.

<div class="diagnosis-repair">

**Cách sửa:** Áp dụng quy tắc cắt tỉa: nếu $K$ là khóa, lập tức bỏ qua mọi tập $K \cup \{X\}$.

</div>
</div>

<div class="diagnosis-card">
<div class="diagnosis-badge">6. <code>incorrect-FD-application</code></div>

**Triệu chứng:** Kích hoạt FD $X \rightarrow Y$ khi vế trái $X$ chưa có đủ trong bao đóng.

<div class="diagnosis-repair">

**Cách sửa:** Chỉ được lấy $Y$ khi toàn bộ thuộc tính của $X$ đã có mặt.

</div>
</div>

</div>

</section>

<!-- BLOCK 14: CLOSED-BOOK RECALL -->
<section class="learning-block" id="block-recall">

## 14. Hồi tưởng đóng sách (Closed-Book Recall)

Đừng cuộn lên xem lại. Hãy tự gõ câu trả lời ngắn gọn từ trí nhớ để kích hoạt hiệu ứng truy xuất (Retrieval Practice):

<div class="recall-item">

<div class="recall-prompt-q">1. Khóa ứng viên cần thỏa mãn đồng thời hai điều kiện gì?</div>

<textarea class="recall-textarea" placeholder="Nhập câu trả lời của bạn..."></textarea>

<div class="recall-model-answer">

**Đáp án chuẩn:** 1. Tính ĐỦ (là siêu khóa: $K^+ = U$) và 2. Tính TỐI THIỂU (không có tập con thực sự nào vẫn là siêu khóa).

</div>

</div>

<div class="recall-item">

<div class="recall-prompt-q">2. Thuộc tính thuộc nhóm L và nhóm N có vai trò gì trong mọi khóa ứng viên?</div>

<textarea class="recall-textarea" placeholder="Nhập câu trả lời của bạn..."></textarea>

<div class="recall-model-answer">

**Đáp án chuẩn:** Bắt buộc phải có mặt trong TẤT CẢ các khóa ứng viên (vì chúng không thể được sinh ra từ bất kỳ vế phải nào).

</div>

</div>

<div class="recall-item">

<div class="recall-prompt-q">3. Khi nào thì thuật toán tính bao đóng thuộc tính $X^+$ dừng lại?</div>

<textarea class="recall-textarea" placeholder="Nhập câu trả lời của bạn..."></textarea>

<div class="recall-model-answer">

**Đáp án chuẩn:** Khi đạt điểm bất động (duyệt một vòng tập FD mà không có thuộc tính mới nào được thêm vào) hoặc khi bao đóng đã chứa toàn bộ thuộc tính của quan hệ ($X^+ = U$).

</div>

</div>

<div class="recall-item">

<div class="recall-prompt-q">4. Nếu tìm được một khóa K, ta có cần xét các tập mở rộng dạng K ∪ {A} không? Vì sao?</div>

<textarea class="recall-textarea" placeholder="Nhập câu trả lời của bạn..."></textarea>

<div class="recall-model-answer">

**Đáp án chuẩn:** Không. Vì $K \cup \{A\}$ chắc chắn là siêu khóa nhưng không tối thiểu (chứa tập con $K$ cũng là siêu khóa). Cần cắt tỉa ngay.

</div>

</div>

<div class="recall-item">

<div class="recall-prompt-q">5. Việc tìm thiếu một khóa ứng viên sẽ dẫn đến hậu quả gì khi phân tích dạng chuẩn?</div>

<textarea class="recall-textarea" placeholder="Nhập câu trả lời của bạn..."></textarea>

<div class="recall-model-answer">

**Đáp án chuẩn:** Làm xác định thiếu thuộc tính khóa (prime attribute), dẫn đến việc kết luận sai một lược đồ đạt 3NF thành vi phạm 3NF.

</div>

</div>

<button type="button" id="btn-reveal-recall" class="interactive-btn-submit">
Đối chiếu với đáp án chuẩn
</button>

</section>

<!-- BLOCK 15: MASTERY UPDATE -->
<section class="learning-block" id="block-mastery-rules">

## 15. Quy chuẩn thăng hạng năng lực (Mastery State Rules)

Hệ thống đánh giá sự thông thạo của bạn dựa trên bằng chứng thực thi, không dựa trên lượt xem trang:

- `UNSEEN → ORIENTED`: Hoàn thành kiểm tra định hướng cốt lõi ở Mục 3.
- `ORIENTED → FOLLOWED`: Theo dõi hết các bước của bộ diễn vết tương tác ở Mục 6.
- `FOLLOWED → GUIDED`: Hoàn thành bài tập có giàn giáo ở Mục 9.
- `GUIDED → INDEPENDENT`: Tự giải chính xác Bài tập độc lập (Mục 10) mà **không sử dụng gợi ý sâu**.
- `INDEPENDENT → ROBUST`: Vượt qua bài kiểm tra ôn tập ngắt quãng (Spaced Retrieval) sau ít nhất 24 giờ.

</section>

<!-- BLOCK 16: REFERENCE MODE ESCAPE HATCH -->
<section class="learning-block" id="block-reference-mode">

## 16. Chuyển đổi chế độ: Tra cứu toàn văn (Reference Mode)

Khi bạn cần tra cứu định nghĩa toán học hình thức, đối chiếu bằng chứng giáo trình UIT gốc, hoặc đọc các bài viết liên quan trong Vườn tri thức:

<div style="display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 0.5rem;">
<a href="./theory/candidate-keys" class="ref-mode-link" style="font-size: 1rem; padding: 0.6rem 1rem;">
📖 Bài viết tra cứu Khóa ứng viên (Reference Mode)
</a>
<a href="./theory/closure" class="ref-mode-link" style="font-size: 1rem; padding: 0.6rem 1rem;">
🔍 Tra cứu lý thuyết Bao đóng thuộc tính ($X^+$)
</a>
<a href="./theory/functional-dependencies" class="ref-mode-link" style="font-size: 1rem; padding: 0.6rem 1rem;">
⚡ Tra cứu Phụ thuộc hàm &amp; Armstrong Axioms
</a>
</div>

</section>

</div>