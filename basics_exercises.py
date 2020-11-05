# name = input("Name: ")
# print(f"Your name is: {name.title()}")
#
# num1 = int(input("Write number: "))
# num2 = int(input("Write a number to multiply: "))
# result = num1 * num2
# print(result)
#
#
# result1 = (3+2) * 6
# print(result1)
#
# annoying_bot = True
# while annoying_bot:
#     vowel = ["a", "o", "e", "i"]
#     check_this = input("Skriv text: ")
#     for i in check_this:
#         if i.lower() in vowel:
#             print(i)
#             annoying_bot = False
#
# age = int(input("How old are you?"))
# if age < 12:
#     print("Grow up kid")
# if 12 < age < 20:
#     print("You are a teen!")
# if 20 < age < 40:
#     print("Get your life together!")
# if age > 40:
#     print("u old...")
#
# money = {
#     "1": "George Washington",
#     "2": "Thomas Jefferson",
#     "5": "Abraham Lincoln",
#     "10": "Alexander Hamilton",
#     "20": "Andrew Jackson",
#     "50": "Ulysses S.Grant",
#     "100": "Benjamin Franklin"
# }
# note = input("Write the number of a bill: ")
# print(money[note])

# X = int(input("Tal: "))
# Y = int(input('Tal: '))
# Z = int(input('Tal: '))
#
# x = 0
# y = 0
# z = 0
#
# if X < Y and X < Z:
#     x = X
#
# if Y < X and Y < Z:
#     x = Y
#
# if Z < X and Z < Y:
#     x = Z
#
#
# if Y > X and X < Z:
#     y = X
#
# if X > Y and Y < Z:
#     y = Y
#
# if X > Z and Z < Y:
#     y = Z
#
#
# if X > Y and X > Z:
#     z = X
#
# if Y > X and Y > Z:
#     z = Y
#
# if Z > X and Z > Y:
#     z = Z
#
# print(f"Största tal: {z}\n"
#       f"Minsta tal: {x}\n"
#       f"Mellan: {y} ")

# up = int(input("UP: "))
# down = int(input("DOWN: "))
# left = int(input("LEFT: "))
# right = int(input("RIGHT: "))
#
#
# def funky(up, down, left, right):
#     updown = up - down
#     leftright = left - right
#     return updown, leftright
#
#
# def fixer(updown, leftright):
#     the_num = 0
#     if leftright > 1:
#         the_num = updown - leftright
#     if leftright < 0:
#         the_num = updown + leftright
#     if leftright == 1:
#         the_num = updown
#
#
#     return the_num
#
#
# print(funky(up, down, left, right))
#
# print(fixer(funky(up, down, left, right)[0], funky(up, down, left, right)[1]))

# vowel = ["a", "o", "e", "i"]
# bluh = input("text: ")
# for i in bluh:
#     if i in vowel:
#         text = i.capitalize()
#
# for i in bluh:
#     print(text)
#
# printar tal som går att dela med 7 men inte att gångra med 5.
# for i in range(2000, 3201):
#     if i%7 == 0 and i%5 != 0:
#         print(i,", ", end="")

# printar (Tal8 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64})
# inp = int(input("Tal"))
# dicti = {}
# for i in range(1, inp + 1):
#     dicti[i] = i * i
#
# print(dicti)

even = [2, 4, 6, 8, 0]
for i in range(1000, 3001):
    ls = list(str(i))
    for n in ls:
        print(n)
        if n in even:
            print(n)



