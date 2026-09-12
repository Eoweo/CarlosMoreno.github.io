#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml

root = Path(__file__).resolve().parents[1]
css = (root / "assets" / "site.css").read_text(encoding="utf-8")
js = (root / "assets" / "site-scripts.html").read_text(encoding="utf-8")
cfg = yaml.safe_load((root / "_quarto.yml").read_text(encoding="utf-8"))

checks = {
    "toc-left configured": cfg["format"]["html"].get("toc-location") == "left",
    "native toc expansion": cfg["format"]["html"].get("toc-expand") == 1,
    "root named grid present": "[screen-start screen-start-inset page-start page-start-inset]" in css,
    "toc starts at page-start": "grid-column: page-start / body-start" in css,
    "content uses native named lines": "grid-column: body-content-start / body-content-end" in css,
    "toc left padding zero": "padding-left: 0 !important;" in css,
    "header target 48px": "--portfolio-header-height: 48px" in css,
    "real toc selector supported": '#TOC.sidebar.toc-left' in js,
    "hard toc-left test": "tocTouchesViewportLeft" in js,
    "hard navbar-top test": "navbarTouchesViewportTop" in js,
}

for name, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'}: {name}")

sys.exit(0 if all(checks.values()) else 1)
