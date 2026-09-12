# TOC Diagnostics — v8.2

## Evidencia recibida desde la página real

v8.1 produjo:

```text
viewport.width   = 2560
toc.left         = 292.5
toc.width        = 280
main.left        = 585.3
main.right       = 2272.5
right gap        = 287.5

header.top       = 53
navbar.top       = 53
navbar.height    = 53
```

El `gridTemplateColumns` seguía siendo el generado por Quarto:

```text
[screen-start] 12.75
[screen-start-inset] 259.75
[page-start] 60
[page-start-inset] 180
[body-start-outset] 60
[body-start] 12.75
[body-content-start] 1574.5
...
```

Esto confirma que la corrección CSS de v8.1 no modificó el grid calculado de la página real.

## Estrategia v8.2

No se reconstruye el TOC.

Se conserva:

```text
contenido del TOC generado por Quarto
enlaces
scroll spy nativo
toc-expand
```

Después del render:

```text
#TOC        → fixed, left 0
#header     → fixed, top 0
main        → screen-start / screen-end + margin-left del TOC
body        → padding-top = altura del navbar
```

Las propiedades se aplican mediante:

```javascript
element.style.setProperty(name, value, "important")
```

de modo que no dependen del orden de las hojas CSS.

## Test A/B

### Quarto sin corrección

```text
portfolio.html?layout-debug=1&layout-fix=0
```

Debe mostrar las medidas originales de Quarto.

### Quarto + corrección v8.2

```text
portfolio.html?layout-debug=1
```

Debe mostrar:

```text
fixApplied = true
tocLeftPx ≈ 0
rightGapPx <= 32
headerTopPx ≈ 0
navbarTopPx ≈ 0
```

El panel también incluye:

```text
baseline
```

para comparar el antes y después dentro del mismo render.

## Contrato PASS desktop

```text
fixApplied                    = true
abs(tocLeftPx)                <= 2
tocMarginLeft                 <= 1
tocPaddingLeft                <= 1
contentGapPx                  -1 .. 28
rightGapPx                    -1 .. 32
abs(headerTopPx)              <= 1
abs(navbarTopPx)              <= 1
navbarHeightPx                <= 50
shell starts after header     sí
notStacked                    sí
```
