def check_number(number):
  """Checks if a number is positive, negative, or zero and prints a message."""
  if number > 0:
    print(f"{number} is a positive number.")
  elif number < 0:
    print(f"{number} is a negative number.")
  else:
    print("The number is zero.")

# Example usage
check_number(10)
check_number(-5)
check_number(0)
