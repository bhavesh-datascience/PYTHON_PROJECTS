import random

rock = '''
    _______
---'   ____)
      (_)
      (_)
      ()
---.(_)
'''

paper = '''
    _______
---'   ___)___
          ______)
          _______)
         _______)
---.)
'''

scissors = '''
    _______
---'   ___)___
          ______)
       __________)
      ()
---.(_)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice==computer_choice:
  print("its tie ")
elif (user_choice==0 and computer_choice==3) or (user_choice==1 and computer_choice==0) or (user_choice==2 and computer_choice==2):
  print("you win")
else:
  print("you lose")