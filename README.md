# Carlos Moreno Rojas — Engineering Portfolio

Quarto-based portfolio for biomedical engineering, electrical engineering, research and technical projects.

## Current version

**v7.2 — Swiss Research**

The current architecture separates:

```text
Home                 → index.qmd
Technical Portfolio  → portfolio.qmd
CV                   → cv.qmd
Contact              → contact.qmd
Project index        → projects/index.qmd
Individual projects  → projects/*.qmd
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
- `CONTENT_TO_ADD.md` — images/data/content still to add.
- `GITHUB_PAGES_GUIDE.md` — deployment guide.
- `BUILD_VALIDATION.md` — validation of the current version only.

## Development rule

Every functional, visual, structural or navigation change must also update:

```text
PORTFOLIO_REQUIREMENTS.md
```
