#!/usr/bin/env python3
from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[1]
index = (root / "index.qmd").read_text(encoding="utf-8")
portfolio = (root / "portfolio.qmd").read_text(encoding="utf-8")
cv = (root / "cv.qmd").read_text(encoding="utf-8")
contact = (root / "contact.qmd").read_text(encoding="utf-8")
css = (root / "assets/site.css").read_text(encoding="utf-8")
pages = index + "\n" + portfolio

chip_icons = cv.count("cv-chip-icon")
card_icons = cv.count("cv-card-icon")
icon_titles = cv.count('class="cv-icon-title"')
icon_labels = cv.count('class="cv-icon-label"')

contact_icons = len(re.findall(r'\{\.contact-icon\}', contact))
contact_rows = len(re.findall(r'\{\.contact-icon-label\}', contact))

checks = {
    "no parentElement add": "parentElement.classList.add('has-image')" not in pages,
    "no parentElement remove": "parentElement.classList.remove('has-image')" not in pages,
    "closest add": "closest('.image-slot')?.classList.add('has-image')" in pages,
    "closest remove": "closest('.image-slot')?.classList.remove('has-image')" in pages,
    "no direct-child base selector": ".image-slot > .portfolio-image {" not in css,
    "no direct-child loaded selector": ".image-slot.has-image > .portfolio-image {" not in css,
    "descendant image selector": ".image-slot .portfolio-image {" in css,

    "4 chip icons": chip_icons == 4,
    "all chip icons inline": icon_titles >= chip_icons,
    "16 card icons": card_icons == 16,
    "all card icons accounted": (icon_titles - chip_icons) + icon_labels == card_icons,
    "no nested icon-title wrappers": '<div class="cv-icon-title"><div class="cv-icon-title">' not in cv,

    "3 contact icons": contact_icons == 3,
    "all contact icons inline": contact_rows == contact_icons,

    "inline cv CSS": ".cv-icon-title," in css and "display: flex;" in css,
    "inline contact CSS": ".contact-icon-label {" in css,
    "contact icon old min-height neutralized": ".contact-icon-label .contact-icon {\n  min-height: 0;" in css,
}

for name, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'}: {name}")

sys.exit(0 if all(checks.values()) else 1)
