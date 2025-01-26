def divide_numbers():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ValueError:
        print("Please enter valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    finally:
        print("This block always executes, regardless of exceptions")
        print("Cleaning up resources...")

print("Program started")
divide_numbers()
print("Program ended")