add_as_lambda = lambda a, b: a + b
print(add_as_lambda(4, 4))

obj = lambda s: s.upper()


# samma som
def upper(s):
    obj = s.upper()
    return obj


join_as_lamba = lambda string, inbetween: inbetween.join(string)


# samma som
def join_as_lambda(string, inbetween):
    text = inbetween.join(string)
    return text


print(join_as_lambda("join", "!"))

anna = ("Anna", "Persson", 42)
lova = ("Lova", "Andersson", 35)
alex = ("Alex", "Börjesson", 10)
people = [anna, lova, alex]
on_surname = sorted(people, key=lambda p: p[2])
for (first, last, age) in on_surname:
    print(f"{first} {last} ({age} år)")

anna = ("Anna", "Persson", 42)
alex = ("Alex", "Börjesson", 10)
lova = ("Lova", "Andersson", 35)
people = [anna, alex, lova]


def age_sorter():
    ett = people[0][2]
    tvo = people[1][2]
    tre = people[2][2]
    ls = [ett, tvo, tre]
    print(sorted(ls))


age_sorter()


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print(self):
        print(self.name)
        print(self.surname)
        print(self.age)


p1 = Person("Anna", "Persson", 42)
p2 = Person("Alex", "Börjesson", 10)
p3 = Person("Lova", "Andersson", 35)

Person.print(p1)
Person.print(p2)
Person.print(p3)
