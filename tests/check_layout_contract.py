#!/usr/bin/env python3
from pathlib import Path
import sys, yaml

root = Path(__file__).resolve().parents[1]
css = (root / "assets" / "site.css").read_text(encoding="utf-8")
js = (root / "assets" / "site-scripts.html").read_text(encoding="utf-8")
cfg = yaml.safe_load((root / "_quarto.yml").read_text(encoding="utf-8"))

checks = {
    "toc-location left": cfg["format"]["html"].get("toc-location") == "left",
    "toc-expand 1": cfg["format"]["html"].get("toc-expand") == 1,
    "custom grid removed": "grid" not in cfg["format"]["html"],
    "TOC portal CSS": "#portfolio-toc-shell" in css,
    "TOC portal JS": "ensureTocPortal" in js,
    "stale slot cleanup": "data-portfolio-stale-toc-slot" in js,
    "main above stale slots": 'setImportant(main, "z-index", "2")' in js,
    "clientWidth right gap": "document.documentElement.clientWidth" in js,
    "occlusion probe": "elementsFromPoint" in js,
    "ancestor diagnostics": "tocAncestorChain" in js,
    "toc 20px left padding runtime": 'setImportant(toc, "padding-left", "20px")' in js,
    "toc 20px top padding runtime": 'setImportant(toc, "padding-top", "20px")' in js,
    "toc 20px left padding CSS": "padding-left: 20px !important;" in css,
    "toc 20px top padding CSS": "padding-top: 20px !important;" in css,
    "padding left QA": "tocPaddingLeftTwenty" in js,
    "padding top QA": "tocPaddingTopTwenty" in js,
}

for name, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'}: {name}")

sys.exit(0 if all(checks.values()) else 1)
