def safe_division(numerator, denominator):
  """Divides two numbers, handling potential errors."""

  try:
    result = numerator / denominator
    return result

  except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    return None  # Or raise a custom exception, return a default value, etc.

  except TypeError:
    print("Error: Invalid input types. Please provide numbers.")
    return None

  except Exception as e: # Catch any other exception
    print(f"An unexpected error occurred: {e}")
    return None

def get_integer_input(prompt):
    """Gets integer input from the user, handling invalid input."""
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    """Demonstrates exception handling."""

    num1 = get_integer_input("Enter the numerator: ")
    num2 = get_integer_input("Enter the denominator: ")

    result = safe_division(num1, num2)

    if result is not None:
        print(f"The result of {num1} / {num2} is: {result}")

    # Example of raising a custom exception
    try:
        if num2 < 0:
            raise ValueError("Denominator cannot be negative")
    except ValueError as e:
        print(f"Custom error: {e}")

    # Example of using finally block
    try:
        file = open("my_file.txt", "w")
        file.write("Hello, world!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'file' in locals() and file: # avoid error if file was never created
            file.close() # Ensures file is closed even if an exception occurs.
            print("File closed")

if __name__ == "__main__":
    main()

