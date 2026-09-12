# TOC Diagnostics — v8.3

## Conclusión de las dos pruebas v8.2

### Prueba A — `layout-fix=0`

Fue una prueba de control y era esperable que fallara:

```text
fixApplied = false
toc.left   = 292.5 px
header.top = 64 px
main width = 940 px
```

Esto reproduce el layout original centrado de Quarto.

### Prueba B — corrección activada

La reparación geométrica principal sí funcionó:

```text
fixApplied = true

toc.left       = 0 px
toc.width      = 306 px
header.top     = 0 px
navbar.top     = 0 px
navbar.height  = 48 px
main.left      = 320.4 px
content gap    = 14.4 px
```

El único `FAIL` numérico anterior era:

```text
rightGap = 35 px
```

pero el cálculo usaba `window.innerWidth = 2560`, que incluye una scrollbar de 15 px.

El ancho CSS real era:

```text
documentElement.clientWidth = 2545 px
```

por lo que el gap real era 20 px.

## Qué explica el bloque blanco

La captura muestra que, aun cuando `main.left` ya era correcto, una caja blanca seguía pintándose sobre la zona inicial del `main`.

Esto coincide con un bug abierto de Quarto sobre `toc-location: left` y contenido screen/full-width: se ha reportado una barra vertical blanca que cubre texto pero no necesariamente gráficos.

Además, Quarto mueve el `nav#TOC` a un target generado durante el post-procesado. Mover solamente `#TOC` con `position: fixed` puede dejar su wrapper/slot original en el grid.

## Solución v8.3

```text
Quarto genera #TOC
        ↓
guardar parent/ancestros originales
        ↓
crear #portfolio-toc-shell en <body>
        ↓
mover EL MISMO #TOC al nuevo shell
        ↓
ocultar wrappers originales vacíos
        ↓
main.content z-index:2
        ↓
testear oclusión con elementsFromPoint()
```

No se clona el TOC, por lo que se mantienen los enlaces y clases que Quarto usa para el scroll-spy.

## Nuevo criterio de PASS

Abrir:

```text
portfolio.html?layout-debug=1
```

Debe cumplir:

```text
fixApplied = true
tocPortalCreated = true
tocLeftPx <= 2
contentGapPx <= 28
rightGapPx <= 18        # medido contra clientWidth
headerTopPx <= 1
navbarTopPx <= 1
noMainOcclusion = true
```

El resultado ahora incluye:

```text
baseline.tocAncestors
runtimeValues.staleSlots
occlusion.probes
scrollbarWidthPx
```

Si aún aparece una caja blanca, copiar esas cuatro secciones.
