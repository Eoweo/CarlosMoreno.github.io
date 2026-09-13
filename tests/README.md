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


## Architecture v9.0

```bash
python tests/check_architecture_v9.py
```

Checks:

- no `projects/*.qmd`;
- no public links to deleted project pages;
- nine legacy redirects exist;
- redirect targets point to valid Portfolio anchors;
- exact six Portfolio groups remain;
- Home and CV follow the simplified architecture.



## Image assets v9.2

```bash
python tests/check_image_assets_v92.py
```
