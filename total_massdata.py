import json
from pathlib import Path

p = Path('massadata.json')

r = p.read_text(encoding='utf8')

data = json.loads(r)

FILE = data["entries"]

TOTAL = sum(item['total'] for item in FILE)
print(TOTAL)