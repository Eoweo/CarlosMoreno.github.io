#!/usr/bin/env python3
from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[1]
index = (root / "index.qmd").read_text(encoding="utf-8")
portfolio = (root / "portfolio.qmd").read_text(encoding="utf-8")
text = index + "\n" + portfolio

refs = re.findall(r'src=["\']imagenes/([^"\']+)["\']', text)
actual = {
    p.name for p in (root / "imagenes").iterdir()
    if p.is_file() and p.name != "README.md"
}

unique_refs = set(refs)

objective3 = re.search(
    r'## Objective 3 — ICG-NIR Functional Marker.*?(?=\n---\n|\Z)',
    portfolio, re.S
)
objective3_text = objective3.group(0) if objective3 else ""

cal = re.search(
    r'### Calibration and validation.*?(?=\n## Objective 2)',
    portfolio, re.S
)
cal_text = cal.group(0) if cal else ""

candel = re.search(
    r'## CandelStim.*?(?=\n---\n)',
    portfolio, re.S
)
candel_text = candel.group(0) if candel else ""

checks = {
    "29 image/media files": len(actual) == 29,
    "29 unique media references": len(unique_refs) == 29,
    "no missing media": unique_refs == actual,
    "rat model explicit": "ex vivo rat liver" in portfolio.lower(),
    "objective 3 coming soon": "Coming soon — this objective is currently in progress." in objective3_text,
    "objective 3 no images": "imagenes/" not in objective3_text,
    "objective 3 no ICG parameters": all(x not in objective3_text for x in ["PDR", "R15", "Fmax", "Tmax", "AUC"]),
    "no damper image references": "tesis_damper" not in text and "grafico_damper" not in text,
    "no dedicated damper heading": "### Pumping, pulse damping and oxygenation" not in portfolio,
    "calibration text only": "imagenes/" not in cal_text,
    "monitor current screenshot": "tesis_monitor_1_canal.png" in portfolio,
    "monitor future pig screenshot": "tesis_monitor_multicanal_cerdo.png" in portfolio,
    "candel confidentiality": "active NDA" in candel_text,
    "candel no detailed protocol list": all(x not in candel_text for x in ["tDCS", "tACS", "tRNS", "ESP32", "STM32", "BLE"]),
    "no FPGA media": "fpga_" not in text,
    "no preservation-machine media": "preservacion_" not in text,
    "Instagram no fake href": "ADD_CYBATHLON" not in portfolio and "instagram.com/" not in portfolio,
}

for name, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'}: {name}")

if unique_refs != actual:
    print("Missing:", sorted(unique_refs - actual))
    print("Orphan:", sorted(actual - unique_refs))

sys.exit(0 if all(checks.values()) else 1)
