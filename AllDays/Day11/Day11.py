# The goal of today is to re-create Blackjack.
# This project assumes an unlimited deck of cards, per the project requirements
# This project also does not take bets into account, also per the project requirements

import random


print("Welcome to PyJack, a CLI version of the popular game Blackjack!")

# Define game variables

deckOfCards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
restart = 0

while restart == 0:
    dealerHand = []
    playerHand = []
    dealerSum = 0
    playerSum = 0

    # The game starts by dealing the player and dealer two cards each
    for i in range(0, 2):
        playerHand.append(random.choice(deckOfCards))
        dealerHand.append(random.choice(deckOfCards))

    # Next, the player's two cards are shown face-up and only one of the dealer's cards is shown face-up
    print(f"You have {playerHand[0]} and {playerHand[1]}.")
    print(f"The dealer is showing {dealerHand[0]}.")

    # Then, the player must decide whether to hit or stand
    inGame = 1
    while inGame == 1:
        playerChoice = str(input("Would you like to hit or stand? (H / S) "))

        if playerChoice == "H":
            playerHand.append(random.choice(deckOfCards))
            for i in range(0, len(playerHand) - 1):
                playerSum += playerHand[i]
            if playerSum > 21:
                print(f"You're showing {playerSum}. You bust!")
                inGame = 0
                restart = str(input("Would you like to continue playing? (Y / N) "))
            else:
                playerChoice = str(input(f"You're showing {playerSum}. Would you like to hit or stand? (H / S) "))

        if playerChoice == "S":
            for i in range(0, len(playerHand) - 1):
                playerSum += playerHand[i]
            for i in range(0, len(dealerHand) - 1):
                dealerSum += dealerHand[i]
            if playerSum > dealerSum:
                print(f"The dealer had {dealerSum} and you had {playerSum}. You win!")
            elif playerSum == dealerSum:
                print(f"The dealer had {dealerSum} and you had {playerSum}. It's a draw!")
            elif playerSum < dealerSum:
                print(f"The dealer had {dealerSum} and you had {playerSum}. You lose!")
            else:
                print("Error in calculating sum.")
            inGame = 0



