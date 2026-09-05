/**
 * Deterministic Mastery State Machine & LocalStorage Store
 *
 * Implements versioned client-side storage, anti-inflation rules,
 * hint disqualification from INDEPENDENT, and safe fallback.
 */

import { LearnerStoreSchema, MasteryState, ProblemAttempt, SkillProgress } from "./types"

export const STORAGE_KEY = "csdl_uit_learning_state_v1"
export const CURRENT_SCHEMA_VERSION = 1

// In-memory fallback if localStorage is disabled or unavailable
let memoryStore: LearnerStoreSchema | null = null

export function getInitialSkillProgress(): SkillProgress {
  return {
    mastery: "UNSEEN",
    orientationCompleted: false,
    traceCompleted: false,
    fadedCompleted: false,
    attempts: [],
  }
}

export function getInitialStore(): LearnerStoreSchema {
  return {
    version: CURRENT_SCHEMA_VERSION,
    skills: {},
  }
}

/**
 * Checks if localStorage is available and functional.
 */
function isLocalStorageAvailable(): boolean {
  try {
    if (typeof window === "undefined" || !window.localStorage) return false
    const testKey = "__storage_test__"
    window.localStorage.setItem(testKey, testKey)
    window.localStorage.removeItem(testKey)
    return true
  } catch {
    return false
  }
}

/**
 * Loads the learner state. Safely falls back to in-memory store on error or corruption.
 */
export function loadLearnerStore(): LearnerStoreSchema {
  if (!isLocalStorageAvailable()) {
    if (!memoryStore) memoryStore = getInitialStore()
    return memoryStore
  }

  try {
    const raw = window.localStorage.getItem(STORAGE_KEY)
    if (!raw) return getInitialStore()
    const parsed = JSON.parse(raw)
    if (!parsed || parsed.version !== CURRENT_SCHEMA_VERSION || typeof parsed.skills !== "object") {
      // Corrupt or outdated format — return default without throwing
      return getInitialStore()
    }
    return parsed as LearnerStoreSchema
  } catch {
    return getInitialStore()
  }
}

/**
 * Saves the learner state. Fails silently on storage quota or security errors.
 */
export function saveLearnerStore(store: LearnerStoreSchema): void {
  if (!isLocalStorageAvailable()) {
    memoryStore = store
    return
  }

  try {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(store))
  } catch {
    // Quota exceeded or private browsing restriction — keep in memory
    memoryStore = store
  }
}

/**
 * Retrieves the progress record for a specific skill without modifying state.
 */
export function getSkillProgress(store: LearnerStoreSchema, skillId: string): SkillProgress {
  return store.skills[skillId] ?? getInitialSkillProgress()
}

/**
 * Transition rules for the mastery state machine.
 */
export function evaluateNextMastery(
  current: MasteryState,
  action: {
    type: "ORIENTATION_CHECK" | "TRACE_CHECK" | "FADED_SUCCESS" | "COLD_ATTEMPT" | "SPACED_REVIEW"
    correct?: boolean
    hintDepthUsed?: number
    isDelayedReview?: boolean
  },
): MasteryState {
  switch (action.type) {
    case "ORIENTATION_CHECK":
      if (current === "UNSEEN") return "ORIENTED"
      return current

    case "TRACE_CHECK":
      if (current === "ORIENTED") return "FOLLOWED"
      return current

    case "FADED_SUCCESS":
      if (current === "FOLLOWED" || current === "ORIENTED") return "GUIDED"
      return current

    case "COLD_ATTEMPT": {
      if (!action.correct) return current
      // Deep hint usage (Hint 3 or Hint 4) disqualifies attempt from INDEPENDENT
      const usedDeepHint = (action.hintDepthUsed ?? 0) >= 3
      if (usedDeepHint) {
        // Successful with scaffolding -> at least GUIDED
        if (current === "UNSEEN" || current === "ORIENTED" || current === "FOLLOWED") {
          return "GUIDED"
        }
        return current
      }
      // Clean success without deep hints achieves INDEPENDENT
      return "INDEPENDENT"
    }

    case "SPACED_REVIEW":
      // ROBUST requires prior INDEPENDENT mastery AND delayed/spaced evidence
      if (current === "INDEPENDENT" && action.correct && action.isDelayedReview) {
        return "ROBUST"
      }
      return current

    default:
      return current
  }
}

/**
 * Records a problem attempt and updates mastery deterministically.
 */
export function recordProblemAttempt(
  store: LearnerStoreSchema,
  skillId: string,
  attempt: Omit<ProblemAttempt, "timestamp">,
  isDelayedReview = false,
): { updatedStore: LearnerStoreSchema; newMastery: MasteryState } {
  const currentSkill = getSkillProgress(store, skillId)
  const fullAttempt: ProblemAttempt = {
    ...attempt,
    timestamp: new Date().toISOString(),
  }

  const nextMastery = evaluateNextMastery(currentSkill.mastery, {
    type: "COLD_ATTEMPT",
    correct: attempt.correct,
    hintDepthUsed: attempt.hintDepthUsed,
    isDelayedReview,
  })

  const updatedSkill: SkillProgress = {
    ...currentSkill,
    mastery: nextMastery,
    lastAttemptAt: fullAttempt.timestamp,
    attempts: [...currentSkill.attempts, fullAttempt],
  }

  const updatedStore: LearnerStoreSchema = {
    ...store,
    skills: {
      ...store.skills,
      [skillId]: updatedSkill,
    },
  }

  saveLearnerStore(updatedStore)
  return { updatedStore, newMastery: nextMastery }
}

/**
 * Records completion of orientation check.
 */
export function recordOrientationComplete(
  store: LearnerStoreSchema,
  skillId: string,
): { updatedStore: LearnerStoreSchema; newMastery: MasteryState } {
  const currentSkill = getSkillProgress(store, skillId)
  const nextMastery = evaluateNextMastery(currentSkill.mastery, { type: "ORIENTATION_CHECK" })

  const updatedSkill: SkillProgress = {
    ...currentSkill,
    orientationCompleted: true,
    mastery: nextMastery,
  }

  const updatedStore: LearnerStoreSchema = {
    ...store,
    skills: {
      ...store.skills,
      [skillId]: updatedSkill,
    },
  }

  saveLearnerStore(updatedStore)
  return { updatedStore, newMastery: nextMastery }
}

/**
 * Records completion of trace stepper.
 */
export function recordTraceComplete(
  store: LearnerStoreSchema,
  skillId: string,
): { updatedStore: LearnerStoreSchema; newMastery: MasteryState } {
  const currentSkill = getSkillProgress(store, skillId)
  const nextMastery = evaluateNextMastery(currentSkill.mastery, { type: "TRACE_CHECK" })

  const updatedSkill: SkillProgress = {
    ...currentSkill,
    traceCompleted: true,
    mastery: nextMastery,
  }

  const updatedStore: LearnerStoreSchema = {
    ...store,
    skills: {
      ...store.skills,
      [skillId]: updatedSkill,
    },
  }

  saveLearnerStore(updatedStore)
  return { updatedStore, newMastery: nextMastery }
}

/**
 * Records completion of faded practice.
 */
export function recordFadedComplete(
  store: LearnerStoreSchema,
  skillId: string,
): { updatedStore: LearnerStoreSchema; newMastery: MasteryState } {
  const currentSkill = getSkillProgress(store, skillId)
  const nextMastery = evaluateNextMastery(currentSkill.mastery, { type: "FADED_SUCCESS" })

  const updatedSkill: SkillProgress = {
    ...currentSkill,
    fadedCompleted: true,
    mastery: nextMastery,
  }

  const updatedStore: LearnerStoreSchema = {
    ...store,
    skills: {
      ...store.skills,
      [skillId]: updatedSkill,
    },
  }

  saveLearnerStore(updatedStore)
  return { updatedStore, newMastery: nextMastery }
}

/**
 * Resets a single skill's progress (for testing and learner restarts).
 */
export function resetSkillProgress(store: LearnerStoreSchema, skillId: string): LearnerStoreSchema {
  const nextSkills = { ...store.skills }
  delete nextSkills[skillId]
  const updatedStore: LearnerStoreSchema = {
    ...store,
    skills: nextSkills,
  }
  saveLearnerStore(updatedStore)
  return updatedStore
}
