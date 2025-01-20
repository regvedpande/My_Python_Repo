def greet(name):
    """
    A simple function that greets a person.
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: The greeting message
    """
    return f"Hello, {name}!"

class Calculator:
    """
    A simple calculator class to demonstrate class docstrings.
    
    This class provides basic arithmetic operations.
    """
    
    def add(self, x, y):
        """
        Add two numbers together.
        
        Args:
            x (float): First number
            y (float): Second number
            
        Returns:
            float: The sum of x and y
        """
        return x + y

# Example of accessing docstrings
if __name__ == "__main__":
    print("Function docstring:", greet.__doc__)
    print("Class docstring:", Calculator.__doc__)
    print("Method docstring:", Calculator.add.__doc__)
    
    # Using the documented code
    print(greet("Alice"))
    calc = Calculator()
    print(calc.add(5, 3))