# TOC Diagnostics — v8.1

## Resultado observado en v8.0

El test real entregó:

```text
viewport.width = 2560
toc.left       = 293
toc.width      = 280
main.left      = 585

sidebar wrapper found = false
TOC found             = true
```

Esto cambia el diagnóstico.

## Qué está generando Quarto

El código actual de Quarto define:

```scss
.sidebar.toc-left {
  grid-column: page-start / body-start;
  grid-row: content-top / page-bottom;
}

.page-columns .content {
  grid-column: body-content-start / body-content-end;
}
```

Por lo tanto, el TOC no está diseñado por defecto para comenzar en `screen-start`.

En el grid capturado por el test, `page-start` estaba varios tracks después del borde de la pantalla. Por eso el TOC comenzó aproximadamente en `x = 293 px`.

## Corrección v8.1

No se utiliza `position: fixed`.

Se conservan los nombres de líneas que Quarto espera, pero se redefine el grid root:

```text
x=0
│
├── [screen-start / page-start]
│    TOC
│
├── [body-start]
│    gap pequeño
│
├── [body-content-start]
│    contenido
│
└── [screen-end]
```

Así, la regla nativa `.sidebar.toc-left { grid-column: page-start / body-start; }` produce ahora el resultado deseado.

## Cómo probar la página real

Abrir:

```text
portfolio.html?layout-debug=1
```

El resultado esperado en desktop es:

```text
PASS
```

y en el JSON:

```text
tocLeftPx             ≈ 0
contentGapPx          0 ... 28
rightGapPx            -1 ... 32
headerTopPx           ≈ 0
navbarTopPx           ≈ 0
navbarHeightPx        <= 54
shellHeaderGapPx      -1 ... 2
```

Visualmente:

```text
ROJO  = TOC
VERDE = contenido
AZUL  = navbar
```

## Si vuelve a fallar

Copiar únicamente estas secciones del panel:

```text
selectorUsed
rects
measurements
computed.sidebar
computed.toc
computed.shell
computed.navbar
checks
```

Con esas medidas se puede identificar la regla exacta que está desplazando el layout sin volver a modificarlo a ciegas.
