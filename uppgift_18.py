n = '\n'
people = {
    "Fredrik": ['0702778511'],
    "Olof": ['123456789'],
    "Lisa": ['9999999999'],
    "Bodil": ['555-666-789']
}
numbers = []


def main():
    print(f"Det finns {len(people)} personer i listan")
    vem = input(' Vem vill du ringa? '
                '\n Vill du ta bort eller uppdatera ett nummer ? '
                '\n Vill du visa alla kontakter? ')
    if vem.lower() == 'lägg till' or 'skriv över':
        tabort()
    if vem.lower() not in people:
        print('Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog')
    else:
        number = people[vem]
        print(f"Numret till {vem} är {number}")


def tabort():
    print(n.join(people))
    overwrite = input("Vill du lägga till eller skriva över")
    if overwrite == 'lägga till':
        action = input("Vilken person vill du modifiera?")
        if action not in people:
            print(n.join(people))
        else:
            added = input("Skriv nummret du vill lägga till")
            people[action] = numbers.append(added)

    return


main()
