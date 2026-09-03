import { createHash } from "node:crypto"
import { copyFileSync, existsSync, mkdirSync, readFileSync, readdirSync, unlinkSync } from "node:fs"
import { dirname, resolve } from "node:path"
import { fileURLToPath } from "node:url"

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..")
const destination = resolve(root, "garden", "quartz", "static", "pdfs")
const handbooks = [
  {
    sourceName: "IT004_CSDL_UIT_LyThuyet_VoTrongPhuc.pdf",
    targetName: "it004_csdl_uit_lythuyet_votrongphuc.pdf",
  },
  {
    sourceName: "IT004_CSDL_UIT_ThucHanh_VoTrongPhuc.pdf",
    targetName: "it004_csdl_uit_thuchanh_votrongphuc.pdf",
  },
]

const sha256 = (file) => createHash("sha256").update(readFileSync(file)).digest("hex")
mkdirSync(destination, { recursive: true })

// Clean destination so exactly and only the chosen convention files exist
const expectedTargets = new Set(handbooks.map((h) => h.targetName))
for (const file of readdirSync(destination)) {
  if (!expectedTargets.has(file)) {
    unlinkSync(resolve(destination, file))
  }
}

for (const { sourceName, targetName } of handbooks) {
  const source = resolve(root, "dist", sourceName)
  const target = resolve(destination, targetName)
  if (!existsSync(source)) throw new Error(`Missing frozen PDF: ${source}`)
  copyFileSync(source, target)
  const sourceHash = sha256(source)
  const targetHash = sha256(target)
  if (sourceHash !== targetHash) throw new Error(`PDF hash mismatch: ${sourceName}`)
  console.log(`${targetName} ${sourceHash}`)
}
