def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Please provide numeric values.")
    finally:
        print("Execution completed.")

# Example usage
divide_numbers(10, 0)
divide_numbers(10, 'five')
divide_numbers(10, 2)
