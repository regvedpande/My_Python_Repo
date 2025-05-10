try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter integers only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
