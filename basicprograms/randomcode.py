import random

def generate_random_password(length=12):
  """Generates a random password with specified length."""
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':\",./<>?"
  password = "".join(random.choice(characters) for i in range(length))
  return password

if __name__ == "__main__":
  password = generate_random_password()
  print("Generated Password:", password)

  password_20 = generate_random_password(20)
  print("Generated 20 length Password:", password_20)
