#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
css = (root / "assets/site.css").read_text(encoding="utf-8")
js = (root / "assets/site-scripts.html").read_text(encoding="utf-8")

checks = {
    "v8.6 WAAPI CSS marker": "VERSION 8.6 — SWISS WIPE VIA WEB ANIMATIONS API" in css,
    "Element.animate used": ".animate([fromFrame, toFrame]" in js,
    "RAF geometry scan": "requestAnimationFrame" in js and "getBoundingClientRect" in js,
    "IntersectionObserver not animation dependency": "buildRevealObserver" not in js,
    "watchdog present": "startRevealWatchdog" in js and "450" in js,
    "fail-visible timeout": "animation-timeout-safety" in js and "1100" in js,
    "targeted monitoring test": "findAnimationTestCandidate" in js and "animation-test" in js,
    "visibleButPending diagnostic": "visibleButPending" in js,
    "reduced motion": "prefers-reduced-motion: reduce" in css,
    "no CSS pending transition": "swiss-pending:not(.swiss-shown)" not in css,
}

for name, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'}: {name}")

sys.exit(0 if all(checks.values()) else 1)
