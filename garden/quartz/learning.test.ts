import test, { describe } from "node:test"
import assert from "node:assert/strict"

import {
  normalizeKey,
  normalizeKeySet,
  compareCandidateKeys,
} from "./learning/normalizer"
import {
  getInitialStore,
  evaluateNextMastery,
  recordProblemAttempt,
  recordOrientationComplete,
  recordTraceComplete,
  recordFadedComplete,
  resetSkillProgress,
} from "./learning/mastery"
import {
  ERROR_REGISTRY,
  diagnoseCandidateKeySubmission,
  ProblemContext,
} from "./learning/diagnosis"

describe("Candidate Keys Answer Normalization", () => {
  test("normalizes individual key attributes alphabetically", () => {
    assert.equal(normalizeKey("ca"), "AC")
    assert.equal(normalizeKey("B, A"), "AB")
    assert.equal(normalizeKey("{ D, C, B }"), "BCD")
    assert.equal(normalizeKey("E D C B A"), "ABCDE")
  })

  test("handles set order independence and case insensitivity", () => {
    const res1 = compareCandidateKeys("{AC, BD}", "{BD, AC}")
    assert.equal(res1.matches, true)
    assert.deepEqual(res1.userKeys, ["AC", "BD"])

    const res2 = compareCandidateKeys("bd, ca", "{AC, BD}")
    assert.equal(res2.matches, true)

    const res3 = compareCandidateKeys("  ac ;   bd  ", "AC, BD")
    assert.equal(res3.matches, true)
  })

  test("detects missing keys", () => {
    const res = compareCandidateKeys("AC", "{AC, BD}")
    assert.equal(res.matches, false)
    assert.deepEqual(res.missingKeys, ["BD"])
    assert.deepEqual(res.extraKeys, [])
  })

  test("detects extra non-minimal keys", () => {
    const res = compareCandidateKeys("AC, BD, ABC", "{AC, BD}")
    assert.equal(res.matches, false)
    assert.deepEqual(res.missingKeys, [])
    assert.deepEqual(res.extraKeys, ["ABC"])
  })

  test("handles empty or whitespace-only input safely", () => {
    const empty1 = normalizeKeySet("")
    assert.equal(empty1.isEmpty, true)
    assert.deepEqual(empty1.normalizedKeys, [])

    const empty2 = normalizeKeySet("   ")
    assert.equal(empty2.isEmpty, true)

    const cmp = compareCandidateKeys("", "AC, BD")
    assert.equal(cmp.matches, false)
  })
})

describe("Mastery State Machine & Rules", () => {
  test("initial state is UNSEEN and page load does not mutate mastery", () => {
    const store = getInitialStore()
    const skillProgress = store.skills["candidate-keys"]
    assert.equal(skillProgress, undefined)
  })

  test("orientation checkpoint advances UNSEEN to ORIENTED", () => {
    const store = getInitialStore()
    const { updatedStore, newMastery } = recordOrientationComplete(store, "candidate-keys")
    assert.equal(newMastery, "ORIENTED")
    assert.equal(updatedStore.skills["candidate-keys"].orientationCompleted, true)
  })

  test("trace stepper checkpoint advances ORIENTED to FOLLOWED", () => {
    let store = getInitialStore()
    store = recordOrientationComplete(store, "candidate-keys").updatedStore
    const { newMastery } = recordTraceComplete(store, "candidate-keys")
    assert.equal(newMastery, "FOLLOWED")
  })

  test("faded example advances FOLLOWED to GUIDED", () => {
    let store = getInitialStore()
    store = recordOrientationComplete(store, "candidate-keys").updatedStore
    store = recordTraceComplete(store, "candidate-keys").updatedStore
    const { newMastery } = recordFadedComplete(store, "candidate-keys")
    assert.equal(newMastery, "GUIDED")
  })

  test("cold problem clean success (hint depth <= 2) earns INDEPENDENT", () => {
    let store = getInitialStore()
    store = recordOrientationComplete(store, "candidate-keys").updatedStore
    store = recordTraceComplete(store, "candidate-keys").updatedStore
    store = recordFadedComplete(store, "candidate-keys").updatedStore

    const { newMastery } = recordProblemAttempt(store, "candidate-keys", {
      skillId: "candidate-keys",
      problemId: "ck-cold-001",
      correct: true,
      hintDepthUsed: 1,
      independent: true,
    })
    assert.equal(newMastery, "INDEPENDENT")
  })

  test("cold problem solved after deep hints (hint depth >= 3) does NOT earn INDEPENDENT", () => {
    let store = getInitialStore()
    store = recordOrientationComplete(store, "candidate-keys").updatedStore
    store = recordTraceComplete(store, "candidate-keys").updatedStore
    store = recordFadedComplete(store, "candidate-keys").updatedStore

    const { newMastery } = recordProblemAttempt(store, "candidate-keys", {
      skillId: "candidate-keys",
      problemId: "ck-cold-001",
      correct: true,
      hintDepthUsed: 3,
      independent: false,
    })
    assert.equal(newMastery, "GUIDED")
  })

  test("ROBUST is not granted in the same session without delayed spaced review", () => {
    const next = evaluateNextMastery("INDEPENDENT", {
      type: "COLD_ATTEMPT",
      correct: true,
      hintDepthUsed: 0,
      isDelayedReview: false,
    })
    assert.equal(next, "INDEPENDENT")

    const robustNext = evaluateNextMastery("INDEPENDENT", {
      type: "SPACED_REVIEW",
      correct: true,
      isDelayedReview: true,
    })
    assert.equal(robustNext, "ROBUST")
  })

  test("resetSkillProgress cleans up state for learner reset", () => {
    let store = getInitialStore()
    store = recordOrientationComplete(store, "candidate-keys").updatedStore
    assert.ok(store.skills["candidate-keys"])
    const resetStore = resetSkillProgress(store, "candidate-keys")
    assert.equal(resetStore.skills["candidate-keys"], undefined)
  })
})

describe("Deterministic Error Diagnosis", () => {
  const context: ProblemContext = {
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

  test("diagnoses missing mandatory attribute", () => {
    const diag = diagnoseCandidateKeySubmission("{BC, CD}", context)
    assert.ok(diag)
    assert.equal(diag?.id, "missing-mandatory-attribute")
    assert.ok(diag?.explanation.includes("thiếu các thuộc tính thuộc nhóm L"))
  })

  test("diagnoses only one key found when multiple exist", () => {
    const diag = diagnoseCandidateKeySubmission("AC", context)
    assert.ok(diag)
    assert.equal(diag?.id, "only-one-key-found")
  })

  test("diagnoses minimality not checked when non-minimal superset submitted", () => {
    const diag = diagnoseCandidateKeySubmission("ABC, AD, AE", context)
    assert.ok(diag)
    assert.equal(diag?.id, "minimality-not-checked")
  })

  test("verifies all 6 error classes exist in registry", () => {
    const requiredIds = [
      "minimality-not-checked",
      "closure-stopped-too-early",
      "missing-mandatory-attribute",
      "only-one-key-found",
      "redundant-branch-search",
      "incorrect-FD-application",
    ]
    for (const id of requiredIds) {
      assert.ok(ERROR_REGISTRY[id as keyof typeof ERROR_REGISTRY])
      assert.equal(ERROR_REGISTRY[id as keyof typeof ERROR_REGISTRY].id, id)
      assert.ok(ERROR_REGISTRY[id as keyof typeof ERROR_REGISTRY].repair.length > 10)
    }
  })
})
