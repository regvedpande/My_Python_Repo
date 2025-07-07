def divide_numbers():
    try:
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        result = num1 / num2
    except ValueError:
        print("❌ Please enter valid integers.")
    except ZeroDivisionError:
        print("❌ Division by zero is not allowed.")
    else:
        print(f"✅ The result is: {result}")
    finally:
        print("🔚 Operation complete.")

# Run the function
divide_numbers()