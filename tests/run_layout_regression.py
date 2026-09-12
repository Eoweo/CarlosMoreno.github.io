#!/usr/bin/env python3
from pathlib import Path
import subprocess,re,json,sys
root=Path(__file__).resolve().parent
html=root/'native-toc-regression.html'
widths=[1920,1440,1100,900]
results=[]
for width in widths:
    cmd=['chromium','--headless','--no-sandbox','--disable-gpu',f'--window-size={width},900','--virtual-time-budget=900','--dump-dom','file://'+str(html)]
    p=subprocess.run(cmd,capture_output=True,text=True,timeout=30)
    dom=p.stdout
    m=re.search(r'data-test-result="(pass|fail)"',dom)
    j=re.search(r'data-test-json="([^"]*)"',dom)
    status=m.group(1) if m else 'no-result'
    results.append({'width':width,'status':status,'returncode':p.returncode})
    # Screenshot for visual inspection
    shot=root/f'native-toc-{width}.png'
    subprocess.run(['chromium','--headless','--no-sandbox','--disable-gpu',f'--window-size={width},900',f'--screenshot={shot}','file://'+str(html)],capture_output=True,text=True,timeout=30)
print(json.dumps(results,indent=2))
if not all(r['status']=='pass' for r in results): sys.exit(1)
