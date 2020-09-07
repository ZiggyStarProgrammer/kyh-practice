def is_it_too_long(name, max_length):

    return len(name) > max_length


# def name_is_ok(name):
  #   return len(name) < 5


def main():
    # students = ["anna", "beatrice", "cecilia", "doris", "esmeralda", "frida", "gunilla"]
    try:
        max_length = int(input("Ange max längd på namn: "))
    except ValueError:
        max_length = 5

    students = input("Ange studenternas namn").split(',')
    for name in students:
        # if name_is_ok():
        fixed_name = name.strip()
        if is_it_too_long(name, max_length):
            print(f"{fixed_name.title()} är för långt!")


if __name__ == '__main__':
    main()
