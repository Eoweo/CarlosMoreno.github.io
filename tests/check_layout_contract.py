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
    "runtime CSS class": "portfolio-runtime-layout" in css,
    "runtime geometry function": "enforceRuntimeDesktopGeometry" in js,
    "baseline measurement": "runtimeGeometryState.baseline" in js,
    "real toc direct positioning": 'setImportant(toc, "position", "fixed")' in js,
    "real toc left zero": 'setImportant(toc, "left", "0px")' in js,
    "header fixed top zero": 'setImportant(header, "top", "0px")' in js,
    "main spans screen lines": 'setImportant(main, "grid-column", "screen-start / screen-end")' in js,
    "A/B layout-fix switch": 'params.get("layout-fix") === "0"' in js,
    "hard runtime pass": "result.checks.fixApplied" in js,
}

for name, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'}: {name}")

sys.exit(0 if all(checks.values()) else 1)
