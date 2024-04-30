size = input("Enter pizza size s, m, l: ")
bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("Invalid input")

    
pepper = input("Do you want pepperoni? (Enter 'y' or 'n'): ")
if pepper == "y":
    bill += 3
elif pepper == "n":
    bill += 1
else:
    print("Invalid input")

cheese = input("Do you want extra cheese? (Enter 'y' or 'n'): ")
if cheese == "y":
    bill += 4
else:
    bill+=1

print("Your total bill is", bill)
