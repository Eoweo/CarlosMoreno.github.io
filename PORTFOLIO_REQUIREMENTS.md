# Especificación de requisitos — Portafolio Carlos Moreno Rojas

> **Documento vivo de requisitos**
>
> **Versión base documentada:** `v8.0 — Swiss Research / Native Quarto TOC`  
> **Base funcional:** `v5.2` + integración visual/interactiva Swiss Research  
> **Propósito:** dejar por escrito el comportamiento, diseño, arquitectura y restricciones actuales del portafolio para poder modificar requisitos de forma controlada sin perder funcionalidades existentes.

---

# 1. Objetivo del documento

Este archivo define el **estado funcional y visual actual del portafolio** y debe utilizarse como referencia antes de realizar cualquier cambio.

La intención es que futuras modificaciones se hagan contra requisitos explícitos, evitando cambios accidentales en:

- estructura del contenido;
- navegación;
- jerarquía de páginas;
- diseño Swiss Research;
- barra lateral;
- animaciones;
- modo claro/oscuro;
- accesibilidad;
- comportamiento responsive;
- publicación mediante GitHub Pages;
- estructura Quarto;
- contenido técnico ya redactado.

Cuando se solicite una modificación futura, este documento puede editarse primero y luego utilizarse como especificación de implementación.

---

# 2. Convenciones para gestionar requisitos

Cada requisito utiliza un identificador único.

Formato recomendado:

```text
REQ-<ÁREA>-<NÚMERO>
```

Ejemplos:

```text
REQ-UI-001
REQ-NAV-004
REQ-ANIM-002
REQ-CONTENT-010
REQ-DEPLOY-003
```

## 2.1 Estados

| Estado | Significado |
|---|---|
| `IMPLEMENTADO` | Existe y funciona en la versión actual. |
| `REQUERIDO` | Debe mantenerse en futuras versiones. |
| `MODIFICAR` | Existe, pero se decidió cambiar. |
| `PROPUESTO` | Requisito nuevo aún no implementado. |
| `PENDIENTE` | Definido pero falta información o contenido. |
| `ELIMINAR` | Se decidió retirar en una versión futura. |
| `VALIDAR` | Implementado, pero requiere prueba adicional. |

## 2.2 Prioridades

| Prioridad | Significado |
|---|---|
| `P0` | Crítico. No se puede romper. |
| `P1` | Importante para la experiencia principal. |
| `P2` | Mejora relevante. |
| `P3` | Opcional / futuro. |

## 2.3 Regla de cambio

Antes de modificar una funcionalidad estable:

1. identificar el requisito correspondiente;
2. editar **este mismo archivo `PORTFOLIO_REQUIREMENTS.md`**;
3. cambiar el requisito afectado a `MODIFICAR` o agregar un requisito nuevo;
4. escribir el nuevo comportamiento esperado;
5. implementar;
6. validar;
7. registrar el cambio en la tabla de versiones;
8. volver a marcarlo como `IMPLEMENTADO`.

> **Regla permanente desde v7:** ningún cambio funcional, visual, de contenido estructural o de navegación se considera terminado si no quedó reflejado en este Markdown de requisitos.

---

# 3. Arquitectura general

## REQ-ARCH-001 — Framework principal

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El sitio debe utilizar **Quarto Website** como sistema principal de generación.

Configuración actual:

```yaml
project:
  type: website
  output-dir: _site
```

El contenido principal se mantiene en archivos `.qmd`.

---

## REQ-ARCH-002 — Separación entre contenido, estilo y comportamiento

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La arquitectura debe mantener separadas las siguientes capas:

```text
Contenido     → archivos .qmd
Configuración → _quarto.yml
Estilo        → assets/site.css
Interacción   → assets/site-scripts.html
Publicación   → .github/workflows/publish.yml
```

No se debe trasladar innecesariamente contenido técnico desde los `.qmd` hacia JavaScript o CSS.

---

## REQ-ARCH-003 — Conservación del contenido v5.2

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La integración Swiss Research de v6 no modifica el contenido de los archivos `.qmd` provenientes de v5.2.

En la validación de v6:

```text
QMD files changed from v5.2: 0
```

Los futuros cambios de diseño deben intentar conservar esta separación.

---

## REQ-ARCH-004 — Estructura principal de archivos

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Estructura actual relevante:

```text
/
├── _quarto.yml
├── index.qmd
├── cv.qmd
├── contact.qmd
├── portfolio.qmd
│
├── projects/
│   ├── index.qmd
│   ├── thesis.qmd
│   ├── cybathlon.qmd
│   ├── candel.qmd
│   ├── borealis.qmd
│   ├── organ-preservation.qmd
│   ├── unet.qmd
│   ├── fpga.qmd
│   └── vscan.qmd
│
├── assets/
│   ├── site.css
│   ├── site-scripts.html
│   └── images/
│
├── .github/
│   └── workflows/
│       └── publish.yml
│
└── portfolio_preview.html
```

---

# 4. Configuración global de Quarto

## REQ-QUARTO-001 — Navegación superior

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La barra superior debe incluir:

### Izquierda

```text
Portfolio
CV
Contact
```

### Derecha

```text
Project pages
```

Configuración actual:

```yaml
website:
  navbar:
    left:
      - href: index.qmd
        text: Portfolio
      - href: cv.qmd
        text: CV
      - href: contact.qmd
        text: Contact
    right:
      - href: projects/index.qmd
        text: Project pages
```

---

## REQ-QUARTO-002 — Buscador

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P2`

El sitio utiliza el buscador nativo de Quarto:

```yaml
search: true
```

---

## REQ-QUARTO-003 — Footer

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P2`

Footer actual:

```text
Izquierda: Carlos Moreno Rojas
Derecha: Biomedical & Electrical Engineering
```

---

## REQ-QUARTO-004 — Tabla de contenido

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Configuración global:

```yaml
toc: true
toc-location: left
toc-depth: 3
smooth-scroll: true
```

Cada página puede sobreescribir `toc-depth` y `toc-title`.

---

## REQ-QUARTO-005 — Código

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P2`

Quarto debe permitir:

```yaml
code-copy: true
code-overflow: wrap
```

---

## REQ-QUARTO-006 — Ejecución

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Actualmente:

```yaml
execute:
  freeze: auto
```

Esto permite conservar resultados renderizados cuando corresponde.

---

# 5. Sistema visual Swiss Research

## REQ-UI-001 — Identidad visual

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La identidad visual actual se denomina:

```text
Swiss Research
```

Principios:

- estética académica;
- estética de ingeniería;
- diseño sobrio;
- poca ornamentación;
- tipografía fuerte;
- separadores horizontales gruesos;
- acento rojo;
- composición editorial;
- evitar apariencia de landing page corporativa;
- evitar gradientes decorativos innecesarios;
- priorizar contenido técnico e imágenes de ingeniería.

---

## REQ-UI-002 — Paleta modo claro

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

| Uso | Color |
|---|---|
| Fondo | `#F7F5EF` |
| Superficie | `#ECE9E0` |
| Superficie secundaria | `#FFFDF8` |
| Texto principal | `#111111` |
| Texto secundario | `#66635D` |
| Bordes | `#CBC7BC` |
| Acento | `#D63230` |

---

## REQ-UI-003 — Paleta modo oscuro

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

| Uso | Color |
|---|---|
| Fondo | `#141414` |
| Superficie | `#1E1E1E` |
| Superficie secundaria | `#181818` |
| Texto principal | `#F1EFE8` |
| Texto secundario | `#A7A39A` |
| Bordes | `#383633` |
| Acento | `#FF615E` |

---

## REQ-UI-004 — Tipografía

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Familia principal:

```css
Arial, Helvetica, sans-serif
```

Características:

- títulos pesados;
- títulos principales en mayúsculas;
- tracking negativo en títulos grandes;
- estructura editorial;
- jerarquía visual clara.

---

## REQ-UI-005 — Título principal

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

El título de página utiliza:

- tamaño responsivo;
- peso `900`;
- mayúsculas;
- interlineado compacto;
- `letter-spacing` negativo;
- ancho máximo controlado.

---

## REQ-UI-006 — Encabezados de sección

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Las principales secciones utilizan una línea superior fuerte:

```css
border-top: 4px solid var(--text);
```

Los encabezados `h1` internos y `h2` utilizan una presentación editorial Swiss.

---

# 6. Barra lateral izquierda / TOC

## REQ-NAV-001 — Posición

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La tabla de contenidos se muestra a la izquierda.

Debe permanecer visible durante la navegación en escritorio.

---

## REQ-NAV-002 — Jerarquía visual

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La barra lateral debe representar una jerarquía tipo:

```text
MASTER'S RESEARCH — LIVER VIABILITY & ICG-NIR
    Research overview
    Objective 1 — Perfusion Platform
    Objective 2 — Baseline Dataset
    Objective 3 — ICG-NIR Marker

ROBOTICS & REHABILITATION
    CYBATHLON 2024

MEDICAL DEVICES & NEUROENGINEERING
    CandelStim
```

Los niveles superiores funcionan visualmente como nombres de categoría.

Los niveles inferiores funcionan como enlaces navegables.

Desde v7, la navegación utiliza un **acordeón contextual**:

```text
estado normal:
    se muestran únicamente los títulos de las categorías

categoría activa:
    se mantiene visible el título
    se expanden sus subtítulos

al pasar a la categoría siguiente:
    se colapsa la categoría anterior
    se expande automáticamente la nueva
```

Solo debe existir un grupo principal expandido en función de la sección que el usuario está visualizando.

---

## REQ-NAV-003 — Estado activo

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Al avanzar por el contenido:

- el enlace correspondiente debe activarse;
- el texto activo cambia al color rojo Swiss;
- se muestra una barra vertical roja;
- se utiliza clase propia `swiss-active`;
- se mantiene compatibilidad con la clase `active` de Quarto.

---

## REQ-NAV-004 — Seguimiento automático del scroll

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La barra izquierda debe seguir dinámicamente la posición del usuario en el documento.

El cálculo utiliza la posición de los headings visibles respecto a un marcador superior.

No depende exclusivamente del comportamiento nativo de Quarto.

---

## REQ-NAV-005 — Auto-scroll interno de la barra lateral

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Cuando el enlace activo deja de estar visible dentro de la barra lateral:

- el TOC debe desplazarse automáticamente;
- el elemento activo debe mantenerse visible;
- el movimiento es suave;
- si está activo `Reduced Motion`, el movimiento pasa a instantáneo.

Margen interno actual de referencia:

```text
42 px
```

---

## REQ-NAV-006 — Altura y scroll independiente

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

La barra lateral posee:

```css
max-height: calc(100vh - header - margen);
overflow-y: auto;
```

Por lo tanto:

- el documento puede continuar bajando;
- la barra lateral mantiene su propio scroll;
- ambos scrolls están coordinados mediante JavaScript.

---

## REQ-NAV-007 — Profundidad

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Soporta visualmente hasta tres niveles:

```text
Nivel 1 → categoría
Nivel 2 → sección/proyecto
Nivel 3 → subsección técnica
```

---

# 7. Animaciones

## REQ-ANIM-001 — Reveal por scroll

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Los elementos aparecen progresivamente al entrar en el viewport.

Elementos actualmente animables:

```text
h1 internos
h2
h3
p
.image-slot
.project-meta
.skill-chips
.project-grid
.skill-grid
.download-grid
.contact-card
.cell
table
blockquote
ul
ol
```

---

## REQ-ANIM-002 — Efecto Swiss

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

El efecto utiliza un reveal horizontal basado en:

```css
clip-path: inset(0 100% 0 0)
```

hasta:

```css
clip-path: inset(0 0 0 0)
```

Curva temporal:

```css
cubic-bezier(.77, 0, .18, 1)
```

---

## REQ-ANIM-003 — Stagger

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P2`

Existe un pequeño desfase entre elementos sucesivos.

Implementación actual:

```text
0 ms
24 ms
48 ms
72 ms
```

El ciclo se repite cada cuatro elementos.

---

## REQ-ANIM-004 — Fail-safe

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Este es un requisito crítico.

**El contenido debe ser visible por defecto.**

JavaScript solo activa los estados ocultos después de inicializarse correctamente.

Por lo tanto:

```text
Si JavaScript funciona → animación visible.
Si JavaScript falla    → contenido visible sin animación.
```

Nunca debe repetirse el problema en que la columna de contenido queda vacía porque `opacity: 0` o `clip-path` permanecen activos.

---

## REQ-ANIM-005 — Activación inicial

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Antes de añadir la clase:

```text
swiss-js-ready
```

los elementos presentes en el viewport inicial se marcan como:

```text
swiss-shown
```

Luego se habilita el sistema de animación.

---

## REQ-ANIM-006 — Optimización del evento scroll

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

El scroll utiliza:

```javascript
requestAnimationFrame()
```

y un flag de control para evitar procesar múltiples actualizaciones simultáneas.

El listener utiliza:

```javascript
{ passive: true }
```

---

## REQ-ANIM-007 — Recalcular después de carga

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Existe una comprobación adicional después de aproximadamente:

```text
250 ms
```

para compensar cambios de layout producidos por:

- Mermaid;
- fuentes;
- elementos renderizados;
- cambios de tamaño posteriores al DOM inicial.

---

# 8. Controles por iconos

## REQ-CTRL-001 — Tipo de controles

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Los controles superiores utilizan iconos SVG inline.

No requieren librerías externas de iconos.

---

## REQ-CTRL-002 — Control de modo compacto

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Icono:

```text
≡ / tres líneas
```

Función:

- reducir separación vertical;
- reducir alturas de placeholders;
- aumentar densidad de información.

Clase aplicada:

```text
swiss-compact
```

Preferencia persistente:

```text
localStorage["swiss-compact"]
```

---

## REQ-CTRL-003 — Reduced Motion

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Icono conceptual:

```text
flechas de movimiento
```

Función:

- desactivar animaciones;
- desactivar transiciones;
- eliminar reveal;
- utilizar scroll inmediato cuando corresponda.

Clase aplicada:

```text
swiss-reduce-motion
```

Preferencia persistente:

```text
localStorage["swiss-reduce-motion"]
```

---

## REQ-CTRL-004 — Claro / oscuro

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Iconos:

```text
Luna → cambiar a oscuro
Sol  → cambiar a claro
```

El sistema intenta utilizar primero el mecanismo nativo de Quarto.

Fallback disponible:

```text
swiss-manual-dark
```

---

## REQ-CTRL-005 — Sincronización de icono de tema

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

El icono del tema se sincroniza con los cambios de Quarto mediante:

```javascript
MutationObserver
```

Se observan:

```text
class
data-bs-theme
```

---

## REQ-CTRL-006 — Persistencia segura

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

El acceso a `localStorage` está protegido mediante `try/catch`.

Esto evita que una restricción del navegador rompa toda la página.

Funciones:

```javascript
safeGet()
safeSet()
```

---

# 9. Modo claro y oscuro

## REQ-THEME-001 — Temas Quarto

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Configuración:

```yaml
theme:
  light: cosmo
  dark: darkly
```

El CSS propio redefine la identidad Swiss por encima de ambos temas.

---

## REQ-THEME-002 — Variables CSS

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Los colores se implementan mediante variables.

Ejemplos:

```css
--page-bg
--surface
--surface-2
--text
--muted
--border
--accent
--accent-soft
```

Por lo tanto, cambiar la paleta futura debe realizarse principalmente modificando variables y no reglas individuales.

---

# 10. Placeholders de imágenes

## REQ-MEDIA-001 — Espacios técnicos

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Los placeholders existentes de v5.2 se conservan.

Clase principal:

```text
.image-slot
```

Variantes:

```text
.image-slot.large
.image-slot.small
```

---

## REQ-MEDIA-002 — Estética

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Los placeholders utilizan:

- superficie Swiss;
- borde discontinuo;
- diagonales cruzadas;
- etiqueta central;
- título de imagen sugerida;
- subtítulo descriptivo.

No deben parecer tarjetas decorativas o mocks de marketing.

---

## REQ-MEDIA-003 — Imágenes futuras

**Estado:** `PENDIENTE`  
**Prioridad:** `P1`

Las imágenes reales deben reemplazar progresivamente los placeholders.

Carpeta prevista:

```text
assets/images/
```

Antes de publicación definitiva se debe revisar:

- confidencialidad;
- propiedad intelectual;
- datos personales;
- autorización de laboratorios/empresas;
- resolución;
- peso de archivo;
- texto alternativo.

---

# 11. Tarjetas, grids y componentes

## REQ-COMP-001 — Tarjetas

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P2`

Componentes soportados:

```text
.project-card
.skill-card
.download-card
.contact-card
```

Estética:

- borde simple;
- sin bordes redondeados prominentes;
- sin sombra decorativa;
- fondo neutro;
- hover discreto.

---

## REQ-COMP-002 — Grids

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P2`

Clases:

```text
.project-grid
.skill-grid
.download-grid
```

Uso de:

```css
repeat(auto-fit, minmax(...))
```

para adaptación automática.

---

## REQ-COMP-003 — Chips / metadata

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P2`

Componentes:

```text
.project-meta
.skill-chips
```

Aspecto técnico, cuadrado y sobrio.

---

## REQ-COMP-004 — Tablas

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P2`

Las tablas heredan correctamente:

- fondo;
- texto;
- bordes;
- modo claro;
- modo oscuro.

---

## REQ-COMP-005 — Código y Mermaid

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

El sitio conserva compatibilidad con:

- bloques de código;
- celdas;
- diagramas Mermaid;
- SVG generados por Quarto.

Los SVG de Mermaid deben limitarse al ancho disponible.

---

# 12. Responsive / dispositivos

## REQ-RESP-001 — Breakpoint 1100 px

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Ajusta tamaño y separación de controles.

---

## REQ-RESP-002 — Breakpoint 991 px

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

En pantallas pequeñas:

- los controles cambian a posición fija;
- el TOC deja de comportarse como panel sticky independiente;
- el título reduce tamaño;
- placeholders grandes reducen altura.

---

## REQ-RESP-003 — Breakpoint 620 px

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Ajustes adicionales:

- controles más pequeños;
- título principal más pequeño;
- menor separación en encabezados.

---

# 13. Contenido del Portfolio principal

## REQ-CONTENT-001 — Tesis de Magíster

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La tesis se organiza como **una investigación coherente de tres objetivos**, no como varios proyectos independientes.

Estructura:

```text
Master's Research — Liver Viability & ICG-NIR
    Objective 1 — Ex Vivo Perfusion Platform
    Objective 2 — Baseline Physiological Dataset
    Objective 3 — ICG-NIR Functional Marker
```

---

## REQ-CONTENT-002 — Robotics & Rehabilitation

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Incluye:

```text
CYBATHLON 2024 — Robotic Transfemoral Prosthesis
Electrical System & Integration
Testing & Competition
```

---

## REQ-CONTENT-003 — Medical Devices & Neuroengineering

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Incluye:

```text
CandelStim — Transcranial Electrical Stimulation
Hardware & PCB
Firmware & Embedded Systems
Validation
```

---

## REQ-CONTENT-004 — Organ Preservation & Transplantation

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Incluye:

```text
Borealis UC — Organ Supercooling
Organ Preservation Machine Redesign
```

---

## REQ-CONTENT-005 — Medical Imaging & AI

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Incluye:

```text
Lung Segmentation with U-Net
Network & Training
Segmentation Results
```

---

## REQ-CONTENT-006 — Embedded Systems & FPGA

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Incluye:

```text
Universal Testing Machine Upgrade
FPGA Architecture
Validation
```

---

## REQ-CONTENT-007 — CAD & Prototyping

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Incluye:

```text
Vscan Air Medical Device Enclosure
Design Iterations
```

---

## REQ-CONTENT-008 — Teaching & Leadership

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Incluye:

```text
Physics Laboratory Teaching Assistant
Biomedical Engineering Student Chapter UC
IEEE EMBS PUC Chile
```

---

## REQ-CONTENT-009 — Industry & Technical Experience

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Incluye:

```text
Meldic Ltda.
```

---

## REQ-CONTENT-010 — Technical Skills

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Existe una sección global de habilidades técnicas.

---

## REQ-CONTENT-011 — Engineering Approach

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Existe una sección para describir metodología de ingeniería y forma de trabajo.

---

# 14. Página CV

## REQ-CV-001 — Perfil

**Estado:** `IMPLEMENTADO`

```text
Professional Profile
    Biomedical & Electrical Engineering
```

---

## REQ-CV-002 — Educación

**Estado:** `IMPLEMENTADO`

```text
MSc Biomedical Engineering
Electrical Engineering
Biomedical Engineering
```

---

## REQ-CV-003 — Research & Development

**Estado:** `IMPLEMENTADO`

```text
Master's Research — Liver Viability & ICG-NIR
Borealis UC — Organ Supercooling
Organ Preservation Machine
```

---

## REQ-CV-004 — Professional Experience

**Estado:** `IMPLEMENTADO`

```text
Candel Medical Company
Meldic Ltda.
```

---

## REQ-CV-005 — Selected Projects

**Estado:** `IMPLEMENTADO`

```text
CYBATHLON 2024
Lung Segmentation — U-Net
FPGA — Universal Testing Machine
Vscan Air Enclosure
```

---

## REQ-CV-006 — Teaching & Leadership

**Estado:** `IMPLEMENTADO`

```text
Physics Laboratory Teaching Assistant
Biomedical Engineering Student Chapter UC
IEEE EMBS PUC Chile
```

---

## REQ-CV-007 — Skills

**Estado:** `IMPLEMENTADO`

```text
Electronics & Embedded Systems
FPGA & Digital Design
Programming & Data
Biomedical Engineering
CAD & Prototyping
```

---

## REQ-CV-008 — Languages

**Estado:** `IMPLEMENTADO`

```text
Spanish
English
```

---

## REQ-CV-009 — Descargas PDF

**Estado:** `PENDIENTE`  
**Prioridad:** `P2`

La estructura contempla:

```text
Research CV
Engineering CV
```

Falta incorporar los archivos PDF reales.

---

# 15. Página Contact

## REQ-CONTACT-001 — Información

**Estado:** `PENDIENTE`  
**Prioridad:** `P1`

La página contempla:

```text
Email
GitHub
LinkedIn
```

Los datos públicos reales todavía deben reemplazar placeholders cuando corresponda.

La disposición visual **ya está implementada** como tarjetas distribuidas y no como una lista vertical simple.

---

## REQ-CONTACT-002 — Perfiles de investigación

**Estado:** `PENDIENTE`  
**Prioridad:** `P2`

Campos contemplados:

```text
ORCID
Google Scholar
```

Solo deben publicarse si existen y se desean hacer públicos.

---

## REQ-CONTACT-003 — Documentos

**Estado:** `IMPLEMENTADO`

La página enlaza conceptualmente a:

```text
Curriculum Vitae
Portfolio
```

---

# 16. Páginas individuales de proyectos

## REQ-PROJ-001 — Índice de proyectos

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Categorías:

```text
Master's Research
Robotics & Rehabilitation
Medical Devices & Neuroengineering
Organ Preservation & Transplantation
Medical Imaging & AI
Embedded Systems & FPGA
CAD & Prototyping
```

---

## REQ-PROJ-002 — Thesis

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Archivo:

```text
projects/thesis.qmd
```

Incluye:

```text
Project overview
Need and hypothesis

Objective 1 — Ex Vivo Perfusion Platform
    Objective
    Perfusion circuit
    Reservoir and pumping
    Pulse damping
    Oxygenation and bubble management
    Physiological monitoring
    Sensors and electronics
    Calibration and validation
    Objective 1 success criterion

Objective 2 — Baseline Dataset without ICG
    Objective
    Recorded variables
    Representative traces
    Vascular resistance
    Reproducibility

Objective 3 — ICG-NIR Functional Marker
    Objective
    ICG experiment
    Optical calibration
    Fluorescence kinetics
    Functional parameters
    Functional viability index
    Validation

Experimental workflow
My engineering contribution
Current status
References
```

---

## REQ-PROJ-003 — Otras páginas

**Estado:** `IMPLEMENTADO`

Archivos:

```text
projects/cybathlon.qmd
projects/candel.qmd
projects/borealis.qmd
projects/organ-preservation.qmd
projects/unet.qmd
projects/fpga.qmd
projects/vscan.qmd
```

Cada página mantiene TOC propio y hereda:

- diseño Swiss;
- modo claro/oscuro;
- animaciones;
- TOC dinámico;
- auto-scroll;
- controles superiores.

---

# 17. Preview local

## REQ-PREVIEW-001 — Archivo autónomo

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Existe:

```text
portfolio_preview.html
```

Su función es permitir probar visualmente:

- Portfolio;
- CV;
- Contact;
- barra lateral;
- scroll activo;
- auto-scroll del sidebar;
- animaciones;
- claro/oscuro;
- compacto;
- reduced motion.

---

## REQ-PREVIEW-002 — Navegación interna

**Estado:** `IMPLEMENTADO`

El preview permite cambiar entre:

```text
Portfolio
CV
Contact
```

sin recargar la página.

---

## REQ-PREVIEW-003 — Fail-safe

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El preview replica la misma filosofía:

```text
contenido visible primero
→ JavaScript inicializa
→ animaciones se habilitan
```

---

# 18. GitHub Pages y despliegue

## REQ-DEPLOY-001 — GitHub Actions

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Workflow:

```text
.github/workflows/publish.yml
```

---

## REQ-DEPLOY-002 — Disparadores

**Estado:** `IMPLEMENTADO`

El workflow se ejecuta:

```text
push a main
workflow_dispatch manual
```

---

## REQ-DEPLOY-003 — Permisos

**Estado:** `IMPLEMENTADO`

```yaml
contents: read
pages: write
id-token: write
```

---

## REQ-DEPLOY-004 — Flujo de build

**Estado:** `IMPLEMENTADO`

Secuencia:

```text
Checkout
↓
Set up Quarto
↓
quarto render
↓
Configure Pages
↓
Upload _site
↓
Deploy GitHub Pages
```

---

## REQ-DEPLOY-005 — Directorio de publicación

**Estado:** `IMPLEMENTADO`

Quarto genera:

```text
_site/
```

GitHub Pages publica dicho directorio como artifact.

---

# 19. Validaciones actuales

## REQ-QA-001 — YAML

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La versión v6 fue validada con:

```text
_quarto.yml: OK
17 QMD revisados
0 errores de front matter YAML
```

---

## REQ-QA-002 — JavaScript

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Validación realizada:

```text
Global scripts JS: OK
Offline preview JS: OK
```

---

## REQ-QA-003 — CSS

**Estado:** `IMPLEMENTADO`

Validación:

```text
CSS braces balanced: YES
```

---

## REQ-QA-004 — Archivos críticos

**Estado:** `IMPLEMENTADO`

Se comprobaron:

```text
_quarto.yml
index.qmd
cv.qmd
contact.qmd
assets/site.css
assets/site-scripts.html
portfolio_preview.html
.github/workflows/publish.yml
```

---

# 20. Accesibilidad y robustez

## REQ-A11Y-001 — Reduced Motion manual

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El usuario puede desactivar explícitamente animaciones.

---

## REQ-A11Y-002 — Labels en controles

**Estado:** `IMPLEMENTADO`

Los botones agregados por JS incluyen:

```text
title
aria-label
```

---

## REQ-A11Y-003 — Contenido independiente de JavaScript

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La información principal debe continuar siendo legible si JavaScript falla.

JavaScript mejora la experiencia, pero no debe ser necesario para acceder al contenido.

---

## REQ-A11Y-004 — Contraste

**Estado:** `VALIDAR`  
**Prioridad:** `P1`

La paleta fue diseñada con contraste fuerte, pero antes de una versión final pública conviene realizar una comprobación WCAG formal de:

- texto principal;
- texto secundario;
- rojo sobre fondos;
- controles;
- links;
- modo oscuro.

---

# 21. Rendimiento

## REQ-PERF-001 — Sin librería JS externa para interacción Swiss

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Los controles y scroll dinámico utilizan JavaScript nativo.

---

## REQ-PERF-002 — SVG inline

**Estado:** `IMPLEMENTADO`

Los iconos de:

```text
Sol
Luna
Movimiento
Compacto
```

son SVG inline.

No requieren Font Awesome ni otra dependencia externa.

---

## REQ-PERF-003 — Scroll optimizado

**Estado:** `IMPLEMENTADO`

Uso de:

```text
requestAnimationFrame
passive scroll listener
```

para minimizar trabajo durante scroll.

---

## REQ-PERF-004 — Optimización futura de imágenes

**Estado:** `PROPUESTO`  
**Prioridad:** `P1`

Cuando se incorporen imágenes reales:

- preferir WebP cuando sea adecuado;
- usar JPG optimizado para fotografías;
- evitar archivos originales excesivamente grandes;
- ancho recomendado general entre `1400–2000 px` para imágenes principales;
- considerar lazy loading;
- comprimir videos o alojarlos externamente según necesidad.

---

# 22. Restricciones de diseño actuales

Los siguientes puntos representan decisiones vigentes y deben considerarse **restricciones**, salvo que se modifique explícitamente este documento.

## REQ-RULE-001

**Estado:** `REQUERIDO`  
**Prioridad:** `P0`

No convertir el portafolio en una landing page de marketing genérica.

---

## REQ-RULE-002

**Estado:** `REQUERIDO`  
**Prioridad:** `P0`

Debe conservar una apariencia de:

```text
investigación
ingeniería
documentación técnica
portfolio académico
```

---

## REQ-RULE-003

**Estado:** `REQUERIDO`  
**Prioridad:** `P0`

La barra lateral jerárquica es parte esencial del diseño.

---

## REQ-RULE-004

**Estado:** `REQUERIDO`  
**Prioridad:** `P0`

La tesis debe permanecer organizada por los tres objetivos científicos.

---

## REQ-RULE-005

**Estado:** `REQUERIDO`  
**Prioridad:** `P0`

Las animaciones nunca deben poder ocultar permanentemente contenido.

---

## REQ-RULE-006

**Estado:** `REQUERIDO`  
**Prioridad:** `P1`

Las animaciones deben ser discretas.

No utilizar:

- parallax agresivo;
- partículas;
- animaciones constantes;
- fondos en movimiento;
- transiciones distractoras.

---

## REQ-RULE-007

**Estado:** `REQUERIDO`  
**Prioridad:** `P1`

Los controles visuales deben usar iconos simples y comprensibles.

---

# 23. Variables fácilmente modificables

Los siguientes valores pueden utilizarse como parámetros de diseño para futuras versiones.

## 23.1 Colores

Archivo:

```text
assets/site.css
```

Variables:

```css
--page-bg
--surface
--surface-2
--text
--muted
--border
--accent
--accent-soft
```

---

## 23.2 Altura del header

```css
--header-height: 62px;
```

---

## 23.3 Margen del auto-scroll lateral

Actualmente:

```text
42 px
```

JavaScript:

```text
keepActiveTocVisible()
```

---

## 23.4 Trigger del scroll-spy

Actualmente:

```javascript
Math.min(165, window.innerHeight * .25)
```

---

## 23.5 Trigger del reveal

Actualmente:

```javascript
window.innerHeight * 0.91
```

---

## 23.6 Trigger inicial del reveal

Actualmente:

```javascript
window.innerHeight * 0.97
```

---

## 23.7 Stagger

Actualmente:

```javascript
(i % 4) * 24 ms
```

---

## 23.8 Duración del reveal

Actualmente aproximadamente:

```text
clip-path: 680 ms
opacity:   360 ms
```

---

## 23.9 Breakpoints

```text
1100 px
991 px
620 px
```

---


# 23A. Requisitos introducidos en v7

## REQ-DOC-001 — Actualización obligatoria del Markdown de requisitos

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

A partir de v7, **cada cambio solicitado al portafolio debe quedar reflejado en `PORTFOLIO_REQUIREMENTS.md`**.

Esto incluye cambios de:

- diseño;
- colores;
- navegación;
- animaciones;
- contenido estructural;
- páginas;
- componentes;
- comportamiento responsive;
- GitHub Pages;
- arquitectura;
- accesibilidad;
- controles;
- imágenes;
- nuevas funcionalidades.

### Criterio de aceptación

Una nueva versión no se considera terminada si:

```text
código actualizado = sí
requirements.md actualizado = no
```

---

## REQ-CTRL-007 — Swiss Controls alineados al extremo derecho

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Los controles Swiss:

```text
Compact Mode
Reduced Motion
Light / Dark
```

deben aparecer agrupados en el **extremo derecho de la barra superior**.

No deben aparecer entre los enlaces de navegación ni desplazar visualmente el nombre del sitio.

Implementación:

```css
.swiss-controls {
    order: 9999;
    margin-left: auto;
    justify-content: flex-end;
}
```

---

## REQ-NAV-008 — TOC lateral en modo acordeón contextual

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La lista lateral debe mostrar por defecto únicamente los títulos principales.

Ejemplo:

```text
PROFILE
CURRENT RESEARCH
SELECTED WORK
ENGINEERING AREAS
EDUCATION & LEADERSHIP
EXPLORE
```

Cuando el usuario visualiza el contenido perteneciente a un título:

```text
CURRENT RESEARCH
    Ex Vivo Liver Viability & ICG-NIR
```

sus subtítulos se expanden.

Al avanzar a otra sección:

```text
CURRENT RESEARCH       → se colapsa
SELECTED WORK          → se expande
    CYBATHLON 2024
    CandelStim
    Other Engineering Projects
```

### Reglas

- solo el grupo activo se expande;
- los demás grupos quedan colapsados;
- el estado se determina por scroll-spy;
- el enlace activo continúa marcado en rojo;
- el auto-scroll del TOC continúa funcionando;
- Reduced Motion elimina la transición pero no el comportamiento;
- el contenido sigue siendo navegable mediante anchors.

---

## REQ-HOME-001 — Página principal como resumen profesional

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

`index.qmd` deja de ser el portafolio técnico completo y pasa a funcionar como una **home/resumen profesional**.

Debe responder rápidamente:

```text
Quién soy
Qué tipo de ingeniería hago
Cuál es mi investigación actual
Cuáles son mis proyectos principales
Qué áreas técnicas manejo
Cuál es mi formación
Dónde ver el detalle
```

### Secciones v7

```text
Profile
    Biomedical & Electrical Engineering

Current Research
    Ex Vivo Liver Viability & ICG-NIR

Selected Work
    CYBATHLON 2024
    CandelStim
    Other Engineering Projects

Engineering Areas
    Biomedical Instrumentation
    Electronics & Embedded Systems
    Medical Imaging, Signals & Optics
    CAD, Prototyping & Integration

Education & Leadership
    Education
    Leadership & Teaching

Explore
    Technical Portfolio
    CV & Contact
```

### Restricción

La home no debe reemplazar ni eliminar el contenido técnico detallado.

El detalle permanece disponible en:

```text
portfolio.qmd
projects/*.qmd
```

---

## REQ-HOME-002 — Accesos directos desde Home

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

La página principal debe ofrecer accesos evidentes hacia:

```text
Technical Portfolio
Curriculum Vitae
Contact
Project Pages
```

---

## REQ-HOME-003 — Resumen de investigación en tres objetivos

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

La investigación de Magíster debe resumirse mediante tres bloques enlazables:

```text
01 Perfusion Platform
02 Physiological Baseline
03 ICG-NIR Marker
```

Los tres elementos deben dirigir al contenido detallado de la tesis.

---

## REQ-CONTACT-004 — Layout distribuido de Contact

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

La página `contact.qmd` no debe presentarse como una lista vertical de campos.

Debe utilizar una estructura visual distribuida:

```text
Hero / presentación
↓
Direct Contact
    Email
    GitHub
    LinkedIn
↓
Research Profiles
    ORCID
    Google Scholar
↓
Documents & Portfolio
    Curriculum Vitae
    Engineering Portfolio
↓
Publishing Status
```

En escritorio se utilizan grids de dos y tres columnas según el bloque.

En móvil se convierten en una columna.

---

## REQ-CONTACT-005 — Contact cards

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Cada canal principal utiliza una tarjeta con:

```text
icono
categoría
nombre
descripción breve
valor / placeholder
```

Los documentos se presentan como tarjetas enlazables.

No se deben inventar datos de contacto: los valores `ADD_...` permanecen hasta recibir información pública real.

---



# 23B. Correcciones introducidas en v7.1

## REQ-NAV-009 — Nombre del sitio enlaza siempre a Home

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El texto:

```text
Carlos Moreno Rojas
```

de la barra superior debe actuar como enlace permanente hacia la página principal:

```text
index.qmd → index.html
```

La ruta debe funcionar tanto:

- desde páginas de nivel raíz;
- desde `projects/*.qmd`;
- en GitHub Pages;
- en rutas relativas.

La implementación utiliza la ruta renderizada del enlace `Portfolio` para derivar de manera segura la ruta relativa hacia `index.html`.

---

## REQ-NAV-010 — Portfolio de la barra superior abre el portafolio técnico

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El enlace superior:

```text
Portfolio
```

debe dirigir a:

```text
portfolio.qmd
```

y **no** a la Home.

La navegación principal queda conceptualmente:

```text
Carlos Moreno Rojas → Home / resumen profesional
Portfolio           → portafolio técnico completo
CV                  → curriculum vitae
Contact             → página de contacto
Project pages       → índice de páginas individuales
```

---

## REQ-NAV-011 — Acordeón TOC robusto con Quarto

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La detección de grupos del TOC no debe depender únicamente de:

```javascript
:scope > ul
```

La lógica debe:

1. encontrar el `UL` raíz del TOC de manera robusta;
2. identificar cada `LI` de nivel superior que contenga un `UL` secundario;
3. asociar cada subtítulo activo con su grupo principal;
4. expandir solo el grupo actual;
5. colapsar los demás;
6. mantener el enlace activo visible mediante auto-scroll;
7. actualizar `aria-expanded` y `aria-hidden`.

Esto debe seguir funcionando aunque Quarto agregue clases o wrappers no funcionales alrededor del TOC.


> **Actualización v7.2:** el comportamiento requerido se mantiene, pero la implementación basada en el árbol generado por Quarto fue reemplazada por `REQ-NAV-012` a `REQ-NAV-016`, que reconstruyen el TOC desde los headings reales.

---

## REQ-RENDER-001 — Componentes personalizados deben usar sintaxis segura de Quarto/Pandoc

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Los componentes complejos de `index.qmd` y `contact.qmd` no deben escribirse como HTML anidado con indentación susceptible de ser interpretada como bloque de código.

Patrón anterior problemático:

```html
<div class="home-intro">
  <div class="home-intro-copy">
    ...
  </div>
</div>
```

Patrón requerido:

```markdown
:::: {.home-intro}

::: {.home-intro-copy}
...
:::

::::
```

Se deben preferir:

- **Pandoc Fenced Divs** para layout y componentes;
- Markdown normal para texto;
- enlaces Markdown con atributos de clase;
- HTML raw únicamente cuando sea imprescindible y sin indentación ambigua.

### Criterio de aceptación

La página renderizada **nunca** debe mostrar literalmente cadenas como:

```text
<div class="home-kicker">
<div class="contact-heading">
<strong>Biomedical R&D</strong>
```

---

## REQ-RENDER-002 — Home y Contact no pueden renderizar HTML como código visible

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Se considera un fallo crítico si cualquier componente personalizado aparece en cajas de código con scroll horizontal.

Debe validarse específicamente:

```text
Home hero
Home metric cards
Home research cards
Home project cards
Contact hero
Contact cards
Contact document cards
```

---



# 23C. Requisitos introducidos en v7.2

## REQ-NAV-012 — TOC reconstruido desde los headings reales

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

A partir de v7.2, el comportamiento dinámico de la lista izquierda **no debe depender de la estructura HTML interna generada por Quarto para su TOC**.

JavaScript debe obtener directamente los headings renderizados del contenido:

```text
h1
h2
h3
```

y construir una nueva jerarquía de navegación.

### Regla de jerarquía

El nivel más alto existente en cada página se convierte en el nivel principal.

Ejemplos:

```text
Página Home:
H1 → título principal del grupo
H2 → subtítulo

Portfolio técnico:
H1 → título principal del grupo
H2 → subtítulo
H3 → subtítulo de tercer nivel

Página de tesis:
H2 → título principal del grupo
H3 → subtítulo
```

Por lo tanto, la navegación se adapta automáticamente a páginas con distintas profundidades de headings.

---

## REQ-NAV-013 — Expansión mediante `<details>` / `<summary>`

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Los grupos principales del TOC dinámico deben utilizar controles HTML nativos:

```html
<details>
  <summary>...</summary>
  ...
</details>
```

La propiedad:

```javascript
details.open
```

es la fuente de verdad para expandir o colapsar el grupo.

### Comportamiento requerido

Mientras el usuario avanza:

```text
Grupo A → open = true
Grupo B → open = false
Grupo C → open = false
```

Al entrar en Grupo B:

```text
Grupo A → open = false
Grupo B → open = true
Grupo C → open = false
```

Este método reemplaza el mecanismo anterior basado principalmente en:

```text
clases CSS + max-height
```

para mejorar robustez.

---

## REQ-NAV-014 — Tercer nivel contextual

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Cuando una página tiene:

```text
H1
    H2
        H3
```

al abrir el grupo `H1` se muestran sus `H2`.

Los `H3` solo deben mostrarse bajo el `H2` correspondiente a la zona activa.

Ejemplo:

```text
MASTER'S THESIS
    Objective 1
        Monitoring
    Objective 2
    Objective 3
```

Si el usuario está viendo `Monitoring`, ese tercer nivel aparece bajo `Objective 1`.

---

## REQ-NAV-015 — Fail-safe del TOC

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La navegación personalizada debe construirse completamente antes de reemplazar el TOC nativo.

Secuencia:

```text
1. Quarto genera su TOC normal.
2. JavaScript lee los headings reales.
3. JavaScript construye el nuevo TOC en memoria.
4. Solo si la construcción termina correctamente:
       reemplazar contenido de #TOC.
```

Si JavaScript falla antes del paso 4:

```text
el TOC normal de Quarto permanece visible y utilizable.
```

---

## REQ-NAV-016 — Auto-scroll del nuevo TOC

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El TOC reconstruido conserva el seguimiento automático:

- marca el heading activo;
- abre el grupo correspondiente;
- abre el tercer nivel contextual cuando existe;
- mantiene visible el enlace activo;
- desplaza únicamente el contenedor lateral;
- respeta Reduced Motion.

---

## REQ-CLEAN-001 — Código CSS y JS consolidado

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

`assets/site.css` y `assets/site-scripts.html` deben contener únicamente la implementación vigente.

No deben mantenerse concatenadas implementaciones obsoletas de:

```text
v6
v7
v7.1
```

El código actual debe estar organizado por secciones funcionales y evitar reglas duplicadas.

---

## REQ-CLEAN-002 — Eliminación de archivos históricos redundantes

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

La raíz del proyecto no debe acumular archivos de validación de versiones anteriores.

Se eliminaron:

```text
BUILD_VALIDATION_V6.md
BUILD_VALIDATION_V7.md
BUILD_VALIDATION_V7_1.md
SWISS_STYLE_INTEGRATION.md
```

Debe conservarse únicamente:

```text
BUILD_VALIDATION.md
```

correspondiente a la versión actual.

---

## REQ-CLEAN-003 — Eliminación de páginas legacy no enlazadas

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Se eliminaron páginas standalone antiguas que ya no formaban parte de la navegación y cuyo contenido está cubierto por Home, Portfolio y CV:

```text
about.qmd
research.qmd
experience.qmd
skills.qmd
```

La información relevante permanece en:

```text
index.qmd
portfolio.qmd
cv.qmd
projects/*.qmd
```

---

## REQ-QA-005 — Prueba de navegación con navegador real

**Estado:** `VALIDAR`  
**Prioridad:** `P0`

La lógica del TOC personalizado debe validarse, además de la sintaxis JavaScript, en Chrome/Chromium real.

La prueba debe verificar al menos:

```text
TOC generado desde headings
grupo inicial expandido
cambio de grupo al hacer scroll
subtítulo activo
uso de <details open>
tercer nivel contextual cuando exista
auto-scroll de la columna izquierda
```

### Estado de la validación automática

El entorno utilizado para construir el proyecto bloqueó la navegación de Chromium/Playwright, incluso para páginas HTML locales y `localhost`.

Por lo tanto:

```text
sintaxis JavaScript → validada
estructura del algoritmo → validada
preview standalone → generado
prueba interactiva real en Chrome → VALIDAR por el usuario
```

Este requisito debe pasar a `IMPLEMENTADO` una vez comprobado el ZIP/preview en Chrome.

---



# 23D. Requisitos introducidos en v7.3

## REQ-PORTFOLIO-TOC-001 — Estructura exacta e invariable de la lista del Portfolio

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La lista lateral del **Portfolio técnico (`portfolio.qmd`)** debe utilizar **exactamente tres niveles jerárquicos**:

```text
TÍTULO
    SUBTÍTULO
        SUBSUBTÍTULO
```

Los **únicos títulos principales permitidos** son, exactamente y en este orden:

```text
MASTER'S RESEARCH — LIVER VIABILITY & ICG-NIR
ROBOTICS & REHABILITATION
ORGAN PRESERVATION & TRANSPLANTATION
MEDICAL IMAGING & AI
EMBEDDED SYSTEMS & FPGA
CAD & PROTOTYPING
```

> **Regla estricta:** no se debe crear, renombrar, eliminar, dividir ni agregar ningún otro título principal del TOC del Portfolio sin modificar primero este requisito.

La lista completa debe ser **exactamente** la siguiente:

```text
MASTER'S RESEARCH — LIVER VIABILITY & ICG-NIR
    Objective 1 — Ex Vivo Perfusion Platform
        Monitoring
    Objective 2 — Baseline Dataset without ICG
    Objective 3 — ICG-NIR Functional Marker

ROBOTICS & REHABILITATION
    Ciervo UC — CYBATHLON 2024
        My role
    CandelStim — Transcranial Electrical Stimulation
        Technical work

ORGAN PRESERVATION & TRANSPLANTATION
    Borealis UC — Organ Supercooling
    Organ Preservation Machine Redesign
        Engineering work

MEDICAL IMAGING & AI
    Lung Segmentation with U-Net

EMBEDDED SYSTEMS & FPGA
    FPGA Upgrade — Universal Testing Machine

CAD & PROTOTYPING
    Vscan Air — Medical Device Enclosure
```

### Interpretación de los niveles

```text
H1 → TÍTULO
H2 → SUBTÍTULO
H3 → SUBSUBTÍTULO
```

La navegación dinámica descrita en `REQ-NAV-012` a `REQ-NAV-016` debe respetar esta jerarquía.

### Asignación de CandelStim

`CandelStim — Transcranial Electrical Stimulation` debe integrarse dentro de:

```text
ROBOTICS & REHABILITATION
```

y no debe generar un título principal independiente como:

```text
MEDICAL DEVICES & NEUROENGINEERING
```

Esto es deliberado porque los seis títulos principales anteriores son la estructura fija definida para el Portfolio.

---

## REQ-PORTFOLIO-TOC-002 — Contenido que se mantiene fuera de la lista técnica

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Las siguientes secciones **se mantienen en el contenido de `portfolio.qmd`**, pero **no deben aparecer en la lista lateral técnica del Portfolio**:

```text
Teaching — Physics Laboratory
Biomedical Engineering Student Chapter UC
IEEE EMBS PUC Chile
Meldic Ltda.
Skills
Engineering approach
Contact
```

Estas secciones deben utilizar:

```text
{.toc-ignore}
```

o un mecanismo equivalente que las excluya de la navegación lateral sin eliminar su contenido.

### Regla

El hecho de que estas secciones existan en la página **no autoriza** a convertirlas en nuevos títulos principales del TOC.

---

## REQ-PORTFOLIO-TOC-003 — Profundidad del TOC del Portfolio

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

`portfolio.qmd` debe utilizar:

```yaml
toc-depth: 3
```

para que el fallback nativo de Quarto pueda representar:

```text
título
subtítulo
subsubtítulo
```

La navegación personalizada también debe leer:

```text
h1
h2
h3
```

---

## REQ-PROJ-004 — Project Pages utiliza botones de redirección

**Estado:** `ELIMINAR`  
**Prioridad:** `P1`

En `projects/index.qmd`, el nombre de cada proyecto **no debe ser un hipervínculo azul**.

Patrón prohibido:

```markdown
## [CYBATHLON 2024](cybathlon.qmd)
```

Patrón requerido:

```markdown
## CYBATHLON 2024

Descripción breve del proyecto.

[Open project](cybathlon.qmd){.project-page-button}
```

Por lo tanto:

- el título del proyecto se muestra como texto normal;
- debajo se mantiene su descripción;
- la navegación hacia la página individual se realiza mediante un botón;
- el botón debe respetar el estilo Swiss;
- el botón no debe mostrarse como texto azul convencional;
- hover/focus utiliza el color de acento Swiss;
- la URL de destino de cada proyecto no cambia.


> **Actualización v7.5:** este requisito queda histórico. `projects/index.qmd` fue eliminado y los botones de acceso a páginas detalladas se trasladaron a `portfolio.qmd`, que ahora es el único índice técnico.

---

## REQ-PROJ-005 — Proyectos que requieren botón en Project Pages

**Estado:** `ELIMINAR`  
**Prioridad:** `P1`

`projects/index.qmd` debe incluir botón de redirección para:

```text
Ex Vivo Liver Viability with ICG-NIR
CYBATHLON 2024
CandelStim
Borealis UC — Supercooling
Organ Preservation Machine Redesign
Lung Segmentation — U-Net
Universal Testing Machine Upgrade
Vscan Air Enclosure
```

Cada botón debe redirigir a su archivo actual:

```text
thesis.qmd
cybathlon.qmd
candel.qmd
borealis.qmd
organ-preservation.qmd
unet.qmd
fpga.qmd
vscan.qmd
```

No se modifica el contenido de las páginas individuales.


> **Actualización v7.5:** este requisito queda histórico. `projects/index.qmd` fue eliminado y los botones de acceso a páginas detalladas se trasladaron a `portfolio.qmd`, que ahora es el único índice técnico.

---



# 23E. Requisitos introducidos en v7.4

## REQ-LAYOUT-001 — El cuerpo debe utilizar la zona derecha disponible

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

El contenido principal no debe quedar visualmente concentrado en una columna angosta dejando una gran zona derecha sin utilizar.

Todas las páginas públicas principales y páginas de proyectos deben utilizar:

```yaml
page-layout: full
```

El cuerpo mantiene un límite máximo para evitar líneas excesivamente largas:

```css
main.content {
    width: 100%;
    max-width: 1180px;
}
```

### Comportamiento esperado

En desktop:

```text
TOC izquierdo
│
│    CUERPO DE CONTENIDO ────────────────────────────────→
│    utiliza una porción significativamente mayor
│    del espacio central/derecho disponible.
```

Grids, imágenes, tablas, diagramas y tarjetas deben poder utilizar todo el ancho del cuerpo.

El texto corrido puede limitarse aproximadamente a:

```css
108ch
```

para conservar legibilidad.

---

## REQ-TYPE-001 — Escala de títulos moderada

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Los títulos deben conservar la jerarquía Swiss Research sin ocupar una parte excesiva de la pantalla.

Escala aproximada actual:

```text
Título de página:
2.15rem → 3.4rem responsive

H1 interno:
1.78rem

H2:
1.42rem

H3:
1.08rem
```

También deben reducirse proporcionalmente:

```text
home-statement
contact-heading
contact-monogram
```

### Regla

No volver a escalas cercanas a `5rem` para el título normal de una página sin modificar primero este requisito.

---

## REQ-ARCH-005 — Diagrama vivo de la estructura de páginas

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

El proyecto debe incluir:

```text
SITE_STRUCTURE.md
```

Este archivo documenta:

- páginas públicas existentes;
- relación entre Home, Portfolio, CV, Contact y Project Pages;
- páginas individuales de proyectos;
- nivel de detalle esperado en cada nivel;
- zonas de solapamiento;
- posibles simplificaciones futuras.

Este archivo es documentación de arquitectura y **no debe agregarse automáticamente al navbar público**.

---

## REQ-ARCH-006 — Niveles de información para reducir redundancia

**Estado:** `REQUERIDO`  
**Prioridad:** `P1`

La profundidad de contenido debe seguir:

```text
HOME < PORTFOLIO < PROJECT PAGE
```

Interpretación:

```text
HOME
→ quién soy + investigación + proyectos destacados

PORTFOLIO
→ resumen técnico suficiente de cada proyecto

PROJECT PAGE
→ documentación detallada del proyecto
```

`CV` debe concentrarse en información curricular.

`Contact` debe concentrarse en contacto/perfiles/documentos.

No se deben copiar bloques extensos idénticos entre estos niveles.

---

## REQ-ARCH-007 — Redundancia Project Pages / Portfolio pendiente de decisión

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P2`

Actualmente existen dos rutas hacia las páginas individuales:

```text
Portfolio → proyecto individual

Project Pages → proyecto individual
```

`SITE_STRUCTURE.md` identifica esta página intermedia como la redundancia estructural más clara.

### Estado v7.4

```text
projects/index.qmd se mantiene.
Project pages permanece en el navbar.
No se elimina contenido.
```

Una posible versión futura podrá retirar `Project Pages` de la navegación y utilizar `Portfolio` como único índice de proyectos, pero esto requiere aprobación explícita.


### Decisión v7.5

La simplificación fue aprobada e implementada:

```text
projects/index.qmd → eliminado
Project Pages en navbar → eliminado
Portfolio → único índice general de proyectos
```

Las páginas individuales `projects/*.qmd` se conservan.

---



# 23F. Requisitos introducidos en v7.5

## REQ-ARCH-008 — Portfolio es el único índice general de proyectos

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La arquitectura pública debe ser:

```text
HOME
├── PORTFOLIO
│   └── páginas individuales de proyectos
├── CV
└── CONTACT
```

Se elimina el nivel intermedio:

```text
Project Pages
```

Por lo tanto:

```text
projects/index.qmd
```

no debe existir en la arquitectura vigente.

---

## REQ-NAV-017 — Navbar simplificado

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La barra superior debe contener únicamente:

```text
Carlos Moreno Rojas → Home
Portfolio           → portfolio.qmd
CV                  → cv.qmd
Contact             → contact.qmd
```

No debe aparecer:

```text
Project pages
```

en ningún sector del navbar.

---

## REQ-PORTFOLIO-NAV-001 — Botones desde Portfolio a páginas detalladas

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Como `Portfolio` es el único índice general, cada proyecto resumido en `portfolio.qmd` debe ofrecer un botón:

```text
Open detailed project →
```

hacia su página individual.

Rutas obligatorias:

```text
Master's Research      → projects/thesis.qmd
CYBATHLON              → projects/cybathlon.qmd
CandelStim             → projects/candel.qmd
Borealis               → projects/borealis.qmd
Preservation Machine   → projects/organ-preservation.qmd
U-Net                  → projects/unet.qmd
FPGA                    → projects/fpga.qmd
Vscan Air               → projects/vscan.qmd
```

Los botones utilizan la clase Swiss existente:

```text
.project-page-button
```

---

## REQ-LAYOUT-002 — Uso dinámico de todo el ancho disponible

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El contenido de escritorio debe utilizar dinámicamente el espacio disponible desde la zona inmediatamente posterior al TOC izquierdo hasta casi el borde derecho de la ventana.

No debe existir un límite fijo como:

```text
1180 px
```

que vuelva a producir una gran zona vacía en monitores anchos.

En desktop, `main.content` debe abarcar:

```css
grid-column: body-start / screen-end;
```

manteniendo el TOC independiente.

---

## REQ-LAYOUT-003 — Márgenes laterales responsive mediante `clamp()`

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Los márgenes no deben ser distancias fijas grandes.

El borde derecho y separación respecto al contenido deben utilizar valores dinámicos similares a:

```css
--portfolio-edge-gutter: clamp(0.875rem, 1.45vw, 2rem);
--portfolio-content-gap: clamp(0.65rem, 1.1vw, 1.25rem);
```

Objetivo:

```text
pantalla pequeña  → margen pequeño
pantalla media    → margen proporcional
pantalla grande   → margen crece ligeramente pero permanece acotado
```

El contenido no debe quedar pegado al borde, pero tampoco debe desperdiciar una franja grande de pantalla.

---

## REQ-LAYOUT-004 — Distinción entre ancho de contenido técnico y ancho de lectura

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Los elementos técnicos deben poder utilizar el 100% del ancho disponible:

```text
imágenes
diagramas
grids
tablas
resultados
Mermaid
cards
```

El texto corrido puede tener un máximo basado en caracteres para preservar legibilidad:

```text
desktop normal → hasta 118ch
pantallas muy grandes → hasta 126ch
```

Esto no debe volver a limitar el ancho de imágenes o componentes técnicos.

---

## REQ-LAYOUT-005 — Comportamiento por resolución

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La distribución debe adaptarse al menos a:

```text
Desktop ≥ 992 px
Large desktop ≥ 1600 px
Tablet / mobile < 992 px
Small mobile < 520 px
```

### Desktop

- TOC lateral independiente;
- contenido se extiende hacia el borde derecho;
- gutters dinámicos pequeños.

### Large desktop

- se sigue aprovechando toda la pantalla;
- el margen derecho puede crecer moderadamente mediante `clamp()`;
- no se centra una columna fija angosta.

### Tablet / mobile

- `main.content` ocupa `100%`;
- padding horizontal responsive;
- no existen anchos desktop rígidos.

---



# 23G. Requisitos introducidos en v7.6

## REQ-LAYOUT-006 — Lista izquierda próxima al borde real de la ventana

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La lista lateral debe permanecer en el lado izquierdo y **no debe moverse a la parte superior**.

En desktop, la columna del TOC debe ocupar:

```css
grid-column: screen-start / body-start;
```

y el margen exterior izquierdo debe ser esencialmente cero.

El único espacio permitido entre el borde del navegador y el contenido de la lista es un padding técnico pequeño y responsive:

```css
--toc-edge-padding: clamp(0.2rem, 0.35vw, 0.42rem);
```

### Comportamiento requerido

```text
BORDE IZQUIERDO DE LA VENTANA
│ TOC
│  MASTER'S RESEARCH...
│    Objective 1...
│
└─ sin una franja vacía grande
```

No debe existir:

- margen izquierdo de la página;
- padding grande de Quarto antes del TOC;
- centrado de la columna lateral.

---

## REQ-NAVBAR-001 — Navbar pegado a la parte superior

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

`navbar navbar-expand-lg` debe comenzar prácticamente en el borde superior del documento.

Se requiere:

```css
#quarto-header {
    top: 0;
    margin: 0;
    padding: 0;
}

.navbar.navbar-expand-lg {
    margin: 0;
    padding-top: 0.18rem;
    padding-bottom: 0.18rem;
}
```

La altura de referencia pasa a:

```css
--header-height: 52px;
```

No debe existir una banda vacía importante sobre la barra superior.

---

## REQ-NAV-018 — Prohibición de acceso a Project Pages

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Como `Project Pages` dejó de existir en v7.5, no debe existir ningún acceso de navegación hacia esa página.

Esto incluye:

```text
navbar
Home
Portfolio
CV
Contact
footer
```

`projects/index.qmd` debe permanecer eliminado.

Las páginas individuales `projects/*.qmd` sí se mantienen y se abren desde `Portfolio`.

---

## REQ-PORTFOLIO-NAV-002 — Botón de detalle al final de cada proyecto

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Cada uno de los ocho proyectos resumidos en `portfolio.qmd` debe terminar con:

```markdown
[Open detailed project](...){.project-page-button}
```

El botón debe estar ubicado **después del contenido visual/textual del proyecto y antes del siguiente proyecto o separador**.

Proyectos obligatorios:

```text
Master's Research
CYBATHLON
CandelStim
Borealis
Organ Preservation Machine
U-Net
FPGA
Vscan Air
```

Los títulos de proyecto no deben transformarse en enlaces azules para resolver esta navegación.

---

## REQ-CV-010 — Dos descargas de CV al inicio

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La sección final:

```text
Downloads
```

debe eliminarse de `cv.qmd`.

En cambio, inmediatamente después del encabezado inicial del CV deben aparecer dos botones:

```text
Download Research CV
Download Engineering CV
```

Los archivos asociados deben existir dentro del proyecto:

```text
downloads/Carlos_Moreno_Research_CV.pdf
downloads/Carlos_Moreno_Engineering_CV.pdf
```

Los botones deben utilizar:

```text
.cv-download-button
```

y el atributo HTML `download`.

### Regla de reemplazo

Los PDF pueden actualizarse posteriormente sin cambiar las URLs siempre que se mantengan exactamente esos nombres de archivo.

---

## REQ-SEARCH-001 — Buscador completamente eliminado

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El sitio no debe mostrar buscador.

La configuración debe utilizar:

```yaml
website:
  search: false
```

Como defensa adicional, los componentes de búsqueda generados por Quarto deben ocultarse por CSS si llegaran a aparecer.

No debe existir:

- icono de lupa;
- campo de búsqueda;
- overlay de búsqueda;
- espacio reservado para el buscador.

---

## REQ-LAYOUT-007 — Página usa la ventana completa

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El layout debe utilizar el ancho completo del navegador:

```css
html,
body {
    width: 100%;
    margin: 0;
    padding: 0;
}
```

En desktop:

```text
screen-start → TOC
body-start   → contenido
screen-end   → final del contenido
```

La página no debe quedar dentro de un contenedor general centrado con márgenes exteriores grandes.

---



# 23H. Corrección de layout introducida en v7.7

## REQ-LAYOUT-008 — El TOC se ancla al borde físico del viewport

**Estado:** `SUPERADO`  
**Prioridad:** `P0`

La lista izquierda no debe depender de:

```text
screen-start
body-start
page-columns
```

para determinar su posición física en desktop.

El problema observado en v7.6 fue que Quarto mantenía una columna invisible antes de `screen-start`, produciendo una gran franja vacía a la izquierda aunque los márgenes internos fueran cero.

A partir de v7.8, la columna lateral utiliza coordenadas directas del viewport y se aplica al **contenedor real del TOC izquierdo de Quarto**:

```css
#quarto-sidebar-toc-left,
.sidebar.toc-left {
    position: fixed;
    left: 0;
    top: var(--header-height);
    bottom: 0;
}
```

> **Corrección respecto de v7.7:** `#quarto-margin-sidebar` no es el contenedor del TOC cuando se usa `toc-location: left`. Aplicar el posicionamiento a ese elemento dejaba `#quarto-sidebar-toc-left` dentro del flujo normal y hacía que la lista apareciera arriba del contenido, como en modo móvil.

### Resultado obligatorio

```text
x = 0 px del navegador
│
├── TOC / lista izquierda
│
└── contenido inmediatamente después del ancho del TOC
```

No se permite ninguna columna vacía antes del TOC en desktop.


> **Superado en v8.0:** la implementación manual del shell/TOC fue retirada. Quarto vuelve a controlar la cuadrícula y la posición del TOC de forma nativa.

---

## REQ-LAYOUT-009 — El contenido principal se posiciona respecto al ancho real del TOC

**Estado:** `SUPERADO`  
**Prioridad:** `P0`

El contenido principal debe comenzar mediante:

```css
margin-left: var(--fixed-toc-width);
```

y utilizar:

```css
width: calc(100vw - var(--fixed-toc-width));
```

Esto reemplaza el uso de columnas de grid Quarto para el shell principal del sitio.

El ancho del TOC es responsive:

```css
--fixed-toc-width: clamp(15.5rem, 16vw, 18.5rem);
```

En pantallas muy grandes puede ajustarse moderadamente, pero el TOC debe seguir empezando en `left: 0`.


> **Superado en v8.0:** la implementación manual del shell/TOC fue retirada. Quarto vuelve a controlar la cuadrícula y la posición del TOC de forma nativa.

---

## REQ-LAYOUT-010 — Quarto page grid desactivado para el shell de escritorio

**Estado:** `SUPERADO`  
**Prioridad:** `P0`

En desktop:

```css
#quarto-content,
#quarto-content.page-columns {
    display: block;
    width: 100vw;
    max-width: none;
    margin: 0;
    padding: 0;
}
```

La navegación interna de Quarto puede seguir existiendo, pero su grid central no debe controlar la posición lateral del TOC ni del cuerpo.


> **Superado en v8.0:** la implementación manual del shell/TOC fue retirada. Quarto vuelve a controlar la cuadrícula y la posición del TOC de forma nativa.

---



# 23I. Corrección de posición del TOC introducida en v7.8

## REQ-LAYOUT-011 — El TOC desktop debe usar `#quarto-sidebar-toc-left`

**Estado:** `SUPERADO`  
**Prioridad:** `P0`

Cuando Quarto utiliza:

```yaml
toc-location: left
```

el contenedor desktop correcto de la navegación lateral es:

```text
#quarto-sidebar-toc-left
```

o su equivalente:

```text
.sidebar.toc-left
```

Este elemento debe ser el que recibe:

```css
position: fixed;
left: 0;
top: var(--header-height);
bottom: 0;
```

No se debe utilizar `#quarto-margin-sidebar` como sustituto del TOC izquierdo.


> **Superado en v8.0:** la implementación manual del shell/TOC fue retirada. Quarto vuelve a controlar la cuadrícula y la posición del TOC de forma nativa.

---

## REQ-LAYOUT-012 — La lista izquierda no puede ocupar una fila superior en desktop

**Estado:** `SUPERADO`  
**Prioridad:** `P0`

En resoluciones desktop (`>= 992px`) la lista lateral:

- permanece a la izquierda;
- comienza debajo del navbar;
- ocupa la altura disponible del viewport;
- queda fuera del flujo vertical del documento;
- **no puede crear una caja o fila encima de `main.content`**;
- no puede empujar el título `PORTFOLIO` hacia abajo.

La geometría obligatoria es:

```text
NAVBAR
────────────────────────────────────────────────────

TOC │ PORTFOLIO / CONTENIDO
TOC │
TOC │
TOC │
```

La siguiente geometría está prohibida:

```text
NAVBAR
────────────────────────────────────────────────────
TOC / lista ocupando una fila completa superior
────────────────────────────────────────────────────
PORTFOLIO / CONTENIDO
```


> **Superado en v8.0:** la implementación manual del shell/TOC fue retirada. Quarto vuelve a controlar la cuadrícula y la posición del TOC de forma nativa.

---

## REQ-LAYOUT-013 — `#quarto-margin-sidebar` no debe reservar espacio

**Estado:** `SUPERADO`  
**Prioridad:** `P1`

En el layout actual no se utilizan contenidos de margin sidebar.

En desktop debe evitarse que:

```text
#quarto-margin-sidebar
.margin-sidebar
.quarto-margin-sidebar
```

reserven ancho o alto adicional.

Se pueden ocultar mientras se preserve:

```text
#quarto-sidebar-toc-left
```

como navegación lateral funcional.


> **Superado en v8.0:** la implementación manual del shell/TOC fue retirada. Quarto vuelve a controlar la cuadrícula y la posición del TOC de forma nativa.

---



# 23J. Corrección definitiva del bloque lateral — v7.9

## REQ-LAYOUT-014 — El bloque completo del TOC comienza exactamente en `left: 0`

**Estado:** `SUPERADO`  
**Prioridad:** `P0`

En desktop, el bloque que contiene la navegación izquierda debe comenzar en la coordenada física:

```text
x = 0 px
```

del viewport.

El contenedor obligatorio es:

```text
#quarto-sidebar-toc-left
```

con:

```css
position: fixed;
left: 0;
top: var(--header-height);
bottom: 0;

margin-left: 0;
padding-left: 0;
```

El propio `#TOC` también debe utilizar:

```css
margin-left: 0;
padding-left: 0;
```

### Regla

La distancia entre:

```text
borde izquierdo del navegador
```

y:

```text
borde exterior del bloque lateral
```

debe ser:

```text
0 px
```

La jerarquía interna puede utilizar indentación en subtítulos y subsubtítulos, pero **esa indentación ocurre dentro del bloque**, no desplazando el bloque completo.


> **Superado en v8.0:** la implementación manual del shell/TOC fue retirada. Quarto vuelve a controlar la cuadrícula y la posición del TOC de forma nativa.

---

## REQ-LAYOUT-015 — El TOC desktop nunca puede volver al flujo vertical

**Estado:** `SUPERADO`  
**Prioridad:** `P0`

En resoluciones desktop (`>= 992 px`) el TOC debe permanecer:

```css
position: fixed;
```

y no puede formar una fila superior antes de `main.content`.

Geometría correcta:

```text
NAVBAR
────────────────────────────────────────────────────────

TOC │ PORTFOLIO / CONTENIDO
TOC │
TOC │
TOC │
```

Geometría prohibida:

```text
NAVBAR
────────────────────────────────────────────────────────
TOC ocupando una fila superior completa
────────────────────────────────────────────────────────
PORTFOLIO / CONTENIDO
```


> **Superado en v8.0:** la implementación manual del shell/TOC fue retirada. Quarto vuelve a controlar la cuadrícula y la posición del TOC de forma nativa.

---

## REQ-DIAG-001 — Causas conocidas de TOC desplazado o ubicado arriba

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Si la lista izquierda aparece separada del borde o encima del contenido, se deben revisar estas causas **antes de rediseñar la página**.

### Causa 1 — Se está modificando el wrapper incorrecto

Con:

```yaml
toc-location: left
```

Quarto puede generar:

```text
#quarto-sidebar-toc-left
```

para el TOC izquierdo y:

```text
#quarto-margin-sidebar
```

para la columna de margen.

Aplicar `position: fixed` al segundo en vez del primero puede dejar el TOC real dentro del flujo normal.

**Síntoma:**

```text
lista arriba
contenido debajo
```

### Causa 2 — `position: fixed` no está llegando al wrapper real

Una regla anterior, Bootstrap o Quarto puede dejar:

```css
position: static;
position: relative;
```

en el wrapper real.

Por eso v7.9 utiliza selectores específicos y `!important`.

### Causa 3 — Media query desktop no se está activando

El comportamiento lateral se aplica desde:

```css
@media (min-width: 992px)
```

Si:

- el viewport efectivo es menor;
- existe zoom muy alto;
- DevTools simula una pantalla angosta;
- otra media query posterior sobrescribe el layout;

el sitio puede usar el comportamiento móvil/tablet.

### Causa 4 — El grid de Quarto sigue reservando una fila o columna

Clases como:

```text
.page-columns
.sidebar
.margin-sidebar
```

pueden introducir:

```text
grid-column
margin
padding
justify-self
```

aunque el contenido parezca haber sido movido.

Por eso el shell desktop no debe depender del grid de Quarto para ubicar el TOC.

### Causa 5 — Bootstrap agrega padding al contenedor

Clases Bootstrap o estilos del theme pueden agregar:

```css
padding-left
margin-left
```

al wrapper, al `#TOC` o a un padre.

v7.9 normaliza explícitamente:

```css
margin-left: 0 !important;
padding-left: 0 !important;
```

en el bloque exterior.

### Causa 6 — Un `transform` cambia el sistema de referencia

Un ancestro con:

```css
transform: ...
```

puede alterar el comportamiento esperado de elementos posicionados.

El wrapper lateral debe utilizar:

```css
transform: none !important;
```

### Causa 7 — CSS anterior sigue en caché

Después de publicar una versión nueva, el navegador o GitHub Pages puede seguir mostrando CSS anterior.

Prueba requerida:

```text
Ctrl + F5
```

o limpiar caché antes de concluir que la nueva regla no funciona.

### Causa 8 — Una regla posterior sobrescribe la corrección

En CSS, una regla posterior con mayor especificidad puede recuperar:

```text
padding
margin
position
display
```

no deseados.

Por eso la implementación vigente debe quedar al final de la cascada o eliminar reglas antiguas incompatibles.

---

## REQ-DIAG-002 — Orden de diagnóstico visual del TOC

**Estado:** `REQUERIDO`  
**Prioridad:** `P1`

Cuando exista un problema visual del sidebar, revisar en este orden:

```text
1. ¿Existe #quarto-sidebar-toc-left?
2. ¿Está position: fixed?
3. ¿Su left calculado es 0px?
4. ¿Su margin-left calculado es 0px?
5. ¿Su padding-left calculado es 0px?
6. ¿Su top coincide con la altura del navbar?
7. ¿#quarto-margin-sidebar está oculto?
8. ¿main.content comienza después del ancho del TOC?
9. ¿Está activa la media query >= 992px?
10. ¿Hay CSS antiguo en caché?
```

No se debe mover la lista arriba como workaround.

---



# 23K. Retorno al TOC nativo de Quarto — v8.0

## REQ-QUARTO-TOC-001 — Quarto controla la posición del TOC

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La posición de la lista izquierda debe ser gestionada por la implementación nativa de Quarto:

```yaml
toc: true
toc-location: left
```

No se permite posicionar manualmente estos elementos:

```text
#quarto-sidebar-toc-left
#quarto-content
.page-columns
main.content
```

mediante hacks de shell como:

```css
position: fixed;
display: block;
margin-left: <ancho sidebar>;
width: calc(100vw - <ancho sidebar>);
```

La razón es que Quarto ya sitúa `.sidebar.toc-left` en su grid de página. Sobrescribir ese grid fue la causa principal de que el TOC apareciera como una fila superior.

---

## REQ-QUARTO-TOC-002 — Expansión nativa del TOC

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La expansión de títulos/subtítulos debe utilizar:

```yaml
toc-expand: 1
```

Quarto administra automáticamente:

- sección activa;
- expansión contextual;
- colapso de niveles;
- scroll/responsividad del TOC.

El JavaScript propio no debe reconstruir el árbol del TOC ni reemplazar `#TOC`.

---

## REQ-QUARTO-LAYOUT-001 — `page-layout: full` para ocupar el ancho disponible

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Se utiliza:

```yaml
page-layout: full
```

Quarto debe ampliar la región de contenido automáticamente hacia regiones no utilizadas, manteniendo ocupado el lado izquierdo cuando existe `toc-location: left`.

---

## REQ-QUARTO-GRID-001 — Anchuras mediante el grid oficial de Quarto

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La adaptación horizontal se realiza mediante:

```yaml
grid:
  sidebar-width: 300px
  body-width: 1600px
  margin-width: 100px
  gutter-width: 0.75rem
```

Estos valores pueden ajustarse, pero el método debe seguir siendo el `grid` oficial de Quarto en vez de reposicionar wrappers mediante CSS.

---

## REQ-QA-006 — Regression test del layout lateral

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El proyecto incluye:

```text
tests/native-toc-regression.html
tests/run_layout_regression.py
```

La prueba debe ejecutarse al menos en:

```text
1920 px
1440 px
1100 px
900 px
```

En desktop debe comprobar:

```text
TOC visible
TOC ancho < 40% viewport
TOC a la izquierda del contenido
TOC y contenido no apilados verticalmente
contenido > 45% viewport
```

En 900 px debe comprobar la respuesta móvil.

---

## REQ-QA-007 — Diagnóstico sobre la página Quarto real

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Añadiendo:

```text
?layout-debug=1
```

a cualquier URL renderizada, el sitio debe mostrar un panel PASS/FAIL con la geometría real del DOM.

Ejemplo:

```text
portfolio.html?layout-debug=1
```

El panel debe informar:

- existencia de `#quarto-sidebar-toc-left`;
- rectángulo del sidebar;
- rectángulo de `main.content`;
- `grid-column` y `grid-row` calculados;
- `display` del shell;
- si TOC y contenido están lado a lado;
- PASS o FAIL.

---

## REQ-QA-008 — Comparación con la implementación antigua funcional

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

El estilo del TOC de v8.0 recupera deliberadamente el enfoque de v6:

```text
#TOC sticky
estilos solo sobre #TOC y sus links
sin cambiar el wrapper lateral
sin cambiar la cuadrícula Quarto
```

Esta comparación debe conservarse en `TOC_DIAGNOSTICS.md` para evitar reintroducir el error.

---



# 23L. Contrato geométrico verificable — v8.1

## REQ-LAYOUT-020 — `page-start` debe coincidir con el borde físico izquierdo

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El diagnóstico real de v8.0 mostró:

```text
viewport.width = 2560 px
toc.left       = 293 px
```

El origen es el comportamiento nativo actual de Quarto:

```css
.sidebar.toc-left {
    grid-column: page-start / body-start;
}
```

La línea `page-start` del grid nativo estaba ubicada dentro de una composición centrada.

En v8.1 se conserva la semántica de Quarto, pero se redefine el grid raíz para que:

```text
page-start = screen-start = x 0 px
```

La primera columna es el TOC.

---

## REQ-LAYOUT-021 — Grid desktop de dos regiones con líneas Quarto

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

En desktop, `#quarto-content.page-columns` debe utilizar líneas nombradas compatibles con Quarto:

```text
[screen-start page-start]
        TOC
[body-start]
        pequeño gap
[body-content-start]
        CONTENIDO
[body-content-end screen-end]
```

Implementación conceptual:

```css
grid-template-columns:
  [screen-start screen-start-inset page-start page-start-inset]
    var(--portfolio-toc-width)
  [body-start-outset body-start]
    var(--portfolio-toc-gap)
  [body-content-start]
    minmax(0, 1fr)
  [body-content-end body-end body-end-outset
   page-end-inset page-end screen-end-inset screen-end];
```

Esto permite que las reglas internas de Quarto continúen ubicando:

```text
.sidebar.toc-left
.content
```

sin `position: fixed` y sin crear una fila superior.


> **Actualización v8.2:** la intención geométrica se conserva, pero la implementación puramente CSS no ganó la cascada del HTML real. La geometría final desktop pasa a ser aplicada y verificada por runtime JavaScript.

---

## REQ-LAYOUT-022 — Selector real del TOC debe detectarse dinámicamente

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El test no debe asumir que existe:

```text
#quarto-sidebar-toc-left
```

porque el HTML observado en v8.0 reportó:

```json
"sidebar": false,
"toc": true
```

El detector debe buscar, en este orden:

```text
#TOC.sidebar.toc-left
nav#TOC.toc-left
.sidebar.toc-left
#quarto-sidebar-toc-left
```

---

## REQ-QA-006 — Contrato numérico del TOC

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

En desktop, `?layout-debug=1` solo debe mostrar `PASS` si:

```text
abs(toc.left) <= 2 px
toc margin-left <= 1 px
toc padding-left <= 1 px

0 <= main.left - toc.right <= 28 px

-1 <= viewport.right - main.right <= 32 px
```

También debe verificar que TOC y contenido estén lado a lado y no apilados.

---

## REQ-NAVBAR-002 — Contrato numérico del navbar

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

En desktop, el test solo debe pasar si:

```text
header.top <= 1 px
navbar.top <= 1 px
navbar.height <= 54 px
```

y:

```text
#quarto-content.top - #quarto-header.bottom <= 2 px
```

La altura objetivo actual es:

```text
48 px
```

---

## REQ-QA-007 — Debug visual por colores

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Con:

```text
?layout-debug=1
```

se deben dibujar:

```text
TOC     → borde rojo
CONTENT → borde verde
NAVBAR  → borde azul
```

Además del panel JSON.

Esto permite confirmar visualmente qué caja está midiendo el test.

---



# 23M. Corrección geométrica runtime — v8.2

## REQ-LAYOUT-023 — Medir el layout Quarto antes de corregirlo

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Antes de aplicar la corrección desktop, JavaScript debe guardar la geometría original generada por Quarto en:

```javascript
window.__portfolioLayoutTest.baseline
```

Esto permite comparar objetivamente:

```text
ANTES → Quarto nativo
DESPUÉS → geometría corregida
```

El caso real que motivó v8.2 fue:

```text
viewport = 2560 px
toc.left = 292.5 px
main.right gap = 287.5 px
header.top = 53 px
```

---

## REQ-LAYOUT-024 — Corrección desktop aplicada al elemento real `#TOC`

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

En desktop, el propio:

```text
#TOC
```

debe actuar como bloque lateral.

La corrección se aplica mediante JavaScript después del render de Quarto:

```text
position: fixed
left: 0
top: altura navbar
bottom: 0
```

No se debe volver a depender de que exista:

```text
#quarto-sidebar-toc-left
```

---

## REQ-LAYOUT-025 — Main ocupa viewport restante después del TOC

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

`main.content` debe ocupar:

```text
TOC + gap → borde derecho
```

La corrección runtime debe aplicar:

```text
grid-column: screen-start / screen-end
margin-left: tocWidth + gap
margin-right: rightGutter
max-width: none
```

El ancho no depende de:

```text
body-width: 1600px
```

para la geometría final desktop.

---

## REQ-NAVBAR-003 — Navbar runtime fijo en `top: 0`

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

En desktop:

```text
#quarto-header
```

se corrige después del render a:

```text
position: fixed
top: 0
left: 0
right: 0
height: 48px
```

y `body` reserva exactamente esa altura mediante `padding-top`.

El objetivo es eliminar el caso medido:

```text
header.top = 53 px
navbar.top = 53 px
```

---

## REQ-QA-008 — Test compara baseline y resultado corregido

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El panel:

```text
?layout-debug=1
```

debe incluir:

```text
baseline
runtimeValues
rects
measurements
checks
```

Se considera especialmente útil comprobar:

```text
baseline.rects.toc.left  ≈ 292.5   (ejemplo real)
rects.toc.left           ≈ 0       (resultado esperado)
```

---

## REQ-QA-009 — Modo A/B sin corrección

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Para diagnosticar Quarto sin la reparación runtime se puede abrir:

```text
?layout-debug=1&layout-fix=0
```

En ese modo:

```text
Quarto se mide sin modificar
```

Mientras que:

```text
?layout-debug=1
```

aplica la corrección y luego mide.

---

## REQ-QA-010 — Reaplicar geometría después de ajustes tardíos

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

La geometría debe reaplicarse:

```text
al iniciar
después de ~80 ms
después de ~400 ms
al cambiar el tamaño de ventana
```

para evitar que scripts posteriores de Quarto/Bootstrap restituyan posiciones anteriores.

---



# 23N. Eliminación del bloque blanco residual — v8.3

## REQ-LAYOUT-026 — El TOC debe salir físicamente del slot Quarto original

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

La prueba v8.2 confirmó que la corrección geométrica principal funciona:

```text
toc.left       = 0 px
header.top     = 0 px
navbar.top     = 0 px
contentGap     = 14.4 px
fixApplied     = true
```

Sin embargo, visualmente permaneció un bloque blanco sobre la zona izquierda del contenido.

En v8.3 el propio elemento:

```text
#TOC
```

se conserva, pero se mueve a un nuevo contenedor de nivel `body`:

```text
#portfolio-toc-shell
```

De este modo deja de participar físicamente en el slot/grid original de Quarto.

---

## REQ-LAYOUT-027 — Shell lateral independiente del grid Quarto

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

En desktop:

```text
#portfolio-toc-shell
```

debe ser:

```css
position: fixed;
left: 0;
top: altura-navbar;
bottom: 0;
```

El shell controla:

```text
ancho
scroll vertical
background
borde derecho
z-index
```

El `#TOC` permanece dentro de este shell y mantiene sus enlaces/clases nativas.

---

## REQ-LAYOUT-028 — El slot TOC original no puede pintar sobre el contenido

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

Después de mover `#TOC`, cualquier ancestro original que quede vacío debe marcarse como:

```text
data-portfolio-stale-toc-slot="empty"
```

y ocultarse.

Si un wrapper no está vacío pero pertenece a la cadena original, debe marcarse como:

```text
data-portfolio-stale-toc-slot="wrapper"
```

y no puede pintar fondo/borde/sombra ni interceptar eventos sobre el cuerpo.

---

## REQ-LAYOUT-029 — El contenido debe pintar por encima de slots residuales

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

`main.content` debe utilizar en desktop:

```css
position: relative;
z-index: 2;
background: var(--page-bg);
```

El TOC shell permanece por encima mediante un `z-index` mayor.

Esto evita el patrón reportado en Quarto donde un bloque vertical asociado al TOC izquierdo cubre texto de contenido ancho.

---

## REQ-QA-011 — El right gap debe medirse contra `clientWidth`

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El test anterior calculaba:

```javascript
window.innerWidth - main.right
```

pero `innerWidth` incluye el ancho de la scrollbar vertical.

En la prueba real:

```text
window.innerWidth             = 2560
documentElement.clientWidth   = 2545
scrollbar                     = 15 px
main.right                    = 2525
```

Por tanto el gap real de layout era:

```text
2545 - 2525 = 20 px
```

y no `35 px`.

Desde v8.3:

```javascript
rightGap = document.documentElement.clientWidth - main.right
```

---

## REQ-QA-012 — Detectar elementos que cubren el inicio del main

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P0`

El test debe utilizar:

```javascript
document.elementsFromPoint(...)
```

en varios puntos dentro de la zona izquierda de `main.content`.

Debe reportar:

```text
occlusion.clear
occlusion.probes
```

y `PASS` exige:

```text
noMainOcclusion = true
```

Esto permite detectar exactamente el problema visual del bloque blanco aunque las coordenadas de `main` sean correctas.

---

## REQ-QA-013 — Guardar la cadena de ancestros original del TOC

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

La medición baseline debe registrar:

```text
tocAncestors
```

con:

```text
tag
id
class
rect
display
position
gridColumn
zIndex
backgroundColor
```

para identificar el wrapper que Quarto haya generado en cada versión.

---

## REQ-QUARTO-001 — No usar grid custom junto con toc-left salvo necesidad validada

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

Se elimina de `_quarto.yml` la configuración custom:

```yaml
grid:
  sidebar-width: ...
  body-width: ...
  margin-width: ...
  gutter-width: ...
```

La documentación e issues de Quarto muestran antecedentes de interacción problemática entre `toc-location: left`, layouts full/screen y configuraciones de grid.

La geometría final del proyecto se controla mediante el contrato runtime validado.

---



# 23N. Padding interno de la lista lateral — v8.4

## REQ-LAYOUT-030 — Padding interno de 20 px en el TOC

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

La geometría exterior validada en v8.3 **no debe cambiar**.

El bloque lateral continúa comenzando en:

```text
portal.left = 0 px
```

pero el contenido visual de la lista debe comenzar con un padding interno de:

```text
20 px desde el borde izquierdo
20 px desde el borde superior
```

Implementación requerida sobre el `#TOC` portalizado:

```css
#portfolio-toc-shell #TOC {
    padding-left: 20px;
    padding-top: 20px;
}
```

### Regla importante

El padding pertenece **al contenido interno de la lista**, no al shell exterior.

Por tanto:

```text
BORDE DE LA VENTANA
x = 0 px
│
│ #portfolio-toc-shell
│ └── 20 px → contenido del TOC
│
```

No se debe volver a introducir un margen exterior entre el navegador y el bloque lateral.

---

## REQ-QA-014 — Test del padding interno del TOC

**Estado:** `IMPLEMENTADO`  
**Prioridad:** `P1`

El test `?layout-debug=1` debe mantener:

```text
toc.left ≈ 0 px
```

porque la caja `#TOC` sigue comenzando en el borde del portal, pero sus estilos calculados deben cumplir:

```text
padding-left ≈ 20 px
padding-top  ≈ 20 px
```

Criterio de aceptación:

```text
abs(toc.padding-left - 20px) <= 1px
abs(toc.padding-top  - 20px) <= 1px
```

Esto debe pasar sin modificar:

```text
contentGapPx
rightGapPx
navbarTopPx
noMainOcclusion
```

---


# 24. Requisitos pendientes conocidos

Esta sección representa trabajo todavía no terminado.

| ID | Requisito | Estado | Prioridad |
|---|---|---|---|
| REQ-PEND-001 | Reemplazar placeholders por fotografías reales | PENDIENTE | P1 |
| REQ-PEND-002 | Agregar email público | PENDIENTE | P1 |
| REQ-PEND-003 | Agregar GitHub público | PENDIENTE | P1 |
| REQ-PEND-004 | Agregar LinkedIn público | PENDIENTE | P1 |
| REQ-PEND-005 | Agregar ORCID si corresponde | PENDIENTE | P2 |
| REQ-PEND-006 | Agregar Google Scholar si corresponde | PENDIENTE | P2 |
| REQ-PEND-007 | Incorporar CV Research PDF | PENDIENTE | P2 |
| REQ-PEND-008 | Incorporar CV Engineering PDF | PENDIENTE | P2 |
| REQ-PEND-009 | Revisar alt text de imágenes | PENDIENTE | P1 |
| REQ-PEND-010 | Optimizar imágenes finales | PENDIENTE | P1 |
| REQ-PEND-011 | Revisión WCAG formal | VALIDAR | P1 |
| REQ-PEND-012 | Prueba final desktop Chrome/Firefox/Edge | VALIDAR | P1 |
| REQ-PEND-013 | Prueba final móvil | VALIDAR | P1 |
| REQ-PEND-014 | Revisar información confidencial antes de publicar | PENDIENTE | P0 |

---

# 25. Criterios de aceptación para futuras versiones

Antes de considerar una nueva versión estable, comprobar como mínimo:

## Navegación

- [ ] Portfolio abre correctamente.
- [ ] CV abre correctamente.
- [ ] Contact abre correctamente.
- [ ] Project Pages abre correctamente.
- [ ] Links internos funcionan.
- [ ] Sidebar refleja correctamente los headings.
- [ ] Sidebar marca la sección actual.
- [ ] Sidebar hace auto-scroll cuando corresponde.

## Visual

- [ ] Modo claro funciona.
- [ ] Modo oscuro funciona.
- [ ] El icono Sol/Luna corresponde al estado.
- [ ] Paleta mantiene contraste.
- [ ] Títulos no se cortan.
- [ ] Placeholders/imágenes no desbordan.

## Animación

- [ ] Reveal funciona.
- [ ] El contenido es visible antes de inicializar JS.
- [ ] Si JS falla, el contenido continúa visible.
- [ ] Reduced Motion desactiva animaciones.
- [ ] Compact mode funciona.
- [ ] Preferencias se recuperan sin romper la página.

## Responsive

- [ ] Desktop ≥ 1200 px.
- [ ] Laptop ~ 1024 px.
- [ ] Tablet ~ 768 px.
- [ ] Smartphone ~ 390 px.
- [ ] Navbar no tapa contenido.
- [ ] Controles no chocan con menú móvil.

## Quarto

- [ ] `_quarto.yml` válido.
- [ ] Front matter YAML válido.
- [ ] `quarto render` termina sin error.
- [ ] `_site` se genera.
- [ ] Mermaid renderiza correctamente.
- [ ] Bloques de código funcionan.

## GitHub

- [ ] Workflow inicia.
- [ ] Build termina en verde.
- [ ] Artifact Pages se sube.
- [ ] Deploy termina en verde.
- [ ] URL pública carga.
- [ ] No existen links rotos.

---

# 26. Plantilla para agregar un requisito nuevo

Copiar y editar:

```markdown
## REQ-AREA-XXX — Nombre del requisito

**Estado:** `PROPUESTO`  
**Prioridad:** `P1`

### Descripción

Explicar qué se quiere implementar o modificar.

### Comportamiento esperado

- ...
- ...
- ...

### Archivos afectados

- `...`
- `...`

### Restricciones

- ...
- ...

### Criterios de aceptación

- [ ] ...
- [ ] ...
- [ ] ...

### Notas

...
```

---

# 27. Plantilla para solicitar un cambio

Ejemplo:

```markdown
## CAMBIO-001 — Modificar color de acento

Requisito relacionado:
REQ-UI-002
REQ-UI-003

Estado:
MODIFICAR

Situación actual:
Acento claro #D63230
Acento oscuro #FF615E

Nuevo requisito:
Usar azul técnico como acento.

Opciones propuestas:
#176B9A
#087EAE

Debe mantenerse:
- sidebar activo;
- contraste;
- modo claro/oscuro;
- animaciones;
- jerarquía Swiss.

Validación:
- [ ] modo claro
- [ ] modo oscuro
- [ ] sidebar
- [ ] links
- [ ] controles
```

---

# 28. Registro de cambios de requisitos

Utilizar esta tabla para mantener trazabilidad.

| Versión | Fecha | Cambio | Requisitos afectados | Estado |
|---|---|---|---|---|
| v5.2 | — | Base Quarto y contenido técnico | múltiples | Base |
| v6 | 2026-09-11 | Integración Swiss Research | UI / NAV / ANIM / CTRL | IMPLEMENTADO |
| v6 | 2026-09-11 | Scroll-spy y auto-scroll lateral | REQ-NAV-003/004/005 | IMPLEMENTADO |
| v6 | 2026-09-11 | Reveal fail-safe | REQ-ANIM-004/005 | IMPLEMENTADO |
| v6 | 2026-09-11 | Controles por iconos | REQ-CTRL-001 a 006 | IMPLEMENTADO |
| v7 | 2026-09-11 | Home convertida en resumen profesional | REQ-HOME-001/002/003 | IMPLEMENTADO |
| v7 | 2026-09-11 | TOC acordeón contextual | REQ-NAV-008 | IMPLEMENTADO |
| v7 | 2026-09-11 | Swiss Controls al extremo derecho | REQ-CTRL-007 | IMPLEMENTADO |
| v7 | 2026-09-11 | Contact distribuido en cards/grids | REQ-CONTACT-004/005 | IMPLEMENTADO |
| v7 | 2026-09-11 | Requirements Markdown obligatorio en cada cambio | REQ-DOC-001 | IMPLEMENTADO |
| v7.1 | 2026-09-11 | Corregido render de Home y Contact mediante Fenced Divs | REQ-RENDER-001/002 | IMPLEMENTADO |
| v7.1 | 2026-09-11 | Nombre superior enlaza a Home | REQ-NAV-009 | IMPLEMENTADO |
| v7.1 | 2026-09-11 | Portfolio superior enlaza al portafolio técnico | REQ-NAV-010 | IMPLEMENTADO |
| v7.1 | 2026-09-11 | Acordeón TOC robusto y accesible | REQ-NAV-011 | IMPLEMENTADO |
| v7.2 | 2026-09-11 | TOC reconstruido desde headings reales con details/summary | REQ-NAV-012/013/014/015/016 | IMPLEMENTADO |
| v7.2 | 2026-09-11 | Consolidación de CSS/JS y limpieza de archivos | REQ-CLEAN-001/002/003 | IMPLEMENTADO |
| v7.2 | 2026-09-11 | Prueba de navegación real preparada; sandbox bloquea Chromium | REQ-QA-005 | VALIDAR |
| v7.3 | 2026-09-11 | Jerarquía fija de seis títulos para el TOC del Portfolio | REQ-PORTFOLIO-TOC-001/002/003 | IMPLEMENTADO |
| v7.3 | 2026-09-11 | Project Pages reemplaza títulos enlazados por botones | REQ-PROJ-004/005 | IMPLEMENTADO |
| v7.4 | 2026-09-11 | Cuerpo ampliado y page-layout full | REQ-LAYOUT-001 | IMPLEMENTADO |
| v7.4 | 2026-09-11 | Reducción global de escala tipográfica | REQ-TYPE-001 | IMPLEMENTADO |
| v7.4 | 2026-09-11 | Diagrama y análisis de estructura de páginas | REQ-ARCH-005/006/007 | IMPLEMENTADO / VALIDAR |
| v7.5 | 2026-09-11 | Eliminación de Project Pages y Portfolio como índice único | REQ-ARCH-007/008, REQ-NAV-017, REQ-PORTFOLIO-NAV-001 | IMPLEMENTADO |
| v7.5 | 2026-09-11 | Contenido realmente full-width y gutters responsive | REQ-LAYOUT-002/003/004/005 | IMPLEMENTADO |
| v7.6 | 2026-09-12 | TOC llevado al borde izquierdo y navbar compactado arriba | REQ-LAYOUT-006/007, REQ-NAVBAR-001 | IMPLEMENTADO |
| v7.6 | 2026-09-12 | Eliminación defensiva de Project Pages y buscador | REQ-NAV-018, REQ-SEARCH-001 | IMPLEMENTADO |
| v7.6 | 2026-09-12 | Botones de detalle verificados en los 8 proyectos | REQ-PORTFOLIO-NAV-002 | IMPLEMENTADO |
| v7.6 | 2026-09-12 | Dos botones de descarga al inicio del CV | REQ-CV-010 | IMPLEMENTADO |
| v7.7 | 2026-09-12 | Eliminación de columna invisible izquierda de Quarto; TOC fijado a viewport x=0 | REQ-LAYOUT-008/009/010 | IMPLEMENTADO |
| v7.8 | 2026-09-12 | TOC fijado usando el wrapper real `#quarto-sidebar-toc-left` | REQ-LAYOUT-011/012/013 | IMPLEMENTADO |
| v7.9 | 2026-09-12 | Bloque TOC con left/margin/padding izquierdo en 0 px y diagnóstico explícito | REQ-LAYOUT-014/015, REQ-DIAG-001/002 | IMPLEMENTADO / REQUERIDO |
| v8.0 | 2026-09-12 | Retorno al TOC/layout nativo de Quarto + tests de regresión y diagnóstico real | REQ-QUARTO-TOC-001/002, REQ-QUARTO-LAYOUT-001, REQ-QUARTO-GRID-001, REQ-QA-006/007/008 | IMPLEMENTADO |
| v8.1 | 2026-09-12 | Grid Quarto redefinido con page-start en x=0 y test geométrico numérico | REQ-LAYOUT-020/021/022, REQ-QA-006/007, REQ-NAVBAR-002 | IMPLEMENTADO |
| v8.2 | 2026-09-12 | Corrección runtime del TOC/navbar con comparación baseline/post-fix y modo A/B | REQ-LAYOUT-023/024/025, REQ-NAVBAR-003, REQ-QA-008/009/010 | IMPLEMENTADO |
| v8.3 | 2026-09-12 | TOC portalizado fuera del grid Quarto, limpieza de slot blanco, test de oclusión y right-gap corregido por clientWidth | REQ-LAYOUT-026/027/028/029, REQ-QA-011/012/013, REQ-QUARTO-001 | IMPLEMENTADO |
| v8.4 | 2026-09-12 | Padding interno TOC 20 px izquierda/superior sin alterar shell x=0 | REQ-LAYOUT-030, REQ-QA-014 | IMPLEMENTADO |
| próxima | — | — | — | — |

---

# 29. Requisitos que no deben perderse accidentalmente

Este bloque sirve como resumen mínimo antes de modificar el código.

```text
[CRÍTICO]

1. Quarto continúa siendo la base del sitio.
2. El contenido .qmd debe permanecer separado de CSS/JS.
3. Portfolio / CV / Contact / Project Pages deben seguir funcionando.
4. Sidebar izquierda debe ser jerárquica.
5. Sidebar debe seguir la sección durante scroll.
6. Sidebar debe hacer auto-scroll para mantener visible el elemento activo.
7. Deben existir modo claro y oscuro.
8. Debe existir botón de Reduced Motion.
9. Debe existir modo compacto.
10. Las preferencias no pueden romper la página si localStorage falla.
11. Animaciones deben ser fail-safe.
12. Si JS falla, el contenido debe permanecer visible.
13. Diseño debe mantener carácter técnico/académico.
14. Tesis debe mantener organización Objetivo 1 → Objetivo 2 → Objetivo 3.
15. GitHub Pages debe seguir desplegándose mediante GitHub Actions.
16. El sitio debe funcionar en desktop y adaptarse a móvil.
17. Mermaid y código deben continuar soportados.
18. Las imágenes reales deben poder reemplazar placeholders sin rediseñar la página.
19. Cada cambio debe actualizar PORTFOLIO_REQUIREMENTS.md.
20. Los Swiss Controls deben permanecer agrupados al extremo derecho.
21. El TOC debe mostrar títulos principales y expandir solo el grupo activo.
22. La página principal debe seguir siendo un resumen profesional; el detalle técnico vive en portfolio.qmd y projects/.
23. Contact debe conservar una distribución visual por cards/grids y no volver a una lista simple.
24. Carlos Moreno Rojas en el navbar debe enlazar siempre a Home.
25. Portfolio en el navbar debe enlazar al portafolio técnico.
26. Home y Contact deben usar sintaxis de componentes segura para Quarto/Pandoc.
27. Nunca debe aparecer HTML literal como código visible.
28. El TOC lateral debe expandir automáticamente el grupo que contiene el subtítulo visible usando la funcionalidad nativa de Quarto.
29. El TOC no debe reconstruirse mediante JavaScript propio.
30. La expansión principal debe usar `toc-expand: 1` de Quarto.
31. Quarto debe conservar el control del wrapper y de la cuadrícula del TOC.
32. CSS y JS deben mantenerse consolidados, sin implementaciones históricas duplicadas.
33. El TOC de portfolio.qmd debe tener exactamente seis títulos principales, en el orden definido por REQ-PORTFOLIO-TOC-001.
34. Teaching, Leadership, Meldic, Skills, Engineering approach y Contact no deben aparecer como títulos del TOC técnico.
35. Project Pages debe usar botones para abrir proyectos; los nombres de proyecto no deben ser hipervínculos azules.
36. El cuerpo de contenido debe aprovechar la zona derecha disponible en desktop.
37. Los títulos deben usar una escala moderada y no dominar el viewport.
38. SITE_STRUCTURE.md debe mantenerse como diagrama vivo de arquitectura.
39. Home, Portfolio y Project Page deben respetar el aumento progresivo de detalle.
40. Portfolio debe ser el único índice general de proyectos.
41. No debe existir Project Pages como nivel intermedio ni enlace de navbar.
42. Cada proyecto del Portfolio debe tener acceso directo a su página detallada.
43. El layout horizontal debe utilizar `page-layout: full` y el `grid` oficial de Quarto.
44. No se deben reposicionar manualmente `#quarto-sidebar-toc-left`, `.page-columns` o `#quarto-content`.
45. El navbar debe comenzar en la parte superior sin una banda vacía.
46. No debe existir ningún acceso a Project Pages.
47. Cada proyecto del Portfolio debe terminar con su botón de detalle.
48. El CV debe comenzar con dos botones de descarga y no tener sección Downloads al final.
49. El sitio no debe mostrar buscador.
50. Debe existir un regression test del TOC en varias resoluciones.
51. Debe poder probarse el layout real añadiendo `?layout-debug=1`.
52. Antes de alterar el shell, comparar con la implementación v6 que funcionaba.
53. El TOC debe ser nativo de Quarto: `toc-location: left` + `toc-expand: 1`.
54. El shell lateral debe seguir en x=0; el contenido interno del TOC usa padding-left:20px y padding-top:20px.
```

---

# 30. Archivos que controlan cada sistema

| Sistema | Archivo principal |
|---|---|
| Configuración Quarto | `_quarto.yml` |
| Portfolio principal | `index.qmd` |
| CV | `cv.qmd` |
| Contact | `contact.qmd` |
| Tesis | `projects/thesis.qmd` |
| CYBATHLON | `projects/cybathlon.qmd` |
| CandelStim | `projects/candel.qmd` |
| Borealis | `projects/borealis.qmd` |
| Preservación | `projects/organ-preservation.qmd` |
| U-Net | `projects/unet.qmd` |
| FPGA | `projects/fpga.qmd` |
| Vscan | `projects/vscan.qmd` |
| Diseño global | `assets/site.css` |
| Animaciones, controles y diagnóstico de layout | `assets/site-scripts.html` |
| Preview local | `portfolio_preview.html` |
| Deploy | `.github/workflows/publish.yml` |
| Imágenes | `assets/images/` |
| Diagnóstico TOC | `TOC_DIAGNOSTICS.md` |
| Test layout | `tests/run_layout_regression.py` |

---

# 31. Filosofía para futuras modificaciones

Una nueva funcionalidad debería incorporarse respetando este orden:

```text
1. Definir requisito
2. Determinar archivo responsable
3. Mantener comportamiento actual no relacionado
4. Implementar la menor modificación posible
5. Probar localmente
6. Validar Quarto
7. Validar desktop
8. Validar móvil
9. Validar modo claro
10. Validar modo oscuro
11. Validar Reduced Motion
12. Validar GitHub Pages
13. Actualizar este documento
```

El portafolio debe evolucionar mediante **cambios incrementales**, no mediante reconstrucciones completas que eliminen funcionalidades ya validadas.

---

# 32. Estado de referencia

La versión descrita por este documento se considera la referencia funcional:

```text
Carlos Moreno Portfolio
Version: v8.4 Swiss Research / Native Quarto TOC
Base: v6 Swiss Research / v5.2 content architecture
Style: Swiss Research
Framework: Quarto
Hosting target: GitHub Pages
Navigation: Navbar + dynamic left TOC
Themes: Light + Dark
Animations: Scroll reveal, fail-safe
Accessibility option: Reduced Motion
Density option: Compact Mode
Deployment: GitHub Actions
```

Cuando se cree una versión nueva, actualizar:

```text
Versión:
Fecha:
Requisitos agregados:
Requisitos modificados:
Requisitos eliminados:
Pruebas realizadas:
```
