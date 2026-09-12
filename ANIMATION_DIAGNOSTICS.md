# Animation Diagnostics — v8.6

## Causa confirmada del fallo de v8.5

El log real de `Monitoring` mostró:

```text
initial = false
pending = true
triggered = false
transitionStarted = true
transitionEnded = false
```

Y el resumen global mostró:

```text
pending   = 25
triggered = 0
started   = 25
completed = 0
```

Esto demuestra dos problemas:

1. La transición comenzaba al aplicar el estado oculto (`pending`), por eso `started=25` aunque ningún bloque fue revelado.
2. `IntersectionObserver` no entregó triggers para los bloques posteriores, por lo que `Monitoring` y el resto quedaron ocultos.

## Método v8.6

### Trigger

```text
scroll / resize / watchdog
        ↓
requestAnimationFrame
        ↓
getBoundingClientRect()
        ↓
rect.top < 90% viewport
        ↓
Element.animate()
```

### Animación

```text
clip-path: inset(0 100% 0 0) → inset(0 0 0 0)
opacity:   0                    → 1
```

La animación se ejecuta con Web Animations API, no CSS transitions.

## Prueba específica de Monitoring

Abrir:

```text
portfolio.html?animation-debug=1&animation-test=monitoring
```

Resultado esperado:

```text
ANIMATION PASS
mode = raf-waapi
visibleButPending = 0
```

En el registro `Monitoring`:

```text
triggered = true
animationStarted = true
animationFinished = true
finalStateVerified = true
failed = false
```

## Prueba manual

Abrir:

```text
portfolio.html?animation-debug=1
```

Bajar lentamente desde Objective 1 hacia Monitoring.

Cuando Monitoring entra al 90% superior del viewport:

```text
triggered aumenta
started aumenta
completed aumenta ~700 ms después
pending disminuye
visibleButPending permanece 0
```

## Seguridad

Existen dos capas adicionales:

```text
watchdog cada 450 ms
animation timeout ~1100 ms
```

Si algo falla, el contenido se fuerza visible; nunca debe quedar oculto de forma permanente.
