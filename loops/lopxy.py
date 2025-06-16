# --- 1. The 'for' loop: Iterating over a sequence ---

print("--- For Loop Examples ---")

# Example 1.1: Iterating over a list of items
fruits = ["apple", "banana", "cherry"]
print("Iterating over a list:")
for fruit in fruits:
    print(fruit)

print("-" * 20)

# Example 1.2: Iterating over a string (characters)
word = "Python"
print("Iterating over a string:")
for char in word:
    print(char)

print("-" * 20)

# Example 1.3: Iterating using range() - a sequence of numbers
# range(stop): 0 up to (but not including) stop
print("Iterating using range(5):")
for i in range(5):
    print(i)

print("-" * 20)

# Example 1.4: Iterating using range(start, stop)
print("Iterating using range(2, 7):")
for i in range(2, 7):
    print(i)

print("-" * 20)

# Example 1.5: Iterating using range(start, stop, step)
print("Iterating using range(0, 10, 2) (even numbers):")
for i in range(0, 10, 2):
    print(i)

print("-" * 20)

# Example 1.6: Using 'else' with 'for' loop (optional, runs if loop completes without 'break')
print("For loop with 'else':")
for i in range(3):
    print(f"Current i: {i}")
else:
    print("For loop finished without breaking.")

print("-" * 20)

# Example 1.7: Nested 'for' loops
print("Nested For Loops:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

print("\n--- While Loop Examples ---")

# --- 2. The 'while' loop: Repeating as long as a condition is true ---

# Example 2.1: Basic while loop
count = 0
print("Basic while loop (count < 5):")
while count < 5:
    print(f"Count is: {count}")
    count += 1  # Increment count to eventually stop the loop

print("-" * 20)

# Example 2.2: Using 'break' to exit a loop prematurely
secret_number = 7
guess = 0
print("While loop with 'break' (guessing game):")
while True:  # Infinite loop until 'break' is encountered
    guess = int(input("Guess the secret number (between 1 and 10): "))
    if guess == secret_number:
        print("Congratulations! You guessed it!")
        break  # Exit the loop
    else:
        print("Wrong guess, try again!")

print("-" * 20)

# Example 2.3: Using 'continue' to skip the rest of the current iteration
print("While loop with 'continue':")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:  # If num is even
        continue      # Skip the rest of this iteration, go to the next
    print(f"Odd number: {num}") # This will only print odd numbers

print("-" * 20)

# Example 2.4: Using 'else' with 'while' loop (optional, runs if loop condition becomes false normally)
print("While loop with 'else':")
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1
else:
    print("While loop finished because the condition became false.")

print("\n--- Loop Control Statements ---")

# Summary of 'break' and 'continue' with a 'for' loop example
print("Demonstrating 'break' and 'continue' in a for loop:")
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at i = 5")
        break  # Exits the loop entirely
    if i % 2 == 0:
        print(f"Skipping even number: {i}")
        continue # Skips the rest of the current iteration
    print(f"Processing odd number: {i}")

print("\n--- Common Loop Pitfalls ---")

# Example of an infinite loop (do NOT run uncommented unless you know how to stop it!)
# counter_infinite = 0
# while True:
#     print(f"This is an infinite loop! Counter: {counter_infinite}")
#     # You would typically have a condition inside to break,
#     # otherwise it runs forever. Press Ctrl+C to stop it.
#     # counter_infinite += 1 # Uncomment this to see it increment

print("Remember to ensure loop termination conditions are met!")
