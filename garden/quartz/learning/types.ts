/**
 * Core type definitions for CSDL_UIT Active Learning System (v1.2)
 */

export type MasteryState =
  | "UNSEEN"
  | "ORIENTED"
  | "FOLLOWED"
  | "GUIDED"
  | "INDEPENDENT"
  | "ROBUST"

export type ErrorClassId =
  | "minimality-not-checked"
  | "closure-stopped-too-early"
  | "missing-mandatory-attribute"
  | "only-one-key-found"
  | "redundant-branch-search"
  | "incorrect-FD-application"

export interface ProblemAttempt {
  skillId: string
  problemId: string
  timestamp: string
  correct: boolean
  hintDepthUsed: number
  errorClass?: ErrorClassId
  independent: boolean
}

export interface SkillProgress {
  mastery: MasteryState
  lastAttemptAt?: string
  orientationCompleted: boolean
  traceCompleted: boolean
  fadedCompleted: boolean
  attempts: ProblemAttempt[]
}

export interface LearnerStoreSchema {
  version: 1
  skills: Record<string, SkillProgress>
}

export interface ErrorDiagnosis {
  id: ErrorClassId
  symptom: string
  explanation: string
  repair: string
  targetBlockId?: string
}

export interface TraceStep {
  stepIndex: number
  title: string
  round?: number
  currentSet: string[]
  currentClosure: string[]
  applicableFd?: string
  newAttributes?: string[]
  reasoning: string
  whyBranchContinuesOrStops: string
}
