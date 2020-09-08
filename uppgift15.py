def main():

    def wordcount(txt):
        return len(txt.split())

    text = input("Skriv något")
    count = wordcount(text)
    print(f'Antal ord: {count}')

main()