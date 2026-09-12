# Animation diagnostics — v8.5

## Estilo implementado

Swiss Wipe horizontal:

```text
hidden  : clip-path inset(0 100% 0 0), opacity 0
visible : clip-path inset(0 0 0 0), opacity 1
```

Trigger principal:

```text
IntersectionObserver
rootMargin = 0px 0px -10% 0px
threshold  = 0.01
```

El listener scroll + requestAnimationFrame existe únicamente como fallback.

## Test pasivo

Abrir cualquier página con:

```text
?animation-debug=1
```

Al cargar, el panel puede indicar:

```text
ANIMATION WAITING
```

Esto es correcto si aún no se ha hecho scroll hasta una sección pendiente.

Al bajar hasta una sección nueva, el resultado esperado es:

```text
ANIMATION PASS
```

El objeto completo también queda disponible en:

```javascript
window.__portfolioAnimationTest
```

## Test automático

Abrir:

```text
?animation-test=1
```

El sitio buscará el primer bloque below-fold pendiente, hará scroll automático y verificará una animación real.

Resultado correcto:

```text
status = PASS
pass   = true
counts.started   >= 1
counts.completed >= 1
counts.failed    = 0
```

## Qué significa PASS

No basta con encontrar la clase `swiss-shown`.

PASS requiere:

```text
transitionrun / transitionstart detectado
transitionend detectado
opacity final >= 0.99
clip-path final visible
```

## Reduced Motion

Con Reduced Motion activo, el test esperado es:

```text
PASS_REDUCED_MOTION
```

porque la omisión de la animación es el comportamiento accesible correcto.

## Fail-safe

Antes de que JavaScript agregue `swiss-js-ready`, `.swiss-reveal` es visible.

Por ello, si JS falla durante inicialización:

```text
contenido visible
animación ausente
```

nunca contenido invisible.
