import random

max_guesses = 0

n = random.randint(1, 100)
print("Jag tänker på ett tal mellan 1 och 100, vilket tal tänker jag på?")


def mainloop(max_guesses, n):
    while True:
        text = input("Din gissar: ")
        as_number = int(text)
        max_guesses = max_guesses + 1

        if as_number == n:
            print("Korrekt! Det tog dig " + str(max_guesses) + " gissningar")
            break

        if as_number < n:
            print("Fel nummer, mitt nummer är högre... Försök igen! ")
            print("Du har " + str(max_guesses))

        if as_number > n:
            print("Fel nummer, mitt nummer är lägre... Försök igen! ")
            print("Du har " + str(max_guesses))


mainloop(max_guesses, n)
