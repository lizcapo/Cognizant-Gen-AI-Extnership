# Step 1: Generate a Random Number
# Use Python’s random module to generate a random number between 1 and 100.

# import random
# number_to_guess = random.randint(1, 100)
# Step 2: Prompt the User for Guesses
# Use a while loop to let the user keep guessing until they get the correct answer. After each guess:

# If the guess is too high, print: "Too high! Try again."
# If the guess is too low, print: "Too low! Try again."
# If the guess is correct, print: "Congratulations! You guessed it!"
# Step 3: Count the Attempts
# Keep track of how many guesses the user has made and display the total number of attempts when they win.

import random

counter = 0 
num_to_guess = random.randint(1, 100)

prompt = int(input("Enter a number b/w 1-100: "))

while 1 <= prompt <= 100:
    counter += 1
    if num_to_guess == prompt: 
        print("Congrats you won!")
        print(f"Number of Tries: {counter}")
        break
    elif num_to_guess > prompt : 
        print("Too low! Try again!")
        print(f"Number of Tries: {counter}")
    else: 
        print("Too high! Try again!")
        print(f"Number of Tries: {counter}")
    
    prompt = int(input("Please enter another number: "))