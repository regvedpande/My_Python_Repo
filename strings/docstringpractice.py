def calculate_square(number):
    """
    Calculate the square of a given number.
    
    Args:
        number: The input number to be squared
        
    Returns:
        The square of the input number
    """
    return number ** 2

def greet(name):
    """
    Returns a greeting message with the given name.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        A string containing the greeting message
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    result = calculate_square(5)
    print(result)
    
    message = greet("Alice")
    print(message)
    
    # Accessing docstrings
    print(calculate_square.__doc__)
    print(greet.__doc__)