"""
scripts/agent/capture_screenshots.py
Captures fresh review screenshots for CSDL_UIT Quartz Knowledge Garden.
"""
import http.server
import os
import socketserver
import threading
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
PUBLIC = ROOT / "garden" / "public"
REVIEW_DIR = ROOT / "dist" / "review" / "v1.1_quartz"
REVIEW_DIR.mkdir(parents=True, exist_ok=True)

PORT = 8766


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PUBLIC), **kwargs)

    def translate_path(self, path):
        # Quartz uses /CSDL_UIT/ prefix
        if path.startswith("/CSDL_UIT"):
            path = path[len("/CSDL_UIT"):]
        if not path or path == "/":
            path = "/index.html"
        p = super().translate_path(path)
        if not os.path.exists(p) and os.path.exists(p + ".html"):
            return p + ".html"
        if os.path.isdir(p) and os.path.exists(os.path.join(p, "index.html")):
            return os.path.join(p, "index.html")
        return p


def start_server():
    server = socketserver.TCPServer(("127.0.0.1", PORT), CustomHandler)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    return server


def capture_all():
    server = start_server()
    time.sleep(0.5)

    base_url = f"http://127.0.0.1:{PORT}/CSDL_UIT"

    targets = [
        ("home-desktop.png", f"{base_url}/", 1440, 900, None),
        ("home-mobile.png", f"{base_url}/", 390, 844, None),
        ("theory-division.png", f"{base_url}/theory/division", 1440, 900, None),
        ("sql-double-not-exists.png", f"{base_url}/theory/double-not-exists", 1440, 900, None),
        ("practice-lab03.png", f"{base_url}/practice/lab-03", 1440, 900, None),
        ("trigger-multirow.png", f"{base_url}/practice/multi-row-trigger", 1440, 900, None),
        ("errors.png", f"{base_url}/errors/", 1440, 900, None),
        ("sources.png", f"{base_url}/sources/", 1440, 900, None),
        ("graph-related.png", f"{base_url}/theory/3nf", 1440, 900, None),
        ("search.png", f"{base_url}/", 1440, 900, "search"),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        for filename, url, width, height, action in targets:
            out_path = REVIEW_DIR / filename
            page = browser.new_page(viewport={"width": width, "height": height})
            page.goto(url, wait_until="networkidle")
            page.wait_for_timeout(600)

            if action == "search":
                # open search dialog
                search_btn = page.locator("#search-button, .search-button, button.search")
                if search_btn.count() > 0:
                    search_btn.first.click()
                    page.wait_for_timeout(400)
                    page.keyboard.type("phép chia")
                    page.wait_for_timeout(500)

            page.screenshot(path=str(out_path), full_page=False)
            print(f"Captured: {filename} ({out_path.stat().st_size} bytes)")
            page.close()

        browser.close()

    server.shutdown()
    print("ALL 10 FRESH SCREENSHOTS CAPTURED SUCCESSFULLY.")


if __name__ == "__main__":
    capture_all()
