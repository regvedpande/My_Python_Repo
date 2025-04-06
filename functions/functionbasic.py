# Basic function example to demonstrate how functions work in Python

def greet_person(name, age):
    """
    This is a simple function that takes two parameters:
    name: person's name
    age: person's age
    Returns a greeting message
    """
    message = f"Hello {name}! You are {age} years old."
    return message

# Example of how to call/use the function
def main():
    # Calling the function with different arguments
    greeting1 = greet_person("Alice", 25)
    print(greeting1)  # Output: Hello Alice! You are 25 years old.
    
    # Another function call with different values
    greeting2 = greet_person("Bob", 30)
    print(greeting2)  # Output: Hello Bob! You are 30 years old.

# Call the main function
if __name__ == "__main__":
    main()