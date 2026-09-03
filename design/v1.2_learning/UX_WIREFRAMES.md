# CSDL_UIT v1.2 — UX Wireframes

Status: DESIGN ONLY. Wireframes are structural, not final visual styling.

## 1. UX principle

The current Quartz layout is excellent for reference browsing but too dense for active study. v1.2 keeps Quartz as the shell while introducing a focused **Learning Mode**.

Learning Mode follows Mayer-style coherence and segmenting principles:

- show one instructional objective at a time;
- keep signaling strong;
- hide nonessential metadata during learning;
- reveal detail progressively;
- keep learner control over progression.

## 2. Global navigation

Desktop primary navigation:

```text
CSDL_UIT
[ Học ] [ Luyện ] [ Ôn ] [ Thi ] [ Tra cứu ]
```

Mobile bottom navigation:

```text
Học    Luyện    Ôn    Thi    Tra cứu
```

`Tra cứu` opens the existing Knowledge Garden / Reference Mode.

## 3. Home — Learning Dashboard

```text
┌──────────────────────────────────────────────────────────────┐
│ IT004 · CƠ SỞ DỮ LIỆU                                      │
│                                                              │
│ Hôm nay bạn có bao nhiêu thời gian?                          │
│ [15 phút] [30 phút] [60 phút]                                │
├──────────────────────────────────────────────────────────────┤
│ CẦN ÔN                                                       │
│ 3 kỹ năng đến hạn                                            │
│                                                              │
│ Bao đóng                 hôm nay                  [Ôn]        │
│ Khóa ứng viên            yếu                      [Ôn]        │
│ GROUP BY                 sai 2 lần                [Ôn]        │
├──────────────────────────────────────────────────────────────┤
│ TIẾP TỤC                                                     │
│ Chương 6 · PTH & Chuẩn hóa                                  │
│ Khóa ứng viên                                                │
│ █████████████░░░  68%                                        │
│ [Tiếp tục học]                                               │
├──────────────────────────────────────────────────────────────┤
│ BẢN ĐỒ MÔN                                                   │
│ 1 Tổng quan              ●●●○○                               │
│ 2 ER & Mô hình quan hệ   ●●○○○                               │
│ 3 Đại số quan hệ         ●●●●○                               │
│ 4 SQL / T-SQL            ●●●○○                               │
│ 5 RBTV                   ●●○○○                               │
│ 6 PTH & Chuẩn hóa        ●●●○○                               │
└──────────────────────────────────────────────────────────────┘
```

Important: percentage is secondary. The primary signal is skill state and due review.

## 4. Chapter Map

Example: Ch06.

```text
Chương 6 · PTH & Chuẩn hóa

Bạn chỉ cần nắm 5 trục chính trước:

[1 Phụ thuộc hàm]
       ↓
[2 Bao đóng]
       ↓
[3 Khóa ứng viên]
       ↓
[4 Phủ tối thiểu]
       ↓
[5 3NF ↔ BCNF]

🔴 Cốt lõi   🟠 Hay thi   🟡 Thực hành   🔵 Mở rộng

[Kiểm tra đầu vào 5 câu]
```

Below the fold:

- prerequisites;
- supporting concepts;
- exam patterns;
- reference links.

## 5. Learning Unit shell

```text
┌──────────────────────────────────────────────────────────────┐
│ ← Chương 6                       Khóa ứng viên               │
│                                                              │
│ Map  Understand  Trace  Recall  Practice  Review             │
│  ✓       ✓        ●       ○        ○        ○                │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│                  CURRENT LEARNING STEP                       │
│                                                              │
│                         ...                                  │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│ [← Quay lại]                              [Tiếp tục →]        │
└──────────────────────────────────────────────────────────────┘
```

No graph/backlinks/properties/timestamps inside this shell.

A small `Tra cứu sâu hơn` link switches to Reference Mode for the same skill.

## 6. Stage — Purpose / Mental Model

```text
KHÓA ỨNG VIÊN DÙNG ĐỂ LÀM GÌ?

Ta cần tìm tập thuộc tính NHỎ NHẤT vẫn xác định được toàn bộ quan hệ.

                 Superkey
                    +
                Minimality
                    ↓
              Candidate Key

Nếu chỉ kiểm tra K⁺ = R mà không kiểm tra minimality,
bạn mới chứng minh được K là superkey.

[Cho tôi xem cơ chế]
```

One screen should not contain the whole textbook explanation.

## 7. Stage — Execution Trace

```text
Tính A⁺

Vòng 0                     {A}
                              │
A → BC                        ▼
Vòng 1                   {A,B,C}
                              │
B → D                         ▼
Vòng 2                 {A,B,C,D}
                              │
CD → E                        ▼
Vòng 3               {A,B,C,D,E}

[←]              Bước 3 / 4              [Bước tiếp →]
```

Rules:

- highlight only the currently applied dependency;
- keep previous states visible but visually quieter;
- optional `Tại sao áp dụng được?` reveal.

## 8. Stage — Closed-book Recall

When entering Recall, the explanatory content collapses.

```text
ĐÓNG TÀI LIỆU

Không nhìn lại phần trên.

1. Superkey khác Candidate Key ở điều kiện nào?

[ textarea .................................... ]

2. Nếu K⁺ = R thì đã đủ kết luận K là Candidate Key chưa?

[ Có ] [ Không ]

[So sánh với checklist]
```

Do not show a green/red answer before the learner commits a response.

## 9. Stage — Worked → Faded → Cold

### Worked

```text
Ví dụ mẫu
R(A,B,C,D,E)
F = {...}

Bước 1  Phân loại L/R/N/LR       [giải thích]
Bước 2  Tạo tập nguồn            [giải thích]
Bước 3  Tính closure             [giải thích]
Bước 4  Kiểm tra minimality      [giải thích]
```

### Faded

```text
Bước 1  L = ∅, R = ∅, N = ∅, LR = {...}
Bước 2  [ bạn điền ]
Bước 3  BC⁺ = [ bạn điền ]
Bước 4  BC có minimal không? [ Có / Không ]
```

### Cold

```text
BÀI TỰ LÀM

R(P,Q,R,S,T)
F = {...}

Tìm tất cả khóa ứng viên.

Không có hint mặc định.

[Kiểm tra]
```

## 10. Hint drawer

Hints appear in layers.

```text
Gợi ý 1 — Mục tiêu
Bạn đang cần chứng minh tập nào xác định toàn bộ R?

[Thêm gợi ý]

Gợi ý 2 — Quy tắc
Hãy bắt đầu từ các thuộc tính bắt buộc xuất hiện trong mọi khóa.

[Thêm gợi ý]

Gợi ý 3 — Bước kế tiếp
Thử tính closure của ...
```

Using a hint is not failure, but it prevents the attempt from counting as fully independent mastery.

## 11. Error Diagnosis panel

```text
Chưa đúng — lỗi nằm ở MENTAL MODEL, không phải phép tính.

Bạn đã tìm được BC⁺ = R nhưng chưa kiểm tra minimality.

Lỗi thường gặp:
SUPERKEY ≠ CANDIDATE KEY

Cách sửa:
1. Loại B → kiểm tra C⁺
2. Loại C → kiểm tra B⁺
3. Chỉ khi cả hai không còn là superkey, BC mới minimal.

[Thử lại bài này]
[1 bài cùng lỗi]
```

Never immediately replace the learner’s path with a full final solution unless requested.

## 12. Compare Mode

Example: 3NF vs BCNF.

```text
┌─────────────────────┬─────────────────────┐
│ 3NF                 │ BCNF                │
├─────────────────────┼─────────────────────┤
│ X superkey → OK     │ X superkey → OK     │
│                     │                     │
│ A prime can rescue  │ No prime rescue     │
│ a non-superkey X    │                     │
└─────────────────────┴─────────────────────┘

PHÂN LOẠI NHANH

B → D
B không là superkey
D là prime

[ 3NF only ] [ BCNF ] [ neither ]
```

## 13. Review Queue

```text
ÔN HÔM NAY · 7 PHÚT

1/4  Candidate Keys       Diagnose
2/4  Closure              Trace
3/4  GROUP BY             Exam trap
4/4  3NF vs BCNF          Compare

Không hiển thị lý thuyết trước.
```

After each item:

- Again;
- Hard;
- Good;

These labels modify a simple deterministic next-review interval.

## 14. Mistake Notebook

```text
LỖI CỦA TÔI

Candidate Keys     ██████  6
Universal Query    █████   5
GROUP BY           ███     3

Gần đây

03/09  Candidate Keys
       Quên kiểm tra minimality
       [Ôn lại]

03/09  NOT IN
       Không xét NULL
       [Ôn lại]
```

Focus on actionable error classes, not shame/gamification.

## 15. Exam Mode

```text
ĐỀ LUYỆN IT004                    73:42
──────────────────────────────────────────
Câu 2 / 8

...

[Đánh dấu xem lại]                 [Tiếp]
```

Hidden during exam:

- hints;
- graph;
- backlinks;
- theory links;
- explanations.

Result screen:

```text
7.8 / 10

Không cần ôn lại
✓ JOIN
✓ Relational algebra basics

Cần vá
! Candidate Keys — minimality
! RBTV — impact table
! Universal Query — candidate domain

[Tạo buổi ôn từ các lỗi này]
```

## 16. Reference Mode cleanup

The Reference Mode may keep Quartz’s Explorer/graph/backlinks, but reader-facing defaults should be cleaner than the current live layout.

Hide or collapse by default:

- Properties block;
- raw `description` row;
- modified timestamp unless useful;
- source/provenance metadata.

Provide an explicit `Thông tin nguồn & metadata` disclosure for advanced/reference users.

## 17. Responsive rules

### Desktop ≥ 1100 px

Learning Mode:

- max content width ~800–920 px;
- optional compact chapter progress rail;
- no permanent right context rail.

### Tablet 700–1099 px

- one main column;
- chapter map scrolls vertically;
- no horizontal compare table overflow; compare cards stack if needed.

### Mobile ≤ 699 px

- one learning task per viewport;
- bottom navigation;
- sticky `Tiếp tục` action;
- code/math blocks horizontally scroll only when unavoidable;
- no overall page horizontal overflow.

## 18. Accessibility requirements

- full keyboard navigation;
- visible focus state;
- semantic heading order;
- no answer state communicated by color alone;
- touch target ≥ 44 px where practical;
- motion optional/reduced-motion friendly;
- math remains readable with KaTeX semantics;
- dark/light themes preserve contrast.
