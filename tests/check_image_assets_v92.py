#!/usr/bin/env python3
from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[1]
index = (root / "index.qmd").read_text(encoding="utf-8")
portfolio = (root / "portfolio.qmd").read_text(encoding="utf-8")
text = index + "\n" + portfolio

expected = set(['Trabajando.png', 'Tesis_Equipo.png', 'Tesis_Completo.jpeg', 'Tesis_Setup.png', 'Tesis_Oxigenador.png', 'Tesis_Monitor2canales.jpeg', 'cybathlon_aeropuerto.png', 'cybathlon_apoyo.jpeg', 'cybathlon_Compitiendo.png', 'cybathlon_diagrama.jpeg', 'candel_dds.png', 'Candel_pcb.png', 'Candel_Software.png', 'Borealis_equipo.jpeg', 'Borealis_liver2.png', 'Borealis_Grafico2.png', 'Ipre.gif', 'ipre_graph.png', 'Vscan_3dReal.png', 'vscan_solo.png', 'Vscan_uso1.png'])
refs = re.findall(r"src=[\"']imagenes/([^\"']+)[\"']", text)
actual = {
    p.name for p in (root / "imagenes").iterdir()
    if p.is_file() and p.name != "README.md"
}

checks = {
    "21 references": len(refs) == 21,
    "21 unique references": len(set(refs)) == 21,
    "21 image files": len(actual) == 21,
    "exact filename contract": set(refs) == expected == actual,
    "no ICG image references": not any("icg" in x.lower() for x in refs),
    "single monitor screenshot": refs.count("Tesis_Monitor2canales.jpeg") == 1 and "Tesis_monitor1canal.jpeg" not in refs,
    "objective 3 coming soon": "## Objective 3 — ICG-NIR Functional Marker" in portfolio and "**Coming soon.**" in portfolio,
    "Fluke mentioned": "Fluke reference equipment" in portfolio,
    "no damper section": "### Pumping, pulse damping and oxygenation" not in portfolio,
    "rat model explicit": "ex vivo rat liver perfusion model" in portfolio.lower(),
}

for name, ok in checks.items():
    print(f"{'PASS' if ok else 'FAIL'}: {name}")

if set(refs) != expected:
    print("Missing refs:", sorted(expected - set(refs)))
    print("Unexpected refs:", sorted(set(refs) - expected))

sys.exit(0 if all(checks.values()) else 1)
