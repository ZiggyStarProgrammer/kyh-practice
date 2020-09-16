import requests
from pprint import pprint
import json
r = requests.get('https://proagile.se/api/publicEvents')

obj = r.json()
pprint(obj)
