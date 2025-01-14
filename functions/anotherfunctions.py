def simple_addition(a, b):
    return a + b

def greet(name="Guest"):
    return f"Hello, {name}!"

def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result

def get_person_details(**kwargs):
    return kwargs

def combine_strings(text1: str, text2: str) -> str:
    return text1 + " " + text2

def calculate_area(length: float, width: float = 1.0) -> float:
    return length * width

def process_list(items: list):
    return [item.upper() if isinstance(item, str) else item for item in items]

def recursive_factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Example lambda function
square = lambda x: x ** 2