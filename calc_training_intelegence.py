def add(n1, n2):
    result = n1 + n2
    return result


def sub(n1, n2):
    result = n1 - n2
    return result


def div(n1, n2):
    result = n1 / n2
    return result


def mul(n1, n2):
    result = n1 * n2
    return result


def calc():
    while True:
        action = input("What do you wanna do? + - / * ")
        number1 = int(input("chose your first number: "))
        number2 = int(input("chose the second number: "))
        if action == "+":
            result = add(number1, number2)
            return result
        if action == "-":
            result = sub(number1, number2)
            return result
        if action == "/":
            result = div(number1, number2)
            return result
        if action == "*":
            result = mul(number1, number2)
            return result


if __name__ == '__main__':
    print(calc())