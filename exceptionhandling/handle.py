# Basic example of exception handling in Python

try:
    # Ask the user to enter a number
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: You can't divide by zero!")

except ValueError:
    print("Error: Please enter a valid number.")

finally:
    print("This block always runs, no matter what.")