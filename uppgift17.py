from pathlib import Path

p = Path('TODO.txt')
content = p.read_text(encoding='utf8')
tasks = content.splitlines()
n = '\n'


def options():
    print('1. Visa lista')
    print('2. Lägg till')
    print('3. Ta bort')
    print('4. Stäng')

    q = input('Vad vill du göra? ')
    if q == '1':
        read()
    if q == '2':
        add()
    if q == '3':
        erase()
    if q == '4':
        return
    else:
        options()


def read():
    content.splitlines()
    content.strip()
    print(', '.join(tasks))
    return


def add():
    task = input("Vad vill du lägga till? (Tryck 1 för att backa)\n").strip()
    if task == '1':
        return
    else:
        tasks.append(task)
        p.write_text(f"{n.join(tasks)}", encoding='utf8')
        return


def erase():
    print(', '.join(tasks))
    delete = input('Skriv det som du vill ta bort. (Tryck 1 för att backa)\n')
    if delete == '1':
        return
    if delete in tasks:
        tasks.remove(delete)
        p.write_text(f"{n.join(tasks)}", encoding='utf8')
        return
    else:
        erase()


options()
