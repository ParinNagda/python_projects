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

#Write your code below this line 👇

import random

hand_image = [rock, paper, scissors]
user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"User chose: {hand_image[user_selection]}")

computer_selection = random.randint(0, 2)
print(f"Computer chose:\n{hand_image[computer_selection]}")

if user_selection >= 3 and user_selection < 0:
  print("You typed an invalid number, you lose!")
elif user_selection == 0 and computer_selection == 2:
  print("You win!")
elif user_selection == 2 and computer_selection == 0:
  print("You lose!")
elif user_selection > computer_selection:
  print("You win!")
elif user_selection < computer_selection:
  print("You lose!")
elif user_selection == computer_selection:
  print("It's a draw!")

