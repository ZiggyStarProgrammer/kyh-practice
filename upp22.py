from pathlib import Path
import json

p = Path('telefonbok.json')
r = p.read_text()
numbers = json.loads(r)


vem = input("Vem vill du ringa?")
if vem not in numbers:
    print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
else:
    number = numbers[vem]
    print(f"Numret till {vem} är {number}")


def main():
    # Vår telefonkatalog är "hårdkodad" i programmet, och representeras
    # av en dictionary (dict).

    # Jag lade till en while-true loop så man kan se vad man lägger
    # till i dict:en; det står inte egentligen i uppgiften om ni
    # undrar! :)
    while True:
        # f-string + len() för att skriva ut antal nummer
        print(f"Det finns {len(numbers)} nummer i telefonkatalogen.")

        svar = input("[S]lå upp eller [L]ägg till? ")
        svar = svar[0].upper()  # plocka ut första tecknet bara, och gör det alltid STORT
        if svar == 'S':
            vem = input("Vem vill du ringa?")
            # Slå upp namnet användaren matar in m.h.a "in" keyword (lätt att läsa!)
            if vem not in numbers:
                # key fanns inte i dict
                print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
            else:
                # key fanns i dict; ta reda på value m.h.a indexering som göra med raka klamrar
                # (precis som med listor fast nycklar måste inte vara heltal!)
                number = numbers[vem]
                print(f"Numret till {vem} är {number}")

        elif svar == 'L':
            namn = input("Ange personens förnamn: ")
            tfn = input("Ange telefonnummer: ")
            numbers[namn] = tfn

        else:
            print("Förstår inte, avbryter programmet.")
            # Avbryter while True och då tar main slut, d.v.s programmet avslutas
            # eftersom det inte står något mer i Pythonfilen på rad 69!
            break


if __name__ == '__main__':
    main()