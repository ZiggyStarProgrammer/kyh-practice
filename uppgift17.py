from pathlib import Path

p = Path('TODO.txt')
tasks = []
content = p.read_text()


def options():
    print('1. Visa lista')
    print('2. Lägg till')
    print('3. Ta bort')
    print('4. Stäng')

    q = input('Vad vill du göra?')
    if q == '1':
        read()
    if q == '2':
        add()
    if q == '3':
        erase()
    else:
        pass


def read():
    print(content)


def add():
    content.splitlines()
    tasks = [content]
    while True:
        task = input("Vad vill du lägga till?")
        tasks.append(task)
        p.write_text(tasks)
        print(content)
        break

def erase():
    data_2 = input('Vad vill du ta bort?')
    p.write_text(data_2)

# def close():
print(tasks)

options()
