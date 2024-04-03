# This is where I complete the example/practice assignments for the day

import random

# *** This is to flip a coin ***

# print("Coin Flipper:")
# rand_num = random.randint(0, 1)
# if rand_num == 1:
#     print("Heads")
# else:
#     print("Tails")



# *** This is to choose a random name from a user-created list ***



# print("Banker Roulette: Who Pays the Bill?")
# numPeople = int(input("How many people are at the table today? "))
# peopleList = []
# nameNum = 0
# for i in range(0, numPeople):
#     nameNum += 1
#     peopleList.append(str(input(f"Name {nameNum}: ")))
# randIndex = random.randint(0, numPeople)
# print(f"{peopleList[randIndex]} will be paying today!")



# *** The original exercise is to mark a spot on a map, a 3 x 3 grid, with an X given a user-inputted coordinate ***
# *** The challenge is I want to push this by allowing the user to define the map's grid ***



# Original

# line1 = ["( )","( )","( )"]
# line2 = ["( )","( )","( )"]
# line3 = ["( )","( )","( )"]
# treasureMap = [line1, line2, line3]
# print("Hide your treasure! X marks the spot.")
# print(f'{line1}\n{line2}\n{line3}')
# position = str(input("Where would you like to hide your treasure? Type in a coordinate (ex. A2). "))
#
# coordinates = [position[0].upper(), int(position[1])]
#
# # print(coordinates), for debugging
#
# if coordinates[0] == "A":
#     lineIndex = 0
# elif coordinates[0] == "B":
#     lineIndex = 1
# elif coordinates[0] == "C":
#     lineIndex = 2
#
# treasureMap[coordinates[1] - 1][lineIndex] = "(X)"  # lineIndex can be undefined if user input is not A, B, or C.
# print(f'{line1}\n{line2}\n{line3}')

# Challenge

lines = int(input("Please enter the number of rows you would like your map to have: "))
columns = int(input("Please enter the number of columns you would like your map to have (Max 26): "))
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
           "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
treasureMapLines = []
blankLine = []
for i in range(0, columns):
    blankLine.append("( )")
for i in range(0, lines):
    treasureMapLines.append(blankLine)

print()

for i in treasureMapLines:
    for item in i:
        print(item, end=" ")
    print()

print()

position = str(input("Where would you like to hide your treasure? Type in a coordinate (ex. A2). "))
coordinates = [position[0].upper(), int(position[1:])]
columnIndex = letters.index(coordinates[0])
lineIndex = coordinates[1]
insertedLine = []
for i in range(0, columns):
    insertedLine.append("( )")
insertedLine[columnIndex] = "(X)"
treasureMapLines[lineIndex - 1] = insertedLine

for i in treasureMapLines:
    for item in i:
        print(item, end=" ")
    print()

print()

print("Here is where we buried your treasure! Don't forget it!")
