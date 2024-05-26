import random
print("Welcome to the number guessing game !\nchoose a difficulty level ,type easy or hard :")
difficulty = input("Enter difficulty level : ")
random_int=random.randint(1,100)
rand_int=(random_int)
if difficulty == "easy":
    attempt=10
else:
    attempt=5
print(random_int)

print(f"You have choosen {difficulty} level and you have {attempt} to guess the number")
for i in range(attempt):
        user_guess=int(input("make a guess : "))
        if user_guess == random_int:
            print("You guessed the number correctly")
            break
        elif user_guess > random_int:
            print("guess is higer")
        else :
            print("guess is lower")
        attempt=attempt-1
        if attempt!=0:
             print(f"You have {attempt} attempts left")
        else:
            print("attempts over ")
            print(f"the number was {random_int}")
             