# Define a list of strings
strings = ["apple", "banana", "cherry", "date"]

# Use a lambda function to filter strings that start with 'a'
a_strings = list(filter(lambda x: x.startswith('a'), strings))

# Print the result
print(a_strings)  # Output: ['apple']
