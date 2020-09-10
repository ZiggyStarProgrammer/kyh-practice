import json
from pathlib import Path

p = Path('DATA.json')

s = p.read_text(encoding='utf8')

data = json.loads(s)
print(data)
