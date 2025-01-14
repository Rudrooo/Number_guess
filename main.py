from art import logo
import random

print(logo)
all_level={
    "EASY":10,
    "HARD":5
}
win=False
print("Welcome to the Number Guessing Game!")
level=input("Choose a difficulty.Type 'easy' or 'hard': ").upper()
attempt=all_level[level]
computer_guess=random.randint(1,100)
for i in range(all_level[level]):
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess=int(input(f"Make a guess: "))
    if computer_guess==guess:
        print("You make the correct guess.")
        win="True"
        break
    elif computer_guess>guess:
        print("Too low \n Guess again")
    else:
        print("Too high \n Guess again")
    attempt-=1

if not win:
    print("You ran out of guesses.You Lose")
