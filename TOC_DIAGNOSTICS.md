# TOC layout diagnosis — v8.0

## What changed

v8.0 intentionally returns the left table of contents to **Quarto's native layout system**.

The project no longer applies `position: fixed`, `display: block`, custom `margin-left`, or a manually computed `width: calc(100vw - sidebar)` to Quarto's TOC wrapper or page grid.

## Why

Quarto already implements this feature:

```yaml
format:
  html:
    toc: true
    toc-location: left
    toc-expand: 1
    page-layout: full
```

The early v5/v6 portfolio versions worked because the custom CSS styled `#TOC` but **did not replace Quarto's page grid**.

The later regression was introduced when the project began overriding `.page-columns`, `#quarto-content`, `#quarto-sidebar-toc-left`, and `main.content` to force viewport coordinates. That can cause the left TOC to participate in normal flow and occupy a full-width row above the document.

## Supported Quarto solution used in v8.0

Widths are configured through Quarto's official `grid` option:

```yaml
grid:
  sidebar-width: 300px
  body-width: 1600px
  margin-width: 100px
  gutter-width: 0.75rem
```

No wrapper positioning hack is needed.

## Test 1 — automatic regression test

Run:

```bash
python tests/run_layout_regression.py
```

The test checks 1920, 1440, 1100 and 900 px viewports. It asserts that on desktop:

- the TOC is a left column;
- it is not full-width;
- main content is to its right;
- the two regions are not vertically stacked;
- content retains useful width.

At 900 px it verifies the responsive mobile behavior.

## Test 2 — test the ACTUAL Quarto-rendered page

After deployment, open any page with:

```text
?layout-debug=1
```

Example:

```text
portfolio.html?layout-debug=1
```

A diagnostic panel appears in the lower-right corner. It reads the real generated DOM and reports:

- whether `#quarto-sidebar-toc-left` exists;
- the actual sidebar and main-content rectangles;
- whether they are side-by-side or stacked;
- sidebar computed `position`, `grid-column`, `grid-row`, margin and padding;
- whether `#quarto-content` is actually using CSS Grid;
- PASS / FAIL.

This test is much more useful than visually guessing which Quarto wrapper is active.

## Expected desktop result

```text
NAVBAR
─────────────────────────────────────────────────────────
TOC                  MAIN CONTENT
MASTER'S RESEARCH    PORTFOLIO
  Objective 1        ...
  Objective 2        ...
```

Not:

```text
NAVBAR
─────────────────────────────────────────────────────────
TOC across the page
─────────────────────────────────────────────────────────
MAIN CONTENT
```
