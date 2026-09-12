# Layout tests — v8.1

## 1. Static source contract

Run:

```bash
python tests/check_layout_contract.py
```

This verifies that the source contains the required Quarto named-grid contract and the runtime checks.

## 2. Real browser / rendered Quarto page

After GitHub Pages renders the site, open:

```text
portfolio.html?layout-debug=1
```

The test must show `PASS`.

Required desktop values:

```text
tocLeftPx        <= 2
contentGapPx     0..28
rightGapPx       -1..32
headerTopPx      <= 1
navbarTopPx      <= 1
navbarHeightPx   <= 54
shellHeaderGapPx -1..2
```

The visual outlines are:

```text
red   = TOC
green = main content
blue  = navbar
```

The runtime browser test is authoritative because it measures the actual HTML/CSS emitted by the installed Quarto version.
