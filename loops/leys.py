def divide_numbers():
    try:
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        result = num1 / num2
    except ValueError:
        print("❌ Invalid input! Please enter integers only.")
    except ZeroDivisionError:
        print("🚫 Cannot divide by zero!")
    else:
        print(f"✅ The result is: {result}")
    finally:
        print("🔚 Execution completed.")

# Run the function
divide_numbers()