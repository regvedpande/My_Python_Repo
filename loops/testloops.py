# Example of Python loops

# For loop example
print("For Loop Example:")
for i in range(1, 6):  # Loops from 1 to 5
    print(f"Number: {i}, Square: {i*i}")

# While loop example
print("\nWhile Loop Example:")
count = 1
while count <= 5:  # Loops as long as count is <= 5
    print(f"Number: {count}, Square: {count*count}")
    count += 1  # Increment count

# Loop with break and continue
print("\nLoop with Break and Continue:")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    if num > 7:
        break  # Exit loop when num > 7
    print(f"Odd number: {num}")

# Nested loop example
print("\nNested Loop Example (Multiplication Table):")
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"{i} x {j} = {i*j}", end="\t")
    print()  # New line after each inner loop completes