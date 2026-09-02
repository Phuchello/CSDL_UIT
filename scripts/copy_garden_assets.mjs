import { createHash } from "node:crypto"
import { copyFileSync, existsSync, mkdirSync, readFileSync } from "node:fs"
import { dirname, resolve } from "node:path"
import { fileURLToPath } from "node:url"

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..")
const destination = resolve(root, "garden", "quartz", "static", "pdfs")
const pdfs = [
  "IT004_CSDL_UIT_CamNang_VoTrongPhuc.pdf",
  "IT004_CSDL_UIT_LyThuyet_VoTrongPhuc.pdf",
  "IT004_CSDL_UIT_ThucHanh_VoTrongPhuc.pdf",
]

const sha256 = (file) => createHash("sha256").update(readFileSync(file)).digest("hex")
mkdirSync(destination, { recursive: true })
for (const name of pdfs) {
  const source = resolve(root, "dist", name)
  const target = resolve(destination, name.toLowerCase())
  if (!existsSync(source)) throw new Error(`Missing frozen PDF: ${source}`)
  copyFileSync(source, target)
  const sourceHash = sha256(source)
  const targetHash = sha256(target)
  if (sourceHash !== targetHash) throw new Error(`PDF hash mismatch: ${name}`)
  console.log(`${name} ${sourceHash}`)
}
