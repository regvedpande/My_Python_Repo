# This is a basic Python program that demonstrates a few fundamental concepts.

# Variables: Used to store data.
name = "Alice"  # String variable
age = 30      # Integer variable
height = 5.7   # Float variable (decimal number)
is_student = False # Boolean variable (True or False)

# Printing: Used to display output.
print("Hello,", name)
print("You are", age, "years old.")
print("Your height is", height, "meters.")
print("Are you a student?", is_student)

# Conditional statement (if-else): Executes different blocks of code based on a condition.
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Loop (for loop): Executes a block of code repeatedly for a sequence of items.
print("Counting from 1 to 5:")
for i in range(1, 6):  # range(start, end) generates numbers from start up to (but not including) end
    print(i)

# List: An ordered collection of items.
fruits = ["apple", "banana", "cherry"]
print("My favorite fruits are:", fruits)

# Accessing elements in a list (using index, starting from 0).
print("The first fruit is:", fruits[0])

# Function: A reusable block of code that performs a specific task.
def greet(person_name):
    """This function greets the person passed as a parameter."""
    print("Hello,", person_name + "!")

# Calling the function.
greet("Bob")
