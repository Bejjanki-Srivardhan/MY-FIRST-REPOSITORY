import random

rock = '''
    _________
---'   _______)
      (________)
      (________)
      (_______)
---.__(______)
'''

paper = '''
    _______
---'   ____)_______
          __________)
          ____________)
         __________)
---._____________)
'''

scissors = '''
    _______
---'   ____)________
          ___________)
       ____________)
      (_______)
---.__(_____)
'''

#👇
game_images = [rock, paper, scissors]

user_choice = int(
  input(
    "What do you chose? Type 0 for ROCK, 1 for PAPER, 2 for  SCISSORS.\n "))

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number. so YOU LOSE !!!")
else:
  print("You chose :-")
  print(game_images[user_choice])
computer_choice = random.randint(0, 2)

print("computer chose :-")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
  print("You win !")
elif user_choice == 2 and computer_choice == 0:
  print("You lose !!!!!!")
elif computer_choice > user_choice:
  print("You lose !!!!!!!")
elif computer_choice == user_choice:
  print("It's an DRAW !")
