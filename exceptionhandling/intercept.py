def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: Cannot divide by zero. Details: {e}")
        result = None
    except TypeError as e:
        print(f"Error: Invalid input type. Details: {e}")
        result = None
    else:
        print(f"Success: The result is {result}")
    finally:
        print("Execution completed. Cleaning up...")

    return result

# Example usage
divide_numbers(10, 2)     # Valid division
divide_numbers(10, 0)     # Triggers ZeroDivisionError
divide_numbers(10, 'a')   # Triggers TypeError
