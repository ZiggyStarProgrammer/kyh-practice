from uppgift_36 import pwstrength


def main():
    passw = input('Skriv ditt lösenord: ')
    print(f"Ditt lösenord är värt {pwstrength.compute_strength(passw)} poäng.")


if __name__ == '__main__':
    main()
