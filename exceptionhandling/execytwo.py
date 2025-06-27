# Example 1: Basic try-except block
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ValueError:
    print("Invalid input! Please enter an integer.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except Exception as e: # A general catch-all for any other exceptions
    print(f"An unexpected error occurred: {e}")
else:
    # This block executes if no exception occurs in the try block
    print("Division successful!")
finally:
    # This block always executes, regardless of whether an exception occurred or not
    print("Execution complete.")

print("\n--- Another example with file handling ---")

# Example 2: File handling with exceptions
file_name = "my_data.txt"
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(f"File content:\n{content}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except IOError as e:
    print(f"Error reading file '{file_name}': {e}")
finally:
    print("Attempted to access file.")
