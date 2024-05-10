#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(1, 100)
print("Correct answer is " + str(random_number))

mode = input("Choose difficulty. Type 'easy' or 'hard': ")
turn = 0
if (mode == "easy"):
    turn = 10
else:
    turn = 5

while(turn > 0):
  print(f"You have {turn} attempts remaining to guess the number.")
  guessed_number = int(input("Make a guess: "))
  if guessed_number == random_number:
      print("You got it. The answer was " + str(random_number))
      break;
  elif guessed_number > random_number:
      print("Too high")
      turn -= 1
  else:
      print("Too low");
      turn -= 1


if turn == 0:
  print("You are out of turn! You lost")
