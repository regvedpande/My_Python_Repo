# This code demonstrates a simple for loop in Python

# We'll iterate through a list of fruits
fruits = ["apple", "banana", "cherry", "date"]

print("Here are my favorite fruits:")

# The 'for' loop iterates over each item in the 'fruits' list.
# In each iteration, the current item is assigned to the variable 'fruit'.
for fruit in fruits:
    print(fruit)

print("\nThat's all!")

# You can also use a for loop with the range() function
print("\nCounting from 0 to 4:")
for i in range(5): # range(5) generates numbers 0, 1, 2, 3, 4
    print(i)

print("\nCounting with a start, stop, and step:")
for j in range(1, 10, 2): # range(start, stop, step) - from 1 up to (but not including) 10, stepping by 2
    print(j)

# This code demonstrates a simple while loop in Python

print("\nDemonstrating a while loop:")
count = 0
while count < 3: # The loop continues as long as 'count' is less than 3
    print(f"Count is: {count}")
    count += 1 # Increment 'count' by 1 in each iteration

print("While loop finished.")
