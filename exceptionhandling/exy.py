def divide_numbers(numerator, denominator):
    """
    This function divides two numbers and handles potential ZeroDivisionError
    and TypeError exceptions.

    Args:
        numerator (int or float): The number to be divided.
        denominator (int or float): The number to divide by.

    Returns:
        float or None: The result of the division if successful, None otherwise.
    """
    try:
        result = numerator / denominator
        print(f"The result of {numerator} divided by {denominator} is: {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")
        return None
    except Exception as e:  # Catch any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        return None

# --- Test cases ---

# Valid division
divide_numbers(10, 2)

# Division by zero
divide_numbers(10, 0)

# Type error (non-numeric input)
divide_numbers("hello", 5)

# Another valid division
divide_numbers(7.5, 2.5)

# Another type error
divide_numbers(10, "world")

# Example of an unexpected error (though less likely with simple division)
# You could simulate this with more complex operations within the try block
# For instance, if you tried to access an attribute that doesn't exist on a variable.
# For this simple example, we'll just show what the output looks like.
try:
    x = [1, 2]
    y = x[5] # This will raise an IndexError
except IndexError:
    print("Caught an IndexError!")
except Exception as e:
    print(f"Caught a different unexpected error: {e}")
