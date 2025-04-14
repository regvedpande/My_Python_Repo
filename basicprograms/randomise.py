import random

# Generate a list of 10 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Calculate the average of the random numbers
average = sum(random_numbers) / len(random_numbers)

random_numbers, average
