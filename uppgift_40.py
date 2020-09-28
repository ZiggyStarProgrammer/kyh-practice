def reverse():
    listo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    otsil = []
    for i in range(len(listo) - 1, -1, -1):
        otsil.append(listo[i])
    return otsil


print(reverse())
