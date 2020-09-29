# skapar en tuple och unpackar en tuple
name = input("Nanm: ")
age = input("Ålder: ")

tup = (name, age)


def info(inf):
    print(f"Ålder: {tup[0]}\n"
          f"Namn: {tup[1]}")


info(tup)


# byter plats på index i en tuple
def swaptup(a, b):
    (a, b) = (b, a)
    return a, b


print(swaptup(1, 3))


# omvandlar en lista till en tuple
def ls_to_tuple(list):
    tup = tuple(list)
    return tup


print(ls_to_tuple([1, 2, 3]))
