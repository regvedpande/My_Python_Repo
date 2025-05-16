# --- Simple if statement ---
temperature = 25

if temperature > 20:
  print("It's a warm day.")

# --- if-else statement ---
age = 17

if age >= 18:
  print("You are an adult.")
else:
  print("You are a minor.")

# --- if-elif-else statement ---
score = 85

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
else:
  print("Grade: Below C")

# --- Using logical operators in conditionals ---
is_sunny = True
is_weekend = False

if is_sunny and is_weekend:
  print("Great day for a picnic!")
elif is_sunny and not is_weekend:
  print("It's sunny, but not the weekend.")
elif not is_sunny and is_weekend:
  print("It's the weekend, but not sunny.")
else:
  print("Not sunny and not the weekend.")

# --- Checking for membership ---
fruit = "banana"
fruits = ["apple", "banana", "cherry"]

if fruit in fruits:
  print(f"Yes, {fruit} is in the list of fruits.")
else:
  print(f"No, {fruit} is not in the list of fruits.")

# --- Checking if something is NOT None ---
user_name = "Alice" # Could be None

if user_name is not None:
  print(f"Welcome, {user_name}!")
else:
  print("Please log in.")
