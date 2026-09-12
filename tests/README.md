# Layout and animation tests — v8.6

## Animation source contract

```bash
python tests/check_animation_contract.py
```

## Browser test — specific Monitoring section

```text
portfolio.html?animation-debug=1&animation-test=monitoring
```

Expected:

```text
ANIMATION PASS
mode = raf-waapi
visibleButPending = 0
```

The Monitoring record must show:

```text
triggered = true
animationStarted = true
animationFinished = true
finalStateVerified = true
failed = false
```

## General automatic animation test

```text
portfolio.html?animation-test=1
```

## Layout regression

Existing v8.4/v8.5 layout diagnostics remain unchanged:

```text
portfolio.html?layout-debug=1
```
