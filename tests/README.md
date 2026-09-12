# Layout tests — v8.2

## Static source test

```bash
python tests/check_layout_contract.py
```

## Browser A/B test

### Baseline Quarto

```text
portfolio.html?layout-debug=1&layout-fix=0
```

### Corrected v8.2

```text
portfolio.html?layout-debug=1
```

The corrected version must show `PASS`.

The result contains:

```text
baseline        → geometry before repair
runtimeValues   → values used by repair
rects           → final rectangles
measurements    → final gaps/positions
checks          → pass/fail contracts
```

For the supplied 2560 px case the key expected change is:

```text
baseline TOC left ~292.5 px
final TOC left    ~0 px
```
