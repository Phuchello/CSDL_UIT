"""Post-build render smoke checks for the Quartz Knowledge Garden."""
from __future__ import annotations

import re
import sys
from pathlib import Path

from lxml import html

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "garden" / "public"

MATH_PAGES = {
    "exercises/normalization-exercise.html": 8,
    "theory/closure.html": 12,
}

RAW_TEX = re.compile(
    r"\\(?:rightarrow|leftarrow|implies|emptyset|subseteq|supseteq|cup|cap|models|neq|notin)\b"
)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    errors: list[str] = []

    for relative, minimum_katex_nodes in MATH_PAGES.items():
        path = PUBLIC / relative
        if not path.is_file():
            errors.append(f"missing built render target: {relative}")
            continue

        try:
            doc = html.fromstring(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            errors.append(f"unable to parse {relative}: {exc}")
            continue

        katex_nodes = doc.xpath(
            '//*[contains(concat(" ", normalize-space(@class), " "), " katex ")]'
        )
        if len(katex_nodes) < minimum_katex_nodes:
            errors.append(
                f"{relative}: expected at least {minimum_katex_nodes} KaTeX nodes, "
                f"found {len(katex_nodes)}"
            )

        visible_article_text = doc.xpath(
            "//article//text()["
            "not(ancestor::code) and not(ancestor::pre) and "
            "not(ancestor::script) and not(ancestor::style) and "
            "not(ancestor::math) and not(ancestor::annotation)"
            "]"
        )
        raw_hits = sorted(
            {
                match.group(0)
                for text_node in visible_article_text
                for match in RAW_TEX.finditer(str(text_node))
            }
        )
        if raw_hits:
            errors.append(
                f"{relative}: raw TeX control sequences remain visible in article: "
                + ", ".join(raw_hits)
            )

    if errors:
        print("Garden render smoke validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Garden render smoke validation PASS")
    for relative in MATH_PAGES:
        print(f"- {relative}: KaTeX rendered; no raw TeX controls in article")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
