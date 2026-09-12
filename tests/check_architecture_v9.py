#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml
from urllib.parse import urlparse

root = Path(__file__).resolve().parents[1]
public_qmd = [root / "index.qmd", root / "portfolio.qmd", root / "cv.qmd", root / "contact.qmd"]

checks = {}

checks["no project qmd files"] = not any((root / "projects").glob("*.qmd"))

combined = "\n".join(p.read_text(encoding="utf-8") for p in public_qmd)
checks["no public projects qmd links"] = re.search(r'projects/[A-Za-z0-9_-]+\.qmd', combined) is None
checks["no public projects html links"] = re.search(r'(?:href=["\']|]\()projects/[A-Za-z0-9_-]+\.html', combined) is None
checks["no detailed-project labels"] = not any(
    token.lower() in combined.lower()
    for token in ["Open detailed project", "View project detail"]
)

redirects = {
    "index.html": "../portfolio.html",
    "thesis.html": "../portfolio.html#masters-research",
    "cybathlon.html": "../portfolio.html#cybathlon",
    "candel.html": "../portfolio.html#candelstim",
    "borealis.html": "../portfolio.html#borealis",
    "organ-preservation.html": "../portfolio.html#organ-preservation-machine",
    "unet.html": "../portfolio.html#unet",
    "fpga.html": "../portfolio.html#fpga",
    "vscan.html": "../portfolio.html#vscan",
}
checks["nine compatibility redirects"] = all((root / "projects" / name).exists() for name in redirects) and len(list((root / "projects").glob("*.html"))) == 9

for name, target in redirects.items():
    text = (root / "projects" / name).read_text(encoding="utf-8")
    checks[f"redirect {name} target"] = target in text

portfolio = (root / "portfolio.qmd").read_text(encoding="utf-8")
required_ids = [
    "masters-research", "objective-1", "objective-2", "objective-3",
    "cybathlon", "candelstim", "borealis", "organ-preservation-machine",
    "unet", "fpga", "vscan"
]
for anchor in required_ids:
    checks[f"portfolio anchor {anchor}"] = ("{#" + anchor + "}") in portfolio

expected_h1 = [
    "MASTER'S RESEARCH — LIVER VIABILITY & ICG-NIR",
    "ROBOTICS & REHABILITATION",
    "ORGAN PRESERVATION & TRANSPLANTATION",
    "MEDICAL IMAGING & AI",
    "EMBEDDED SYSTEMS & FPGA",
    "CAD & PROTOTYPING",
]
actual_h1 = []
for line in portfolio.splitlines():
    m = re.match(r'^#\s+(.+?)(?:\s+\{#[^}]+\})?\s*$', line)
    if m:
        title = re.sub(r'\s+\{#[^}]+\}\s*$', '', m.group(1)).strip()
        actual_h1.append(title)
checks["exact six portfolio groups"] = actual_h1 == expected_h1

index = (root / "index.qmd").read_text(encoding="utf-8")
checks["home sections simplified"] = all(
    f"# {h}" in index
    for h in ["Profile", "Current Research", "Selected Work", "Engineering Areas"]
) and "# Education & Leadership" not in index and "# Explore" not in index

cv = (root / "cv.qmd").read_text(encoding="utf-8")
checks["cv selected-projects section removed"] = "# Selected Engineering Projects" not in cv
checks["cv trajectory section present"] = "# Research & Engineering Experience" in cv

cfg = yaml.safe_load((root / "_quarto.yml").read_text(encoding="utf-8"))
resources = cfg.get("project", {}).get("resources", [])
checks["redirect resources configured"] = "projects/*.html" in resources

for name, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'}: {name}")

sys.exit(0 if all(checks.values()) else 1)
