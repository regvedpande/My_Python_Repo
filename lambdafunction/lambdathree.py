# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use a lambda function to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Print the result
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
