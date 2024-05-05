from blackjackart import logo
from replit import clear
import random


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
  
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has a blackjack"
    elif user_score == 0:
        return "You win with a blackjack"
    elif user_score > 21:
        return "You lose, you went over 21"
    elif computer_score > 21:
        return "Opponent went over 21, You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False
  user_score = 0
  computer_score = 0
  for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
  
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  
  while not is_game_over:
  
    print(f" Your cards: {user_cards}, current score: {user_score}")
    print(f" Computer's first card: {computer_cards[0]}")
  
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_cards())
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f" Your cards: {user_cards}, current score: {user_score}")
            print(f" Computer's first card: {computer_cards[0]}")
        else:
            is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_cards())
      computer_score = calculate_score(computer_cards)
      
  print(f" Your final hand: {user_cards}, current score: {user_score}")
  print(f" Computer's final hand: {computer_cards}, current score: {computer_score}")
  result = compare(user_score, computer_score)
  print(result)
  
 
print(logo)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
 
