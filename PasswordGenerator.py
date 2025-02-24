import random

def passgen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Password Generator!")
    nr_platform = input("What platform are you generating the password for:\n")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    full_password = []

    for character in range(1, nr_letters):
        full_password.append(random.choice(letters))
    for character in range(1, nr_symbols):
        full_password.append(random.choice(symbols))
    for character in range(1, nr_numbers):
        full_password.append(random.choice(numbers))

    random.shuffle(full_password)

    password = ""
    for character in full_password:
        password+=character

    print(f"Your password for {nr_platform} : {password}")

    with open('password.txt', 'a') as file:
        test = "->" + nr_platform + " : " + repr(password) + "\n"
        file.writelines(test)
    response = input("Would you like to generate another password (Type yes or no):\n")
    if response == "yes":
        passgen()
    elif response == "no":
        print("Thank you")
    else:
        print("Invalid Response")
passgen()