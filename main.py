from replit import clear  #used to clear the output between users.
from art import logo

print(logo)
print("Welcome to the Blind Auction Program!")
bid_dict = {}
another_input = True

while another_input == True:  #Filling up the dictionary
  input_name = input("What is your name?\n")
  input_bid = int(input("What is your bid?\n$"))
  bid_dict[input_name] = input_bid
  new_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if new_bidder == "no":
    another_input = False
  else:
    clear()

highest_bid = 0
winner = ""
for bidder in bid_dict:  #The bids are compared
  current_bid = bid_dict[bidder]
  if current_bid > highest_bid:
    highest_bid = current_bid
    winner = bidder

clear()
print(f"The winner is {winner}, with a bid of ${highest_bid}.")
