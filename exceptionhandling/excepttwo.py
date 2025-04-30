def divide_numbers(a, b):
    try:
        result = a / b
        print(f"{a} divided by {b} is {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Example usage:
divide_numbers(10, 2)  # Output: 10 divided by 2 is 5.0
divide_numbers(10, 0)  # Output: Error: Division by zero is not allowed.