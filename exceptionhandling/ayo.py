def safe_divide():
    """
    This function demonstrates exception handling for division.
    """
    try:
        # Get input from the user
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        # Perform the division
        result = numerator / denominator

    except ValueError:
        # This block runs if the user enters a non-numeric value
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        # This block runs if the user enters 0 for the denominator
        print("Error: Cannot divide by zero.")

    else:
        # This block runs if no exceptions were raised
        print(f"The result of the division is: {result}")

    finally:
        # This block runs no matter what, whether an exception occurred or not
        print("Division attempt finished.")

# Call the function to run the example
safe_divide()