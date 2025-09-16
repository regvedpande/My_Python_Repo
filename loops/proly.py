# 🔁 FOR loop: Print squares of numbers from 1 to 5
print("Squares using for loop:")
for i in range(1, 6):
    print(f"{i}² = {i**2}")

# 🔄 WHILE loop: Countdown from 5 to 1
print("\nCountdown using while loop:")
count = 5
while count > 0:
    print(f"T-minus {count}")
    count -= 1

# 🔂 NESTED loop: Simple multiplication table (1 to 3)
print("\nMultiplication Table (1 to 3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")  # Separator for each row
