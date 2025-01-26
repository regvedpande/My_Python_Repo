def divide_numbers():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("This block always executes")

def main():
    print("Exception Handling Demo")
    try:
        # List index error example
        my_list = [1, 2, 3]
        print(my_list[10])
    except IndexError:
        print("Error: List index out of range!")

    # Division function call
    divide_numbers()

if __name__ == "__main__":
    main()