def safe_divide():
    try:
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))
        result = numerator / denominator
    except ValueError:
        print("❌ Invalid input! Please enter integers only.")
    except ZeroDivisionError:
        print("🚫 Cannot divide by zero. Try a different denominator.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
    else:
        print(f"✅ Result: {result}")
    finally:
        print("🔚 Operation complete.")

# Run the function
safe_divide()
