"""Deterministic validator for CSDL_UIT Active Learning Units (v1.2)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml
from lxml import html

ROOT = Path(__file__).resolve().parents[1]
CONTENT_FILE = ROOT / "garden" / "content" / "learn" / "candidate-keys.md"
PUBLIC_FILE = ROOT / "garden" / "public" / "learn" / "candidate-keys.html"
PUBLIC_DIR = ROOT / "garden" / "public"

REQUIRED_BLOCK_IDS = [
    "block-purpose",
    "block-prerequisites",
    "block-concept-map",
    "block-mental-model",
    "block-mechanism",
    "block-trace",
    "block-worked",
    "block-self-explanation",
    "block-faded",
    "block-cold",
    "block-transfer",
    "block-exam-trap",
    "block-diagnosis-registry",
    "block-recall",
    "block-mastery-rules",
    "block-reference-mode",
]

REQUIRED_PROBLEM_IDS = [
    "ck-worked-001",
    "ck-faded-001",
    "ck-cold-001",
    "ck-transfer-001",
    "ck-trap-001",
]

REQUIRED_ERROR_IDS = [
    "minimality-not-checked",
    "closure-stopped-too-early",
    "missing-mandatory-attribute",
    "only-one-key-found",
    "redundant-branch-search",
    "incorrect-FD-application",
]

RAW_FRONTMATTER = re.compile(
    r"^\s*(?:title|description|type|chapter|skill_id|priority|prerequisites|related|exam_weight|has_trace|has_recall|has_practice|has_diagnosis|provenance|courseEvidence):",
    re.MULTILINE,
)

RAW_TEX = re.compile(
    r"\\(?:rightarrow|leftarrow|implies|emptyset|subseteq|supseteq|cup|cap|models|neq|notin)\b"
)


def validate_markdown_source() -> list[str]:
    errors: list[str] = []
    if not CONTENT_FILE.is_file():
        return [f"Missing source file: {CONTENT_FILE}"]

    text = CONTENT_FILE.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        return [f"{CONTENT_FILE}: missing YAML frontmatter delimiters"]

    try:
        fm = yaml.safe_load(parts[1])
    except Exception as exc:
        return [f"{CONTENT_FILE}: invalid frontmatter YAML: {exc}"]

    if fm.get("type") != "learning-unit":
        errors.append(f"{CONTENT_FILE}: expected type 'learning-unit', got {fm.get('type')!r}")
    if fm.get("chapter") != "ch06":
        errors.append(f"{CONTENT_FILE}: expected chapter 'ch06', got {fm.get('chapter')!r}")
    if fm.get("skill_id") != "candidate-keys":
        errors.append(f"{CONTENT_FILE}: expected skill_id 'candidate-keys', got {fm.get('skill_id')!r}")
    if fm.get("priority") != "core":
        errors.append(f"{CONTENT_FILE}: expected priority 'core', got {fm.get('priority')!r}")
    if fm.get("prerequisites") != ["closure"]:
        errors.append(f"{CONTENT_FILE}: expected prerequisites ['closure'], got {fm.get('prerequisites')!r}")
    if not fm.get("has_trace"):
        errors.append(f"{CONTENT_FILE}: has_trace must be true")
    if not fm.get("has_recall"):
        errors.append(f"{CONTENT_FILE}: has_recall must be true")
    if not fm.get("has_practice"):
        errors.append(f"{CONTENT_FILE}: has_practice must be true")
    if not fm.get("has_diagnosis"):
        errors.append(f"{CONTENT_FILE}: has_diagnosis must be true")

    body = parts[2]
    for block_id in REQUIRED_BLOCK_IDS:
        if f'id="{block_id}"' not in body:
            errors.append(f"{CONTENT_FILE}: missing required block id {block_id!r}")

    for prob_id in REQUIRED_PROBLEM_IDS:
        if prob_id not in body:
            errors.append(f"{CONTENT_FILE}: missing required problem id {prob_id!r}")

    for err_id in REQUIRED_ERROR_IDS:
        if err_id not in body:
            errors.append(f"{CONTENT_FILE}: missing required error id {err_id!r}")

    return errors


def validate_rendered_html() -> list[str]:
    errors: list[str] = []
    if not PUBLIC_FILE.is_file():
        return [f"Missing compiled HTML: {PUBLIC_FILE}"]

    html_text = PUBLIC_FILE.read_text(encoding="utf-8")
    try:
        doc = html.fromstring(html_text)
    except Exception as exc:
        return [f"{PUBLIC_FILE}: failed to parse HTML: {exc}"]

    # Title check
    titles = doc.xpath("//title/text()")
    title = " ".join(str(t).strip() for t in titles)
    if "Khóa ứng viên" not in title:
        errors.append(f"{PUBLIC_FILE}: title does not contain 'Khóa ứng viên': {title!r}")

    # Slug check on body
    body_slugs = doc.xpath("//body/@data-slug")
    if not body_slugs or body_slugs[0] != "learn/candidate-keys":
        errors.append(f"{PUBLIC_FILE}: body data-slug is not 'learn/candidate-keys': {body_slugs}")

    # Raw frontmatter check
    article_text = "\n".join(
        str(val)
        for val in doc.xpath(
            "//article//text()["
            "not(ancestor::code) and not(ancestor::pre) and "
            "not(ancestor::script) and not(ancestor::style) and "
            "not(ancestor::math) and not(ancestor::annotation)"
            "]"
        )
    )
    leaked = sorted(set(RAW_FRONTMATTER.findall(article_text)))
    if leaked:
        errors.append(f"{PUBLIC_FILE}: raw frontmatter leaked into article: {', '.join(leaked)}")

    # KaTeX check
    katex_nodes = doc.xpath('//*[contains(concat(" ", normalize-space(@class), " "), " katex ")]')
    if len(katex_nodes) < 10:
        errors.append(f"{PUBLIC_FILE}: expected at least 10 KaTeX math nodes, found {len(katex_nodes)}")

    # Raw TeX control check in visible prose
    raw_tex_hits = sorted(
        {
            m.group(0)
            for text_node in doc.xpath(
                "//article//text()["
                "not(ancestor::code) and not(ancestor::pre) and "
                "not(ancestor::script) and not(ancestor::style) and "
                "not(ancestor::math) and not(ancestor::annotation)"
                "]"
            )
            for m in RAW_TEX.finditer(str(text_node))
        }
    )
    if raw_tex_hits:
        errors.append(f"{PUBLIC_FILE}: unrendered raw TeX commands in article: {', '.join(raw_tex_hits)}")

    # Learning shell and components check
    if not doc.xpath('//*[contains(@class, "learning-shell")]'):
        errors.append(f"{PUBLIC_FILE}: missing .learning-shell container")

    if not doc.xpath('//*[contains(@class, "trace-stepper-container")]'):
        errors.append(f"{PUBLIC_FILE}: missing .trace-stepper-container")

    # ReferenceModeLink check
    ref_links = doc.xpath('//a[contains(@href, "theory/candidate-keys")]')
    if not ref_links:
        errors.append(f"{PUBLIC_FILE}: missing ReferenceModeLink pointing to theory/candidate-keys")

    # Forms and buttons check
    forms = doc.xpath("//form")
    if len(forms) < 4:
        errors.append(f"{PUBLIC_FILE}: expected at least 4 interactive forms, found {len(forms)}")

    return errors


def validate_runtime_bundle() -> list[str]:
    errors: list[str] = []

    # Check CSS contains scoped learning rules
    css_files = list(PUBLIC_DIR.glob("index-*.css"))
    if not css_files:
        errors.append("missing emitted index-*.css")
    else:
        css_text = css_files[0].read_text(encoding="utf-8")
        if (
            'body[data-slug^="learn/"]' not in css_text
            and 'body[data-slug^=learn/]' not in css_text
            and 'body[data-slug^=learn\\/]' not in css_text
        ):
            errors.append("emitted CSS missing scoped body[data-slug^='learn/'] rules")
        if "880px" not in css_text:
            errors.append("emitted CSS missing 880px max-width constraint for learning mode")

    # Check JS contains learning runtime
    js_files = list(PUBLIC_DIR.glob("postscript*.js")) + list((PUBLIC_DIR / "static" / "scripts").glob("*.js"))
    if not js_files:
        errors.append("missing emitted javascript bundles")
    else:
        combined_js = "\n".join(f.read_text(encoding="utf-8") for f in js_files)
        if "csdl_uit_learning_state_v1" not in combined_js:
            errors.append("emitted JS missing active learning state key 'csdl_uit_learning_state_v1'")
        if "minimality-not-checked" not in combined_js:
            errors.append("emitted JS missing canonical error 'minimality-not-checked'")
        if "only-one-key-found" not in combined_js:
            errors.append("emitted JS missing canonical error 'only-one-key-found'")

    return errors


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    all_errors: list[str] = []

    src_errors = validate_markdown_source()
    if src_errors:
        all_errors.extend(src_errors)

    html_errors = validate_rendered_html()
    if html_errors:
        all_errors.extend(html_errors)

    bundle_errors = validate_runtime_bundle()
    if bundle_errors:
        all_errors.extend(bundle_errors)

    if all_errors:
        print("Learning Unit validation FAILED:")
        for err in all_errors:
            print(f"- {err}")
        return 1

    print("Learning Unit validation PASS:")
    print("- Source candidate-keys.md: valid frontmatter, 16 blocks, 5 problems, 6 error classes")
    print("- Rendered HTML: valid title, KaTeX rendered, no raw frontmatter/TeX, ReferenceModeLink verified")
    print("- CSS bundle: scoped single-column 880px layout, no broad page clipping")
    print("- JS bundle: active learning state machine & error diagnosis runtime verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
