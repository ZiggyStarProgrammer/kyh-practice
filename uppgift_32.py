string = input("Skriv något: ")

text = string.replace(" ", "")
# istället för replace kan man använda
# ''.join([c for c in string.lower() if c != ' '])

print(" ".join(string.split()))

print(len(text))

if text.lower() == text.lower()[::-1]:
    print(" ".join(string.split()), "Detta är ett palindrom")
else:
    print(" ".join(string.split()), "är inte ett palindrom")
   #  print(f"{' '.join(string.split())} är inte ett palindrom")
   #  print(f"{" ".join(string.split())} är inte ett palindrom")
