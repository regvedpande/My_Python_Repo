# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use a lambda function to filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Print the result
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
