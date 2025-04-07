def check_number(num):
  """
  Checks if a number is positive, negative, or zero and prints a corresponding message.

  Args:
    num: An integer or float.
  """
  if num > 0:
    print(f"{num} is a positive number.")
  elif num < 0:
    print(f"{num} is a negative number.")
  else:
    print(f"{num} is zero.")

# Example usage:
check_number(10)
check_number(-5)
check_number(0)
