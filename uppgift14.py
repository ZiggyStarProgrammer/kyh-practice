FRUITS = ['banana', 'apple', 'orange']
CARS = ['volvo', 'ford', 'tesla']
ANIMAL = ['cat', 'doggo', 'birb', 'giraffe']


def run():
    basket = input("Skriv vad du vill handla separerat, separera med komma...").split(',')
    basket.sort()
    cars = []
    fruits = []
    animal = []
    rest = []
    for item in basket:
        item = item.strip()
        if item in CARS:
            cars.append(item)
        elif item in FRUITS:
            fruits.append(item)
        elif item in ANIMAL:
            animal.append(item)
        else:
            rest.append(item)
    write_things(cars, 'Cars')
    write_things(fruits, 'Fruits')
    write_things(animal, 'Animals')
    write_things(rest, 'Misc')


def write_things(items, kind):
    print(kind.upper(), len(items))
    for item in items:
        print(f" {item}")

# den nedanför gör samma sak som printen ovanför
"""    if kind == 'Cars':
        print(kind.upper(), len(cars))
        for item in items:
            print(f" {item}")
    if kind == 'Fruits':
        print(kind.upper(), len(fruits))
        for item in items:
            print(f" {item}")
    if kind == 'Misc':
        print(kind.upper(), len(rest))
        for item in items:
            print(f" {item}")
"""

if __name__ == '__main__':
    run()
