print("Example 1: break statement")
for i in range(1, 6):
    if i == 4:
        print(f"Found {i}! Breaking the loop...")
        break
    print(f"Current number is: {i}")

print("\nExample 2: continue statement")
for i in range(1, 6):
    if i == 3:
        print(f"Skipping number {i}...")
        continue
    print(f"Current number is: {i}")

print("\nExample 3: break in while loop")
while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input.lower() == 'q':
        print("Exiting the program...")
        break
    
    number = int(user_input)
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
