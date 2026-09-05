/**
 * CSDL_UIT Active Learning Client Runtime
 *
 * Runs inside the browser on pages containing .learning-shell.
 * Manages interactive TraceStepper, progressive HintDrawer, answer normalization,
 * deterministic error diagnosis, and versioned localStorage mastery state.
 */

import { compareCandidateKeys, normalizeKeySet } from "../../learning/normalizer"
import {
  loadLearnerStore,
  getSkillProgress,
  recordOrientationComplete,
  recordTraceComplete,
  recordFadedComplete,
  recordProblemAttempt,
  resetSkillProgress,
} from "../../learning/mastery"
import { diagnoseCandidateKeySubmission, ERROR_REGISTRY, ProblemContext } from "../../learning/diagnosis"
import { MasteryState } from "../../learning/types"

const SKILL_ID = "candidate-keys"

const MASTERY_LABELS: Record<MasteryState, string> = {
  UNSEEN: "Chưa học (UNSEEN)",
  ORIENTED: "Đã định hướng (ORIENTED)",
  FOLLOWED: "Đã theo dõi vết (FOLLOWED)",
  GUIDED: "Luyện tập có hướng dẫn (GUIDED)",
  INDEPENDENT: "Tự chủ độc lập (INDEPENDENT)",
  ROBUST: "Vững vàng bền vững (ROBUST)",
}

// Canonical trace steps for Candidate Keys stepper
const TRACE_STEPS = [
  {
    step: 0,
    title: "Bước 0 — Lập bảng phân loại L / R / N / LR",
    currentSet: "L: ∅, R: ∅, N: ∅, LR: {A, B, C, D, E}",
    action: "Lập bảng vị trí xuất hiện",
    closure: "Chưa tính",
    reasoning:
      "Tất cả 5 thuộc tính đều xuất hiện ở cả hai vế (A trong A→BC và E→A; B trong A→BC và B→D; C trong A→BC và CD→E; D trong B→D và CD→E; E trong CD→E và E→A). Vì L ∪ N = ∅, tập nguồn rỗng và ta cần duyệt tổ hợp từ LR bắt đầu từ các tập đơn bậc 1.",
    continues: "Bắt đầu thử các tập đơn bậc 1: {A}, {B}, {C}, {D}, {E}.",
  },
  {
    step: 1,
    title: "Bước 1 — Bắt đầu tính bao đóng {A}⁺",
    currentSet: "{A}",
    action: "Khởi tạo tập bao đóng X⁽⁰⁾ = {A}",
    closure: "{A}",
    reasoning: "Theo tính chất phản xạ của hệ tiên đề Armstrong, A luôn tự suy dẫn ra chính nó: A ⊆ {A}⁺.",
    continues: "Duyệt qua tập F để tìm phụ thuộc hàm có vế trái nằm trong {A}.",
  },
  {
    step: 2,
    title: "Bước 2 — Áp dụng A → BC",
    currentSet: "{A}",
    action: "Áp dụng FD: A → BC (do A ⊆ {A})",
    closure: "{A, B, C}",
    reasoning: "Vế trái A đã có trong bao đóng, do đó toàn bộ vế phải BC được bổ sung vào bao đóng.",
    continues: "Bao đóng được mở rộng thành {A, B, C}. Tiếp tục vòng lặp.",
  },
  {
    step: 3,
    title: "Bước 3 — Áp dụng B → D",
    currentSet: "{A}",
    action: "Áp dụng FD: B → D (do B ⊆ {A, B, C})",
    closure: "{A, B, C, D}",
    reasoning: "Thuộc tính B đã xuất hiện trong bao đóng từ bước trước, nên ta kích hoạt được B → D để lấy thêm D.",
    continues: "Bao đóng mở rộng thành {A, B, C, D}. Kiểm tra các FD còn lại.",
  },
  {
    step: 4,
    title: "Bước 4 — Áp dụng CD → E",
    currentSet: "{A}",
    action: "Áp dụng FD: CD → E (do {C, D} ⊆ {A, B, C, D})",
    closure: "{A, B, C, D, E} = U",
    reasoning: "Cả C và D đều đã có mặt, kích hoạt CD → E. Lúc này bao đóng chứa đủ toàn bộ 5 thuộc tính của quan hệ.",
    continues: "Bao đóng đã phủ toàn bộ quan hệ U. Đạt điều kiện SIÊU KHÓA (K⁺ = U).",
  },
  {
    step: 5,
    title: "Bước 5 — Kiểm tra tính tối thiểu của {A}",
    currentSet: "{A}",
    action: "Kiểm tra mọi tập con thực sự của {A}",
    closure: "{A}⁺ = U",
    reasoning:
      "Tập {A} có đúng một phần tử. Tập con thực sự duy nhất là tập rỗng ∅. Vì ∅⁺ = ∅ ≠ U, không tồn tại tập con nào phủ được U. Do đó {A} là siêu khóa tối thiểu.",
    continues: "Ghi nhận: {A} là KHÓA ỨNG VIÊN ĐẦU TIÊN! Chuyển sang xét các tập đơn còn lại.",
  },
  {
    step: 6,
    title: "Bước 6 — Thử tập đơn {B}",
    currentSet: "{B}",
    action: "Tính {B}⁺ theo F",
    closure: "{B, D} ≠ U",
    reasoning:
      "Từ B chỉ áp dụng được B → D. Không còn FD nào khác áp dụng được vì CD cần cả C, A→BC cần A, E→A cần E. Bao đóng dừng tại {B, D}.",
    continues: "{B} không phải là siêu khóa. Loại bỏ {B} khỏi danh sách khóa đơn.",
  },
  {
    step: 7,
    title: "Bước 7 — Thử tập đơn {E}",
    currentSet: "{E}",
    action: "Tính {E}⁺: E → A → BC → D",
    closure: "{E, A, B, C, D} = U",
    reasoning:
      "E sinh ra A (qua E→A), A sinh ra BC (qua A→BC), B sinh ra D (qua B→D). Bao đóng bằng U và không có tập con thực sự nào khác ∅.",
    continues: "Ghi nhận: {E} là KHÓA ỨNG VIÊN THỨ HAI! Đã duyệt xong 5 tập đơn.",
  },
  {
    step: 8,
    title: "Bước 8 — Rẽ nhánh bậc 2: Thử {BC}",
    currentSet: "{B, C}",
    action: "Tính {BC}⁺: B→D, CD→E, E→A",
    closure: "{B, C, D, E, A} = U",
    reasoning:
      "Bổ sung D (qua B→D) thành BCD; CD→E thành BCDE; E→A thành ABCDE = U. Kiểm tra tập con: {B}⁺ = BD ≠ U, {C}⁺ = C ≠ U. Cả hai tập con đều không phủ U.",
    continues: "Ghi nhận: {BC} là KHÓA ỨNG VIÊN THỨ BA!",
  },
  {
    step: 9,
    title: "Bước 9 — Rẽ nhánh bậc 2: Thử {CD}",
    currentSet: "{C, D}",
    action: "Tính {CD}⁺: CD→E, E→A, A→BC, B→D",
    closure: "{C, D, E, A, B} = U",
    reasoning:
      "CD sinh E, E sinh A, A sinh BC. Bao đóng bằng U. Kiểm tra tập con: {C}⁺ = C ≠ U, {D}⁺ = D ≠ U. Cả hai tập con đều không phủ U.",
    continues: "Ghi nhận: {CD} là KHÓA ỨNG VIÊN THỨ TƯ!",
  },
  {
    step: 10,
    title: "Bước 10 — Quy tắc cắt tỉa & Kết luận toàn bộ khóa",
    currentSet: "Tất cả các nhánh bậc 3+",
    action: "Áp dụng quy tắc cắt tỉa (Branch Pruning)",
    closure: "Hoàn tất tìm kiếm",
    reasoning:
      "Mọi tổ hợp bậc cao hơn chứa A, E, BC, hoặc CD đều là siêu khóa dư thừa (không tối thiểu) nên bị cắt tỉa. Các tổ hợp còn lại không thể sinh ra U.",
    continues: "KẾT LUẬN TOÀN BỘ 4 KHÓA ỨNG VIÊN: {A}, {E}, {BC}, {CD}.",
  },
]

// Cold problem context
const COLD_CONTEXT: ProblemContext = {
  schema: ["A", "B", "C", "D", "E"],
  fds: [
    { lhs: ["A"], rhs: ["B"] },
    { lhs: ["B", "C"], rhs: ["D"] },
    { lhs: ["D"], rhs: ["E"] },
    { lhs: ["E"], rhs: ["C"] },
  ],
  expectedKeys: ["AC", "AD", "AE"],
  mandatorySeed: ["A"],
  lrAttributes: ["B", "C", "D", "E"],
}

// Transfer problem context
const TRANSFER_CONTEXT: ProblemContext = {
  schema: ["A", "B", "C", "D", "X"],
  fds: [
    { lhs: ["A", "B"], rhs: ["C"] },
    { lhs: ["C"], rhs: ["D"] },
    { lhs: ["D"], rhs: ["A"] },
  ],
  expectedKeys: ["ABX", "BCX", "BDX"],
  mandatorySeed: ["B", "X"],
  lrAttributes: ["A", "C", "D"],
}

let currentStepIdx = 0
let currentColdHintDepth = 0
let currentTransferHintDepth = 0

function updateMasteryBadge(mastery: MasteryState) {
  const badge = document.querySelector(".mastery-status-badge")
  if (badge) {
    badge.textContent = MASTERY_LABELS[mastery] || mastery
    badge.setAttribute("data-mastery", mastery)
  }
}

function initLearningUnit() {
  const shell = document.querySelector(".learning-shell")
  if (!shell) return

  let store = loadLearnerStore()
  let progress = getSkillProgress(store, SKILL_ID)
  updateMasteryBadge(progress.mastery)

  // Reset progress button
  const resetBtn = document.querySelector(".btn-reset-mastery")
  if (resetBtn) {
    resetBtn.addEventListener("click", () => {
      if (confirm("Bạn có chắc chắn muốn đặt lại toàn bộ tiến độ học kỹ năng Khóa ứng viên?")) {
        store = resetSkillProgress(store, SKILL_ID)
        progress = getSkillProgress(store, SKILL_ID)
        updateMasteryBadge(progress.mastery)
        location.reload()
      }
    })
  }

  // 1. Orientation Check
  const orientationForm = document.querySelector("#form-orientation-check")
  if (orientationForm) {
    orientationForm.addEventListener("submit", (e) => {
      e.preventDefault()
      const selected = orientationForm.querySelector('input[name="orientation-q1"]:checked') as HTMLInputElement
      const feedback = document.querySelector("#feedback-orientation")
      if (!feedback) return

      if (selected && selected.value === "minimal") {
        feedback.innerHTML = `
          <div class="callout-alert callout-success">
            <strong>Chính xác!</strong> Khóa ứng viên bắt buộc phải là <em>siêu khóa tối thiểu</em> — nghĩa là không có bất kỳ tập con thực sự nào vẫn là siêu khóa.
          </div>
        `
        const res = recordOrientationComplete(store, SKILL_ID)
        store = res.updatedStore
        updateMasteryBadge(res.newMastery)
      } else {
        feedback.innerHTML = `
          <div class="callout-alert callout-warn">
            <strong>Chưa chính xác:</strong> Siêu khóa chỉ cần điều kiện ĐỦ (K⁺ = U). Để trở thành Khóa ứng viên, siêu khóa đó phải TỐI THIỂU (không dư thừa bất kỳ thuộc tính nào).
          </div>
        `
      }
    })
  }

  // 2. TraceStepper
  const stepperContainer = document.querySelector(".trace-stepper-container")
  if (stepperContainer) {
    const prevBtn = stepperContainer.querySelector(".stepper-btn-prev") as HTMLButtonElement
    const nextBtn = stepperContainer.querySelector(".stepper-btn-next") as HTMLButtonElement
    const stepCounter = stepperContainer.querySelector(".stepper-step-counter")
    const stepTitle = stepperContainer.querySelector(".stepper-step-title")
    const currentSetEl = stepperContainer.querySelector(".stepper-current-set")
    const actionEl = stepperContainer.querySelector(".stepper-action")
    const closureEl = stepperContainer.querySelector(".stepper-closure")
    const reasoningEl = stepperContainer.querySelector(".stepper-reasoning")
    const continuesEl = stepperContainer.querySelector(".stepper-continues")

    function renderTraceStep(idx: number) {
      const data = TRACE_STEPS[idx]
      if (!data) return
      currentStepIdx = idx

      if (stepCounter) stepCounter.textContent = `Bước ${idx} / ${TRACE_STEPS.length - 1}`
      if (stepTitle) stepTitle.textContent = data.title
      if (currentSetEl) currentSetEl.textContent = data.currentSet
      if (actionEl) actionEl.textContent = data.action
      if (closureEl) closureEl.textContent = data.closure
      if (reasoningEl) reasoningEl.textContent = data.reasoning
      if (continuesEl) continuesEl.textContent = data.continues

      if (prevBtn) prevBtn.disabled = idx === 0
      if (nextBtn) {
        if (idx === TRACE_STEPS.length - 1) {
          nextBtn.textContent = "Hoàn tất vết ✓"
        } else {
          nextBtn.textContent = "Bước tiếp →"
        }
      }

      if (idx === TRACE_STEPS.length - 1) {
        const res = recordTraceComplete(store, SKILL_ID)
        store = res.updatedStore
        updateMasteryBadge(res.newMastery)
      }
    }

    if (prevBtn) {
      prevBtn.addEventListener("click", () => {
        if (currentStepIdx > 0) renderTraceStep(currentStepIdx - 1)
      })
    }

    if (nextBtn) {
      nextBtn.addEventListener("click", () => {
        if (currentStepIdx < TRACE_STEPS.length - 1) {
          renderTraceStep(currentStepIdx + 1)
        }
      })
    }

    // Keyboard navigation within stepper
    stepperContainer.addEventListener("keydown", (e: Event) => {
      const ke = e as KeyboardEvent
      if (ke.key === "ArrowRight" && currentStepIdx < TRACE_STEPS.length - 1) {
        renderTraceStep(currentStepIdx + 1)
      } else if (ke.key === "ArrowLeft" && currentStepIdx > 0) {
        renderTraceStep(currentStepIdx - 1)
      }
    })

    renderTraceStep(0)
  }

  // 3. Self-Explanation Prompts
  const selfCheck1 = document.querySelector("#btn-check-self-1")
  if (selfCheck1) {
    selfCheck1.addEventListener("click", () => {
      const answerEl = document.querySelector("#answer-self-1")
      if (answerEl) (answerEl as HTMLElement).style.display = "block"
    })
  }

  const selfCheck2 = document.querySelector("#btn-check-self-2")
  if (selfCheck2) {
    selfCheck2.addEventListener("click", () => {
      const answerEl = document.querySelector("#answer-self-2")
      if (answerEl) (answerEl as HTMLElement).style.display = "block"
    })
  }

  // 4. Faded Example Form
  const fadedForm = document.querySelector("#form-faded-example")
  if (fadedForm) {
    fadedForm.addEventListener("submit", (e) => {
      e.preventDefault()
      const blank1 = (fadedForm.querySelector("#faded-blank-1") as HTMLInputElement)?.value.trim().toUpperCase()
      const blank2 = (fadedForm.querySelector("#faded-blank-2") as HTMLInputElement)?.value.trim().toUpperCase()
      const blank3 = (fadedForm.querySelector('input[name="faded-q3"]:checked') as HTMLInputElement)?.value
      const feedback = document.querySelector("#feedback-faded")
      if (!feedback) return

      const isB1Correct = blank1 === "A" || blank1 === "{A}"
      const isB2Correct = blank2.replace(/[\s,]/g, "") === "ABCD"
      const isB3Correct = blank3 === "yes"

      if (isB1Correct && isB2Correct && isB3Correct) {
        feedback.innerHTML = `
          <div class="callout-alert callout-success">
            <strong>Rất tốt!</strong> Bạn đã điền chính xác:
            <ul>
              <li>Tập nguồn bắt buộc: <strong>S = {A}</strong> (do A ∈ L).</li>
              <li>Bao đóng: <strong>{A}⁺ = ABCD = U</strong> (qua A→B, B→C, C→D).</li>
              <li>{A} tối thiểu vì không có tập con thực sự khác rỗng nào phủ được U. Khóa duy nhất là <strong>{A}</strong>.</li>
            </ul>
          </div>
        `
        const res = recordFadedComplete(store, SKILL_ID)
        store = res.updatedStore
        updateMasteryBadge(res.newMastery)
      } else {
        feedback.innerHTML = `
          <div class="callout-alert callout-warn">
            <strong>Hãy kiểm tra lại:</strong>
            <ul>
              <li>${isB1Correct ? "✓" : "✗"} Thuộc tính nhóm L chỉ xuất hiện ở vế trái là A.</li>
              <li>${isB2Correct ? "✓" : "✗"} Bao đóng {A}⁺ lần lượt mở rộng qua A→B→C→D để thành ABCD.</li>
              <li>${isB3Correct ? "✓" : "✗"} {A} là tập 1 phần tử nên hiển nhiên tối thiểu.</li>
            </ul>
          </div>
        `
      }
    })
  }

  // 5. Hint Drawer for Cold Problem
  const btnColdHint = document.querySelector("#btn-cold-hint")
  if (btnColdHint) {
    btnColdHint.addEventListener("click", () => {
      currentColdHintDepth++
      const hintContainer = document.querySelector("#cold-hint-container")
      const hintNotice = document.querySelector("#cold-hint-notice")
      if (!hintContainer) return

      const hints = [
        "<strong>Gợi ý 1 (Mục tiêu):</strong> Bạn cần tìm tập thuộc tính nhỏ nhất mà bao đóng phủ kín R(A,B,C,D,E).",
        "<strong>Gợi ý 2 (Quy tắc):</strong> Phân loại thuộc tính: A chỉ xuất hiện bên trái (L). B, C, D, E đều xuất hiện cả 2 bên (LR). Do đó mọi khóa đều PHẢI chứa A.",
        "<strong>Gợi ý 3 (Trạng thái trung gian):</strong> Tính {A}⁺ = {A, B} ≠ U. Hãy thử kết hợp A với từng thuộc tính trong LR: {AC}, {AD}, {AE}. <em>(Chú ý: Đã dùng gợi ý sâu, lượt làm này sẽ được tính là có hướng dẫn).</em>",
        "<strong>Gợi ý 4 (Lời giải mẫu):</strong> {AC}⁺ = ABCDE = U; {AD}⁺ = ABCDE = U; {AE}⁺ = ABCDE = U. Kiểm tra tính tối thiểu: không có tập con 1 phần tử nào phủ U. Vậy có 3 khóa là AC, AD, AE.",
      ]

      const renderedHints = hints.slice(0, currentColdHintDepth).map((h) => `<div class="hint-tier">${h}</div>`).join("")
      hintContainer.innerHTML = renderedHints

      if (currentColdHintDepth >= 3 && hintNotice) {
        (hintNotice as HTMLElement).style.display = "block"
      }
      if (currentColdHintDepth >= 4) {
        btnColdHint.setAttribute("disabled", "true")
      }
    })
  }

  // 6. Cold Problem Submission
  const coldForm = document.querySelector("#form-cold-problem")
  if (coldForm) {
    coldForm.addEventListener("submit", (e) => {
      e.preventDefault()
      const input = (coldForm.querySelector("#cold-answer-input") as HTMLInputElement)?.value
      const feedback = document.querySelector("#feedback-cold")
      if (!feedback) return

      const comparison = compareCandidateKeys(input, COLD_CONTEXT.expectedKeys)

      if (comparison.matches) {
        const isIndependent = currentColdHintDepth <= 2
        const res = recordProblemAttempt(
          store,
          SKILL_ID,
          {
            skillId: SKILL_ID,
            problemId: "ck-cold-001",
            correct: true,
            hintDepthUsed: currentColdHintDepth,
            independent: isIndependent,
          },
          false,
        )
        store = res.updatedStore
        updateMasteryBadge(res.newMastery)

        feedback.innerHTML = `
          <div class="callout-alert callout-success">
            <h4>✓ Hoàn toàn chính xác!</h4>
            <p>Đáp án chuẩn: <strong>{AC, AD, AE}</strong>.</p>
            <p>${
              isIndependent
                ? "<strong>Tuyệt vời!</strong> Bạn đã tự giải đúng bài tập độc lập mà không dùng gợi ý sâu. Mastery của bạn đã đạt <strong>INDEPENDENT</strong>!"
                : "Bạn đã làm đúng! Tuy nhiên vì đã dùng gợi ý sâu (tầng 3 trở lên), kết quả này được ghi nhận là <strong>GUIDED</strong>. Hãy thử sức với bài chuyển giao bên dưới để đạt INDEPENDENT."
            }</p>
          </div>
        `
      } else {
        const diag = diagnoseCandidateKeySubmission(input, COLD_CONTEXT)
        recordProblemAttempt(store, SKILL_ID, {
          skillId: SKILL_ID,
          problemId: "ck-cold-001",
          correct: false,
          hintDepthUsed: currentColdHintDepth,
          errorClass: diag?.id,
          independent: false,
        })

        feedback.innerHTML = `
          <div class="callout-alert callout-danger">
            <h4>Chưa chính xác</h4>
            ${
              diag
                ? `
              <div class="diagnosis-card">
                <div class="diagnosis-badge">Chẩn đoán: <code>${diag.id}</code></div>
                <p><strong>Triệu chứng:</strong> ${diag.symptom}</p>
                <p><strong>Bản chất lỗi:</strong> ${diag.explanation}</p>
                <p class="diagnosis-repair"><strong>Hướng sửa chữa:</strong> ${diag.repair}</p>
              </div>
            `
                : "<p>Hãy kiểm tra lại danh sách các khóa và đảm bảo đã tìm hết các nhánh rẽ.</p>"
            }
          </div>
        `
      }
    })
  }

  // 7. Transfer Problem Submission
  const transferForm = document.querySelector("#form-transfer-problem")
  if (transferForm) {
    transferForm.addEventListener("submit", (e) => {
      e.preventDefault()
      const input = (transferForm.querySelector("#transfer-answer-input") as HTMLInputElement)?.value
      const feedback = document.querySelector("#feedback-transfer")
      if (!feedback) return

      const comparison = compareCandidateKeys(input, TRANSFER_CONTEXT.expectedKeys)

      if (comparison.matches) {
        feedback.innerHTML = `
          <div class="callout-alert callout-success">
            <h4>✓ Xuất sắc!</h4>
            <p>Đáp án chuẩn: <strong>{ABX, BCX, BDX}</strong>.</p>
            <p>Bạn đã nhận diện chính xác: X là thuộc tính thuộc nhóm N (không xuất hiện ở bất kỳ FD nào) và B chỉ xuất hiện ở vế trái (nhóm L). Do đó mọi khóa ứng viên bắt buộc phải chứa {B, X}!</p>
          </div>
        `
      } else {
        const diag = diagnoseCandidateKeySubmission(input, TRANSFER_CONTEXT)
        feedback.innerHTML = `
          <div class="callout-alert callout-danger">
            <h4>Chưa chính xác</h4>
            ${
              diag
                ? `
              <div class="diagnosis-card">
                <div class="diagnosis-badge">Chẩn đoán: <code>${diag.id}</code></div>
                <p><strong>Triệu chứng:</strong> ${diag.symptom}</p>
                <p><strong>Bản chất lỗi:</strong> ${diag.explanation}</p>
                <p class="diagnosis-repair"><strong>Hướng sửa chữa:</strong> ${diag.repair}</p>
              </div>
            `
                : "<p>Lưu ý: Quan sát kỹ thuộc tính X có xuất hiện trong bất kỳ phụ thuộc hàm nào không!</p>"
            }
          </div>
        `
      }
    })
  }

  // 8. Exam Trap Activity
  const trapForm = document.querySelector("#form-trap-activity")
  if (trapForm) {
    trapForm.addEventListener("submit", (e) => {
      e.preventDefault()
      const selected = trapForm.querySelector('input[name="trap-choice"]:checked') as HTMLInputElement
      const feedback = document.querySelector("#feedback-trap")
      if (!feedback) return

      if (selected && selected.value === "minimality") {
        feedback.innerHTML = `
          <div class="callout-alert callout-success">
            <strong>Chính xác!</strong> Sinh viên này đã mắc lỗi kinh điển trong bài thi UIT:
            <ol>
              <li><strong>Vi phạm tính tối thiểu:</strong> {A} đứng một mình đã có {A}⁺ = ABCD = U, do đó {A, B} là siêu khóa nhưng không tối thiểu!</li>
              <li><strong>Dừng quá sớm:</strong> Khóa thực sự chỉ là {A}.</li>
            </ol>
          </div>
        `
      } else {
        feedback.innerHTML = `
          <div class="callout-alert callout-warn">
            <strong>Chưa chuẩn xác:</strong> Hãy chú ý: {A}⁺ bằng bao nhiêu? {A}⁺ đã bằng ABCD rồi, vậy thêm B vào có còn là <em>khóa tối thiểu</em> không?
          </div>
        `
      }
    })
  }

  // 9. Closed-Book Recall
  const btnRecallReveal = document.querySelector("#btn-reveal-recall")
  if (btnRecallReveal) {
    btnRecallReveal.addEventListener("click", () => {
      const answers = document.querySelectorAll(".recall-model-answer")
      answers.forEach((el) => {
        ;(el as HTMLElement).style.display = "block"
      })
      btnRecallReveal.setAttribute("disabled", "true")
      btnRecallReveal.textContent = "Đã đối chiếu đáp án ✓"
    })
  }
}

// Initialize on DOM ready or nav event
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initLearningUnit)
} else {
  initLearningUnit()
}
document.addEventListener("nav", initLearningUnit)
