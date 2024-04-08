# The goal of this project is to create a silent auction program that takes users' names and bids, hides the bids,
# then, at the end of the program, prints out the winner's name and bid.

# NOTE: The clear screen function intended to be used in this program will not work because PyCharm does not have
# the same libraries. This challenge was completed on Replit, which DOES have a clear function.

print("Welcome to the secret auction program! Follow the prompts to get started.")
restart = 0
bidders = {}

while restart == 0:
    name = str(input("What is your name? "))
    try:
        bid = float(input("Please type the amount you wish to bid: $"))
    except:
        print("Please type a valid number.")
        bid = float(input("Please type the amount you wish to bid: $"))
    bidders[name] = bid
    nextPerson = str(input("Would another person like to bid? (Y/N) ").lower())
    while nextPerson != "y" and nextPerson != "n":
        print("Please choose Y or N.")
        nextPerson = str(input("Would another person like to bid? (Y/N) ").lower())
    if nextPerson == "n":
        restart += 1
    print()

if restart == 1:
    highestBid = max(bidders.values())
    highestBidder = max(bidders, key=bidders.get)
    print(f"The highest bidder was {highestBidder} with a bid of ${highestBid:.2f}.")
    print()
    print("Thank you for auctioning with us!")
