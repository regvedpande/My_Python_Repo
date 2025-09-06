# Factorial using a for loop
def factorial_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Factorial using a while loop
def factorial_while(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

# Example usage
num = 5
print(f"Factorial of {num} using for loop: {factorial_for(num)}")
print(f"Factorial of {num} using while loop: {factorial_while(num)}")
