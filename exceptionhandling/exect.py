def safe_division(numerator, denominator):
    """
    Attempts to divide two numbers and handles potential ZeroDivisionError
    and TypeError exceptions.

    Args:
        numerator: The number to be divided.
        denominator: The number to divide by.

    Returns:
        The result of the division if successful, or a string indicating
        the type of error encountered.
    """
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Both inputs must be numbers!"
    except Exception as e:
        # This is a general catch-all for any other unexpected errors
        return f"An unexpected error occurred: {e}"
    else:
        # This block executes if no exception occurs in the try block
        return "Division successful (this should not be reached if result is returned in try)"
    finally:
        # This block always executes, regardless of whether an exception occurred or not
        print("Execution of safe_division function completed.")

# --- Examples of using the function ---

# Valid division
print(f"10 / 2 = {safe_division(10, 2)}")

# Division by zero
print(f"10 / 0 = {safe_division(10, 0)}")

# Type error
print(f"'a' / 2 = {safe_division('a', 2)}")

# Another valid division
print(f"7 / 3 = {safe_division(7, 3)}")

# Using a non-numeric denominator
print(f"10 / 'b' = {safe_division(10, 'b')}")
