import random

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

random_choice = random.choice([rock, paper, scissors])
user_choice = input("Choose Rock, Paper, or Scissor: ").lower()
print("Computer : " + random_choice)
print("User: " + user_choice)

if (user_choice == "rock" and random_choice == rock):
  print("Game tied")
elif (user_choice == "rock" and random_choice == paper):
  print("You lost!")
elif (user_choice == "rock" and random_choice == scissors):
  print("You won!")

elif (user_choice == "paper" and random_choice == paper):
  print("Game tied")
elif(user_choice == "paper" and random_choice == scissors):
  print("You lost!")
elif (user_choice == "paper" and random_choice == rock):
  print("You won!")

elif (user_choice == "scissor" and random_choice == scissors):
  print("Game tied")
elif(user_choice == "scissor" and random_choice == rock):
  print("You lost!")
elif(user_choice == "scissor" and random_choice == paper):
  print("You won!")

else:
  print("Restart the game.")
