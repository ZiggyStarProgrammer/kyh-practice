import webbrowser
from pathlib import Path

OUTPUT_PATH = Path("djur.html")
TEMPLATE_PATH = Path('djur_template.html')


class Djur():
    def __init__(self, name, carnivore, wiki_url):
        self.name = name
        self.carnivore = carnivore
        self.wiki_url = wiki_url

    def carnivore_or_vegetarian(self):
        # Samma funktion på en rad
        # return 'Köttätare' if self.carnivore else 'Vegetarian'
        if self.carnivore:
            return "Köttätare"
        else:
            return "Vetegarian"

    def htmll(self, html):
        html += f'<tr><td><a href="{d.wiki_url}">{d.name}</td><td>{cell_2}</td></tr>\n'
        return html


if __name__ == '__main__':
    djur = []
    zebra = Djur('Zebra', False, 'https://sv.wikipedia.org/wiki/Zebror')
    tiger = Djur('Tiger', True, 'https://sv.wikipedia.org/wiki/Tiger')
    elefant = Djur('Elefant', False, 'https://sv.wikipedia.org/wiki/Elefanter')
    platypus = Djur('Näbbdjur', True, 'https://sv.wikipedia.org/wiki/Näbbdjur')
    snowleopard = Djur('Snöleopard', True, 'https://sv.wikipedia.org/wiki/Snöleopard')
    djur.append(zebra)
    djur.append(tiger)
    djur.append(elefant)
    djur.append(platypus)
    djur.append(snowleopard)
    html = '<html><table>'
    for d in djur:
        # denna kan även skrivas som cell_2 = Djur.carnivore_or_vegetarian(d)
        cell_2 = d.carnivore_or_vegetarian()
        html = d.htmll(html)
    html += '</table></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))
