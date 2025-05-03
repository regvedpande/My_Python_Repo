# Get the user's age as input
try:
    age_str = input("Please enter your age: ")
    age = int(age_str) # Convert the input string to an integer

    # Check the age using conditional statements
    if age < 0:
        print("Age cannot be negative. Please enter a valid age.")
    elif age < 13:
        print("You are a child.")
    elif age < 18:
        print("You are a teenager.")
    else:
        print("You are an adult.")

except ValueError:
    # Handle the case where the input is not a valid number
    print(f"Invalid input: '{age_str}' is not a whole number. Please run the program again and enter a number.")

