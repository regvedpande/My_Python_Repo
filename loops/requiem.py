# --- Example 1: Basic for loop (iterating over a list) ---
print("--- Example 1: Iterating over a list ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("-" * 30)

# --- Example 2: for loop with range() (iterating a specific number of times) ---
print("--- Example 2: Iterating with range() ---")
# range(5) generates numbers from 0 to 4
for i in range(5):
    print(f"Iteration {i}")
print("-" * 30)

# --- Example 3: for loop with range(start, stop) ---
print("--- Example 3: Iterating with range(start, stop) ---")
# range(2, 7) generates numbers from 2 to 6
for j in range(2, 7):
    print(f"Number: {j}")
print("-" * 30)

# --- Example 4: for loop with range(start, stop, step) ---
print("--- Example 4: Iterating with range(start, stop, step) ---")
# range(0, 10, 2) generates numbers 0, 2, 4, 6, 8
for k in range(0, 10, 2):
    print(f"Even number: {k}")
print("-" * 30)

# --- Example 5: Iterating over a string ---
print("--- Example 5: Iterating over a string ---")
word = "Python"
for char in word:
    print(char)
print("-" * 30)

# --- Example 6: while loop (executes as long as a condition is true) ---
print("--- Example 6: Basic while loop ---")
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1  # Increment count to eventually break the loop
print("-" * 30)

# --- Example 7: while loop with a break statement ---
print("--- Example 7: while loop with break ---")
secret_number = 7
guess = 0
while True:  # Infinite loop, will be broken by condition
    guess += 1
    if guess == secret_number:
        print(f"You found the secret number ({secret_number}) in {guess} guesses!")
        break  # Exit the loop
    else:
        print(f"Guess {guess} is not the secret number.")
print("-" * 30)

# --- Example 8: while loop with a continue statement ---
print("--- Example 8: while loop with continue ---")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:  # If num is even
        continue  # Skip the rest of the current iteration and go to the next
    print(f"{num} is an odd number.")
print("-" * 30)

# --- Example 9: Nested loops (for loop inside another for loop) ---
print("--- Example 9: Nested Loops ---")
for i in range(3):
    for j in range(2):
        print(f"Outer loop iteration {i}, Inner loop iteration {j}")
print("-" * 30)

# --- Example 10: Looping through a dictionary ---
print("--- Example 10: Looping through a dictionary ---")
person = {"name": "Alice", "age": 30, "city": "New York"}

print("Keys:")
for key in person:  # By default, iterates over keys
    print(key)

print("\nValues:")
for value in person.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in person.items():
    print(f"{key}: {value}")
print("-" * 30)
