# Ask the user for a number
n = int(input("Enter a positive integer: "))

# Initialize sum variable
total_sum = 0

# Calculate the sum of numbers from 1 to n
for i in range(1, n + 1):
    total_sum += i

# Print the result
print(f"The sum of numbers from 1 to {n} is {total_sum}")