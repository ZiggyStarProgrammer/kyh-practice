import requests
from pprint import pprint
import datetime
r = requests.get('https://proagile.se/api/publicEvents')

obj = r.json()
n = '\n'
today = datetime.datetime.today()
#
# for element in obj:
#     startdate = "2020-10-01"
#     enddate = "2020-10-31"
#     coursedate = element['startDate']
#     if startdate < coursedate and coursedate < enddate:
#         print(f"Kursnamn: {element['name']} "
#         f"{n}Start datum: {element['startDate']} "
#         f"{n}Slut datum: {element['endDate']}")


def main(startdate, enddate):
    for element in obj:
        coursedate = element['startDate']
        if startdate < coursedate and coursedate < enddate:
            print(f"Kursnamn: {element['name']} "
                  f"{n}Start datum: {element['startDate']} "
                  f"{n}Slut datum: {element['endDate']}")


if __name__ == '__main__':
    year = input("year: ")
    month = input("month: ")
    startdate = f"{year}-{month:>02}-01"
    enddate = f"{year}-{month:>02}-31"
    main(startdate, enddate)
