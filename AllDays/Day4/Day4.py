# The goal of this project is to create a randomized rock-paper-scissors game against a computer.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameImages = [rock, paper, scissors]

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. "))
computerChoice = random.randint(0, 2)
if userChoice > 2 or userChoice < 0:
    print("Invalid Selection. Try again!")
else:
    print("You chose...")
    print(gameImages[userChoice])
    if userChoice == 0:
        print("...ROCK!")
    elif userChoice == 1:
        print("...PAPER!")
    elif userChoice == 2:
        print("...SCISSORS!")

    print("The computer chose...")
    print(gameImages[computerChoice])
    if computerChoice == 0:
        print("...ROCK!")
    elif computerChoice == 1:
        print("...PAPER!")
    elif computerChoice == 2:
        print("...SCISSORS!")

    if userChoice == computerChoice:
        print("IT'S A DRAW!!!")
    elif userChoice == 1 and computerChoice == 0:
        print("YOU WIN!!!")
    elif userChoice == 2 and computerChoice == 1:
        print("YOU WIN!!!")
    elif userChoice == 0 and computerChoice == 2:
        print("YOU WIN!!!")
    elif userChoice == 0 and computerChoice == 1:
        print("YOU LOSE!!!")
    elif userChoice == 1 and computerChoice == 2:
        print("YOU LOSE!!!")
    elif userChoice == 2 and computerChoice == 0:
        print("YOU LOSE!!!")
