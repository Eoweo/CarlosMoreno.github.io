# Carlos Moreno Rojas — Portfolio

Quarto-based engineering and biomedical research portfolio.

## Structure

- `index.qmd` — Home
- `projects/` — Individual project pages
- `research.qmd`
- `experience.qmd`
- `skills.qmd`
- `about.qmd`
- `cv.qmd`
- `contact.qmd`
- `assets/site.css`
- `.github/workflows/publish.yml`

## Local preview

Install Quarto:

https://quarto.org/

Then run:

```bash
quarto preview
```

## Publish with GitHub Pages

1. Create a GitHub repository.
2. Upload all files from this folder.
3. In GitHub: **Settings → Pages → Source → GitHub Actions**.
4. Push to the `main` branch.
5. The included workflow will render and deploy the site.

## Important before publishing

Replace placeholders in `contact.qmd`.

Add:
- project photographs;
- videos;
- diagrams;
- validated plots;
- public datasets;
- repository links;
- final CV PDFs.

See `CONTENT_TO_ADD.md`.


## Version 2 design

Simplified visual style, interactive preview tabs and previous/next navigation between pages.

## Version 3 design

Documentation-style layout:

- fixed / sticky section index on the left;
- active section highlighted while scrolling;
- long-form technical pages;
- image placeholders with the exact suggested image title centered in each slot;
- simplified visual styling inspired by electronics/computer technical documentation.


## Version 4

Added a complete long-form portfolio page with all major projects and experiences. See `portfolio.qmd` and `GITHUB_PAGES_GUIDE.md`.

## Version 5

- Working Portfolio / CV / Contact top navigation.
- Hierarchical left sidebar with technical-area titles and project / objective subtitles.
- Portfolio home is now the long-form technical page.
- CV and Contact have their own working content and side navigation.


## Version 5.1

- Sidebar hierarchy revised to match the requested documentation style.
- Top-level section names are uppercase/bold.
- Project/objective links are indented below each section.
- Same hierarchy applied to Portfolio, CV, Contact, Project Pages and detailed project pages.
- Light and dark themes enabled in Quarto.
- Interactive preview includes a persistent light/dark toggle.


## Version 5.3 — Swiss Research

This version applies the Swiss Research visual system across the complete Quarto portfolio.

- Swiss academic/editorial palette.
- Sharp, square geometry.
- Red accent and active sidebar state.
- Hierarchical left TOC preserved across all pages.
- Custom icon controls for compact mode, reduced motion and light/dark mode.
- Fail-safe JavaScript reveal animation: page content stays visible if JavaScript fails.
- Standalone `portfolio_preview.html` updated to the same Swiss visual language.
