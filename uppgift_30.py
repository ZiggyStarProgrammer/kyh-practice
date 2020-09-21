
# reg = input("Ange regnr: ")
#
# print(f"Bokstäver: {reg[0 : 3]} \n"
#       f"Siffror: {reg[3:]}")


numbers = input("Ange ett tal med komma emellan: ")
tal = []
for ele in numbers.split(","):
    tal.append(int(ele))
tal2 = [int(elem) for elem in numbers.split(",")]
print(f"Första talet: {numbers[0]} \n"
      f"Sista talet: {numbers[-1]}")

print(f"Summan av talen: {sum(tal2)} \n")
# Variant 1 för att köra baklänges
print(f"Talen baklänges: {tal2[::-1]}")
# Variant 2
backwards = "".join(list(reversed(numbers)))
print(f"Talen baklänges: {backwards}")


odd = [num for num in numbers.split(",") if int(num) % 2 != 0]
print(f"Udda tal: {odd[0:len(odd)]}")
# print(f"Jämna tal: {odd[1:len(odd):2]}")
