import random

secret_number = random.randint(1, 10)
attempts = 0

print("🎯 Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 10:
            raise ValueError("Out of range!")

        if guess == secret_number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

    except ValueError as ve:
        print(f"⚠️ Invalid input: {ve}. Please enter a number between 1 and 10.")