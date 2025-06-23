# Get user input for a number
try:
    number = float(input("Enter a number: "))

    # Check the conditions
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

except ValueError:
    print("Invalid input. Please enter a valid number.")

