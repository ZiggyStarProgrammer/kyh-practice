def sum_all(pop):
    summa = 0
    for element in pop:
        summa += element
    return summa


def mul_all(poppa):
    mul_summa = 1
    for element in poppa:
        mul_summa *= element
    return mul_summa


print(sum_all([1, 2]))
print(mul_all([3, 4]))


#
# def subtract(a, b):
#     e = add(a, b, 4)
#     minus = e - b
#     return minus


# f = subtract(10, 15)

