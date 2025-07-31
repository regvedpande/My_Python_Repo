def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ValueError:
        print("Oops! Please enter valid numbers.")
    except ZeroDivisionError:
        print("Can't divide by zero, try a different number.")
    except Exception as e:
        print(f"Something went wrong: {e}")
    else:
        print("Division performed successfully.")
    finally:
        print("Execution complete.")

divide_numbers()
