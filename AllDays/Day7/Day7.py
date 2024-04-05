# The goal of today's project is to create a hangman game

import random
import hangmanWords

# Defining variables and initializing the game

print("Hello, and welcome to Hangman!")
chosenWord = random.choice(hangmanWords.wordList)
chosenWordBlank = []
gameOver = 0
lifeCount = 6
userLetters = ""

# Print the number of blank spaces as there are letters in the randomly chosen word

for letter in chosenWord:
    print("_", end="")
    chosenWordBlank += "_"
print()

# Runs the game until gameOver == 1

while gameOver == 0:
    userGuess = (str.lower((input("What letter would you like to try? "))))
    userLetters += userGuess + " "

# Checks to see what letters in the word the user's guess matches, then prints the word blank with matches

    i = -1
    for letter in chosenWord:
        i += 1
        if userGuess == letter:
            chosenWordBlank[i] = userGuess
    if userGuess not in chosenWord:
        lifeCount -= 1

    completedWord = ""
    for letter in chosenWordBlank:
        completedWord += letter
    print(completedWord)

# Prints some quality-of-life information and whitespace

    print(f"Lives remaining: {lifeCount}")
    print(f"You have tried: {userLetters}")
    print()

# Defines the "win" condition

    countInc = 0
    for letter in chosenWordBlank:
        count = len(chosenWord)
        if letter != "_":
            countInc += 1
        if countInc == count:
            gameOver += 1
            print(f"The word was: {chosenWord}")
            print()
            print("YOU WIN!")

# Defines the "lose" condition

    if lifeCount == 0:
        gameOver += 1
        print(f"The word was: {chosenWord}")
        print()
        print("YOU LOSE!")

# Defines the "game over" condition

if gameOver == 1:
    print("GAME OVER")
