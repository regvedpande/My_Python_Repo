# Factorial calculator using a for loop

num = int(input("Enter a number: "))
factorial = 1

# Loop from 1 to num (inclusive)
for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")
