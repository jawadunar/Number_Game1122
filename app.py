import random
from typing import Union

lowest_num: int = 1
highest_num: int = 100
answer: int = random.randint(lowest_num, highest_num)

guesses: int = 0
is_running: bool = True 

print("Python Number Guessing Game:")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess_input: str = input("Enter your guess: ")

    if guess_input.isdigit():
        guess: int = int(guess_input)
        guesses += 1  

        if guess < lowest_num or guess > highest_num:
            print("Number out of range!")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        
        elif guess < answer:
            print("Too Low! Try again")
        
        elif guess > answer:
            print("Too High! Try again")
        
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False 

    else:
        print("Invalid Guess")
        print(f"Please enter a valid number between {lowest_num} and {highest_num}")
