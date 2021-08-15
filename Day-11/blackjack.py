from art import logo
import random

print (logo)

start = input('Do you want to play the game of Black Jack? Type "y" for yes and "n" for no: ').lower()

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card =  random.choice(cards)
    return card

user_cards = []
computer_cards = []
is_game_over = False

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)
def compare_score(user_score, computer_score):
    if user_score == computer_score:
        return "Push"
    elif computer_score == 0:
        return "You Lost. Computer has Blackjack!"
    elif user_score == 0:
        return "BLACKJACK! You Win!"
    elif user_score > 21:
        return "You went over 21. You Lose!"
    elif computer_score > 21:
        return "Computer went over 21. You Win!"
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You Lose!"

for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Your cards: {user_cards}")
print(f"Current card count: {user_score}")
print(f"Computer's first cards: {computer_cards[0]}")

while user_score != 0 and user_score < 21:
    
    deal = input('Type "y" to Hit "n" to Stand: ').lower()
    if deal == 'y':
        user_cards.append(deal_cards()) 
        user_score = calculate_score(user_cards)
        print (f"Your cards: {user_cards}")
        print(f"Current card count: {user_score}")
    elif user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    elif deal == 'n':
        print(f"Your final hand: {user_cards}), final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare_score(user_score, computer_score))
        is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_cards())
    computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}), final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare_score(user_score, computer_score))
