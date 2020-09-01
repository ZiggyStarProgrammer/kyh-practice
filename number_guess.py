import random

n = random.randint(1, 20)
print("Im thinking of a nu")

while True:
    text = input("Your guess")
    as_number = int(text)

    if as_number == n:
        print("Correct!")
        break

    if as_number < n:
        print("Wrong, my number is higher... Try again")

    if as_number > n:
        print("Wrong, my number is lower... Try again!")

