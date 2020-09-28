def add(a, b, c):
    number = a + b + c
    return number


def subtract(a, b):
    e = add(a, b, 4)
    minus = e - b
    return minus


f = subtract(10, 15)
print(f)
