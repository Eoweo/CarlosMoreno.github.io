# Build validation — v8.0

- YAML valid: YES
- toc-location left: YES
- toc-expand 1: YES
- page-layout full: YES
- grid sidebar 300px: YES
- grid body 1600px: YES
- grid margin 100px: YES
- search false: YES
- native TOC styling present: YES
- manual fixed TOC absent: YES
- manual #quarto-content display block absent: YES
- custom TOC builder absent: YES
- TOC replacement absent: YES
- layout self-test present: YES
- layout debug query present: YES
- QMD YAML valid: YES
- projects/index absent: YES
- 8 detail buttons: YES
- CV two download buttons: YES
- JS syntax: YES
- CSS braces: YES
- REQ-QUARTO-TOC-001: YES
- REQ-QUARTO-TOC-002: YES
- REQ-QUARTO-LAYOUT-001: YES
- REQ-QUARTO-GRID-001: YES
- REQ-QA-006: YES
- REQ-QA-007: YES
- REQ-QA-008: YES

## Browser regression test

The project includes `tests/run_layout_regression.py` and an actual-page self-test available with `?layout-debug=1`.

The construction sandbox could not complete headless Chromium navigation (Chromium hangs in this container), so the interactive geometry check is intentionally left for the rendered GitHub Pages site. The code/YAML/CSS structural checks above passed.

Recommended final check: open `portfolio.html?layout-debug=1` after deployment and verify that the panel says `PASS`.
