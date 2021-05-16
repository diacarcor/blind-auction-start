from replit import clear
from art import logo

print(logo)

bidding_finished = False
bidders = {}

def get_winner(bidders):
    winner_bid = 0
    winner_name = ""
    for name in bidders:
        actual_bid = bidders[name]
        if actual_bid > winner_bid:
            winner_bid = actual_bid
            winner_name = name
    
    print(f"The winner is {winner_name} with a bid of ${winner_bid}")

while not bidding_finished:
    
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid

    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    
    if other_bidder == "no":
        bidding_finished = True
        get_winner(bidders)
    elif other_bidder == "yes":
        clear()


#HINT: You can call clear() to clear the output in the console.