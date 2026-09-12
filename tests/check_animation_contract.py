#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
css = (root / "assets/site.css").read_text(encoding="utf-8")
js = (root / "assets/site-scripts.html").read_text(encoding="utf-8")
combined = css + js

checks = {
    "WAAPI animation": ".animate([fromFrame, toFrame]" in js,
    "RAF geometry scan": "requestAnimationFrame" in js and "getBoundingClientRect" in js,
    "watchdog present": "startRevealWatchdog" in js and "450" in js,
    "fail-visible timeout": "animation-timeout-safety" in js and "1100" in js,
    "monitoring test remains": "findAnimationTestCandidate" in js and "animation-test" in js,
    "visibleButPending diagnostic": "visibleButPending" in js,
    "compact protocol absent": all(x not in combined for x in [
        "swiss-compact", "swissCompactToggle", "Compact mode"
    ]),
    "reduced-motion protocol absent": all(x not in combined for x in [
        "swiss-reduce-motion", "swissMotionToggle", "prefers-reduced-motion",
        "prefersReducedMotion", "PASS_REDUCED_MOTION"
    ]),
    "theme control remains": "swissThemeToggle" in js,
}

for name, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'}: {name}")

sys.exit(0 if all(checks.values()) else 1)
