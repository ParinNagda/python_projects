from art import logo, vs
from game_data import data

print(logo)
guess = True
score = 0
while guess:
  print("Compare A: " + data[score]["name"] + ", a " + data[score]["description"] + " " + data[score]["country"] + "\n\n")

  print(vs)

  print("Against B: " + data[score + 1]["name"] + ", a " + data[score + 1]["description"] + " " + data[score + 1]["country"])

  guess = input("Who has more followers? Type 'A' or 'B': ")
  if guess == "A" and (data[score]['follower_count'] > data[score + 1]['follower_count']):
      score += 1
      print("You are right! Current score: " + str(score))
  elif guess == "B" and (data[score]['follower_count'] < data[score + 1]['follower_count']):
      score += 1
      print("You are right! Current score: " + str(score))
  else:
    guess = False


if not guess:
  print("Sorry that's wrong. Final Score " + str(score))
