print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are rs5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are rs7.")
    else:
        bill = 12
        print("Adult tickets are rs12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    if age >= 45 and age <= 55:  
        bill +=0   

    print(f"Your final bill is rs{bill}")
else:
    print("you cant take ride")