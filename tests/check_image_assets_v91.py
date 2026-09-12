#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml

root = Path(__file__).resolve().parents[1]
text = "\n".join((root / x).read_text(encoding="utf-8") for x in ["index.qmd", "portfolio.qmd"])
refs = re.findall(r'src=["\']imagenes/([^"\']+)["\']', text)
actual = {
    p.name for p in (root / "imagenes").iterdir()
    if p.is_file() and p.name != "README.md"
}
cfg = yaml.safe_load((root / "_quarto.yml").read_text(encoding="utf-8"))
resources = cfg.get("project", {}).get("resources", [])

checks = {
    "54 references": len(refs) == 54,
    "54 unique references": len(set(refs)) == 54,
    "54 files": len(actual) == 54,
    "no missing/orphan files": set(refs) == actual,
    "load fallback": "classList.add('has-image')" in text,
    "error fallback": "classList.remove('has-image')" in text,
    "inventory": (root / "IMAGENES_REQUERIDAS.md").exists(),
    "quarto resources": "imagenes/*" in resources,
}
for name, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'}: {name}")
if set(refs) != actual:
    print("Missing:", sorted(set(refs) - actual))
    print("Orphan:", sorted(actual - set(refs)))
sys.exit(0 if all(checks.values()) else 1)
