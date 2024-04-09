# The goal of today's project is to create a four-function calculator

from Day10_Art import logo
import Day10_Math

print(logo)

endProgram = 0
lastResult = 0
operations = ["+", "-", "*", "/"]
restart = ""
reuseNum = False

print("Welcome to PyCalc, a four-function CLI calculator!")
print()

while endProgram == 0:
    # Checks to see if reuseNum flag is True or False
    if not reuseNum:
        firstNum = float(input("Please enter the first number: "))
    elif reuseNum:
        firstNum = lastResult
    else:
        firstNum = float(input("Please enter the first number: "))
    operation = input("Please enter the operation (+ - * /): ")
    operationName = ""
    secondNum = float(input("Please enter the second number: "))

    # Error handling if the user enters an invalid operation
    while operation not in operations:
        print("Invalid operator chosen.")
        operation = input("Please enter the operation (+ - * /): ")

    # Calculates using the user's numbers
    operationResult = Day10_Math.calculate(firstNum, secondNum, operation)

    restart = str(input(f"Would you like to continue calculating with {operationResult}? (Y/N/Exit) ").lower())

    # Restart error checking
    while restart != "y" and restart != "n" and restart != "exit":
        print("Please type either Y, N, or Exit.")
        restart = str(input(f"Would you like to continue calculating with {operationResult}? (Y/N/Exit) ").lower())

    if restart == "y":
        lastResult = operationResult
        reuseNum = True

    if restart == "n":
        reuseNum = False
        print()

    if restart == "exit":
        endProgram = 1

if endProgram == 1:
    print()
    print("Thank you for calculating with PyCalc!")
