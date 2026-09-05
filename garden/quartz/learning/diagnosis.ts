/**
 * Candidate Key Deterministic Error Diagnosis Registry
 *
 * Maps student error patterns to 6 canonical error classes with
 * Vietnamese explanations, failure reasons, and actionable repair steps.
 */

import { ErrorClassId, ErrorDiagnosis } from "./types"
import { normalizeKeySet } from "./normalizer"

export const ERROR_REGISTRY: Record<ErrorClassId, ErrorDiagnosis> = {
  "minimality-not-checked": {
    id: "minimality-not-checked",
    symptom: "Kết luận siêu khóa là khóa ứng viên mà không kiểm tra tính tối thiểu",
    explanation:
      "Bạn đã tìm được một siêu khóa (bao đóng phủ toàn bộ R), nhưng chưa kiểm tra các tập con thực sự. Tập thuộc tính này vẫn chứa thuộc tính dư thừa, vi phạm định nghĩa tối thiểu của Candidate Key.",
    repair:
      "Với mỗi siêu khóa K tìm được, hãy lần lượt loại bỏ từng thuộc tính và tính lại bao đóng của tập con. Nếu mọi tập con đều không phủ R thì K mới là khóa ứng viên.",
    targetBlockId: "block-mental-model",
  },
  "closure-stopped-too-early": {
    id: "closure-stopped-too-early",
    symptom: "Dừng tính bao đóng trước khi đạt điểm cố định (fixed point)",
    explanation:
      "Bao đóng bị kết luận quá sớm. Vẫn còn phụ thuộc hàm có vế trái thỏa mãn trong các vòng sau nhưng chưa được kích hoạt.",
    repair:
      "Duyệt lại toàn bộ tập FD từ đầu sau mỗi lần bổ sung thuộc tính mới, cho đến khi duyệt trọn 1 vòng mà không có thêm bất kỳ thuộc tính nào (điểm bất động).",
    targetBlockId: "block-mechanism",
  },
  "missing-mandatory-attribute": {
    id: "missing-mandatory-attribute",
    symptom: "Bỏ sót thuộc tính nguồn bắt buộc (nhóm L hoặc N) trong khóa",
    explanation:
      "Khóa của bạn thiếu các thuộc tính thuộc nhóm L (chỉ xuất hiện vế trái) hoặc nhóm N (không xuất hiện ở vế nào). Các thuộc tính này không thể được suy dẫn từ bất kỳ thuộc tính nào khác.",
    repair:
      "Lập bảng phân loại L, R, N, LR trước khi tìm khóa. Tập nguồn bắt buộc S = L ∪ N phải có mặt trong TẤT CẢ các khóa ứng viên.",
    targetBlockId: "block-mechanism",
  },
  "only-one-key-found": {
    id: "only-one-key-found",
    symptom: "Dừng lại sau khi chỉ tìm được 1 khóa ứng viên",
    explanation:
      "Bạn đã tìm đúng một khóa, nhưng quan hệ này có nhiều hơn 1 khóa ứng viên. Việc dừng lại quá sớm sẽ làm mất thuộc tính khóa (prime attributes) và dẫn đến xác định sai dạng chuẩn 3NF / BCNF.",
    repair:
      "Tiếp tục kiểm tra các nhánh rẽ tổ hợp khác từ các thuộc tính nhóm LR cho đến khi vét cạn toàn bộ không gian tìm kiếm hợp lệ.",
    targetBlockId: "block-exam-trap",
  },
  "redundant-branch-search": {
    id: "redundant-branch-search",
    symptom: "Tìm kiếm mở rộng trên tập cha của khóa đã tìm thấy",
    explanation:
      "Bạn đang xét tổ hợp chứa một khóa ứng viên đã được chứng minh. Mọi tập cha của khóa đều là siêu khóa dư thừa, không thể là khóa ứng viên.",
    repair:
      "Áp dụng quy tắc cắt tỉa nhánh: nếu K đã là candidate key, lập tức loại bỏ mọi tập có dạng K ∪ {X}.",
    targetBlockId: "block-mental-model",
  },
  "incorrect-FD-application": {
    id: "incorrect-FD-application",
    symptom: "Áp dụng phụ thuộc hàm khi vế trái chưa nằm trọn vẹn trong bao đóng",
    explanation:
      "Bạn đã kích hoạt phụ thuộc hàm X → Y nhưng trong bao đóng hiện tại chỉ có một phần thuộc tính của X, chưa đủ điều kiện tiên quyết.",
    repair:
      "Chỉ được đưa vế phải Y vào tập bao đóng khi TOÀN BỘ các thuộc tính ở vế trái X đã thuộc về bao đóng hiện tại.",
    targetBlockId: "block-mechanism",
  },
}

export interface ProblemContext {
  schema: string[]
  fds: Array<{ lhs: string[]; rhs: string[] }>
  expectedKeys: string[]
  mandatorySeed: string[]
  lrAttributes: string[]
}

/**
 * Deterministically analyzes a student's answer to classify mistakes against the 6 error IDs.
 */
export function diagnoseCandidateKeySubmission(
  userInput: string,
  context: ProblemContext,
): ErrorDiagnosis | null {
  const userNorm = normalizeKeySet(userInput)
  const expectedNorm = normalizeKeySet(context.expectedKeys.join(", "))

  if (userNorm.isEmpty) return null

  // 1. Missing mandatory attributes (L or N)
  for (const key of userNorm.normalizedKeys) {
    for (const mandatoryAttr of context.mandatorySeed) {
      if (!key.includes(mandatoryAttr)) {
        return ERROR_REGISTRY["missing-mandatory-attribute"]
      }
    }
  }

  // 2. Only one key found when multiple exist
  if (userNorm.normalizedKeys.length === 1 && expectedNorm.normalizedKeys.length > 1) {
    if (expectedNorm.normalizedKeys.includes(userNorm.normalizedKeys[0])) {
      return ERROR_REGISTRY["only-one-key-found"]
    }
  }

  // 3. Minimality not checked or redundant branch search (user submitted a superset of a valid key)
  for (const userKey of userNorm.normalizedKeys) {
    for (const expKey of expectedNorm.normalizedKeys) {
      if (userKey !== expKey && isSubsequence(expKey, userKey)) {
        return ERROR_REGISTRY["minimality-not-checked"]
      }
    }
  }

  // 4. If user submitted fewer keys than expected but not just 1
  if (
    userNorm.normalizedKeys.length < expectedNorm.normalizedKeys.length &&
    userNorm.normalizedKeys.every((k) => expectedNorm.normalizedKeys.includes(k))
  ) {
    return ERROR_REGISTRY["only-one-key-found"]
  }

  // 5. Default fallback if user has invalid key (closure stopped too early or incorrect FD)
  for (const userKey of userNorm.normalizedKeys) {
    if (!expectedNorm.normalizedKeys.includes(userKey)) {
      return ERROR_REGISTRY["closure-stopped-too-early"]
    }
  }

  return null
}

function isSubsequence(needle: string, haystack: string): boolean {
  for (const ch of needle) {
    if (!haystack.includes(ch)) return false
  }
  return true
}
