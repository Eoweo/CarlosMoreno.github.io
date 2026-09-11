# Build validation — v7.2

## Configuration

- `_quarto.yml`: OK
- QMD files checked: 13
- QMD YAML errors: 0
- JavaScript syntax (`assets/site-scripts.html`): OK
- JavaScript syntax (`portfolio_preview.html`): OK
- CSS brace balance: OK

## Navigation implementation

- Custom TOC is generated from rendered `h1`, `h2`, `h3`: implemented
- Native `<details>/<summary>` used for main-group expansion: implemented
- Active group selection based on scroll position: implemented
- Exact active heading highlighting: implemented
- Contextual third level: implemented
- Internal sidebar auto-scroll: implemented
- Fallback to native Quarto TOC if custom build fails: implemented
- Fallback creation of `#TOC` container if Quarto does not emit one: implemented

## Cleanup

Removed historical validation files:

- `BUILD_VALIDATION_V6.md`
- `BUILD_VALIDATION_V7.md`
- `BUILD_VALIDATION_V7_1.md`

Removed obsolete style note:

- `SWISS_STYLE_INTEGRATION.md`

Removed unlinked legacy pages whose content is covered elsewhere:

- `about.qmd`
- `research.qmd`
- `experience.qmd`
- `skills.qmd`

Current root documentation is limited to:

- `README.md`
- `PORTFOLIO_REQUIREMENTS.md`
- `CONTENT_TO_ADD.md`
- `GITHUB_PAGES_GUIDE.md`
- `BUILD_VALIDATION.md`

## Browser validation

The construction environment blocks Chrome/Chromium navigation, including local files and localhost.

Therefore the final interactive test is intentionally marked:

**VALIDAR EN CHROME**

Use `portfolio_preview.html` or the rendered GitHub Pages site and confirm:

- [ ] first visible group opens automatically;
- [ ] scrolling into the next main section closes the previous group;
- [ ] the new group opens;
- [ ] its subtitles appear;
- [ ] the exact active subtitle becomes red;
- [ ] third-level items appear only under the active second-level item;
- [ ] the left column scrolls internally to keep the active item visible;
- [ ] the main page itself does not jump when the TOC auto-scrolls.
