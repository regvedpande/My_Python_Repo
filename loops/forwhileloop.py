print("1. For Loop Example - Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Count is: {i}")

print("\n2. While Loop Example - Counting down from 5 to 1:")
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1

print("\n3. Hybrid Example - Using both loops:")
number = 1
while number <= 3:
    print(f"\nTable of {number}:")
    for multiplier in range(1, 5):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")
    number += 1

print("\nProgram completed!")
