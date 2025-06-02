def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid input type!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
divide_numbers(10, 2)  # Successful division
divide_numbers(10, 0)  # Division by zero error
divide_numbers(10, 'a')  # Invalid input type error