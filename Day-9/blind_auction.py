from replit import clear
from art import logo

print(logo)
continue_prog = True
bid = {}

while continue_prog:

    name = input("Enter your name: ")
    bid_amount = int(input("Enter your bid: $"))

    bid[name] = bid_amount

    other_bidders = input("Any other biders? Type 'Yes' or 'No': ").lower()

    highest_bid = 0
    for highest in bid:
        if bid[highest] > highest_bid:
            highest_bid = bid[highest]
            highest_bidder = highest
    print(f"Highest bidder is {highest_bidder} with the bid of ${highest_bid}.")

    if other_bidders == 'yes':
        clear()
    else:
        continue_prog = False
        print(f"Highest bidder is {highest_bidder} with the bid of ${highest_bid}.")
