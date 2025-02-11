def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Division by zero!")
        return None  # Or handle differently
    except TypeError:
        print("Invalid input types!")
        return None  # Or handle differently

# Examples
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Division by zero! \n None
print(divide("a", 2))  # Output: Invalid input types! \n None

