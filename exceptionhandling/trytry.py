def safe_division(numerator, denominator):
    """
    This function attempts to divide two numbers and handles potential ZeroDivisionError
    or TypeError using a try-except block.

    Args:
        numerator: The number to be divided.
        denominator: The number to divide by.

    Returns:
        The result of the division if successful, or a descriptive error message.
    """
    try:
        result = numerator / denominator
        return f"The result of the division is: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Both numerator and denominator must be numbers."
    except Exception as e:  # Catch any other unexpected errors
        return f"An unexpected error occurred: {e}"

# --- Examples of usage ---

# Successful division
print(safe_division(10, 2))

# Division by zero
print(safe_division(10, 0))

# Type error (denominator is a string)
print(safe_division(10, "a"))

# Type error (numerator is a list)
print(safe_division([10], 2))

# Another successful division with float
print(safe_division(7.5, 2.5))
