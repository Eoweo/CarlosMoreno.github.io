# Layout and animation tests — v8.11

## Animation source contract

```bash
python tests/check_animation_contract.py
```

Checks that the Swiss Wipe remains active and that Compact Mode / Reduced Motion protocols are absent.

## Monitoring animation test

```text
portfolio.html?animation-debug=1&animation-test=monitoring
```

Expected:

```text
ANIMATION PASS
mode = raf-waapi
visibleButPending = 0
```

## General animation test

```text
portfolio.html?animation-test=1
```

## Layout regression

```text
portfolio.html?layout-debug=1
```
