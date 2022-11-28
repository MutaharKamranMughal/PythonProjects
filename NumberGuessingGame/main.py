# Number Guesser Game

import random 

range_of_number = input("Enter your range 1-10: ")

if range_of_number.isdigit():
    range_of_number = int(range_of_number)

    if range_of_number <= 0:
        print("Please Enter a Number greater then 0.")
        quit()
    if range_of_number > 10:
        print("Please Enter a number less than 10.")
        quit()
else:
    print("Please Enter a Number next time.")
    quit()

random_number = random.randint(0, range_of_number)
guesses = 0

while True:
    guesses += 1
    print(f"{4 - guesses} guesses left.")

    if guesses > 3:
        print("You are out of guesses. Better luck next time :).")
        break

    user_guess = input(f"Make a Guess 0-{range_of_number}: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a number next time.')
        continue

    if user_guess == random_number:
        print("You got it right....Luckyy!!!")
        break
    else:
        print("You got it wrong.Try Again!")

