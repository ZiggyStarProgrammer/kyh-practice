import requests
import json
from pathlib import Path

r = Path("oboy.json")
rex = r.read_text(encoding='utf8')
rec = json.loads(rex)

for stuff in rec:
    print(f"{stuff['what']} {stuff['value']}{stuff['unit']} {stuff['value'] * 0.135} {stuff['unit']}")

