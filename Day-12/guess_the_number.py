from art import logo
from random import randint
print (logo)
print ("I am guessing a number between 1 and 100")
number = randint(1,100)
difficulty = input("Choose your difficulty level. Hard or Easy: ").lower()
# user_guess = int(input("Enter your guess: ").lower())

# Reduce the repeating code like, user_guess and difficulty levels.

def game():
    global difficulty

    if difficulty == "hard":
        lives = 5
        print(f"You have {lives} lives remaining")
        while lives > 0:
            
            user_guess = int(input("Enter your guess: ").lower())
            if user_guess == number:
                print("Correct guess! You are a genius!")
            elif user_guess > number:
                print ("Too high.")
                lives -= 1
                print(f"You have {lives} lives remaining")
            elif user_guess < number:
                print("Too low.")
                lives -= 1
                print(f"You have {lives} lives remaining")
    
    elif difficulty == "easy":
        lives = 10
        print(f"You have {lives} lives remaining")
        while lives > 0:
            
            user_guess = int(input("Enter your guess: ").lower())
            if user_guess == number:
                print("Correct guess! You are a genius!")
            elif user_guess > number:
                print ("Too high.")
                lives -= 1
                print(f"You have {lives} lives remaining")
            elif user_guess < number:
                print("Too low.")
                lives -= 1
                print(f"You have {lives} lives remaining")


game()
