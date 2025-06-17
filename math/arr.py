# Python program to demonstrate basic array operations using lists

# Creating an array (list) of integers
numbers = [10, 20, 30, 40, 50]

# Printing the array
print("Original array:", numbers)

# Accessing elements
print("First element:", numbers[0])         # 10
print("Last element:", numbers[-1])         # 50

# Modifying an element
numbers[2] = 35
print("After modifying 3rd element:", numbers)

# Adding elements
numbers.append(60)
print("After appending 60:", numbers)

# Removing elements
numbers.remove(20)
print("After removing 20:", numbers)

# Slicing the array
print("Elements from index 1 to 3:", numbers[1:4])

# Finding the length of the array
print("Length of array:", len(numbers))