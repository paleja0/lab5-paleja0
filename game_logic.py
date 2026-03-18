from secret_number import seed_secret_numbers, generate_secret_number
from response import input_response

seed = int(input("Enter a seed number: "))
seed_secret_numbers(seed)
secret_number = generate_secret_number()

tries = 0
guessed = False

while not guessed:
    guess = int(input("What is your guess: "))
    tries += 1

    message, guessed = input_response(secret_number, guess)
    print(message)

print(f"It took you {tries} tries!")