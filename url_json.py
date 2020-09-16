import requests
from pprint import pprint
import datetime
r = requests.get('https://proagile.se/api/publicEvents')

obj = r.json()
n = '\n'
today = datetime.datetime.today()
print(today)
for element in obj:
        if element is not datetime.datetime.now():
            pprint(f"Kursnamn: {element['name']} "
               f"{n} Start datum: {element['startDate']} "
               f"{n}Slut datum: {element['endDate']}")
