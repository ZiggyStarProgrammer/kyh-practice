from pathlib import Path

r = Path("TODO2.txt")
saved_file = r.read_text(encoding="utf8")
list_of_todo = saved_file.split(" ")


def actions():
    while True:

        print(f"1. Display list")
        print("2. Add to list")
        print("3. Remove from list")
        print("4. Quit")

        action = int(input("What do you wanna do?"))

        if action == 1:
            show_list()
        if action == 2:
            add()
        if action == 3:
            erase()
        if action == 4:
            break


def show_list():
    for word in list_of_todo:
        print(word)


def add():
    task = input("Type what to add")
    list_of_todo.append(task)
    r.write_text(" ".join(list_of_todo))


def erase():
    delete = input("Type what to remove")
    list_of_todo.remove(delete)
    r.write_text(" ".join(list_of_todo))


if __name__ == '__main__':
    actions()
