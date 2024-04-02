# The goal of this project is to create a text-based "Choose Your Own Adventure" game

print("Welcome to Treasure Island! Your mission is to find the treasure.")
direction = str(input("Choose a direction: Left or Right? "))
if direction == "Left":
    swim = str(input("Swim or Wait? "))
    if swim == "Wait":
        door = str(input("Which door? Red, Blue, or Yellow? "))
        if door == "Red":
            print("Burned by fire. Game Over!")
        elif door == "Yellow":
            print("You Win!")
        elif door == "Blue":
            print("Eaten by beasts. Game Over!")
        else:
            print("Game Over!")
    else:
        print("Attacked by a trout. Game Over!")
else:
    print("Fall into a hole. Game Over!")
