#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
css = (root / 'assets' / 'site.css').read_text(encoding='utf-8')
js = (root / 'assets' / 'site-scripts.html').read_text(encoding='utf-8')

checks = {
    'wipe hidden state': 'clip-path: inset(0 100% 0 0)' in css,
    'wipe shown state': 'clip-path: inset(0 0 0 0)' in css,
    'fail-safe visible base': '.swiss-reveal {\n  opacity: 1;' in css,
    'system reduced motion': '@media (prefers-reduced-motion: reduce)' in css,
    'IntersectionObserver primary': 'new IntersectionObserver' in js,
    'observer root margin': 'rootMargin: "0px 0px -10% 0px"' in js,
    'scroll fallback exists': 'scroll-fallback' in js,
    'transition start instrumentation': 'transitionrun' in js and 'transitionstart' in js,
    'transition end instrumentation': 'transitionend' in js,
    'transition cancel instrumentation': 'transitioncancel' in js,
    'debug query': 'animation-debug' in js,
    'automatic test query': 'animation-test' in js,
    'global test object': '__portfolioAnimationTest' in js,
    'toc excluded': 'el.closest("#TOC")' in js,
    'navbar excluded': 'el.closest("#quarto-header")' in js,
}
for name, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'}: {name}")
sys.exit(0 if all(checks.values()) else 1)
