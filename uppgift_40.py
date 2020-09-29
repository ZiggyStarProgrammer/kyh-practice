# vänder på en lista
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

# räknar och skriver ut antal stora bokstäver
def upper(text):
    counter = 0
    for c in text:
        if c.isupper():
            counter += 1
    return counter

# räknar och skriver ut vilka bokstäver som är stor bokstav
def upperC(text):
    chars = []
    counter = 0
    for c in text:
        if c.isupper():
            counter += 1
            chars.append(c)
    return chars

# räknar blanksteg och skriver ut antal
def blank(text):
    counter = 0
    for c in text:
        if c == " ":
            counter += 1
    return counter


print(reverse([1, 2, 3]))
print(rev("1, 2, 3"))
print(upper("hej HoPop"))
print(" ".join(upperC("heJ HoPPo")))
print(blank("h sdf dsfsdf  sdfsdf sdf s"))