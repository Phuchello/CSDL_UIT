import re
from pathlib import Path
from urllib.parse import urlparse, unquote

public = Path("garden/public")
html_files = list(public.rglob("*.html"))
print(f"Total HTML files emitted: {len(html_files)}")

broken = []
total_links = 0

existing_paths = set()
for p in public.rglob("*"):
    rel = p.relative_to(public).as_posix()
    existing_paths.add(rel)
    existing_paths.add("/" + rel)

for html in html_files:
    content = html.read_text(encoding="utf-8")
    links = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
    for l in links:
        total_links += 1
        if l.startswith(("http://", "https://", "mailto:", "data:", "#", "javascript:")):
            continue
        parsed = urlparse(l)
        target = parsed.path
        if not target:
            continue
        target = unquote(target)

        # Handle /CSDL_UIT/ base path prefix
        if target.startswith("/CSDL_UIT/"):
            check_target = target[len("/CSDL_UIT/"):]
        elif target.startswith("/CSDL_UIT"):
            check_target = target[len("/CSDL_UIT"):]
        elif target.startswith("/"):
            check_target = target[1:]
        else:
            rel_dir = html.parent.relative_to(public).as_posix()
            if rel_dir == ".":
                check_target = target
            else:
                resolved = (html.parent / target).resolve()
                try:
                    check_target = resolved.relative_to(public.resolve()).as_posix()
                except ValueError:
                    broken.append((html.name, l, "resolves outside public"))
                    continue

        check_target = check_target.strip("/")
        candidates = [
            check_target,
            check_target + ".html",
            (check_target + "/index.html") if check_target else "index.html",
            check_target + ".pdf",
        ]
        if not any(c in existing_paths or (public / c).exists() for c in candidates):
            broken.append((html.name, l, check_target))

print(f"Total internal links checked: {total_links}")
print(f"Broken internal links: {len(broken)}")
for b in broken[:20]:
    print(" ", b)

if broken:
    exit(1)
else:
    print("LINK CRAWL: ALL PASS")
    exit(0)
