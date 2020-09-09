from pathlib import Path

p = Path('TODO.txt')
p.write_text("Chores", encoding='utf8')
