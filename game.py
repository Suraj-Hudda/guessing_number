import random

# Generate a random number between 1 and 100
jackpot = random.randint(1, 100)

# Initialize counter for attempts
counter = 1

# Prompt the user for their first guess
try:
    guess = int(input("Guess a number between 1 and 100: "))
except ValueError:
    print("Please enter a valid number.")
    guess = int(input("Guess a number between 1 and 100: "))

# Main game loop
while guess != jackpot:
    if guess < jackpot:
        print("Guess higher!")
    else:
        print("Guess lower!")
    
    # Prompt the user for another guess and increase the counter
    try:
        guess = int(input("Guess again: "))
    except ValueError:
        print("Please enter a valid number.")
        guess = int(input("Guess again: "))
    
    counter += 1

# Congratulate the user
print("Congratulations! You guessed the correct number.")
print(f"It took you {counter} attempts.")
