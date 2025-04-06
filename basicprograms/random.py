import random

def random_examples():
  """Demonstrates various uses of the random module."""

  # Generate a random integer within a range
  random_int = random.randint(1, 10)  # Inclusive range [1, 10]
  print(f"Random integer between 1 and 10: {random_int}")

  # Generate a random float between 0 and 1
  random_float = random.random()
  print(f"Random float between 0 and 1: {random_float}")

  # Generate a random float within a specific range
  random_uniform = random.uniform(5, 10) #random float between 5 and 10
  print(f"Random float between 5 and 10 : {random_uniform}")

  # Choose a random element from a list
  my_list = ["apple", "banana", "cherry", "date"]
  random_element = random.choice(my_list)
  print(f"Random element from the list: {random_element}")

  # Shuffle a list in place
  random.shuffle(my_list)
  print(f"Shuffled list: {my_list}")

  # Sample a list without replacement (k unique elements)
  sample_list = random.sample(my_list, 2) #sample 2 unique elements
  print(f"Sampled list: {sample_list}")

  # Generate a random number with Gaussian distribution
  random_gauss = random.gauss(0, 1) # mean 0, standard deviation 1.
  print(f"Random number with Gaussian distribution: {random_gauss}")

  # generate a random number with exponential distribution
  random_expovariate = random.expovariate(1/5) #lambda = 1/5
  print(f"Random number with exponential distribution: {random_expovariate}")


if __name__ == "__main__":
  random_examples()

