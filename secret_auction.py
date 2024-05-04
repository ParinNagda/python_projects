from replit import clear
from art import logo
print(logo)
is_bidding_going = True
all_bidders = []
def calculate_max_bidder(all_bidders):
    max = 0
    max_bidder = {}
    for bidder in all_bidders:
        if bidder["bid"] > max:
            max = bidder["bid"]
            max_bidder = bidder
    print(f"The winner is {max_bidder['name']} with a bid of ${max_bidder['bid']}")
  
while is_bidding_going:
  bidder = {}
  name = input("What is your name? \n")
  bid = int(input("What is your bid? \n"))
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n")
  bidder["name"] = name
  bidder["bid"] = bid
  all_bidders.append(bidder)
  if more_bidders == "no":
      is_bidding_going = False;
      calculate_max_bidder(all_bidders)
  else:
    clear()



    
