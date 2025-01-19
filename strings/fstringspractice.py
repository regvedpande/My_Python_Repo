# F-string examples
name = "Alice"
age = 25
height = 1.75
is_student = True

# Basic f-string usage
print(f"Name: {name}")

# F-string with numbers
print(f"Age: {age}")
print(f"Height: {height:.2f} meters")  # Format with 2 decimal places

# F-string with expressions
print(f"Will be {age + 5} years old in 5 years")

# F-string with boolean
print(f"Student status: {is_student}")

# F-string with string methods
print(f"Name in uppercase: {name.upper()}")

# F-string with calculations
price = 49.99
quantity = 3
print(f"Total cost: ${price * quantity:.2f}")