def safe_division(numerator, denominator):
    """
    Performs division and handles potential ZeroDivisionError and TypeError.

    Args:
        numerator: The number to be divided.
        denominator: The number to divide by.

    Returns:
        The result of the division if successful, otherwise an error message.
    """
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Both numerator and denominator must be numbers."
    except Exception as e:  # Catch any other unexpected errors
        return f"An unexpected error occurred: {e}"
    else:
        # This block executes if no exceptions were raised in the try block
        return f"Division successful! Result: {result}"
    finally:
        # This block always executes, regardless of whether an exception occurred
        print("--- Division attempt completed ---")

# --- Test Cases ---

# Successful division
print(safe_division(10, 2))

# Division by zero
print(safe_division(5, 0))

# Type error
print(safe_division(10, "a"))

# Another successful division
print(safe_division(7, 3))

# An unexpected error (e.g., if one of the operands was a complex object not supporting division)
# (This is harder to demonstrate simply, but the generic Exception handles it)
class MyObject:
    pass

obj1 = MyObject()
# print(safe_division(10, obj1)) # Uncommenting this would raise a TypeError handled by the generic Exception
