import webbrowser
from pathlib import Path
import requests
import json

p = Path('test.html')

life_advice_r = requests.get("https://api.adviceslip.com/advice")
advice_text = p.read_text(encoding='utf8')
life_advice = json.loads(life_advice_r.text)
life_advice = life_advice["slip"].get("advice")
advice_text = advice_text.replace("QUOTE_TEXT", life_advice)

new_browser = Path('goat_quote.html')
new_browser.write_text(advice_text)
webbrowser.open(str(new_browser))
