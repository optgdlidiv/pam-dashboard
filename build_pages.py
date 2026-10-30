"""Make the separate suburban-only link from index.html (run after every change to index.html).

  python build_pages.py   -> writes suburban-live/index.html

The copy is identical to index.html except: suburban view only (no PAM views), its own title.
Which trains it shows is decided by the Sheet's public feed (Apps Script PUBLIC_TRAINS), not here.
"""
from pathlib import Path

BASE = Path(__file__).parent
src = (BASE / "index.html").read_text(encoding="utf-8")
out = src.replace('<html lang="en">', '<html lang="en" data-sub-only="1">', 1) \
         .replace("<title>Mail-Express Punctuality Dashboard</title>", "<title>LIVE Suburban Trains Tracking - DLI</title>", 1)
assert 'data-sub-only="1"' in out
(BASE / "suburban-live").mkdir(exist_ok=True)
(BASE / "suburban-live" / "index.html").write_text(out, encoding="utf-8")
print("Written: suburban-live/index.html")
