# Carlos Moreno Rojas — Engineering Portfolio

Quarto-based portfolio for biomedical engineering, electrical engineering, research and technical projects.

## Current version

**v7.8 — Swiss Research**

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
