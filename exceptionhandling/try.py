def divide(numerator, denominator):
    """Divides two numbers and handles potential ZeroDivisionError."""
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")
        return None

# Example usage
numerator = 10
denominator = 2
quotient = divide(numerator, denominator)
if quotient is not None:
    print(f"{numerator} divided by {denominator} is: {quotient}")

numerator = 5
denominator = 0
quotient = divide(numerator, denominator)
if quotient is not None:
    print(f"{numerator} divided by {denominator} is: {quotient}")

numerator = "hello"
denominator = 5
quotient = divide(numerator, denominator)
if quotient is not None:
    print(f"{numerator} divided by {denominator} is: {quotient}")
