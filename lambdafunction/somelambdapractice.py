# Define a lambda function to add two numbers
add = lambda x, y: x + y
print("Addition using lambda:", add(5, 3))

# Define a lambda function to find the square of a number
square = lambda x: x ** 2
print("Square using lambda:", square(4))

# Define a lambda function to check if a number is even
is_even = lambda x: x % 2 == 0
print("Is 4 even using lambda?", is_even(4))
print("Is 5 even using lambda?", is_even(5))

# Define a lambda function to reverse a string
reverse_string = lambda s: s[::-1]
print("Reverse of 'hello' using lambda:", reverse_string("hello"))

# Define a lambda function to find the maximum of two numbers
maximum = lambda x, y: x if x > y else y
print("Maximum of 5 and 3 using lambda:", maximum(5, 3))

# Use lambda with map to double each element in a list
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("Doubled numbers using lambda and map:", doubled_numbers)

# Use lambda with filter to find all even numbers in a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using lambda and filter:", even_numbers)

# Use lambda with sorted to sort a list of tuples based on the second element
tuples = [(1, 3), (2, 1), (4, 2)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print("Sorted tuples using lambda:", sorted_tuples)
