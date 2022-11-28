# Rock, Paper, Scissors Game

import random

print("Welcome to my game of Rock, Paper, Scissors. You have a total of 5 turns. Enjoy. Have fun.")

user_score = 0 
computer_score = 0
counter = 0

options = ["rock", "paper", "scissors"]

while True:
    counter += 1 
    print(f"{6 - counter} turns left.")
    if counter > 5:
        break

    user_input = input("Make your Selection Rock/Paper/Scissors or Type Q to QUIT: ").lower()

    if user_input == "q":
        print("Until Next Time. Bubyee!!")
        break
    
    if user_input not in options:
        print("Enter Valid Selection Next Time.")
        counter -= 1
        continue

    random_number = random.randint(0, 2)
    # Rock: 0, Paper: 1, Scissors: 2
    computer_pick = options[random_number]
    print(f"Computer Picked: {computer_pick}")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You win.")
        user_score += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!!")
        user_score += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!!")
        user_score += 1

    elif user_input == computer_pick:
        counter -= 1
        print("Its a Tie. Try again.")
        
    else:
        print("You lose!! :(")
        computer_score += 1

print(f"You won {user_score} times.")
print(f"Computer won {computer_score} times.")
print("GoodBye :), Hope you had fun.")
