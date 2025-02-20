import random

# Function to generate a random greeting
def random_greeting():
    greetings = ["Hello!", "Hi there!", "Greetings!", "Hey!", "Howdy!"]
    return random.choice(greetings)

# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    if length <= 0 or width <= 0:
        return "Invalid dimensions. Length and width must be positive."
    else:
        return length * width

# Function to check if a number is even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Main part of the script
greeting = random_greeting()
print(greeting)

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = rectangle_area(length, width)
print(f"The area of the rectangle is: {area}")

num = int(input("Enter a number to check if it's even or odd: "))
result = even_or_odd(num)
print(f"The number {num} is {result}.")


# A simple loop to print numbers from 1 to 5
print("\nNumbers from 1 to 5:")
for i in range(1, 6):
    print(i)


# Demonstrating a list and some list operations
my_list = [10, 20, 30, 40, 50]
print("\nMy list:", my_list)
print("First element:", my_list[0])
my_list.append(60)
print("List after appending 60:", my_list)
print("Length of the list:", len(my_list))

# A dictionary example
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("\nMy dictionary:", my_dict)
print("Name:", my_dict["name"])

