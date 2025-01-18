def square(x):
    print(x) #not gonna print anything so print(square(5)) will print None
    """Return the square of x."""
    '''This is a multiline docstring.'''
    return x * x
# The docstring is stored in the __doc__ attribute of the function.
# Python give special treatment to docstrings. It is used to generate documentation for the code.
print(square.__doc__)


#pep 8 defines the standard for writing python code:
# zen of python is a collection of 19 software principles that influence the design of python programming language 