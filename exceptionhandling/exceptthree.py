def safe_division(numerator, denominator):
    """
    Performs division of two numbers with robust exception handling.

    Args:
        numerator: The number to be divided.
        denominator: The number to divide by.

    Returns:
        The result of the division if successful, or None if an error occurs.
    """
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# --- Examples of usage ---

# Successful division
print(f"10 / 2 = {safe_division(10, 2)}")

# Division by zero
print(f"5 / 0 = {safe_division(5, 0)}")

# Type error
print(f"'abc' / 2 = {safe_division('abc', 2)}")

# Another successful division
print(f"7.5 / 2.5 = {safe_division(7.5, 2.5)}")

# An unexpected error (e.g., if we pass a custom object that doesn't support division)
class MyObject:
    pass

obj = MyObject()
print(f"10 / MyObject = {safe_division(10, obj)}")
