# The purpose of today's project is to create a tip calculator that
# takes into account the total, tip, and number of people paying

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? ")) / 100
numPeople = int(input("How many ways would you like to split the bill? "))
totalToPay = (total + (total * tip)) / numPeople
print(f"Each person should pay: ${totalToPay:.2f}")
