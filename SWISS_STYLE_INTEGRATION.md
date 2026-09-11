# Swiss Research integration — v6

This version is based on the uploaded **v5.2**. The content and project structure were preserved.

## Integrated from the approved Swiss Research prototype

- Swiss light palette:
  - `#F7F5EF` background
  - `#ECE9E0` surfaces
  - `#111111` primary text
  - `#66635D` secondary text
  - `#CBC7BC` borders
  - `#D63230` red accent
- Swiss dark palette:
  - `#141414` background
  - `#1E1E1E` surfaces
  - `#F1EFE8` primary text
  - `#A7A39A` secondary text
  - `#383633` borders
  - `#FF615E` red accent
- Editorial Swiss typography and strong section rules.
- Square technical image placeholders from v5.2 retained.
- Light / dark icon.
- Compact-view icon.
- Reduced-motion icon.
- Reveal animation copied conceptually from the working Swiss prototype.
- Animation is fail-safe: content is visible if JavaScript does not run.
- Left TOC follows the currently viewed heading.
- Left TOC automatically scrolls to keep the active link visible.
- The same behavior is applied globally to Portfolio, CV, Contact and individual project pages.

## Files added / changed

- `_quarto.yml`
- `assets/site.css`
- `assets/site-scripts.html`
- `portfolio_preview.html`

All `.qmd` project content from v5.2 remains unchanged.
