name = input("Nanm: ")
age = input("Ålder: ")

tup = (name, age)


def info(inf):
    print(f"Ålder: {tup[0]}\n"
          f"Namn: {tup[1]}")


info(tup)

def swaptup(a, b):
    (a, b) = (b, a)
    return a, b


print(swaptup(1, 3))