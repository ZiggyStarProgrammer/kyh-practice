"""
#15.1

def main():

    def wordcount(txt):
        return len(txt.split())

    text = input("Skriv något")
    count = wordcount(text)

    print(f'Antal ord: {count}')


main()
"""


# 15.2

def vowel_counter(char):
        if char.lower() == 'a' or char.lower() == 'e':
            print(char)
            return True


def main():
    counter = 0
    text = input("Ange text")
    for char in text:
        if vowel_counter(char):
            counter = counter + 1
            print(counter)


main()
