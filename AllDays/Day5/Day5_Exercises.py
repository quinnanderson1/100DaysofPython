# The goal of the first exercise is to calculate the average height of students from a given list of heights
# This is to practice for loops, so I will not be using len() or sum()

student_heights = [180, 124, 165, 173, 189, 169, 146]
numStudents = 0
sumHeights = 0
for i in student_heights:
    numStudents += 1
for i in student_heights:
    sumHeights += i
avgHeight = sumHeights / numStudents

print(f"The total height is {sumHeights}")
print(f"The number of students is {numStudents}")
print(f"The average height is {avgHeight:.2f}")

# The goal of this is to find the highest number in a list only using a for loop

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
maxNum = 0
for i in student_scores:
    if i > maxNum:
        maxNum = i
print(f"The highest number in this list is {maxNum}.")

# The goal of this is to calculate the sum of all even numbers from 1 to X, X being user input

userIn = int(input("Please enter your desired number. "))
total = 0
for i in range(0, userIn + 1, 2):
    total += i
print(total)

# The goal of this is to recreate the FizzBuzz game where if a number is
# divisible by 3, you say Fizz, and 5, you say Buzz. This goes from 1 to 100.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
