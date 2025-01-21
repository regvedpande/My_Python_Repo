# Recursion is the process of defining something in terms of itself.
# In this case, we are defining the factorial of a number in terms 
# of the factorial of a number that is one less than it. 
# This is a recursive definition of the factorial function.
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)

factorial(5)