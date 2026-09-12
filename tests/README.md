# TOC layout tests

## Test the real rendered website (recommended)

After Quarto/GitHub Pages renders the site, append:

```text
?layout-debug=1
```

Example:

```text
portfolio.html?layout-debug=1
```

A PASS/FAIL panel will show the actual `#quarto-sidebar-toc-left` and `main.content` geometry.

If it says FAIL, capture that panel and send it with a screenshot. It contains the exact wrapper, computed position, grid column, and rectangles needed to diagnose the problem.

## Local regression fixture

With Chromium installed:

```bash
python tests/run_layout_regression.py
```

The fixture emulates the documented Quarto `toc-left` DOM/grid and checks desktop and mobile widths.
