import random

max_guesses = 3

n = random.randint(1, 100)
print("Jag tänker på ett tal mellan 1 och 100, vilket tal tänker jag på?")

for guesses in range(max_guesses):
    text = input("Din gissar: ")
    as_number = int(text)

    if as_number == n:
        print("Korrekt! Det tog dig")
        break

    if as_number < n:
            print("Fel nummer, mitt nummer är högre... Försök igen! ")

    if as_number > n:
            print("Fel nummer, mitt nummer är lägre... Försök igen! ")

else:
    raise ValueError("Detta var inte din grej Alla dina " + max_guesses + "är slut.")

