import remarkFrontmatter from "remark-frontmatter"
import { Root } from "mdast"
import { VFile } from "vfile"
import YAML from "yaml"
import { BuildCtx } from "../../util/ctx"
import { QuartzTransformerPlugin } from "../types"

type FrontmatterNode = {
  type: "yaml"
  value: string
}

function parseFrontmatter(tree: Root, file: VFile) {
  const firstNode = tree.children[0]
  if (!firstNode || firstNode.type !== "yaml") return

  const metadata = YAML.parse((firstNode as FrontmatterNode).value)
  if (metadata !== null && (typeof metadata !== "object" || Array.isArray(metadata))) {
    throw new Error("YAML frontmatter must contain a mapping")
  }

  file.data.frontmatter = metadata ?? {}
  tree.children.shift()
}

export const FrontMatter: QuartzTransformerPlugin = () => ({
  name: "FrontMatter",
  markdownPlugins(_ctx: BuildCtx) {
    return [remarkFrontmatter, () => parseFrontmatter]
  },
})
