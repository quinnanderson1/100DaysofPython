# The goal of this project is to create a random password generator based on user input

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
numLetters = int(input("How many letters would you like in your password? "))
numSymbols = int(input(f"How many symbols would you like? "))
numNumbers = int(input(f"How many numbers would you like? "))

randLetters = []
randSymbols = []
randNumbers = []

for i in range(0, numLetters):
    randLetters.append(letters[random.randint(0, len(letters) - 1)])
for i in range(0, numSymbols):
    randSymbols.append(symbols[random.randint(0, len(symbols) - 1)])
for i in range(0, numNumbers):
    randNumbers.append(numbers[random.randint(0, len(numbers) - 1)])

passwordChars = []
for i in range(0, numLetters):
    passwordChars.append(randLetters[i])
for i in range(0, numSymbols):
    passwordChars.append(randSymbols[i])
for i in range(0, numNumbers):
    passwordChars.append(randNumbers[i])

random.shuffle(passwordChars)
password = ""
for i in range(0, len(passwordChars)):
    password += str(passwordChars[i])

print(f"Your password is: {password}")
