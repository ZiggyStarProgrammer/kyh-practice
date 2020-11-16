import random


def hello(name):
    rnd_age = random.randint(1, 150)
    print(f"Hell {name} age {rnd_age}")


result = hello("Olof")
print(result)