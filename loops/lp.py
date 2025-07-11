# Using for and while loops to generate Fibonacci sequence
def fibonacci(n):
    # Initialize first two numbers
    a, b = 0, 1
    fib_list = []
    
    # Using while loop to generate sequence
    while len(fib_list) < n:
        fib_list.append(a)
        a, b = b, a + b
    
    # Using for loop to print the sequence
    print("First", n, "Fibonacci numbers:")
    for i, num in enumerate(fib_list):
        print(f"F({i}) = {num}")

# Call the function
fibonacci(10)