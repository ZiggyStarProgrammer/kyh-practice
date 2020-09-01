max_tries = 2

for i in range(max_tries):
    password = input('What is your password?')
    if password == "abc123":
        break
    print("Please Try Again")

if i == max_tries:
    raise ValueError("Too many attempts")