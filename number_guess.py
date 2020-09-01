import random

max_guesses = 0
n = random.randint(1, 5)
print("Jag tänker på ett tal mellan 1 och 100, vilket tal tänker jag på?")


def ask_number(max_guesses):
    max_guesses = max_guesses + 1
    text = input("Vad är din gissning?")
    as_number = int(text)
    mainloop(max_guesses, n, as_number)
    return as_number


def mainloop(max_guesses, n, as_number):
    while True:

        if as_number == n:
            print("Korrekt! Det tog dig " + str(max_guesses) + " gissningar")
            return

        if as_number < n:
            print("Fel nummer, mitt nummer är högre... Försök igen! ")
            print("Du har gjort " + str(max_guesses) + " gissningar")
            ask_number(max_guesses)

        if as_number > n:
            print("Fel nummer, mitt nummer är lägre... Försök igen! ")
            print("Du har gjort " + str(max_guesses) + " gissningar")
            ask_number(max_guesses)
        break


ask_number(max_guesses)
