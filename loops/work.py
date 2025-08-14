# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # Efficient loop up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Using a for loop to print prime numbers between 10 and 50
print("Prime numbers between 10 and 50:")
for num in range(10, 51):
    if is_prime(num):
        print(num, end=" ")

# Using a while loop to find the first 5 prime numbers greater than 100
print("\n\nFirst 5 prime numbers after 100:")
count = 0
current = 101
while count < 5:
    if is_prime(current):
        print(current, end=" ")
        count += 1
    current += 1
