# This is to recall how to make/call a function

# def greet():
#     print("This is line 1")
#     print("This is line 2")
#     print("This is line 3")
#
# greet()

# Create a function that allows for input

# def greet_with_name(name):
#     print(f"Hello {name}!")
#
# greet_with_name("Quinn")

# Create a function that allows for multiple inputs, both positional and keyword

# def greet_with(name, location):
#     print(f"Hello {name}!")
#     print(f"What's it like in {location} this time of year?")
#
# greet_with("Quinn", "America")
#
# greet_with(location="Brazil", name="Sal Paul-o")

# Create a program to calculate the number of cans of paint needed to paint a wall given height,
# width, and coverage per can of paint.

# import math
#
#
# def paint_calc(height, width, cover):
#     numCans = math.ceil((height * width) / cover)   # math.ceil rounds up to the next integer given a float (4.1 -> 5)
#     print(f"You'll need {numCans} cans of paint.")
#
#
# test_h = int(input())
# test_w = int(input())
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Create a function to check if a user-inputted number is prime

def prime_checker(number):
    if 1 <= number <= 100:
        isPrime = True
        for i in range(2, number - 1):
            if number / i == int(number / i):
                isPrime = False
        if isPrime == False:
            print("It's not a prime number.")
        elif isPrime == True:
            print("It's a prime number.")
    else:
        print("Error, number invalid. Select a number between 1 and 100.")


n = int(input("What number would you like to check (1 - 100)? "))
prime_checker(number=n)
