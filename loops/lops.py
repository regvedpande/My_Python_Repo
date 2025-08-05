def factorial(n):
    # Initialize the result
    result = 1

    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        result *= i

    return result

# Example usage
number = 5
print(f"The factorial of {number} is {factorial(number)}")
