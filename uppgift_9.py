import random


def game(number_of_questions):
    correct_answers = 0
    for i in range(number_of_questions):
        a = random.randint(1, max_value)
        b = random.randint(1, max_value)
        answer = input(f"{a} + {b}")
        number = int(answer)

        if number == a + b:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f"Fel... Det blir {a+b}")
            print("---")
        print(correct_answers, " av ", number_of_questions, " rätt!")


if __name__ == '__main__':
    number_of_questions = int(input("Hur många frågor?"))
    max_value = int(input("Största tal?"))
    game(number_of_questions)
