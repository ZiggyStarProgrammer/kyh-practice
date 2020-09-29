def reverse(normal_list):
    listo = normal_list
    otsil = []
    for i in range(len(listo) - 1, -1, -1):
        otsil.append(listo[i])
    return otsil

def rev(normal):
    rev = normal[::-1]
    return rev


print(reverse([1, 2, 3]))
print(rev("1, 2, 3"))