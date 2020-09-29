def reverse(normal_list):
    listo = normal_list
    otsil = []
    for i in range(len(listo) - 1, -1, -1):
        otsil.append(listo[i])
    return otsil

# annat sätt att skriva baklänges fast som en sträng
def rev(normal):
    rev = normal[::-1]
    return rev


def upper(text):
    counter = 0
    for c in text:
        if c.isupper():
            counter += 1
    return counter


def upperC(text):
    chars = []
    counter = 0
    for c in text:
        if c.isupper():
            counter += 1
            chars.append(c)
    return chars


def blank():
    counter = 0



print(reverse([1, 2, 3]))
print(rev("1, 2, 3"))
print(upper("hej HoPop"))