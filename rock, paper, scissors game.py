import time
import random


options = ["rock", "paper", "scissors"]

random_num = random.randint(0,2)

user_choice = input("Choose and write 'r' for 'rock', 'p' for 'paper' or 's' for 'scissors'.")

if user_choice == 'r':

    user_choice_full_name = options[0]

elif user_choice == 'p':

    user_choice_full_name = options[1]

elif user_choice == 's':

    user_choice_full_name = options[2]

time.sleep(0.5)

print("Your choice is " + user_choice_full_name + "!")

time.sleep(0.5)

opponent_choice = options[random_num]

print("Your opponent's choice is " + opponent_choice + "!")

time.sleep(0.5)

if user_choice_full_name == options[0] and opponent_choice == options[1]:

    print("Paper beats rock! You loose! :(")

elif user_choice_full_name == options[0] and opponent_choice == options[2]:

    print("Rock beats scissors! You win! :)")

elif user_choice_full_name == options[1] and opponent_choice == options[0]:

    print("Paper beats rock! You win! :)")

elif user_choice_full_name == options[1] and opponent_choice == options[2]:
    
    print("Scissors beat paper! You loose! :(")

elif user_choice_full_name == options[2] and opponent_choice == options[0]:

    print("Rock beats scissors! You loose! :(")

elif user_choice_full_name == options[2] and opponent_choice == options[1]:

    print("Scissors beat paper! You win! :)")

elif user_choice_full_name == opponent_choice:

    print("It's a draw!")

