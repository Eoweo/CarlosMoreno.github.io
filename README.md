# Carlos Moreno Rojas — Engineering Portfolio

Quarto-based portfolio for biomedical engineering, electrical engineering, research and technical projects.

## Current version

**v8.0 — Swiss Research / Native Quarto TOC**

The current architecture separates:

```text
Home                 → index.qmd
Technical Portfolio  → portfolio.qmd
CV                   → cv.qmd
Contact              → contact.qmd
Individual projects  → projects/*.qmd (opened from Portfolio)
Design               → assets/site.css
Interaction          → assets/site-scripts.html
Requirements         → PORTFOLIO_REQUIREMENTS.md
Deployment           → .github/workflows/publish.yml
```

## Navigation

The left navigation is rebuilt in the browser directly from the rendered `h1`, `h2` and `h3` headings.

It uses native HTML:

```html
<details>
<summary>
```

This avoids depending on Quarto's internal nested TOC markup.

Behavior:

- only main titles are shown normally;
- the group currently being viewed opens automatically;
- its subtitles appear;
- third-level headings appear only for the active second-level subsection;
- the exact active heading is marked in Swiss red;
- the sidebar scrolls automatically to keep the active item visible.

If JavaScript fails, Quarto's native TOC remains intact because it is replaced only after the custom TOC has been fully built.

## Display controls

Top-right controls:

- compact mode;
- reduced motion;
- light/dark mode.

## Local preview

With Quarto installed:

```bash
quarto preview
```

## GitHub Pages

1. Upload the project files to GitHub.
2. Go to **Settings → Pages**.
3. Choose **GitHub Actions**.
4. Push to `main`.
5. `.github/workflows/publish.yml` renders and deploys the site.

## Project documentation

- `PORTFOLIO_REQUIREMENTS.md` — mandatory living requirements specification.
- `SITE_STRUCTURE.md` — page map, information levels and redundancy analysis.
- `CONTENT_TO_ADD.md` — images/data/content still to add.
- `GITHUB_PAGES_GUIDE.md` — deployment guide.
- `BUILD_VALIDATION.md` — validation of the current version only.

## Development rule

Every functional, visual, structural or navigation change must also update:

```text
PORTFOLIO_REQUIREMENTS.md
```


## v7.3

- Portfolio TOC is fixed to six top-level technical categories.
- Existing projects are reorganized under those six categories.
- Non-project sections remain in `portfolio.qmd` but are excluded from the technical TOC.
- `Project Pages` uses Swiss-styled redirect buttons instead of linked blue project titles.


## v7.4

- User-facing pages use a wider `full` page layout.
- Main content can use up to 1180 px of horizontal body width.
- Swiss title sizes were reduced globally.
- `SITE_STRUCTURE.md` documents the current page architecture and highlights the overlap between Portfolio and Project Pages.
- No page was removed in this version.


## v7.5

- Removed the redundant `Project Pages` navigation layer.
- Deleted `projects/index.qmd`.
- Portfolio is now the only general technical index.
- Each summarized project in Portfolio includes an `Open detailed project` button.
- Desktop content now spans from Quarto's `body-start` grid line to `screen-end`.
- Responsive edge gutters use `clamp()` instead of large fixed margins.
- Technical media can use 100% of available width; prose keeps a character-based readability limit.


## v7.6

- Left TOC now starts near the physical left edge of the browser window.
- Navbar top spacing reduced and header height set to 52 px.
- Search disabled completely.
- No Project Pages access exists.
- All eight Portfolio projects end with an `Open detailed project` button.
- CV Downloads section removed.
- Research and Engineering CV download buttons are now placed at the beginning of the CV.
- Actual downloadable PDF files are included in `/downloads`.


## v7.7

- Removed Quarto's centered page-grid dependency from the desktop shell.
- Left TOC is physically fixed at `left: 0` of the browser viewport.
- Main content starts at the responsive TOC width and fills the remaining `100vw`.
- This specifically fixes the large blank band visible to the left of the TOC in v7.6.


## v7.8

- Corrected the Quarto wrapper used for the left TOC.
- Desktop left navigation now fixes `#quarto-sidebar-toc-left` / `.sidebar.toc-left`.
- The unrelated margin sidebar is prevented from reserving layout space.
- The TOC can no longer become a full-width row above the document on desktop.


## v7.9

- Desktop TOC uses Quarto's actual `#quarto-sidebar-toc-left` wrapper.
- The complete sidebar block is pinned to viewport `left: 0`.
- Sidebar wrapper and `#TOC` use `margin-left: 0` and `padding-left: 0`.
- The TOC cannot participate in normal vertical document flow on desktop.
- Requirements now document the known causes of the “sidebar above content / space on the left” bug.


## v8.0 — native Quarto TOC regression reset

- Restored the working v6 philosophy: Quarto owns the TOC/page grid.
- Uses `toc-location: left`, `toc-expand: 1`, `page-layout: full`.
- Uses official Quarto `grid` width configuration.
- Removed custom JS TOC reconstruction and wrapper positioning hacks.
- Added `tests/run_layout_regression.py`.
- Added actual-page diagnostics using `?layout-debug=1`.
- Added `TOC_DIAGNOSTICS.md`.


## v8.1

- The v8.0 runtime test revealed that current Quarto emits the TOC itself as `.sidebar.toc-left`; no `#quarto-sidebar-toc-left` wrapper was present.
- Quarto's default `page-start / body-start` placement caused a measured 293 px left offset at 2560 px viewport width.
- The root Quarto named grid is now redefined so `page-start` equals the physical left edge.
- No fixed-position sidebar is used.
- `?layout-debug=1` now has hard numeric pass/fail contracts for TOC x-position, content gap, right edge, navbar top and navbar height.


## v8.2

- Uses the actual measured Quarto output as baseline before applying layout repair.
- Keeps Quarto's native TOC content and behavior.
- Applies desktop geometry directly to `#TOC`, `main.content` and `#quarto-header` with inline `!important` properties.
- Adds A/B mode: `?layout-debug=1&layout-fix=0`.
- Normal test mode `?layout-debug=1` reports both baseline and post-fix geometry.
- Reapplies the geometry after short/long settle windows and on resize.


## v8.3

- The v8.2 A/B test proved the left/top geometry repair itself works.
- The remaining white block is treated as a stale Quarto TOC layout slot / occlusion issue.
- The real `#TOC` is now moved into a body-level `#portfolio-toc-shell` instead of only being fixed in its original grid slot.
- Empty original TOC wrappers are hidden and non-empty wrappers are neutralized behind the main content.
- Main content is layered above stale layout boxes.
- Right-edge testing now uses `document.documentElement.clientWidth`, excluding the vertical scrollbar.
- The debug test now probes for visual occlusion using `document.elementsFromPoint()`.
- Custom Quarto `grid:` widths were removed from `_quarto.yml`.


## v8.4

- Keeps the validated v8.3 TOC portal geometry unchanged.
- Adds 20 px internal left padding to the TOC list.
- Adds 20 px internal top padding to the TOC list.
- Runtime test now validates both 20 px padding values while still requiring the outer TOC geometry to remain at the viewport edge.


## v8.5 — Swiss Wipe animation

- Content reveal now matches the approved Swiss reference: horizontal `clip-path` wipe + opacity.
- `IntersectionObserver` is the primary scroll trigger; RAF scroll scanning is fallback only.
- Animations run per logical section/block rather than on every individual paragraph.
- Fail-safe visibility remains mandatory.
- System `prefers-reduced-motion` and the manual Reduced Motion control are both respected.
- `?animation-debug=1` provides live passive verification.
- `?animation-test=1` automatically scrolls to a pending real section and verifies transition start/end plus final computed styles.
- See `ANIMATION_DIAGNOSTICS.md`.


## v8.6

- Replaces IntersectionObserver reveal triggering with `requestAnimationFrame + getBoundingClientRect` on every scroll/resize.
- Uses the Web Animations API (`Element.animate`) for the Swiss wipe.
- Removes CSS transition instrumentation that could count the hide transition as a reveal.
- Adds a 450 ms watchdog and 1100 ms fail-visible timeout.
- Adds targeted test mode: `?animation-test=monitoring`.
- Keeps all v8.5 layout, TOC, navbar, content and CV behavior unchanged.


## v8.7 — Dynamic CV

This version keeps the validated layout / TOC / animation base from v8.6 and introduces:

- a more dynamic CV page built with hero, card and timeline sections;
- lighter section-title spacing (smaller gap below the top rule);
- moderate emoji / textual icon cues for faster reading.


## v8.8

- Reduced the Swiss rule-to-title spacing to `0.16rem`.
- Kept the CV in a visual card/timeline structure rather than a linear list.
- Replaced all CV emoji markers with self-contained monochrome vector icons using CSS SVG masks.
- Added vector download icons to both CV download buttons.
- Re-validated the Portfolio TOC against the exact six-title hierarchy documented in `PORTFOLIO_REQUIREMENTS.md`.
- No changes to TOC geometry, navbar, runtime portal, project content or Swiss Wipe animation.


## v8.9

- Portfolio sidebar now follows the approved screenshot exactly at the visible hierarchy level.
- `portfolio.qmd` uses `toc-depth: 2`; H3 items such as Monitoring are content-only and no longer appear in the sidebar.
- CV card/timeline design is preserved.
- Replaced fragile nested Pandoc fenced divs with explicit semantic HTML (`section`, `article`, `div`) to prevent literal `::: {.class}` compilation artifacts.
- Added a Pandoc render test that fails if fenced-div markup leaks into `cv.html`.
- No changes to the validated TOC portal geometry or reveal animation.


## v8.10

- Fixed the remaining CV rendering problem by wrapping every complex CV HTML block in explicit Pandoc raw-HTML fences (`{=html}`).
- Validation now uses plain `pandoc -f markdown`, matching the failure mode more closely.
- Technical Skills cards now use a compact `cv-skill-grid` variant with 132 px reference minimum height.
- Other CV cards keep their previous dimensions.
- Portfolio TOC hierarchy and validated layout/animation systems are unchanged.


## v8.11

- CV timeline/cards are explicitly left-aligned.
- Bold inline phrases in CV prose no longer become block elements, removing artificial line breaks.
- Education uses a fixed 120 px date column on desktop.
- Technical Skills cards are substantially shorter.
- Compact Mode was removed from UI, CSS, JS, localStorage behavior and tests.
- Reduced Motion was removed from UI, CSS, JS, animation branches and tests.
- Light/Dark is now the only Swiss display control.
- Portfolio TOC, runtime TOC portal and project content remain unchanged.


## v9.0 — Consolidated architecture

The public site now has four real content pages:

```text
Home
Portfolio
CV
Contact
```

Changes:

- Deleted all eight dedicated project `.qmd` pages.
- Consolidated their useful technical content into `portfolio.qmd`.
- Removed all project-detail buttons and internal links to deleted project files.
- Simplified Home to profile, current research, selected work and engineering areas.
- Simplified CV so it presents trajectory rather than duplicating the Portfolio.
- Removed Teaching / Leadership / Skills / Contact sections from the bottom of Portfolio because those belong to CV or Contact.
- Preserved legacy `/projects/...` URLs through static redirect-only HTML files to avoid 404s.
- Preserved Swiss layout, TOC portal, animations, responsive behavior and Light/Dark control.
