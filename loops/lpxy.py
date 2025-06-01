# A simple 'for' loop that prints numbers from 0 to 4
print("--- For loop (range) ---")
for i in range(5):  # range(5) generates numbers 0, 1, 2, 3, 4
    print(f"Current number: {i}")

print("\n--- For loop (range with start and stop) ---")
for i in range(2, 7): # range(2, 7) generates numbers 2, 3, 4, 5, 6
    print(f"Number from 2 to 6: {i}")

print("\n--- For loop (range with step) ---")
for i in range(1, 10, 2): # range(1, 10, 2) generates numbers 1, 3, 5, 7, 9
    print(f"Odd number: {i}")
