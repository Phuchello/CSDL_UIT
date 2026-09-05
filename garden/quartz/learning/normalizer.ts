/**
 * Candidate Key Answer Normalization Engine
 *
 * Handles set-order independence, attribute-order normalization within keys,
 * case-insensitivity, and flexible input formats (e.g. "{AC, BD}", "BD, CA", "ac; bd").
 */

export interface NormalizationResult {
  rawInput: string
  normalizedKeys: string[]
  formatted: string
  isEmpty: boolean
}

export interface AnswerComparisonResult {
  matches: boolean
  userKeys: string[]
  expectedKeys: string[]
  missingKeys: string[]
  extraKeys: string[]
}

/**
 * Normalizes an individual candidate key string (e.g. "ca", "C, A", "{B, A}")
 * Returns attributes sorted uppercase without delimiters (e.g. "AC", "AB").
 */
export function normalizeKey(rawKey: string): string {
  if (!rawKey) return ""
  // Strip braces, parentheses, whitespace
  const cleaned = rawKey.replace(/[{}\[\]()]/g, "").trim().toUpperCase()
  if (!cleaned) return ""

  // Extract individual attributes (single uppercase letters or tokens)
  // Handles "A, B", "A B", or "AB"
  const tokens = cleaned.split(/[\s,;]+/).filter(Boolean)
  const attributes: string[] = []

  if (tokens.length > 1) {
    for (const token of tokens) {
      for (const ch of token) {
        if (/[A-Z0-9]/.test(ch)) attributes.push(ch)
      }
    }
  } else if (tokens.length === 1) {
    for (const ch of tokens[0]) {
      if (/[A-Z0-9]/.test(ch)) attributes.push(ch)
    }
  }

  // Deduplicate and sort attributes alphabetically
  const uniqueSorted = Array.from(new Set(attributes)).sort()
  return uniqueSorted.join("")
}

/**
 * Parses user input into a normalized list of distinct candidate keys.
 * Handles inputs like:
 * - "{AC, BD}"
 * - "AC, BD"
 * - "ac; bd"
 * - "{A, C}, {B, D}"
 * - "{CA}, {DB}"
 */
export function normalizeKeySet(rawInput: string): NormalizationResult {
  if (!rawInput || typeof rawInput !== "string") {
    return { rawInput: "", normalizedKeys: [], formatted: "{}", isEmpty: true }
  }

  const trimmed = rawInput.trim()
  if (!trimmed) {
    return { rawInput: trimmed, normalizedKeys: [], formatted: "{}", isEmpty: true }
  }

  const keys: string[] = []

  // Check if input uses explicit braces: e.g. "{AC}, {BD}" or "{A, C}, {B, D}"
  const braceMatches = trimmed.match(/\{[^{}]+\}/g)
  if (braceMatches && braceMatches.length > 0) {
    // If there's a single outer brace containing commas like "{AC, BD}"
    if (braceMatches.length === 1 && trimmed.startsWith("{") && trimmed.endsWith("}")) {
      const inner = trimmed.slice(1, -1).trim()
      // If inner has sub-braces or just comma-separated keys
      const innerParts = inner.split(/[,;]+/).map((s) => s.trim()).filter(Boolean)
      for (const part of innerParts) {
        const norm = normalizeKey(part)
        if (norm) keys.push(norm)
      }
    } else {
      // Multiple braced groups: e.g. "{AC}, {BD}"
      for (const match of braceMatches) {
        const norm = normalizeKey(match)
        if (norm) keys.push(norm)
      }
    }
  } else {
    // No braces: split by comma or semicolon: "AC, BD" or "ac; bd"
    const parts = trimmed.split(/[,;]+/).map((s) => s.trim()).filter(Boolean)
    for (const part of parts) {
      const norm = normalizeKey(part)
      if (norm) keys.push(norm)
    }
  }

  // Deduplicate keys in the set and sort them lexicographically
  const uniqueSortedKeys = Array.from(new Set(keys)).sort()

  return {
    rawInput,
    normalizedKeys: uniqueSortedKeys,
    formatted: `{${uniqueSortedKeys.join(", ")}}`,
    isEmpty: uniqueSortedKeys.length === 0,
  }
}

/**
 * Compares a user's submitted answer with expected candidate keys.
 */
export function compareCandidateKeys(
  userInput: string,
  expectedInput: string | string[],
): AnswerComparisonResult {
  const userNorm = normalizeKeySet(userInput)
  const expectedNorm = Array.isArray(expectedInput)
    ? normalizeKeySet(expectedInput.join(", "))
    : normalizeKeySet(expectedInput)

  const userKeySet = new Set(userNorm.normalizedKeys)
  const expectedKeySet = new Set(expectedNorm.normalizedKeys)

  const missingKeys = expectedNorm.normalizedKeys.filter((k) => !userKeySet.has(k))
  const extraKeys = userNorm.normalizedKeys.filter((k) => !expectedKeySet.has(k))

  const matches = missingKeys.length === 0 && extraKeys.length === 0 && !userNorm.isEmpty

  return {
    matches,
    userKeys: userNorm.normalizedKeys,
    expectedKeys: expectedNorm.normalizedKeys,
    missingKeys,
    extraKeys,
  }
}
