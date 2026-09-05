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

REPRESENTATIVE_PAGES = {
    "theory/candidate-keys.html": "Khóa ứng viên",
    "exercises/normalization-exercise.html": None,
    "exam-patterns/rbtv-trigger.html": None,
}

RAW_FRONTMATTER = re.compile(
    r"^\s*(?:title|description|type|topics|related|provenance|courseEvidence|aliases):",
    re.MULTILINE,
)

RAW_TEX = re.compile(
    r"\\(?:rightarrow|leftarrow|implies|emptyset|subseteq|supseteq|cup|cap|models|neq|notin)\b"
)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    errors: list[str] = []

    for relative, expected_title in REPRESENTATIVE_PAGES.items():
        path = PUBLIC / relative
        if not path.is_file():
            errors.append(f"missing built frontmatter render target: {relative}")
            continue

        try:
            doc = html.fromstring(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            errors.append(f"unable to parse {relative}: {exc}")
            continue

        title = " ".join(str(value).strip() for value in doc.xpath("//title/text()"))
        if "Không có tiêu đề" in title:
            errors.append(f"{relative}: document title still uses the missing-title fallback")
        if expected_title and expected_title not in title:
            errors.append(f"{relative}: document title does not contain {expected_title!r}")

        article_text = "\n".join(
            str(value)
            for value in doc.xpath(
                "//article//text()["
                "not(ancestor::code) and not(ancestor::pre) and "
                "not(ancestor::script) and not(ancestor::style) and "
                "not(ancestor::math) and not(ancestor::annotation)"
                "]"
            )
        )
        leaked_fields = sorted(set(RAW_FRONTMATTER.findall(article_text)))
        if leaked_fields:
            errors.append(
                f"{relative}: raw YAML frontmatter fields remain in article: "
                + ", ".join(leaked_fields)
            )

        breadcrumb_text = " ".join(
            str(value).strip()
            for value in doc.xpath(
                '//nav[contains(concat(" ", normalize-space(@class), " "), " breadcrumb-container ")]//text()'
            )
        )
        if "Trang chủ" not in breadcrumb_text:
            errors.append(f"{relative}: breadcrumb root is not Trang chủ")

        # Breadcrumb deduplication gate: current page title must not appear in breadcrumbs
        article_h1 = " ".join(
            str(value).strip()
            for value in doc.xpath("//h1[contains(@class, 'article-title')]//text()")
        )
        if article_h1 and article_h1 in breadcrumb_text:
            errors.append(
                f"{relative}: breadcrumbs duplicate current page title ({article_h1!r})"
            )

    # 1. Prescript light-mode default gate
    prescripts = list(PUBLIC.glob("prescript*.js"))
    if not prescripts:
        errors.append("missing prescript.js in garden/public")
    else:
        prescript_text = prescripts[0].read_text(encoding="utf-8")
        if 'localStorage.getItem("theme")' not in prescript_text:
            errors.append("prescript.js does not check localStorage theme")
        if 'setAttribute("saved-theme"' not in prescript_text:
            errors.append("prescript.js does not set saved-theme attribute")
        if "(prefers-color-scheme: light)" in prescript_text:
            errors.append(
                "prescript.js still contains prefers-color-scheme fallback to dark on first visit"
            )

    # 2. CSS theme and typography gate
    css_files = list(PUBLIC.glob("index-*.css"))
    if not css_files:
        errors.append("missing index-*.css in garden/public")
    else:
        css_text = css_files[0].read_text(encoding="utf-8")
        if not any(
            token in css_text
            for token in ("--light: #ffffff", "--light:#ffffff", "--light: #fff", "--light:#fff")
        ):
            errors.append("emitted CSS does not define --light as true white #ffffff")
        if "Georgia" in css_text or "Times New Roman" in css_text:
            errors.append("emitted CSS contains serif overrides (Georgia / Times New Roman)")
        if "system-ui" not in css_text:
            errors.append("emitted CSS does not include system-ui typography stack")

    # 3. Wikilink math delimiter gate and academic notation preservation
    norm_page = PUBLIC / "exam-patterns" / "normalization.html"
    if norm_page.is_file():
        norm_text = norm_page.read_text(encoding="utf-8")
        if "$X^+$" in norm_text or "$X^+" in norm_text:
            errors.append("normalization.html contains literal math delimiter $X^+$ in text")

    theory_index = PUBLIC / "theory" / "index.html"
    if theory_index.is_file():
        t_text = theory_index.read_text(encoding="utf-8")
        if "$F_c$" in t_text:
            errors.append("theory/index.html contains unrendered literal $F_c$")
        try:
            doc_t = html.fromstring(t_text)
            mc_links = doc_t.xpath(
                '//a[@data-slug="theory/minimal-cover" or contains(@href, "theory/minimal-cover")]'
            )
            if not mc_links:
                errors.append("theory/index.html missing link to theory/minimal-cover")
            else:
                parent = mc_links[0].getparent()
                katex_nodes = parent.xpath(
                    './/*[contains(concat(" ", normalize-space(@class), " "), " katex ")]'
                )
                if not katex_nodes:
                    errors.append(
                        "theory/index.html missing KaTeX rendering for F_c notation adjacent to minimal-cover"
                    )
        except (OSError, ValueError) as exc:
            errors.append(f"unable to parse theory/index.html: {exc}")

    content_dir = ROOT / "garden" / "content"
    if content_dir.is_dir():
        for md_path in content_dir.rglob("*.md"):
            md_text = md_path.read_text(encoding="utf-8")
            if re.search(r"\[\[[^\]]*\$", md_text):
                rel = md_path.relative_to(ROOT)
                errors.append(f"{rel}: source markdown contains math delimiter in wikilink alias")

    # 4. Architectural mobile overflow gate (reject broad overflow-x: hidden clipping)
    custom_scss = ROOT / "garden" / "quartz" / "styles" / "custom.scss"
    if custom_scss.is_file():
        scss_text = custom_scss.read_text(encoding="utf-8")
        if re.search(r"(?:body|\.page|article)\s*\{[^}]*overflow-x:\s*hidden", scss_text):
            errors.append(
                "custom.scss still applies broad overflow-x: hidden clipping on body/.page/article"
            )
        if "min-width: 0" not in scss_text:
            errors.append("custom.scss missing min-width: 0 flex/grid child constraint")
        if not re.search(r"table\s*\{[^}]*overflow-x:\s*auto", scss_text):
            errors.append("custom.scss missing table horizontal scroll constraint")
        if not re.search(r"pre\s*\{[^}]*overflow-x:\s*auto", scss_text):
            errors.append("custom.scss missing pre horizontal scroll constraint")
        if not re.search(r"(?:\.katex-display|\.math)[^{]*\{[^}]*overflow-x:\s*auto", scss_text):
            errors.append("custom.scss missing display math horizontal scroll constraint")
        if "max-width: 100%" not in scss_text:
            errors.append("custom.scss missing max-width: 100% element constraint")

    if css_files:
        css_text = css_files[0].read_text(encoding="utf-8")
        if re.search(r"(?:^|[},;])(?:body|\.page|article)\s*\{[^}]*overflow-x:\s*hidden", css_text):
            errors.append(
                "emitted CSS applies broad overflow-x: hidden clipping on body/.page/article"
            )

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
    print("- Prescript theme default: light mode on first visit")
    print("- Typography: clean system sans; no Georgia/Times serif overrides")
    print("- Palette: #ffffff true white background")
    print("- Wikilinks: 0 math delimiters leaked in wikilink aliases")
    print("- Academic notation: F_c preserved outside wikilink alias and rendered via KaTeX")
    print("- Breadcrumbs: current page title deduplicated")
    print("- Mobile overflow: broad clipping removed; wide elements architecturally constrained")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
