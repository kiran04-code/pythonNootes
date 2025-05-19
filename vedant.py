
import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
correct_number=random.randint(1,100)
def play_game(attempts):
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess_number = int(input("Make a Guess :"))
        if guess_number > correct_number:
            print("Too High")
            attempts -= 1
        elif guess_number < correct_number:
            print("Too Low")
            attempts -= 1
        else:
            print("You Guessed Right")
            attempts -= 1

    if attempts==0:
        print("You loose")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if difficulty=="easy":
    attempts=10
    play_game(attempts)

elif difficulty=="hard":
    attempts = 5
    play_game(attempts)
