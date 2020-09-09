"""
def case():

    dokument = "system.log"
    important = []
    keep_phrases = ["BEAR", "X-RAY"]
    with open(dokument) as f:
            lines = f.readlines()

    for line in lines:
        line = line.strip()
        for phrase in keep_phrases:
            if phrase in line:
                important.append(line)
                break

    print(*important, sep='\n')


case()
"""

"""
from pathlib import Path


def case():

    dokument = "system.log"
    important = []
    keep_phrases = ["BEAR", "X-RAY"]
    lines = Path(dokument).read_text().splitlines()

    for line in lines:
        line = line.strip()
        for phrase in keep_phrases:
            if phrase in line:
                important.append(line)
                break

    print('\n'.join(important))


case()
"""


# sista funkar inte
from pathlib import Path


def run():
    important = []
    for line in Path('system.log').read_text().splitlines():
        if 'BEAR' in line or 'X-RAY':
            important.append(line)
    print(important)


run()
