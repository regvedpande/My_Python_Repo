import random

def random_conditional_message():
  """Generates a random message based on a randomly chosen number."""

  random_number = random.randint(1, 10)

  if random_number < 4:
    message = "It's a low number! Things might be slow today."
  elif 4 <= random_number < 8:
    message = "A moderate number. The day should be average."
  else:
    message = "High number! Expect a busy day."

  print(f"The random number is: {random_number}")
  print(message)

random_conditional_message()
